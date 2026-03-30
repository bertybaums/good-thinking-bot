# Good Thinking Bot

## Project Overview

An interactive, game-based learning system that teaches critical thinking, logic, decision theory, and economics through LLM-powered NPCs. The organizing frame is Dennett's "Moral First Aid Manual": the bot helps players build their own practical guides to better thinking by taking them from formal ideals through real-world friction to practical wisdom.

Collaborators: Bert Baumgaertner (philosophy, logic, decision theory) and Nicholas Potter (economics, game design).

## Project Status

**Phase: Corpus Complete, Ready for QLoRA Training.** We have:
- 28,038 training corpus records across 182 taxonomy codes (expanded from 167 via PHIL 4040 gap analysis)
- Full QC pipeline complete: QC1-QC6 all passing, 100% Pydantic-valid
- Benchmarks for five models: gpt-oss-20b, gpt-oss-120b, Nemotron-3-Super-120b, qwen2.5:7b, qwen3.5-122b
- Nick's QLoRA adapter merging PoC in `qlora_merge/`
- Full pipeline infrastructure for generation, adaptation, verification, and evaluation
- Fine-tuning target: qwen2.5:7b (2.52/2.22 baseline → target 3.0+ after QLoRA)

## Repository Structure

```
/resources/                          # Source material for content
  Notes for 2010 Critical Thinking.txt  # Bert's PHIL 201 lecture notes
  rationality-and-strategic-interactions/
    W1-W14 lecture notes (.md)          # Full semester DT/GT notes
  (PDFs gitignored — kept local only)

/corpus-tools/                       # Training corpus pipeline
  config.py                          # API keys (.env), endpoints, model routing
  schema.py                          # Pydantic models for corpus records
  taxonomy.py                        # 182-code taxonomy of reasoning patterns
  llm_client.py                      # Unified client: Anthropic + MindRouter
  source_loader.py                   # Maps taxonomy codes to source material passages
  benchmark.py                       # Model evaluation (identify/classify/explain modes)
  01_anchor_craft.py                 # Interactive: Opus generates, Bert approves
  02_dataset_adapt.py                # Batch: MindRouter enriches existing datasets
  03_synthetic_gen.py                # Batch: MindRouter generates, Sonnet verifies
  04_cross_validate.py               # Batch: strip labels, classify, flag disagreements
  05_mechanical_verify.py            # Local: compute correct answers for DT/GT
  06_coverage_dashboard.py           # Local: taxonomy x tier x domain matrix
  run_sprint2_adapt.py               # Sprint 2: dataset adaptation (with resume)
  run_sprint3_synthetic_dt.py        # Sprint 3: synthetic decision theory
  run_sprint4_synthetic_biases.py    # Sprint 4: synthetic cognitive biases
  run_sprint5_synthetic_gt.py        # Sprint 5: game theory + integrated scenarios
  run_overnight_fill.py              # Bulk fill for thin codes
  run_cross_validate_anchors.py      # Cross-validation via MindRouter
  run_mindrouter_synthetic.py        # Pilot synthetic generation
  prompts/                           # Prompt templates per pipeline
  output/                            # Generated corpus (JSONL) + benchmarks

/data/external/                      # Downloaded datasets for adaptation
  jin_fallacy.jsonl                  # 3,761 fallacy detection examples
  folio.jsonl                        # 1,204 logical reasoning examples
  corr2cause.jsonl                   # 2,238 causal reasoning examples
  semeval2020_propaganda.jsonl       # 6,129 propaganda detection examples

/qlora_merge/                        # Nick's QLoRA adapter merging PoC
  adapter.py                         # Adapter loading + from_peft() stub
  methods.py                         # 5 merging strategies (linear, task arith, TIES, DARE, router)
  demo.py                            # Demo with synthetic adapters

/reports/                            # Analysis and evaluation reports
  benchmark-gpt-oss-20b.md          # 20b baseline (identify: 2.62, explain: 2.47)
  benchmark-gpt-oss-120b.md         # 120b baseline (identify: 2.95, explain: 3.04)
  benchmark-qwen3.5-122b.md         # 122b baseline (identify: 3.47, explain: 3.60)
  qc1-schema-validation.md          # Schema validation: 99.6% clean
  qc2-mechanical-verification.md    # DT/GT math: 96.6% pass (56 failures)
  qc3-expert-review.md              # Content quality: 4.1-4.5/5
  qc5-schema-cleanup.md             # Full cleanup: 100% Pydantic-valid (24,761 records)
  qc6-phil4040-expansion.md         # PHIL 4040 expansion: 167->182 codes, 46 adapted records
  taxonomy-gap-analysis.md          # 40 missing concepts from PHIL 4040 lectures

/notes/                              # Design documents
  qlora-weighting.md                 # QLoRA + adapter merging explainer
  report-for-nick.md                 # Summary report for Nick

/plan-training-corpus.md             # The original corpus construction plan
/dataset-landscape-research.md       # Existing dataset analysis
```

## Training Corpus Summary

**28,038 records** across 182 taxonomy codes, 6 tracks:

| Track | Codes | Records |
|-------|-------|---------|
| Logic & Critical Thinking (A1-A10) | 65 | ~14,000 |
| Decision Theory (B1-B5) | 31 | ~3,500 |
| Game Theory (B6-B15) | 33 | ~5,200 |
| Cognitive Biases (E1) | 24 | ~4,900 |
| Microeconomics (C1-C7) | 16 | ~950 |
| Dennett's Tools (D1-D2) | 14 | ~800 |

Sources: 182 hand-crafted anchors, ~13K adapted from existing datasets (Jin, FOLIO, Corr2Cause, SemEval, PHIL 4040 problems), ~14K synthetic (MindRouter gpt-oss-120b + qwen3.5-400b).

Quality: 100% Pydantic-valid. Mechanically verified (0 failures), cross-validated (71.7% blind agreement), expert-reviewed (4.1-4.5/5). See `reports/` for full QC history.

## Benchmark Results (Pre-Training Baselines, 182 anchors)

| Mode | qwen2.5:7b | gpt-oss-20b | gpt-oss-120b | Nemotron-120b | qwen3.5-122b* |
|------|-----------|------------|-------------|--------------|--------------|
| Identify | 2.52/4 | 2.61/4 | 3.15/4 | 3.40/4 | 3.47/4 |
| Explain | 2.22/4 | 2.41/4 | 2.93/4 | 3.54/4 | 3.60/4 |

*qwen3.5-122b benchmarked on prior 167-anchor set; others on current 182-anchor set.

**Fine-tuning target:** qwen2.5:7b (2.52/2.22 baseline → target 3.0+ after QLoRA). Weakest areas: Dennett tools (1.21 explain), game theory (2.16), argument structure. Nemotron-3-Super-120b (3.54 explain) could serve as distillation teacher.

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

## Technical Direction

- Modular LoRA adapters for specific reasoning skills with MoE routing
- QLoRA for on-device inference (Nick's merging PoC supports 5 strategies: linear, task arithmetic, TIES, DARE, router-based)
- Stealth assessment via NPC dialogue (no XP bars) — built into every corpus record's assessment block
- Retro-style open-world game with agent-driven NPCs
- Game mechanics mapped to concepts: knights & knaves for propositional logic, money pumps for decision theory, fallacy-committing NPCs for informal logic
- MindRouter (campus HPC) for bulk generation: gpt-oss-120b (8 concurrent), qwen3.5-400b (4 concurrent), gpt-oss-20b (4 concurrent)

## Infrastructure

- **API keys**: Stored in `.env` (gitignored), loaded via python-dotenv
- **MindRouter**: https://mindrouter.uidaho.edu/v1 (OpenAI-compatible)
- **Model IDs**: openai/gpt-oss-120b, openai/gpt-oss-20b, qwen/qwen3.5-400b, qwen/qwen3.5-122b
- **Qwen thinking mode**: Must pass `extra_body={"chat_template_kwargs": {"enable_thinking": False}}` for JSON output
