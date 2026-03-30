#!/usr/bin/env python3
"""
QC7: Expert review — stratified quality assessment of the corpus.

Samples 10 records per taxonomy code (1,820 total for 182 codes) and scores
each on 5 dimensions using Nemotron-3-Super-120b as reviewer.

For weak tracks (microeconomics, dennett_tools) and new synthetic records
(phil4040_synthetic.jsonl), reviews 100% of records.

Dimensions (0-5 scale):
  1. Taxonomy accuracy — does the scenario match the assigned code?
  2. Scenario quality — is the scenario vivid, specific, and pedagogically sound?
  3. Structure accuracy — is the pattern analysis correct?
  4. Assessment quality — does the rubric probe real understanding?
  5. Game integration — does the NPC/game framing feel natural?

Usage:
    python3 qc7_expert_review.py                     # Full stratified review
    python3 qc7_expert_review.py --track dennett_tools  # Review one track fully
    python3 qc7_expert_review.py --file phil4040_synthetic.jsonl  # Review one file
    python3 qc7_expert_review.py --limit 50           # Test run
    python3 qc7_expert_review.py --resume             # Resume from checkpoint
    python3 qc7_expert_review.py --report             # Generate report from results
"""

import argparse
import asyncio
import json
import os
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

import openai

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

# ── Config ──

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"
REVIEWER_MODEL = "Nemotron-3-Super-120b"
CONCURRENCY = 6  # Lower than cross-val — longer prompts
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
RESULTS_FILE = OUTPUT_DIR / "qc7_expert_review.jsonl"
REPORT_FILE = Path(__file__).resolve().parent.parent / "reports" / "qc7-expert-review.md"

# Tracks to review 100% (weak areas)
FULL_REVIEW_TRACKS = {"dennett_tools", "microeconomics"}
# Files to review 100% (new/unreviewed)
FULL_REVIEW_FILES = {"phil4040_synthetic.jsonl", "anchors_phil4040.jsonl", "adapted_phil4040.jsonl"}
SAMPLES_PER_CODE = 10


def build_review_prompt(record: dict) -> str:
    """Build an expert review prompt."""
    return f"""You are an expert reviewer assessing the quality of a training record for
an educational AI system that teaches critical thinking, logic, decision theory,
and game theory.

Review this record on 5 dimensions (score each 1-5):

**RECORD:**
- ID: {record.get('id', '?')}
- Taxonomy: {record.get('taxonomy_code', '?')}: {record.get('taxonomy_label', '?')}
- Track: {record.get('track', '?')}
- Pattern type: {record.get('pattern_type', '?')}
- Difficulty: {record.get('difficulty_tier', '?')}

- Scenario context: {record.get('scenario', {}).get('context', 'MISSING')}
- Scenario text: {record.get('scenario', {}).get('text', 'MISSING')[:500]}
- Pattern name: {record.get('structure', {}).get('pattern_name', 'MISSING')}
- Pattern description: {record.get('structure', {}).get('pattern_description', 'MISSING')[:500]}
- Why wrong: {record.get('structure', {}).get('why_wrong', 'N/A')[:300] if record.get('structure', {}).get('why_wrong') else 'N/A'}
- Why right: {record.get('structure', {}).get('why_right', 'N/A')[:300] if record.get('structure', {}).get('why_right') else 'N/A'}
- Formal form: {record.get('structure', {}).get('formal_form', 'N/A')[:300] if record.get('structure', {}).get('formal_form') else 'N/A'}
- Assessment prompt: {record.get('assessment', {}).get('identification_prompt', 'MISSING')[:200]}
- NPC personality: {record.get('game_hooks', {}).get('npc_personality', 'MISSING')[:200]}

**DIMENSIONS (score each 1-5):**
1. **taxonomy_accuracy**: Does this scenario genuinely illustrate the claimed taxonomy code? (1=wrong code, 5=perfect match)
2. **scenario_quality**: Is the scenario vivid, specific, well-written, and pedagogically sound? (1=generic/confusing, 5=engaging and clear)
3. **structure_accuracy**: Is the pattern analysis (description, why_wrong/right, formal_form) correct? (1=factual errors, 5=precise and insightful)
4. **assessment_quality**: Does the identification prompt + rubric probe genuine understanding, not just recall? (1=trivial/leading, 5=Socratic and probing)
5. **game_integration**: Does the NPC framing feel natural and engaging? (1=awkward/forced, 5=immersive)

Also provide:
- **issues**: List any specific problems found (empty list if none)
- **overall_verdict**: "pass" (all scores ≥ 3), "marginal" (any score 2), or "fail" (any score 1)

Respond with ONLY valid JSON:
{{"taxonomy_accuracy": N, "scenario_quality": N, "structure_accuracy": N, "assessment_quality": N, "game_integration": N, "issues": ["..."], "overall_verdict": "pass|marginal|fail"}}"""


# ── Load and sample ──

def load_all_records() -> list[tuple[str, dict]]:
    """Load all training records with source filename."""
    records = []
    for filepath in sorted(OUTPUT_DIR.glob("*.jsonl")):
        if "benchmark" in filepath.name or "qc7" in filepath.name:
            continue
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    if rec.get("scenario", {}).get("text"):
                        records.append((filepath.name, rec))
                except json.JSONDecodeError:
                    continue
    return records


def select_review_set(
    all_records: list[tuple[str, dict]],
    track_filter: str | None = None,
    file_filter: str | None = None,
) -> list[dict]:
    """Select records for review: stratified sample + full review of weak areas."""
    if track_filter:
        return [rec for fname, rec in all_records if rec.get("track") == track_filter]

    if file_filter:
        return [rec for fname, rec in all_records if fname == file_filter]

    selected = set()  # Track by ID to avoid duplicates
    review_list = []

    # 1. Full review of weak tracks
    for fname, rec in all_records:
        track = rec.get("track", "")
        if track in FULL_REVIEW_TRACKS:
            rid = rec.get("id", "")
            if rid not in selected:
                selected.add(rid)
                review_list.append(rec)

    # 2. Full review of new/unreviewed files
    for fname, rec in all_records:
        if fname in FULL_REVIEW_FILES:
            rid = rec.get("id", "")
            if rid not in selected:
                selected.add(rid)
                review_list.append(rec)

    # 3. Stratified sample: 10 per code for remaining
    by_code = defaultdict(list)
    for fname, rec in all_records:
        rid = rec.get("id", "")
        if rid not in selected:
            by_code[rec.get("taxonomy_code", "?")].append(rec)

    random.seed(42)
    for code, recs in sorted(by_code.items()):
        sample = random.sample(recs, min(SAMPLES_PER_CODE, len(recs)))
        for rec in sample:
            rid = rec.get("id", "")
            if rid not in selected:
                selected.add(rid)
                review_list.append(rec)

    return review_list


def load_existing_results() -> set[str]:
    done = set()
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE) as f:
            for line in f:
                if line.strip():
                    try:
                        done.add(json.loads(line).get("id", ""))
                    except json.JSONDecodeError:
                        pass
    return done


# ── API ──

async def review_record(
    client: openai.AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    record: dict,
) -> dict:
    """Review a single record."""
    prompt = build_review_prompt(record)
    rid = record.get("id", "?")

    for attempt in range(3):
        try:
            async with semaphore:
                resp = await client.chat.completions.create(
                    model=REVIEWER_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=300,
                    temperature=0.1,
                    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                )
            text = (resp.choices[0].message.content or "").strip()

            # Parse JSON
            if text.startswith("```"):
                text = text.split("```")[1].strip()
                if text.startswith("json"):
                    text = text[4:].strip()
            parsed = json.loads(text)

            return {
                "id": rid,
                "taxonomy_code": record.get("taxonomy_code", "?"),
                "taxonomy_label": record.get("taxonomy_label", "?"),
                "track": record.get("track", "?"),
                "difficulty_tier": record.get("difficulty_tier", "?"),
                "source_type": record.get("source", {}).get("type", "?"),
                "taxonomy_accuracy": parsed.get("taxonomy_accuracy", 0),
                "scenario_quality": parsed.get("scenario_quality", 0),
                "structure_accuracy": parsed.get("structure_accuracy", 0),
                "assessment_quality": parsed.get("assessment_quality", 0),
                "game_integration": parsed.get("game_integration", 0),
                "issues": parsed.get("issues", []),
                "overall_verdict": parsed.get("overall_verdict", "?"),
            }

        except Exception as e:
            if attempt == 2:
                return {
                    "id": rid,
                    "taxonomy_code": record.get("taxonomy_code", "?"),
                    "taxonomy_label": record.get("taxonomy_label", "?"),
                    "track": record.get("track", "?"),
                    "difficulty_tier": record.get("difficulty_tier", "?"),
                    "source_type": record.get("source", {}).get("type", "?"),
                    "taxonomy_accuracy": -1,
                    "scenario_quality": -1,
                    "structure_accuracy": -1,
                    "assessment_quality": -1,
                    "game_integration": -1,
                    "issues": [f"Review error: {str(e)[:100]}"],
                    "overall_verdict": "error",
                }
            await asyncio.sleep(2 ** (attempt + 1))


# ── Report ──

def generate_report():
    """Generate expert review report."""
    if not RESULTS_FILE.exists():
        print("No results file found.")
        return

    results = []
    with open(RESULTS_FILE) as f:
        for line in f:
            if line.strip():
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    pass

    valid = [r for r in results if r.get("taxonomy_accuracy", -1) >= 0]
    total = len(valid)

    if not total:
        print("No valid results.")
        return

    dims = ["taxonomy_accuracy", "scenario_quality", "structure_accuracy",
            "assessment_quality", "game_integration"]

    # Overall averages
    overall = {d: sum(r[d] for r in valid) / total for d in dims}
    verdicts = Counter(r["overall_verdict"] for r in valid)

    # By track
    track_scores = defaultdict(lambda: {d: [] for d in dims})
    for r in valid:
        for d in dims:
            track_scores[r["track"]][d].append(r[d])

    # By source type
    source_scores = defaultdict(lambda: {d: [] for d in dims})
    for r in valid:
        for d in dims:
            source_scores[r["source_type"]][d].append(r[d])

    # Failures
    failures = [r for r in valid if r["overall_verdict"] == "fail"]
    marginals = [r for r in valid if r["overall_verdict"] == "marginal"]

    lines = [
        "# QC7: Expert Review Report",
        "",
        f"**Date:** {time.strftime('%Y-%m-%d')}",
        f"**Scope:** {total} records reviewed",
        f"**Reviewer:** {REVIEWER_MODEL}",
        "",
        "## Overall Scores",
        "",
        "| Dimension | Mean |",
        "|-----------|------|",
    ]
    for d in dims:
        lines.append(f"| {d.replace('_', ' ').title()} | {overall[d]:.2f} / 5 |")

    lines.extend([
        "",
        f"| Verdict | Count | Rate |",
        f"|---------|-------|------|",
        f"| Pass | {verdicts.get('pass', 0)} | {verdicts.get('pass', 0)/total:.1%} |",
        f"| Marginal | {verdicts.get('marginal', 0)} | {verdicts.get('marginal', 0)/total:.1%} |",
        f"| Fail | {verdicts.get('fail', 0)} | {verdicts.get('fail', 0)/total:.1%} |",
        "",
        "## Scores by Track",
        "",
        "| Track | Tax | Scen | Struct | Assess | Game | n |",
        "|-------|-----|------|--------|--------|------|---|",
    ])
    for track in sorted(track_scores):
        s = track_scores[track]
        n = len(s[dims[0]])
        means = [sum(s[d]) / n for d in dims]
        lines.append(f"| {track} | {means[0]:.1f} | {means[1]:.1f} | {means[2]:.1f} | {means[3]:.1f} | {means[4]:.1f} | {n} |")

    lines.extend([
        "",
        "## Scores by Source Type",
        "",
        "| Source | Tax | Scen | Struct | Assess | Game | n |",
        "|--------|-----|------|--------|--------|------|---|",
    ])
    for src in sorted(source_scores):
        s = source_scores[src]
        n = len(s[dims[0]])
        means = [sum(s[d]) / n for d in dims]
        lines.append(f"| {src} | {means[0]:.1f} | {means[1]:.1f} | {means[2]:.1f} | {means[3]:.1f} | {means[4]:.1f} | {n} |")

    if failures:
        lines.extend([
            "",
            f"## Failed Records ({len(failures)})",
            "",
        ])
        for r in failures[:30]:
            issues = "; ".join(r.get("issues", [])[:2])
            lines.append(f"- **{r['id']}** ({r['taxonomy_code']}: {r['taxonomy_label']}): {issues}")

    if marginals:
        lines.extend([
            "",
            f"## Marginal Records ({len(marginals)})",
            "",
        ])
        for r in marginals[:30]:
            low_dims = [d for d in dims if r[d] <= 2]
            lines.append(f"- **{r['id']}** ({r['taxonomy_code']}): low on {', '.join(low_dims)}")

    report_text = "\n".join(lines) + "\n"
    with open(REPORT_FILE, "w") as f:
        f.write(report_text)
    print(f"Report written to {REPORT_FILE}")

    print(f"\n{'='*60}")
    print(f"QC7 EXPERT REVIEW SUMMARY")
    print(f"{'='*60}")
    print(f"Reviewed: {total} records")
    for d in dims:
        print(f"  {d}: {overall[d]:.2f}/5")
    print(f"Pass: {verdicts.get('pass', 0)} | Marginal: {verdicts.get('marginal', 0)} | Fail: {verdicts.get('fail', 0)}")


# ── Main ──

async def run_review(records: list[dict], resume: bool = False):
    client = openai.AsyncOpenAI(
        api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL
    )
    semaphore = asyncio.Semaphore(CONCURRENCY)

    done_ids = load_existing_results() if resume else set()
    remaining = [r for r in records if r.get("id", "") not in done_ids]

    print(f"Total to review: {len(records)}")
    print(f"Already done: {len(done_ids)}")
    print(f"Remaining: {len(remaining)}")

    if not remaining:
        print("Nothing to do.")
        return

    mode = "a" if resume and done_ids else "w"
    outf = open(RESULTS_FILE, mode)

    done = 0
    start = time.time()

    batch_size = CONCURRENCY * 2
    for batch_start in range(0, len(remaining), batch_size):
        batch = remaining[batch_start:batch_start + batch_size]
        results = await asyncio.gather(*[
            review_record(client, semaphore, r) for r in batch
        ])
        for result in results:
            outf.write(json.dumps(result, ensure_ascii=False) + "\n")
            done += 1
        outf.flush()

        if done % 50 == 0 or done == len(remaining):
            elapsed = time.time() - start
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(remaining) - done) / rate if rate > 0 else 0
            print(f"  Progress: {done}/{len(remaining)} "
                  f"[{elapsed:.0f}s, {rate:.1f}/s, ETA {eta:.0f}s]", flush=True)

    outf.close()


def main():
    parser = argparse.ArgumentParser(description="QC7: Expert review with Nemotron")
    parser.add_argument("--track", help="Review all records in this track")
    parser.add_argument("--file", help="Review all records in this file")
    parser.add_argument("--limit", type=int, help="Limit total records")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    if args.report:
        generate_report()
        return

    all_records = load_all_records()
    review_set = select_review_set(all_records, args.track, args.file)

    if args.limit:
        random.seed(42)
        random.shuffle(review_set)
        review_set = review_set[:args.limit]

    print(f"Selected {len(review_set)} records for review")
    asyncio.run(run_review(review_set, resume=args.resume))
    generate_report()


if __name__ == "__main__":
    main()
