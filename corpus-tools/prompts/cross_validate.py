"""
Prompt templates for Pipeline 4: Cross-Validation.

These prompts ask a separate LLM to classify examples WITHOUT seeing the
assigned taxonomy code, then compare to the intended classification.
Disagreements are flagged for expert review.
"""

SYSTEM_PROMPT = """\
You are a reasoning pattern classifier. You will receive a scenario \
containing an argument, decision, or reasoning pattern. Your job is to:

1. Identify the PRIMARY reasoning pattern or fallacy being demonstrated
2. Classify it using the provided taxonomy
3. Assess the difficulty level
4. Rate your confidence

Be precise. Many patterns are similar — distinguish carefully. \
For example, distinguish ad hominem from genetic fallacy, or \
straw man from false dichotomy.

Output valid JSON only. No markdown wrapping.\
"""


def classify_scenario(
    scenario_text: str,
    scenario_context: str,
    taxonomy_options: str,
) -> str:
    """Ask the classifier to identify the reasoning pattern in a scenario."""
    return f"""\
Classify the reasoning pattern in the following scenario.

## Scenario
**Context:** {scenario_context}
**Text:** {scenario_text}

## Available Taxonomy Codes
{taxonomy_options}

## Instructions
Identify the PRIMARY reasoning pattern. Return:
{{
  "predicted_code": "the taxonomy code (e.g. A7.1)",
  "predicted_label": "the pattern name",
  "predicted_pattern_type": "good_tool | bad_thinking | dual",
  "predicted_difficulty": "drill | what_if | puzzle",
  "confidence": 0.0 to 1.0,
  "reasoning": "Brief explanation of why you chose this classification",
  "alternative_codes": ["other plausible codes, if any"]
}}\
"""


def classify_batch_header(taxonomy_options: str) -> str:
    """System prompt variant that includes the taxonomy for batch processing."""
    return f"""\
You are a reasoning pattern classifier. Classify each scenario using this taxonomy:

{taxonomy_options}

For each scenario, return a JSON object with:
- predicted_code, predicted_label, predicted_pattern_type
- predicted_difficulty (drill/what_if/puzzle)
- confidence (0.0-1.0)
- reasoning (brief)
- alternative_codes (list)

Output valid JSON only.\
"""
