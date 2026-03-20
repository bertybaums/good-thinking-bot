#!/usr/bin/env python3
"""
Sprint 2: Adapt external datasets using MindRouter (qwen3.5-400b).

Enriches Jin fallacy, FOLIO, Corr2Cause, and SemEval propaganda datasets
with full corpus schema fields (structure, assessment, game_hooks).
Uses anchor examples as few-shot demonstrations.
"""

import asyncio
import json
import os
import random
import sys
import time
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

import openai

# ── Config ───────────────────────────────────────────────────────────────────

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"
MODEL = "qwen/qwen3.5-400b"
MAX_CONCURRENT = 4
MAX_RETRIES = 3

DATA_DIR = PROJECT_ROOT / "data" / "external"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
ANCHORS_FILE = OUTPUT_DIR / "anchors.jsonl"

# ── Label → Taxonomy Code Mappings ───────────────────────────────────────────

JIN_MAPPING = {
    "ad hominem": "A7.1",
    "ad populum": "A7.9",
    "appeal to emotion": "A7.7",
    "circular reasoning": "A6.3",
    "equivocation": "A6.5",
    "fallacy of credibility": "A7.6",
    "fallacy of extension": "A7.2",  # straw man / exaggeration
    "fallacy of logic": "A5.1",  # formal fallacies
    "fallacy of relevance": "A7.5",  # red herring / appeal to consequences
    "false causality": "A8.7",
    "false dilemma": "A6.4",
    "faulty generalization": "A8.6",
    "intentional": "A10.1",  # propaganda / manipulation
}

FOLIO_MAPPING = {
    "True": "A2.1",
    "False": "A2.7",
    "Uncertain": "A2.8",
}

CORR2CAUSE_MAPPING = {
    0: "A3.5",  # no causal relation (correlation ≠ causation)
    1: "A3.4",  # causal relation exists
}

PROPAGANDA_MAPPING = {
    "Appeal_to_Authority": "A7.6",
    "Appeal_to_fear-prejudice": "A7.7",
    "Bandwagon": "A7.9",
    "Black-and-White_Fallacy": "A6.4",
    "Causal_Oversimplification": "A8.7",
    "Doubt": "A10.7",
    "Exaggeration,Minimisation": "A10.6",
    "Flag-Waving": "A10.4",
    "Loaded_Language": "A9.1",
    "Name_Calling,Labeling": "A10.1",
    "Repetition": "A10.2",
    "Slogans": "A10.5",
    "Straw_Men": "A7.2",
    "Whataboutism,Red_Herring": "A10.3",
}

# ── Load Anchors for Few-Shot ────────────────────────────────────────────────

def load_anchors_by_code() -> dict[str, str]:
    """Load anchor examples keyed by taxonomy code, as formatted JSON strings."""
    anchors = {}
    with open(ANCHORS_FILE) as f:
        for line in f:
            rec = json.loads(line)
            code = rec["taxonomy_code"]
            if code not in anchors:
                anchors[code] = json.dumps(rec, indent=2)
    return anchors

# ── Enrichment Prompt ────────────────────────────────────────────────────────

def build_enrich_prompt(
    original_text: str,
    original_label: str,
    taxonomy_code: str,
    taxonomy_label: str,
    pattern_type: str,
    track: str,
    record_id: str,
    source_dataset: str,
    anchor_example: str,
) -> str:
    return f"""Enrich this existing dataset example into a full training corpus record for an educational RPG game.

## Original Example
- **Source dataset:** {source_dataset}
- **Original text:** {original_text}
- **Original label:** {original_label}

## Target Taxonomy
- **Code:** {taxonomy_code}
- **Label:** {taxonomy_label}
- **Pattern type:** {pattern_type}
- **Track:** {track}

## Quality Reference (anchor example for this code)
{anchor_example[:3000]}

## Instructions
1. Keep the original text as the scenario text (lightly edit for clarity if needed)
2. Add a realistic game context and NPC speaker
3. Fill in ALL structure fields (pattern_name, pattern_description, formal_form, why_wrong/why_right, related_patterns, counterpoint)
4. Create assessment scaffolding (identification_prompt, rubric with levels 0-4, follow_ups)
5. Create game hooks (npc_personality, dialogue_seed, resolution_path)
6. Assign difficulty_tier: "drill" for clear-cut cases, "what_if" for ambiguous ones

Return a single valid JSON object with these exact fields:
{{
  "id": "{record_id}",
  "taxonomy_code": "{taxonomy_code}",
  "taxonomy_label": "{taxonomy_label}",
  "track": "{track}",
  "pattern_type": "{pattern_type}",
  "difficulty_tier": "drill",
  "scenario": {{"context": "...", "text": "...", "speaker_context": "..."}},
  "structure": {{"pattern_name": "...", "pattern_description": "...", "formal_form": null, "why_wrong": "...", "why_right": null, "related_patterns": [], "counterpoint": "..."}},
  "assessment": {{"identification_prompt": "...", "rubric": [{{"level": 0, "description": "..."}}, {{"level": 1, "description": "..."}}, {{"level": 2, "description": "..."}}, {{"level": 3, "description": "..."}}, {{"level": 4, "description": "..."}}], "follow_up_if_wrong": "...", "follow_up_if_right": "..."}},
  "game_hooks": {{"npc_personality": "...", "npc_dialogue_seed": "...", "resolution_path": "..."}},
  "source": {{"type": "existing_dataset", "source_material": "{source_dataset}", "original_id": null}}
}}

Return ONLY valid JSON, no markdown wrapping."""

# ── Dataset Loaders ──────────────────────────────────────────────────────────

def load_jin() -> list[dict]:
    records = []
    with open(DATA_DIR / "jin_fallacy.jsonl") as f:
        for i, line in enumerate(f):
            rec = json.loads(line)
            label = rec.get("logical_fallacies", "")
            code = JIN_MAPPING.get(label)
            if code:
                records.append({
                    "text": rec.get("source_article", ""),
                    "label": label,
                    "taxonomy_code": code,
                    "dataset": "jin_fallacy",
                    "idx": i,
                })
    return records

def load_folio() -> list[dict]:
    records = []
    with open(DATA_DIR / "folio.jsonl") as f:
        for i, line in enumerate(f):
            rec = json.loads(line)
            label = rec.get("label", "")
            code = FOLIO_MAPPING.get(label)
            if code:
                premises = rec.get("premises", "")
                conclusion = rec.get("conclusion", "")
                text = f"Premises: {premises}\nConclusion: {conclusion}"
                records.append({
                    "text": text,
                    "label": label,
                    "taxonomy_code": code,
                    "dataset": "folio",
                    "idx": i,
                })
    return records

def load_corr2cause() -> list[dict]:
    records = []
    with open(DATA_DIR / "corr2cause.jsonl") as f:
        for i, line in enumerate(f):
            rec = json.loads(line)
            label = rec.get("label", -1)
            code = CORR2CAUSE_MAPPING.get(label)
            if code:
                records.append({
                    "text": rec.get("input", ""),
                    "label": str(label),
                    "taxonomy_code": code,
                    "dataset": "corr2cause",
                    "idx": i,
                })
    return records

def load_propaganda() -> list[dict]:
    records = []
    with open(DATA_DIR / "semeval2020_propaganda.jsonl") as f:
        for i, line in enumerate(f):
            rec = json.loads(line)
            label = rec.get("technique", rec.get("label", ""))
            code = PROPAGANDA_MAPPING.get(label)
            if code:
                text = rec.get("text", rec.get("sentence", ""))
                records.append({
                    "text": text,
                    "label": label,
                    "taxonomy_code": code,
                    "dataset": "semeval2020_propaganda",
                    "idx": i,
                })
    return records

# ── Main Pipeline ────────────────────────────────────────────────────────────

async def enrich_record(
    client: openai.AsyncOpenAI,
    semaphore: asyncio.Semaphore,
    record: dict,
    anchors: dict[str, str],
    taxonomy: dict,
    counter: dict,
) -> dict | None:
    code = record["taxonomy_code"]
    entry = taxonomy.get(code, {})
    anchor = anchors.get(code, "(No anchor available)")
    record_id = f"{code}-{record['dataset'][:3].upper()}{record['idx']:04d}"

    prompt = build_enrich_prompt(
        original_text=record["text"][:1500],  # cap length
        original_label=record["label"],
        taxonomy_code=code,
        taxonomy_label=entry.get("label", code),
        pattern_type=entry.get("pattern_type", "bad_thinking"),
        track=entry.get("track", "logic_critical_thinking"),
        record_id=record_id,
        source_dataset=record["dataset"],
        anchor_example=anchor[:3000],
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with semaphore:
                resp = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": "You enrich dataset examples into full training corpus records for an educational RPG. Return ONLY valid JSON."},
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=4096,
                    temperature=0.5,
                    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                )

            content = resp.choices[0].message.content or ""
            # Try to extract JSON if wrapped in markdown
            if "```" in content:
                content = content.split("```json")[-1].split("```")[0] if "```json" in content else content.split("```")[1].split("```")[0]

            result = json.loads(content)
            # Basic validation
            required = ["id", "taxonomy_code", "scenario", "structure", "assessment", "game_hooks"]
            if all(k in result for k in required):
                counter["valid"] += 1
                return result
            else:
                counter["invalid"] += 1
                return None

        except json.JSONDecodeError:
            counter["json_error"] += 1
            if attempt == MAX_RETRIES:
                return None
        except Exception as e:
            if attempt == MAX_RETRIES:
                counter["api_error"] += 1
                return None
            await asyncio.sleep(2 ** attempt)

    return None


async def process_dataset(name: str, records: list[dict], max_records: int | None = None):
    """Process a dataset through the enrichment pipeline."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from taxonomy import TAXONOMY

    anchors = load_anchors_by_code()
    client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    if max_records:
        records = records[:max_records]

    print(f"\n{'='*60}")
    print(f"Processing: {name} ({len(records)} records)")
    print(f"{'='*60}")

    counter = {"valid": 0, "invalid": 0, "json_error": 0, "api_error": 0}
    results = []
    start = time.time()

    async def process_one(rec):
        result = await enrich_record(client, semaphore, rec, anchors, TAXONOMY, counter)
        total = counter["valid"] + counter["invalid"] + counter["json_error"] + counter["api_error"]
        if total % 50 == 0:
            elapsed = time.time() - start
            print(f"  Progress: {total}/{len(records)} ({counter['valid']} valid) [{elapsed:.0f}s]", flush=True)
        return result

    all_results = await asyncio.gather(*[process_one(r) for r in records])
    results = [r for r in all_results if r is not None]

    # Write output
    output_file = OUTPUT_DIR / f"adapted_{name}.jsonl"
    with open(output_file, "w") as f:
        for rec in results:
            f.write(json.dumps(rec) + "\n")

    elapsed = time.time() - start
    print(f"\n  Done: {len(results)}/{len(records)} valid ({len(results)/len(records):.1%})")
    print(f"  Errors: json={counter['json_error']}, api={counter['api_error']}, invalid={counter['invalid']}")
    print(f"  Time: {elapsed:.0f}s")
    print(f"  Output: {output_file}")

    return len(results)


async def main():
    datasets = {
        "jin": load_jin(),
        "folio": load_folio(),
        "corr2cause": load_corr2cause(),
        "propaganda": load_propaganda(),
    }

    print("Sprint 2: Dataset Adaptation via MindRouter")
    print(f"Model: {MODEL} | Concurrency: {MAX_CONCURRENT}")
    for name, records in datasets.items():
        labels = Counter(r["taxonomy_code"] for r in records)
        print(f"  {name}: {len(records)} records -> {dict(labels)}")

    total = 0
    for name, records in datasets.items():
        count = await process_dataset(name, records)
        total += count

    print(f"\n{'='*60}")
    print(f"SPRINT 2 COMPLETE: {total} adapted records total")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
