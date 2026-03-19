# Datasets, Corpora, and Benchmarks for Logic, Critical Thinking, and Reasoning

Research conducted March 2026. Comprehensive survey of existing resources that could be used or adapted for training language models on critical thinking skills.

---

## 1. Formal Logic Datasets

### FOLIO (First-Order Logic Open-domain Inference)
- **Where**: [HuggingFace](https://huggingface.co/datasets/yale-nlp/FOLIO) | [GitHub](https://github.com/Yale-LILY/FOLIO) | [Paper](https://arxiv.org/abs/2209.00840)
- **Size**: 1,435 examples (unique conclusions) paired with 487 sets of premises
- **Format**: Natural language premises + conclusions paired with first-order logic (FOL) annotations. Task: determine if conclusion is True/False/Unknown given premises
- **Skills**: First-order logic reasoning, deductive reasoning, NL-to-FOL translation
- **Quality**: Expert-written (Yale), FOL correctness verified by automated inference engine. High quality but relatively small
- **License**: CC-BY-4.0

### ProofWriter
- **Where**: [Allen AI](https://allenai.org/data/proofwriter) | [Paper](https://arxiv.org/abs/2012.13048)
- **Size**: ~500K synthetic examples across multiple depth levels (D0-D5)
- **Format**: Theory (NL rules + facts) + query -> answer (True/False/Unknown) + proof tree. Depths D0-D5 require 0-5 chaining steps
- **Skills**: Multi-step deductive reasoning, proof generation, modus ponens, logical chaining
- **Quality**: Synthetic/template-based. Linguistically simple but logically rigorous. Lacks diversity in language
- **Limitations**: Template-generated, limited linguistic naturalness

### RuleTaker
- **Where**: [Allen AI](https://allenai.org/data/ruletaker)
- **Size**: ~500K examples
- **Format**: Similar to ProofWriter -- rules + facts in NL, query True/False
- **Skills**: Simple implication rules (mainly modus ponens), logical deduction
- **Quality**: Predecessor to ProofWriter; simpler rule types

### ProntoQA
- **Where**: [GitHub](https://github.com/asaparov/prontoqa)
- **Size**: Configurable synthetic generation (typically thousands of examples)
- **Format**: Ontology-generated QA with chain-of-thought proofs. Each example has a unique proof
- **Skills**: Deductive reasoning from ontological hierarchies, syllogistic reasoning
- **Quality**: Synthetic, amenable to formal verification. Limited linguistic diversity
- **Limitations**: Overly simplistic rules, template-based

### ergotts/propositional-logic
- **Where**: [HuggingFace](https://huggingface.co/datasets/ergotts/propositional-logic)
- **Size**: 400 proofs, each with 4 natural language representations (1,600 total)
- **Format**: Formal propositional logic proofs with natural language translations
- **Skills**: Propositional logic, formal proof understanding

### text2log
- **Where**: [HuggingFace](https://huggingface.co/datasets/text2log)
- **Size**: 100,000 examples
- **Format**: English sentences paired with First-Order Logic translations (using ccg2lambda)
- **Skills**: NL-to-FOL translation, logical formalization

### LogicBench
- **Where**: [OpenReview](https://openreview.net/forum?id=7NR2ZVzZxx) | [Paper](https://arxiv.org/abs/2404.15522)
- **Size**: Covers 25 reasoning patterns
- **Format**: NL question-answering covering propositional, first-order, and non-monotonic logics
- **Skills**: Modus ponens, modus tollens, disjunctive syllogism, hypothetical syllogism, DeMorgan's laws, quantifier reasoning, default reasoning, and more
- **Quality**: Systematically constructed to cover formal logic patterns. LLMs achieve ~52% (near random), showing genuine difficulty
- **Limitations**: Relatively new, still being validated

### LogiCoT
- **Where**: [HuggingFace](https://huggingface.co/datasets/datatune/LogiCoT)
- **Size**: Large-scale instruction dataset
- **Format**: Chain-of-thought demonstrations for logical reasoning
- **Skills**: Formal logical reasoning with step-by-step explanations

### nlplabtdtu/data-syllogism-v3
- **Where**: [HuggingFace](https://huggingface.co/datasets/nlplabtdtu/data-syllogism-v3)
- **Format**: Syllogistic reasoning problems
- **Skills**: Categorical syllogisms, validity testing

---

## 2. Fallacy Detection Datasets

### Logic (Jin et al., 2022) -- Logical Fallacy Detection
- **Where**: [HuggingFace](https://huggingface.co/datasets/tasksource/logical-fallacy) | [GitHub](https://github.com/causalNLP/logical-fallacy) | [Paper](https://arxiv.org/abs/2202.13758)
- **Size**: 3,761 examples (2,680 train / 570 dev / 511 test) + LogicClimate challenge set
- **Format**: Text segments labeled with one of 14 fallacy categories
- **Categories**: Ad hominem, ad populum, appeal to emotion, circular reasoning, equivocation, fallacy of credibility, fallacy of extension, fallacy of logic, fallacy of relevance, false causality, false dilemma, faulty generalization, intentional, miscellaneous
- **Skills**: Fallacy identification and classification
- **Quality**: Reasonable size for fine-tuning, well-defined categories. Includes climate domain challenge set
- **License**: MIT

### MAFALDA
- **Where**: [GitHub](https://github.com/ChadiHelwe/MAFALDA) | [Paper](https://arxiv.org/abs/2311.09761) (NAACL 2024)
- **Size**: 200 annotated texts (unifies and merges multiple prior fallacy datasets)
- **Format**: Multi-label annotation with explanations, hierarchical taxonomy across 3 levels of granularity
- **Skills**: Fallacy detection and classification with unified taxonomy across prior work
- **Quality**: High -- expert annotations with explanations, handles subjectivity explicitly. Small but carefully curated
- **License**: CC-BY-SA
- **Note**: Particularly valuable because it unifies fragmented prior fallacy taxonomies

### CoCoLoFa (Common Logical Fallacies in News Comments)
- **Where**: [Paper](https://arxiv.org/abs/2410.03457) (EMNLP 2024)
- **Size**: 7,706 comments for 648 news articles
- **Format**: News comments labeled by fallacy type, crowd-written with LLM assistance
- **Skills**: Fallacy detection in realistic news comment contexts

### MMLU Logical Fallacies
- **Where**: [HuggingFace](https://huggingface.co/datasets/brucewlee1/mmlu-logical-fallacies)
- **Format**: Multiple-choice questions about identifying logical fallacies
- **Skills**: Fallacy identification in exam-style format

### Argotario
- **Where**: Referenced in fallacy detection literature
- **Size**: 430 arguments across 6 fallacy types
- **Format**: Gamified crowdsourced fallacy examples
- **Skills**: Loaded language, appeal to fear, appeal to ridicule, hasty generalization, ad hominem, false dilemma
- **Quality**: Small but notable for gamified collection approach

### Propaganda Techniques Detection (SemEval-2020 Task 11)
- **Where**: [HuggingFace](https://huggingface.co/datasets/SemEvalWorkshop/sem_eval_2020_task_11) | [Zenodo](https://zenodo.org/records/3952415) | [Paper](https://aclanthology.org/2020.semeval-1.186/)
- **Size**: 371 training articles + 75 test articles, 6,129 labeled propaganda spans
- **Format**: Two subtasks: (1) span identification in news articles, (2) technique classification into 14 categories
- **Techniques/Categories**: Loaded Language (2,123), Name Calling (1,058), Repetition (621), Exaggeration/Minimization, Doubt, Appeal to Fear/Prejudice, Flag-Waving, Causal Oversimplification, Slogans, Appeal to Authority, Black-and-White Fallacy, Thought-terminating Cliches, Bandwagon/Reductio ad Hitlerum, Straw Men/Whataboutism/Red Herring
- **Skills**: Propaganda/fallacy detection in news text, span-level annotation
- **Quality**: High -- 250 teams participated in shared task. Class imbalance is a known issue
- **Note**: 12 of the 18 propaganda techniques qualify as logical fallacies -- highly relevant for fallacy training

---

## 3. Argument Mining Corpora

### Argument Annotated Essays Corpus (AAEC) -- Stab & Gurevych
- **Where**: [TU Darmstadt](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2422) | [Paper](https://aclanthology.org/J17-3005/)
- **Size**: 402 persuasive essays containing 751 major claims, 1,506 claims, 3,832 premises, 3,613 support relations, 219 attack relations
- **Format**: Essays annotated with argument components (major claim, claim, premise) and argumentative relations (support, attack)
- **Skills**: Argument component identification, relation classification, argument structure parsing
- **Quality**: Gold standard for argument mining. Inter-annotator agreement is substantial
- **License**: Research use

### Kialo Debate Dataset
- **Where**: [Zenodo](https://zenodo.org/records/5341248) | Collected by Durmus et al. (2019)
- **Size**: 47,219 argument claims from 1,560 discussion threads
- **Format**: Tree-structured debates with pro/con labels. Each node: text, author, votes, relation polarity (+1 support / -1 attack)
- **Skills**: Argument structure, support/attack classification, debate analysis
- **Quality**: Moderated platform ensures accurate pro/con labels. Natural arguments from real debates
- **Note**: Excellent source of structured argument data with natural language

### IBM Debater Datasets (multiple)
- **Where**: [HuggingFace](https://huggingface.co/datasets/ibm-research/argument_quality_ranking_30k) | [Paper](https://aclanthology.org/D19-1564/)
- **Datasets**:
  - **IBM-Rank-30k**: 30,000+ arguments across 71 topics, each with a quality score
  - **IBM-ArgQ-5.3kArgs**: 5,300 arguments with individual quality annotations (15-17 annotators each)
  - **IBM-ArgQ-9.1kPairs**: 9,100 argument pairs with pairwise quality comparisons
  - **debate_speeches**: Available on HuggingFace
- **Format**: Arguments with quality scores/rankings, topic labels, stance labels
- **Skills**: Argument quality assessment, argument strength ranking, persuasiveness
- **Quality**: Very high -- IBM research project with extensive annotation. Controls for confounds like length
- **License**: Research use (check specific datasets)

### PE Corpus (Persuasive Essays)
- **Where**: Referenced in argument mining literature
- **Size**: 402 essays, 2,235 paragraphs with argumentation graphs
- **Format**: Essays annotated with full argumentation graphs
- **Skills**: Argument mining, claim/premise identification

### AMT Corpus (Peldszus and Stede, 2015)
- **Where**: Academic distribution
- **Size**: 112 short texts (3-5 sentences each), 576 argumentative discourse units
- **Format**: Short texts with fine-grained argumentative annotation
- **Skills**: Argument component and relation identification in short texts

### ECHR Corpus (European Court of Human Rights)
- **Where**: Academic distribution
- **Format**: Legal texts annotated for premises, conclusions, non-argumentative sentences
- **Skills**: Legal argument mining

---

## 4. Critical Thinking Benchmarks

### ReClor (Reading Comprehension requiring Logical Reasoning)
- **Where**: [Website](https://whyu.me/reclor/) | [GitHub](https://github.com/yuweihao/reclor) | [Paper](https://arxiv.org/abs/2002.04326) (ICLR 2020)
- **Size**: 6,138 questions (4,638 train / 500 dev / 1,000 test)
- **Format**: Multiple-choice reading comprehension from LSAT and GMAT standardized tests. Context passage + question + 4 answer options
- **Skills**: Logical reasoning in reading comprehension, argument evaluation, assumption identification, flaw detection, strengthening/weakening arguments
- **Quality**: Very high -- from real standardized tests. EASY/HARD split identifies bias-free examples
- **License**: Non-commercial research only
- **Note**: LSAT questions are particularly aligned with critical thinking education (argument analysis, assumption identification, flaw detection)

### LogiQA 2.0
- **Where**: [GitHub](https://github.com/csitfun/LogiQA2.0) | [HuggingFace](https://huggingface.co/datasets/tasksource/logiqa-2.0-nli) | [Paper](https://ieeexplore.ieee.org/document/10174688/)
- **Size**: 15,708 questions (MRC format) + 35,000 NLI pairs
- **Format**: Multiple-choice questions from Chinese Civil Service Exam (bilingual Chinese/English) + NLI pairs (Entailed / Not Entailed)
- **Skills**: Categorical reasoning, sufficient/necessary conditions, disjunctive reasoning, conjunctive reasoning, conditional reasoning
- **Quality**: Professional translation, improved over LogiQA 1.0 (which had 8,678 questions). Removed culturally-specific items
- **License**: Research use

### LSAT Logic Games Dataset
- **Where**: Zhong et al. dataset | [Paper](https://arxiv.org/abs/2409.19012)
- **Format**: Analytical reasoning problems with constraint satisfaction from LSAT exams
- **Skills**: Multi-step constraint satisfaction, rule application, scheduling/ordering problems
- **Quality**: Very challenging multi-step logic requiring simultaneous constraint satisfaction
- **Limitations**: Copyright restrictions on LSAT materials

### CritPt (Complex Research Integrated Thinking -- Physics Test)
- **Where**: [GitHub](https://github.com/CritPt-Benchmark/CritPt)
- **Size**: 71 challenges, 190 checkpoints
- **Format**: Research-level physics reasoning tasks
- **Skills**: Deep analytical reasoning (domain-specific to physics)

### Benchmarking Critical Questions Generation
- **Where**: [Paper](https://arxiv.org/abs/2505.11341)
- **Format**: Evaluates AI's ability to generate critical questions about arguments in texts
- **Skills**: Critical question generation, argument evaluation

---

## 5. Cognitive Bias Datasets

### CoBBLEr (COgnitive Bias Benchmark for LLMs as EvaluatoRs)
- **Where**: [Project page](https://minnesotanlp.github.io/cobbler-project-page/) | [Paper](https://arxiv.org/abs/2309.17012) (ACL Findings 2024)
- **Size**: 13,465 prompts derived from 50 QA instructions (BigBench + Eli5)
- **Format**: Evaluation prompts testing 6 cognitive biases: Egocentric bias, Anchoring bias, Confirmation bias, Primacy effect, Recency effect, Halo effect
- **Skills**: Identifying/measuring cognitive biases in LLM evaluation behavior
- **Quality**: Systematic evaluation framework. Found 40% of LLM comparisons show bias
- **Limitations**: Focused on LLM-as-evaluator setting, not general bias detection in text

### CBEval
- **Where**: [Paper](https://arxiv.org/abs/2412.03605)
- **Format**: Framework for evaluating and interpreting cognitive biases in LLMs
- **Skills**: Cognitive bias evaluation

### BBQ (Bias Benchmark for QA)
- **Where**: [Paper](https://arxiv.org/abs/2110.08193) (ACL Findings 2022)
- **Size**: 58,492 unique multiple-choice QA instances from 325 hand-crafted templates
- **Format**: Under-informative and adequately-informative contexts paired with questions. Tests whether models rely on social stereotypes when information is ambiguous
- **Skills**: Social bias detection, stereotype awareness, reasoning under ambiguity
- **Quality**: Very high -- hand-crafted, covers 9 social dimensions. Widely used benchmark
- **Note**: Tests a specific form of cognitive bias (social stereotypes) rather than general reasoning biases

### Anchoring Bias in LLMs (experimental datasets)
- **Where**: [Paper](https://arxiv.org/abs/2412.06593)
- **Format**: Experimental setups testing anchoring bias with synthetic profiles
- **Skills**: Anchoring bias, insufficient adjustment

**Gap identified**: There is no comprehensive, publicly available dataset specifically designed for teaching/testing cognitive biases like framing effects, base rate neglect, conjunction fallacy, or availability heuristic in text form. This is a significant opportunity for dataset creation.

---

## 6. Decision Theory / Game Theory Datasets

### GTBench
- **Where**: [Paper](https://arxiv.org/abs/2402.12348) (NeurIPS 2024)
- **Format**: Suite of strategic games for LLM-vs-LLM competition
- **Skills**: Strategic reasoning, Nash equilibrium approximation, game-theoretic decision making
- **Quality**: Comprehensive, tests 22 state-of-the-art LLMs

### TMGBench
- **Where**: [Paper](https://arxiv.org/abs/2410.10479)
- **Size**: 144 types of game-theoretic scenarios
- **Format**: Text-based game theory problems
- **Skills**: Strategic reasoning in varied game types

### CHBench (Cognitive Hierarchy Benchmark)
- **Where**: [Paper](https://arxiv.org/abs/2508.11944)
- **Format**: Strategic reasoning evaluation using cognitive hierarchy theory
- **Skills**: Multi-level strategic thinking, theory of mind in games

**Gap identified**: No standard dataset exists for teaching expected utility calculation, probability puzzles, or decision theory concepts in an educational format. The existing benchmarks evaluate LLM strategic play rather than teaching decision theory.

---

## 7. Analogical Reasoning Datasets

### BATS (Bigger Analogy Test Set)
- **Where**: [Website](https://vecto.space/projects/BATS/)
- **Size**: 10 categories x 50 word pairs per category = 500 word pairs
- **Format**: A:B :: C:D proportional analogies covering morphology and semantics
- **Skills**: Lexical/semantic analogy
- **Limitations**: Word-level only, not argument-by-analogy

### E-KAR (Knowledge-intensive Analogical Reasoning)
- **Where**: [Paper](https://arxiv.org/abs/2203.08480)
- **Format**: Analogical reasoning problems from Chinese Civil Service Exams with explanations/rationales
- **Skills**: Complex analogical reasoning requiring background knowledge
- **Quality**: Includes rationales for each answer, making it useful for training

### ARN (Analogical Reasoning on Narratives)
- **Where**: [Paper](https://arxiv.org/abs/2310.00996)
- **Format**: Four categories: far analogies, near analogies, far disanalogies, near disanalogies over narrative texts
- **Skills**: Cross-domain and within-domain analogical mapping over stories
- **Quality**: First large dataset for analogical reasoning over narratives

### SAT Analogy Dataset
- **Where**: Academic distribution (Turney, 2006)
- **Size**: 374 analogy problems
- **Format**: SAT-style A:B :: C:D multiple choice
- **Skills**: Psychometric-style analogical reasoning
- **Limitations**: Small, older dataset

### Google Analogy Test Set
- **Where**: Distributed with word2vec
- **Size**: ~19,544 analogy questions
- **Format**: Word-level proportional analogies
- **Skills**: Semantic and syntactic word analogies
- **Limitations**: Word-level only

**Gap identified**: No dataset specifically covers argument by analogy (the informal reasoning pattern of drawing conclusions based on similarities between cases). This is distinct from word/concept analogies.

---

## 8. Causal Reasoning Datasets

### Corr2Cause
- **Where**: [HuggingFace](https://huggingface.co/datasets/causal-nlp/corr2cause) | [GitHub](https://github.com/causalNLP/corr2cause) | [Paper](https://openreview.net/forum?id=vqIH0ObdqL) (ICLR 2024)
- **Size**: 415,944 total samples (411,452 train / 2,246 dev / 2,246 test)
- **Format**: Correlational statements (premise, avg 424 tokens) -> causal relationship claim (hypothesis, avg 11 tokens) -> valid/invalid
- **Skills**: Distinguishing correlation from causation, causal inference validity
- **Quality**: Large-scale, rigorously constructed. 18.57% valid samples (realistic base rate). First pure causal inference benchmark for LLMs
- **Note**: Extremely relevant -- tests the "correlation is not causation" distinction that is core to critical thinking

### COPA (Choice of Plausible Alternatives)
- **Where**: [GitHub](https://github.com/drwiner/COPA) | SemEval 2012 Task 7
- **Size**: 1,000 examples (500 dev / 500 test)
- **Format**: Premise + "What was the cause?" or "What happened as a result?" + 2 alternatives -> binary choice
- **Skills**: Commonsense causal reasoning
- **Quality**: Small but well-validated. Has multilingual extension (XCOPA)
- **Limitations**: Only 1,000 examples, binary choice

### XCOPA (Cross-lingual COPA)
- **Where**: [GitHub](https://github.com/cambridgeltl/xcopa)
- **Size**: Translation of COPA into 11 languages
- **Format**: Same as COPA but multilingual
- **Skills**: Causal reasoning across languages

### CausalBench
- **Where**: [Paper](https://arxiv.org/abs/2404.06349) | [GitHub](https://github.com/Rainy-ZhouYu/CausalBN-Bench)
- **Format**: Spans textual, mathematical, and coding domains. Evaluates cause-to-effect, effect-to-cause, and interventional reasoning
- **Skills**: Causal structure understanding, interventional reasoning

### BIG-Bench Causal Judgment
- **Where**: [GitHub](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/causal_judgment)
- **Format**: Short stories with causal questions ("Did X cause Y?")
- **Skills**: Causal judgment involving moral, intentional, and counterfactual reasoning

---

## 9. Natural Language Inference (NLI) Datasets

### SNLI (Stanford Natural Language Inference)
- **Where**: [Stanford NLP](https://nlp.stanford.edu/projects/snli/)
- **Size**: 570,000 sentence pairs
- **Format**: Premise-hypothesis pairs labeled entailment / contradiction / neutral
- **Skills**: Textual entailment, contradiction detection, semantic reasoning
- **Quality**: Large, widely used benchmark. Known annotation artifacts (lexical overlap cues)
- **License**: CC-BY-SA-4.0

### e-SNLI
- **Where**: [GitHub](https://github.com/OanaMariaCamburu/e-SNLI) | [Paper](https://papers.nips.cc/paper/8163)
- **Size**: Same as SNLI (~570K) with added explanations
- **Format**: SNLI + human-written natural language explanations + highlighted rationale tokens
- **Skills**: Entailment reasoning with explanations
- **Quality**: Adds interpretability layer to SNLI. Explanations focus on non-obvious reasoning steps
- **Note**: Particularly useful for training models that need to explain their reasoning

### MultiNLI (MNLI)
- **Where**: [Website](https://cims.nyu.edu/~sbowman/multinli/)
- **Size**: 433,000 sentence pairs
- **Format**: Same labels as SNLI but across 10 genres (fiction, government, travel, etc.)
- **Skills**: Cross-genre entailment, domain transfer
- **Quality**: More diverse than SNLI. Same annotation artifact issues

### ANLI (Adversarial NLI)
- **Where**: [HuggingFace](https://huggingface.co/datasets/facebook/anli) | [GitHub](https://github.com/facebookresearch/anli) | [Paper](https://arxiv.org/abs/1910.14599)
- **Size**: 169,265 examples across 3 rounds (R1: ~17K, R2: ~45K, R3: ~100K)
- **Format**: Same entailment/contradiction/neutral labels, adversarially collected
- **Skills**: Robust NLI, hard reasoning cases that fool models
- **Quality**: Much harder than SNLI/MNLI -- collected via human-and-model-in-the-loop. Each round targets weaknesses found in previous round
- **License**: CC-BY-NC-4.0

### WANLI (Worker-AI Collaboration for NLI)
- **Where**: [HuggingFace](https://huggingface.co/datasets/alisawuffles/WANLI) | [Paper](https://arxiv.org/abs/2201.05955)
- **Size**: 108,000 sentence pairs
- **Format**: NLI pairs generated by GPT-3, filtered automatically, revised and labeled by humans
- **Skills**: Challenging reasoning patterns in entailment
- **Quality**: Training on WANLI (108K) outperforms training on MNLI (433K) on 7 out-of-domain test sets
- **Note**: Efficient dataset -- smaller but more effective than larger alternatives

### AbductiveNLI (alpha-NLI)
- **Where**: [Website](http://abductivecommonsense.xyz/) | [GitHub](https://github.com/allenai/abductive-commonsense-reasoning) | [Paper](https://arxiv.org/abs/1908.05739) (ICLR 2020)
- **Size**: 20,000+ narrative contexts, 200,000+ explanations
- **Format**: Two observations (beginning + ending) + two possible explanations -> choose more likely one
- **Skills**: Abductive reasoning, commonsense inference, narrative understanding
- **Quality**: Best model achieves 68.9% vs. human 91.4%, showing genuine difficulty

### LogicNLI
- **Where**: Referenced in logical reasoning literature
- **Format**: NLI with full FOL spectrum, labels: Contradiction, Entailment, Neutral, Paradox
- **Skills**: Logical inference with negation, quantifiers, logical operators

### EntailmentBank
- **Where**: [Allen AI](https://allenai.org/data/entailmentbank) | [GitHub](https://github.com/allenai/entailment_bank) | [Paper](https://arxiv.org/abs/2104.08661)
- **Size**: Multi-step entailment trees; average tree has 7.6 nodes across 3.2 entailment steps
- **Format**: Science question + answer + entailment tree (proof) from known facts through intermediate conclusions. Three difficulty levels
- **Skills**: Multi-step entailment, proof generation, explicit reasoning chains
- **Quality**: First dataset of multi-step entailment trees. Makes reasoning steps explicit
- **Note**: Very useful for teaching step-by-step logical reasoning

### FEVER (Fact Extraction and VERification)
- **Where**: [Website](https://fever.ai/) | [Paper](https://arxiv.org/abs/1803.05355)
- **Size**: 185,445 claims
- **Format**: Claims labeled Supported / Refuted / Not Enough Information against Wikipedia
- **Skills**: Evidence evaluation, fact verification, textual entailment
- **Quality**: Large-scale, multi-stage (retrieval + verification). Well-established benchmark

---

## 10. Math/Logic Reasoning Benchmarks (Beyond GSM8K)

### BIG-Bench Hard (BBH)
- **Where**: [HuggingFace](https://huggingface.co/datasets/maveriq/bigbenchhard)
- **Size**: 23 tasks, each with hundreds of examples
- **Format**: Multiple formats depending on task (multiple choice, free response)
- **Relevant logical tasks**:
  - **Logical Deduction** (3/5/7 objects): Deduce ordering from spatial relationship clues
  - **Causal Judgment**: Causal questions about short stories
  - **Boolean Expressions**: Evaluate nested boolean logic
  - **Formal Fallacies**: Identify syllogistic fallacies
  - **Web of Lies**: Truth-teller/liar puzzles
- **Skills**: Multi-step algorithmic reasoning, logical deduction, causal reasoning
- **Quality**: Curated for difficulty -- selected because LLMs perform poorly on them

### ARC (AI2 Reasoning Challenge)
- **Where**: [HuggingFace](https://huggingface.co/datasets/allenai/ai2_arc) | [Paper](https://arxiv.org/abs/1803.05457)
- **Size**: 7,787 grade-school science questions + 14M sentence corpus
- **Format**: Multiple-choice science questions, split into Easy and Challenge sets
- **Skills**: Scientific reasoning, knowledge application, multi-step inference
- **Quality**: Challenge set filtered to include only questions that retrieval-based models get wrong

### LogicGame
- **Where**: [Paper](https://arxiv.org/abs/2408.15778)
- **Format**: Rule-based reasoning games with varying difficulty, verifiability, and determinism
- **Skills**: Rule application, constraint satisfaction, logical deduction

### CLUTRR (Compositional Language Understanding and Text-based Relational Reasoning)
- **Where**: [HuggingFace](https://huggingface.co/datasets/CLUTRR/v1) | [GitHub](https://github.com/facebookresearch/clutrr) | [Paper](https://arxiv.org/abs/1908.06177)
- **Size**: Configurable (semi-synthetic generation)
- **Format**: Short stories about families -> infer kinship relations not explicitly stated
- **Skills**: Inductive reasoning, compositional generalization, multi-step relational reasoning
- **Quality**: Precisely tests systematic generalization. Can add noise facts for robustness testing
- **License**: MIT

### Atlas-Reasoning
- **Where**: [HuggingFace](https://huggingface.co/datasets/AtlasUnified/Atlas-Reasoning)
- **Format**: Multi-category reasoning dataset covering syllogistic arguments, propositional logic, predicate logic, deduction rules, formal systems, and logical fallacies
- **Skills**: Broad coverage of reasoning types

### sdiazlor/logic-problems-reasoning-dataset
- **Where**: [HuggingFace](https://huggingface.co/datasets/sdiazlor/logic-problems-reasoning-dataset)
- **Format**: Multiple problem types: syllogisms, truth-teller/liar puzzles, cryptograms, arithmetic, K-level thinking
- **Skills**: Diverse logical puzzle solving

### GLoRE (General Logical Reasoning Evaluation)
- **Where**: [GitHub](https://github.com/csitfun/glore)
- **Format**: Assembled suite of multiple logical reasoning benchmarks
- **Skills**: Unified evaluation across logical reasoning types
- **Limitations**: Recent LLMs achieve very high performance on component datasets

---

## Summary: Key Gaps and Opportunities

Based on this survey, the following areas are **underserved** and represent opportunities for new dataset creation:

1. **Cognitive biases as reasoning errors**: No dataset teaches recognition of framing effects, anchoring bias, base rate neglect, conjunction fallacy, availability heuristic, etc. in natural text. CoBBLEr tests LLM biases but doesn't teach bias recognition.

2. **Argument by analogy**: Existing analogy datasets test word/concept analogies, not the informal reasoning pattern of drawing conclusions based on case similarities. No dataset evaluates whether an analogy is strong or weak.

3. **Decision theory / expected utility in educational format**: Game theory benchmarks test LLM strategic play but don't teach decision theory concepts (expected value, risk assessment, probability assessment).

4. **Integrated critical thinking**: No single dataset combines fallacy detection + argument evaluation + bias recognition + evidence assessment in a unified format suitable for education.

5. **Fallacy detection with explanations at scale**: MAFALDA has explanations but only 200 texts. The Jin et al. dataset has ~3,700 examples but no explanations. A larger dataset with both labels and reasoning explanations would be valuable.

6. **Everyday reasoning scenarios**: Most datasets use academic or formal contexts. Few present the kind of everyday reasoning situations (news articles, social media posts, advertisements, political speech) where critical thinking is most needed.

---

## Recommended Priority Datasets for Your Project

For building training data for a critical thinking educational game, these are the most directly useful:

### Tier 1 -- Directly Applicable
1. **Logic (Jin et al.)** -- Fallacy classification, 3,761 examples, MIT license
2. **Propaganda Techniques (SemEval 2020)** -- Fallacy-adjacent, 6,129 labeled spans
3. **ReClor** -- LSAT/GMAT logical reasoning, 6,138 questions (non-commercial)
4. **LogiQA 2.0** -- Critical reasoning exam questions, 15,708 questions
5. **Corr2Cause** -- Correlation vs. causation, 415K examples
6. **IBM-Rank-30k** -- Argument quality, 30K arguments
7. **Kialo** -- Structured debate with pro/con labels, 47K arguments

### Tier 2 -- Useful with Adaptation
8. **FOLIO** -- Formal logic with NL, 1,435 examples
9. **MAFALDA** -- Fallacy detection with explanations, 200 texts
10. **EntailmentBank** -- Step-by-step reasoning chains
11. **e-SNLI** -- NLI with explanations, 570K examples
12. **ANLI** -- Hard NLI examples, 169K examples
13. **BIG-Bench Hard** (logical deduction, formal fallacies, causal judgment tasks)
14. **LogicBench** -- 25 formal logic patterns

### Tier 3 -- Supplementary / Reference
15. **ProofWriter / ProntoQA** -- Synthetic logic (template-based)
16. **AAEC** -- Argument structure in essays
17. **COPA** -- Causal commonsense reasoning
18. **BBQ** -- Social bias/stereotype awareness
19. **ARN** -- Narrative analogies
20. **CoBBLEr** -- Cognitive bias evaluation framework
