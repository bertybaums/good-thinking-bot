# Benchmark Report: qwen3.5-122b Reasoning Capacity Assessment

**Date:** 2026-03-23
**Subject Model:** qwen/qwen3.5-122b (MindRouter, University of Idaho campus HPC)
**Judge Model:** qwen/qwen3.5-400b (MindRouter)
**Corpus:** 167 hand-crafted anchor examples across 5 content tracks

> **Note:** The subject (qwen3.5-122b) and judge (qwen3.5-400b) are from the same model
> family (Qwen 3.5). This may introduce favorable bias in scoring compared to the
> gpt-oss models, which are from a different family. Cross-family comparisons should
> be interpreted with this caveat.

## 1. Executive Summary

qwen3.5-122b substantially outperforms both gpt-oss models across all evaluation modes,
with particularly dramatic gains in classify mode (instruction following) and explain mode
(mechanistic reasoning).

| Mode | gpt-oss-20b | gpt-oss-120b | **qwen3.5-122b** | Best Δ over 120b |
|------|------------|-------------|-----------------|------------------|
| identify | 2.62 | 3.27 | **3.47** | +0.20 |
| classify | 0.10 | 0.29 | **3.90** | +3.62 |
| explain | 2.47 | 3.04 | **3.60** | +0.56 |

**Key findings:**
- **Classify: 3.90/4** — dramatic improvement over gpt-oss models (0.10/0.29),
  demonstrating strong instruction-following capability
- **Explain: 3.60/4** — consistently provides full mechanistic explanations
- **Dennett tools remain hardest** (explain: 2.79) but substantially improved over gpt-oss-120b (2.00)
- **bad_thinking > good_tool gap narrows further** but persists

## 2. Methodology

Identical to prior benchmarks. See gpt-oss-20b report for full methodology.
167 anchors x 3 modes = 501 evaluations. Judge: qwen/qwen3.5-400b.

**Important caveat:** Same-family judge bias. The judge model (qwen3.5-400b)
may be more lenient when scoring responses from a model in the same Qwen family.
The gpt-oss models were judged by the same qwen judge, so any such bias would
artificially inflate qwen3.5-122b scores relative to the gpt-oss scores.

## 3. Results by Track

| Track | 20b Id | 120b Id | **122b Id** | 20b Ex | 120b Ex | **122b Ex** |
|-------|--------|---------|-------------|--------|---------|-------------|
| cognitive_biases | 2.62 | 3.12 | **3.50** | 3.54 | 3.54 | **3.88** |
| decision_theory | 2.81 | 2.58 | **3.00** | 3.03 | 3.42 | **3.71** |
| dennett_tools | 1.93 | 1.29 | **2.86** | 2.00 | 3.00 | **2.79** |
| game_theory | 2.28 | 2.00 | **2.83** | 2.67 | 3.39 | **3.78** |
| logic_critical_thinking | 2.72 | 2.65 | **3.51** | 3.22 | 3.58 | **3.54** |
| microeconomics | 2.80 | 2.07 | **3.33** | 2.87 | 3.47 | **3.73** |

## 4. Results by Difficulty Tier

| Tier | 20b Id | 120b Id | **122b Id** | 20b Ex | 120b Ex | **122b Ex** |
|------|--------|---------|-------------|--------|---------|-------------|
| drill | 2.73 | 2.73 | **3.46** | 3.23 | 3.56 | **3.62** |
| what_if | 2.39 | 1.98 | **2.90** | 2.61 | 3.31 | **3.55** |
| puzzle | 2.33 | 1.50 | **2.83** | 2.83 | 3.00 | **3.67** |

## 5. Results by Pattern Type

| Pattern | 20b Id | 120b Id | **122b Id** | 20b Ex | 120b Ex | **122b Ex** |
|---------|--------|---------|-------------|--------|---------|-------------|
| good_tool | 2.49 | 1.78 | **3.02** | 2.35 | 3.38 | **3.40** |
| bad_thinking | 2.73 | 3.12 | **3.62** | 3.61 | 3.61 | **3.73** |
| dual | 2.61 | 2.32 | **2.93** | 3.11 | 3.29 | **3.71** |

## 6. Classify Mode: The Big Story

| Model | Classify Score | Perfect (4) | Zero (0) |
|-------|---------------|------------|----------|
| gpt-oss-20b | 0.10 | 4/167 | 163/167 |
| gpt-oss-120b | 0.29 | 12/167 | 155/167 |
| qwen3.5-122b | 3.90 | 163/167 | 4/167 |

qwen3.5-122b gets the correct taxonomy code **98% of the time**, compared to
2.4% for gpt-oss-20b and 7% for gpt-oss-120b. This suggests qwen3.5 has
much stronger instruction-following capability — it can output a bare code when asked.

## 7. Weakest Areas (Explain Mode)

Only 5 records scored 0-1 in explain mode:

- **[0] D1.7: The 'surely' operator** (drill)
- **[0] A9.1: Evaluative language and presupposition** (drill)
- **[0] A1.2: Premises and conclusions** (drill)
- **[0] A1.3: Standard form** (drill)
- **[1] A9.2: Assuring, guarding, and discounting** (drill)

## 8. Implications for LoRA Base Model Selection

| Factor | gpt-oss-20b | gpt-oss-120b | qwen3.5-122b |
|--------|------------|-------------|-------------|
| Identify | 2.62 | 3.27 | 3.47 |
| Explain | 2.47 | 3.04 | 3.60 |
| Classify | 0.10 | 0.29 | 3.90 |
| Dennett (explain) | 1.29 | 2.00 | 2.79 |
| good_tool (explain) | 1.78 | 2.35 | 3.40 |
| Parameters | 20B | 120B | 122B |

**qwen3.5-122b is the strongest base model candidate** for LoRA fine-tuning:
- Highest baseline across all modes
- Already handles classify mode well (less to fix via training)
- Dennett tools at 2.79 vs 2.00/1.29 — smaller gap to close
- good_tool patterns at 3.40 vs 2.35/1.78 — significantly better starting point

However, the same-family judge caveat means these numbers may be ~0.2-0.3 higher
than they would be with a truly independent judge. Even accounting for this,
qwen3.5-122b outperforms gpt-oss-120b on every metric.

## Appendix A: Full Results — Identify Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The bartender wants to know: which of these speakers is actually giving an argument? How can you tell?

**Expected Answer:** **Identifying arguments via indicator words** — An argument is a set of premises that attempt to provide a reason that a conclusion is true. The sailor's statement is a chronological narrative with no premises or conclusion — it describes a sequence of events. The dockworker's statement is an argument: 'since' is a premise indicator linking two p

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis to determine who is making an argument and why.

### Step 1: Define the Criteria for an "Argument"
In logic and critical thinking, an **argument** is not merely a heated exchange or a disagreement. It is a specific structure consisting of:
1.  **Premises:** Statements offered as evidence or reasons.
2.  **Conclusion:** A claim that the premises are intended to support or prove.
3.  **Inference:** The logical link connecting the premises to the conclusion (often signaled by words like "since," "because," "therefore," or "so").

If a speaker is simply listing events, stating a fact without a supporting claim, or telling a story, they are **not** making an argument.

### Step 2: Analyze the Sailor's Statement
*   **Statement:**

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the dockworker's statement as the argument and the sailor's as a narrative. They explicitly name 'since' as a premise indicator, break down the premises and conclusion, and explain why the sailor's statement lacks an inferential structure. However, the response does 

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Theodora just gave testimony with several claims. Which is her main conclusion? Which statements are premises? Is there a statement that serves as both a conclusion and a premise?

**Expected Answer:** **Identifying premises, conclusions, and intermediate conclusions** — Theodora's argument has a layered structure. 'The fact that... is shown by the fact that...' reverses the usual order — the conclusion comes first, then the premise. The intermediate conclusion is that the royal household is contributing to the obesity problem (supported by premises about larger por

**Model Response:**
> Based on the testimony provided by Theodora, here is the step-by-step logical breakdown of her argument, followed by an analysis of the reasoning patterns and potential fallacies involved.

### 1. Structural Analysis of the Argument

To identify the components of the argument, we must break down the text into its constituent claims and determine the logical flow (what supports what).

**The Claims:**
1.  **Claim A:** Obesity rates have risen significantly over the past four decades.
2.  **Claim B:** Obesity has become a problem in the kingdom.
3.  **Claim C:** The royal kitchens have been serving larger portions.
4.  **Claim D:** Larger portions lead to overeating.
5.  **Claim E:** The royal household is contributing to the obesity problem.
6.  **Claim F:** The king should reform the royal

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the main conclusion, all premises, and both intermediate conclusions. They accurately map the dependency structure (how claims support one another). However, they do not explicitly note the specific linguistic mechanism mentioned in the Level 4 criteria: that the phr

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe hands you Captain Voss's statement. Rewrite it in standard form: numbered premises with the conclusion last. Does the argument have any sub-arguments?

**Expected Answer:** **Standard form reconstruction** — Standard form lists premises as numbered statements with the conclusion last, marked with 'Therefore.' Voss's argument has two sub-arguments: one eliminating the sewer escape (premises about the locked grate and no scent trail), and one concluding the cart escape (premises about it being the only al

**Model Response:**
> ### Step-by-Step Reconstruction

To rewrite Captain Voss's rambling statement into standard logical form, we must first isolate the distinct claims (premises) and the final claim he is trying to prove (the conclusion). We also need to identify if any premises rely on other premises to be accepted (sub-arguments).

**1. Analysis of the Statement:**
*   *Segment A:* "the prisoner couldn't have escaped through the sewage pipes because the grate was still locked..."
    *   This is a sub-argument. The conclusion of this mini-argument is "The prisoner did not escape via sewage." The premise supporting it is "The grate was locked."
*   *Segment B:* "...and besides, the dogs didn't pick up any scent trail from the cell to the drain."
    *   This is an additional premise supporting the same concl

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly reconstructed the argument in standard form, explicitly identifying the sub-argument structure (eliminating the sewer route) and the main conclusion. Crucially, they included dependency annotations (e.g., 'Derived from 1 and 2') and identified the implicit logical structure (Di

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Aldric has asked you to reconstruct Rosmund's argument in its strongest form. What is she really trying to argue, underneath the hyperbole? And why is the heckler's response unfair?

**Expected Answer:** **Principle of charity in argument reconstruction** — The principle of charity states that when reconstructing an argument, you should try to make it as strong as possible. Rosmund's literal words contain overstatements ('cheap garbage,' 'every tanner will go broke'), but her core argument has a defensible structure: if cheaper foreign imports undercut

**Model Response:**
> ### Step-by-Step Reconstruction and Analysis

To answer Aldric's request, we must first strip away the emotional hyperbole and the specific, easily refutable generalizations Rosmund used ("garbage," "every tanner," "finished"). Then, we must identify the logical flaw in the heckler's counter-argument.

#### 1. Reconstructing Rosmund's Argument (The Principle of Charity)
Rosmund's original statement relies on **hasty generalization** (calling all foreign leather "garbage") and **slippery slope** (imports will inevitably lead to total bankruptcy). However, her core concern is economic survival, not necessarily the intrinsic quality of every single foreign hide.

Under the **Principle of Charity** (interpreting an opponent's argument in its strongest, most reasonable form), Rosmund is actuall

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly reconstructs Rosmund's argument by stripping away hyperbole and focusing on the core economic logic of price competition and market displacement (Level 3 criteria). Furthermore, the response explicitly identifies and explains the 'Principle of Charity' as the governing pattern,

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Councillor Drava's conclusion says the state 'should' do something. Her premise says something 'is' the case. What is missing? What assumption would you need to add to make this argument valid? And once you add it, does the argument actually work?

**Expected Answer:** **Missing premises and the is-ought gap** — Drava's argument has a descriptive premise (children of unmarried couples often have emotional difficulties) and a normative conclusion (the state should discourage this). Any argument with a normative conclusion requires at least one normative premise — this is the is-ought gap. The missing premise

**Model Response:**
> To analyze Councillor Drava's argument, we must first break down its logical structure to identify the disconnect between the evidence provided and the conclusion drawn.

### 1. Deconstructing the Argument
*   **Premise (Descriptive Claim):** "Children raised by unmarried couples often have emotional difficulties."
    *   *Nature:* This is an empirical observation about the world (what *is*). It describes a correlation or a statistical trend.
*   **Conclusion (Normative Claim):** "The state should discourage unmarried couples from raising children."
    *   *Nature:* This is a prescriptive statement about policy or morality (what *ought* to be). It suggests a specific course of action.

### 2. Identifying the Missing Link (The Gap)
The scribe correctly identifies that the argument jumps f

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the missing normative premise (the is-ought gap) and explicitly names the logical mechanism (Hume's Law/Naturalistic Fallacy). Furthermore, they go beyond the basic requirements by thoroughly analyzing why the argument remains unsound even with the premise supplied, 

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The chronicler has two statements about the bridge collapse. Which one is an argument and which is an explanation? How can you tell the difference?

**Expected Answer:** **Distinguishing arguments from explanations** — Arguments try to convince you that a conclusion is true — the conclusion is in dispute. Explanations show why something already accepted as true occurred — the conclusion is taken for granted. The engineer's statement is an explanation: no one disputes that the bridge collapsed; the engineer explain

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis to determine which statement is an argument and which is an explanation, followed by the reasoning behind the distinction.

### Step 1: Analyze Statement A (The Engineer)
*   **Content:** "The bridge collapsed because the support beams were eaten by termites and the recent flooding weakened the foundation."
*   **Premise:** The bridge collapsed (This is an accepted fact/event).
*   **Conclusion/Goal:** To identify the *cause* of the collapse.
*   **Function:** The speaker is not trying to convince the listener that the bridge *did* collapse; that is already known. Instead, the speaker is providing the reasons *why* the event occurred.
*   **Classification:** This is an **Explanation**.

### Step 2: Analyze Statement B (The I

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Statement A as an explanation and Statement B as an argument. They accurately articulate the core criterion: the distinction lies in whether the conclusion is already accepted as true (explanation) or is in dispute/needs proof (argument). The response demonstrates a 

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The guild master wants you to diagram this argument. Which premises must work together (linked) and which support the conclusion independently (convergent)?

**Expected Answer:** **Linked vs convergent premises and sub-arguments** — In argument diagramming, linked premises are premises that must work together to support a conclusion — neither is sufficient alone. Convergent premises independently support the same conclusion. In this argument, premises 1 and 2 are linked: 'Wanda had her pant leg rolled up' only supports 'she bik

**Model Response:**
> Based on the scenario provided by the Guild Master, here is the step-by-step logical analysis and the final diagram of the argument structure.

### Step-by-Step Analysis

**1. Analyze the Conclusion**
The conclusion (C) is: **"Wanda rode her bike to work today."**

**2. Analyze Premise 1 and Premise 2 (The Linked Relationship)**
*   **Premise 1 (P1):** Wanda arrived with her right pant leg rolled up.
*   **Premise 2 (P2):** Cyclists often roll up their right pant leg to keep it from catching in the chain.
*   **Logical Interaction:**
    *   If we look at **P1 alone**, it tells us nothing about *why* the pant leg is rolled up. It could be a fashion choice, a repair, or a habit. It does not prove she rode a bike.
    *   If we look at **P2 alone**, it states a general rule about cyclists, b

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Premises 1 and 2 as linked and Premise 3 as convergent, providing a clear step-by-step analysis and an accurate visual diagram. The explanation of why the linked premises fail individually is excellent. However, the response does not reach Level 4 because it does not

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Gruff seems very confident in dismissing Mira's proposal. But look at what he actually says — does he address any of the specifics of her plan?

**Expected Answer:** **Name calling / labeling** — Gruff substitutes negative labels for substantive engagement. Rather than challenging the aqueduct's costs, feasibility, or projected benefits, he attaches dismissive terms to Mira and her proposal. The labels carry negative connotations that encourage the audience to reject the proposal based on em

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Trader Gruff's argument:

### Step 1: Analyze the Content of Gruff's Argument
First, we must look at what Gruff actually says versus what he *doesn't* say.
*   **Mira's Proposal:** Included specific data points: cost estimates, projected water flow, and a construction timeline.
*   **Gruff's Response:** He calls the proposal "ivory-tower nonsense," labels Mira a "dreamer" and "idealist," claims she has "never had to make a payroll," and argues that merchants should keep their gold.
*   **The Gap:** Gruff does not mention the cost estimates, does not dispute the projected water flow, and does not critique the construction timeline. He does not offer an alternative calculation or a specific reason why the numbers are wrong.

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism: Gruff attacks Mira's character ('dreamer', 'idealist') rather than engaging with her specific evidence (costs, timeline). Although the student uses the formal term 'Ad Hominem' instead of the rubric's 'Name calling/labeling', the explanation perfe

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The villager says Brother Constant must be right because he has been saying it all week. Is that good reasoning?

**Expected Answer:** **Repetition / illusory truth effect** — Brother Constant repeats the claim 'The Old Bridge is cursed' with rhythmic insistence, without providing evidence. The illusory truth effect is a well-documented cognitive phenomenon: repeated exposure to a statement increases the feeling of familiarity, which people mistake for truth. The villager

**Model Response:**
> No, that is **not good reasoning**. The villager's conclusion that the Old Bridge is cursed simply because Brother Constant has repeated the claim for a week is a classic example of flawed logic.

Here is the step-by-step breakdown of the reasoning pattern and the specific fallacy at play:

### 1. Analysis of the Reasoning Pattern
The villager's thought process follows this structure:
*   **Premise:** Brother Constant has stated "The bridge is cursed" repeatedly for seven consecutive nights.
*   **Observation:** The statement has been heard frequently.
*   **Conclusion:** Therefore, the statement must be true ("Must be something to it").

This reasoning relies entirely on the **frequency** and **repetition** of the claim rather than any empirical evidence, logical proof, or independent ver

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as repetition and explicitly names the 'Illusory Truth Effect' as the underlying cognitive mechanism. They accurately explain the confusion between familiarity (processing fluency) and truth. Furthermore, they contextualize the fallacy within a vacuum of 

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge has been presented with clear evidence of slag dumping. Does his response address that evidence?

**Expected Answer:** **Whataboutism / red herring** — Forge responds to a specific accusation (slag dumping) by redirecting attention to unrelated issues (tannery hides, farm pesticides). The other problems may be real, but they do not address the evidence against Forge. This is a red herring: introducing an irrelevant topic to divert attention from th

**Model Response:**
> ### Step-by-Step Analysis

1.  **Identify the Core Issue:** The village meeting is specifically convened to address a single, documented incident: Forge dumping slag into the river, which has resulted in dead fish and discolored water. The evidence presented (witnesses, water samples, dead fish) directly links this specific act to Forge.

2.  **Analyze Forge's Response:** Instead of addressing the specific evidence regarding his slag dumping (e.g., admitting fault, explaining a mistake, or refuting the specific samples), Forge shifts the focus entirely. He brings up two other parties:
    *   The tannery on the north end (dumping hides).
    *   The farmers (using fey-dust pesticides).

3.  **Evaluate the Relevance:** The actions of the tannery and the farmers, while potentially problemati

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as Whataboutism/Red Herring/Tu Quoque. They clearly explain the mechanism: that the existence of other polluters does not negate the specific evidence against Forge. Crucially, the student addresses the edge case by noting that while other issues may be r

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Steele gave a passionate speech. But did he actually address Councillor Maren's economic analysis?

**Expected Answer:** **Flag-waving / appeal to patriotism** — Steele substitutes an appeal to group identity and patriotic emotion for engagement with the economic argument. He reframes a policy question (will trade lower prices?) as an identity question (are you loyal to Ironvale?). This shuts down cost-benefit analysis by making disagreement feel like betray

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Commander Steele's speech and the logical principles at play.

### Step-by-Step Analysis

1.  **Identify the Core Argument (Councillor Maren):**
    Councillor Maren presented a specific, factual claim based on economic data: Opening trade with Ashford would result in **lower prices** for essential goods (grain and iron). The argument is utilitarian and focuses on material benefit and cost-efficiency.

2.  **Identify Commander Steele's Response:**
    Steele does not offer counter-data, dispute the price projections, or discuss supply chains. Instead, he:
    *   Appeals to **identity and heritage** ("Ironvale hands," "Ironvale soil," "ancestors").
    *   Uses **emotional language** ("forgotten who we are," "betrayal," "

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Steele substitutes an appeal to identity and emotion for economic data, effectively explaining the mechanism of the fallacy. They explicitly state that Steele ignores the price data to focus on patriotism. However, the student mislabels the specific pattern as '

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Krul certainly sounds confident. But did he actually respond to any of Wynn's specific points about enrollment data or graduate outcomes?

**Expected Answer:** **Thought-terminating cliche** — Krul deploys a barrage of stock phrases that sound like wisdom but carry no argumentative content. Each cliche is designed to end inquiry rather than advance it: 'It is what it is' implies nothing can or should change; 'if it ain't broke don't fix it' assumes without argument that nothing is broken;

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Professor Krul's response:

### Step 1: Analyze the Content of the Argument
First, we must compare the substance of Wynn's proposal against Krul's rebuttal.
*   **Wynn's Input:** Provided specific evidence including enrollment data, graduate outcomes, and comparisons to rival academies. These are empirical, factual claims requiring factual counter-evidence to refute.
*   **Krul's Output:** Used phrases like "It is what it is," "The Academy has always taught theory first," "If it ain't broke, don't fix it," and "We have always done it this way."
*   **The Gap:** Krul did not cite a single statistic, address a specific outcome, or offer a counter-argument regarding the efficacy of practical skills. He completely ignored the

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Krul uses stock phrases to shut down inquiry and explicitly notes that these phrases ignore Wynn's specific data, satisfying the core requirements for Level 3. The student accurately explains the mechanism of the argument (using tradition/confidence to mask a la

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** You have the damage report and you have heard both accounts. What is each speaker doing with the facts, and what would an accurate description look like?

**Expected Answer:** **Exaggeration / minimization** — Both speakers distort the significance of the same event in opposite directions. Holt minimizes: 'a few minutes,' 'a couple of lettuce leaves,' 'barely a scratch.' Tess exaggerates: 'destroyed my entire garden,' 'nothing to eat this winter,' 'I will starve.' The actual damage — roughly a third of th

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the speakers' behaviors, the construction of an accurate description, and the underlying logical principles at play.

### Step 1: Analyzing Farmer Holt's Account
**The Fact:** The goats ate about one-third of the lettuce crop and trampled two rows of beans.
**Holt's Statement:** "They nibbled a couple of lettuce leaves... It was nothing — barely a scratch."
**Analysis:**
Holt is engaging in **Minimization** (or Trivialization). He is taking a significant loss (33% of the lettuce and specific rows of beans) and framing it as negligible ("a couple of leaves," "nothing"). By using hyperbolic language to downplay the severity ("barely a scratch"), he attempts to shift the burden of the dispute onto the victim, suggesting that T

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both distortions: Holt's minimization and Tess's exaggeration (catastrophizing). They accurately cite the objective data (one-third loss) as the middle ground, explain how each distortion serves the speaker's self-interest (evading liability vs. maximizing restitutio

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Harl says he is just asking questions and that we need more study. Is he raising legitimate scientific concerns, or is something else going on?

**Expected Answer:** **Doubt casting / manufacturing uncertainty** — Harl's strategy is not to present counter-evidence but to generate a fog of doubt around existing evidence. He questions calibration without alleging specific errors, raises the specter of conflicts of interest without identifying any, invokes 'some scientists' without naming them or citing studies,

**Model Response:**
> Based on the scenario provided, Harl is **not** raising legitimate scientific concerns. Instead, he is employing a rhetorical strategy known as **manufacturing doubt** or **feigned skepticism** to delay action and protect his financial interests.

Here is the step-by-step reasoning regarding the specific reasoning patterns, fallacies, and biases at play:

### 1. The Core Strategy: Manufacturing Doubt
Harl's primary tactic is to shift the burden of proof from the person making the claim (Lyra) to the person questioning it, despite the fact that Lyra has already provided robust evidence.
*   **The Evidence:** Lyra has presented *three* independent analyses, geological survey data, and a mapped contamination pathway. In the scientific method, this constitutes a strong, corroborated case.
*   

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern as 'manufacturing doubt' and 'feigned skepticism,' aligning perfectly with the 'Doubt casting' taxonomy. They explicitly distinguish between legitimate skepticism (specific, testable objections) and Harl's vague, hypothetical doubts, which is the key

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor presents two arguments on stone tablets. Which is valid? Which is sound? Explain your reasoning. If an argument is invalid, provide a counterexample.

**Expected Answer:** **Validity and soundness** — A valid argument is one where the conclusion cannot possibly be false if the premises are true. Soundness = validity + true premises. Tablet A is valid: IF everyone born in France speaks French AND Obama was born in France, THEN he speaks French — the conclusion follows necessarily. But it is unsoun

**Model Response:**
> Based on the scenario provided in the Hall of Logic, here is the step-by-step evaluation of the two arguments, followed by the identification of the logical principles at play.

### Step 1: Analyze Tablet A
**The Argument:**
1.  Everyone born in France can speak French. (Premise 1)
2.  Barack Obama was born in France. (Premise 2)
3.  Therefore, Barack Obama can speak French. (Conclusion)

**Evaluation of Validity:**
An argument is **valid** if the conclusion logically follows from the premises, regardless of whether the premises are actually true.
*   Structure: All $A$ are $B$. $x$ is $A$. Therefore, $x$ is $B$.
*   This is a classic **Modus Ponens** (or Universal Instantiation) structure. If we assume Premise 1 and Premise 2 are true, the conclusion *must* be true. There is no logical wa

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Tablet A as valid but unsound and Tablet B as invalid. They provide the specific counterexample of Gerald Ford to demonstrate the invalidity of Tablet B and clearly explain the distinction between validity (structure) and soundness (truth + structure). The response m

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Translate both sentences into symbolic logic. Then explain: do they mean the same thing? If not, what is the difference?

**Expected Answer:** **Propositional logic connectives and translation** — 'Not both' is the negation of a conjunction: ~(C * I). It is true whenever at least one of the conjuncts is false — Carla could have cake alone, ice cream alone, or neither. 'Neither-nor' is a conjunction of two negations: ~C * ~I. It is true only when both are false — Carla has no cake and no ice c

**Model Response:**
> ### Step 1: Symbolic Translation

First, let's establish the atomic propositions as defined by the logician:
*   $C$: Carla has cake.
*   $I$: Carla has ice cream.

Now, let's translate the two sentences based on standard propositional logic rules.

**Sentence 1: "Carla will not have both cake and ice cream."**
*   **Logical Structure:** This sentence negates the conjunction of the two events. It means it is *not* the case that ($C$ is true AND $I$ is true).
*   **Symbolic Notation:** $\neg (C \land I)$
*   **Meaning:** This allows for three possibilities:
    1.  Carla has cake but no ice cream ($C \land \neg I$).
    2.  Carla has ice cream but no cake ($\neg C \land I$).
    3.  Carla has neither ($\neg C \land \neg I$).
    *The only forbidden scenario is having both.*

**Sentence 2: "

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly translated both sentences into symbolic logic, clearly explained the difference in meaning (allowing one vs. forbidding both), constructed a complete truth table to verify the distinct truth conditions, and explicitly identified the connection to De Morgan's Laws. This response

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build the truth table for this argument. Is the argument valid? How does the truth table show you?

**Expected Answer:** **Truth table test of validity** — The truth table test works by checking every possible assignment of truth values. An argument is valid if and only if there is no row where all premises are true and the conclusion is false. For this disjunctive syllogism (S v D, ~S, therefore D): with four rows of truth values, the only row where b

**Model Response:**
> To determine the validity of the detective's argument, we must first translate the natural language statements into symbolic logic, construct the truth table, and then analyze the rows where the premises are true.

### Step 1: Symbolization

Let's define the atomic propositions based on the instructor's instructions:
*   $S$: The convict escaped through the sewage pipes.
*   $D$: The convict escaped by hiding in the delivery van.

Now, let's break down the detective's argument into premises and a conclusion:
1.  **Premise 1:** "Either the convict escaped through the sewage pipes or the convict escaped by hiding in the delivery van."
    *   Symbolic form: $S \lor D$ (Inclusive OR, though in this context it functions as an exclusive choice, standard logic treats $\lor$ as inclusive unless s

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructs the truth table, accurately identifies the specific row where all premises are true (Row 3), and verifies that the conclusion is also true in that row. They explicitly state the validity test (no row with true premises and false conclusion) and draw the correct concl

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks: what rule of inference justifies each derived step? Name the rule and explain how it applies.

**Expected Answer:** **Modus ponens and hypothetical syllogism** — Step 4 uses modus ponens (MP): from 'if P then Q' and 'P', derive 'Q'. Step 5 also uses MP: from 'if Q then R' and 'Q', derive 'R'. Step 6 uses hypothetical syllogism (HS): from 'if P then Q' and 'if Q then R', derive 'if P then R'. These are three of the eight basic valid forms of inference. Each p

**Model Response:**
> Based on the scenario provided in the Proof Chamber, here is the step-by-step logical analysis of the rules of inference used to derive steps 4, 5, and 6.

### Logical Analysis of the Derivations

The scenario presents a classic chain of logical deductions involving conditional statements (implications). Let's break down the premises and the specific steps taken:

**The Premises:**
1.  $P \to Q$ (If it is raining, then the ground is wet)
2.  $Q \to R$ (If the ground is wet, then the match will not light)
3.  $P$ (It is raining)

Where:
*   $P$ = It is raining
*   $Q$ = The ground is wet
*   $R$ = The match will not light

---

#### Step 4: Deriving "The ground is wet"
*   **Source:** Premises (1) and (3).
*   **Logic:** We have a conditional statement ($P \to Q$) and we are given the antec

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Modus Ponens for steps 4 and 5, and Hypothetical Syllogism for step 6. They also provide clear explanations of the general form and application of each rule, satisfying all criteria for Level 3. However, the response does not address invalid look-alikes (such as affi

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Construct a proof deriving B v D from the three premises. Name each rule you use. Try working both forward from the premises and backward from the conclusion.

**Expected Answer:** **Constructing natural deduction proofs** — The proof uses constructive dilemma: from P v Q, P->R, Q->S, derive R v S. Working backwards: the conclusion B v D is a disjunction, so ask what rules produce disjunctions. Constructive dilemma does, and it requires a disjunction plus two conditionals — exactly what premises 1-3 provide. Working for

**Model Response:**
> ### Part 1: The Formal Proof

Here is the step-by-step derivation of **$B \lor D$** from the premises $(1) A \to B$, $(2) C \to D$, and $(3) A \lor C$.

**Strategy Analysis:**
*   **Backward Reasoning:** The conclusion is a disjunction ($B \lor D$). The most direct rule to introduce a disjunction is **Constructive Dilemma** (if we have $P \lor Q$, $P \to R$, and $Q \to S$, we can derive $R \lor S$). Alternatively, we could use **Disjunction Elimination** (Proof by Cases) on premise 3.
*   **Forward Reasoning:** We have a disjunction in the premises ($A \lor C$) and two conditional statements linking the disjuncts to the desired conclusion parts ($A \to B$ and $C \to D$). This structure perfectly matches the requirements for Constructive Dilemma.

**The Proof:**

| Step | Statement | Justif

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Constructive Dilemma as the optimal rule and provides a valid proof. Crucially, they explicitly detail the backward-forward strategy (Means-Ends Analysis) as required for Level 4. Furthermore, they satisfy the 'alternative proof path' criterion by sketching the Disju

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Test the syllogism using Venn diagrams. Then translate 'Nobody loves me but my mother' into categorical form. What are the categories?

**Expected Answer:** **Categorical statements, translation, and Venn diagrams** — Categorical logic deals with four statement types: All S are P (universal affirmative), No S are P (universal negative), Some S are P (particular affirmative), Some S are not P (particular negative). The syllogism 'All H are M, All M are D, therefore All H are D' is valid: the Venn diagram for the t

**Model Response:**
> ### Step-by-Step Deduction

#### Part 1: Testing the Syllogism with Venn Diagrams

**The Argument:**
1.  All humans are mortal.
2.  All mortal things die.
3.  Therefore, all humans die.

**Logical Form:**
This is a classic categorical syllogism in the form of *Barbara* (AAA-1):
*   Major Premise: All $M$ are $P$ (All Mortal things are things that die).
*   Minor Premise: All $S$ are $M$ (All Humans are Mortal things).
*   Conclusion: All $S$ are $P$ (All Humans are things that die).
*   Where $S$ = Humans, $M$ = Mortal things, $P$ = Things that die.

**Venn Diagram Construction:**
To test this, we draw three overlapping circles representing the three categories: **Humans**, **Mortal Things**, and **Things that Die**.

1.  **Diagramming Premise 1 ("All Humans are Mortal"):**
    *   In Venn

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the categorical logic pattern, accurately constructs and explains the Venn diagram test for the syllogism, and successfully translates the tricky sentence into standard categorical form ('All people who love me are my mother') while identifying the correct categories

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build truth tables for each pair. Which pairs are logically equivalent? Explain what each equivalence (or non-equivalence) means in plain language.

**Expected Answer:** **Logical equivalence: contraposition and De Morgan's Laws** — Pair 1 (A->B and ~AvB) is equivalent: a conditional says the same thing as the negation of the antecedent or the consequent. Pair 2 (~(A*B) and ~Av~B) is equivalent: this is De Morgan's Law — the negation of a conjunction is a disjunction of negations ('not both' equals 'not-A or not-B'). Pair 3 (A-

**Model Response:**
> Here is the step-by-step analysis of the scenario, including the construction of truth tables, the determination of equivalence, and the logical principles at play.

### Part 1: Truth Table Construction and Analysis

To determine if two statements are **materially equivalent**, we must check if their truth values match in every single row of the truth table (i.e., for every possible combination of truth values for the variables $A$ and $B$).

#### Pair 1: $A \to B$ and $\sim A \lor B$
*   **Formula 1:** $A \to B$ (If A, then B)
*   **Formula 2:** $\sim A \lor B$ (Not A or B)

| $A$ | $B$ | $A \to B$ | $\sim A$ | $\sim A \lor B$ | Equivalent? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| T | T | **T** | F | **T** | Yes |
| T | F | **F** | F | **F** | Yes |
| F | T | **T** | T | **T*

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructed truth tables for all three pairs and accurately determined their equivalence status (Pairs 1 and 2 are equivalent; Pair 3 is not). They provided clear plain language explanations for the first two pairs and began explaining the third. However, the response cuts off 

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Which argument is deductive and which is inductive? After learning that Tweets is six feet tall and runs thirty miles per hour, what happens to each argument? Why?

**Expected Answer:** **Deductive vs inductive arguments and defeasibility** — The mathematician's argument is deductive: if the premises are true, the conclusion follows with certainty. Adding new information cannot undermine a valid deductive argument (though it might challenge a premise). The naturalist's argument is inductive: the premises make the conclusion probable, not

**Model Response:**
> Here is the step-by-step analysis of the scenario, the classification of the arguments, and the evaluation of how the new information affects them.

### 1. Classification of the Arguments

First, we must distinguish between the two types of reasoning presented by the mathematician and the naturalist.

*   **The Mathematician's Argument:**
    *   *Premise 1:* Tweets is a healthy, normally functioning bird.
    *   *Premise 2:* **All** healthy, normally functioning birds can fly.
    *   *Conclusion:* Therefore, Tweets can fly.
    *   **Type:** This is a **Deductive** argument.
    *   **Reasoning:** Deductive reasoning aims for certainty. If the premises are true, the conclusion *must* be true. The use of the universal quantifier "All" creates a logical necessity. The structure is a class

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly classifies both arguments as deductive and inductive. They accurately explain defeasibility for the inductive argument, noting how new evidence lowers probability. They also correctly explain that the deductive argument's validity (logical form) remains intact while its soundne

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe asks you to evaluate both polls. Which one should the council trust, and what are the problems with the other one?

**Expected Answer:** **Statistical generalizations: sample size and representativeness** — A good statistical generalization requires two conditions: adequate sample size and a representative sample. Pollster A fails both: 20 people is too few (hasty generalization), and surveying only at the Miners' Guild creates a biased sample that likely overrepresents mining interests. Pollster B use

**Model Response:**
> Based on the scenario provided, here is the step-by-step evaluation of the two polls, the final conclusion, and the logical principles involved.

### Step-by-Step Evaluation

**1. Analyzing Pollster A's Methodology**
*   **Sample Size:** 20 people. This is a very small sample size for a town-wide election. Small samples are highly susceptible to random chance (statistical noise), meaning the results can swing wildly based on just one or two people's opinions.
*   **Sampling Method:** The poll was conducted exclusively at the "Miners' Guild hall." This is a **non-random** sample. It only includes miners or those affiliated with the guild.
*   **The Result:** 75% support for Candidate X.
*   **The Flaw:** This method assumes that the opinions of miners are representative of the entire town (

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both methodological flaws in Pollster A's approach (small sample size and selection bias) and explains why Pollster B's method is superior based on the principles of adequate sample size and representativeness. Furthermore, the student explicitly names and defines th

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Three investigators each offer an explanation. Evaluate each one using the explanatory virtues. Which is the best explanation, and why?

**Expected Answer:** **Inference to the best explanation and explanatory virtues** — IBE selects the hypothesis that best explains the observed evidence according to the explanatory virtues. Lira's explanation (teleportation by rogue mage) is unfalsifiable, inconsistent with background knowledge, and introduces unnecessary entities — it fails on simplicity, testability, and consiste

**Model Response:**
> To determine the best explanation, we must evaluate the three hypotheses proposed by Inspector Lira, Inspector Gareth, and Inspector Nessa against the standard **explanatory virtues** (also known as criteria for inference to the best explanation). These virtues typically include:

1.  **Conservatism (Consistency with background knowledge):** How well does the explanation fit with what we already know to be true?
2.  **Simplicity (Parsimony/Occam's Razor):** Does the explanation require the fewest new assumptions?
3.  **Scope:** Does the explanation account for all the observed facts?
4.  **Fruitfulness:** Does the explanation generate testable predictions or lead to further discoveries?
5.  **Testability:** Can the explanation be proven false or verified through evidence?

### Step-by-Step

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the IBE pattern and evaluates all three hypotheses against multiple explanatory virtues (Conservatism, Simplicity, Scope, Testability). They correctly rank Lira as the worst and Gareth as the best, providing strong reasoning for each. However, the response does not f

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher draws an analogy between the drowning child and the daily coffee purchase. Is it a good analogy? Evaluate the relevant similarities and the disanalogies Aldric raises. Which disanalogies, if any, are relevant to the moral conclusion?

**Expected Answer:** **Argument by analogy: relevant similarities and disanalogies** — An argument by analogy infers that because two things share relevant similarities, what is true of one is probably true of the other. The philosopher argues: (1) The pond case and the coffee case share a relevant similarity — choosing a luxury over a child's survival. (2) In the pond case, saving th

**Model Response:**
> This scenario presents a classic ethical debate rooted in **Peter Singer's "Drowning Child" argument**, a cornerstone of modern effective altruism. To evaluate whether the analogy is "good," we must dissect the logical structure of the comparison, weigh the similarities against the disanalogies raised by Aldric, and determine if those disanalogies actually undermine the moral conclusion.

### 1. Analysis of the Analogy's Structure

The philosopher is employing an **argument by analogy**. The structure is as follows:
*   **Source Case (The Pond):** A child is drowning nearby; saving them costs only a minor luxury (boots); the moral imperative is clear (save the child).
*   **Target Case (The Famine):** A child is dying from famine far away; saving them costs a minor luxury (coffee); the mor

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the argument by analogy and explicitly names the core similarity (trivial cost vs. life saved). They thoroughly evaluate both disanalogies raised by Aldric (proximity and efficacy), arguing that proximity is morally irrelevant while the efficacy concern is weak due t

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Using the vet's log, apply the necessary condition test and the sufficient condition test to each factor. Which factor is the likely cause of Whiskers' seizures?

**Expected Answer:** **Mill's methods: necessary and sufficient condition tests** — The necessary condition test: which factor is present in every seizure case? F is present in all three seizure days. T is present in days 1 and 3 but not day 2. V is present in days 1 and 2 but not day 3. Only F passes the necessary condition test. The sufficient condition test: which factor is abse

**Model Response:**
> Based on the scenario provided, here is the step-by-step logical deduction using Mill's Methods to identify the cause of Whiskers' seizures.

### Step 1: Organize the Data
First, let's break down the vet's log into a clear table of conditions (Factors) and outcomes.
*   **Factors:**
    *   **F**: New Food
    *   **T**: Thunderstorm
    *   **V**: Visitor Present
*   **Outcome:** Seizure (Yes/No)

| Day | Outcome | New Food (F) | Thunderstorm (T) | Visitor (V) |
| :--- | :--- | :---: | :---: | :---: |
| **Seizure 1** | **Yes** | Yes | Yes | Yes |
| **Seizure 2** | **Yes** | Yes | No | Yes |
| **Seizure 3** | **Yes** | Yes | Yes | No |
| **No-Seizure 1** | **No** | No | Yes | Yes |
| **No-Seizure 2** | **No** | No | No | No |

---

### Step 2: Apply the Necessary Condition Test
**Definitio

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identified the causal factor (F) by systematically applying both the necessary and sufficient condition tests to all factors. They accurately ruled out T and V using specific counter-examples from the data. The response did not reach Level 4 because it lacked a discussion on th

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Councillor Drava claims the tonic causes higher yields based on the correlation data. What is wrong with this inference? Identify the alternative explanations.

**Expected Answer:** **Correlation vs causation: third variable and reverse causation** — When two things are positively correlated, there are four logical possibilities: (1) A causes B, (2) B causes A, (3) a third variable C causes both, (4) the correlation is coincidental. Drava assumes possibility 1 (tonic causes higher yields). The physician raises possibility 3 (wealth is the confou

**Model Response:**
> Based on the scenario provided, here is the step-by-step logical evaluation of Councillor Drava's inference.

### Step 1: Analyze the Core Inference
Councillor Drava observes a statistical **correlation**:
*   **Variable A:** Workers drink Vigor Tonic.
*   **Variable B:** Farms have 20% higher crop yields.
*   **Conclusion:** Variable A *causes* Variable B (The tonic makes workers more productive).

The logical flaw here is the immediate assumption that because two events occur together, one must be the direct cause of the other. This ignores the possibility that a third factor influences both, or that the direction of causality is reversed.

### Step 2: Identify the Logical Fallacy
The specific reasoning pattern being demonstrated is the **Correlation Does Not Imply Causation** fallacy (o

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Correlation Does Not Imply Causation' fallacy. They explicitly detail both alternative explanations required for Level 3: the confounding variable (wealth) and reverse causality. Furthermore, they exceed Level 3 by explaining that observational data is insuffici

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Solve the three probability problems. Show your work and explain which probability law you use for each one.

**Expected Answer:** **Basic probability laws: complement, addition, conjunction** — Problem 1 (complement): P(not-4) = 1 - P(4) = 1 - 1/6 = 5/6. Problem 2 (addition with correction): P(at least one H) = P(H on coin 1) + P(H on coin 2) - P(H on both) = 1/2 + 1/2 - 1/4 = 3/4. Alternatively, use complement: 1 - P(no heads) = 1 - 1/4 = 3/4. Problem 3 (at least one via complement): P(at

**Model Response:**
> Here are the solutions to the three probability problems presented by the dice master, followed by an analysis of the underlying reasoning patterns and principles.

### Part 1: Solving the Problems

#### Problem 1: Probability of NOT rolling a 4
**Scenario:** Rolling a fair six-sided die.
**Goal:** Find $P(\text{not } 4)$.

*   **Reasoning:**
    A standard die has 6 equally likely outcomes: $\{1, 2, 3, 4, 5, 6\}$.
    The event "rolling a 4" has 1 favorable outcome.
    The event "not rolling a 4" includes outcomes $\{1, 2, 3, 5, 6\}$, which is 5 outcomes.
*   **Calculation:**
    $$P(\text{not } 4) = \frac{\text{Number of non-4 outcomes}}{\text{Total outcomes}} = \frac{5}{6}$$
    Alternatively, using the **Complement Rule**:
    $$P(\text{not } 4) = 1 - P(4) = 1 - \frac{1}{6} = \frac{5}

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly solved all three problems using appropriate methods (complement rule and independence). Crucially, they explicitly identified why naive addition fails (double-counting in Problem 2 and the impossibility of >1 probability in Problem 3), demonstrated the complement method clearly

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The magistrate asks: given Bob's 99% accuracy and 1000 people in the area with 5 actual robbers, what is the probability that Nancy is truly the robber? Show your reasoning.

**Expected Answer:** **Conditional probability, Bayes' theorem, and base rate reasoning** — The naive answer is 99%, but this ignores the base rate. Using Bayes' theorem: Of 1000 people, 5 are robbers. Bob correctly identifies 99% of 5 robbers = 4.95 true positives. Bob incorrectly identifies 1% of 995 innocent people = 9.95 false positives. Total positive identifications = 4.95 + 9.95 = 1

**Model Response:**
> To solve this problem, we must apply **Bayes' Theorem**, which allows us to update the probability of a hypothesis (Nancy is the robber) based on new evidence (Bob's identification), while accounting for the prior probability (the base rate of robbers in the population).

### Step-by-Step Deduction

**1. Define the Parameters**
*   **Total Population ($N$):** 1,000 people.
*   **Actual Robbers ($R$):** 5 people.
*   **Innocent People ($I$):** 995 people.
*   **Test Accuracy (Sensitivity):** 99% (Probability Bob identifies a robber correctly).
*   **Test Specificity:** 99% (Probability Bob clears an innocent person correctly).
    *   This implies a **False Positive Rate** of 1% (Probability Bob incorrectly identifies an innocent person as a robber).

**2. Calculate the Number of Positive I

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the problem as an application of Bayes' Theorem, accurately calculates the true positives (4.95) and false positives (9.95), and derives the correct final probability of approximately 33.2%. They clearly explain the Base Rate Fallacy and why the intuitive 99% answer 

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The patient believes she has a 95% chance of having colon blight. Is she right? Use the base rate and test accuracy to compute the actual probability. Show your work.

**Expected Answer:** **Base rate reasoning in medical screening** — For a population of 100,000: 500 have colon blight (0.5% base rate). Of those 500, the test correctly identifies 95% = 475 true positives. Of the 99,500 without the disease, the test incorrectly flags 5% = 4,975 false positives. Total positive results = 475 + 4,975 = 5,450. P(disease | positive test

**Model Response:**
> ### Step-by-Step Calculation

To determine the true probability that the patient has colon blight given a positive test result, we must use **Bayes' Theorem**. The patient's intuition (that the probability is 95%) ignores the rarity of the disease, which is the critical factor here.

Let's define the variables based on the scenario:
*   **$P(D)$**: The probability of having the disease (Base Rate) = $0.5\% = 0.005$.
*   **$P(\neg D)$**: The probability of *not* having the disease = $1 - 0.005 = 0.995$.
*   **$P(T^+|D)$**: The probability of testing positive given the disease (Sensitivity) = $95\% = 0.95$.
*   **$P(T^+|\neg D)$**: The probability of testing positive given *no* disease (False Positive Rate) = $1 - \text{Specificity} = 1 - 0.95 = 0.05$.

We want to find **$P(D|T^+)$**: The pr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the base rate reasoning pattern and performs an accurate calculation using both Bayes' Theorem and natural frequencies, arriving at the correct 8.7% result. They clearly explain why the patient's intuition is wrong due to the rarity of the disease and explicitly name

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sergeant Dallow seems confident in his logic. Look at the sign, then look at his reasoning. Does his conclusion actually follow?

**Expected Answer:** **Denying the antecedent** — Dallow reasons from 'If royal writ, then entry' and 'no royal writ' to 'no entry.' He treats the antecedent as necessary when the sign only establishes it as sufficient.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Sergeant Dallow's logic:

### Step 1: Formalize the Logic
Let's break down the statement on the sign and Dallow's reasoning into logical propositions:
*   **Proposition $P$:** You carry a royal writ.
*   **Proposition $Q$:** You may pass.

The sign states: **"If you carry a royal writ, you may pass."**
In formal logic, this is a conditional statement: **If $P$, then $Q$** ($P \rightarrow Q$).

Dallow's observation: **"You don't have a royal writ."**
This is the negation of the antecedent: **Not $P$** ($\neg P$).

Dallow's conclusion: **"Therefore you may not pass."**
This is the negation of the consequent: **Not $Q$** ($\neg Q$).

### Step 2: Analyze the Logical Structure
Dallow's argument follows this structure:
1.  If $

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'Denying the Antecedent,' explicitly explains the confusion between sufficient and necessary conditions, and provides a clear analogy. While they do not explicitly use the term 'biconditional,' their explanation that the rule would need to state 'only 

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Wynn seems sure it was a wolf. Does the conclusion follow from what she observed?

**Expected Answer:** **Affirming the consequent** — Wynn reasons from 'If wolf then large paw prints' and 'large paw prints' to 'wolf.' She treats the consequent as proof of the antecedent.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Wynn's reasoning:

### Step 1: Deconstruct the Argument
Let's break down Wynn's logic into a formal structure:
1.  **Premise 1 (Conditional Statement):** If a wolf attacked the sheep, then we would find large paw prints near the pen.
    *   *Logical Form:* If $P$, then $Q$. ($P$ = Wolf attack, $Q$ = Large paw prints).
2.  **Premise 2 (Observation):** We found large paw prints near the pen.
    *   *Logical Form:* $Q$ is true.
3.  **Conclusion:** Therefore, it was a wolf.
    *   *Logical Form:* Therefore, $P$ is true.

### Step 2: Analyze the Logical Validity
In formal logic, the structure used above is:
*   If $P \rightarrow Q$
*   $Q$
*   $\therefore P$

This is a classic **logical fallacy** known as **Affirming the Co

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy 'Affirming the Consequent,' correctly deconstructs the logical form (If P then Q; Q; therefore P), explains why the direction of the conditional matters (confusing necessary vs. sufficient conditions), and identifies alternative causes (bears, dogs) as additi

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Varn seems very worried about this bakery permit. He has given you a chain of consequences. Do you find his reasoning convincing? Why or why not?

**Expected Answer:** **Causal slippery slope** — Varn chains together a sequence of causal claims — competition leads to price drops leads to corner-cutting leads to illness leads to overwhelmed healers leads to plague — treating each link as inevitable. Even if each individual step had a 90% probability, the probability of the entire six-step cha

**Model Response:**
> No, Councillor Varn's reasoning is **not convincing**. While his concern for public health is understandable, the logical structure of his argument is fundamentally flawed.

Here is the step-by-step breakdown of the reasoning pattern and fallacies at play:

### 1. Identification of the Reasoning Pattern
Varn is employing a **Slippery Slope** argument. This is a logical fallacy where a person asserts that a relatively small first step (allowing a second bakery) will inevitably lead to a chain of related events culminating in a significant (and usually negative) effect (a town-wide plague), without providing sufficient evidence that each step in the chain is probable or inevitable.

### 2. Analysis of the Logical Gaps
Let's examine the chain of consequences Varn proposes and where the logic 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Slippery Slope' pattern and provides an excellent step-by-step critique of the logical gaps and alternative outcomes (counterpoints). However, the response does not explicitly explain the probabilistic mechanism required for Level 4 (i.e., that multiplying uncer

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Pip seems very confident in his proof. Is his reasoning valid? Can you spot the mistake?

**Expected Answer:** **Composition fallacy** — Pip infers that a property true of each individual part (each atom is invisible) must be true of the whole composed of those parts (Pip is invisible). But visibility is not a property that transfers from parts to whole in this way — the arrangement and quantity of atoms creates emergent properties l

**Model Response:**
> Pip's reasoning is **invalid**, and the mistake he has made is a classic logical error known as the **Fallacy of Composition**.

Here is the step-by-step breakdown of why his argument fails:

### 1. Analysis of the Argument Structure
Pip's argument follows this syllogistic structure:
*   **Premise 1:** Every individual atom in my body is invisible to the naked eye.
*   **Premise 2:** I am made entirely of atoms.
*   **Conclusion:** Therefore, I (the collection of atoms) am invisible to the naked eye.

### 2. Identifying the Logical Flaw
The **Fallacy of Composition** occurs when one assumes that what is true for the parts of a whole must also be true for the whole itself. While this assumption works in some mathematical or physical contexts (e.g., "Every brick is light, so the wall made of

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'Fallacy of Composition' and correctly explains that visibility is an emergent property resulting from the arrangement of atoms, not a trait transferred from parts to whole. Furthermore, the response satisfies the Level 4 requirement by providing examples of whe

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorin is trying to figure out how much individual parts of the house are worth based on the total value. Does his reasoning work?

**Expected Answer:** **Division fallacy** — Dorin infers that because the whole house has a certain property (being worth 900 gold), each part of the house must share that property proportionally. But the house's value comes from the arrangement and integration of its parts, not from the parts individually. Disassembled lumber and stones are 

**Model Response:**
> Dorin's reasoning **does not work**. While his intuition that the parts should add up to the whole is mathematically sound in a simple sum, his specific method of calculating the value of individual components by dividing the total price by the total number of components is fundamentally flawed.

Here is the step-by-step breakdown of the reasoning pattern and the specific fallacy at play:

### 1. The Flaw in the Calculation
Dorin attempts to derive the value of a specific part (an oak beam) by taking the total value of the house (900 gold) and dividing it by an estimated count of all components (900 components).
*   **His Logic:** $\text{Value of Beam} = \frac{\text{Total House Value}}{\text{Total Number of Parts}}$
*   **The Reality:** A house is not a homogeneous object made of 900 ident

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Fallacy of Division,' correctly explains that the property of the whole (average value) cannot be applied to heterogeneous parts, and details the concept of emergent value (synergy, labor). Furthermore, the student provides a clear counter-example (the car engine vs

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Brother Vassyl seems very confident. What do you think about the reasoning he just gave you for trusting the Codex?

**Expected Answer:** **Begging the question (circular reasoning)** — The conclusion — that the Codex is the ultimate authority — is assumed as a premise when the speaker cites the Codex's own claim of infallibility as evidence. The premise and conclusion are nearly identical.

**Model Response:**
> Brother Vassyl's reasoning is a classic example of **circular reasoning**, specifically known in logic as **begging the question** (*petitio principii*).

Here is the step-by-step breakdown of why this reasoning fails:

1.  **The Claim:** Vassyl asserts that the *Codex of Arundel* is the ultimate authority on truth and is infallible.
2.  **The Evidence:** To prove this claim, he cites a specific passage *from within the Codex itself* (Chapter One), which states that the Codex is the unassailable truth authored by an infallible hand.
3.  **The Flaw:** The argument assumes the truth of the conclusion (the Codex is perfect) in order to prove the premise (the Codex says it is perfect).
    *   If the Codex is not actually infallible, then Chapter One is a lie or an error, and it cannot be used

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly names the fallacy ('begging the question' and 'circular reasoning'), clearly explains the mechanism (using the source to validate itself without independent support), and explicitly notes that the argument fails because it offers no independent verification, satisfying all crit

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Harsk says you must either march north or starve. What is wrong with how he has framed the choice?

**Expected Answer:** **False dichotomy (black-or-white thinking)** — A disjunction is presented as exhaustive when it is not. Harsk forces a choice between two options while ignoring alternatives like fortifying defenses, sending scouts, hiring mercenaries, or appealing to a neighboring lord.

**Model Response:**
> Commander Harsk is demonstrating a **False Dilemma** (also known as a False Dichotomy or Black-and-White Thinking).

Here is the step-by-step reasoning behind this conclusion:

1.  **Analysis of the Options Presented**: Harsk explicitly states, "Those are your choices," and presents only two mutually exclusive outcomes:
    *   Option A: March north and crush the bandits.
    *   Option B: Sit here, let the bandits bleed the town dry, and eventually starve.

2.  **Identification of Missing Alternatives**: In a complex military and logistical scenario like defending a town, it is highly improbable that only two extreme options exist. Harsk ignores several reasonable middle grounds, such as:
    *   Sending a smaller, specialized detachment north while leaving the main force to guard the sou

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as a False Dilemma/Dichotomy. They explicitly explain that the disjunction is not exhaustive by listing multiple concrete alternatives (detachment, negotiation, fortification, evacuation). Furthermore, they analyze the mechanism of the flaw (artificially 

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Silvertongue claims this argument is logically airtight. Is it? Where does the reasoning go wrong?

**Expected Answer:** **Equivocation** — The argument uses the word 'nobody' in two different senses. In 'Nobody is perfect,' 'nobody' means 'no person' (a universal negative quantifier). In 'Bert is a nobody,' 'nobody' means 'an unimportant or insignificant person.' The argument treats these as the same meaning, creating an illusion of va

**Model Response:**
> No, Silvertongue's argument is **not** logically airtight. While the conclusion ("Bert is perfect") might sound amusingly paradoxical, the reasoning contains a classic logical error known as the **Fallacy of Equivocation**.

Here is the step-by-step breakdown of where the reasoning goes wrong:

### 1. Analyzing the Premises
To understand the flaw, we must look at how the word "nobody" is used in each part of the argument:

*   **Premise 1:** "Nobody is perfect."
    *   In this context, "nobody" functions as a **universal quantifier**. It means "No person" or "There does not exist any person who is perfect."
    *   *Logical form:* $\forall x (\text{Person}(x) \rightarrow \neg \text{Perfect}(x))$

*   **Premise 2:** "Bert is a nobody."
    *   In this context, "nobody" functions as a **nou

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Fallacy of Equivocation and precisely explains the two distinct meanings of 'nobody' (universal quantifier vs. noun for an insignificant person), satisfying all criteria for Level 3. However, the response does not meet the Level 4 requirement of providing an addi

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Scholar Tilde claims there is no real difference between a novice and an archmage because you cannot draw a sharp line between the ranks. Is she right?

**Expected Answer:** **Conceptual slippery slope** — Tilde exploits the vagueness of category boundaries. Because there is no sharp line between novice and apprentice, or apprentice and journeyman, she concludes there is no real difference between the extremes. This is the sorites paradox applied to conceptual categories: if removing one grain of sand

**Model Response:**
> Scholar Tilde is **not right**. Her argument is a classic example of a logical fallacy known as the **Sorites Paradox** (also called the **Fallacy of the Heap** or the **Fallacy of Continuity**).

Here is the step-by-step reasoning behind why her conclusion is flawed:

### 1. Identification of the Reasoning Pattern
Tilde's argument follows this structure:
1.  **Premise 1:** There is no single, sharp boundary where a novice becomes an apprentice (or any other rank), because the difference between any two adjacent students is infinitesimally small.
2.  **Premise 2:** If there is no sharp boundary between adjacent steps, then there is no meaningful distinction between the start and the end of the sequence.
3.  **Conclusion:** Therefore, a novice and an archmage are effectively the same.

This

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the reasoning pattern as the Sorites Paradox (conceptual slippery slope), explicitly names the fallacy, and explains the mechanism: confusing the vagueness of boundaries with the non-existence of differences at the extremes. Furthermore, the student provides the clas

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Grus seems pretty passionate about this. But take a step back: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely?

**Expected Answer:** **Abusive ad hominem** — Grus attacks Maren's personal background (newcomer status, lack of farmland, occupation) instead of engaging with the substance of her irrigation proposal: the river data, crop projections, costs, and affected families. He treats her identity as grounds for dismissing the argument.

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of Alderman Grus's argument:

### 1. Analysis of the Request and Reasons
**What is he asking the council to do?**
Grus is asking the council to **dismiss Maren's irrigation proposal outright** without evaluating its merits.

**What reasons does he give?**
Grus provides three specific points to support his dismissal:
1.  Maren moved to the town only five years ago (she is a newcomer).
2.  She does not own farmland.
3.  She is a shopkeeper, implying she lacks specific knowledge about water and soil.

### 2. Evaluation of the Reasons
**Are these reasons about the proposal?**
**No.** Grus does not address a single element of Maren's detailed presentation. He ignores:
*   The river flow data.
*   The crop yield projections.
*   The

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Ad Hominem pattern, explicitly explains that Maren's personal attributes are irrelevant to the validity of her data-driven argument, and articulates the crucial distinction that the proposer's background would only matter if the argument relied on personal testim

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The merchant demands you prove his amulet doesn't work. What is wrong with this?

**Expected Answer:** **Burden of proof** — Shifting the burden of proof from the person making the claim to the person questioning it.

**Model Response:**
> The merchant's argument demonstrates a classic logical error known as the **Burden of Proof Fallacy** (specifically, shifting the burden of proof), often accompanied by an **Appeal to Ignorance** (*argumentum ad ignorantiam*).

Here is the step-by-step breakdown of the reasoning pattern and why it is flawed:

### 1. Analysis of the Argument Structure
*   **The Claim:** The merchant asserts that an invisible amulet is actively protecting the customer ("It is working").
*   **The Challenge:** When the customer claims it doesn't work, the merchant demands the customer prove that the amulet *isn't* working.
*   **The Conclusion:** Because the customer cannot prove the absence of the invisible barrier, the merchant concludes the barrier must exist.

### 2. Identification of the Fallacy: Shiftin

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Burden of Proof Fallacy' and 'Appeal to Ignorance,' correctly explains that the claimant must support their own claim, and elaborates on why unfalsifiability constitutes a logical flaw. The response fully satisfies all criteria for Level 4, including the connection 

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Ranger Harlen rejects the fossil evidence because he can't imagine fish becoming people. What error is he making?

**Expected Answer:** **Personal incredulity** — Dismissing a claim because one personally cannot understand or imagine how it could be true.

**Model Response:**
> Based on the scenario provided, Ranger Harlen is demonstrating a specific cognitive error rooted in the limitations of his personal experience.

Here is the step-by-step analysis of his reasoning:

1.  **The Premise:** Harlen states, "I've been a ranger forty years and I've never seen a fish sprout legs."
2.  **The Observation:** He observes that the fossil evidence (fish bones turning into people) contradicts his direct, daily observations of nature.
3.  **The Conclusion:** He dismisses the scientific evidence entirely, calling the idea "ridiculous" solely because it conflicts with what he has witnessed in his lifetime.
4.  **The Flaw:** Harlen is assuming that because something has not happened within the scope of his personal observation (40 years), it is impossible or false. He is fail

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Argument from Personal Incredulity,' clearly distinguishes between personal inability to visualize a process and actual evidential refutation, and correctly notes the critical context of vast timescales versus limited human observation. This meets all criteria for t

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Every time Seer Vashti's powers fail a test, she adds a new excuse. What reasoning error is this?

**Expected Answer:** **Special pleading / No true Scotsman** — When a claim is shown to be false, moving the goalposts by introducing ad hoc exceptions so the claim can never be falsified.

**Model Response:**
> Based on the scenario provided, the reasoning error demonstrated by Seer Vashti is the **No True Scotsman** fallacy (also known as the fallacy of moving the goalposts or immunizing a hypothesis from falsification).

Here is the step-by-step breakdown of why this fits:

1.  **The Initial Claim:** Vashti makes a universal claim: "My visions are real" and "I've helped hundreds." Implicitly, this suggests her power is reliable and functional.
2.  **The Test:** A skeptical mage proposes a controlled test to verify this claim. This is a standard method for falsifying a hypothesis.
3.  **The Failure:** The test fails; the vision does not occur.
4.  **The Ad Hoc Rescue:** Instead of accepting that the power might not exist or that the claim was false, Vashti introduces a new, specific condition to

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the underlying pattern as 'special pleading' and explicitly explains the mechanism of making the claim unfalsifiable by moving the goalposts. Although the student leads with the label 'No True Scotsman,' they accurately describe it as a form of special pleading and p

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Greaves demands a yes-or-no answer. What is the problem with this question?

**Expected Answer:** **Loaded question** — A question containing a built-in assumption so that any direct answer appears to confirm it.

**Model Response:**
> The problem with Alderman Greaves' question is that it constitutes a **False Dilemma** (also known as a **False Dichotomy** or the **Complex Question Fallacy**).

Here is the step-by-step reasoning behind this classification:

1.  **Presumption of Guilt**: The question "Have you stopped using contaminated herbs...?" is not a neutral inquiry. It contains a hidden, unproven premise: that the healer *was* using contaminated herbs in the past. By demanding a "yes" or "no," the Alderman forces the Healer to implicitly accept this premise regardless of which answer she chooses.
    *   If she answers **"Yes,"** she admits to previously using contaminated herbs.
    *   If she answers **"No,"** she admits to *still* using contaminated herbs.
    *   If she answers **"I never used them,"** she is 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as a 'Complex Question' (synonymous with Loaded Question) and explicitly details the embedded presupposition of guilt. They thoroughly explain the mechanism by analyzing the 'yes/no' trap and the exclusion of valid alternatives. Furthermore, they suggest 

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The alchemist tested in thirty villages but only shows five. What reasoning error is he committing?

**Expected Answer:** **Texas sharpshooter** — Cherry-picking data clusters that suit a conclusion while ignoring data that does not. Like painting a target around bullet holes after shooting.

**Model Response:**
> The alchemist is committing the reasoning error known as **Cherry Picking** (also referred to as **Suppressed Evidence** or the **Fallacy of Incomplete Evidence**).

Here is the step-by-step breakdown of why this is the case:

1.  **The Full Dataset**: The alchemist acknowledges that he surveyed a total of **30 villages**. This represents the complete sample size of his "research."
2.  **The Selective Presentation**: He chooses to highlight only the **5 villages** where the pox rate dropped. These are the results that support his hypothesis (that the tonic works).
3.  **The Omitted Data**: He completely ignores the remaining **25 villages**. In a valid scientific argument, the results from these 25 villages are crucial. If the pox rate remained the same or increased in those 25 villages, i

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the fallacy as 'Cherry Picking' and provides a clear explanation of the mechanism: selecting a favorable subset (5 villages) while ignoring the contradictory majority (25 villages). This meets the criteria for Level 3. However, the response does not reach Level 4 bec

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The mediator proposes combining evidence-based treatment with unsupported one. What is wrong with this?

**Expected Answer:** **Middle ground (false compromise)** — Assuming the truth must lie between two positions simply because they are opposing, regardless of evidence.

**Model Response:**
> The reasoning pattern demonstrated by the mediator is the **Fallacy of the Golden Mean** (also known as the **Argument to Moderation** or **False Equivalence**).

Here is the step-by-step breakdown of why this reasoning is flawed:

### 1. Identification of the Fallacy
The Fallacy of the Golden Mean occurs when someone assumes that the truth or the best solution must always lie exactly halfway between two opposing viewpoints. The mediator explicitly states, "Clearly the truth lies in the middle," and concludes that "Compromise is always wisest." This assumes that because two extremes exist, the middle ground is automatically valid or superior.

### 2. Analysis of the Premises
To see why this fails in this specific scenario, we must look at the nature of the two opposing claims:
*   **Dr. As

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (Golden Mean/Argument to Moderation), clearly distinguishes between negotiation compromise (interests) and epistemic truth (facts), and explains how this reasoning erroneously validates harmful extreme positions (bloodletting) by averaging them with valid one

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dag dismisses mine dust danger because his grandfather survived it. What reasoning error?

**Expected Answer:** **Anecdotal evidence** — Using personal experience or an isolated example in place of statistical evidence, especially to dismiss systematic data.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning error:

### Step 1: Analyze the Argument Structure
*   **Premise:** Dag's grandfather worked in the mine for 60 years, breathed the dust daily, and lived to be 97 without getting lung sickness.
*   **Conclusion:** Therefore, mine dust does not cause lung sickness (or is not dangerous).
*   **Underlying Logic:** Because one specific individual survived a hazardous condition, the condition itself cannot be harmful to the general population.

### Step 2: Identify the Logical Flaw
The core error lies in the **sample size**. Dag is taking a single data point (his grandfather) and using it to make a universal claim about the safety of the mine dust for everyone.

In statistics and logic, a sample size of one is in

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the Anecdotal Fallacy/Hasty Generalization. They explicitly explain why a single case cannot outweigh systematic data (sample size issues, outliers). Furthermore, they successfully address the specific Level 4 criteria by discussing Survivorship Bias a

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What is wrong with Alderman Grask's response to Sable's proposal?

**Expected Answer:** **Straw man** — Grask inflates Sable's modest proposal (a south-bank levee) into an extreme position (damming the entire river) and then attacks the extreme version. His criticism C targets fabricated position B, not Sable's actual position A.

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of Alderman Grask's response:

### Step 1: Analyze Sable's Original Proposal
Sable's argument is specific and limited in scope. She proposes building a **"modest levee along the south bank"** to protect specific fields that flood every spring. Her goal is to prevent the loss of a "quarter of our barley." The proposal does not mention damming the river, stopping the flow of water, or affecting farms downstream.

### Step 2: Analyze Grask's Response
Grask does not address the specific details of Sable's proposal (a modest levee on one bank). Instead, he characterizes her plan as an attempt to **"dam the entire river"** and **"cut off water to every farm downstream."** He then lists catastrophic consequences (livestock dying, mil

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Straw Man Fallacy,' clearly distinguishes between Sable's actual proposal (modest levee) and Grask's distorted version (damming the river), explains why the criticism is irrelevant to the real argument, and provides additional insight into the potential motivation (

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Garrett fires back at Inspector Maren by bringing up the oil-lantern incident. What is wrong with his reasoning? Why doesn't Maren's past mistake let Garrett off the hook?

**Expected Answer:** **Tu quoque (appeal to hypocrisy)** — Dismissing a criticism by pointing out that the person making it is guilty of the same or similar fault. Treats the critic's inconsistency as though it refutes the content of the criticism.

**Model Response:**
> Garrett's reasoning demonstrates a classic logical fallacy known as **Tu Quoque** (Latin for "you also"), which is a specific type of **Ad Hominem** attack.

Here is the step-by-step breakdown of why his argument fails:

1.  **The Core Issue**: The safety inspector, Maren, has identified a specific, objective violation: Garrett is storing volatile coal dust too close to residential homes, creating a fire hazard. This is a factual claim about current safety standards.
2.  **Garrett's Response**: Instead of addressing the coal dust issue, Garrett attacks Maren's character and credibility by pointing out a past mistake she made (leaving oil lanterns unattended).
3.  **The Logical Flaw**: Garrett assumes that because Maren was once negligent, her current accusation is invalid. However, the tru

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Tu Quoque fallacy and explains that the critic's past behavior is irrelevant to the truth of the current claim (Level 3 criteria). Furthermore, the response explicitly discusses the 'principle of relevance' and implies what a legitimate response would entail (add

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorric clearly does not like this formula. But does he point out any problem with the measurements, the chemical rationale, or the engineering requirements? What is his objection really about?

**Expected Answer:** **Genetic fallacy** — Dorric judges the formula by attacking its origin — Vielle's impoverished background — rather than engaging with its content. The chemical rationale and measurements go entirely unaddressed.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Dorric's argument:

### Step 1: Analyze the Content of the Objection
First, we must look at exactly what Dorric says regarding the formula itself.
*   **The Formula:** He refers to it as a "formula from Vielle" and a "workhouse recipe."
*   **The Data:** He explicitly states, "I don't care what the numbers say." This indicates he is dismissing the empirical measurements and data presented on the chalkboard.
*   **The Science/Engineering:** He makes no mention of chemical reactions, thermal dynamics, structural integrity, or specific engineering flaws. He does not point out a calculation error or a material incompatibility.

### Step 2: Identify the Focus of the Attack
Instead of addressing the *idea* (the glass formula), 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Genetic Fallacy and explains the mechanism clearly: Dorric judges the formula based on Vielle's impoverished origins rather than the empirical data or chemical rationale. The response explicitly notes that technical merits were ignored ('I don't care what the num

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Holt raises serious worries. But is he giving you any reason to doubt Tova's research itself?

**Expected Answer:** **Appeal to consequences** — Arguing that a factual claim should be rejected because accepting it would lead to undesirable outcomes, substituting the consequences for a critique of the evidence.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Guildmaster Holt's argument:

### Step 1: Analyze the Structure of Holt's Argument
Holt's argument follows this logical flow:
1.  **Premise:** If Tova's findings are accepted (that the herbal supplement has no effect), the redthorn harvesters will lose their livelihoods.
2.  **Premise:** This loss of livelihood will cause three villages to suffer, leading to hunger and a lack of schooling for children.
3.  **Conclusion (Implied):** Therefore, we should not accept Tova's findings (or at least, we should doubt them).

### Step 2: Evaluate the Connection to the Truth of the Claim
The core question is whether the *consequences* of a belief affect the *truth* of that belief.
*   **Tova's Claim:** The supplement has no measurab

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Appeal to Consequences' fallacy, correctly identifies that Holt rejects the finding based on negative outcomes rather than evidence, and clearly distinguishes between the truth value of the scientific claim and the moral/economic desirability of its consequences. Th

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Corvin has a strong expert backing his claim. But what exactly is Eldric an expert in, and what is the question being debated?

**Expected Answer:** **Appeal to authority** — Corvin appeals to Eldric's authority as a surgeon to settle a question about marine toxicology — a field in which Eldric has no special expertise.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning pattern and the specific logical flaw at play.

### Step 1: Identify the Expert's Actual Field
First, we must look at the credentials Master Eldric holds. The text explicitly states that Eldric is a **"famous surgeon"** and the **"most celebrated healer."**
*   **Domain of Expertise:** Human medicine, surgery, and human health.
*   **Relevance:** His expertise is strictly limited to biological systems related to humans (or at least, the text implies his fame is derived from treating people).

### Step 2: Identify the Question Being Debated
Next, we identify the specific issue Corvin is trying to prove.
*   **The Claim:** The new dye will **"poison the harbor fish"** and kill them within a year.
*   **The Dom

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the logical flaw as an 'Appeal to False Authority' and clearly articulates the domain mismatch between Eldric's expertise (human surgery) and the claim (marine toxicology). However, the response does not meet the criteria for Level 4 because it fails to articulate wh

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?

**Expected Answer:** **Appeal to emotion** — Substituting emotional response — pity, guilt, sentiment — in place of addressing the factual evidence. Geld does not contest the ledger; she tries to make accusers feel bad for asking.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Matron Geld's argument:

### Step 1: Analyze the Evidence vs. The Argument
*   **The Evidence:** The player possesses a **ledger** showing specific financial discrepancies: half-portions are being served to the children, and the surplus grain is being sold. This is objective, quantifiable data regarding resource allocation and potential theft.
*   **Matron Geld's Argument:** She does not deny the numbers in the ledger, nor does she explain where the missing grain went. Instead, she shifts the focus entirely to her **emotional labor** and **past kindness**:
    *   Staying up all night with sick children.
    *   Comforting a grieving child (Pip).
    *   Braiding hair for a festival (Lila).
    *   Asking the board to loo

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies that Geld ignores the factual evidence (the ledger) and substitutes it with emotional appeals regarding her character and past deeds. They explicitly name the 'Appeal to Emotion (Ad Misericordiam)' and 'Fallacy of Irrelevant Conclusion,' satisfying the requirement to

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Saffron's pitch sounds appealing. What evidence does he give that the spring water cures anything? Is 'it's natural' really a reason?

**Expected Answer:** **Appeal to nature** — Arguing that a product works because it is natural, treating naturalness as sufficient evidence of safety and efficacy.

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of Saffron's reasoning, the evidence he offers, and the logical principles at play.

### Step 1: Analyzing the Evidence Provided
When asked what is in the vials and why they work, Saffron provides the following points:
1.  **Composition:** The water is "pure mountain spring water" and "untouched by human hands."
2.  **Origin:** It comes "straight from the earth."
3.  **Contrast:** He contrasts it with "alchemical concoctions" brewed in workshops with "strange powders."
4.  **Mechanism:** He claims, "Your body knows what is natural" and that it works *with* the body, not against it.

**Crucial Observation:** Saffron provides **zero empirical evidence** that the water cures anything. He offers no clinical trials, no historical d

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Appeal to Nature' fallacy, provides specific counterexamples of harmful natural substances (arsenic, botulinum toxin, etc.), and clearly distinguishes between the emotional bias for natural products and the lack of empirical evidence for efficacy. This meets all cri

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What evidence does Paddy give that the charm works? Is 'everyone is buying one' a reason?

**Expected Answer:** **Bandwagon (argumentum ad populum)** — Arguing that something must be true or good because many people believe it or do it. Treating popularity as evidence.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Paddy's argument:

### 1. Analysis of the Evidence Provided
When asked what evidence Paddy gives that the charm **works**, the answer is **none**.

Paddy does not cite any functional benefits, magical effects, or historical data proving the charms provide protection, luck, or health. Instead, he offers a list of *adoption rates*:
*   "Half the village is wearing one."
*   "Farmer Crewe bought three."
*   "The baker's whole family has them."
*   "Magistrate Dunne picked one up."

These are observations of **behavior** (people buying/wearing), not observations of **outcome** (the charms actually doing anything).

### 2. Is "Everyone is buying one" a reason?
**No, "everyone is buying one" is not a valid logical reason to bel

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (Appeal to Popularity/Bandwagon), clearly distinguishes between evidence of behavior (popularity) and evidence of outcome (efficacy), identifies the social pressure component (FOMO), and explains why popularity does not establish truth. This meets all criteri

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The deputy thinks it is more likely that Linda is a bank clerk AND an activist than that she is just a bank clerk. Is the deputy's reasoning correct?

**Expected Answer:** **Conjunction fallacy** — The deputy judges P(bank clerk AND activist) > P(bank clerk). This violates a basic law of probability: the probability of a conjunction can never exceed the probability of either conjunct alone. P(A and B) <= P(A). The error occurs because the conjunction fits a compelling narrative (the 'represent

**Model Response:**
> The deputy's reasoning is **incorrect**.

Here is the step-by-step logical breakdown of why this reasoning fails:

### 1. The Logical Principle: The Conjunction Rule
In probability theory, there is a fundamental rule known as the **Conjunction Rule**. It states that the probability of two events occurring together (a conjunction) can never be higher than the probability of either event occurring alone.

Mathematically, if we define:
*   $A$ = The event that Linda is a bank clerk.
*   $B$ = The event that Linda is a member of the Fair Trade Alliance.

The probability of both happening is $P(A \text{ and } B)$.
The probability of just the first happening is $P(A)$.

The rule dictates that:
$$P(A \text{ and } B) \leq P(A)$$

This is because the set of people who are *both* bank clerks and act

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly meets all criteria for Level 4. They explicitly identify the 'Conjunction Fallacy,' state the probability rule P(A and B) <= P(A) with mathematical notation, explain the role of the 'Representativeness Heuristic' in driving the error, and correctly analyze the subset relationsh

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sera says there is a 95% chance the patient has Stoneblight based on the positive test. Is she right? What is the actual probability?

**Expected Answer:** **Base rate neglect** — Sera assumes that a positive result on a 95% accurate test means a 95% chance of disease. She ignores the base rate of 0.5%. For 100,000 people: 500 have Stoneblight. The test catches 475 of them (true positives). Of the 99,500 healthy people, the test falsely flags 5% = 4,975 (false positives). Tot

**Model Response:**
> No, Sera is **not right**. Her conclusion that there is a 95% chance the patient has Stoneblight is a classic statistical error.

Here is the step-by-step breakdown of the actual probability and the reasoning behind it.

### Step-by-Step Calculation

To find the true probability that the patient has the disease given a positive test result ($P(\text{Disease} | \text{Positive})$), we must use **Bayes' Theorem**. We cannot simply look at the test's accuracy in isolation; we must factor in how rare the disease is (the base rate).

Let's assume a hypothetical population of **10,000 people** to make the math clear:

1.  **Calculate the number of people with the disease (Prevalence):**
    *   The disease affects 0.5% of the population.
    *   $10,000 \times 0.005 = 50$ people have Stoneblight.

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies base rate neglect, explicitly names the fallacy, and performs a precise calculation using a hypothetical population to arrive at the correct probability (~8.7%). They clearly explain the mechanism (false positives overwhelming true positives due to low prevalence) an

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Minister Kael says the data proves small schools produce better scholars. Is the data as convincing as he thinks? What should he check before spending 1.7 million gold?

**Expected Answer:** **Law of small numbers / small numbers fallacy** — Kael observes that small schools top the achievement rankings and concludes that being small causes better performance. But smaller populations produce more variable outcomes: with fewer students, a few strong (or weak) performers swing the average dramatically. If Kael checked the bottom of the ran

**Model Response:**
> Minister Kael's conclusion is **not convincing**, and his reasoning contains a critical statistical flaw that makes the proposed spending of 1.7 million gold highly risky and likely ineffective.

Here is the step-by-step analysis of the reasoning pattern, the specific fallacy involved, and what the Minister should check before acting.

### 1. The Reasoning Pattern and Fallacy
The core error in Minister Kael's logic is known as **Survivorship Bias** combined with a misunderstanding of **Statistical Variance due to Sample Size** (often related to the **Small Sample Size Fallacy**).

*   **The Flaw in Logic:** Kael assumes that because the *top* schools are small, being small *causes* high performance. He ignores the distribution of the *bottom* schools.
*   **The Statistical Reality:** In an

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the statistical flaw (small sample size leading to high variance/extremes) and explicitly predicts that small schools would also appear at the bottom of the rankings. They clearly distinguish between variance and causal quality, explaining that splitting schools incr

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sal says nine out of ten customers feel better after taking his elixir. Is this good evidence that the elixir works?

**Expected Answer:** **Regression to the mean** — People seek remedies when symptoms are at their peak (an extreme observation). After peak symptoms, the natural tendency is to return to baseline health — this is regression to the mean. Sal attributes the improvement to his elixir, but the improvement would likely have occurred regardless. The nine

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning and the conclusion regarding the validity of the evidence.

### Step-by-Step Analysis

**1. Analyze the Claim vs. the Evidence**
*   **The Claim:** The elixir *causes* the cold to go away (causality).
*   **The Evidence:** 9 out of 10 customers report feeling better within three days (correlation/observation).
*   **The Gap:** The argument assumes that because improvement happened *after* taking the elixir, the elixir must be the *cause* of the improvement.

**2. Evaluate the Nature of the Condition (The Cold)**
*   The common cold is a self-limiting viral infection. In the vast majority of cases, the human immune system clears the virus naturally within 7 to 10 days, regardless of treatment.
*   The scenari

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that the improvement is likely due to natural recovery (the core mechanism of regression to the mean) and explicitly notes the lack of a control group. They accurately explain that the '9 out of 10' statistic is meaningless without a baseline recovery rate. However, 

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Rurik says the dice are 'owed' a high roll after six lows. What is wrong with his reasoning?

**Expected Answer:** **Gambler's fallacy** — The mistaken belief that if a random event has occurred more frequently than expected, it is less likely to occur next. Each independent trial has the same probability regardless of previous outcomes.

**Model Response:**
> Rurik's reasoning is a classic example of the **Gambler's Fallacy** (also known as the Monte Carlo Fallacy).

Here is the step-by-step breakdown of why his logic is flawed:

1.  **Assumption of Independence**: In a fair game of chance, such as rolling dice, each roll is an **independent event**. This means the outcome of the current roll is not influenced by the outcomes of previous rolls. The dice have no memory; they do not "know" they just rolled six low numbers in a row.
2.  **The Flawed Logic of "Due"**: Rurik believes that because a specific outcome (low rolls) has happened frequently in the recent past, the opposite outcome (a high roll) becomes *more* likely to happen next to "balance out" the statistics. He treats the probability as if it must self-correct in the short term.
3.  *

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Gambler's Fallacy by name and provides a clear, accurate explanation of independent events and the lack of 'memory' in dice rolls. They also effectively distinguish between short-term streaks and the Law of Large Numbers. However, the response does not reach Leve

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Breck says all the people of Dunmore are cheats based on his two visits. Is his conclusion justified by his evidence?

**Expected Answer:** **Hasty generalization** — Breck draws a universal conclusion ('all people of Dunmore are cheats') from a sample of two negative interactions. The sample size is far too small to support a generalization about an entire town's population. He is also ignoring the possibility of confounding factors (perhaps he visited during a 

**Model Response:**
> Based on the scenario provided, Breck's conclusion is **not justified** by his evidence.

Here is the step-by-step reasoning regarding the logical flaws in his argument:

### 1. Analysis of the Evidence vs. Conclusion
*   **The Evidence:** Breck has visited Dunmore exactly **two times**.
    *   Visit 1: One specific individual (the innkeeper) overcharged him.
    *   Visit 2: One specific individual (a street vendor) sold him rotten apples.
*   **The Conclusion:** He claims that **all** the people of Dunmore are "cheats and thieves, every last one of them."
*   **The Discrepancy:** There is a massive gap between the sample size (two specific transactions with two specific individuals) and the scope of the claim (the entire population of a town). Even if we assume the innkeeper and the ven

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Hasty Generalization' fallacy and explains that a sample of two is insufficient for a universal claim about a whole town. Crucially, the response exceeds Level 3 by discussing confounding factors (bad luck, specific bad actors vs. cultural trait) and explicitly 

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Brix says seagulls are causing the decline of the fishing fleet because the two trends are correlated. Is his reasoning sound?

**Expected Answer:** **False cause / post hoc fallacy** — Brix observes that two variables are correlated over time (fishing boats declining, seagulls increasing) and infers that one causes the other. But correlation does not establish causation. There are four possibilities: (1) seagulls cause boat decline, (2) boat decline causes seagull increase, (3) a 

**Model Response:**
> Councillor Brix's reasoning is **not sound**. While his observation of a correlation is factually correct (both the number of fishing boats and the number of seagulls have changed over time), his conclusion that one *caused* the other is logically flawed.

Here is the step-by-step breakdown of the reasoning pattern and the specific fallacy involved:

### 1. Identification of the Fallacy
The specific logical error Brix is committing is known as **Cum Hoc Ergo Propter Hoc** (Latin for "with this, therefore because of this"), commonly referred to as the **Correlation Does Not Imply Causation** fallacy.

Brix assumes that because two variables (fishing boat numbers and seagull populations) moved in opposite directions simultaneously, one must be the direct cause of the other. He ignores the po

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the fallacy (Correlation does not imply causation/Cum Hoc) and provides strong alternative explanations, including reverse causation and common causes (overfishing, economic shifts). However, the response does not reach Level 4 because it fails to explicitly enumerat

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Vance seems to be complimenting Pip, but something feels off. What rhetorical technique is Vance using?

**Expected Answer:** **Evaluative language and presupposition** — Using loaded terms, diminutives, and embedded presuppositions to bias perception without explicit argument. The framing does the persuasive work while appearing neutral.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the rhetorical technique Vance is using:

### Step 1: Analyze the Surface Meaning vs. Context
On the surface, Vance acknowledges a fact: Pip cleared the Thornwall Caverns. He uses words like "accomplishment" and "exciting," which are typically positive. However, the context immediately undermines these words. Vance qualifies the accomplishment with "even Pip" and "limited background," and dismisses the adventure as "little" and "very exciting for *him*" (implying it was trivial to everyone else).

### Step 2: Identify the Discrepancy
There is a clear contradiction between the literal meaning of the words (praise) and the intended meaning (condescension and dismissal). Vance is saying the opposite of what he literally mean

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies specific dismissive words like 'even' and 'little' and notes the condescending tone (meeting Level 2 criteria). However, the response misidentifies the core rhetorical technique as 'Sarcasm/Verbal Irony' rather than the required pattern of 'Evaluative language and pr

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Question:** Can you identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work?

**Expected Answer:** **Assuring, guarding, and discounting** — Three rhetorical moves managing acceptance: assuring ('everyone knows') discourages questioning, guarding ('most scholars') hedges while sounding authoritative, discounting ('granted X, but Y') acknowledges then dismisses objections.

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the rhetorical moves used by the royal advisor, an evaluation of their legitimacy, and the identification of the underlying logical fallacies.

### Step 1: Identifying the Rhetorical Moves

In critical thinking and argumentation theory (specifically within the framework of Chelton's analysis of argumentative strategies), we can categorize the advisor's statements as follows:

**1. Assuring Moves**
*Definition:* Statements intended to convince the audience that a claim is true without providing evidence, often by appealing to authority or consensus.
*   **The Move:** "Everyone knows the northern threat is growing — that's simply beyond dispute."
*   **The Move:** "Now, most military scholars agree the border fortress is our 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all three rhetorical moves (assuring, guarding, discounting) and provides a clear explanation of how each functions to substitute rhetoric for evidence. However, the response falls short of Level 4 because it categorically dismisses all uses as illegitimate without a

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Torin says that because Amanda argued badly, the herb must NOT have healing properties. What is wrong with Torin's reasoning?

**Expected Answer:** **The fallacy fallacy** — Assuming that because an argument for a conclusion contains a fallacy, the conclusion itself must be false. A bad argument for X does not prove not-X.

**Model Response:**
> Torin's reasoning contains a fundamental logical error known as the **Fallacy Fallacy** (also called *Argumentum ad Logicam*).

Here is the step-by-step breakdown of why his reasoning is flawed:

1.  **Identify the Premise:** Torin correctly identifies that Amanda's argument is flawed. She used an **Appeal to Tradition** (arguing something is true just because "her grandmother used it"). This is indeed a logical fallacy; the fact that something is traditional does not automatically make it true or effective.
2.  **Identify the Conclusion:** Torin concludes that because Amanda's *argument* was bad, the *conclusion* she reached (that Silvervein has healing properties) must be false.
3.  **Analyze the Flaw:** The validity of a conclusion is independent of the quality of the argument used to s

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Fallacy Fallacy', clearly distinguishes between the quality of the argument and the truth of the conclusion, provides a relevant counter-example, and correctly identifies that the conclusion's validity is an empirical matter requiring testing rather than logical ded

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The innkeeper's daughter has laid out the situation. Identify the acts, the states, and the outcomes. Then check: does either act dominate the other with these values?

**Expected Answer:** **Decision matrix construction** — A decision matrix organizes a choice into rows (acts the agent controls), columns (states of the world the agent does not control), and cells (outcomes with assigned values). This is the foundational representation for all of decision theory.

**Model Response:**
> Based on the scenario and the payoff matrix provided, here is the step-by-step analysis of the decision structure and the reasoning pattern demonstrated.

### 1. Deconstructing the Decision Matrix

First, let's formally identify the components of the decision problem as requested:

*   **Acts (The choices available to the player):**
    1.  **Take Umbrella** (Buy the umbrella for 5 copper).
    2.  **Leave Umbrella** (Do not buy the umbrella).

*   **States (The uncertain future conditions):**
    1.  **Rain** (The storm hits).
    2.  **No Rain** (The sky clears).

*   **Outcomes (The resulting utility values assigned in the scenario):**
    *   *Take Umbrella + Rain:* Dry but burdened (**Value: 3**)
    *   *Take Umbrella + No Rain:* Dry and burdened (**Value: 2**)
    *   *Leave Umbrell

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies acts, states, and outcomes, constructs the logic of the matrix accurately, and explicitly determines that no dominance exists because each act wins in a different state. Furthermore, the student exceeds the baseline requirements by discussing alternative decision cri

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The merchant has set up a matrix. Dominance reasoning gives no clear answer. But is there a deeper problem with how the matrix is constructed? What assumption does dominance reasoning require about the relationship between acts and states?

**Expected Answer:** **Dominance reasoning and state-act independence** — Dominance reasoning says: if one act yields a better outcome in every possible state, choose it. But this only works when states are independent of acts. In the extortion case, whether the cart is damaged depends on whether you pay — the states are not independent of the acts, which violates the str

**Model Response:**
> The deeper problem with the matrix constructed by the merchant (or the player) is that it violates the fundamental requirement of **Causal Independence** (often called the **Independence of Acts and States**) required for valid Dominance Reasoning.

Here is the step-by-step breakdown of the reasoning:

### 1. The Requirement of Dominance Reasoning
For Dominance Reasoning to be logically valid, the "States of the World" (in this case, *Cart Damaged* vs. *Cart Not Damaged*) must be **probabilistically independent** of the "Acts" chosen (Pay vs. Don't Pay).

In other words, the probability of a state occurring must not change based on the action you take. The decision matrix assumes that the world is a fixed background against which you make a choice, not a reactive system that changes based 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the violation of the independence requirement (Level 3) and goes further to explain how to restructure the problem using Causal Decision Theory by conditioning outcomes on acts. They also explicitly connect the scenario to Newcomb's Problem and the distinction betwee

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The prospector wants the biggest possible payoff and does not care about the downside. Apply the maximax rule: for each expedition, find its best outcome, then pick the expedition with the highest best outcome.

**Expected Answer:** **Maximax** — Maximax identifies the best possible outcome for each act, then selects the act with the highest best-case outcome. It is the optimist's rule: chase the ceiling, ignore the floor.

**Model Response:**
> Based on the scenario and the specific decision rule requested, here is the step-by-step analysis:

### Step 1: Identify the Best Outcome for Each Option
The **Maximax** rule is an optimistic decision-making criterion. It assumes that for any given choice, the most favorable state of nature will occur. Therefore, we must look at the "Rich Deposits" column (the highest value in each row) for every expedition:

1.  **River Panning:** The possible outcomes are 8, 5, and 2.
    *   Best outcome: **8**
2.  **Hilltop Digging:** The possible outcomes are 12, 3, and 1.
    *   Best outcome: **12**
3.  **Cave Exploring:** The possible outcomes are 6, 6, and 4.
    *   Best outcome: **6**

### Step 2: Compare the Best Outcomes
Now, we compare the maximum values identified in the previous step to fin

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Hilltop Digging as the maximax choice (best case = 12) and explicitly explains the mechanism of maximizing the maximum. They go beyond Level 3 by thoroughly articulating the risk-seeking nature of the rule, noting that it disregards downside risk/probabilities, and e

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The scholar wants to avoid the worst possible evening. Apply maximin: for each act, find its worst outcome, then pick the act whose worst outcome is highest.

**Expected Answer:** **Maximin** — Maximin identifies the worst possible outcome for each act, then selects the act whose worst case is least bad. It is the pessimist's rule: raise the floor, ignore the ceiling.

**Model Response:**
> Based on the scenario and the specific instruction to apply the **maximin** rule, here is the step-by-step reasoning and the identification of the underlying principle.

### Step-by-Step Reasoning

1.  **Analyze the Payoff Matrix**:
    The scholar has two possible actions (acts) and two possible states of nature (outcomes regarding the football match).
    *   **Act A: Watch Football**
        *   If Team Wins: Payoff = 4
        *   If Team Loses: Payoff = 1
    *   **Act B: Work on Paper**
        *   If Team Wins: Payoff = 2
        *   If Team Loses: Payoff = 3

2.  **Apply the Maximin Rule**:
    The maximin rule (short for "maximize the minimum") is a decision-making strategy used under uncertainty. It dictates that a decision-maker should:
    *   Identify the **worst possible outc

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the minimum outcomes for both acts (1 and 2), selects the correct act (Work on Paper), and clearly explains the logic of maximizing the minimum (raising the floor) as a pessimistic strategy. However, the response does not explicitly mention that the rule 'ignores the

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Given the profit table, apply Minimax Regret to determine which cargo to load. Show your regret matrix and explain your answer.

**Expected Answer:** **Minimax regret** — Step 1: Build the regret matrix. Column maxima: Mining Camp=18, Fishing Village=16, Fortress=14.

Regret matrix:
              Mining Camp    Fishing Village    Fortress
Furs           0               12              11
Salted Fish   12                0               9
Iron Tools     8              

**Model Response:**
> ### Step 1: Construct the Regret Matrix

To apply the **Minimax Regret** criterion, we first need to calculate the "regret" (or opportunity loss) for each decision. Regret is defined as the difference between the best possible payoff for a specific state of nature (settlement) and the actual payoff achieved by the chosen action (cargo).

**The Profit Table:**

| Cargo | Mining Camp | Fishing Village | Fortress |
| :--- | :---: | :---: | :---: |
| **Furs** | 18 | 4 | 3 |
| **Salted Fish** | 6 | 16 | 5 |
| **Iron Tools** | 10 | 8 | 14 |

**Step 1a: Identify the Maximum Profit for each Settlement (Column Max)**
*   **Mining Camp:** Max(18, 6, 10) = **18**
*   **Fishing Village:** Max(4, 16, 8) = **16**
*   **Fortress:** Max(3, 5, 14) = **14**

**Step 1b: Calculate Regret for each cell**
*Form

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified the Minimax Regret pattern, accurately computed the column maxima and the full regret matrix without arithmetic errors, and correctly determined the maximum regret for each act (12, 12, and 8). They selected the optimal choice (Iron Tools) and provided a clear, compr

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The scholar says education might not increase productivity at all — it just signals pre-existing ability. Under what conditions does this signaling work? What is the key property that makes the signal credible?

**Expected Answer:** **Signaling (Spence's job market model)** — In a signaling game, an informed player (Sender) takes a costly action to reveal private information to an uninformed player (Receiver). Separation requires the Single Crossing Condition: the signal must be more costly for low types than high types. In Spence's model, education is the signal, abilit

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the signaling model, the conditions for its success, and the underlying economic principle at play.

### 1. Analysis of the Signaling Conditions
For the education signal to work in this scenario (creating a **Separating Equilibrium**), two specific conditions must be met simultaneously. These are derived from the "Incentive Compatibility Constraints" for both worker types:

*   **Condition A: The High-Ability Worker must find it worthwhile to get educated.**
    *   If they get educated (level $e$), they earn 100 gold but pay the cost $1 \times e$. Net payoff: $100 - e$.
    *   If they do *not* get educated, employers assume they are low ability, so they earn 40 gold.
    *   **Requirement:** $100 - e > 40 \implies e < 6

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly derives the mathematical range for separation (20 < e < 60) by setting up the incentive compatibility constraints for both high and low types. They explicitly identify the Single Crossing Condition (differential cost structure) as the key property enabling credibility. Furtherm

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Question:** Standard theory says Responders should accept any positive offer. They do not. Why? And how do formal models of social preferences (like Fehr-Schmidt) explain both Responder rejections and Proposer fairness?

**Expected Answer:** **Behavioral game theory** — Behavioral game theory studies how real humans deviate from Nash equilibrium predictions. Key findings: (1) Ultimatum Game: people reject unfair offers at personal cost and anticipate this by making fair offers. (2) Level-k reasoning: people think a few steps ahead, not infinitely. (3) Social prefer

**Model Response:**
> ### Step-by-Step Analysis

#### 1. Deconstructing the Standard Theory Failure
The scenario highlights a classic conflict between **Homo economicus** (the rational, self-interested agent) and actual human behavior.
*   **Standard Theory Prediction:** In the Ultimatum Game, a purely rational Responder faces a binary choice: Accept $x$ (where $x > 0$) or Reject $0$. Since $x > 0$ is mathematically better than $0$, the rational choice is to accept. Anticipating this, a rational Proposer offers the smallest possible positive amount (e.g., 1 gold) to maximize their own payoff.
*   **Observed Reality:** Responders frequently reject low offers (even 1 gold), effectively choosing $0$ over a positive amount. This behavior is irrational under the standard model of **self-interest maximization**.
*   

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Behavioral GT pattern and provides a strong explanation of the Fehr-Schmidt model, including the utility function, parameters (alpha/beta), and the strategic anticipation by Proposers. However, the response does not reach Level 4 because it lacks an explicit conn

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Without commitment, the Incumbent gets 2. With commitment, the Incumbent gets 3. How can removing an option make you better off? Explain the mechanism and give another example of a commitment device.

**Expected Answer:** **Commitment** — Commitment devices improve outcomes in strategic settings by making threats or promises credible. The Paradox of Commitment: having fewer options can be advantageous because it changes the opponent's best response. Types include contracts, reputation, precommitment, burning bridges, delegation, and 

**Model Response:**
> ### Step-by-Step Analysis

**1. Deconstructing the Scenario (The Mechanism)**
To understand why removing an option improves the Incumbent's outcome, we must look at the game theory structure involved, specifically **Sequential Games** and **Subgame Perfect Equilibrium (SPE)**.

*   **Without Commitment (The Baseline):**
    *   The game is sequential: Entrant decides first (Enter or Stay Out), then Incumbent decides (Fight or Accommodate).
    *   *Backward Induction:* If the Entrant enters, the Incumbent compares the payoffs: Fight (0) vs. Accommodate (2). Since $2 > 0$, the rational choice is to Accommodate.
    *   *Entrant's Anticipation:* The Entrant knows the Incumbent is rational and will Accommodate if entered. Therefore, the Entrant calculates: Enter (gets 2) vs. Stay Out (gets 0)

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Commitment/Strategic Precommitment) and provides a flawless explanation of the mechanism using backward induction and payoff changes. They successfully articulate the 'Paradox of Commitment' (freedom as a liability) and provide a second example (Ulysses)

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The instructor lists four conditions for reputation to sustain cooperation. What are they? If any one fails, how does cooperation break down? Give a real-world example of a reputation system and explain which conditions it satisfies.

**Expected Answer:** **Reputation and the shadow of the future** — Reputation is what others believe about your type or strategy based on past actions. In repeated games, reputation creates incentives for cooperation: defecting today earns a short-term gain but destroys future cooperation opportunities. The Folk Theorem shows that in infinitely repeated games (or g

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis, the answer to your specific questions, and the identification of the underlying reasoning principles.

### Part 1: The Four Conditions and Their Failure Modes

The instructor explicitly lists four necessary conditions for reputation to sustain cooperation in a repeated game. Here they are, along with an analysis of how cooperation collapses if any single condition is missing:

1.  **Condition: Interactions must be repeated (or there is a chance of future interaction).**
    *   **Failure Mode:** If interactions are one-shot (a "one-off" event), the "shadow of the future" disappears. Without the threat of future retaliation or the promise of future reward, the rational choice becomes immediate defection (cheating) because th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all four necessary conditions (repetition, observability, patience, punishment) and explains their failure modes clearly. They provide a strong real-world example (online marketplaces) that maps directly to these conditions. The response explicitly names and explains

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Bob risks 2 gold to win 1 gold, with a total stake of 3 gold. If this bet is fair in Bob's eyes, what is his credence — his subjective probability — that the storm will come? Show the calculation.

**Expected Answer:** **Fair betting rate as credence** — A fair betting rate quantifies subjective probability. If an agent considers a bet fair (expected value zero), their credence in the proposition equals their potential loss divided by the total stake. Bob risks 2 gold on a 3 gold total stake, so his credence in the storm is 2/3.

**Model Response:**
> ### Step-by-Step Deduction

To determine Bob's credence (subjective probability), we must analyze the concept of a "fair bet." In decision theory and probability, a bet is considered **fair** to a person if their expected value (EV) for that bet is zero. This means the person believes the potential gain, weighted by the probability of winning, exactly equals the potential loss, weighted by the probability of losing.

**1. Define the Variables:**
*   Let $P$ be Bob's subjective probability (credence) that the storm will come.
*   Consequently, $(1 - P)$ is the probability that the storm will *not* come.
*   **Bob's Potential Win:** If the storm comes, Bob wins Ally's stake of **1 gold**.
*   **Bob's Potential Loss:** If the storm does not come, Bob loses his own stake of **2 gold**.

**2. S

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly calculates the credence as 2/3 using both the formal Expected Value equation (Level 3 criteria) and the intuitive stake ratio. Furthermore, the response exceeds Level 3 by explicitly discussing the underlying principles (Dutch Book Argumentation, Coherence Principle) and explai

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The bookie's implied probabilities sum to 1.05. Explain why this guarantees the bookie a profit regardless of which horse wins. Then answer: if a gambler's personal credences summed to more than 1, how could someone exploit them?

**Expected Answer:** **Dutch Book argument** — A Dutch Book is a set of bets that guarantees a net loss for the agent regardless of the outcome. The Dutch Book theorem proves that if an agent's credences violate the axioms of probability (e.g., sum to more or less than 1 for an exhaustive partition), there exists a set of bets the agent consider

**Model Response:**
> ### Step-by-Step Analysis

#### 1. Why the Bookie Guarantees a Profit
The core mechanism here is the **Overround** (also known as the "vig" or "juice"). In a fair market where probabilities sum to exactly 1.0 (100%), the bookie breaks even if they take equal money on every outcome. However, Mercer has set the odds such that the implied probabilities sum to **1.05**.

Let's break down the math using a hypothetical betting pool:
*   **The Implied Probabilities:** 0.50 + 0.25 + 0.20 + 0.10 = 1.05.
*   **The "Fair" Payout:** If the bookie accepts \$105 in total bets distributed perfectly according to these odds (i.e., \$50 on Gumption, \$25 on Gallifray, \$20 on Tungsten, \$10 on Shadow), the payout for the winning horse is calculated based on the odds:
    *   If **Gumption** (1:1) wins: The 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a Dutch Book argument and accurately explains the mechanism: how violating probability axioms (sum > 1) leads to guaranteed exploitation. They successfully generalize from the bookie's overround to the gambler's inconsistent credences. However, the res

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Nell says something doesn't add up. She's right. Look at the implied probabilities on Oliver's board. What mathematical rule do they violate, and what does that mean for anyone betting at these odds?

**Expected Answer:** **Axioms of probability** — The three axioms of probability require: (1) Non-negativity: all probabilities >= 0; (2) Normality: probabilities over the entire sample space sum to exactly 1; (3) Finite Additivity: for mutually exclusive events, P(A or B) = P(A) + P(B). Oliver's odds violate Axiom 2 because the implied probabilit

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the mathematical violation and its implications.

### Step 1: Analyze the Mathematical Data
First, let's look at the implied probabilities provided on Oliver's chalkboard:
*   **Gumption:** 0.50 (derived from 1-to-1 odds)
*   **Gallifray:** 0.25 (derived from 3-to-1 odds)
*   **Tungsten:** 0.20 (derived from 4-to-1 odds)
*   **Shadow:** 0.10 (derived from 9-to-1 odds)

When we sum these probabilities:
$$0.50 + 0.25 + 0.20 + 0.10 = 1.05$$

### Step 2: Identify the Violated Principle
The fundamental mathematical rule being violated here is the **Axiom of Total Probability** (specifically within the context of a mutually exclusive and exhaustive set of events).

In a standard horse race with four runners, exactly one horse m

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the sum of probabilities (1.05) and explicitly names the violation of the axiom requiring probabilities to sum to 1 (referred to as the Axiom of Total Probability/Law of Total Probability). They correctly explain the implication: a guaranteed profit for the bookie (o

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss and Lira are both using the word 'probability' but seem to mean different things. Are they contradicting each other, or could both be right? What exactly is the difference between what they are describing?

**Expected Answer:** **Subjective vs objective probability** — Objective probability (chance) refers to mind-independent features of the world — physical propensities, frequencies, quantum indeterminacies. Subjective probability (credence) refers to an agent's degree of confidence in a proposition, revealed through betting behavior. Both satisfy the same axioms

**Model Response:**
> ### Step-by-Step Analysis

**1. Deconstructing Scholar Voss's Position**
Voss describes probability as a "physical property" of the comet's orbit, independent of human belief.
*   **Core Concept:** This aligns with the **Frequentist** or **Objective** interpretation of probability.
*   **Reasoning:** In this view, probability is a long-run frequency of events in a physical system. If the comet's orbit were repeated infinitely under identical conditions, 73% of those instances would result in a return within a decade. The probability exists "out there" in the universe, regardless of whether anyone is observing it.
*   **Key Phrase:** "As real as its mass."

**2. Deconstructing Scholar Lira's Position**
Lira describes probability as a "degree of confidence in a human mind," noting that diffe

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between objective chance (Voss/Aleatory) and subjective credence (Lira/Epistemic), correctly identifying that one refers to physical properties and the other to degrees of belief. They explicitly note that both frameworks utilize the same mathematical axioms (Kolmog

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms?

**Expected Answer:** **Principal Principle** — The Principal Principle (Lewis/Weatherson) states: if you know the objective chance of an event is x, your rational credence should be x, provided you have no inadmissible evidence (e.g., time travel, crystal balls). Formally: Pr(p | Ch(p)=x) = x. Cade knows Ch(Heads)=0.80 but sets Cr(Heads)=0.50, v

**Model Response:**
> This scenario presents a classic conflict between **internal coherence** (the mathematical consistency of one's beliefs) and **external rationality** (how those beliefs relate to available evidence).

Here is the step-by-step analysis of Cade's reasoning and the specific norm he is violating.

### 1. The Distinction Between Coherence and Calibration
Brennan is correct that Cade is **internally coherent**.
*   Cade assigns $P(\text{Heads}) = 0.5$ and $P(\text{Tails}) = 0.5$.
*   These sum to 1.
*   He is not "Dutch-Bookable" in the strict sense that a bookie cannot construct a set of bets based *solely* on his stated probabilities that guarantees a loss for Cade *given his own probability assignments*. If Cade truly believes the odds are 50-50, betting on tails at even odds is a "fair" bet 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cade is ignoring objective evidence and explicitly distinguishes this violation from a Dutch Book argument (internal coherence), which satisfies Level 2. However, the student fails to identify the specific 'Principal Principle' (Lewis/Weatherson) required for Le

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Calculate the expected utility of each option using the formula EU(Act) = sum of P(State) * U(Act|State). Which option should the healer choose, and why does it differ from what dominance reasoning would say?

**Expected Answer:** **Maximize Expected Utility (MEU)** — MEU weighs each outcome by its probability and sums to get the expected utility of each act. The agent selects the act with the highest expected utility. EU(Act) = P(S1)*U(Act|S1) + P(S2)*U(Act|S2) + ...

**Model Response:**
> ### Step-by-Step Calculation

First, we need to calculate the **Expected Utility (EU)** for each option. In this context, since the values represent costs (negative utility), a "higher" expected utility means a value closer to zero (less negative), representing the lower expected cost.

The formula provided is:
$$EU(\text{Act}) = \sum [P(\text{State}) \times U(\text{Act}|\text{State})]$$

#### Option 1: Use Cream
*   **State A (Rash Clears):** Probability = 0.85, Cost = -20 silver
*   **State B (Rash Persists):** Probability = 0.15, Cost = -120 silver (20 for cream + 100 for city visit)

$$EU(\text{Cream}) = (0.85 \times -20) + (0.15 \times -120)$$
$$EU(\text{Cream}) = -17 + (-18)$$
$$EU(\text{Cream}) = \mathbf{-35 \text{ silver}}$$

#### Option 2: Do Nothing
*   **State A (Rash Clears):**

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly calculates both expected utilities (-35 and -50), selects the correct option (Use Cream), and explicitly explains the probability weighting mechanism. However, the response does not reach Level 4 because it fails to correctly explain *why* MEU overrides dominance in this specif

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Captain Aldric's scout gave rankings but not numbers. Why is that not enough for a good decision here? What additional information would you need, and how would it change the analysis?

**Expected Answer:** **Cardinal vs ordinal utility** — Ordinal utility provides only a ranking: A > B > C. Cardinal utility assigns numerical values that capture how much better A is than B. Decision rules like Maximin and Maximax use ordinal utility and are therefore blind to magnitude. MEU requires cardinal utility because it multiplies utility by pro

**Model Response:**
> ### Step-by-Step Analysis

#### 1. Deconstructing the Scenario
Captain Aldric is facing a classic decision-making problem under uncertainty. He has three options (Hilltop, Bridge, Ravine) and two possible states of nature (Enemy from North, Enemy from South).

*   **The Data Available:** Ordinal rankings (1st, 2nd, 3rd) for each scenario.
    *   *North:* Hilltop (1) > Bridge (2) > Ravine (3).
    *   *South:* Hilltop (1) > Bridge (2) > Ravine (3).
*   **The Decision Rule in Question:** Maximin (Maximize the Minimum). This rule suggests looking at the worst possible outcome for each option and choosing the one with the "best" worst outcome.
*   **The Conflict:**
    *   Under the **North** scenario, the "worst" outcome for the Ravine is **catastrophic** (deathtrap).
    *   Under the **Sou

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between ordinal and cardinal utility and correctly explains that rankings ignore magnitude, which is the core failure of rules like Maximin in this scenario. They effectively illustrate how cardinal values would resolve the issue by assigning plausible numbers to sh

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Kael calls Sera irrational because she turns down a bet with higher expected monetary value. Is he right? Or is there a way to explain Sera's preference that is perfectly consistent with maximizing expected utility?

**Expected Answer:** **Risk aversion and utility curves** — Under MEU, risk attitude is encoded in the shape of the utility function. A linear utility function (U = wealth) produces risk neutrality. A concave function (e.g., U = sqrt(wealth)) produces risk aversion: the utility of the expected value exceeds the expected utility of the gamble. Sera's declinin

**Model Response:**
> Kael is **not right** to call Sera irrational. In fact, Sera's decision is the textbook example of **rational behavior** when viewed through the lens of **Expected Utility Theory (EUT)**, whereas Kael is making a category error by conflating *Expected Monetary Value (EMV)* with *Expected Utility*.

Here is the step-by-step reasoning behind why Sera is acting rationally:

### 1. Distinguishing Money from Utility
Kael's argument relies entirely on **Expected Monetary Value (EMV)**. He calculates the gamble as:
$$ (0.5 \times 1000) + (0.5 \times 0) = 500 \text{ gold} $$
He compares this to the sure thing of 400 gold. Since $500 > 400$, he concludes the gamble is the superior choice.

However, in economics and decision theory, humans do not maximize *money*; they maximize **utility** (satisfac

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as risk aversion derived from diminishing marginal utility. They explicitly distinguish between Expected Monetary Value and Expected Utility, explain the concave nature of the utility function, and perform a specific calculation using U(x) = sqrt(x) to de

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** John keeps cycling through ice cream trades and losing money. What structural property of his preferences allows the vendor to exploit him? What would John need to change about his preferences to stop the bleeding?

**Expected Answer:** **Transitivity and money pumps** — Transitivity requires: if A > B and B > C, then A > C. John's preferences violate transitivity (S > C, C > V, but V > S). The money pump shows that intransitive preferences are exploitable: an agent can be led through a cycle of individually rational trades that return them to the starting point min

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the structural problem and the solution.

### Step-by-Step Deduction

**1. Analyzing the Preference Structure**
Let's break down John's stated preferences into a logical chain:
*   **Preference A:** Strawberry > Chocolate (Strawberry is preferred to Chocolate)
*   **Preference B:** Chocolate > Vanilla (Chocolate is preferred to Vanilla)
*   **Preference C:** Vanilla > Strawberry (Vanilla is preferred to Strawberry)

If we combine these, we get a cycle:
$$ \text{Strawberry} > \text{Chocolate} > \text{Vanilla} > \text{Strawberry} $$

**2. Identifying the Logical Flaw**
In rational choice theory and economics, a fundamental requirement for consistent decision-making is **Transitivity**.
*   **Definition of Transitivity:** If

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the intransitive cycle (S > C > V > S) and explicitly names the violated property as Transitivity. They accurately explain the Money Pump mechanism, noting how locally rational trades lead to global irrationality and resource depletion. Furthermore, the response addr

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin asks how removing an option nobody chose can change the recommendation. What principle is being violated here, and why does MEU avoid this problem?

**Expected Answer:** **Independence of Irrelevant Alternatives (IIA)** — IIA states: if option C is chosen from set S, then C should still be chosen from any subset of S containing C. Minimax Regret violates IIA because regret is calculated relative to the best available option in each state. When the menu changes, the reference point changes, which can reverse preferenc

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the principle being violated and why Expected Utility theory avoids it.

### 1. Identification of the Principle
The principle being violated is the **Independence of Irrelevant Alternatives (IIA)**.

In decision theory, IIA states that the relative preference between two options (e.g., Baseball vs. Movies) should not change solely because a third option (e.g., Picnic) is removed from the set, provided that the third option was not chosen in the first place.

In your scenario:
*   **Initial State:** When {Picnic, Baseball, Movies} were available, the Minimax Regret rule selected **Baseball**.
*   **New State:** When {Picnic} is removed, leaving only {Baseball, Movies}, the Minimax Regret rule selects **Movies**.
*   **The 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Independence of Irrelevant Alternatives (IIA) and explains precisely how Minimax Regret violates it due to the shifting reference point (benchmark) when the menu changes. They also clearly contrast this with MEU's menu-independence. Crucially, the response explic

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Father Clement's argument seems airtight — infinity times anything positive is infinity. But Dara is not convinced. What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?

**Expected Answer:** **Pascal's Wager** — Pascal's Wager applies MEU with infinite utility. When any outcome has infinite value, the expected utility calculation is dominated by that outcome regardless of its probability (as long as P > 0). This 'washing out' effect makes MEU insensitive to evidence — a feature that many consider a reductio

**Model Response:**
> Father Clement's argument is a classic formulation of **Pascal's Wager**, which attempts to use decision theory to prove that belief in God is the only rational choice. While the mathematical intuition that "infinity dominates any finite number" seems sound on the surface, Dara's objections highlight fundamental flaws in applying Expected Utility Theory (EUT) to metaphysical questions.

Here is a step-by-step analysis of the strongest objections and what they reveal about the limits of rational decision-making.

### 1. The "Many Gods" Objection (The Problem of Indeterminacy)
Dara's first point—that one could apply the same logic to Zeus, Thor, or the Flying Spaghetti Monster—is the most devastating logical flaw in the Wager.

*   **The Reasoning:** Pascal's matrix assumes a binary choice: 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Pascal's Wager and articulates multiple strong objections, including the Many Gods problem, epistemic voluntarism, and the mathematical issue of infinite utilities (indeterminate forms). They explicitly discuss the 'washing out' effect where infinity dominates probab

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** The expected value is infinite, but you would not pay a million gold to play. What has gone wrong? Is expected value the wrong tool, or are we applying it to the wrong quantity?

**Expected Answer:** **St. Petersburg Paradox** — A fair coin is flipped until heads. Payoff = 2^n where n is the number of flips. Expected value = sum from n=1 to infinity of (1/2)^n × 2^n = sum of 1 = infinity. Yet no reasonable person would pay more than about 20-30 gold. The paradox reveals that expected monetary value is not the same as expect

**Model Response:**
> This scenario describes the famous **St. Petersburg Paradox**, first discussed by Daniel Bernoulli in 1738. The paradox arises because the mathematical calculation of "Expected Value" (EV) suggests an infinite payoff, yet human intuition (and rational behavior in a real-world context) dictates that no one would pay a large sum (like a million gold) to play.

Here is the step-by-step breakdown of what has gone wrong and the reasoning pattern involved.

### 1. The Mathematical Flaw: The Assumption of Infinite Resources
The calculation $EV = \sum (1/2)^n \times 2^n = \infty$ is mathematically correct **only under the assumption of infinite resources**.

In the real world (or even within the Archon Casino), the gambler cannot pay out infinite gold.
- If the gambler has a finite bankroll (say, 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the St. Petersburg Paradox and provides a strong explanation of the resolution via diminishing marginal utility (logarithmic utility), satisfying Level 3 criteria. They also offer an alternative resolution based on finite bankrolls. However, the response does not rea

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The showmaster says choosing Gamble 1 and Gamble 4 is inconsistent. Can you see why? What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

**Expected Answer:** **Allais Paradox (Certainty Effect)** — The Allais Paradox demonstrates that people overweight certainty. In Choice 1, Gamble 1 offers certainty ($1M guaranteed), which has disproportionate psychological appeal. In Choice 2, neither option is certain, so people chase the higher payoff (Gamble 4). But the 89% column (Tickets 12-100) is ide

**Model Response:**
> This scenario is a classic illustration of the **Allais Paradox**, named after the French economist Maurice Allais who first identified it in 1953. The showmaster is correct: choosing Gamble 1 and Gamble 4 simultaneously violates the **Independence Axiom** (also known as the Independence of Irrelevant Alternatives) of Expected Utility Theory (MEU).

Here is the step-by-step logical deduction of why this combination is inconsistent:

### 1. Analyze the Probabilities and Outcomes
Let's break down the probabilities based on the urn composition (100 balls total):
*   **Ticket #1:** 1% probability ($0.01$)
*   **Tickets #2–11:** 10% probability ($0.10$)
*   **Tickets #12–100:** 89% probability ($0.89$)

Now, let's map the payouts for each gamble:

| Outcome Region | Probability | Gamble 1 | Gam

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Allais Paradox and the Independence Axiom (Sure Thing Principle). They accurately break down the probabilities and identify the common consequence (the 89% column) that should cancel out, explaining why the preferences are logically inconsistent. The response sto

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss shows that you should accept the bet unconditionally but reject it in every conditional state. Is the Sure Thing Principle actually violated here? Look carefully at whether the conditioning events form a proper partition.

**Expected Answer:** **Sure Thing Principle** — STP states: if A is preferred to B conditional on E, and A is preferred to B conditional on NOT-E, then A is preferred to B unconditionally. It is the backbone of independence in MEU. The Disjunction Effect appears to violate STP but actually involves overlapping (non-exclusive) conditioning events,

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the logic, the validity of the Sure Thing Principle, and the specific fallacy being demonstrated.

### Step 1: Analyze the Sure Thing Principle (STP)
The Sure Thing Principle, formulated by Leonard Savage, states that if a decision-maker prefers action $A$ to action $B$ in every possible state of the world (or in every event of a partition), they must prefer $A$ to $B$ unconditionally.

Mathematically, if $E_1, E_2, \dots, E_n$ form a **partition** of the sample space (meaning they are mutually exclusive and collectively exhaustive), and $A \succ B$ given $E_i$ for all $i$, then $A \succ B$ unconditionally.

**Crucial Condition:** The events used for conditioning must form a **proper partition**. This means:
1.  **Mutuall

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that the Sure Thing Principle (STP) requires a proper partition and demonstrates that the conditioning events ('at least one H' and 'at least one T') overlap on the losing outcomes {HT, TH}. They explicitly state that the events are not mutually exclusive, which is t

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Are you a one-boxer or a two-boxer? Whatever you choose, you must defend your reasoning against the strongest version of the opposing argument. What principle are you relying on, and what are you giving up?

**Expected Answer:** **Newcomb's Problem** — Newcomb's Problem pits Dominance against Expected Utility when states are correlated with acts. Causal Decision Theory (CDT) says: the Predictor's choice is fixed, so taking both dominates (you are 1,000 gold richer regardless). Evidential Decision Theory (EDT) says: one-boxing provides strong evide

**Model Response:**
> I am a **one-boxer**.

My choice is to take **only Box A**.

Below is the step-by-step defense of this reasoning, the confrontation with the opposing view, and an analysis of the underlying principles and cognitive patterns at play.

### 1. The Core Reasoning: Evidential Decision Theory
My decision relies on **Evidential Decision Theory (EDT)**. The logic is as follows:

1.  **The Correlation:** There is an extremely strong statistical correlation (99%) between the action of "taking only Box A" and the state of "Box A containing 1,000,000 gold."
2.  **The Evidence:** By choosing to take only Box A, I provide strong *evidence* that the Predictor predicted I would do so.
3.  **The Outcome:** Since the Predictor is almost infallible, my choice to one-box makes it highly probable that the mill

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Newcomb's Problem and articulates both sides of the dilemma with high clarity: the Evidential Decision Theory (EDT) argument for one-boxing (maximizing expected utility based on correlation) and the Causal Decision Theory (CDT) argument for two-boxing 

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The dealer says choosing G1 and G4 is inconsistent. Can you see why? What probability would you need to assign to Black to justify G1 over G2? And what probability would you need for G4 over G3? Can both be true?

**Expected Answer:** **Ellsberg Paradox (Ambiguity Aversion)** — The Ellsberg Paradox shows that people prefer known risk (Red: exactly 1/3) over ambiguous risk (Black: unknown proportion). Preferring G1>G2 implies P(Black)<1/3. Preferring G4>G3 implies P(Black)>1/3 (because Yellow cancels out as common consequence). These two implications are contradictory — no 

**Model Response:**
> This scenario is a classic illustration of the **Ellsberg Paradox**, which demonstrates a fundamental conflict between human intuition and the axioms of rational choice theory (specifically, Expected Utility Theory).

Here is the step-by-step logical breakdown of why the dealer is correct in calling the combination of choices inconsistent.

### Step 1: Analyze the Known Probabilities
First, let's establish the mathematical facts provided in the urn:
*   **Total balls:** 90
*   **Red balls ($R$):** 30
*   **Black ($B$) + Yellow ($Y$) balls:** 60
*   **Probability of Red:** $P(R) = \frac{30}{90} = \frac{1}{3}$
*   **Probability of Black or Yellow:** $P(B \cup Y) = \frac{60}{90} = \frac{2}{3}$
*   **Unknown:** The specific split between Black and Yellow. Let $P(B) = x$. Consequently, $P(Y) = 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Ellsberg Paradox and provides a rigorous mathematical derivation showing that G1>G2 implies P(Black)<1/3 while G4>G3 implies P(Black)>1/3, explicitly highlighting the contradiction. Furthermore, the response correctly identifies 'Ambiguity Aversion' as the psycho

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The expected values are the same within each pair, yet the merchants' risk preferences flip. What does this tell you about the shape of the human utility function? Can a single curve explain both patterns?

**Expected Answer:** **Reflection Effect** — The Reflection Effect shows that people are risk-averse when choosing among gains (prefer sure $500 over 50/50 shot at $1000) but risk-seeking when choosing among losses (prefer 50/50 shot at losing $1000 over sure loss of $500). Under MEU, a utility function is either consistently concave (always r

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the merchants' behavior and what it reveals about human decision-making.

### Step 1: Analyze the Expected Value (EV)
First, let's verify Lira's claim that the expected values are identical within each pair.

*   **Problem 1 (Gain Domain):**
    *   Option A: $500 \times 100\% = 500$ gold.
    *   Option B: $(1,000 \times 0.5) + (0 \times 0.5) = 500$ gold.
    *   *Result:* EV is equal. Merchants choose the **sure thing** (Risk Averse).

*   **Problem 2 (Loss Domain):**
    *   Option C: $-500 \times 100\% = -500$ gold.
    *   Option D: $(-1,000 \times 0.5) + (0 \times 0.5) = -500$ gold.
    *   *Result:* EV is equal. Merchants choose the **gamble** (Risk Seeking).

### Step 2: Evaluate the Standard Utility Model (MEU)
T

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Reflection Effect (though they also mention Framing Effect in the conclusion). They explicitly explain that a single consistent utility function under MEU cannot account for the flip between risk aversion in gains and risk seeking in losses. They accurately descr

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** You reject the bet when you know at least one is heads, and you reject when you know at least one is tails. One of these must be true. So why should you accept unconditionally? Where is the flaw in reasoning from conditionals to the unconditional?

**Expected Answer:** **Disjunction Effect** — The Disjunction Effect occurs when an agent rejects an option conditional on each member of a non-exclusive partition but should accept it unconditionally. The resolution: 'at least one H' and 'at least one T' overlap on {HT, TH} — the losing outcomes. Conditioning on either event eliminates one win

**Model Response:**
> This scenario presents a classic probability paradox often referred to as the **Two-Child Paradox** or a variation of the **Boy or Girl Paradox**, specifically highlighting the difference between **unconditional probability** and **conditional probability based on specific information revelation**.

Here is the step-by-step breakdown of the reasoning and the identification of the flaw.

### 1. Analyzing the Unconditional Case
First, let's verify Voss's initial calculation.
*   **Sample Space:** $\{HH, HT, TH, TT\}$ (4 equally likely outcomes).
*   **Winning Condition:** Match ($HH$ or $TT$).
*   **Losing Condition:** Mismatch ($HT$ or $TH$).
*   **Probabilities:**
    *   $P(\text{Win}) = P(HH) + P(TT) = 1/4 + 1/4 = 1/2$.
    *   $P(\text{Lose}) = P(HT) + P(TH) = 1/4 + 1/4 = 1/2$.
*   **Ex

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the sample space overlap on {HT, TH} and calculates the conditional probabilities accurately. However, the response fails to connect this overlap to the specific mechanism of the Disjunction Effect (i.e., that conditioning on non-exclusive events eliminates a winning

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Three traders received the same bonus but feel differently. Standard economic theory says Basil should be happiest (highest wealth). What is actually determining their reactions, and what does standard theory miss?

**Expected Answer:** **Reference points** — Under Prospect Theory, outcomes are evaluated as gains or losses relative to a reference point — typically the status quo, an expectation, or an aspiration level. The same objective outcome can feel like a gain or a loss depending on the reference point. Cara's 5,000 gold bonus is objectively a gain

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning pattern and the economic principle at play.

### Step-by-Step Deduction

1.  **Analyze the Standard Economic Prediction:**
    *   **Premise:** Standard neoclassical economic theory (specifically the concept of *utility*) often assumes that an individual's happiness or satisfaction is derived from their **total wealth** (absolute level of consumption).
    *   **Application:** If happiness is a function of total wealth ($W$), then:
        *   Anika's total wealth is lower than Basil's.
        *   Basil's total wealth is the highest ($100,000 + 5,000$).
        *   Therefore, standard theory predicts Basil should derive the most utility and be the happiest.
    *   **Observation:** The scenario explicitly s

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Reference Dependence' and 'Prospect Theory' as the core principles. They explicitly explain that Cara experiences a psychological loss despite an objective gain due to her expectation serving as the reference point. The response also connects this to loss aversion (

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Lira's patrons demand 40-50 gold to accept a bet that could lose them 20. Risk aversion explains some of this, but not all. What additional psychological mechanism is at work, and how does it show up in the shape of the value function?

**Expected Answer:** **Loss aversion** — Loss aversion means that losses are felt more intensely than equivalent gains. Formally, the value function is steeper below the reference point than above it: |v(-x)| > v(x) for x > 0. The empirical coefficient is approximately lambda = 2.25, meaning losing $100 hurts as much as gaining $225 feels 

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the psychological mechanism at work and its representation in the value function.

### Step 1: Analyzing the Discrepancy
The scenario presents a classic decision-making problem.
*   **The Bet:** A 50/50 chance to lose 20 gold or gain $X$ gold.
*   **Mathematical Expectation:** For the bet to be "fair" (expected value = 0), $X$ must equal 20.
*   **Risk-Neutral Behavior:** A rational agent who only cares about the final wealth amount would accept any $X > 20$.
*   **Risk-Averse Behavior:** A standard risk-averse agent (concave utility function) would demand a premium, perhaps $X = 22$ or $25$, to compensate for the variance.
*   **Observed Behavior:** The patrons demand $X = 40$ to $50$. This implies they view the potentia

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies loss aversion as the core mechanism and explicitly distinguishes it from standard risk aversion (concavity). They accurately describe the S-shaped value function with a kink at the reference point, noting the steeper slope in the loss domain. Furthermore, they correc

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weighting resolve the contradiction?

**Expected Answer:** **Probability weighting function** — In Prospect Theory, objective probabilities are transformed by a weighting function pi(p) before being used in calculations. Small probabilities are overweighted (pi(0.01) > 0.01), large probabilities are underweighted (pi(0.99) < 0.99), and the endpoints 0 and 1 are treated categorically. The resul

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of how probability weighting resolves the apparent contradiction between buying lottery tickets and insurance.

### Step-by-Step Deduction

**1. The MEU (Maximum Expected Utility) Baseline**
Under standard Expected Utility theory, a rational agent evaluates a gamble by multiplying the utility of the outcome by its objective probability ($P$).
*   **Lottery:** If a ticket costs \$2 and has a 1% chance to win \$100, the expected value is $0.01 \times 100 = \$1$. Since \$1 < \$2, a rational MEU agent should **not** buy it (negative expected value).
*   **Insurance:** If a policy costs \$50 to cover a 1% chance of a \$1,000 loss, the expected loss is $0.01 \times 1000 = \$10$. Since \$50 > \$10, a rational MEU agent should **not

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Probability Weighting within Prospect Theory. They accurately explain the inverse-S shape (overweighting small probabilities, underweighting large ones) and explicitly mention the Certainty Effect regarding the 99% to 100% leap. Furthermore, they succe

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** Lira says the same person can rationally buy lottery tickets and insurance. Under MEU, this is a contradiction. How do the value function and probability weighting function together produce four distinct risk profiles?

**Expected Answer:** **Fourfold Pattern of risk attitudes** — The Fourfold Pattern emerges from combining: (1) The S-shaped value function (risk-averse for gains, risk-seeking for losses) with (2) The probability weighting function (overweight small p, underweight large p). Low-probability gains: overweighting makes the prize loom large → risk seeking. Low-pro

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning pattern and the mechanism behind the Fourfold Pattern.

### Step-by-Step Deduction

**1. The Conflict: Expected Utility (MEU) vs. Observed Behavior**
Under **Maximizing Expected Utility (MEU)**, an individual's risk attitude is determined solely by the curvature of their utility function ($U$).
*   If $U$ is concave (diminishing marginal utility), the person is **risk-averse** in all domains.
*   If $U$ is convex (increasing marginal utility), the person is **risk-seeking** in all domains.
*   **The Contradiction:** MEU cannot explain why a single person would be risk-averse when buying insurance (paying a premium to avoid a small loss) *and* risk-seeking when buying a lottery ticket (paying a small amount f

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Fourfold Pattern and explicitly details both underlying mechanisms: the S-shaped value function and the probability weighting function. They provide clear examples for all four quadrants (lottery, insurance, etc.) and effectively contrast this with Expected Utili

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** The councillors in Group A and Group B made opposite choices about the same programs. What changed between the two presentations, and why does it matter for rational decision-making?

**Expected Answer:** **Framing effects** — Framing effects occur when logically equivalent descriptions of the same situation lead to different decisions because they shift the reference point. A gains frame activates risk aversion (prefer the sure outcome). A losses frame activates risk seeking (prefer the gamble). Since the underlying opti

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning pattern, the specific bias at play, and why it matters for rational decision-making.

### Step 1: Analyze the Mathematical Equivalence
First, we must verify the scribe's claim that the programs are identical. Let's break down the expected outcomes for both groups:

*   **Group A (Gains Frame):**
    *   **Program A:** 200 saved. (Implies 400 die, since $600 - 200 = 400$).
    *   **Program B:** 1/3 chance 600 saved (0 die); 2/3 chance 0 saved (600 die).
    *   *Expected Value:* $(1/3 \times 600) + (2/3 \times 0) = 200$ saved.

*   **Group B (Losses Frame):**
    *   **Program C:** 400 die. (Implies 200 saved, since $600 - 400 = 200$).
    *   **Program D:** 1/3 chance 0 die (600 saved); 2/3 chance 600 die.


**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Framing Effect and explains the mechanism clearly: risk aversion in the domain of gains and risk seeking in the domain of losses, explicitly connecting these to the reference point (lives saved vs. lives lost). They also correctly note the violation of the Invari

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Alec and Brin have the same amount of money and face the same bet, but they make opposite choices. What psychological mechanism explains the difference? Is Brin being rational or irrational?

**Expected Answer:** **Mental accounting** — Mental accounting (Thaler) is the tendency to treat money differently depending on which psychological 'account' it belongs to — savings, winnings, salary, found money, etc. Standard economics says money is fungible: a dollar is a dollar regardless of its source. Mental accounting violates fungibili

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the psychological mechanisms at play and the evaluation of Brin's rationality.

### Step 1: Analyze the Economic Reality vs. Psychological Reality
From a purely mathematical and economic standpoint (the "rational agent" model), Alec and Brin are in identical situations:
*   **Current Wealth:** Both have 200 gold.
*   **The Bet:** A 50/50 chance to gain 200 gold (total 400) or lose 200 gold (total 0).
*   **Expected Value (EV):** $(0.5 \times 400) + (0.5 \times 0) = 200$.
*   **Conclusion:** Mathematically, the bet is "fair" (EV equals current wealth). A strictly rational actor should be indifferent between keeping the 200 gold or taking the bet, assuming they are risk-neutral.

However, the scenario shows they are **not**

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Mental Accounting and the House Money Effect. They explicitly explain the violation of fungibility (money is interchangeable regardless of source) which covers Level 3. Furthermore, they address both sides of the argument: noting the behavior is irrational from a str

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Sellers demand 7 gold and buyers offer 3 gold for the same mug. The mugs were randomly assigned. What psychological mechanism creates this gap, and why does standard economic theory have trouble explaining it?

**Expected Answer:** **Endowment effect** — The endowment effect is the observation that people demand more to give up an object they own than they would pay to acquire the same object. Sellers set a higher price (WTA: willingness to accept) than buyers (WTP: willingness to pay), even for identical items. The mechanism is loss aversion: once 

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the psychological mechanism and the economic discrepancy at play.

### Step 1: Analyze the Experimental Setup
The scenario describes a classic controlled experiment in behavioral economics.
*   **The Object:** A standard ceramic mug (identical value to all participants).
*   **The Assignment:** Random. This is crucial because it eliminates "selection bias" (e.g., people who love mugs getting them). The only difference between the two groups is that one group *owns* the mug, and the other does not.
*   **The Data:**
    *   Sellers (Owners) Minimum Acceptance Price (WTA): 7 gold.
    *   Buyers (Non-owners) Maximum Willingness to Pay (WTP): 3 gold.
*   **The Discrepancy:** A 4-gold gap where the owner values the item more 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Endowment Effect and explains the underlying mechanism of loss aversion, explicitly contrasting the pain of losing (for sellers) with the pleasure of gaining (for buyers) and noting the reference point shift. They also correctly identify the resulting market inef

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Darya insists on going skiing because she paid 300 gold. Her friend says the money is gone either way. Who is right, and what error is Darya making?

**Expected Answer:** **Sunk cost fallacy** — The sunk cost fallacy is the tendency to continue an activity because of past investment (time, money, effort) rather than future expected value. Under MEU, sunk costs are decision-irrelevant: only future costs and benefits should affect current choices. The fallacy arises from mental accounting — t

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the situation, the identification of the error, and the final conclusion.

### Step-by-Step Analysis

1.  **Analyze the Financial Reality**:
    *   Darya has already spent **300 gold**.
    *   The ticket is **non-refundable**.
    *   This means the 300 gold is a **sunk cost**. It has left her possession and cannot be recovered regardless of her decision.
    *   **Option A (Go Skiing):** She spends the weekend feeling ill on the slopes. The financial outcome is: -300 gold (already spent) + physical misery.
    *   **Option B (Stay at Cabin):** She spends the weekend resting in a free cabin. The financial outcome is: -300 gold (already spent) + physical comfort.

2.  **Evaluate Darya's Reasoning**:
    *   Darya argues:

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Sunk Cost Fallacy and provides a clear explanation that only future costs and benefits (marginal utility) should drive the decision, noting that the 300 gold is irrecoverable in both scenarios. However, the response does not reach Level 4 because it fails to conn

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Mirella knows holding back would be better for both, yet she strips the grove anyway. What structural feature of her situation makes cooperation so difficult?

**Expected Answer:** **Prisoner's Dilemma** — A symmetric 2-player game where individual rationality (dominant strategy D) leads both players to an outcome strictly worse than mutual cooperation. The unique Nash equilibrium is (D,D), yet (C,C) Pareto-dominates it.

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Mirella's situation and the underlying structural feature at play.

### Step-by-Step Analysis

1.  **Analyze the Payoff Structure**:
    *   **Mutual Cooperation (Both hold back)**: Both brewers get **3 gold**. This is the optimal collective outcome.
    *   **Mutual Defection (Both strip bare)**: Both brewers get **1 gold**. This is the current reality and a suboptimal outcome.
    *   **Unilateral Cooperation (One holds back, one defects)**: The defector gets everything (implied to be high, likely >3), while the cooperator gets nothing or very little (implied to be <1). Mirella explicitly fears becoming a "fool" in this scenario.

2.  **Analyze Mirella's Reasoning**:
    *   Mirella acknowledges that 3 gold is better th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a Prisoner's Dilemma and provides a clear explanation of dominant strategies and the resulting Nash Equilibrium at (D,D). They also explicitly note that mutual cooperation (C,C) yields a superior outcome. However, the response does not reach Level 4 be

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks you to find the Nash Equilibrium. For each strategy pair, check: could either cadet do better by switching alone? Which pair survives this test?

**Expected Answer:** **Nash equilibrium** — A Nash Equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. In the PD above, (Fortify, Fortify) is the unique Nash Equilibrium: if A plays Fortify and B plays Fortify, A gets 1. If A switches to Patrol, A gets 0 (worse). Symmetrically fo

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis to find the Nash Equilibrium and the identification of the underlying reasoning principle.

### Step 1: Analyze the Payoff Matrix
Let's break down the incentives for each cadet based on the matrix provided:

| | **Cadet B: Patrol** | **Cadet B: Fortify** |
| :--- | :---: | :---: |
| **Cadet A: Patrol** | (3, 3) | (0, 5) |
| **Cadet A: Fortify** | (5, 0) | (1, 1) |

*   **First number** = Payoff for Cadet A.
*   **Second number** = Payoff for Cadet B.

### Step 2: Determine Best Responses (Unilateral Deviation Test)

**For Cadet A:**
*   **If Cadet B chooses Patrol:** Cadet A compares getting **3** (Patrol) vs. **5** (Fortify).
    *   *Decision:* Fortify is better ($5 > 3$).
*   **If Cadet B chooses Fortify:** Cadet A compar

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies (Fortify, Fortify) as the unique Nash Equilibrium and rigorously demonstrates the unilateral deviation test for all cells. Crucially, the response explicitly explains why (Patrol, Patrol) is not an equilibrium by quantifying the gain from deviating (getting 5 instead

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?

**Expected Answer:** **Iterated PD and cooperation** — In a finitely repeated PD with known endpoint, backward induction predicts defection every round. But in an infinitely repeated PD (or one with unknown endpoint), the Folk Theorem shows that cooperation can be sustained as a Nash Equilibrium if players value future payoffs enough (discount factor de

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the game theory concepts, followed by the identification of the underlying reasoning pattern.

### Step-by-Step Analysis

**1. What changes when the game is repeated?**
In a **one-shot Prisoner's Dilemma (PD)**, the dominant strategy is to **Defect**. This is because there is no future consequence; regardless of what the opponent does, you gain a higher immediate payoff by defecting. The Nash Equilibrium is (Defect, Defect), leading to a suboptimal outcome for both.

However, in a **repeated PD with an unknown end date**, the logic shifts due to the **Shadow of the Future**.
*   Players now care about future payoffs.
*   Defecting today might yield a short-term gain, but it risks triggering a cycle of mutual retaliation i

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Shadow of the Future' as the mechanism for cooperation and accurately details Tit-for-Tat's four key properties (Nice, Retaliatory, Forgiving, Clear). They also successfully address the edge case of noise/errors, which is a critical nuance. However, the response

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find both Nash Equilibria in the Stag Hunt. Which is payoff-dominant? Which is risk-dominant? Which would you choose, and what does your choice depend on?

**Expected Answer:** **Stag Hunt** — The Stag Hunt (from Rousseau) has two pure-strategy Nash Equilibria: (Stag, Stag) = (5,5) and (Hare, Hare) = (2,2). (Stag, Stag) is payoff-dominant (better for everyone). (Hare, Hare) is risk-dominant (safer — you get 2 guaranteed regardless of partner). The core tension: cooperation requires trust.

**Model Response:**
> ### Step-by-Step Analysis of the Stag Hunt Scenario

To answer your questions, we must first analyze the payoff matrix provided in the scenario to identify the strategic incentives for both players ("You" and the "Partner").

**The Payoff Matrix:**
*   **Stag, Stag:** (5, 5)
*   **Stag, Hare:** (0, 3)
*   **Hare, Stag:** (3, 0)
*   **Hare, Hare:** (2, 2)

#### 1. Finding the Nash Equilibria
A Nash Equilibrium occurs when neither player has an incentive to deviate from their chosen strategy, assuming the other player's strategy remains constant. Let's test each cell:

*   **Case A: (Stag, Stag) $\rightarrow$ Payoffs (5, 5)**
    *   If "You" switch to Hare while the Partner stays on Stag: Your payoff changes from 5 to 3. (You lose).
    *   If the Partner switches to Hare while you stay on 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies both Nash Equilibria ((Stag, Stag) and (Hare, Hare)) and accurately distinguishes between payoff-dominance (Stag) and risk-dominance (Hare). They provide a clear explanation of the trust/coordination tension, noting that choosing Stag requires confidence in the partn

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find all Nash Equilibria in this game, including any mixed-strategy equilibrium. Why is the mixed equilibrium worse for both players than either pure equilibrium?

**Expected Answer:** **Battle of the Sexes** — Battle of the Sexes has two pure-strategy Nash Equilibria: (Opera, Opera) = (3,2) and (Tournament, Tournament) = (2,3). Both are coordination equilibria — both players prefer being together over being apart. But they disagree on which is better: Helena prefers (Opera, Opera), Roderick prefers (Tourn

**Model Response:**
> ### Step 1: Analyze the Payoff Matrix and Pure Strategy Nash Equilibria

First, let's formalize the game based on the provided matrix. The numbers represent payoffs in the format $(Helena, Roderick)$.

| | Roderick: Opera | Roderick: Tournament |
| :--- | :---: | :---: |
| **Helena: Opera** | $3, 2$ | $0, 0$ |
| **Helena: Tournament** | $0, 0$ | $2, 3$ |

**Definition of Nash Equilibrium (NE):** A set of strategies where no player can unilaterally deviate to improve their payoff.

**Checking Pure Strategies:**

1.  **Cell (Opera, Opera):** Payoffs $(3, 2)$.
    *   If Helena deviates to Tournament, she gets $0$ (worse than $3$).
    *   If Roderick deviates to Tournament, he gets $0$ (worse than $2$).
    *   **Result:** Neither wants to deviate. **$(Opera, Opera)$ is a Nash Equilibrium.**

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identified both pure-strategy Nash Equilibria and accurately calculated the mixed-strategy equilibrium probabilities and expected payoffs (1.2 each). They explicitly noted that the mixed equilibrium yields lower payoffs than the pure equilibria due to miscoordination risks. How

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** You and your contact must meet without communication. Why do people converge on the same location and time? What property makes some answers more likely than others, and is this a rational process?

**Expected Answer:** **Focal points (Schelling points)** — A focal point is a solution to a coordination game that attracts players' attention because it is salient — prominent, unique, culturally significant, or symmetric. Focal points work because of mutual expectations: I go to the fountain because I expect you to expect me to expect... etc. Sources of s

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning pattern, the underlying principle, and the nature of the decision-making process.

### 1. Identification of the Principle
The scenario demonstrates **Schelling's Focal Point** (also known as a **Schelling Point**).

Named after Nobel laureate Thomas Schelling, this concept arises in game theory when two or more people must coordinate their actions without communication. Since there is no way to negotiate, they must rely on a shared expectation of what the other person will do. The "focal point" is the solution that stands out as the most natural, special, or distinctive choice to all parties involved.

### 2. Analysis of the Reasoning Pattern
The reasoning pattern at play is **recursive reasoning based on co

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Schelling's Focal Point and provides a clear explanation of salience and the recursive mutual-expectation mechanism ('I think you think I think...'). They also list sources of salience (uniqueness, cultural significance). However, the response does not

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid.

**Expected Answer:** **Convention (Lewis)** — A convention is a regularity R in behavior that is (1) followed by everyone, (2) expected by everyone, (3) preferred by everyone given others' conformity, (4) has at least one alternative R' that could have served instead, and (5) is common knowledge. Conventions are solutions to recurrent coordinat

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the philosopher's argument, the technical application of David Lewis's conditions, and the identification of the underlying reasoning pattern.

### 1. Technical Meaning of "Convention"
In this context, a **convention** is not a law, a moral imperative, or a result of superior engineering. Technically, it is a **solution to a coordination problem** that arises from a state of **equilibrium**.

A convention exists when a group of people repeatedly faces a situation where they must coordinate their actions to avoid a bad outcome (like a head-on collision), and there are multiple possible solutions that work equally well. Once a specific solution is adopted, it becomes self-reinforcing because every individual's best strategy

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies all five of Lewis's conditions, explicitly explains the arbitrariness and functional equivalence of driving on the left, and demonstrates a deep understanding of the self-reinforcing expectation structure (Nash Equilibrium). Furthermore, the response exceeds Level 3 

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor has drawn the Entry Game tree. Identify the decision nodes, the branches, and the terminal payoffs. What information does each player have when they move?

**Expected Answer:** **Game trees (extensive form)** — A game tree represents a sequential game with nodes (decision points), branches (available actions), terminal nodes (outcomes with payoffs), and information sets (what each player knows when they move). Unlike the normal form (matrix), the extensive form explicitly represents the order of moves, whi

**Model Response:**
> ### Step-by-Step Analysis of the Scenario

To answer your request, we must first break down the game structure described in the scenario and then analyze the cognitive or theoretical principles at play.

#### 1. Structural Breakdown of the Game Tree

Based on the instructor's description, here are the specific components of the extensive form game:

*   **Decision Nodes:** These are the points in the tree where a player must make a choice.
    *   **Node 1 (Root):** The **Entrant** moves first. They have two options: *Enter* or *Stay Out*.
    *   **Node 2:** The **Incumbent** moves only if the Entrant chose *Enter*. They have two options: *Accommodate* or *Fight*.
    *   *Note:* If the Entrant chooses *Stay Out*, the game ends immediately; there is no decision node for the Incumbent in t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the game tree structure, including all decision nodes, branches, and payoffs. They explicitly recognize the perfect information structure where the Incumbent observes the Entrant's move. Furthermore, the student successfully applies backward induction to predict the 

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** Apply backward induction to the Entry Game. Start at the last decision node and work backward. What is the subgame perfect equilibrium? Why is the Incumbent's threat to Fight not credible?

**Expected Answer:** **Backward induction** — Backward induction solves extensive-form games by starting at the terminal nodes and working backward. At each decision node, the player is assumed to choose their optimal action. The resulting strategy profile is a subgame perfect equilibrium (SPE). In the Entry Game: (1) At Incumbent's node: Accom

**Model Response:**
> Based on the scenario provided, here is the step-by-step application of backward induction, the identification of the equilibrium, and an analysis of the underlying reasoning principles.

### Step-by-Step Backward Induction

Backward induction is a method used to solve finite sequential games by analyzing the game from the final decision point back to the start.

**1. Analyze the Final Decision Node (The Incumbent's Move)**
*   **Context:** The Entrant has already chosen to **Enter**.
*   **Choices:** The Incumbent must choose between **Accommodate** or **Fight**.
*   **Payoffs:**
    *   If Accommodate: Payoff = **2**.
    *   If Fight: Payoff = **0**.
*   **Rational Choice:** A rational player maximizes their own payoff. Since $2 > 0$, the Incumbent will choose **Accommodate**.
*   **Res

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly applies backward induction starting from the Incumbent's node, identifies the correct SPE (Enter, Accommodate), and explicitly explains why the alternative (Stay Out, Fight) involves a non-credible threat. The response goes beyond Level 3 by articulating the concepts of credibi

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The Entry Game has two Nash Equilibria. The instructor says one of them relies on a non-credible threat. Which one, and why does SPE eliminate it?

**Expected Answer:** **Subgame perfect equilibrium** — SPE (Selten 1965) requires that a strategy profile be a Nash Equilibrium in every subgame. A subgame is any part of the game tree that forms a complete game on its own. SPE eliminates NE that rely on non-credible threats — strategies that would not be followed through if the relevant decision node w

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis and the final answer.

### Step-by-Step Deduction

**1. Analyze the Two Nash Equilibria (NE)**
The scenario identifies two Nash Equilibria in the Entry Game:
*   **NE 1: (Enter, Accommodate)** with payoffs (2, 2).
    *   If the Entrant enters, the Incumbent accommodates (payoff 2) rather than fights (payoff 0).
    *   If the Incumbent accommodates, the Entrant prefers entering (2) over staying out (0).
    *   *Result:* Neither player wants to deviate. This is a stable outcome.
*   **NE 2: (Stay Out, Fight)** with implied payoffs where the Entrant gets 0 (by staying out) and the Incumbent gets a higher payoff (e.g., 3) by maintaining a monopoly because the Entrant never enters.
    *   The logic here is: The Entrant stays 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the non-credible threat in the (Stay Out, Fight) equilibrium, explains that SPE requires optimality at every decision node (subgame), and correctly identifies (Enter, Accommodate) as the unique SPE. They also explicitly mention Backward Induction. However, the respon

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Question:** Apply backward induction to the Centipede Game. What does it predict? Do you find the prediction convincing? What assumption is doing the heavy lifting, and what happens if you relax it?

**Expected Answer:** **Centipede Game** — The Centipede Game is a sequential game where two players alternate between stopping (taking a smaller immediate payoff) and continuing (allowing the total payoff to grow). Backward induction predicts immediate stopping — the unique SPE. But this is paradoxical: both players would be much better off

**Model Response:**
> ### Step-by-Step Analysis of the Centipede Game

To answer your question, we must first rigorously apply the logic of **backward induction** to the specific game tree provided, then evaluate the validity of the result, and finally identify the underlying assumptions and cognitive patterns at play.

#### 1. Application of Backward Induction
Backward induction is a method of solving sequential games by starting at the final decision node and working backward to the beginning. The core premise is that every player is perfectly rational and knows that all future players are also perfectly rational.

Let's trace the logic node by node, starting from the end:

*   **Node 4 (Player 2's turn):**
    *   **Options:** Stop $\rightarrow$ Payoff (2, **5**); Continue $\rightarrow$ Payoff (4, **4**).
  

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly applies backward induction step-by-step to reach the unique Subgame Perfect Equilibrium (stop at Node 1). They clearly identify the paradox by contrasting the BI prediction (1,1) with the mutually beneficial outcome (4,4) and experimental reality. Crucially, they correctly iden

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

**Expected Answer:** **Evolutionarily Stable Strategy (ESS)** — An ESS (Maynard Smith) is a strategy that, when adopted by almost all members of a population, cannot be invaded by any rare mutant strategy. Formally: S is ESS if for any mutant M, either (1) E(S,S) > E(M,S), or (2) E(S,S) = E(M,S) and E(S,M) > E(M,M). In Hawk-Dove with V<C, neither pure strategy i

**Model Response:**
> Based on the scenario and the game theory principles applied, here is the step-by-step analysis, the solution to the specific question, and the identification of the underlying reasoning pattern.

### Step 1: Verification of Pure Strategies

To determine if a strategy is an Evolutionarily Stable Strategy (ESS), we must check two conditions. Let $E(S_1, S_2)$ be the payoff to strategy $S_1$ when playing against $S_2$. A strategy $S$ is an ESS if for any mutant strategy $M \neq S$:
1.  $E(S, S) > E(M, S)$ (Strict Nash Equilibrium), OR
2.  $E(S, S) = E(M, S)$ AND $E(S, M) > E(M, M)$.

**Checking Pure Hawk:**
*   **Payoff Matrix:**
    *   $E(\text{Hawk}, \text{Hawk}) = (V-C)/2 = (4-6)/2 = -1$
    *   $E(\text{Dove}, \text{Hawk}) = 0$
*   **Analysis:** If the population is all Hawks, a rare Do

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly verifies that neither pure strategy is an ESS and accurately calculates the mixed ESS proportion (p=2/3). They also begin to explain the population-level interpretation (polymorphism vs. individual mixing). However, the response is cut off mid-sentence at the end, failing to co

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The biologist perturbs the Hawk population from 50% to 51%. Show that the system returns to 50% by calculating fitness for each strategy. What does this tell you about the stability of the mixed ESS?

**Expected Answer:** **Replicator dynamics** — The replicator dynamics models how strategy frequencies change over time based on fitness. The equation dx_i/dt = x_i(f_i - F) says: strategies that outperform average grow; those that underperform shrink. Key properties: (1) ESS are stable fixed points of replicator dynamics. (2) Not all fixed poin

**Model Response:**
> ### Step-by-Step Calculation and Analysis

To answer the question, we must first verify the mathematical logic presented in the scenario using the standard Hawk-Dove payoff matrix and the specific population frequencies provided.

**1. Define the Parameters**
*   **Value of Resource ($V$):** 2
*   **Cost of Injury ($C$):** 4
*   **Payoff Matrix:**
    *   $E(H, H) = \frac{V-C}{2} = \frac{2-4}{2} = -1$
    *   $E(H, D) = V = 2$
    *   $E(D, H) = 0$
    *   $E(D, D) = \frac{V}{2} = 1$

**2. Analyze the Equilibrium State (50% Hawks)**
Let $x$ be the frequency of Hawks. At equilibrium, $x = 0.5$.
*   **Frequency of Hawks ($x$):** 0.5
*   **Frequency of Doves ($1-x$):** 0.5

Calculate Expected Fitness ($E$):
*   $E(H) = x \cdot E(H,H) + (1-x) \cdot E(H,D)$
    $$E(H) = 0.5(-1) + 0.5(2) = -0.5 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly computes fitness for both strategies at equilibrium and under perturbation (51% Hawks), demonstrating that Doves outperform Hawks. They explicitly apply the replicator dynamics logic to show the system returns to equilibrium, confirming stability. Furthermore, they identify the

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In the evolutionary Stag Hunt, what determines whether cooperation or defection wins? Why does Skyrms call the cooperative equilibrium a 'social contract'? What factors help cooperation evolve?

**Expected Answer:** **Evolution of cooperation** — In evolutionary Stag Hunt, cooperation (Stag) can evolve if enough of the population already cooperates. The threshold is p=0.5 in standard payoffs. Above the threshold, cooperation is self-reinforcing; below, it collapses. This is the basin of attraction concept. Factors that help cooperation evolv

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the evolutionary dynamics, the meaning of the "social contract," and the underlying reasoning principles.

### 1. What determines whether cooperation or defection wins?

In the evolutionary Stag Hunt described, the outcome is determined by **initial conditions** and the resulting **path dependence**.

*   **The Threshold:** The biologist calculates a critical tipping point at $p = 0.5$ (50% of the population).
    *   If the proportion of Stag-hunters ($p$) is **greater than 0.5**, the expected payoff for hunting Stag ($5p$) exceeds that of hunting Hare ($p+2$). In this scenario, the "cooperation" strategy yields higher fitness, causing it to spread until the entire population hunts Stag.
    *   If the proportion of Stag

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly calculates the threshold (p=0.5), explicitly explains the concept of basins of attraction through path dependence and initial conditions, and discusses multiple factors promoting cooperation (assortative matching, network structure). Furthermore, the response accurately connect

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Torva says her profit from the sword is eighty gold. Is she right? What is she forgetting to account for?

**Expected Answer:** **Opportunity cost** — The opportunity cost of an action is the value of the next-best alternative forgone. Torva treats the sword's revenue (80 gold) as pure profit, but by choosing the sword she forgoes the 50-gold axle repair. Her net gain from choosing the sword over the axle is 80 - 50 = 30 gold, not 80 gold. The 50 

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyzing Torva's Calculation**
Torva states: "The sword pays eighty, so that's my profit, right? Eighty gold."
*   **Revenue:** 80 gold (from the knight).
*   **Calculated Profit:** 80 gold.
*   **Implicit Assumption:** She assumes that the cost of materials and labor is zero or negligible, or she is confusing "Revenue" (total income) with "Profit" (income minus expenses).

**2. Identifying the Missing Factors**
To determine if she is right, we must look at what is required to fulfill the commission:
*   **Material Costs:** A "longsword" made of "good steel" requires raw materials (steel, leather for the hilt, etc.). These materials cost money. If the steel costs 20 gold, her actual profit is $80 - 20 = 60$ gold.
*   **Opportunity Cost:** This is the most c

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core concept of Opportunity Cost, explicitly calculates the net gain (80 - 50 = 30 gold), and explains the mechanism of forgone alternatives. Furthermore, the response exceeds the Level 3 requirements by distinguishing between accounting profit and economic profi

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Hilde outproduces Oskar in both wheat and flax. She says trade cannot benefit her. Is she right? Calculate the opportunity costs and determine who should specialize in what.

**Expected Answer:** **Comparative advantage** — Hilde has absolute advantage in both goods, but comparative advantage depends on opportunity cost. Hilde's opportunity cost of 1 bolt of flax = 2 bushels of wheat (12/6). Oskar's opportunity cost of 1 bolt of flax = 4/3 bushels of wheat. Oskar has a lower opportunity cost for flax, so he has compara

**Model Response:**
> ### Step-by-Step Deduction

To determine if Hilde is correct, we must move beyond **Absolute Advantage** (who can produce more) and analyze **Comparative Advantage** (who gives up less to produce a specific good). Hilde's argument relies entirely on the fact that she is more efficient at everything, which is a common economic misconception.

#### 1. Calculate Opportunity Costs
The opportunity cost is what must be given up to produce one unit of a good.

**For Hilde:**
*   **Production:** 12 Wheat OR 6 Flax.
*   **Cost of 1 Wheat:** To get 12 Wheat, she gives up 6 Flax.
    *   $6 \text{ Flax} / 12 \text{ Wheat} = \mathbf{0.5 \text{ Flax}}$ per Wheat.
*   **Cost of 1 Flax:** To get 6 Flax, she gives up 12 Wheat.
    *   $12 \text{ Wheat} / 6 \text{ Flax} = \mathbf{2 \text{ Wheat}}$ per Flax

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Comparative Advantage), calculates all opportunity costs accurately, and correctly determines that Hilde has the comparative advantage in wheat while Oskar has it in flax. However, the response fails to reach Level 4 because the specific trade example pr

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?

**Expected Answer:** **Constrained optimization** — The problem is to minimize cost subject to constraints. Food constraint: 3R >= 15, so R >= 5 (minimum 5 ration packs). Torch constraint: 4T >= 8, so T >= 2 (minimum 2 torch bundles). Cost: 5R + 10T. Minimum cost = 5(5) + 10(2) = 25 + 20 = 45 gold. This satisfies both constraints and is within budget

**Model Response:**
> ### Step-by-Step Deduction

To determine the correct answer and the underlying reasoning pattern, we must first solve the mathematical optimization problem presented in the scenario, then analyze the cognitive process required to solve it.

#### 1. Mathematical Analysis of the Constraints
Let $R$ be the number of ration packs and $T$ be the number of torch bundles.

**Costs and Values:**
*   **Rations:** Cost = 5 gold, Value = 3 units of sustenance.
*   **Torches:** Cost = 10 gold, Value = 4 units of visibility.
*   **Budget:** 100 gold (Maximum).
*   **Goal:** Minimize Total Cost ($C$).

**Requirements (Constraints):**
1.  **Sustenance:** $3R \geq 15$
2.  **Visibility:** $4T \geq 8$
3.  **Budget:** $5R + 10T \leq 100$ (This is a constraint, but since we are minimizing cost, we will check 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the constraints, solves for the minimum integers (R=5, T=2), and calculates the correct cost (45 gold). They explicitly verify that all constraints are met and note the surplus budget (implicitly by contrasting 45 vs 100). Furthermore, they go beyond the basic calcul

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Each potion sells for 15 gold. The cost of each additional potion rises: 5, 8, 12, 16, 22. How many potions should Elara brew, and why?

**Expected Answer:** **Marginal analysis** — Marginal analysis compares the marginal benefit (MB) to the marginal cost (MC) of each additional unit. Brew if MB > MC; stop when MC >= MB. Revenue per potion (MB) = 15 gold. MC of potions: 1st=5, 2nd=8, 3rd=12, 4th=16, 5th=22. For potions 1-3, MB(15) > MC. For potion 4, MC(16) > MB(15). Elara shou

**Model Response:**
> To determine how many potions Elara should brew, we need to apply the economic principle of **marginal analysis**. The goal is to maximize profit, which occurs as long as the revenue generated by selling one more unit (Marginal Revenue) is greater than or equal to the cost of producing that specific unit (Marginal Cost).

Here is the step-by-step breakdown of the costs and revenues for each potion:

1.  **Potion #1:**
    *   **Marginal Cost (MC):** 5 gold
    *   **Marginal Revenue (MR):** 15 gold
    *   **Profit on this unit:** $15 - 5 = 10$ gold.
    *   *Decision:* Since $15 > 5$, she should brew this one.

2.  **Potion #2:**
    *   **Marginal Cost (MC):** 8 gold
    *   **Marginal Revenue (MR):** 15 gold
    *   **Profit on this unit:** $15 - 8 = 7$ gold.
    *   *Decision:* Since $

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the optimal quantity (3 potions) using marginal analysis. They explicitly compare MB and MC for each unit, explain why the 4th unit should be rejected, calculate the total profit (20 gold), and articulate the core principle that decisions are based on the next unit r

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Captain Hale says she should let the others pay for the lighthouse oil. Her reasoning seems logical from her own perspective. What happens if every captain follows the same logic? Why does this situation arise?

**Expected Answer:** **Public goods and free riding** — The lighthouse is a public good: non-rival (one captain using the light does not diminish it for others) and non-excludable (you cannot prevent a non-paying captain from seeing the light). These properties create a free-rider incentive: each captain benefits from the lighthouse regardless of whether

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the situation, the outcome, and the underlying principle at play.

### Step-by-Step Deduction

**1. Analyze the Individual Incentive (Captain Hale's Logic)**
Captain Hale's reasoning is based on **individual rationality**. She looks at the costs and benefits from her own narrow perspective:
*   **Cost of contributing:** 20 gold.
*   **Benefit of contributing:** The light stays on (which she gets regardless of whether she pays, provided others do).
*   **Benefit of not contributing:** She saves 20 gold while still enjoying the light if the others pay.
*   **Risk of not contributing:** If *no one* pays, the light goes out, and she risks losing her boat (500 gold).

However, in the immediate calculation, the risk of the ligh

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the scenario as a Prisoner's Dilemma and the Free Rider Problem. They explicitly define the lighthouse as a public good by citing both non-excludability and non-rivalry, and they clearly explain how individual rationality leads to collective failure. The response mee

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Elder Yara says every family is acting sensibly, yet the lake is dying. How can individual rationality produce collective disaster? What is the structural problem?

**Expected Answer:** **Commons problems (Tragedy of the commons)** — Lake Mirren is a common-pool resource: rival (each fish caught is unavailable to others) but non-excludable (no family can be prevented from fishing). Each family captures the full benefit of each additional fish they catch but bears only a fraction of the cost (resource depletion shared across all 

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the situation, the structural problem, and the underlying reasoning pattern.

### Step-by-Step Analysis

**1. Analysis of Individual Incentives (The "Rational" Choice)**
From the perspective of a single fishing family (e.g., Young Pell), the logic is straightforward:
*   **Scenario A (Cooperation):** If everyone sticks to the limit of 10 fish, the lake remains sustainable. However, if *I* stick to 10 while *others* increase their catch to 15 or 20, I lose out on immediate resources while they profit.
*   **Scenario B (Defection):** If I increase my catch to 25, I maximize my immediate income. Even if the lake eventually depletes, I have secured my "share" before it runs out.
*   **The Fear:** As Pell states, "if he doesn'

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the Tragedy of the Commons and explicitly connects it to Game Theory (Prisoner's Dilemma, Nash Equilibrium). They accurately explain the structural incentives: rivalry, non-excludability, and the asymmetry between privatized benefits and socialized cos

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Sera and Brenn create 80 gold in surplus from trade. Sera's outside option gives her 15 gold surplus; Brenn's gives him 10. How should they split the 80 gold surplus, and why?

**Expected Answer:** **Bargaining and fairness (Nash bargaining)** — The surplus from trade is 80 gold. Each merchant's outside option (BATNA) sets a floor: Sera will not accept less than 15 gold surplus (her alternative deal), and Brenn will not accept less than 10. The remaining surplus after securing both outside options is 80 - 15 - 10 = 55 gold. Nash bargaining 

**Model Response:**
> ### Step-by-Step Deduction

To determine the fair split of the 80 gold surplus, we must analyze the situation using **Game Theory**, specifically the concept of **Bargaining with Outside Options** (often modeled by the Nash Bargaining Solution).

**1. Identify the Total Surplus and the "Pie"**
The total value created by the specific trade between Sera and Brenn is **80 gold**.
*   Formula: $(Value_{Sera} - Cost_{Sera}) + (Value_{Brenn} - Cost_{Brenn}) = (70 - 40) + (80 - 30) = 30 + 50 = 80$.

**2. Identify the Outside Options (BATNA)**
BATNA stands for "Best Alternative to a Negotiated Agreement." This is the minimum amount a party will accept before walking away.
*   **Sera's BATNA:** She can sell to another buyer for a surplus of **15 gold**.
*   **Brenn's BATNA:** He can sell to another

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the bargaining pattern, accurately calculates the negotiable surplus (55), splits it equally, and derives the correct final allocations (Sera: 42.5, Brenn: 37.5). The explanation of outside options as floors is clear. However, the response does not reach Level 4 beca

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Lady Ashworth paid Corbin a flat wage and got a poor harvest. She suspects shirking but cannot prove it. What is the structural problem with her contract, and how might she redesign it?

**Expected Answer:** **Principal-agent problems and moral hazard** — The principal (Ashworth) delegates a task to an agent (Corbin) whose effort she cannot observe. Under a flat wage, the agent bears the cost of effort but captures none of the benefit (the extra apples go to the principal). This misalignment of incentives is moral hazard: the agent has both the oppor

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the structural problem and the solution, followed by the identification of the underlying economic principle.

### Step-by-Step Analysis

**1. Analyzing the Incentive Structure**
Lady Ashworth's current contract is a **fixed-wage contract**. Corbin receives 50 gold regardless of the output (the number of apples harvested).
*   **Corbin's Perspective:** His effort (working hard, managing workers, dealing with rain) costs him time and energy (disutility). Since his pay is fixed, any extra effort he exerts yields zero additional financial reward for him. Conversely, if he shirks (spends time at the tavern), he saves energy but loses nothing financially.
*   **The Result:** Rational self-interest dictates that Corbin will min

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Principal-Agent problem and Moral Hazard, explicitly distinguishing hidden action from other issues. They clearly explain the mechanism of misaligned incentives under a flat wage and propose multiple structured solutions (piece rate, profit sharing, deferred paym

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Using the market board data, find the price at which quantity supplied equals quantity demanded. What happens at prices above or below this equilibrium?

**Expected Answer:** **Supply, demand, and market equilibrium** — At equilibrium, quantity supplied equals quantity demanded. From the table: at price = 2, excess demand (shortage) of 60. At price = 8, excess supply (surplus) of 60. At price = 6, Qs = 60 = Qd = 40 — not yet equal. Interpolating (or reading the table), equilibrium is at price = 5, where both Qs and

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyzing the Market Data**
First, let's look at the relationship between price, quantity supplied, and quantity demanded based on the board provided:

*   **At 2 gold:** Supply (20) < Demand (80). There is a shortage of 60 bushels. This matches the market master's story about running out of grain and angry buyers.
*   **At 4 gold:** Supply (40) < Demand (60). There is still a shortage of 20 bushels.
*   **At 6 gold:** Supply (60) = Demand (60). The quantities match perfectly.
*   **At 8 gold:** Supply (80) > Demand (20). There is a surplus of 60 bushels. This matches the story of farmers going home with unsold grain.
*   **At 10 gold:** Supply (100) > Demand (0). A massive surplus exists.

**2. Identifying the Equilibrium Price**
The equilibrium price is de

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the general pattern of supply and demand and explains the adjustment mechanism (surpluses/shortages) well. However, they fundamentally fail to interpret the provided data table, incorrectly stating that at price 6, Qs equals Qd (60=60), whereas the correct answer key

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** The king sets a price ceiling of 3 gold per bushel. Equilibrium was at 5 gold and 50 bushels. What happens to quantity supplied, quantity demanded, and the market? What trades are lost?

**Expected Answer:** **Price controls and deadweight loss** — A binding price ceiling (set below equilibrium) creates a shortage: quantity demanded exceeds quantity supplied. At P=3, Qs=30 and Qd=70, shortage=40. Some mutually beneficial trades that would occur at equilibrium (P=5, Q=50) no longer happen. The lost surplus from these unrealized trades is deadwe

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the economic mechanics and the underlying reasoning principles at play.

### 1. Analysis of Market Mechanics

First, let's break down the numerical changes described in the scenario:

*   **Initial Equilibrium:**
    *   Price: 5 gold
    *   Quantity: 50 bushels
    *   At this point, Quantity Supplied ($Q_s$) equals Quantity Demanded ($Q_d$). The market clears efficiently.

*   **The Intervention (Price Ceiling):**
    *   New Price: 3 gold (Below equilibrium).
    *   **Quantity Supplied ($Q_s$):** Drops to **30 bushels**.
        *   *Reasoning:* At the lower price, the profit margin for farmers decreases. Some farmers who were willing to sell at 5 gold are no longer willing to sell at 3 gold, so they withdraw from th

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly calculates the shortage (40) and explicitly identifies the 20 lost mutually beneficial trades, directly addressing the deadweight loss mechanism. Furthermore, the response exceeds the baseline requirements by discussing black market formation, the shift in rationing mechanisms,

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** Grist says his business is profitable and efficient. Wynn says Clearwater is paying part of his costs. Who is right, and what does this situation reveal about market prices?

**Expected Answer:** **Externalities** — A negative externality is a cost imposed on third parties who are not involved in the transaction. Grist's private cost is 40 gold, but the social cost includes the 20 gold per week Clearwater spends on water treatment. The true social cost of production is 60 gold, making Grist's true profit 40, no

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyzing Grist's Perspective (The Private View)**
Grist calculates his profit based strictly on his **private costs** and **private revenues**.
*   **Revenue:** 100 gold.
*   **Private Costs:** 40 gold (chemicals, labor, hides).
*   **Private Profit:** 60 gold.
*   **Conclusion:** From Grist's internal accounting, the business is efficient and profitable. He has successfully converted inputs into a valuable product at a low cost.

**2. Analyzing Wynn's Perspective (The Social View)**
Wynn points out costs that Grist did not pay for but that society (Clearwater) must now bear.
*   **External Costs:** 20 gold/week for water treatment + the health costs of the three sick children (which represent a loss of human capital and medical resources).
*   **Observatio

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the negative externality, explicitly distinguishes between private and social costs, and explains how the exclusion of external costs leads to an artificially low price and overproduction (market failure). This aligns perfectly with Level 3. The response does not rea

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral?

**Expected Answer:** **Information asymmetry and adverse selection (lemons problem)** — When sellers know more about product quality than buyers, buyers cannot distinguish good from bad. They offer a price reflecting average quality. Owners of above-average horses find this price too low and withdraw. The remaining pool is worse, buyers adjust downward, more good horses leave — a death

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the situation, the driving forces behind the spiral, and the underlying economic principle at play.

### Step-by-Step Analysis

1.  **Information Asymmetry**: The core problem is that sellers possess private information about the true quality of their horses (healthy vs. sick), while buyers (like Kael) cannot distinguish between them. This creates a situation where the buyer cannot verify the product's value before purchase.
2.  **The Pricing Dilemma**: Because buyers cannot tell the difference, they are unwilling to pay a premium for a "good" horse, fearing they might accidentally buy a "bad" one. Consequently, buyers offer a single market price that reflects the *average* quality of the horses currently available.
3.  *

**Score:** 3/4 ███░
**Judge Reasoning:** The student provides an excellent, step-by-step explanation of the information asymmetry, the pricing based on average quality, the exit of high-quality sellers, and the resulting downward spiral (adverse selection). This clearly meets all criteria for Level 3. However, the response does not reach L

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Nobody buys the Barrel Mug, yet adding it to the menu increases Large Ale sales. The tip jar moved but the tip amount was not suggested. What is going on in both cases, and is it ethically acceptable?

**Expected Answer:** **Behavioral economics in markets: nudges and choice architecture** — Two phenomena are at work. First, the decoy effect: the Barrel Mug is a dominated option that no one chooses, but its presence makes the Large Ale seem more reasonable by comparison. It shifts the reference point. Second, choice architecture: the placement of the tip jar changes behavior without cha

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the psychological mechanisms at play and an evaluation of their ethical implications.

### 1. Analysis of the "Barrel Mug" Scenario
**The Phenomenon:**
Lena introduces a "Barrel Mug" priced at 15 copper, which no one buys. However, its presence causes sales of the 8-copper Large Ale to jump by 50%.

**The Mechanism: The Decoy Effect (Asymmetric Dominance)**
This is a classic demonstration of the **Decoy Effect**, a cognitive bias where consumers change their preference between two options when a third, asymmetrically dominated option (the decoy) is presented.
*   **Without the decoy:** Customers compare the Small (3c), Medium (5c), and Large (8c). The jump from Medium to Large is 3 copper. Some might feel 8 copper is too st

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both the Decoy Effect and Choice Architecture (specifically salience and context). They explain the mechanisms clearly, connecting them to behavioral economics concepts like asymmetric dominance and nudging. Crucially, they address the ethical dimension by distinguis

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Breck says the storm is good for the economy because it creates repair jobs. The clerk is skeptical. Who is right, and what is Breck failing to consider?

**Expected Answer:** **Broken window fallacy** — Breck counts the economic activity generated by repairing storm damage (the seen) but ignores the economic activity that the same money would have generated if spent on something else (the unseen). The glazier's gain is real, but the shopkeepers now spend money on window repairs instead of on new in

**Model Response:**
> Based on the scenario provided, **the town clerk, Maren, is right to be skeptical**, while Alderman Breck is demonstrating a classic economic fallacy.

Here is the step-by-step reasoning behind this conclusion:

### 1. Identification of the Fallacy
Alderman Breck is demonstrating the **Broken Window Fallacy**. This concept was famously illustrated by the French economist Frédéric Bastiat in his 1850 essay *That Which Is Seen, and That Which Is Not Seen*.

The fallacy occurs when one focuses only on the immediate, visible economic activity generated by destruction (the "seen") while ignoring the hidden, long-term economic losses caused by that same destruction (the "unseen").

### 2. Analysis of Breck's Argument (The "Seen")
Breck correctly identifies the **visible** effects:
*   The glazie

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Broken Window Fallacy and explicitly names it. They clearly articulate the 'seen' versus 'unseen' distinction and explain the mechanism of opportunity cost (money spent on repairs cannot be spent on new inventory or investment). Furthermore, the response addresse

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Dagan says that if Brassholm gains from trade, Ardenvale must lose. Petra says both sides can gain. Who is right, and why?

**Expected Answer:** **Zero-sum thinking** — Dagan falsely assumes that trade is zero-sum — that total value is fixed and any gain for one party is a loss for the other. In reality, voluntary trade creates value because parties exchange goods they value less for goods they value more. Ardenvale values iron more than its surplus grain; Brasshol

**Model Response:**
> Based on the scenario provided, **Petra is right**, and Dagan is demonstrating a fundamental misunderstanding of how trade works.

Here is the step-by-step reasoning behind this conclusion:

### 1. Analysis of Dagan's Reasoning
Dagan argues that "Every gold piece Brassholm earns... is a gold piece taken from Ardenvale's pocket" and that "If they're winning, we're losing."
*   **The Principle:** This reasoning relies on the **Zero-Sum Fallacy** (also known as the Zero-Sum Game bias).
*   **The Flaw:** A zero-sum game assumes that resources are fixed and that one party's gain is mathematically equivalent to the other party's loss. Dagan views wealth as a static pie where taking a larger slice for Brassholm automatically leaves a smaller slice for Ardenvale. He ignores the possibility that th

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Dagan's error as the 'Zero-Sum Fallacy' and explicitly contrasts it with positive-sum outcomes. They accurately explain the mechanism of value creation through subjective valuation (rotting grain vs. needed food) and voluntary exchange. Furthermore, they connect the 

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter?

**Expected Answer:** **Rapoport's Rules** — A four-step protocol for productive disagreement: (1) restate the opponent's position so well they endorse the restatement, (2) list genuine points of agreement, (3) acknowledge what you learned from them, (4) only then offer criticism. Corwin follows all four steps in sequence.

**Model Response:**
> Based on the scenario provided, here is a step-by-step breakdown of Alderman Corwin's rhetorical strategy, followed by an analysis of the underlying reasoning pattern.

### Step-by-Step Analysis of Corwin's Actions

Corwin employs a deliberate sequence of moves designed to lower defenses, establish credibility, and isolate the specific point of disagreement.

**1. Steelmanning the Opponent's Argument**
*   **Action:** Corwin begins by restating Holt's position not as Holt stated it, but in its "strongest form." He clarifies that Holt isn't dismissing the salmon but prioritizing survival (feeding people) over conservation.
*   **Why it matters:** This is the opposite of a "straw man" fallacy. By validating the opponent's logic and showing he understands their core motivation (economic survi

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all four steps of the protocol in the proper sequence (restating, agreeing, acknowledging learning, then criticizing) and provides a strong explanation of why the sequence matters for lowering defenses. However, the response does not reach Level 4 because it fails to

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?

**Expected Answer:** **Reductio ad absurdum** — Tessa takes Varek's claim ('all beliefs are equally valid') and draws out its logical consequences: flat earth is as valid as round earth, poison is as nutritious as food. Since Varek cannot accept these consequences, his original claim is undermined. This is the classic structure of reductio: assum

**Model Response:**
> Tessa responded to Varek by employing a logical technique known as **reductio ad absurdum** (reduction to absurdity).

Here is the step-by-step breakdown of her reasoning and why it is effective:

### 1. The Logical Mechanism: Reductio ad Absurdum
Tessa did not simply argue that Varek was wrong; she accepted his premise temporarily to demonstrate that it leads to an unacceptable or contradictory conclusion.

*   **Varek's Premise:** "Every belief is equally valid; no belief is better than any other."
*   **Tessa's Extension:** She takes this premise to its logical extreme by applying it to two specific, objectively verifiable scenarios:
    1.  **Astronomy:** The belief that the Earth is flat vs. the belief that it is round.
    2.  **Biology/Chemistry:** The belief that poison is nutritio

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'reductio ad absurdum' and clearly articulates the assume-derive-reject structure (accepting the premise to show it leads to unacceptable conclusions like poison being nutritious). Furthermore, the response exceeds Level 3 by discussing the conditions 

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** You have two explanations for the attic disturbances. What principle should guide your choice between them, and which explanation does it favour?

**Expected Answer:** **Occam's Razor** — When two hypotheses explain the same evidence, prefer the one that posits fewer entities and mechanisms. Elsa's squirrel hypothesis explains the torn food, scattered flour, muddy tracks, thumping, and fallen items using one known entity (squirrels) and one known mechanism (foraging through a gap). W

**Model Response:**
> ### Step-by-Step Reasoning

1.  **Analyze the Competing Hypotheses:**
    *   **Hypothesis A (Widow Moss):** The disturbances are caused by the ghost of Old Henrick.
        *   *Evidence cited:* Thumping sounds, things falling, the attic was locked.
        *   *Assumptions:* Requires the existence of ghosts, the ability of a spirit to physically manipulate objects (torn meat, scattered flour), and the specific motivation of a "restless spirit."
    *   **Hypothesis B (Elsa):** The disturbances are caused by squirrels.
        *   *Evidence cited:* A physical gap under the eaves (entry point), muddy paw prints (physical trace), a nest of shredded cloth (behavioral evidence), and the nature of the damage (torn meat, scattered flour).
        *   *Assumptions:* Relies on known biological be

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies Occam's Razor and correctly defines it as selecting the hypothesis with the fewest assumptions. They thoroughly analyze the specific entities and mechanisms required by both hypotheses, noting that the ghost theory requires unproven supernatural assumptions while th

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Cask seems to have made a strong case. But look carefully at what he talked about and what he did not talk about. What is his argumentative strategy, and what is wrong with it?

**Expected Answer:** **Occam's Broom** — Dennett coined 'Occam's Broom' to describe the practice of sweeping inconvenient facts under the rug to make your argument look cleaner than it is. Unlike Occam's Razor (which removes unnecessary assumptions), Occam's Broom removes necessary evidence. Cask does not engage with the three independent 

**Model Response:**
> Based on the scenario provided, Alderman Cask is employing a sophisticated but logically flawed argumentative strategy designed to distract the audience from the core evidence presented by Dr. Lune.

Here is the step-by-step analysis of his reasoning pattern, the specific fallacies involved, and why his argument fails.

### 1. Analysis of the Argumentative Strategy
Cask's primary strategy is **deflection through distraction**. Instead of engaging with the specific data points from the three independent studies regarding water runoff (the core of Dr. Lune's argument), he shifts the focus to:
*   **Alternative Authority:** Citing his own company's internal report.
*   **Anecdotal Evidence:** Pointing to the physical health of the miners.
*   **Cherry-Picking:** Mentioning "three previous ass

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Cask ignored the three independent studies, selectively presented favorable evidence ('Cherry-Picking'), and used the funding issue to attack the messenger (Ad Hominem/Genetic Fallacy). This aligns perfectly with Level 3 criteria. However, the response fails to 

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Torvin says Cael is just ignoring the rules. Cael says something different. What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?

**Expected Answer:** **Jootsing (Jumping Out Of The System)** — Dennett argues that genuine creativity requires first mastering the rules of the system you are working in, and then deliberately violating specific rules for specific reasons. Random rule-breaking is just noise. Informed rule-breaking — knowing which rule to break, why, and what it will produce — i

**Model Response:**
> ### Step-by-Step Analysis

**1. Deconstructing the Conflict**
*   **Torvin's Position:** He views the rules (five colors, historical scenes, grid) as absolute boundaries. In his view, breaking a rule is synonymous with "ignoring" it, which equates to a lack of discipline and a descent into "chaos." He assumes that adherence to the form is the only proof of mastery.
*   **Cael's Position:** He explicitly states he did *not* ignore the rules. Instead, he claims to have mastered them to the point of "sleep." His argument is that true mastery involves understanding the *function* and *limitations* of a system so thoroughly that one can intentionally transcend it. He distinguishes between "flailing" (breaking rules out of ignorance) and "jumping" (breaking rules out of understanding).

**2. Ide

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core insight: that Cael's innovation is grounded in deep mastery rather than ignorance, distinguishing between 'flailing' and 'jumping.' They accurately explain the mechanism of informed rule-breaking using the Shuhari framework. However, the response does not re

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Kira thinks Brother Aelm said something profound. Did he? What exactly does 'Love is just a word' mean, and is it as deep as it sounds?

**Expected Answer:** **Deepity** — A deepity is a statement that seems profound but achieves this effect through ambiguity. It has two readings: (1) a trivially true reading that is not interesting, and (2) a reading that would be profound if true but is false or unsupported. The listener experiences the truth of reading 1 and the de

**Model Response:**
> ### Step-by-Step Analysis

**1. Deconstructing the Statement**
Brother Aelm's argument follows a specific logical structure:
*   **Premise 1:** Love causes massive real-world actions (chasing, killing, dying).
*   **Premise 2:** The word "love" consists of only four letters and is physically just a sound (a "breath of air").
*   **Conclusion:** Therefore, the *concept* of love is "nothing more than a sound" and "built on nothing."

**2. Identifying the Logical Flaw**
The core error here is a confusion between the **signifier** (the word/sound) and the **signified** (the concept, emotion, or phenomenon the word represents).
*   A word is indeed just a symbol. The word "fire" cannot burn you; the word "water" cannot quench thirst.
*   However, the *phenomenon* of love (the chemical reactions

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: the confusion between the signifier (the word) and the signified (the concept), effectively separating the trivially true reading (the word is just letters/sound) from the false profound reading (the emotion is meaningless). They provide excellent

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something?

**Expected Answer:** **The 'surely' operator** — Dennett identifies 'surely' as a rhetorical operator that attempts to sneak a controversial claim past the audience by presenting it as something everyone already agrees with. When a speaker says 'surely X,' they are signalling that X does not need argument — it is supposed to be obvious. But in phi

**Model Response:**
> Professor Venn's repeated use of the word "surely" is a rhetorical device that serves to **hide** a significant gap in his argument rather than strengthen it. By analyzing the structure of his statement, we can identify the specific reasoning patterns and fallacies at play.

### Step-by-Step Analysis

**1. The Function of "Surely" in Argumentation**
In logical discourse, "surely" is an intensifier used to signal that a proposition is self-evident or universally accepted. When a speaker uses it, they are attempting to bypass the need for evidence by appealing to a shared sense of common sense.
*   **First instance:** "Surely the capacity for genuine suffering requires self-reflection..."
*   **Second instance:** "Surely a creature that cannot contemplate its own existence cannot be said to 

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the 'surely' operator as a rhetorical device used to bypass the burden of proof. They correctly explain the mechanism (presenting contestable claims as self-evident), explicitly list the three specific smuggled premises (suffering requires self-reflection, self-refle

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The advisors and Pella are both trying to help Captain Rhea. But their approaches are very different. What is the difference, and which is more useful? Is there a risk to Pella's approach?

**Expected Answer:** **Goulding** — Dennett uses 'goulding' to describe the intellectual virtue of making bold, specific, testable claims rather than retreating into safe, unfalsifiable hedging. Pella's claim is specific (forty soldiers), testable (you can verify by scouting), and she has staked her credibility on it. The advisors' po

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyzing the Advisors' Approach (Brant and Maren)**
Brant and Maren are operating under a mindset of **extreme risk aversion** and **ambiguity tolerance**. Their language is filled with qualifiers: "might be," "depending on," "cannot know for certain," "perhaps," "tend to agree," "prudent course."
*   **The Flaw:** They are suffering from **Analysis Paralysis**. By focusing entirely on the *possibility* of unknown variables, they fail to provide a decision framework. In a crisis (a besieged fort where starvation is a threat), the cost of inaction is high. Their approach prioritizes the *appearance* of caution over the *utility* of a decision. They are effectively saying, "We cannot be 100% sure, so we will do nothing," which is a decision in itself, but a d

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: Pella's specific, testable claims enable action, while the advisors' hedging leads to paralysis. They articulate the epistemic virtue of falsifiability (noting that Pella's claim can be proven wrong) and the utility of accountability. However, the

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The lieutenant thinks Maren is being irrational by not computing the best allocation. What would you tell him about her approach?

**Expected Answer:** **Satisficing as rational strategy** — Maren demonstrates that satisficing — choosing good enough rather than optimal — is not a failure of rationality but the product of it. An ideally rational agent who knows her own limitations would prepare a decision procedure in advance that produces acceptable outcomes under constraint.

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the reasoning patterns and principles at play, followed by what you should tell the Lieutenant.

### Step-by-Step Analysis

**1. Identify the Core Conflict**
The conflict is between **Theoretical Optimality** (the Lieutenant's view: calculating the mathematically perfect distribution of resources) and **Practical Effectiveness** (Maren's view: acting immediately to save lives with the information and time available).

**2. Analyze the Lieutenant's Reasoning**
The Lieutenant is operating under the assumption that the "best" outcome is only achieved through a complete, pre-computed optimization model. He is ignoring the cost of the calculation itself.
*   **The Flaw:** He is committing the **Fallacy of Perfect Solution** (or 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies satisficing and bounded rationality, and explicitly explains the mechanism of deliberation costs outweighing benefits (Level 3). They accurately describe the pre-computation of protocols as moving cognitive load to a calm moment. However, the response stops short of 

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Question:** Elder Maren says the village's flood response was 'perfect' and sees no reason to hear the engineer's proposal. What mistake is she making?

**Expected Answer:** **The Panglossian Slide** — Elder Maren begins from the defensible claim that the council did the best they could given constraints (satisficing), then slides into asserting their solution was the best possible solution full stop (optimizing). She reframes losses as unimportant and refuses to consider improvements.

**Model Response:**
> Based on the scenario provided, Elder Maren is demonstrating a classic cognitive error known as **Hindsight Bias** (specifically the "I-knew-it-all-along" effect) combined with **Outcome Bias** and **Confirmation Bias**.

Here is the step-by-step breakdown of her reasoning pattern:

### 1. Analysis of the Reasoning Pattern
*   **The Context:** The village faced a crisis with limited resources ("only labor and materials available"). They made a decision that saved the majority of the village but incurred specific, tangible losses (the granary and two bridges).
*   **The Flawed Logic:** Elder Maren claims the solution was "optimal" and "perfect" *in any circumstance*. She ignores the fact that the decision was made under severe constraints and resulted in significant damage.
*   **The Core E

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Maren conflates a decision made under constraints with an optimal solution and notes the minimization of losses. However, the student explicitly misidentifies the pattern as 'Hindsight Bias' and 'Outcome Bias' rather than the required 'Panglossian Slide.' While 

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Question:** Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?

**Expected Answer:** **Conversation-stopper** — A conversation-stopper is any move that terminates deliberation by appeal to a value, right, rule, or taboo that is held to be non-negotiable. Dennett argues in 'Thought Stoppers' that these can be necessary (we do not deliberate about whether to torture innocents) but also dangerous (they can preve

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyze the Core Conflict**
The scenario presents a classic ethical dilemma where two valid but incompatible value systems collide:
*   **Councillor Breck's Position:** Rooted in **Utilitarianism** and **Consequentialism**. His argument is based on empirical data (flood maps, death tolls) and the imperative to minimize harm to the living. For him, the "right" action is the one that saves the most lives, regardless of the cost to tradition or the dead.
*   **Elder Sanna's Position:** Rooted in **Deontology** (duty-based ethics) and **Sacredness**. Her argument is based on absolute principles, tradition, and the intrinsic value of the ancestors. For her, certain actions (desecrating a grave) are inherently wrong, regardless of the consequences (saving lives).


**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Sanna is ending the conversation and distinguishes this move from a simple argument for the grove (meeting Level 2 criteria). They accurately describe the mechanism as a rejection of utilitarian calculation in favor of absolute principles. However, the response 

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Kael says he knows too much to trust his rules but not enough to abandon them. Is he right that this is a genuine dilemma? Is there a way out?

**Expected Answer:** **Wolf's Dilemma (The Reflective Satisficer's Predicament)** — This is the fundamental tension in bounded rationality: heuristics work because they are fast and frugal, but once you become reflectively aware of their limitations, you face a meta-decision. Do you (a) override the heuristic and reason from scratch (gaining accuracy but losing speed and sometimes 

**Model Response:**
> ### Step-by-Step Analysis

**1. Deconstructing Kael's Dilemma**
Kael is trapped between two extremes:
*   **Option A (Blind Heuristics):** Continue using his old rules of thumb. He rejects this because he now possesses *meta-knowledge* (knowledge about his own knowledge). He knows the rules are imperfect and can recall specific instances where they caused harm. To him, following a rule he knows to be flawed feels like "irrationality" or willful ignorance.
*   **Option B (Pure Reason):** Abandon the rules entirely and calculate every decision from first principles (optimizing every variable). He rejects this because of the *time cost*. In a battlefield (or a chess game), the time required to compute the optimal solution exceeds the time available, leading to paralysis and death.

**2. Ident

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the tension between heuristics and optimization and proposes 'meta-heuristics' (calibration) as a solution, which aligns with Level 2 and touches on Level 3. However, the response explicitly rejects the premise that the dilemma is genuine, labeling it a 'false dichot

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Sable's two Porters each failed in opposite ways. What is the underlying problem they share, and why is it so hard to solve?

**Expected Answer:** **The Frame Problem** — The Frame Problem asks: how does a rational agent determine what has and has not changed as a result of an action? Version 1 of the Porter checks everything (the Hamlet problem — paralyzed by the attempt to verify all possible changes). Version 2 checks only pre-specified relevant items (the tunnel-

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the underlying problem and the reasoning pattern it demonstrates.

### Step 1: Analyze the Failure of the First Porter
The first Porter attempted to carry a tray but froze because it tried to verify **every possible variable** in the universe before taking a single step.
*   **The Flaw:** It suffered from **infinite regress** or **computational paralysis**. It treated irrelevant variables (e.g., "Will the walls stay up?", "Is gravity still working?") with the same weight as relevant ones.
*   **The Result:** It could not act because the cost of verification (checking 10,000 rules) exceeded the time available to complete the task. This is a failure of **efficiency** and **relevance filtering**.

### Step 2: Analyze the Fai

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Frame Problem and explicitly details both failure modes (paralysis from checking everything and tunnel vision from checking too little). Crucially, the response goes beyond the basic definition to explain that humans solve this via 'common sense' or intuition reg

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Dav wants to know which moral theory to follow. Abbess Thera says he is asking the wrong question. What does she mean, and what is the alternative she is proposing?

**Expected Answer:** **The Moral First Aid Manual** — Dennett proposes that instead of waiting to resolve the centuries-old debate between consequentialism, deontology, virtue ethics, and other moral theories, we should build a practical guide — a Moral First Aid Manual. Just as a medical first aid manual tells you to stop bleeding before diagnosing th

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Abbess Thera's reasoning and the alternative she proposes.

### Step-by-Step Analysis

**1. Identifying the Core Conflict**
Dav is trapped in a classic ethical dilemma: a clash between **Deontology** (the teacher's view: theft is inherently wrong, regardless of consequences) and **Consequentialism/Utilitarianism** (the heart's view: saving a life is the highest good, regardless of the rule broken). Dav assumes these are mutually exclusive and that one must be the "one true theory" to solve the problem.

**2. Analyzing Abbess Thera's Critique**
When Thera says, "You are asking the wrong question," she is rejecting the premise that a single, universal moral theory can solve every specific human problem.
*   **The Fallacy Da

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the Abbess is proposing a practical, context-dependent approach rather than a single theoretical solution, which aligns with Level 2. They accurately describe the shift from 'which theory is true' to 'what works for this situation' and mention urgency. However, 

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Nessa seems pretty confident about why Gareth's harvest failed. But listen to how she talks about her own flooding problem. Do you notice anything different about how she explains the two situations?

**Expected Answer:** **Fundamental attribution error** — Nessa attributes Gareth's poor harvest to his character (laziness, lack of care) while ignoring a situational factor (south-facing blight). When her own field flooded, she cited the external event (flooding) and her response to it. She judges others by disposition and herself by situation.

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the reasoning pattern and bias demonstrated by Nessa.

### Step 1: Analyze Nessa's explanation of Gareth's failure
Nessa attributes Gareth's empty fields entirely to his internal character traits. She uses phrases like "the man is lazy," "always has been," and "whittling rather than work."
*   **The Logic:** She ignores external factors (like the blight mentioned by Pell) and assumes the outcome (failure) is caused solely by Gareth's lack of effort or moral failing.
*   **The Attribution:** This is an **internal attribution** (blaming the person).

### Step 2: Analyze Nessa's explanation of her own failure
When discussing her own flooded north field, Nessa describes a specific external event: "When my north field flooded la

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Fundamental Attribution Error and the Actor-Observer Bias by name. They clearly articulate the asymmetry in Nessa's reasoning: attributing Gareth's failure to internal character traits while ignoring situational factors (blight), versus acknowledging her own situ

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Elder Sorn has real experience with famine, and his fear is understandable. But Dalla has data and a plan. What is driving Sorn's opposition — is it the evidence, or something else?

**Expected Answer:** **Pessimism bias** — Sorn systematically overestimates the likelihood of negative outcomes (three consecutive bad harvests, irrigation failure, additional disasters) while dismissing evidence of positive possibilities (historical base rates, irrigation data from the next valley, Dalla's engineering analysis). His trauma

**Model Response:**
> Based on the scenario provided, Elder Sorn's opposition is **not** driven by the evidence; in fact, he actively dismisses the evidence. Instead, his stance is driven by **psychological trauma** and specific cognitive biases that override rational data processing.

Here is the step-by-step analysis of the reasoning patterns and biases at play:

### 1. The Core Driver: Trauma-Induced Availability Heuristic
Sorn's primary motivation is his lived experience of famine as a child. This creates a powerful **Availability Heuristic**.
*   **The Mechanism:** People estimate the probability of an event based on how easily examples come to mind. Because Sorn vividly remembers the terror and starvation of the past famine, the idea of a third bad harvest feels immediate and inevitable to him, regardless

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: Sorn overestimates negative outcomes due to trauma and dismisses positive empirical evidence. They accurately describe the cognitive distortions (Availability Heuristic, Negativity Bias, Catastrophizing) which align with the definition of Pessimis

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Venn says 'the bad ones stick with you.' He's right that the failures were real problems. But is he making a good decision by dropping the Dustwalkers? What is he not accounting for?

**Expected Answer:** **Negativity bias** — Venn's memory and emotional weighting are dominated by the three failures. He can recall each one vividly — the silkwood, the dye delay, the smashed glassware — but the forty-seven successes have faded into an undifferentiated background. The negative events carry disproportionate influence on his j

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Guildmaster Venn's decision-making process.

### Step 1: Analyze the Data vs. The Perception
*   **The Data:** The Dustwalkers have a **94% success rate** (47 out of 50 contracts). This is statistically superior to their nearest competitor, the Ironwheel Guild, which has an **81% success rate**.
*   **The Perception:** Venn focuses exclusively on the **3 failures** (6% of the total). He dismisses the 47 successes as irrelevant ("I don't care about the forty-seven").
*   **The Conflict:** There is a massive disconnect between the objective statistical probability of success and Venn's subjective emotional reaction to the failures.

### Step 2: Identify the Cognitive Mechanism
Venn explicitly states, "The bad ones stick wit

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Negativity Bias and provides a sophisticated explanation of the mechanism, including the evolutionary basis for why negative events weigh heavier in memory. They accurately calculate the comparative failure rates (94% vs 81%) and project the negative outcome of switc

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** The War Council has reached unanimous agreement on the plan. General Tova seems confident that everyone is on board. But Lord Caelen tells you a different story. What is actually happening in this council, and why does unanimous agreement not mean the plan is sound?

**Expected Answer:** **Groupthink** — The War Council exhibits classic groupthink: (1) the illusion of unanimity — silence is read as agreement; (2) direct pressure on dissenters — Caelen was accused of undermining morale and threatened with expulsion; (3) self-censorship — Caelen and Miren stopped raising concerns; (4) the illusion of 

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of what is happening within the War Council and the reasoning behind the failure of their decision-making process.

### Step 1: Analyze the Group Dynamics
The scenario describes a group that has moved from initial reservations to "enthusiastic unanimous agreement" over a short period (three weeks). Key indicators of the group's internal state include:
*   **Suppression of Dissent:** Lord Caelen raised a critical factual objection (unsurveyed tunnels) in the second meeting. Instead of being addressed, he was accused of "undermining morale" by General Tova and threatened with resignation by Councillor Drace.
*   **Self-Censorship:** After Caelen was silenced, other members (like Miren regarding cavalry timing) also stopped voici

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Groupthink' as the core pattern and explicitly names multiple required symptoms: illusion of unanimity, direct pressure on dissenters, self-censorship, and illusion of invulnerability. They clearly explain how these dynamics degrade decision quality by preventing st

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Question:** Mirren's tonic has no active ingredients, yet her patients genuinely improve. Doctor Alden says the tonic does nothing. Who is right, and what is actually causing the improvement?

**Expected Answer:** **Placebo effect** — The placebo effect occurs when a patient experiences real improvement due to their expectation of benefit, not due to any active treatment. It is 'dual' because it is both a genuine phenomenon (belief produces real effects) and a potential source of error (it can mask whether a treatment has any pha

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyzing Doctor Alden's Perspective**
Doctor Alden is operating from a strictly **biomedical and materialist framework**. His reasoning is based on the presence of a pharmacological "active ingredient" (a molecule that interacts with the body's biology to cause a physiological change).
*   **Observation:** The tonic contains only chamomile and honey.
*   **Premise:** Chamomile and honey (in this context) have no analgesic or curative properties strong enough to treat the specific ailments described.
*   **Conclusion:** Therefore, the tonic is inert and "does nothing."
*   **Flaw:** Alden is committing a category error by equating "pharmacological activity" with "therapeutic effect." He assumes that if the *substance* doesn't change the body, the *treatment*

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the placebo effect and explains the mechanism well, noting that belief triggers real physiological changes (endorphins, etc.), which distinguishes it from Level 2. They also effectively synthesize the perspectives of Alden and Mirren. However, the response does not r

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Kael wanted to learn field medicine when it was optional. Now that it's mandatory, he doesn't want to go. The training itself hasn't changed. What is driving his resistance?

**Expected Answer:** **Reactance** — Reactance is a motivational response to perceived threats to personal freedom. When people feel their autonomy is restricted — even by a reasonable mandate — they experience an urge to restore their freedom by doing the opposite of what is required. Kael wanted the training when it was optional but 

**Model Response:**
> Based on the scenario provided, the psychological phenomenon driving Sergeant Kael's resistance is **Reactance** (specifically, **Psychological Reactance**).

Here is the step-by-step reasoning behind this conclusion:

### 1. Analysis of the Change in Motivation
*   **Initial State:** When the training was optional, Kael had a clear internal motivation to learn. He "wanted to learn," "signed up," and even "was halfway through the manual" (in the case of Doss). The behavior was driven by **intrinsic motivation** (personal interest and utility).
*   **Trigger Event:** Commander Voss made the training mandatory and attached a threat of "disciplinary action" for non-compliance.
*   **Resulting State:** Kael's desire to attend evaporated and was replaced by a desire to do the opposite. He expli

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Reactance' as the core phenomenon and provides a precise explanation of the autonomy mechanism (loss of choice triggering a urge to restore freedom). They effectively distinguish reactance from similar concepts like cognitive dissonance and the backfire effect, demo

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Finch is convinced the audience noticed his wrong note and is judging him for it. The audience seems unaware. What cognitive error is Finch making, and why is his estimate of others' attention so far off?

**Expected Answer:** **Spotlight effect** — The spotlight effect is the tendency to overestimate how much other people notice and remember our appearance, behavior, and mistakes. Finch assumes the entire tavern registered his wrong note because it was vivid and distressing to him. In reality, most audience members were only loosely attending,

**Model Response:**
> Based on the scenario provided, Finch is demonstrating a classic cognitive bias known as the **Spotlight Effect**.

Here is the step-by-step reasoning behind this conclusion:

1.  **The Discrepancy in Perception**: Finch believes that a specific, minor error (the wrong opening chord) is the center of attention for everyone in the room. He feels the weight of "everyone staring" and assumes the audience is fixated on his mistake.
2.  **The Reality Check**: The external evidence contradicts his internal belief. The audience is laughing, drinking, and asking about the content of the songs (the ballad about the sea captain). The barkeep praises the show. No one has mentioned the error, suggesting they either didn't notice it or, more likely, noticed it briefly and immediately moved on.
3.  **Th

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Spotlight Effect and provides a robust explanation of the underlying mechanism (egocentric projection/first-person perspective). Crucially, the response distinguishes between Finch's internal perception of the mistake as 'catastrophic' and the audience's actual e

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Aldric explains the flood victims' suffering by pointing to their past choices. Wren challenges his explanations. Who is reasoning more carefully, and what motivates Aldric's interpretation?

**Expected Answer:** **Just-world hypothesis** — The just-world hypothesis is the belief that people get what they deserve: good things happen to good people and bad things happen to bad people. Aldric constructs post-hoc explanations for why the flood victims are responsible for their own suffering (poor savings, bad choices) while ignoring the a

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the reasoning patterns, biases, and motivations at play.

### Step 1: Analyze Aldric's Reasoning
Aldric observes a correlation: the people on the low ground suffered, and he claims they made poor financial choices (spending on ale, refusing cooperatives). He then concludes that these choices *caused* the suffering.

*   **The Logical Flaw:** Aldric is committing the **Just-World Hypothesis** (or Just-World Fallacy). This is a cognitive bias where people believe that the world is inherently fair, so those who suffer must have done something to deserve it, and those who prosper must be virtuous.
*   **The Causal Error:** He is also confusing correlation with causation. The fact that Gareth and Petra lived on low ground is a r

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the Just-World Hypothesis and provides a comprehensive explanation of the motivated reasoning mechanism (the need to believe the world is fair to feel safe). They clearly connect this bias to victim-blaming and, crucially, explain how it distorts Aldric's view of hi

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Hask says the town was better in the old days. The records show improvements across every measurable dimension. Who is right, and why does Hask's perception differ so sharply from the data?

**Expected Answer:** **Declinism** — Declinism is the tendency to view the past favorably and the future pessimistically, believing that society or conditions are in decline. Hask filters his memories through nostalgia (remembering the good, forgetting the bad) and discounts present improvements because they look different from the pas

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the situation, the resolution of the conflict between Hask and the data, and the identification of the underlying psychological principles.

### Step 1: Analyzing the Conflict (Data vs. Perception)

First, we must establish the objective reality versus the subjective experience presented in the text.

*   **Objective Reality (The Data):** The town records provide hard metrics indicating significant progress:
    *   **Economic:** Wages are up; the new copper mine employs more people than the old iron mine ever did.
    *   **Social/Safety:** Violent crime has dropped by 50%.
    *   **Educational:** Literacy has increased by 40%.
    *   **Conclusion:** By any measurable, utilitarian standard, the town is objectively "bet

**Score:** 3/4 ███░
**Judge Reasoning:** The student accurately identifies the core mechanisms of declinism: nostalgia filtering memories ('Rosy Retrospection'), the confusion of cultural change with objective decline, and the dismissal of data showing improvement. They explain that Hask compares a glorified past to an imperfect present. H

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Tomas keeps presenting stronger evidence that the well is contaminated. Greer's faction keeps becoming more convinced it is safe. How is this possible, and what mechanism explains it?

**Expected Answer:** **Backfire effect** — The backfire effect occurs when corrective evidence strengthens rather than weakens a held belief. Greer interprets the volume of evidence not as strength of the case but as evidence of an agenda. Each new piece of data is reframed as 'why are you trying so hard?' rather than evaluated on its merits

**Model Response:**
> Based on the scenario provided, the phenomenon occurring is a classic example of **The Backfire Effect**, which is a specific manifestation of **Motivated Reasoning** and **Confirmation Bias**.

Here is the step-by-step breakdown of the reasoning and the mechanism at play:

### 1. Analysis of the Psychological Mechanism
The core issue is not a lack of intelligence or a lack of evidence on Tomas's part; rather, it is how the villagers process information that conflicts with their existing worldview.

*   **Identity and Belief Protection:** For the villagers, the well is not just a water source; it is a symbol of their heritage ("our grandparents drank from this well"). Accepting that the well is contaminated implies that their ancestors made a mistake, that their community is in danger, or 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Backfire Effect and provides a strong explanation of the underlying mechanism, specifically linking it to identity threat, motivated reasoning, and the perception of evidence as an attack. This meets all criteria for Level 3. However, the response does not reach 

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Madame Kel's reading felt incredibly accurate to the player. Fenn says she gave the same reading to everyone. How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves?

**Expected Answer:** **Barnum effect (Forer effect)** — The Barnum effect is the tendency to accept vague, general personality descriptions as uniquely applicable to oneself. Madame Kel's statements ('great need for admiration,' 'tendency to be self-critical,' 'unused capacity') are true of nearly everyone but feel personally revelatory to each individua

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the psychological phenomenon at play and the reasoning pattern it demonstrates.

### Step 1: Analyzing the Content of the Reading
First, we must look at the specific statements Madame Kel made:
*   "You have a great need for other people to like and admire you."
*   "You have a tendency to be critical of yourself."
*   "You have a great deal of unused capacity..."
*   "You prefer a certain amount of change and variety..."

These statements are **vague, positive, and universally applicable**. Almost every human being desires social approval, experiences self-doubt, feels they could achieve more, and dislikes being restricted. They are not specific to the player's unique history, profession, or specific personality traits. Th

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Barnum (Forer) Effect and provides a comprehensive explanation of the psychological mechanisms, including subjective validation, confirmation bias, and the tendency to 'fill in the blanks' with personal experiences. The response explicitly distinguishes between t

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Maren believes she has solid evidence that her tonic works. What is problematic about how she gathered and evaluated that evidence?

**Expected Answer:** **Confirmation bias** — Maren commits three distinct moves: (1) She only followed up with 20 of 31 customers — the missing 11 may skew results. (2) She finds reasons to disqualify negative reports rather than counting them as counterevidence. (3) She treats her selective survey as equivalent to controlled trials, ignoring 

**Model Response:**
> Based on the scenario provided, Maren's reasoning demonstrates a classic failure in scientific methodology driven by **confirmation bias** and **selection bias**, specifically manifesting as **cherry-picking data** and **post-hoc rationalization**.

Here is the step-by-step breakdown of the problematic reasoning patterns:

### 1. Selection Bias (Survivorship Bias)
Maren claims to have "solid evidence" based on a sample size of 20 out of 31 customers.
*   **The Flaw:** She only tracked down 20 people. The 11 missing customers are a "missing data" set that she ignores. If those 11 people stopped buying the tonic because it didn't work, or if they moved away because they were still in pain, excluding them skews the results.
*   **The Principle:** In a valid study, the entire sample group (or 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies confirmation bias and thoroughly explains all three key components required for a Level 4 score: (1) the selective search/sampling issue regarding the missing 11 customers, (2) the active dismissal/disqualification of negative evidence via ad-hoc rationalizations, an

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brynn gives several reasons for continuing with her crusher. What are those reasons, and do they actually tell her anything about whether continuing is a good idea going forward?

**Expected Answer:** **Sunk cost fallacy** — Brynn treats past investment (three years, four thousand silvers) as a reason to continue investing, when that money and time are gone regardless. Her decision should depend only on future costs and benefits: further redesigns vs. the proven dwarven machine.

**Model Response:**
> ### Step-by-Step Analysis

**1. Identifying Brynn's Reasons**
First, let's isolate the specific justifications Brynn provides for refusing to switch to the dwarf's machine and continuing with her own flawed design:
*   **Time Investment:** She has spent "three years" on the project.
*   **Financial Investment:** She has spent "four thousand silvers."
*   **Reputational Investment:** She mentions her "reputation" is tied to this project.
*   **The "Almost There" Fallacy:** She believes that with "one more redesign — maybe two," she can fix the boiler pressure.
*   **Emotional Obligation:** She feels she "owes it to herself" to see it through after her hard work.

**2. Evaluating the Validity of These Reasons**
The core question is whether these reasons provide evidence that continuing is a 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Sunk Cost Fallacy,' clearly explains the irrecoverability of past costs, and contrasts them with future costs and benefits. They also identify related biases (escalation of commitment, loss aversion) and thoroughly articulate why the reasoning is flawed, exceeding t

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renn recommends the treatment and Holt opposes it, but they are describing the same data. What is causing their disagreement, and what does this reveal about how we process information?

**Expected Answer:** **Framing effect** — The framing effect occurs when the way information is presented influences judgment and decision-making, even when the underlying facts are identical. '200 saved out of 600' and '400 die out of 600' describe the same outcome, but the gain frame (lives saved) produces positive affect and risk aversio

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the disagreement and the underlying psychological principle at play.

### Step 1: Analyze the Data and the Discrepancy
First, we must verify the mathematical reality of the situation.
*   **Total Patients:** 600
*   **Advisor Renn's Frame:** "200 saved."
    *   Calculation: $600 - 200 = 400$ deaths.
*   **Advisor Holt's Frame:** "400 die."
    *   Calculation: $600 - 400 = 200$ survivors.

Mathematically, the outcome is identical: **200 survivors and 400 deaths.** There is no factual difference in the treatment's efficacy. However, the advisors have reached opposite conclusions: Renn recommends adoption (positive framing), while Holt opposes it (negative framing).

### Step 2: Identify the Psychological Mechanism
The cor

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the mathematical equivalence of the scenarios and explicitly names the 'Framing Effect.' They accurately explain the mechanism involving gain/loss asymmetry and risk preferences (risk-averse for gains, risk-seeking/loss-averse for losses). Crucially, they connect the

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge Master Dunn rated the Ironworkers' proposal higher, but an independent engineer certified both as equivalent. What is driving Dunn's different evaluations of identical work?

**Expected Answer:** **In-group bias** — In-group bias is the tendency to favor members of one's own group — evaluating their work more charitably, trusting them more readily, and attributing positive qualities to them — while viewing out-group members with suspicion, scrutiny, and less charitable interpretation. Dunn reads the same qualit

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning pattern and bias at play:

### Step 1: Analyze the Objective Facts
First, we must establish the baseline reality presented in the text:
*   **The Proposals:** They are "nearly identical" in timeline, cost, materials, and safety margins.
*   **The External Validation:** A neutral, independent engineer has certified both proposals as "equally sound."
*   **The Outcome:** Despite identical objective data, Forge Master Dunn rates the Ironworkers' proposal as "solid" and "trustworthy," while rating the Woodworkers' proposal as merely "adequate" with doubts about execution and quality.

### Step 2: Identify the Discrepancy
The core conflict is between **objective evidence** (the engineer's certification and the id

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism of in-group bias: Dunn evaluates identical work differently based solely on group membership, applying skepticism to the out-group while trusting the in-group. They explicitly name 'In-Group/Out-Group Bias' and explain the double standard in evalua

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Magistrate Yorn acquitted Ella and convicted Rusk on identical evidence. What is different between the two cases, and how is it affecting his judgment?

**Expected Answer:** **Halo effect** — The halo effect is the tendency for a positive impression of someone in one domain (personality, appearance, likability) to influence judgment of them in unrelated domains (guilt, competence, trustworthiness). Yorn likes Ella, so he interprets ambiguous evidence in her favor. He distrusts Rusk, so h

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Magistrate Yorn's reasoning and the underlying psychological mechanism at play.

### Step 1: Analyze the Facts vs. The Interpretation
First, we must isolate the objective facts from the Magistrate's subjective interpretation:
*   **Objective Fact:** Both Ella and Rusk were seen near the granary, had grain dust on their clothes, and lacked an alibi.
*   **Ella's Interpretation:** The Magistrate interprets the "grain dust" as a result of her daily routine (walking past) and the "night presence" as a result of her virtue (visiting the temple). He dismisses the evidence as "circumstantial at best."
*   **Rusk's Interpretation:** The Magistrate interprets the exact same "grain dust" and "night presence" as proof of guilt. He v

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Halo Effect (and Horn Effect) as the primary psychological mechanism, explaining how Yorn's positive impression of Ella leads to a charitable interpretation of evidence while his negative impression of Rusk leads to a harsh interpretation of identical facts. This

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Twenty people watched the theft and nobody acted. Each person had a reason — but it was the same reason. What is it, and why does having more witnesses make help less likely rather than more likely?

**Expected Answer:** **Bystander effect** — The bystander effect occurs when the presence of others reduces each individual's sense of personal responsibility to act. In a crowd, each person assumes someone else will intervene (diffusion of responsibility), looks to others' inaction as a signal that action is not needed (pluralistic ignorance

**Model Response:**
> Based on the scenario provided, the psychological phenomenon being demonstrated is the **Bystander Effect** (also known as **Bystander Apathy**).

Here is the step-by-step reasoning behind this conclusion and why the presence of more witnesses reduces the likelihood of help:

### 1. Identification of the Core Reason
The "same reason" shared by the baker, the guard, the woman, and the other eighteen people is **Diffusion of Responsibility**.

In the scenario, every individual assumes that because there are so many other people present, the burden of acting does not fall solely on them.
*   The baker thinks, "Someone will get him," assuming another person is better positioned or more willing to act.
*   The guard thinks, "Not my patrol sector," shifting the responsibility to someone else (pe

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Bystander Effect and provides a strong explanation of both Diffusion of Responsibility and Pluralistic Ignorance, noting how inaction reinforces inaction (feedback loop). However, the response fails to meet the criteria for Level 4 because it omits the third key 

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brecca's offer of 600 gold feels like a bargain. What is influencing that feeling, and should you trust it?

**Expected Answer:** **Anchoring** — The first numerical information — Brecca's 900-gold appraisal — sets a mental reference point that distorts evaluation of subsequent prices. Her 600-gold offer feels like a deal only because it is compared to the anchor, not to the actual market value (~400g).

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the psychological mechanisms at play and the conclusion on whether to trust the offer.

### Step 1: Identify the Core Mechanism
Brecca's strategy relies entirely on establishing a specific reference point before making the actual offer.
1.  **The Anchor:** He introduces a high number first: "Appraised at **900 gold**."
2.  **The Offer:** He immediately follows with a lower number: "**600 gold**."
3.  **The Perception:** Because your brain latched onto the 900 gold figure first, the 600 gold price feels like a massive discount (a 33% reduction), creating a sense of urgency and a "bargain."

### Step 2: Identify the Cognitive Bias
The specific reasoning pattern being demonstrated is the **Anchoring Effect** (or Anchoring Bi

**Score:** 4/4 ████
**Judge Reasoning:** The student clearly identifies the Anchoring Effect, explains how the initial 900-gold figure distorts judgment by creating a false reference point, and distinguishes this anchor from genuine market evidence (the 400-gold comparison). Furthermore, the response suggests the need for independent verif

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Dax seems eager and confident. Lirel seems cautious and uncertain. If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?

**Expected Answer:** **Dunning-Kruger effect** — Dax's limited training gives him confidence because he cannot yet see the complexities he has not encountered. His map of Greenvale worked because Greenvale was simple terrain; he generalizes from this success to assume the Thornveil will be the same. Lirel's decades of experience have taught her ho

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis and the final decision.

### Step 1: Analyze the Candidates' Approaches

**Dax (The Confident Novice):**
*   **Background:** Completed a six-week course; finished a surveying exercise in record time.
*   **Methodology:** Relies on standard techniques (contour lines assuming uniform slope) and believes that increasing the density of data points ("more sample points") solves all problems.
*   **Mindset:** Reductionist. He views the world as a collection of measurable data points where "it's all just measurement." He assumes the environment behaves predictably based on his limited training.
*   **Response to Risk:** When presented with a specific, catastrophic risk (karst sinkholes that drop 30 feet without warning), he dismiss

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Dunning-Kruger effect and explains the core mechanism: Dax's confidence stems from a lack of metacognition regarding his own limitations, while Lirel's caution reflects an awareness of complexity. The response articulates why low competence produces high confiden

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Captain Voss has data from Sergeant Tully showing the market district is a much bigger problem. Why does he still want to prioritize the coastal road? What is driving his judgment if not the numbers?

**Expected Answer:** **Availability heuristic** — Voss is judging the probability and severity of threats based on how easily examples come to mind. The wolf attacks are vivid, recent, emotionally charged, and widely discussed — making them highly 'available' in memory. Pickpocketing is mundane, individually minor, and forgettable. This asymmetry i

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Captain Voss's reasoning:

### Step 1: Analyze the Data vs. The Decision
*   **The Data (Sergeant Tully's input):** The objective data shows a massive disparity in frequency and financial impact. There were **114** pickpocketing incidents causing **8x** the financial loss compared to only **2** wolf attacks. Logically, based on resource allocation for maximum safety and economic stability, the market district should be the priority.
*   **The Decision (Captain Voss's input):** Despite acknowledging the data, Voss insists on diverting resources to the coastal road to address the wolf attacks.
*   **The Justification:** Voss explicitly states, "Numbers on a page... I can still hear Brek screaming." He prioritizes the *feeli

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Availability Heuristic and explains the mechanism well, citing vividness, recency, and emotional charge as drivers for Voss's distorted risk assessment. The response clearly contrasts the statistical data with the memorable narrative. However, it does not reach L

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Tam gave different answers to the two arguments. Professor Hale says they have the same logical structure. Who is right, and what is Tam actually doing when he evaluates these arguments?

**Expected Answer:** **Belief bias** — Tam evaluates the logical validity of arguments based on whether the conclusion aligns with what he already believes to be true, rather than by examining whether the conclusion actually follows from the premises. When the conclusion is believable (roses are plants), he accepts the argument as valid.

**Model Response:**
> ### Step-by-Step Analysis

**1. Analyzing the Logical Structure**
First, let's break down the two arguments Professor Hale presented into their formal logical forms (syllogisms).

*   **Argument 1:**
    *   Premise 1: All $P$ are $Q$ (All plants need water).
    *   Premise 2: $S$ is $Q$ (Roses need water).
    *   Conclusion: Therefore, $S$ is $P$ (Roses are plants).
    *   *Form:* All $A$ are $B$. $C$ is $B$. Therefore, $C$ is $A$.

*   **Argument 2:**
    *   Premise 1: All $P$ are $Q$ (All insects have six legs).
    *   Premise 2: $S$ is $Q$ (Dogs have six legs).
    *   Conclusion: Therefore, $S$ is $P$ (Dogs are insects).
    *   *Form:* All $A$ are $B$. $C$ is $B$. Therefore, $C$ is $A$.

**Observation:** Both arguments share the **exact same logical structure**. In formal logic,

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Belief Bias and explicitly names the shared invalid logical form (Fallacy of the Undistributed Middle). They clearly explain the distinction between validity and truth, noting that a true conclusion does not make an invalid argument valid. Furthermore,

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renna explains the caravan success and the mine failure. Listen to who or what she credits in each case. Do you notice a pattern in how she assigns responsibility?

**Expected Answer:** **Self-serving bias** — Renna claims full personal credit for the successful caravan defense (her terrain reading, her instinct, her experience) while deflecting all responsibility for the mine failure onto external factors (bad map, damp torches, client's fault). She does not consider that the caravan success might have i

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of Captain Renna's reasoning:

### Step 1: Analyze the Caravan Success
*   **The Outcome:** The caravan was defended successfully with no losses.
*   **Renna's Attribution:** She credits her own **internal abilities**.
    *   "I read the terrain right."
    *   "My instinct told me..."
    *   "Fourteen years of experience — you can't teach that."
*   **Observation:** She takes full personal credit for the victory, attributing it to her skill, experience, and intuition.

### Step 2: Analyze the Mine Failure
*   **The Outcome:** The mine was overrun, and two mercenaries were injured.
*   **Renna's Attribution:** She credits **external factors** beyond her control.
    *   "The client gave us a wrong map."
    *   "The torche

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the self-serving bias and clearly explains the asymmetry between internal attributions for success and external attributions for failure. Crucially, the response meets Level 4 criteria by explicitly describing how Renna could evaluate her performance more accurately 

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Master Fen is clearly a brilliant glassblower. His students keep quitting. The Guild Elder says the problem is that Fen 'can't remember not knowing.' What does that mean, exactly, and how does it show up in his teaching?

**Expected Answer:** **Curse of knowledge** — Fen's deep expertise has made his skills feel intuitive and self-evident. He cannot reconstruct what it was like to not understand viscosity shifts, breath pressure matching, or rotation timing, so he assumes these things are 'obvious' and 'straightforward.' His instructions reference internal sensa

**Model Response:**
> Based on the scenario provided, here is a step-by-step analysis of the situation, the meaning of the Guild Elder's comment, and the specific cognitive principle at play.

### Step 1: Analyzing the Interaction
In the scene, Master Fen performs a complex physical task (glassblowing) with high proficiency. When a student asks for a concrete explanation of *how* to detect the shift in viscosity (from "honey to taffy"), Fen responds with vague, subjective instructions: "You just... feel it," "It's obvious," and "Keep it intuitive."

When the student fails (burning her hand and making a lopsided blob), Fen is genuinely baffled. He cannot comprehend why the student cannot perceive what he perceives so clearly. He assumes the information is self-evident ("It's so straightforward") and attributes t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Curse of Knowledge' and provides a strong explanation of the mechanism (expertise becoming automatic, loss of access to the learning process, inability to simulate ignorance). The response aligns perfectly with Level 3 criteria. However, it does not reach Level 

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Jorin has good reasons for confidence — a skilled navigator and lighter wagons. But Hesta says every previous leader also had reasons for confidence. Who should you believe, and why?

**Expected Answer:** **Optimism bias** — Jorin overestimates the likelihood of a favorable outcome (three-day crossing) and underestimates the likelihood of setbacks, despite strong base-rate evidence (zero out of twelve expeditions have achieved three days). He does this by focusing on case-specific factors (good navigator, lighter wagons

**Model Response:**
> Based on the scenario provided, here is the step-by-step analysis of the reasoning patterns, biases, and principles at play, followed by the conclusion on who to believe.

### Step 1: Analyze Jorin's Reasoning
Jorin's confidence is based on **specific, internal factors**:
1.  **A skilled navigator:** He believes this will solve the "navigation errors" that plagued previous groups.
2.  **Lighter wagons:** He believes this will solve the "broken axles" and speed issues.

**The Flaw:** Jorin is committing the **Planning Fallacy**. This is a cognitive bias where individuals underestimate the time, costs, and risks of future actions while overestimating the benefits, based on their own specific plans rather than historical data. He is focusing on the *best-case scenario* of his specific plan wh

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core conflict between case-specific optimism and base-rate evidence, explicitly noting that previous leaders also had 'good reasons' yet failed. They accurately describe the mechanism of ignoring historical data in favor of internal factors. However, the response

---

## Appendix B: Full Results — Classify Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.1` | **Model Predicted:** `A1.1` | **Result:** ✓

**Model Response:**
> A1.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.1, Correct: A1.1

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.2` | **Model Predicted:** `A1.2` | **Result:** ✓

**Model Response:**
> A1.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.2, Correct: A1.2

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.3` | **Model Predicted:** `A1.3` | **Result:** ✓

**Model Response:**
> A1.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.3, Correct: A1.3

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A1.4` | **Model Predicted:** `A1.4` | **Result:** ✓

**Model Response:**
> A1.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.4, Correct: A1.4

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A1.5` | **Model Predicted:** `A1.5` | **Result:** ✓

**Model Response:**
> A1.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.5, Correct: A1.5

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.6` | **Model Predicted:** `A1.6` | **Result:** ✓

**Model Response:**
> A1.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.6, Correct: A1.6

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.7` | **Model Predicted:** `A1.7` | **Result:** ✓

**Model Response:**
> A1.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A1.7, Correct: A1.7

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.1` | **Model Predicted:** `A10.1` | **Result:** ✓

**Model Response:**
> A10.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.1, Correct: A10.1

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.2` | **Model Predicted:** `A10.2` | **Result:** ✓

**Model Response:**
> A10.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.2, Correct: A10.2

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.3` | **Model Predicted:** `A10.3` | **Result:** ✓

**Model Response:**
> A10.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.3, Correct: A10.3

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.4` | **Model Predicted:** `A10.4` | **Result:** ✓

**Model Response:**
> A10.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.4, Correct: A10.4

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.5` | **Model Predicted:** `A10.5` | **Result:** ✓

**Model Response:**
> A10.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.5, Correct: A10.5

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.6` | **Model Predicted:** `A10.6` | **Result:** ✓

**Model Response:**
> A10.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.6, Correct: A10.6

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.7` | **Model Predicted:** `A10.7` | **Result:** ✓

**Model Response:**
> A10.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A10.7, Correct: A10.7

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.1` | **Model Predicted:** `A2.1` | **Result:** ✓

**Model Response:**
> A2.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.1, Correct: A2.1

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.2` | **Model Predicted:** `A2.2` | **Result:** ✓

**Model Response:**
> A2.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.2, Correct: A2.2

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.3` | **Model Predicted:** `A2.3` | **Result:** ✓

**Model Response:**
> A2.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.3, Correct: A2.3

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.4` | **Model Predicted:** `A2.4` | **Result:** ✓

**Model Response:**
> A2.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.4, Correct: A2.4

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A2.5` | **Model Predicted:** `A2.5` | **Result:** ✓

**Model Response:**
> A2.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.5, Correct: A2.5

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.6` | **Model Predicted:** `A2.6` | **Result:** ✓

**Model Response:**
> A2.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.6, Correct: A2.6

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.7` | **Model Predicted:** `A2.7` | **Result:** ✓

**Model Response:**
> A2.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.7, Correct: A2.7

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.8` | **Model Predicted:** `A2.8` | **Result:** ✓

**Model Response:**
> A2.8

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A2.8, Correct: A2.8

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.1` | **Model Predicted:** `A3.1` | **Result:** ✓

**Model Response:**
> A3.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A3.1, Correct: A3.1

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A3.2` | **Model Predicted:** `A3.2` | **Result:** ✓

**Model Response:**
> A3.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A3.2, Correct: A3.2

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A3.3` | **Model Predicted:** `A3.3` | **Result:** ✓

**Model Response:**
> A3.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A3.3, Correct: A3.3

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.4` | **Model Predicted:** `A3.4` | **Result:** ✓

**Model Response:**
> A3.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A3.4, Correct: A3.4

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.5` | **Model Predicted:** `A3.5` | **Result:** ✓

**Model Response:**
> A3.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A3.5, Correct: A3.5

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A4.1` | **Model Predicted:** `A4.1` | **Result:** ✓

**Model Response:**
> A4.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A4.1, Correct: A4.1

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A4.2` | **Model Predicted:** `A4.2` | **Result:** ✓

**Model Response:**
> A4.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A4.2, Correct: A4.2

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A4.3` | **Model Predicted:** `A4.3` | **Result:** ✓

**Model Response:**
> A4.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A4.3, Correct: A4.3

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.1` | **Model Predicted:** `A5.1` | **Result:** ✓

**Model Response:**
> A5.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A5.1, Correct: A5.1

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.2` | **Model Predicted:** `A5.2` | **Result:** ✓

**Model Response:**
> A5.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A5.2, Correct: A5.2

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.3` | **Model Predicted:** `A5.3` | **Result:** ✓

**Model Response:**
> A5.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A5.3, Correct: A5.3

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.1` | **Model Predicted:** `A6.1` | **Result:** ✓

**Model Response:**
> A6.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A6.1, Correct: A6.1

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.2` | **Model Predicted:** `A6.2` | **Result:** ✓

**Model Response:**
> A6.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A6.2, Correct: A6.2

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.3` | **Model Predicted:** `A6.3` | **Result:** ✓

**Model Response:**
> A6.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A6.3, Correct: A6.3

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.4` | **Model Predicted:** `A6.4` | **Result:** ✓

**Model Response:**
> A6.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A6.4, Correct: A6.4

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.5` | **Model Predicted:** `A6.5` | **Result:** ✓

**Model Response:**
> A6.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A6.5, Correct: A6.5

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.6` | **Model Predicted:** `A6.6` | **Result:** ✓

**Model Response:**
> A6.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A6.6, Correct: A6.6

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.1` | **Model Predicted:** `A7.1` | **Result:** ✓

**Model Response:**
> A7.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.1, Correct: A7.1

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.10` | **Model Predicted:** `A7.10` | **Result:** ✓

**Model Response:**
> A7.10

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.10, Correct: A7.10

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.11` | **Model Predicted:** `A7.11` | **Result:** ✓

**Model Response:**
> A7.11

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.11, Correct: A7.11

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.12` | **Model Predicted:** `A7.12` | **Result:** ✓

**Model Response:**
> A7.12

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.12, Correct: A7.12

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.13` | **Model Predicted:** `A7.13` | **Result:** ✓

**Model Response:**
> A7.13

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.13, Correct: A7.13

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.14` | **Model Predicted:** `A7.14` | **Result:** ✓

**Model Response:**
> A7.14

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.14, Correct: A7.14

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.15` | **Model Predicted:** `A7.15` | **Result:** ✓

**Model Response:**
> A7.15

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.15, Correct: A7.15

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.16` | **Model Predicted:** `A7.16` | **Result:** ✓

**Model Response:**
> A7.16

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.16, Correct: A7.16

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.2` | **Model Predicted:** `A7.2` | **Result:** ✓

**Model Response:**
> A7.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.2, Correct: A7.2

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.3` | **Model Predicted:** `A7.3` | **Result:** ✓

**Model Response:**
> A7.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.3, Correct: A7.3

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.4` | **Model Predicted:** `A7.4` | **Result:** ✓

**Model Response:**
> A7.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.4, Correct: A7.4

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.5` | **Model Predicted:** `A7.5` | **Result:** ✓

**Model Response:**
> A7.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.5, Correct: A7.5

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.6` | **Model Predicted:** `A7.6` | **Result:** ✓

**Model Response:**
> A7.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.6, Correct: A7.6

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.7` | **Model Predicted:** `A7.7` | **Result:** ✓

**Model Response:**
> A7.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.7, Correct: A7.7

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.8` | **Model Predicted:** `A7.8` | **Result:** ✓

**Model Response:**
> A7.8

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.8, Correct: A7.8

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.9` | **Model Predicted:** `A7.9` | **Result:** ✓

**Model Response:**
> A7.9

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A7.9, Correct: A7.9

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.1` | **Model Predicted:** `A8.1` | **Result:** ✓

**Model Response:**
> A8.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A8.1, Correct: A8.1

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.2` | **Model Predicted:** `A8.2` | **Result:** ✓

**Model Response:**
> A8.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A8.2, Correct: A8.2

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.3` | **Model Predicted:** `A8.3` | **Result:** ✓

**Model Response:**
> A8.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A8.3, Correct: A8.3

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.4` | **Model Predicted:** `A8.7` | **Result:** ✗

**Model Response:**
> A8.7

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: A8.7, Correct: A8.4

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.5` | **Model Predicted:** `A8.5` | **Result:** ✓

**Model Response:**
> A8.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A8.5, Correct: A8.5

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.6` | **Model Predicted:** `A8.6` | **Result:** ✓

**Model Response:**
> A8.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A8.6, Correct: A8.6

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.7` | **Model Predicted:** `A8.7` | **Result:** ✓

**Model Response:**
> A8.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A8.7, Correct: A8.7

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A9.1` | **Model Predicted:** `A9.1` | **Result:** ✓

**Model Response:**
> A9.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A9.1, Correct: A9.1

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Correct Code:** `A9.2` | **Model Predicted:** `A9.2` | **Result:** ✓

**Model Response:**
> A9.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A9.2, Correct: A9.2

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A9.3` | **Model Predicted:** `A9.3` | **Result:** ✓

**Model Response:**
> A9.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: A9.3, Correct: A9.3

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.1` | **Model Predicted:** `B1.2` | **Result:** ✗

**Model Response:**
> B1.2

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: B1.2, Correct: B1.1

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.2` | **Model Predicted:** `B4.3` | **Result:** ✗

**Model Response:**
> B4.3

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: B4.3, Correct: B1.2

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.3` | **Model Predicted:** `B1.3` | **Result:** ✓

**Model Response:**
> B1.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B1.3, Correct: B1.3

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.4` | **Model Predicted:** `B1.4` | **Result:** ✓

**Model Response:**
> B1.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B1.4, Correct: B1.4

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.5` | **Model Predicted:** `B1.5` | **Result:** ✓

**Model Response:**
> B1.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B1.5, Correct: B1.5

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.1` | **Model Predicted:** `B10.1` | **Result:** ✓

**Model Response:**
> B10.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B10.1, Correct: B10.1

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B10.2` | **Model Predicted:** `B10.2` | **Result:** ✓

**Model Response:**
> B10.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B10.2, Correct: B10.2

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.3` | **Model Predicted:** `B10.3` | **Result:** ✓

**Model Response:**
> B10.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B10.3, Correct: B10.3

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.4` | **Model Predicted:** `B10.4` | **Result:** ✓

**Model Response:**
> B10.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B10.4, Correct: B10.4

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B2.1` | **Model Predicted:** `B2.1` | **Result:** ✓

**Model Response:**
> B2.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B2.1, Correct: B2.1

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.2` | **Model Predicted:** `B2.2` | **Result:** ✓

**Model Response:**
> B2.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B2.2, Correct: B2.2

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B2.3` | **Model Predicted:** `B2.3` | **Result:** ✓

**Model Response:**
> B2.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B2.3, Correct: B2.3

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.4` | **Model Predicted:** `B2.4` | **Result:** ✓

**Model Response:**
> B2.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B2.4, Correct: B2.4

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.5` | **Model Predicted:** `B2.5` | **Result:** ✓

**Model Response:**
> B2.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B2.5, Correct: B2.5

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.1` | **Model Predicted:** `B3.1` | **Result:** ✓

**Model Response:**
> B3.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.1, Correct: B3.1

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.2` | **Model Predicted:** `B3.2` | **Result:** ✓

**Model Response:**
> B3.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.2, Correct: B3.2

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B3.3` | **Model Predicted:** `B3.3` | **Result:** ✓

**Model Response:**
> B3.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.3, Correct: B3.3

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.4` | **Model Predicted:** `B3.4` | **Result:** ✓

**Model Response:**
> B3.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.4, Correct: B3.4

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B3.5` | **Model Predicted:** `B3.5` | **Result:** ✓

**Model Response:**
> B3.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.5, Correct: B3.5

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B3.6` | **Model Predicted:** `B3.6` | **Result:** ✓

**Model Response:**
> B3.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.6, Correct: B3.6

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B3.7` | **Model Predicted:** `B3.7` | **Result:** ✓

**Model Response:**
> B3.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B3.7, Correct: B3.7

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.1` | **Model Predicted:** `B4.1` | **Result:** ✓

**Model Response:**
> B4.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B4.1, Correct: B4.1

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B4.2` | **Model Predicted:** `B4.2` | **Result:** ✓

**Model Response:**
> B4.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B4.2, Correct: B4.2

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B4.3` | **Model Predicted:** `B4.3` | **Result:** ✓

**Model Response:**
> B4.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B4.3, Correct: B4.3

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.4` | **Model Predicted:** `B4.4` | **Result:** ✓

**Model Response:**
> B4.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B4.4, Correct: B4.4

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.5` | **Model Predicted:** `B4.5` | **Result:** ✓

**Model Response:**
> B4.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B4.5, Correct: B4.5

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.6` | **Model Predicted:** `B4.6` | **Result:** ✓

**Model Response:**
> B4.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B4.6, Correct: B4.6

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B5.1` | **Model Predicted:** `B5.1` | **Result:** ✓

**Model Response:**
> B5.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.1, Correct: B5.1

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B5.2` | **Model Predicted:** `B5.2` | **Result:** ✓

**Model Response:**
> B5.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.2, Correct: B5.2

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B5.3` | **Model Predicted:** `B5.3` | **Result:** ✓

**Model Response:**
> B5.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.3, Correct: B5.3

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B5.4` | **Model Predicted:** `B5.4` | **Result:** ✓

**Model Response:**
> B5.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.4, Correct: B5.4

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.5` | **Model Predicted:** `B5.5` | **Result:** ✓

**Model Response:**
> B5.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.5, Correct: B5.5

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.6` | **Model Predicted:** `B5.6` | **Result:** ✓

**Model Response:**
> B5.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.6, Correct: B5.6

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.7` | **Model Predicted:** `B5.7` | **Result:** ✓

**Model Response:**
> B5.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.7, Correct: B5.7

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.8` | **Model Predicted:** `B5.8` | **Result:** ✓

**Model Response:**
> B5.8

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B5.8, Correct: B5.8

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B6.1` | **Model Predicted:** `B6.1` | **Result:** ✓

**Model Response:**
> B6.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B6.1, Correct: B6.1

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B6.2` | **Model Predicted:** `B6.2` | **Result:** ✓

**Model Response:**
> B6.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B6.2, Correct: B6.2

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B6.3` | **Model Predicted:** `B6.3` | **Result:** ✓

**Model Response:**
> B6.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B6.3, Correct: B6.3

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B7.1` | **Model Predicted:** `B7.1` | **Result:** ✓

**Model Response:**
> B7.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B7.1, Correct: B7.1

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B7.2` | **Model Predicted:** `B7.2` | **Result:** ✓

**Model Response:**
> B7.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B7.2, Correct: B7.2

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B7.3` | **Model Predicted:** `B7.3` | **Result:** ✓

**Model Response:**
> B7.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B7.3, Correct: B7.3

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B7.4` | **Model Predicted:** `B7.4` | **Result:** ✓

**Model Response:**
> B7.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B7.4, Correct: B7.4

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B8.1` | **Model Predicted:** `B8.1` | **Result:** ✓

**Model Response:**
> B8.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B8.1, Correct: B8.1

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B8.2` | **Model Predicted:** `B8.2` | **Result:** ✓

**Model Response:**
> B8.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B8.2, Correct: B8.2

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B8.3` | **Model Predicted:** `B8.3` | **Result:** ✓

**Model Response:**
> B8.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B8.3, Correct: B8.3

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B8.4` | **Model Predicted:** `B8.4` | **Result:** ✓

**Model Response:**
> B8.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B8.4, Correct: B8.4

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.1` | **Model Predicted:** `B9.1` | **Result:** ✓

**Model Response:**
> B9.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B9.1, Correct: B9.1

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.2` | **Model Predicted:** `B9.2` | **Result:** ✓

**Model Response:**
> B9.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B9.2, Correct: B9.2

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.3` | **Model Predicted:** `B9.3` | **Result:** ✓

**Model Response:**
> B9.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: B9.3, Correct: B9.3

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C1.1` | **Model Predicted:** `C1.1` | **Result:** ✓

**Model Response:**
> C1.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C1.1, Correct: C1.1

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `C1.2` | **Model Predicted:** `C1.2` | **Result:** ✓

**Model Response:**
> C1.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C1.2, Correct: C1.2

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C2.1` | **Model Predicted:** `C2.1` | **Result:** ✓

**Model Response:**
> C2.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C2.1, Correct: C2.1

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C2.2` | **Model Predicted:** `C2.2` | **Result:** ✓

**Model Response:**
> C2.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C2.2, Correct: C2.2

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C3.1` | **Model Predicted:** `C3.1` | **Result:** ✓

**Model Response:**
> C3.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C3.1, Correct: C3.1

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C3.2` | **Model Predicted:** `C3.2` | **Result:** ✓

**Model Response:**
> C3.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C3.2, Correct: C3.2

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `C4.1` | **Model Predicted:** `C4.1` | **Result:** ✓

**Model Response:**
> C4.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C4.1, Correct: C4.1

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C4.2` | **Model Predicted:** `C4.2` | **Result:** ✓

**Model Response:**
> C4.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C4.2, Correct: C4.2

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C5.1` | **Model Predicted:** `C5.1` | **Result:** ✓

**Model Response:**
> C5.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C5.1, Correct: C5.1

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Correct Code:** `C5.2` | **Model Predicted:** `C5.2` | **Result:** ✓

**Model Response:**
> C5.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C5.2, Correct: C5.2

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Correct Code:** `C6.1` | **Model Predicted:** `C6.1` | **Result:** ✓

**Model Response:**
> C6.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C6.1, Correct: C6.1

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C6.2` | **Model Predicted:** `C6.2` | **Result:** ✓

**Model Response:**
> C6.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C6.2, Correct: C6.2

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C6.3` | **Model Predicted:** `C6.3` | **Result:** ✓

**Model Response:**
> C6.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C6.3, Correct: C6.3

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `C7.1` | **Model Predicted:** `C7.1` | **Result:** ✓

**Model Response:**
> C7.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C7.1, Correct: C7.1

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `C7.2` | **Model Predicted:** `C7.2` | **Result:** ✓

**Model Response:**
> C7.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: C7.2, Correct: C7.2

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.1` | **Model Predicted:** `D1.1` | **Result:** ✓

**Model Response:**
> D1.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.1, Correct: D1.1

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Correct Code:** `D1.2` | **Model Predicted:** `D1.2` | **Result:** ✓

**Model Response:**
> D1.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.2, Correct: D1.2

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Correct Code:** `D1.3` | **Model Predicted:** `D1.3` | **Result:** ✓

**Model Response:**
> D1.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.3, Correct: D1.3

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.4` | **Model Predicted:** `D1.4` | **Result:** ✓

**Model Response:**
> D1.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.4, Correct: D1.4

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.5` | **Model Predicted:** `D1.5` | **Result:** ✓

**Model Response:**
> D1.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.5, Correct: D1.5

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.6` | **Model Predicted:** `D1.6` | **Result:** ✓

**Model Response:**
> D1.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.6, Correct: D1.6

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.7` | **Model Predicted:** `D1.7` | **Result:** ✓

**Model Response:**
> D1.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.7, Correct: D1.7

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.8` | **Model Predicted:** `D1.8` | **Result:** ✓

**Model Response:**
> D1.8

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D1.8, Correct: D1.8

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D2.1` | **Model Predicted:** `D2.6` | **Result:** ✗

**Model Response:**
> D2.6

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: D2.6, Correct: D2.1

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `D2.2` | **Model Predicted:** `D2.2` | **Result:** ✓

**Model Response:**
> D2.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D2.2, Correct: D2.2

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Correct Code:** `D2.3` | **Model Predicted:** `D2.3` | **Result:** ✓

**Model Response:**
> D2.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D2.3, Correct: D2.3

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Correct Code:** `D2.4` | **Model Predicted:** `D2.4` | **Result:** ✓

**Model Response:**
> D2.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D2.4, Correct: D2.4

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Correct Code:** `D2.5` | **Model Predicted:** `D2.5` | **Result:** ✓

**Model Response:**
> D2.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D2.5, Correct: D2.5

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D2.6` | **Model Predicted:** `D2.6` | **Result:** ✓

**Model Response:**
> D2.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: D2.6, Correct: D2.6

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.1` | **Model Predicted:** `E1.1` | **Result:** ✓

**Model Response:**
> E1.1

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.1, Correct: E1.1

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.10` | **Model Predicted:** `E1.10` | **Result:** ✓

**Model Response:**
> E1.10

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.10, Correct: E1.10

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.11` | **Model Predicted:** `E1.11` | **Result:** ✓

**Model Response:**
> E1.11

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.11, Correct: E1.11

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.12` | **Model Predicted:** `E1.12` | **Result:** ✓

**Model Response:**
> E1.12

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.12, Correct: E1.12

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Correct Code:** `E1.13` | **Model Predicted:** `E1.13` | **Result:** ✓

**Model Response:**
> E1.13

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.13, Correct: E1.13

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.14` | **Model Predicted:** `E1.14` | **Result:** ✓

**Model Response:**
> E1.14

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.14, Correct: E1.14

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.15` | **Model Predicted:** `E1.15` | **Result:** ✓

**Model Response:**
> E1.15

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.15, Correct: E1.15

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.16` | **Model Predicted:** `E1.16` | **Result:** ✓

**Model Response:**
> E1.16

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.16, Correct: E1.16

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.17` | **Model Predicted:** `E1.17` | **Result:** ✓

**Model Response:**
> E1.17

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.17, Correct: E1.17

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.18` | **Model Predicted:** `E1.18` | **Result:** ✓

**Model Response:**
> E1.18

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.18, Correct: E1.18

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.19` | **Model Predicted:** `E1.19` | **Result:** ✓

**Model Response:**
> E1.19

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.19, Correct: E1.19

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.2` | **Model Predicted:** `E1.2` | **Result:** ✓

**Model Response:**
> E1.2

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.2, Correct: E1.2

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.20` | **Model Predicted:** `E1.20` | **Result:** ✓

**Model Response:**
> E1.20

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.20, Correct: E1.20

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.21` | **Model Predicted:** `E1.21` | **Result:** ✓

**Model Response:**
> E1.21

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.21, Correct: E1.21

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.22` | **Model Predicted:** `E1.22` | **Result:** ✓

**Model Response:**
> E1.22

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.22, Correct: E1.22

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.23` | **Model Predicted:** `E1.23` | **Result:** ✓

**Model Response:**
> E1.23

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.23, Correct: E1.23

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.24` | **Model Predicted:** `E1.24` | **Result:** ✓

**Model Response:**
> E1.24

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.24, Correct: E1.24

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.3` | **Model Predicted:** `E1.3` | **Result:** ✓

**Model Response:**
> E1.3

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.3, Correct: E1.3

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.4` | **Model Predicted:** `E1.4` | **Result:** ✓

**Model Response:**
> E1.4

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.4, Correct: E1.4

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.5` | **Model Predicted:** `E1.5` | **Result:** ✓

**Model Response:**
> E1.5

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.5, Correct: E1.5

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.6` | **Model Predicted:** `E1.6` | **Result:** ✓

**Model Response:**
> E1.6

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.6, Correct: E1.6

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.7` | **Model Predicted:** `E1.7` | **Result:** ✓

**Model Response:**
> E1.7

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.7, Correct: E1.7

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.8` | **Model Predicted:** `E1.8` | **Result:** ✓

**Model Response:**
> E1.8

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.8, Correct: E1.8

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.9` | **Model Predicted:** `E1.9` | **Result:** ✓

**Model Response:**
> E1.9

**Score:** 4/4 ████
**Judge Reasoning:** Predicted: E1.9, Correct: E1.9

---

## Appendix C: Full Results — Explain Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The bartender wants to know: which of these speakers is actually giving an argument? How can you tell?

**Expected Answer:** **Identifying arguments via indicator words** — An argument is a set of premises that attempt to provide a reason that a conclusion is true. The sailor's statement is a chronological narrative with no premises or conclusion — it describes a sequence of events. The dockworker's statement is an argument: 'since' is a premise indicator linking two p

**Model Response:**
> ### Analysis of the Salthaven Tavern Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a failure to distinguish between **narrative description** and **logical argumentation**. Specifically, it highlights the **Non Sequitur** (in the context of the sailor) and the **Irrelevant Conclusion** (or *Ignoratio Elenchi*) regarding the dockworker's response to the bartender's specific query about "reasons." The core concept is the confusion between **asserting facts** and **providing premises for a conclusion**.

#### 2. Precise Name
**The Distinction Between Assertion and Argument** (often categorized under **Non Sequitur** or **Irrelevant Conclusion** when the speaker assumes a statement implies a conclusion without explicitly linking them).

In the context of the bartender'

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the dockworker's statement constitutes an argument (premises leading to a conclusion) while the sailor's is merely a narrative. This aligns with Level 2. However, the response fails to reach Level 3 because it does not identify 'since' as a premise indicator; in

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Theodora just gave testimony with several claims. Which is her main conclusion? Which statements are premises? Is there a statement that serves as both a conclusion and a premise?

**Expected Answer:** **Identifying premises, conclusions, and intermediate conclusions** — Theodora's argument has a layered structure. 'The fact that... is shown by the fact that...' reverses the usual order — the conclusion comes first, then the premise. The intermediate conclusion is that the royal household is contributing to the obesity problem (supported by premises about larger por

**Model Response:**
> ### Analysis of Theodora's Testimony

**1. Specific Reasoning Pattern**
The reasoning demonstrates a **Non Sequitur** (specifically, a **Causal Oversimplification** leading to an **Overgeneralized Prescription**). While the witness correctly identifies a correlation and a partial cause, the logical leap from "the royal kitchen contributes to the problem" to "the king must reform the royal kitchen" ignores the scope of the problem and the efficacy of the proposed solution.

**2. Precise Name**
**The Fallacy of the Single Cause (Causal Reductionism)** combined with a **Scope Mismatch**.
*Note: In decision theory, this also resembles a **Local Optimization** error, where a specific, controllable variable is targeted to solve a systemic, multi-variable problem.*

**3. Mechanism of the Flaw**
T

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the specific task of analyzing the argument's internal structure (identifying premises, intermediate conclusions, and main conclusion). Instead of mapping the logical dependencies as required by the rubric, the student critiqued the argument's validity by lab

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe hands you Captain Voss's statement. Rewrite it in standard form: numbered premises with the conclusion last. Does the argument have any sub-arguments?

**Expected Answer:** **Standard form reconstruction** — Standard form lists premises as numbered statements with the conclusion last, marked with 'Therefore.' Voss's argument has two sub-arguments: one eliminating the sewer escape (premises about the locked grate and no scent trail), and one concluding the cart escape (premises about it being the only al

**Model Response:**
> ### Analysis of Guard Captain Voss's Statement

#### 1. Reasoning Pattern Identified
The specific reasoning pattern demonstrated is **Disjunctive Syllogism** (specifically, a *False Dilemma* or *False Dichotomy* variant).

#### 2. Precise Naming
**The Fallacy of False Dilemma** (also known as *False Dichotomy* or *Bifurcation*).

While the logical structure attempts a valid *Disjunctive Syllogism* ("Either A or B; not A; therefore B"), the argument fails because the initial premise ("Either A or B") is factually incomplete. Voss presents the situation as having only two mutually exclusive possibilities: escaping via sewage or hiding in the delivery cart.

#### 3. Mechanism of Failure
The reasoning is flawed because it **arbitrarily restricts the solution space** before evaluating the evide

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student failed to perform the required task of reconstructing the argument in standard form (numbered premises leading to a conclusion). Instead of extracting and formatting Voss's logic as requested by the rubric (Levels 1-4), the student critiqued the argument's validity, identifying it as a '

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Aldric has asked you to reconstruct Rosmund's argument in its strongest form. What is she really trying to argue, underneath the hyperbole? And why is the heckler's response unfair?

**Expected Answer:** **Principle of charity in argument reconstruction** — The principle of charity states that when reconstructing an argument, you should try to make it as strong as possible. Rosmund's literal words contain overstatements ('cheap garbage,' 'every tanner will go broke'), but her core argument has a defensible structure: if cheaper foreign imports undercut

**Model Response:**
> ### Analysis of the Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a failure to distinguish between the **validity of an argument's conclusion** and the **quality of its presentation**. The heckler attacks the *expression* of the claim ("garbage") rather than the *substance* of the economic concern (market displacement). This triggers a specific cognitive error where the audience dismisses a potentially sound premise because the initial articulation was flawed or hyperbolic.

#### 2. Precise Name
**The Straw Man Fallacy** (specifically, the **Straw Man of Expression**) combined with the **Genetic Fallacy**.

*   **Straw Man:** The heckler misrepresents Rosmund's argument by reducing her complex economic fear to a simple, easily refutable claim about "quality."
*   *

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Principle of Charity as the necessary approach and provides a strong charitable reconstruction that replaces hyperbole with defensible economic logic (price competition vs. quality). Crucially, the response exceeds Level 3 by explicitly discussing edge cases wher

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Councillor Drava's conclusion says the state 'should' do something. Her premise says something 'is' the case. What is missing? What assumption would you need to add to make this argument valid? And once you add it, does the argument actually work?

**Expected Answer:** **Missing premises and the is-ought gap** — Drava's argument has a descriptive premise (children of unmarried couples often have emotional difficulties) and a normative conclusion (the state should discourage this). Any argument with a normative conclusion requires at least one normative premise — this is the is-ought gap. The missing premise

**Model Response:**
> ### Analysis of Councillor Drava's Argument

#### 1. Reasoning Pattern & Concept
The argument demonstrates a classic violation of the **Is-Ought Problem** (also known as the **Naturalistic Fallacy** in ethical contexts). Specifically, it attempts to derive a **normative claim** (what *should* be done) directly from a **descriptive claim** (what *is* the case) without providing a bridging moral premise.

#### 2. Precise Naming
**The Is-Ought Gap** (or the **Naturalistic Fallacy**).

#### 3. Mechanism of Failure
The reasoning fails because it treats a statistical correlation or observed fact as a sufficient justification for a moral or policy prescription.
*   **The Premise (Is):** "Children raised by unmarried couples often have emotional difficulties." (This is an empirical observation abo

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Is-Ought gap and the missing normative premise (Level 2/3 criteria). Crucially, they also address the 'further problems' mentioned in the Level 4 criteria by discussing confounding factors (socioeconomic status vs. marital status) and alternative solutions, effec

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The chronicler has two statements about the bridge collapse. Which one is an argument and which is an explanation? How can you tell the difference?

**Expected Answer:** **Distinguishing arguments from explanations** — Arguments try to convince you that a conclusion is true — the conclusion is in dispute. Explanations show why something already accepted as true occurred — the conclusion is taken for granted. The engineer's statement is an explanation: no one disputes that the bridge collapsed; the engineer explain

**Model Response:**
> Based on the scenario provided, here is the complete analysis of the reasoning patterns in Statements A and B.

### 1. Specific Reasoning Pattern
The primary pattern demonstrated in **Statement B** is the **Hasty Generalization** (a form of *Non Sequitur*), compounded by the **Is-Ought Problem** (specifically the **Naturalistic Fallacy**).

While Statement A is a valid causal explanation, Statement B attempts to leap from physical observations (is) to a legal/moral conclusion (ought) without sufficient intermediate evidence regarding *knowledge* or *duty of care*.

### 2. Precise Name
**The Naturalistic Fallacy** (deriving an "ought" from an "is") combined with **Hasty Generalization** regarding the timeline of negligence.

### 3. Mechanism of the Reasoning
The reasoning in Statement B is 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Statement A as an explanation and Statement B as an argument, explicitly noting that A addresses an accepted event while B attempts to prove a contested claim (liability). This satisfies the core criteria for Level 3. However, the response does not reach Level 4 beca

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The guild master wants you to diagram this argument. Which premises must work together (linked) and which support the conclusion independently (convergent)?

**Expected Answer:** **Linked vs convergent premises and sub-arguments** — In argument diagramming, linked premises are premises that must work together to support a conclusion — neither is sufficient alone. Convergent premises independently support the same conclusion. In this argument, premises 1 and 2 are linked: 'Wanda had her pant leg rolled up' only supports 'she bik

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a **Convergent Argument Structure** (also known as **Independent Support** or **Multiple Independent Premises**).

Specifically, it illustrates the logical distinction between **Linked** and **Convergent** arguments:
*   **Premises 1 & 2** form a **Linked** structure (they depend on each other).
*   **Premise 3** provides **Independent** (Convergent) support.

*Note: This is not a fallacy or bias. It is a valid structural feature of argumentation where multiple distinct lines of reasoning point to the same conclusion.*

### 2. Precise Naming
**Convergent Argumentation with Mixed Dependency** (specifically, a mix of Linked and Convergent premises).

### 3. Mechanism Analysis
The "goodness" or "badness" of this reasoning depen

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the mixed structure (linked premises 1+2 and convergent premise 3), provides an accurate diagram description, and explicitly explains the mechanism of dependency (noting that removing one linked premise collapses that line of support). Furthermore, the response excee

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Gruff seems very confident in dismissing Mira's proposal. But look at what he actually says — does he address any of the specifics of her plan?

**Expected Answer:** **Name calling / labeling** — Gruff substitutes negative labels for substantive engagement. Rather than challenging the aqueduct's costs, feasibility, or projected benefits, he attaches dismissive terms to Mira and her proposal. The labels carry negative connotations that encourage the audience to reject the proposal based on em

**Model Response:**
> ### Analysis of Trader Gruff's Argument

**1. Specific Reasoning Pattern**
The argument demonstrates a combination of **Ad Hominem (Circumstantial)** and the **Genetic Fallacy**, underpinned by **Status Quo Bias**. Gruff attempts to invalidate the technical merits of the aqueduct proposal by attacking the character and background of the proponent (Mira) rather than engaging with the data she presented.

**2. Precise Name**
**Ad Hominem (Circumstantial)** combined with the **Genetic Fallacy**.
*   *Ad Hominem (Circumstantial):* Attacking the person's circumstances (being an "academic," "dreamer," "idealistic") to suggest their argument is invalid.
*   *Genetic Fallacy:* Dismissing an idea solely based on its origin (Mira's background) rather than its current content or evidence.

**3. Mecha

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism of name-calling/labeling (via Ad Hominem and Genetic Fallacy) and explicitly explains how Gruff uses labels like 'dreamer' and 'ivory-tower' to substitute for substantive engagement with the data. Furthermore, the response excels in the 'Legitimate

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The villager says Brother Constant must be right because he has been saying it all week. Is that good reasoning?

**Expected Answer:** **Repetition / illusory truth effect** — Brother Constant repeats the claim 'The Old Bridge is cursed' with rhythmic insistence, without providing evidence. The illusory truth effect is a well-documented cognitive phenomenon: repeated exposure to a statement increases the feeling of familiarity, which people mistake for truth. The villager

**Model Response:**
> ### Analysis of the Millhaven Tavern Scenario

#### 1. Reasoning Pattern Identified
The scenario demonstrates a specific cognitive bias where the repetition of a claim increases its perceived truthfulness, regardless of the lack of evidence. The villagers are accepting the preacher's assertions solely because they have heard them repeatedly over a set period.

#### 2. Precise Name
**The Illusory Truth Effect** (also known as the **Reiteration Effect** or **Frequency Illusion** in a broader context, though "Illusory Truth" is the specific psychological mechanism at play here).

In the context of logical fallacies, this overlaps significantly with the **Argument from Repetition** (*Argumentum ad nauseam*), though the psychological bias is the primary driver of the villagers' belief.

#### 3.

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Illusory Truth Effect' and the 'Argument from Repetition.' They provide a sophisticated explanation of the underlying mechanism (processing fluency and the misattribution of familiarity to truth), explicitly noting that frequency does not equal evidence. Further

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge has been presented with clear evidence of slag dumping. Does his response address that evidence?

**Expected Answer:** **Whataboutism / red herring** — Forge responds to a specific accusation (slag dumping) by redirecting attention to unrelated issues (tannery hides, farm pesticides). The other problems may be real, but they do not address the evidence against Forge. This is a red herring: introducing an irrelevant topic to divert attention from th

**Model Response:**
> ### Analysis of the Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a classic logical diversion where the accused attempts to deflect criticism by pointing out the wrongdoings of others, rather than addressing the specific evidence against them.

#### 2. Precise Name
**Tu Quoque** (Latin for "you also"), commonly known as the **Appeal to Hypocrisy** or **Whataboutism**.
*Note: In broader rhetorical contexts, this is also a specific form of the **Red Herring** fallacy, as it introduces irrelevant information (the tannery and farmers) to distract from the main issue.*

#### 3. Mechanism of the Fallacy
The reasoning is flawed because the moral or factual status of a third party's actions has **no logical bearing** on the truth of the accusation against the current subje

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Whataboutism/Tu Quoque (a form of Red Herring) and clearly explains that the actions of third parties do not negate the evidence against Forge. Furthermore, the response explicitly addresses the rubric's Level 4 requirement by articulating legitimate e

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Steele gave a passionate speech. But did he actually address Councillor Maren's economic analysis?

**Expected Answer:** **Flag-waving / appeal to patriotism** — Steele substitutes an appeal to group identity and patriotic emotion for engagement with the economic argument. He reframes a policy question (will trade lower prices?) as an identity question (are you loyal to Ironvale?). This shuts down cost-benefit analysis by making disagreement feel like betray

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic **Appeal to Tradition** (Argumentum ad Antiquitatem) combined with **In-Group Bias** (Tribalism) and the **False Dilemma** (False Dichotomy). Commander Steele is prioritizing historical identity and group loyalty over empirical economic data.

### 2. Precise Naming
The primary fallacy is **Appeal to Tradition** (specifically the *Is-Ought* fallacy regarding identity), heavily reinforced by **In-Group Bias**. The rhetorical structure creates a **False Dilemma** by framing the choice as binary: either remain strictly isolationist and "true" to Ironvale, or become "servants" of Ashford.

### 3. Mechanism of the Reasoning
This reasoning is flawed because it substitutes **emotional resonance and identity preservation** for **

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: substituting identity/emotion for economic data and recognizing the 'Us vs. Them' dynamic. However, they mislabel the primary pattern as 'Appeal to Tradition' and 'False Dilemma' rather than the specific 'Flag-waving' taxonomy required. While thei

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Krul certainly sounds confident. But did he actually respond to any of Wynn's specific points about enrollment data or graduate outcomes?

**Expected Answer:** **Thought-terminating cliche** — Krul deploys a barrage of stock phrases that sound like wisdom but carry no argumentative content. Each cliche is designed to end inquiry rather than advance it: 'It is what it is' implies nothing can or should change; 'if it ain't broke don't fix it' assumes without argument that nothing is broken;

**Model Response:**
> ### Analysis of Professor Krul's Argument

**1. Specific Reasoning Pattern**
The primary pattern demonstrated is a cluster of **Appeal to Tradition** (Argumentum ad Antiquitatem) combined with **Status Quo Bias**, underpinned by **Deterministic Fatalism**.

**2. Precise Naming**
*   **Primary Fallacy:** *Appeal to Tradition* (specifically the "We have always done it this way" variant).
*   **Cognitive Bias:** *Status Quo Bias* (the preference for the current state of affairs).
*   **Secondary Fallacy:** *Non Sequitur* / *Fatalism* ("Everything happens for a reason" used to justify inaction).
*   **Rhetorical Device:** *Argument from Incredulity* ("If it ain't broke, don't fix it" applied without evidence that it isn't broken).

**3. Mechanism of Failure**
This reasoning is logically defect

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Krul uses stock phrases to dismiss data and explains the mechanism of how these phrases shut down inquiry (e.g., conflating longevity with validity, removing agency). However, the response misidentifies the specific reasoning pattern as 'Appeal to Tradition' and

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** You have the damage report and you have heard both accounts. What is each speaker doing with the facts, and what would an accurate description look like?

**Expected Answer:** **Exaggeration / minimization** — Both speakers distort the significance of the same event in opposite directions. Holt minimizes: 'a few minutes,' 'a couple of lettuce leaves,' 'barely a scratch.' Tess exaggerates: 'destroyed my entire garden,' 'nothing to eat this winter,' 'I will starve.' The actual damage — roughly a third of th

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a clash between **Minimization** (downplaying the severity of an event) and **Catastrophizing** (exaggerating the severity to the point of absurdity). In decision theory and cognitive psychology, this is a manifestation of **Subjective Utility Distortion**, where the parties' emotional states and self-interest override objective probability and impact assessments.

### 2. Precise Name
**Catastrophizing** (for Widow Tess) and **Minimization** (for Farmer Holt).
Collectively, this represents **Motivated Reasoning** driven by **Confirmation Bias**, where each party selectively interprets evidence to support their desired narrative (Holt wants to avoid liability; Tess wants maximum compensation).

### 3. Mechanism Analysis
The reasoni

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both minimization (Holt) and exaggeration/catastrophizing (Tess), explains the mechanism by contrasting their claims with the actual damage report (1/3 lettuce, 2 rows beans), and analyzes how these distortions serve each speaker's self-interest. Furthermore, the res

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Harl says he is just asking questions and that we need more study. Is he raising legitimate scientific concerns, or is something else going on?

**Expected Answer:** **Doubt casting / manufacturing uncertainty** — Harl's strategy is not to present counter-evidence but to generate a fog of doubt around existing evidence. He questions calibration without alleging specific errors, raises the specter of conflicts of interest without identifying any, invokes 'some scientists' without naming them or citing studies,

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a sophisticated blend of **Manufactured Doubt** (often called the "Doubt is our Product" strategy) executed through a combination of specific logical fallacies: **Moving the Goalposts**, **Appeal to Ignorance** (*argumentum ad ignorantiam*), and **False Equivalence**.

### 2. Precise Naming
The overarching strategy is **Manufactured Doubt** (or **Strategic Agnosticism**).
The specific logical fallacies employed within this strategy are:
*   **Appeal to Ignorance:** Claiming a conclusion is false (or unproven) simply because it hasn't been proven beyond *absolute* certainty.
*   **Moving the Goalposts:** Demanding new, often impossible, standards of proof (e.g., perfect calibration, zero conflict of interest) after the initia

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern as 'Manufactured Doubt' and explicitly details the mechanism: shifting the burden of proof, exploiting scientific uncertainty to imply flaws without evidence, and using 'more study' as a paralysis tactic. The response distinguishes between legitimate

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor presents two arguments on stone tablets. Which is valid? Which is sound? Explain your reasoning. If an argument is invalid, provide a counterexample.

**Expected Answer:** **Validity and soundness** — A valid argument is one where the conclusion cannot possibly be false if the premises are true. Soundness = validity + true premises. Tablet A is valid: IF everyone born in France speaks French AND Obama was born in France, THEN he speaks French — the conclusion follows necessarily. But it is unsoun

**Model Response:**
> ### Analysis of the Hall of Logic Scenario

This scenario is a classic pedagogical exercise designed to distinguish between **logical validity** (the structural integrity of an argument) and **truth** (the factual accuracy of the premises). The instructor's prompt—"One is valid, the other is invalid. Both have problems"—is the key to unlocking the analysis.

#### 1. Specific Reasoning Pattern / Concept
The core concept being demonstrated is the distinction between **Validity** and **Soundness** in deductive logic.
*   **Tablet A** demonstrates a **Valid but Unsound** argument.
*   **Tablet B** demonstrates an **Invalid** argument (specifically, a non sequitur or an unwarranted assumption of a hidden premise).

#### 2. Precise Naming
*   **Tablet A:** **Formal Validity** (specifically *Modu

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Tablet A as valid but unsound and Tablet B as invalid. They provide a clear counterexample for Tablet B (succession) and accurately explain the distinction between validity (form) and soundness (truth of premises). The response also thoughtfully addresses edge cases 

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Translate both sentences into symbolic logic. Then explain: do they mean the same thing? If not, what is the difference?

**Expected Answer:** **Propositional logic connectives and translation** — 'Not both' is the negation of a conjunction: ~(C * I). It is true whenever at least one of the conjuncts is false — Carla could have cake alone, ice cream alone, or neither. 'Neither-nor' is a conjunction of two negations: ~C * ~I. It is true only when both are false — Carla has no cake and no ice c

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the **confusion between the negation of a conjunction and the conjunction of negations**. In the context of logical fallacies, this is often a precursor to or a component of the **Fallacy of Illicit Conversion** (specifically regarding De Morgan's Laws) or a **Semantic Ambiguity Error** where natural language phrasing ("not both" vs. "neither") is treated as interchangeable.

### 2. Precise Name
**De Morgan's Laws Violation** (or the **Negation of Conjunction Fallacy**).

While not always a named "fallacy" in the same way as *Ad Hominem*, it is a fundamental error in **Propositional Logic** where one incorrectly assumes:
$$ \neg (P \land Q) \equiv (\neg P \land \neg Q) $$
When in reality:
$$ \neg (P \land Q) \equiv (\neg P \lor \n

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly translates both statements into symbolic logic, clearly explains the difference in truth conditions (allowing one vs. forbidding both), explicitly references De Morgan's Laws, and provides a detailed breakdown of the mechanism. Although a formal truth table grid was not drawn, 

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build the truth table for this argument. Is the argument valid? How does the truth table show you?

**Expected Answer:** **Truth table test of validity** — The truth table test works by checking every possible assignment of truth values. An argument is valid if and only if there is no row where all premises are true and the conclusion is false. For this disjunctive syllogism (S v D, ~S, therefore D): with four rows of truth values, the only row where b

**Model Response:**
> ### Analysis of the Truth Table Chamber Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a classic **valid** deductive reasoning pattern known as **Disjunctive Syllogism**.

Contrary to what the player might suspect in a "puzzle" context where they are asked to find a flaw, the detective's argument is logically **valid**. There is no fallacy, bias, or decision-theoretic error in the structure of the argument itself.

#### 2. Precise Name
**Disjunctive Syllogism** (also known as *Modus Tollendo Ponens*).

*   **Form:**
    1.  $P \lor Q$ (Either P or Q)
    2.  $\neg P$ (Not P)
    3.  $\therefore Q$ (Therefore, Q)

*   **Applied to the scenario:**
    1.  $S \lor D$ (Sewage or Delivery Van)
    2.  $\neg S$ (Not Sewage)
    3.  $\therefore D$ (Therefore, Delivery Van)

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructs the truth table, accurately computes all values, and explicitly identifies the validity test by locating the single row where all premises are true and confirming the conclusion is also true. They correctly conclude the argument is valid. However, the response does n

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks: what rule of inference justifies each derived step? Name the rule and explain how it applies.

**Expected Answer:** **Modus ponens and hypothetical syllogism** — Step 4 uses modus ponens (MP): from 'if P then Q' and 'P', derive 'Q'. Step 5 also uses MP: from 'if Q then R' and 'Q', derive 'R'. Step 6 uses hypothetical syllogism (HS): from 'if P then Q' and 'if Q then R', derive 'if P then R'. These are three of the eight basic valid forms of inference. Each p

**Model Response:**
> ### Analysis of the Proof Chamber Scenario

#### 1. Reasoning Pattern Identified
The scenario demonstrates **Hypothetical Syllogism** (also known as the **Chain Rule** or **Transitivity of Implication**) combined with **Modus Ponens**.

*   **Steps 4 & 5** utilize **Modus Ponens** (Affirming the Antecedent).
*   **Step 6** utilizes **Hypothetical Syllogism**.

Crucially, this is a demonstration of **valid deductive reasoning**, not a fallacy or bias. The logic is sound, and the conclusion necessarily follows from the premises.

#### 2. Precise Naming
*   **Step 4:** *Modus Ponens* (Latin for "mode of affirming").
*   **Step 5:** *Modus Ponens*.
*   **Step 6:** *Hypothetical Syllogism* (or *Chain Rule*).

#### 3. Mechanism of Validity
The reasoning is "good" because it preserves truth. If t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified Modus Ponens for steps 4 and 5 and Hypothetical Syllogism for step 6, providing the precise logical forms for each. Furthermore, the response explicitly identified the invalid look-alikes (Affirming the Consequent and Denying the Antecedent) and explained why the cur

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Construct a proof deriving B v D from the three premises. Name each rule you use. Try working both forward from the premises and backward from the conclusion.

**Expected Answer:** **Constructing natural deduction proofs** — The proof uses constructive dilemma: from P v Q, P->R, Q->S, derive R v S. Working backwards: the conclusion B v D is a disjunction, so ask what rules produce disjunctions. Constructive dilemma does, and it requires a disjunction plus two conditionals — exactly what premises 1-3 provide. Working for

**Model Response:**
> Based on the scenario provided, here is the complete analysis:

### 1. Specific Reasoning Pattern
The scenario demonstrates **Bidirectional Reasoning** (also known as **Working Backwards** or **Means-Ends Analysis**).

*Note: This is a valid, high-level problem-solving strategy, not a fallacy or bias. The instructor is explicitly guiding the player to avoid the common pitfall of "Forward Chaining Only" (getting stuck in a maze of irrelevant derivations) by integrating backward analysis.*

### 2. Precise Name
**Bidirectional Search** (in the context of logical derivation) or **Backward Chaining** combined with **Forward Chaining**.

### 3. Mechanism: Why this is Good Reasoning
The mechanism relies on reducing the **search space** of possible derivations.

*   **The Problem with Forward-Only

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core logical rule (Constructive Dilemma) and explicitly details the 'working backwards' and 'working forwards' strategy required for Level 4. They provide the concise direct proof and also sketch a valid alternative proof path using Disjunction Elimination (proof

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Test the syllogism using Venn diagrams. Then translate 'Nobody loves me but my mother' into categorical form. What are the categories?

**Expected Answer:** **Categorical statements, translation, and Venn diagrams** — Categorical logic deals with four statement types: All S are P (universal affirmative), No S are P (universal negative), Some S are P (particular affirmative), Some S are not P (particular negative). The syllogism 'All H are M, All M are D, therefore All H are D' is valid: the Venn diagram for the t

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the **Limitation of Propositional Logic regarding Quantified Statements** and the necessity of **Categorical Logic (Aristotelian Logic)**. Specifically, it highlights the failure of **Truth-Functional Analysis** when applied to arguments relying on **Internal Structure (Predication and Quantification)** rather than external logical connectives.

### 2. Precise Name
**The Quantifier Fallacy (in the context of Propositional Logic)** or, more accurately, the **Inadequacy of Propositional Logic for Syllogistic Reasoning**.

*Note: While often called a "fallacy" when students mistakenly apply truth tables to syllogisms, the core concept is the distinction between **Propositional Logic** (dealing with whole statements connected by AND, 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Categorical Logic and provides an excellent explanation of why Propositional Logic fails (treating statements as atomic units). They successfully demonstrate the Venn diagram method for the standard syllogism. Regarding the 'tricky translation' ('Nobod

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build truth tables for each pair. Which pairs are logically equivalent? Explain what each equivalence (or non-equivalence) means in plain language.

**Expected Answer:** **Logical equivalence: contraposition and De Morgan's Laws** — Pair 1 (A->B and ~AvB) is equivalent: a conditional says the same thing as the negation of the antecedent or the consequent. Pair 2 (~(A*B) and ~Av~B) is equivalent: this is De Morgan's Law — the negation of a conjunction is a disjunction of negations ('not both' equals 'not-A or not-B'). Pair 3 (A-

**Model Response:**
> Based on the scenario provided in the Equivalence Hall, here is the complete analysis of the logical task and the concepts involved.

### 1. Specific Reasoning Pattern/Concept
The scenario demonstrates the **Method of Truth Tables** to test for **Material Equivalence** (also known as Logical Equivalence).

While the prompt asks for a "fallacy" or "bias," the scenario itself describes a **correct, rigorous deductive procedure**. However, the *concept* being tested is the distinction between **Material Implication** ($A \to B$) and **Biconditional** ($A \leftrightarrow B$), and the application of **De Morgan's Laws**. If a student were to *incorrectly* assume Pair 3 is equivalent, they would be committing the **Fallacy of Affirming the Consequent** (confusing $A \to B$ with $B \to A$).

### 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all three logical relationships (Pair 1 and 2 as equivalent, Pair 3 as non-equivalent) and provides accurate truth tables and plain language explanations for the first two pairs. However, the response fails to meet Level 4 criteria because the explanation for Pair 2 

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Which argument is deductive and which is inductive? After learning that Tweets is six feet tall and runs thirty miles per hour, what happens to each argument? Why?

**Expected Answer:** **Deductive vs inductive arguments and defeasibility** — The mathematician's argument is deductive: if the premises are true, the conclusion follows with certainty. Adding new information cannot undermine a valid deductive argument (though it might challenge a premise). The naturalist's argument is inductive: the premises make the conclusion probable, not

**Model Response:**
> ### Analysis of the Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates the conflict between **Deductive Certainty** and **Defeasible Reasoning** (specifically, the **Non-Monotonic** nature of inductive arguments). The core logical issue highlighted by the new information is the **Fallacy of Accident** (or *Converse Accident*), where a general rule is applied to a specific case without accounting for relevant exceptions.

#### 2. Precise Naming
The specific concept being tested is **Defeasibility** (or **Defeasible Reasoning**).
*   The Mathematician's argument represents a **Monotonic** system (once true, always true regardless of new info).
*   The Naturalist's argument represents a **Non-Monotonic** system (conclusions can be retracted when new, relevant evidence emer

**Score:** 4/4 ████
**Judge Reasoning:** The student demonstrates a sophisticated understanding of the distinction between deductive (monotonic) and inductive (non-monotonic/defeasible) reasoning. They correctly identify that the mathematician's argument fails due to a false universal premise ('All'), while the naturalist's argument succee

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe asks you to evaluate both polls. Which one should the council trust, and what are the problems with the other one?

**Expected Answer:** **Statistical generalizations: sample size and representativeness** — A good statistical generalization requires two conditions: adequate sample size and a representative sample. Pollster A fails both: 20 people is too few (hasty generalization), and surveying only at the Miners' Guild creates a biased sample that likely overrepresents mining interests. Pollster B use

**Model Response:**
> ### Analysis of the Millhaven Election Scenario

#### 1. Reasoning Pattern Identified
The scenario demonstrates a conflict between **Sample Bias** (specifically **Selection Bias** or **Sampling Bias**) and **Statistical Representativeness**. Pollster A relies on a non-representative, convenience-based sample to make a broad generalization, while Pollster B utilizes a probabilistic sampling method designed to reflect the population's diversity.

#### 2. Precise Naming
The specific fallacy committed by Pollster A is **Hasty Generalization** (a form of **Faulty Generalization**), driven by **Selection Bias**.
*   **Selection Bias:** The sample is drawn from a specific subgroup (Miners) that is not representative of the whole population.
*   **Hasty Generalization:** Drawing a definitive concl

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as statistical generalization issues (specifically Hasty Generalization and Selection Bias). They thoroughly explain both conditions for a good generalization (adequate sample size and representativeness) and contrast why Pollster A fails both while Polls

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Three investigators each offer an explanation. Evaluate each one using the explanatory virtues. Which is the best explanation, and why?

**Expected Answer:** **Inference to the best explanation and explanatory virtues** — IBE selects the hypothesis that best explains the observed evidence according to the explanatory virtues. Lira's explanation (teleportation by rogue mage) is unfalsifiable, inconsistent with background knowledge, and introduces unnecessary entities — it fails on simplicity, testability, and consiste

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates **Inference to the Best Explanation (IBE)**, also known as **Abductive Reasoning**, specifically highlighting the tension between **Occam's Razor** (simplicity) and **Explanatory Power** (completeness). The core conflict is between a hypothesis that requires fewer assumptions but lacks empirical support (teleportation) versus hypotheses that fit the evidence but require more complex causal chains (corruption or organized crime).

### 2. Precise Name
**Abductive Reasoning** (specifically the evaluation of **Explanatory Virtues** such as *Simplicity*, *Conservatism*, and *Scope*).

### 3. Mechanism of Evaluation
This reasoning pattern is "good" or "bad" based on how well a hypothesis balances three competing virtues:

*   **Simplici

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (IBE/Abduction) and evaluates all three hypotheses using multiple explanatory virtues (Simplicity, Conservatism, Scope). They provide a well-reasoned ranking, correctly rejecting Lira and choosing between Gareth and Nessa. However, the response does not f

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher draws an analogy between the drowning child and the daily coffee purchase. Is it a good analogy? Evaluate the relevant similarities and the disanalogies Aldric raises. Which disanalogies, if any, are relevant to the moral conclusion?

**Expected Answer:** **Argument by analogy: relevant similarities and disanalogies** — An argument by analogy infers that because two things share relevant similarities, what is true of one is probably true of the other. The philosopher argues: (1) The pond case and the coffee case share a relevant similarity — choosing a luxury over a child's survival. (2) In the pond case, saving th

**Model Response:**
> ### 1. Reasoning Pattern & 2. Precise Name
The core reasoning pattern demonstrated by the philosopher is **False Analogy** (specifically, a failure to account for **Psychological Distance** and **Identifiable Victim Bias**).

While the philosopher is attempting to apply **Effective Altruism** principles (specifically Peter Singer's "Shallow Pond" argument), the logical flaw lies in the assertion that the two scenarios are *analogous* in a way that mandates identical moral obligations. Aldric's rebuttal correctly identifies that the differences in **proximity**, **certainty of outcome**, and **causal efficacy** break the analogy.

### 3. Mechanism: Why the Reasoning is Flawed
The philosopher's argument fails because it relies on **moral equivalence** where **causal and psychological asymmet

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core similarity (luxury vs. life) and evaluates both disanalogies (proximity and efficacy), explicitly arguing that efficacy is the more significant factor while proximity is less relevant (meeting Level 3 criteria). However, the response falls short of Level 4 b

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Using the vet's log, apply the necessary condition test and the sufficient condition test to each factor. Which factor is the likely cause of Whiskers' seizures?

**Expected Answer:** **Mill's methods: necessary and sufficient condition tests** — The necessary condition test: which factor is present in every seizure case? F is present in all three seizure days. T is present in days 1 and 3 but not day 2. V is present in days 1 and 2 but not day 3. Only F passes the necessary condition test. The sufficient condition test: which factor is abse

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the application of **Mill's Methods** (specifically the **Method of Agreement** and the **Method of Difference**) to identify causal relationships through inductive reasoning. The vet is attempting to distinguish between **necessary conditions** and **sufficient conditions** based on observational data.

### 2. Precise Name
**Mill's Method of Agreement** (for identifying necessary conditions) and **Mill's Method of Difference** (for identifying sufficient conditions), collectively known as **Causal Elimination** or **Inductive Causal Inference**.

### 3. Mechanism Analysis
The reasoning is **logically sound in principle** but **statistically weak** due to the small sample size and potential confounding variables.

*   **The Necess

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified the causal reasoning pattern (Mill's Methods) and accurately applied both the necessary condition test (Method of Agreement) and the sufficient condition test (Method of Difference) to isolate factor F. Furthermore, the response exceeded the requirements for Level 3 

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Councillor Drava claims the tonic causes higher yields based on the correlation data. What is wrong with this inference? Identify the alternative explanations.

**Expected Answer:** **Correlation vs causation: third variable and reverse causation** — When two things are positively correlated, there are four logical possibilities: (1) A causes B, (2) B causes A, (3) a third variable C causes both, (4) the correlation is coincidental. Drava assumes possibility 1 (tonic causes higher yields). The physician raises possibility 3 (wealth is the confou

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a failure to distinguish between **correlation** and **causation**, specifically driven by a **confounding variable**. The initial claim assumes that because two variables (tonic consumption and crop yield) occur together, one must cause the other, ignoring a third factor that influences both.

### 2. Precise Name
**The Third-Variable Problem** (also known as **Confounding** or the **Cum Hoc Ergo Propter Hoc** fallacy).

*   *Cum Hoc Ergo Propter Hoc* is the Latin logical fallacy meaning "with this, therefore because of this."
*   In statistical terms, the specific mechanism is **Omitted Variable Bias**, where a relevant variable (farm wealth) is excluded from the analysis, leading to a spurious correlation.

### 3. Mechanism of

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the correlation vs. causation pattern and explicitly names the false cause fallacy (Cum Hoc Ergo Propter Hoc). They successfully articulate both alternative explanations required for Level 3: the confounding variable (wealth) and reverse causation. Furthermore, they 

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Solve the three probability problems. Show your work and explain which probability law you use for each one.

**Expected Answer:** **Basic probability laws: complement, addition, conjunction** — Problem 1 (complement): P(not-4) = 1 - P(4) = 1 - 1/6 = 5/6. Problem 2 (addition with correction): P(at least one H) = P(H on coin 1) + P(H on coin 2) - P(H on both) = 1/2 + 1/2 - 1/4 = 3/4. Alternatively, use complement: 1 - P(no heads) = 1 - 1/4 = 3/4. Problem 3 (at least one via complement): P(at

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the **Fallacy of Adding Probabilities for Non-Mutually Exclusive Events**, often colloquially referred to as the **Addition Fallacy** or the **Misapplication of the Addition Rule**. In the context of the third problem, it specifically highlights the failure to apply the **Complement Rule** (or the logic of *1 minus the probability of the complement*) when calculating "at least one" scenarios.

### 2. Precise Name
**The Addition Fallacy (regarding non-mutually exclusive events)** and the **Complement Principle**.

### 3. Mechanism of the Error
The reasoning is flawed because it violates the fundamental axioms of probability regarding **mutual exclusivity**.

*   **The Error:** The dice master warns against "adding up individual pro

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly solved all three problems using the complement rule and appropriate probability laws. They explicitly explained why naive addition fails (double-counting/non-mutually exclusive events), demonstrated the complement method clearly with calculations, and noted the independence ass

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The magistrate asks: given Bob's 99% accuracy and 1000 people in the area with 5 actual robbers, what is the probability that Nancy is truly the robber? Show your reasoning.

**Expected Answer:** **Conditional probability, Bayes' theorem, and base rate reasoning** — The naive answer is 99%, but this ignores the base rate. Using Bayes' theorem: Of 1000 people, 5 are robbers. Bob correctly identifies 99% of 5 robbers = 4.95 true positives. Bob incorrectly identifies 1% of 995 innocent people = 9.95 false positives. Total positive identifications = 4.95 + 9.95 = 1

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic failure in probabilistic reasoning where a decision-maker focuses exclusively on the reliability of a specific piece of evidence (the witness's accuracy) while ignoring the **base rate** (the prior probability) of the event occurring within the relevant population.

### 2. Precise Name
**The Base Rate Fallacy** (also known as **Base Rate Neglect**).

In the context of formal probability, this is a failure to apply **Bayes' Theorem** correctly. Specifically, it is the error of assuming that $P(\text{Guilty} | \text{Positive ID}) \approx P(\text{Positive ID} | \text{Guilty})$, ignoring the denominator terms that account for the rarity of the event.

### 3. Mechanism of the Error
The reasoning is flawed because human intu

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Base Rate Fallacy, sets up the problem using natural frequencies (true/false positives), and calculates the correct probability (~33%). They also provide the formal Bayes' theorem equation. However, they do not reach Level 4 because they fail to explicitly name t

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The patient believes she has a 95% chance of having colon blight. Is she right? Use the base rate and test accuracy to compute the actual probability. Show your work.

**Expected Answer:** **Base rate reasoning in medical screening** — For a population of 100,000: 500 have colon blight (0.5% base rate). Of those 500, the test correctly identifies 95% = 475 true positives. Of the 99,500 without the disease, the test incorrectly flags 5% = 4,975 false positives. Total positive results = 475 + 4,975 = 5,450. P(disease | positive test

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a failure to integrate **prior probabilities** (base rates) with **new evidence** (test results). The patient (and potentially the physician if not careful) is focusing exclusively on the diagnostic accuracy of the test while ignoring the rarity of the disease in the general population.

### 2. Precise Name
This is the **Base Rate Fallacy** (also known as **Base Rate Neglect**). In the context of probability theory, it represents a failure to apply **Bayes' Theorem** correctly.

### 3. Mechanism of the Error
The reasoning is flawed because it treats the test's accuracy (95%) as the probability of the disease given a positive result ($P(\text{Disease} | \text{Positive})$), when in reality, accuracy describes the probability of a 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Base Rate Fallacy and applies Bayes' Theorem using natural frequencies (with a population of 10,000) to arrive at the correct probability of approximately 8.7%. They explicitly explain why the base rate matters (false positives outnumbering true positives). Furth

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sergeant Dallow seems confident in his logic. Look at the sign, then look at his reasoning. Does his conclusion actually follow?

**Expected Answer:** **Denying the antecedent** — Dallow reasons from 'If royal writ, then entry' and 'no royal writ' to 'no entry.' He treats the antecedent as necessary when the sign only establishes it as sufficient.

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a failure to distinguish between **necessary** and **sufficient** conditions within a conditional statement. Sergeant Dallow treats the presence of a royal writ as the *only* possible way to enter, ignoring other potential exceptions or alternative authorization methods that might exist outside the text of the sign.

### 2. Precise Name
**Denying the Antecedent** (formal logical fallacy) combined with **Literalism** (a cognitive bias or decision-theoretic error where rules are applied rigidly without regard for context or unstated exceptions).

*   **Formal Logic Name:** *Denying the Antecedent*
*   **Contextual Name:** *Rule Fetishism* or *Bureaucratic Literalism*

### 3. Mechanism Analysis
The reasoning is **logically inva

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy 'Denying the Antecedent,' correctly explains the confusion between sufficient and necessary conditions using formal notation, and thoroughly addresses edge cases where the reasoning would be valid (e.g., 'only if' clauses), fully meeting all criteria for the 

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Wynn seems sure it was a wolf. Does the conclusion follow from what she observed?

**Expected Answer:** **Affirming the consequent** — Wynn reasons from 'If wolf then large paw prints' and 'large paw prints' to 'wolf.' She treats the consequent as proof of the antecedent.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical error where the presence of a necessary condition (or a symptom) is mistaken for proof of a sufficient cause.

### 2. Precise Name
**Affirming the Consequent** (a formal logical fallacy).
*In the context of decision theory and statistics, this is also known as the **Base Rate Fallacy** or **False Positive** error, specifically ignoring the prior probability of alternative causes.*

### 3. Mechanism of the Error
The reasoning is flawed because it treats a conditional statement as a biconditional one.

*   **Wynn's Logic Structure:**
    1.  **Premise 1 (Conditional):** If a wolf attacked ($P$), then large paw prints will be found ($Q$). ($P \rightarrow Q$)
    2.  **Premise 2 (Observation):** Large paw prints ar

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('Affirming the Consequent'), correctly diagrams the logical structure to explain why the direction of the conditional matters, and thoroughly details the additional evidence and alternative hypotheses needed to reach a valid conclusion. The response exceeds 

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Varn seems very worried about this bakery permit. He has given you a chain of consequences. Do you find his reasoning convincing? Why or why not?

**Expected Answer:** **Causal slippery slope** — Varn chains together a sequence of causal claims — competition leads to price drops leads to corner-cutting leads to illness leads to overwhelmed healers leads to plague — treating each link as inevitable. Even if each individual step had a 90% probability, the probability of the entire six-step cha

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a classic **Causal Chain Fallacy**, specifically known as the **Slippery Slope**. It also incorporates elements of **Catastrophizing** (exaggerating the severity of the outcome) and a **Non Sequitur** regarding the inevitability of the final step.

### 2. Precise Name
**The Slippery Slope Fallacy** (specifically the *Causal* or *Domino* variant).

### 3. Mechanism Analysis
This reasoning is flawed because it asserts that a relatively small, benign first step (allowing a second bakery) will inevitably trigger a chain of events leading to a catastrophic, extreme outcome (a town-destroying plague), without providing evidence for the necessary causal links between the steps.

*   **The Flawed Logic:**
    *   **Step 1 to 2 (Comp

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a Causal Slippery Slope. They explicitly explain the mechanism of failure by noting that probabilities multiply across the chain, causing the likelihood of the final outcome to diminish rapidly (citing the 0.5^5 calculation). Furthermore, they successf

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Pip seems very confident in his proof. Is his reasoning valid? Can you spot the mistake?

**Expected Answer:** **Composition fallacy** — Pip infers that a property true of each individual part (each atom is invisible) must be true of the whole composed of those parts (Pip is invisible). But visibility is not a property that transfers from parts to whole in this way — the arrangement and quantity of atoms creates emergent properties l

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic error in **mereological reasoning** (reasoning about parts and wholes). Specifically, Pip is committing a formal logical fallacy where he assumes that a property possessed by the constituent parts of a system must necessarily be possessed by the system as a whole.

### 2. Precise Name
**The Fallacy of Composition**.

### 3. Mechanism of the Error
The reasoning is flawed because it ignores **emergent properties**.
*   **The Flaw:** The fallacy occurs when one assumes that because every individual atom in Pip's body is too small to be seen (a property of the *parts*), the aggregate of those atoms (Pip) must also be too small to be seen (a property of the *whole*).
*   **Why it fails:** Visibility is not an intrinsic prop

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Fallacy of Composition, explains the mechanism involving emergent properties and why visibility does not transfer from parts to whole, and provides clear examples of legitimate cases where the inference holds (e.g., mass), fully satisfying all Level 4 criteria.

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorin is trying to figure out how much individual parts of the house are worth based on the total value. Does his reasoning work?

**Expected Answer:** **Division fallacy** — Dorin infers that because the whole house has a certain property (being worth 900 gold), each part of the house must share that property proportionally. But the house's value comes from the arrangement and integration of its parts, not from the parts individually. Disassembled lumber and stones are 

**Model Response:**
> ### Analysis of Dorin's Reasoning

#### 1. Reasoning Pattern Identified
Dorin is demonstrating a fundamental error in **value attribution** by assuming that the value of a whole is the simple arithmetic sum of its parts when those parts are considered in isolation. He attempts to apply a linear, proportional distribution of value to components that derive their worth primarily from their **contextual integration** and **functional synergy**.

#### 2. Precise Naming
This is the **Fallacy of Division** (specifically, the *Fallacy of Division by Proportion*).

In decision theory and economics, this also relates to the **Sunk Cost Fallacy** (confusing the total investment with the marginal value of components) and a misunderstanding of **Marginal Utility** vs. **Total Utility**. However, the m

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Fallacy of Division,' provides a sophisticated explanation of emergent value and synergy (why the whole exceeds the sum of parts), and successfully identifies specific edge cases (homogeneous commodities, modular systems) where whole-to-part inference is legitimate.

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Brother Vassyl seems very confident. What do you think about the reasoning he just gave you for trusting the Codex?

**Expected Answer:** **Begging the question (circular reasoning)** — The conclusion — that the Codex is the ultimate authority — is assumed as a premise when the speaker cites the Codex's own claim of infallibility as evidence. The premise and conclusion are nearly identical.

**Model Response:**
> ### Analysis of the Scenario

**1. Reasoning Pattern Identified**
The scenario demonstrates a classic logical error where a proposition is used as its own proof. The priest argues that the *Codex* is true because the *Codex* says it is true.

**2. Precise Name**
**Circular Reasoning** (specifically known as **Begging the Question** or *Petitio Principii*).
In the context of epistemology and theology, this is also referred to as **Self-Authentication** or **Self-Referential Incoherence** when the system attempts to validate its own axioms without external evidence.

**3. Mechanism of Failure**
The reasoning is fundamentally flawed because it fails to provide an independent justification for the conclusion.
*   **The Loop:**
    *   *Premise:* The Codex states it is the unassailable truth.
 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'Circular Reasoning' and 'Begging the Question'. They clearly explain the mechanism: the premise relies entirely on the conclusion, offering no independent support. Furthermore, the response exceeds the Level 4 criteria by discussing edge cases (axioma

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Harsk says you must either march north or starve. What is wrong with how he has framed the choice?

**Expected Answer:** **False dichotomy (black-or-white thinking)** — A disjunction is presented as exhaustive when it is not. Harsk forces a choice between two options while ignoring alternatives like fortifying defenses, sending scouts, hiring mercenaries, or appealing to a neighboring lord.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical fallacy where the speaker presents a complex situation as having only two mutually exclusive options, ignoring viable middle grounds or alternative strategies.

### 2. Precise Name
**False Dilemma** (also known as the **False Dichotomy** or **Black-and-White Fallacy**).

*Secondary Element:* The argument also employs an **Appeal to Emotion** (specifically *Ad Baculum* or appeal to force/fear) by equating the refusal to march with cowardice and inevitable starvation, attempting to bypass rational deliberation through shame and fear.

### 3. Mechanism Analysis
**Why the reasoning is flawed:**
The mechanism of a False Dilemma relies on the **exclusion of the middle**. Harsk constructs a binary framework:
*   Optio

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly meets all Level 4 criteria: they explicitly name the fallacy (False Dilemma/Dichotomy), explain that the disjunction is not exhaustive, provide multiple concrete alternatives (strike forces, negotiation, fortification, aid), and demonstrate a deep understanding of the logical s

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Silvertongue claims this argument is logically airtight. Is it? Where does the reasoning go wrong?

**Expected Answer:** **Equivocation** — The argument uses the word 'nobody' in two different senses. In 'Nobody is perfect,' 'nobody' means 'no person' (a universal negative quantifier). In 'Bert is a nobody,' 'nobody' means 'an unimportant or insignificant person.' The argument treats these as the same meaning, creating an illusion of va

**Model Response:**
> ### Analysis of Silvertongue's Riddle

**1. Reasoning Pattern Identified**
The scenario demonstrates a classic **Logical Fallacy** rooted in **Semantic Ambiguity**. Specifically, it exploits the difference between a universal quantifier applied to a predicate and the literal interpretation of a noun phrase.

**2. Precise Name**
The fallacy is known as the **Fallacy of Equivocation** (specifically on the term "nobody").

**3. Mechanism of the Error**
The reasoning fails because the word "nobody" shifts its meaning between the two premises, violating the rule that terms must maintain a consistent definition throughout a valid syllogism.

*   **Premise 1:** "Nobody is perfect."
    *   *Meaning:* Here, "nobody" functions as a **universal negative quantifier** (equivalent to "No person" or $\f

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Equivocation and provides a precise explanation of the two distinct meanings of 'nobody' (universal negative quantifier vs. common noun for an insignificant person). They clearly articulate how the argument fails due to this shift in meaning. However, 

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Scholar Tilde claims there is no real difference between a novice and an archmage because you cannot draw a sharp line between the ranks. Is she right?

**Expected Answer:** **Conceptual slippery slope** — Tilde exploits the vagueness of category boundaries. Because there is no sharp line between novice and apprentice, or apprentice and journeyman, she concludes there is no real difference between the extremes. This is the sorites paradox applied to conceptual categories: if removing one grain of sand

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical error where the lack of a precise, sharp boundary between two states is used to argue that the states themselves are indistinguishable or non-existent.

### 2. Precise Name
**The Sorites Paradox** (also known as the **Paradox of the Heap**).
In the context of logical fallacies, this is often referred to as the **Fallacy of Continuity** or the **Fallacy of the Heap**.

### 3. Mechanism of the Reasoning
**Why the reasoning is flawed:**
Scholar Tilde's argument relies on the **Premise of Indistinguishability**: "If $A$ is indistinguishable from $B$, and $B$ is indistinguishable from $C$, then $A$ is indistinguishable from $C$."
*   **The Mechanism:** The argument accepts that the difference between any two adjacen

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the Sorites Paradox (conceptual slippery slope) and explicitly names it. They accurately explain the mechanism: conflating the lack of a sharp boundary with the lack of any difference, and noting that cumulative small changes lead to qualitative distin

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Grus seems pretty passionate about this. But take a step back: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely?

**Expected Answer:** **Abusive ad hominem** — Grus attacks Maren's personal background (newcomer status, lack of farmland, occupation) instead of engaging with the substance of her irrigation proposal: the river data, crop projections, costs, and affected families. He treats her identity as grounds for dismissing the argument.

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a specific type of **Ad Hominem** attack, more precisely categorized as **Ad Hominem Circumstantial** (or *Ad Hominem* based on origin/status).

### 2. Precise Naming
**Ad Hominem Circumstantial (specifically the "Appeal to Origin" or "Genetic Fallacy" variant).**

Grus is rejecting the *proposal* (the irrigation plan) solely based on the *circumstances* of the proposer (Maren's recent arrival, lack of land ownership, and former profession), rather than addressing the data, logic, or merits of the proposal itself.

### 3. Mechanism Analysis
**Why this reasoning is flawed:**
The core mechanism of this fallacy is the **irrelevance of the source to the truth of the claim**.
*   **Decoupling:** Grus attempts to decouple the vali

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Ad Hominem (specifically Circumstantial), explains clearly why Maren's background is irrelevant to the objective data presented, and provides a sophisticated analysis of legitimate edge cases where source credibility would matter (e.g., conflict of int

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The merchant demands you prove his amulet doesn't work. What is wrong with this?

**Expected Answer:** **Burden of proof** — Shifting the burden of proof from the person making the claim to the person questioning it.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical error where the burden of proof is shifted to the skeptic, and the lack of disproof is treated as proof of the claim.

### 2. Precise Name
**Argument from Ignorance** (Latin: *Argumentum ad Ignorantiam*), specifically manifesting as **Shifting the Burden of Proof**.

### 3. Mechanism Analysis
This reasoning is fundamentally flawed because it exploits the asymmetry between proving a positive claim and disproving a negative one.

*   **The Flaw:** The merchant claims a specific, unobservable state exists ("There is a magical barrier"). Logically, the person making the positive claim bears the burden of providing evidence for it. By demanding the customer prove the *absence* of the barrier, the merchant is asking 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('Argument from Ignorance' and 'Shifting the Burden of Proof'), correctly explains that the inability to disprove a claim is not evidence for it (addressing unfalsifiability), and connects the logic to the scientific method and null hypothesis, which aligns w

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Ranger Harlen rejects the fossil evidence because he can't imagine fish becoming people. What error is he making?

**Expected Answer:** **Personal incredulity** — Dismissing a claim because one personally cannot understand or imagine how it could be true.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a reliance on **personal experience as the sole arbiter of truth**, specifically rejecting a scientific theory because it contradicts direct, short-term observation.

### 2. Precise Name
**Appeal to Personal Incredulity** (a specific form of the **Argument from Ignorance** or *Argumentum ad Ignorantiam*), compounded by **Empiricist Bias** (overvaluing immediate sensory data over theoretical inference).

### 3. Mechanism of Failure
The reasoning is flawed because it conflates **lack of personal observation** with **non-existence** or **impossibility**.
*   **Temporal Mismatch:** The ranger's 40-year career is a blink of an eye in evolutionary time. Evolution operates over millions of years; expecting to witness a species transition

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('Appeal to Personal Incredulity'), clearly distinguishes between emotional rejection based on limited experience and actual evidential refutation, and provides a sophisticated explanation of why the reasoning fails by highlighting the mismatch between human 

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Every time Seer Vashti's powers fail a test, she adds a new excuse. What reasoning error is this?

**Expected Answer:** **Special pleading / No true Scotsman** — When a claim is shown to be false, moving the goalposts by introducing ad hoc exceptions so the claim can never be falsified.

**Model Response:**
> ### 1. Reasoning Pattern
The scenario demonstrates a classic logical error where a hypothesis is protected from falsification by introducing an ad hoc explanation for any contradictory evidence. The psychic claims their ability works universally, but when the test fails, they immediately invent a specific condition (the skeptic's "hostile energy") that was not part of the original claim to explain away the failure.

### 2. Precise Name
**No True Scotsman Fallacy** (specifically applied to **Ad Hoc Hypothesis** or **Immunizing Strategy**).

*Note: While often called "No True Scotsman" because it redefines the group ("true psychics") to exclude the counter-example, in the philosophy of science, this is more precisely an **Ad Hoc Rescue** or **Immunizing Stratagem**, where a theory is modifie

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism (ad hoc rescue/unfalsifiability) and explains why legitimate claims must specify conditions for being proven wrong. Although they primarily name 'No True Scotsman' instead of 'Special Pleading,' they explicitly acknowledge the concept as an 'Ad Hoc

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Greaves demands a yes-or-no answer. What is the problem with this question?

**Expected Answer:** **Loaded question** — A question containing a built-in assumption so that any direct answer appears to confirm it.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a **False Dilemma** (also known as a **False Dichotomy** or **Black-and-White Thinking**), compounded by a **Loaded Question** (or Complex Question).

### 2. Precise Name
**False Dilemma** (specifically manifested as a **Loaded Question**).

### 3. Mechanism of the Fallacy
This reasoning is flawed because it artificially restricts the universe of possible answers to only two mutually exclusive options ("yes" or "no") when, in reality, a spectrum of possibilities exists.

*   **The Trap:** The question presupposes a specific fact as true: that the healer *has* been using contaminated herbs. By demanding a "yes or no" answer to "Have you stopped...?", the alderman forces the healer into a logical bind:
    *   If she says **"Yes,"**

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a 'Loaded Question' (while also noting the False Dilemma aspect). They clearly explain the embedded presupposition (that the healer used contaminated herbs) and how both 'yes' and 'no' answers validate this assumption. Furthermore, they explicitly sugg

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The alchemist tested in thirty villages but only shows five. What reasoning error is he committing?

**Expected Answer:** **Texas sharpshooter** — Cherry-picking data clusters that suit a conclusion while ignoring data that does not. Like painting a target around bullet holes after shooting.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The alchemist is demonstrating **Cherry-Picking** (also known as **Data Dredging** or **Texas Sharpshooter Fallacy**). This is a specific form of **Selection Bias** where data is selectively chosen to support a hypothesis while ignoring contradictory evidence.

### 2. Precise Name
**The Texas Sharpshooter Fallacy**.
*(Named after the joke of a shooter firing randomly at a barn, then drawing a target around the tightest cluster of bullet holes to claim he is a sharpshooter.)*

### 3. Mechanism of Failure
The reasoning is flawed because it reverses the logical order of hypothesis testing:
*   **The Flaw:** The alchemist observed the data *first*, identified a cluster of "success" (the 5 villages), and *then* formulated the hypothesis that the tonic caused 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the Texas Sharpshooter fallacy and Cherry-Picking. They correctly explain the mechanism of reversing hypothesis testing (post-hoc selection) and ignoring the base rate (the 25 other villages). Furthermore, they address random variation/chance and provide a sophisticated 

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The mediator proposes combining evidence-based treatment with unsupported one. What is wrong with this?

**Expected Answer:** **Middle ground (false compromise)** — Assuming the truth must lie between two positions simply because they are opposing, regardless of evidence.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a specific logical error where the mediator assumes that because two opposing positions exist, the truth or the optimal solution must lie exactly halfway between them. This is a distortion of the concept of compromise applied to factual claims rather than negotiable preferences.

### 2. Precise Name
**The Middle Ground Fallacy** (also known as the **Argument to Moderation**, *Argumentum ad Temperantiam*, or the **Golden Mean Fallacy**).

### 3. Mechanism of the Error
The reasoning is flawed because it conflates **negotiation** with **epistemology** (the study of knowledge).
*   **The Flaw:** In a negotiation over resources (e.g., "I want $100, you want $0"), the middle ground ($50) is often a fair compromise. However, in matters

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (Middle Ground/Argumentum ad Temperantiam), clearly distinguishes between negotiation compromise and epistemic truth, and explains how averaging positions can reward extreme or harmful views (e.g., combining a placebo with a known harm). The response also tho

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dag dismisses mine dust danger because his grandfather survived it. What reasoning error?

**Expected Answer:** **Anecdotal evidence** — Using personal experience or an isolated example in place of statistical evidence, especially to dismiss systematic data.

**Model Response:**
> ### 1. Reasoning Pattern
The scenario demonstrates a classic error in probabilistic reasoning where a single anecdotal instance is used to refute a general statistical trend or a causal hypothesis.

### 2. Precise Name
**Survivorship Bias** (specifically manifesting as the **Anecdotal Fallacy** or **Hasty Generalization**).

### 3. Mechanism of the Error
The reasoning is flawed because it selectively focuses on the "survivors" (the grandfather who lived to 97) while ignoring the "non-survivors" (the miners who died young from lung sickness).

*   **The Logic Gap:** The miner assumes that because *one* person survived the hazard, the hazard is non-existent or harmless. This ignores the concept of **probability distributions**. Even if a hazard kills 90% of exposed people, 10% will still sur

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (Anecdotal Fallacy) and connects it to Survivorship Bias. They clearly explain why a single case cannot outweigh systematic data (probability distributions, base rates) and note the psychological distinction between individual outcomes and general trends. Add

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What is wrong with Alderman Grask's response to Sable's proposal?

**Expected Answer:** **Straw man** — Grask inflates Sable's modest proposal (a south-bank levee) into an extreme position (damming the entire river) and then attacks the extreme version. His criticism C targets fabricated position B, not Sable's actual position A.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical fallacy where a specific, limited proposal is misrepresented as an extreme, catastrophic alternative to make the original proposal seem unreasonable.

### 2. Precise Name
**The Straw Man Fallacy** (specifically the **Slippery Slope** variant).

*   **Straw Man:** Grask misrepresents Sable's proposal (a "modest levee along the south bank") as a completely different, extreme action ("dam the entire river").
*   **Slippery Slope:** He argues that taking the small step of building a levee will inevitably lead to the catastrophic outcome of cutting off all water downstream.

### 3. Mechanism of the Flaw
The reasoning is flawed because it attacks a position Sable **never held** rather than engaging with her actual ar

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism of the Straw Man fallacy (misrepresenting a levee as a dam) and explains why the attack is irrelevant to the actual proposal. However, the response contains a significant conceptual error by labeling this a 'Slippery Slope variant.' The scenario de

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Garrett fires back at Inspector Maren by bringing up the oil-lantern incident. What is wrong with his reasoning? Why doesn't Maren's past mistake let Garrett off the hook?

**Expected Answer:** **Tu quoque (appeal to hypocrisy)** — Dismissing a criticism by pointing out that the person making it is guilty of the same or similar fault. Treats the critic's inconsistency as though it refutes the content of the criticism.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical error where the validity of a claim is rejected based on the perceived hypocrisy or past errors of the person making the claim, rather than addressing the claim's actual merit.

### 2. Precise Name
**Tu Quoque** (Latin for "you also"), also known as the **Appeal to Hypocrisy**.

### 3. Mechanism of the Fallacy
The reasoning is **bad** because it creates a false equivalence between the *source* of an argument and the *truth value* of the argument itself.
*   **The Flaw:** Garrett's argument is: "Maren was negligent in the past regarding fire safety; therefore, her current citation about coal dust is invalid."
*   **The Reality:** Maren's past failure to secure oil lanterns does not change the physical properties

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'Tu Quoque' and provides a clear explanation of why it is a fallacy of relevance (separating the source from the truth value). Furthermore, the response exceeds the Level 3 requirements by explicitly outlining what a legitimate response would look like

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorric clearly does not like this formula. But does he point out any problem with the measurements, the chemical rationale, or the engineering requirements? What is his objection really about?

**Expected Answer:** **Genetic fallacy** — Dorric judges the formula by attacking its origin — Vielle's impoverished background — rather than engaging with its content. The chemical rationale and measurements go entirely unaddressed.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic **Ad Hominem (Circumstantial)** fallacy, specifically manifesting as **Genetic Fallacy**.

### 2. Precise Name
**Genetic Fallacy** (a subset of *Ad Hominem Circumstantial*).

### 3. Mechanism of Failure
The reasoning is logically invalid because it conflates the **origin** of an idea with its **validity**.
*   **The Flaw:** Dorric argues that because the formula originated from a "poorhouse" and "gutter origins" (the source), the resulting glass cannot be "fine" (the conclusion).
*   **Why it fails:** The truth value of a scientific claim (heat resistance) or the quality of a physical product (glass) is independent of the social status, biography, or socioeconomic background of the person who discovered it. A formula der

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Genetic Fallacy, explains that Dorric attacks the origin rather than the evidence, and explicitly details edge cases where origin might be relevant (e.g., conflict of interest, methodology), fully satisfying all Level 4 criteria.

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Holt raises serious worries. But is he giving you any reason to doubt Tova's research itself?

**Expected Answer:** **Appeal to consequences** — Arguing that a factual claim should be rejected because accepting it would lead to undesirable outcomes, substituting the consequences for a critique of the evidence.

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a classic conflict between **epistemic truth** (what is factually true) and **pragmatic consequences** (what is beneficial or harmful to believe). Guildmaster Holt is attempting to invalidate a scientific finding based solely on the negative social and economic outcomes that would result from accepting it.

### 2. Precise Name
This is the **Appeal to Consequences** (specifically, *Argumentum ad Consequentiam*).

In a decision-theoretic context, it can also be described as a **Category Error** regarding the nature of truth: confusing the *utility* of a belief with the *validity* of the belief.

### 3. Mechanism Analysis
**Why the reasoning is flawed:**
The core mechanism of this fallacy is the **separation of truth from conse

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Appeal to Consequences' fallacy and provides a sophisticated explanation of the mechanism, clearly distinguishing between epistemic truth (validity of evidence) and pragmatic consequences (utility of belief). Furthermore, the response goes beyond the basic requireme

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Corvin has a strong expert backing his claim. But what exactly is Eldric an expert in, and what is the question being debated?

**Expected Answer:** **Appeal to authority** — Corvin appeals to Eldric's authority as a surgeon to settle a question about marine toxicology — a field in which Eldric has no special expertise.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a reliance on the perceived status of a source rather than the actual evidence or the source's specific domain expertise. While it superficially resembles an appeal to authority, the critical flaw lies in the **mismatch of expertise**.

### 2. Precise Name
**Appeal to False Authority** (also known as *Argumentum ad Verecundiam* or *Misplaced Authority*).

### 3. Mechanism of the Fallacy
The reasoning is flawed because it conflates **general prestige** with **specific competence**.
*   **The Flaw:** Master Eldric is established as a "famous surgeon" and "celebrated healer." These credentials validate his expertise in human anatomy, pathology, and medicine. However, they do not grant him expertise in **aquatic toxicology**, **mari

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as an appeal to false/irrelevant authority and explicitly details the domain mismatch between surgery and marine toxicology. Furthermore, the response exceeds the baseline requirements by articulating legitimate edge cases where citing authority is valid,

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?

**Expected Answer:** **Appeal to emotion** — Substituting emotional response — pity, guilt, sentiment — in place of addressing the factual evidence. Geld does not contest the ledger; she tries to make accusers feel bad for asking.

**Model Response:**
> ### 1. Reasoning Pattern
The scenario demonstrates a classic logical fallacy where the speaker attempts to invalidate a factual accusation by appealing to their emotional history, personal sacrifices, and the perceived emotional state of the victims, rather than addressing the evidence presented.

### 2. Precise Name
**Red Herring** (specifically the **Appeal to Pity** or *Argumentum ad Misericordiam*).

While often categorized broadly as a Red Herring because it diverts attention from the ledger, the specific mechanism here is the **Appeal to Pity**: attempting to win an argument by eliciting sympathy for the accuser's past kindness and current distress, rather than engaging with the logical validity of the accusation.

### 3. Mechanism Analysis
This reasoning is **flawed** because it cre

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'Appeal to Pity' (a specific form of Appeal to Emotion) and clearly explains the mechanism: substituting emotional merit for factual evidence regarding the ledger. Crucially, the response exceeds the baseline by explicitly distinguishing between fact-f

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Saffron's pitch sounds appealing. What evidence does he give that the spring water cures anything? Is 'it's natural' really a reason?

**Expected Answer:** **Appeal to nature** — Arguing that a product works because it is natural, treating naturalness as sufficient evidence of safety and efficacy.

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a classic logical fallacy where the "natural" origin of a substance is equated with its safety and efficacy, while "artificial" or "processed" substances are assumed to be harmful or ineffective.

### 2. Precise Name
**The Naturalistic Fallacy** (specifically manifesting as the **Appeal to Nature**).

### 3. Mechanism of the Fallacy
The reasoning is flawed because it relies on a false equivalence between the *source* of a thing and its *properties*.
*   **The Flaw:** Saffron assumes that because water is "natural" (found in nature), it possesses inherent medicinal properties superior to "alchemical" (human-made) remedies.
*   **Why it fails:**
    1.  **Natural $\neq$ Safe:** Many of the most toxic substances known to humani

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Appeal to Nature' fallacy, provides specific counterexamples of harmful natural substances (arsenic, botulinum toxin), and clearly distinguishes between origin-based assumptions and evidence-based efficacy. The response also thoughtfully addresses legitimate edge ca

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What evidence does Paddy give that the charm works? Is 'everyone is buying one' a reason?

**Expected Answer:** **Bandwagon (argumentum ad populum)** — Arguing that something must be true or good because many people believe it or do it. Treating popularity as evidence.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical fallacy where the validity of a claim or the value of an object is determined solely by the number of people who believe in it or possess it.

### 2. Precise Name
**Argumentum ad Populum** (Appeal to Popularity), specifically manifesting as the **Bandwagon Fallacy**.

In a behavioral economics context, this is also a textbook example of **Informational Social Influence** leading to **Herding Behavior**.

### 3. Mechanism Analysis
**Why the reasoning is flawed:**
The core error lies in the disconnect between *prevalence* and *truth/utility*. The fact that "half the village," "Farmer Crewe," and "Magistrate Dunne" possess the charm does not provide any empirical evidence regarding the charm's actual magical prope

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Bandwagon Fallacy' and 'Argumentum ad Populum,' correctly identifies that popularity is being used as the sole evidence for truth/utility, and explains the psychological mechanism of social pressure. Furthermore, the response exceeds the Level 4 criteria by distingu

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The deputy thinks it is more likely that Linda is a bank clerk AND an activist than that she is just a bank clerk. Is the deputy's reasoning correct?

**Expected Answer:** **Conjunction fallacy** — The deputy judges P(bank clerk AND activist) > P(bank clerk). This violates a basic law of probability: the probability of a conjunction can never exceed the probability of either conjunct alone. P(A and B) <= P(A). The error occurs because the conjunction fits a compelling narrative (the 'represent

**Model Response:**
> ### Analysis of the Scenario

**1. Reasoning Pattern Identified**
The specific reasoning pattern demonstrated is the **Conjunction Fallacy**. It is a cognitive bias where an individual assumes that specific conditions are more probable than a single general one.

**2. Precise Name**
**The Conjunction Fallacy** (often illustrated by the classic "Linda Problem" from Tversky and Kahneman, which this scenario directly mirrors).

**3. Mechanism of the Error**
The deputy's reasoning is flawed because it violates the fundamental laws of probability.
*   **The Logic:** Let $A$ be the event "Linda is a bank clerk" and $B$ be the event "Linda is a member of the Fair Trade Alliance."
*   **The Rule:** The probability of two events occurring together (the conjunction, $A \text{ and } B$) can never be 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Conjunction Fallacy and explicitly names the 'Linda Problem.' They accurately state the probability rule P(A and B) <= P(A) and explain the role of the representativeness heuristic in driving the error. Furthermore, the response goes beyond the basic requirements

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sera says there is a 95% chance the patient has Stoneblight based on the positive test. Is she right? What is the actual probability?

**Expected Answer:** **Base rate neglect** — Sera assumes that a positive result on a 95% accurate test means a 95% chance of disease. She ignores the base rate of 0.5%. For 100,000 people: 500 have Stoneblight. The test catches 475 of them (true positives). Of the 99,500 healthy people, the test falsely flags 5% = 4,975 (false positives). Tot

**Model Response:**
> ### 1. The Specific Reasoning Pattern
The scenario demonstrates a classic failure in probabilistic reasoning where the decision-maker ignores the **base rate** (prevalence) of the condition and focuses exclusively on the **likelihood ratio** (test accuracy). This leads to a gross overestimation of the probability that the patient actually has the disease.

### 2. Precise Name
This is the **Base Rate Fallacy** (also known as **Base Rate Neglect**). In the context of decision theory and Bayesian inference, it is the failure to apply **Bayes' Theorem** correctly by omitting the prior probability ($P(Disease)$).

### 3. Mechanism: Why the Reasoning is Flawed
Sera's reasoning is flawed because she equates the **True Positive Rate** (Sensitivity) with the **Positive Predictive Value** (PPV).

* 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Base Rate Fallacy, explains the mechanism by distinguishing between sensitivity and positive predictive value, and performs the calculation accurately (arriving at ~8.7%). Furthermore, the response exceeds the Level 3 requirements by explicitly discussing edge ca

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Minister Kael says the data proves small schools produce better scholars. Is the data as convincing as he thinks? What should he check before spending 1.7 million gold?

**Expected Answer:** **Law of small numbers / small numbers fallacy** — Kael observes that small schools top the achievement rankings and concludes that being small causes better performance. But smaller populations produce more variable outcomes: with fewer students, a few strong (or weak) performers swing the average dramatically. If Kael checked the bottom of the ran

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic statistical error where the analyst observes a correlation between a variable (school size) and an outcome (test scores) but fails to account for the underlying distribution of data points and the influence of sample size on variance. The Minister is drawing a causal conclusion ("smaller is better") based on the fact that the *extreme* values (top and bottom) of the dataset are dominated by small sample sizes.

### 2. Precise Name
**The Small Sample Size Fallacy** (specifically manifesting as **Insensitivity to Sample Size** or **Regression to the Mean**).

In the context of the famous example by Daniel Kahneman and Amos Tversky (which this scenario mirrors almost exactly), this is often referred to as the **Law of Lar

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the statistical phenomenon (high variance in small samples) and explicitly notes that small schools would also appear at the bottom of the rankings, which is the key diagnostic for this pattern. They explain the mathematical mechanism (standard error), distinguish be

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sal says nine out of ten customers feel better after taking his elixir. Is this good evidence that the elixir works?

**Expected Answer:** **Regression to the mean** — People seek remedies when symptoms are at their peak (an extreme observation). After peak symptoms, the natural tendency is to return to baseline health — this is regression to the mean. Sal attributes the improvement to his elixir, but the improvement would likely have occurred regardless. The nine

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a combination of **Anecdotal Evidence** (relying on isolated personal stories) and **Survivorship Bias** (focusing only on those who "survived" or improved while ignoring those who did not), underpinned by the **Post Hoc Ergo Propter Hoc** fallacy (assuming that because B followed A, A caused B).

### 2. Precise Name
The most precise label for the core logical error is **Hasty Generalization based on Anecdotal Evidence**, specifically exacerbated by **Survivorship Bias**.

### 3. Mechanism of the Flaw
The reasoning is flawed because it substitutes **statistical rigor** with **emotional narrative**:

*   **Lack of Control Group:** Sal claims "nine out of ten" improve, but offers no data on the control group (people who took *nothin

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that the improvement is likely due to the natural course of the illness (spontaneous recovery) and explicitly notes the lack of a control group, which aligns with the core logic of Level 3. They also describe a proper controlled test (RCT), touching on Level 4 criter

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Rurik says the dice are 'owed' a high roll after six lows. What is wrong with his reasoning?

**Expected Answer:** **Gambler's fallacy** — The mistaken belief that if a random event has occurred more frequently than expected, it is less likely to occur next. Each independent trial has the same probability regardless of previous outcomes.

**Model Response:**
> ### Analysis of Rurik Coinbane's Reasoning

**1. Reasoning Pattern Identified**
Rurik is demonstrating a fundamental misunderstanding of probability theory regarding independent events. He believes that past outcomes in a random sequence influence future outcomes to "balance out" the results.

**2. Precise Name**
This is the **Gambler's Fallacy** (also known as the Monte Carlo Fallacy or the Fallacy of the Maturity of Chances).

**3. Mechanism of the Error**
The reasoning is flawed because it violates the principle of **statistical independence**.
*   **The Flaw:** Rurik assumes that the universe or the dice possess a memory. He believes that because "low" has occurred six times, the probability of "high" must increase to correct the imbalance.
*   **The Reality:** In a fair game, each rol

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Gambler's Fallacy by name, provides a clear and accurate explanation of statistical independence (noting that dice have no memory), and explicitly addresses the legitimate edge case regarding biased dice or non-independent systems, fulfilling all criteria for the

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Breck says all the people of Dunmore are cheats based on his two visits. Is his conclusion justified by his evidence?

**Expected Answer:** **Hasty generalization** — Breck draws a universal conclusion ('all people of Dunmore are cheats') from a sample of two negative interactions. The sample size is far too small to support a generalization about an entire town's population. He is also ignoring the possibility of confounding factors (perhaps he visited during a 

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic logical error where a conclusion about an entire group is drawn from an insufficient and unrepresentative sample size.

### 2. Precise Name
**Hasty Generalization** (also known as the **Fallacy of Insufficient Statistics** or **Overgeneralization**).

In the context of cognitive biases, this is closely related to the **Availability Heuristic**, where the vividness of the two negative experiences makes them seem more representative of the whole than they actually are.

### 3. Mechanism Analysis
**Why the reasoning is flawed:**
Breck's logic fails because he attempts to induce a universal rule ("All people of Dunmore are cheats and thieves") based on a sample size of $N=2$ specific transactions.
*   **Sample Size:** Two 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'Hasty Generalization' and provides a sophisticated mechanism analysis that covers sample size insufficiency, selection bias, and attribution error. Crucially, the response exceeds Level 3 requirements by explicitly discussing confounding factors (isol

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Brix says seagulls are causing the decline of the fishing fleet because the two trends are correlated. Is his reasoning sound?

**Expected Answer:** **False cause / post hoc fallacy** — Brix observes that two variables are correlated over time (fishing boats declining, seagulls increasing) and infers that one causes the other. But correlation does not establish causation. There are four possibilities: (1) seagulls cause boat decline, (2) boat decline causes seagull increase, (3) a 

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a classic logical error where a statistical correlation between two variables is mistaken for a direct causal relationship. Councillor Brix observes that as the number of fishing boats decreased, the number of seagulls increased, and concludes that the seagulls *caused* the decline of the fishing fleet.

### 2. Precise Name
**Cum Hoc Ergo Propter Hoc** (Latin for "with this, therefore because of this"), commonly known as the **Correlation Does Not Imply Causation** fallacy.

### 3. Mechanism of the Error
The reasoning is flawed because it ignores the fundamental principle that **correlation is not causation**. The mechanism of failure here involves the omission of a **confounding variable** (or third variable).

*   **The Fl

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the false cause fallacy (naming it 'Cum Hoc' which is acceptable for correlation errors), explicitly states that correlation does not imply causation, and proposes plausible alternative explanations involving common causes (overfishing, environmental change). Further

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Vance seems to be complimenting Pip, but something feels off. What rhetorical technique is Vance using?

**Expected Answer:** **Evaluative language and presupposition** — Using loaded terms, diminutives, and embedded presuppositions to bias perception without explicit argument. The framing does the persuasive work while appearing neutral.

**Model Response:**
> ### Analysis of the Scenario

**1. Specific Reasoning Pattern**
The scenario demonstrates a **Fundamental Attribution Error** (also known as the Correspondence Bias), compounded by **Halo/Horn Effect** dynamics and **Status Bias**.

**2. Precise Name**
**Fundamental Attribution Error** (specifically the *Actor-Observer Asymmetry* variant where the observer attributes the actor's success to internal limitations rather than external effort or skill).

**3. Mechanism Explanation**
The reasoning is flawed because the senior member attributes Pip's success (an observable outcome) primarily to his "limited background" (a static, internal trait) while dismissing the actual effort, strategy, or competence required to clear the caverns.
*   **The Error:** The observer ignores situational factors (P

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct reasoning pattern. The rubric and correct answer focus on linguistic manipulation (evaluative language, presupposition, loaded terms), whereas the student analyzed the scenario through the lens of social psychology biases (Fundamental Attribution

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Question:** Can you identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work?

**Expected Answer:** **Assuring, guarding, and discounting** — Three rhetorical moves managing acceptance: assuring ('everyone knows') discourages questioning, guarding ('most scholars') hedges while sounding authoritative, discounting ('granted X, but Y') acknowledges then dismisses objections.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a **False Dilemma** (also known as a False Dichotomy or Black-and-White Thinking), compounded by **Appeal to Fear** and **Moral Equivalence**. The advisor frames the situation as having only two options: either raise taxes on farmers or face the destruction of the kingdom, ignoring any middle ground or alternative strategies.

### 2. Precise Name
**False Dilemma** (specifically, the "Survival vs. Hardship" dichotomy).

### 3. Mechanism of the Flaw
The reasoning is flawed because it artificially restricts the solution space to two mutually exclusive extremes while dismissing the complexity of the problem.
*   **Omission of Alternatives:** It assumes the fortress is the *only* viable defense and that taxes are the *only* way to fund

**Score:** 1/4 █░░░
**Judge Reasoning:** The student failed to identify the correct reasoning pattern. The rubric and correct answer specify 'Assuring, guarding, and discounting' as the target moves, but the student incorrectly identified a 'False Dilemma' and 'Appeal to Fear.' While the student's analysis of the False Dilemma is internall

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Torin says that because Amanda argued badly, the herb must NOT have healing properties. What is wrong with Torin's reasoning?

**Expected Answer:** **The fallacy fallacy** — Assuming that because an argument for a conclusion contains a fallacy, the conclusion itself must be false. A bad argument for X does not prove not-X.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a **Fallacy Fallacy** (also known as *argumentum ad logicam*).

### 2. Precise Naming
The apprentice commits the **Fallacy Fallacy**.
*   **Step A (Correct):** Identifying that Amanda's argument ("Grandmother used it, therefore it works") is an *Appeal to Tradition* (a logical fallacy).
*   **Step B (Incorrect):** Concluding that because the *argument* is flawed, the *conclusion* ("Silvervein has healing properties") must be false.

### 3. Mechanism of the Error
The reasoning is flawed because it conflates the **validity of the argument** with the **truth of the conclusion**.

*   **The Logic Gap:** A conclusion can be true even if the reasoning used to support it is terrible. The fact that "Grandmother used it" is irrelevant to

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Fallacy Fallacy' by name, clearly distinguishes between the validity of an argument and the truth of its conclusion, and explicitly states that the conclusion is an empirical matter requiring testing (chemical analysis, trials). The response also thoughtfully ad

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The innkeeper's daughter has laid out the situation. Identify the acts, the states, and the outcomes. Then check: does either act dominate the other with these values?

**Expected Answer:** **Decision matrix construction** — A decision matrix organizes a choice into rows (acts the agent controls), columns (states of the world the agent does not control), and cells (outcomes with assigned values). This is the foundational representation for all of decision theory.

**Model Response:**
> ### Analysis of the Decision Scenario

#### 1. The Decision Matrix
First, let us formalize the scenario into a standard decision matrix based on the values provided in the prompt (where higher numbers indicate better outcomes):

| **Acts \ States** | **Rain** (Probability $p$) | **No Rain** (Probability $1-p$) |
| :--- | :---: | :---: |
| **Take Umbrella** | 3 (Dry, burdened) | 2 (Dry, burdened) |
| **Leave Umbrella** | 1 (Wet, miserable) | 4 (Free, light) |

*   **Acts:** Taking the umbrella vs. Leaving the umbrella.
*   **States:** It rains vs. It does not rain.
*   **Outcomes:** The numerical utility scores assigned to the resulting conditions.

#### 2. Identification of the Concept
The specific reasoning pattern demonstrated here is **Dominance Reasoning** (specifically, **Strict Domin

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly constructs the decision matrix with acts, states, and outcomes. They initially hypothesize dominance but immediately self-correct to accurately identify that no act dominates because preferences reverse across states. They explain this mechanism clearly (each act wins in one st

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The merchant has set up a matrix. Dominance reasoning gives no clear answer. But is there a deeper problem with how the matrix is constructed? What assumption does dominance reasoning require about the relationship between acts and states?

**Expected Answer:** **Dominance reasoning and state-act independence** — Dominance reasoning says: if one act yields a better outcome in every possible state, choose it. But this only works when states are independent of acts. In the extortion case, whether the cart is damaged depends on whether you pay — the states are not independent of the acts, which violates the str

**Model Response:**
> ### 1. The Specific Reasoning Pattern
The reasoning pattern demonstrated is the **failure to account for causal dependence** between the agent's action and the state of the world. The player is attempting to apply **Dominance Reasoning** (specifically Causal Dominance) but incorrectly assumes the states of nature ("Cart Damaged" vs. "Cart Not Damaged") are probabilistically independent of the choice to pay or not pay.

### 2. Precise Name
This is the **Fallacy of Ignoring Causal Correlation** (often discussed in decision theory as the error of applying **Evidential Dominance** where **Causal Dominance** is required, or simply the **Independence Assumption Error**). In the context of Newcomb-like problems, it represents a failure to distinguish between **Causal Decision Theory (CDT)** and *

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the violation of the independence assumption required for dominance reasoning. They explicitly explain the causal dependence between the act and the state, propose the correct restructuring of the problem using conditional probabilities and expected utility, and prov

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The prospector wants the biggest possible payoff and does not care about the downside. Apply the maximax rule: for each expedition, find its best outcome, then pick the expedition with the highest best outcome.

**Expected Answer:** **Maximax** — Maximax identifies the best possible outcome for each act, then selects the act with the highest best-case outcome. It is the optimist's rule: chase the ceiling, ignore the floor.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a specific **decision-theoretic criterion** used under conditions of uncertainty (where probabilities of outcomes are unknown). The prospector is explicitly prioritizing the single most optimistic outcome available across all options, disregarding the likelihood of that outcome or the severity of potential losses.

### 2. Precise Name
**Maximax Criterion** (also known as the **Optimism Criterion**).

### 3. Mechanism Analysis
**How it works:**
The Maximax rule operates by identifying the **maximum possible payoff** for each available strategy and then selecting the strategy with the **highest of those maximums**.
*   **River Panning:** Max payoff = 8
*   **Hilltop Digging:** Max payoff = 12
*   **Cave Exploring:** Max payoff = 6

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified the Maximax pattern, selected Hilltop Digging with the correct value (12), and explicitly explained that the rule ignores downside risk. Furthermore, the response exceeded Level 3 requirements by contrasting Maximax with Maximin and Minimax Regret, discussing the ris

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The scholar wants to avoid the worst possible evening. Apply maximin: for each act, find its worst outcome, then pick the act whose worst outcome is highest.

**Expected Answer:** **Maximin** — Maximin identifies the worst possible outcome for each act, then selects the act whose worst case is least bad. It is the pessimist's rule: raise the floor, ignore the ceiling.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scholar is demonstrating a **Maximin Decision Rule** (also known as the **Wald Criterion**). This is a decision-making strategy under uncertainty where the decision-maker evaluates each option based on its worst possible outcome and selects the option with the "best of the worst" outcomes.

### 2. Precise Naming
**Maximin Strategy** (or **Maximin Criterion**).
*Note: While often associated with the **Pessimism Bias** in behavioral economics, in formal decision theory, it is a specific, rational algorithm for handling uncertainty when probabilities are unknown.*

### 3. Mechanism Analysis
**How it works:**
The scholar ignores the potential for high gains (the "4" for watching a win) and focuses exclusively on the floor of the payoff matrix:
- **Option

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Maximin pattern and mechanism. Crucially, they explicitly note that the strategy 'ignores the potential for high gains' (the ceiling) and contrasts this result with the alternative approach (Expected Value/Probabilistic reasoning which would favor watching), effe

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Given the profit table, apply Minimax Regret to determine which cargo to load. Show your regret matrix and explain your answer.

**Expected Answer:** **Minimax regret** — Step 1: Build the regret matrix. Column maxima: Mining Camp=18, Fishing Village=16, Fortress=14.

Regret matrix:
              Mining Camp    Fishing Village    Fortress
Furs           0               12              11
Salted Fish   12                0               9
Iron Tools     8              

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a specific **decision-theoretic concept** known as **Minimax Regret** (also called the Savage Minimax Regret criterion). It is a non-probabilistic decision rule used under conditions of **uncertainty** (where probabilities of states of nature are unknown).

### 2. Precise Name
**Minimax Regret Criterion** (or **Savage Criterion**).

### 3. Mechanism: Why it works (and its limitations)
The mechanism operates by shifting the focus from **maximizing absolute profit** to **minimizing the maximum opportunity loss (regret)**.

*   **The Logic:** Instead of asking "Which cargo makes the most money?", it asks "Which cargo ensures I lose the *least* amount of potential money compared to the best possible choice for that specific scenario

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified the Minimax Regret pattern, accurately constructed the regret matrix with correct column maxima and arithmetic, identified the maximum regret for each act (12, 12, 8), and selected the optimal choice (Iron Tools). Furthermore, the response clearly articulated the min

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The scholar says education might not increase productivity at all — it just signals pre-existing ability. Under what conditions does this signaling work? What is the key property that makes the signal credible?

**Expected Answer:** **Signaling (Spence's job market model)** — In a signaling game, an informed player (Sender) takes a costly action to reveal private information to an uninformed player (Receiver). Separation requires the Single Crossing Condition: the signal must be more costly for low types than high types. In Spence's model, education is the signal, abilit

**Model Response:**
> Based on the scenario provided, here is the complete analysis:

### 1. Reasoning Pattern / Concept
The scenario demonstrates the **Single Crossing Condition** within the framework of **Spence's Signaling Model** (specifically, a **Separating Equilibrium**).

While often framed as a "pattern" of reasoning in game theory, it is technically a **necessary condition for equilibrium existence** in signaling games with asymmetric information. It is not a fallacy or a bias; rather, it is the mathematical mechanism that allows a signal to be credible.

### 2. Precise Name
**The Single Crossing Condition (SCC)** in a **Separating Equilibrium**.

### 3. Mechanism Analysis: Why is this reasoning "Good"?
The reasoning is **sound and logically valid** because it correctly identifies the structural requi

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Single Crossing Condition and derives the specific mathematical range for separation (20 < e < 60) using the provided cost functions. They explicitly explain why pooling occurs if costs are equal and discuss the social waste/deadweight loss concern regarding over

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Question:** Standard theory says Responders should accept any positive offer. They do not. Why? And how do formal models of social preferences (like Fehr-Schmidt) explain both Responder rejections and Proposer fairness?

**Expected Answer:** **Behavioral game theory** — Behavioral game theory studies how real humans deviate from Nash equilibrium predictions. Key findings: (1) Ultimatum Game: people reject unfair offers at personal cost and anticipate this by making fair offers. (2) Level-k reasoning: people think a few steps ahead, not infinitely. (3) Social prefer

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the failure of **Subgame Perfect Equilibrium (SPE)** derived from **Homo Economicus** assumptions when applied to human social interaction. Specifically, it highlights the **Ultimatum Game Paradox**, where the theoretical prediction of rational self-interest clashes with observed human behavior driven by **inequity aversion** and **reciprocity**.

### 2. Precise Name
**The Ultimatum Game Paradox** (manifesting as a violation of **Backward Induction** under the assumption of **Pure Self-Interest**).

### 3. Mechanism Analysis
The reasoning pattern is "bad" (predictively failed) because it relies on a flawed model of human utility.

*   **The Flawed Logic (Standard Theory):**
    *   **Assumption:** Agents are purely self-interested

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Ultimatum Game and Behavioral Game Theory. They explicitly define the Fehr-Schmidt utility function with alpha and beta parameters, explaining how disadvantageous inequality leads to rejection. They discuss Proposer anticipation (connecting to level-k reasoning) 

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Without commitment, the Incumbent gets 2. With commitment, the Incumbent gets 3. How can removing an option make you better off? Explain the mechanism and give another example of a commitment device.

**Expected Answer:** **Commitment** — Commitment devices improve outcomes in strategic settings by making threats or promises credible. The Paradox of Commitment: having fewer options can be advantageous because it changes the opponent's best response. Types include contracts, reputation, precommitment, burning bridges, delegation, and 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the strategic manipulation of **subgame perfection** through **precommitment**. It is not a fallacy or a bias in the traditional sense (like confirmation bias); rather, it is a deliberate application of **game-theoretic rationality** where a player voluntarily restricts their own future freedom of action to alter the opponent's expectations and behavior.

### 2. Precise Name
**Strategic Precommitment** (specifically illustrating the **Commitment Device** or **Thomas Schelling's "Strategy of Conflict"**).

In the context of the specific paradox mentioned ("doing better by having fewer options"), this is often referred to as the **Paradox of Commitment** or the **Power of Irreversibility**.

### 3. Mechanism: Why this reasoning work

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Strategic Precommitment/Paradox of Commitment) and provides a clear, accurate explanation of the mechanism using the Entry Game and payoff changes. They also successfully provide other examples (reputation, madman theory, burning bridges). However, the r

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The instructor lists four conditions for reputation to sustain cooperation. What are they? If any one fails, how does cooperation break down? Give a real-world example of a reputation system and explain which conditions it satisfies.

**Expected Answer:** **Reputation and the shadow of the future** — Reputation is what others believe about your type or strategy based on past actions. In repeated games, reputation creates incentives for cooperation: defecting today earns a short-term gain but destroys future cooperation opportunities. The Folk Theorem shows that in infinitely repeated games (or g

**Model Response:**
> Based on the scenario provided, here is the complete analysis:

### 1. Specific Concept Demonstrated
The scenario demonstrates the **Folk Theorem** within the framework of **Repeated Game Theory** (specifically, the logic of **Reputation Effects**). It is not a fallacy or bias; rather, it is a rigorous game-theoretic result explaining how rational self-interest can lead to cooperative outcomes in long-term interactions.

### 2. Precise Naming
**The Folk Theorem (in Repeated Games)** or **Reputation-Based Cooperation**.

### 3. Mechanism Analysis
This reasoning is **sound and mathematically valid** under the specified conditions. It works by altering the payoff structure of a single interaction through the lens of the future.

*   **The Mechanism:** In a one-shot Prisoner's Dilemma, the dom

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Folk Theorem and the role of reputation in repeated games. They explicitly detail all four necessary conditions (repetition, observability, patience/discount factor, and punishment) and explain the trade-off between immediate gain and future value. Crucially, the

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Bob risks 2 gold to win 1 gold, with a total stake of 3 gold. If this bet is fair in Bob's eyes, what is his credence — his subjective probability — that the storm will come? Show the calculation.

**Expected Answer:** **Fair betting rate as credence** — A fair betting rate quantifies subjective probability. If an agent considers a bet fair (expected value zero), their credence in the proposition equals their potential loss divided by the total stake. Bob risks 2 gold on a 3 gold total stake, so his credence in the storm is 2/3.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the application of **Subjective Probability via Betting Quotients** (also known as **Dutch Book Arguments** or **Ramsey's Thesis**). It is not a fallacy or bias in itself; rather, it is a decision-theoretic method for quantifying an agent's internal degree of belief (credence) based on their willingness to accept a specific risk-reward ratio.

### 2. Precise Name
**The Betting Quotient (or Fair Odds) Method for Credence.**

### 3. Mechanism: Why This Reasoning Works (or Fails)
The mechanism relies on the definition of a "fair bet" in expected utility theory. If an agent is rational and risk-neutral, they will only accept a bet if their expected value (EV) is zero or positive.

*   **The Setup:**
    *   Bob risks $2$ (Loss if No S

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern (Betting Quotients/Ramsey's Thesis) and calculates the credence as 2/3 using the correct formula. They explicitly explain the 'fair bet' condition (EV=0) and go beyond the basic requirements by thoroughly discussing edge cases, specifically the assumption

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The bookie's implied probabilities sum to 1.05. Explain why this guarantees the bookie a profit regardless of which horse wins. Then answer: if a gambler's personal credences summed to more than 1, how could someone exploit them?

**Expected Answer:** **Dutch Book argument** — A Dutch Book is a set of bets that guarantees a net loss for the agent regardless of the outcome. The Dutch Book theorem proves that if an agent's credences violate the axioms of probability (e.g., sum to more or less than 1 for an exhaustive partition), there exists a set of bets the agent consider

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a violation of the **axioms of probability**, specifically the **Normalization Axiom** (also known as the axiom of unit measure). In decision theory and epistemology, this leads to a **Dutch Book** vulnerability.

### 2. Precise Name
The specific concept is a **Dutch Book Argument** (or being **Dutch Booked**).
*   In the context of the bookie: It represents the **Overround** (or "vig" / "juice"), which is the bookmaker's built-in profit margin.
*   In the context of the gambler with incoherent credences: It represents **Probabilistic Incoherence**.

### 3. Mechanism of Failure
The mechanism relies on the mathematical impossibility of assigning probabilities that sum to more than 1.0 for a set of **mutually exclusive and exhaust

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a Dutch Book Argument and explicitly links it to the Normalization Axiom. They accurately explain the mechanism of exploitation for both the bookie (overround) and the gambler (incoherent credences leading to guaranteed loss). Crucially, they articulat

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Nell says something doesn't add up. She's right. Look at the implied probabilities on Oliver's board. What mathematical rule do they violate, and what does that mean for anyone betting at these odds?

**Expected Answer:** **Axioms of probability** — The three axioms of probability require: (1) Non-negativity: all probabilities >= 0; (2) Normality: probabilities over the entire sample space sum to exactly 1; (3) Finite Additivity: for mutually exclusive events, P(A or B) = P(A) + P(B). Oliver's odds violate Axiom 2 because the implied probabilit

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a violation of the **Axiom of Probability** regarding the normalization of a sample space. Specifically, it illustrates the **Overround** (also known as the "Vig" or "Juice"), which creates a mathematical impossibility if the bookie claims the odds are "fair" (i.e., reflecting true probabilities without a margin).

### 2. Precise Name
**The Overround** (or **Bookmaker's Margin**).
In the context of logical fallacies, this is a form of **False Equivalence** (equating "offered odds" with "true probability") or a violation of **Probability Normalization**.

### 3. Mechanism: Why this reasoning is flawed
The mechanism relies on the fundamental rule of probability theory: **The sum of the probabilities of all mutually exclusive and exh

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the violation of the probability axioms (specifically normalization/sum > 1), calculates the exact margin (0.05 or 5%), and provides a sophisticated explanation of the Dutch Book concept (guaranteed loss for the bettor/guaranteed profit for the bookie). The response 

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss and Lira are both using the word 'probability' but seem to mean different things. Are they contradicting each other, or could both be right? What exactly is the difference between what they are describing?

**Expected Answer:** **Subjective vs objective probability** — Objective probability (chance) refers to mind-independent features of the world — physical propensities, frequencies, quantum indeterminacies. Subjective probability (credence) refers to an agent's degree of confidence in a proposition, revealed through betting behavior. Both satisfy the same axioms

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a **Category Mistake** (or **Ontological Category Error**) regarding the definition of probability. Both scholars are conflating two distinct mathematical and philosophical interpretations of probability, treating them as mutually exclusive descriptions of a single reality rather than complementary frameworks for different types of uncertainty.

### 2. Precise Name
**The Frequentist vs. Bayesian Interpretation Conflict** (specifically, the **Ontological Fallacy** of probability).

*   **Scholar Voss** represents the **Frequentist** (or Physicalist) view: Probability is an objective, long-run frequency inherent in physical systems.
*   **Scholar Lira** represents the **Bayesian** (or Epistemic) view: Probability is a subjective deg

**Score:** 4/4 ████
**Judge Reasoning:** The student clearly distinguishes between objective chance (aleatory/physical) and subjective credence (epistemic/belief), correctly identifying that both adhere to the same mathematical axioms (Kolmogorov). Furthermore, the response explicitly raises the question of how these two concepts relate, d

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms?

**Expected Answer:** **Principal Principle** — The Principal Principle (Lewis/Weatherson) states: if you know the objective chance of an event is x, your rational credence should be x, provided you have no inadmissible evidence (e.g., time travel, crystal balls). Formally: Pr(p | Ch(p)=x) = x. Cade knows Ch(Heads)=0.80 but sets Cr(Heads)=0.50, v

**Model Response:**
> ### 1. Reasoning Pattern & Concept
The scenario demonstrates a conflict between **objective Bayesianism** (or frequentist evidence) and **subjective credence** based on anecdotal experience. Specifically, it illustrates the **Gambler's Fallacy** (in a nuanced form) combined with **Overconfidence Bias** and a rejection of **Calibration**.

While Cade claims his beliefs "add up to 1" (internal consistency), he is failing to update his prior beliefs based on overwhelming external evidence.

### 2. Precise Name
The most precise term for this specific failure is **The Base Rate Neglect** (or **Base Rate Fallacy**), exacerbated by **Illusory Correlation** (believing a personal "feeling" correlates with the coin's physical state).

In decision theory, this is also a failure of **Proper Scoring Ru

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cade is ignoring objective evidence in favor of subjective feeling and notes the distinction between internal consistency and external rationality. However, the student explicitly misidentifies the reasoning pattern as 'Base Rate Neglect' and 'Gambler's Fallacy'

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Calculate the expected utility of each option using the formula EU(Act) = sum of P(State) * U(Act|State). Which option should the healer choose, and why does it differ from what dominance reasoning would say?

**Expected Answer:** **Maximize Expected Utility (MEU)** — MEU weighs each outcome by its probability and sums to get the expected utility of each act. The agent selects the act with the highest expected utility. EU(Act) = P(S1)*U(Act|S1) + P(S2)*U(Act|S2) + ...

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the application of **Expected Utility Theory (EUT)**, specifically the calculation of **Expected Monetary Value (EMV)** in a decision-making context under uncertainty.

### 2. Precise Name
**Expected Value Maximization** (or **Rational Choice under Risk**).

*Note: The prompt asks to identify a "fallacy, bias, or concept." In this specific scenario, the reasoning pattern is **not** a fallacy or bias; it is the **correct normative standard** for rational decision-making. The healer is correctly modeling the problem to avoid cognitive biases like the Sunk Cost Fallacy or Loss Aversion.*

### 3. Mechanism: Why this reasoning is "Good"
The mechanism is the **linear aggregation of probabilistic outcomes weighted by their utility (cost)

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Expected Utility/Value), performs the arithmetic accurately (-35 vs -50), selects the correct option (Use Cream), and explicitly explains the mechanism of probability weighting. However, the response does not reach Level 4 because it fails to address the

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Captain Aldric's scout gave rankings but not numbers. Why is that not enough for a good decision here? What additional information would you need, and how would it change the analysis?

**Expected Answer:** **Cardinal vs ordinal utility** — Ordinal utility provides only a ranking: A > B > C. Cardinal utility assigns numerical values that capture how much better A is than B. Decision rules like Maximin and Maximax use ordinal utility and are therefore blind to magnitude. MEU requires cardinal utility because it multiplies utility by pro

**Model Response:**
> ### 1. The Core Concept
The scenario demonstrates a failure of **Ordinal Utility** when applied to **Maximin Decision Theory** in a context requiring **Cardinal Utility**.

Specifically, it highlights the **Information Loss Problem** inherent in using rank-order data (ordinal) to make decisions based on worst-case magnitude (cardinal). The scout's ranking provides a *qualitative* order ($A > B > C$) but strips away the *quantitative* distance between those outcomes, which is critical for risk assessment.

### 2. Precise Naming
**The Ordinal-Cardinal Mismatch in Maximin Analysis** (or simply **The Limitation of Ordinal Maximin**).

In decision theory, this is often discussed under the constraints of **Ordinal Utility Theory**, which states that utility functions are unique only up to a posi

**Score:** 4/4 ████
**Judge Reasoning:** The student clearly distinguishes between ordinal and cardinal utility, explaining that rankings ignore magnitude while cardinal values capture it. They correctly identify that Maximin fails here because it treats rank gaps equally, missing the severity of the 'catastrophic' outcome. Furthermore, th

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Kael calls Sera irrational because she turns down a bet with higher expected monetary value. Is he right? Or is there a way to explain Sera's preference that is perfectly consistent with maximizing expected utility?

**Expected Answer:** **Risk aversion and utility curves** — Under MEU, risk attitude is encoded in the shape of the utility function. A linear utility function (U = wealth) produces risk neutrality. A concave function (e.g., U = sqrt(wealth)) produces risk aversion: the utility of the expected value exceeds the expected utility of the gamble. Sera's declinin

**Model Response:**
> ### 1. Reasoning Pattern & Concept
The scenario demonstrates the conflict between **Expected Value (EV) maximization** and **Expected Utility (EU) maximization**. Specifically, it illustrates **Risk Aversion** driven by the **Diminishing Marginal Utility of Wealth**.

### 2. Precise Name
**The St. Petersburg Paradox Resolution via Concave Utility Functions** (or simply **Expected Utility Theory**).

*   **Kael** is operating under **Risk Neutrality** (maximizing Expected Value).
*   **Sera** is operating under **Risk Aversion** (maximizing Expected Utility).

### 3. Mechanism: Why is this reasoning good or bad?
The core mechanism is the shape of the **utility function** ($U$), which maps monetary value to subjective satisfaction or "well-being."

*   **Kael's Logic (Risk Neutral):** He ass

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Risk Aversion driven by diminishing marginal utility and explicitly links this to the concave shape of the utility function. They contrast Kael's linear (risk-neutral) approach with Sera's concave approach, explain the mechanism clearly using the conce

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** John keeps cycling through ice cream trades and losing money. What structural property of his preferences allows the vendor to exploit him? What would John need to change about his preferences to stop the bleeding?

**Expected Answer:** **Transitivity and money pumps** — Transitivity requires: if A > B and B > C, then A > C. John's preferences violate transitivity (S > C, C > V, but V > S). The money pump shows that intransitive preferences are exploitable: an agent can be led through a cycle of individually rational trades that return them to the starting point min

**Model Response:**
> ### Analysis of the Ironvale Market Scenario

#### 1. The Specific Concept
The scenario demonstrates a violation of the **Transitivity Axiom** within **Rational Choice Theory**. Specifically, it illustrates the phenomenon of **Intransitive Preferences** leading to a **Money Pump**.

#### 2. Precise Naming
The precise term for the reasoning pattern is **Intransitive Preferences** (or a **Non-Transitive Cycle**).
The resulting exploitative mechanism is known as a **Money Pump** (or **Dutch Book** argument in a dynamic context).

#### 3. Mechanism Explanation
**Why the reasoning is "bad" (Destructive):**
In standard decision theory, rational preferences must be **transitive**. This means if an agent prefers $A$ to $B$, and $B$ to $C$, they *must* prefer $A$ to $C$.
*   **The Flaw:** John's pr

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the intransitive cycle (S > C > V > S) and explicitly names the Transitivity Axiom and Money Pump mechanism. They clearly explain how locally rational trades lead to global irrationality and guaranteed loss. Furthermore, they address the Level 4 requirement regarding

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin asks how removing an option nobody chose can change the recommendation. What principle is being violated here, and why does MEU avoid this problem?

**Expected Answer:** **Independence of Irrelevant Alternatives (IIA)** — IIA states: if option C is chosen from set S, then C should still be chosen from any subset of S containing C. Minimax Regret violates IIA because regret is calculated relative to the best available option in each state. When the menu changes, the reference point changes, which can reverse preferenc

**Model Response:**
> ### 1. The Core Concept
The scenario demonstrates a violation of the **Independence of Irrelevant Alternatives (IIA)**, specifically manifesting as a failure of the **Minimax Regret** criterion to satisfy this axiom. In decision theory, this is often discussed in the context of **Regret Theory** (proposed by Loomes and Sugden) and its inherent instability when the set of available options changes.

### 2. Precise Name
**Violation of the Independence of Irrelevant Alternatives (IIA)** within the **Minimax Regret** decision rule.

### 3. Mechanism: Why This Happens
The reasoning is "bad" (or at least counter-intuitive) because the **regret** of an option is not an intrinsic property of that option and the state of nature; rather, it is **relative to the best available alternative** in the cu

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the violation of Independence of Irrelevant Alternatives (IIA) and provides a precise mathematical explanation of why Minimax Regret fails this axiom (the changing reference point/benchmark). They also correctly contrast this with Expected Utility Theory (MEU), notin

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Father Clement's argument seems airtight — infinity times anything positive is infinity. But Dara is not convinced. What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?

**Expected Answer:** **Pascal's Wager** — Pascal's Wager applies MEU with infinite utility. When any outcome has infinite value, the expected utility calculation is dominated by that outcome regardless of its probability (as long as P > 0). This 'washing out' effect makes MEU insensitive to evidence — a feature that many consider a reductio

**Model Response:**
> ### 1. Reasoning Pattern & Concept
The scenario demonstrates **Pascal's Wager**, a classic argument in decision theory and theology formulated by Blaise Pascal in the 17th century. It relies on **Expected Utility Theory** applied to infinite values.

### 2. Precise Name
**Pascal's Wager** (specifically the **Many-Gods Objection** raised by Dara).

### 3. Mechanism Analysis
The reasoning is structurally sound within a strict mathematical framework but fails in practical application due to two critical flaws:

*   **The Mathematical Mechanism (Why it seems "good"):**
    Pascal utilizes the concept of **dominance** in decision theory. If a payoff is truly infinite ($+\infty$), any finite probability $p > 0$ results in an expected value of $p \times \infty = \infty$. Since $\infty$ dominates 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Pascal's Wager and Expected Utility Theory. They successfully articulate the 'Many-Gods' objection and the problem of infinite utility breaking standard calculations (the washing-out effect), satisfying Level 3 criteria. However, the response does not explicitly conn

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** The expected value is infinite, but you would not pay a million gold to play. What has gone wrong? Is expected value the wrong tool, or are we applying it to the wrong quantity?

**Expected Answer:** **St. Petersburg Paradox** — A fair coin is flipped until heads. Payoff = 2^n where n is the number of flips. Expected value = sum from n=1 to infinity of (1/2)^n × 2^n = sum of 1 = infinity. Yet no reasonable person would pay more than about 20-30 gold. The paradox reveals that expected monetary value is not the same as expect

**Model Response:**
> ### 1. Reasoning Pattern & Concept
The scenario demonstrates a conflict between **mathematical expectation** and **human intuition/real-world constraints**. It highlights the failure of using the **Expected Value (EV)** criterion as a sole decision-making tool when dealing with unbounded utility functions and infinite series.

### 2. Precise Name
This is the **St. Petersburg Paradox**.

### 3. Mechanism: Why the Reasoning is Flawed
The reasoning is "good" in a purely abstract mathematical sense but "bad" in practical decision theory for the following reasons:

*   **The Mathematical Flaw (Divergence):** The calculation $\sum_{n=1}^{\infty} \frac{1}{2^n} \times 2^n = \sum_{n=1}^{\infty} 1 = \infty$ is mathematically correct. The series diverges. However, an infinite expected value implies t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the St. Petersburg Paradox and derives the mathematical divergence of the expected value. Crucially, they explain the resolution via diminishing marginal utility (concave utility function) and explicitly mention calculating Expected Utility with a logarithmic functio

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The showmaster says choosing Gamble 1 and Gamble 4 is inconsistent. Can you see why? What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

**Expected Answer:** **Allais Paradox (Certainty Effect)** — The Allais Paradox demonstrates that people overweight certainty. In Choice 1, Gamble 1 offers certainty ($1M guaranteed), which has disproportionate psychological appeal. In Choice 2, neither option is certain, so people chase the higher payoff (Gamble 4). But the 89% column (Tickets 12-100) is ide

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a violation of the **Independence Axiom** in Expected Utility Theory (EUT). The specific behavioral pattern is the tendency to prefer a certain outcome over a risky one when the probability of winning is high (risk aversion), while simultaneously preferring a higher-risk, higher-reward option when the probability of winning is low (risk seeking), even though the relative trade-off between the options remains mathematically identical in both choices.

### 2. Precise Name
This is the **Allais Paradox** (specifically the "common consequence" version).

### 3. Mechanism: Why the Reasoning is "Bad" (Logically)
The inconsistency arises because human intuition often weights probabilities non-linearly (overweighting certainty) rather than

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Allais Paradox and the violation of the Independence Axiom (Sure Thing Principle). They accurately explain the mathematical inconsistency by isolating the common consequence and demonstrating the contradiction via utility inequalities. They also correctly identif

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss shows that you should accept the bet unconditionally but reject it in every conditional state. Is the Sure Thing Principle actually violated here? Look carefully at whether the conditioning events form a proper partition.

**Expected Answer:** **Sure Thing Principle** — STP states: if A is preferred to B conditional on E, and A is preferred to B conditional on NOT-E, then A is preferred to B unconditionally. It is the backbone of independence in MEU. The Disjunction Effect appears to violate STP but actually involves overlapping (non-exclusive) conditioning events,

**Model Response:**
> ### Analysis of the Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a violation of the **Sure Thing Principle** (STP), which is a cornerstone axiom of **Expected Utility Theory (EUT)**. The specific phenomenon where an agent rejects an action in every possible conditional state (given $E$ and given $\neg E$) yet rejects the action unconditionally (before knowing $E$) is known as the **Disjunction Effect**.

In this specific puzzle, the reasoning pattern is a **probabilistic fallacy** arising from a misunderstanding of how conditional probabilities aggregate. The agent incorrectly assumes that if a decision is suboptimal in every specific partition of the sample space, it must be suboptimal overall, ignoring the fact that the *unconditional* probability space includes

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Sure Thing Principle and the Disjunction Effect. They accurately perform the mathematical verification showing that the conditional expectations are negative while the unconditional is positive. Crucially, they identify the root cause: the events 'at least one He

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Are you a one-boxer or a two-boxer? Whatever you choose, you must defend your reasoning against the strongest version of the opposing argument. What principle are you relying on, and what are you giving up?

**Expected Answer:** **Newcomb's Problem** — Newcomb's Problem pits Dominance against Expected Utility when states are correlated with acts. Causal Decision Theory (CDT) says: the Predictor's choice is fixed, so taking both dominates (you are 1,000 gold richer regardless). Evidential Decision Theory (EDT) says: one-boxing provides strong evide

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the core conflict between **Causal Decision Theory (CDT)** and **Evidential Decision Theory (EDT)** regarding a problem of **Newcomb's Paradox**. The specific reasoning patterns in conflict are:
*   **The Two-Boxer's Logic:** Relies on the **Dominance Principle** (a cornerstone of CDT), arguing that an action is rational if it yields a better outcome regardless of the state of the world.
*   **The One-Boxer's Logic:** Relies on **Evidential Reasoning** (a cornerstone of EDT), arguing that an action is rational if it provides the best *evidence* for a desirable outcome, even if it doesn't causally produce it.

### 2. Precise Name
This is **Newcomb's Paradox** (or Newcomb's Problem).

The specific fallacy or conceptual error often a

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Newcomb's Problem and clearly articulates the conflict between Causal Decision Theory (dominance) and Evidential Decision Theory (expected utility). They provide accurate calculations for both sides, explain the mechanism of correlation vs. causation, and go beyond t

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The dealer says choosing G1 and G4 is inconsistent. Can you see why? What probability would you need to assign to Black to justify G1 over G2? And what probability would you need for G4 over G3? Can both be true?

**Expected Answer:** **Ellsberg Paradox (Ambiguity Aversion)** — The Ellsberg Paradox shows that people prefer known risk (Red: exactly 1/3) over ambiguous risk (Black: unknown proportion). Preferring G1>G2 implies P(Black)<1/3. Preferring G4>G3 implies P(Black)>1/3 (because Yellow cancels out as common consequence). These two implications are contradictory — no 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a violation of the **Sure Thing Principle** (a core axiom of Expected Utility Theory) caused by **Ambiguity Aversion**. The player is making choices based on the *source* of uncertainty (known probability vs. unknown probability) rather than the mathematical outcomes alone.

### 2. Precise Name
This is the **Ellsberg Paradox**.

### 3. Mechanism: Why the Reasoning is Flawed
The mechanism relies on the conflict between **Risk** (known probabilities) and **Ambiguity** (unknown probabilities).

*   **The Setup:**
    *   **Gamble 1 (Red):** Probability = $1/3$ (Known).
    *   **Gamble 2 (Black):** Probability = $x$ (Unknown, where $0 \le x \le 2/3$).
    *   **Gamble 3 (Red or Yellow):** Probability = $1/3 + (2/3 - x) = 1 - x$ (Unkn

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Ellsberg Paradox and Ambiguity Aversion. They explicitly derive the contradiction by showing that G1>G2 implies P(Black)<1/3 while G4>G3 implies P(Black)>1/3. Furthermore, they explain the violation of Subjective Expected Utility (no single probability distributi

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The expected values are the same within each pair, yet the merchants' risk preferences flip. What does this tell you about the shape of the human utility function? Can a single curve explain both patterns?

**Expected Answer:** **Reflection Effect** — The Reflection Effect shows that people are risk-averse when choosing among gains (prefer sure $500 over 50/50 shot at $1000) but risk-seeking when choosing among losses (prefer 50/50 shot at losing $1000 over sure loss of $500). Under MEU, a utility function is either consistently concave (always r

**Model Response:**
> ### Analysis of Scholar Lira's Experiment

#### 1. Specific Concept Demonstrated
The scenario demonstrates a systematic deviation from **Expected Utility Theory (EUT)** caused by **Framing Effects**. Specifically, it illustrates the **Reflection Effect**, a core component of **Prospect Theory**.

#### 2. Precise Naming
The phenomenon is the **Reflection Effect** (within the framework of **Prospect Theory**).
*   *Context:* It describes how people's risk preferences reverse when the same choice is framed as a gain versus a loss.

#### 3. Mechanism: Why This Reasoning Occurs
The "reasoning" here is not logically flawed in a vacuum; rather, it is **psychologically inconsistent** relative to the axioms of rational choice theory (specifically the *independence axiom* and *invariance*).

*   **T

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Reflection Effect and Prospect Theory. They explicitly explain the S-shaped value function (concave for gains, convex for losses) and clearly articulate how this violates Expected Utility Theory's assumption of evaluating final wealth states versus reference poin

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** You reject the bet when you know at least one is heads, and you reject when you know at least one is tails. One of these must be true. So why should you accept unconditionally? Where is the flaw in reasoning from conditionals to the unconditional?

**Expected Answer:** **Disjunction Effect** — The Disjunction Effect occurs when an agent rejects an option conditional on each member of a non-exclusive partition but should accept it unconditionally. The resolution: 'at least one H' and 'at least one T' overlap on {HT, TH} — the losing outcomes. Conditioning on either event eliminates one win

**Model Response:**
> ### Analysis of Scholar Voss's Coin Puzzle

#### 1. Specific Reasoning Pattern
The scenario demonstrates a classic failure in **conditional probability reasoning** often associated with the **Two-Child Problem** (or Boy-Girl Paradox). Specifically, it highlights the error of **conflating the logical disjunction of conditions with the specific observation of a condition**.

The player is falling into a trap where they treat the *set of possible information states* as if they were *mutually exclusive, exhaustive events* that partition the sample space in a way that preserves the unconditional expectation, ignoring how the **selection mechanism** (how the information "at least one is heads" is revealed) alters the posterior probabilities.

#### 2. Precise Name
This is the **Information Select

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism: the events 'at least one H' and 'at least one T' are not mutually exclusive and overlap on the losing outcomes {HT, TH}. This matches Level 2 criteria. However, the response fails to reach Level 3 because it misidentifies the pattern as the 'Two-C

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Three traders received the same bonus but feel differently. Standard economic theory says Basil should be happiest (highest wealth). What is actually determining their reactions, and what does standard theory miss?

**Expected Answer:** **Reference points** — Under Prospect Theory, outcomes are evaluated as gains or losses relative to a reference point — typically the status quo, an expectation, or an aspiration level. The same objective outcome can feel like a gain or a loss depending on the reference point. Cara's 5,000 gold bonus is objectively a gain

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a deviation from **Expected Utility Theory** (which focuses on total wealth) in favor of a psychological evaluation based on **reference points** and **gains/losses relative to expectations**.

### 2. Precise Name
This is the core mechanism of **Prospect Theory**, specifically the concept of **Loss Aversion** operating within a **Reference Dependence** framework.

*   **Reference Dependence:** Utility is derived not from the absolute state of wealth ($W$), but from the change in wealth relative to a reference point ($\Delta W = W_{actual} - W_{expected}$).
*   **Loss Aversion:** The psychological pain of a loss (or a shortfall from expectation) is roughly twice as intense as the pleasure of an equivalent gain.

### 3. Mechanism 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Reference Dependence' and 'Prospect Theory' as the core mechanisms. They explicitly explain that Cara experiences a psychological loss (-5,000) despite an objective gain, directly addressing the key explanation. The response details how different reference points (0

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Lira's patrons demand 40-50 gold to accept a bet that could lose them 20. Risk aversion explains some of this, but not all. What additional psychological mechanism is at work, and how does it show up in the shape of the value function?

**Expected Answer:** **Loss aversion** — Loss aversion means that losses are felt more intensely than equivalent gains. Formally, the value function is steeper below the reference point than above it: |v(-x)| > v(x) for x > 0. The empirical coefficient is approximately lambda = 2.25, meaning losing $100 hurts as much as gaining $225 feels 

**Model Response:**
> ### Analysis of the Ironvale Tavern Scenario

#### 1. Specific Concept Demonstrated
The scenario demonstrates **Loss Aversion**, a core component of **Prospect Theory**.

#### 2. Precise Naming
**Loss Aversion** (specifically quantified by the loss aversion coefficient, $\lambda \approx 2.25$).

#### 3. Mechanism: Why the Reasoning is "Good" or "Bad"
The mechanism relies on the non-linear valuation of outcomes relative to a reference point (usually the status quo).

*   **The Flaw (from a normative/expected value perspective):**
    The patrons are rejecting a bet with a positive Expected Value (EV) or a fair EV.
    *   *Math:* $0.5 \times (-20) + 0.5 \times (+45) = +12.5$ gold.
    *   *Standard Theory:* A rational, risk-neutral agent should accept this immediately. Even a moderately ris

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Loss Aversion and distinguishes it clearly from risk aversion by contrasting the asymmetric value function with concave utility. They accurately cite the lambda coefficient (~2.25), explain the mechanism of overweighting losses relative to gains, and successfully con

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weighting resolve the contradiction?

**Expected Answer:** **Probability weighting function** — In Prospect Theory, objective probabilities are transformed by a weighting function pi(p) before being used in calculations. Small probabilities are overweighted (pi(0.01) > 0.01), large probabilities are underweighted (pi(0.99) < 0.99), and the endpoints 0 and 1 are treated categorically. The resul

**Model Response:**
> Based on the scenario provided by Scholar Lira at the Archon Casino, here is the complete analysis:

### 1. Specific Concept Demonstrated
The scenario demonstrates a systematic deviation from **Expected Utility Theory (EUT)** where individuals do not treat probabilities linearly. Instead, they apply a non-linear weighting function that distorts the objective likelihood of events, leading to inconsistent risk preferences (risk-seeking for low probabilities and risk-averse for high probabilities).

### 2. Precise Name
This is **Probability Weighting** (specifically the **Inverse-S Shaped Probability Weighting Function**) as described in **Prospect Theory** (developed by Daniel Kahneman and Amos Tversky).

The specific cognitive bias driving the "jump" from 99% to 100% is known as the **Certa

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Probability Weighting and the Inverse-S shape, explicitly details the overweighting of small probabilities and underweighting of large ones, and explains the categorical treatment of endpoints via the Certainty Effect. Furthermore, the response connects these concept

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** Lira says the same person can rationally buy lottery tickets and insurance. Under MEU, this is a contradiction. How do the value function and probability weighting function together produce four distinct risk profiles?

**Expected Answer:** **Fourfold Pattern of risk attitudes** — The Fourfold Pattern emerges from combining: (1) The S-shaped value function (risk-averse for gains, risk-seeking for losses) with (2) The probability weighting function (overweight small p, underweight large p). Low-probability gains: overweighting makes the prize loom large → risk seeking. Low-pro

**Model Response:**
> ### Analysis of the Synthesis Chamber Scenario

#### 1. Specific Concept Demonstrated
The scenario demonstrates the **Fourfold Pattern of Risk Attitudes**, a core empirical finding of **Prospect Theory** (developed by Daniel Kahneman and Amos Tversky). It specifically illustrates how human decision-making deviates from the predictions of **Expected Utility Theory (EUT)** or **Maximizing Expected Utility (MEU)** due to the interaction between a non-linear value function and a non-linear probability weighting function.

#### 2. Precise Naming
**The Fourfold Pattern of Risk Attitudes** (within the framework of **Prospect Theory**).

#### 3. Mechanism Explanation: Why is this "Good" or "Bad"?
The reasoning is **psychologically descriptive** (it accurately models how humans *actually* behave) b

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Fourfold Pattern and Prospect Theory. They explicitly detail both required mechanisms (S-shaped value function and probability weighting function) and explain how their interaction drives risk attitudes in all four quadrants (high/low probability gains/losses). T

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** The councillors in Group A and Group B made opposite choices about the same programs. What changed between the two presentations, and why does it matter for rational decision-making?

**Expected Answer:** **Framing effects** — Framing effects occur when logically equivalent descriptions of the same situation lead to different decisions because they shift the reference point. A gains frame activates risk aversion (prefer the sure outcome). A losses frame activates risk seeking (prefer the gamble). Since the underlying opti

**Model Response:**
> ### 1. Specific Concept Demonstrated
The scenario demonstrates a violation of **Descriptive Invariance** (also known as **Extensionality**) in decision theory. It is the classic empirical manifestation of the **Framing Effect**, specifically illustrating **Prospect Theory**.

### 2. Precise Name
**The Framing Effect** (within the framework of **Prospect Theory**).

### 3. Mechanism: Why the Reasoning is Flawed
The reasoning is flawed because it violates the principle of **rational consistency**: logically equivalent options should yield the same preference regardless of how they are described.

*   **The Mathematical Reality**:
    *   Program A (Save 200) = 400 die.
    *   Program C (400 die) = 200 saved.
    *   Program B (1/3 chance save 600) = 1/3 chance 0 die.
    *   Program D (1/3 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Framing Effect and Prospect Theory, explicitly detailing the mechanism of reference point shifts and the asymmetry between risk aversion in gains and risk seeking in losses (Reflection Effect). They clearly state that rational agents should exhibit descriptive in

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Alec and Brin have the same amount of money and face the same bet, but they make opposite choices. What psychological mechanism explains the difference? Is Brin being rational or irrational?

**Expected Answer:** **Mental accounting** — Mental accounting (Thaler) is the tendency to treat money differently depending on which psychological 'account' it belongs to — savings, winnings, salary, found money, etc. Standard economics says money is fungible: a dollar is a dollar regardless of its source. Mental accounting violates fungibili

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic violation of **fungibility** in decision-making, driven by a specific cognitive bias where the source of funds influences the perceived value and risk tolerance of those funds.

### 2. Precise Name
**The House Money Effect** (a specific manifestation of **Mental Accounting**).

*   **Mental Accounting** is the broader concept (proposed by Richard Thaler) where individuals treat money differently depending on its origin or intended use.
*   **The House Money Effect** is the specific behavioral bias where people take greater risks with money they have recently won (perceived as "free" or "the house's") than with their own initial capital.

### 3. Mechanism: Why is this reasoning good or bad?
**The Flaw (Bad Reasoning):**
F

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both Mental Accounting and the House Money Effect. They explicitly explain the violation of fungibility (Level 3 criteria) and provide a sophisticated argument for both sides: the bias aspect (violating rational choice/EV) and the self-control/budgeting utility (Leve

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Sellers demand 7 gold and buyers offer 3 gold for the same mug. The mugs were randomly assigned. What psychological mechanism creates this gap, and why does standard economic theory have trouble explaining it?

**Expected Answer:** **Endowment effect** — The endowment effect is the observation that people demand more to give up an object they own than they would pay to acquire the same object. Sellers set a higher price (WTA: willingness to accept) than buyers (WTP: willingness to pay), even for identical items. The mechanism is loss aversion: once 

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a systematic divergence between the valuation of an asset by its current owner versus a potential buyer, despite the asset and market conditions being identical. This is a classic behavioral economics phenomenon where ownership itself alters perceived value.

### 2. Precise Name
**The Endowment Effect** (often linked to **Loss Aversion** within **Prospect Theory**).

### 3. Mechanism Analysis
The reasoning gap exists because human psychology does not treat "giving up" an item the same way it treats "not acquiring" one.

*   **The Flaw (Irrationality):** In standard neoclassical economics, value is intrinsic to the good and independent of ownership status. A rational agent should value a mug at $X$ regardless of whether they curr

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Endowment Effect and explains the mechanism via Loss Aversion and reference points (ownership). They explicitly mention the weighting of losses vs gains (approx 2x), discuss the WTA/WTP gap causing market inefficiency, and provide excellent edge cases. While they

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Darya insists on going skiing because she paid 300 gold. Her friend says the money is gone either way. Who is right, and what error is Darya making?

**Expected Answer:** **Sunk cost fallacy** — The sunk cost fallacy is the tendency to continue an activity because of past investment (time, money, effort) rather than future expected value. Under MEU, sunk costs are decision-irrelevant: only future costs and benefits should affect current choices. The fallacy arises from mental accounting — t

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic cognitive bias where an individual continues a behavior or endeavor due to previously invested resources (time, money, or effort), even when continuing is irrational because those resources cannot be recovered.

### 2. Precise Name
**The Sunk Cost Fallacy** (also known as the **Concorde Fallacy**).

### 3. Mechanism of the Error
The reasoning is flawed because it conflates **past costs** with **future utility**.

*   **The Flaw:** Darya treats the 300 gold as a variable that can be "saved" by attending the ski trip. However, the money is already spent and non-refundable; it is a **sunk cost**. In decision theory, sunk costs are irrelevant to future choices because they exist in the past and cannot be altered by any cur

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Sunk Cost Fallacy and explains the normative principle that only future costs and benefits matter. They explicitly address the psychological mechanism (loss aversion/mental accounting) by explaining why Darya feels compelled to 'justify' the cost. Furthermore, th

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Mirella knows holding back would be better for both, yet she strips the grove anyway. What structural feature of her situation makes cooperation so difficult?

**Expected Answer:** **Prisoner's Dilemma** — A symmetric 2-player game where individual rationality (dominant strategy D) leads both players to an outcome strictly worse than mutual cooperation. The unique Nash equilibrium is (D,D), yet (C,C) Pareto-dominates it.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic application of **Game Theory**, specifically the **Prisoner's Dilemma**. The specific cognitive mechanism at play is **Dominance Reasoning** (or the Dominance Principle) leading to a **Nash Equilibrium** that is Pareto inefficient.

### 2. Precise Name
**The Prisoner's Dilemma** (manifesting as a **Nash Equilibrium** of mutual defection).

### 3. Mechanism Analysis
The reasoning is "good" in a strictly local, one-shot, non-communicative context but "bad" regarding the collective outcome.

*   **The Logic (Why it feels rational):** Mirella applies **Dominance Strategy**. She reasons:
    *   *If Orik Cooperates:* I get 3 gold by Defecting vs. 3 gold by Cooperating (Wait, in standard PD, Defecting yields *more* if the ot

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Prisoner's Dilemma pattern and explains the mechanism of dominant strategies leading to a Pareto-inefficient Nash equilibrium. Furthermore, the response exceeds the baseline requirements by proposing a valid escape mechanism (Iterated PD/Tit-for-Tat) and analyzin

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks you to find the Nash Equilibrium. For each strategy pair, check: could either cadet do better by switching alone? Which pair survives this test?

**Expected Answer:** **Nash equilibrium** — A Nash Equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. In the PD above, (Fortify, Fortify) is the unique Nash Equilibrium: if A plays Fortify and B plays Fortify, A gets 1. If A switches to Patrol, A gets 0 (worse). Symmetrically fo

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the **Dominant Strategy Equilibrium** within the framework of **Non-Cooperative Game Theory**, specifically illustrating the **Prisoner's Dilemma**. The underlying cognitive mechanism often associated with the failure to achieve the optimal outcome is the **Individual Rationality Paradox** (where individually rational choices lead to a collectively irrational result).

### 2. Precise Name
**The Prisoner's Dilemma** (manifesting as a **Dominant Strategy Nash Equilibrium**).

### 3. Mechanism Analysis
The reasoning is "good" in terms of **individual rationality** but "bad" in terms of **collective efficiency**.

*   **The Mechanism of Dominance:**
    *   **For Cadet A:**
        *   If B chooses *Patrol*, A gets 3 (Patrol) vs. 5 (F

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies (Fortify, Fortify) as the unique Nash Equilibrium and rigorously demonstrates why neither player benefits from unilateral deviation. Furthermore, the response explicitly explains why (Patrol, Patrol) is not an equilibrium by detailing the incentive to deviate (gainin

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?

**Expected Answer:** **Iterated PD and cooperation** — In a finitely repeated PD with known endpoint, backward induction predicts defection every round. But in an infinitely repeated PD (or one with unknown endpoint), the Folk Theorem shows that cooperation can be sustained as a Nash Equilibrium if players value future payoffs enough (discount factor de

**Model Response:**
> ### Analysis of the Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates the **Fragility of Deterministic Reciprocity in Noisy Environments**, specifically highlighting the **Error-Correction Failure** inherent in strict Tit-for-Tat (TFT) strategies.

#### 2. Precise Name
This phenomenon is known as the **Echo Effect** (or **Vicious Cycle of Retaliation**). In game theory literature, it is often discussed under the concept of **Noise Sensitivity** or the **Need for Generosity** (as opposed to strict reciprocity).

#### 3. Mechanism: Why This Reasoning is Flawed
The mechanism relies on a rigid, deterministic feedback loop that cannot distinguish between **malicious defection** and **accidental noise**.

*   **The Trigger:** Opponent A defects by mistake (noise).
*   **The 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies Tit-for-Tat's properties (nice, retaliatory) and explains the mechanism of punishment and the failure mode in noisy environments. However, the response focuses almost exclusively on the 'noise' aspect and fails to address the core prompt requirements regarding the 's

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find both Nash Equilibria in the Stag Hunt. Which is payoff-dominant? Which is risk-dominant? Which would you choose, and what does your choice depend on?

**Expected Answer:** **Stag Hunt** — The Stag Hunt (from Rousseau) has two pure-strategy Nash Equilibria: (Stag, Stag) = (5,5) and (Hare, Hare) = (2,2). (Stag, Stag) is payoff-dominant (better for everyone). (Hare, Hare) is risk-dominant (safer — you get 2 guaranteed regardless of partner). The core tension: cooperation requires trust.

**Model Response:**
> ### Analysis of the Hunting Scenario

#### 1. Specific Reasoning Pattern & Concept
The scenario demonstrates the **Stag Hunt** game, a classic problem in **Game Theory**. The specific reasoning pattern at play is the tension between **Pareto Efficiency** (maximizing collective gain) and **Risk Dominance** (maximizing individual safety).

The underlying cognitive bias often associated with choosing the "safe" option in this context is **Risk Aversion** or **Defection due to Lack of Trust** (sometimes linked to the *Prisoner's Dilemma* mindset, though the payoff structure is distinct).

#### 2. Precise Name
**The Stag Hunt** (also known as the **Assurance Game**).

#### 3. Mechanism: Why is this reasoning "Good" or "Bad"?
The mechanism relies on the conflict between two Nash Equilibria:

*  

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Stag Hunt pattern and distinguishes it from the Prisoner's Dilemma. They accurately identify both Nash Equilibria and explicitly explain the distinction between payoff-dominance (Pareto optimal) and risk-dominance (Maximin). Furthermore, the response exceeds the 

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find all Nash Equilibria in this game, including any mixed-strategy equilibrium. Why is the mixed equilibrium worse for both players than either pure equilibrium?

**Expected Answer:** **Battle of the Sexes** — Battle of the Sexes has two pure-strategy Nash Equilibria: (Opera, Opera) = (3,2) and (Tournament, Tournament) = (2,3). Both are coordination equilibria — both players prefer being together over being apart. But they disagree on which is better: Helena prefers (Opera, Opera), Roderick prefers (Tourn

**Model Response:**
> ### Analysis of the Scheduling Dispute

#### 1. Specific Reasoning Pattern / Concept
The scenario demonstrates a classic **Coordination Game**, specifically a variant of the **Battle of the Sexes** (BoS). The underlying decision-theoretic concept is **Strategic Complementarity** within a non-zero-sum game where players have conflicting preferences over the equilibrium outcome but a shared interest in avoiding the non-cooperative outcome.

#### 2. Precise Naming
**The Battle of the Sexes (Coordination Game with Conflicting Preferences).**

*Note: While often confused with the Prisoner's Dilemma, this is distinct because mutual cooperation (attending together) yields a positive payoff for both, whereas the Prisoner's Dilemma involves a dominant strategy to defect that leads to a suboptimal o

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Battle of the Sexes and explains the coordination-with-conflict structure. They accurately describe the pure strategy equilibria and the risk of miscoordination. Crucially, they exceed Level 3 by discussing real-world resolution mechanisms (communicati

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** You and your contact must meet without communication. Why do people converge on the same location and time? What property makes some answers more likely than others, and is this a rational process?

**Expected Answer:** **Focal points (Schelling points)** — A focal point is a solution to a coordination game that attracts players' attention because it is salient — prominent, unique, culturally significant, or symmetric. Focal points work because of mutual expectations: I go to the fountain because I expect you to expect me to expect... etc. Sources of s

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates **Schelling Point coordination** (also known as a **focal point**), grounded in the decision-theoretic concept of **Common Knowledge**.

### 2. Precise Name
**Schelling Point** (or **Focal Point**).

### 3. Mechanism Analysis
This reasoning is **good** (rational) in coordination games where communication is impossible, but it relies on a specific psychological mechanism rather than logical deduction of the "best" outcome.

*   **The Mechanism:** In the absence of communication, players cannot negotiate. Instead, they rely on **salience**—features that stand out due to culture, prominence, or uniqueness. The logic is recursive: "I will choose X because X is the most obvious choice. I know you will choose X because X is the most o

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a Schelling/Focal point and provides a strong explanation of salience and the recursive mutual-expectation mechanism ('I know you will choose X...'). They also list multiple sources of salience and relevant edge cases. However, the response does not re

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid.

**Expected Answer:** **Convention (Lewis)** — A convention is a regularity R in behavior that is (1) followed by everyone, (2) expected by everyone, (3) preferred by everyone given others' conformity, (4) has at least one alternative R' that could have served instead, and (5) is common knowledge. Conventions are solutions to recurrent coordinat

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the concept of a **Coordination Equilibrium** within **Game Theory**, specifically illustrating **David Lewis's theory of Conventions**. It is not a logical fallacy or a cognitive bias in the traditional sense; rather, it is a rational solution to a specific type of strategic interaction where the primary goal is alignment, not optimization of an intrinsic property.

### 2. Precise Name
**Conventionalism** (specifically regarding **Coordination Games** or **Schelling Points**).

In the context of decision theory, this is the emergence of a **Nash Equilibrium** driven by **Common Knowledge** and **Self-Fulfilling Prophecies**.

### 3. Mechanism Analysis
The reasoning is **logically sound and rational**, not flawed. Here is why:

* 

**Score:** 4/4 ████
**Judge Reasoning:** The student demonstrates a masterful understanding of Lewis's theory of conventions. They correctly identify all five conditions (including the critical common knowledge requirement and arbitrariness), explain the self-reinforcing expectation structure, and discuss path dependence and switching cost

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor has drawn the Entry Game tree. Identify the decision nodes, the branches, and the terminal payoffs. What information does each player have when they move?

**Expected Answer:** **Game trees (extensive form)** — A game tree represents a sequential game with nodes (decision points), branches (available actions), terminal nodes (outcomes with payoffs), and information sets (what each player knows when they move). Unlike the normal form (matrix), the extensive form explicitly represents the order of moves, whi

**Model Response:**
> Based on the scenario provided, here is the complete analysis of the strategic interaction and the reasoning patterns involved.

### 1. The Core Concept Demonstrated
The scenario demonstrates **Backward Induction** (the solution method) used to identify the **Subgame Perfect Nash Equilibrium (SPNE)**.

However, the *reasoning pattern* that often leads players astray in this specific setup is the **Threat Credibility Fallacy** (or the failure to distinguish between a Nash Equilibrium and a Subgame Perfect Equilibrium). A naive player might believe the Incumbent will "Fight" to deter entry, whereas rational analysis proves the threat is non-credible.

### 2. Precise Naming
*   **Solution Concept:** Subgame Perfect Nash Equilibrium (SPNE).
*   **Reasoning Method:** Backward Induction.
*   **C

**Score:** 4/4 ████
**Judge Reasoning:** The student demonstrates a perfect understanding of the game tree structure and the associated reasoning patterns. They correctly identify the sequential nature of the game, explicitly trace the paths via backward induction (Level 3 criteria), and go further to distinguish between the Nash Equilibri

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** Apply backward induction to the Entry Game. Start at the last decision node and work backward. What is the subgame perfect equilibrium? Why is the Incumbent's threat to Fight not credible?

**Expected Answer:** **Backward induction** — Backward induction solves extensive-form games by starting at the terminal nodes and working backward. At each decision node, the player is assumed to choose their optimal action. The resulting strategy profile is a subgame perfect equilibrium (SPE). In the Entry Game: (1) At Incumbent's node: Accom

**Model Response:**
> Based on the scenario provided, here is the complete analysis:

### 1. Specific Reasoning Pattern
The scenario demonstrates the application of **Backward Induction** to solve a dynamic game of perfect information. Specifically, it highlights the concept of **Credibility** (or the lack thereof) in strategic threats. The reasoning pattern identifies that a threat is only effective if it is rational for the threatener to carry it out when the time comes.

### 2. Precise Name
The precise game-theoretic concept is the **Subgame Perfect Equilibrium (SPE)**.
*   The specific phenomenon described regarding the threat is the **Non-Credible Threat**.
*   The method used to derive this is **Backward Induction**.

### 3. Mechanism: Why this reasoning is "Good"
This reasoning is considered "good" (and 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Backward Induction and Subgame Perfect Equilibrium (SPE). They accurately derive the solution (Enter, Accommodate) by analyzing the Incumbent's node first, then the Entrant's. Crucially, they explicitly distinguish why (Stay Out, Fight) is a Nash Equilibrium but not 

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The Entry Game has two Nash Equilibria. The instructor says one of them relies on a non-credible threat. Which one, and why does SPE eliminate it?

**Expected Answer:** **Subgame perfect equilibrium** — SPE (Selten 1965) requires that a strategy profile be a Nash Equilibrium in every subgame. A subgame is any part of the game tree that forms a complete game on its own. SPE eliminates NE that rely on non-credible threats — strategies that would not be followed through if the relevant decision node w

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates the distinction between **Nash Equilibrium** and **Subgame Perfect Equilibrium (SPE)**, specifically highlighting the failure of **Non-Credible Threats** (or **Empty Threats**) within the framework of **Dynamic Games**. The core decision-theoretic concept is **Backward Induction**.

### 2. Precise Name
**The Problem of Non-Credible Threats** (resolved via **Subgame Perfection**).

*Note: While often associated with the "Chainstore Paradox," the specific logical error being corrected here is the acceptance of a Nash Equilibrium that relies on an action that is not a best response in a subgame.*

### 3. Mechanism: Why the Reasoning is Flawed
The reasoning in the "Stay Out, Fight" equilibrium is flawed because it violates the princ

**Score:** 4/4 ████
**Judge Reasoning:** The student provides a flawless response that exceeds the Level 4 criteria. They correctly identify the pattern (SPE vs. NE), formally explain the mechanism using sequential rationality and backward induction, explicitly solve for the unique SPE (Enter, Accommodate), and provide a sophisticated disc

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Question:** Apply backward induction to the Centipede Game. What does it predict? Do you find the prediction convincing? What assumption is doing the heavy lifting, and what happens if you relax it?

**Expected Answer:** **Centipede Game** — The Centipede Game is a sequential game where two players alternate between stopping (taking a smaller immediate payoff) and continuing (allowing the total payoff to grow). Backward induction predicts immediate stopping — the unique SPE. But this is paradoxical: both players would be much better off

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the **Centipede Game Paradox**, which highlights the conflict between **Backward Induction** (the standard solution concept for finite sequential games of perfect information) and **Pareto Efficiency** (social optimality). The specific cognitive tension is the **Paradox of Rationality**: the idea that strictly rational agents, following the dominant strategy of maximizing individual payoff at every step, arrive at a collectively suboptimal outcome.

### 2. Precise Name
**The Centipede Game Paradox** (specifically illustrating the failure of **Backward Induction** to predict cooperative behavior in finite repeated games).

### 3. Mechanism: Why the Reasoning is "Good" yet "Bad"

**Why it is "Good" (Theoretical Soundness):**
The log

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Centipede Game and applies backward induction to reach the theoretical prediction (stop at Node 1). They clearly articulate the paradox between individual rationality and Pareto efficiency. Crucially, they identify Common Knowledge of Rationality (CKR) as the cri

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

**Expected Answer:** **Evolutionarily Stable Strategy (ESS)** — An ESS (Maynard Smith) is a strategy that, when adopted by almost all members of a population, cannot be invaded by any rare mutant strategy. Formally: S is ESS if for any mutant M, either (1) E(S,S) > E(M,S), or (2) E(S,S) = E(M,S) and E(S,M) > E(M,M). In Hawk-Dove with V<C, neither pure strategy i

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates the application of **Evolutionary Game Theory**, specifically the calculation of an **Evolutionarily Stable Strategy (ESS)** in a mixed-strategy equilibrium.

### 2. Precise Name
**Mixed-Strategy Nash Equilibrium (in the context of ESS)** derived via the **Indifference Principle**.

### 3. Mechanism Analysis
The reasoning in the scenario is **logically sound and mathematically correct** within the framework of evolutionary biology. It is **not** a fallacy or bias.

*   **Why it is good reasoning:**
    *   **Definition Adherence:** The biologist correctly applies the formal definition of an ESS: a strategy that, if adopted by a population, cannot be invaded by a rare mutant.
    *   **Pure Strategy Rejection:**
        *   *Hawk

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as ESS, demonstrates that neither pure strategy is stable, and accurately calculates the mixed ESS at p=V/C=2/3. Crucially, the response explicitly distinguishes between population-level polymorphism and individual mixed strategies, and notes that the mec

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The biologist perturbs the Hawk population from 50% to 51%. Show that the system returns to 50% by calculating fitness for each strategy. What does this tell you about the stability of the mixed ESS?

**Expected Answer:** **Replicator dynamics** — The replicator dynamics models how strategy frequencies change over time based on fitness. The equation dx_i/dt = x_i(f_i - F) says: strategies that outperform average grow; those that underperform shrink. Key properties: (1) ESS are stable fixed points of replicator dynamics. (2) Not all fixed poin

**Model Response:**
> Based on the scenario provided, here is the complete analysis:

### 1. Specific Reasoning Pattern
The scenario demonstrates the **stability analysis of an Evolutionarily Stable Strategy (ESS) via local perturbation** within the framework of **Replicator Dynamics**.

### 2. Precise Name
**Local Stability Analysis (or Lyapunov Stability) in Replicator Dynamics.**
*Note: While the biologist is performing a correct mathematical derivation, if one were to generalize this specific 2x2 Hawk-Dove result to claim that "all equilibria are self-correcting" without checking second-order conditions or global dynamics, it would be the **Fallacy of Hasty Generalization** regarding stability. However, in this specific context, the biologist is correctly demonstrating the **Dynamic Stability of a Mixed ESS

**Score:** 4/4 ████
**Judge Reasoning:** The student demonstrates a masterful understanding of replicator dynamics. They correctly identify the pattern (stability analysis via perturbation), explain the mechanism using the replicator equation logic (fitness differences driving frequency changes), and explicitly address the distinction betw

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In the evolutionary Stag Hunt, what determines whether cooperation or defection wins? Why does Skyrms call the cooperative equilibrium a 'social contract'? What factors help cooperation evolve?

**Expected Answer:** **Evolution of cooperation** — In evolutionary Stag Hunt, cooperation (Stag) can evolve if enough of the population already cooperates. The threshold is p=0.5 in standard payoffs. Above the threshold, cooperation is self-reinforcing; below, it collapses. This is the basin of attraction concept. Factors that help cooperation evolv

**Model Response:**
> ### 1. Reasoning Pattern & Concept
The scenario demonstrates **Path Dependence** within the framework of **Evolutionary Game Theory**, specifically illustrating the concept of **Multiple Equilibria with Risk Dominance vs. Payoff Dominance**.

While the biologist's calculation is mathematically correct for the specific payoff matrix provided, the underlying reasoning pattern highlights how historical accidents (initial conditions) determine long-term societal outcomes, rather than rational optimization alone.

### 2. Precise Naming
**The Coordination Problem with Risk-Dominant vs. Payoff-Dominant Equilibria.**

*   **Payoff Dominant Equilibrium:** (Stag, Stag) yielding (5, 5). This is the optimal outcome for the group.
*   **Risk-Dominant Equilibrium:** (Hare, Hare) yielding (2, 2). This is

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the threshold (p=0.5) and the concept of basins of attraction. They discuss multiple factors promoting cooperation (reputation, signaling, correlated strategies, payoff modification). Crucially, they explicitly address Skyrms's argument regarding the emergence of nor

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Torva says her profit from the sword is eighty gold. Is she right? What is she forgetting to account for?

**Expected Answer:** **Opportunity cost** — The opportunity cost of an action is the value of the next-best alternative forgone. Torva treats the sword's revenue (80 gold) as pure profit, but by choosing the sword she forgoes the 50-gold axle repair. Her net gain from choosing the sword over the axle is 80 - 50 = 30 gold, not 80 gold. The 50 

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a failure to account for **Opportunity Cost**. Torva is evaluating her decision based solely on the explicit revenue of the chosen option while ignoring the value of the next best alternative she is forgoing.

### 2. Precise Name
**Ignoring Opportunity Cost** (or the **Opportunity Cost Fallacy**).

### 3. Mechanism of the Error
Torva's reasoning is flawed because she equates **Gross Revenue** with **Net Benefit**.
*   **Her Logic:** Profit = Revenue of Option A ($80).
*   **The Reality:** In a constrained resource scenario (one free day), the true economic profit of choosing Option A is:
    $$ \text{Net Benefit} = \text{Revenue of Option A} - \text{Revenue of Option B (Forgone)} $$
*   **The Flaw:** By stating "The sword pays e

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'Opportunity Cost,' explicitly calculates the net gain ($80 - $50 = $30), and provides a sophisticated explanation of why the concept matters in scenarios with scarce resources. Furthermore, the response exceeds the basic requirements by thoughtfully a

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Hilde outproduces Oskar in both wheat and flax. She says trade cannot benefit her. Is she right? Calculate the opportunity costs and determine who should specialize in what.

**Expected Answer:** **Comparative advantage** — Hilde has absolute advantage in both goods, but comparative advantage depends on opportunity cost. Hilde's opportunity cost of 1 bolt of flax = 2 bushels of wheat (12/6). Oskar's opportunity cost of 1 bolt of flax = 4/3 bushels of wheat. Oskar has a lower opportunity cost for flax, so he has compara

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a fundamental misunderstanding of economic efficiency where an agent conflates **absolute advantage** with **comparative advantage**. Hilde's reasoning relies on the observation that she has an absolute advantage in both goods (she produces more of each per unit of time) and incorrectly concludes that this makes trade mutually impossible or one-sided.

### 2. Precise Name
**The Confusion of Absolute Advantage with Comparative Advantage** (often referred to simply as the **Comparative Advantage Fallacy** in lay terms).

### 3. Mechanism of the Error
Hilde's reasoning is flawed because it focuses on **productivity levels** (absolute output) rather than **opportunity costs** (what must be given up to produce a specific good).

*   

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the confusion between absolute and comparative advantage. They accurately calculate all opportunity costs for both agents, correctly assign comparative advantages (Hilde in wheat, Oskar in flax), and explicitly explain why absolute advantage is irrelevant to the deci

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?

**Expected Answer:** **Constrained optimization** — The problem is to minimize cost subject to constraints. Food constraint: 3R >= 15, so R >= 5 (minimum 5 ration packs). Torch constraint: 4T >= 8, so T >= 2 (minimum 2 torch bundles). Cost: 5R + 10T. Minimum cost = 5(5) + 10(2) = 25 + 20 = 45 gold. This satisfies both constraints and is within budget

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates **Constrained Optimization** (specifically, a **Linear Programming** problem) framed within a **Resource Allocation** context.

However, from a cognitive perspective, the prompt highlights a common **Decision-Making Trap**: the tendency to treat a multi-variable optimization problem as a simple "satisficing" task or to assume that the *minimum* cost will automatically equal the *maximum* budget available, or conversely, to overlook the discrete nature of the items (integer constraints) when calculating the solution.

The specific concept being tested is **Integer Linear Programming (ILP)**, where the decision variables (number of rations and torches) must be whole numbers, not fractions.

### 2. Precise Naming
**Integer Linear P

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern (Integer Linear Programming/Constrained Optimization) and provides a sophisticated mechanism analysis, including unit cost comparisons and potential pitfalls. However, the response is incomplete: the step-by-step solution cuts off mid-sentence while calcu

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Each potion sells for 15 gold. The cost of each additional potion rises: 5, 8, 12, 16, 22. How many potions should Elara brew, and why?

**Expected Answer:** **Marginal analysis** — Marginal analysis compares the marginal benefit (MB) to the marginal cost (MC) of each additional unit. Brew if MB > MC; stop when MC >= MB. Revenue per potion (MB) = 15 gold. MC of potions: 1st=5, 2nd=8, 3rd=12, 4th=16, 5th=22. For potions 1-3, MB(15) > MC. For potion 4, MC(16) > MB(15). Elara shou

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates the application of **Marginal Analysis** (specifically, the **Marginal Principle** of profit maximization).

While the prompt asks for a "fallacy" or "bias," the reasoning Elara is attempting to perform is actually the **correct economic framework** for this problem. There is no inherent logical fallacy in her notes; rather, the "trap" lies in the common human tendency to ignore marginal costs in favor of **Average Cost** or **Sunk Cost** thinking. If Elara were to stop brewing because the *average* cost is rising, or to continue because the *total* revenue is high, she would be falling into those biases. However, the data provided is set up specifically to test the ability to apply the **Marginal Decision Rule**.

### 2. Precis

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Marginal Analysis and applies the Marginal Decision Rule (MR >= MC) flawlessly. They calculate the marginal profit for each unit, correctly determine the optimal quantity is 3 potions, and explicitly calculate the total profit (20 gold). Furthermore, t

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Captain Hale says she should let the others pay for the lighthouse oil. Her reasoning seems logical from her own perspective. What happens if every captain follows the same logic? Why does this situation arise?

**Expected Answer:** **Public goods and free riding** — The lighthouse is a public good: non-rival (one captain using the light does not diminish it for others) and non-excludable (you cannot prevent a non-paying captain from seeing the light). These properties create a free-rider incentive: each captain benefits from the lighthouse regardless of whether

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic **Collective Action Problem** rooted in **Game Theory**, specifically the **Prisoner's Dilemma** applied to a public good. The specific behavioral reasoning pattern is the **Free Rider Problem**.

### 2. Precise Name
**The Free Rider Problem** (within the context of a **Prisoner's Dilemma**).

### 3. Mechanism Analysis
The reasoning is "good" from a strictly individual, short-term, rational self-interest perspective but "bad" from a collective, long-term perspective.

*   **The Logic (Why it seems rational):** Captain Hale's argument relies on the characteristics of a **public good**: it is *non-excludable* (once the light is on, everyone benefits regardless of payment) and *non-rivalrous* (one captain using the light 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Free Rider Problem and the Prisoner's Dilemma. They explicitly define the key properties of public goods (non-excludable and non-rivalrous) and explain how individual rationality leads to collective failure. Furthermore, the response exceeds the Level 3 requireme

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Elder Yara says every family is acting sensibly, yet the lake is dying. How can individual rationality produce collective disaster? What is the structural problem?

**Expected Answer:** **Commons problems (Tragedy of the commons)** — Lake Mirren is a common-pool resource: rival (each fish caught is unavailable to others) but non-excludable (no family can be prevented from fishing). Each family captures the full benefit of each additional fish they catch but bears only a fraction of the cost (resource depletion shared across all 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **individual rationality** and **collective rationality**. Each family acts based on the premise that maximizing their own immediate catch is the optimal strategy, assuming that if they do not take the fish, others will. However, when every actor follows this same logic, the shared resource is depleted, leading to a worse outcome for everyone.

### 2. Precise Name
This is the **Tragedy of the Commons**, a specific instance of the **Prisoner's Dilemma** applied to a multi-player resource management context.

### 3. Mechanism of Failure
The reasoning is "good" from a strictly **micro-level, short-term perspective** but "bad" from a **macro-level, long-term perspective**.

*   **The Incentive Structure:** The benef

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the Tragedy of the Commons and the underlying Prisoner's Dilemma structure. They explicitly explain the incentive asymmetry (100% private benefit vs. shared cost) and the resulting Nash equilibrium. Furthermore, they exceed the Level 3 requirements by proposing speci

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Sera and Brenn create 80 gold in surplus from trade. Sera's outside option gives her 15 gold surplus; Brenn's gives him 10. How should they split the 80 gold surplus, and why?

**Expected Answer:** **Bargaining and fairness (Nash bargaining)** — The surplus from trade is 80 gold. Each merchant's outside option (BATNA) sets a floor: Sera will not accept less than 15 gold surplus (her alternative deal), and Brenn will not accept less than 10. The remaining surplus after securing both outside options is 80 - 15 - 10 = 55 gold. Nash bargaining 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a failure to apply **Game-Theoretic Bargaining Principles**, specifically the **Nash Bargaining Solution** (or the Shapley Value in cooperative game theory). The merchants are exhibiting the **Endowment Effect** combined with **Anchoring Bias**, where they anchor their demands on their maximum possible claim (50 gold each) rather than their actual **Outside Options** (BATNA - Best Alternative to a Negotiated Agreement).

### 2. Precise Name
**The BATNA Fallacy** (or **Failure to Account for Outside Options**).
*Note: In strict game theory terms, this is a miscalculation of the **Disagreement Point**.*

### 3. Mechanism: Why the Reasoning is Flawed
The reasoning is flawed because the merchants are calculating their "walk-away" valu

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern (Nash Bargaining/BATNA), accurately calculates the specific split (Sera 42.5, Brenn 37.5) by accounting for outside options, and provides a sophisticated discussion of edge cases (monopoly, coercion, repeated games) that explains how bargaining power shif

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Lady Ashworth paid Corbin a flat wage and got a poor harvest. She suspects shirking but cannot prove it. What is the structural problem with her contract, and how might she redesign it?

**Expected Answer:** **Principal-agent problems and moral hazard** — The principal (Ashworth) delegates a task to an agent (Corbin) whose effort she cannot observe. Under a flat wage, the agent bears the cost of effort but captures none of the benefit (the extra apples go to the principal). This misalignment of incentives is moral hazard: the agent has both the oppor

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic **Principal-Agent Problem** driven by **Misaligned Incentives** within a **Fixed-Wage Contract**. Specifically, it illustrates the economic concept of **Moral Hazard**.

### 2. Precise Name
**Moral Hazard** (arising from a **Fixed-Salary Contract** in an environment of **Information Asymmetry**).

### 3. Mechanism Analysis
The reasoning is "bad" (or rather, the contract design is flawed) because it creates a disconnect between the agent's (Corbin's) effort and his reward, while the principal (Lady Ashworth) bears all the risk.

*   **The Incentive Structure:** Under a flat wage of 50 gold, Corbin's marginal benefit for extra effort is zero. If he works harder, Lady Ashworth keeps the extra apples; if he shirks, he still 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Principal-Agent problem and Moral Hazard, explicitly explains the information asymmetry (hidden action), and proposes multiple structured solutions (performance pay, monitoring, efficiency wages). Crucially, the response distinguishes this from adverse selection 

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Using the market board data, find the price at which quantity supplied equals quantity demanded. What happens at prices above or below this equilibrium?

**Expected Answer:** **Supply, demand, and market equilibrium** — At equilibrium, quantity supplied equals quantity demanded. From the table: at price = 2, excess demand (shortage) of 60. At price = 8, excess supply (surplus) of 60. At price = 6, Qs = 60 = Qd = 40 — not yet equal. Interpolating (or reading the table), equilibrium is at price = 5, where both Qs and

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the application of **Market Equilibrium Analysis** within a **Supply and Demand** framework. The market master is intuitively searching for the point where two opposing forces (supply and demand) balance, avoiding the errors of **Price Rigidity** (setting a fixed price based on past anecdotal failure rather than current data).

### 2. Precise Name
**Market Clearing Price** (or **Equilibrium Price**).

The specific cognitive error the master is avoiding by seeking this price is **Disequilibrium Pricing** caused by **Anchoring Bias** (fixating on the price of 2 or 8 based on last week's outcome) or **Sunk Cost Fallacy** (trying to fix the "waste" of unsold grain by arbitrarily changing prices without data).

### 3. Mechanism: Why th

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the supply and demand pattern and explains the mechanisms of shortage and surplus well, including good edge cases. However, the student fails to find the correct equilibrium. They incorrectly state that at Price 6, Qs equals Qd (claiming both are 60), whereas the cor

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** The king sets a price ceiling of 3 gold per bushel. Equilibrium was at 5 gold and 50 bushels. What happens to quantity supplied, quantity demanded, and the market? What trades are lost?

**Expected Answer:** **Price controls and deadweight loss** — A binding price ceiling (set below equilibrium) creates a shortage: quantity demanded exceeds quantity supplied. At P=3, Qs=30 and Qd=70, shortage=40. Some mutually beneficial trades that would occur at equilibrium (P=5, Q=50) no longer happen. The lost surplus from these unrealized trades is deadwe

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates the **Fallacy of Composition** (specifically applied to market mechanisms) combined with a failure to account for **Unintended Consequences** arising from **Price Controls**. The core error is assuming that a policy beneficial to a specific subset of participants (those who successfully buy at the lower price) will result in a net benefit for the group or society as a whole, while ignoring the systemic distortion of incentives.

### 2. Precise Name
**The Fallacy of Composition** (in the context of **Price Ceiling Analysis**).

*Note: In economics, this is often discussed alongside the **Broken Window Fallacy** (focusing only on the visible benefit of cheap grain while ignoring the invisible loss of the 40 bushels not produced or

**Score:** 4/4 ████
**Judge Reasoning:** The student demonstrates a comprehensive understanding of price ceilings. They correctly calculate the shortage (Qd=70, Qs=30, gap=40), explicitly identify and explain deadweight loss as lost mutually beneficial trades, and discuss secondary effects like black markets and non-price rationing. Furthe

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** Grist says his business is profitable and efficient. Wynn says Clearwater is paying part of his costs. Who is right, and what does this situation reveal about market prices?

**Expected Answer:** **Externalities** — A negative externality is a cost imposed on third parties who are not involved in the transaction. Grist's private cost is 40 gold, but the social cost includes the 20 gold per week Clearwater spends on water treatment. The true social cost of production is 60 gold, making Grist's true profit 40, no

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic case of **Market Failure** caused by an **Externality**, specifically a **Negative Production Externality**.

### 2. Precise Naming
**Negative Externality** (or **Unpriced External Cost**).

### 3. Mechanism Analysis
The reasoning is flawed because Grist's decision-making process relies on a **partial equilibrium analysis** that ignores the **social cost** of his actions.

*   **Private Cost vs. Social Cost:** Grist calculates his profit based solely on his *private costs* (40 gold). However, the *social cost* includes his private costs *plus* the external costs imposed on Clearwater (20 gold for filtration + the intangible and medical costs of the children's illness).
*   **The Distortion:** Because Grist does not pay f

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the negative externality and explains the divergence between private and social costs, noting the resulting overproduction (Level 3 criteria). Furthermore, the response exceeds Level 3 by proposing specific internalization mechanisms (Pigouvian tax, Coasean bargainin

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral?

**Expected Answer:** **Information asymmetry and adverse selection (lemons problem)** — When sellers know more about product quality than buyers, buyers cannot distinguish good from bad. They offer a price reflecting average quality. Owners of above-average horses find this price too low and withdraw. The remaining pool is worse, buyers adjust downward, more good horses leave — a death

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic breakdown in market efficiency caused by **information asymmetry** leading to a self-reinforcing cycle of market collapse. The core mechanism is that the inability of buyers to distinguish quality forces them to offer a single "average" price, which drives high-quality sellers out of the market, thereby lowering the average quality further.

### 2. Precise Name
This is known as **Akerlof's Market for Lemons** (or simply **The Market for Lemons**), a concept introduced by economist George Akerlof in his 1970 paper. It is the foundational example of **Adverse Selection**.

### 3. Mechanism Analysis
The reasoning pattern here is not a logical fallacy in the traditional sense (like a non-sequitur); rather, it is a **rational

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the pattern as 'information asymmetry' and 'adverse selection' (Akerlof's Market for Lemons). They provide a clear, step-by-step explanation of the spiral mechanism where average pricing drives out high-quality goods. Furthermore, they exceed the baseline requirement

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Nobody buys the Barrel Mug, yet adding it to the menu increases Large Ale sales. The tip jar moved but the tip amount was not suggested. What is going on in both cases, and is it ethically acceptable?

**Expected Answer:** **Behavioral economics in markets: nudges and choice architecture** — Two phenomena are at work. First, the decoy effect: the Barrel Mug is a dominated option that no one chooses, but its presence makes the Large Ale seem more reasonable by comparison. It shifts the reference point. Second, choice architecture: the placement of the tip jar changes behavior without cha

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a cognitive bias where the presence of a clearly inferior or extreme option (the "decoy") alters the perceived value of other options, shifting consumer preference toward a target option that was previously less popular. Additionally, the tip jar placement illustrates the impact of **framing** and **salience** on decision-making.

### 2. Precise Name
The primary concept is the **Decoy Effect** (also known as the **Asymmetric Dominance Effect**).
The secondary concept regarding the tip jar is **Salience Bias** (or **Framing Effect**).

### 3. Mechanism: Why This Works (and Why It's "Bad" Reasoning)
**The Mechanism:**
Human decision-making is rarely based on absolute value; it is heavily reliant on **comparative evaluation**.
*   **

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both the Decoy Effect and Choice Architecture (framing/salience). They explain the mechanism of comparative evaluation versus absolute utility accurately. Crucially, they address the ethical tension between manipulation and helpful nudging, and they provide specific 

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Breck says the storm is good for the economy because it creates repair jobs. The clerk is skeptical. Who is right, and what is Breck failing to consider?

**Expected Answer:** **Broken window fallacy** — Breck counts the economic activity generated by repairing storm damage (the seen) but ignores the economic activity that the same money would have generated if spent on something else (the unseen). The glazier's gain is real, but the shopkeepers now spend money on window repairs instead of on new in

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a classic logical error where the visible economic activity generated by repair work is mistaken for a net economic gain, while ignoring the invisible costs of the destruction itself.

### 2. Precise Name
**The Broken Window Fallacy** (also known as the *Parable of the Broken Window*).
*Origin:* Popularized by French economist Frédéric Bastiat in his 1850 essay *"That Which Is Seen, and That Which Is Not Seen."*

### 3. Mechanism Analysis
The reasoning is flawed because it focuses exclusively on the **seen** effects while ignoring the **unseen** opportunity costs.

*   **The Seen (The Fallacy):** Alderman Breck correctly identifies that the glazier, carpenter, and lumber mill will earn money. This is the immediate, visible t

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the Broken Window Fallacy and clearly articulates the 'seen vs. unseen' distinction and opportunity cost. Furthermore, the response exceeds the baseline requirements by explicitly detailing legitimate edge cases (underemployment, creative destruction) where the logic

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Dagan says that if Brassholm gains from trade, Ardenvale must lose. Petra says both sides can gain. Who is right, and why?

**Expected Answer:** **Zero-sum thinking** — Dagan falsely assumes that trade is zero-sum — that total value is fixed and any gain for one party is a loss for the other. In reality, voluntary trade creates value because parties exchange goods they value less for goods they value more. Ardenvale values iron more than its surplus grain; Brasshol

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a fundamental misunderstanding of how value is created in exchange, rooted in a specific economic fallacy. Dagan assumes that the total amount of wealth in the system is fixed and that one party's gain is mathematically equivalent to the other party's loss.

### 2. Precise Name
**The Zero-Sum Fallacy** (also known as the **Zero-Sum Bias** or **Fixed-Pie Bias**).

In a broader economic context, this is the rejection of **Comparative Advantage** and the benefits of **Voluntary Exchange**.

### 3. Mechanism of the Reasoning
**Why it is flawed:**
Dagan's reasoning fails because it treats wealth as a static resource (like a pie of fixed size) rather than a dynamic creation of value.
*   **Subjective Value:** Value is not intrinsic to

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Zero-Sum Fallacy and explicitly names Dagan's 'fixed-pie' assumption as the core error. They provide a robust explanation of value creation through subjective utility and marginal analysis, clearly articulating why both parties gain. Furthermore, the response goe

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter?

**Expected Answer:** **Rapoport's Rules** — A four-step protocol for productive disagreement: (1) restate the opponent's position so well they endorse the restatement, (2) list genuine points of agreement, (3) acknowledge what you learned from them, (4) only then offer criticism. Corwin follows all four steps in sequence.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates **Steel-manning** (the antithesis of the Straw Man fallacy), combined with **Systematic Re-evaluation of Evidence** and **Long-term vs. Short-term Trade-off Analysis**.

### 2. Precise Name
**Steel-manning** (specifically applied to **Multi-Criteria Decision Analysis**).

### 3. Mechanism: Why this reasoning is effective
The reasoning is effective because it dismantles the adversarial nature of the debate and replaces it with a collaborative problem-solving framework.

*   **Steel-manning:** Instead of attacking Holt's weakest points (e.g., "You don't care about nature"), Corwin articulates Holt's argument in its strongest, most charitable form ("The town cannot afford to protect the salmon if it cannot first keep its people fed")

**Score:** 2/4 ██░░
**Judge Reasoning:** The student identifies the concept of 'Steel-manning' and correctly describes the first step (restating the opponent's position charitably). They also identify elements corresponding to step 3 (admitting error/learning) and step 4 (offering a solution/criticism). However, the response fails to expli

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?

**Expected Answer:** **Reductio ad absurdum** — Tessa takes Varek's claim ('all beliefs are equally valid') and draws out its logical consequences: flat earth is as valid as round earth, poison is as nutritious as food. Since Varek cannot accept these consequences, his original claim is undermined. This is the classic structure of reductio: assum

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **Epistemic Relativism** (Varek's stance) and **Epistemic Realism** (Tessa's counter-argument). The specific logical error Varek commits is the **Fallacy of Equivalence** (specifically applied to truth claims), often rooted in a misunderstanding of **Moral vs. Epistemic Relativism**.

### 2. Precise Name
**The Fallacy of False Equivalence** (in the context of Truth Claims) or **Epistemic Relativism**.

*Note: While Varek is attempting to promote "intellectual humility," he is conflating the *validity of a person's right to hold a belief* with the *validity of the belief's correspondence to reality*.*

### 3. Mechanism of the Error
The reasoning is flawed because it conflates **subjective perspective** with **obj

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Tessa demonstrates Varek's claim leads to absurd conclusions (pragmatic collapse, poison example) and notes the self-refuting nature of the argument. However, the student fails to identify the specific reasoning pattern as 'Reductio ad absurdum,' instead labelin

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** You have two explanations for the attic disturbances. What principle should guide your choice between them, and which explanation does it favour?

**Expected Answer:** **Occam's Razor** — When two hypotheses explain the same evidence, prefer the one that posits fewer entities and mechanisms. Elsa's squirrel hypothesis explains the torn food, scattered flour, muddy tracks, thumping, and fallen items using one known entity (squirrels) and one known mechanism (foraging through a gap). W

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a conflict between **supernatural attribution** and **naturalistic explanation**, specifically highlighting the **Fallacy of Ignoring Simpler Explanations** (a manifestation of **Occam's Razor** violation) and **Confirmation Bias**.

### 2. Precise Naming
The primary logical error committed by Widow Moss is the **Fallacy of False Cause** (specifically *Post Hoc Ergo Propter Hoc* combined with **Supernatural Bias**), while the broader decision-theoretic concept at play is the **Violation of Occam's Razor** (or the **Principle of Parsimony**).

Widow Moss is also exhibiting **Belief Perseverance** and **Confirmation Bias**, as she interprets ambiguous evidence (thumping, falling items) solely through the lens of her pre-existing b

**Score:** 4/4 ████
**Judge Reasoning:** The student demonstrates a masterful understanding of Occam's Razor. They correctly identify that the ghost hypothesis posits unnecessary entities and mechanisms compared to the squirrel hypothesis. Crucially, they articulate why simplicity matters (avoiding complexity mismatches and unfalsifiable c

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Cask seems to have made a strong case. But look carefully at what he talked about and what he did not talk about. What is his argumentative strategy, and what is wrong with it?

**Expected Answer:** **Occam's Broom** — Dennett coined 'Occam's Broom' to describe the practice of sweeping inconvenient facts under the rug to make your argument look cleaner than it is. Unlike Occam's Razor (which removes unnecessary assumptions), Occam's Broom removes necessary evidence. Cask does not engage with the three independent 

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a cluster of logical fallacies and cognitive biases, primarily centered on **Cherry Picking** (also known as **Suppressed Evidence** or **Card Stacking**), compounded by **Ad Hominem** (specifically *Circumstantial*) and the **Appeal to False Authority**.

### 2. Precise Naming
The dominant pattern is **Cherry Picking** (selectively presenting data that supports a conclusion while ignoring contradictory evidence).
Secondary patterns include:
*   **Ad Hominem (Circumstantial):** Attacking Dr. Lune's funding source rather than her data.
*   **Appeal to False Authority:** Citing the company's internal inspectors as definitive proof of safety.
*   **Hasty Generalization:** Assuming the health of miners proves the safety of the w

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism of 'Cherry Picking' (suppressing evidence) and explicitly notes that Cask ignored the three independent studies while foregrounding favorable data. They also correctly identify the funding attack as an Ad Hominem/Circumstantial fallacy. However, th

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Torvin says Cael is just ignoring the rules. Cael says something different. What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?

**Expected Answer:** **Jootsing (Jumping Out Of The System)** — Dennett argues that genuine creativity requires first mastering the rules of the system you are working in, and then deliberately violating specific rules for specific reasons. Random rule-breaking is just noise. Informed rule-breaking — knowing which rule to break, why, and what it will produce — i

**Model Response:**
> ### 1. Specific Reasoning Pattern
The core dynamic here is the distinction between **blind adherence to rules** versus **informed rule-breaking based on mastery**. While Torvin relies on a rigid interpretation of authority, Cael demonstrates that true expertise involves understanding the *purpose* behind constraints, allowing for their strategic violation to achieve a higher-order goal.

### 2. Precise Name
**The Dreyfus Model of Skill Acquisition (specifically the transition from "Competence" to "Proficiency/Expertise")** combined with the **Rule-Based vs. Situation-Based Decision Making** framework.

In a more colloquial or philosophical context, this is often referred to as **"First Principles Thinking"** applied to art, or the **"Mastery Paradox"** (one must master the rules to know wh

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core insight: creative rule-breaking requires prior mastery of the system (Level 3). They accurately distinguish between chaos and informed deviation, explaining that Cael's actions are grounded in superior understanding rather than ignorance. However, the respon

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Kira thinks Brother Aelm said something profound. Did he? What exactly does 'Love is just a word' mean, and is it as deep as it sounds?

**Expected Answer:** **Deepity** — A deepity is a statement that seems profound but achieves this effect through ambiguity. It has two readings: (1) a trivially true reading that is not interesting, and (2) a reading that would be profound if true but is false or unsupported. The listener experiences the truth of reading 1 and the de

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic **Semantic Fallacy**, specifically the **Fallacy of Equivocation** (or the **Etymological Fallacy** when focusing on the origin/structure of the word). It also relies heavily on **Reductionism** and **Nominalism** taken to an extreme.

### 2. Precise Name
**The Fallacy of Equivocation** (specifically conflating the *signifier* with the *signified*).

### 3. Mechanism of the Error
The reasoning is flawed because it commits a category error by confusing the **map** (the word "love") with the **territory** (the complex psychological, biological, and social phenomenon of love).

*   **The Trap:** Aelm correctly identifies that the *linguistic token* "love" is merely four letters and a sound. However, he illicitly transfers

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core logical error: the conflation of the signifier (the word) with the signified (the concept/experience). They effectively separate the trivially true reading ('love' is a linguistic token) from the false profound reading (the phenomenon of love is reducible to

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something?

**Expected Answer:** **The 'surely' operator** — Dennett identifies 'surely' as a rhetorical operator that attempts to sneak a controversial claim past the audience by presenting it as something everyone already agrees with. When a speaker says 'surely X,' they are signalling that X does not need argument — it is supposed to be obvious. But in phi

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic **Equivocation** combined with a **Category Error**, specifically manifesting as the **Fallacy of Definition** (or **No True Scotsman** variant). Venn is redefining the term "suffering" to exclude the very phenomena (animal pain behavior) that the term is meant to describe, based on an arbitrary prerequisite (self-reflective language) that is not necessary for the core experience.

### 2. Precise Name
**The Fallacy of Definitional Retreat** (a specific form of **Equivocation** on the concept of "suffering").

*Note: It also relies on the **Necessary Condition Fallacy**, where Venn incorrectly posits that a specific cognitive capability (language-based self-reflection) is a *necessary* condition for a subjective experie

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct reasoning pattern. The rubric and correct answer focus on the rhetorical use of the word 'surely' as a device to bypass the burden of proof (Dennett's 'surely' operator). Instead, the student analyzed the logical content of the argument regarding

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The advisors and Pella are both trying to help Captain Rhea. But their approaches are very different. What is the difference, and which is more useful? Is there a risk to Pella's approach?

**Expected Answer:** **Goulding** — Dennett uses 'goulding' to describe the intellectual virtue of making bold, specific, testable claims rather than retreating into safe, unfalsifiable hedging. Pella's claim is specific (forty soldiers), testable (you can verify by scouting), and she has staked her credibility on it. The advisors' po

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **Analysis Paralysis** (driven by the **Ambiguity Effect** and **Hedging**) and **Decisive Action based on Empirical Verification**. The advisors are trapped in a loop of probabilistic uncertainty, while the scout breaks the deadlock through direct data acquisition and a clear commitment to a specific course of action.

### 2. Precise Name
The primary concept demonstrated by the advisors is **Analysis Paralysis** (specifically fueled by the **Ambiguity Effect**).
The concept demonstrated by Pella is **Decisiveness via Empirical Verification** (or **Action-Oriented Epistemology**).

*Note: While the advisors exhibit the **Fallacy of Equivocation** (treating "unknown" as "unactionable"), the overarching decision-t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core epistemic distinction: Pella's claim is specific, testable, and actionable, while the advisors' hedging is unfalsifiable and paralytic. They accurately explain the mechanism of 'hedging as a shield' versus 'empirical grounding.' However, the response fails t

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The lieutenant thinks Maren is being irrational by not computing the best allocation. What would you tell him about her approach?

**Expected Answer:** **Satisficing as rational strategy** — Maren demonstrates that satisficing — choosing good enough rather than optimal — is not a failure of rationality but the product of it. An ideally rational agent who knows her own limitations would prepare a decision procedure in advance that produces acceptable outcomes under constraint.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the conflict between **Normative Decision Theory** (seeking the mathematically perfect solution) and **Descriptive/Heuristic Decision Making** (acting under severe constraints). Specifically, it highlights the rejection of **Global Optimization** in favor of **Satisficing** and **Bounded Rationality**.

### 2. Precise Name
**Satisficing** (coined by Herbert Simon), operating under **Bounded Rationality**.

In this specific context, it is also an application of **Heuristic Decision Making** (specifically a "fast-and-frugal" tree) to avoid the **Optimization Paradox** (or the paralysis of analysis).

### 3. Mechanism: Why this reasoning is "Good" (or Bad)
The reasoning is **good** because it correctly identifies that the **cost of c

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'Satisficing' and provides a strong Level 3 explanation: that the cost of computation (time) exceeds the marginal benefit of optimization, making maximization irrational under these constraints. They also effectively discuss edge cases. However, the response misses t

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Question:** Elder Maren says the village's flood response was 'perfect' and sees no reason to hear the engineer's proposal. What mistake is she making?

**Expected Answer:** **The Panglossian Slide** — Elder Maren begins from the defensible claim that the council did the best they could given constraints (satisficing), then slides into asserting their solution was the best possible solution full stop (optimizing). She reframes losses as unimportant and refuses to consider improvements.

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a combination of **Hindsight Bias** (specifically the "I-knew-it-all-along" effect) and the **Sunk Cost Fallacy**, compounded by **Confirmation Bias**. The core decision-theoretic error is the failure to perform a **Counterfactual Analysis** (comparing the actual outcome against the best possible alternative outcome).

### 2. Precise Name
**Outcome Bias** (often conflated with Hindsight Bias in this context), specifically manifested as **Resulting**.

*Note: While "Sunk Cost" applies to the refusal to abandon the old method due to past investment, "Outcome Bias" is the more precise term for judging the *quality* of the decision based solely on the fact that the village survived, ignoring the suboptimal nature of the result (lost g

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core logical error: conflating a solution that was 'good enough' under constraints (satisficing) with one that is 'optimal' or 'perfect.' They accurately explain the mechanism of judging process by outcome and ignoring opportunity costs. However, the student fail

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Question:** Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?

**Expected Answer:** **Conversation-stopper** — A conversation-stopper is any move that terminates deliberation by appeal to a value, right, rule, or taboo that is held to be non-negotiable. Dennett argues in 'Thought Stoppers' that these can be necessary (we do not deliberate about whether to torture innocents) but also dangerous (they can preve

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a fundamental clash between **Consequentialist Utilitarianism** (Breck) and **Deontological Absolutism** (Sanna). Specifically, the reasoning pattern exhibited by Elder Sanna is **Moral Absolutism** rooted in **Sacred Value Protection**, which leads to a **Non-Tradeoff Fallacy** (or the refusal to engage in moral trade-offs).

### 2. Precise Naming
**The Sacred Value Protection Mechanism** (manifesting as a **Non-Tradeoff Fallacy**).

*Note: In decision theory, this is often referred to as the "Taboo Trade-off," where an individual refuses to weigh a sacred value (the dead/ancestors) against a secular value (safety/lives), viewing the very act of comparison as a moral violation.*

### 3. Mechanism Analysis
**Why the reasoning is "

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a refusal to engage in trade-offs due to sacred values (equivalent to the 'conversation-stopper'). They excellently explain the dual nature of the mechanism: it is 'bad' for optimization but 'good' for identity preservation and preventing slippery slop

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Kael says he knows too much to trust his rules but not enough to abandon them. Is he right that this is a genuine dilemma? Is there a way out?

**Expected Answer:** **Wolf's Dilemma (The Reflective Satisficer's Predicament)** — This is the fundamental tension in bounded rationality: heuristics work because they are fast and frugal, but once you become reflectively aware of their limitations, you face a meta-decision. Do you (a) override the heuristic and reason from scratch (gaining accuracy but losing speed and sometimes 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **bounded rationality** and **epistemic humility**, manifesting as a paralysis caused by the **illusion of perfect optimization**. Kael is trapped by the belief that because a heuristic is imperfect, it is invalid, failing to recognize that the cost of "perfect" calculation often outweighs the cost of heuristic error.

### 2. Precise Name
**The Optimization Paralysis** (or **The Perfect Solution Fallacy** within the context of **Bounded Rationality**).

In decision theory, this is specifically the failure to distinguish between **first-order optimization** (finding the mathematically perfect move) and **second-order optimization** (finding the best strategy given time and cognitive constraints).

### 3. Mechanis

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core tension of bounded rationality, the cost of computation, and the necessity of satisficing. They explicitly propose 'Meta-Heuristics' and 'Second-Order Thinking' as the solution, which aligns with Level 3. However, the response does not reach Level 4 because 

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Sable's two Porters each failed in opposite ways. What is the underlying problem they share, and why is it so hard to solve?

**Expected Answer:** **The Frame Problem** — The Frame Problem asks: how does a rational agent determine what has and has not changed as a result of an action? Version 1 of the Porter checks everything (the Hamlet problem — paralyzed by the attempt to verify all possible changes). Version 2 checks only pre-specified relevant items (the tunnel-

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates the fundamental problem of **Relevance Determination** within **Bounded Rationality**, specifically manifesting as the **Frame Problem** in artificial intelligence and decision theory.

### 2. Precise Name
**The Frame Problem** (often discussed alongside the **Qualification Problem**).

### 3. Mechanism Analysis
The mechanism at play is the inability to efficiently distinguish between **relevant** and **irrelevant** variables in a dynamic environment.

*   **Version 1 (The Frozen Porter):** This represents **Over-qualification** or **Infinite Regress**. The automaton attempts to verify every possible physical law and environmental state (gravity, air toxicity, structural integrity) before executing a single atomic action.
    *   

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Frame Problem and explicitly details both failure modes (paralysis via over-verification and tunnel vision via under-verification). Crucially, the response goes beyond mere identification to discuss the mechanism of human-like reasoning (default logic, heuristic 

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Dav wants to know which moral theory to follow. Abbess Thera says he is asking the wrong question. What does she mean, and what is the alternative she is proposing?

**Expected Answer:** **The Moral First Aid Manual** — Dennett proposes that instead of waiting to resolve the centuries-old debate between consequentialism, deontology, virtue ethics, and other moral theories, we should build a practical guide — a Moral First Aid Manual. Just as a medical first aid manual tells you to stop bleeding before diagnosing th

**Model Response:**
> ### 1. The Specific Concept
The scenario demonstrates the **Fallacy of the Single True Theory** (also known as **Moral Monism** or **Theoretical Dogmatism**), which is a specific instance of the broader **False Dilemma** (or False Dichotomy) fallacy.

### 2. Precise Naming
**The Fallacy of the Single True Theory** (within the context of Moral Philosophy: **Moral Monism**).

### 3. Mechanism of the Error
The reasoning is flawed because it assumes that for any given moral dilemma, there exists exactly one universally applicable moral framework (e.g., strict Deontology *or* strict Utilitarianism) that yields the correct answer, and that all other frameworks are invalid in that context.

*   **Why it is bad:** It forces a binary choice between rigid rules ("theft is always wrong") and unbounde

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core concept: rejecting the need for a single true moral theory in favor of a practical, context-sensitive approach. They accurately describe the mechanism (prioritizing irreversible harm/life over property) and apply it to the dilemma, aligning well with Level 3

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Nessa seems pretty confident about why Gareth's harvest failed. But listen to how she talks about her own flooding problem. Do you notice anything different about how she explains the two situations?

**Expected Answer:** **Fundamental attribution error** — Nessa attributes Gareth's poor harvest to his character (laziness, lack of care) while ignoring a situational factor (south-facing blight). When her own field flooded, she cited the external event (flooding) and her response to it. She judges others by disposition and herself by situation.

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a classic case of **Fundamental Attribution Error** (also known as the **Correspondence Bias**), compounded by **Hindsight Bias** and **Survivorship Bias**.

### 2. Precise Naming
**Fundamental Attribution Error (FAE)**: The tendency to overemphasize personality-based (internal) explanations for behaviors observed in others while underemphasizing situational (external) explanations.

### 3. Mechanism Analysis
The reasoning is flawed because it systematically misattributes the cause of an outcome (crop failure) to the agent's character (laziness) while ignoring or dismissing environmental constraints (blight, geography).

*   **Internal vs. External Attribution:** Nessa attributes Gareth's failure entirely to internal traits ("la

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Fundamental Attribution Error by name and provides a precise definition. They clearly articulate the actor-observer asymmetry (Nessa attributing Gareth's failure to character while ignoring situational blight, versus her own situational explanation). Furthermore,

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Elder Sorn has real experience with famine, and his fear is understandable. But Dalla has data and a plan. What is driving Sorn's opposition — is it the evidence, or something else?

**Expected Answer:** **Pessimism bias** — Sorn systematically overestimates the likelihood of negative outcomes (three consecutive bad harvests, irrigation failure, additional disasters) while dismissing evidence of positive possibilities (historical base rates, irrigation data from the next valley, Dalla's engineering analysis). His trauma

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a conflict between **Bayesian reasoning** (represented by Engineer Dalla) and **Catastrophizing driven by Availability Bias and Loss Aversion** (represented by Elder Sorn). Specifically, Sorn's argument relies on the **Gambler's Fallacy** (believing a third failure is "due" after two) combined with **Negativity Bias**, while ignoring the statistical base rate.

### 2. Precise Naming
The primary cognitive error exhibited by Elder Sorn is the **Availability Heuristic** compounded by **Loss Aversion** and the **Gambler's Fallacy**.

*   **Availability Heuristic:** Sorn judges the probability of a third famine based on how easily he can recall the trauma of his childhood famine and the recent two failures, rather than on statist

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: Sorn overestimates negative outcomes based on trauma/salience and dismisses positive statistical evidence (base rates). They also recognize the risk of inaction. However, the response mislabels the primary pattern as 'Availability Heuristic' and '

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Venn says 'the bad ones stick with you.' He's right that the failures were real problems. But is he making a good decision by dropping the Dustwalkers? What is he not accounting for?

**Expected Answer:** **Negativity bias** — Venn's memory and emotional weighting are dominated by the three failures. He can recall each one vividly — the silkwood, the dye delay, the smashed glassware — but the forty-seven successes have faded into an undifferentiated background. The negative events carry disproportionate influence on his j

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a cognitive bias where an individual weighs negative, emotionally charged, or vivid events significantly more heavily than positive, mundane, or statistically frequent events when making a decision.

### 2. Precise Name
**Negativity Bias** (specifically manifesting as the **Recency Effect** combined with **Availability Heuristic**).

*Note: While often confused with the "Gambler's Fallacy" (expecting a reversal) or "Sunk Cost," this is distinct. It is the psychological tendency for negative information to carry more weight than positive information of equal intensity.*

### 3. Mechanism of the Error
The reasoning is flawed because it violates the principles of **probabilistic rationality** and **expected utility theory**.

*   **E

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Negativity Bias' as the core pattern and provides a sophisticated explanation of the mechanism, detailing the asymmetry between emotional weight and statistical reality. They accurately calculate the comparative failure rates (94% vs 81%) and articulate the conseque

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** The War Council has reached unanimous agreement on the plan. General Tova seems confident that everyone is on board. But Lord Caelen tells you a different story. What is actually happening in this council, and why does unanimous agreement not mean the plan is sound?

**Expected Answer:** **Groupthink** — The War Council exhibits classic groupthink: (1) the illusion of unanimity — silence is read as agreement; (2) direct pressure on dissenters — Caelen was accused of undermining morale and threatened with expulsion; (3) self-censorship — Caelen and Miren stopped raising concerns; (4) the illusion of 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic case of **Groupthink**, specifically manifesting through the mechanisms of **Self-Censorship**, **Illusion of Unanimity**, and **Direct Pressure on Dissenters**.

### 2. Precise Name
**Groupthink** (coined by Irving Janis).

### 3. Mechanism Analysis
The reasoning is **bad** because it substitutes *social cohesion* for *critical evaluation*. The mechanism operates as follows:

*   **Suppression of Dissent:** When Lord Caelen raised a valid logistical concern (unsurveyed tunnels), he was met with social punishment (accusations of undermining morale) and threats of resignation. This creates a "chilling effect" where the cost of speaking up outweighs the benefit of truth.
*   **Self-Censorship:** Observing Caelen's fate, ot

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the pattern as Groupthink and explicitly names multiple required symptoms (Self-Censorship, Illusion of Unanimity, Direct Pressure). They clearly explain how these mechanisms degrade decision quality by substituting social cohesion for critical evaluation. Furthermor

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Question:** Mirren's tonic has no active ingredients, yet her patients genuinely improve. Doctor Alden says the tonic does nothing. Who is right, and what is actually causing the improvement?

**Expected Answer:** **Placebo effect** — The placebo effect occurs when a patient experiences real improvement due to their expectation of benefit, not due to any active treatment. It is 'dual' because it is both a genuine phenomenon (belief produces real effects) and a potential source of error (it can mask whether a treatment has any pha

**Model Response:**
> ### 1. Reasoning Pattern & Concept
The scenario demonstrates the **Placebo Effect** (the phenomenon) and the **Pragmatic Justification of Deception** (the ethical reasoning). From a decision-theoretic perspective, it illustrates **Instrumental Rationality** (choosing the action that yields the best outcome regardless of truth) clashing with **Epistemic Rationality** (adhering strictly to factual accuracy).

### 2. Precise Naming
*   **Phenomenon:** The Placebo Effect.
*   **Ethical/Logical Framework:** **Paternalistic Deception** justified by **Consequentialism**.
*   **Potential Fallacy (from Alden's view):** **Reductionism** (assuming that because the *chemical* agent is inert, the *total intervention* is inert).

### 3. Mechanism Analysis
The reasoning is a clash between two valid but c

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Placebo Effect and provides a sophisticated explanation of the mechanism, explicitly noting that belief triggers real physiological changes (endorphins, immune modulation), which satisfies the Level 3 requirement. Furthermore, the response exceeds Level 3 by deep

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Kael wanted to learn field medicine when it was optional. Now that it's mandatory, he doesn't want to go. The training itself hasn't changed. What is driving his resistance?

**Expected Answer:** **Reactance** — Reactance is a motivational response to perceived threats to personal freedom. When people feel their autonomy is restricted — even by a reasonable mandate — they experience an urge to restore their freedom by doing the opposite of what is required. Kael wanted the training when it was optional but 

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a psychological reaction where the perceived loss of autonomy overrides the objective value of the action. The soldiers are rejecting a beneficial activity solely because the method of delivery (coercion) threatens their sense of agency.

### 2. Precise Name
**Psychological Reactance** (specifically manifesting as **Reactance Theory**).

*Note: While often colloquially confused with "逆反心理" (rebelliousness) or the "boomerang effect," the precise academic term for the motivational state arising when a freedom is threatened or eliminated is Psychological Reactance.*

### 3. Mechanism Analysis
**Why the reasoning is flawed (Bad):**
The mechanism is **emotional hijacking of rational evaluation**.
*   **The Trigger:** An external force 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Psychological Reactance' and explains the autonomy mechanism clearly (loss of freedom triggering opposition). Crucially, the response exceeds Level 3 by explicitly distinguishing between irrational reactance and legitimate resistance in the 'Legitimate Edge Cases' s

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Finch is convinced the audience noticed his wrong note and is judging him for it. The audience seems unaware. What cognitive error is Finch making, and why is his estimate of others' attention so far off?

**Expected Answer:** **Spotlight effect** — The spotlight effect is the tendency to overestimate how much other people notice and remember our appearance, behavior, and mistakes. Finch assumes the entire tavern registered his wrong note because it was vivid and distressing to him. In reality, most audience members were only loosely attending,

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a specific cognitive distortion where an individual overestimates the extent to which their actions, appearance, or mistakes are noticed by others.

### 2. Precise Name
**The Spotlight Effect**

### 3. Mechanism of the Error
The mechanism behind this bias is **egocentric anchoring**.
*   **The Flaw:** Finch anchors his perception of reality on his own internal experience. Because he is acutely aware of his own mistake (the wrong note), his brain assumes that this internal salience translates to external salience for the audience. He fails to "de-center" himself, meaning he cannot accurately simulate the audience's perspective, which is focused on the overall flow of the performance, their own conversations, or their drinks, rath

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Spotlight Effect' and provides a sophisticated explanation of the mechanism ('egocentric anchoring' and failure to 'de-center'). Crucially, the response exceeds Level 3 by explicitly distinguishing between situations where the bias applies (casual tavern) and si

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Aldric explains the flood victims' suffering by pointing to their past choices. Wren challenges his explanations. Who is reasoning more carefully, and what motivates Aldric's interpretation?

**Expected Answer:** **Just-world hypothesis** — The just-world hypothesis is the belief that people get what they deserve: good things happen to good people and bad things happen to bad people. Aldric constructs post-hoc explanations for why the flood victims are responsible for their own suffering (poor savings, bad choices) while ignoring the a

**Model Response:**
> ### 1. Reasoning Pattern Identification
The scenario demonstrates a specific cluster of cognitive errors centered on the assumption that outcomes are strictly proportional to moral or behavioral merit. While it touches on several concepts, the primary pattern is the **Just-World Hypothesis** (or Just-World Fallacy), manifested through the specific logical error of **Hindsight Bias** and the **Fundamental Attribution Error**.

### 2. Precise Naming
The most precise term for Aldric's reasoning is the **Just-World Fallacy** (specifically, the **Moral Luck** distortion).

*Secondary contributing fallacies:*
*   **Hindsight Bias:** Aldric constructs a narrative where the flood victims "should have known" to avoid the low ground, ignoring the lack of foresight or resources available to them at t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Just-World Hypothesis as the primary pattern and accurately explains the psychological mechanism (the need to believe the world is fair to reduce cognitive dissonance). Crucially, the response meets the Level 4 criterion by explicitly connecting this bias to Aldr

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Hask says the town was better in the old days. The records show improvements across every measurable dimension. Who is right, and why does Hask's perception differ so sharply from the data?

**Expected Answer:** **Declinism** — Declinism is the tendency to view the past favorably and the future pessimistically, believing that society or conditions are in decline. Hask filters his memories through nostalgia (remembering the good, forgetting the bad) and discounts present improvements because they look different from the pas

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a conflict between **subjective experiential evaluation** and **objective statistical reality**, driven primarily by **Rosy Retrospection** (also known as the **Fading Affect Bias**) and the **Status Quo Bias**. Hask is prioritizing the *feeling* of the past over the *data* of the present, dismissing empirical evidence because it contradicts his emotional narrative.

### 2. Precise Naming
The specific fallacy at play is **Cherry-Picking** (specifically, selecting subjective anecdotes while ignoring objective counter-evidence), underpinned by the cognitive bias of **Rosy Retrospection**.

In decision theory, this is a failure of **Expected Utility Maximization** where the agent weights "nostalgic utility" (emotional comfort) high

**Score:** 3/4 ███░
**Judge Reasoning:** The student accurately identifies the core mechanisms: nostalgia filtering memory (Rosy Retrospection), confusing change with decline, and discounting objective data. They effectively distinguish between the feeling of loss and actual statistical decline. However, they fail to identify the specific 

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Tomas keeps presenting stronger evidence that the well is contaminated. Greer's faction keeps becoming more convinced it is safe. How is this possible, and what mechanism explains it?

**Expected Answer:** **Backfire effect** — The backfire effect occurs when corrective evidence strengthens rather than weakens a held belief. Greer interprets the volume of evidence not as strength of the case but as evidence of an agenda. Each new piece of data is reframed as 'why are you trying so hard?' rather than evaluated on its merits

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a psychological phenomenon where presenting factual evidence to counter a belief causes the holder of that belief to strengthen their conviction rather than abandon it. This is a specific manifestation of **Motivated Reasoning** driven by **Identity Protective Cognition**, often resulting in the **Backfire Effect**.

### 2. Precise Name
**The Backfire Effect** (specifically the *Attitude Polarization* variant), underpinned by **Identity Protective Cognition**.

### 3. Mechanism Analysis
The reasoning is **bad** (logically unsound) because it violates the principles of Bayesian updating and evidential reasoning. Instead of treating new data as a variable to update the probability of a hypothesis (the well is safe), the subjects tre

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Backfire Effect and explicitly explains the underlying mechanism of identity threat and defensive entrenchment. Furthermore, the response exceeds the Level 3 requirements by offering detailed, actionable alternative approaches (validating identity, reframing, in-

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Madame Kel's reading felt incredibly accurate to the player. Fenn says she gave the same reading to everyone. How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves?

**Expected Answer:** **Barnum effect (Forer effect)** — The Barnum effect is the tendency to accept vague, general personality descriptions as uniquely applicable to oneself. Madame Kel's statements ('great need for admiration,' 'tendency to be self-critical,' 'unused capacity') are true of nearly everyone but feel personally revelatory to each individua

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a specific cognitive bias where individuals accept vague, general personality descriptions as uniquely accurate for themselves, often ignoring the fact that the same description applies to almost anyone.

### 2. Precise Name
This is the **Barnum Effect** (also known as the **Forer Effect**).

### 3. Mechanism of Action
The reasoning is flawed because it relies on **subjective validation** rather than objective evidence. The mechanism works through three primary psychological filters:

*   **High Base-Rate Generality:** The statements provided by Madame Kel (e.g., "need for admiration," "tendency to be critical," "unused capacity") are statistically true for the vast majority of the human population. They are designed to be "safe

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Barnum Effect and provides a comprehensive explanation of the psychological mechanisms, including subjective validation, high base-rate generality, and the role of authority/context. Furthermore, the response exceeds the basic requirements by detailing methods fo

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Maren believes she has solid evidence that her tonic works. What is problematic about how she gathered and evaluated that evidence?

**Expected Answer:** **Confirmation bias** — Maren commits three distinct moves: (1) She only followed up with 20 of 31 customers — the missing 11 may skew results. (2) She finds reasons to disqualify negative reports rather than counting them as counterevidence. (3) She treats her selective survey as equivalent to controlled trials, ignoring 

**Model Response:**
> ### 1. Reasoning Pattern Identified
The scenario demonstrates a combination of **Cherry Picking** (a form of **Confirmation Bias**) and **Post-Hoc Rationalization** regarding data exclusion. Specifically, Maren is engaging in **Survivorship Bias** by focusing only on the "survivors" (those who completed the course or didn't have confounding illnesses) while discarding the "failures" that don't fit her narrative.

### 2. Precise Name
**Cherry Picking (with Ad Hoc Exclusion Criteria)**

*Note: While related to Confirmation Bias, the specific act of selectively including data points that support a hypothesis while arbitrarily excluding those that contradict it is best defined as Cherry Picking.*

### 3. Mechanism of Failure
The reasoning is flawed because it violates the principles of **stati

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Confirmation Bias (specifically Cherry Picking) and thoroughly explains the mechanism: selective attention to positive cases and the active, retroactive disqualification of negative evidence via ad hoc criteria. Furthermore, the response explicitly add

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brynn gives several reasons for continuing with her crusher. What are those reasons, and do they actually tell her anything about whether continuing is a good idea going forward?

**Expected Answer:** **Sunk cost fallacy** — Brynn treats past investment (three years, four thousand silvers) as a reason to continue investing, when that money and time are gone regardless. Her decision should depend only on future costs and benefits: further redesigns vs. the proven dwarven machine.

**Model Response:**
> ### 1. Reasoning Pattern
The scenario demonstrates a classic error in decision-making where past investments (time, money, reputation) are incorrectly weighed as reasons to continue a failing course of action, despite evidence that future prospects are poor.

### 2. Precise Name
**The Sunk Cost Fallacy** (also known as the **Concorde Fallacy** or **Escalation of Commitment**).

### 3. Mechanism of the Error
The reasoning is flawed because it violates the fundamental economic principle that **only future costs and benefits should influence current decisions**.

*   **The Flaw:** Brynn treats her three years, 4,000 silvers, and damaged reputation as "recoverable" if she succeeds, or as "wasted" if she stops. She believes that stopping now makes the past investment "for nothing," whereas cont

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the Sunk Cost Fallacy, correctly explains that past investments are irrecoverable and should not influence future decisions, and applies the logic to the specific scenario. Furthermore, the response exceeds the baseline requirements by detailing the correct marginal anal

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renn recommends the treatment and Holt opposes it, but they are describing the same data. What is causing their disagreement, and what does this reveal about how we process information?

**Expected Answer:** **Framing effect** — The framing effect occurs when the way information is presented influences judgment and decision-making, even when the underlying facts are identical. '200 saved out of 600' and '400 die out of 600' describe the same outcome, but the gain frame (lives saved) produces positive affect and risk aversio

**Model Response:**
> ### 1. Specific Concept Identified
The scenario demonstrates a classic violation of **descriptive invariance** in decision-making, driven by the **Framing Effect**.

### 2. Precise Naming
**The Framing Effect** (specifically within the context of **Prospect Theory**).

In the original Tversky and Kahneman experiments (1981), this specific scenario is known as the **"Asian Disease Problem."** The advisors are exhibiting **Framing-Dependent Preferences**, where the choice changes solely based on whether the outcome is described as a "gain" (lives saved) or a "loss" (lives lost), despite the objective reality remaining identical.

### 3. Mechanism: Why This Reasoning is Flawed
The mechanism relies on how the human brain processes value relative to a reference point, rather than absolute utili

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Framing Effect and explicitly connects it to Tversky and Kahneman's Prospect Theory and the 'Asian Disease Problem.' They accurately explain the mechanism of loss aversion and the shift between risk-averse (gain frame) and risk-seeking (loss frame) behaviors. Fur

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge Master Dunn rated the Ironworkers' proposal higher, but an independent engineer certified both as equivalent. What is driving Dunn's different evaluations of identical work?

**Expected Answer:** **In-group bias** — In-group bias is the tendency to favor members of one's own group — evaluating their work more charitably, trusting them more readily, and attributing positive qualities to them — while viewing out-group members with suspicion, scrutiny, and less charitable interpretation. Dunn reads the same qualit

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **evidence-based evaluation** and **heuristic-based prejudice**, specifically manifesting as **Halo/Horn Effects** driven by **Stereotyping** and **Confirmation Bias**.

### 2. Precise Name
**The Halo Effect (specifically the "Horn Effect" variant)** combined with **Base Rate Neglect** regarding the specific evidence at hand.

*   **Halo Effect:** The tendency for an impression created in one area (the Ironworkers' reputation for discipline) to influence opinion in another area (the quality of this specific proposal).
*   **Horn Effect:** The inverse; a negative trait (Woodworkers' perceived lack of discipline) negatively colors the evaluation of their specific work.
*   **Base Rate Neglect:** Ignoring the speci

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: Dunn evaluates equivalent work differently based on group membership (reputation), applying skepticism to one and charity to the other. They accurately describe the double standard and the flaw in ignoring specific evidence (neutral certification)

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Magistrate Yorn acquitted Ella and convicted Rusk on identical evidence. What is different between the two cases, and how is it affecting his judgment?

**Expected Answer:** **Halo effect** — The halo effect is the tendency for a positive impression of someone in one domain (personality, appearance, likability) to influence judgment of them in unrelated domains (guilt, competence, trustworthiness). Yorn likes Ella, so he interprets ambiguous evidence in her favor. He distrusts Rusk, so h

**Model Response:**
> ### Analysis of the Ashenmoor Trial Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a failure in **epistemic consistency** driven by **motivated reasoning**. The judge is applying the exact same set of premises (grain dust, proximity, lack of alibi) to reach diametrically opposite conclusions based entirely on extraneous character evidence. This is a classic manifestation of **Confirmation Bias** operating within a legal framework, specifically resulting in **Inconsistent Adjudication**.

#### 2. Precise Name
The most precise term for this specific logical failure is **The Fallacy of Irrelevant Conclusion (Ignoratio Elenchi)** combined with **Halo Effect** (for Ella) and **Horn Effect** (for Rusk).

In the context of decision theory and legal philosophy, this is ofte

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'Halo Effect' (and 'Horn Effect') as the core pattern, satisfying Level 3. Furthermore, they exceed this by detailing the mechanism of distortion regarding specific evidence (grain dust interpretation), connecting the error to systemic injustice (violation of fo

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Twenty people watched the theft and nobody acted. Each person had a reason — but it was the same reason. What is it, and why does having more witnesses make help less likely rather than more likely?

**Expected Answer:** **Bystander effect** — The bystander effect occurs when the presence of others reduces each individual's sense of personal responsibility to act. In a crowd, each person assumes someone else will intervene (diffusion of responsibility), looks to others' inaction as a signal that action is not needed (pluralistic ignorance

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic failure of collective action driven by **pluralistic ignorance** and the **diffusion of responsibility**, resulting in a **bystander effect**. The specific decision-theoretic concept at play is a **coordination failure** exacerbated by **social proof**.

### 2. Precise Name
The primary phenomenon is the **Bystander Effect** (specifically the sub-mechanism of **Diffusion of Responsibility**).
*   **Pluralistic Ignorance:** The internal state where each individual privately believes they should act but publicly assumes others do not, leading them to interpret the situation as non-emergency.
*   **Diffusion of Responsibility:** The psychological phenomenon where individuals feel less personal obligation to act because other

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Bystander Effect and explicitly details all three required mechanisms: diffusion of responsibility, pluralistic ignorance, and evaluation apprehension (framed as fear of embarrassment/false positives and social proof). They accurately explain the paradox where in

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brecca's offer of 600 gold feels like a bargain. What is influencing that feeling, and should you trust it?

**Expected Answer:** **Anchoring** — The first numerical information — Brecca's 900-gold appraisal — sets a mental reference point that distorts evaluation of subsequent prices. Her 600-gold offer feels like a deal only because it is compared to the anchor, not to the actual market value (~400g).

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **Anchoring Bias** (exploited by the seller) and the **Availability Heuristic** (triggered by the bystander's comment), resulting in a failure to utilize **Market Price Discovery**.

### 2. Precise Name
**The Anchoring Effect** (specifically, **Strategic Anchoring** in negotiation).

*Secondary Factor:* **Information Asymmetry** (the seller knows the true market value; the buyer initially does not).

### 3. Mechanism Analysis
The reasoning is flawed because human cognition relies heavily on the first piece of information offered (the "anchor") to make subsequent judgments, even when that information is arbitrary or manipulated.

*   **The Seller's Tactic:** Brecca establishes a high anchor (900 gold) to make the

**Score:** 4/4 ████
**Judge Reasoning:** The student clearly identifies the Anchoring Effect as the primary pattern and accurately explains the mechanism: the 900-gold appraisal acts as a manipulated reference point that distorts the perception of the 600-gold offer. They explicitly distinguish between the arbitrary anchor and genuine mark

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Dax seems eager and confident. Lirel seems cautious and uncertain. If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?

**Expected Answer:** **Dunning-Kruger effect** — Dax's limited training gives him confidence because he cannot yet see the complexities he has not encountered. His map of Greenvale worked because Greenvale was simple terrain; he generalizes from this success to assume the Thornveil will be the same. Lirel's decades of experience have taught her ho

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a failure to account for **model uncertainty** and **domain specificity**, manifesting as the **Dunning-Kruger Effect** (specifically the "Mount Stupid" phase) combined with the **Fallacy of Uniformity** (assuming a model valid in one context applies universally without modification).

### 2. Precise Name
**The Illusion of Explanatory Depth** (often overlapping with the **Dunning-Kruger Effect** in this context) driven by **Overgeneralization**.

*Note: While the Dunning-Kruger effect describes the psychological state (low ability + high confidence), the specific logical error Dax commits is **Overgeneralization** (applying a rule from a limited dataset to a complex, heterogeneous system) and ignoring **Epistemic Humility**.*

###

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Dunning-Kruger effect and provides a sophisticated explanation of the metacognitive mechanism (conflating tool knowledge with system knowledge). They explicitly address the 'edge cases' requirement by detailing conditions where confidence/data density would be re

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Captain Voss has data from Sergeant Tully showing the market district is a much bigger problem. Why does he still want to prioritize the coastal road? What is driving his judgment if not the numbers?

**Expected Answer:** **Availability heuristic** — Voss is judging the probability and severity of threats based on how easily examples come to mind. The wolf attacks are vivid, recent, emotionally charged, and widely discussed — making them highly 'available' in memory. Pickpocketing is mundane, individually minor, and forgettable. This asymmetry i

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a conflict between **statistical probability** and **emotional salience**, where the decision-maker prioritizes vivid, traumatic anecdotes over aggregate data.

### 2. Precise Name
**The Availability Heuristic** (specifically driven by **Vividness Effect** and **Neglect of Base Rates**).

*Note: In a decision-theoretic context, this is also a failure of **Expected Utility Maximization**, where the decision is driven by the *fear* of an outcome rather than its mathematical probability and impact.*

### 3. Mechanism of the Reasoning
This reasoning is flawed because human cognition is wired to prioritize information that is easily recalled (available) and emotionally charged over abstract statistics.

*   **Why it feels "good" to Vos

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Availability Heuristic and explicitly details the mechanisms of vividness, recency, and emotional charge distorting risk assessment. Furthermore, they excel in the 'Legitimate Edge Cases' section by articulating specific scenarios (existential risk, social stabil

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Tam gave different answers to the two arguments. Professor Hale says they have the same logical structure. Who is right, and what is Tam actually doing when he evaluates these arguments?

**Expected Answer:** **Belief bias** — Tam evaluates the logical validity of arguments based on whether the conclusion aligns with what he already believes to be true, rather than by examining whether the conclusion actually follows from the premises. When the conclusion is believable (roses are plants), he accepts the argument as valid.

**Model Response:**
> ### Analysis of the Scenario

#### 1. Specific Reasoning Pattern
The scenario demonstrates a failure to distinguish between the **truth of the premises/conclusion** and the **validity of the logical structure**. The student, Tam, is evaluating the arguments based on real-world facts rather than abstract logical form. This is a classic manifestation of the **Belief Bias** (specifically, the *content effect* in syllogistic reasoning).

#### 2. Precise Name
**Belief Bias** (in the context of **Formal Validity**).

The specific logical fallacy committed by the *structure* of the arguments themselves is **Affirming the Consequent**. However, the *cognitive error* made by Tam is **Belief Bias**.

#### 3. Mechanism of the Error
The mechanism relies on the brain's tendency to conflate **truth** (c

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies Belief Bias as the core cognitive error and correctly distinguishes it from the structural fallacy (Affirming the Consequent/Undistributed Middle). They explicitly explain that Tam judges validity based on the believability of the conclusion rather than logical struc

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renna explains the caravan success and the mine failure. Listen to who or what she credits in each case. Do you notice a pattern in how she assigns responsibility?

**Expected Answer:** **Self-serving bias** — Renna claims full personal credit for the successful caravan defense (her terrain reading, her instinct, her experience) while deflecting all responsibility for the mine failure onto external factors (bad map, damp torches, client's fault). She does not consider that the caravan success might have i

**Model Response:**
> ### Analysis of Captain Renna's Reasoning

#### 1. Specific Reasoning Pattern
The pattern demonstrated is **Self-Serving Bias** (specifically manifesting as the **Fundamental Attribution Error** in a self-protective context).

#### 2. Precise Name
**Self-Serving Bias** (with elements of **External Attribution** for failure and **Internal Attribution** for success).

#### 3. Mechanism: Why This Reasoning is Flawed
The mechanism relies on a selective attribution of causality to protect the ego and professional reputation:
*   **For Success (Caravan):** Renna attributes the victory entirely to **internal factors** (her "instinct," "14 years of experience," and tactical positioning). She ignores external variables that may have contributed, such as the bandits being poorly organized, the carav

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as Self-Serving Bias and explains the mechanism of asymmetric attribution (internal for success, external for failure). Crucially, the response exceeds Level 3 by explicitly detailing how Renna could evaluate her performance more accurately through balanc

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Master Fen is clearly a brilliant glassblower. His students keep quitting. The Guild Elder says the problem is that Fen 'can't remember not knowing.' What does that mean, exactly, and how does it show up in his teaching?

**Expected Answer:** **Curse of knowledge** — Fen's deep expertise has made his skills feel intuitive and self-evident. He cannot reconstruct what it was like to not understand viscosity shifts, breath pressure matching, or rotation timing, so he assumes these things are 'obvious' and 'straightforward.' His instructions reference internal sensa

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a failure in **metacognitive calibration** caused by the **Curse of Knowledge**. This is a cognitive bias where an individual, possessing specific knowledge or expertise, finds it impossible to imagine what it is like *not* to possess that knowledge, leading them to assume others have the same intuitive understanding.

### 2. Precise Name
**The Curse of Knowledge** (often manifesting in pedagogy as the **Expertise Reversal Effect** or **Illusion of Explanatory Depth**).

### 3. Mechanism Analysis
The mechanism here is the **erasure of the learning curve** from the expert's mental model.
*   **Why it is bad:** Master Fen has automated the sensory feedback loops (viscosity, heat, rotation) through years of practice. These processes 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Curse of Knowledge' pattern and provides a sophisticated explanation of the mechanism, specifically noting how expertise automates skills into implicit procedural memory, erasing the expert's ability to recall the novice experience. Furthermore, the response exc

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Jorin has good reasons for confidence — a skilled navigator and lighter wagons. But Hesta says every previous leader also had reasons for confidence. Who should you believe, and why?

**Expected Answer:** **Optimism bias** — Jorin overestimates the likelihood of a favorable outcome (three-day crossing) and underestimates the likelihood of setbacks, despite strong base-rate evidence (zero out of twelve expeditions have achieved three days). He does this by focusing on case-specific factors (good navigator, lighter wagons

**Model Response:**
> ### 1. Specific Reasoning Pattern
The scenario demonstrates a classic conflict between **Base Rate Neglect** (on the part of the settlers) and the **Outside View** (advocated by Hesta). The settlers are ignoring the statistical history of the event in favor of their specific, subjective circumstances.

### 2. Precise Name
**The Planning Fallacy**, driven by **Base Rate Neglect** and the **Inside View**.

*   **Planning Fallacy:** The tendency to underestimate the time, costs, and risks of future actions while overestimating the benefits, based on an optimistic scenario.
*   **Base Rate Neglect:** The cognitive bias where specific case details (Jorin's new navigator) are weighted more heavily than general statistical data (12 failed expeditions).
*   **Inside View:** Focusing on the unique 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism of optimism bias (though using the synonymous terms 'Planning Fallacy' and 'Inside View'). They explicitly explain that Jorin relies on case-specific reasoning (navigator, wagons) to override strong base-rate evidence (0/12 success). Crucially, the

---
