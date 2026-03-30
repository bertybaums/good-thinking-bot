#!/usr/bin/env python3
"""
Convert CorpusRecords from corpus-tools/output/*.jsonl into chat conversation
format for QLoRA SFT training.

Usage:
    python3 train/prepare_data.py                  # Full conversion
    python3 train/prepare_data.py --sample 5       # Print 5 sample conversations
    python3 train/prepare_data.py --stats-only     # Just report stats
"""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORPUS_OUTPUT_DIR = PROJECT_ROOT / "corpus-tools" / "output"
TRAIN_DATA_DIR = PROJECT_ROOT / "train" / "data"

# ─── System prompt ───────────────────────────────────────────────────────────

SYSTEM_PROMPT = (
    "You are an expert tutor in critical thinking, logic, decision theory, "
    "and game theory. When presented with a reasoning scenario, you: "
    "(1) identify the specific reasoning pattern, fallacy, bias, or strategic "
    "concept; (2) name it precisely; (3) explain the mechanism — what makes "
    "this reasoning good, bad, or strategically important; (4) note edge cases "
    "or counterpoints where the pattern might not apply. Be thorough but "
    "concise. Ground explanations in the specific scenario details."
)

# ─── Load taxonomy ───────────────────────────────────────────────────────────


def load_taxonomy() -> dict[str, str]:
    """Load TAXONOMY from taxonomy.py and return {code: label} mapping."""
    # Import directly from corpus-tools
    sys.path.insert(0, str(PROJECT_ROOT / "corpus-tools"))
    from taxonomy import TAXONOMY
    return {code: entry["label"] for code, entry in TAXONOMY.items()}


# ─── Load records ────────────────────────────────────────────────────────────


def load_all_records() -> list[dict]:
    """Load all JSONL files from corpus-tools/output/, excluding benchmarks."""
    records = []
    for jsonl_file in sorted(CORPUS_OUTPUT_DIR.glob("*.jsonl")):
        if "benchmark" in jsonl_file.name:
            continue
        with open(jsonl_file) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    records.append(record)
                except json.JSONDecodeError:
                    continue
    return records


# ─── Convert one record ─────────────────────────────────────────────────────


def record_to_conversation(record: dict, taxonomy: dict[str, str]) -> dict | None:
    """Convert a CorpusRecord dict to a chat conversation dict.

    Returns None if the record should be skipped.
    """
    scenario = record.get("scenario", {})
    text = scenario.get("text")
    if not text or not text.strip():
        return None

    context = scenario.get("context", "")
    assessment = record.get("assessment", {})
    identification_prompt = assessment.get("identification_prompt", "")
    structure = record.get("structure", {})

    # Build user message
    user_parts = []
    if context and context.strip():
        user_parts.append(context.strip())
    user_parts.append(text.strip())
    if identification_prompt and identification_prompt.strip():
        user_parts.append(identification_prompt.strip())
    user_message = "\n\n".join(user_parts)

    # Build assistant message
    assistant_parts = []

    pattern_name = structure.get("pattern_name", "")
    if pattern_name:
        assistant_parts.append(f"**Pattern:** {pattern_name}")

    pattern_description = structure.get("pattern_description", "")
    if pattern_description:
        assistant_parts.append(f"**Analysis:** {pattern_description}")

    why_wrong = structure.get("why_wrong")
    if why_wrong:
        assistant_parts.append(f"**Why this is problematic:** {why_wrong}")

    why_right = structure.get("why_right")
    if why_right:
        assistant_parts.append(f"**Why this works:** {why_right}")

    formal_form = structure.get("formal_form")
    if formal_form:
        assistant_parts.append(f"**Formal structure:** {formal_form}")

    related_patterns = structure.get("related_patterns", [])
    if related_patterns:
        labels = []
        for code in related_patterns:
            label = taxonomy.get(code)
            if label:
                labels.append(label)
            else:
                labels.append(code)
        assistant_parts.append(f"**Related concepts:** {', '.join(labels)}")

    counterpoint = structure.get("counterpoint")
    if counterpoint:
        assistant_parts.append(f"**Edge case:** {counterpoint}")

    assistant_message = "\n\n".join(assistant_parts)

    if not assistant_message.strip():
        return None

    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": assistant_message},
        ]
    }


# ─── Main ────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Convert corpus records to chat format for QLoRA SFT."
    )
    parser.add_argument(
        "--sample", type=int, default=0,
        help="Print N sample conversations and exit."
    )
    parser.add_argument(
        "--stats-only", action="store_true",
        help="Report stats without writing output files."
    )
    args = parser.parse_args()

    # Load taxonomy and records
    print("Loading taxonomy...")
    taxonomy = load_taxonomy()
    print(f"  {len(taxonomy)} taxonomy codes loaded.")

    print("Loading corpus records...")
    records = load_all_records()
    print(f"  {len(records)} raw records loaded.")

    # Convert
    print("Converting to chat format...")
    conversations = []
    skipped = 0
    track_counts = Counter()

    for record in records:
        conv = record_to_conversation(record, taxonomy)
        if conv is None:
            skipped += 1
            continue
        conversations.append(conv)
        track = record.get("track", "unknown")
        track_counts[track] += 1

    print(f"  {len(conversations)} conversations produced, {skipped} records skipped.")

    # Shuffle
    random.seed(42)
    random.shuffle(conversations)

    # Split
    split_idx = int(len(conversations) * 0.95)
    train_set = conversations[:split_idx]
    val_set = conversations[split_idx:]

    # Stats
    assistant_lengths = [
        len(conv["messages"][2]["content"]) for conv in conversations
    ]
    avg_len = sum(assistant_lengths) / len(assistant_lengths) if assistant_lengths else 0

    print("\n" + "=" * 60)
    print("STATS")
    print("=" * 60)
    print(f"Total conversations: {len(conversations)}")
    print(f"  Train: {len(train_set)}")
    print(f"  Val:   {len(val_set)}")
    print(f"  Skipped: {skipped}")
    print(f"\nRecords per track:")
    for track, count in sorted(track_counts.items(), key=lambda x: -x[1]):
        print(f"  {track:30s} {count:>6,}")
    print(f"\nAvg assistant response length: {avg_len:,.0f} chars")
    print(f"Min: {min(assistant_lengths):,} chars")
    print(f"Max: {max(assistant_lengths):,} chars")
    print("=" * 60)

    # Sample mode
    if args.sample > 0:
        print(f"\n{'=' * 60}")
        print(f"SAMPLE CONVERSATIONS ({args.sample})")
        print(f"{'=' * 60}")
        for i, conv in enumerate(conversations[:args.sample]):
            print(f"\n--- Conversation {i+1} ---")
            for msg in conv["messages"]:
                role = msg["role"].upper()
                content = msg["content"]
                if role == "SYSTEM":
                    print(f"[SYSTEM] {content[:80]}...")
                else:
                    print(f"[{role}]")
                    print(content)
                print()
        return

    if args.stats_only:
        return

    # Write output
    TRAIN_DATA_DIR.mkdir(parents=True, exist_ok=True)
    train_path = TRAIN_DATA_DIR / "train.jsonl"
    val_path = TRAIN_DATA_DIR / "val.jsonl"

    with open(train_path, "w") as f:
        for conv in train_set:
            f.write(json.dumps(conv, ensure_ascii=False) + "\n")
    print(f"\nWrote {len(train_set):,} train examples to {train_path}")

    with open(val_path, "w") as f:
        for conv in val_set:
            f.write(json.dumps(conv, ensure_ascii=False) + "\n")
    print(f"Wrote {len(val_set):,} val examples to {val_path}")


if __name__ == "__main__":
    main()
