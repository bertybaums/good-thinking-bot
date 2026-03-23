#!/usr/bin/env python3
"""
Sprint 5: Synthetic Game Theory (B6-B10) + Integrated Scenarios

Part A: ~1,000 game theory examples (B6-B10, ~200 per group)
Part B: ~200 integrated multi-code scenarios (puzzle tier, require multiple skills)

Uses gpt-oss-120b (8 concurrent).
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

MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"
MODEL = "openai/gpt-oss-120b"
MAX_CONCURRENT = 8

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
ANCHORS_FILE = OUTPUT_DIR / "anchors.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY

DOMAINS = [
    "medieval trading post", "pirate ship crew", "frontier farming village",
    "guild apprentice workshop", "battlefield logistics", "royal court intrigue",
    "traveling merchant caravan", "mining colony", "fishing village",
    "tavern alliance", "blacksmith guild", "apothecary trade",
    "ship captain diplomacy", "castle siege", "tournament politics",
    "harvest cooperation", "bandit territory", "monastery commons",
    "ranger patrol coordination", "marketplace competition",
]

TIERS_WEIGHTED = ["drill", "drill", "what_if", "what_if", "puzzle"]

# ── Game Theory Seeds ────────────────────────────────────────────────────────

GT_SEEDS = {
    "B6.1": {
        "label": "Prisoner's Dilemma",
        "type": "dual",
        "seed": "Two players, each choosing Cooperate or Defect. Payoffs: (C,C)>(D,D) but D dominates. Create a concrete social dilemma with exact payoff numbers.",
        "math_note": "Players: [Row, Col]; Strategies: [C, D]; Payoffs: (C,C)=(R,R), (C,D)=(S,T), (D,C)=(T,S), (D,D)=(P,P) where T>R>P>S.",
    },
    "B6.2": {
        "label": "Nash equilibrium",
        "type": "good_tool",
        "seed": "A 2x2 or 2x3 game where finding Nash equilibria requires checking best responses. Include at least one pure NE.",
        "math_note": "Show the game matrix with payoffs. Identify best responses and NE.",
    },
    "B6.3": {
        "label": "Iterated PD and cooperation",
        "type": "good_tool",
        "seed": "A repeated interaction where tit-for-tat or similar conditional strategy sustains cooperation. Include the shadow-of-the-future calculation: delta > (T-R)/(T-P).",
        "math_note": "Include discount factor threshold calculation.",
    },
    "B7.1": {
        "label": "Stag Hunt",
        "type": "dual",
        "seed": "Two players choosing between safe (Hare) and risky cooperative (Stag) options. Two NE: (Stag,Stag) and (Hare,Hare). The trust problem.",
        "math_note": "Payoffs must satisfy: Stag,Stag > Hare,Hare > Stag,Hare. Show both equilibria.",
    },
    "B7.2": {
        "label": "Battle of the Sexes",
        "type": "dual",
        "seed": "Coordination with conflict: both prefer to coordinate but disagree on which equilibrium. Asymmetric payoffs.",
        "math_note": "Two pure NE with different preferred outcomes for each player.",
    },
    "B7.3": {
        "label": "Focal points (Schelling points)",
        "type": "good_tool",
        "seed": "Players must coordinate without communication. One option is culturally/contextually salient. Show how context determines the focal point.",
        "math_note": "No formal matrix needed — focus on salience and coordination.",
    },
    "B7.4": {
        "label": "Convention (Lewis)",
        "type": "good_tool",
        "seed": "An arbitrary solution to a recurrent coordination problem that persists because everyone expects it. Show why no individual has reason to deviate.",
        "math_note": "Show the self-reinforcing equilibrium structure.",
    },
    "B8.1": {
        "label": "Game trees and extensive form",
        "type": "good_tool",
        "seed": "A sequential game with 2-3 moves. Draw the tree structure in text. Decision nodes, branches, terminal payoffs.",
        "math_note": "Include full tree with payoffs at terminal nodes.",
    },
    "B8.2": {
        "label": "Backward induction",
        "type": "good_tool",
        "seed": "A sequential game where backward induction yields a clear (possibly counterintuitive) solution. Show the reasoning from end to beginning.",
        "math_note": "Show the BI reasoning at each node.",
    },
    "B8.3": {
        "label": "Subgame perfect equilibrium",
        "type": "good_tool",
        "seed": "A game with a non-credible threat. The NE includes the threat but the SPE eliminates it via backward induction.",
        "math_note": "Show both the NE (with threat) and the SPE (without).",
    },
    "B8.4": {
        "label": "Centipede Game paradox",
        "type": "dual",
        "seed": "A passing game where BI says stop immediately but intuition says cooperate. Show the paradox between theory and intuition.",
        "math_note": "Include the full game tree with escalating payoffs.",
    },
    "B9.1": {
        "label": "Evolutionarily Stable Strategy (ESS)",
        "type": "good_tool",
        "seed": "Hawk-Dove game: aggressive vs peaceful. ESS depends on V (value) vs C (cost of fighting). If V<C, mixed ESS; if V>C, Hawk is ESS.",
        "math_note": "Include V and C values. Show the ESS calculation.",
    },
    "B9.2": {
        "label": "Replicator dynamics",
        "type": "good_tool",
        "seed": "A population with two strategies. Show how the more successful strategy spreads over generations. Include fitness calculations.",
        "math_note": "Show fitness of each strategy against population mix.",
    },
    "B9.3": {
        "label": "Evolution of cooperation",
        "type": "good_tool",
        "seed": "How cooperation emerges among non-rational agents: kin selection, reciprocity, spatial structure, or group selection.",
        "math_note": "Include conditions under which cooperation is stable.",
    },
    "B10.1": {
        "label": "Signaling and costly signals",
        "type": "good_tool",
        "seed": "Asymmetric information: one player signals quality through costly action. Separating equilibrium where only high-quality types signal.",
        "math_note": "Include cost for high vs low types. Show separation condition.",
    },
    "B10.2": {
        "label": "Behavioral game theory",
        "type": "dual",
        "seed": "Ultimatum game: proposer offers a split, responder accepts or rejects. Nash says accept any positive offer; real humans reject unfair splits.",
        "math_note": "Include specific offer amounts and typical rejection thresholds.",
    },
    "B10.3": {
        "label": "Commitment and precommitment",
        "type": "good_tool",
        "seed": "A player does better by restricting their own future options. Burning bridges, making binding promises, Odysseus and the Sirens.",
        "math_note": "Show payoffs with and without commitment.",
    },
    "B10.4": {
        "label": "Reputation and repeated games",
        "type": "good_tool",
        "seed": "The shadow of the future sustains cooperation. A player builds a reputation that changes the game for future interactions.",
        "math_note": "Include discount factor or probability of continuation.",
    },
}

# ── Integrated scenario codes (multi-skill) ─────────────────────────────────

INTEGRATED_COMBOS = [
    (["A7.1", "A7.2"], "A fallacy combining ad hominem and straw man"),
    (["B6.1", "B5.2"], "A PD situation complicated by loss aversion"),
    (["A8.5", "B3.1"], "Gambler's fallacy meeting expected utility calculation"),
    (["E1.2", "A7.14"], "Confirmation bias driving Texas sharpshooter data selection"),
    (["D2.1", "B3.1"], "Satisficing vs MEU — when is good enough better than optimal?"),
    (["B7.1", "E1.12"], "Stag Hunt where groupthink pressures toward the wrong equilibrium"),
    (["A6.4", "A7.7"], "False dichotomy reinforced by emotional appeal"),
    (["C1.1", "B5.8"], "Opportunity cost reasoning undermined by sunk cost fallacy"),
    (["D1.1", "A7.2"], "Using Rapoport's Rules to counter a straw man argument"),
    (["B10.2", "E1.16"], "Ultimatum game rejection driven by just-world hypothesis"),
    (["A3.5", "A8.7"], "Correlation vs causation with post hoc reasoning"),
    (["D2.2", "C3.2"], "Panglossian Slide about commons management"),
    (["B4.1", "B5.3"], "Allais Paradox driven by probability weighting"),
    (["E1.3", "C4.1"], "Anchoring effect in bargaining negotiations"),
    (["A7.6", "E1.4"], "Appeal to authority meeting Dunning-Kruger"),
    (["B8.2", "B10.3"], "Backward induction with commitment — changing the game tree"),
    (["E1.18", "A7.9"], "Backfire effect amplified by bandwagon pressure"),
    (["D2.3", "A10.5"], "Conversation-stopper as thought-terminating cliché"),
    (["B9.1", "C3.1"], "ESS in a public goods / free-rider context"),
    (["A4.3", "A8.2"], "Base rate reasoning vs base rate neglect"),
]

# ── Load anchor ──────────────────────────────────────────────────────────────

def load_anchor(code: str) -> str:
    with open(ANCHORS_FILE) as f:
        for line in f:
            rec = json.loads(line)
            if rec["taxonomy_code"] == code:
                return json.dumps(rec, indent=2)[:2500]
    return ""

# ── Prompts ──────────────────────────────────────────────────────────────────

def build_gt_prompt(code, seed, domain, tier, record_id, anchor):
    return f"""Generate a game theory training example for an educational RPG game.

## Taxonomy
- **Code:** {code}
- **Label:** {seed['label']}
- **Pattern type:** {seed['type']}

## Seed Problem
{seed['seed']}

## Math Requirements
{seed['math_note']}

## Domain: {domain}
## Difficulty: {tier}

## Quality Reference
{anchor}

Return ONLY valid JSON:
{{
  "id": "{record_id}",
  "taxonomy_code": "{code}",
  "taxonomy_label": "{seed['label']}",
  "track": "game_theory",
  "pattern_type": "{seed['type']}",
  "difficulty_tier": "{tier}",
  "scenario": {{"context": "...", "text": "... (include exact payoffs)", "speaker_context": "..."}},
  "structure": {{"pattern_name": "...", "pattern_description": "... (show computation)", "formal_form": "Players: [...]; Strategies: [...]; Payoffs: ...", "why_wrong": {'"..."' if seed['type'] == 'bad_thinking' else 'null'}, "why_right": {'"..."' if seed['type'] != 'bad_thinking' else 'null'}, "related_patterns": [], "counterpoint": "..."}},
  "assessment": {{"identification_prompt": "...", "rubric": [{{"level": 0, "description": "..."}}, {{"level": 1, "description": "..."}}, {{"level": 2, "description": "..."}}, {{"level": 3, "description": "..."}}, {{"level": 4, "description": "..."}}], "follow_up_if_wrong": "...", "follow_up_if_right": "..."}},
  "game_hooks": {{"npc_personality": "...", "npc_dialogue_seed": "...", "resolution_path": "..."}},
  "source": {{"type": "synthetic_verified", "source_material": "Generated from {code} anchor + W8-W14 seeds", "original_id": null}}
}}"""


def build_integrated_prompt(codes, description, domain, record_id, anchors_text):
    code_labels = ", ".join(f"{c} ({TAXONOMY[c]['label']})" for c in codes)
    return f"""Generate an INTEGRATED multi-skill training example for an educational RPG game.

This scenario must require the player to recognize and reason about MULTIPLE concepts simultaneously.

## Codes Required: {code_labels}
## Description: {description}
## Domain: {domain}
## Difficulty: puzzle (these are always the hardest tier)

## Anchor References
{anchors_text}

Return ONLY valid JSON:
{{
  "id": "{record_id}",
  "taxonomy_code": "{codes[0]}",
  "taxonomy_label": "Integrated: {' + '.join(TAXONOMY[c]['label'] for c in codes)}",
  "track": "{TAXONOMY[codes[0]]['track']}",
  "pattern_type": "dual",
  "difficulty_tier": "puzzle",
  "scenario": {{"context": "... (complex scenario requiring multiple skills)", "text": "...", "speaker_context": "..."}},
  "structure": {{"pattern_name": "Integrated: {' + '.join(TAXONOMY[c]['label'] for c in codes)}", "pattern_description": "... (explain how both/all concepts interact)", "formal_form": null, "why_wrong": null, "why_right": "...", "related_patterns": {json.dumps(codes)}, "counterpoint": "..."}},
  "assessment": {{"identification_prompt": "... (must probe both/all concepts)", "rubric": [{{"level": 0, "description": "..."}}, {{"level": 1, "description": "..."}}, {{"level": 2, "description": "Identifies one concept but misses the other(s)"}}, {{"level": 3, "description": "Identifies both/all concepts"}}, {{"level": 4, "description": "Identifies all concepts AND explains how they interact"}}], "follow_up_if_wrong": "...", "follow_up_if_right": "..."}},
  "game_hooks": {{"npc_personality": "...", "npc_dialogue_seed": "...", "resolution_path": "..."}},
  "source": {{"type": "synthetic_verified", "source_material": "Integrated scenario: {code_labels}", "original_id": null}}
}}"""

# ── Main ─────────────────────────────────────────────────────────────────────

async def main():
    client = openai.AsyncOpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    # Part A: Game theory (18 codes x ~56 each ≈ 1,000)
    plan_gt = []
    for code, seed in GT_SEEDS.items():
        anchor = load_anchor(code)
        for i in range(56):
            domain = random.choice(DOMAINS)
            tier = random.choice(TIERS_WEIGHTED)
            record_id = f"{code}-S5{i:04d}"
            plan_gt.append(("gt", code, seed, domain, tier, record_id, anchor))

    # Part B: Integrated scenarios (20 combos x 10 each = 200)
    plan_int = []
    for combo_idx, (codes, description) in enumerate(INTEGRATED_COMBOS):
        anchors_text = "\n---\n".join(load_anchor(c)[:1500] for c in codes)
        for i in range(10):
            domain = random.choice(DOMAINS)
            record_id = f"INT-S5{combo_idx:02d}{i:02d}"
            plan_int.append(("int", codes, description, domain, record_id, anchors_text))

    total_plan = len(plan_gt) + len(plan_int)
    print(f"Sprint 5: Game Theory + Integrated Scenarios")
    print(f"Model: {MODEL} | Concurrency: {MAX_CONCURRENT}")
    print(f"Part A: {len(plan_gt)} game theory examples")
    print(f"Part B: {len(plan_int)} integrated scenarios")
    print(f"Total: {total_plan}")

    valid = 0
    failed = 0
    start = time.time()

    async def generate_one(item):
        nonlocal valid, failed
        if item[0] == "gt":
            _, code, seed, domain, tier, record_id, anchor = item
            prompt = build_gt_prompt(code, seed, domain, tier, record_id, anchor)
        else:
            _, codes, description, domain, record_id, anchors_text = item
            prompt = build_integrated_prompt(codes, description, domain, record_id, anchors_text)

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
                if all(k in result for k in ["id", "taxonomy_code", "scenario", "structure"]):
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

    # Combine and shuffle
    all_items = plan_gt + plan_int
    random.shuffle(all_items)

    output_file = OUTPUT_DIR / "synthetic_GT_integrated_sprint5.jsonl"
    batch_size = 40
    with open(output_file, "w") as out_f:
        for batch_start in range(0, len(all_items), batch_size):
            batch = all_items[batch_start : batch_start + batch_size]
            results = await asyncio.gather(*[generate_one(item) for item in batch])
            for r in results:
                if r is not None:
                    out_f.write(json.dumps(r) + "\n")
            out_f.flush()
            elapsed = time.time() - start
            total = valid + failed
            print(f"  Progress: {total}/{total_plan} ({valid} valid, {failed} failed) [{elapsed:.0f}s]", flush=True)

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"SPRINT 5 COMPLETE")
    print(f"{'='*60}")
    print(f"Total: {valid} valid, {failed} failed ({valid/(valid+failed):.1%} success)")
    print(f"Time: {elapsed:.0f}s")
    print(f"Output: {output_file}")

    records = [json.loads(l) for l in open(output_file) if l.strip()]
    code_counts = Counter(r.get("taxonomy_code", "?") for r in records)
    print(f"\nPer-code counts:")
    for code in sorted(code_counts):
        print(f"  {code}: {code_counts[code]}")


if __name__ == "__main__":
    asyncio.run(main())
