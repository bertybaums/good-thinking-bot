#!/usr/bin/env python3
"""
Good Thinking Bot — Interactive Critical Thinking Tutor

A Gradio-based educational app that teaches critical thinking, logic,
decision theory, and economics through scenario-based practice with
NPC characters.

Two modes:
  - Corpus-only (default): Shows scenarios from the training corpus,
    reveals correct answers after student submits. No GPU needed.
  - Model mode: Loads a fine-tuned model for real-time evaluation.
    Activated by setting MODEL_PATH environment variable.

Authors: Bert Baumgaertner & Nicholas Potter, University of Idaho
License: CC BY-NC-SA 4.0
"""

import json
import os
import random
from collections import defaultdict
from pathlib import Path

import gradio as gr

# ── Configuration ────────────────────────────────────────────────────────────

DATA_DIR = Path(__file__).resolve().parent / "data"
SCENARIOS_FILE = DATA_DIR / "scenarios.jsonl"
MODEL_PATH = os.environ.get("MODEL_PATH", "")

# ── Data Loading ─────────────────────────────────────────────────────────────

def load_scenarios() -> list[dict]:
    """Load all scenario records from the bundled JSONL file."""
    records = []
    if not SCENARIOS_FILE.exists():
        return records
    with open(SCENARIOS_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return records


SCENARIOS = load_scenarios()

# Build indexes
TRACK_LABELS = {
    "logic_critical_thinking": "Logic & Critical Thinking",
    "decision_theory": "Decision Theory",
    "game_theory": "Game Theory",
    "microeconomics": "Microeconomics",
    "dennett_tools": "Dennett's Thinking Tools",
    "cognitive_biases": "Cognitive Biases",
}

TIER_LABELS = {
    "drill": "Drill (apply mechanically)",
    "what_if": "What-If (stress-test, connect concepts)",
    "puzzle": "Puzzle (genuine philosophical engagement)",
}

# Index by taxonomy code
BY_CODE = defaultdict(list)
for s in SCENARIOS:
    BY_CODE[s["taxonomy_code"]].append(s)

# Build taxonomy code dropdown choices: "A7.1: Ad hominem"
CODE_CHOICES = sorted(
    set(f"{s['taxonomy_code']}: {s['taxonomy_label']}" for s in SCENARIOS)
)

# Unique tracks and tiers for filters
TRACK_CHOICES = ["All"] + [
    TRACK_LABELS.get(t, t)
    for t in sorted(set(s.get("track", "") for s in SCENARIOS))
    if t
]

TIER_CHOICES = ["All"] + [
    TIER_LABELS.get(t, t)
    for t in ["drill", "what_if", "puzzle"]
]


def filter_scenarios(track: str, tier: str) -> list[dict]:
    """Filter scenarios by track and difficulty tier."""
    pool = SCENARIOS
    if track != "All":
        track_key = next(
            (k for k, v in TRACK_LABELS.items() if v == track), track
        )
        pool = [s for s in pool if s.get("track") == track_key]
    if tier != "All":
        tier_key = next(
            (k for k, v in TIER_LABELS.items() if v == tier), tier
        )
        pool = [s for s in pool if s.get("difficulty_tier") == tier_key]
    return pool


# ── Score Display Helpers ────────────────────────────────────────────────────

def score_color(score: int) -> str:
    """Return a CSS color for the score."""
    if score <= 1:
        return "#d32f2f"  # red
    elif score == 2:
        return "#f9a825"  # yellow/amber
    else:
        return "#388e3c"  # green


def format_rubric(rubric: list[dict], highlight_level: int | None = None) -> str:
    """Format the rubric as HTML, optionally highlighting a level."""
    lines = []
    for r in sorted(rubric, key=lambda x: x["level"]):
        level = r["level"]
        desc = r["description"]
        color = score_color(level)
        if highlight_level is not None and level == highlight_level:
            lines.append(
                f'<div style="padding:6px 10px; margin:3px 0; '
                f'border-left:4px solid {color}; background:#2a2a2a;">'
                f'<strong style="color:{color}">Level {level}</strong>: {desc}</div>'
            )
        else:
            lines.append(
                f'<div style="padding:4px 10px; margin:2px 0; '
                f'border-left:3px solid #ccc; color:#666;">'
                f'Level {level}: {desc}</div>'
            )
    return "\n".join(lines)


def format_scenario_display(record: dict) -> str:
    """Format a scenario for display, including NPC character info."""
    scenario = record["scenario"]
    hooks = record.get("game_hooks", {})
    taxonomy_code = record.get("taxonomy_code", "")
    taxonomy_label = record.get("taxonomy_label", "")
    tier = record.get("difficulty_tier", "")
    tier_display = TIER_LABELS.get(tier, tier)
    track = record.get("track", "")
    track_display = TRACK_LABELS.get(track, track)

    npc_name = ""
    npc_personality = hooks.get("npc_personality", "")
    # Extract a name from the personality if possible
    if npc_personality:
        # Try to get the first sentence as a character intro
        first_sentence = npc_personality.split(".")[0].strip()
        npc_name = first_sentence

    dialogue_seed = hooks.get("npc_dialogue_seed", "")

    html = f"""
<div style="margin-bottom:16px;">
  <div style="display:flex; gap:12px; margin-bottom:10px; flex-wrap:wrap;">
    <span style="background:#e3f2fd; padding:3px 10px; border-radius:12px;
                 font-size:0.85em; color:#1565c0;">{track_display}</span>
    <span style="background:#f3e5f5; padding:3px 10px; border-radius:12px;
                 font-size:0.85em; color:#7b1fa2;">{tier_display}</span>
    <span style="background:#e8f5e9; padding:3px 10px; border-radius:12px;
                 font-size:0.85em; color:#2e7d32;">{taxonomy_code}: {taxonomy_label}</span>
  </div>
"""
    if npc_name:
        html += f"""
  <div style="background:#3e2723; border-left:4px solid #ff8f00; padding:10px 14px;
              margin-bottom:12px; border-radius:0 6px 6px 0;">
    <div style="font-size:0.85em; color:#ffb74d; margin-bottom:4px;">CHARACTER</div>
    <div style="font-style:italic; color:#ffe0b2;">{npc_name}</div>
  </div>
"""
    html += f"""
  <div style="background:#1b3a2a; padding:14px; border-radius:6px; margin-bottom:12px;
              border-left:4px solid #66bb6a;">
    <div style="font-size:0.85em; color:#81c784; margin-bottom:6px;">SETTING</div>
    <div style="color:#c8e6c9;">{scenario['context']}</div>
  </div>

  <div style="background:#0d253f; padding:14px; border-radius:6px; margin-bottom:12px;
              border-left:4px solid #42a5f5;">
    <div style="font-size:0.85em; color:#64b5f6; margin-bottom:6px;">WHAT HAPPENED</div>
    <div style="color:#bbdefb;">{scenario['text']}</div>
  </div>
"""
    if dialogue_seed:
        html += f"""
  <div style="background:#3e2723; padding:14px; border-radius:6px; margin-bottom:12px;
              border-left:4px solid #ff8f00; font-style:italic;">
    <div style="font-size:0.85em; color:#ffb74d; margin-bottom:6px;">NPC SAYS</div>
    <div style="color:#ffe0b2;">"{dialogue_seed}"</div>
  </div>
"""
    html += "</div>"
    return html


def format_question(record: dict) -> str:
    """Format the identification prompt as the question."""
    assessment = record.get("assessment", {})
    prompt = assessment.get("identification_prompt", "What is going on here?")
    return f"""
<div style="background:#0d253f; padding:16px; border-radius:8px;
            border-left:4px solid #42a5f5; margin:8px 0;">
  <div style="font-size:0.9em; color:#64b5f6; margin-bottom:6px; font-weight:600;">
    QUESTION</div>
  <div style="font-size:1.05em; color:#e3f2fd;">{prompt}</div>
</div>
"""


def format_feedback(record: dict, student_response: str) -> str:
    """
    Generate feedback based on the corpus record.

    In corpus-only mode, we reveal the correct answer and let the student
    self-assess. In model mode (future), the model would score the response.
    """
    structure = record.get("structure", {})
    assessment = record.get("assessment", {})
    rubric = assessment.get("rubric", [])
    pattern_type = record.get("pattern_type", "")

    # In corpus-only mode, we show the full analysis without auto-scoring
    # The student can self-assess against the rubric
    explanation = structure.get("why_wrong") or structure.get("why_right") or ""
    pattern_name = structure.get("pattern_name", "")
    pattern_desc = structure.get("pattern_description", "")
    formal_form = structure.get("formal_form", "")
    counterpoint = structure.get("counterpoint", "")
    follow_right = assessment.get("follow_up_if_right", "")
    follow_wrong = assessment.get("follow_up_if_wrong", "")

    html = """
<div style="margin-top:12px;">
  <h3 style="color:#1565c0; border-bottom:2px solid #e3f2fd; padding-bottom:6px;">
    Analysis</h3>
"""
    # Pattern name and description
    html += f"""
  <div style="background:#1b3a2a; padding:14px; border-radius:6px; margin-bottom:12px;">
    <div style="font-weight:600; color:#81c784; font-size:1.05em; margin-bottom:6px;">
      {pattern_name}</div>
    <div style="color:#c8e6c9;">{pattern_desc}</div>
  </div>
"""
    # Why wrong / why right
    if explanation:
        label = "Why this is problematic" if pattern_type == "bad_thinking" else "Why this works"
        color = "#c62828" if pattern_type == "bad_thinking" else "#2e7d32"
        html += f"""
  <div style="padding:10px 14px; margin-bottom:10px; border-left:4px solid {color};
              background:#2a2a2a; border-radius:0 6px 6px 0;">
    <div style="font-size:0.85em; color:{color}; margin-bottom:4px; font-weight:600;">
      {label}</div>
    <div style="color:#e0e0e0;">{explanation}</div>
  </div>
"""
    # Formal form
    if formal_form:
        html += f"""
  <div style="background:#1a1a2e; padding:10px 14px; margin-bottom:10px;
              border-radius:6px; font-family:monospace; font-size:0.9em;">
    <div style="font-size:0.85em; color:#666; margin-bottom:4px;">FORMAL STRUCTURE</div>
    <span style="color:#b0bec5;">{formal_form}</span>
  </div>
"""
    # Counterpoint
    if counterpoint:
        html += f"""
  <div style="background:#3e2723; padding:10px 14px; margin-bottom:10px;
              border-left:4px solid #ef6c00; border-radius:0 6px 6px 0;">
    <div style="font-size:0.85em; color:#e65100; margin-bottom:4px; font-weight:600;">
      Nuance / Edge Case</div>
    <div style="color:#ffe0b2;">{counterpoint}</div>
  </div>
"""
    # Rubric for self-assessment
    html += """
  <h3 style="color:#1565c0; border-bottom:2px solid #e3f2fd; padding-bottom:6px;
             margin-top:16px;">
    Self-Assessment Rubric</h3>
  <p style="color:#666; font-size:0.9em;">
    Compare your response to the rubric below. Where does your analysis fall?</p>
"""
    html += format_rubric(rubric)

    # Follow-up questions
    html += """
  <h3 style="color:#1565c0; border-bottom:2px solid #e3f2fd; padding-bottom:6px;
             margin-top:16px;">
    Follow-Up Questions</h3>
"""
    if follow_wrong:
        html += f"""
  <div style="padding:10px 14px; margin-bottom:8px; background:#3b1515;
              border-radius:6px;">
    <div style="font-size:0.85em; color:#c62828; margin-bottom:4px; font-weight:600;">
      If you struggled with this one</div>
    <div style="color:#ef9a9a;">{follow_wrong}</div>
  </div>
"""
    if follow_right:
        html += f"""
  <div style="padding:10px 14px; margin-bottom:8px; background:#e8f5e9;
              border-radius:6px;">
    <div style="font-size:0.85em; color:#2e7d32; margin-bottom:4px; font-weight:600;">
      If you got it right — go deeper</div>
    <div style="color:#c8e6c9;">{follow_right}</div>
  </div>
"""
    html += "</div>"
    return html


# ── Tab 1: Interactive Tutor ─────────────────────────────────────────────────

def get_random_scenario(track: str, tier: str) -> tuple[str, str, dict]:
    """Pick a random scenario and return (scenario_html, question_html, record)."""
    pool = filter_scenarios(track, tier)
    if not pool:
        return (
            "<p style='color:#c62828;'>No scenarios match these filters. "
            "Try different track/difficulty settings.</p>",
            "",
            {},
        )
    record = random.choice(pool)
    return format_scenario_display(record), format_question(record), record


def submit_response(student_text: str, record: dict) -> str:
    """Evaluate the student's response (corpus-only mode: reveal answer)."""
    if not record:
        return "<p style='color:#c62828;'>No scenario loaded. Click 'New Scenario' first.</p>"
    if not student_text or not student_text.strip():
        return "<p style='color:#c62828;'>Please enter your analysis before submitting.</p>"
    return format_feedback(record, student_text)


# ── Tab 2: Practice by Topic ─────────────────────────────────────────────────

def load_topic_scenarios(code_label: str) -> tuple[str, list[dict], int]:
    """Load all scenarios for a taxonomy code and display the first."""
    if not code_label:
        return "Select a topic to begin.", [], 0
    code = code_label.split(":")[0].strip()
    records = BY_CODE.get(code, [])
    if not records:
        return f"<p>No scenarios found for code {code}.</p>", [], 0
    return display_topic_scenario(records, 0), records, 0


def display_topic_scenario(records: list[dict], idx: int) -> str:
    """Display a specific scenario from a topic's list."""
    if not records or idx < 0 or idx >= len(records):
        return "<p>No more scenarios for this topic.</p>"
    record = records[idx]
    counter = f"""
<div style="text-align:right; color:#666; font-size:0.9em; margin-bottom:8px;">
  Scenario {idx + 1} of {len(records)}
</div>
"""
    return counter + format_scenario_display(record) + format_question(record)


def next_topic_scenario(records: list[dict], idx: int) -> tuple[str, int]:
    """Advance to the next scenario in the topic."""
    if not records:
        return "Select a topic first.", 0
    new_idx = (idx + 1) % len(records)
    return display_topic_scenario(records, new_idx), new_idx


def prev_topic_scenario(records: list[dict], idx: int) -> tuple[str, int]:
    """Go back to the previous scenario in the topic."""
    if not records:
        return "Select a topic first.", 0
    new_idx = (idx - 1) % len(records)
    return display_topic_scenario(records, new_idx), new_idx


def submit_topic_response(
    student_text: str, records: list[dict], idx: int
) -> str:
    """Evaluate the student's response for the current topic scenario."""
    if not records or idx < 0 or idx >= len(records):
        return "<p>No scenario loaded.</p>"
    if not student_text or not student_text.strip():
        return "<p style='color:#c62828;'>Please enter your analysis before submitting.</p>"
    return format_feedback(records[idx], student_text)


# ── Tab 3: About ─────────────────────────────────────────────────────────────

ABOUT_HTML = """
<div style="max-width:800px; margin:0 auto; line-height:1.7;">

<h2 style="color:#1565c0;">Good Thinking Bot</h2>

<p>An interactive learning system that teaches <strong>critical thinking, logic,
decision theory, and economics</strong> through scenario-based practice with
NPC characters. The organizing frame is Dennett's "Moral First Aid Manual":
the bot helps learners build practical guides to better thinking by moving
from formal ideals through real-world friction to practical wisdom.</p>

<h3 style="color:#333;">The Corpus</h3>

<p>The Good Thinking Corpus contains <strong>27,252 training records</strong> across
<strong>182 taxonomy codes</strong> organized in six tracks:</p>

<table style="border-collapse:collapse; width:100%; margin:12px 0;">
<tr style="background:#e3f2fd;">
  <th style="padding:8px; text-align:left; border-bottom:2px solid #1565c0;">Track</th>
  <th style="padding:8px; text-align:right; border-bottom:2px solid #1565c0;">Codes</th>
  <th style="padding:8px; text-align:right; border-bottom:2px solid #1565c0;">Records</th>
</tr>
<tr><td style="padding:6px 8px;">Logic & Critical Thinking</td>
    <td style="padding:6px 8px; text-align:right;">65</td>
    <td style="padding:6px 8px; text-align:right;">~14,000</td></tr>
<tr style="background:#2a2a2a;">
    <td style="padding:6px 8px;">Decision Theory</td>
    <td style="padding:6px 8px; text-align:right;">31</td>
    <td style="padding:6px 8px; text-align:right;">~3,500</td></tr>
<tr><td style="padding:6px 8px;">Game Theory</td>
    <td style="padding:6px 8px; text-align:right;">33</td>
    <td style="padding:6px 8px; text-align:right;">~5,200</td></tr>
<tr style="background:#2a2a2a;">
    <td style="padding:6px 8px;">Cognitive Biases</td>
    <td style="padding:6px 8px; text-align:right;">24</td>
    <td style="padding:6px 8px; text-align:right;">~4,900</td></tr>
<tr><td style="padding:6px 8px;">Microeconomics</td>
    <td style="padding:6px 8px; text-align:right;">16</td>
    <td style="padding:6px 8px; text-align:right;">~950</td></tr>
<tr style="background:#2a2a2a;">
    <td style="padding:6px 8px;">Dennett's Thinking Tools</td>
    <td style="padding:6px 8px; text-align:right;">14</td>
    <td style="padding:6px 8px; text-align:right;">~800</td></tr>
</table>

<p>Each record includes a scenario, structural analysis, a 0-4 rubric, follow-up
questions, and NPC game hooks. Sources: 182 hand-crafted anchors, ~13K adapted
from existing datasets, ~14K synthetic (verified by cross-validation at 87.7%
blind agreement and expert review at 4.40/5).</p>

<h3 style="color:#333;">Three-Tier Difficulty</h3>
<ul>
  <li><strong>Drill</strong> — Apply a concept mechanically to a clear example</li>
  <li><strong>What-If</strong> — Stress-test the concept, connect it to other ideas</li>
  <li><strong>Puzzle</strong> — Engage with genuine philosophical or strategic complexity</li>
</ul>

<h3 style="color:#333;">Links</h3>
<ul>
  <li>HuggingFace Dataset:
    <a href="https://huggingface.co/datasets/bertybaums/good-thinking-corpus"
       target="_blank">bertybaums/good-thinking-corpus</a></li>
  <li>GitHub:
    <a href="https://github.com/bertybaums/good-thinking-bot"
       target="_blank">bertybaums/good-thinking-bot</a></li>
  <li>Zenodo:
    <a href="https://doi.org/10.5281/zenodo.19324917"
       target="_blank">10.5281/zenodo.19324917</a></li>
</ul>

<h3 style="color:#333;">Citation</h3>
<pre style="background:#2a2a2a; padding:14px; border-radius:6px; overflow-x:auto;
            font-size:0.85em; line-height:1.5;">
@dataset{baumgaertner2026goodthinking,
  title     = {Good Thinking Corpus: Training Data for Critical Thinking,
               Logic, Decision Theory, and Economics},
  author    = {Baumgaertner, Bert and Potter, Nicholas},
  year      = {2026},
  publisher = {HuggingFace / Zenodo},
  doi       = {10.5281/zenodo.19324917},
  url       = {https://huggingface.co/datasets/bertybaums/good-thinking-corpus},
  license   = {CC BY-NC-SA 4.0}
}
</pre>

<h3 style="color:#333;">Credits</h3>
<p><strong>Bert Baumgaertner</strong> — Philosophy, logic, decision theory<br>
<strong>Nicholas Potter</strong> — Economics, game design<br>
University of Idaho</p>

<p style="color:#999; font-size:0.85em; margin-top:20px;">
This app is running in corpus-only mode: it presents scenarios from the
training corpus and reveals correct answers for self-assessment. A future
version will incorporate the fine-tuned model for real-time evaluation of
student responses.</p>

</div>
"""


# ── Build the Gradio App ─────────────────────────────────────────────────────

CSS = """
.scenario-display { min-height: 200px; }
.feedback-display { min-height: 200px; }
footer { display: none !important; }
"""

THEME = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="slate",
    neutral_hue="slate",
)

def build_app() -> gr.Blocks:
    with gr.Blocks(title="Good Thinking Bot") as app:
        gr.Markdown(
            "# Good Thinking Bot\n"
            "*Interactive critical thinking tutor — "
            "learn to spot fallacies, biases, and reasoning patterns*"
        )

        # State variables
        current_record = gr.State({})
        topic_records = gr.State([])
        topic_idx = gr.State(0)

        # ── Tab 1: Interactive Tutor ─────────────────────────────────
        with gr.Tab("Interactive Tutor"):
            with gr.Row():
                track_filter = gr.Dropdown(
                    choices=TRACK_CHOICES,
                    value="All",
                    label="Track",
                    scale=1,
                )
                tier_filter = gr.Dropdown(
                    choices=TIER_CHOICES,
                    value="All",
                    label="Difficulty",
                    scale=1,
                )
                new_btn = gr.Button(
                    "New Scenario",
                    variant="primary",
                    scale=1,
                )

            scenario_display = gr.HTML(
                value="<p style='color:#666; text-align:center; padding:40px;'>"
                "Click <strong>New Scenario</strong> to begin.</p>",
                elem_classes=["scenario-display"],
            )
            question_display = gr.HTML()

            student_input = gr.Textbox(
                label="Your Analysis",
                placeholder="Type your analysis of the scenario here...",
                lines=5,
            )
            submit_btn = gr.Button("Submit", variant="secondary")
            feedback_display = gr.HTML(elem_classes=["feedback-display"])

            def on_new_scenario(track, tier):
                s_html, q_html, record = get_random_scenario(track, tier)
                # Clear previous feedback and input
                return s_html, q_html, record, "", ""

            new_btn.click(
                fn=on_new_scenario,
                inputs=[track_filter, tier_filter],
                outputs=[
                    scenario_display,
                    question_display,
                    current_record,
                    student_input,
                    feedback_display,
                ],
            )

            submit_btn.click(
                fn=submit_response,
                inputs=[student_input, current_record],
                outputs=[feedback_display],
            )

        # ── Tab 2: Practice by Topic ─────────────────────────────────
        with gr.Tab("Practice by Topic"):
            topic_dropdown = gr.Dropdown(
                choices=CODE_CHOICES,
                label="Select Topic",
                info="Choose a taxonomy code to practice",
            )

            topic_display = gr.HTML(
                value="<p style='color:#666; text-align:center; padding:40px;'>"
                "Select a topic from the dropdown above.</p>"
            )

            with gr.Row():
                prev_btn = gr.Button("Previous", scale=1)
                next_btn = gr.Button("Next", scale=1)

            topic_input = gr.Textbox(
                label="Your Analysis",
                placeholder="Type your analysis of the scenario here...",
                lines=5,
            )
            topic_submit_btn = gr.Button("Submit", variant="secondary")
            topic_feedback = gr.HTML()

            def on_topic_select(code_label):
                html, records, idx = load_topic_scenarios(code_label)
                return html, records, idx, "", ""

            topic_dropdown.change(
                fn=on_topic_select,
                inputs=[topic_dropdown],
                outputs=[
                    topic_display,
                    topic_records,
                    topic_idx,
                    topic_input,
                    topic_feedback,
                ],
            )

            def on_next(records, idx):
                html, new_idx = next_topic_scenario(records, idx)
                return html, new_idx, "", ""

            def on_prev(records, idx):
                html, new_idx = prev_topic_scenario(records, idx)
                return html, new_idx, "", ""

            next_btn.click(
                fn=on_next,
                inputs=[topic_records, topic_idx],
                outputs=[topic_display, topic_idx, topic_input, topic_feedback],
            )

            prev_btn.click(
                fn=on_prev,
                inputs=[topic_records, topic_idx],
                outputs=[topic_display, topic_idx, topic_input, topic_feedback],
            )

            topic_submit_btn.click(
                fn=submit_topic_response,
                inputs=[topic_input, topic_records, topic_idx],
                outputs=[topic_feedback],
            )

        # ── Tab 3: About ─────────────────────────────────────────────
        with gr.Tab("About"):
            gr.HTML(ABOUT_HTML)

    return app


# ── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if not SCENARIOS:
        print(
            "WARNING: No scenarios loaded. Run create_sample_data.py first:\n"
            "  python app/create_sample_data.py"
        )
    app = build_app()
    app.launch(theme=THEME, css=CSS)
