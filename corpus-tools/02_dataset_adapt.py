#!/usr/bin/env python3
"""
Pipeline 2: Dataset Adaptation (Sprint 2)

Batch pipeline: enriches existing dataset examples with full corpus schema
fields using MindRouter for bulk work, Sonnet for validation.

Supported datasets:
- Jin et al. (fallacy detection, 3,761 examples) -> A5-A7
- FOLIO (logical reasoning, 1,435 examples) -> A2
- LogiQA 2.0 (LSAT-style, 15,708 examples) -> mixed A codes
- IBM-Rank-30k (argument quality, 30,000 examples) -> A1, A3
- Corr2Cause (causal reasoning, ~5,000 examples) -> A3.4-A3.5, A8.7
- SemEval Propaganda (6,129 examples) -> A9-A10
- EconNLI (economic reasoning, 10,810 examples) -> C codes

Usage:
    python 02_dataset_adapt.py --dataset jin --input data/jin.jsonl
    python 02_dataset_adapt.py --dataset folio --input data/folio.jsonl --validate
    python 02_dataset_adapt.py --validate-only --input output/adapted_jin.jsonl
"""

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

from config import (
    ADAPTATION_BATCH_SIZE,
    BERT_REVIEW_SAMPLE_RATE,
    CORPUS_OUTPUT_DIR,
)
from llm_client import AsyncLLMClient
from prompts.dataset_adapt import SYSTEM_PROMPT, enrich_existing
from schema import CorpusRecord, read_corpus, write_corpus

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


# ─── Dataset-specific label → taxonomy code mappings ──────────────────────────

DATASET_MAPPINGS: dict[str, dict[str, str]] = {
    "jin": {
        # Jin et al. fallacy labels -> taxonomy codes
        "ad hominem": "A7.1",
        "straw man": "A7.2",
        "appeal to emotion": "A7.7",
        "false cause": "A8.7",
        "slippery slope": "A5.3",
        "appeal to authority": "A7.6",
        "bandwagon": "A7.9",
        "false dichotomy": "A6.4",
        "circular reasoning": "A6.3",
        "hasty generalization": "A8.6",
        "red herring": "A10.3",
        "tu quoque": "A7.3",
        "equivocation": "A6.5",
        "appeal to nature": "A7.8",
        "loaded question": "A7.13",
        "burden of proof": "A7.10",
        "anecdotal": "A7.16",
        "middle ground": "A7.15",
    },
    "folio": {
        # FOLIO: all map to deductive logic
        "entailment": "A2.1",
        "contradiction": "A2.7",
        "neutral": "A2.1",
    },
    "propaganda": {
        # SemEval propaganda techniques
        "name_calling": "A10.1",
        "repetition": "A10.2",
        "whataboutism": "A10.3",
        "flag_waving": "A10.4",
        "thought_terminating_cliche": "A10.5",
        "exaggeration": "A10.6",
        "doubt": "A10.7",
        "appeal_to_fear": "A7.7",
        "loaded_language": "A9.1",
        "bandwagon": "A7.9",
        "straw_man": "A7.2",
        "red_herring": "A10.3",
    },
    "corr2cause": {
        # Corr2Cause labels
        "correlation": "A3.5",
        "causation": "A3.4",
        "no_relation": "A8.7",
    },
    "econnli": {
        # EconNLI -> C codes (simplified)
        "entailment": "C6.3",
        "contradiction": "C7.1",
        "neutral": "C1.1",
    },
}


def load_input_dataset(path: Path, dataset_name: str) -> list[dict]:
    """
    Load a dataset from JSONL. Expected format per line:
    {"text": "...", "label": "...", "id": "...", ...}
    """
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    logger.info(f"Loaded {len(records)} records from {path}")
    return records


def map_to_taxonomy(
    record: dict, dataset_name: str
) -> tuple[str, str] | None:
    """Map a dataset record's label to a taxonomy code. Returns (code, label) or None."""
    mapping = DATASET_MAPPINGS.get(dataset_name, {})
    original_label = record.get("label", "").lower().strip()

    code = mapping.get(original_label)
    if code is None:
        # Try partial matching
        for key, value in mapping.items():
            if key in original_label or original_label in key:
                code = value
                break

    if code is None:
        return None

    from taxonomy import TAXONOMY
    entry = TAXONOMY.get(code)
    if entry is None:
        return None

    return code, entry["label"]


def load_anchor_examples(taxonomy_code: str, max_examples: int = 3) -> str:
    """Load anchor examples for few-shot prompting."""
    anchor_file = CORPUS_OUTPUT_DIR / "anchors.jsonl"
    if not anchor_file.exists():
        return "(No anchor examples available yet)"

    anchors = read_corpus(anchor_file)
    # Find anchors with matching code group
    prefix = taxonomy_code.split(".")[0]  # e.g. "A7" from "A7.1"
    relevant = [a for a in anchors if a.taxonomy_code.startswith(prefix)]

    if not relevant:
        # Fall back to any anchors in the same track
        from taxonomy import TAXONOMY
        track = TAXONOMY[taxonomy_code]["track"]
        relevant = [a for a in anchors if a.track.value == track]

    examples = relevant[:max_examples]
    if not examples:
        return "(No anchor examples available yet)"

    return "\n---\n".join(
        json.dumps(json.loads(ex.to_jsonl_line()), indent=2)
        for ex in examples
    )


async def adapt_batch(
    client: AsyncLLMClient,
    records: list[dict],
    dataset_name: str,
    output_path: Path,
    start_idx: int = 0,
) -> tuple[int, int]:
    """Adapt a batch of records. Returns (success_count, fail_count)."""
    from taxonomy import TAXONOMY

    requests = []
    valid_records = []

    for i, record in enumerate(records):
        mapping = map_to_taxonomy(record, dataset_name)
        if mapping is None:
            continue

        code, label = mapping
        entry = TAXONOMY[code]
        record_id = f"{code}-{start_idx + i:04d}"
        anchor_examples = load_anchor_examples(code)

        prompt = enrich_existing(
            original_text=record.get("text", ""),
            original_label=record.get("label", ""),
            taxonomy_code=code,
            taxonomy_label=label,
            pattern_type=entry["pattern_type"],
            track=entry["track"],
            description=entry["description"],
            difficulty_tier="drill",  # Default; can be adjusted
            anchor_examples=anchor_examples,
            record_id=record_id,
            source_dataset=dataset_name,
            original_id=record.get("id"),
        )

        requests.append({
            "messages": [{"role": "user", "content": prompt}],
            "task": "adapt",
            "system": SYSTEM_PROMPT,
            "temperature": 0.5,
            "max_tokens": 4096,
            "json_mode": True,
        })
        valid_records.append(record)

    if not requests:
        logger.warning("No records could be mapped to taxonomy codes")
        return 0, 0

    logger.info(f"Processing {len(requests)} records...")

    def on_progress(done: int, total: int) -> None:
        if done % 10 == 0 or done == total:
            logger.info(f"  Progress: {done}/{total}")

    results = await client.batch_complete(requests, on_progress=on_progress)

    success = 0
    failures = 0
    adapted: list[CorpusRecord] = []

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            failures += 1
            continue

        try:
            data = json.loads(result.content)
            record = CorpusRecord.model_validate(data)
            adapted.append(record)
            success += 1
        except (json.JSONDecodeError, Exception) as e:
            logger.warning(f"Record {i} parse error: {e}")
            failures += 1

    # Append to output file
    if adapted:
        mode = "a" if output_path.exists() else "w"
        with open(output_path, mode) as f:
            for record in adapted:
                f.write(record.to_jsonl_line() + "\n")

    logger.info(f"Batch complete: {success} succeeded, {failures} failed")
    return success, failures


async def validate_sample(
    client: AsyncLLMClient,
    corpus_path: Path,
    sample_rate: float = 0.10,
) -> None:
    """Validate a stratified sample using Sonnet."""
    import random

    records = read_corpus(corpus_path)
    sample_size = max(1, int(len(records) * sample_rate))
    sample = random.sample(records, min(sample_size, len(records)))

    logger.info(f"Validating {len(sample)} records ({sample_rate*100:.0f}% sample)")

    requests = []
    for record in sample:
        prompt = f"""\
Review this training corpus record for quality.

Record:
{json.dumps(json.loads(record.to_jsonl_line()), indent=2)}

Check:
1. Is the taxonomy_code correct for this scenario?
2. Is the structure.pattern_description accurate?
3. Is the assessment.identification_prompt pedagogically sound?
4. Does the game_hooks content feel natural for an NPC?
5. Is the difficulty_tier appropriate?

Return JSON:
{{
  "pass": true/false,
  "issues": ["list of issues if any"],
  "suggested_fixes": ["list of suggested changes if any"]
}}\
"""
        requests.append({
            "messages": [{"role": "user", "content": prompt}],
            "task": "verify",
            "temperature": 0.3,
            "max_tokens": 2048,
            "json_mode": True,
        })

    results = await client.batch_complete(requests)

    passes = 0
    failures = 0
    issues_by_type: dict[str, int] = {}

    for result in results:
        if isinstance(result, Exception):
            failures += 1
            continue
        try:
            data = json.loads(result.content)
            if data.get("pass"):
                passes += 1
            else:
                failures += 1
                for issue in data.get("issues", []):
                    issues_by_type[issue] = issues_by_type.get(issue, 0) + 1
        except json.JSONDecodeError:
            failures += 1

    total = passes + failures
    pass_rate = passes / total if total > 0 else 0
    logger.info(f"\nValidation results: {passes}/{total} passed ({pass_rate:.1%})")
    if issues_by_type:
        logger.info("Common issues:")
        for issue, count in sorted(issues_by_type.items(), key=lambda x: -x[1]):
            logger.info(f"  [{count}x] {issue}")


async def run_adaptation(args: argparse.Namespace) -> None:
    """Main adaptation pipeline."""
    async with AsyncLLMClient() as client:
        if args.validate_only:
            await validate_sample(
                client, Path(args.input), args.sample_rate or BERT_REVIEW_SAMPLE_RATE
            )
            return

        input_path = Path(args.input)
        if not input_path.exists():
            logger.error(f"Input file not found: {input_path}")
            sys.exit(1)

        dataset = load_input_dataset(input_path, args.dataset)
        output_path = CORPUS_OUTPUT_DIR / f"adapted_{args.dataset}.jsonl"

        total_success = 0
        total_fail = 0

        # Process in batches
        for batch_start in range(0, len(dataset), ADAPTATION_BATCH_SIZE):
            batch = dataset[batch_start : batch_start + ADAPTATION_BATCH_SIZE]
            logger.info(
                f"\nBatch {batch_start // ADAPTATION_BATCH_SIZE + 1}: "
                f"records {batch_start}-{batch_start + len(batch)}"
            )
            s, f = await adapt_batch(
                client, batch, args.dataset, output_path, start_idx=batch_start
            )
            total_success += s
            total_fail += f

        logger.info(
            f"\nAdaptation complete: {total_success} succeeded, {total_fail} failed"
        )
        logger.info(f"Output: {output_path}")

        if args.validate:
            logger.info("\nRunning validation on adapted records...")
            await validate_sample(client, output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dataset adaptation pipeline")
    parser.add_argument(
        "--dataset",
        choices=["jin", "folio", "logiqa", "ibm", "corr2cause", "propaganda", "econnli"],
        help="Source dataset name",
    )
    parser.add_argument("--input", required=True, help="Path to input JSONL")
    parser.add_argument(
        "--validate", action="store_true", help="Run validation after adaptation"
    )
    parser.add_argument(
        "--validate-only", action="store_true", help="Only run validation"
    )
    parser.add_argument(
        "--sample-rate", type=float, help="Validation sample rate (default: 0.10)"
    )
    args = parser.parse_args()

    if not args.validate_only and not args.dataset:
        parser.error("--dataset is required unless using --validate-only")

    asyncio.run(run_adaptation(args))


if __name__ == "__main__":
    main()
