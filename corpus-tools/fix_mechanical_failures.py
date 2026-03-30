#!/usr/bin/env python3
"""
Fix the 56 mechanical verification failures identified in QC2.

For each failing record:
1. Parse the payoff matrix from formal_form (the matrix defines the problem)
2. Recompute the correct answer (MEU, minimax regret, maximin, Nash equilibria)
3. Patch the text fields (why_right, why_wrong, pattern_description) with corrected values
4. Write the corrected records back to the source JSONL files

Usage:
    python3 fix_mechanical_failures.py --dry-run    # Show what would change
    python3 fix_mechanical_failures.py --apply       # Apply fixes in place
"""

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np

from config import CORPUS_OUTPUT_DIR

# Import solvers from the verification script
from importlib.util import spec_from_file_location, module_from_spec
_spec = spec_from_file_location("verify", Path(__file__).parent / "05_mechanical_verify.py")
_verify = module_from_spec(_spec)
_spec.loader.exec_module(_verify)

parse_decision_matrix = _verify.parse_decision_matrix
parse_2x2_game = _verify.parse_2x2_game
find_pure_nash = _verify.find_pure_nash
solve_meu = _verify.solve_meu
solve_minimax_regret = _verify.solve_minimax_regret
solve_maximin = _verify.solve_maximin


# ─── Raw JSONL I/O (bypasses Pydantic to handle minor schema quirks) ─────────

def read_jsonl_raw(filepath: Path) -> list[dict]:
    records = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_jsonl_raw(records: list[dict], filepath: Path) -> None:
    with open(filepath, "w") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ─── Known failing record IDs ────────────────────────────────────────────────

FAILING_IDS = {
    # MEU failures (7)
    "B3.2-ON0070", "B3.2-ON0000", "B3.2-ON0005",
    "B3.1-PIR001", "B3.1-M3001", "B3.1-S30015", "B3.1-S30087",
    # Maximin failure (1)
    "B1.4-S30098",
    # Minimax regret failures (16)
    "B1.5-S30062", "B1.5-S30074", "B1.5-S30072", "B1.5-S30087",
    "B1.5-S30001", "B1.5-S30103", "B1.5-S30045", "B1.5-S30100",
    "B1.5-S30079", "B1.5-S30013", "B1.5-S30098", "B1.5-S30016",
    "B1.5-S30066", "B1.5-WS30042", "B1.5-S30113", "B1.5-S30089",
    # Nash equilibrium failures (30)
    "B6.2-TU0059", "B6.2-XYZ123", "B8.1-TU0071", "B7.1-CASTLE-004",
    "B6.2-TU0087", "B6.1-TU0085", "B8.3-TU0096", "B6.2-TU0073",
    "B6.2-TU0044", "B6.2-AP001", "B6.2-TU0095", "B6.1-TU0088",
    "B8.3-S50043", "B6.2-TRN-202603", "B8.3-S50024", "B6.2-MC001",
    "B7.2-FV001", "B8.3-S50025", "B6.2-HC001", "B6.2-FV001",
    "B6.2-TS001", "B8.3-S50019", "B6.1-S50036", "B6.2-S50019",
    "B6.2-TRX904", "B8.3-S50037", "B6.2-ROYAL-001", "B7.2-S50049",
    "B6.2-PIR001", "B7.2-S50017",
}

TARGET_FILES = [
    "overnight_thin_DT.jsonl",
    "overnight_topup_GT.jsonl",
    "synthetic_DT_sprint3.jsonl",
    "synthetic_GT_integrated_sprint5.jsonl",
]


# ─── Helpers ─────────────────────────────────────────────────────────────────

def get_sf(record: dict, field: str) -> str | None:
    """Get a structure field."""
    return record.get("structure", {}).get(field)


def set_sf(record: dict, field: str, value: str) -> None:
    """Set a structure field."""
    record.setdefault("structure", {})[field] = value


def format_nash_equilibria(equilibria: list[tuple[str, str]]) -> str:
    if not equilibria:
        return "no pure-strategy Nash equilibrium"
    eq_strs = [f"({s1}, {s2})" for s1, s2 in equilibria]
    if len(eq_strs) == 1:
        return f"the Nash equilibrium is {eq_strs[0]}"
    return f"the Nash equilibria are {', '.join(eq_strs)}"


# ─── Fix functions (all operate on raw dicts) ───────────────────────────────

def fix_meu_record(record: dict, matrix: dict) -> list[str]:
    changes = []
    payoffs = matrix["payoffs"]
    probs = matrix["probabilities"]
    acts = matrix["acts"]

    if probs is None:
        return ["SKIP: no probabilities found"]

    prob_sum = sum(probs)
    formal_form = get_sf(record, "formal_form") or ""

    if abs(prob_sum - 1.0) > 0.01:
        normalized = [p / prob_sum for p in probs]
        for state, old_p, new_p in zip(matrix["states"], probs, normalized):
            if abs(old_p - new_p) > 0.001:
                old_str = f"(p={old_p})"
                new_str = f"(p={new_p:.2f})"
                if old_str in formal_form:
                    formal_form = formal_form.replace(old_str, new_str, 1)
                    changes.append(f"Fixed probability for {state}: {old_p} -> {new_p:.2f}")
        set_sf(record, "formal_form", formal_form)
        probs = normalized

    probs_arr = np.array(probs)
    eus = payoffs @ probs_arr
    best_idx = int(np.argmax(eus))
    best_act = acts[best_idx]

    for field_name in ["why_right", "why_wrong", "pattern_description"]:
        text = get_sf(record, field_name)
        if not text:
            continue

        new_text = text
        for i, act in enumerate(acts):
            correct_eu = eus[i]
            patterns = [
                (rf"EU\({re.escape(act)}\)\s*[=~≈]\s*-?[0-9.]+",
                 f"EU({act}) = {correct_eu:.2f}"),
                (rf"expected utility of {re.escape(act)}(?:\s+is|\s*[=:])\s*-?[0-9.]+",
                 f"expected utility of {act} is {correct_eu:.2f}"),
            ]
            for pattern, replacement in patterns:
                new_text, n = re.subn(pattern, replacement, new_text, flags=re.IGNORECASE)
                if n > 0:
                    changes.append(f"Fixed EU({act}) in {field_name}: -> {correct_eu:.2f}")

        for i, act in enumerate(acts):
            if i == best_idx:
                continue
            rec_patterns = [
                rf"(should choose|best (?:option|act|choice|strategy) is|recommends?|MEU selects?|optimal (?:act|choice|option) is)\s+{re.escape(act)}",
            ]
            for pat in rec_patterns:
                match = re.search(pat, new_text, re.IGNORECASE)
                if match:
                    old_phrase = match.group(0)
                    new_phrase = old_phrase.replace(act, best_act)
                    new_text = new_text.replace(old_phrase, new_phrase)
                    changes.append(f"Fixed recommended act in {field_name}: {act} -> {best_act}")

        if new_text != text:
            set_sf(record, field_name, new_text)

    return changes


def fix_minimax_regret_record(record: dict, matrix: dict) -> list[str]:
    changes = []
    payoffs = matrix["payoffs"]
    acts = matrix["acts"]

    best_idx = solve_minimax_regret(payoffs)
    correct_act = acts[best_idx]

    max_per_state = payoffs.max(axis=0)
    regret = max_per_state - payoffs
    max_regrets = regret.max(axis=1)

    for field_name in ["why_right", "why_wrong", "pattern_description"]:
        text = get_sf(record, field_name)
        if not text:
            continue

        new_text = text
        for i, act in enumerate(acts):
            if i == best_idx:
                continue
            patterns = [
                rf"(minimax regret (?:rule )?(?:recommends?|selects?|chooses?|suggests?|picks?))\s+{re.escape(act)}",
                rf"(best (?:option|act|choice) (?:under|by|for) minimax regret is)\s+{re.escape(act)}",
                rf"(lowest maximum regret(?:.*?)is)\s+{re.escape(act)}",
                rf"(minimize(?:s)? (?:the )?(?:maximum |worst[- ]case )?regret(?:.*?)(?:by choosing|with|is))\s+{re.escape(act)}",
            ]
            for pat in patterns:
                match = re.search(pat, new_text, re.IGNORECASE)
                if match:
                    old_phrase = match.group(0)
                    new_phrase = old_phrase.replace(act, correct_act)
                    new_text = new_text.replace(old_phrase, new_phrase)
                    changes.append(f"Fixed minimax regret in {field_name}: {act} -> {correct_act}")

        for i, act in enumerate(acts):
            correct_regret = max_regrets[i]
            pat = rf"(maximum regret (?:for|of) {re.escape(act)}(?:\s*(?:is|=|:))\s*)-?[0-9.]+"
            new_text, n = re.subn(
                pat, rf"\g<1>{correct_regret:.0f}", new_text, flags=re.IGNORECASE
            )
            if n > 0:
                changes.append(f"Fixed max regret for {act} in {field_name}")

        if new_text != text:
            set_sf(record, field_name, new_text)

    return changes


def fix_maximin_record(record: dict, matrix: dict) -> list[str]:
    changes = []
    payoffs = matrix["payoffs"]
    acts = matrix["acts"]

    best_idx = solve_maximin(payoffs)
    correct_act = acts[best_idx]

    for field_name in ["why_right", "why_wrong", "pattern_description"]:
        text = get_sf(record, field_name)
        if not text:
            continue

        new_text = text
        for i, act in enumerate(acts):
            if i == best_idx:
                continue
            patterns = [
                rf"(maximin (?:rule )?(?:recommends?|selects?|chooses?|suggests?))\s+{re.escape(act)}",
                rf"(best (?:option|act|choice) (?:under|by|for) maximin is)\s+{re.escape(act)}",
                rf"(maximize(?:s)? (?:the )?(?:minimum |worst[- ]case )?(?:payoff|outcome)(?:.*?)(?:by choosing|with|is))\s+{re.escape(act)}",
            ]
            for pat in patterns:
                match = re.search(pat, new_text, re.IGNORECASE)
                if match:
                    old_phrase = match.group(0)
                    new_phrase = old_phrase.replace(act, correct_act)
                    new_text = new_text.replace(old_phrase, new_phrase)
                    changes.append(f"Fixed maximin in {field_name}: {act} -> {correct_act}")

        if new_text != text:
            set_sf(record, field_name, new_text)

    return changes


def fix_nash_record(record: dict, game: dict) -> list[str]:
    changes = []
    strategies = game["strategies"]
    equilibria = find_pure_nash(game["row_payoffs"], game["col_payoffs"])
    correct_eq = [(strategies[i], strategies[j]) for i, j in equilibria]
    correct_eq_str = format_nash_equilibria(correct_eq)

    eq_list_str = "[" + ", ".join(f"('{s1}', '{s2}')" for s1, s2 in correct_eq) + "]"
    if not correct_eq:
        eq_list_str = "none (no pure-strategy equilibrium)"

    # Fix formal_form
    ff = get_sf(record, "formal_form") or ""
    if ff:
        nash_patterns = [
            r"((?:Pure[- ]?[Ss]trategy )?[Nn]ash [Ee]quilibri(?:um|a)\s*[:=]\s*)(\[.*?\])",
            r"(NE\s*[:=]\s*)(\[.*?\])",
            r"((?:Pure )?[Ee]quilibri(?:um|a)\s*[:=]\s*)(\[.*?\])",
        ]
        for pat in nash_patterns:
            match = re.search(pat, ff)
            if match:
                old_eq = match.group(2)
                new_ff = ff[:match.start(2)] + eq_list_str + ff[match.end(2):]
                set_sf(record, "formal_form", new_ff)
                changes.append(f"Fixed Nash in formal_form: {old_eq} -> {eq_list_str}")
                break

    # Fix text fields
    for field_name in ["why_right", "why_wrong", "pattern_description"]:
        text = get_sf(record, field_name)
        if not text:
            continue

        new_text = text
        # Match various Nash equilibrium claim patterns
        nash_text_patterns = [
            r"(?:pure[- ]strategy )?Nash equilibri(?:um|a) (?:is|are) (?:at )?\([^)]+,\s*[^)]+\)(?:\s*and\s*\([^)]+,\s*[^)]+\))*",
            r"(?:the )?NE (?:is|are) (?:at )?\([^)]+,\s*[^)]+\)",
        ]
        for pat in nash_text_patterns:
            if re.search(pat, new_text, re.IGNORECASE):
                new_text = re.sub(
                    pat, correct_eq_str, new_text, count=1, flags=re.IGNORECASE
                )
                changes.append(f"Fixed Nash claim in {field_name}")
                break

        eq_at_pat = r"equilibri(?:um|a) at \([^)]+,\s*[^)]+\)"
        if re.search(eq_at_pat, new_text, re.IGNORECASE):
            replacement = correct_eq_str.replace("the Nash ", "")
            new_text = re.sub(
                eq_at_pat, replacement, new_text, count=1, flags=re.IGNORECASE
            )
            changes.append(f"Fixed equilibrium reference in {field_name}")

        if new_text != text:
            set_sf(record, field_name, new_text)

    return changes


# ─── Main processing ────────────────────────────────────────────────────────

def process_file(filepath: Path, dry_run: bool = True) -> tuple[int, int]:
    records = read_jsonl_raw(filepath)
    fixes_attempted = 0
    fixes_applied = 0
    modified = False

    for record in records:
        rid = record.get("id", "")
        if rid not in FAILING_IDS:
            continue

        fixes_attempted += 1
        code = record.get("taxonomy_code", "")
        formal_form = get_sf(record, "formal_form") or ""
        changes = []

        if code.startswith(("B3.", "B2.")):
            matrix = parse_decision_matrix(formal_form)
            if matrix:
                changes = fix_meu_record(record, matrix)

        elif code == "B1.5":
            matrix = parse_decision_matrix(formal_form)
            if matrix:
                changes = fix_minimax_regret_record(record, matrix)

        elif code == "B1.4":
            matrix = parse_decision_matrix(formal_form)
            if matrix:
                changes = fix_maximin_record(record, matrix)

        elif code.startswith(("B6.", "B7.", "B8.")):
            game = parse_2x2_game(formal_form)
            if game:
                changes = fix_nash_record(record, game)

        if changes:
            fixes_applied += 1
            modified = True
            status = "WOULD FIX" if dry_run else "FIXED"
            print(f"\n  {status}: {rid} ({code})")
            for c in changes:
                print(f"    - {c}")
        else:
            print(f"\n  NO AUTO-FIX: {rid} ({code}) -- needs manual review")

    if not dry_run and modified:
        write_jsonl_raw(records, filepath)
        print(f"\n  >> Wrote {filepath.name}")

    return fixes_attempted, fixes_applied


def main():
    parser = argparse.ArgumentParser(description="Fix mechanical verification failures")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Show what would change")
    group.add_argument("--apply", action="store_true", help="Apply fixes in place")
    args = parser.parse_args()

    dry_run = args.dry_run
    mode = "DRY RUN" if dry_run else "APPLYING FIXES"
    print(f"\n{'='*60}")
    print(f"MECHANICAL FAILURE FIX -- {mode}")
    print(f"{'='*60}")
    print(f"Target: {len(FAILING_IDS)} known failing records across {len(TARGET_FILES)} files\n")

    total_attempted = 0
    total_applied = 0

    for filename in TARGET_FILES:
        filepath = CORPUS_OUTPUT_DIR / filename
        if not filepath.exists():
            print(f"SKIP: {filename} not found")
            continue

        print(f"\n--- {filename} ---")
        attempted, applied = process_file(filepath, dry_run=dry_run)
        total_attempted += attempted
        total_applied += applied

    print(f"\n{'='*60}")
    print(f"SUMMARY: {total_applied}/{total_attempted} records {'would be' if dry_run else ''} fixed")
    unfixed = total_attempted - total_applied
    if unfixed > 0:
        print(f"  {unfixed} records need manual review (text patterns didn't match)")
    if not dry_run:
        print(f"\nRun verification to confirm: python3 05_mechanical_verify.py --all --report")
    print()


if __name__ == "__main__":
    main()
