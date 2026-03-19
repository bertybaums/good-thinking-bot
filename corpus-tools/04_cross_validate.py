#!/usr/bin/env python3
"""
Pipeline 4: Cross-Validation (QA, runs after each sprint)

Strips the taxonomy code from each example, sends the scenario to MindRouter,
asks it to classify, and compares to the intended code. Flags disagreements
for expert review.

Usage:
    python 04_cross_validate.py --input output/adapted_jin.jsonl
    python 04_cross_validate.py --all  # Validate all corpus files
    python 04_cross_validate.py --report  # Show agreement report
"""

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

from config import CORPUS_OUTPUT_DIR, CROSS_VAL_AGREEMENT_THRESHOLD, CROSS_VAL_BATCH_SIZE
from llm_client import AsyncLLMClient
from prompts.cross_validate import SYSTEM_PROMPT, classify_scenario
from schema import CorpusRecord, read_corpus
from taxonomy import TAXONOMY

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def build_taxonomy_options(track: str | None = None) -> str:
    """Build a compact taxonomy reference for the classifier prompt."""
    lines = []
    for code, entry in sorted(TAXONOMY.items()):
        if track and entry["track"] != track:
            continue
        lines.append(f"- {code}: {entry['label']} ({entry['pattern_type']}) — {entry['description'][:80]}")
    return "\n".join(lines)


async def cross_validate_file(
    client: AsyncLLMClient,
    corpus_path: Path,
) -> dict:
    """
    Cross-validate a corpus file. Returns statistics and flagged records.
    """
    records = read_corpus(corpus_path)
    logger.info(f"Cross-validating {len(records)} records from {corpus_path.name}")

    # Build taxonomy options scoped to relevant tracks
    tracks = {TAXONOMY[r.taxonomy_code]["track"] for r in records if r.taxonomy_code in TAXONOMY}
    taxonomy_options = build_taxonomy_options()  # Full taxonomy for best accuracy

    requests = []
    for record in records:
        prompt = classify_scenario(
            scenario_text=record.scenario.text,
            scenario_context=record.scenario.context,
            taxonomy_options=taxonomy_options,
        )
        requests.append({
            "messages": [{"role": "user", "content": prompt}],
            "task": "cross_val",
            "system": SYSTEM_PROMPT,
            "temperature": 0.2,
            "max_tokens": 512,
            "json_mode": True,
        })

    # Process in batches
    all_results = []
    for batch_start in range(0, len(requests), CROSS_VAL_BATCH_SIZE):
        batch = requests[batch_start : batch_start + CROSS_VAL_BATCH_SIZE]
        logger.info(f"  Batch {batch_start // CROSS_VAL_BATCH_SIZE + 1}...")
        results = await client.batch_complete(batch)
        all_results.extend(results)

    # Analyze results
    agreements = 0
    disagreements = 0
    errors = 0
    flagged: list[dict] = []

    for i, result in enumerate(all_results):
        record = records[i]
        if isinstance(result, Exception):
            errors += 1
            continue

        try:
            prediction = json.loads(result.content)
            predicted_code = prediction.get("predicted_code", "")

            if predicted_code == record.taxonomy_code:
                agreements += 1
            else:
                # Check if it's a "close" disagreement (same group)
                intended_group = record.taxonomy_code.split(".")[0]
                predicted_group = predicted_code.split(".")[0] if predicted_code else ""

                disagreements += 1
                flagged.append({
                    "record_id": record.id,
                    "intended_code": record.taxonomy_code,
                    "intended_label": record.taxonomy_label,
                    "predicted_code": predicted_code,
                    "predicted_label": prediction.get("predicted_label", ""),
                    "confidence": prediction.get("confidence", 0),
                    "reasoning": prediction.get("reasoning", ""),
                    "close_match": intended_group == predicted_group,
                    "scenario_text": record.scenario.text[:200],
                })

        except (json.JSONDecodeError, Exception) as e:
            errors += 1

    total = agreements + disagreements
    agreement_rate = agreements / total if total > 0 else 0

    stats = {
        "file": corpus_path.name,
        "total_records": len(records),
        "classified": total,
        "agreements": agreements,
        "disagreements": disagreements,
        "errors": errors,
        "agreement_rate": agreement_rate,
        "passes_threshold": agreement_rate >= CROSS_VAL_AGREEMENT_THRESHOLD,
        "flagged": flagged,
    }

    return stats


def save_flagged(stats: dict, output_dir: Path) -> None:
    """Save flagged records for expert review."""
    flagged = stats.get("flagged", [])
    if not flagged:
        return

    file_stem = Path(stats["file"]).stem
    output_path = output_dir / f"flagged_{file_stem}.jsonl"

    with open(output_path, "w") as f:
        for item in flagged:
            f.write(json.dumps(item) + "\n")

    logger.info(f"  Saved {len(flagged)} flagged records to {output_path}")


def print_report(all_stats: list[dict]) -> None:
    """Print a summary report across all validated files."""
    print(f"\n{'='*70}")
    print("CROSS-VALIDATION REPORT")
    print(f"{'='*70}")
    print(f"\n{'File':<35} {'Records':>8} {'Agree':>8} {'Rate':>8} {'Pass':>6}")
    print("-" * 70)

    total_records = 0
    total_agree = 0

    for stats in all_stats:
        total_records += stats["classified"]
        total_agree += stats["agreements"]
        status = "YES" if stats["passes_threshold"] else "NO"
        print(
            f"{stats['file']:<35} "
            f"{stats['classified']:>8} "
            f"{stats['agreements']:>8} "
            f"{stats['agreement_rate']:>7.1%} "
            f"{status:>6}"
        )

    overall_rate = total_agree / total_records if total_records > 0 else 0
    print("-" * 70)
    print(f"{'TOTAL':<35} {total_records:>8} {total_agree:>8} {overall_rate:>7.1%}")

    # Most common disagreement patterns
    all_flagged = []
    for stats in all_stats:
        all_flagged.extend(stats.get("flagged", []))

    if all_flagged:
        print(f"\nTop confusion pairs (n={len(all_flagged)}):")
        pairs: dict[str, int] = {}
        for f in all_flagged:
            pair = f"{f['intended_code']} -> {f['predicted_code']}"
            pairs[pair] = pairs.get(pair, 0) + 1
        for pair, count in sorted(pairs.items(), key=lambda x: -x[1])[:10]:
            print(f"  [{count:>3}x] {pair}")


async def run_cross_validation(args: argparse.Namespace) -> None:
    """Main cross-validation pipeline."""
    if args.report:
        # Load all flagged files and generate report
        flagged_files = list(CORPUS_OUTPUT_DIR.glob("flagged_*.jsonl"))
        if not flagged_files:
            print("No flagged files found. Run cross-validation first.")
            return
        # TODO: Rebuild stats from flagged files
        print("Report generation from saved flags not yet implemented.")
        print(f"Found {len(flagged_files)} flagged files in {CORPUS_OUTPUT_DIR}")
        return

    async with AsyncLLMClient() as client:
        all_stats = []

        if args.all:
            corpus_files = sorted(CORPUS_OUTPUT_DIR.glob("*.jsonl"))
            corpus_files = [
                f for f in corpus_files if not f.name.startswith("flagged_")
            ]
        else:
            corpus_files = [Path(args.input)]

        for corpus_path in corpus_files:
            if not corpus_path.exists():
                logger.error(f"File not found: {corpus_path}")
                continue

            stats = await cross_validate_file(client, corpus_path)
            all_stats.append(stats)
            save_flagged(stats, CORPUS_OUTPUT_DIR)

        print_report(all_stats)


def main() -> None:
    parser = argparse.ArgumentParser(description="Cross-validation pipeline")
    parser.add_argument("--input", help="Path to corpus JSONL file")
    parser.add_argument("--all", action="store_true", help="Validate all corpus files")
    parser.add_argument("--report", action="store_true", help="Show agreement report")
    args = parser.parse_args()

    if not args.all and not args.report and not args.input:
        parser.error("Provide --input, --all, or --report")

    asyncio.run(run_cross_validation(args))


if __name__ == "__main__":
    main()
