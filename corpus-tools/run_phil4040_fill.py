#!/usr/bin/env python3
"""
PHIL 4040 bulk generation: fill 15 new taxonomy codes from gap analysis.

Codes (150 each = 2,250 total):
  C1.3  Pareto efficiency
  B6.4  Zero-sum games          B6.5  Mixed strategy NE
  B6.6  Dominance reasoning     B7.5  Hawk-Dove
  B7.6  Ultimatum/Trust         B7.7  Public Goods
  B8.5  Signaling games         B8.6  Commitment devices
  B10.5 Folk Theorem            B13.1 Level-k thinking
  B13.2 Social preference       B15.1 Condorcet's Paradox
  B15.2 Arrow's Impossibility   B15.3 Voting systems

Uses MindRouter gpt-oss-120b at 8 concurrent.

Usage:
    python3 run_phil4040_fill.py                    # Generate all 2,250
    python3 run_phil4040_fill.py --codes B6.4 B6.5  # Generate specific codes
    python3 run_phil4040_fill.py --count 50         # Override per-code count
    python3 run_phil4040_fill.py --dry-run          # Show plan without generating
"""

import argparse
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
OUTPUT_FILE = OUTPUT_DIR / "phil4040_synthetic.jsonl"
ANCHORS_FILE = OUTPUT_DIR / "anchors_phil4040.jsonl"
FALLBACK_ANCHORS = OUTPUT_DIR / "anchors.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

# ── Target codes ─────────────────────────────────────────────────────────────

PHIL4040_CODES = [
    "C1.3",   # Pareto efficiency
    "B6.4",   # Zero-sum games
    "B6.5",   # Mixed strategy NE
    "B6.6",   # Dominance reasoning
    "B7.5",   # Hawk-Dove
    "B7.6",   # Ultimatum/Trust
    "B7.7",   # Public Goods
    "B8.5",   # Signaling games
    "B8.6",   # Commitment devices
    "B10.5",  # Folk Theorem
    "B13.1",  # Level-k thinking
    "B13.2",  # Social preference models
    "B15.1",  # Condorcet's Paradox
    "B15.2",  # Arrow's Impossibility Theorem
    "B15.3",  # Voting systems
]

# ── Domains (20 standard) ───────────────────────────────────────────────────

DOMAINS = [
    "healthcare", "education", "workplace", "sports", "cooking",
    "travel", "technology", "politics", "environment", "finance",
    "relationships", "parenting", "music", "gaming", "housing",
    "agriculture", "legal", "military", "science", "retail",
]

# ── Difficulty distribution: 60% drill, 30% what_if, 10% puzzle ─────────────

def make_tier_pool(count):
    """Build a tier list with 60/30/10 distribution for the given count."""
    n_drill = int(count * 0.60)
    n_whatif = int(count * 0.30)
    n_puzzle = count - n_drill - n_whatif  # remainder gets puzzle
    return ["drill"] * n_drill + ["what_if"] * n_whatif + ["puzzle"] * n_puzzle


# ── Anchor loading ───────────────────────────────────────────────────────────

def load_anchor(code):
    """Load an anchor example for few-shot reference. Try phil4040 anchors first."""
    for anchor_path in [ANCHORS_FILE, FALLBACK_ANCHORS]:
        if not anchor_path.exists():
            continue
        # Exact match first
        with open(anchor_path) as f:
            for line in f:
                r = json.loads(line)
                if r.get("taxonomy_code") == code:
                    return json.dumps(r, indent=2)[:2500]
        # Prefix match (same group)
        prefix = code.split(".")[0]
        with open(anchor_path) as f:
            for line in f:
                r = json.loads(line)
                if r.get("taxonomy_code", "").startswith(prefix):
                    return json.dumps(r, indent=2)[:2500]
    return "(No anchor examples available)"


# ── Prompt builder ───────────────────────────────────────────────────────────

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
  "source": {{"type": "synthetic_verified", "source_material": "PHIL 4040 fill generation from {code} anchor", "original_id": null}}
}}"""


# ── Resume support ───────────────────────────────────────────────────────────

def load_existing_ids(output_file):
    """Load IDs already in the output file for resume support."""
    existing = set()
    if output_file.exists():
        with open(output_file) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                    existing.add(r.get("id", ""))
                except json.JSONDecodeError:
                    continue
    return existing


# ── Schema validation ────────────────────────────────────────────────────────

REQUIRED_KEYS = {"id", "taxonomy_code", "scenario", "structure", "assessment", "game_hooks"}
SCENARIO_KEYS = {"context", "text", "speaker_context"}
STRUCTURE_KEYS = {"pattern_name", "pattern_description"}

def validate_record(record):
    """Basic schema validation. Returns (is_valid, reason)."""
    if not isinstance(record, dict):
        return False, "not a dict"
    missing = REQUIRED_KEYS - set(record.keys())
    if missing:
        return False, f"missing top-level keys: {missing}"
    scenario = record.get("scenario", {})
    if not isinstance(scenario, dict):
        return False, "scenario is not a dict"
    missing_s = SCENARIO_KEYS - set(scenario.keys())
    if missing_s:
        return False, f"missing scenario keys: {missing_s}"
    structure = record.get("structure", {})
    if not isinstance(structure, dict):
        return False, "structure is not a dict"
    missing_st = STRUCTURE_KEYS - set(structure.keys())
    if missing_st:
        return False, f"missing structure keys: {missing_st}"
    return True, "ok"


# ── Batch generation ─────────────────────────────────────────────────────────

async def generate_batch(client, semaphore, plan, output_file):
    """Generate all records. Write incrementally. Returns (valid, failed)."""
    valid = 0
    failed = 0
    start = time.time()

    print(f"\n{'='*60}")
    print(f"PHIL 4040 Fill: {len(plan)} records")
    print(f"Output: {output_file}")
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
                is_valid, reason = validate_record(result)
                if is_valid:
                    valid += 1
                    return result
                failed += 1
                return None
            except Exception:
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
            if total % 50 < batch_size or bs + batch_size >= len(plan):
                print(f"  Progress: {total}/{len(plan)} ({valid} valid, {failed} failed) [{elapsed:.0f}s]", flush=True)

    success_pct = valid / (valid + failed) * 100 if (valid + failed) > 0 else 0
    print(f"\n  DONE: {valid} valid, {failed} failed ({success_pct:.1f}%)", flush=True)
    return valid, failed


# ── Main ─────────────────────────────────────────────────────────────────────

async def main():
    parser = argparse.ArgumentParser(
        description="PHIL 4040 bulk generation: fill 15 new taxonomy codes"
    )
    parser.add_argument(
        "--codes", nargs="+", default=None,
        help="Generate only specific codes (e.g. --codes B6.4 B6.5)"
    )
    parser.add_argument(
        "--count", type=int, default=150,
        help="Records per code (default: 150)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show plan without generating"
    )
    args = parser.parse_args()

    # Determine which codes to generate
    codes = args.codes if args.codes else PHIL4040_CODES
    for c in codes:
        if c not in PHIL4040_CODES:
            print(f"ERROR: {c} is not a PHIL 4040 target code.")
            print(f"Valid codes: {', '.join(PHIL4040_CODES)}")
            sys.exit(1)
        if c not in TAXONOMY:
            print(f"ERROR: {c} not found in taxonomy.")
            sys.exit(1)

    count_per_code = args.count

    # Load existing IDs for resume
    existing_ids = load_existing_ids(OUTPUT_FILE)
    if existing_ids:
        print(f"Resume: found {len(existing_ids)} existing records in {OUTPUT_FILE}")

    # Build plan with 60/30/10 difficulty distribution
    plan = []
    domain_idx = 0
    for code in codes:
        tiers = make_tier_pool(count_per_code)
        random.shuffle(tiers)
        for i, tier in enumerate(tiers):
            record_id = f"{code}-PF{i:04d}"
            if record_id in existing_ids:
                continue
            domain = DOMAINS[domain_idx % len(DOMAINS)]
            domain_idx += 1
            plan.append((code, domain, tier, record_id))
    random.shuffle(plan)

    # Summary
    code_counts = Counter(item[0] for item in plan)
    tier_counts = Counter(item[2] for item in plan)
    total = len(plan)

    print(f"\n{'='*60}")
    print(f"PHIL 4040 FILL PLAN")
    print(f"{'='*60}")
    print(f"Codes: {len(codes)}")
    print(f"Per code: {count_per_code}")
    print(f"Total planned: {total}")
    print(f"Already generated: {len(existing_ids)}")
    print(f"Remaining: {total}")
    print(f"\nDifficulty distribution:")
    print(f"  drill:   {tier_counts.get('drill', 0):>5} ({tier_counts.get('drill', 0)/total*100:.0f}%)" if total else "")
    print(f"  what_if: {tier_counts.get('what_if', 0):>5} ({tier_counts.get('what_if', 0)/total*100:.0f}%)" if total else "")
    print(f"  puzzle:  {tier_counts.get('puzzle', 0):>5} ({tier_counts.get('puzzle', 0)/total*100:.0f}%)" if total else "")
    print(f"\nPer-code breakdown:")
    for code in codes:
        entry = TAXONOMY[code]
        n = code_counts.get(code, 0)
        print(f"  {code:<7} {entry['label']:<45} {n:>4} records")

    if args.dry_run:
        print(f"\n[DRY RUN] Would generate {total} records. Exiting.")
        return

    if total == 0:
        print("\nNothing to generate (all records already exist).")
        return

    # Generate
    client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    grand_start = time.time()

    valid, failed = await generate_batch(client, semaphore, plan, OUTPUT_FILE)

    elapsed = time.time() - grand_start
    print(f"\n{'='*60}")
    print(f"PHIL 4040 FILL COMPLETE")
    print(f"{'='*60}")
    print(f"Planned:  {total}")
    print(f"Valid:    {valid}")
    print(f"Failed:   {failed}")
    if valid + failed > 0:
        print(f"Success:  {valid/(valid+failed)*100:.1f}%")
    print(f"Time:     {elapsed:.0f}s ({elapsed/3600:.1f} hours)")
    print(f"Output:   {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
