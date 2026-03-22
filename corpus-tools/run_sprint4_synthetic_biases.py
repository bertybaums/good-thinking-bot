#!/usr/bin/env python3
"""
Sprint 4: Synthetic Cognitive Biases Generation (E1.1-E1.24)

Generates ~2,400 cognitive bias examples (24 codes x 100 each) across
diverse domains. Uses gpt-oss-120b (8 concurrent) for quality.
"""

import asyncio
import json
import os
import random
import sys
import time
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

import openai

# ── Config ───────────────────────────────────────────────────────────────────

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"
MODEL = "openai/gpt-oss-120b"
MAX_CONCURRENT = 8

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
ANCHORS_FILE = OUTPUT_DIR / "anchors.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

# ── Domains ──────────────────────────────────────────────────────────────────

DOMAINS = [
    "workplace office", "school classroom", "hospital ward", "sports team",
    "political campaign", "courtroom trial", "restaurant kitchen", "startup company",
    "military unit", "research lab", "family dinner", "online forum",
    "neighborhood dispute", "job interview", "dating scene", "road trip",
    "volunteer organization", "financial planning", "parenting decision",
    "creative project", "customer service", "real estate deal",
    "college admissions", "jury deliberation", "emergency response",
]

TIERS = ["drill", "drill", "what_if", "what_if", "puzzle"]

# ── Bias codes ───────────────────────────────────────────────────────────────

BIAS_CODES = [f"E1.{i}" for i in range(1, 25)]

# ── Load anchor for few-shot ─────────────────────────────────────────────────

def load_anchor(code: str) -> str:
    with open(ANCHORS_FILE) as f:
        for line in f:
            rec = json.loads(line)
            if rec["taxonomy_code"] == code:
                return json.dumps(rec, indent=2)[:3000]
    return "(No anchor available)"

# ── Generation prompt ────────────────────────────────────────────────────────

def build_prompt(code: str, entry: dict, domain: str, tier: str, record_id: str, anchor: str) -> str:
    return f"""Generate a cognitive bias training example for an educational RPG game.

## Bias
- **Code:** {code}
- **Label:** {entry['label']}
- **Pattern type:** {entry['pattern_type']}
- **Description:** {entry['description']}

## Domain: {domain}
## Difficulty: {tier} (drill=clear-cut, what_if=subtle/ambiguous, puzzle=deep engagement)

## Requirements
1. Create a scenario where a character exhibits this bias NATURALLY
2. The bias should be subtle enough to be realistic but clear enough to identify
3. Include a concrete behavioral choice that reveals the bias
4. The NPC should NOT name the bias — the player must recognize it
5. For "dual" biases (like placebo effect), show both the value and limitations
6. Make the scenario feel like a real RPG NPC encounter

## Quality Reference
{anchor}

## Output
Return ONLY valid JSON (no markdown):
{{
  "id": "{record_id}",
  "taxonomy_code": "{code}",
  "taxonomy_label": "{entry['label']}",
  "track": "cognitive_biases",
  "pattern_type": "{entry['pattern_type']}",
  "difficulty_tier": "{tier}",
  "scenario": {{"context": "...", "text": "...", "speaker_context": "..."}},
  "structure": {{"pattern_name": "...", "pattern_description": "...", "formal_form": null, "why_wrong": "...", "why_right": null, "related_patterns": [], "counterpoint": "When might this heuristic be useful?"}},
  "assessment": {{"identification_prompt": "...", "rubric": [{{"level": 0, "description": "..."}}, {{"level": 1, "description": "..."}}, {{"level": 2, "description": "..."}}, {{"level": 3, "description": "..."}}, {{"level": 4, "description": "..."}}], "follow_up_if_wrong": "...", "follow_up_if_right": "..."}},
  "game_hooks": {{"npc_personality": "...", "npc_dialogue_seed": "...", "resolution_path": "..."}},
  "source": {{"type": "synthetic_verified", "source_material": "Generated from {code} anchor + bias poster", "original_id": null}}
}}"""

# ── Main pipeline ────────────────────────────────────────────────────────────

async def main():
    client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    # Build plan: 100 per code = 2,400 total
    plan = []
    examples_per_code = 100
    for code in BIAS_CODES:
        entry = TAXONOMY.get(code)
        if not entry:
            continue
        anchor = load_anchor(code)
        for i in range(examples_per_code):
            domain = DOMAINS[i % len(DOMAINS)]
            tier = random.choice(TIERS)
            record_id = f"{code}-S4{i:04d}"
            plan.append({
                "code": code,
                "entry": entry,
                "domain": domain,
                "tier": tier,
                "record_id": record_id,
                "anchor": anchor,
            })

    random.shuffle(plan)
    print(f"Sprint 4: Synthetic Cognitive Biases Generation")
    print(f"Model: {MODEL} | Concurrency: {MAX_CONCURRENT}")
    print(f"Plan: {len(plan)} examples across {len(BIAS_CODES)} codes")

    output_file = OUTPUT_DIR / "synthetic_biases_sprint4.jsonl"
    valid = 0
    failed = 0
    start = time.time()

    async def generate_one(item):
        nonlocal valid, failed
        prompt = build_prompt(
            item["code"], item["entry"], item["domain"],
            item["tier"], item["record_id"], item["anchor"],
        )
        for attempt in range(3):
            try:
                async with semaphore:
                    resp = await client.chat.completions.create(
                        model=MODEL,
                        messages=[
                            {"role": "system", "content": "Generate training examples for an educational game. Return ONLY valid JSON."},
                            {"role": "user", "content": prompt},
                        ],
                        max_tokens=4096,
                        temperature=0.7,
                        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                    )
                content = resp.choices[0].message.content or ""
                if "```" in content:
                    content = content.split("```json")[-1].split("```")[0] if "```json" in content else content.split("```")[1].split("```")[0]
                result = json.loads(content)
                required = ["id", "taxonomy_code", "scenario", "structure", "assessment"]
                if all(k in result for k in required):
                    valid += 1
                    return result
                failed += 1
                return None
            except (json.JSONDecodeError, Exception):
                if attempt == 2:
                    failed += 1
                    return None
                await asyncio.sleep(2 ** (attempt + 1))
        return None

    # Process in batches, write incrementally
    batch_size = 40
    with open(output_file, "w") as out_f:
        for batch_start in range(0, len(plan), batch_size):
            batch = plan[batch_start : batch_start + batch_size]
            results = await asyncio.gather(*[generate_one(item) for item in batch])
            for r in results:
                if r is not None:
                    out_f.write(json.dumps(r) + "\n")
            out_f.flush()
            elapsed = time.time() - start
            total = valid + failed
            print(f"  Progress: {total}/{len(plan)} ({valid} valid, {failed} failed) [{elapsed:.0f}s]", flush=True)

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"SPRINT 4 COMPLETE")
    print(f"{'='*60}")
    print(f"Total: {valid} valid, {failed} failed ({valid/(valid+failed):.1%} success)")
    print(f"Time: {elapsed:.0f}s")
    print(f"Output: {output_file}")

    records = [json.loads(l) for l in open(output_file) if l.strip()]
    code_counts = Counter(r["taxonomy_code"] for r in records)
    tier_counts = Counter(r["difficulty_tier"] for r in records)
    print(f"\nPer-code counts:")
    for code in sorted(code_counts):
        print(f"  {code}: {code_counts[code]}")
    print(f"\nTier distribution: {dict(tier_counts)}")


if __name__ == "__main__":
    asyncio.run(main())
