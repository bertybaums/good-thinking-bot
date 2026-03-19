"""
Prompt templates for Pipeline 1: Anchor Crafting.

These prompts guide Opus in generating high-quality anchor examples
from source material. Each anchor defines the quality bar for its
taxonomy code.
"""

SYSTEM_PROMPT = """\
You are an expert in logic, critical thinking, decision theory, game theory, \
and cognitive science. You are helping build a training corpus for an \
educational game that teaches good thinking through NPC interactions.

Your task is to create exemplary training examples that will serve as \
"anchor" examples — the gold standard that all other generated examples \
are measured against.

Each example must be:
- Pedagogically sound (follows the ideal-to-real arc: formal framework → \
paradox/real case → practical wisdom)
- Accurately classified (correct taxonomy code and pattern type)
- Engaging (suitable for game NPC dialogue, not dry textbook prose)
- Multi-layered (works at the assigned difficulty tier)
- Self-contained (all context needed is in the example)

Output valid JSON matching the corpus schema exactly. No markdown wrapping.\
"""


def anchor_from_source(
    taxonomy_code: str,
    taxonomy_label: str,
    pattern_type: str,
    track: str,
    description: str,
    source_passage: str,
    difficulty_tier: str,
) -> str:
    """Generate a prompt for creating an anchor example from source material."""
    return f"""\
Create a training corpus record for the following reasoning pattern.

## Taxonomy Entry
- **Code:** {taxonomy_code}
- **Label:** {taxonomy_label}
- **Pattern type:** {pattern_type}
- **Track:** {track}
- **Description:** {description}

## Source Material
{source_passage}

## Requirements
- **Difficulty tier:** {difficulty_tier}
- Create a realistic scenario that a game NPC could present
- The scenario should naturally illustrate this specific pattern
- For "bad_thinking" patterns: the NPC commits the error; the player must identify it
- For "good_tool" patterns: the NPC demonstrates good reasoning; the player learns from it
- For "dual" patterns: show both the value and the limitations

## Output Format
Return a single JSON object with these fields:
{{
  "id": "{taxonomy_code}-001",
  "taxonomy_code": "{taxonomy_code}",
  "taxonomy_label": "{taxonomy_label}",
  "track": "{track}",
  "pattern_type": "{pattern_type}",
  "difficulty_tier": "{difficulty_tier}",
  "scenario": {{
    "context": "Setting/situation description",
    "text": "The actual argument or reasoning to analyze",
    "speaker_context": "NPC identity"
  }},
  "structure": {{
    "pattern_name": "Specific variant name",
    "pattern_description": "What is happening and why",
    "formal_form": "Schematic form if applicable, else null",
    "why_wrong": "For bad_thinking patterns, else null",
    "why_right": "For good_tool patterns, else null",
    "related_patterns": ["other taxonomy codes"],
    "counterpoint": "Edge case or exception"
  }},
  "assessment": {{
    "identification_prompt": "Question to probe understanding",
    "rubric": [
      {{"level": 0, "description": "No recognition"}},
      {{"level": 1, "description": "Vague awareness"}},
      {{"level": 2, "description": "Identifies the pattern"}},
      {{"level": 3, "description": "Explains the mechanism"}},
      {{"level": 4, "description": "Applies to novel cases"}}
    ],
    "follow_up_if_wrong": "Socratic redirect",
    "follow_up_if_right": "Deepening question"
  }},
  "game_hooks": {{
    "npc_personality": "Character sketch",
    "npc_dialogue_seed": "Opening line",
    "resolution_path": "What happens when player succeeds"
  }},
  "source": {{
    "type": "hand_crafted",
    "source_material": "Reference to origin",
    "original_id": null
  }}
}}\
"""


def anchor_revision(
    original_json: str,
    feedback: str,
) -> str:
    """Generate a prompt for revising an anchor based on expert feedback."""
    return f"""\
Revise this training corpus record based on expert feedback.

## Current Record
{original_json}

## Expert Feedback
{feedback}

## Instructions
- Address all feedback points
- Maintain the same taxonomy code and track
- Keep the JSON structure identical
- Return the complete revised JSON object (not just the changed parts)

Return valid JSON only, no markdown wrapping.\
"""


def anchor_batch_plan(
    codes_with_sources: list[dict],
) -> str:
    """Generate a prompt for planning which anchor examples to create first."""
    code_list = "\n".join(
        f"- {c['code']}: {c['label']} ({c['pattern_type']})"
        for c in codes_with_sources
    )
    return f"""\
I need to create anchor examples for the following taxonomy codes. \
For each one, suggest:
1. The best difficulty tier to start with
2. Which source material passage to use as the seed
3. A one-sentence sketch of the scenario

## Codes
{code_list}

Return a JSON array of objects with fields: \
code, tier, source_reference, scenario_sketch.\
"""
