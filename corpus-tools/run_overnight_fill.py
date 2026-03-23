#!/usr/bin/env python3
"""
Overnight bulk generation: fill thin codes + top-up existing ones.

Batch 1: Thin A-codes (A2-A4, thin fallacies, thin stats) — ~5,000
Batch 2: Thin DT paradoxes (B2-B5 codes with <10 examples) — ~1,400
Batch 3: Top-up biases to 200 each — ~2,400
Batch 4: Top-up game theory to 150 each — ~1,800

Total: ~10,600 via gpt-oss-120b at 8 concurrent.
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

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"
MODEL = "openai/gpt-oss-120b"
MAX_CONCURRENT = 8

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
ANCHORS_FILE = OUTPUT_DIR / "anchors.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

DOMAINS = [
    "medieval trading post", "pirate ship crew", "frontier village",
    "guild workshop", "battlefield hospital", "royal court",
    "merchant caravan", "mining colony", "fishing village",
    "tavern owner", "blacksmith forge", "apothecary shop",
    "ship captain", "castle siege", "tournament",
    "harvest season", "bandit hideout", "monastery",
    "ranger patrol", "marketplace", "school academy",
    "theater troupe", "library archive", "prison yard",
    "explorer expedition",
]

TIERS_W = ["drill", "drill", "drill", "what_if", "what_if", "puzzle"]


def load_anchor(code):
    with open(ANCHORS_FILE) as f:
        for line in f:
            r = json.loads(line)
            if r["taxonomy_code"] == code:
                return json.dumps(r, indent=2)[:2500]
    return ""


def build_prompt(code, entry, domain, tier, record_id, anchor):
    track = entry["track"]
    ptype = entry["pattern_type"]
    label = entry["label"]
    desc = entry["description"]

    return f"""Generate a training example for an educational RPG game.

## Taxonomy
- **Code:** {code}
- **Label:** {label}
- **Pattern type:** {ptype}
- **Track:** {track}
- **Description:** {desc}

## Domain: {domain}
## Difficulty: {tier}

## Quality Reference
{anchor}

Return ONLY valid JSON:
{{
  "id": "{record_id}",
  "taxonomy_code": "{code}",
  "taxonomy_label": "{label}",
  "track": "{track}",
  "pattern_type": "{ptype}",
  "difficulty_tier": "{tier}",
  "scenario": {{"context": "...", "text": "...", "speaker_context": "..."}},
  "structure": {{"pattern_name": "...", "pattern_description": "...", "formal_form": null, "why_wrong": {"'...'" if ptype == 'bad_thinking' else 'null'}, "why_right": {"'...'" if ptype != 'bad_thinking' else 'null'}, "related_patterns": [], "counterpoint": "..."}},
  "assessment": {{"identification_prompt": "...", "rubric": [{{"level": 0, "description": "..."}}, {{"level": 1, "description": "..."}}, {{"level": 2, "description": "..."}}, {{"level": 3, "description": "..."}}, {{"level": 4, "description": "..."}}], "follow_up_if_wrong": "...", "follow_up_if_right": "..."}},
  "game_hooks": {{"npc_personality": "...", "npc_dialogue_seed": "...", "resolution_path": "..."}},
  "source": {{"type": "synthetic_verified", "source_material": "Overnight fill generation from {code} anchor", "original_id": null}}
}}"""


async def generate_batch(client, semaphore, plan, output_file, batch_name):
    """Generate a batch and write incrementally. Returns (valid, failed)."""
    valid = 0
    failed = 0
    start = time.time()

    print(f"\n{'='*60}")
    print(f"Batch: {batch_name} ({len(plan)} records)")
    print(f"{'='*60}", flush=True)

    async def gen_one(item):
        nonlocal valid, failed
        code, domain, tier, record_id = item
        entry = TAXONOMY[code]
        anchor = load_anchor(code)
        prompt = build_prompt(code, entry, domain, tier, record_id, anchor)

        for attempt in range(3):
            try:
                async with semaphore:
                    resp = await client.chat.completions.create(
                        model=MODEL,
                        messages=[
                            {"role": "system", "content": "Generate training examples. Return ONLY valid JSON."},
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
                if all(k in result for k in ["id", "taxonomy_code", "scenario", "structure"]):
                    valid += 1
                    return result
                failed += 1
                return None
            except:
                if attempt == 2:
                    failed += 1
                    return None
                await asyncio.sleep(2 ** (attempt + 1))
        return None

    batch_size = 40
    with open(output_file, "a") as out_f:
        for bs in range(0, len(plan), batch_size):
            batch = plan[bs : bs + batch_size]
            results = await asyncio.gather(*[gen_one(item) for item in batch])
            for r in results:
                if r is not None:
                    out_f.write(json.dumps(r) + "\n")
            out_f.flush()
            elapsed = time.time() - start
            total = valid + failed
            print(f"  {batch_name}: {total}/{len(plan)} ({valid} valid) [{elapsed:.0f}s]", flush=True)

    print(f"  {batch_name} DONE: {valid} valid, {failed} failed ({valid/(valid+failed)*100:.1f}%)", flush=True)
    return valid, failed


async def main():
    client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    grand_valid = 0
    grand_failed = 0
    grand_start = time.time()

    # ── Batch 1: Thin A-codes ────────────────────────────────────────────
    thin_a_codes = [
        "A2.1", "A2.2", "A2.3", "A2.4", "A2.5", "A2.6", "A2.7", "A2.8",
        "A3.1", "A3.2", "A3.3", "A3.4", "A3.5",
        "A4.1", "A4.2", "A4.3",
        "A5.2", "A5.3",
        "A6.1", "A6.2", "A6.6",
        "A7.3", "A7.4", "A7.8", "A7.10", "A7.11", "A7.12", "A7.13",
        "A7.14", "A7.15", "A7.16",
        "A8.1", "A8.2", "A8.3", "A8.4",
        "A9.2", "A9.3",
    ]
    plan1 = []
    for code in thin_a_codes:
        for i in range(100):
            plan1.append((code, random.choice(DOMAINS), random.choice(TIERS_W), f"{code}-ON{i:04d}"))
    random.shuffle(plan1)
    v, f = await generate_batch(client, semaphore, plan1,
                                OUTPUT_DIR / "overnight_thin_A.jsonl", "Thin A-codes")
    grand_valid += v
    grand_failed += f

    # ── Batch 2: Thin DT paradoxes ───────────────────────────────────────
    thin_dt = [
        "B2.3", "B2.4", "B2.5",
        "B3.2", "B3.6", "B3.7",
        "B4.2", "B4.3", "B4.4", "B4.5", "B4.6",
        "B5.3", "B5.4", "B5.6", "B5.7",
    ]
    plan2 = []
    for code in thin_dt:
        for i in range(100):
            plan2.append((code, random.choice(DOMAINS), random.choice(TIERS_W), f"{code}-ON{i:04d}"))
    random.shuffle(plan2)
    v, f = await generate_batch(client, semaphore, plan2,
                                OUTPUT_DIR / "overnight_thin_DT.jsonl", "Thin DT paradoxes")
    grand_valid += v
    grand_failed += f

    # ── Batch 3: Top-up biases to 200 ────────────────────────────────────
    bias_codes = [f"E1.{i}" for i in range(1, 25)]
    plan3 = []
    for code in bias_codes:
        for i in range(100):
            plan3.append((code, random.choice(DOMAINS), random.choice(TIERS_W), f"{code}-TU{i:04d}"))
    random.shuffle(plan3)
    v, f = await generate_batch(client, semaphore, plan3,
                                OUTPUT_DIR / "overnight_topup_biases.jsonl", "Top-up biases")
    grand_valid += v
    grand_failed += f

    # ── Batch 4: Top-up game theory ──────────────────────────────────────
    gt_codes = [
        "B6.1", "B6.2", "B6.3",
        "B7.1", "B7.2", "B7.3", "B7.4",
        "B8.1", "B8.2", "B8.3", "B8.4",
        "B9.1", "B9.2", "B9.3",
        "B10.1", "B10.2", "B10.3", "B10.4",
    ]
    plan4 = []
    for code in gt_codes:
        for i in range(100):
            plan4.append((code, random.choice(DOMAINS), random.choice(TIERS_W), f"{code}-TU{i:04d}"))
    random.shuffle(plan4)
    v, f = await generate_batch(client, semaphore, plan4,
                                OUTPUT_DIR / "overnight_topup_GT.jsonl", "Top-up game theory")
    grand_valid += v
    grand_failed += f

    elapsed = time.time() - grand_start
    total_plan = len(plan1) + len(plan2) + len(plan3) + len(plan4)
    print(f"\n{'='*60}")
    print(f"OVERNIGHT RUN COMPLETE")
    print(f"{'='*60}")
    print(f"Planned: {total_plan}")
    print(f"Valid: {grand_valid}")
    print(f"Failed: {grand_failed}")
    print(f"Success: {grand_valid/(grand_valid+grand_failed)*100:.1f}%")
    print(f"Time: {elapsed:.0f}s ({elapsed/3600:.1f} hours)")


if __name__ == "__main__":
    asyncio.run(main())
