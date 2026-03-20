#!/usr/bin/env python3
"""
Pipeline 1: Anchor Crafting (Sprint 1)

Interactive pipeline: Opus generates anchor examples from source material,
Bert reviews and approves. ~100 examples, ~500 Opus calls.

This is the ONE pipeline that stays interactive — all others are batch.

Usage:
    python 01_anchor_craft.py                    # Interactive mode
    python 01_anchor_craft.py --code A7.1        # Generate for specific code
    python 01_anchor_craft.py --group A7         # Generate for code group
    python 01_anchor_craft.py --track logic_critical_thinking  # Whole track
    python 01_anchor_craft.py --list             # List codes needing anchors
"""

import argparse
import json
import sys
from pathlib import Path

from config import CORPUS_OUTPUT_DIR
from llm_client import LLMClient
from prompts.anchor_craft import SYSTEM_PROMPT, anchor_from_source, anchor_revision
from schema import CorpusRecord, SourceType, write_corpus, read_corpus
from taxonomy import TAXONOMY, get_codes_by_group, get_codes_by_track, get_label

ANCHOR_FILE = CORPUS_OUTPUT_DIR / "anchors.jsonl"


def load_existing_anchors() -> dict[str, CorpusRecord]:
    """Load existing anchor records, keyed by taxonomy_code."""
    if not ANCHOR_FILE.exists():
        return {}
    records = read_corpus(ANCHOR_FILE)
    return {r.taxonomy_code: r for r in records}


def save_anchor(record: CorpusRecord, existing: dict[str, CorpusRecord]) -> None:
    """Save or update an anchor record."""
    existing[record.taxonomy_code] = record
    write_corpus(list(existing.values()), ANCHOR_FILE)


def codes_needing_anchors(existing: dict[str, CorpusRecord]) -> list[str]:
    """Return taxonomy codes that don't yet have an anchor."""
    return [code for code in TAXONOMY if code not in existing]


def get_source_passage(code: str) -> str:
    """Load relevant source material for a taxonomy code."""
    from source_loader import get_source_passage as _load
    return _load(code)


def interactive_craft(client: LLMClient, code: str, existing: dict) -> None:
    """Interactive loop: generate, review, revise, approve."""
    entry = TAXONOMY[code]

    print(f"\n{'='*60}")
    print(f"Crafting anchor for: {code} — {entry['label']}")
    print(f"Type: {entry['pattern_type']} | Track: {entry['track']}")
    print(f"{'='*60}")

    # Get source material
    source = get_source_passage(code)
    print(f"\nSource material:\n{source}")

    # Choose difficulty tier
    tier = input("\nDifficulty tier [drill/what_if/puzzle] (default: drill): ").strip()
    if tier not in ("drill", "what_if", "puzzle"):
        tier = "drill"

    # Generate with Opus
    print("\nGenerating with Opus... ", end="", flush=True)
    prompt = anchor_from_source(
        taxonomy_code=code,
        taxonomy_label=entry["label"],
        pattern_type=entry["pattern_type"],
        track=entry["track"],
        description=entry["description"],
        source_passage=source,
        difficulty_tier=tier,
    )

    response = client.complete(
        messages=[{"role": "user", "content": prompt}],
        task="anchor",
        system=SYSTEM_PROMPT,
        temperature=0.7,
        max_tokens=4096,
    )
    print(f"done ({response.latency_ms:.0f}ms, {response.output_tokens} tokens)")

    # Parse and display
    try:
        record_data = json.loads(response.content)
        record = CorpusRecord.model_validate(record_data)
        print(f"\n--- Generated Record ---")
        print(json.dumps(record_data, indent=2))
    except (json.JSONDecodeError, Exception) as e:
        print(f"\nError parsing response: {e}")
        print(f"Raw response:\n{response.content[:500]}")
        return

    # Review loop
    while True:
        action = input(
            "\n[a]pprove / [r]evise / [s]kip / [q]uit? "
        ).strip().lower()

        if action == "a":
            save_anchor(record, existing)
            print(f"Saved anchor for {code}.")
            break
        elif action == "r":
            feedback = input("Feedback for revision: ").strip()
            if not feedback:
                continue

            print("Revising with Opus... ", end="", flush=True)
            rev_prompt = anchor_revision(
                original_json=json.dumps(record_data, indent=2),
                feedback=feedback,
            )
            rev_response = client.complete(
                messages=[{"role": "user", "content": rev_prompt}],
                task="anchor",
                system=SYSTEM_PROMPT,
                temperature=0.5,
                max_tokens=4096,
            )
            print(f"done ({rev_response.latency_ms:.0f}ms)")

            try:
                record_data = json.loads(rev_response.content)
                record = CorpusRecord.model_validate(record_data)
                print(json.dumps(record_data, indent=2))
            except (json.JSONDecodeError, Exception) as e:
                print(f"Error parsing revision: {e}")
                print(f"Raw:\n{rev_response.content[:500]}")

        elif action == "s":
            print(f"Skipped {code}.")
            break
        elif action == "q":
            sys.exit(0)


def list_status(existing: dict) -> None:
    """Print status of all taxonomy codes."""
    total = len(TAXONOMY)
    done = len(existing)
    remaining = codes_needing_anchors(existing)

    print(f"\nAnchor Status: {done}/{total} complete\n")

    # Group by track
    tracks: dict[str, list] = {}
    for code in TAXONOMY:
        track = TAXONOMY[code]["track"]
        tracks.setdefault(track, [])
        status = "✓" if code in existing else "·"
        tracks[track].append(f"  {status} {code}: {TAXONOMY[code]['label']}")

    for track, lines in tracks.items():
        done_in_track = sum(1 for l in lines if l.strip().startswith("✓"))
        total_in_track = len(lines)
        print(f"\n{track} ({done_in_track}/{total_in_track}):")
        for line in lines:
            print(line)


def main() -> None:
    parser = argparse.ArgumentParser(description="Anchor crafting pipeline")
    parser.add_argument("--code", help="Generate for a specific taxonomy code")
    parser.add_argument("--group", help="Generate for a code group (e.g. A7)")
    parser.add_argument("--track", help="Generate for an entire track")
    parser.add_argument("--list", action="store_true", help="List anchor status")
    args = parser.parse_args()

    existing = load_existing_anchors()

    if args.list:
        list_status(existing)
        return

    client = LLMClient()

    if args.code:
        if args.code not in TAXONOMY:
            print(f"Unknown code: {args.code}")
            sys.exit(1)
        interactive_craft(client, args.code, existing)

    elif args.group:
        codes = get_codes_by_group(args.group)
        remaining = [c for c in codes if c not in existing]
        print(f"Group {args.group}: {len(remaining)} codes need anchors")
        for code in remaining:
            interactive_craft(client, code, existing)

    elif args.track:
        codes = get_codes_by_track(args.track)
        remaining = [c for c in codes if c not in existing]
        print(f"Track {args.track}: {len(remaining)} codes need anchors")
        for code in remaining:
            interactive_craft(client, code, existing)

    else:
        # Interactive: pick next code needing an anchor
        remaining = codes_needing_anchors(existing)
        if not remaining:
            print("All taxonomy codes have anchors!")
            return
        print(f"\n{len(remaining)} codes need anchors. Starting with first...")
        for code in remaining:
            interactive_craft(client, code, existing)


if __name__ == "__main__":
    main()
