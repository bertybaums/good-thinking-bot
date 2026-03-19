"""
Prompt templates for Pipeline 2: Dataset Adaptation.

These prompts guide MindRouter in enriching existing dataset examples
with the full corpus schema fields (structure, assessment, game_hooks).
"""

SYSTEM_PROMPT = """\
You are enriching existing logic and reasoning dataset examples for use in \
an educational game. You will receive an example from an existing dataset \
(with its text and classification) and must add structured fields for \
pedagogical assessment and game integration.

Your output must be valid JSON matching the corpus schema exactly. \
Be precise with taxonomy codes and pattern types. \
No markdown wrapping.\
"""


def enrich_existing(
    original_text: str,
    original_label: str,
    taxonomy_code: str,
    taxonomy_label: str,
    pattern_type: str,
    track: str,
    description: str,
    difficulty_tier: str,
    anchor_examples: str,
    record_id: str,
    source_dataset: str,
    original_id: str | None = None,
) -> str:
    """Enrich an existing dataset example with full corpus schema fields."""
    return f"""\
Enrich the following existing dataset example into a full training corpus record.

## Original Example
- **Source dataset:** {source_dataset}
- **Original text:** {original_text}
- **Original label:** {original_label}

## Target Taxonomy
- **Code:** {taxonomy_code}
- **Label:** {taxonomy_label}
- **Pattern type:** {pattern_type}
- **Track:** {track}
- **Description:** {description}

## Anchor Examples (for quality reference)
{anchor_examples}

## Instructions
1. Keep the original text as the scenario text (lightly edit for clarity if needed)
2. Add a realistic game context and NPC speaker
3. Fill in the structure fields (pattern_name, description, formal_form, etc.)
4. Create assessment scaffolding (identification_prompt, rubric, follow-ups)
5. Create game hooks (npc_personality, dialogue_seed, resolution_path)
6. Set difficulty_tier to: {difficulty_tier}

Return a single JSON object:
{{
  "id": "{record_id}",
  "taxonomy_code": "{taxonomy_code}",
  "taxonomy_label": "{taxonomy_label}",
  "track": "{track}",
  "pattern_type": "{pattern_type}",
  "difficulty_tier": "{difficulty_tier}",
  "scenario": {{
    "context": "...",
    "text": "{original_text[:200]}...",
    "speaker_context": "..."
  }},
  "structure": {{
    "pattern_name": "...",
    "pattern_description": "...",
    "formal_form": null,
    "why_wrong": "...",
    "why_right": null,
    "related_patterns": [],
    "counterpoint": "..."
  }},
  "assessment": {{
    "identification_prompt": "...",
    "rubric": [
      {{"level": 0, "description": "..."}},
      {{"level": 1, "description": "..."}},
      {{"level": 2, "description": "..."}},
      {{"level": 3, "description": "..."}},
      {{"level": 4, "description": "..."}}
    ],
    "follow_up_if_wrong": "...",
    "follow_up_if_right": "..."
  }},
  "game_hooks": {{
    "npc_personality": "...",
    "npc_dialogue_seed": "...",
    "resolution_path": "..."
  }},
  "source": {{
    "type": "existing_dataset",
    "source_material": "{source_dataset}",
    "original_id": {f'"{original_id}"' if original_id else 'null'}
  }}
}}\
"""
