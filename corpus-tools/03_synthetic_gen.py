#!/usr/bin/env python3
"""
Pipeline 3: Synthetic Generation (Sprints 3-5)

Three-stage batch pipeline:
  Stage A — Draft generation (MindRouter): bulk generate examples
  Stage B — Verification pass (Sonnet): review accuracy
  Stage C — Mechanical verification (local): compute correct answers for DT/GT

Fills gaps in: decision theory (B1-B5), game theory (B6-B10),
cognitive biases (E1), argument by analogy (A3.3), integrated scenarios,
and microeconomics (C1-C6).

Usage:
    python 03_synthetic_gen.py --group B1 --count 200 --domain healthcare
    python 03_synthetic_gen.py --group E1 --count 200 --domain workplace
    python 03_synthetic_gen.py --verify output/synthetic_B1.jsonl
    python 03_synthetic_gen.py --coverage  # Show what needs generating
"""

import argparse
import asyncio
import json
import logging
import random
import sys
from pathlib import Path

from config import CORPUS_OUTPUT_DIR, SYNTHETIC_GEN_BATCH_SIZE
from llm_client import AsyncLLMClient
from prompts.synthetic_gen import (
    SYSTEM_PROMPT,
    generate_bias_scenario,
    generate_decision_theory,
    generate_synthetic,
)
from schema import CorpusRecord, read_corpus, write_corpus
from taxonomy import TAXONOMY, get_codes_by_group, get_codes_by_track

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Domains for variety in synthetic generation
DOMAINS = [
    "healthcare", "education", "workplace", "sports", "cooking",
    "travel", "technology", "politics", "environment", "finance",
    "relationships", "parenting", "music", "gaming", "housing",
    "agriculture", "legal", "military", "science", "retail",
]

DIFFICULTY_TIERS = ["drill", "what_if", "puzzle"]


def load_anchor_examples(taxonomy_code: str) -> str:
    """Load relevant anchor examples for few-shot prompting."""
    anchor_file = CORPUS_OUTPUT_DIR / "anchors.jsonl"
    if not anchor_file.exists():
        return "(No anchor examples available yet)"

    anchors = read_corpus(anchor_file)
    prefix = taxonomy_code.split(".")[0]
    relevant = [a for a in anchors if a.taxonomy_code.startswith(prefix)]
    if not relevant:
        track = TAXONOMY[taxonomy_code]["track"]
        relevant = [a for a in anchors if a.track.value == track]

    examples = relevant[:3]
    if not examples:
        return "(No anchor examples available yet)"

    return "\n---\n".join(
        json.dumps(json.loads(ex.to_jsonl_line()), indent=2) for ex in examples
    )


def build_generation_plan(
    codes: dict[str, dict], count_per_code: int
) -> list[dict]:
    """Build a plan distributing examples across codes, tiers, and domains."""
    plan = []
    seq = 0

    for code, entry in codes.items():
        per_tier = max(1, count_per_code // len(DIFFICULTY_TIERS))

        for tier in DIFFICULTY_TIERS:
            for i in range(per_tier):
                domain = DOMAINS[seq % len(DOMAINS)]
                record_id = f"{code}-S{seq:04d}"
                plan.append({
                    "code": code,
                    "entry": entry,
                    "tier": tier,
                    "domain": domain,
                    "record_id": record_id,
                })
                seq += 1

    random.shuffle(plan)  # Mix codes to avoid sequential bias
    return plan


def build_request(item: dict) -> dict:
    """Build an LLM request for a single generation plan item."""
    code = item["code"]
    entry = item["entry"]
    track = entry["track"]
    anchor_examples = load_anchor_examples(code)

    # Choose specialized prompt for certain tracks
    if track in ("decision_theory",) and code.startswith("B"):
        prompt = generate_decision_theory(
            taxonomy_code=code,
            taxonomy_label=entry["label"],
            description=entry["description"],
            difficulty_tier=item["tier"],
            domain_constraint=item["domain"],
            seed_problem=entry["description"],  # Use description as seed
            record_id=item["record_id"],
        )
    elif track == "cognitive_biases":
        prompt = generate_bias_scenario(
            taxonomy_code=code,
            taxonomy_label=entry["label"],
            description=entry["description"],
            difficulty_tier=item["tier"],
            domain_constraint=item["domain"],
            record_id=item["record_id"],
        )
    else:
        prompt = generate_synthetic(
            taxonomy_code=code,
            taxonomy_label=entry["label"],
            pattern_type=entry["pattern_type"],
            track=track,
            description=entry["description"],
            difficulty_tier=item["tier"],
            domain_constraint=item["domain"],
            anchor_examples=anchor_examples,
            record_id=item["record_id"],
        )

    return {
        "messages": [{"role": "user", "content": prompt}],
        "task": "bulk_gen",
        "system": SYSTEM_PROMPT,
        "temperature": 0.8,
        "max_tokens": 4096,
        "json_mode": True,
    }


async def stage_a_generate(
    client: AsyncLLMClient,
    plan: list[dict],
    output_path: Path,
) -> int:
    """Stage A: Draft generation using MindRouter."""
    logger.info(f"Stage A: Generating {len(plan)} drafts...")

    requests = [build_request(item) for item in plan]
    success = 0
    records: list[CorpusRecord] = []

    def on_progress(done: int, total: int) -> None:
        if done % 20 == 0 or done == total:
            logger.info(f"  Generated: {done}/{total}")

    # Process in batches
    for batch_start in range(0, len(requests), SYNTHETIC_GEN_BATCH_SIZE):
        batch = requests[batch_start : batch_start + SYNTHETIC_GEN_BATCH_SIZE]
        results = await client.batch_complete(batch, on_progress=on_progress)

        for result in results:
            if isinstance(result, Exception):
                continue
            try:
                data = json.loads(result.content)
                record = CorpusRecord.model_validate(data)
                records.append(record)
                success += 1
            except (json.JSONDecodeError, Exception) as e:
                logger.debug(f"Parse error: {e}")

    write_corpus(records, output_path)
    logger.info(f"Stage A complete: {success}/{len(plan)} generated -> {output_path}")
    return success


async def stage_b_verify(
    client: AsyncLLMClient,
    corpus_path: Path,
    output_path: Path,
) -> tuple[int, int]:
    """Stage B: Verification pass using Sonnet."""
    records = read_corpus(corpus_path)
    logger.info(f"Stage B: Verifying {len(records)} records with Sonnet...")

    requests = []
    for record in records:
        entry = TAXONOMY.get(record.taxonomy_code)
        if entry is None:
            continue

        prompt = f"""\
Verify this synthetic training example for accuracy and quality.

## Record
{json.dumps(json.loads(record.to_jsonl_line()), indent=2)}

## Expected Taxonomy
- Code: {record.taxonomy_code}
- Label: {entry['label']}
- Description: {entry['description']}
- Pattern type: {entry['pattern_type']}

## Checks
1. Does the scenario actually illustrate {entry['label']}? (not a different pattern)
2. Is the structure.pattern_description accurate?
3. For quantitative examples: are the numbers and computations correct?
4. Is the difficulty_tier appropriate?
5. Is the assessment pedagogically sound?

Return JSON:
{{
  "pass": true/false,
  "taxonomy_correct": true/false,
  "math_correct": true/false/null,
  "issues": ["list of issues"],
  "severity": "minor" | "major" | "critical"
}}\
"""
        requests.append({
            "messages": [{"role": "user", "content": prompt}],
            "task": "verify",
            "temperature": 0.2,
            "max_tokens": 1024,
            "json_mode": True,
        })

    results = await client.batch_complete(requests)

    passed: list[CorpusRecord] = []
    failed = 0

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            failed += 1
            continue
        try:
            verdict = json.loads(result.content)
            if verdict.get("pass") and verdict.get("severity") != "critical":
                passed.append(records[i])
            else:
                failed += 1
                logger.debug(
                    f"Failed {records[i].id}: {verdict.get('issues', [])}"
                )
        except json.JSONDecodeError:
            failed += 1

    write_corpus(passed, output_path)
    logger.info(
        f"Stage B complete: {len(passed)} passed, {failed} failed -> {output_path}"
    )
    return len(passed), failed


def show_coverage() -> None:
    """Show which taxonomy codes have synthetic examples and which need more."""
    counts: dict[str, dict[str, int]] = {}

    for jsonl_file in CORPUS_OUTPUT_DIR.glob("synthetic_*.jsonl"):
        records = read_corpus(jsonl_file)
        for r in records:
            counts.setdefault(r.taxonomy_code, {"drill": 0, "what_if": 0, "puzzle": 0})
            counts[r.taxonomy_code][r.difficulty_tier.value] += 1

    # Also count anchors
    anchor_file = CORPUS_OUTPUT_DIR / "anchors.jsonl"
    if anchor_file.exists():
        for r in read_corpus(anchor_file):
            counts.setdefault(r.taxonomy_code, {"drill": 0, "what_if": 0, "puzzle": 0})
            counts[r.taxonomy_code][r.difficulty_tier.value] += 1

    print(f"\n{'Code':<8} {'Label':<40} {'Drill':>6} {'WhatIf':>6} {'Puzzle':>6} {'Total':>6}")
    print("-" * 80)

    for code in sorted(TAXONOMY.keys()):
        entry = TAXONOMY[code]
        c = counts.get(code, {"drill": 0, "what_if": 0, "puzzle": 0})
        total = sum(c.values())
        marker = " !" if total == 0 else ""
        print(
            f"{code:<8} {entry['label']:<40} {c['drill']:>6} {c['what_if']:>6} "
            f"{c['puzzle']:>6} {total:>6}{marker}"
        )


async def run_generation(args: argparse.Namespace) -> None:
    """Main generation pipeline."""
    if args.coverage:
        show_coverage()
        return

    async with AsyncLLMClient() as client:
        if args.verify:
            input_path = Path(args.verify)
            output_path = input_path.with_stem(input_path.stem + "_verified")
            await stage_b_verify(client, input_path, output_path)
            return

        # Build generation plan
        codes = get_codes_by_group(args.group)
        if not codes:
            logger.error(f"No codes found for group: {args.group}")
            sys.exit(1)

        count_per_code = args.count // len(codes)
        plan = build_generation_plan(codes, count_per_code)

        if args.domain:
            # Override domain constraint
            for item in plan:
                item["domain"] = args.domain

        output_path = CORPUS_OUTPUT_DIR / f"synthetic_{args.group}.jsonl"

        # Stage A: Generate drafts
        generated = await stage_a_generate(client, plan, output_path)

        # Stage B: Verify (if requested)
        if args.auto_verify and generated > 0:
            verified_path = output_path.with_stem(output_path.stem + "_verified")
            await stage_b_verify(client, output_path, verified_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Synthetic generation pipeline")
    parser.add_argument("--group", help="Taxonomy group to generate for (e.g. B1, E1)")
    parser.add_argument("--count", type=int, default=100, help="Total examples to generate")
    parser.add_argument("--domain", help="Override domain constraint")
    parser.add_argument("--verify", help="Run Stage B verification on a file")
    parser.add_argument("--auto-verify", action="store_true", help="Auto-verify after generation")
    parser.add_argument("--coverage", action="store_true", help="Show coverage report")
    args = parser.parse_args()

    if not args.coverage and not args.verify and not args.group:
        parser.error("--group is required for generation")

    asyncio.run(run_generation(args))


if __name__ == "__main__":
    main()
