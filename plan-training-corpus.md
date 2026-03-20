# Plan: Good Thinking Bot Training Corpus

## Context

We need a training corpus for LoRA adapters that will power NPCs in an educational game teaching critical thinking, logic, decision theory, and economics. Existing datasets cover formal logic and fallacy detection partially, but there are major gaps in decision theory, cognitive bias recognition, game theory, and integrated reasoning. The corpus must be structured around a taxonomy of "good thinking tools" and "bad thinking patterns," with each example illustrating a specific reasoning structure.

## Step 1: Define the Taxonomy (~120 codes)

A categorization of every reasoning pattern across all three content tracks, organized as:

**Track A: Logic & Critical Thinking** (~65 codes)
- A1: Argument structure (7 codes: identifying arguments, premises/conclusions, standard form, principle of charity, missing premises...)
- A2: Deductive logic (8 codes: validity, propositional logic, truth tables, 8 inference forms, proofs, categorical logic)
- A3: Inductive reasoning (5 codes: statistical generalizations, IBE, analogical arguments, causal reasoning, correlation vs causation)
- A4: Probability (3 codes: basic laws, conditional probability, base rate reasoning)
- A5: Formal fallacies (3 codes: denying antecedent, affirming consequent, causal slippery slope)
- A6: Informal fallacies (6 codes: composition, division, begging question, false dichotomy, equivocation, conceptual slippery slope)
- A7: Fallacies of relevance (16 codes: ad hominem, straw man, tu quoque, genetic, appeal to consequences/authority/emotion/nature, bandwagon, burden of proof, personal incredulity, special pleading, loaded question, Texas sharpshooter, middle ground, anecdotal)
- A8: Statistical fallacies (7 codes: conjunction, base rate, small numbers, regression to mean, gambler's, hasty generalization, false cause)
- A9: Rhetorical manipulation (3 codes: evaluative language, assuring/guarding/discounting, fallacy fallacy)
- A10: Propaganda techniques (7 codes)

**Track B: Decision Theory & Game Theory** (~40 codes)
- B1: Decision under ignorance (5: matrices, dominance, maximax, maximin, minimax regret)
- B2: Probability/consistency (5: betting rates, Dutch Books, axioms, subjective vs objective, Principal Principle)
- B3: Expected utility (7: MEU formula, cardinal vs ordinal, risk aversion, transitivity/money pumps, IIA, Pascal's Wager, St. Petersburg)
- B4: Paradoxes (6: Allais, STP, Newcomb, Ellsberg, reflection effect, disjunction)
- B5: Prospect Theory (8: reference points, loss aversion, probability weighting, fourfold pattern, framing, mental accounting, endowment, disposition)
- B6-B10: Game theory through synthesis (remaining codes for PD, coordination, sequential, evolutionary, signaling, behavioral GT, commitment)

**Track C: Microeconomics** (~15 codes)
- C1-C6: Opportunity cost, constrained optimization, public goods, bargaining/fairness, markets, market failures, economic fallacies

**Cross-cutting layers:**
- D: Dennett's thinking tools (~15 codes: Rapoport's Rules, reductio, Occam's Razor/Broom, Jootsing, deepities, "surely" operator, Goulding, satisficing, Panglossian Slide, conversation-stoppers, Wolf's Dilemma, Frame Problem, the Manual)
- E: Cognitive biases (24 codes from the poster)

Each code is labeled: `good_tool`, `bad_thinking`, or `dual` (e.g., satisficing is good; Panglossian Slide is bad; conversation-stoppers are dual).

## Step 2: Define the Corpus Schema

Each example is a JSON record with:

```json
{
  "id": "A7.1-042",
  "taxonomy_code": "A7.1",
  "taxonomy_label": "Ad hominem",
  "track": "logic_critical_thinking",
  "pattern_type": "bad_thinking",
  "difficulty_tier": "drill | what_if | puzzle",
  "scenario": {
    "context": "Setting/situation description",
    "text": "The actual argument or reasoning to analyze",
    "speaker_context": "NPC identity for game use"
  },
  "structure": {
    "pattern_name": "Ad hominem (circumstantial)",
    "pattern_description": "What's happening and why",
    "formal_form": "Schematic form if applicable",
    "why_wrong": "Or why_right for good tools",
    "related_patterns": ["A7.3", "A7.4"],
    "counterpoint": "Edge case or exception"
  },
  "assessment": {
    "identification_prompt": "Question to probe understanding",
    "rubric": [{"level": 0-4, "description": "..."}],
    "follow_up_if_wrong": "Socratic redirect",
    "follow_up_if_right": "Deepening question"
  },
  "game_hooks": {
    "npc_personality": "Character sketch",
    "npc_dialogue_seed": "Opening line",
    "resolution_path": "What happens when player succeeds"
  },
  "source": {
    "type": "hand_crafted | existing_dataset | synthetic_verified",
    "source_material": "Reference to origin"
  }
}
```

## Step 3: Construction Strategy (by source)

### 3a. Hand-Craft Anchor Examples (~500)
- One per taxonomy code from Bert's lecture notes and source material
- These define quality/voice; everything else is measured against them
- Priority: all fallacy poster examples, all bias poster examples, all worked decision theory problems from W1-W14, Dennett's 12 tools

### 3b. Adapt Existing Datasets (~60K)
| Dataset | Size | Maps To |
|---------|------|---------|
| Jin et al. (fallacy, MIT) | 3,761 | A5-A7: enrich with structure + assessment fields |
| FOLIO (CC-BY-4.0) | 1,435 | A2: add knights-and-knaves game hooks |
| LogiQA 2.0 | 15,708 | Mixed A codes: LSAT critical reasoning |
| IBM-Rank-30k | 30,000 | A1, A3: argument quality scores |
| Corr2Cause (dev+test) | ~5,000 | A3.4-A3.5, A8.7: causal reasoning |
| SemEval Propaganda | 6,129 | A9-A10: propaganda in real text |
| EconNLI | 10,810 | C6: economic causal reasoning |
| e-SNLI (sampled) | ~10,000 | A2: entailment with explanations |

Adaptation pipeline: map to taxonomy code -> add structure/assessment fields via LLM -> cross-validate classification -> Bert spot-checks 10%.

### 3c. Generate Synthetically (~11K, filling the gaps)
| Gap | Target | Method | Verification |
|-----|--------|--------|-------------|
| Decision theory (B1-B5) | ~2,000 | Vary domains on Bert's worked examples, preserve math structure | Mechanical: compute correct answers |
| Game theory (B6-B10) | ~1,500 | Vary PD/coordination/sequential game contexts | Mechanical: compute equilibria |
| Cognitive biases (E1) | ~4,800 | 24 biases x 200 examples across domains | LLM cross-validation: classify from scenario |
| Argument by analogy (A3.3) | ~500 | Generate analogy + evaluate strength + disanalogies | LLM cross-validation |
| Integrated scenarios | ~500 | Multi-code scenarios requiring multiple skills | Bert review (puzzle tier) |
| Microeconomics (C1-C6) | ~2,000 | Extract concepts from CORE textbook, generate scenarios | LLM + Bert review |

## Step 4: Prioritization (Pilot Sprints)

| Sprint | Weeks | Deliverable | Count |
|--------|-------|-------------|-------|
| 1 | 1-2 | Hand-craft anchor set (24 fallacies, 10 biases, 10 DT, 10 GT, 12 Dennett tools + more) | ~100 |
| 2 | 3-4 | Adapt Jin et al. + FOLIO + Corr2Cause subset | ~5,700 |
| 3 | 5-6 | Synthetic decision theory (B1-B5) from Bert's W1-W7 notes | ~2,000 |
| 4 | 7-8 | Synthetic cognitive biases (E1.1-E1.24) | ~2,400 |
| 5 | 9-10 | Synthetic game theory (B6-B10) + integrated scenarios | ~1,200 |
| **Pilot total** | **10 weeks** | | **~11,400** |

## Step 5: Quality Assurance (4 tiers)

1. **Mechanical verification** -- for all decision theory and game theory examples: compute correct answer, compare to stated answer. Reject rate ~10-20%.
2. **LLM cross-validation** -- for fallacy/bias/propaganda examples: strip label, ask separate LLM to classify, flag disagreements. Pass rate ~75-85%.
3. **Bert expert review** -- 100% of anchors, 10% stratified sample of everything else, 100% of flagged items. Checks correctness, pedagogical soundness, difficulty calibration, voice.
4. **Coverage dashboard** -- matrix of taxonomy codes x difficulty tiers x domains. Identifies gaps for targeted generation.

## Verification

After each sprint:
- Run coverage dashboard to confirm no taxonomy codes are empty
- Run mechanical verification on all quantitative examples
- Run LLM cross-validation on all classification examples
- Bert reviews stratified sample
- Compute inter-annotator agreement between LLM classifier and intended labels

## Step 6: Execution Architecture

### Compute Resources

| Resource | Models | Access | Best For |
|----------|--------|--------|----------|
| **Anthropic (Max plan)** | Opus 4.6, Sonnet 4.6 | Claude Code CLI + API | Quality-sensitive work, anchors, review, complex generation |
| **MindRouter (Campus HPC)** | gpt-oss-120b, qwen3.5-400b | OpenAI-compatible API (`/v1/chat/completions`) | Bulk generation, domain variation, reformatting, cross-validation |

Anthropic tokens are the bottleneck (Max plan has monthly limits). MindRouter on campus HPC is essentially unlimited. So the design principle is: **use Anthropic for quality, MindRouter for volume.**

### Pipeline Architecture

All pipelines are standalone Python scripts with a shared config:

```
corpus-tools/
  config.py              # API keys, endpoints, model names
  schema.py              # Pydantic models for the corpus schema
  taxonomy.py            # The full taxonomy as a Python dict

  # Pipeline scripts (one per task type)
  01_anchor_craft.py     # Interactive: Opus generates, Bert approves
  02_dataset_adapt.py    # Batch: MindRouter enriches existing datasets
  03_synthetic_gen.py    # Batch: MindRouter generates, Sonnet verifies
  04_cross_validate.py   # Batch: MindRouter classifies, flags disagreements
  05_mechanical_verify.py # Local: Python computes correct answers for DT/GT
  06_coverage_dashboard.py # Local: Reports gaps in taxonomy x tier x domain

  # Shared utilities
  llm_client.py          # Unified client that routes to Anthropic or MindRouter
  prompts/               # Prompt templates per task type
  output/                # Generated corpus (JSONL per taxonomy group)
```

### Model Allocation by Task

**Pipeline 1: Anchor Crafting (Sprint 1)**
- **Model: Opus 4.6** via Claude Code subagents
- Bert provides source passage → Opus drafts full schema record → Bert reviews/edits
- ~100 examples, ~500 Opus calls (with revisions). Manageable on Max plan.
- This is the ONE pipeline that stays interactive in Claude Code rather than batch scripts.

**Pipeline 2: Dataset Adaptation (Sprint 2)**
- **Model: qwen3.5-400b** (MindRouter) for enrichment
- **Model: Sonnet 4.6** (Anthropic) for spot-check validation of 10% sample
- Bulk work: for each of ~60K existing dataset examples, call MindRouter to add `structure`, `assessment`, and `game_hooks` fields. This is mechanical enrichment — good fit for a capable but cheaper model.
- Prompt template includes 3 anchor examples as few-shot demonstrations (from Pipeline 1 output).
- Sonnet validates a stratified 10% sample (~6K calls). If enrichment quality is poor for a category, escalate that category to Sonnet for full re-enrichment.

**Pipeline 3: Synthetic Generation (Sprints 3-5)**
- **Stage A — Draft generation: gpt-oss-120b or qwen3.5-400b** (MindRouter)
  - Bulk generation of decision theory, game theory, bias, analogy, econ examples.
  - Prompt includes: taxonomy code definition + 2-3 anchor examples as few-shot + domain constraint + difficulty tier.
  - Generate 2x the target count (expect ~50% to survive verification).

- **Stage B — Verification pass: Sonnet 4.6** (Anthropic)
  - For each MindRouter-generated example, Sonnet reviews: Is the taxonomy code correct? Is the structure explanation accurate? Is the difficulty tier right?
  - Binary pass/fail + optional revision suggestion.
  - ~22K Sonnet calls across Sprints 3-5.

- **Stage C — Mechanical verification** (local Python, no API calls)
  - For B1-B10 (decision theory + game theory): parse the decision matrix / game tree from the JSON, compute the correct answer using numpy/scipy, compare to stated answer.
  - Reject mismatches. No token cost.

**Pipeline 4: Cross-Validation (QA, runs after each sprint)**
- **Model: qwen3.5-400b** (MindRouter)
- Strip taxonomy code from example → send scenario to MindRouter → ask it to classify → compare to intended code.
- Flag disagreements for Bert review.
- Bulk job, runs on all classification-type examples (~50K calls total across all sprints). Free on HPC.

**Pipeline 5: Mechanical Verification (QA, local)**
- Pure Python. No API calls.
- Parses decision matrices and game trees.
- Computes: maximin, maximax, minimax regret, MEU, Nash equilibria, backward induction, ESS.
- Compares to stated answers. Rejects mismatches.

**Pipeline 6: Coverage Dashboard (reporting, local)**
- Pure Python. Reads corpus JSONL files.
- Generates a matrix: taxonomy_code x difficulty_tier x domain.
- Highlights gaps (zero examples, single-tier-only codes, underrepresented domains).
- Outputs HTML report.

### Token Budget Estimate

| Pipeline | Model | Calls | ~Tokens/call | Total tokens |
|----------|-------|-------|-------------|-------------|
| Anchor crafting | Opus 4.6 | ~500 | ~4K | ~2M |
| Dataset adaptation (bulk) | MindRouter | ~60K | ~2K | ~120M |
| Dataset adaptation (validation) | Sonnet 4.6 | ~6K | ~2K | ~12M |
| Synthetic draft gen | MindRouter | ~22K | ~3K | ~66M |
| Synthetic verification | Sonnet 4.6 | ~22K | ~2K | ~44M |
| Cross-validation | MindRouter | ~50K | ~1K | ~50M |
| **Anthropic total** | | | | **~58M tokens** |
| **MindRouter total** | | | | **~236M tokens** |

Anthropic budget (~58M tokens) is spread across ~10 weeks. At Max plan rates this should be feasible. MindRouter handles the heavy lifting (~236M tokens) on campus HPC.

### MindRouter Configuration

```python
# config.py
MINDROUTER_BASE_URL = "https://mindrouter.uidaho.edu/v1"
MINDROUTER_API_KEY = "<from .env file>"
MINDROUTER_MODELS = {
    "bulk_gen": "openai/gpt-oss-120b",
    "cross_val": "qwen/qwen3.5-400b",
}

ANTHROPIC_MODELS = {
    "anchor": "claude-opus-4-6",
    "verify": "claude-sonnet-4-6",
}
```

### MindRouter Concurrency Limits

- **gpt-oss-120b**: 8 concurrent calls
- **qwen3.5-400b**: 4 concurrent calls

## Key Files

- `resources/Notes for 2010 Critical Thinking.txt` -- source for Track A anchors
- `resources/rationality-and-strategic-interactions/W1-W14` -- source for Track B anchors and synthetic generation seeds
- `resources/the-economy-2-0-microeconomics-epub.epub` -- source for Track C
- `resources/Poster - Cognitive Biases.pdf` -- seed definitions for E1
- `resources/Poster - Logical Fallacies.pdf` -- seed definitions for A5-A8 (supplement)
- `dataset-landscape-research.md` -- URLs and details for all existing datasets
