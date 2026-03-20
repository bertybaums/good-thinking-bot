#!/usr/bin/env python3
"""
Cross-validate anchor examples using MindRouter (qwen3.5-400b).

For each anchor, strips the taxonomy code and sends ONLY the scenario
to MindRouter for blind classification. Compares predictions to actual labels.

Usage:
    python run_cross_validate_anchors.py
"""

import asyncio
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

import openai

# ── Config ───────────────────────────────────────────────────────────────────

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = os.environ.get(
    "MINDROUTER_BASE_URL", "https://mindrouter.uidaho.edu/v1"
)
MODEL = "qwen/qwen3.5-400b"
MAX_CONCURRENT = 4
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2.0

ANCHORS_PATH = Path(__file__).resolve().parent / "output" / "anchors.jsonl"

# ── Build taxonomy reference from taxonomy.py ────────────────────────────────

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

TAXONOMY_REF = "\n".join(
    f"  {code}: {entry['label']} — {entry['description']}"
    for code, entry in TAXONOMY.items()
)

# ── Classification prompt ────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are an expert classifier of reasoning patterns. You will be given a scenario \
from a game-based learning system that teaches critical thinking, logic, decision \
theory, and economics. Your job is to identify which reasoning pattern the scenario \
primarily demonstrates.

You must respond with a JSON object containing exactly three fields:
- "predicted_code": the taxonomy code (e.g. "A7.1")
- "confidence": a number between 0 and 1
- "reasoning": a brief explanation (1-2 sentences)

Do NOT include any text outside the JSON object."""

USER_PROMPT_TEMPLATE = """\
Below is a scenario. Classify which reasoning pattern it primarily demonstrates.

SCENARIO:
{scenario_text}

TAXONOMY OF REASONING PATTERNS:
{taxonomy_ref}

Respond with JSON only: {{"predicted_code": "...", "confidence": ..., "reasoning": "..."}}"""


def build_scenario_text(record: dict) -> str:
    """Extract the scenario text from a record, combining context + text."""
    scenario = record.get("scenario", {})
    parts = []
    if scenario.get("context"):
        parts.append(scenario["context"])
    if scenario.get("text"):
        parts.append(scenario["text"])
    if scenario.get("speaker_context"):
        parts.append(f"[Speaker context: {scenario['speaker_context']}]")
    return "\n\n".join(parts)


# ── Async API calls ─────────────────────────────────────────────────────────

async def classify_record(
    client: openai.AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    record: dict,
    record_idx: int,
    progress_counter: dict,
    total: int,
) -> dict:
    """Classify a single record via MindRouter."""
    scenario_text = build_scenario_text(record)
    user_prompt = USER_PROMPT_TEMPLATE.format(
        scenario_text=scenario_text,
        taxonomy_ref=TAXONOMY_REF,
    )

    result = {
        "id": record["id"],
        "actual_code": record["taxonomy_code"],
        "actual_label": record.get("taxonomy_label", ""),
        "track": record.get("track", ""),
        "predicted_code": None,
        "confidence": None,
        "reasoning": None,
        "error": None,
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with semaphore:
                response = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    max_tokens=512,
                    temperature=0.2,
                    response_format={"type": "json_object"},
                    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                )

            content = response.choices[0].message.content or ""

            # Parse JSON response
            parsed = json.loads(content)
            result["predicted_code"] = parsed.get("predicted_code", "").strip()
            result["confidence"] = float(parsed.get("confidence", 0))
            result["reasoning"] = parsed.get("reasoning", "")
            break

        except json.JSONDecodeError:
            # Try to extract JSON from response
            try:
                start = content.index("{")
                end = content.rindex("}") + 1
                parsed = json.loads(content[start:end])
                result["predicted_code"] = parsed.get("predicted_code", "").strip()
                result["confidence"] = float(parsed.get("confidence", 0))
                result["reasoning"] = parsed.get("reasoning", "")
                break
            except (ValueError, json.JSONDecodeError):
                if attempt == MAX_RETRIES:
                    result["error"] = f"JSON parse failed: {content[:200]}"

        except (openai.RateLimitError, openai.APITimeoutError) as e:
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF_BASE ** attempt
                await asyncio.sleep(wait)
            else:
                result["error"] = str(e)

        except Exception as e:
            if attempt == MAX_RETRIES:
                result["error"] = str(e)
            else:
                await asyncio.sleep(RETRY_BACKOFF_BASE ** attempt)

    # Update progress
    progress_counter["done"] += 1
    done = progress_counter["done"]
    if done % 10 == 0 or done == total:
        print(f"  Progress: {done}/{total} records classified")

    return result


async def run_cross_validation(records: list[dict]) -> list[dict]:
    """Run cross-validation on all records with concurrency control."""
    client = openai.AsyncOpenAI(
        api_key=MINDROUTER_API_KEY,
        base_url=MINDROUTER_BASE_URL,
    )
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    progress = {"done": 0}
    total = len(records)

    tasks = [
        classify_record(client, semaphore, rec, i, progress, total)
        for i, rec in enumerate(records)
    ]

    results = await asyncio.gather(*tasks)
    await client.close()
    return list(results)


# ── Analysis ─────────────────────────────────────────────────────────────────

def analyze_results(results: list[dict]) -> None:
    """Print cross-validation analysis."""
    # Filter out errors
    errors = [r for r in results if r["error"]]
    valid = [r for r in results if not r["error"]]

    print("\n" + "=" * 70)
    print("CROSS-VALIDATION RESULTS: Anchors vs MindRouter (qwen3.5-400b)")
    print("=" * 70)

    if errors:
        print(f"\n  Errors: {len(errors)} records failed API calls")
        for e in errors[:5]:
            print(f"    {e['id']}: {e['error'][:80]}")
        if len(errors) > 5:
            print(f"    ... and {len(errors) - 5} more")

    if not valid:
        print("\n  No valid results to analyze.")
        return

    # Overall agreement
    agree = sum(1 for r in valid if r["predicted_code"] == r["actual_code"])
    total = len(valid)
    rate = agree / total * 100
    print(f"\n  OVERALL AGREEMENT: {agree}/{total} ({rate:.1f}%)")

    # Agreement by track
    print(f"\n  AGREEMENT BY TRACK:")
    track_stats = defaultdict(lambda: {"agree": 0, "total": 0})
    for r in valid:
        track = r["track"]
        track_stats[track]["total"] += 1
        if r["predicted_code"] == r["actual_code"]:
            track_stats[track]["agree"] += 1

    for track in sorted(track_stats.keys()):
        s = track_stats[track]
        pct = s["agree"] / s["total"] * 100 if s["total"] else 0
        print(f"    {track:30s}  {s['agree']:3d}/{s['total']:3d}  ({pct:5.1f}%)")

    # Confusion pairs
    print(f"\n  TOP 10 CONFUSION PAIRS (actual → predicted):")
    confusions = Counter()
    for r in valid:
        if r["predicted_code"] != r["actual_code"]:
            actual_label = TAXONOMY.get(r["actual_code"], {}).get("label", "?")
            pred_label = TAXONOMY.get(r["predicted_code"], {}).get("label", "?")
            key = (
                f"{r['actual_code']} ({actual_label})",
                f"{r['predicted_code']} ({pred_label})",
            )
            confusions[key] += 1

    for (actual, pred), count in confusions.most_common(10):
        print(f"    {actual:45s} → {pred:45s}  [{count}x]")

    # High-confidence errors
    hc_errors = [
        r for r in valid
        if r["predicted_code"] != r["actual_code"]
        and r["confidence"] is not None
        and r["confidence"] > 0.8
    ]
    print(f"\n  HIGH-CONFIDENCE ERRORS (confidence > 0.8 but wrong): {len(hc_errors)}")
    if hc_errors:
        hc_errors.sort(key=lambda r: -(r["confidence"] or 0))
        for r in hc_errors:
            actual_label = TAXONOMY.get(r["actual_code"], {}).get("label", "?")
            pred_label = TAXONOMY.get(r["predicted_code"], {}).get("label", "?")
            print(
                f"    {r['id']:15s}  "
                f"actual={r['actual_code']} ({actual_label})  "
                f"predicted={r['predicted_code']} ({pred_label})  "
                f"conf={r['confidence']:.2f}"
            )
            if r["reasoning"]:
                print(f"      Reasoning: {r['reasoning'][:120]}")

    # Summary stats
    if valid:
        confidences = [r["confidence"] for r in valid if r["confidence"] is not None]
        if confidences:
            avg_conf = sum(confidences) / len(confidences)
            avg_conf_correct = [
                r["confidence"] for r in valid
                if r["predicted_code"] == r["actual_code"] and r["confidence"] is not None
            ]
            avg_conf_wrong = [
                r["confidence"] for r in valid
                if r["predicted_code"] != r["actual_code"] and r["confidence"] is not None
            ]
            print(f"\n  CONFIDENCE STATS:")
            print(f"    Mean confidence (all):     {avg_conf:.3f}")
            if avg_conf_correct:
                print(f"    Mean confidence (correct): {sum(avg_conf_correct)/len(avg_conf_correct):.3f}")
            if avg_conf_wrong:
                print(f"    Mean confidence (wrong):   {sum(avg_conf_wrong)/len(avg_conf_wrong):.3f}")

    print("\n" + "=" * 70)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("Cross-validating anchor examples via MindRouter (qwen3.5-400b)")
    print(f"  Anchors file: {ANCHORS_PATH}")
    print(f"  Model: {MODEL}")
    print(f"  Max concurrent: {MAX_CONCURRENT}")

    # Load records
    records = []
    with open(ANCHORS_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    print(f"  Loaded {len(records)} records")
    print(f"  Taxonomy codes: {len(TAXONOMY)}")
    print()

    # Run cross-validation
    start = time.time()
    results = asyncio.run(run_cross_validation(records))
    elapsed = time.time() - start

    print(f"\n  Completed in {elapsed:.1f}s ({elapsed/len(records):.1f}s per record)")

    # Save raw results
    output_path = ANCHORS_PATH.parent / "cross_val_results.jsonl"
    with open(output_path, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    print(f"  Raw results saved to {output_path}")

    # Analyze
    analyze_results(results)


if __name__ == "__main__":
    main()
