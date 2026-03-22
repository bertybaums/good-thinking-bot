#!/usr/bin/env python3
"""
Sprint 3: Synthetic Decision Theory Generation (B1-B5)

Generates ~2,000 decision theory examples by varying domains on Bert's
worked problems from W1-W7. Uses gpt-oss-120b (8 concurrent) for quality,
since these require precise numerical values for mechanical verification.

Also generates game theory examples (B6-B10) as part of Sprint 5 prep.
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
MODEL = "openai/gpt-oss-120b"
MAX_CONCURRENT = 8

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
ANCHORS_FILE = OUTPUT_DIR / "anchors.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

# ── Domains for variation ────────────────────────────────────────────────────

DOMAINS = [
    "medieval trading post", "pirate ship crew", "frontier farming village",
    "guild apprentice workshop", "battlefield field hospital", "royal court politics",
    "traveling merchant caravan", "mining colony", "fishing village",
    "tavern owner decisions", "blacksmith forge", "apothecary shop",
    "ship captain navigation", "castle siege defense", "tournament preparation",
    "harvest season planning", "bandit hideout", "monastery resource allocation",
    "ranger wilderness patrol", "marketplace negotiations",
]

TIERS = ["drill", "drill", "drill", "what_if", "what_if", "puzzle"]  # weighted toward drill

# ── Decision Theory Seed Problems ────────────────────────────────────────────

DT_SEEDS = {
    "B1.1": {
        "label": "Decision matrices",
        "type": "good_tool",
        "seed": "Construct a decision matrix with 2-3 acts and 2-3 states. Assign ordinal values (1-4 or 1-6). Ask: which act is best? Note: there should be NO dominant act (if there were, the problem would be trivial).",
        "math_note": "Include exact payoff values. Format: Acts: [A1, A2]; States: [S1, S2]; Payoffs: A1|S1=V1, ...",
    },
    "B1.2": {
        "label": "Dominance reasoning",
        "type": "good_tool",
        "seed": "Construct a matrix where one act strictly dominates another. The player must identify the dominant act. Include a twist: one scenario where state-act independence is violated.",
        "math_note": "Include exact payoff values showing dominance.",
    },
    "B1.3": {
        "label": "Maximax",
        "type": "good_tool",
        "seed": "3 acts, 3 states, cardinal utilities. The maximax choice should differ from maximin. Ask the player to identify the maximax act and explain why a risk-seeker would choose it.",
        "math_note": "Best-case for each act must be clearly different.",
    },
    "B1.4": {
        "label": "Maximin",
        "type": "good_tool",
        "seed": "3 acts, 2-3 states. The maximin choice should differ from maximax. The worst-case floors should be clearly distinguishable.",
        "math_note": "Worst-case for each act must be clearly different.",
    },
    "B1.5": {
        "label": "Minimax regret",
        "type": "good_tool",
        "seed": "3 acts, 3 states, cardinal utilities. Compute the regret matrix. The minimax regret act should differ from both maximin and maximax.",
        "math_note": "Show full regret computation in pattern_description.",
    },
    "B2.1": {
        "label": "Betting rates and credences",
        "type": "good_tool",
        "seed": "Someone accepts a bet: risks $X to win $Y. Calculate their implied credence using Fair Betting Rate = Loss/Stake.",
        "math_note": "Include exact numbers for the bet.",
    },
    "B2.2": {
        "label": "Dutch Book arguments",
        "type": "good_tool",
        "seed": "A bookie offers odds on 3-4 outcomes where implied probabilities sum to more (or less) than 1. Show the guaranteed profit/loss.",
        "math_note": "Probabilities must sum to != 1. Show exact profit calculation.",
    },
    "B3.1": {
        "label": "MEU formula and calculation",
        "type": "good_tool",
        "seed": "2-3 acts with known probabilities. Calculate EU for each. The MEU act should be non-obvious (not the one with highest single payoff).",
        "math_note": "EU(A) = sum P(S)*U(A|S). Include probabilities and payoffs.",
    },
    "B3.3": {
        "label": "Risk aversion and utility curves",
        "type": "good_tool",
        "seed": "Two options: a certain outcome vs a gamble with same expected value. A risk-averse agent prefers the certainty. Show why via concave utility.",
        "math_note": "Include EU calculation showing indifference point.",
    },
    "B3.4": {
        "label": "Transitivity and money pumps",
        "type": "good_tool",
        "seed": "Three options A, B, C where someone prefers A>B, B>C, C>A. Show how they can be money-pumped through a cycle of trades.",
        "math_note": "Show the cycle and cumulative loss per cycle.",
    },
    "B3.5": {
        "label": "Independence of Irrelevant Alternatives",
        "type": "good_tool",
        "seed": "Minimax regret on 3 options. Remove one option and show the recommendation changes. This violates IIA.",
        "math_note": "Show both regret matrices (with and without the removed option).",
    },
    "B4.1": {
        "label": "Allais Paradox",
        "type": "dual",
        "seed": "Present the classic Allais setup: Gamble 1 (certain) vs Gamble 2 (risky), then Gamble 3 vs 4 where the 'common consequence' is removed. Most people choose 1 and 4, violating STP.",
        "math_note": "Use exact probabilities and payoffs. Show the STP violation.",
    },
    "B5.1": {
        "label": "Reference points",
        "type": "dual",
        "seed": "Two people receive the same outcome but feel differently because their reference points differ (one expected more, one expected less).",
        "math_note": "Include specific salary/price numbers.",
    },
    "B5.2": {
        "label": "Loss aversion",
        "type": "dual",
        "seed": "A coin flip gamble: lose $X or win $Y. Most people need Y ≈ 2.25X to accept. Show why MEU says they should accept at Y > X.",
        "math_note": "Include lambda ≈ 2.25 calculation.",
    },
    "B5.5": {
        "label": "Framing effects",
        "type": "bad_thinking",
        "seed": "Present the same scenario in gain frame vs loss frame. The Asian Disease Problem: '200 saved' vs '400 die' — logically identical but elicit different choices.",
        "math_note": "Show the two frames are mathematically equivalent.",
    },
    "B5.8": {
        "label": "Sunk cost fallacy (decision-theoretic)",
        "type": "bad_thinking",
        "seed": "Someone continues a failing project because of past investment. Show the MEU calculation that proves switching is better.",
        "math_note": "Include future costs/benefits for continue vs switch.",
    },
}

# ── Load anchors for few-shot ────────────────────────────────────────────────

def load_anchor(code: str) -> str:
    with open(ANCHORS_FILE) as f:
        for line in f:
            rec = json.loads(line)
            if rec["taxonomy_code"] == code:
                return json.dumps(rec, indent=2)[:3000]
    return "(No anchor available)"

# ── Generation prompt ────────────────────────────────────────────────────────

def build_prompt(code: str, seed: dict, domain: str, tier: str, record_id: str, anchor: str) -> str:
    return f"""Generate a decision theory training example for an educational RPG game.

## Taxonomy
- **Code:** {code}
- **Label:** {seed['label']}
- **Pattern type:** {seed['type']}
- **Track:** decision_theory

## Seed Problem (vary the domain, preserve the math structure)
{seed['seed']}

## Mathematical Requirements
{seed['math_note']}

## Domain
Set this in: {domain}

## Difficulty: {tier}
- drill: clear-cut, apply mechanically
- what_if: stress-test, moderate ambiguity
- puzzle: genuine philosophical tension

## Quality Reference
{anchor}

## Output
Return a single valid JSON object (no markdown wrapping):
{{
  "id": "{record_id}",
  "taxonomy_code": "{code}",
  "taxonomy_label": "{seed['label']}",
  "track": "decision_theory",
  "pattern_type": "{seed['type']}",
  "difficulty_tier": "{tier}",
  "scenario": {{"context": "...", "text": "... (include exact numbers)", "speaker_context": "..."}},
  "structure": {{"pattern_name": "...", "pattern_description": "... (show full computation)", "formal_form": "Acts: [...]; States: [...]; Payoffs: ...", "why_wrong": {"'...'" if seed['type'] == 'bad_thinking' else 'null'}, "why_right": {"'...'" if seed['type'] != 'bad_thinking' else 'null'}, "related_patterns": [], "counterpoint": "..."}},
  "assessment": {{"identification_prompt": "...", "rubric": [{{"level": 0, "description": "..."}}, {{"level": 1, "description": "..."}}, {{"level": 2, "description": "..."}}, {{"level": 3, "description": "..."}}, {{"level": 4, "description": "..."}}], "follow_up_if_wrong": "...", "follow_up_if_right": "..."}},
  "game_hooks": {{"npc_personality": "...", "npc_dialogue_seed": "...", "resolution_path": "..."}},
  "source": {{"type": "synthetic_verified", "source_material": "Generated from {code} anchor + W1-W7 lecture seeds", "original_id": null}}
}}"""

# ── Main pipeline ────────────────────────────────────────────────────────────

async def main():
    client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    # Build generation plan: ~125 examples per code, 16 codes = ~2,000
    plan = []
    for code, seed in DT_SEEDS.items():
        anchor = load_anchor(code)
        examples_per_code = 125
        for i in range(examples_per_code):
            domain = random.choice(DOMAINS)
            tier = random.choice(TIERS)
            record_id = f"{code}-S3{i:04d}"
            plan.append({
                "code": code,
                "seed": seed,
                "domain": domain,
                "tier": tier,
                "record_id": record_id,
                "anchor": anchor,
            })

    random.shuffle(plan)
    print(f"Sprint 3: Synthetic Decision Theory Generation")
    print(f"Model: {MODEL} | Concurrency: {MAX_CONCURRENT}")
    print(f"Plan: {len(plan)} examples across {len(DT_SEEDS)} codes")
    print(f"Codes: {', '.join(DT_SEEDS.keys())}")

    output_file = OUTPUT_DIR / "synthetic_DT_sprint3.jsonl"
    valid = 0
    failed = 0
    start = time.time()

    async def generate_one(item):
        nonlocal valid, failed
        prompt = build_prompt(
            item["code"], item["seed"], item["domain"],
            item["tier"], item["record_id"], item["anchor"],
        )
        for attempt in range(3):
            try:
                async with semaphore:
                    resp = await client.chat.completions.create(
                        model=MODEL,
                        messages=[
                            {"role": "system", "content": "Generate training examples for an educational game. Return ONLY valid JSON."},
                            {"role": "user", "content": prompt},
                        ],
                        max_tokens=4096,
                        temperature=0.7,
                        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                    )
                content = resp.choices[0].message.content or ""
                if "```" in content:
                    content = content.split("```json")[-1].split("```")[0] if "```json" in content else content.split("```")[1].split("```")[0]
                result = json.loads(content)
                required = ["id", "taxonomy_code", "scenario", "structure", "assessment"]
                if all(k in result for k in required):
                    valid += 1
                    return result
                failed += 1
                return None
            except (json.JSONDecodeError, Exception):
                if attempt == 2:
                    failed += 1
                    return None
                await asyncio.sleep(2 ** (attempt + 1))
        return None

    # Process in batches of 40, write incrementally
    batch_size = 40
    with open(output_file, "w") as out_f:
        for batch_start in range(0, len(plan), batch_size):
            batch = plan[batch_start : batch_start + batch_size]
            results = await asyncio.gather(*[generate_one(item) for item in batch])
            for r in results:
                if r is not None:
                    out_f.write(json.dumps(r) + "\n")
            out_f.flush()
            elapsed = time.time() - start
            total = valid + failed
            print(f"  Progress: {total}/{len(plan)} ({valid} valid, {failed} failed) [{elapsed:.0f}s]", flush=True)

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"SPRINT 3 COMPLETE")
    print(f"{'='*60}")
    print(f"Total: {valid} valid, {failed} failed ({valid/(valid+failed):.1%} success)")
    print(f"Time: {elapsed:.0f}s")
    print(f"Output: {output_file}")

    # Show per-code counts
    records = [json.loads(l) for l in open(output_file) if l.strip()]
    code_counts = Counter(r["taxonomy_code"] for r in records)
    print(f"\nPer-code counts:")
    for code in sorted(code_counts):
        print(f"  {code}: {code_counts[code]}")


if __name__ == "__main__":
    asyncio.run(main())
