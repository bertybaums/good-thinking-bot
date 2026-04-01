# Good Thinking Bot

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19324917.svg)](https://doi.org/10.5281/zenodo.19324917)
[![Dataset on HuggingFace](https://img.shields.io/badge/HuggingFace-good--thinking--corpus-blue)](https://huggingface.co/datasets/bertybaums/good-thinking-corpus)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**A 27,252-record training corpus and fine-tuning pipeline for teaching critical thinking, logic, decision theory, and game theory through LLM-powered NPCs.**

Critical thinking education needs training data that goes beyond pattern matching. This corpus pairs every reasoning scenario with a structured analysis, a Socratic assessment rubric, and game-world hooks for NPC dialogue -- making it suitable for supervised fine-tuning of instruction-following models that can actually *teach*, not just classify. The organizing pedagogical frame is Daniel Dennett's "Moral First Aid Manual": help learners build their own practical guides to better thinking by moving from formal ideals through real-world friction to practical wisdom.

## Key Numbers

| Metric | Value |
|--------|-------|
| Training records | 27,252 |
| Taxonomy codes | 182 |
| Content tracks | 6 |
| Cross-validation agreement | 87.7% |
| Expert review score | 4.40 / 5.0 |
| Schema validity | 100% (Pydantic) |
| Pre-training baselines | 5 models benchmarked |

## Taxonomy

The corpus is organized around a 182-code taxonomy spanning six tracks of reasoning skills:

| Track | Codes | Records | Example Codes |
|-------|-------|---------|---------------|
| Logic and Critical Thinking (A1--A10) | 65 | ~12,860 | Ad hominem, straw man, modus ponens, base rate neglect |
| Decision Theory (B1--B5) | 31 | ~3,370 | Expected utility, Allais paradox, prospect theory, sunk cost |
| Game Theory (B6--B15) | 33 | ~4,860 | Prisoner's dilemma, Nash equilibrium, signaling, Arrow's theorem |
| Cognitive Biases (E1) | 24 | ~4,660 | Confirmation bias, anchoring, framing effect, Dunning-Kruger |
| Microeconomics (C1--C7) | 16 | ~850 | Pareto efficiency, supply and demand, market equilibrium |
| Dennett's Thinking Tools (D1--D2) | 14 | ~650 | Occam's razor, satisficing, Panglossian slide |

Each code has a hand-crafted anchor record written and reviewed by a domain expert, plus adapted and synthetic records at three difficulty tiers: Drill (apply mechanically), What-If (stress-test and connect concepts), and Puzzle (genuine philosophical engagement).

**Known thin areas:** Microeconomics (850 records) and Dennett's Thinking Tools (650 records) are sparser than the other tracks and may benefit from additional generation.

## Corpus Details

### Record Format

Every record is a self-contained training example with scenario, structured analysis, assessment rubric, and game integration:

```json
{
  "id": "A7.1-001",
  "taxonomy_code": "A7.1",
  "taxonomy_label": "Ad hominem",
  "track": "logic_critical_thinking",
  "pattern_type": "bad_thinking",
  "difficulty_tier": "drill",
  "scenario": {
    "context": "A town hall debate on water quality...",
    "text": "Instead of addressing the data, the councilmember says: 'Why should we listen to someone who couldn't even pass chemistry in college?'",
    "speaker_context": "Councilmember Jenkins, a career politician"
  },
  "structure": {
    "pattern_name": "Abusive ad hominem",
    "pattern_description": "Attacks the person rather than their argument",
    "formal_form": "Person S claims P. S has property Q. Therefore P is false.",
    "why_wrong": "A speaker's personal history is irrelevant to the truth of their factual claims about water quality data.",
    "related_patterns": ["A7.3", "A10.1"],
    "counterpoint": "Character can be relevant when credibility is genuinely at issue (e.g., expert testimony)"
  },
  "assessment": {
    "identification_prompt": "What's going wrong with the councilmember's response?",
    "rubric": [
      {"level": 0, "description": "No recognition of the problem"},
      {"level": 1, "description": "Senses something unfair but can't articulate it"},
      {"level": 2, "description": "Identifies it as a personal attack"},
      {"level": 3, "description": "Names ad hominem and explains why it's irrelevant"},
      {"level": 4, "description": "Full analysis including when character IS relevant"}
    ],
    "follow_up_if_wrong": "Forget the speaker for a moment -- is the data itself being addressed?",
    "follow_up_if_right": "When might someone's background actually matter for evaluating a claim?"
  },
  "game_hooks": {
    "npc_personality": "Blowhard politician, loud but insecure",
    "npc_dialogue_seed": "Listen, I've been on this council for twenty years...",
    "resolution_path": "Player helps townspeople see past the rhetoric to evaluate the actual evidence"
  },
  "source": {
    "type": "hand_crafted",
    "source_material": "Van Cleave, Introduction to Logic and Critical Thinking"
  }
}
```

### Source Breakdown

| Source | Records | Notes |
|--------|---------|-------|
| Hand-crafted anchors | 317 | One per taxonomy code plus extras; manually written and reviewed |
| Adapted from existing datasets | ~8,480 | Jin (fallacy), FOLIO (logic), Corr2Cause (causal), SemEval (propaganda) |
| Synthetic verified | ~18,460 | Generated by gpt-oss-120b via MindRouter; verified by independent model |

### Quality Assurance

The corpus underwent seven QC stages:

| Stage | Method | Result |
|-------|--------|--------|
| QC1: Schema validation | Pydantic type checking | 100% valid |
| QC2: Mechanical verification | Automated DT/GT math checking | 0 failures remaining |
| QC3: Expert review | 60-record sample scored on 5 dimensions | 4.1--4.5 / 5.0 |
| QC4: Cross-validation | Blind reclassification (qwen3.5-400b) | 71.7% agreement |
| QC5: Schema cleanup | Type coercion, field normalization | 100% Pydantic-valid |
| QC6: Taxonomy expansion | 15 new codes, 2,311 new records | All validated |
| QC7: Final cross-validation + expert review | Full corpus (Nemotron-3-Super-120b) | 87.7% agreement, 4.40/5.0 |

**QC7 breakdown:** Taxonomy accuracy 4.99/5, Scenario quality 4.40/5, Structure accuracy 4.82/5, Assessment quality 4.02/5, Game integration 4.55/5. Assessment quality is the weakest dimension -- some rubrics are more generic than ideal.

## Benchmark Results

Five models were benchmarked on the 182 anchor records in Identify and Explain modes, scored on a 1--4 scale by qwen3.5-400b:

| Model | Size | Identify | Explain |
|-------|------|----------|---------|
| qwen2.5:7b | 7B | 2.52 | 2.22 |
| gpt-oss-20b | 20B | 2.61 | 2.41 |
| gpt-oss-120b | 120B | 3.15 | 2.93 |
| Nemotron-3-Super-120b | 120B | 3.40 | 3.54 |
| qwen3.5-122b* | 122B | 3.47 | 3.60 |

*qwen3.5-122b was benchmarked on the earlier 167-anchor set; other models on the current 182-anchor set.

**Fine-tuning target:** qwen2.5:7b, with a goal of pushing Explain from 2.22 toward 3.0+ via QLoRA on the full corpus.

## Getting Started

### Download the Corpus

The corpus is hosted on HuggingFace:

```bash
# Using the HuggingFace CLI
huggingface-cli download bertybaums/good-thinking-corpus

# Or clone the dataset repo
git clone https://huggingface.co/datasets/bertybaums/good-thinking-corpus
```

### Load in Python

```python
from datasets import load_dataset

dataset = load_dataset("bertybaums/good-thinking-corpus")

# Inspect a record
print(dataset["train"][0]["taxonomy_label"])
print(dataset["train"][0]["scenario"]["text"])
```

Or load the JSONL directly:

```python
import json

records = []
with open("good-thinking-corpus-v1.0.jsonl") as f:
    for line in f:
        records.append(json.loads(line))

print(f"{len(records)} records across {len(set(r['taxonomy_code'] for r in records))} codes")
```

### Run the Benchmark

```bash
cd corpus-tools
cp .env.example .env  # Add your API keys

# Benchmark a model on all 182 anchors
python benchmark.py --model qwen2.5:7b --mode identify
python benchmark.py --model qwen2.5:7b --mode explain
```

The benchmark script supports any OpenAI-compatible endpoint. Results are written to `corpus-tools/output/benchmarks/`.

## Training

The repo includes a QLoRA fine-tuning pipeline targeting qwen2.5:7b:

```
train/
  prepare_data.py      # Corpus records -> chat-format conversations
  sft_qlora.py         # QLoRA training (Unsloth + TRL + PEFT)
  submit.slurm         # SLURM job for HPC submission
  eval_after_training.sh  # Post-training benchmark comparison
```

**Pipeline:**

1. `prepare_data.py` converts 27,252 corpus records into instruction-tuning conversations (scenario as user prompt, structured analysis as assistant response). Outputs a train/val split.
2. `sft_qlora.py` runs QLoRA training on `unsloth/Qwen2.5-7B-Instruct` (4-bit quantized, LoRA r=16, all attention + MLP projections, 3 epochs).
3. `submit.slurm` submits to a SLURM cluster (tested on RTX 4090, ~4,860 steps).
4. `eval_after_training.sh` benchmarks the trained model against the pre-training baselines.

## Project Structure

```
good-thinking-bot/
  corpus-tools/              # Corpus generation and evaluation pipeline
    schema.py                #   Pydantic models for corpus records
    taxonomy.py              #   182-code taxonomy definitions
    benchmark.py             #   Model evaluation (identify/classify/explain)
    01_anchor_craft.py       #   Interactive anchor creation
    02_dataset_adapt.py      #   Adapt existing datasets into corpus format
    03_synthetic_gen.py      #   Synthetic generation with verification
    04_cross_validate.py     #   Blind reclassification QC
    05_mechanical_verify.py  #   Automated math checking for DT/GT
    06_coverage_dashboard.py #   Taxonomy coverage matrix
    output/                  #   Generated JSONL files and benchmarks
      release/               #   v1.0 release files (JSONL, taxonomy, license)
  train/                     # QLoRA fine-tuning pipeline
    prepare_data.py          #   Corpus -> instruction-tuning format
    sft_qlora.py             #   QLoRA training script
    submit.slurm             #   SLURM job submission
    eval_after_training.sh   #   Post-training evaluation
  data/external/             # Source datasets (Jin, FOLIO, Corr2Cause, SemEval)
  qlora_merge/               # Adapter merging PoC (linear, TIES, DARE, router)
  reports/                   # QC reports, benchmarks, analyses
  notes/                     # Design documents
```

**Note:** The bulk corpus files (27,252 records) are hosted on [HuggingFace](https://huggingface.co/datasets/bertybaums/good-thinking-corpus), not in this repository. The repo contains the pipeline code, taxonomy definitions, anchor records, and training infrastructure.

## Citation

```bibtex
@dataset{baumgaertner2026goodthinking,
  title     = {Good Thinking Corpus v1.0: A Training Dataset for Critical
               Thinking, Logic, and Decision Theory Education},
  author    = {Baumgaertner, Bert and Potter, Nicholas},
  year      = {2026},
  publisher = {HuggingFace / Zenodo},
  doi       = {10.5281/zenodo.19324917},
  license   = {CC BY-NC-SA 4.0},
  url       = {https://huggingface.co/datasets/bertybaums/good-thinking-corpus}
}
```

## License

The corpus and pipeline code are released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Adapted records draw on source datasets with their own licenses (see [Data Sources](#source-breakdown) above). Van Cleave's *Introduction to Logic and Critical Thinking* is used under CC BY 4.0.

## Authors

- **Bert Baumgaertner** -- Department of Philosophy, University of Idaho
- **Nicholas Potter** -- Department of Agricultural Economics and Rural Sociology, University of Idaho

## Acknowledgments

- **MindRouter** -- University of Idaho HPC infrastructure for LLM inference and training
- **Claude Code** (Anthropic) -- Corpus pipeline development and quality assurance
- **Source datasets:** Van Cleave, *Introduction to Logic and Critical Thinking* (CC BY 4.0); Jin et al. fallacy detection corpus; FOLIO logical reasoning dataset; Corr2Cause causal reasoning dataset; SemEval 2020 Task 11 propaganda detection dataset
