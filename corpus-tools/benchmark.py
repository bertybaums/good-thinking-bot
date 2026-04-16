#!/usr/bin/env python3
"""
Benchmark: assess a model's reasoning capacity against the anchor corpus.

Presents each anchor's scenario + identification_prompt to the subject model,
then uses a judge model to score the response against the 0-4 rubric.

Three evaluation modes:
  1. IDENTIFY  — open-ended: "What's going on here?" (scored by judge)
  2. CLASSIFY  — pick the taxonomy code from a list (auto-scored)
  3. EXPLAIN   — identify AND explain the mechanism (scored by judge)

Usage:
    python benchmark.py --subject openai/gpt-oss-20b
    python benchmark.py --subject openai/gpt-oss-20b --mode classify --limit 20
    python benchmark.py --subject openai/gpt-oss-120b --mode all
    python benchmark.py --report output/benchmark_gpt-oss-20b.jsonl
"""

import argparse
import asyncio
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

import openai

# ── Config ───────────────────────────────────────────────────────────────────

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"

# Concurrency limits by model
MODEL_CONCURRENCY = {
    "openai/gpt-oss-20b": 8,
    "openai/gpt-oss-120b": 8,
    "Nemotron-3-Super-120b": 8,
    "qwen2.5:7b": 8,
    "qwen/qwen3.5-400b": 4,
    "google/gemma-4-26b": 8,
    "google/gemma-4-31b": 8,
}

JUDGE_MODEL = "qwen/qwen3.5-122b"
JUDGE_CONCURRENCY = 4

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
ANCHORS_FILE = OUTPUT_DIR / "anchors.jsonl"
ANCHORS_PHIL4040_FILE = OUTPUT_DIR / "anchors_phil4040.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

# ── Load Anchors ─────────────────────────────────────────────────────────────

def load_anchors(limit: int | None = None, source: str | None = None) -> list[dict]:
    """Load anchors from default anchor files, or from a custom JSONL if `source` is given."""
    records = []
    if source:
        with open(source) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
                    if limit and len(records) >= limit:
                        return records
        return records
    for anchor_file in [ANCHORS_FILE, ANCHORS_PHIL4040_FILE]:
        if not anchor_file.exists():
            continue
        with open(anchor_file) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
                    if limit and len(records) >= limit:
                        return records
    return records


# ── Evaluation Prompts ───────────────────────────────────────────────────────

def build_identify_prompt(anchor: dict) -> str:
    """Open-ended: present scenario, ask what's going on."""
    s = anchor["scenario"]
    a = anchor["assessment"]
    return f"""Read this scenario carefully, then answer the question.

**Setting:** {s['context']}

**What happened:** {s['text']}

**Question:** {a['identification_prompt']}

Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."""


def build_classify_prompt(anchor: dict) -> str:
    """Multiple-choice: pick the taxonomy code."""
    s = anchor["scenario"]
    code = anchor["taxonomy_code"]
    track = anchor.get("track", "")

    # Build options: the correct code + 4 distractors from the same track
    track_codes = [c for c, v in TAXONOMY.items() if v["track"] == track and c != code]
    import random
    distractors = random.sample(track_codes, min(4, len(track_codes)))
    options = sorted([code] + distractors)
    options_text = "\n".join(f"  {c}: {TAXONOMY[c]['label']}" for c in options)

    return f"""Read this scenario and identify the PRIMARY reasoning pattern from the options below.

**Setting:** {s['context']}

**What happened:** {s['text']}

**Options:**
{options_text}

Reply with ONLY the code (e.g., "A7.1"). No explanation needed."""


def build_explain_prompt(anchor: dict) -> str:
    """Full explanation: identify, name, and explain the mechanism."""
    s = anchor["scenario"]
    a = anchor["assessment"]
    return f"""Read this scenario carefully and provide a complete analysis.

**Setting:** {s['context']}

**What happened:** {s['text']}

**Your task:**
1. What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?
2. Name it precisely.
3. Explain the mechanism: what exactly makes this reasoning good or bad?
4. What would be the correct approach in this situation?
5. Are there edge cases where this pattern might be legitimate?

Be thorough but concise."""


# ── Judge Prompt ─────────────────────────────────────────────────────────────

def build_judge_prompt(anchor: dict, subject_response: str, mode: str) -> str:
    """Ask the judge to score the subject's response against the rubric."""
    rubric = anchor["assessment"]["rubric"]
    rubric_text = "\n".join(
        f"  Level {r['level']}: {r['description']}" for r in rubric
    )

    return f"""You are scoring a student's response to a reasoning assessment.

**The correct answer:**
- Taxonomy code: {anchor['taxonomy_code']}
- Pattern: {anchor['taxonomy_label']}
- Key explanation: {anchor['structure']['pattern_description']}

**Rubric (0-4 scale):**
{rubric_text}

**Student's response:**
{subject_response}

**Your task:**
Score the response on the 0-4 rubric. Consider:
- Does the student identify the correct pattern (even without naming it formally)?
- Does the student explain the mechanism correctly?
- Does the student note edge cases or counterpoints?

Return ONLY valid JSON:
{{"score": 0-4, "reasoning": "brief explanation of your scoring"}}"""


# ── API Calls ────────────────────────────────────────────────────────────────

async def call_model(
    client: openai.AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    model: str,
    prompt: str,
    max_tokens: int = 1024,
    temperature: float = 0.3,
) -> str:
    """Call a model with retry logic."""
    for attempt in range(3):
        try:
            async with semaphore:
                resp = await client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens,
                    temperature=temperature,
                    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                )
            return resp.choices[0].message.content or ""
        except Exception as e:
            if attempt == 2:
                return f"[ERROR: {e}]"
            await asyncio.sleep(2 ** (attempt + 1))
    return "[ERROR: max retries]"


# ── Benchmark Runner ─────────────────────────────────────────────────────────

async def run_benchmark(
    subject_model: str,
    anchors: list[dict],
    mode: str = "identify",
) -> list[dict]:
    """Run the benchmark and return scored results."""
    client = openai.AsyncOpenAI(
        api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL
    )

    subject_concurrency = MODEL_CONCURRENCY.get(subject_model, 4)
    subject_sem = asyncio.Semaphore(subject_concurrency)
    judge_sem = asyncio.Semaphore(JUDGE_CONCURRENCY)

    results = []
    done = 0
    start = time.time()

    async def evaluate_one(anchor: dict) -> dict:
        nonlocal done

        # Step 1: Get subject response
        if mode == "classify":
            prompt = build_classify_prompt(anchor)
        elif mode == "explain":
            prompt = build_explain_prompt(anchor)
        else:
            prompt = build_identify_prompt(anchor)

        subject_response = await call_model(
            client, subject_sem, subject_model, prompt,
            max_tokens=1024 if mode != "classify" else 50,
            temperature=0.3,
        )

        # Step 2: Score
        if mode == "classify":
            # Auto-score: extract the code from response
            predicted = subject_response.strip().split()[0].strip("()[]\"'.,")
            correct = anchor["taxonomy_code"]
            score = 4 if predicted == correct else 0
            judge_reasoning = f"Predicted: {predicted}, Correct: {correct}"
        else:
            # Judge scores the response
            judge_prompt = build_judge_prompt(anchor, subject_response, mode)
            judge_response = await call_model(
                client, judge_sem, JUDGE_MODEL, judge_prompt,
                max_tokens=200, temperature=0.1,
            )
            try:
                parsed = json.loads(judge_response)
                score = int(parsed.get("score", 0))
                judge_reasoning = parsed.get("reasoning", "")
            except (json.JSONDecodeError, ValueError):
                score = -1
                judge_reasoning = f"Parse error: {judge_response[:200]}"

        done += 1
        if done % 10 == 0:
            elapsed = time.time() - start
            print(f"  Progress: {done}/{len(anchors)} [{elapsed:.0f}s]", flush=True)

        return {
            "id": anchor["id"],
            "taxonomy_code": anchor["taxonomy_code"],
            "taxonomy_label": anchor["taxonomy_label"],
            "track": anchor.get("track", ""),
            "difficulty_tier": anchor.get("difficulty_tier", ""),
            "pattern_type": anchor.get("pattern_type", ""),
            "mode": mode,
            "subject_model": subject_model,
            "subject_response": subject_response[:2000],
            "score": score,
            "judge_reasoning": judge_reasoning,
        }

    # Process in batches to avoid overwhelming the API
    batch_size = subject_concurrency * 2
    for batch_start in range(0, len(anchors), batch_size):
        batch = anchors[batch_start : batch_start + batch_size]
        batch_results = await asyncio.gather(*[evaluate_one(a) for a in batch])
        results.extend(batch_results)

    return results


# ── Reporting ────────────────────────────────────────────────────────────────

def print_report(results: list[dict], subject_model: str):
    """Print a comprehensive benchmark report."""
    valid = [r for r in results if r["score"] >= 0]
    if not valid:
        print("No valid results to report.")
        return

    scores = [r["score"] for r in valid]
    mean_score = sum(scores) / len(scores)

    print(f"\n{'='*70}")
    print(f"BENCHMARK REPORT: {subject_model}")
    print(f"{'='*70}")
    print(f"Records evaluated: {len(valid)}")
    print(f"Mean score: {mean_score:.2f} / 4.00")
    print(f"Score distribution: {Counter(scores)}")

    # By track
    print(f"\n{'Track':<35} {'Mean':>6} {'n':>5} {'0':>4} {'1':>4} {'2':>4} {'3':>4} {'4':>4}")
    print("-" * 70)
    track_scores = defaultdict(list)
    for r in valid:
        track_scores[r["track"]].append(r["score"])
    for track in sorted(track_scores):
        s = track_scores[track]
        dist = Counter(s)
        mean = sum(s) / len(s)
        print(
            f"{track:<35} {mean:>6.2f} {len(s):>5} "
            f"{dist.get(0,0):>4} {dist.get(1,0):>4} {dist.get(2,0):>4} "
            f"{dist.get(3,0):>4} {dist.get(4,0):>4}"
        )

    # By difficulty tier
    print(f"\n{'Tier':<15} {'Mean':>6} {'n':>5}")
    print("-" * 30)
    tier_scores = defaultdict(list)
    for r in valid:
        tier_scores[r["difficulty_tier"]].append(r["score"])
    for tier in ["drill", "what_if", "puzzle"]:
        if tier in tier_scores:
            s = tier_scores[tier]
            print(f"{tier:<15} {sum(s)/len(s):>6.2f} {len(s):>5}")

    # By pattern type
    print(f"\n{'Pattern Type':<15} {'Mean':>6} {'n':>5}")
    print("-" * 30)
    ptype_scores = defaultdict(list)
    for r in valid:
        ptype_scores[r["pattern_type"]].append(r["score"])
    for pt in ["good_tool", "bad_thinking", "dual"]:
        if pt in ptype_scores:
            s = ptype_scores[pt]
            print(f"{pt:<15} {sum(s)/len(s):>6.2f} {len(s):>5}")

    # Worst performers (score 0-1)
    weak = [r for r in valid if r["score"] <= 1]
    if weak:
        print(f"\nWeakest areas (score 0-1, n={len(weak)}):")
        for r in sorted(weak, key=lambda x: x["score"])[:15]:
            print(f"  [{r['score']}] {r['taxonomy_code']}: {r['taxonomy_label']} ({r['difficulty_tier']})")

    # Strongest performers (score 3-4)
    strong = [r for r in valid if r["score"] >= 3]
    if strong:
        print(f"\nStrongest areas (score 3-4, n={len(strong)}):")
        for r in sorted(strong, key=lambda x: -x["score"])[:10]:
            print(f"  [{r['score']}] {r['taxonomy_code']}: {r['taxonomy_label']}")


def load_report(path: Path) -> list[dict]:
    """Load saved benchmark results."""
    results = []
    with open(path) as f:
        for line in f:
            if line.strip():
                results.append(json.loads(line))
    return results


# ── Main ─────────────────────────────────────────────────────────────────────

async def main_async(args):
    anchors = load_anchors(args.limit, source=args.anchors)
    print(f"Loaded {len(anchors)} anchors")
    print(f"Subject model: {args.subject}")
    print(f"Judge model: {JUDGE_MODEL}")
    print(f"Mode: {args.mode}")

    modes = ["identify", "classify", "explain"] if args.mode == "all" else [args.mode]
    all_results = []

    for mode in modes:
        print(f"\n--- Mode: {mode} ---")
        results = await run_benchmark(args.subject, anchors, mode=mode)
        all_results.extend(results)

    # Save results
    model_slug = args.subject.replace("/", "-")
    output_file = OUTPUT_DIR / f"benchmark_{model_slug}.jsonl"
    with open(output_file, "w") as f:
        for r in all_results:
            f.write(json.dumps(r) + "\n")
    print(f"\nResults saved to {output_file}")

    # Print report
    for mode in modes:
        mode_results = [r for r in all_results if r["mode"] == mode]
        print(f"\n{'#'*70}")
        print(f"MODE: {mode.upper()}")
        print(f"{'#'*70}")
        print_report(mode_results, args.subject)


def main():
    parser = argparse.ArgumentParser(description="Benchmark a model against the anchor corpus")
    parser.add_argument("--subject", default="openai/gpt-oss-20b", help="Model to evaluate")
    parser.add_argument("--mode", default="identify", choices=["identify", "classify", "explain", "all"],
                        help="Evaluation mode")
    parser.add_argument("--limit", type=int, help="Limit number of anchors to evaluate")
    parser.add_argument("--anchors", help="Path to alternative anchor JSONL (e.g. output/quick_benchmark_set.jsonl)")
    parser.add_argument("--report", help="Load and display a saved benchmark report")
    args = parser.parse_args()

    if args.report:
        results = load_report(Path(args.report))
        print_report(results, results[0]["subject_model"] if results else "unknown")
        return

    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
