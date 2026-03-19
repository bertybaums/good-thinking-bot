"""
Prompt templates for Pipeline 3: Synthetic Generation.

These prompts guide MindRouter in generating new examples for taxonomy
codes that lack sufficient coverage, especially decision theory, game theory,
cognitive biases, and integrated scenarios.
"""

SYSTEM_PROMPT = """\
You are generating training examples for an educational game that teaches \
critical thinking, decision theory, and economics through NPC interactions.

Each example must be:
- Accurately illustrating the specified reasoning pattern
- Set in a concrete, relatable scenario (not abstract philosophy)
- Appropriate for the assigned difficulty tier
- Self-contained with all necessary context

For decision theory and game theory examples, include precise numerical \
values so answers can be mechanically verified.

Output valid JSON matching the corpus schema exactly. No markdown wrapping.\
"""


def generate_synthetic(
    taxonomy_code: str,
    taxonomy_label: str,
    pattern_type: str,
    track: str,
    description: str,
    difficulty_tier: str,
    domain_constraint: str,
    anchor_examples: str,
    record_id: str,
) -> str:
    """Generate a new synthetic example for a taxonomy code."""
    return f"""\
Generate a new training corpus example for the following reasoning pattern.

## Taxonomy Entry
- **Code:** {taxonomy_code}
- **Label:** {taxonomy_label}
- **Pattern type:** {pattern_type}
- **Track:** {track}
- **Description:** {description}

## Domain Constraint
Set this example in the following domain: {domain_constraint}

## Difficulty Tier
{difficulty_tier}
- "drill": Apply the concept mechanically. Clear-cut case.
- "what_if": Stress-test or connect concepts. Moderate ambiguity.
- "puzzle": Genuine philosophical engagement. Real tension.

## Anchor Examples (for quality and style reference)
{anchor_examples}

## Instructions
1. Create a realistic, engaging scenario in the specified domain
2. For quantitative patterns (decision theory, game theory, probability): \
include precise numbers so answers can be mechanically verified
3. The scenario should feel like something a game NPC would say
4. Make the assessment questions Socratic, not quiz-like

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
    "text": "...",
    "speaker_context": "..."
  }},
  "structure": {{
    "pattern_name": "...",
    "pattern_description": "...",
    "formal_form": "... (include decision matrix or game tree if applicable)",
    "why_wrong": "... or null",
    "why_right": "... or null",
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
    "type": "synthetic_verified",
    "source_material": "Generated from taxonomy definition + anchor examples",
    "original_id": null
  }}
}}\
"""


def generate_decision_theory(
    taxonomy_code: str,
    taxonomy_label: str,
    description: str,
    difficulty_tier: str,
    domain_constraint: str,
    seed_problem: str,
    record_id: str,
) -> str:
    """
    Specialized prompt for decision theory examples.
    Requires precise numerical structure for mechanical verification.
    """
    return f"""\
Generate a decision theory training example based on the seed problem below.

## Taxonomy
- **Code:** {taxonomy_code}
- **Label:** {taxonomy_label}
- **Description:** {description}

## Seed Problem (vary the domain but preserve the mathematical structure)
{seed_problem}

## Domain
Set this in: {domain_constraint}

## Difficulty: {difficulty_tier}

## Critical Requirements
1. Include a complete decision matrix or game tree with EXACT numerical values
2. The correct answer must be computable from the numbers given
3. Show the computation steps in structure.pattern_description
4. Include the formal_form field with the matrix/tree representation

For decision matrices, use this format in formal_form:
"Acts: [A1, A2, ...]; States: [S1 (p=X), S2 (p=Y), ...]; Payoffs: A1|S1=V1, A1|S2=V2, ..."

Return a single JSON corpus record with id="{record_id}".\
"""


def generate_bias_scenario(
    taxonomy_code: str,
    taxonomy_label: str,
    description: str,
    difficulty_tier: str,
    domain_constraint: str,
    record_id: str,
) -> str:
    """Specialized prompt for cognitive bias examples."""
    return f"""\
Generate a cognitive bias training example.

## Bias
- **Code:** {taxonomy_code}
- **Label:** {taxonomy_label}
- **Description:** {description}

## Domain: {domain_constraint}
## Difficulty: {difficulty_tier}

## Instructions
1. Create a scenario where a character exhibits this bias naturally
2. The bias should be subtle enough to be realistic but clear enough to identify
3. Include a concrete behavioral choice that reveals the bias
4. The NPC should NOT name the bias — the player must recognize it
5. The assessment should guide discovery, not test recall

For the structure fields:
- pattern_description: Explain how the bias manifests in this specific scenario
- why_wrong: Explain how the bias leads to a suboptimal judgment or decision
- counterpoint: Note when this heuristic might actually be useful (if applicable)

Return a single JSON corpus record with id="{record_id}".\
"""
