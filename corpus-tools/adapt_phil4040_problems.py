#!/usr/bin/env python3
"""
Extract Type 1 (Drill) and Type 2 (What-If) problems from PHIL 4040 lecture notes
and convert them into CorpusRecord-format JSONL records.

No API calls — runs entirely locally by parsing problem text from markdown files.

Usage:
    python3 adapt_phil4040_problems.py              # Process all lectures
    python3 adapt_phil4040_problems.py --week W10   # Process one week
    python3 adapt_phil4040_problems.py --dry-run    # Show what would be extracted
"""

import argparse
import json
import re
import sys
from pathlib import Path

from config import CORPUS_OUTPUT_DIR

RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources" / "rationality-and-strategic-interactions"

# Lecture files to process (skip W9_notes-for-students duplicate and W16 review)
LECTURE_FILES = [
    "W9_The_Prisoners_Dilemma_and_the_Structure_of_Games.md",
    "W10_Nash_Equilibrium_Coordination_and_Convention.md",
    "W11_Mixed_Strategies_and_Zero_Sum_Games.md",
    "W12_Sequential_Games_Backwards_Induction_and_Signaling.md",
    "W13_Behavioral_Game_Theory.md",
    "W14_Repeated_Games_Evolutionary_Dynamics_and_Cooperation.md",
    "W15_Social_Choice_Arrows_Theorem_and_the_Moral_First_Aid_Manual.md",
]

# Keywords → taxonomy code mapping for problem classification
CODE_KEYWORDS = [
    # Order matters — more specific patterns first
    (r"Condorcet|cyclical.*preference|pairwise.*vote", "B15.1"),
    (r"Arrow.s|impossibility|five conditions|IIA.*voting|Universal Domain", "B15.2"),
    (r"voting system|plurality|Borda|IRV|instant runoff|approval voting|Gibbard|strategic vot", "B15.3"),
    (r"Folk Theorem|Grim Trigger|discount factor|delta\s*[><=*]|infinitely repeated|indefinitely repeated", "B10.5"),
    (r"level[- ]k|level[- ][0-9]|beauty contest|p-beauty|guess.*average", "B13.1"),
    (r"Fehr.Schmidt|inequality aversion|Bolton.Ockenfels|Charness.Rabin|social preference|fairness model", "B13.2"),
    (r"signal|separating equilibrium|pooling equilibrium|Spence|Zahavi|handicap principle|cheap talk|costly signal", "B8.5"),
    (r"commitment device|Odysseus|burning bridge|credible threat|incredible threat|binding.*future", "B8.6"),
    (r"Hawk.Dove|hawk.*dove|escalat.*resource|V\s*[<>]\s*C", "B7.5"),
    (r"Ultimatum|ultimatum game|Trust Game|proposer.*responder|investor.*trustee", "B7.6"),
    (r"Public Goods|public good|free.rid|altruistic punishment|contribute.*pool", "B7.7"),
    (r"zero.sum|minimax theorem|von Neumann|maximin.*game|constant.sum", "B6.4"),
    (r"mixed strateg|indifference principle|randomiz|mixing probabilit", "B6.5"),
    (r"dominat.*strateg|iterated.*eliminat|strictly dominat|weakly dominat|IESDS", "B6.6"),
    (r"Pareto efficien|Pareto improv|Pareto dominat|Pareto optimal", "C1.3"),
    (r"Stag Hunt|payoff dominan|risk dominan", "B7.1"),
    (r"Battle of the Sexes|coordination conflict", "B7.2"),
    (r"focal point|Schelling|salien", "B7.3"),
    (r"Lewis.*condition|convention.*condition|Lewis.*convention", "B7.4"),
    (r"backward induction|backwards induction|game tree|extensive form|subgame perfect", "B8.2"),
    (r"Prisoner.s Dilemma|PD.*payoff|T\s*>\s*R\s*>\s*P\s*>\s*S", "B6.1"),
    (r"Nash [Ee]quilibri|best.response|NE\b|pure strategy", "B6.2"),
    (r"[Pp]rospect [Tt]heory|loss aversion|reference point|PT.*payoff|value function", "B5.1"),
    (r"Centipede", "B8.4"),
    (r"Tit.for.Tat|TFT|Axelrod|iterated PD|repeated PD", "B6.3"),
]

# Default rubric template
DEFAULT_RUBRIC = [
    {"level": 0, "description": "No attempt or completely incorrect approach"},
    {"level": 1, "description": "Shows some understanding but major errors in application"},
    {"level": 2, "description": "Correct general approach with some computational or conceptual errors"},
    {"level": 3, "description": "Correct analysis with minor gaps in explanation"},
    {"level": 4, "description": "Complete, correct analysis with clear explanation of reasoning"},
]


def extract_week(filename: str) -> str:
    """Extract week number from filename."""
    m = re.match(r"(W\d+)", filename)
    return m.group(1) if m else "W?"


def classify_problem(text: str) -> str:
    """Classify a problem's taxonomy code based on keyword matching."""
    for pattern, code in CODE_KEYWORDS:
        if re.search(pattern, text, re.IGNORECASE):
            return code
    return "B6.2"  # default to Nash equilibrium


def extract_problems(filepath: Path) -> list[dict]:
    """Extract Type 1 and Type 2 problems from a lecture markdown file."""
    text = filepath.read_text(encoding="utf-8")
    week = extract_week(filepath.name)
    problems = []

    # Find the problem set section
    ps_match = re.search(r"^## .*Problem Set.*$", text, re.MULTILINE)
    if not ps_match:
        return problems

    ps_text = text[ps_match.start():]

    # Extract Type 1 and Type 2 sections
    for type_num, tier in [(1, "drill"), (2, "what_if")]:
        type_label = "Type 1" if type_num == 1 else "Type 2"
        # Find section boundaries
        start_pat = rf"^### {type_label}.*$"
        next_pat = r"^### Type [2-9]|^### Type [1-9][0-9]|^---\s*$|^## "

        start_m = re.search(start_pat, ps_text, re.MULTILINE)
        if not start_m:
            continue

        section_start = start_m.end()
        end_m = re.search(next_pat, ps_text[section_start:], re.MULTILINE)
        section_end = section_start + end_m.start() if end_m else len(ps_text)
        section = ps_text[section_start:section_end].strip()

        # Extract individual problems
        prob_splits = re.split(r"(?=^\*\*\d+\.)", section, flags=re.MULTILINE)

        for prob_text in prob_splits:
            prob_text = prob_text.strip()
            if not prob_text or not re.match(r"\*\*\d+\.", prob_text):
                continue

            # Get problem number and title
            title_m = re.match(r"\*\*(\d+)\.\s*(.*?)\*\*", prob_text)
            if not title_m:
                continue
            prob_num = title_m.group(1)
            prob_title = title_m.group(2).strip()

            # Check for sub-problems (a), (b), (c)
            sub_parts = re.split(r"(?=^\*\*\([a-z]\)\*\*)", prob_text, flags=re.MULTILINE)

            if len(sub_parts) > 1:
                # Has sub-problems — get the preamble (shared context)
                preamble = sub_parts[0].strip()
                for sub in sub_parts[1:]:
                    sub = sub.strip()
                    if not sub:
                        continue
                    sub_m = re.match(r"\*\*\(([a-z])\)\*\*", sub)
                    sub_letter = sub_m.group(1) if sub_m else "x"

                    full_text = preamble + "\n\n" + sub
                    code = classify_problem(full_text)

                    problems.append({
                        "week": week,
                        "problem_num": prob_num,
                        "sub_part": sub_letter,
                        "title": prob_title,
                        "tier": tier,
                        "text": full_text,
                        "sub_text": sub,
                        "code": code,
                    })
            else:
                # Single problem, no sub-parts
                code = classify_problem(prob_text)
                problems.append({
                    "week": week,
                    "problem_num": prob_num,
                    "sub_part": None,
                    "title": prob_title,
                    "tier": tier,
                    "text": prob_text,
                    "sub_text": None,
                    "code": code,
                })

    return problems


def extract_formal_form(text: str) -> str | None:
    """Try to extract a payoff matrix from markdown table format."""
    # Look for markdown tables with payoff pairs
    tables = re.findall(
        r"(\|[^\n]*\|\n\|[-| :]+\|\n(?:\|[^\n]*\|\n)+)", text
    )
    if tables:
        return tables[0].strip()
    return None


def problem_to_record(prob: dict) -> dict:
    """Convert an extracted problem to a CorpusRecord dict."""
    code = prob["code"]
    week = prob["week"]
    num = prob["problem_num"]
    sub = prob["sub_part"]

    # Build ID
    id_suffix = f"{num}{sub}" if sub else num
    record_id = f"{code}-P4040{week}-{id_suffix}"

    # Get taxonomy label from the code
    try:
        from taxonomy import TAXONOMY
        tax_entry = TAXONOMY.get(code, {})
        label = tax_entry.get("label", code)
        track = tax_entry.get("track", "game_theory")
        pattern_type = tax_entry.get("pattern_type", "good_tool")
    except ImportError:
        label = code
        track = "game_theory"
        pattern_type = "good_tool"

    # Extract formal form (payoff matrix) if present
    formal_form = extract_formal_form(prob["text"])

    # Build scenario
    title = prob["title"]
    main_text = prob["sub_text"] if prob["sub_text"] else prob["text"]
    # Strip the bold problem number header from text
    main_text = re.sub(r"^\*\*\d+\..*?\*\*\s*\n?", "", main_text).strip()
    main_text = re.sub(r"^\*\*\([a-z]\)\*\*\s*", "", main_text).strip()

    # Build why_right / why_wrong based on pattern_type
    why_right = None
    why_wrong = None
    if pattern_type in ("good_tool", "dual"):
        why_right = f"Correctly applying {label} demonstrates understanding of strategic reasoning and formal analysis."
    if pattern_type in ("bad_thinking", "dual"):
        why_wrong = f"Failing to recognize {label} leads to incorrect strategic predictions."

    record = {
        "id": record_id,
        "taxonomy_code": code,
        "taxonomy_label": label,
        "track": track,
        "pattern_type": pattern_type,
        "difficulty_tier": prob["tier"],
        "scenario": {
            "context": f"From a problem set on {title} ({week}, PHIL 4040 Rationality & Strategic Interactions).",
            "text": main_text,
            "speaker_context": "Professor Baumgaertner's problem set for decision theory and game theory students.",
        },
        "structure": {
            "pattern_name": label,
            "pattern_description": f"This problem tests the student's ability to apply {label} concepts. {tax_entry.get('description', '')[:200] if tax_entry else ''}",
            "formal_form": formal_form,
            "why_wrong": why_wrong,
            "why_right": why_right,
            "related_patterns": [],
            "counterpoint": None,
        },
        "assessment": {
            "identification_prompt": f"Work through this problem step by step. What concept from {label} is being tested here?",
            "rubric": DEFAULT_RUBRIC,
            "follow_up_if_wrong": "Let's start from the basics — what are each player's available strategies, and what do the payoffs tell us?",
            "follow_up_if_right": "Good. Can you connect this to a broader principle or another game structure we've studied?",
        },
        "game_hooks": {
            "npc_personality": "A patient instructor who values precise reasoning and asks probing follow-up questions.",
            "npc_dialogue_seed": f"Let's work through this {label} problem together. Take your time with the analysis.",
            "resolution_path": "The student demonstrates mastery by correctly completing the analysis and explaining their reasoning.",
        },
        "source": {
            "type": "existing_dataset",
            "source_material": f"Bert's PHIL 4040 lecture notes, {week}",
            "original_id": f"{week}-Problem{num}" + (sub or ""),
        },
    }

    return record


def validate_record(record: dict) -> bool:
    """Validate a record against the Pydantic schema."""
    try:
        from schema import CorpusRecord
        CorpusRecord.model_validate(record)
        return True
    except Exception as e:
        print(f"  Validation error for {record['id']}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Adapt PHIL 4040 problems to corpus format")
    parser.add_argument("--week", help="Process only this week (e.g., W10)")
    parser.add_argument("--dry-run", action="store_true", help="Show extraction without writing")
    args = parser.parse_args()

    # Select files to process
    files_to_process = []
    for fname in LECTURE_FILES:
        if args.week and not fname.startswith(args.week):
            continue
        fpath = RESOURCES_DIR / fname
        if fpath.exists():
            files_to_process.append(fpath)
        else:
            print(f"Warning: {fname} not found in {RESOURCES_DIR}")

    if not files_to_process:
        print("No lecture files to process.")
        return

    all_problems = []
    for fpath in files_to_process:
        week = extract_week(fpath.name)
        problems = extract_problems(fpath)
        print(f"{week} ({fpath.name}): {len(problems)} problems extracted")
        all_problems.extend(problems)

    print(f"\nTotal problems extracted: {len(all_problems)}")

    if args.dry_run:
        print("\n--- DRY RUN ---")
        from collections import Counter
        by_code = Counter(p["code"] for p in all_problems)
        by_tier = Counter(p["tier"] for p in all_problems)
        print(f"\nBy taxonomy code:")
        for code, count in sorted(by_code.items()):
            print(f"  {code}: {count}")
        print(f"\nBy difficulty tier:")
        for tier, count in sorted(by_tier.items()):
            print(f"  {tier}: {count}")
        print(f"\nProblems:")
        for p in all_problems:
            sub = f"({p['sub_part']})" if p["sub_part"] else ""
            print(f"  {p['week']} P{p['problem_num']}{sub} → {p['code']} [{p['tier']}] {p['title']}")
        return

    # Convert to records
    records = []
    valid = 0
    invalid = 0
    for prob in all_problems:
        record = problem_to_record(prob)
        if validate_record(record):
            records.append(record)
            valid += 1
        else:
            invalid += 1

    # Write output
    output_path = CORPUS_OUTPUT_DIR / "adapted_phil4040.jsonl"
    with open(output_path, "w") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"\nWrote {valid} valid records to {output_path.name}")
    if invalid:
        print(f"  {invalid} records failed validation")


if __name__ == "__main__":
    main()
