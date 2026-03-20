"""
Generate synthetic training examples for the Good Thinking Bot corpus
using MindRouter (University of Idaho campus HPC).

Generates 5 domain variations for each of the 13 E1 cognitive bias codes
that already have anchor examples, using qwen/qwen3.5-400b via the
OpenAI-compatible MindRouter API.
"""

import asyncio
import json
import os
import random
import re
import sys
import time
from functools import partial
from pathlib import Path

# Force unbuffered output
print = partial(print, flush=True)

from dotenv import load_dotenv

# ── Load environment ─────────────────────────────────────────────────────────

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

API_KEY = os.getenv("MINDROUTER_API_KEY")
BASE_URL = os.getenv("MINDROUTER_BASE_URL", "https://mindrouter.uidaho.edu/v1")
MODEL = "qwen/qwen3.5-400b"
MAX_CONCURRENT = 4

# ── Target codes and domains ─────────────────────────────────────────────────

TARGET_CODES = [
    "E1.1", "E1.2", "E1.3", "E1.4", "E1.5", "E1.6", "E1.7",
    "E1.8", "E1.9", "E1.10", "E1.11", "E1.12", "E1.20",
]

DOMAINS = [
    ("workplace", "a corporate office or professional workplace"),
    ("school", "a high school or university classroom setting"),
    ("healthcare", "a hospital, clinic, or public health context"),
    ("sports", "a sports team, athletic competition, or coaching scenario"),
    ("politics", "a local, national, or international political context"),
]

DIFFICULTY_TIERS = ["drill", "what_if", "puzzle"]

# ── Taxonomy definitions (imported from taxonomy.py) ─────────────────────────

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

# ── Load anchor examples ─────────────────────────────────────────────────────

ANCHORS_PATH = Path(__file__).resolve().parent / "output" / "anchors.jsonl"
OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "synthetic_E1_mindrouter.jsonl"


def load_anchors_by_code() -> dict[str, list[dict]]:
    """Load anchor examples grouped by taxonomy_code."""
    anchors: dict[str, list[dict]] = {}
    with open(ANCHORS_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            code = record["taxonomy_code"]
            anchors.setdefault(code, []).append(record)
    return anchors


def build_prompt(
    taxonomy_code: str,
    taxonomy_entry: dict,
    anchor_examples: list[dict],
    domain_name: str,
    domain_description: str,
    difficulty_tier: str,
    sequence_num: int,
) -> str:
    """Build the generation prompt with few-shot examples."""
    # Pick 2 anchor examples for few-shot
    few_shot = random.sample(anchor_examples, min(2, len(anchor_examples)))

    few_shot_text = ""
    for i, ex in enumerate(few_shot, 1):
        few_shot_text += f"\n--- Example {i} ---\n{json.dumps(ex, indent=2)}\n"

    new_id = f"{taxonomy_code}-S{sequence_num:03d}"

    prompt = f"""You are generating training data for a critical thinking education game.
Produce a single JSON object (no markdown, no explanation, ONLY valid JSON) that matches the exact schema shown in the examples below.

## Taxonomy Code: {taxonomy_code}
- Label: {taxonomy_entry['label']}
- Description: {taxonomy_entry['description']}
- Pattern type: {taxonomy_entry['pattern_type']}
- Track: {taxonomy_entry['track']}

## Domain Setting
Create a scenario set in: {domain_description}
The scenario must be realistic, specific, and clearly illustrate {taxonomy_entry['label']} in a {domain_name} context.

## Difficulty Tier: {difficulty_tier}
- "drill": Straightforward example where the bias is clearly present and identifiable
- "what_if": More nuanced example that connects to related concepts or has complicating factors
- "puzzle": Genuinely challenging case where the bias interacts with other reasoning patterns

## Few-Shot Reference Examples
These show the exact JSON structure and quality level expected:
{few_shot_text}

## Requirements
1. Output ONLY a single valid JSON object — no markdown fences, no commentary
2. Use id: "{new_id}"
3. Set taxonomy_code: "{taxonomy_code}"
4. Set taxonomy_label: "{taxonomy_entry['label']}"
5. Set track: "{taxonomy_entry['track']}"
6. Set pattern_type: "{taxonomy_entry['pattern_type']}"
7. Set difficulty_tier: "{difficulty_tier}"
8. The scenario must be set in {domain_description} — NOT in a fantasy game world
9. Set source.type to "synthetic_verified"
10. Set source.source_material to "MindRouter qwen3.5-400b synthetic generation"
11. Set source.original_id to null
12. Include all fields: scenario (context, text, speaker_context), structure (pattern_name, pattern_description, formal_form, why_wrong, why_right, related_patterns, counterpoint), assessment (identification_prompt, rubric with levels 0-4, follow_up_if_wrong, follow_up_if_right), game_hooks (npc_personality, npc_dialogue_seed, resolution_path)
13. Make the scenario realistic and specific to the {domain_name} domain
14. The game_hooks should translate the real-world scenario into an NPC interaction

Generate the JSON object now:"""

    return prompt


# ── Async generation ─────────────────────────────────────────────────────────

try:
    from openai import AsyncOpenAI
except ImportError:
    print("Installing openai package...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import AsyncOpenAI


async def generate_one(
    client: AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    taxonomy_code: str,
    taxonomy_entry: dict,
    anchor_examples: list[dict],
    domain_name: str,
    domain_description: str,
    difficulty_tier: str,
    sequence_num: int,
) -> dict | None:
    """Generate a single synthetic example via MindRouter."""
    prompt = build_prompt(
        taxonomy_code, taxonomy_entry, anchor_examples,
        domain_name, domain_description, difficulty_tier, sequence_num,
    )

    async with semaphore:
        try:
            response = await asyncio.wait_for(
                client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": "You are a JSON generation assistant. Output only valid JSON, no markdown fences or commentary."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.8,
                    max_tokens=4096,
                    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                ),
                timeout=180,  # 3 minute timeout per call
            )
            msg = response.choices[0].message
            # Qwen3.5 thinking models may put content in reasoning_content
            raw = msg.content or getattr(msg, "reasoning_content", None) or ""
            raw = raw.strip()

            # Strip markdown fences if present
            if raw.startswith("```"):
                raw = re.sub(r"^```(?:json)?\s*\n?", "", raw)
                raw = re.sub(r"\n?```\s*$", "", raw)

            # Strip any <think>...</think> tags (Qwen thinking mode)
            raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()

            record = json.loads(raw)

            # Basic validation
            required_top = ["id", "taxonomy_code", "taxonomy_label", "track",
                            "pattern_type", "difficulty_tier", "scenario",
                            "structure", "assessment", "game_hooks", "source"]
            missing = [k for k in required_top if k not in record]
            if missing:
                print(f"  INVALID {taxonomy_code}/{domain_name}: missing keys {missing}")
                return None

            # Validate nested structures
            for sub_key, sub_fields in [
                ("scenario", ["context", "text"]),
                ("structure", ["pattern_name", "pattern_description"]),
                ("assessment", ["identification_prompt", "rubric"]),
                ("game_hooks", ["npc_personality", "npc_dialogue_seed", "resolution_path"]),
                ("source", ["type", "source_material"]),
            ]:
                if not isinstance(record.get(sub_key), dict):
                    print(f"  INVALID {taxonomy_code}/{domain_name}: {sub_key} not a dict")
                    return None
                sub_missing = [f for f in sub_fields if f not in record[sub_key]]
                if sub_missing:
                    print(f"  INVALID {taxonomy_code}/{domain_name}: {sub_key} missing {sub_missing}")
                    return None

            # Validate rubric has 5 levels
            rubric = record["assessment"].get("rubric", [])
            if not isinstance(rubric, list) or len(rubric) < 3:
                print(f"  INVALID {taxonomy_code}/{domain_name}: rubric has {len(rubric)} levels (need >=3)")
                return None

            return record

        except asyncio.TimeoutError:
            print(f"  TIMEOUT {taxonomy_code}/{domain_name}: exceeded 180s")
            return None
        except json.JSONDecodeError as e:
            print(f"  JSON ERROR {taxonomy_code}/{domain_name}: {e}")
            if raw:
                print(f"    Raw start: {raw[:200]}...")
            return None
        except Exception as e:
            print(f"  API ERROR {taxonomy_code}/{domain_name}: {e}")
            return None


async def main():
    print(f"Loading anchors from {ANCHORS_PATH}...")
    anchors_by_code = load_anchors_by_code()

    # Verify we have anchors for all target codes
    for code in TARGET_CODES:
        if code not in anchors_by_code:
            print(f"  WARNING: No anchor found for {code}")

    # Also load a pool of diverse anchors for extra few-shot variety
    all_e1_anchors = []
    for code in TARGET_CODES:
        all_e1_anchors.extend(anchors_by_code.get(code, []))
    print(f"Loaded {len(all_e1_anchors)} E1 anchor examples across {len(TARGET_CODES)} codes")

    client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    # Build all tasks
    tasks = []
    task_labels = []
    seq_counter: dict[str, int] = {}

    for code in TARGET_CODES:
        entry = TAXONOMY.get(code)
        if not entry:
            print(f"  WARNING: {code} not in TAXONOMY, skipping")
            continue
        code_anchors = anchors_by_code.get(code, [])
        if not code_anchors:
            print(f"  WARNING: No anchors for {code}, skipping")
            continue

        for i, (domain_name, domain_desc) in enumerate(DOMAINS):
            tier = DIFFICULTY_TIERS[i % len(DIFFICULTY_TIERS)]
            seq = seq_counter.get(code, 1)
            seq_counter[code] = seq + 1

            tasks.append(generate_one(
                client, semaphore, code, entry, code_anchors,
                domain_name, domain_desc, tier, seq,
            ))
            task_labels.append(f"{code}/{domain_name}/{tier}")

    total = len(tasks)
    print(f"\nGenerating {total} synthetic examples ({len(TARGET_CODES)} codes x {len(DOMAINS)} domains)...")
    print(f"Model: {MODEL} | Concurrency: {MAX_CONCURRENT}")
    print("-" * 60)

    start_time = time.time()

    # Run with progress tracking
    valid_results = []
    failed = 0

    # Process in batches to show progress
    BATCH_SIZE = 8
    for batch_start in range(0, total, BATCH_SIZE):
        batch_end = min(batch_start + BATCH_SIZE, total)
        batch_tasks = tasks[batch_start:batch_end]
        batch_labels = task_labels[batch_start:batch_end]

        results = await asyncio.gather(*batch_tasks, return_exceptions=True)

        for label, result in zip(batch_labels, results):
            if isinstance(result, Exception):
                print(f"  EXCEPTION {label}: {result}")
                failed += 1
            elif result is None:
                failed += 1
            else:
                valid_results.append(result)
                print(f"  OK {label}")

        done = batch_end
        elapsed = time.time() - start_time
        print(f"  Progress: {done}/{total} ({len(valid_results)} valid, {failed} failed) [{elapsed:.1f}s]")

    # Write results
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        for record in valid_results:
            f.write(json.dumps(record) + "\n")

    elapsed = time.time() - start_time
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total attempted:  {total}")
    print(f"Valid generated:  {len(valid_results)}")
    print(f"Failed:           {failed}")
    print(f"Success rate:     {len(valid_results)/total*100:.1f}%" if total else "N/A")
    print(f"Time elapsed:     {elapsed:.1f}s")
    print(f"Output file:      {OUTPUT_PATH}")

    # Coverage summary
    codes_covered = set()
    for r in valid_results:
        codes_covered.add(r.get("taxonomy_code", "?"))
    print(f"Codes covered:    {len(codes_covered)}/{len(TARGET_CODES)}")

    # Tier distribution
    tier_counts: dict[str, int] = {}
    for r in valid_results:
        t = r.get("difficulty_tier", "?")
        tier_counts[t] = tier_counts.get(t, 0) + 1
    print(f"Tier distribution: {dict(sorted(tier_counts.items()))}")


if __name__ == "__main__":
    asyncio.run(main())
