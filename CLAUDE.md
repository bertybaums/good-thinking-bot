# Good Thinking Bot

## Project Overview

An interactive, game-based learning system that teaches critical thinking, logic, decision theory, and economics through LLM-powered NPCs. The organizing frame is Dennett's "Moral First Aid Manual": the bot helps players build their own practical guides to better thinking by taking them from formal ideals through real-world friction to practical wisdom.

Collaborators: Bert Baumgaertner (philosophy, logic, decision theory) and Nicholas Potter (economics, game design).

## Project Status

**Phase: Corpus Construction (Sprint 1)** -- training corpus pipeline built, ready for anchor crafting. We have:
- Source material assembled in `/resources`
- Landscape research completed (see `report-for-nick.md`, `dataset-landscape-research.md`)
- Training corpus pipeline in `/corpus-tools` (taxonomy, schema, 6 pipeline scripts)
- 167-code taxonomy covering all content tracks

## Repository Structure

```
/resources/                          # Source material for content
  Intro to Logic and Critical Thinking v2.0.pdf   # Van Cleave (CC BY 4.0)
  Notes for 2010 Critical Thinking.txt             # Bert's PHIL 201 lecture notes
  Dennett - Thought Stoppers.pdf
  Poster - Cognitive Biases.pdf                    # yourbias.is (~24 biases)
  Poster - Logical Fallacies.pdf                   # yourfallacy.is (~24 fallacies)
  the-economy-2-0-microeconomics-epub.epub         # CORE Economy 2.0
  rationality-and-strategic-interactions/          # Bert's decision theory course
    Baumgaertner-decisiontheory.pdf                # Bert's textbook
    Dennett - The Moral First Aid Manual.pdf
    W1-W14 lecture notes (.md)                     # Full semester of notes
/corpus-tools/                       # Training corpus pipeline
  config.py                          # API keys, endpoints, model routing
  schema.py                          # Pydantic models for corpus records
  taxonomy.py                        # 167-code taxonomy of reasoning patterns
  llm_client.py                      # Unified client: Anthropic + MindRouter
  01_anchor_craft.py                 # Interactive: Opus generates, Bert approves
  02_dataset_adapt.py                # Batch: MindRouter enriches existing datasets
  03_synthetic_gen.py                # Batch: MindRouter generates, Sonnet verifies
  04_cross_validate.py               # Batch: strip labels, classify, flag disagreements
  05_mechanical_verify.py            # Local: compute correct answers for DT/GT
  06_coverage_dashboard.py           # Local: taxonomy x tier x domain matrix
  prompts/                           # Prompt templates per pipeline
  output/                            # Generated corpus (JSONL per taxonomy group)
/report-for-nick.md                  # Summary report for Nicholas Potter
/dataset-landscape-research.md       # Existing dataset analysis
```

## Content Tracks

Three tracks that converge on "how to be a better thinker":

1. **Logic & Critical Thinking** (Van Cleave + Bert's PHIL 201 notes + Dennett's thinking tools + bias/fallacy posters)
2. **Decision Theory & Game Theory** (Bert's textbook + Weatherson + Bert's "Rationality & Strategic Interactions" lecture notes W1-W14)
3. **Microeconomics** (CORE "The Economy 2.0")

Cross-cutting theme: Dennett's Moral First Aid Manual -- bounded rationality as an ideal, not a compromise.

## Pedagogical Approach

When generating content, problems, or NPC dialogue for this project, follow Bert's teaching style:

- **Ideal-to-real arc**: Present the clean formal framework first, then break it with paradoxes/real cases, then rebuild something practical
- **Experience before description**: Let the learner encounter the concept (e.g., discover their own inconsistency) before naming it
- **Three-tier problems**: Drill (apply mechanically) -> What-If (stress-test, connect concepts) -> Puzzle (genuine philosophical engagement)
- **Dennett as throughline**: Satisficing, conversation-stoppers, the Panglossian Slide, and the Manual connect everything

## Technical Direction (Early)

- Modular LoRA adapters for specific reasoning skills with MoE routing
- QLoRA for on-device inference
- Stealth assessment via NPC dialogue (no XP bars)
- Retro-style open-world game with agent-driven NPCs
- Game mechanics mapped to concepts: knights & knaves for propositional logic, money pumps for decision theory, fallacy-committing NPCs for informal logic
