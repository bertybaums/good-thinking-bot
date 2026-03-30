#!/usr/bin/env python3
"""
QC7: Full cross-validation of the 28K-record corpus using Nemotron-3-Super-120b.

For each record:
1. Strip the taxonomy code and label
2. Present the scenario + structure to Nemotron
3. Ask it to classify into one of the 182 codes
4. Compare to the assigned code
5. Flag disagreements with reasoning

Output: qc7_cross_validation.jsonl (one result per record)
Summary: qc7_cross_validation_summary.md

Usage:
    python3 qc7_cross_validate.py                    # Full run
    python3 qc7_cross_validate.py --limit 100        # Test run
    python3 qc7_cross_validate.py --resume            # Resume from last checkpoint
    python3 qc7_cross_validate.py --report            # Generate report from existing results
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
SUBJECT_MODEL = "Nemotron-3-Super-120b"
CONCURRENCY = 8
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
RESULTS_FILE = OUTPUT_DIR / "qc7_cross_validation.jsonl"
REPORT_FILE = Path(__file__).resolve().parent.parent / "reports" / "qc7-cross-validation.md"

# Build taxonomy reference (code → label + description, grouped by track)
TRACK_CODES = defaultdict(list)
for code, entry in sorted(TAXONOMY.items()):
    TRACK_CODES[entry["track"]].append(code)

def build_options_text(track: str) -> str:
    """Build the classification options for a given track."""
    codes = TRACK_CODES.get(track, [])
    if not codes:
        # Fallback: show all codes
        codes = sorted(TAXONOMY.keys())
    lines = []
    for c in codes:
        e = TAXONOMY[c]
        lines.append(f"  {c}: {e['label']} — {e['description'][:100]}")
    return "\n".join(lines)


def build_classify_prompt(record: dict) -> str:
    """Build a classification prompt for the record."""
    scenario = record.get("scenario", {})
    structure = record.get("structure", {})
    track = record.get("track", "")

    # Show all codes in the same track (narrower choice set = better accuracy)
    options = build_options_text(track)

    # Also include 5 random codes from other tracks as distractors
    other_codes = [c for c in TAXONOMY if TAXONOMY[c]["track"] != track]
    distractors = random.sample(other_codes, min(5, len(other_codes)))
    distractor_lines = []
    for c in distractors:
        e = TAXONOMY[c]
        distractor_lines.append(f"  {c}: {e['label']} — {e['description'][:100]}")

    all_options = options + "\n" + "\n".join(distractor_lines)

    return f"""You are classifying a reasoning scenario into a taxonomy of critical thinking,
logic, decision theory, game theory, and related concepts.

Read the scenario and analysis carefully, then select the SINGLE most appropriate
taxonomy code from the options below.

**Scenario context:** {scenario.get('context', '')}

**Scenario text:** {scenario.get('text', '')}

**Pattern analysis:** {structure.get('pattern_description', '')}

**Available codes:**
{all_options}

Respond with ONLY valid JSON: {{"code": "X.Y", "confidence": "high/medium/low", "reasoning": "brief explanation"}}"""


# ── Load corpus ──

def load_training_corpus() -> list[dict]:
    """Load all training records (exclude benchmarks)."""
    records = []
    for filepath in sorted(OUTPUT_DIR.glob("*.jsonl")):
        if "benchmark" in filepath.name:
            continue
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    if rec.get("scenario", {}).get("text"):
                        records.append(rec)
                except json.JSONDecodeError:
                    continue
    return records


def load_existing_results() -> set[str]:
    """Load IDs already processed."""
    done = set()
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        r = json.loads(line)
                        done.add(r.get("id", ""))
                    except json.JSONDecodeError:
                        continue
    return done


# ── API call ──

async def classify_record(
    client: openai.AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    record: dict,
) -> dict:
    """Classify a single record."""
    prompt = build_classify_prompt(record)
    rid = record.get("id", "?")
    assigned_code = record.get("taxonomy_code", "?")

    for attempt in range(3):
        try:
            async with semaphore:
                resp = await client.chat.completions.create(
                    model=SUBJECT_MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    temperature=0.1,
                    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                )
            text = resp.choices[0].message.content or ""

            # Parse response
            try:
                # Try to extract JSON from the response
                text = text.strip()
                if text.startswith("```"):
                    text = text.split("```")[1].strip()
                    if text.startswith("json"):
                        text = text[4:].strip()
                parsed = json.loads(text)
                predicted_code = parsed.get("code", "?")
                confidence = parsed.get("confidence", "?")
                reasoning = parsed.get("reasoning", "")
            except json.JSONDecodeError:
                # Fallback: try to extract code from plain text
                predicted_code = text.strip().split()[0].strip("()[]\"'.,") if text else "?"
                confidence = "?"
                reasoning = text[:200]

            # Determine verdict
            if predicted_code == assigned_code:
                verdict = "confirmed"
            elif predicted_code in TAXONOMY:
                # Check if same track
                pred_track = TAXONOMY[predicted_code]["track"]
                assigned_track = TAXONOMY.get(assigned_code, {}).get("track", "")
                if pred_track == assigned_track:
                    verdict = "reclassify_same_track"
                else:
                    verdict = "reclassify_different_track"
            else:
                verdict = "unparseable"

            return {
                "id": rid,
                "assigned_code": assigned_code,
                "assigned_label": TAXONOMY.get(assigned_code, {}).get("label", "?"),
                "predicted_code": predicted_code,
                "predicted_label": TAXONOMY.get(predicted_code, {}).get("label", "?"),
                "confidence": confidence,
                "reasoning": reasoning,
                "verdict": verdict,
                "track": record.get("track", ""),
            }

        except Exception as e:
            if attempt == 2:
                return {
                    "id": rid,
                    "assigned_code": assigned_code,
                    "assigned_label": TAXONOMY.get(assigned_code, {}).get("label", "?"),
                    "predicted_code": "ERROR",
                    "predicted_label": "",
                    "confidence": "",
                    "reasoning": str(e)[:200],
                    "verdict": "error",
                    "track": record.get("track", ""),
                }
            await asyncio.sleep(2 ** (attempt + 1))


# ── Main ──

async def run_cross_validation(records: list[dict], resume: bool = False):
    """Run cross-validation on all records."""
    client = openai.AsyncOpenAI(
        api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL
    )
    semaphore = asyncio.Semaphore(CONCURRENCY)

    # Resume support
    done_ids = load_existing_results() if resume else set()
    remaining = [r for r in records if r.get("id", "") not in done_ids]

    print(f"Total records: {len(records)}")
    print(f"Already done: {len(done_ids)}")
    print(f"Remaining: {len(remaining)}")
    print(f"Model: {SUBJECT_MODEL}")
    print(f"Concurrency: {CONCURRENCY}")

    if not remaining:
        print("Nothing to do.")
        return

    # Open output file (append mode for resume)
    mode = "a" if resume and done_ids else "w"
    outf = open(RESULTS_FILE, mode)

    done = 0
    start = time.time()

    # Process in batches
    batch_size = CONCURRENCY * 3
    for batch_start in range(0, len(remaining), batch_size):
        batch = remaining[batch_start:batch_start + batch_size]
        results = await asyncio.gather(*[
            classify_record(client, semaphore, r) for r in batch
        ])

        for result in results:
            outf.write(json.dumps(result, ensure_ascii=False) + "\n")
            done += 1

        outf.flush()

        if done % 100 == 0 or done == len(remaining):
            elapsed = time.time() - start
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(remaining) - done) / rate if rate > 0 else 0
            print(f"  Progress: {done}/{len(remaining)} "
                  f"[{elapsed:.0f}s, {rate:.1f}/s, ETA {eta:.0f}s]", flush=True)

    outf.close()
    print(f"\nDone. Results in {RESULTS_FILE}")


def generate_report():
    """Generate a summary report from cross-validation results."""
    if not RESULTS_FILE.exists():
        print("No results file found. Run cross-validation first.")
        return

    results = []
    with open(RESULTS_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                results.append(json.loads(line))

    total = len(results)
    verdicts = Counter(r["verdict"] for r in results)
    confirmed = verdicts.get("confirmed", 0)
    agreement_rate = confirmed / total if total > 0 else 0

    # By track
    track_stats = defaultdict(lambda: {"total": 0, "confirmed": 0})
    for r in results:
        track = r.get("track", "unknown")
        track_stats[track]["total"] += 1
        if r["verdict"] == "confirmed":
            track_stats[track]["confirmed"] += 1

    # Reclassifications
    reclassifications = [r for r in results if r["verdict"].startswith("reclassify")]

    # Most common reclassification patterns
    reclass_patterns = Counter()
    for r in reclassifications:
        pattern = f"{r['assigned_code']}→{r['predicted_code']}"
        reclass_patterns[pattern] += 1

    # Write report
    lines = [
        "# QC7: Cross-Validation Report",
        "",
        f"**Date:** {time.strftime('%Y-%m-%d')}",
        f"**Scope:** {total} training corpus records",
        f"**Classifier:** {SUBJECT_MODEL} (via MindRouter)",
        f"**Method:** Blind classification — taxonomy code stripped, scenario + analysis presented, model selects code from track options + distractors",
        "",
        "## Summary",
        "",
        f"| Metric | Count | Rate |",
        f"|--------|-------|------|",
        f"| Total records | {total} | — |",
        f"| **Confirmed** (agree with assigned code) | {confirmed} | **{agreement_rate:.1%}** |",
        f"| Reclassify (same track) | {verdicts.get('reclassify_same_track', 0)} | {verdicts.get('reclassify_same_track', 0)/total:.1%} |",
        f"| Reclassify (different track) | {verdicts.get('reclassify_different_track', 0)} | {verdicts.get('reclassify_different_track', 0)/total:.1%} |",
        f"| Unparseable | {verdicts.get('unparseable', 0)} | {verdicts.get('unparseable', 0)/total:.1%} |",
        f"| Error | {verdicts.get('error', 0)} | {verdicts.get('error', 0)/total:.1%} |",
        "",
        "## Agreement by Track",
        "",
        f"| Track | Total | Confirmed | Rate |",
        f"|-------|-------|-----------|------|",
    ]

    for track in sorted(track_stats):
        s = track_stats[track]
        rate = s["confirmed"] / s["total"] if s["total"] > 0 else 0
        lines.append(f"| {track} | {s['total']} | {s['confirmed']} | {rate:.1%} |")

    lines.extend([
        "",
        "## Most Common Reclassifications",
        "",
        f"| Pattern | Count | Assigned | Predicted |",
        f"|---------|-------|----------|-----------|",
    ])

    for pattern, count in reclass_patterns.most_common(20):
        assigned, predicted = pattern.split("→")
        a_label = TAXONOMY.get(assigned, {}).get("label", "?")
        p_label = TAXONOMY.get(predicted, {}).get("label", "?")
        lines.append(f"| {pattern} | {count} | {a_label} | {p_label} |")

    # Low-confidence confirmations (might still be wrong)
    low_conf = [r for r in results if r["verdict"] == "confirmed" and r["confidence"] == "low"]
    if low_conf:
        lines.extend([
            "",
            f"## Low-Confidence Confirmations ({len(low_conf)} records)",
            "",
            "These records were classified to the same code but with low confidence — consider spot-checking.",
            "",
        ])
        for r in low_conf[:20]:
            lines.append(f"- {r['id']} ({r['assigned_code']}: {r['assigned_label']}): {r['reasoning'][:100]}")

    report_text = "\n".join(lines) + "\n"

    with open(REPORT_FILE, "w") as f:
        f.write(report_text)
    print(f"Report written to {REPORT_FILE}")

    # Also print summary
    print(f"\n{'='*60}")
    print(f"QC7 CROSS-VALIDATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total: {total}")
    print(f"Confirmed: {confirmed} ({agreement_rate:.1%})")
    print(f"Reclassify (same track): {verdicts.get('reclassify_same_track', 0)}")
    print(f"Reclassify (different track): {verdicts.get('reclassify_different_track', 0)}")
    print(f"Previous QC4 agreement: 71.7%")
    print(f"Current QC7 agreement: {agreement_rate:.1%}")


def main():
    parser = argparse.ArgumentParser(description="QC7: Cross-validation with Nemotron")
    parser.add_argument("--limit", type=int, help="Limit number of records")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--report", action="store_true", help="Generate report from results")
    args = parser.parse_args()

    if args.report:
        generate_report()
        return

    records = load_training_corpus()
    if args.limit:
        random.seed(42)
        random.shuffle(records)
        records = records[:args.limit]

    asyncio.run(run_cross_validation(records, resume=args.resume))
    generate_report()


if __name__ == "__main__":
    main()
