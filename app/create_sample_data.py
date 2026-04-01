#!/usr/bin/env python3
"""
Create a stratified sample of the Good Thinking Corpus for the Gradio app.

Strategy: Up to 3 records per taxonomy code, stratified across difficulty tiers.
This yields ~546 records from the full 27K corpus, keeping the app lightweight
while covering all 182 taxonomy codes.

Run once from the project root:
    python app/create_sample_data.py
"""

import json
import random
import sys
from collections import defaultdict
from pathlib import Path

CORPUS_DIR = Path(__file__).resolve().parent.parent / "corpus-tools" / "output"
RELEASE_FILE = CORPUS_DIR / "release" / "good-thinking-corpus-v1.0.jsonl"
ANCHORS_FILE = CORPUS_DIR / "anchors.jsonl"
ANCHORS_PHIL4040_FILE = CORPUS_DIR / "anchors_phil4040.jsonl"
OUTPUT_FILE = Path(__file__).resolve().parent / "data" / "scenarios.jsonl"

RECORDS_PER_CODE = 3
SEED = 42


def load_jsonl(path: Path) -> list[dict]:
    """Load all records from a JSONL file."""
    records = []
    if not path.exists():
        print(f"  Warning: {path} not found, skipping")
        return records
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return records


def stratified_sample(records: list[dict], n_per_code: int) -> list[dict]:
    """Sample up to n_per_code records per taxonomy code, preferring tier diversity."""
    by_code = defaultdict(lambda: defaultdict(list))
    for r in records:
        code = r.get("taxonomy_code", "unknown")
        tier = r.get("difficulty_tier", "drill")
        by_code[code][tier].append(r)

    sampled = []
    tiers = ["drill", "what_if", "puzzle"]

    for code in sorted(by_code.keys()):
        tier_buckets = by_code[code]
        selected = []

        # First pass: one from each tier
        for tier in tiers:
            if tier in tier_buckets and tier_buckets[tier] and len(selected) < n_per_code:
                selected.append(random.choice(tier_buckets[tier]))

        # Second pass: fill remaining slots from any tier
        if len(selected) < n_per_code:
            remaining = []
            for tier in tiers:
                for r in tier_buckets.get(tier, []):
                    if r not in selected:
                        remaining.append(r)
            random.shuffle(remaining)
            selected.extend(remaining[: n_per_code - len(selected)])

        sampled.extend(selected)

    return sampled


def main():
    random.seed(SEED)

    # Always include all anchors (the hand-crafted gold-standard records)
    print("Loading anchors...")
    anchors = load_jsonl(ANCHORS_FILE) + load_jsonl(ANCHORS_PHIL4040_FILE)
    anchor_ids = {a["id"] for a in anchors}
    print(f"  {len(anchors)} anchor records")

    # Load the full release corpus for supplementary sampling
    print("Loading release corpus...")
    corpus = load_jsonl(RELEASE_FILE)
    non_anchors = [r for r in corpus if r["id"] not in anchor_ids]
    print(f"  {len(corpus)} total, {len(non_anchors)} non-anchor records")

    # Group anchors by code to see which codes need more records
    anchor_by_code = defaultdict(list)
    for a in anchors:
        anchor_by_code[a["taxonomy_code"]].append(a)

    # For codes with fewer than RECORDS_PER_CODE anchors, sample from corpus
    print("Stratified sampling from corpus...")
    supplementary = []
    non_anchor_by_code = defaultdict(lambda: defaultdict(list))
    for r in non_anchors:
        code = r.get("taxonomy_code", "unknown")
        tier = r.get("difficulty_tier", "drill")
        non_anchor_by_code[code][tier].append(r)

    tiers = ["drill", "what_if", "puzzle"]
    for code in sorted(non_anchor_by_code.keys()):
        needed = RECORDS_PER_CODE - len(anchor_by_code.get(code, []))
        if needed <= 0:
            continue
        tier_buckets = non_anchor_by_code[code]
        selected = []
        # Prefer tier diversity
        for tier in tiers:
            if tier in tier_buckets and tier_buckets[tier] and len(selected) < needed:
                selected.append(random.choice(tier_buckets[tier]))
        if len(selected) < needed:
            remaining = []
            for tier in tiers:
                for r in tier_buckets.get(tier, []):
                    if r not in selected:
                        remaining.append(r)
            random.shuffle(remaining)
            selected.extend(remaining[: needed - len(selected)])
        supplementary.extend(selected)

    all_records = anchors + supplementary
    print(f"  {len(supplementary)} supplementary records added")

    # Deduplicate by ID
    seen = set()
    unique = []
    for r in all_records:
        if r["id"] not in seen:
            seen.add(r["id"])
            unique.append(r)

    # Sort by taxonomy code then ID
    unique.sort(key=lambda r: (r.get("taxonomy_code", ""), r.get("id", "")))

    # Count stats
    codes = set(r["taxonomy_code"] for r in unique)
    tracks = defaultdict(int)
    for r in unique:
        tracks[r.get("track", "unknown")] += 1

    print(f"\nFinal sample: {len(unique)} records across {len(codes)} taxonomy codes")
    print("By track:")
    for track in sorted(tracks.keys()):
        print(f"  {track}: {tracks[track]}")

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        for r in unique:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"\nWritten to {OUTPUT_FILE}")
    print(f"File size: {OUTPUT_FILE.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
