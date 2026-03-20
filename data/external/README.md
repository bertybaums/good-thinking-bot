# External Datasets for Sprint 2

Downloaded: 2026-03-20

## 1. Jin et al. Fallacy Detection (`jin_fallacy.jsonl`)

- **Source**: [tasksource/logical-fallacy](https://huggingface.co/datasets/tasksource/logical-fallacy)
- **Paper**: Jin et al. (2022), "Logical Fallacy Detection" (arXiv:2202.13758)
- **License**: Check original paper/dataset card
- **Records**: 3,761 (train: 2,680 / dev: 570 / test: 511)
- **Taxonomy mapping**: A5-A7 (fallacies)
- **Fields**:
  - `config`: dataset subset (e.g., "edu")
  - `source_article`: text containing the fallacy
  - `logical_fallacies`: fallacy label (13 categories)
  - `split`: train/dev/test
- **Label distribution**:
  - faulty generalization: 574
  - intentional: 480
  - ad hominem: 398
  - appeal to emotion: 308
  - ad populum: 295
  - false causality: 289
  - fallacy of relevance: 265
  - fallacy of credibility: 263
  - fallacy of logic: 240
  - fallacy of extension: 205
  - false dilemma: 190
  - circular reasoning: 178
  - equivocation: 76

## 2. FOLIO - First-Order Logic Reasoning (`folio.jsonl`)

- **Source**: [tasksource/folio](https://huggingface.co/datasets/tasksource/folio) (mirror of [Yale-LILY/FOLIO](https://github.com/Yale-LILY/FOLIO))
- **Paper**: Han et al. (2022), "FOLIO: Natural Language Reasoning with First-Order Logic" (arXiv:2209.00840)
- **License**: CC-BY-4.0
- **Records**: 1,204 (train: 1,001 / validation: 203)
- **Taxonomy mapping**: A2 (deductive logic)
- **Fields**:
  - `story_id`: identifier for the premise set
  - `premises`: natural language premises
  - `premises-FOL`: first-order logic translation of premises
  - `conclusion`: natural language conclusion
  - `conclusion-FOL`: first-order logic translation of conclusion
  - `label`: True (460) / Uncertain (393) / False (351)
  - `example_id`: unique example identifier
  - `split`: train/validation
- **Note**: The official `yale-nlp/FOLIO` on HuggingFace is gated (requires authentication). This uses the `tasksource/folio` mirror which is freely accessible.

## 3. Corr2Cause (`corr2cause.jsonl`)

- **Source**: [causalnlp/corr2cause](https://huggingface.co/datasets/causalnlp/corr2cause)
- **Paper**: Jin et al. (2024), "Can Large Language Models Infer Causation from Correlation?"
- **License**: Check original dataset card
- **Records**: 2,238 (test: 1,162 / validation: 1,076) -- filtered to dev+test only; full dataset has 207,972 including train
- **Taxonomy mapping**: A3.4-A3.5, A8.7 (causal reasoning, correlation vs causation)
- **Fields**:
  - `input`: text describing correlational observations and a causal claim
  - `label`: 0 = invalid causal claim (1,919) / 1 = valid causal claim (319)
  - `num_variables`: number of variables in the scenario
  - `template`: template identifier
  - `split`: test/validation
- **Note**: Heavily imbalanced toward label 0 (invalid). The full train set (205,734 examples) was excluded per spec.

## 4. SemEval 2020 Task 11 - Propaganda Detection (`semeval2020_propaganda.jsonl`)

- **Source**: [Zenodo record 3952415](https://zenodo.org/records/3952415) (Propaganda Techniques Corpus v2)
- **Paper**: Da San Martino et al. (2020), "SemEval-2020 Task 11: Detection of Propaganda Techniques in News Articles" (arXiv:2009.02696)
- **License**: Check original dataset card / task website
- **Records**: 6,129 (training set technique classification labels across 371 articles)
- **Taxonomy mapping**: A9-A10 (rhetorical manipulation, propaganda techniques)
- **Fields**:
  - `article_id`: source article identifier
  - `technique`: propaganda technique label (14 categories)
  - `start`: character offset start in original article
  - `end`: character offset end in original article
  - `span_text`: extracted text span containing the technique
  - `context`: span plus ~200 characters of surrounding context
- **Technique distribution**:
  - Loaded_Language: 2,123
  - Name_Calling,Labeling: 1,058
  - Repetition: 621
  - Doubt: 493
  - Exaggeration,Minimisation: 466
  - Appeal_to_fear-prejudice: 294
  - Flag-Waving: 229
  - Causal_Oversimplification: 209
  - Appeal_to_Authority: 144
  - Slogans: 129
  - Whataboutism,Straw_Men,Red_Herring: 108
  - Black-and-White_Fallacy: 107
  - Thought-terminating_Cliches: 76
  - Bandwagon,Reductio_ad_hitlerum: 72
- **Note**: Only training set labels are included (dev/test labels were not distributed in the Zenodo archive). The HuggingFace version (`SemEvalWorkshop/sem_eval_2020_task_11`) uses a deprecated loading script and is not compatible with current `datasets` library versions.
