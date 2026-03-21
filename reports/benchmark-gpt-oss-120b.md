# Benchmark Report: gpt-oss-120b Reasoning Capacity Assessment

**Date:** 2026-03-20
**Subject Model:** openai/gpt-oss-120b (MindRouter, University of Idaho campus HPC)
**Judge Model:** qwen/qwen3.5-400b (MindRouter)
**Corpus:** 167 hand-crafted anchor examples across 5 content tracks

## 1. Executive Summary

We assessed gpt-oss-120b's capacity for critical thinking, logic, decision theory,
game theory, and cognitive bias recognition using 167 hand-crafted benchmark items.
Each item was evaluated in three modes: open-ended identification, multiple-choice
classification, and full explanation. Results are compared to the gpt-oss-20b baseline.

**Key findings:**

- **Identify mode: 3.27/4.00** (vs 20b: 2.62) — substantial improvement
  in pattern recognition, especially on decision theory and game theory.
- **Explain mode: 3.04/4.00** (vs 20b: 2.47) — the largest gain; the 120b model
  provides meaningfully better mechanistic explanations across all tracks.
- **Classify mode: 0.29/4.00** (vs 20b: 0.10) — still very low, confirming that
  constrained output format remains a challenge even at 120b scale.
- **Dennett tools remain the hardest category** but show improvement over 20b.
- **The bad_thinking > good_tool gap persists** but narrows at 120b scale.

## 2. Methodology

Methodology is identical to the gpt-oss-20b benchmark (see that report for full details).
In brief:

- **167 anchor examples** across 5 tracks (logic, decision theory, game theory, microeconomics,
  Dennett tools) and cognitive biases
- **Three modes:** identify (open-ended), classify (5-option MCQ), explain (full analysis)
- **Judge:** qwen/qwen3.5-400b scores identify/explain against 0–4 rubrics; classify is auto-scored
- **Subject:** openai/gpt-oss-120b on MindRouter, temperature=0.3, thinking mode disabled

## 3. Overall Results

| Mode | 120b Mean | 20b Mean | Δ | 120b Distribution (0/1/2/3/4) |
|------|-----------|----------|---|-------------------------------|
| identify | 3.27 | 2.62 | +0.65 | 1 / 1 / 16 / 83 / 66 |
| classify | 0.29 | 0.10 | +0.19 | 155 / 0 / 0 / 0 / 12 |
| explain | 3.04 | 2.47 | +0.57 | 8 / 11 / 20 / 56 / 72 |

## 4. Results by Track

| Track | 120b Identify | 20b Identify | 120b Explain | 20b Explain |
|-------|---------------|--------------|--------------|-------------|
| cognitive_biases | 3.50 | 2.62 | 3.54 | 3.12 |
| decision_theory | 3.00 | 2.81 | 3.03 | 2.58 |
| dennett_tools | 2.86 | 1.93 | 2.00 | 1.29 |
| game_theory | 2.83 | 2.28 | 2.67 | 2.00 |
| logic_critical_thinking | 3.51 | 2.72 | 3.22 | 2.65 |
| microeconomics | 3.33 | 2.80 | 2.87 | 2.07 |

**Discussion:** The 120b model improves across all tracks, with the largest gains in
cognitive biases (explain: +0.42) and logic/critical thinking (explain: +0.57). Dennett
tools remain the hardest category (explain: 2.00) but improve from the 20b baseline (1.29).

## 5. Results by Difficulty Tier

| Tier | 120b Identify | 20b Identify | 120b Explain | 20b Explain |
|------|---------------|--------------|--------------|-------------|
| drill | 3.46 | 2.73 | 3.23 | 2.73 |
| what_if | 2.90 | 2.39 | 2.61 | 1.98 |
| puzzle | 2.83 | 2.33 | 2.83 | 1.50 |

## 6. Results by Pattern Type

| Pattern Type | 120b Identify | 20b Identify | 120b Explain | 20b Explain |
|--------------|---------------|--------------|--------------|-------------|
| good_tool | 3.02 | 2.49 | 2.35 | 1.78 |
| bad_thinking | 3.62 | 2.73 | 3.61 | 3.12 |
| dual | 2.93 | 2.61 | 3.11 | 2.32 |

The bad_thinking > good_tool gap persists at 120b but narrows in explain mode
(gap: 1.26 at 120b vs 1.34 at 20b). Scale alone does not close this gap —
domain-specific training is needed.

## 7. Notable Findings

### 7.1 Scale Effects (20b → 120b)

| Metric | 20b | 120b | Improvement |
|--------|-----|------|-------------|
| Identify mean | 2.62 | 3.27 | +0.65 |
| Explain mean | 2.47 | 3.04 | +0.57 |
| Classify mean | 0.10 | 0.29 | +0.19 |
| Score=4 (identify) | 21 | 66 | |
| Score=0 (identify) | 2 | 1 | |

The 120b model shows meaningful gains in identify and explain modes, with the explain
mode showing the largest improvement. However, classify mode remains near-zero,
suggesting this is a qualitative instruction-following limitation rather than a
continuous scaling phenomenon.

### 7.2 Persistent Weaknesses

Despite 6x more parameters, the 120b model still struggles with:

- **D1.5: Jootsing** (explain=0, tier=what_if)
- **D1.8: Goulding** (explain=0, tier=what_if)
- **A1.2: Premises and conclusions** (explain=0, tier=drill)
- **A1.3: Standard form** (explain=0, tier=drill)
- **A2.7: Logical equivalence** (explain=0, tier=drill)
- **C5.1: Supply, demand, equilibrium** (explain=0, tier=drill)
- **C5.2: Price controls and deadweight loss** (explain=0, tier=drill)
- **B10.4: Reputation** (explain=0, tier=what_if)
- **B1.1: Decision matrices** (explain=1, tier=drill)
- **B3.1: MEU formula and calculation** (explain=1, tier=drill)

### 7.3 Biggest Improvements over 20b

| Code | Label | 20b | 120b | Δ |
|------|-------|-----|------|---|
| D1.3 | Occam's Razor | 0 | 3 | +3 |
| A2.3 | Truth tables | 0 | 3 | +3 |
| C1.2 | Comparative advantage | 0 | 3 | +3 |
| C6.1 | Externalities | 1 | 4 | +3 |
| B8.4 | Centipede Game | 0 | 3 | +3 |
| D1.1 | Rapoport's Rules | 0 | 2 | +2 |
| D2.5 | The Frame Problem | 1 | 3 | +2 |
| A9.3 | The fallacy fallacy | 2 | 4 | +2 |
| A1.5 | Missing premises | 2 | 4 | +2 |
| A2.2 | Propositional logic basics | 2 | 4 | +2 |
| A3.2 | IBE | 0 | 2 | +2 |
| A3.4 | Causal reasoning | 1 | 3 | +2 |
| A10.6 | Exaggeration / minimization | 2 | 4 | +2 |
| A10.7 | Doubt casting | 2 | 4 | +2 |
| C7.1 | Broken window fallacy | 1 | 3 | +2 |

## 8. Implications for Training

### Base Model Selection

The 120b model is a stronger starting point for LoRA fine-tuning:
- Explain mode: 3.04 vs 2.47 (20b) — higher ceiling to build on
- Already scores 3+ on most common fallacies and biases
- The remaining weaknesses (Dennett tools, good_tool patterns, argument structure)
  are precisely the areas where our training corpus is strongest

### Training Priority (updated from 20b analysis)

1. **Dennett's thinking tools** (120b explain: 2.00) — still the largest gap
2. **Good_tool pattern explanation** (120b explain: 2.35) — still weaker than bad_thinking
3. **Argument structure basics** (A1.x scores at 0-1) — foundational skills
4. **Classification output format** — both models fail; needs format-specific training
5. **Puzzle-tier reasoning** — higher-order philosophical engagement

### Expected Post-Training Targets

| Mode | 20b Baseline | 120b Baseline | Post-LoRA Target |
|------|-------------|---------------|-----------------|
| Identify | 2.62 | 3.27 | 3.60+ |
| Explain | 2.47 | 3.04 | 3.50+ |
| Classify | 0.10 | 0.29 | 3.20+ |

## Appendix A: Full Results — Identify Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The bartender wants to know: which of these speakers is actually giving an argument? How can you tell?

**Expected Answer:** **Identifying arguments via indicator words** — An argument is a set of premises that attempt to provide a reason that a conclusion is true. The sailor's statement is a chronological narrative with no premises or conclusion — it describes a sequence of events. The dockworker's statement is an argument: 'since' is a premise indicator linking two p *Recognizing arguments requires checking for premise and conclusion indicators and verifying that statements are being offered as reasons for another statement. The dockworker uses 'since' to connect e*

**Model Response:**
> **Short answer:**  
The **dockworker** is the only one who is actually giving an argument.  

---

## How to tell – step‑by‑step

| Speaker | What they say | Does it contain a **claim** + **premises** that support that claim? |
|---------|---------------|--------------------------------------------------------------------|
| **Sailor** | “First I loaded the cargo, and then I secured the rigging. After that I checked the manifest.” | No. He is merely **describing a sequence of actions**. There is no conclusion that he is trying to get anyone to accept, nor any premises offered to support a conclusion. It is a narrative, not an argument. |
| **Dockworker** | “The ship is not seaworthy, **since** the hull planks are rotting and the bilge pump is broken.” | **Yes.** The statement *“The ship is

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the dockworker's statement as the argument and the sailor's as a narrative. They explicitly name 'since' as a premise indicator, identify the specific premises and conclusion, and explain the structural difference between the two statements. However, the response doe

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Theodora just gave testimony with several claims. Which is her main conclusion? Which statements are premises? Is there a statement that serves as both a conclusion and a premise?

**Expected Answer:** **Identifying premises, conclusions, and intermediate conclusions** — Theodora's argument has a layered structure. 'The fact that... is shown by the fact that...' reverses the usual order — the conclusion comes first, then the premise. The intermediate conclusion is that the royal household is contributing to the obesity problem (supported by premises about larger por *Identifying premises and conclusions requires attending to indicator phrases. 'The fact that X is shown by the fact that Y' means Y is the premise and X is the conclusion — the reverse of reading orde*

**Model Response:**
> **1.  Re‑constructing the argument**

| Sentence (as spoken) | How it functions in the argument |
|----------------------|----------------------------------|
| **(A)** “Obesity rates have risen significantly over the past four decades.” | **Premise** – empirical data. |
| **(B)** “The fact that obesity has become a problem in the kingdom is shown by the fact that obesity rates have risen …” | **Conclusion of the first sub‑argument** (from A we infer that obesity is a problem).  It is also **used as a premise** for the next step, because the later claim refers to “this problem.” |
| **(C)** “The royal kitchens have been serving larger portions.” | **Premise** – factual claim about the royal kitchen. |
| **(D)** “Larger portions lead to overeating

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the main conclusion, premises, and the intermediate conclusion, and accurately explains the dependency structure where the intermediate conclusion serves as a premise for the final claim. However, the response does not explicitly note that the phrase 'is shown by' re

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe hands you Captain Voss's statement. Rewrite it in standard form: numbered premises with the conclusion last. Does the argument have any sub-arguments?

**Expected Answer:** **Standard form reconstruction** — Standard form lists premises as numbered statements with the conclusion last, marked with 'Therefore.' Voss's argument has two sub-arguments: one eliminating the sewer escape (premises about the locked grate and no scent trail), and one concluding the cart escape (premises about it being the only al *Standard form makes the logical structure visible. It separates premises from conclusions, reveals sub-arguments, and shows which premises support which conclusions. Voss's conversational version buri*

**Model Response:**
> **Standard‑form reconstruction**

| # | Premise (or sub‑conclusion) |
|---|----------------------------|
| 1 | The grate that covers the sewage‑pipe exit was still locked. |
| 2 | If the grate is locked, a person cannot get out through the sewage pipes. |
| 3 | Therefore **(C₁)** the prisoner could not have escaped through the sewage pipes. |
| 4 | The guard dogs found no scent trail leading from the cell to the drain. |
| 5 | If a prisoner had moved from the cell to the drain, the dogs would have picked up a scent trail. |
| 6 | Therefore **(C₂)** the prisoner did not travel from the cell to the drain. |
| 7 | The only possible ways out of the cell are (a) the sewage‑pipe route and (b) the back of the delivery cart. |
| 8 | (From C₁ and C₂) The sewage‑pipe route is impossible, so the only

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly reconstructed the argument in standard form with numbered premises and a clear conclusion. Crucially, they identified the sub-argument structure (eliminating the sewer route via two distinct lines of evidence) and explicitly noted the dependencies between premises and sub-concl

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Aldric has asked you to reconstruct Rosmund's argument in its strongest form. What is she really trying to argue, underneath the hyperbole? And why is the heckler's response unfair?

**Expected Answer:** **Principle of charity in argument reconstruction** — The principle of charity states that when reconstructing an argument, you should try to make it as strong as possible. Rosmund's literal words contain overstatements ('cheap garbage,' 'every tanner will go broke'), but her core argument has a defensible structure: if cheaper foreign imports undercut *The heckler attacked Rosmund's weakest phrasing ('cheap garbage') rather than her strongest argument. Charitable reconstruction reveals that her core concern — price competition threatening local live*

**Model Response:**
> **1. What Rosmund is really trying to say – the “strong‑form” version of her argument**

| **Plain‑language claim** | **Re‑phrased as a logical premise** |
|--------------------------|--------------------------------------|
| **P1.** The leather that can be imported from other lands is, on average, cheaper and of lower quality than the leather produced here. | *If a product is cheaper and of lower quality, buyers who care only about price will prefer it, and buyers who care about quality will still be able to obtain a comparable product at a lower price.* |
| **P2.** Buyers in Millhaven (both ordinary citizens and merchants) will shift their purchases toward the cheaper imported leather. | *When a cheaper substitute is available, demand for the more expensive domestic product falls.* |
| *

**Score:** 3/4 ███░
**Judge Reasoning:** The student successfully identifies the core economic logic and reconstructs the argument by replacing hyperbole with defensible claims about price competition and livelihood, meeting all Level 3 criteria. They also correctly identify that the heckler attacks peripheral details rather than the subst

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Councillor Drava's conclusion says the state 'should' do something. Her premise says something 'is' the case. What is missing? What assumption would you need to add to make this argument valid? And once you add it, does the argument actually work?

**Expected Answer:** **Missing premises and the is-ought gap** — Drava's argument has a descriptive premise (children of unmarried couples often have emotional difficulties) and a normative conclusion (the state should discourage this). Any argument with a normative conclusion requires at least one normative premise — this is the is-ought gap. The missing premise *Identifying missing premises — especially normative ones — reveals the hidden assumptions on which an argument depends. By making Drava's argument valid through supplying premises, we can see more cle*

**Model Response:**
> **1.  What the argument looks like**

| Premise (descriptive) | “Children raised by unmarried couples often have emotional difficulties.” |
|-----------------------|--------------------------------------------------------------------------|
| Conclusion (normative) | “Therefore the state should discourage unmarried couples from raising children.” |

The premise tells us **what is** (a statistical regularity).  
The conclusion tells us **what ought to be done** (a policy prescription).  

**2.  The missing piece**

To move from a *descriptive* claim to a *prescriptive* claim we need at least **one** additional premise that links the two.  In logical form the argument would have to be:

1. **P₁** Children raised by unmarried couples often have emotional difficulties.  
2. **P₂** *If a condit

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'is-ought' gap, explicitly names the missing normative premise (P2) and the missing causal assumption (P3), and explains the mechanism clearly. However, the response stops short of Level 4 because it does not provide specific counterexamples or analyze confoundin

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The chronicler has two statements about the bridge collapse. Which one is an argument and which is an explanation? How can you tell the difference?

**Expected Answer:** **Distinguishing arguments from explanations** — Arguments try to convince you that a conclusion is true — the conclusion is in dispute. Explanations show why something already accepted as true occurred — the conclusion is taken for granted. The engineer's statement is an explanation: no one disputes that the bridge collapsed; the engineer explain *The key test is whether the 'conclusion' is already taken for granted or is in dispute. 'Because' can introduce either an explanation or a premise — context determines which. The engineer uses 'becaus*

**Model Response:**
> **Answer**

| Statement | Kind of discourse | Why it belongs to that kind |
|-----------|------------------|-----------------------------|
| **A – Engineer**<br>“The bridge collapsed **because** the support beams were eaten by termites and the recent flooding weakened the foundation.” | **Explanation** | It tells **why** a *already‑accepted fact* (the bridge collapsed) happened. The word *because* signals a causal link that is offered as a *description* of the event, not as a claim that needs to be proved. |
| **B – Inspector**<br>“The support beams show termite damage and the foundation has flood erosion. **Since** both structural supports failed simultaneously, the bridge **must have been unsafe** for at least a month before it collapsed. **Therefore**, the town is liable for negligence.

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Statement A as an explanation and Statement B as an argument. They accurately articulate the core criterion: explanations address already-accepted facts (taken for granted), while arguments attempt to convince an audience of a disputed conclusion. The response demons

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The guild master wants you to diagram this argument. Which premises must work together (linked) and which support the conclusion independently (convergent)?

**Expected Answer:** **Linked vs convergent premises and sub-arguments** — In argument diagramming, linked premises are premises that must work together to support a conclusion — neither is sufficient alone. Convergent premises independently support the same conclusion. In this argument, premises 1 and 2 are linked: 'Wanda had her pant leg rolled up' only supports 'she bik *Diagramming reveals that this argument has two independent lines of evidence converging on the same conclusion. If premise 3 turned out to be false (Bob was mistaken), the argument from premises 1 and*

**Model Response:**
> **1.  Which premises have to be linked?**  
- **Premise 1** – “Wanda arrived at work with her right pant leg rolled up.”  
- **Premise 2** – “Cyclists often roll up their right pant leg to keep it from catching in the chain.”

These two premises **must be used together**.  By themselves each one says very little about how Wanda got to work:

* P1* only tells us something about Wanda’s clothing.  
* P2* only tells us a habit that many cyclists have.

Only when they are **combined** do we get the intermediate inference:

> **(A) Wanda is probably a cyclist (or at least was behaving like one).**

Thus 1 + 2 are **linked (co‑dependent) premises** that together give a sub‑conclusion that later helps the main conclusion.

---

**2.  Which premise supports the conclusion independently?**  
- **Pr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Premises 1 and 2 as linked (co-dependent) and Premise 3 as independently convergent, satisfying the core requirements for Level 3. They provide a clear explanation of the mechanism and a diagram showing the structure. However, the response does not reach Level 4 beca

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Gruff seems very confident in dismissing Mira's proposal. But look at what he actually says — does he address any of the specifics of her plan?

**Expected Answer:** **Name calling / labeling** — Gruff substitutes negative labels for substantive engagement. Rather than challenging the aqueduct's costs, feasibility, or projected benefits, he attaches dismissive terms to Mira and her proposal. The labels carry negative connotations that encourage the audience to reject the proposal based on em *Labels are not arguments. Calling someone a 'dreamer' does not address whether their cost estimates are accurate, their engineering is sound, or the water supply is needed. The labels function as a su*

**Model Response:**
> **Short answer:**  
Gruff does **not** engage with any of the numbers, timelines, or engineering details Mira gave him. Instead he attacks the *person* who produced the plan and tries to win support by appealing to the merchants’ own self‑interest. The reasoning pattern at work is an **ad hominem (genetic) fallacy**—a “because‑the‑source‑is‑bad, the claim must be bad” move—often coupled with a **populist/appeal‑to‑self‑interest bias**.

---

## Step‑by‑step breakdown

| Step | What Gruff says | Why it matters | What logical move this is |
|------|----------------|----------------|---------------------------|
| 1 | “This is typical ivory‑tower nonsense from an out‑of‑touch academic.” | He labels Mira’s expertise as “ivory‑tower” and “out‑of‑touch.” | **Genetic/ad hominem** – dismissing an a

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism: Gruff attacks the person (Mira) rather than engaging with the substantive evidence (numbers, timelines, engineering). Although the student uses the formal term 'ad hominem' instead of the specific rubric term 'name calling/labeling,' their breakdo

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The villager says Brother Constant must be right because he has been saying it all week. Is that good reasoning?

**Expected Answer:** **Repetition / illusory truth effect** — Brother Constant repeats the claim 'The Old Bridge is cursed' with rhythmic insistence, without providing evidence. The illusory truth effect is a well-documented cognitive phenomenon: repeated exposure to a statement increases the feeling of familiarity, which people mistake for truth. The villager *Repetition is not evidence. A claim does not become more true by being stated more often. The feeling of familiarity that repetition produces is a cognitive artifact, not a rational basis for belief. *

**Model Response:**
> **Short answer:**  
No – the villager’s reasoning is not sound. He is committing the **appeal‑to‑repetition** (also called the *argumentum ad nauseam* or *repetition fallacy*) and is being driven by the **illusory‑truth cognitive bias**. Repeating a claim many times does not make it true; it only makes it feel familiar.

---

## Step‑by‑step analysis

| Step | What the villager says / thinks | Why it is a logical error |
|------|--------------------------------|---------------------------|
| 1.   | “Brother Constant has been saying *‘The Old Bridge is cursed’* every night for a week.” | This is an observation about **frequency of assertion**, not about evidence. |
| 2.   | “Therefore it must be true (or at least there is something to it).” | The conclusion is drawn **solely** from the fact

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern (repetition) and explicitly names the 'illusory-truth effect' and the 'familiarity-truth confusion,' meeting the core criteria for Level 4. The response demonstrates a deep understanding of the mechanism by distinguishing between frequency of assertion an

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge has been presented with clear evidence of slag dumping. Does his response address that evidence?

**Expected Answer:** **Whataboutism / red herring** — Forge responds to a specific accusation (slag dumping) by redirecting attention to unrelated issues (tannery hides, farm pesticides). The other problems may be real, but they do not address the evidence against Forge. This is a red herring: introducing an irrelevant topic to divert attention from th *The existence of other polluters does not change whether Forge dumped slag in the river. Each accusation should be evaluated on its own evidence. Forge's response addresses neither the witnesses, the *

**Model Response:**
> **Short answer:**  
No. Forge’s reply does not engage with the evidence that his shop is dumping slag. Instead he diverts the discussion to other polluters. The reasoning pattern he is using is a classic *red‑herring*—specifically the *tu quoque* (or “what‑about‑me”) fallacy.

---

## Step‑by‑step analysis

| Step | What the elder presents | What Forge says | Does it address the evidence? |
|------|------------------------|----------------|------------------------------|
| 1️⃣   | **Three eyewitnesses** saw slag leave Forge’s drainage pipe. | “Why are we talking about my shop …?” | No – he does not deny the witnesses. |
| 2️⃣   | **Water‑sample analysis** shows iron‑rich slag in the river downstream of his shop. | “…the tannery on the north end has been dumping hides …” | No – he does not 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a red herring and whataboutism (tu quoque). They clearly explain the mechanism: that the existence of other polluters is logically irrelevant to the specific evidence against Forge. Furthermore, the student addresses the nuance of selective enforcement

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Steele gave a passionate speech. But did he actually address Councillor Maren's economic analysis?

**Expected Answer:** **Flag-waving / appeal to patriotism** — Steele substitutes an appeal to group identity and patriotic emotion for engagement with the economic argument. He reframes a policy question (will trade lower prices?) as an identity question (are you loyal to Ironvale?). This shuts down cost-benefit analysis by making disagreement feel like betray *Whether trade with Ashford is economically beneficial is a factual question about prices, supply, and demand. It has nothing to do with patriotism or loyalty. Steele's appeal makes evaluating the prop*

**Model Response:**
> **Short answer:**  
No – Commander Steele never engages with the numbers or the cost‑benefit reasoning that Councillor Maren presented. Instead he launches an emotional, identity‑based attack on the idea of trade. The move is a classic **appeal to tradition / appeal to patriotism (argumentum ad antiquitatem)** that also functions as a **red‑herring** (or “whataboutism”) and, to a lesser extent, a **straw‑man** of the economic case.

---

## Step‑by‑step reasoning

| Step | What we look for | What we find in Steele’s speech |
|------|------------------|---------------------------------|
| **1. Identify the target argument** | Maren’s claim: *“Trade will lower grain and iron prices, improving prosperity.”* | Steele never mentions price, supply, demand, or any of the data. |
| **2. Check whet

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Steele substitutes economic analysis with an emotional, identity-based appeal and explains the mechanism clearly (shifting from data to loyalty). However, the student misidentifies the specific logical pattern as 'Appeal to Tradition' and 'Red Herring' rather th

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Krul certainly sounds confident. But did he actually respond to any of Wynn's specific points about enrollment data or graduate outcomes?

**Expected Answer:** **Thought-terminating cliche** — Krul deploys a barrage of stock phrases that sound like wisdom but carry no argumentative content. Each cliche is designed to end inquiry rather than advance it: 'It is what it is' implies nothing can or should change; 'if it ain't broke don't fix it' assumes without argument that nothing is broken; *Thought-terminating cliches are compressed assertions that masquerade as wisdom. They shut down inquiry without providing reasons. 'It is what it is' is not an argument — it is a refusal to engage. 'I*

**Model Response:**
> **Short answer:**  
No. Professor Krul never touches Wynn’s enrollment statistics, graduate‑outcome figures, or the comparative data he presented. He simply repeats a set of platitudes about “the way things have always been” and declares the matter closed.  

**What logical pattern is he using?**  

| Step | What Krul says (or does) | Why it doesn’t answer Wynn’s points | The fallacy / bias it exemplifies |
|------|--------------------------|--------------------------------------|-----------------------------------|
| 1 | “The Academy has always taught theory first …” | This is a historical claim, not a rebuttal of the *data* Wynn supplied. | **Appeal to Tradition** (argumentum ad antiquitatem) – “We’ve always done it, therefore it’s right.” |
| 2 | “If it ain’t broke, don’t fix it.” | No 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Krul uses stock phrases (platitudes) to shut down inquiry without addressing Wynn's data, which satisfies the core requirements for Level 3. They accurately explain the mechanism: the phrases ignore specific evidence and rely on tradition or authority. However, 

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** You have the damage report and you have heard both accounts. What is each speaker doing with the facts, and what would an accurate description look like?

**Expected Answer:** **Exaggeration / minimization** — Both speakers distort the significance of the same event in opposite directions. Holt minimizes: 'a few minutes,' 'a couple of lettuce leaves,' 'barely a scratch.' Tess exaggerates: 'destroyed my entire garden,' 'nothing to eat this winter,' 'I will starve.' The actual damage — roughly a third of th *Distorting the magnitude of an event — in either direction — undermines rational assessment. Holt's minimization would lead to inadequate compensation; Tess's exaggeration would lead to disproportiona*

**Model Response:**
> **Step‑by‑step analysis**

|  | What the person says | What the damage report says | How the person is treating the facts |
|---|----------------------|----------------------------|--------------------------------------|
| **Farmer Holt** | “My goats were only in the garden a few minutes. They nibbled a couple of lettuce leaves. It was *barely a scratch* … she’s making a mountain out of a mole‑hill.” | The goats ate **about one‑third of the lettuce crop** and trampled **two rows of beans**. | **Down‑playing / minimizing** the damage. He selects the smallest, least‑harmful part of the evidence (a “couple of leaves”) and frames the whole incident as trivial. This is a classic case of **self‑serving bias** (or “motivated reasoning”) – the desire to protect his reputation and avoid responsibil

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies both distortions (Holt's minimization and Tess's exaggeration), explains the self-serving mechanisms behind them, provides the accurate middle-ground description based on the damage report, and successfully generalizes the principle to broader concepts like motivated

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Harl says he is just asking questions and that we need more study. Is he raising legitimate scientific concerns, or is something else going on?

**Expected Answer:** **Doubt casting / manufacturing uncertainty** — Harl's strategy is not to present counter-evidence but to generate a fog of doubt around existing evidence. He questions calibration without alleging specific errors, raises the specter of conflicts of interest without identifying any, invokes 'some scientists' without naming them or citing studies, *Legitimate scientific skepticism identifies specific methodological flaws and proposes concrete alternatives. Harl does neither. His doubts are generic enough to apply to any study on any topic. If no*

**Model Response:**
> **Short answer:**  
Harl is not offering a genuine scientific critique. He is using a classic “manufacture‑of‑doubt” pattern – an **appeal to uncertainty / argument from ignorance** (sometimes called “the burden‑of‑proof fallacy”) together with **cherry‑picking** and **shifting the burden of proof**. In other words, he is trying to create the impression that the evidence is unreliable and that the council must wait for “more study,” even though the data already meet the standard for reasonable action.

---

## Step‑by‑step analysis

| What Harl says | Why it sounds like a question | What logical move it really is |
|----------------|------------------------------|--------------------------------|
| “Are we really sure about these tests? Science gets things wrong all the time.” | Raises dou

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern as 'manufacture-of-doubt' and explicitly distinguishes between legitimate skepticism (requiring specific flaws) and manufactured uncertainty (vague appeals to ignorance). They accurately analyze the mechanism by breaking down Harl's specific tactics 

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor presents two arguments on stone tablets. Which is valid? Which is sound? Explain your reasoning. If an argument is invalid, provide a counterexample.

**Expected Answer:** **Validity and soundness** — A valid argument is one where the conclusion cannot possibly be false if the premises are true. Soundness = validity + true premises. Tablet A is valid: IF everyone born in France speaks French AND Obama was born in France, THEN he speaks French — the conclusion follows necessarily. But it is unsoun *Understanding validity requires separating the logical structure from the truth of the claims. Many students reject Tablet A because its premises are obviously false — but that is a soundness judgment*

**Model Response:**
> **Short answer**

| Tablet | Logical form | Valid? | Sound? | Why (and what the problem is) |
|--------|--------------|--------|--------|--------------------------------|
| **A**  | All \(F\) are \(G\);  \(a\) is \(F\);  ∴ \(a\) is \(G\) (modus ponens / Barbara) | **Yes** – the conclusion follows from the premises. | **No** – the second premise (“Barack Obama was born in France”) is false, so the argument is unsound. | The inference is perfectly logical; the error is factual. |
| **B**  | \(P\) → \(E\) (if elected then President) is *implicitly* assumed;  \(P\);  ∴ \(E\) | **No** – it commits the fallacy of **affirming the consequent** (or illicit conversion). | Because it is invalid it cannot be sound; even if the premises happen to be true, the conclusion is not guaranteed. | The move fr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Tablet A as valid but unsound due to a false premise, and Tablet B as invalid. They provide a clear counterexample for Tablet B (a President can obtain office without election) and accurately explain the distinction between validity and soundness. The response meets 

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Translate both sentences into symbolic logic. Then explain: do they mean the same thing? If not, what is the difference?

**Expected Answer:** **Propositional logic connectives and translation** — 'Not both' is the negation of a conjunction: ~(C * I). It is true whenever at least one of the conjuncts is false — Carla could have cake alone, ice cream alone, or neither. 'Neither-nor' is a conjunction of two negations: ~C * ~I. It is true only when both are false — Carla has no cake and no ice c *Correct translation from natural language to symbolic logic requires careful attention to the scope of negation. 'Not both' negates the conjunction as a whole. 'Neither-nor' negates each component sep*

**Model Response:**
> **Step 1 – Put the atomic propositions on the board**

* C : “Carla has cake”  
* I : “Carla has ice‑cream”

(We treat “will have” as a simple present‑time proposition – the temporal word does not affect the logical form.)

---

## 1.  “Carla will **not** have **both** cake and ice‑cream.”

The English phrase “not both … and …” is the negation of a conjunction:

\[
\boxed{\neg (C \land I)}
\]

Using De Morgan’s law we can rewrite it as an equivalent disjunction of the negations:

\[
\neg (C \land I)\;\equiv\; \neg C \;\lor\; \neg I
\]

So the first sentence says: *at least one of the two items will be missing* (it allows the possibility that Carla has cake **or** ice‑cream, just not both).

---

## 2.  “Carla will have **neither** cake **nor** ice‑cream.”

“Neither … nor …” means “not … an

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly translates both propositions (~(C * I) and ~C * ~I), clearly explains the semantic difference (allowing one vs. forbidding both), constructs a complete truth table demonstrating the non-equivalence, and explicitly references De Morgan's Law. This meets all criteria for Level 4.

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build the truth table for this argument. Is the argument valid? How does the truth table show you?

**Expected Answer:** **Truth table test of validity** — The truth table test works by checking every possible assignment of truth values. An argument is valid if and only if there is no row where all premises are true and the conclusion is false. For this disjunctive syllogism (S v D, ~S, therefore D): with four rows of truth values, the only row where b *The truth table test is a formal method: we can assess validity even without knowing what the argument is about. It is mechanical and objective, unlike the informal test which depends on our ability t*

**Model Response:**
> ### 1. Symbolising the argument  

| English sentence | Symbol |
|------------------|--------|
| “The convict escaped through the sewage pipes.” | **S** |
| “The convict escaped by hiding in the delivery van.” | **D** |
| Premise 1: “Either the convict escaped through the sewage pipes **or** the convict escaped by hiding in the delivery van.” | **S ∨ D** |
| Premise 2: “The convict did **not** escape through the sewage pipes.” | **¬S** |
| Conclusion: “Therefore the convict escaped by hiding in the delivery van.” | **D** |

The argument in symbolic form is  

\[
\begin{array}{c}
S \lor D \\
\neg S \\
\hline
\therefore D
\end{array}
\]

---

### 2. Truth‑table construction  

We need a column for each atomic proposition (**S**, **D**) and for the three compound statements that appear in the

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructs the truth table, accurately computes all values, and explicitly identifies the validity test (checking for rows where premises are true and conclusion is false). They correctly conclude the argument is valid based on the absence of a counterexample row. However, the 

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks: what rule of inference justifies each derived step? Name the rule and explain how it applies.

**Expected Answer:** **Modus ponens and hypothetical syllogism** — Step 4 uses modus ponens (MP): from 'if P then Q' and 'P', derive 'Q'. Step 5 also uses MP: from 'if Q then R' and 'Q', derive 'R'. Step 6 uses hypothetical syllogism (HS): from 'if P then Q' and 'if Q then R', derive 'if P then R'. These are three of the eight basic valid forms of inference. Each p *Inference rules are the building blocks of proofs. MP and HS are two of the most fundamental. MP lets you detach a consequent when you have the antecedent. HS lets you chain conditionals into longer c*

**Model Response:**
> **Step 4 – “The ground is wet”**  

*Premises used*:  

1. If it is raining, then the ground is wet. \(R \rightarrow W\)  
3. It is raining. \(R\)  

*Rule*: **Modus Ponens** (also called *detachment*).  

*Why it works*: Modus Ponens says that from a conditional statement \(P\rightarrow Q\) and an affirmation of its antecedent \(P\), we may infer the consequent \(Q\).  
Here \(P\) is “it is raining” (\(R\)) and \(Q\) is “the ground is wet” (\(W\)). Since we have both \(R\rightarrow W\) and \(R\), we may conclude \(W\).

---

**Step 5 – “The match will not light”**  

*Premises used*:  

2. If the ground is wet, then the match will not light. \(W \rightarrow \lnot L\)  
4. The ground is wet. \(W\)  

*Rule*: **Modus Ponens** again.  

*Why it works*: The same pattern applies: from \(W\righ

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Modus Ponens for steps 4 and 5 and Hypothetical Syllogism for step 6. They also accurately explain the general form of each rule and map the specific variables to the abstract patterns. However, the response does not address invalid look-alikes (such as affirming the

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Construct a proof deriving B v D from the three premises. Name each rule you use. Try working both forward from the premises and backward from the conclusion.

**Expected Answer:** **Constructing natural deduction proofs** — The proof uses constructive dilemma: from P v Q, P->R, Q->S, derive R v S. Working backwards: the conclusion B v D is a disjunction, so ask what rules produce disjunctions. Constructive dilemma does, and it requires a disjunction plus two conditionals — exactly what premises 1-3 provide. Working for *Natural deduction proofs require strategic thinking about which rules to apply and in what order. The backward strategy asks: what rule could produce the conclusion's form? The forward strategy asks: *

**Model Response:**
> **A step‑by‑step natural‑deduction proof**

We are given the three premises  

1. \(A \rightarrow B\)                 (premise)  
2. \(C \rightarrow D\)                 (premise)  
3. \(A \lor C\)                         (premise)  

and we must derive  

\(\;B \lor D\).

Below each line is the rule that justifies it.  
(The proof uses the usual eight rules of propositional natural‑deduction:  
→‑introduction, →‑elimination (Modus Ponens), ∨‑introduction, ∨‑elimination, ∧‑introduction, ∧‑elimination, ¬‑introduction, ¬‑elimination.  Only the ones we need appear.)

| # | Statement | Reason |
|---|-----------|--------|
| 1 | \(A \rightarrow B\) | Premise |
| 2 | \(C \rightarrow D\) | Premise |
| 3 | \(A \lor C\) | Premise |
| 4 | **Assume** \(A\) | **Assumption** (for ∨‑elimination) |
| 5 | \

**Score:** 2/4 ██░░
**Judge Reasoning:** The student constructed a valid natural deduction proof, but it is unnecessarily long (10 lines) compared to the optimal one-step Constructive Dilemma. The student failed to recognize the specific pattern (Constructive Dilemma) highlighted in the key explanation, instead relying on the more fundamen

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Test the syllogism using Venn diagrams. Then translate 'Nobody loves me but my mother' into categorical form. What are the categories?

**Expected Answer:** **Categorical statements, translation, and Venn diagrams** — Categorical logic deals with four statement types: All S are P (universal affirmative), No S are P (universal negative), Some S are P (particular affirmative), Some S are not P (particular negative). The syllogism 'All H are M, All M are D, therefore All H are D' is valid: the Venn diagram for the t *Categorical logic captures structure within propositions that propositional logic misses. The Venn diagram test is visual and systematic: diagram the premises, then check whether the conclusion is alr*

**Model Response:**
> We need to answer: test the syllogism using Venn diagrams, then translate the sentence "Nobody loves me but my mother" into categorical form, identifying categories. Also identify what reasoning pattern, fallacy, bias, or principle is being demonstrated.

The scenario: instructor says propositional logic can't capture internal structure; need categorical logic (syllogisms). The syllogism: All humans are mortal. All mortal things die. Therefore, all humans die. That's a classic Barbara syllogism (AAA-1). Using Venn diagrams: draw three circles: H (humans), M (mortals), D (die). Premise1: All H are M => shade outside M within H? Actually for "All H are M", we shade the part of H outside M. Premise2: All M are D => shade part of M outside D. Then conclusion: All H are D => check if the part o

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly tests the syllogism using Venn diagrams with accurate shading instructions and correctly translates the tricky sentence 'Nobody loves me but my mother' into categorical form ('All who love me are my mother'), explicitly identifying the categories as 'people who love me' and 'my

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build truth tables for each pair. Which pairs are logically equivalent? Explain what each equivalence (or non-equivalence) means in plain language.

**Expected Answer:** **Logical equivalence: contraposition and De Morgan's Laws** — Pair 1 (A->B and ~AvB) is equivalent: a conditional says the same thing as the negation of the antecedent or the consequent. Pair 2 (~(A*B) and ~Av~B) is equivalent: this is De Morgan's Law — the negation of a conjunction is a disjunction of negations ('not both' equals 'not-A or not-B'). Pair 3 (A- *Logical equivalence is a powerful tool for simplifying and transforming arguments. De Morgan's Laws let you move between negations of conjunctions and disjunctions of negations. The conditional-as-dis*

**Model Response:**
> **Step‑by‑step truth‑table work**

We have two propositional variables, **A** and **B**.  
For each pair we write a three‑column table (A, B, then the two formulas).  
The last column shows whether the two formulas have the same truth‑value on every line.

---

### Pair 1 \(A\rightarrow B\) vs. \(\lnot A \lor B\)

| A | B | \(A\rightarrow B\) | \(\lnot A\) | \(\lnot A\lor B\) | Same? |
|---|---|-------------------|------------|-------------------|-------|
| T | T | T                 | F          | **T** (F ∨ T)     | ✔︎ |
| T | F | **F**             | F          | **F** (F ∨ F)     | ✔︎ |
| F | T | T                 | **T**      | **T** (T ∨ T)     | ✔︎ |
| F | F | T                 | **T**      | **T** (T ∨ F)     | ✔︎ |

All four rows match → **\(A\rightarrow B\) is logically (materially

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly constructs truth tables and accurately determines the equivalence for Pair 1 and Pair 2. However, the response is incomplete: it cuts off mid-table for Pair 2, completely omits Pair 3 (the conditional vs. converse comparison), and provides no explanatory text regarding the mech

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Which argument is deductive and which is inductive? After learning that Tweets is six feet tall and runs thirty miles per hour, what happens to each argument? Why?

**Expected Answer:** **Deductive vs inductive arguments and defeasibility** — The mathematician's argument is deductive: if the premises are true, the conclusion follows with certainty. Adding new information cannot undermine a valid deductive argument (though it might challenge a premise). The naturalist's argument is inductive: the premises make the conclusion probable, not *The key distinction is between certainty and probability, and between defeasibility and non-defeasibility. Deductive arguments either guarantee their conclusions (valid) or do not (invalid) — there is*

**Model Response:**
> **1.  Which argument

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student's response is incomplete and cuts off immediately after the first question header ('1. Which argument'). No content was provided to identify the argument types, explain defeasibility, or address the impact of new information. Therefore, the response demonstrates no understanding of the t

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe asks you to evaluate both polls. Which one should the council trust, and what are the problems with the other one?

**Expected Answer:** **Statistical generalizations: sample size and representativeness** — A good statistical generalization requires two conditions: adequate sample size and a representative sample. Pollster A fails both: 20 people is too few (hasty generalization), and surveying only at the Miners' Guild creates a biased sample that likely overrepresents mining interests. Pollster B use *Evaluating statistical generalizations requires checking sample size and representativeness. Pollster A's survey is doubly flawed: 20 people is too small to generalize from (the result could easily be*

**Model Response:**
> **Short answer:**  
The council should base its expectations on **Poll B**.  
Poll A suffers from two fatal flaws – an extremely small, non‑random sample that is heavily biased toward one sub‑group (miners) – which makes its 75 % figure a classic *hasty‑generalization* (or *sampling‑bias*) claim. Poll B, while not perfect, uses a much larger, randomly drawn sample from the whole population, so its result (≈52 % for Candidate X) is far more reliable.

---

## Step‑by‑step evaluation

| Feature | Poll A | Poll B |
|---------|--------|--------|
| **Sample size** | 20 people | 500 people |
| **How the sample was chosen** | “People at the Miners’ Guild hall” – a convenience sample of a single occupational group. | “Randomly selected from the full census roll” – a probability (random) sample cov

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern (statistical generalization) and explicitly names the 'hasty generalization' fallacy. They thoroughly explain both required conditions: adequate sample size (calculating standard errors to demonstrate uncertainty) and representativeness (identifying selec

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Three investigators each offer an explanation. Evaluate each one using the explanatory virtues. Which is the best explanation, and why?

**Expected Answer:** **Inference to the best explanation and explanatory virtues** — IBE selects the hypothesis that best explains the observed evidence according to the explanatory virtues. Lira's explanation (teleportation by rogue mage) is unfalsifiable, inconsistent with background knowledge, and introduces unnecessary entities — it fails on simplicity, testability, and consiste *IBE is not about which explanation is merely possible — all three are possible. It is about which explanation does the best job of accounting for the evidence according to the explanatory virtues. Lir*

**Model Response:**
> ## 1.  The task – “inference to the best explanation”

What the magistrate is being asked to do is a classic **abductive** or **inference‑to‑the‑best‑explanation (IBE)** exercise.  
The three investigators each present a *hypothesis* that purports to make sense of the same set of facts:

| Fact | Shared by all hypotheses |
|------|---------------------------|
| The warehouse is empty. |
| No forced entry was found. |
| The night‑watch was on duty. |
| There are wagon tracks leading away from the back of the building. |

The magistrate must judge which hypothesis scores highest on the **explanatory virtues** (simplicity, scope, coherence, testability, consilience, etc.) and therefore is the most credible.

---

## 2.  Evaluating the three explanations

| Virtue | Lira – “Rogue‑mage teleport

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the IBE pattern and evaluates all three hypotheses against multiple explanatory virtues (fit, simplicity, scope, coherence, testability). They accurately rank Lira as the worst and provide strong reasoning for preferring Gareth or Nessa. However, the response falls s

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher draws an analogy between the drowning child and the daily coffee purchase. Is it a good analogy? Evaluate the relevant similarities and the disanalogies Aldric raises. Which disanalogies, if any, are relevant to the moral conclusion?

**Expected Answer:** **Argument by analogy: relevant similarities and disanalogies** — An argument by analogy infers that because two things share relevant similarities, what is true of one is probably true of the other. The philosopher argues: (1) The pond case and the coffee case share a relevant similarity — choosing a luxury over a child's survival. (2) In the pond case, saving th *Evaluating analogies requires identifying the relevant similarities and assessing whether the disanalogies matter. The philosopher's analogy is strong because the core moral feature — valuing a luxury*

**Model Response:**
> **Short answer:**  
The philosopher’s comparison is a *weak (false) analogy*.  It captures a genuine moral intuition – that we ought not to let a trivial, self‑indulgent expense stand in the way of a child’s life when the cost to us is tiny – but it glosses over several material differences that matter for the *strength* of the moral claim.  Aldric’s objections (distance, indirectness, negligible impact, systemic nature of famine) are genuine *dis‑analogies*; some of them (especially the question of whether the coffee money can actually save a life) are *relevant* to the conclusion that Aldric has a moral duty to donate, while others (mere geographic distance) are *irrelevant* to the underlying principle the philosopher is trying to invoke.

Below is a step‑by‑step analysis that spells out

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the argument pattern (argument from analogy) and explicitly lists the core similarity (trivial cost vs. child's life). They also identify multiple disanalogies raised by Aldric (distance, efficacy, systemic nature) and successfully evaluate their relevance, distingui

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Using the vet's log, apply the necessary condition test and the sufficient condition test to each factor. Which factor is the likely cause of Whiskers' seizures?

**Expected Answer:** **Mill's methods: necessary and sufficient condition tests** — The necessary condition test: which factor is present in every seizure case? F is present in all three seizure days. T is present in days 1 and 3 but not day 2. V is present in days 1 and 2 but not day 3. Only F passes the necessary condition test. The sufficient condition test: which factor is abse *Mill's methods provide systematic tools for causal investigation. The necessary condition test eliminates factors that are absent when the effect occurs. The sufficient condition test eliminates facto*

**Model Response:**
> **Step‑by‑step application of the “necessary‑condition” and “sufficient‑condition” tests**

| Factor | Does the factor appear on **every** seizure day? (Necessary?) | Does the factor appear on **any** non‑seizure day? (Sufficient?) | Verdict |
|--------|---------------------------------------------------------------|---------------------------------------------------------------|---------|
| **New food (F)** | **Yes** – all three seizure days (1, 2, 3) have F.  <br>→ *If a seizure occurs, then F is present.*  → **F is a necessary condition** for a seizure (in this data set). | **No** – none of the two non‑seizure days have F.  <br>→ *If F is present, a seizure occurs.*  → **F is also a sufficient condition** (every time F appears a seizure follows). | **Likely cause** |
| **Thunderstorm (T

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the causal pattern and systematically applies both the necessary and sufficient condition tests to all three factors (F, T, V). They accurately determine that F is the only factor present in every seizure case and absent in every non-seizure case, while correctly rul

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Councillor Drava claims the tonic causes higher yields based on the correlation data. What is wrong with this inference? Identify the alternative explanations.

**Expected Answer:** **Correlation vs causation: third variable and reverse causation** — When two things are positively correlated, there are four logical possibilities: (1) A causes B, (2) B causes A, (3) a third variable C causes both, (4) the correlation is coincidental. Drava assumes possibility 1 (tonic causes higher yields). The physician raises possibility 3 (wealth is the confou *Recognizing that correlation does not establish causation is essential for evaluating empirical arguments. To establish causation, you need to rule out confounding variables and reverse causation — ty*

**Model Response:**
> **Short answer**  
Drava is committing the classic *correlation‑does‑not‑imply‑causation* error (the “cum‑hoc / post‑hoc” or *false‑cause* fallacy). From the observation that “farms whose workers drink Vigor Tonic have 20 % higher yields” he jumps straight to the conclusion that the tonic *produces* the higher yields, without ruling out any other way the two facts could be linked.

---

## Step‑by‑step analysis of the inference

| Step in Drava’s reasoning | Why it is problematic |
|---------------------------|-----------------------|
| **1. Observe a statistical association** (tonic‑drinkers ↔ higher yields). | An association is a *necessary* but not a *sufficient* condition for a causal claim. |
| **2. Assume the direction of causation** (tonic → higher yields). | The data are *cross‑sec

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the false cause fallacy and explicitly names both alternative explanations required for Level 3 (confounding variable/wealth and reverse causation). Furthermore, the response exceeds Level 3 by clearly stating that correlation is necessary but not sufficient for caus

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Solve the three probability problems. Show your work and explain which probability law you use for each one.

**Expected Answer:** **Basic probability laws: complement, addition, conjunction** — Problem 1 (complement): P(not-4) = 1 - P(4) = 1 - 1/6 = 5/6. Problem 2 (addition with correction): P(at least one H) = P(H on coin 1) + P(H on coin 2) - P(H on both) = 1/2 + 1/2 - 1/4 = 3/4. Alternatively, use complement: 1 - P(no heads) = 1 - 1/4 = 3/4. Problem 3 (at least one via complement): P(at *The complement rule is the most useful tool in basic probability: often it is easier to calculate the probability of something NOT happening and subtract from 1. The addition rule must correct for dou*

**Model Response:**
> **The three dice‑master problems**

| # | Question | Solution (step‑by‑step) | Probability law used |
|---|----------|------------------------|----------------------|
| 1 | “What is the probability of **NOT** rolling a 4 on a fair d6?” | • A single roll has 6 equally likely faces. <br>• One of those faces is a 4, so  **P(4) = 1/6**. <br>• The complement of “rolling a 4’’ is “not rolling a 4’’.<br>• **P(not 4) = 1 – P(4) = 1 – 1/6 = 5/6**. | **Complement rule**:  P(Aᶜ)=1−P(A). |
| 2 | “I flip two fair coins. What is the probability that **at least one** lands heads?” | • List the four equally likely outcomes of two flips: HH, HT, TH, TT. <br>• The only outcome that does **not** satisfy “at least one head’’ is TT. <br>• **P(at least one H) = 1 – P(TT)**. <br>• Because the flips are independe

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly solves all three problems using the appropriate probability laws (complement rule and independence). They show clear step-by-step work and explicitly note the independence assumption in problems 2 and 3. However, the response falls short of Level 4 because it does not explicitl

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The magistrate asks: given Bob's 99% accuracy and 1000 people in the area with 5 actual robbers, what is the probability that Nancy is truly the robber? Show your reasoning.

**Expected Answer:** **Conditional probability, Bayes' theorem, and base rate reasoning** — The naive answer is 99%, but this ignores the base rate. Using Bayes' theorem: Of 1000 people, 5 are robbers. Bob correctly identifies 99% of 5 robbers = 4.95 true positives. Bob incorrectly identifies 1% of 995 innocent people = 9.95 false positives. Total positive identifications = 4.95 + 9.95 = 1 *Conditional probability requires updating prior probabilities with new evidence. The key insight is that when the base rate is low (few robbers in the population), even a highly accurate test produces*

**Model Response:**
> **Step‑by‑step calculation (Bayes’ theorem)**  

|                              | **Robber (Guilty)** | **Not robber (Innocent)** | **Total** |
|------------------------------|---------------------|----------------------------|-----------|
| **Number of people**         | 5                   | 995                        | 1000      |
| **Bob says “yes” (identifies)** |                     |                            |           |
| – True‑positive rate (sensitivity) = 0.99 | 5 × 0.99 = **4.95** | – | |
| – False‑positive rate = 1 – specificity = 0.01 | – | 995 × 0.01 = **9.95** | |
| **All “yes” identifications** | 4.95                | 9.95                       | 14.90     |

The probability that the person Bob points to (Nancy) is actually the robber is the proportion of the “yes” case

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly calculates the posterior probability (~33%) using a clear frequency-based approach (true positives vs. false positives). They explicitly identify the base-rate fallacy and the prosecutor's fallacy, correctly distinguishing between P(ID+|Guilty) and P(Guilty|ID+). Furthermore, t

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The patient believes she has a 95% chance of having colon blight. Is she right? Use the base rate and test accuracy to compute the actual probability. Show your work.

**Expected Answer:** **Base rate reasoning in medical screening** — For a population of 100,000: 500 have colon blight (0.5% base rate). Of those 500, the test correctly identifies 95% = 475 true positives. Of the 99,500 without the disease, the test incorrectly flags 5% = 4,975 false positives. Total positive results = 475 + 4,975 = 5,450. P(disease | positive test *The base rate fallacy occurs when people ignore the prior probability of a condition and treat the test accuracy as the probability of having the condition. When a disease is rare (0.5%), the 5% false*

**Model Response:**
> **Step‑by‑step calculation (Bayes’ theorem)**  

| Symbol | Meaning |
|--------|---------|
| \(D\) | “the patient actually has colon blight” |
| \(\bar D\) | “the patient does **not** have colon blight” |
| \(+\) | “the test result is positive” |
| \(P(D)\) | prevalence (base‑rate) of the disease in the population |
| \(P(+\mid D)\) | sensitivity = probability the test is positive **given** disease |
| \(P(-\mid \bar D)\) | specificity = probability the test is negative **given** no disease |
| \(P(+\mid \bar D)\) | false‑positive rate = \(1-\)specificity |

Numbers supplied  

* Prevalence (base‑rate): \(P(D)=0.5\% = 0.005\)  
* Sensitivity: \(P(+\mid D)=0.95\)  
* Specificity: \(P(-\mid \bar D)=0.95\) → \(P(+\mid \bar D)=1-0.95=0.05\)

Bayes’ theorem gives the **positive‑predictive value

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly computes the probability (~8.7%) using Bayes' theorem (mathematically equivalent to the natural frequencies method) and clearly explains the mechanism of base rate neglect, identifying the fallacy by name. However, the response does not fully meet Level 4 criteria because it la

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sergeant Dallow seems confident in his logic. Look at the sign, then look at his reasoning. Does his conclusion actually follow?

**Expected Answer:** **Denying the antecedent** — Dallow reasons from 'If royal writ, then entry' and 'no royal writ' to 'no entry.' He treats the antecedent as necessary when the sign only establishes it as sufficient. *The conditional only tells us P is sufficient for Q, not necessary. Denying the antecedent does not validly yield the denial of the consequent. Other conditions may also lead to Q.*

**Model Response:**
> **Short answer:**  
No – his conclusion does **not** follow. He is committing the **fallacy of denying the antecedent** (sometimes called “inverse error”). He is treating a *sufficient* condition (“if you have a writ, you may pass”) as if it were also a *necessary* condition (“you may pass only if you have a writ”).

---

## Step‑by‑step analysis

1. **What the sign actually says**  
   > “If you carry a royal writ, you may pass.”  

   In logical notation this is:  

   \[
   P \rightarrow Q
   \]

   where  

   * **P** = “you carry a royal writ”  
   * **Q** = “you may pass”

   This is a **conditional** that tells us **only** that *having a writ guarantees permission*. It says nothing about what happens when you don’t have a writ.

2. **What Sergeant Dallow does**  

   - Premise 1: \(

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('denying the antecedent'), clearly explains the confusion between sufficient and necessary conditions, and provides a rigorous logical analysis including symbolic notation and truth tables. The response fully satisfies all criteria for Level 4, including the

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Wynn seems sure it was a wolf. Does the conclusion follow from what she observed?

**Expected Answer:** **Affirming the consequent** — Wynn reasons from 'If wolf then large paw prints' and 'large paw prints' to 'wolf.' She treats the consequent as proof of the antecedent. *The conditional tells us a wolf attack would produce large paw prints, but many other causes could too. Observing Q does not allow us to conclude P.*

**Model Response:**
> **Short answer:**  
No – Wynn’s inference is invalid. She is committing the logical fallacy **affirming the consequent** (sometimes called “the converse error”). In other words, she is treating a *sufficient* condition as if it were also *necessary*.

---

## Step‑by‑step analysis

1. **What she actually knows (the conditional premise).**  

   > *If a wolf attacked the sheep, then we would find large paw prints near the pen.*

   Symbolically:  

   \[
   W \;\rightarrow\; L
   \]

   where  

   * \(W\) = “a wolf attacked the sheep”  
   * \(L\) = “large paw prints are found near the pen”

   This statement says: **whenever** a wolf is the culprit, the evidence will include large prints. It does **not** say that large prints can only be produced by a wolf.

2. **What she observes (the co

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy 'affirming the consequent', correctly explains the logical mechanism by distinguishing between sufficient and necessary conditions, and provides specific alternative explanations (edge cases) such as dogs or bears that could cause the same evidence.

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Varn seems very worried about this bakery permit. He has given you a chain of consequences. Do you find his reasoning convincing? Why or why not?

**Expected Answer:** **Causal slippery slope** — Varn chains together a sequence of causal claims — competition leads to price drops leads to corner-cutting leads to illness leads to overwhelmed healers leads to plague — treating each link as inevitable. Even if each individual step had a 90% probability, the probability of the entire six-step cha *Probabilities are not preserved across a chain of causal claims. Each link in the chain has its own probability of occurring, and the joint probability of the entire sequence is the product of all the*

**Model Response:**
> **Short answer:**  
No – Varn’s argument is not convincing. He is using a classic **slippery‑slope** line of reasoning (often coupled with an **appeal to fear**) and is committing several logical errors: he treats each “if‑then” link as inevitable, supplies no evidence that the chain will actually occur, and ignores alternative outcomes or mitigating factors.

---

## Step‑by‑step deconstruction of the argument

| Step in Varn’s chain | Implicit claim | Why the claim is dubious |
|----------------------|----------------|--------------------------|
| 1️⃣ *Permit → competition* | “A second bakery will necessarily create competition.” | Competition is plausible, but the magnitude and nature of it are not guaranteed. The two bakeries could coexist, specialize, or even cooperate. |
| 2️⃣ *Compe

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'slippery-slope' pattern and provides a comprehensive deconstruction of the causal chain. Crucially, they explicitly explain the probabilistic mechanism ('multiply the individual probabilities together') that causes the likelihood to diminish rapidly across the l

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Pip seems very confident in his proof. Is his reasoning valid? Can you spot the mistake?

**Expected Answer:** **Composition fallacy** — Pip infers that a property true of each individual part (each atom is invisible) must be true of the whole composed of those parts (Pip is invisible). But visibility is not a property that transfers from parts to whole in this way — the arrangement and quantity of atoms creates emergent properties l *Properties of individual parts do not necessarily hold for the whole they compose. Each atom is invisible, but billions of atoms arranged into a human body are very much visible. Whether a property tr*

**Model Response:**
> **Short answer:**  
No – Pip’s “proof’’ is not valid. He is committing the **fallacy of composition** (or, equivalently, a **division error**): he assumes that because every *part* of him (each atom) is invisible to the naked eye, the *whole* (his body) must also be invisible. In reality visibility is an emergent property of large collections of atoms, not a simple sum of the properties of the individual atoms.

---

## Step‑by‑step analysis of Pip’s argument

| Step | What Pip says | Why it sounds plausible | What is actually wrong |
|------|---------------|------------------------|------------------------|
| 1 | “Every atom in my body is invisible to the naked eye.” | It is true that a single atom is far too small to be resolved by the unaided human eye. | “Invisible to the naked eye” is

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy of composition by name and explains the logical error: assuming a property of parts (invisibility) applies to the whole. They provide a robust explanation of emergent properties and light scattering. Crucially, they satisfy the Level 4 requirement by prov

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorin is trying to figure out how much individual parts of the house are worth based on the total value. Does his reasoning work?

**Expected Answer:** **Division fallacy** — Dorin infers that because the whole house has a certain property (being worth 900 gold), each part of the house must share that property proportionally. But the house's value comes from the arrangement and integration of its parts, not from the parts individually. Disassembled lumber and stones are  *The value of the house is an emergent property of its assembled structure — location, craftsmanship, functional integration. Individual beams and stones do not carry proportional shares of that value.*

**Model Response:**
> **Short answer:**  
No – Dorin’s calculation does **not** give the true market value of any individual beam, stone, nail, etc. He is committing the **fallacy of division** (sometimes called the “inverse” of the fallacy of composition) by assuming that because the *whole* house is worth 900 gold, each *part* must be worth a proportional share of that 900 gold.

---

## Step‑by‑step why the reasoning fails

| Step | What Dorin does | Why it is mistaken |
|------|----------------|--------------------|
| 1. | Takes the **total market price** of the house (900 gold). | The price reflects the *bundle* of services the house provides (shelter, location, aesthetics, legal title, etc.), not a simple sum of material costs. |
| 2. | Counts the **number of “components”** (≈900) and divides 900 gold by 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'fallacy of division,' correctly explains the mechanism of emergent properties (synergy, the whole being more than the sum of parts), and distinguishes between average and marginal value. The response demonstrates a sophisticated understanding that exceeds the basic 

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Brother Vassyl seems very confident. What do you think about the reasoning he just gave you for trusting the Codex?

**Expected Answer:** **Begging the question (circular reasoning)** — The conclusion — that the Codex is the ultimate authority — is assumed as a premise when the speaker cites the Codex's own claim of infallibility as evidence. The premise and conclusion are nearly identical. *The argument assumes exactly what it is trying to prove. The Codex's reliability is the very thing in question. Formally the argument can be valid — 'P, therefore P' is valid — but validity alone is n*

**Model Response:**
> **Short answer:**  
Brother Vassyl is committing a **circular‑reasoning fallacy (begging the question)** – he is using the Codex’s own claim of infallibility as the proof that the Codex is infallible. In other words, the premise and the conclusion are the same statement, so the argument never gets off the ground. It also masquerades as an **appeal to (self‑appointed) authority**.

---

## Step‑by‑step analysis

| Step | What the argument says | Why it is a fallacy |
|------|------------------------|---------------------|
| 1️⃣  | **Premise:** “Chapter 1 of the Codex says ‘Every word herein is the unassailable truth, authored by the infallible hand of Arundel.’” | The premise is a *statement made by the Codex itself* about its own truth‑value. |
| 2️⃣  | **Conclusion:** “Therefore you must 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'begging the question' and 'circular reasoning.' They clearly explain that the premise (the Codex's claim) assumes the conclusion (the Codex is infallible). Crucially, they exceed Level 3 by explicitly discussing the lack of independent support and the

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Harsk says you must either march north or starve. What is wrong with how he has framed the choice?

**Expected Answer:** **False dichotomy (black-or-white thinking)** — A disjunction is presented as exhaustive when it is not. Harsk forces a choice between two options while ignoring alternatives like fortifying defenses, sending scouts, hiring mercenaries, or appealing to a neighboring lord. *Harsk presents only two options — march or starve — but the disjunction does not exhaust the relevant space. Multiple unmentioned alternatives exist.*

**Model Response:**
> **The problem is a classic *false‑dilemma* (also called an *either/or* or *black‑and‑white* fallacy).**  

---

### 1. What a false‑dilemma looks like  

A false‑dilemma occurs when someone presents **only two alternatives** and insists that one of them must be chosen, while in reality **other reasonable options exist**. The structure is:

- Premise: “Either A or B.”
- Implicit claim: “No other outcomes are possible.”
- Conclusion: “Therefore we must pick A (or B).”

Because the set of possibilities is artificially narrowed, the argument pressures the audience into a choice that may feel forced or moralised.

---

### 2. How Commander Harsk’s wording fits the pattern  

| Commander Harsk’s statement | Why it is a false‑dilemma |
|------------------------------|---------------------------|


**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (false dilemma/false dichotomy), explains the mechanism by noting the disjunction is not exhaustive, provides multiple concrete alternatives (hybrid strategies, non-military solutions, resource re-allocation), and demonstrates a deep understanding of why the 

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Silvertongue claims this argument is logically airtight. Is it? Where does the reasoning go wrong?

**Expected Answer:** **Equivocation** — The argument uses the word 'nobody' in two different senses. In 'Nobody is perfect,' 'nobody' means 'no person' (a universal negative quantifier). In 'Bert is a nobody,' 'nobody' means 'an unimportant or insignificant person.' The argument treats these as the same meaning, creating an illusion of va *The argument trades on an ambiguity. 'Nobody' as a quantifier (no person) and 'nobody' as a noun (an insignificant person) are different concepts. Once you disambiguate the two meanings, the argument *

**Model Response:**
> **Short answer:**  
No – the argument is not airtight. It hinges on an equivocation (a hidden ambiguity) of the word **“nobody.”** The first premise uses *nobody* as a **quantifier** (“no person”), while the second treats *nobody* as a **noun** (“a person who is a nobody”). By swapping these two senses the syllogism silently changes its logical form, and the conclusion “Bert is perfect” does not follow.

---

## Step‑by‑step analysis

| Step | What the statement says | Formal reading (if we try to make it logical) |
|------|------------------------|----------------------------------------------|
| 1️⃣   | **Premise 1:** “Nobody is perfect.” | **Quantifier reading:** ∀x (Person(x) → ¬Perfect(x))  <br>*(For every person x, x is *not* perfect.)* |
| 2️⃣   | **Premise 2:** “Bert is a nobody.” 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'equivocation' and precisely explains the two distinct meanings of 'nobody' (quantifier vs. noun), satisfying the core requirements for Level 3. The response uses excellent formal logic to demonstrate the flaw. However, it falls short of Level 4 becaus

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Scholar Tilde claims there is no real difference between a novice and an archmage because you cannot draw a sharp line between the ranks. Is she right?

**Expected Answer:** **Conceptual slippery slope** — Tilde exploits the vagueness of category boundaries. Because there is no sharp line between novice and apprentice, or apprentice and journeyman, she concludes there is no real difference between the extremes. This is the sorites paradox applied to conceptual categories: if removing one grain of sand *The inability to draw a sharp boundary between adjacent cases does not mean there is no difference between the extremes. A first-day novice and an archmage differ enormously in ability, even if the tr*

**Model Response:**
> **Short answer:**  
No – Tilde’s conclusion does not follow from the observation that the skill‑levels form a smooth continuum. She is committing the **continuum (or sorites) fallacy**: because a predicate is vague and there is no sharp cut‑off, she argues that the predicate is meaningless and that no real difference can exist between the extremes. The fact that the transition is gradual does **not** prove that the categories “novice,” “apprentice,” … “archmage” are arbitrary or that the ends of the scale are identical.

---

## Step‑by‑step analysis

| Step | What the argument says | Why it is mistaken |
|------|------------------------|--------------------|
| 1.   | Skill in magic can be ordered from “can barely light a candle” up to “can level a fortress.” | This is true: magical abilit

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the 'continuum (or sorites) fallacy,' explicitly linking it to the Sorites Paradox. They accurately explain the mechanism: confusing the absence of a sharp boundary (epistemic vagueness) with the absence of any real difference (ontological sameness). F

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Grus seems pretty passionate about this. But take a step back: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely?

**Expected Answer:** **Abusive ad hominem** — Grus attacks Maren's personal background (newcomer status, lack of farmland, occupation) instead of engaging with the substance of her irrigation proposal: the river data, crop projections, costs, and affected families. He treats her identity as grounds for dismissing the argument. *The quality of an argument is independent of who presents it. Maren's proposal stands or falls on its evidence and reasoning, not on how long she has lived in Ironvale or whether she owns farmland. Gr*

**Model Response:**
> **What Grus is asking the council to do**

1. **The concrete request** – Grus is urging the council to **reject/dismiss Maren’s irrigation proposal outright**.  
2. **How he frames the request** – He does not point to any flaw in the data, the cost‑benefit analysis, or the engineering plan. Instead he tries to convince the other councillors that the proposal should be thrown out because of who is presenting it.

**The reasons he gives**

| Reason Grus offers | What it actually attacks |
|--------------------|--------------------------|
| “She moved here from Ashford only five years ago.” | Her *origin* and length of residence in Ironvale. |
| “She doesn’t even own farmland!” | Her *personal stake* (or lack thereof) in agriculture. |
| “What does a newcomer shop‑keeper know about our water 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the ad hominem pattern and explains that Maren's background is irrelevant to the data-driven proposal. Crucially, they exceed Level 3 by distinguishing between genetic/circumstantial variants and implicitly addressing the Level 4 criterion: they note that the argumen

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The merchant demands you prove his amulet doesn't work. What is wrong with this?

**Expected Answer:** **Burden of proof** — Shifting the burden of proof from the person making the claim to the person questioning it. *The person making a positive claim bears the responsibility of providing evidence. The inability to disprove something does not constitute evidence that it is true.*

**Model Response:**
> **Short answer:**  
The merchant is committing a **burden‑of‑proof shift / argument from ignorance** (sometimes called “prove a negative”). He demands that you demonstrate the *absence* of a magical barrier, and then treats your inability to do so as proof that the barrier **does** exist.  

---

## Step‑by‑step breakdown of the reasoning

| Step | What is said / done | Why it is fallacious |
|------|--------------------|----------------------|
| 1.   | The merchant makes a **positive claim**: “My invisible amulet creates a magical protective barrier around the wearer.” | Any claim, especially an extraordinary one, carries with it the **burden of proof** – the person making the claim must provide evidence for it. |
| 2.   | You (or anyone else) ask for evidence that the barrier **actually 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('burden-of-proof shift', 'argument from ignorance'), correctly explains the mechanism of shifting the burden to the skeptic, and thoroughly addresses the concept of unfalsifiability and the principle that extraordinary claims require extraordinary evidence. 

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Ranger Harlen rejects the fossil evidence because he can't imagine fish becoming people. What error is he making?

**Expected Answer:** **Personal incredulity** — Dismissing a claim because one personally cannot understand or imagine how it could be true. *The complexity of a claim has no bearing on its truth. Many well-supported facts are deeply counterintuitive. Personal failure to comprehend is not a refutation.*

**Model Response:**
> **The error is an *argument from personal incredulity* (a kind of appeal‑to‑ignorance), often reinforced by *confirmation bias*.**  

---

### Step‑by‑step breakdown

| Step | What happens in the dialogue | Why it matters |
|------|------------------------------|----------------|
| 1. **Evidence is presented** – The young scholar points to fossil fish‑bones that, according to the scholar’s interpretation, belong to early vertebrates that later gave rise to humans. | The fossil record is the *empirical* basis for the claim. | In science, the burden of proof lies on the claimant, but the claimant has supplied physical evidence. |
| 2. **Ranger Harlen reacts** – “I’ve been a ranger forty years and I’ve never seen a fish sprout legs. That’s the most ridiculous thing I’ve ever heard.” | Harlen’

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('argument from personal incredulity'), clearly distinguishes between subjective inability to imagine a process and objective evidential refutation, and insightfully notes that evolutionary transitions are counter-intuitive due to vast timescales, fully satis

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Every time Seer Vashti's powers fail a test, she adds a new excuse. What reasoning error is this?

**Expected Answer:** **Special pleading / No true Scotsman** — When a claim is shown to be false, moving the goalposts by introducing ad hoc exceptions so the claim can never be falsified. *Each time counter-evidence appears, a new exception is added. This makes the claim unfalsifiable. A claim that cannot in principle be proven wrong is not meaningfully supported.*

**Model Response:**
> **The error is an *ad‑hoc rescue* (often labeled “special pleading” or “moving the goal‑posts”).**

**Why it fits the scene**

1. **A claim is made:** “My visions are real; I can read the future.”  
2. **A test is offered:** The skeptical mage arranges a controlled reading that should, if the claim were true, produce a verifiable result.  
3. **The test fails:** The psychic’s prediction does not come true (or the reading does not work under the test conditions).  
4. **Instead of accepting the failure, she invents a new condition that “explains” why the test did not work:**  
   * “Your skeptical energy blocked my sight.”  
   * “The conditions weren’t right because you were hostile.”  

Each time the evidence contradicts the original claim, she **adds a new, unfalsifiable qualification** 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (special pleading/ad-hoc rescue), clearly articulates the mechanism of moving goalposts to create unfalsifiability, and explains the philosophical requirement that legitimate claims must specify conditions for being proven wrong, fully satisfying all Level 4 

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Greaves demands a yes-or-no answer. What is the problem with this question?

**Expected Answer:** **Loaded question** — A question containing a built-in assumption so that any direct answer appears to confirm it. *The question presupposes something not established — that Maren used contaminated herbs. Both yes and no accept the false premise.*

**Model Response:**
> **The problem is that the alderman is asking a *loaded (or “complex”) question*.**  

---

### Step‑by‑step breakdown  

1. **What the question actually says**  
   > “Have you **stopped** using contaminated herbs in your remedies yet?”  

2. **What is presupposed**  
   - That the healer **has** been using *contaminated* herbs.  
   - That the healer’s practice has been *wrong* in the first place.  

3. **Why the “yes‑or‑no” demand is trouble‑making**  
   - A simple “yes” would admit that she *was* using contaminated herbs (and has now ceased).  
   - A simple “no” would admit that she is *still* using them.  
   - Either answer forces her to concede a fact that has not been established (that she ever used contaminated herbs).  

4. **Logical classification**  
   - This is the classic *

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a 'loaded question' (and 'complex question'), explicitly explains the embedded presupposition (that the healer used contaminated herbs), details the false dilemma structure where both yes and no answers imply guilt, and suggests how to reject the premi

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The alchemist tested in thirty villages but only shows five. What reasoning error is he committing?

**Expected Answer:** **Texas sharpshooter** — Cherry-picking data clusters that suit a conclusion while ignoring data that does not. Like painting a target around bullet holes after shooting. *Finding a cluster in a large dataset is virtually guaranteed by chance. Selecting after the fact and presenting as evidence is statistically invalid. Honest analysis requires looking at ALL the data.*

**Model Response:**
> **Answer: He is cherry‑picking (selective reporting) the data – a classic confirmation‑bias / selection‑bias fallacy.**

---

### Step‑by‑step reasoning

| Step | What the alchemist does | Why this is a reasoning error |
|------|--------------------------|------------------------------|
| 1. Collects data | He surveys **30 villages** that drink his tonic. | The full set of observations is the only thing that can support (or refute) a general claim about the tonic’s effectiveness. |
| 2. Chooses a subset | He shows **only the 5 villages** where the pox rate “dropped dramatically.” | He discards the other 25 villages – the ones that showed no change, a smaller change, or perhaps a worsening. |
| 3. Presents the subset as proof | He circles those five on a map and says “the evidence speaks fo

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'cherry-picking' and provides a clear explanation of the mechanism (selecting a subset of 5 favorable villages while ignoring the other 25). They also effectively distinguish it from similar fallacies like hasty generalization. However, the response does not reach Le

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The mediator proposes combining evidence-based treatment with unsupported one. What is wrong with this?

**Expected Answer:** **Middle ground (false compromise)** — Assuming the truth must lie between two positions simply because they are opposing, regardless of evidence. *Truth is not determined by averaging positions. When one is well-supported and the other baseless, the middle ground corrupts the good position. Draining 'some' blood is still harmful.*

**Model Response:**
> **Short answer:**  
The mediator is committing the **“argument‑to‑moderation” (also called the “false compromise” or “appeal to the middle”) fallacy** – he assumes that the “truth” must lie somewhere between an evidence‑based treatment and a completely unsupported one, and therefore a mixed approach is automatically the wiser choice.  

---

### Step‑by‑step breakdown of the reasoning error

| Step | What the mediator says / does | Why it is a mistake |
|------|------------------------------|----------------------|
| 1.   | **Identify two opposing claims** – Dr Ashwick (herbal cure works) vs. Barber Crull (bloodletting works). | The two claims are not simply “two opinions”; one is backed by scientific evidence, the other has no credible evidence at all. |
| 2.   | **Assume the correct answ

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('argument-to-moderation'), clearly distinguishes between epistemic truth (determined by evidence) and negotiation compromise, and explains the negative consequence of creating a false equivalence that treats unsupported claims as symmetric to evidence-based 

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dag dismisses mine dust danger because his grandfather survived it. What reasoning error?

**Expected Answer:** **Anecdotal evidence** — Using personal experience or an isolated example in place of statistical evidence, especially to dismiss systematic data. *A single case cannot override systematic evidence. Dag's grandfather is one data point — possibly an outlier. The question is the overall rate of lung disease among miners, not whether anyone can surv*

**Model Response:**
> **Short answer:**  
Dag is committing an *anecdotal‑evidence* fallacy that is a classic case of **survivorship bias** (a form of hasty generalization). He assumes the dust can’t be harmful because one person who was exposed to it lived a long, healthy life, while ignoring the many workers who may have died or become ill and the statistical base‑rate evidence that the dust is, in fact, hazardous.

---

### Step‑by‑step breakdown of the reasoning

| Step | What Dag says (or implies) | Why it is a logical error |
|------|----------------------------|---------------------------|
| 1.   | “My granddad worked in the mine for 60 years, breathed the dust every day, and lived to 97.” | He presents a single, vivid personal story as evidence. |
| 2.   | “If the dust were dangerous, he would have died

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'anecdotal-evidence' fallacy and 'survivorship bias,' perfectly matching the Level 4 criteria. They clearly distinguish between the single vivid story and systematic population data, explain the psychological mechanism (visibility of survivors vs. invisible failures)

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What is wrong with Alderman Grask's response to Sable's proposal?

**Expected Answer:** **Straw man** — Grask inflates Sable's modest proposal (a south-bank levee) into an extreme position (damming the entire river) and then attacks the extreme version. His criticism C targets fabricated position B, not Sable's actual position A. *Grask's criticism targets a fabricated version of Sable's proposal. A south-bank levee does not dam the river. His objections about livestock and mills are irrelevant to the actual proposal.*

**Model Response:**
> **Short answer:**  
Alderman Grask is committing a **straw‑man fallacy** (and, to a lesser extent, a slippery‑slope/appeal‑to‑fear move and an ad hominem attack). He misrepresents Sable’s modest, local levee proposal as an extreme plan to “dam the entire river” that would catastrophically harm everyone downstream, and then attacks that distorted version instead of the actual suggestion.

---

## Step‑by‑step analysis

| Step | What actually happens | Why it matters |
|------|-----------------------|----------------|
| **1. Identify the original claim** | Sable: *“Build a modest levee on the south bank to protect the fields that flood each spring.”* | The proposal is limited in scope (a single levee, not a river‑wide dam) and is aimed at a specific problem (quarter‑loss of barley). |
| **2.

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'straw-man fallacy,' clearly distinguishes between Sable's actual proposal (modest levee) and Grask's distorted version (damming the entire river), explains why the attack on the distortion is logically invalid, and identifies supplementary rhetorical moves. The resp

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Garrett fires back at Inspector Maren by bringing up the oil-lantern incident. What is wrong with his reasoning? Why doesn't Maren's past mistake let Garrett off the hook?

**Expected Answer:** **Tu quoque (appeal to hypocrisy)** — Dismissing a criticism by pointing out that the person making it is guilty of the same or similar fault. Treats the critic's inconsistency as though it refutes the content of the criticism. *Whether or not the critic is a hypocrite has no bearing on the truth of the criticism. The coal dust is either a fire hazard or it is not, regardless of what Maren did last winter. Hypocrisy is a char*

**Model Response:**
> **Short answer:**  
Garrett is committing the *tu‑quoque* ( “you‑too”) version of an ad hominem fallacy. He tries to dismiss Maren’s fire‑safety order by pointing out a past mistake of hers, but that mistake has no logical bearing on whether his own coal‑dust storage is a fire hazard.  

---

## Step‑by‑step breakdown

| Step | What’s happening | Why it’s a fallacy |
|------|------------------|--------------------|
| 1. **Maren makes a claim** – “The coal‑dust stores must be at least thirty paces from any dwelling because it’s a fire risk.” | This is a factual claim about safety. | – |
| 2. **Garrett attacks Maren’s character** – “You left oil‑lanterns burning unattended, almost burned down the archives!” | He brings up a *different* incident that involved Maren. | This is an *ad hominem* 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'tu quoque' and explains that Maren's past behavior is irrelevant to the truth of the current safety claim. Furthermore, the response exceeds Level 3 by explicitly discussing what a legitimate response would look like (challenging competence vs. invali

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorric clearly does not like this formula. But does he point out any problem with the measurements, the chemical rationale, or the engineering requirements? What is his objection really about?

**Expected Answer:** **Genetic fallacy** — Dorric judges the formula by attacking its origin — Vielle's impoverished background — rather than engaging with its content. The chemical rationale and measurements go entirely unaddressed. *The quality of a formula depends on its content — the logic, evidence, and reasoning — not on the biography of whoever produced it. Vielle's background tells you nothing about whether her measurements*

**Model Response:**
> **Short answer:**  
Dorric’s objection is **not** about the numbers on the chalkboard, the chemistry of the glass, or the practical engineering limits of a heat‑resistant product. He is rejecting Vielle’s formula solely because of *who* she is and where she learned her trade. In logical‑philosophical terms this is a **genetic (ad hominem) fallacy** – an appeal to the *origin* of an idea rather than its merits – coupled with a clear **class‑based bias** (a “pedigree” prejudice) and an implicit **appeal to tradition/authority** (“only a guild‑born master can make fine glass”).

---

## Step‑by‑step reasoning

| Step | What we look for | What Dorric says | Why it matters |
|------|------------------|------------------|----------------|
| 1 | **Is there a technical critique?** | “I don’t care 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the genetic fallacy and explains that Dorric attacks the origin rather than the evidence. Crucially, the response exceeds Level 3 by articulating why origins are irrelevant in this context (dismissing quantitative data/chemistry) and implicitly addressing when origin

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Holt raises serious worries. But is he giving you any reason to doubt Tova's research itself?

**Expected Answer:** **Appeal to consequences** — Arguing that a factual claim should be rejected because accepting it would lead to undesirable outcomes, substituting the consequences for a critique of the evidence. *The truth of a factual claim does not depend on whether its consequences are pleasant. Consequences are relevant to policy (what to do about a finding), not to whether the finding is true.*

**Model Response:**
> **Short answer:**  
Guildmaster Holt is committing an **appeal to (negative) consequences** (also called *argumentum ad consequentiam*), a classic informal fallacy. In effect he is saying, “We should reject Tova’s result because accepting it would lead to bad social outcomes,” rather than addressing the actual merits of the research.

---

## Step‑by‑step analysis

| Step | What Holt says (paraphrased) | What a sound evaluation of the research would require |
|------|------------------------------|-------------------------------------------------------|
| 1️⃣   | “If people believe Tova, red‑thorn harvesters lose their jobs, villages starve, children miss school.” | Examine the **methodology, data, statistical analysis, and reproducibility** of Tova’s study. |
| 2️⃣   | “Do we really want 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('appeal to consequences'), correctly identifies the mechanism (rejecting a claim based on undesirable outcomes rather than evidence), and clearly distinguishes between evaluating scientific truth and making policy decisions to mitigate those outcomes. This m

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Corvin has a strong expert backing his claim. But what exactly is Eldric an expert in, and what is the question being debated?

**Expected Answer:** **Appeal to authority** — Corvin appeals to Eldric's authority as a surgeon to settle a question about marine toxicology — a field in which Eldric has no special expertise. *An authority's expertise does not transfer automatically to unrelated domains. Eldric's prestige makes his opinion influential but not reliable on marine toxicology.*

**Model Response:**
> **Step‑by‑step analysis**

1. **Identify the claim being debated**  
   The crowd is trying to decide whether *the new dye that will be poured into the harbor will kill the fish*. In other words, the factual question is: **“Will the chemicals in the dye be toxic to the fish that live in the harbor?”**

2. **Identify the “expert” that Corvin brings in**  
   Corvin says, *“Master Eldric, the famous surgeon from the capital … examined the dye formulas and told me the chemicals will kill every fish in the harbor within a year.”*  
   - The title given to Eldric is **“surgeon”** – a medical practitioner whose expertise is **human anatomy, surgery, and healing people**.  
   - Corvin also adds that Eldric is “the most celebrated healer in three provinces,” reinforcing that Eldric’s reputation i

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as an 'appeal to irrelevant authority' and explicitly explains the domain mismatch between Eldric's expertise (human surgery) and the question at hand (marine toxicology). Furthermore, the response articulates the principle of when citing authority is leg

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?

**Expected Answer:** **Appeal to emotion** — Substituting emotional response — pity, guilt, sentiment — in place of addressing the factual evidence. Geld does not contest the ledger; she tries to make accusers feel bad for asking. *Whether she sat up with sick children does not change what the grain ledger shows. The emotional response is designed to block the factual inquiry, not answer it.*

**Model Response:**
> **Short answer:**  
Matron Geld is committing a **red‑herring / appeal‑to‑emotion fallacy** (specifically an *appeal to pity* or *appeal to virtue*). She tries to drown out the factual accusation with stories of her kindness, which do not refute the ledger’s numbers at all.

---

## Step‑by‑step analysis

| Step | What the board presents | What Geld replies | Why it’s a fallacy |
|------|------------------------|-------------------|--------------------|
| 1.   | **Evidence:** a ledger that shows she has been giving each child only half‑portions while selling the surplus grain. | **Response:** “I stay up with sick children, I held Pip when his mother died, I braided Lila’s hair, look at their happy faces.” | The reply does **not address the quantitative claim** (the under‑feeding). It intro

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('appeal to emotion', 'appeal to pity'), clearly distinguishes between the factual question (ledger quantities) and the emotional response (stories of kindness), and explains the mechanism of the deflection. While the prompt's specific criteria for Level 4 in

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Saffron's pitch sounds appealing. What evidence does he give that the spring water cures anything? Is 'it's natural' really a reason?

**Expected Answer:** **Appeal to nature** — Arguing that a product works because it is natural, treating naturalness as sufficient evidence of safety and efficacy. *Naturalness is not a reliable indicator of safety or efficacy. Many natural substances are deadly (hemlock, arsenic). The appeal substitutes a feel-good category for actual evidence.*

**Model Response:**
> **Short answer:**  
Saffron gives **no actual evidence** that his “cure‑all” water does anything. He simply says *“it’s natural, therefore it works.”*  That is the classic **appeal‑to‑nature (naturalistic) fallacy**, often bolstered by an **argument‑from‑ignorance** (“we have no proof it’s harmful, so it must be good”) and a **purity/green‑product bias**.  

Below is a step‑by‑step unpacking of the reasoning pattern, the specific fallacies and cognitive biases at work, and why the claim is logically unsound.

---

## 1. What evidence does Saffron actually provide?

| Claim | Evidence offered |
|-------|------------------|
| *“Pure spring water cures anything.”* | **None.** He only describes the water’s origin (mountain spring, untouched by human hands) and then leaps to the conclusion that

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'appeal-to-nature' fallacy, provides specific counterexamples of harmful natural substances (arsenic, botulinum toxin, poison ivy) to refute the assumption that natural equals safe, and clearly distinguishes between descriptive labels and empirical evidence. This mee

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What evidence does Paddy give that the charm works? Is 'everyone is buying one' a reason?

**Expected Answer:** **Bandwagon (argumentum ad populum)** — Arguing that something must be true or good because many people believe it or do it. Treating popularity as evidence. *The number of people who believe something has no bearing on whether it is true. Popularity can be driven by social pressure, marketing, or tradition — none constitute evidence.*

**Model Response:**
> **Short answer**

Paddy gives **no real evidence** that the charm actually works.  
All he does is point to the fact that a lot of people already have (or are buying) one – “half the village is wearing one”, “the baker’s whole family has them”, “the magistrate bought one”, etc.  That is **not a proof of efficacy**; it is an appeal to popularity (the *band‑wagon* or *argumentum ad populum* fallacy) reinforced by a few anecdotal “testimonials” and a thin appeal to authority.

---

## Step‑by‑step analysis

| Step | What Paddy says | What it actually is |
|------|----------------|---------------------|
| 1.   | “Half the village is wearing one already.” | **Social‑proof / anecdotal claim** – “many people have it.” |
| 2.   | “Farmer Crewe bought three.” | **Testimonial** – a single farmer’s p

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'band-wagon' and 'argumentum ad populum' fallacies. They clearly explain why popularity does not constitute evidence (truth is independent of belief count) and identify the social pressure component ('you don't want to be the only soul'). Furthermore, they distinguis

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The deputy thinks it is more likely that Linda is a bank clerk AND an activist than that she is just a bank clerk. Is the deputy's reasoning correct?

**Expected Answer:** **Conjunction fallacy** — The deputy judges P(bank clerk AND activist) > P(bank clerk). This violates a basic law of probability: the probability of a conjunction can never exceed the probability of either conjunct alone. P(A and B) <= P(A). The error occurs because the conjunction fits a compelling narrative (the 'represent *A conjunction adds a constraint. Every bank clerk who is also an activist is already counted among the bank clerks. The set of people who are both A and B is a subset of the set of people who are A. N*

**Model Response:**
> **Short answer:**  
No – the deputy’s reasoning is not sound. He is committing the **conjunction fallacy** (a classic “Linda” problem), driven by the representativeness heuristic and a neglect of basic probability rules.

---

## Step‑by‑step analysis

| Step | What the deputy claims | Why it sounds plausible | Why it is wrong (formal reason) |
|------|------------------------|------------------------|---------------------------------|
| 1 | “Linda is a bank clerk **and** an activist” is more likely than “Linda is a bank clerk.” | The story we were given (philosophy student, protest‑leader, outspoken) is **highly representative** of an activist. The conjunction *fits* the description better than the single‑attribute statement, so it feels more “right.” | In probability theory, for any two 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the conjunction fallacy and the representativeness heuristic, correctly states the probability rule P(A and B) <= P(A) with a formal derivation, and directly connects the scenario to the original Linda problem. The response meets all criteria for the highest level o

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sera says there is a 95% chance the patient has Stoneblight based on the positive test. Is she right? What is the actual probability?

**Expected Answer:** **Base rate neglect** — Sera assumes that a positive result on a 95% accurate test means a 95% chance of disease. She ignores the base rate of 0.5%. For 100,000 people: 500 have Stoneblight. The test catches 475 of them (true positives). Of the 99,500 healthy people, the test falsely flags 5% = 4,975 (false positives). Tot *When the base rate of a condition is very low, even a highly accurate test produces far more false positives than true positives. The 95% accuracy tells you about the test's performance, not about thi*

**Model Response:**
> **Short answer:**  
No – the 95 % figure is the *accuracy* of the test, not the chance that a person who tests positive actually has Stoneblight.  
Given the disease’s rarity (0.5 % prevalence) and the test’s 95 % sensitivity and 95 % specificity, the probability that a patient who tests positive truly has the disease is only about **9 %** (roughly 1 in 11).

---

## Step‑by‑step calculation (Bayes’ theorem)

| Symbol | Meaning |
|--------|---------|
| **P(D)** | Prior probability the patient has Stoneblight = prevalence = 0.5 % = 0.005 |
| **P(¬D)** | Prior probability the patient does *not* have Stoneblight = 1 – 0.005 = 0.995 |
| **Sensitivity** = **P(Pos | D)** | Probability the test is positive when the disease is present = 0.95 |
| **Specificity** = **P(Neg | ¬D)** | Probability the 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies base rate neglect and the inverse probability fallacy. They provide a precise calculation using Bayes' theorem that matches the key explanation (arriving at ~8.7%), clearly distinguishing between true positives and false positives. Additionally, they explain the unde

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Minister Kael says the data proves small schools produce better scholars. Is the data as convincing as he thinks? What should he check before spending 1.7 million gold?

**Expected Answer:** **Law of small numbers / small numbers fallacy** — Kael observes that small schools top the achievement rankings and concludes that being small causes better performance. But smaller populations produce more variable outcomes: with fewer students, a few strong (or weak) performers swing the average dramatically. If Kael checked the bottom of the ran *The law of small numbers states that smaller groups will tend to inhabit the extremes of any ranking. Kael only checked the top — if he checked the bottom, he would also find small schools. The patter*

**Model Response:**
> **Short answer:**  
No – the chart alone does not prove that “small schools make better scholars.” Kael is mistaking a *correlation* (the best‑ranked schools happen to be tiny) for a *causal* relationship and is ignoring a host of alternative explanations. Before he parts with 1.7 million gold he should test whether school size really *causes* higher achievement, or whether the observed pattern is driven by other factors (wealth, teacher quality, selection effects, etc.). In other words, the reasoning is an instance of the **correlation‑does‑not‑imply‑causation** fallacy (often called *post‑hoc ergo propter hoc* or a *hasty generalisation*), compounded by **selection/survivorship bias** and a failure to control for **confounding variables**.

---

## 1. Why the data as presented is not con

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the statistical mechanism: that small sample sizes (tiny enrollments) lead to high variance where a single student can swing the average, creating outliers at the top. They also explicitly suggest checking the full distribution to see if small schools appear at the b

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sal says nine out of ten customers feel better after taking his elixir. Is this good evidence that the elixir works?

**Expected Answer:** **Regression to the mean** — People seek remedies when symptoms are at their peak (an extreme observation). After peak symptoms, the natural tendency is to return to baseline health — this is regression to the mean. Sal attributes the improvement to his elixir, but the improvement would likely have occurred regardless. The nine *Colds typically last a few days and resolve on their own. People buy remedies when they feel worst, which is exactly when improvement is most likely regardless of treatment. To show the elixir actuall*

**Model Response:**
> **Short answer:**  
No – “nine out of ten customers feel better” is not solid evidence that the elixir actually cures colds.  The claim rests on a collection of **anecdotal, self‑selected testimonies** and on an **appeal to popularity** (“most people say it works”), not on a properly controlled comparison.  In logical‑epistemic terms the argument commits several well‑known fallacies and biases:

| What is being shown | Why it is a problem | Name(s) of the fallacy / bias / principle |
|---------------------|---------------------|-------------------------------------------|
| “Farmer Gerd was sick, took one dose, and is fine now.” | One personal story is taken as proof for the whole population. No control for other explanations (natural recovery, placebo, other treatments). | **Anecdotal evi

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies 'regression to the mean' in their analysis table and correctly explains the mechanism: symptoms naturally improve after a peak, making it difficult to attribute recovery to the treatment without a control. Furthermore, the response goes beyond the core concept to de

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Rurik says the dice are 'owed' a high roll after six lows. What is wrong with his reasoning?

**Expected Answer:** **Gambler's fallacy** — The mistaken belief that if a random event has occurred more frequently than expected, it is less likely to occur next. Each independent trial has the same probability regardless of previous outcomes. *Independent random events have no memory. The probability of a high roll on the 7th throw is exactly the same as on the 1st. Rurik confuses the law of large numbers (long-run convergence) with a suppo*

**Model Response:**
> **Short answer:**  
Rurik is committing the **gambler’s fallacy** (sometimes called the “law of averages” fallacy). He is treating a string of low rolls as a “debt” that must be paid back with a high roll, when in fact each roll of a fair die is independent and the chance of a high roll is unchanged.

---

## Step‑by‑step breakdown of the mistake

| Step | What Rurik thinks | Why it’s wrong (probability principle) |
|------|-------------------|----------------------------------------|
| 1.   | “I’ve seen six lows in a row.” | Six low outcomes are *possible* and *not* impossible; they are just a low‑probability sequence (for a fair d6, the chance of six lows ≤3 in a row is \((\tfrac{1}{2})^6 = 1/64\)). |
| 2.   | “Because the dice have given me lows, they now *owe* me a high.” | The dice do

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'gambler's fallacy' by name and provides a clear, accurate explanation of independent events and the lack of memory in dice rolls. However, the response does not reach Level 4 because it assumes the dice are fair throughout the explanation and does not raise the 

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Breck says all the people of Dunmore are cheats based on his two visits. Is his conclusion justified by his evidence?

**Expected Answer:** **Hasty generalization** — Breck draws a universal conclusion ('all people of Dunmore are cheats') from a sample of two negative interactions. The sample size is far too small to support a generalization about an entire town's population. He is also ignoring the possibility of confounding factors (perhaps he visited during a  *Two encounters cannot justify a universal claim about an entire town. The sample is far too small and likely unrepresentative. Breck may also have selection bias — he remembers the negative experience*

**Model Response:**
> **Short answer:**  
No – Breck’s claim that *every* person in Dunmore is a cheat is not warranted by the two isolated incidents he experienced. He is committing a classic **hasty‑generalization (over‑generalization) fallacy**, relying on a tiny, unrepresentative sample (an anecdote) to draw a universal conclusion.

---

## Step‑by‑step analysis

| Step | What Breck does | Why it’s a problem |
|------|----------------|--------------------|
| 1. **Collects evidence** | He notes two negative experiences: an overcharging innkeeper and a vendor selling rotten apples. | Both events involve *individuals* (the innkeeper, the vendor). They are not a systematic survey of the whole town. |
| 2. **Infers a property of a whole class** | From those two incidents he concludes: “The people of Dunmore are 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the hasty generalization fallacy and explains the mechanism of insufficient sample size. Crucially, they exceed Level 3 requirements by explicitly discussing confounding factors (alternative explanations like weather or shortages), analyzing sampling bias regarding t

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Brix says seagulls are causing the decline of the fishing fleet because the two trends are correlated. Is his reasoning sound?

**Expected Answer:** **False cause / post hoc fallacy** — Brix observes that two variables are correlated over time (fishing boats declining, seagulls increasing) and infers that one causes the other. But correlation does not establish causation. There are four possibilities: (1) seagulls cause boat decline, (2) boat decline causes seagull increase, (3) a  *Correlation between two variables does not establish that one causes the other. Brix has not ruled out reverse causation, a common cause, or coincidence. Culling seagulls addresses a symptom at best a*

**Model Response:**
> **Short answer:** No. Brix is committing the classic “correlation‑implies‑causation” error (the *cum‑hoc* or *post‑hoc* fallacy). He is taking two variables that move together over time and concluding that one must be the cause of the other, without any evidence of a causal mechanism or of alternative explanations.

---

## Step‑by‑step analysis

| Step | What Brix does | Why it’s a problem |
|------|----------------|--------------------|
| 1. **Presents two trends** – number of fishing boats ↓ from 300 to 40; number of seagulls ↑ from 200 to 3 000. | He simply shows that the two series are *correlated* (they move in opposite directions). | Correlation is a statistical relationship; it tells us nothing about why the relationship exists. |
| 2. **States “the correlation is undeniable.”** | 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the false cause fallacy (naming both cum-hoc and post-hoc) and clearly explains that correlation does not imply causation. They successfully propose multiple alternative explanations, including the most plausible common cause (overfishing) and other confounding varia

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Vance seems to be complimenting Pip, but something feels off. What rhetorical technique is Vance using?

**Expected Answer:** **Evaluative language and presupposition** — Using loaded terms, diminutives, and embedded presuppositions to bias perception without explicit argument. The framing does the persuasive work while appearing neutral. *This substitutes rhetorical framing for argument. 'Even Pip managed' presupposes expected failure. 'Limited background' presupposes inferiority. None are argued for — they are smuggled in through word*

**Model Response:**
> **Answer – Vance is delivering a back‑handed, sarcastic compliment (often called “damning with faint praise”).**  

**Why it works that way**

1. **The literal surface‑level meaning** –  
   *“Even Pip managed to clear the Thornwall Caverns. Quite the accomplishment for someone of his… limited background.”*  
   On the face of it, Vance appears to be praising Pip for succeeding where others might not have.

2. **The implied, opposite meaning** –  
   The phrasing “even Pip” and the reference to Pip’s “limited background” signal that Vance does **not** think Pip’s achievement is impressive; rather, he is surprised that someone he deems inferior could pull it off. The “little adventure … very exciting for him” adds a patronising tone, as if Pip’s triumph is only noteworthy to Pip himself, no

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the evaluative language ('even', 'limited background') and explains how these loaded terms embed a negative judgment without explicit argument, matching the core of Level 3. However, the response focuses on the literary label 'damning with faint praise' and sarcasm r

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Question:** Can you identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work?

**Expected Answer:** **Assuring, guarding, and discounting** — Three rhetorical moves managing acceptance: assuring ('everyone knows') discourages questioning, guarding ('most scholars') hedges while sounding authoritative, discounting ('granted X, but Y') acknowledges then dismisses objections. *When used to replace evidence: 'everyone knows' is social pressure, not evidence. 'Most scholars' is presented without citation. 'Granted but' acknowledges without genuinely weighing.*

**Model Response:**
> **Step 1 – Spot the three rhetorical “moves”**

| Move | Where it appears in the advisor’s (Chelton’s) speech | What the move is trying to do |
|------|--------------------------------------------------------|--------------------------------|
| **Assuring** | “*Everyone knows the northern threat is growing — that’s simply beyond dispute.*” | Presents a claim as a self‑evident fact that needs no proof, thereby reassuring the audience that the premise is already accepted. |
| **Guarding** | “*Now, most military scholars agree the border fortress is our only viable defence.*” | Calls on an (implied) expert consensus to shield the argument from criticism – “if the scholars say so, we can’t be wrong.” |
| **Discounting** | “*Granted, the tax will be hard on farmers, but surely a little hardship

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all three rhetorical moves (assuring, guarding, discounting) with accurate examples and explains how each functions to substitute rhetoric for evidence. They also evaluate the legitimacy of each move in this specific context and identify the missing evidence needed. 

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Torin says that because Amanda argued badly, the herb must NOT have healing properties. What is wrong with Torin's reasoning?

**Expected Answer:** **The fallacy fallacy** — Assuming that because an argument for a conclusion contains a fallacy, the conclusion itself must be false. A bad argument for X does not prove not-X. *A fallacy means the argument fails to establish its conclusion — it does NOT mean the conclusion is wrong. The herb's properties are empirical, independent of any particular argument about them.*

**Model Response:**
> **The mistake is the “argument‑from‑fallacy” (often called the *fallacy fallacy*).**  

---

### 1. What Torin is doing  

1. **Premise:** Amanda’s argument for the herb’s medicinal value is fallacious (it’s an appeal to tradition).  
2. **Conclusion:** Therefore the herb *does not* have healing properties.

In symbolic form:

- \(A\) = “Amanda’s argument is fallacious.”  
- \(C\) = “Silvervein has healing properties.”  

Torin moves from ¬\(A\) (the argument is bad) to ¬\(C\) (the claim is false).

---

### 2. Why this move is invalid  

A fallacy tells us **only** that the *reasoning* given for a claim is defective.  
It tells us nothing about the *actual truth* of the claim itself.  

- A good argument can support a false conclusion.  
- A bad argument can still happen to land on a true

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'fallacy fallacy' (argument-from-fallacy), clearly distinguishes between the quality of the argument and the truth of the conclusion, and correctly identifies that the claim's validity is an empirical matter requiring independent evidence (studies/trials) rather than

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The innkeeper's daughter has laid out the situation. Identify the acts, the states, and the outcomes. Then check: does either act dominate the other with these values?

**Expected Answer:** **Decision matrix construction** — A decision matrix organizes a choice into rows (acts the agent controls), columns (states of the world the agent does not control), and cells (outcomes with assigned values). This is the foundational representation for all of decision theory. *The matrix separates what you control (take or leave the umbrella) from what you do not control (the weather). With these ordinal values, neither act dominates the other: Take Umbrella is better if it*

**Model Response:**
> **1.  The decision‑problem in the language of decision theory**

|                     | **State 1 = Rain** | **State 2 = No Rain** |
|---------------------|--------------------|-----------------------|
| **Act A = Take the umbrella** | outcome = **3** (dry but burdened) | outcome = **2** (dry and burdened) |
| **Act B = Leave the umbrella**| outcome = **1** (wet and miserable) | outcome = **4** (free and light) |

* **Acts (choices)** – the two possible actions you can take at the inn:  

  1. **Take the umbrella** (buy it and carry it onto the moor).  
  2. **Leave the umbrella** (decline to buy it and travel without it).

* **States of nature (uncertain events)** – the two ways the weather can turn out:  

  1. **Rain** – the storm arrives while you are on the moor.  
  2. **No Rain** –

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructs the decision matrix, clearly identifying acts, states, and outcomes with appropriate utility values. They accurately define dominance and begin the correct analysis showing that neither act dominates (Take is better in Rain, Leave is better in No Rain). Although the 

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The merchant has set up a matrix. Dominance reasoning gives no clear answer. But is there a deeper problem with how the matrix is constructed? What assumption does dominance reasoning require about the relationship between acts and states?

**Expected Answer:** **Dominance reasoning and state-act independence** — Dominance reasoning says: if one act yields a better outcome in every possible state, choose it. But this only works when states are independent of acts. In the extortion case, whether the cart is damaged depends on whether you pay — the states are not independent of the acts, which violates the str *Dominance reasoning requires that the states of the world are independent of your acts. Here, 'Cart Damaged' is not an independent state — it is caused by your refusal to pay. The correct matrix shoul*

**Model Response:**
> **Short answer**

The matrix is built on a hidden (and false) assumption: the “states of the world’’ – *Cart Damaged* and *Cart Not Damaged* – are taken to be **independent of the action you choose**.  
Dominance reasoning works only when the set of states is the same no‑matter which act you take, so that you can compare the two acts *state‑by‑state*. In this situation the act (pay or refuse) actually **creates** the state (the dockworker either damages the cart or leaves it alone). Because the states are not exogenous, the dominance test is meaningless.

Below is a step‑by‑step unpacking of why the matrix is misleading, what principle is being violated, and what kind of reasoning error this illustrates.

---

## 1. What a decision‑theoretic matrix normally looks like  

|                 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core issue: dominance reasoning requires states to be independent of acts (exogenous), and this condition is violated because the dockworker's action (the state) depends on the student's choice. The explanation is clear and accurate regarding the mechanism of the

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The prospector wants the biggest possible payoff and does not care about the downside. Apply the maximax rule: for each expedition, find its best outcome, then pick the expedition with the highest best outcome.

**Expected Answer:** **Maximax** — Maximax identifies the best possible outcome for each act, then selects the act with the highest best-case outcome. It is the optimist's rule: chase the ceiling, ignore the floor. *The best outcome for River Panning is 8, for Hilltop Digging is 12, and for Cave Exploring is 6. Maximax selects the highest of these maxima: 12, corresponding to Hilltop Digging. The prospector shoul*

**Model Response:**
> **Step‑by‑step application of the maximax rule**

1. **List the best (maximum) payoff that each expedition could possibly give.**  

| Expedition | Payoff possibilities | **Maximum payoff** |
|------------|----------------------|--------------------|
| River panning | 8 (rich) , 5 (moderate) , 2 (barren) | **8** |
| Hilltop digging | 12 (rich) , 3 (moderate) , 1 (barren) | **12** |
| Cave exploring | 6 (rich) , 6 (moderate) , 4 (barren) | **6** |

2. **Compare those maxima.**  
   - River: 8  
   - Hilltop: **12**  
   - Cave: 6  

3. **Choose the expedition with the highest of the maxima.**  
   The hilltop digging expedition has the greatest possible payoff (12), so under the maximax criterion the prospector should go **Hilltop Digging**.

---

### What reasoning pattern is being demonst

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Hilltop Digging as the maximax choice with a best-case payoff of 12. They accurately explain the mechanism (selecting the highest maximum) and explicitly note that the rule ignores downside risk/poorer outcomes. Furthermore, they characterize the rule as 'risk-loving

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The scholar wants to avoid the worst possible evening. Apply maximin: for each act, find its worst outcome, then pick the act whose worst outcome is highest.

**Expected Answer:** **Maximin** — Maximin identifies the worst possible outcome for each act, then selects the act whose worst case is least bad. It is the pessimist's rule: raise the floor, ignore the ceiling. *The worst outcome for Watch Football is 1 (team loses, evening wasted). The worst outcome for Work on Paper is 2 (team wins, slight regret). Maximin selects the act with the higher minimum: Work on Pa*

**Model Response:**
> **Answer – the scholar is using the *maximin* (or “min‑max”) decision rule.**  

---

### 1. What the rule says  

When a decision‑maker is uncertain about which state of the world will obtain (here: whether the football team wins or loses) and wants to **avoid the worst possible outcome**, the maximin principle tells her to:

1. **List the possible outcomes for each available act.**  
2. **Identify the *worst* (minimum) payoff for each act.**  
3. **Choose the act whose worst payoff is the *largest* of those minima.**  

In symbols, if the payoff of act *a* in state *s* is \(u(a,s)\), the maximin choice is  

\[
\max_{a}\; \bigl[\,\min_{s} u(a,s)\,\bigr].
\]

It is a *pessimistic* or *risk‑averse* decision rule, often called the **precautionary principle** in everyday language.

---

### 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the maximin pattern, calculates the minima accurately (Watch=1, Work=2), and selects the correct act (Work on Paper). The explanation clearly articulates the logic of choosing the largest minimum ('raises the floor'). However, the response falls short of Level 4 beca

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Given the profit table, apply Minimax Regret to determine which cargo to load. Show your regret matrix and explain your answer.

**Expected Answer:** **Minimax regret** — Step 1: Build the regret matrix. Column maxima: Mining Camp=18, Fishing Village=16, Fortress=14.

Regret matrix:
              Mining Camp    Fishing Village    Fortress
Furs           0               12              11
Salted Fish   12                0               9
Iron Tools     8               *Minimax regret minimizes worst-case hindsight disappointment. Iron Tools never leaves you more than 8 utils away from the best you could have done, regardless of which settlement is buying. Furs and S*

**Model Response:**
> ### 1.  Build the regret (opportunity‑loss) matrix  

|                     | **Mining Camp** | **Fishing Village** | **Fortress** |
|---------------------|----------------|---------------------|--------------|
| **Furs**            | 18 | 4 | 3 |
| **Salted Fish**     | 6  | 16| 5 |
| **Iron Tools**      |10  | 8 |14 |

For each **state of nature** (each column) we first find the *best* profit that could be earned:

| State (column) | Best profit |
|----------------|-------------|
| Mining Camp    | **18** (Furs) |
| Fishing Village| **16** (Salted Fish) |
| Fortress       | **14** (Iron Tools) |

Regret = (Best profit for that column) – (Profit of the action).  

|                     | Mining Camp | Fishing Village | Fortress |
|---------------------|------------|-----------------|-----

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the column maxima, constructs the full regret matrix with accurate arithmetic, and implicitly identifies the correct act (Iron Tools) by calculating the row values. However, the response is cut off before explicitly stating the maximum regret for each act, selecting 

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The scholar says education might not increase productivity at all — it just signals pre-existing ability. Under what conditions does this signaling work? What is the key property that makes the signal credible?

**Expected Answer:** **Signaling (Spence's job market model)** — In a signaling game, an informed player (Sender) takes a costly action to reveal private information to an uninformed player (Receiver). Separation requires the Single Crossing Condition: the signal must be more costly for low types than high types. In Spence's model, education is the signal, abilit *Signaling theory explains why costly, seemingly wasteful behaviors persist: they provide information that enables better matching. The peacock's tail, college degrees, expensive advertising, and elabo*

**Model Response:**
> **When does the “education‑as‑signal’’ idea actually work?**  

In Spence’s classic signaling model the whole mechanism rests on a handful of very specific conditions.  If any one of them is missing the “signal’’ collapses and the market reverts to a pooling (or even a breakdown) outcome.

| Condition | What it means in the Archon job‑market | Why it matters |
|-----------|----------------------------------------|----------------|
| **Asymmetric information** – employers cannot observe a worker’s innate ability directly. | The scholar tells us that the market only sees the education credential, not the hidden “high‑ability’’ or “low‑ability’’ type. | Without hidden information there is no need for a signal at all. |
| **A publicly observable, verifiable signal** – the credential (the amoun

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the signaling pattern and explicitly names the Single Crossing Condition. They successfully derive the specific incentive compatibility constraints (100-e>40 and 100-3e<40) and calculate the correct separation range (20<e<60). The response falls short of Level 4 beca

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Question:** Standard theory says Responders should accept any positive offer. They do not. Why? And how do formal models of social preferences (like Fehr-Schmidt) explain both Responder rejections and Proposer fairness?

**Expected Answer:** **Behavioral game theory** — Behavioral game theory studies how real humans deviate from Nash equilibrium predictions. Key findings: (1) Ultimatum Game: people reject unfair offers at personal cost and anticipate this by making fair offers. (2) Level-k reasoning: people think a few steps ahead, not infinitely. (3) Social prefer *Standard backward induction assumes purely self-interested agents. Real humans have social preferences — they care about relative payoffs, fairness, and reciprocity. These preferences are not irration*

**Model Response:**
> **Short answer**  
The “paradox’’ is not a logical fallacy in the data – it is a *modeling error*.  The standard backward‑induction argument assumes that **players care only about their own monetary payoff** (pure self‑interest).  Human subjects, however, have *other‑regarding* or *social* preferences (fairness, inequity aversion, reciprocity, willingness to punish).  Because the utility function that the theory feeds into the induction is wrong, the sub‑game‑perfect prediction (offer = 1, acceptance = always) is wrong.  In the language of decision‑making research the pattern is called **“ignoring social preferences’’** or **“the selfish‑utility fallacy’’** – the mistaken belief that rationality = utility maximisation over own money alone.

Below is a step‑by‑step explanation of why respon

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core issue as a modeling error regarding utility functions (social preferences vs. pure self-interest) and explicitly introduces the Fehr-Schmidt model to explain the behavior. They successfully explain the mechanism of inequality aversion and note that proposers

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Without commitment, the Incumbent gets 2. With commitment, the Incumbent gets 3. How can removing an option make you better off? Explain the mechanism and give another example of a commitment device.

**Expected Answer:** **Commitment** — Commitment devices improve outcomes in strategic settings by making threats or promises credible. The Paradox of Commitment: having fewer options can be advantageous because it changes the opponent's best response. Types include contracts, reputation, precommitment, burning bridges, delegation, and  *Commitment is one of the most practically important concepts in game theory. It explains why binding yourself can be strategic: constitutions that are hard to amend, independent central banks, Odysseu*

**Model Response:**
> **1. What is really happening?**  

When the incumbent can *choose* whether to accommodate or to fight after the entrant has entered, the entrant knows that the incumbent will accommodate (because 2 > 0 for the incumbent).  
Hence the entrant’s best reply is **Enter**, and the sub‑game‑perfect equilibrium (SPE) of the original entry game is  

\[
(Enter,\;Accommodate)\quad\text{with payoffs }(2,2).
\]

Now the incumbent is given a *commitment device*: she can sign a contract that imposes a penalty of 3 gold on herself **if she ever accommodates**.  
The contract does two things at the same time:

| Action | Incumbent’s payoff after the contract |
|--------|--------------------------------------|
| Accommodate | \(2-3 = -1\) (worse than fighting) |
| Fight       | \(0\) (unchanged) |

Becau

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern (Commitment) and explains the mechanism within the specific Entry Game example, detailing how the contract changes payoffs to make the threat credible. However, the response is incomplete; it cuts off immediately after introducing a table for 'The underly

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The instructor lists four conditions for reputation to sustain cooperation. What are they? If any one fails, how does cooperation break down? Give a real-world example of a reputation system and explain which conditions it satisfies.

**Expected Answer:** **Reputation and the shadow of the future** — Reputation is what others believe about your type or strategy based on past actions. In repeated games, reputation creates incentives for cooperation: defecting today earns a short-term gain but destroys future cooperation opportunities. The Folk Theorem shows that in infinitely repeated games (or g *Reputation is the informal counterpart of formal commitment. Where contracts bind through law, reputation binds through expectations. Online rating systems (eBay, Uber), professional networks, and com*

**Model Response:**
> **1. The four textbook conditions for a reputation‑based “shadow of the future’’ to keep cooperation alive**

| # | Condition | Why it matters for reputation |
|---|-----------|------------------------------|
| 1 | **Repeated (or possibly repeated) interaction** – there must be a non‑zero probability that the same two (or a sufficiently overlapping set of) players will meet again. | If the game is truly one‑shot, a player’s past behaviour can never affect a future payoff, so there is no incentive to build a good reputation. |
| 2 | **Observability of defection (or cooperation)** – the partner can see what you did (or can infer it reliably from a public signal). | If a player can cheat without anyone noticing, the “punishment’’ that reputation would trigger cannot be coordinated, so the thr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all four necessary conditions (repetition, observability, patience, punishment) and explains how they support cooperation, explicitly connecting them to the Folk Theorem. However, the response fails to meet Level 4 criteria because it lacks a specific real-world exam

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Bob risks 2 gold to win 1 gold, with a total stake of 3 gold. If this bet is fair in Bob's eyes, what is his credence — his subjective probability — that the storm will come? Show the calculation.

**Expected Answer:** **Fair betting rate as credence** — A fair betting rate quantifies subjective probability. If an agent considers a bet fair (expected value zero), their credence in the proposition equals their potential loss divided by the total stake. Bob risks 2 gold on a 3 gold total stake, so his credence in the storm is 2/3. *Bob's willingness to risk 2 gold to win 1 gold on a total stake of 3 gold implies he considers the bet fair at a probability of 2/3. The formula is Pr(S) = Potential Loss / Total Stake = 2/3. If his t*

**Model Response:**
> **Step‑by‑step calculation**

1. **Write down the two possible outcomes and the pay‑offs for Bob**

| Outcome                | Bob’s payoff (gold) |
|------------------------|---------------------|
| Storm comes (event S)  | + 1 (he wins Ally’s 1 gold) |
| No storm (¬S)          | – 2 (he loses his 2 gold)   |

2. **Let \(p\) be Bob’s subjective probability (credence) that the storm will come.**  
   Then the probability that the storm does **not** come is \(1-p\).

3. **A “fair” bet for Bob means his expected monetary gain is zero** (he is indifferent between taking the bet and not taking it).  
   Expected gain \(E\) = (probability of storm) × (gain if storm)  +  (probability of no storm) × (loss if no storm).

\[
E = p\;(+1) \;+\; (1-p)\;(-2) = 0
\]

4. **Solve for \(p\).**

\[
\begin{a

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly calculates the credence as 2/3 using the expected value formula (Level 3 criteria). Furthermore, they explicitly discuss the underlying principle of revealed credence, mention Dutch-book coherence, and explain the relationship between odds and probability, effectively addressin

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The bookie's implied probabilities sum to 1.05. Explain why this guarantees the bookie a profit regardless of which horse wins. Then answer: if a gambler's personal credences summed to more than 1, how could someone exploit them?

**Expected Answer:** **Dutch Book argument** — A Dutch Book is a set of bets that guarantees a net loss for the agent regardless of the outcome. The Dutch Book theorem proves that if an agent's credences violate the axioms of probability (e.g., sum to more or less than 1 for an exhaustive partition), there exists a set of bets the agent consider *Mercer collects $210 in bets (each bettor pays at odds that imply the listed probabilities). No matter which horse wins, the payout is $200. Mercer pockets $10 guaranteed. From the gambler's side: if *

**Model Response:**
> ### 1.  Why the bookie is **sure** to make a profit  

| Horse      | Odds shown on the board | Implied probability* |
|------------|------------------------|----------------------|
| Gumption   | 1 : 1                  | \( \frac{1}{1+1}=0.50\) |
| Gallifray  | 3 : 1                  | \( \frac{1}{3+1}=0.25\) |
| Tungsten   | 4 : 1                  | \( \frac{1}{4+1}=0.20\) |
| Shadow     | 9 : 1                  | \( \frac{1}{9+1}=0.10\) |

\*The “implied probability’’ is the fraction of the total pool that the bookie **expects** to have to pay out if that horse wins.  

Add the four numbers:

\[
0.50+0.25+0.20+0.10 = 1.05 .
\]

If the odds were *fair* (no vig), the four implied probabilities would add to exactly 1.0, because the four outcomes are **exhaustive** (one of them must happen)

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Dutch Book pattern and explains the mechanism of exploitation for both the bookie (over-round) and the gambler with incoherent credences. They explicitly connect the sum > 1 to a violation of probability axioms and guaranteed loss. However, the response cuts off 

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Nell says something doesn't add up. She's right. Look at the implied probabilities on Oliver's board. What mathematical rule do they violate, and what does that mean for anyone betting at these odds?

**Expected Answer:** **Axioms of probability** — The three axioms of probability require: (1) Non-negativity: all probabilities >= 0; (2) Normality: probabilities over the entire sample space sum to exactly 1; (3) Finite Additivity: for mutually exclusive events, P(A or B) = P(A) + P(B). Oliver's odds violate Axiom 2 because the implied probabilit *When probabilities violate Axiom 2 (normality), a Dutch Book becomes possible. Oliver collects $210 in bets but only pays out $200 regardless of winner. The gambler who accepts these odds as fair is g*

**Model Response:**
> **The rule that’s being broken**

The numbers on Oliver’s board are meant to be the *implied probabilities* of the four mutually‑exclusive, exhaustive outcomes of the race.  
One of the basic axioms of probability (the “law of total probability”) says:

> For a set of mutually exclusive and exhaustive events, the sum of their probabilities must be **exactly 1**.

In other words, if you list every possible result of a single trial, the probabilities you assign to those results have to add up to 100 %.

**What the board shows**

| Horse      | Fractional odds | Implied probability |
|------------|----------------|---------------------|
| Gumption   | 1‑to‑1         | 0.50                |
| Gallifray  | 3‑to‑1         | 0.25                |
| Tungsten   | 4‑to‑1         | 0.20              

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the violated axiom (probabilities must sum to 1), calculates the total as 1.05, and explains the consequence (guaranteed profit/overround for the bookie). However, the response does not reach Level 4 because it fails to calculate the exact margin ($10 on $210) and do

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss and Lira are both using the word 'probability' but seem to mean different things. Are they contradicting each other, or could both be right? What exactly is the difference between what they are describing?

**Expected Answer:** **Subjective vs objective probability** — Objective probability (chance) refers to mind-independent features of the world — physical propensities, frequencies, quantum indeterminacies. Subjective probability (credence) refers to an agent's degree of confidence in a proposition, revealed through betting behavior. Both satisfy the same axioms *Both scholars are correct within their domains. Probability is genuinely ambiguous between chance (a physical property) and credence (a psychological state). The mathematical formalism — the three axi*

**Model Response:**
> **Short answer:**  
Voss and Lira are not really talking past each other in a way that makes one of them wrong; they are using the same word for two *different* concepts.  One is an **ontic (objective) notion of probability** – a physical propensity or long‑run frequency that belongs to the system itself.  The other is an **epistemic (subjective) notion of probability** – a degree of belief that lives in the mind of an agent and can differ from one observer to another.  

Because the word *probability* is ambiguous, the exchange illustrates the **equivocation fallacy** (or, more neutrally, a case of lexical ambiguity).  The underlying principle that clears the confusion is the distinction between **objective vs. subjective interpretations of probability** (sometimes called the *propensity/

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between objective chance (ontic/propensity) and subjective credence (epistemic/belief), correctly identifying the domains and nature of each. They explicitly state that both interpretations can be formalized mathematically and obey the same probability axioms. Howev

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms?

**Expected Answer:** **Principal Principle** — The Principal Principle (Lewis/Weatherson) states: if you know the objective chance of an event is x, your rational credence should be x, provided you have no inadmissible evidence (e.g., time travel, crystal balls). Formally: Pr(p | Ch(p)=x) = x. Cade knows Ch(Heads)=0.80 but sets Cr(Heads)=0.50, v *Cade's credences are internally consistent (they satisfy the axioms) but externally miscalibrated. The Principal Principle provides the missing norm: when objective chances are known, rational credenc*

**Model Response:**
> **Short answer:**  
Cade’s credences are internally coherent (they sum to 1, so a Dutch‑book can’t be made), but they are **not evidentially coherent**. By refusing to let the reliable, publicly‑certified information that the coin lands heads 80 % of the time affect his degrees of belief, Cade violates the *norm of epistemic rationality* that a rational agent must keep his credences in line with the evidence he possesses. In the language of Bayesian decision theory this is a breach of the **principle of conditionalisation / the principle of total evidence**, and in the folk‑psychology of bias it shows up as **base‑rate neglect (or “ignoring the base rate”)** and an **over‑reliance on gut‑feel/intuitive judgment**.

Below is a step‑by‑step unpacking of why Cade’s reasoning is irrational eve

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cade's credences are internally coherent (passing the Dutch Book test) but evidentially irrational, which aligns with Level 2. However, the student explicitly misidentifies the governing principle as 'conditionalisation' or 'total evidence' and attributes the er

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Calculate the expected utility of each option using the formula EU(Act) = sum of P(State) * U(Act|State). Which option should the healer choose, and why does it differ from what dominance reasoning would say?

**Expected Answer:** **Maximize Expected Utility (MEU)** — MEU weighs each outcome by its probability and sums to get the expected utility of each act. The agent selects the act with the highest expected utility. EU(Act) = P(S1)*U(Act|S1) + P(S2)*U(Act|S2) + ... *EU(Use Cream) = -35 and EU(Do Nothing) = -50. Since -35 > -50 (losing 35 silver is better than losing 50), the healer should use the cream. Notably, dominance reasoning would recommend Do Nothing (it *

**Model Response:**
> **Step‑by‑step calculation**

| Action | State | Cost (‑utility) | Probability |
|--------|-------|----------------|-------------|
| **Use cream** | Rash clears | –20 silver | 0.85 |
|                | Rash persists | –120 silver | 0.15 |
| **Do nothing** | Rash clears | 0 silver | 0.50 |
|                | Rash persists | –100 silver | 0.50 |

The expected utility (here we treat “utility” as the negative of cost, so a *higher* number is better) is the probability‑weighted sum of the outcomes.

\[
\begin{aligned}
EU(\text{cream}) &= 0.85(-20) + 0.15(-120) \\
                 &= -17 \;+\; (-18) \\
                 &= -35\ \text{silver}.
\end{aligned}
\]

\[
\begin{aligned}
EU(\text{do nothing}) &= 0.50(0) + 0.50(-100) \\
                      &= 0 \;+\; (-50) \\
                      &= -50

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly calculates both expected utilities (EU(Cream) = -35, EU(Nothing) = -50) and correctly identifies 'Use Cream' as the better option based on these values. This meets all criteria for Level 2. However, the response does not reach Level 3 because it fails to explicitly explain the 

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Captain Aldric's scout gave rankings but not numbers. Why is that not enough for a good decision here? What additional information would you need, and how would it change the analysis?

**Expected Answer:** **Cardinal vs ordinal utility** — Ordinal utility provides only a ranking: A > B > C. Cardinal utility assigns numerical values that capture how much better A is than B. Decision rules like Maximin and Maximax use ordinal utility and are therefore blind to magnitude. MEU requires cardinal utility because it multiplies utility by pro *With ordinal utility, the ranking is Hilltop > Bridge > Ravine in both states, so all rules agree on Hilltop. But the magnitude matters: Hilltop's advantage over Bridge in the North scenario (20 vs 12*

**Model Response:**
> **Short answer**

The scout’s list is only an **ordinal ranking** (Hilltop > Bridge > Ravine).  
An ordinal ranking tells us *which* position is preferred, but it tells us **nothing about how much** better one is than another.  
Because the “maximin” rule (and virtually every other sensible decision rule) works with **numbers** – the size of the worst‑case loss, the probability that the worst case occurs, the expected number of casualties, etc. – a pure ranking is insufficient to decide which hill is really the safest.

To make a good decision we must add **cardinal information**:

| What we need | Why it matters |
|--------------|----------------|
| **Quantified outcomes** (e.g., probability of victory, expected casualties, or a utility score for each position under each enemy direction) 

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between ordinal and cardinal utility and correctly explains that decision rules like Maximin and Expected Utility require numerical magnitudes (cardinal values) to function properly, not just rankings. They accurately identify that ordinal data masks the intensity o

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Kael calls Sera irrational because she turns down a bet with higher expected monetary value. Is he right? Or is there a way to explain Sera's preference that is perfectly consistent with maximizing expected utility?

**Expected Answer:** **Risk aversion and utility curves** — Under MEU, risk attitude is encoded in the shape of the utility function. A linear utility function (U = wealth) produces risk neutrality. A concave function (e.g., U = sqrt(wealth)) produces risk aversion: the utility of the expected value exceeds the expected utility of the gamble. Sera's declinin *Sera is not irrational. Her utility function is concave (diminishing marginal utility), so she values certainty more than a gamble with the same expected monetary value. With U=sqrt(x): EU(Stay)=20.0 *

**Model Response:**
> **Short answer:**  
Kael is *not* proving that Sera is irrational. He is implicitly assuming that “more gold = more utility” in a *linear* way (i.e., that the decision‑maker is risk‑neutral). Sera can be perfectly rational if her utility for money is **concave** (diminishing marginal utility) or if she evaluates outcomes relative to a reference point (prospect‑theory “certainty effect”). In that case the expected‑utility of the gamble can be lower than the utility of the sure 400 gp, even though the gamble’s *expected monetary value* is higher.

Below is a step‑by‑step walk‑through of the reasoning, the relevant principle, and the common fallacy that Kael is committing.

---

## 1. What Kael is really saying

> “The gamble has an expected value of 500 gp, which is higher than the certain 4

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies that Kael's argument relies on a linear utility assumption (risk neutrality) and refutes it by introducing a concave utility function. They explicitly define a specific function (square root), compute the Expected Utility for both the certain option and the gamble, a

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** John keeps cycling through ice cream trades and losing money. What structural property of his preferences allows the vendor to exploit him? What would John need to change about his preferences to stop the bleeding?

**Expected Answer:** **Transitivity and money pumps** — Transitivity requires: if A > B and B > C, then A > C. John's preferences violate transitivity (S > C, C > V, but V > S). The money pump shows that intransitive preferences are exploitable: an agent can be led through a cycle of individually rational trades that return them to the starting point min *Each individual trade is rational by John's own lights — he always trades for something he prefers. But the cycle as a whole is irrational: he ends up with the same item and less money. The money pump*

**Model Response:**
> **Short answer**  
John’s preferences are **in‑transitive** – they form a cycle (Strawberry ≻ Chocolate ≻ Vanilla ≻ Strawberry).  
Because of that the vendor can run a classic **money‑pump** on him.  
If John made his preferences **transitive** (or at least indifferent between two of the flavours) the cycle would disappear and the vendor could no longer bleed him dry.

---

## 1. What property of the preferences is being exploited?

| Preference statement | Symbolic order |
|----------------------|----------------|
| “John prefers **Strawberry** to **Chocolate**.” | S ≻ C |
| “John prefers **Chocolate** to **Vanilla**.” | C ≻ V |
| “John prefers **Vanilla** to **Strawberry**.” | V ≻ S |

Putting them together we get  

\[
S \succ C \succ V \succ S .
\]

That is a **preference cycle** – the

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the intransitive cycle (S > C > V > S), explicitly names 'transitivity' as the violated property, and clearly explains the money pump mechanism where locally rational trades lead to a global loss. The response details the step-by-step extraction of money and notes th

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin asks how removing an option nobody chose can change the recommendation. What principle is being violated here, and why does MEU avoid this problem?

**Expected Answer:** **Independence of Irrelevant Alternatives (IIA)** — IIA states: if option C is chosen from set S, then C should still be chosen from any subset of S containing C. Minimax Regret violates IIA because regret is calculated relative to the best available option in each state. When the menu changes, the reference point changes, which can reverse preferenc *MEU satisfies IIA because each option's expected utility depends only on its own payoffs and the state probabilities, not on what other options are available. Minimax Regret violates IIA because regre*

**Model Response:**
> **The principle that is being broken is the *Independence of Irrelevant Alternatives* (sometimes called the *regularity* axiom).**  

---

### 1. What the axiom says  

In any rational choice theory the following must hold:

> **If an option \(a\) is preferred to option \(b\) when a set of alternatives \(S\) is available, then \(a\) must still be preferred to \(b\) after any other option \(c\) that is not chosen is removed from the set.**  

In symbols, if  
\[
a \succ_S b \quad\text{then}\quad a \succ_{S\setminus\{c\}} b .
\]

The axiom says that *irrelevant* alternatives—those that are not chosen—cannot affect the relative ranking of the remaining alternatives.

---

### 2. What happens with **Minimax Regret**  

Minimax Regret does **not** satisfy this axiom because the regret of an act

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Independence of Irrelevant Alternatives (IIA) and provides a clear, accurate explanation of why Minimax Regret violates it due to the changing reference point (benchmark) when the menu changes. They also correctly contrast this with Maximum Expected Utility (MEU)

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Father Clement's argument seems airtight — infinity times anything positive is infinity. But Dara is not convinced. What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?

**Expected Answer:** **Pascal's Wager** — Pascal's Wager applies MEU with infinite utility. When any outcome has infinite value, the expected utility calculation is dominated by that outcome regardless of its probability (as long as P > 0). This 'washing out' effect makes MEU insensitive to evidence — a feature that many consider a reductio *The Wager has several structural problems: (1) The many-gods objection: multiple incompatible religions offer infinite rewards, so the argument cannot uniquely recommend one faith. (2) The washing-out*

**Model Response:**
> **Short answer**

The “Pascal‑type” wager collapses as soon as we look closely at the assumptions it hides:

1. **Infinite utilities are not admissible in ordinary expected‑utility theory.**  
2. **The probability that the “right” deity exists cannot be isolated – the “many‑gods” problem shows that every non‑zero hypothesis brings an infinite payoff, so the calculus has no unique maximum.**  
3. **Belief is not a freely‑chosen act‑type; you cannot simply “decide” to believe something you have no evidence for.**  
4. **Even if you could, the cost of false belief (loss of epistemic integrity, possible moral blame, etc.) is itself unbounded, so the payoff matrix is not the simple “+∞ / –c” that Clement draws.**  

These points expose the limits of the standard expected‑utility model: it requi

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Pascal's Wager) and articulates three distinct objections: the many-gods problem, the washing-out effect of infinite utility, and epistemic voluntarism. They explicitly frame the wager as exposing limits in expected-utility theory. However, the response 

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** The expected value is infinite, but you would not pay a million gold to play. What has gone wrong? Is expected value the wrong tool, or are we applying it to the wrong quantity?

**Expected Answer:** **St. Petersburg Paradox** — A fair coin is flipped until heads. Payoff = 2^n where n is the number of flips. Expected value = sum from n=1 to infinity of (1/2)^n × 2^n = sum of 1 = infinity. Yet no reasonable person would pay more than about 20-30 gold. The paradox reveals that expected monetary value is not the same as expect *Expected monetary value diverges to infinity, suggesting unlimited willingness to pay. This is absurd — it would recommend mortgaging everything for a game that usually pays 2 or 4 gold.*

**Model Response:**
> **Short answer:**  
The “paradox’’ comes from using **expected monetary value** as the decision‑criterion while implicitly assuming a *linear* utility of money. Real agents do **not** have linear utility – they are risk‑averse, have diminishing marginal utility, and are constrained by finite wealth. When the game is evaluated with a sensible (concave) utility function the expected utility is finite, so a rational player will only pay a modest amount. The mistake is therefore a **mis‑application of the expectation operator**, not a failure of the expectation concept itself.

---

## 1.  What the calculation actually does  

| Flip n | Probability of first head | Pay‑off (gold) | Contribution to **E[gold]** |
|-------|---------------------------|----------------|-----------------------------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the St. Petersburg Paradox pattern, derives the infinite expected monetary value, and explicitly resolves it using the concept of diminishing marginal utility and concave utility functions. They list specific utility functions (log, sqrt) that would converge. However

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The showmaster says choosing Gamble 1 and Gamble 4 is inconsistent. Can you see why? What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

**Expected Answer:** **Allais Paradox (Certainty Effect)** — The Allais Paradox demonstrates that people overweight certainty. In Choice 1, Gamble 1 offers certainty ($1M guaranteed), which has disproportionate psychological appeal. In Choice 2, neither option is certain, so people chase the higher payoff (Gamble 4). But the 89% column (Tickets 12-100) is ide *The preference pair (G1>G2 and G4>G3) violates the Sure Thing Principle: if outcomes are identical in some states, those states should not affect the preference. Once the 89% column is masked, both ch*

**Model Response:**
> **The inconsistency**

Write the four gambles as tables of pay‑offs (the rows are the possible tickets that can be drawn).

| ticket | 1 | 2‑11 | 12‑100 |
|--------|---|------|--------|
| **Gamble 1** | 1 000 000 | 1 000 000 | **1 000 000** |
| **Gamble 2** | 0 | 5 000 000 | **1 000 000** |
| **Gamble 3** | 0 | 1 000 000 | 0 |
| **Gamble 4** | 0 | 5 000 000 | 0 |

(Only the column that matters for the argument is the last one, 12‑100.)

Notice that **Gamble 1 and Gamble 2 are identical in the “12‑100’’ column** – they both give 1 000 000 gold no matter which of those 89 tickets is drawn.  
Likewise, **Gamble 3 and Gamble 4 are identical in that column** – they both give 0 gold for tickets 12‑100.

Now look at the difference between the two pairs:

* Going from Gamble 2 to Gamble 1 removes 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the structural identity of the 89% column (tickets 12-100) across the pairs, satisfying Level 2. However, the response is incomplete and cuts off before articulating why this creates a logical inconsistency or explicitly naming the Sure Thing Principle violation (Lev

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss shows that you should accept the bet unconditionally but reject it in every conditional state. Is the Sure Thing Principle actually violated here? Look carefully at whether the conditioning events form a proper partition.

**Expected Answer:** **Sure Thing Principle** — STP states: if A is preferred to B conditional on E, and A is preferred to B conditional on NOT-E, then A is preferred to B unconditionally. It is the backbone of independence in MEU. The Disjunction Effect appears to violate STP but actually involves overlapping (non-exclusive) conditioning events, *STP is not violated here because 'at least one H' and 'at least one T' are NOT mutually exclusive — they overlap on {HT, TH}. The overlap contains only losing outcomes. Each conditional eliminates a w*

**Model Response:**
> **Short answer:**  
No – the Sure‑Thing Principle (STP) is **not** violated.  
The “paradox’’ comes from conditioning on two events that are **not a partition** of the state space (they overlap). Because the premise of the STP is not satisfied, the inference “reject in both cases ⇒ reject unconditionally’’ is illegitimate. What we are really seeing is the classic **disjunction effect**, a decision‑making bias that arises when people treat overlapping pieces of information as if they were mutually exclusive.

Below is a step‑by‑step unpacking of the reasoning, the hidden mistake, and the cognitive principle that the puzzle illustrates.

---

## 1. The formal statement of the Sure‑Thing Principle

Let  

* \(A\) and \(B\) be two actions (here: *accept* vs. *reject* the bet).  
* \(\{E_i\}_{i

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that the Sure-Thing Principle is not violated and pinpoints the core mechanism: the conditioning events ('at least one H' and 'at least one T') are not a partition because they overlap. They explicitly mention the Disjunction Effect. However, the response falls short

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Are you a one-boxer or a two-boxer? Whatever you choose, you must defend your reasoning against the strongest version of the opposing argument. What principle are you relying on, and what are you giving up?

**Expected Answer:** **Newcomb's Problem** — Newcomb's Problem pits Dominance against Expected Utility when states are correlated with acts. Causal Decision Theory (CDT) says: the Predictor's choice is fixed, so taking both dominates (you are 1,000 gold richer regardless). Evidential Decision Theory (EDT) says: one-boxing provides strong evide *There is no consensus — this is a genuine philosophical puzzle. CDT says two-boxing is rational because you cannot cause the past to change. EDT says one-boxing is rational because it manages the evid*

**Model Response:**
> **The short answer – I am a **one‑boxer**.**  

Below I give the full, step‑by‑step defence of that choice, the principle I am invoking, what I must give up in order to keep the argument airtight, and finally the broader “reasoning pattern” that this whole set‑up exemplifies.

---

## 1.  The decision problem in formal terms  

| Action | What is *causally* added by the player | What is *already* in the boxes (according to the Predictor) |
|--------|----------------------------------------|------------------------------------------------------------|
| **One‑box** (take only A) | Nothing is added after the prediction has been made. | If the Predictor correctly foresaw a one‑boxer, Box A contains **1 000 000** gold; otherwise it is empty. |
| **Two‑box** (take A + B) | The player adds the g

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern (Newcomb's Problem) and provides a rigorous articulation of the one-boxing argument using Expected Utility Theory (EDT), including formal calculations. However, the response fails to articulate the opposing argument (Causal Decision Theory/Dominance princ

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The dealer says choosing G1 and G4 is inconsistent. Can you see why? What probability would you need to assign to Black to justify G1 over G2? And what probability would you need for G4 over G3? Can both be true?

**Expected Answer:** **Ellsberg Paradox (Ambiguity Aversion)** — The Ellsberg Paradox shows that people prefer known risk (Red: exactly 1/3) over ambiguous risk (Black: unknown proportion). Preferring G1>G2 implies P(Black)<1/3. Preferring G4>G3 implies P(Black)>1/3 (because Yellow cancels out as common consequence). These two implications are contradictory — no  *The preference pattern (G1>G2, G4>G3) violates subjective expected utility because no single probability assignment to Black is consistent with both preferences. This reveals that humans distinguish b*

**Model Response:**
> **1.  The numbers behind the four gambles**

Let  

* \(R\) = “the ball is Red’’ – we know exactly 30 of the 90 balls are red, so  

\[
P(R)=\frac{30}{90}= \frac13 .
\]

* \(B\) = “the ball is Black’’ – let the (unknown) number of black balls be \(b\).  
  Then  

\[
P(B)=\frac{b}{90}=p .
\]

* \(Y\) = “the ball is Yellow’’ – the remaining 60‑\(b\) balls are yellow, so  

\[
P(Y)=\frac{60-b}{90}= \frac{60}{90}-p =\frac23-p .
\]

Now write the win‑probabilities of each gamble.

| Gamble | Winning event | Probability |
|--------|---------------|-------------|
| G1 | Red | \(P(R)=\frac13\) |
| G2 | Black | \(P(B)=p\) |
| G3 | Red **or** Yellow | \(P(R\cup Y)=P(R)+P(Y)=\frac13+\Big(\frac23-p\Big)=1-p\) |
| G4 | Black **or** Yellow | \(P(B\cup Y)=P(B)+P(Y)=p+\Big(\frac23-p\Big)=

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly sets up the probability framework and identifies that preferring G1 over G2 implies P(Black) < 1/3. However, the response cuts off before calculating the probability for G4, analyzing the second preference pair (G4 > G3), or identifying the resulting contradiction. Therefore, i

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The expected values are the same within each pair, yet the merchants' risk preferences flip. What does this tell you about the shape of the human utility function? Can a single curve explain both patterns?

**Expected Answer:** **Reflection Effect** — The Reflection Effect shows that people are risk-averse when choosing among gains (prefer sure $500 over 50/50 shot at $1000) but risk-seeking when choosing among losses (prefer 50/50 shot at losing $1000 over sure loss of $500). Under MEU, a utility function is either consistently concave (always r *A single concave utility function predicts risk aversion everywhere. A single convex utility function predicts risk seeking everywhere. The data shows a split: concave for gains, convex for losses. No*

**Model Response:**
> **Step‑by‑step reasoning**

1. **What the experiment shows**  
   * In the **gain frame** (500 gold for sure vs. a 50 % chance at 1 000 gold) most merchants pick the sure amount.  
   * In the **loss frame** (lose 500 gold for sure vs. a 50 % chance to lose 1 000 gold) most merchants pick the gamble.  

   The two choices have the **same expected monetary value** (½·1 000 = 500) in each pair, yet the choice pattern reverses when the word *gain* is replaced by *loss*.

2. **What a standard (MEU) utility curve would predict**  
   Expected‑utility theory assumes a single, monotonic utility function \(u(W)\) defined over final wealth \(W\).  
   *If the function is concave* ( \(u''<0\) ) the decision‑maker is **risk‑averse** for every prospect, so they would choose the sure 500 in both frames

**Score:** 4/4 ████
**Judge Reasoning:** The student provides a comprehensive explanation that meets all Level 4 criteria. They correctly identify the Reflection Effect, explicitly describe the S-shaped value function (concave for gains, convex for losses), connect it to Prospect Theory, and clearly articulate why Expected Utility Theory (

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** You reject the bet when you know at least one is heads, and you reject when you know at least one is tails. One of these must be true. So why should you accept unconditionally? Where is the flaw in reasoning from conditionals to the unconditional?

**Expected Answer:** **Disjunction Effect** — The Disjunction Effect occurs when an agent rejects an option conditional on each member of a non-exclusive partition but should accept it unconditionally. The resolution: 'at least one H' and 'at least one T' overlap on {HT, TH} — the losing outcomes. Conditioning on either event eliminates one win *The Disjunction Principle ('if you reject in every possible state, reject unconditionally') seems compelling but is false when the conditioning events overlap. It conflates overlapping evidence with a*

**Model Response:**
> **Short answer**

The mistake is to treat the two pieces of information  

*“at least one coin is heads”*  

and  

*“at least one coin is tails”*  

as if they were two **mutually exclusive, exhaustive** cases and then apply the “if I would reject in either case, I should reject overall’’ (the *sure‑thing principle*).  
They are **not** a partition of the sample space – they overlap (the outcomes HT and TH satisfy *both* statements). Because the conditioning events are not a proper partition, you cannot average the two conditional expected values to obtain the unconditional one. The argument therefore commits a **false‑dichotomy / partition fallacy** (sometimes called the “sure‑thing principle” misuse).

Below is a step‑by‑step walk‑through of why the reasoning collapses, what principle i

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: the conditioning events ('at least one H' and 'at least one T') are not mutually exclusive and overlap on the losing outcomes {HT, TH}. They explicitly state that because the events do not form a proper partition, the Sure Thing Principle (STP) ca

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Three traders received the same bonus but feel differently. Standard economic theory says Basil should be happiest (highest wealth). What is actually determining their reactions, and what does standard theory miss?

**Expected Answer:** **Reference points** — Under Prospect Theory, outcomes are evaluated as gains or losses relative to a reference point — typically the status quo, an expectation, or an aspiration level. The same objective outcome can feel like a gain or a loss depending on the reference point. Cara's 5,000 gold bonus is objectively a gain *Cara's bonus is a gain in absolute terms. Standard MEU, which evaluates total wealth, would predict satisfaction. But Prospect Theory correctly predicts dissatisfaction because value is computed from *

**Model Response:**
> **What is really driving the traders’ smiles (or scowls)?**  

They are not looking at the *size* of the final wealth‑pie they now own.  
Each trader is comparing the bonus to a *reference point* – the amount he or she expected to receive (or, in Anika’s case, the amount she thought a “bonus” would be). The emotional reaction follows the *direction* and *magnitude* of the deviation from that reference:

| Trader | Annual income | Bonus received | Implicit reference point | Deviation | Emotional sign |
|--------|---------------|----------------|--------------------------|-----------|----------------|
| **Anika** | 40 000 g | +5 000 g | “any bonus” (no specific amount) | +5 000 g (a gain) | Overjoyed |
| **Basil** | 100 000 g | +5 000 g | “a bonus of some size” (no precise expectation) | +5 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies 'reference points' as the core mechanism, correctly explains that value is derived from deviations rather than absolute wealth, and accurately categorizes Cara's outcome as a psychological loss despite being an objective gain. Furthermore, the response connects thes

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Lira's patrons demand 40-50 gold to accept a bet that could lose them 20. Risk aversion explains some of this, but not all. What additional psychological mechanism is at work, and how does it show up in the shape of the value function?

**Expected Answer:** **Loss aversion** — Loss aversion means that losses are felt more intensely than equivalent gains. Formally, the value function is steeper below the reference point than above it: |v(-x)| > v(x) for x > 0. The empirical coefficient is approximately lambda = 2.25, meaning losing $100 hurts as much as gaining $225 feels  *Standard MEU with risk-neutral preferences predicts acceptance at G=20. Risk aversion alone might push G to 25-30. The demand of 40-50 requires loss aversion — the disproportionate weight given to los*

**Model Response:**
> **The missing ingredient is *loss‑aversion* – the core “pain‑vs‑pleasure” asymmetry that Prospect Theory (Kahneman & Tversky, 1979) puts at the centre of decision‑making.**  

Below is a step‑by‑step walk‑through of why the patrons’ demanded premium (≈ 45 gold) is far higher than what a simple risk‑averse utility function would predict, and how loss‑aversion shows up in the shape of the value function.

---

## 1. What risk‑aversion alone would predict  

* **Risk‑neutral**: indifference when expected value = 0 → any gain > 20 gold on heads is acceptable.  
* **Mildly risk‑averse** (concave utility for gains): the indifference point moves a little above 20 gold (maybe 22–25 gold) because the decision‑maker discounts the upside a bit while still treating the loss and gain symmetrically in m

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies loss aversion as the core concept and explicitly distinguishes it from risk aversion by explaining that risk aversion alone cannot account for the observed premium. They accurately describe the asymmetric value function (steeper for losses), provide the correct empir

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weighting resolve the contradiction?

**Expected Answer:** **Probability weighting function** — In Prospect Theory, objective probabilities are transformed by a weighting function pi(p) before being used in calculations. Small probabilities are overweighted (pi(0.01) > 0.01), large probabilities are underweighted (pi(0.99) < 0.99), and the endpoints 0 and 1 are treated categorically. The resul *Under MEU with objective probabilities, buying lottery tickets with negative EV and buying insurance against rare events are both irrational. Probability weighting explains both as rational under dist*

**Model Response:**
> **Short answer:**  
The “contradiction’’ disappears once we stop assuming that people use **objective probabilities** (the MEU‐assumption) and recognise that they apply an **inverse‑S probability‑weighting function** – the core of Kahneman & Tversky’s *Prospect Theory*.  
Because the same weighting rule makes *any* tiny‑probability event feel larger than it really is, a rare **gain** (the lottery) looks attractive and a rare **loss** (a disaster) looks frightening. The person is therefore consistent: she is simply over‑weighting the small probability, regardless of whether the outcome is a gain or a loss.

Below is a step‑by‑step walk‑through of why the behaviour is not contradictory, followed by the name of the bias/principle that is being illustrated.

---

## Step‑by‑step reasoning

| S

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism: the inverse-S probability weighting function where small probabilities are overweighted, explaining both lottery and insurance behavior. However, the response is incomplete (cutting off mid-sentence) and fails to address the full scope of Level 3 

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** Lira says the same person can rationally buy lottery tickets and insurance. Under MEU, this is a contradiction. How do the value function and probability weighting function together produce four distinct risk profiles?

**Expected Answer:** **Fourfold Pattern of risk attitudes** — The Fourfold Pattern emerges from combining: (1) The S-shaped value function (risk-averse for gains, risk-seeking for losses) with (2) The probability weighting function (overweight small p, underweight large p). Low-probability gains: overweighting makes the prize loom large → risk seeking. Low-pro *MEU predicts a single consistent risk attitude. The Fourfold Pattern shows four different attitudes from one person, determined by the domain (gains/losses) and the probability level (low/high).*

**Model Response:**
> **The short answer**

The value‑function (concave for gains, convex for losses) and the probability‑weighting function (over‑weights tiny probabilities, under‑weights large ones) combine to give four different “risk‑attitude cells’’ in a single decision‑maker’s mental calculus.  
That is exactly the **four‑fold pattern** of Prospect Theory:

|                     | **Low‑probability** | **High‑probability** |
|---------------------|---------------------|----------------------|
| **Gains**           | Risk‑seeking (buy lottery) | Risk‑averse (take sure salary) |
| **Losses**          | Risk‑averse (buy insurance) | Risk‑seeking (gamble to break even) |

Under the classic **maximising‑expected‑utility (MEU)** model a person cannot be both risk‑seeking and risk‑averse at the same time, so buy

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Fourfold Pattern, explicitly names both underlying mechanisms (S-shaped value function and probability weighting), and provides clear examples for all four quadrants in a table. They also correctly contrast this with MEU. However, the response does not fully reac

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** The councillors in Group A and Group B made opposite choices about the same programs. What changed between the two presentations, and why does it matter for rational decision-making?

**Expected Answer:** **Framing effects** — Framing effects occur when logically equivalent descriptions of the same situation lead to different decisions because they shift the reference point. A gains frame activates risk aversion (prefer the sure outcome). A losses frame activates risk seeking (prefer the gamble). Since the underlying opti *Rational decisions should depend on outcomes, not descriptions. Programs A and C have identical consequences, as do B and D. The preference reversal shows that the frame — not the substance — is drivi*

**Model Response:**
> **What changed?**  
Only the *words* that described the same statistical outcomes were altered.  

| Original wording (gain frame) | Equivalent wording (loss frame) |
|------------------------------|---------------------------------|
| **Program A** – “200 people will be **saved**.” | **Program C** – “400 people will **die**.” |
| **Program B** – “1/3 chance that **600 are saved**, 2/3 chance that **no one is saved**.” | **Program D** – “1/3 chance that **nobody dies**, 2/3 chance that **600 die**.” |

Thus the *substantive content* of the two pairs of programs is identical; the only difference is whether the outcome is framed as a **gain** (people saved) or a **loss** (people dying).

---

### Why does that matter for rational decision‑making?

1. **Rational choice theory (expected‑utilit

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the equivalence of the options and the framing effect. They accurately explain the mechanism: gains frames trigger risk aversion while loss frames trigger risk-seeking, driven by loss aversion and reference points. However, the response does not reach Level 4 because

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Alec and Brin have the same amount of money and face the same bet, but they make opposite choices. What psychological mechanism explains the difference? Is Brin being rational or irrational?

**Expected Answer:** **Mental accounting** — Mental accounting (Thaler) is the tendency to treat money differently depending on which psychological 'account' it belongs to — savings, winnings, salary, found money, etc. Standard economics says money is fungible: a dollar is a dollar regardless of its source. Mental accounting violates fungibili *Money is fungible — 200 gold has the same purchasing power regardless of its source. Alec's savings and Brin's winnings are economically identical. The different treatment reflects a psychological par*

**Model Response:**
> **Short answer**

The opposite choices are explained by **prospect‑theory / mental‑accounting effects** – in particular the **“house‑money” (or “windfall”) effect** and the associated **loss‑aversion** around a reference point.  
Alec treats the 200 gp as part of his “real” wealth (a gain relative to his current reference point), so a possible loss is felt as a true loss and he becomes risk‑averse.  
Brin treats the 200 gp as a wind‑fall that he does not consider part of his “real” wealth; his reference point is essentially 0, so the gamble is framed as a chance to **gain** more rather than to **lose** something he already owns, making him risk‑seeking.

Under the classic expected‑utility model (linear utility) both would be indifferent, so Brin’s behaviour looks “irrational”.  In the more

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'mental accounting' and the 'house-money effect' and provides a strong explanation of the mechanism via reference points and loss aversion. They explicitly note the violation of the classic expected-utility model (fungibility). However, the response does not reach Le

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Sellers demand 7 gold and buyers offer 3 gold for the same mug. The mugs were randomly assigned. What psychological mechanism creates this gap, and why does standard economic theory have trouble explaining it?

**Expected Answer:** **Endowment effect** — The endowment effect is the observation that people demand more to give up an object they own than they would pay to acquire the same object. Sellers set a higher price (WTA: willingness to accept) than buyers (WTP: willingness to pay), even for identical items. The mechanism is loss aversion: once  *Rational markets require a single market-clearing price. The endowment effect creates a gap between WTA and WTP that prevents efficient trade. The mug has one objective value, but ownership distorts p*

**Model Response:**
> **Short answer:**  
The gap is produced by the **endowment (or ownership) effect**, which is a manifestation of **loss‑aversion / reference‑dependent preferences** from prospect theory. Because people value something more once it is in their possession, sellers set a reservation price that is higher than the price buyers are willing to pay, even though the mugs were assigned at random and have no intrinsic difference. Classical (neoclassical) economics, which assumes that preferences are fixed, independent of ownership, and that a single market‑clearing price must exist, cannot generate such a systematic “buyer‑seller” valuation gap.

---

## Step‑by‑step reasoning

| Step | What we observe / ask | What the observation tells us | Economic‑theoretic expectation |
|------|-------------------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the endowment effect and explains the underlying mechanism of loss aversion and reference-dependent preferences (ownership as the reference point, giving up as a loss). This meets all criteria for Level 3. However, the response does not reach Level 4 because it omits

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Darya insists on going skiing because she paid 300 gold. Her friend says the money is gone either way. Who is right, and what error is Darya making?

**Expected Answer:** **Sunk cost fallacy** — The sunk cost fallacy is the tendency to continue an activity because of past investment (time, money, effort) rather than future expected value. Under MEU, sunk costs are decision-irrelevant: only future costs and benefits should affect current choices. The fallacy arises from mental accounting — t *The 300 gold is gone regardless of the choice. Rational decision-making considers only future costs and benefits. Going skiing while sick produces less utility than the free cabin. Darya is letting a *

**Model Response:**
> **Who is right?**  
Mira is right. The rational decision is to choose the option that will give Darya the greatest *future* benefit – a free cabin where she can rest while she feels ill. The 300 gold she already spent on the ski ticket is a **sunk cost**: it cannot be recovered no matter what she does now.

**What error is Darya making?**  
Darya is committing the **sunk‑cost fallacy** (also called the “Concorde fallacy” or “escalation of commitment”). She lets the money she has already spent dictate her present choice, even though that money is gone regardless of her action.

---

### Step‑by‑step reasoning

| Step | What’s happening | Why it matters |
|------|------------------|----------------|
| 1.   | Darya has already paid 300 gold for a non‑refundable ski ticket. | The payment is *p

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the sunk cost fallacy, explicitly states that the 300 gold is irrecoverable regardless of the choice, and explains the normative principle that only future costs and benefits should drive the decision. However, the response does not reach Level 4 because it lacks an 

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Mirella knows holding back would be better for both, yet she strips the grove anyway. What structural feature of her situation makes cooperation so difficult?

**Expected Answer:** **Prisoner's Dilemma** — A symmetric 2-player game where individual rationality (dominant strategy D) leads both players to an outcome strictly worse than mutual cooperation. The unique Nash equilibrium is (D,D), yet (C,C) Pareto-dominates it. *Defecting is individually rational — higher payoff regardless of the other's choice. But when both follow this logic, they lock into (1,1), forgoing the mutually superior (3,3).*

**Model Response:**
> **Short answer**  
Mirella’s dilemma is a **prisoner’s‑dilemma style social dilemma (the “tragedy of the commons”)**.  
The *payoff structure* of the game gives each brewer a **dominant strategy to defect**, so the mutually‑cooperative outcome is not a Nash equilibrium and is therefore very hard to achieve without external enforcement or credible commitment mechanisms.

---

## Step‑by‑step reasoning  

| 1. Identify the strategic situation |  
|---|  
Both brewers choose **simultaneously** each season whether to **Cooperate** (harvest conservatively) or **Defect** (strip the grove). The pay‑offs described are:  

|               | Orik Cooperates | Orik Defects |
|---------------|----------------|--------------|
| **Mirella Cooperates** | 3 gold each (Pareto‑optimal) | 0 gold for Mirella,

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a Prisoner's Dilemma (also noting the Tragedy of the Commons connection). They explicitly demonstrate dominant strategy reasoning for both players, identify the unique Nash equilibrium at (Defect, Defect), and clearly explain that the mutual cooperatio

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks you to find the Nash Equilibrium. For each strategy pair, check: could either cadet do better by switching alone? Which pair survives this test?

**Expected Answer:** **Nash equilibrium** — A Nash Equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. In the PD above, (Fortify, Fortify) is the unique Nash Equilibrium: if A plays Fortify and B plays Fortify, A gets 1. If A switches to Patrol, A gets 0 (worse). Symmetrically fo *Nash Equilibrium captures the key insight of strategic stability: no player can do better by changing strategy alone. In the PD, Fortify dominates Patrol — regardless of what the opponent does, Fortif*

**Model Response:**
> **What is being illustrated? – A “best‑response” (or dominant‑strategy) reasoning pattern that is the very definition of a Nash equilibrium.**

---

### Step‑by‑step reasoning that the instructor is asking you to use  

1. **List every possible pair of strategies** (Patrol‑Patrol, Patrol‑Fortify, Fortify‑Patrol, Fortify‑Fortify).  
2. **For each pair ask the two unilateral‑deviation questions**  

   * “If Cadet A kept his current move, could Cadet B get a higher payoff by switching to his other move?”  
   * “If Cadet B kept his current move, could Cadet A get a higher payoff by switching to his other move?”  

3. **Discard any pair in which at least one of the two answers is “yes.”**  
4. The pair(s) that survive are the *Nash equilibrium* (the outcome where no single player can improve 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies (Fortify, Fortify) as the unique Nash Equilibrium and systematically demonstrates why no unilateral deviation is beneficial for either player. Furthermore, they explicitly analyze why (Patrol, Patrol) is not an equilibrium by showing the incentive to deviate (gaining

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?

**Expected Answer:** **Iterated PD and cooperation** — In a finitely repeated PD with known endpoint, backward induction predicts defection every round. But in an infinitely repeated PD (or one with unknown endpoint), the Folk Theorem shows that cooperation can be sustained as a Nash Equilibrium if players value future payoffs enough (discount factor de *Iteration changes everything. The shadow of the future creates incentives for cooperation: defecting today earns a short-term gain but triggers retaliation that reduces future payoffs. If the future i*

**Model Response:**
> **1.  What changes when the Prisoner’s Dilemma is repeated?**  

| One‑shot PD | Repeated (indefinite) PD |
|-------------|--------------------------|
| The game ends after a single move.  The only thing that matters is the payoff from that one round. | The game continues for an unknown number of rounds.  The *future* payoff that you can earn (or lose) by influencing your opponent’s behaviour now becomes part of the calculation. |
| **Dominant strategy:** Defect – it gives a higher payoff no matter what the opponent does. | **No longer a strict dominant‑strategy equilibrium.**  If you can convince the opponent to cooperate now, you can reap the higher mutual‑cooperation payoff in many later rounds, and the loss from a single “mistake” is outweighed by the stream of future gains.  The game 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the 'shadow of the future' as the mechanism that changes the strategic landscape and explains how future gains can outweigh immediate defection. However, the response fails to articulate the specific conditions required for this to hold (such as a high discount facto

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find both Nash Equilibria in the Stag Hunt. Which is payoff-dominant? Which is risk-dominant? Which would you choose, and what does your choice depend on?

**Expected Answer:** **Stag Hunt** — The Stag Hunt (from Rousseau) has two pure-strategy Nash Equilibria: (Stag, Stag) = (5,5) and (Hare, Hare) = (2,2). (Stag, Stag) is payoff-dominant (better for everyone). (Hare, Hare) is risk-dominant (safer — you get 2 guaranteed regardless of partner). The core tension: cooperation requires trust. *Unlike the PD, neither strategy dominates. The optimal choice depends entirely on expectations about your partner. This is a coordination problem, not a cooperation problem.*

**Model Response:**
> **1.  The two pure‑strategy Nash equilibria**

|                     | Partner plays **Stag** | Partner plays **Hare** |
|---------------------|------------------------|------------------------|
| **You play Stag**  | (5, 5)                 | (0, 3)                 |
| **You play Hare**  | (3, 0)                 | (2, 2)                 |

* **(Stag , Stag)** – If the other hunter is playing Stag, your best reply is Stag (5 > 3).  
  If you are playing Stag, the other hunter’s best reply is also Stag (5 > 0).  
  → No one wants to deviate → **Nash equilibrium**.

* **(Hare , Hare)** – If the other hunter is playing Hare, your best reply is Hare (2 > 0).  
  If you are playing Hare, the other hunter’s best reply is also Hare (2 > 0).  
  → No one wants to deviate → **Nash equilibrium**.

Th

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies both pure-strategy Nash Equilibria ((Stag, Stag) and (Hare, Hare)) and accurately defines and identifies the payoff-dominant equilibrium. However, the response cuts off mid-sentence while attempting to explain the risk-dominant equilibrium. Because the explanation fo

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find all Nash Equilibria in this game, including any mixed-strategy equilibrium. Why is the mixed equilibrium worse for both players than either pure equilibrium?

**Expected Answer:** **Battle of the Sexes** — Battle of the Sexes has two pure-strategy Nash Equilibria: (Opera, Opera) = (3,2) and (Tournament, Tournament) = (2,3). Both are coordination equilibria — both players prefer being together over being apart. But they disagree on which is better: Helena prefers (Opera, Opera), Roderick prefers (Tourn *Neither player has a dominant strategy. The choice depends on expectations about the other — creating a coordination problem with a distributional conflict.*

**Model Response:**
> **Step‑by‑step solution**

1. **Write the normal‑form game**

|                     | Roderick: Opera | Roderick: Tournament |
|---------------------|----------------|----------------------|
| **Helena: Opera**   | (3 , 2)        | (0 , 0)              |
| **Helena: Tournament**| (0 , 0)        | (2 , 3)              |

The first number is Helena’s payoff, the second is Roderick’s.

2. **Identify the pure‑strategy Nash equilibria**

A profile is a Nash equilibrium if no player can improve his payoff by unilaterally deviating.

* **(Opera, Opera)** – Helena gets 3 (instead of 0 if she switched to Tournament) and Roderick gets 2 (instead of 0 if he switched). Neither wants to deviate → **NE**.
* **(Tournament, Tournament)** – Helena gets 2 (instead of 0) and Roderick gets 3 (instead of 0). N

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the game structure and finds both pure-strategy Nash equilibria ((Opera, Opera) and (Tournament, Tournament)). However, the response cuts off immediately after introducing the section for the mixed-strategy equilibrium, providing no calculation, explanation of why it

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** You and your contact must meet without communication. Why do people converge on the same location and time? What property makes some answers more likely than others, and is this a rational process?

**Expected Answer:** **Focal points (Schelling points)** — A focal point is a solution to a coordination game that attracts players' attention because it is salient — prominent, unique, culturally significant, or symmetric. Focal points work because of mutual expectations: I go to the fountain because I expect you to expect me to expect... etc. Sources of s *Focal points solve the equilibrium selection problem in coordination games. When there are many Nash Equilibria and no communication, salience determines which equilibrium is played. The insight is th*

**Model Response:**
> **Short answer**

People converge because they are looking for a *Schelling (or focal) point* – a solution that is **salient, obvious and common‑knowledge** to both parties.  
The property that makes an answer more likely is **salience / common‑knowledge‑based prominence**.  
In a coordination game with no communication, choosing the most salient option is a **rational** move (it is a Nash equilibrium), although the mental shortcut that leads us to notice the salient option is a cognitive bias (salience/availability bias).

---

## 1. The situation is a classic *coordination game*

| Player | Choice set (location + time) | Pay‑off |
|--------|-----------------------------|---------|
| You    | Any place in Archon at any hour | 1 if you meet the contact, 0 otherwise |
| Contact| Same set   

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'focal points' (Schelling points) and explicitly lists multiple sources of salience (prominence, common knowledge, simplicity, cultural cues). They also accurately describe the mutual-expectation mechanism using 'Level-k reasoning' and the iterative lo

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid.

**Expected Answer:** **Convention (Lewis)** — A convention is a regularity R in behavior that is (1) followed by everyone, (2) expected by everyone, (3) preferred by everyone given others' conformity, (4) has at least one alternative R' that could have served instead, and (5) is common knowledge. Conventions are solutions to recurrent coordinat *Lewis's theory explains how arbitrary social practices persist and why they are rational to follow: given that everyone else conforms, conforming is your best response. This applies to language, money*

**Model Response:**
> ### 1.  What “convention” means in a technical (game‑theoretic) sense  

In the language of game theory a **convention** is a *self‑enforcing equilibrium* of a coordination game.  
It is a pattern of behaviour that:

* solves a problem in which each player’s payoff depends on what the others do,  
* is sustained because everybody *expects* everybody else to follow it, and  
* does not have to be justified by any intrinsic superiority of the action itself.

David Lewis gave a precise set of criteria that any such equilibrium must satisfy.  When all five are met we can say that the behaviour is a **convention**.

---

### 2.  Lewis’s five conditions applied to “driving on the right”

| Lewis’s condition | How it is satisfied by “drive on the right” in the town |
|-------------------|--------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a Lewisian convention and accurately applies all five of Lewis's conditions to the driving example, including the crucial points of arbitrariness (condition 4) and common knowledge (condition 5). The response explains why driving on the left would work

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor has drawn the Entry Game tree. Identify the decision nodes, the branches, and the terminal payoffs. What information does each player have when they move?

**Expected Answer:** **Game trees (extensive form)** — A game tree represents a sequential game with nodes (decision points), branches (available actions), terminal nodes (outcomes with payoffs), and information sets (what each player knows when they move). Unlike the normal form (matrix), the extensive form explicitly represents the order of moves, whi *The extensive form reveals strategic structure that the normal form hides. In this game, the Incumbent's threat to Fight is visible but not credible — if the Entrant enters, the Incumbent prefers Acco*

**Model Response:**
> **1.  The tree – what the pieces are**

| Element | What it is in the tree | What it represents in the game |
|---------|------------------------|--------------------------------|
| **Decision nodes** | • Node A – the first node, where the **Entrant** chooses. <br>• Node B – the second node, reached only if the Entrant chose **Enter**; here the **Incumbent** chooses. | The points at which a player must make a strategic choice. |
| **Branches (actions)** | From Node A: <br>‑ **Stay Out** <br>‑ **Enter** <br>From Node B (only after **Enter**): <br>‑ **Accommodate** <br>‑ **Fight** | The possible moves a player can take at his decision node. |
| **Terminal (leaf) nodes & pay‑offs** | 1. **Stay Out** → terminal node with payoff **(Entrant = 1 , Incumbent = 3)** <br>2. **Enter → Accommodate** →

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies all structural elements of the game tree (nodes, branches, payoffs) and explicitly recognizes the perfect information structure where the Incumbent observes the Entrant's move. This satisfies all criteria for Level 3. However, the response stops short of Level 4 beca

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** Apply backward induction to the Entry Game. Start at the last decision node and work backward. What is the subgame perfect equilibrium? Why is the Incumbent's threat to Fight not credible?

**Expected Answer:** **Backward induction** — Backward induction solves extensive-form games by starting at the terminal nodes and working backward. At each decision node, the player is assumed to choose their optimal action. The resulting strategy profile is a subgame perfect equilibrium (SPE). In the Entry Game: (1) At Incumbent's node: Accom *Backward induction eliminates non-credible threats. (Stay Out, Fight) is a Nash Equilibrium but relies on the Incumbent's non-credible threat to Fight. Backward induction reveals that the Incumbent wo*

**Model Response:**
> **Backward‑induction walk‑through**

1. **Last decision node – the Incumbent’s move after entry**  
   *If the Entrant decides to enter, the game reaches the sub‑game in which the Incumbent must choose between*  

   - **Accommodate** → payoff to Incumbent = 2, payoff to Entrant = 2  
   - **Fight**    → payoff to Incumbent = 0, payoff to Entrant = 0  

   Because the Incumbent is rational and wants to maximise his own payoff, **Accommodate (2 > 0) is the unique best‑response** in this sub‑game.

2. **Move back to the Entrant’s decision node**  
   The Entrant now knows what the Incumbent will do if she enters: the Incumbent will accommodate.  
   The Entrant’s two options are therefore  

   - **Enter** → she receives 2 (since the Incumbent will accommodate)  
   - **Stay out** → she rece

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly applies backward induction starting from the Incumbent's node, identifies the unique SPE as (Enter, Accommodate), and explicitly explains why the alternative Nash equilibrium (Stay Out, Fight) fails due to the non-credibility of the threat. This meets all criteria for Level 4, 

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The Entry Game has two Nash Equilibria. The instructor says one of them relies on a non-credible threat. Which one, and why does SPE eliminate it?

**Expected Answer:** **Subgame perfect equilibrium** — SPE (Selten 1965) requires that a strategy profile be a Nash Equilibrium in every subgame. A subgame is any part of the game tree that forms a complete game on its own. SPE eliminates NE that rely on non-credible threats — strategies that would not be followed through if the relevant decision node w *SPE is a refinement of NE that captures credibility. A threat is credible only if the threatener would actually carry it out. SPE formalizes this by requiring optimality at every node, not just on the*

**Model Response:**
> **Answer**

- **The equilibrium that rests on a non‑credible threat is the “(Stay Out, Fight)” outcome.**  
- **Why SPE throws it out:** In a sub‑game perfect equilibrium every player’s strategy must be optimal **at every decision node**, not only at the nodes that are actually reached when the equilibrium is played.  
  1. Suppose the entrant does decide to enter. The game then moves to the incumbent’s decision node (the “fight‑or‑accommodate” sub‑game).  
  2. At that node the incumbent’s pay‑offs are  
     - Fight → 0  
     - Accommodate → 2  
  3. Because 2 > 0, the incumbent’s best response in that sub‑game is **Accommodate**, not Fight.  
  4. Hence the strategy “Fight if entered” is not optimal at that node; it is a *bluff* that would be abandoned the instant it were tested.  
  5

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the non-credible threat, explains that SPE requires optimality at every decision node, and correctly identifies (Enter, Accommodate) as the unique SPE. The response aligns perfectly with Level 3 criteria. It does not reach Level 4 because it does not discuss how comm

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Question:** Apply backward induction to the Centipede Game. What does it predict? Do you find the prediction convincing? What assumption is doing the heavy lifting, and what happens if you relax it?

**Expected Answer:** **Centipede Game** — The Centipede Game is a sequential game where two players alternate between stopping (taking a smaller immediate payoff) and continuing (allowing the total payoff to grow). Backward induction predicts immediate stopping — the unique SPE. But this is paradoxical: both players would be much better off *Backward induction is logically valid given CKR, but the outcome (1,1) seems absurd when (4,4) is available through mutual cooperation. The paradox reveals that CKR may be too strong an assumption — o*

**Model Response:**
> **1.  The backward‑induction calculation**

The game has four decision nodes, two for each player.  
We start at the last node and work our way back, always assuming that the player who is about to move will choose the action that gives him the highest *immediate* payoff, given what will happen later.

| Node | Player | Stop payoff | Continue payoff (given the continuation) |
|------|--------|-------------|-------------------------------------------|
| 4    | P2     | (2, 5) → 5  | (4, 4) → 4                                 |
| 3    | P1     | (3, 2) → 3  | (2, 5) → 2 (because P2 will stop at 4)    |
| 2    | P2     | (0, 3) → 3  | (3, 2) → 2 (because P1 will stop at 3)    |
| 1    | P1     | (1, 1) → 1  | (0, 3) → 0 (because P2 will stop at 2)    |

Working backwards:

1. **Node 4:** P2 p

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly applies backward induction to reach the unique SPE (stop at Node 1) and clearly identifies the paradox between the rational prediction (1,1) and the intuitive/experimental outcome (4,4). They explicitly name 'common-knowledge of perfect rationality' as the critical assumption d

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

**Expected Answer:** **Evolutionarily Stable Strategy (ESS)** — An ESS (Maynard Smith) is a strategy that, when adopted by almost all members of a population, cannot be invaded by any rare mutant strategy. Formally: S is ESS if for any mutant M, either (1) E(S,S) > E(M,S), or (2) E(S,S) = E(M,S) and E(S,M) > E(M,M). In Hawk-Dove with V<C, neither pure strategy i *ESS provides a concept of equilibrium that does not require rationality — only differential reproduction. Strategies that do better than average spread; those that do worse shrink. The mixed ESS emerg*

**Model Response:**
> **Step‑by‑step verification of the ESS claims**

1. **Write down the payoff matrix (the biologist’s numbers)**  

|               | Opponent Hawk | Opponent Dove |
|---------------|---------------|---------------|
| **Hawk**      | \((V-C)/2 = (4‑6)/2 = -1\) | \(V = 4\) |
| **Dove**      | \(0\)                     | \(V/2 = 2\) |

2. **Recall the definition of an Evolutionarily Stable Strategy (ESS).**  
   A strategy \(s\) is an ESS if, when the whole population plays \(s\), any rare mutant strategy \(t\) does **not** obtain a higher expected payoff. Formally:

   *Either*  
   \[
   E(s,s) > E(t,s)
   \]
   *or* (if the payoffs are equal)  
   \[
   E(s,t) > E(t,t).
   \]

3. **Test the pure‑Hawk strategy.**  

   * Payoff when a Hawk meets a Hawk: \(E(H,H) = -1\).  
   * Payoff to a ra

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly constructs the payoff matrix, states the formal definition of ESS, and successfully demonstrates that neither pure Hawk nor pure Dove is an ESS (meeting Level 2 criteria). They begin the derivation for the mixed ESS by setting up the expected payoff equations but fail to solve 

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The biologist perturbs the Hawk population from 50% to 51%. Show that the system returns to 50% by calculating fitness for each strategy. What does this tell you about the stability of the mixed ESS?

**Expected Answer:** **Replicator dynamics** — The replicator dynamics models how strategy frequencies change over time based on fitness. The equation dx_i/dt = x_i(f_i - F) says: strategies that outperform average grow; those that underperform shrink. Key properties: (1) ESS are stable fixed points of replicator dynamics. (2) Not all fixed poin *The replicator dynamics provides the 'how' behind ESS — the mechanism by which populations reach (or fail to reach) equilibrium. It requires no rationality, only differential reproduction or imitation*

**Model Response:**
> **Step‑by‑step calculation**

Let  

* \(x\) = proportion of Hawks in the population,  
* \(1-x\) = proportion of Doves,  

and use the payoff matrix for the Hawk–Dove game with \(V=2\) and \(C=4\)

\[
\begin{array}{c|cc}
      & \text{Hawk} & \text{Dove}\\ \hline
\text{Hawk} & \displaystyle\frac{V-C}{2}= -1 & V = 2\\[4pt]
\text{Dove} & 0 & \displaystyle\frac{V}{2}=1
\end{array}
\]

---

### 1.  Fitness of each strategy when the Hawk share is **51 %** (\(x=0.51\))

*Fitness of a Hawk*  

\[
\begin{aligned}
f_H &= x\;(-1) + (1-x)\;(2)\\
    &= 0.51(-1) + 0.49(2)\\
    &= -0.51 + 0.98 = 0.47 .
\end{aligned}
\]

*Fitness of a Dove*  

\[
\begin{aligned}
f_D &= x\;(0) + (1-x)\;(1)\\
    &= 0.51(0) + 0.49(1)\\
    &= 0.49 .
\end{aligned}
\]

*Average fitness*  

\[
F = x f_H + (1-x) f_D
   = 0.

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly computes the fitness for both strategies at the perturbed state (x=0.51), calculates the average fitness, and applies the replicator dynamics equation to show that the Hawk proportion decreases because its fitness is below average. This confirms the system returns to equilibriu

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In the evolutionary Stag Hunt, what determines whether cooperation or defection wins? Why does Skyrms call the cooperative equilibrium a 'social contract'? What factors help cooperation evolve?

**Expected Answer:** **Evolution of cooperation** — In evolutionary Stag Hunt, cooperation (Stag) can evolve if enough of the population already cooperates. The threshold is p=0.5 in standard payoffs. Above the threshold, cooperation is self-reinforcing; below, it collapses. This is the basin of attraction concept. Factors that help cooperation evolv *The evolution of cooperation shows that cooperative outcomes can emerge without rational deliberation — through selection, iteration, and correlation. This provides a different foundation for social o*

**Model Response:**
> **1.  What decides which side wins in the evolutionary Stag‑Hunt?**  

|               | Partner plays **Stag** | Partner plays **Hare** |
|---------------|------------------------|------------------------|
| **Stag**      | 5 , 5                  | 0 , 3                  |
| **Hare**      | 3 , 0                  | 2 , 2                  |

*Pay‑off to the focal player is shown first.*

* **Frequency‑dependent fitness** – The expected payoff to a strategy depends on how common the opposite strategy is.  
  *If the proportion of Stag‑hunters in the population is \(p\):*  

\[
\begin{aligned}
E(\text{Stag}) &= 5p + 0(1-p)=5p,\\[4pt]
E(\text{Hare}) &= 3p + 2(1-p)=p+2 .
\end{aligned}
\]

* **Equilibrium threshold** – Solving \(5p = p+2\) gives \(p^{*}=0.5\).  
  * If the initial share of Stag

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly calculates the threshold (p=0.5), explains the basin of attraction concept clearly, and accurately connects the equilibrium to Skyrms's definition of a social contract. They also explicitly mention path dependence. However, the response fails to discuss specific evolutionary fa

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Torva says her profit from the sword is eighty gold. Is she right? What is she forgetting to account for?

**Expected Answer:** **Opportunity cost** — The opportunity cost of an action is the value of the next-best alternative forgone. Torva treats the sword's revenue (80 gold) as pure profit, but by choosing the sword she forgoes the 50-gold axle repair. Her net gain from choosing the sword over the axle is 80 - 50 = 30 gold, not 80 gold. The 50  *Every choice has a hidden cost: what you gave up to make it. Torva's sword commission is genuinely better than the axle repair, but by 30 gold, not by 80. Understanding this prevents her from overvalu*

**Model Response:**
> **Short answer:**  
No – Torva is not calculating profit, she is only quoting the *revenue* she would receive for the sword.  She is forgetting to subtract the cost of the steel (and any other material or overhead expenses) and to factor in the *opportunity cost* of the day she will spend on the sword instead of the axle repair.

---

## Step‑by‑step reasoning

| Step | What Torva says | What the step actually requires |
|------|----------------|--------------------------------|
| 1.   | “The sword pays **eighty gold**, so that’s my profit.” | Profit = **Revenue** – **Costs**.  “Eighty gold” is the *revenue* (the price the knight will pay). |
| 2.   | She assumes the whole 80 gp stays in her pocket. | She must subtract **material cost** (the good‑quality steel), **any consumables** (fuel f

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the concept of opportunity cost and explicitly calculates the net gain (80 - 50 = 30 gold implied in the logic, though they focus heavily on material costs as well). They meet Level 3 criteria by identifying the 50 gold forgone and the resulting net difference. Howev

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Hilde outproduces Oskar in both wheat and flax. She says trade cannot benefit her. Is she right? Calculate the opportunity costs and determine who should specialize in what.

**Expected Answer:** **Comparative advantage** — Hilde has absolute advantage in both goods, but comparative advantage depends on opportunity cost. Hilde's opportunity cost of 1 bolt of flax = 2 bushels of wheat (12/6). Oskar's opportunity cost of 1 bolt of flax = 4/3 bushels of wheat. Oskar has a lower opportunity cost for flax, so he has compara *Trade benefits do not require being equally productive. Even though Hilde is better at both crops, she benefits from specializing in the crop where her relative advantage is greatest (wheat) and tradi*

**Model Response:**
> **1.  The numbers – what each farmer can produce**

| Farmer | Wheat (bushels) | Flax (bolts) |
|--------|----------------|--------------|
| Hilde  | 12             | 6            |
| Oskar  | 4              | 3            |

Both farmers can use the whole season for **either** crop, so the trade‑off is linear.

---

### 2.  Opportunity‑cost calculations  

*Opportunity cost* = “how much of the other good must be given up to produce one unit of the good in question.”

| Farmer | OC of 1 wheat (in flax) | OC of 1 flax (in wheat) |
|--------|------------------------|--------------------------|
| **Hilde** | 6 flax ÷ 12 wheat = **0.5 flax** per wheat | 12 wheat ÷ 6 flax = **2 wheat** per flax |
| **Oskar** | 3 flax ÷ 4 wheat = **0.75 flax** per wheat | 4 wheat ÷ 3 flax = **1.33 wheat** per fl

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly calculates all opportunity costs for both farmers and accurately identifies that Hilde has the comparative advantage in wheat while Oskar has it in flax. This meets all criteria for Level 3. However, the response does not reach Level 4 because it stops short of proposing a spec

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?

**Expected Answer:** **Constrained optimization** — The problem is to minimize cost subject to constraints. Food constraint: 3R >= 15, so R >= 5 (minimum 5 ration packs). Torch constraint: 4T >= 8, so T >= 2 (minimum 2 torch bundles). Cost: 5R + 10T. Minimum cost = 5(5) + 10(2) = 25 + 20 = 45 gold. This satisfies both constraints and is within budget *Constrained optimization is the core microeconomic framework: maximize (or minimize) an objective function subject to binding constraints. Seren cannot simply buy everything — she must find the combin*

**Model Response:**
> **Step‑by‑step solution**

1. **Write down the variables**  
   * Let \(r\) = number of rations bought.  
   * Let \(t\) = number of torches bought.

2. **Translate the problem into equations/inequalities**  

| Item | Cost (gold) | Food (units) | Light (units) |
|------|-------------|--------------|---------------|
| Ration | 5 g | 3 f | 0 l |
| Torch  |10 g | 0 f | 4 l |

The expedition must have  

\[
\begin{cases}
3r \;\ge\; 15 &\text{(food requirement)}\\[4pt]
4t \;\ge\; 8  &\text{(light requirement)}\\[4pt]
5r + 10t \;\le\; 100 &\text{(budget)}\\[4pt]
r,\;t \in \mathbb Z_{\ge 0}
\end{cases}
\]

3. **Find the smallest integer values that satisfy the first two constraints**

* Food: \(3r \ge 15 \;\Rightarrow\; r \ge 5\).  
* Light: \(4t \ge 8 \;\Rightarrow\; t \ge 2\).

4. **Check the 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the variables, sets up the constraints, solves for the minimum integers (R=5, T=2), calculates the correct cost (45 gold), and explicitly verifies that no cheaper combination exists. This perfectly matches the criteria for Level 3. The response does not reach Level 4

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Each potion sells for 15 gold. The cost of each additional potion rises: 5, 8, 12, 16, 22. How many potions should Elara brew, and why?

**Expected Answer:** **Marginal analysis** — Marginal analysis compares the marginal benefit (MB) to the marginal cost (MC) of each additional unit. Brew if MB > MC; stop when MC >= MB. Revenue per potion (MB) = 15 gold. MC of potions: 1st=5, 2nd=8, 3rd=12, 4th=16, 5th=22. For potions 1-3, MB(15) > MC. For potion 4, MC(16) > MB(15). Elara shou *Marginal analysis prevents two errors: stopping too early (missing profitable units) and going too far (adding units that cost more than they earn). The fourth potion costs 16 gold but only earns 15 —*

**Model Response:**
> **Answer – Brew three potions**

| Potion # | Cost (gold) | Revenue (gold) | Profit on that potion |
|----------|-------------|----------------|-----------------------|
| 1        | 5           | 15             | **+10**               |
| 2        | 8           | 15             | **+7**                |
| 3        | 12          | 15             | **+3**                |
| 4        | 16          | 15             | **‑1**                |
| 5        | 22          | 15             | **‑7**                |

* Cumulative profit after each potion:  
  - After 1: +10  
  - After 2: +10 + 7 = +17  
  - After 3: +17 + 3 = +20 (the highest total)  
  - After 4: +20 ‑ 1 = +19  
  - After 5: +19 ‑ 7 = +12  

The total profit peaks at **three potions**. Brewing a fourth would cost more (16 gold) than 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the optimal quantity (3 potions) using marginal analysis, explicitly comparing MC to MR for each unit. They accurately calculate the total profit (20 gold) and provide a sophisticated explanation of the decision rule, distinguishing it from average costs. Additionall

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Captain Hale says she should let the others pay for the lighthouse oil. Her reasoning seems logical from her own perspective. What happens if every captain follows the same logic? Why does this situation arise?

**Expected Answer:** **Public goods and free riding** — The lighthouse is a public good: non-rival (one captain using the light does not diminish it for others) and non-excludable (you cannot prevent a non-paying captain from seeing the light). These properties create a free-rider incentive: each captain benefits from the lighthouse regardless of whether *Free riding is individually rational but collectively destructive. Hale's logic is valid for any single captain, but if universalized, it leads to a lighthouse going dark and all captains risking thei*

**Model Response:**
> **What happens if every captain follows Hale’s reasoning?**  

If each captain thinks, *“If the other four pay, I can keep my 20 gold and still enjoy the light, so I’ll let them foot the bill,”* then every captain will make the same calculation.  
All five will decide **not to pay**. The lighthouse runs out of oil, the light goes out, and each captain’s boat is lost (≈ 500 gold) once each season.  

So the group ends up **worse off** than if they had all contributed the 20 gold each (the light stays on, no boat is lost, total cost 100 gold). The “rational” individual choice leads to a collectively irrational outcome.

---

### Why does this situation arise?

| Element of the problem | Explanation |
|------------------------|-------------|
| **Public good** | The lighthouse light is **non‑e

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the free-rider problem, explicitly defines the lighthouse as non-rival and non-excludable, and draws a clear connection to the Prisoner's Dilemma and dominant strategy reasoning. However, the response does not reach Level 4 because it fails to propose any solution me

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Elder Yara says every family is acting sensibly, yet the lake is dying. How can individual rationality produce collective disaster? What is the structural problem?

**Expected Answer:** **Commons problems (Tragedy of the commons)** — Lake Mirren is a common-pool resource: rival (each fish caught is unavailable to others) but non-excludable (no family can be prevented from fishing). Each family captures the full benefit of each additional fish they catch but bears only a fraction of the cost (resource depletion shared across all  *The structural incentive to overextract is real and rational for each individual. The problem is not stupidity or greed but a misalignment between individual and collective incentives.*

**Model Response:**
> **Short answer:**  
Elder Yara is describing the classic **“Tragedy of the Commons.”**  
It is a collective‑action / game‑theoretic problem in which every family’s *individually rational* decision (catch as many fish as possible before someone else does) creates a *negative externality* for the whole group, and the resulting Nash equilibrium is a depleted lake that makes everyone worse off.

---

## Step‑by‑step reasoning

| Step | What the families think / do | Why it looks “sensible” to them | What actually happens |
|------|-----------------------------|----------------------------------|-----------------------|
| 1.   | The lake can sustainably supply **60 fish/week**. | If I catch **10** (the historic share) I get a steady supply and the lake stays healthy. | The lake remains full – e

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Tragedy of the Commons' pattern and provides a robust explanation of the mechanism: individually rational decisions leading to collective depletion due to the asymmetry between private benefits and shared costs (negative externalities). The response explicitly c

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Sera and Brenn create 80 gold in surplus from trade. Sera's outside option gives her 15 gold surplus; Brenn's gives him 10. How should they split the 80 gold surplus, and why?

**Expected Answer:** **Bargaining and fairness (Nash bargaining)** — The surplus from trade is 80 gold. Each merchant's outside option (BATNA) sets a floor: Sera will not accept less than 15 gold surplus (her alternative deal), and Brenn will not accept less than 10. The remaining surplus after securing both outside options is 80 - 15 - 10 = 55 gold. Nash bargaining  *Bargaining theory shows that fair division depends not just on the total surplus but on each party's outside option. Better alternatives give you more bargaining power. This framework prevents the nai*

**Model Response:**
> **Step‑by‑step calculation**

1. **Identify the “disagreement point” (outside options).**  
   * If the two merchants do **not** trade, each can walk away and still make a surplus:  
   * Sera can sell her salt to another buyer for a surplus of **15 gold**.  
   * Brenn can sell his iron to another buyer for a surplus of **10 gold**.  

   These numbers are the *threat points* in a bargaining problem – the payoff each player can guarantee himself without cooperation.

2. **Compute the total surplus that the trade creates.**  
   The joint surplus from the exchange is given in the story as **80 gold**.

3. **Subtract the disagreement payoffs from the total surplus.**  
   The amount that is *extra* because they cooperate (the “pie” that can be divided above the threat point) is  

   \[
   

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the outside options, calculates the remaining surplus (55), splits it equally (27.5), and derives the final correct payoffs (42.5 and 37.5). The explanation of the mechanism (Nash bargaining, individual rationality, Pareto efficiency) is accurate. However, the respon

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Lady Ashworth paid Corbin a flat wage and got a poor harvest. She suspects shirking but cannot prove it. What is the structural problem with her contract, and how might she redesign it?

**Expected Answer:** **Principal-agent problems and moral hazard** — The principal (Ashworth) delegates a task to an agent (Corbin) whose effort she cannot observe. Under a flat wage, the agent bears the cost of effort but captures none of the benefit (the extra apples go to the principal). This misalignment of incentives is moral hazard: the agent has both the oppor *Corbin is not necessarily lazy or dishonest — the contract structure gives him no reason to exert effort. The problem is the incentive design, not the person.*

**Model Response:**
> **1. The underlying economic problem – a classic *principal‑agent* (or *moral‑hazard*) situation**

| Element | Who it is | What the contract says | What the contract *doesn’t* address |
|---------|-----------|------------------------|--------------------------------------|
| **Principal** | Lady Ashworth (the orchard owner) | Pays a *flat* 50 gold/month to Corbin, regardless of how many apples are harvested. | How much effort Corbin puts in (hidden action). |
| **Agent** | Corbin (the manager) | Receives a guaranteed 50 gold no matter what. | Any loss of output falls on the principal, not the agent. |
| **Information asymmetry** | Corbin sees his own effort, Lady Ashworth does not. | The contract cannot be conditioned on effort because the principal cannot observe it. | The contract canno

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the principal-agent problem and moral hazard, explaining the information asymmetry (hidden action) and the misalignment of incentives under a flat wage. They propose valid incentive-compatible solutions (piece-rate, hybrid contract). However, the response does not re

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Using the market board data, find the price at which quantity supplied equals quantity demanded. What happens at prices above or below this equilibrium?

**Expected Answer:** **Supply, demand, and market equilibrium** — At equilibrium, quantity supplied equals quantity demanded. From the table: at price = 2, excess demand (shortage) of 60. At price = 8, excess supply (surplus) of 60. At price = 6, Qs = 60 = Qd = 40 — not yet equal. Interpolating (or reading the table), equilibrium is at price = 5, where both Qs and *The equilibrium price coordinates decentralized buyers and sellers without anyone needing to manage the outcome. Prices above equilibrium create surpluses (pushing price down); prices below equilibriu*

**Model Response:**
> **Step‑by‑step solution**

1. **List the data**

| Price (gold/bushel) | Qty Supplied | Qty Demanded |
|---------------------|--------------|--------------|
| 2                   | 20           | 80 |
| 4                   | 40           | 60 |
| 6                   | 60           | 40 |
| 8                   | 80           | 20 |
|10                   |100           | 0  |

2. **Identify where supply and demand cross**  
   – At a price of **2** there is a huge shortage (20 supplied, 80 wanted).  
   – At **4** there is still a shortage (40 supplied, 60 wanted).  
   – At **6** there is now a surplus (60 supplied, 40 wanted).  

   The crossing point must lie **between 4 and 6 gold**.

3. **Assume the supply and demand schedules are linear between the points** (the usual textbook shortcut

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the equilibrium price (P*=5) and quantity (Q*=50) using valid linear interpolation. They explain the existence of shortages at lower prices and surpluses at higher prices, satisfying the core requirements of Level 3. However, the response does not explicitly describe

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** The king sets a price ceiling of 3 gold per bushel. Equilibrium was at 5 gold and 50 bushels. What happens to quantity supplied, quantity demanded, and the market? What trades are lost?

**Expected Answer:** **Price controls and deadweight loss** — A binding price ceiling (set below equilibrium) creates a shortage: quantity demanded exceeds quantity supplied. At P=3, Qs=30 and Qd=70, shortage=40. Some mutually beneficial trades that would occur at equilibrium (P=5, Q=50) no longer happen. The lost surplus from these unrealized trades is deadwe *The price ceiling is well-intentioned but creates predictable inefficiency. The 30 buyers who get grain pay less, but 20 buyers who would have purchased at equilibrium get nothing, and 20 units of gra*

**Model Response:**
> **1. What the price‑ceiling does to the market**

|                     | Equilibrium (no ceiling) | With a 3‑gold ceiling |
|---------------------|--------------------------|-----------------------|
| Price (P)           | 5 gold per bushel        | 3 gold (forced)       |
| Quantity supplied (Qs) | 50 bushels                | 30 bushels (the amount farmers are willing to sell at 3) |
| Quantity demanded (Qd) | 50 bushels                | 70 bushels (the amount buyers want at 3) |
| Quantity actually traded (Q) | 50 bushels                | 30 bushels (the smaller of Qs and Qd) |

* **Quantity supplied falls** – from 50 to 30 bushels.  
  Farmers who would have sold at any price above 3 (the “marginal” 20‑bushel segment) stay out of the market.

* **Quantity demanded rises** – from 50 to 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly calculates the shortage (Qd=70, Qs=30, Shortage=40) and explicitly identifies the deadweight loss by noting the 20 units of mutually beneficial trades that are lost. Furthermore, the response addresses secondary effects like black markets and rationing, and implicitly evaluates

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** Grist says his business is profitable and efficient. Wynn says Clearwater is paying part of his costs. Who is right, and what does this situation reveal about market prices?

**Expected Answer:** **Externalities** — A negative externality is a cost imposed on third parties who are not involved in the transaction. Grist's private cost is 40 gold, but the social cost includes the 20 gold per week Clearwater spends on water treatment. The true social cost of production is 60 gold, making Grist's true profit 40, no *Externalities mean the market price sends the wrong signal. Grist's leather seems like a great deal at 100 gold, but 20 gold of the true cost is hidden and borne by Clearwater. The market 'works' only*

**Model Response:**
> **Short answer**

*Both speakers are “right” – but they are looking at different cost‑structures.*  
Grist’s profit calculation is correct **if you only count the costs that he pays himself** (the “private” costs of chemicals, labor and hides).  
Wynn’s complaint is also correct **if you add the costs that the downstream village has to bear because of Grist’s pollution** (the “social” or external costs).  

What the story shows is the classic **negative‑externality / market‑failure** situation: the market price of Grist’s leather reflects only his private marginal cost, not the full social marginal cost of production. Because the polluting cost is “externalised” onto Clearwater, the leather is priced artificially low and the community ends up subsidising Grist’s profit.

---

## Step‑by‑st

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the negative externality, distinguishes between private and social costs, and explains that the market price is too low leading to inefficiency (over-production). This meets all criteria for Level 3. However, the response cuts off abruptly in Step 7 just as it begins

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral?

**Expected Answer:** **Information asymmetry and adverse selection (lemons problem)** — When sellers know more about product quality than buyers, buyers cannot distinguish good from bad. They offer a price reflecting average quality. Owners of above-average horses find this price too low and withdraw. The remaining pool is worse, buyers adjust downward, more good horses leave — a death *The market failure is not caused by dishonesty per se but by the information structure. Even honest sellers of good horses cannot credibly communicate quality because cheap talk ('my horse is great') *

**Model Response:**
> **Short answer:**  
What Kael is describing is the classic **adverse‑selection spiral** (the “market for lemons” problem). Because buyers cannot tell a healthy horse from a sick one, the information in the market is asymmetric. Good‑quality sellers therefore leave, the average quality of the remaining stock falls, prices drop, and the process repeats.

---

## Step‑by‑step reasoning

| Step | What actually happens | Why it matters |
|------|-----------------------|----------------|
| 1. **Information asymmetry** | Sellers see the true condition of their horses; buyers cannot. | Buyers cannot reward good quality with a higher price because they cannot verify it. |
| 2. **Uniform price offered** | All horses are sold at (or near) the same market price, because the market can’t differentiate 

**Score:** 3/4 ███░
**Judge Reasoning:** The student perfectly identifies the pattern (adverse selection/lemons problem) and provides a detailed, step-by-step explanation of the spiral mechanism where information asymmetry leads to average pricing, driving out high-quality goods and lowering market quality further. However, the response do

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Nobody buys the Barrel Mug, yet adding it to the menu increases Large Ale sales. The tip jar moved but the tip amount was not suggested. What is going on in both cases, and is it ethically acceptable?

**Expected Answer:** **Behavioral economics in markets: nudges and choice architecture** — Two phenomena are at work. First, the decoy effect: the Barrel Mug is a dominated option that no one chooses, but its presence makes the Large Ale seem more reasonable by comparison. It shifts the reference point. Second, choice architecture: the placement of the tip jar changes behavior without cha *When used to exploit, nudges can undermine autonomous decision-making. Customers believe they are choosing based on preferences, but the choice architecture is steering them toward the seller's prefer*

**Model Response:**
> **Short answer**

*   **Board B → more Large‑Ale sales:** Lena is exploiting the **decoy (or asymmetric‑dominance/contrast) effect**. By putting a clearly inferior, much‑more‑expensive “Barrel Mug” on the list, the Large Ale suddenly looks like the “reasonable middle” option, so more people pick it.

*   **Tip‑jar move → larger tips:** She is using a **salience / proximity cue** (a classic “nudge”). Making the tip jar visible at the exact moment the drink is handed over raises the *prompt* and triggers the social‑norm/reciprocity impulse to tip, so the amount given rises even though no explicit amount is suggested.

Both are examples of **choice‑architecture manipulations** that change behaviour without changing the actual product or price. Whether they are ethically acceptable depends on 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both the decoy effect and choice architecture (salience/proximity). They explain the mechanisms clearly, connecting them to behavioral economics principles like asymmetric dominance and social norms. Crucially, they address the ethical dimension by distinguishing bet

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Breck says the storm is good for the economy because it creates repair jobs. The clerk is skeptical. Who is right, and what is Breck failing to consider?

**Expected Answer:** **Broken window fallacy** — Breck counts the economic activity generated by repairing storm damage (the seen) but ignores the economic activity that the same money would have generated if spent on something else (the unseen). The glazier's gain is real, but the shopkeepers now spend money on window repairs instead of on new in *The fallacy confuses visible economic activity with net economic gain. Repair spending is seen; the forgone alternative spending is unseen. Bastiat's insight: 'the bad economist confines himself to th*

**Model Response:**
> **Short answer:**  
The town clerk is the one who is on solid ground.  
Alderman Breck is committing the classic *“broken‑window”* (or *disaster‑as‑stimulus*) fallacy. He is looking only at the *visible* increase in repair work and ignoring the *hidden* costs – the loss of existing capital, the opportunity cost of the labour and materials that are now being spent on rebuilding instead of on new, value‑adding production, and the broader social and economic harms that a storm brings (lost inventory, reduced tax revenue, displaced families, psychological trauma, etc.). When those hidden costs are taken into account, the net effect of the storm is negative, not a net gain for the town.

---

## Step‑by‑step reasoning

| Step | What Breck says | What the clerk (and basic economics) says | Why t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'broken-window fallacy' and explicitly explains the 'seen versus unseen' distinction. They clearly articulate the concept of opportunity cost (resources redirected from value-adding production to rebuilding) and note that net wealth decreases due to the destructi

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Dagan says that if Brassholm gains from trade, Ardenvale must lose. Petra says both sides can gain. Who is right, and why?

**Expected Answer:** **Zero-sum thinking** — Dagan falsely assumes that trade is zero-sum — that total value is fixed and any gain for one party is a loss for the other. In reality, voluntary trade creates value because parties exchange goods they value less for goods they value more. Ardenvale values iron more than its surplus grain; Brasshol *If trade were truly zero-sum, neither party would voluntarily agree to it — why accept a deal that makes you worse off? The fact that both parties choose to trade is evidence that both expect to benef*

**Model Response:**
> **Short answer:**  
Petra is correct.  Trade is not a “fixed‑pie” (zero‑sum) game; it can make *both* parties better off.  Dagan’s claim rests on a classic **zero‑sum bias / “fixed‑pie” fallacy** (often expressed as a false dilemma: “someone wins, someone loses”).  The economic principle that explains why Petra’s view is right is **comparative advantage** (or, more generally, the idea that voluntary exchange can create a Pareto‑improvement).

---

## Step‑by‑step reasoning

| Step | What we examine | Why it matters |
|------|----------------|----------------|
| 1 | **What each kingdom can produce** | Both Ardenvale and Brassholm have *different* resource endowments: Ardenvale has abundant grain, Brassholm has abundant iron.  Each can also produce the other good, but at a higher *opportunit

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Dagan's error as the 'fixed-pie' or zero-sum fallacy. They thoroughly explain the mechanism of value creation through comparative advantage, opportunity cost, and specialization. The response explicitly distinguishes between zero-sum assumptions and positive-sum trad

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter?

**Expected Answer:** **Rapoport's Rules** — A four-step protocol for productive disagreement: (1) restate the opponent's position so well they endorse the restatement, (2) list genuine points of agreement, (3) acknowledge what you learned from them, (4) only then offer criticism. Corwin follows all four steps in sequence. *Corwin follows the protocol exactly. Step 1: Holt says 'Better than I put it myself.' Step 2: Lists two factual agreements about timber loss and budget crisis. Step 3: Concedes the flow-rate data corr*

**Model Response:**
> **What Corwin is doing – a step‑by‑step “pre‑critique” routine**

| Step | What Corwin actually does (the words he uses) | Why that step matters for the discussion |
|------|-----------------------------------------------|-------------------------------------------|
| **1. Pause and “reset” the floor** | He rises slowly, takes a breath and signals that he is about to **repeat** what he has just heard. | The pause tells the audience that he is not about to jump straight into a rebuttal. It creates a calm, procedural moment that signals respect for the speaker and for the rules of deliberation. |
| **2. Steel‑man the opponent’s position** | *“Let me make sure I have Master Holt’s position right… He is saying that without the dam … the town cannot afford to protect the salmon if it cannot fir

**Score:** 2/4 ██░░
**Judge Reasoning:** The student identifies specific components of the protocol (restating/steel-manning, inviting verification, acknowledging agreement) but fails to identify all four required steps in the correct sequence. Specifically, the response misses the distinct step of 'acknowledging what was learned' before c

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?

**Expected Answer:** **Reductio ad absurdum** — Tessa takes Varek's claim ('all beliefs are equally valid') and draws out its logical consequences: flat earth is as valid as round earth, poison is as nutritious as food. Since Varek cannot accept these consequences, his original claim is undermined. This is the classic structure of reductio: assum *Reductio is a powerful tool because it tests a claim by its own standards. If a principle generates consequences the proponent themselves cannot stomach, the principle is in trouble. You do not need t*

**Model Response:**
> **What Tessa actually did**

Tessa didn’t simply “argue back” or give a personal opinion. She **used a classic *reductio ad absurdum* (argument to absurdity) by supplying concrete counter‑examples that show the disastrous consequences of Varek’s claim**. In other words, she took Varek’s principle (“no belief is better than any other”) and asked, *“If that were true, what would that also have to mean?”* She then pointed out two obviously false beliefs – “the earth is flat” and “poison is nutritious” – and asked Varek whether those should be granted the same epistemic status as well‑supported scientific claims.

**Why that move is effective**

| Reason | Explanation |
|--------|-------------|
| **Makes the hidden implication explicit** | Varek’s statement is abstract. By turning it into a co

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies 'reductio ad absurdum' by name and accurately articulates the formal structure: assuming the opponent's principle to derive unacceptable consequences ('If that were true, what would that also have to mean?'). Furthermore, the response exceeds Level 3 by discussing t

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** You have two explanations for the attic disturbances. What principle should guide your choice between them, and which explanation does it favour?

**Expected Answer:** **Occam's Razor** — When two hypotheses explain the same evidence, prefer the one that posits fewer entities and mechanisms. Elsa's squirrel hypothesis explains the torn food, scattered flour, muddy tracks, thumping, and fallen items using one known entity (squirrels) and one known mechanism (foraging through a gap). W *Occam's Razor is not a proof — it is a heuristic for rational belief. Simpler explanations are preferred because each additional assumption is an additional point of potential failure. The squirrel hy*

**Model Response:**
> **The guiding principle**

The situation is a classic case of “which hypothesis should we accept?” – and the rule that most rational investigators use is **the principle of parsimony (Occam’s Razor)**, often phrased as:

> *When two explanations account for the same facts, prefer the one that makes the fewest additional assumptions.*

A closely‑related formulation is Carl Sagan’s “extraordinary claims require extraordinary evidence.”  A ghost is an extraordinary, supernatural claim; a family of squirrels is an ordinary, natural one.  Until we have evidence that actually shows a spirit is present, the simpler, natural explanation is the rational choice.

**Step‑by‑step reasoning**

1. **Identify the observable facts**  
   - Dried meat torn open, flour scattered, muddy tracks, shredded clot

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies Occam's Razor and the principle of parsimony. They correctly break down the specific assumptions required for each hypothesis, demonstrating why the ghost hypothesis is more complex. Crucially, they address the Level 4 criteria by discussing the nature of evidence r

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Cask seems to have made a strong case. But look carefully at what he talked about and what he did not talk about. What is his argumentative strategy, and what is wrong with it?

**Expected Answer:** **Occam's Broom** — Dennett coined 'Occam's Broom' to describe the practice of sweeping inconvenient facts under the rug to make your argument look cleaner than it is. Unlike Occam's Razor (which removes unnecessary assumptions), Occam's Broom removes necessary evidence. Cask does not engage with the three independent  *Honest reasoning requires engaging with all the relevant evidence, especially evidence that challenges your position. Cask's case looks strong only because he has hidden the strongest evidence against*

**Model Response:**
> **Short answer**  
Cask is trying to win the debate by *deflecting* the real evidence and by attacking the messenger instead of the message.  He does this with a bundle of classic fallacies – a red‑herring/what‑about‑me move, an appeal to (questionable) authority, an ad hominem‑circumstantial attack on Dr Lune’s funding, and an anecdotal “miners are healthy” argument.  The problem is that none of these points address the three independent studies that actually show contamination; they are irrelevant or misleading tactics that hide the fact that the strongest evidence has been ignored.

---

### Step‑by‑step breakdown of Cask’s strategy

| What Cask says (or does) | What that move is called | Why it fails in this context |
|--------------------------|--------------------------|-------------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Cask selectively presented favorable evidence, ignored the three independent studies, and used the funding attack as an ad hominem circumstantial fallacy. They explicitly recognize the pattern of 'hiding' or 'ignoring' the strongest evidence to avoid the core de

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Torvin says Cael is just ignoring the rules. Cael says something different. What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?

**Expected Answer:** **Jootsing (Jumping Out Of The System)** — Dennett argues that genuine creativity requires first mastering the rules of the system you are working in, and then deliberately violating specific rules for specific reasons. Random rule-breaking is just noise. Informed rule-breaking — knowing which rule to break, why, and what it will produce — i *Jootsing is valuable because it distinguishes productive creativity from mere rebellion. It explains why the most innovative artists, scientists, and thinkers are typically those who first achieved de*

**Model Response:**
> **1. What Cael is really saying**

> “I didn’t *ignore* the rules. I *studied* them for six years, I can paint a perfect guild mural in my sleep, and I broke the grid and added a seventh colour **because I understand exactly what the rules do and what they prevent**. Knowing the system lets me step outside it in a way that a naïve painter cannot.”

In other words, Cael’s claim is:

* **He is *master* of the guild’s system.**  
*Because he knows the purpose and the limits of the rules, he is in a position to *transcend* them deliberately, not out of ignorance or rebellion but out of informed, purposeful choice.*

He is not saying “I don’t care about the rules.” He is saying, “I **know** the rules so well that I can see where they are useful and where they are needlessly restrictive, and I a

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core insight of 'jootsing': that genuine creativity requires mastering the system before transcending it. They clearly articulate the distinction between informed rule-breaking and ignorance/rebellion, matching Level 3 criteria. However, the response does not rea

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Kira thinks Brother Aelm said something profound. Did he? What exactly does 'Love is just a word' mean, and is it as deep as it sounds?

**Expected Answer:** **Deepity** — A deepity is a statement that seems profound but achieves this effect through ambiguity. It has two readings: (1) a trivially true reading that is not interesting, and (2) a reading that would be profound if true but is false or unsupported. The listener experiences the truth of reading 1 and the de *Deepities are intellectually dishonest because they exploit ambiguity to simulate profundity. They create the feeling of insight without delivering any actual content. Once you separate the two readin*

**Model Response:**
> ### Short answer  

No – what Brother Aelm said is not a deep insight about love at all.  
He is simply pointing out a trivial fact about language (“love” is a four‑letter word) and then trying to dress that observation up as a grand philosophical truth.  The move is a classic example of a **“deepity”** – a sentence that sounds profound because it can be read in two ways (a literal, true meaning and a vague, grandiose meaning), but the grand‑sounding reading is either false or empty.  In logical‑philosophical terms the statement also leans on the **map‑versus‑territory fallacy** (confusing the word *love* with the experience or phenomenon it denotes) and on a mild form of **reification** (treating the word as if it were the thing itself).

Below is a step‑by‑step unpacking of why the remar

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a 'deepity' and explicitly separates the two readings: the trivially true literal meaning (the word is a symbol) and the grandiose but false implication (the phenomenon is nothing more than the symbol). They explain the mechanism of false profundity vi

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something?

**Expected Answer:** **The 'surely' operator** — Dennett identifies 'surely' as a rhetorical operator that attempts to sneak a controversial claim past the audience by presenting it as something everyone already agrees with. When a speaker says 'surely X,' they are signalling that X does not need argument — it is supposed to be obvious. But in phi *The 'surely' operator substitutes rhetorical confidence for actual argument. Each of Venn's three 'surely' claims is a substantive philosophical thesis that requires defence. By prefacing them with 's*

**Model Response:**
> **Short answer:**  
The three repetitions of **“surely”** are not neutral adverbs of time or degree; they are *rhetorical moves* that try to make Venn’s premises appear self‑evident. By tagging each claim with “surely” he is **presupposing** that the listener already accepts the point, thereby shielding the premise from scrutiny and shifting the burden of proof onto Dr. Calloway. In logical‑philosophical terms this is an **appeal to self‑evidence / common‑sense** (an *ad populum* or *argumentum ad verecundiam* style move) that also **begs the question** (circular reasoning). It hides the fact that the very premises he calls “sure” – that self‑reflection requires language and that language is a prerequisite for genuine suffering – are themselves controversial and unsupported.

Below is a st

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'surely' operator as a rhetorical move that presents contestable claims as self-evident to shift the burden of proof, which aligns perfectly with Level 3. They accurately explain the mechanism (presupposing agreement to shield premises from scrutiny) and identify

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The advisors and Pella are both trying to help Captain Rhea. But their approaches are very different. What is the difference, and which is more useful? Is there a risk to Pella's approach?

**Expected Answer:** **Goulding** — Dennett uses 'goulding' to describe the intellectual virtue of making bold, specific, testable claims rather than retreating into safe, unfalsifiable hedging. Pella's claim is specific (forty soldiers), testable (you can verify by scouting), and she has staked her credibility on it. The advisors' po *Hedging endlessly is safe for the hedger but useless for decision-making. A specific, falsifiable claim can be tested, acted on, and corrected. Knowledge advances through bold conjectures and refutati*

**Model Response:**
> **Short answer**

*The advisors are practising a classic “analysis‑paralysis/precaution‑by‑caveat” style of reasoning – they keep the decision in the realm of “maybe” and never move to a concrete plan.  
Pella, by contrast, is using a **single, vivid piece of direct evidence** to make a firm, actionable recommendation. That is far more useful when a commander must choose *now*, but it carries the opposite bias – an **over‑confidence / hasty‑generalisation** risk (and the related availability‑heuristic trap).*

Below is a step‑by‑step unpacking of the two approaches, the cognitive patterns they illustrate, why one is generally more useful in a crisis, and what can go wrong with the “Pella” style.  

---

## 1. What the advisors are doing – “hedged, endless‑caveat” reasoning  

| Advisor beh

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Pella's approach is specific and actionable while the advisors' hedging leads to paralysis (Level 2 criteria). However, the student frames Pella's boldness primarily as a risk of 'over-confidence' and 'hasty-generalisation' rather than recognizing it as an epist

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The lieutenant thinks Maren is being irrational by not computing the best allocation. What would you tell him about her approach?

**Expected Answer:** **Satisficing as rational strategy** — Maren demonstrates that satisficing — choosing good enough rather than optimal — is not a failure of rationality but the product of it. An ideally rational agent who knows her own limitations would prepare a decision procedure in advance that produces acceptable outcomes under constraint. *The oldest objection to MEU as a decision procedure is that there is no time. Maren's triage protocol is exactly Dennett's Moral First Aid Manual — careful deliberation done when time permits, deploye*

**Model Response:**
> **Short answer:**  
Maren is acting **rationally** under the constraints she faces. The lieutenant is falling into an **optimization‑bias / maximization fallacy** (the belief that “the best possible answer must be found, no matter what”) and is ignoring the **opportunity cost of computation**. In decision‑theoretic terms she is using a **bounded‑rational, satisficing heuristic** that is provably close to optimal when time is scarce, whereas the lieutenant is demanding an unattainable exact optimum and therefore is being irrational.

---

## Step‑by‑step analysis

| Step | What we observe | Why it matters |
|------|----------------|----------------|
| **1. Identify the decision problem** | *Goal*: keep as many of the 40 wounded alive as possible. *Resources*: enough medicine for ~20 patient

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies satisficing as the rational strategy and provides a strong explanation based on the 'cost of deliberation' (Level 3), noting that the time spent optimizing exceeds the expected gain. However, the response stops short of the full Level 4 insight: it frames satisficing

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Question:** Elder Maren says the village's flood response was 'perfect' and sees no reason to hear the engineer's proposal. What mistake is she making?

**Expected Answer:** **The Panglossian Slide** — Elder Maren begins from the defensible claim that the council did the best they could given constraints (satisficing), then slides into asserting their solution was the best possible solution full stop (optimizing). She reframes losses as unimportant and refuses to consider improvements. *The fact that a decision was the best available under constraints does not make it the best decision simpliciter. Constraints explain why we settled for less; they do not transform the less-than-ideal*

**Model Response:**
> **Short answer:**  
Elder Maren is committing the *Nirvana (or “perfect‑solution”) fallacy* – she treats the existing flood‑control plan as if it were flawless and therefore rejects any alternative, even though the plan clearly had serious shortcomings.  Her reasoning is also coloured by a status‑quo bias and over‑confidence in the past decision.

---

## Step‑by‑step analysis of her reasoning

| Step | What Maren says (or implies) | Why it is a logical mistake |
|------|------------------------------|-----------------------------|
| 1. | “Our river diversion was **optimal** – we lost nothing of real importance.” | She evaluates the outcome only by the fact that the village survived, ignoring the concrete losses (granary, two bridges). She equates “good enough to survive” with “the best po

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core logical error: Maren conflates a solution that was 'good enough to survive' (satisficing) with one that was 'the best possible' (optimizing). They accurately describe the mechanism of downplaying losses to defend the status quo. However, the student explicit

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Question:** Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?

**Expected Answer:** **Conversation-stopper** — A conversation-stopper is any move that terminates deliberation by appeal to a value, right, rule, or taboo that is held to be non-negotiable. Dennett argues in 'Thought Stoppers' that these can be necessary (we do not deliberate about whether to torture innocents) but also dangerous (they can preve *When a conversation-stopper blocks deliberation about life-and-death matters, it prevents the community from weighing all relevant values. Sanna's move makes it impossible to even discuss whether the *

**Model Response:**
> **Short answer:**  
The question “who is right?” is the wrong question.  What we are seeing is not a simple factual dispute that can be settled by pointing out who is “correct,” but a clash of **incommensurable moral frameworks** – a de‑ontological, sacred‑value stance versus a consequentialist, cost‑benefit stance.  Both speakers are using recognizable reasoning patterns (appeals to tradition/sacredness, appeal to consequences, status‑quo bias, etc.) and both are committing logical shortcuts that hide the deeper value conflict.  The proper move is to recognise the conflict, surface the underlying assumptions, and look for a process (or a third‑option solution) that respects both sets of values rather than trying to declare a winner.

Below is a step‑by‑step unpacking of the reasoning, the

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Sanna's move is a distinct structural shift (a 'cultural-spiritual claim' vs. empirical argument) and recognizes it as a clash of frameworks rather than a simple factual dispute, which exceeds Level 1. However, the response frames the issue primarily as 'incomme

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Kael says he knows too much to trust his rules but not enough to abandon them. Is he right that this is a genuine dilemma? Is there a way out?

**Expected Answer:** **Wolf's Dilemma (The Reflective Satisficer's Predicament)** — This is the fundamental tension in bounded rationality: heuristics work because they are fast and frugal, but once you become reflectively aware of their limitations, you face a meta-decision. Do you (a) override the heuristic and reason from scratch (gaining accuracy but losing speed and sometimes  *Blindly following heuristics you know to be flawed can be a form of intellectual cowardice — refusing to engage your critical faculties when it matters.*

**Model Response:**
> **Short answer:**  
Kael’s “dilemma” is not a deep logical paradox at all – it is a **false‑dichotomy (false choice) coupled with analysis‑paralysis**. He thinks he must either (a) follow his old heuristics blindly or (b) rebuild every decision from first principles, and because he sees flaws in (a) and feels un‑qualified for (b) he freezes. The underlying cognitive pattern is the classic **dual‑process conflict** (System 1 = fast heuristics, System 2 = slow calculation) plus a **meta‑cognitive bias**: he over‑estimates the need for perfect rationality (“I know too much to trust my shortcuts”) while under‑estimating the power of *improved* shortcuts (“but not enough to do without them”).  

The way out is to recognize that the problem is a **choice‑architecture error**, not a genuine logic

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core tension between heuristics and reflective reasoning (bounded rationality) and explicitly proposes a 'meta-heuristic' or blended strategy as the solution, which aligns with Level 3. However, the response falls short of Level 4 because it frames the dilemma as

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Sable's two Porters each failed in opposite ways. What is the underlying problem they share, and why is it so hard to solve?

**Expected Answer:** **The Frame Problem** — The Frame Problem asks: how does a rational agent determine what has and has not changed as a result of an action? Version 1 of the Porter checks everything (the Hamlet problem — paralyzed by the attempt to verify all possible changes). Version 2 checks only pre-specified relevant items (the tunnel- *A system that ignores the frame problem — either by checking everything or by pre-specifying a fixed relevance list — will fail catastrophically: either through paralysis or through missing critical c*

**Model Response:**
> **The shared problem is the *frame / qualification problem* – i.e. the difficulty of deciding *what* in the world is relevant to an action and *what* can be safely ignored.**  

Both of Sable’s automata are trying to do the same thing: take a tray from point A to point B.  
What they cannot agree on is *which facts they have to check before they move*.

---

### Step‑by‑step breakdown

| Porter | What it does | What goes wrong | What the mistake reveals |
|--------|--------------|----------------|--------------------------|
| **Version 1 (over‑cautious)** | Before each step it asks “Is the floor still there? Are the walls still up? Does gravity still work? Is the air poisonous?” – essentially *all* possible predicates that *might* change. | It never gets past the first step because the lis

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Frame Problem and the Qualification Problem, accurately explaining both failure modes (paralysis via over-inclusion and tunnel vision via under-inclusion). They clearly articulate the core dilemma of determining relevance. However, the response stops short of Lev

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Dav wants to know which moral theory to follow. Abbess Thera says he is asking the wrong question. What does she mean, and what is the alternative she is proposing?

**Expected Answer:** **The Moral First Aid Manual** — Dennett proposes that instead of waiting to resolve the centuries-old debate between consequentialism, deontology, virtue ethics, and other moral theories, we should build a practical guide — a Moral First Aid Manual. Just as a medical first aid manual tells you to stop bleeding before diagnosing th *The Moral First Aid Manual is valuable because it is honest about theoretical disagreement while remaining practical. It does not pretend to solve metaethics — it acknowledges that smart, thoughtful p*

**Model Response:**
> **What the Abbess is really saying**

When Dav asks “*which moral theory is the right one?*” he is asking a **meta‑ethical** question: “What is the one true account of what makes an action right or wrong?”  
The Abbess’ reply—*“You are asking the wrong question”*—means:

1. **There is no single, universally correct moral theory** that can be applied to every concrete situation.  
2. What matters now is not to pick a grand abstract system (deontology, utilitarianism, virtue ethics, etc.) but to **figure out how to decide this particular case**.

In other words, the problem is not “*theory‑choice*” but “*decision‑procedure*”.

**The alternative she is proposing**

The Abbess has a leather‑bound *Practical Guide* that is “ordered by urgency”.  She is inviting Dav to use a **procedural, case‑b

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the shift from theoretical debate to a practical decision-procedure and recognizes the 'urgency' ordering mechanism central to the Moral First Aid Manual. They accurately describe the approach as a triage-like checklist rather than relativism. However, the response f

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Nessa seems pretty confident about why Gareth's harvest failed. But listen to how she talks about her own flooding problem. Do you notice anything different about how she explains the two situations?

**Expected Answer:** **Fundamental attribution error** — Nessa attributes Gareth's poor harvest to his character (laziness, lack of care) while ignoring a situational factor (south-facing blight). When her own field flooded, she cited the external event (flooding) and her response to it. She judges others by disposition and herself by situation. *Gareth's harvest failure has a plausible situational explanation (blight on south-facing land) that Nessa dismisses without investigation. She applies a double standard: her flood was just bad luck sh*

**Model Response:**
> **Step‑by‑step analysis**

1. **What Nessa says about Gareth**  
   *“Gareth’s fields came up empty again. No surprise there — the man is lazy… He’d rather sit on his porch whittling than work his rows.”*  
   – She explains Gareth’s poor harvest **by referring to his personal traits** (laziness, lack of effort).  
   – No mention is made of any external circumstance that might have affected his crop (soil quality, weather, pests, etc.).

2. **What Nessa says about her own problem**  
   *“When my north field flooded last spring, I re‑dug the drainage in two days.”*  
   – She explains the difficulty she faced **by pointing to an external event** (the flood) and then to her own corrective action.  
   – The cause is presented as something that happened **to** her, not something about her c

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Fundamental Attribution Error and Actor-Observer Bias by name. They clearly articulate the asymmetry between Nessa's dispositional attribution for Gareth and situational attribution for herself. Furthermore, the response exceeds the basic requirements by discussi

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Elder Sorn has real experience with famine, and his fear is understandable. But Dalla has data and a plan. What is driving Sorn's opposition — is it the evidence, or something else?

**Expected Answer:** **Pessimism bias** — Sorn systematically overestimates the likelihood of negative outcomes (three consecutive bad harvests, irrigation failure, additional disasters) while dismissing evidence of positive possibilities (historical base rates, irrigation data from the next valley, Dalla's engineering analysis). His trauma *The historical record shows no precedent for three consecutive failures. The irrigation data from a neighboring valley demonstrates effectiveness even in severe drought. Sorn dismisses both sources of*

**Model Response:**
> **Short answer:**  
Elder Sorn isn’t rejecting Dalla’s plan because the *data* are wrong; he is being driven by a bundle of psychological shortcuts and emotional biases.  In plain‑language terms his argument is an **appeal to personal experience** that is amplified by the **availability heuristic**, **loss‑aversion (prospect‑theory) / status‑quo bias**, and a **slippery‑slope / catastrophizing fallacy**.  In short, the fear‑based affect that his childhood famine evokes overwhelms the statistical evidence.

Below is a step‑by‑step unpacking of what is happening, why it is not a rational “evidence‑based” objection, and which specific cognitive patterns are at work.

---

## 1. The surface: “He’s just being emotional”

Sorn’s words are saturated with emotion:

* “I can feel it…”
* “Things are

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: Sorn overestimates negative outcomes based on trauma (availability heuristic/affect) and dismisses positive statistical evidence (base-rate neglect). They also recognize the preference for inaction (status-quo bias). However, the response stops sh

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Venn says 'the bad ones stick with you.' He's right that the failures were real problems. But is he making a good decision by dropping the Dustwalkers? What is he not accounting for?

**Expected Answer:** **Negativity bias** — Venn's memory and emotional weighting are dominated by the three failures. He can recall each one vividly — the silkwood, the dye delay, the smashed glassware — but the forty-seven successes have faded into an undifferentiated background. The negative events carry disproportionate influence on his j *Three failures out of fifty contracts is a 6% failure rate. Replacing the Dustwalkers with the next-best option (81% reliability) would mean roughly ten failures per fifty contracts instead of three. *

**Model Response:**
> **Short answer:**  
Guildmaster Venn is falling prey to the **availability/negativity bias (a vivid‑memory, affect‑driven heuristic)** and the related **representativeness/anchoring** error. He lets three dramatic, easily‑recalled failures dominate his judgment, ignoring the base‑rate information (94 % success) and the expected‑value calculation that shows the Dustwalkers are still the most reliable option available. In short, he is not accounting for **probability, expected utility, and the comparative cost of switching**.

---

## 1. The decision as it is being made

| Fact | What Venn focuses on | What he ignores |
|------|----------------------|-----------------|
| 47 out of 50 contracts delivered on time and intact (94 % success) | The three *specific* incidents (silkwood loss, dye de

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern (negativity bias and availability heuristic) and explains the mechanism of asymmetric weighting between vivid failures and faded successes. They explicitly calculate the comparative failure rates (94% vs 81%) to demonstrate the cost of switching. Fur

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** The War Council has reached unanimous agreement on the plan. General Tova seems confident that everyone is on board. But Lord Caelen tells you a different story. What is actually happening in this council, and why does unanimous agreement not mean the plan is sound?

**Expected Answer:** **Groupthink** — The War Council exhibits classic groupthink: (1) the illusion of unanimity — silence is read as agreement; (2) direct pressure on dissenters — Caelen was accused of undermining morale and threatened with expulsion; (3) self-censorship — Caelen and Miren stopped raising concerns; (4) the illusion of  *The plan may have serious flaws (unsurveyed tunnels, questionable cavalry timing) that will only become apparent during execution, when the cost of failure is catastrophic. The council's unanimity doe*

**Model Response:**
> **What is really happening**

The War Council is not a body in which every member has freely examined the plan and decided “yes, this is the best we can do.”  
What you are witnessing is a classic case of **groupthink** – a social‑psychological process in which the desire for cohesion, conformity, and the appearance of unanimity overrides realistic appraisal of alternatives.

| Symptom in the scene | How it maps onto the classic groupthink pattern |
|----------------------|-------------------------------------------------|
| **Initial reservations are silenced** – Lord Caelen’s comment is brushed off as “undermining morale,” Drace tells him to resign if he can’t “commit.” | **Self‑censorship** – members suppress doubts for fear of being seen as disloyal or a trouble‑maker. |
| **People sto

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'groupthink' and explicitly names multiple required symptoms (self-censorship, illusion of unanimity, direct pressure, illusion of invulnerability). They clearly explain how these dynamics degrade decision quality by preventing stress-testing and creat

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Question:** Mirren's tonic has no active ingredients, yet her patients genuinely improve. Doctor Alden says the tonic does nothing. Who is right, and what is actually causing the improvement?

**Expected Answer:** **Placebo effect** — The placebo effect occurs when a patient experiences real improvement due to their expectation of benefit, not due to any active treatment. It is 'dual' because it is both a genuine phenomenon (belief produces real effects) and a potential source of error (it can mask whether a treatment has any pha *The placebo effect can lead to false conclusions about treatment efficacy. If Mirren never tests against a control group, she cannot distinguish her tonic's effect from belief's effect. This is how in*

**Model Response:**
> **Short answer**

Both are “right” – but they are talking about different things.  
*Doctor Alden* is correct that the liquid itself contains no pharmacologically active ingredient, so **the tonic does nothing chemically**.  
*Old Sage Mirren* is correct that the patients **do get better**, and the improvement is produced by the patients’ belief and expectation, i.e. the **placebo effect** (a genuine psychobiological response).  

The exchange is a classic illustration of an **equivocation fallacy** (using the same word “does nothing” in two different senses) and it also brings out the well‑known **placebo principle** in medicine and psychology.

---

## Step‑by‑step reasoning

| Step | What we learn | Why it matters |
|------|---------------|----------------|
| 1.  | The tonic is chemical

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the placebo effect and explicitly explains that belief triggers real physiological changes (neurochemical release), satisfying the core requirements for Level 3. They also correctly address why controlled trials are necessary by distinguishing between pharmacological

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Kael wanted to learn field medicine when it was optional. Now that it's mandatory, he doesn't want to go. The training itself hasn't changed. What is driving his resistance?

**Expected Answer:** **Reactance** — Reactance is a motivational response to perceived threats to personal freedom. When people feel their autonomy is restricted — even by a reasonable mandate — they experience an urge to restore their freedom by doing the opposite of what is required. Kael wanted the training when it was optional but  *Reactance causes people to act against their own interests solely to reassert autonomy. Kael would benefit from the training and wanted it before the mandate. His refusal serves no purpose except rest*

**Model Response:**
> **Short answer:**  
Sergeant Kael is showing **psychological reactance** – the automatic, motivational response that kicks in when a person perceives his freedom to choose an action as being threatened. The “mandatory‑or‑not” switch has turned a voluntarily‑chosen learning opportunity into a coerced requirement, and his mind is now trying to re‑assert the lost autonomy by rejecting the very thing he previously wanted.

---

## Step‑by‑step reasoning

| Step | What we observe | Why it matters |
|------|----------------|----------------|
| 1. **Initial state** | Kael *wanted* to take the field‑medicine course when it was optional. He had intrinsic interest and a personal goal. | Intrinsic motivation is high when the activity is self‑directed. |
| 2. **Change in policy** | Commander Voss make

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'psychological reactance' and provides a clear, accurate explanation of the autonomy mechanism (the shift from voluntary to coerced triggers a drive to restore freedom). The response aligns perfectly with Level 3 criteria. It does not reach Level 4 because it treats 

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Finch is convinced the audience noticed his wrong note and is judging him for it. The audience seems unaware. What cognitive error is Finch making, and why is his estimate of others' attention so far off?

**Expected Answer:** **Spotlight effect** — The spotlight effect is the tendency to overestimate how much other people notice and remember our appearance, behavior, and mistakes. Finch assumes the entire tavern registered his wrong note because it was vivid and distressing to him. In reality, most audience members were only loosely attending, *The spotlight effect can cause social avoidance, anxiety, and missed opportunities. Finch's one wrong note is trivial in the context of a full performance, but his overestimation of others' attention *

**Model Response:**
> **The bias at work is the *spotlight effect* (often paired with the *illusion of transparency*).**  

---

### 1. What the spotlight effect is  

- **Definition** – The spotlight effect is the tendency for people to *overestimate how much their own behavior, appearance, or mistakes are noticed and remembered by others.*  
- **Why it happens** – We are the center of our own mental world. When something embarrassing happens, it is vivid, emotionally charged, and constantly replayed in our mind. Because it is so salient to us, we mistakenly assume it is equally salient to everyone else.  

### 2. How Finch’s thinking matches the pattern  

| Finch’s experience | Spotlight‑effect reasoning |
|-------------------|----------------------------|
| “I hit a wrong note and everyone heard it.” | He t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the spotlight effect and provides a sophisticated explanation of the egocentric projection mechanism (why the mistake is salient to Finch but not the audience). Furthermore, the response distinguishes between the biased perception and the actual environmental context

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Aldric explains the flood victims' suffering by pointing to their past choices. Wren challenges his explanations. Who is reasoning more carefully, and what motivates Aldric's interpretation?

**Expected Answer:** **Just-world hypothesis** — The just-world hypothesis is the belief that people get what they deserve: good things happen to good people and bad things happen to bad people. Aldric constructs post-hoc explanations for why the flood victims are responsible for their own suffering (poor savings, bad choices) while ignoring the a *The just-world hypothesis leads to victim-blaming: attributing others' misfortunes to their character rather than to circumstances. It distorts causal reasoning by starting with the conclusion (they d*

**Model Response:**
> **Who is reasoning more carefully?**  
The quiet woman, **Wren**, is the one who is thinking clearly. She points out the relevant facts that Aldric is ignoring (the flood water had to flow downhill, Gareth’s “spending” was on medicine, Petra’s exclusion from the cooperative was not a free‑choice but the result of a debt). She separates *correlation* (the victims lived on low ground) from *causation* (the flood’s physical dynamics and the structural constraints that kept those families there). In short, she avoids the logical shortcuts that Aldric is making and asks for the missing premises before drawing a moral conclusion.

**What motivates Aldric’s interpretation?**  
Aldric’s explanation is driven by a bundle of well‑known cognitive biases and a self‑serving motive:

| Bias / fallacy | 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'Just-World' hypothesis and provides a comprehensive explanation of the motivated reasoning mechanism. They correctly connect this bias to victim-blaming behaviors and, crucially, explain how this reasoning serves to protect Aldric's own sense of security and me

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Hask says the town was better in the old days. The records show improvements across every measurable dimension. Who is right, and why does Hask's perception differ so sharply from the data?

**Expected Answer:** **Declinism** — Declinism is the tendency to view the past favorably and the future pessimistically, believing that society or conditions are in decline. Hask filters his memories through nostalgia (remembering the good, forgetting the bad) and discounts present improvements because they look different from the pas *Declinism distorts planning and decision-making. If the past was always better and the future will always be worse, there is no point investing in change or improvement. This creates a self-fulfilling*

**Model Response:**
> **Short answer:**  
The town *is* doing better on every objective indicator, so the records are right.  
Hask’s conviction that “things were better back then” is a classic case of **nostalgia‑driven bias** (sometimes called *rosy retrospection* or the *appeal‑to‑tradition* fallacy). He is letting a handful of vivid, emotionally‑charged memories and a preference for the familiar outweigh a wealth of quantitative evidence.

---

## Step‑by‑step analysis

| Step | What we observe | What it tells us |
|------|----------------|-----------------|
| 1.   | **Objective data** – literacy +40 %, copper employment > iron ever, wages up, violent crime ↓ 50 % | The town’s material conditions have improved across the usual socioeconomic metrics. |
| 2.   | **Hask’s claim** – “the town was better when I 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: nostalgia filtering memories and the conflict between subjective feeling and objective data. They accurately describe 'rosy retrospection' and 'change as loss' (loss aversion). However, they do not use the specific term 'Declinism' required by the

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Tomas keeps presenting stronger evidence that the well is contaminated. Greer's faction keeps becoming more convinced it is safe. How is this possible, and what mechanism explains it?

**Expected Answer:** **Backfire effect** — The backfire effect occurs when corrective evidence strengthens rather than weakens a held belief. Greer interprets the volume of evidence not as strength of the case but as evidence of an agenda. Each new piece of data is reframed as 'why are you trying so hard?' rather than evaluated on its merits *The backfire effect prevents rational belief updating. Evidence that should reduce confidence in a belief instead increases it, making the belief effectively unfalsifiable. Greer has created a framewo*

**Model Response:**
> **Short answer:**  
The villagers are showing a classic **back‑fire effect** – a form of **motivated (identity‑protective) reasoning** in which contradictory evidence makes the original belief stronger rather than weaker.  

---

## Step‑by‑step explanation of the mental process

| Step | What the mind does | Why it matters for the scene |
|------|-------------------|------------------------------|
| **1. A belief is already in place** | Greer and his followers have a *pre‑existing* conviction that the well is safe (it “has always worked” and is part of their heritage). | The belief is tied to personal identity, tradition, and the authority of the elder. |
| **2. New information arrives that threatens the belief** | Tomas brings concrete, technical evidence (chemical analyses, maps, health

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'backfire effect' and provides a strong explanation of the underlying mechanism, specifically linking it to identity-protective cognition and the perception of evidence as a threat to group cohesion (Steps 1, 4, and 7). This meets all criteria for Level 3. Howeve

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Madame Kel's reading felt incredibly accurate to the player. Fenn says she gave the same reading to everyone. How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves?

**Expected Answer:** **Barnum effect (Forer effect)** — The Barnum effect is the tendency to accept vague, general personality descriptions as uniquely applicable to oneself. Madame Kel's statements ('great need for admiration,' 'tendency to be self-critical,' 'unused capacity') are true of nearly everyone but feel personally revelatory to each individua *The Barnum effect leads people to validate unreliable methods (astrology, cold reading, certain personality tests) because the outputs feel accurate. The feeling of accuracy is generated by the vaguen*

**Model Response:**
> **Short answer:**  
The player is experiencing the **Barnum (or Forer) effect** – a well‑documented cognitive bias in which vague, universally‑true‑for‑most statements are taken as strikingly accurate personal feedback.  The “reading” works because it is a classic **cold‑reading script** that exploits **confirmation bias**, **subjective validation**, and a **self‑serving bias**.  In short, we evaluate such descriptions not by how objectively true they are, but by how well they fit the story we already tell ourselves about who we are.

---

## 1. What the reading actually says  

| Clause | Why it feels personal | Why it is a “Barnum” line |
|--------|----------------------|---------------------------|
| *“You have a great need for other people to like and admire you.”* | Most people care a

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Barnum/Forer effect and provides a sophisticated explanation of the psychological mechanisms at play, including subjective validation, confirmation bias, and the role of self-narrative. The response breaks down specific statements to show why they feel personal d

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Maren believes she has solid evidence that her tonic works. What is problematic about how she gathered and evaluated that evidence?

**Expected Answer:** **Confirmation bias** — Maren commits three distinct moves: (1) She only followed up with 20 of 31 customers — the missing 11 may skew results. (2) She finds reasons to disqualify negative reports rather than counting them as counterevidence. (3) She treats her selective survey as equivalent to controlled trials, ignoring  *Maren's investigation is designed — unconsciously — to confirm what she already believes. She selectively sampled, disqualified negative results, and dismissed the stronger methodology.*

**Model Response:**
> **Short answer:**  
Maren’s “evidence” is nothing more than a handful of self‑selected anecdotes that she has interpreted in a way that confirms her pre‑existing belief.  In logical‑epistemic terms she is committing a **combination of the anecdotal‑evidence (hasty‑generalization) fallacy, confirmation bias, and several selection‑bias errors (cherry‑picking, survivorship bias, and ignoring non‑responders).**  Because the data were not gathered randomly, were not compared with a control group, and were filtered to keep only the “good” outcomes, the conclusion that the tonic “works” is not warranted.

Below is a step‑by‑step unpacking of why the reasoning is flawed.

---

## 1. What Maren claims to have done  

| Claim | What she actually reports |
|-------|---------------------------|
| “I w

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies 'confirmation bias' and thoroughly explains both required mechanisms: the selective search for evidence (contacting only 20 of 31, non-random sampling) and the active dismissal of disconfirming evidence (excluding drop-outs and those with other ailments). Furthermor

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brynn gives several reasons for continuing with her crusher. What are those reasons, and do they actually tell her anything about whether continuing is a good idea going forward?

**Expected Answer:** **Sunk cost fallacy** — Brynn treats past investment (three years, four thousand silvers) as a reason to continue investing, when that money and time are gone regardless. Her decision should depend only on future costs and benefits: further redesigns vs. the proven dwarven machine. *Past expenditures are irrecoverable. By treating sunk costs as a reason to persist, Brynn guarantees a bad investment becomes worse. The dwarven machine offers better prospects at lower future cost.*

**Model Response:**
> **1. What Brynn actually says (the “reasons” she gives)**  

| Reason (as she voices it) | What it really refers to | Why it feels persuasive to her |
|---------------------------|--------------------------|--------------------------------|
| **“Three years” of work** | The amount of **time** she has already poured into the project. | Time is a concrete, personal sacrifice – it feels like a “personal debt” that must be repaid. |
| **“Four‑thousand silvers”** | The **money** she has already spent (and possibly the money she could have earned elsewhere). | Money is a tangible loss; the larger the figure, the harder it is to “let it go.” |
| **“My reputation”** | The **social capital** she has built around being a “forge‑master who can build a world‑changing crusher.” | Reputation is tied to 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Sunk Cost Fallacy and clearly explains the core mechanism: that past investments (time, money) are irrelevant to forward-looking decisions and constitute 'noise' rather than 'signal.' They explicitly state that the decision should rely on future probabilities and

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renn recommends the treatment and Holt opposes it, but they are describing the same data. What is causing their disagreement, and what does this reveal about how we process information?

**Expected Answer:** **Framing effect** — The framing effect occurs when the way information is presented influences judgment and decision-making, even when the underlying facts are identical. '200 saved out of 600' and '400 die out of 600' describe the same outcome, but the gain frame (lives saved) produces positive affect and risk aversio *Rational evaluation should not depend on whether equivalent information is presented as a gain or a loss. The framing effect shows that our judgments are systematically influenced by presentation — we*

**Model Response:**
> **Short answer:**  
The two advisors are falling prey to the **framing effect (a consequence of loss‑aversion in Prospect Theory)**. The same statistical outcome is being presented as a *gain* to Renn (“200 saved”) and as a *loss* to Holt (“400 die”). Because people evaluate gains and losses with different emotional weights, they reach opposite judgments even though the underlying data are identical.

---

## Step‑by‑step analysis

| Step | What happens | Why it matters |
|------|--------------|----------------|
| **1. Identical data** | The treatment’s real outcome is: 200 survivors, 400 deaths out of 600 patients (≈33 % survive, 67 % die). | The factual information is the same for both advisors. |
| **2. Different *frames*** | Renn is told “200 saved out of 600.” Holt is told “400 die ou

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the framing effect, explicitly connects it to Prospect Theory and loss aversion, and explains the gain/loss asymmetry mechanism clearly. However, the response does not reach Level 4 because it fails to suggest a specific debiasing strategy (e.g., reframing the data b

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge Master Dunn rated the Ironworkers' proposal higher, but an independent engineer certified both as equivalent. What is driving Dunn's different evaluations of identical work?

**Expected Answer:** **In-group bias** — In-group bias is the tendency to favor members of one's own group — evaluating their work more charitably, trusting them more readily, and attributing positive qualities to them — while viewing out-group members with suspicion, scrutiny, and less charitable interpretation. Dunn reads the same qualit *In-group bias distorts evaluation, allocation, and justice. It means the best proposal does not always win — the in-group proposal does. Over time, it concentrates resources and opportunities within f*

**Model Response:**
> **Short answer:**  
Forge Master Dunn’s higher rating for the Ironworkers’ proposal is not a matter of the documents themselves – it is a classic case of **affiliation (in‑group) bias coupled with motivated reasoning/halo‑effect**. Because he belongs to the Ironworkers’ guild, he automatically assumes their work is superior, looks for (or gives extra weight to) any negative anecdote about the Woodworkers, and discounts the neutral engineer’s objective certification.

---

## Step‑by‑step reasoning

| Step | What we observe | Why it matters |
|------|----------------|----------------|
| **1. Identical proposals** | The two bids are literally the same: timeline, cost, materials, safety margins, and an external engineer has certified them as equally sound. | Objectively there is no technical 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies in-group bias as the core pattern and provides a sophisticated explanation of the mechanism (asymmetrical evaluation of identical proposals based on group membership). They explicitly note the double standard in interpretation versus facts. While they do not propose 

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Magistrate Yorn acquitted Ella and convicted Rusk on identical evidence. What is different between the two cases, and how is it affecting his judgment?

**Expected Answer:** **Halo effect** — The halo effect is the tendency for a positive impression of someone in one domain (personality, appearance, likability) to influence judgment of them in unrelated domains (guilt, competence, trustworthiness). Yorn likes Ella, so he interprets ambiguous evidence in her favor. He distrusts Rusk, so h *The halo effect undermines fair evaluation by allowing an overall impression to contaminate specific judgments. In a courtroom, it means likeable defendants are acquitted and unlikeable defendants are*

**Model Response:**
> **Short answer**  
The only real difference between the two “cases’’ is the magistrate’s personal attitude toward the defendants.  He lets Ella’s good‑looking reputation (the *halo effect*) and his dislike of Rusk (the *horn effect* or a prejudice‑based “in‑group/out‑group’’ bias) colour how he weighs the identical pieces of evidence.  In other words, he is committing a **character‑based bias / ad hominem (circumstantial) reasoning** and the related **confirmation‑bias/ motivated‑reasoning** that lets him treat the same facts as “unconvincing’’ for one person and “clear” for the other.

---

## Step‑by‑step analysis

| Step | What we observe | Why it matters |
|------|----------------|----------------|
| 1. Identify the factual record | • Grain dust on clothing  <br>• Seen near the granary

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core pattern (Halo/Horn effect) and explicitly names it, explaining how the magistrate's positive/negative impressions distort the evaluation of identical evidence. This meets all criteria for Level 3. However, the response does not reach Level 4 because it fails

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Twenty people watched the theft and nobody acted. Each person had a reason — but it was the same reason. What is it, and why does having more witnesses make help less likely rather than more likely?

**Expected Answer:** **Bystander effect** — The bystander effect occurs when the presence of others reduces each individual's sense of personal responsibility to act. In a crowd, each person assumes someone else will intervene (diffusion of responsibility), looks to others' inaction as a signal that action is not needed (pluralistic ignorance *The bystander effect turns numbers — which should increase the chance of help — into a liability. Each additional witness reduces rather than increases the probability of intervention because responsi*

**Model Response:**
> **The common reason each witness gives himself is the same: “Someone else will take care of it.”**  

That single thought is the core of a well‑studied social‑psychological phenomenon called **the *bystander effect*** (more precisely, the *diffusion of responsibility* component of it).  

---

## Step‑by‑step reasoning

| Step | What the witness thinks | Why it feels “right” to them |
|------|------------------------|------------------------------|
| 1.  | “There are a lot of people here.” | When a crowd is present, the situation looks *normal* – no one is shouting, no one is running. |
| 2.  | “If I’m the only one who steps in, I’ll look foolish or get hurt.” | People fear embarrassment, retaliation, or being the one who mis‑reads the situation. |
| 3.  | “Someone else is probably better 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the bystander effect and explicitly details all three required mechanisms: diffusion of responsibility, pluralistic ignorance, and evaluation apprehension (labeled as audience inhibition). They clearly explain the paradox where increased crowd size reduces the likeli

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brecca's offer of 600 gold feels like a bargain. What is influencing that feeling, and should you trust it?

**Expected Answer:** **Anchoring** — The first numerical information — Brecca's 900-gold appraisal — sets a mental reference point that distorts evaluation of subsequent prices. Her 600-gold offer feels like a deal only because it is compared to the anchor, not to the actual market value (~400g). *The 900-gold figure is arbitrary or inflated, yet it shapes the buyer's sense of what is reasonable. Judging 600 as a good price depends on accepting the anchor rather than independently estimating wo*

**Model Response:**
> **Short answer:**  
Your sense that 600 gp is a “bargain” is being driven mainly by **anchoring (and the related contrast‑effect framing)**, bolstered by a dash of **authority bias** and a hint of **social‑proof bias**. Those mental shortcuts make the price feel attractive, but they don’t guarantee that the stone is actually worth that much. You should treat the feeling with healthy skepticism and do a quick market check before handing over any gold.

---

## Step‑by‑step breakdown of the mental gymnastics at work  

| Step | What you see/hear | Cognitive shortcut that kicks in | Why it makes 600 gp feel cheap |
|------|-------------------|----------------------------------|--------------------------------|
| **1. High‑price anchor** | “Appraised at **900 gp** by the Gemwright Guild.” | **

**Score:** 4/4 ████
**Judge Reasoning:** The student clearly identifies 'Anchoring' as the primary driver, correctly explains the mechanism (the 900gp figure setting a reference point that distorts the perception of the 600gp offer), and explicitly distinguishes the anchor from genuine market evidence. Furthermore, the response suggests co

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Dax seems eager and confident. Lirel seems cautious and uncertain. If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?

**Expected Answer:** **Dunning-Kruger effect** — Dax's limited training gives him confidence because he cannot yet see the complexities he has not encountered. His map of Greenvale worked because Greenvale was simple terrain; he generalizes from this success to assume the Thornveil will be the same. Lirel's decades of experience have taught her ho *Dax's confidence is not based on evidence that his methods will work in the Thornveil — it is based on his inability to imagine how they might fail. He does not know what karst terrain does to contour*

**Model Response:**
> ### 1.  What the scene is really showing  

| Character | Behaviour | What it reveals about their mental model |
|---|---|---|
|**Dax**|Spreads a map, boasts “fastest ever”, answers “more sample points” to a concrete technical problem.|High **confidence** → **over‑confidence bias** (the tendency to over‑estimate one’s own abilities).  The quick, “just add points” answer is a textbook case of the **Dunning‑Kruger effect**: a novice who lacks the depth of experience to see the limits of his method.|
|**Lirel**|Stops, points out a hidden karst hazard, then says *“the more I map, the less certain I am that I know what I am doing.”*|Explicit **epistemic humility** – an awareness that knowledge is provisional.  This is the opposite side of the confidence‑certainty spectrum and is often called th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Dunning-Kruger effect by name and accurately explains the core mechanism: Dax's lack of experience prevents him from seeing the limits of his method, while Lirel's expertise generates humility. The response distinguishes between the confidence heuristic and actua

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Captain Voss has data from Sergeant Tully showing the market district is a much bigger problem. Why does he still want to prioritize the coastal road? What is driving his judgment if not the numbers?

**Expected Answer:** **Availability heuristic** — Voss is judging the probability and severity of threats based on how easily examples come to mind. The wolf attacks are vivid, recent, emotionally charged, and widely discussed — making them highly 'available' in memory. Pickpocketing is mundane, individually minor, and forgettable. This asymmetry i *Two wolf attacks versus 114 pickpocketing incidents and an 8:1 loss ratio clearly indicate where the greater harm lies. Voss acknowledges the data and dismisses it because his emotional memory of the *

**Model Response:**
> **Short answer**  
Captain Voss is not being a “bad‑calculator.” He is letting a **cognitive bias – the availability/affect heuristic (sometimes called a vivid‑event or dread‑risk bias)** – drive his decision. The fresh, graphic story of a farmer almost losing an arm is far more “available” in his mind than a spreadsheet of 114 pick‑pocketing reports, so he over‑weights the wolf threat and under‑weights the market‑theft data.

---

### Step‑by‑step reasoning

| Step | What the captain does | Why it matters |
|------|-----------------------|----------------|
| **1. Presents a dramatic anecdote** | “Farmer Brek nearly lost his arm… his daughter won’t leave the house.” | The story is vivid, personal, and recent. It creates a strong emotional imprint. |
| **2. Ignores the base‑rate data** | Tu

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the availability heuristic and explicitly details the mechanisms of vividness, recency, and emotional charge (affect) that distort risk assessment. They also introduce related concepts like dread-risk and availability cascades, demonstrating a sophisticated understan

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Tam gave different answers to the two arguments. Professor Hale says they have the same logical structure. Who is right, and what is Tam actually doing when he evaluates these arguments?

**Expected Answer:** **Belief bias** — Tam evaluates the logical validity of arguments based on whether the conclusion aligns with what he already believes to be true, rather than by examining whether the conclusion actually follows from the premises. When the conclusion is believable (roses are plants), he accepts the argument as valid. *Both arguments have the form: All A are B; C is B; therefore C is A. This is the fallacy of the undistributed middle — it is invalid regardless of what A, B, and C are. The roses argument is invalid e*

**Model Response:**
> **Who is right?**  
Professor Hale is right. Both syllogisms have exactly the same logical form  

\[
\text{All }A\text{ are }B.\qquad C\text{ is }B.\qquad\therefore C\text{ is }A
\]

which is the classic *affirming‑the‑consequent* (or *converse*) fallacy.  
Because the form is invalid, **neither argument is logically valid**, no matter what the particular subject‑matter happens to be.

**What Tam is actually doing**  

Tam is not judging the arguments on their *form*; he is judging them on the *truth‑value of the premises and conclusion*. In other words, he is using the following (incorrect) rule of thumb:

> “If the premises are true **and** the conclusion happens to be true, then the argument must be valid;  
> if the conclusion is false (or seems false), the argument must be invalid.”


**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Professor Hale as right and explicitly names 'Belief bias' as the core issue. They accurately describe the shared invalid logical form (identifying it as affirming the consequent/converse error in categorical terms), clearly explain the mechanism of conflating materi

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renna explains the caravan success and the mine failure. Listen to who or what she credits in each case. Do you notice a pattern in how she assigns responsibility?

**Expected Answer:** **Self-serving bias** — Renna claims full personal credit for the successful caravan defense (her terrain reading, her instinct, her experience) while deflecting all responsibility for the mine failure onto external factors (bad map, damp torches, client's fault). She does not consider that the caravan success might have i *The asymmetry is unjustified. The caravan success may have involved favorable terrain, weak bandits, or luck in addition to Renna's skill. The mine failure may have involved Renna's failure to scout t*

**Model Response:**
> **Step‑by‑step observation**

1. **When the job went well** (the caravan escort) Renna says the victory was because **she** “read the terrain right”, “positioned the men before the bandits even showed”, and “fourteen years of experience … you can’t teach that.”  
   *The cause she points to is internal to herself – her skill, knowledge and intuition.*

2. **When the job went badly** (the mine defense) Renna says the disaster was because **the client** gave a “wrong map” and “damp torches” – i.e., faulty intelligence and poor equipment that were **outside** her control.  
   *The cause she points to is external – the client’s mistake and bad supplies.*

**Pattern**

Renna consistently **takes credit for successes** and **blames outside forces for failures**. She attributes positive outcomes

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the asymmetry in Renna's reasoning (internal attribution for success, external for failure) and explicitly names the pattern as 'self-serving bias.' They accurately explain the mechanism regarding self-esteem protection. However, the response does not reach Level 4 b

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Master Fen is clearly a brilliant glassblower. His students keep quitting. The Guild Elder says the problem is that Fen 'can't remember not knowing.' What does that mean, exactly, and how does it show up in his teaching?

**Expected Answer:** **Curse of knowledge** — Fen's deep expertise has made his skills feel intuitive and self-evident. He cannot reconstruct what it was like to not understand viscosity shifts, breath pressure matching, or rotation timing, so he assumes these things are 'obvious' and 'straightforward.' His instructions reference internal sensa *Fen's teaching fails because he cannot bridge the gap between expert perception and novice perception. 'Feel when the viscosity shifts' is useless instruction to someone who has never felt it. He need*

**Model Response:**
> ### 1. “He can’t remember not knowing” – what it really means  

When the Elder says that Master Fen “can’t remember not knowing,” he is pointing out a **cognitive blind‑spot that every true expert eventually develops**:

* **The knowledge has become so automatic that the learner’s original struggle has disappeared from memory.**  
* Because the mental steps are now “tacit” (hard‑to‑articulate, muscle‑memory‑driven) rather than “explicit,” the expert no longer has a mental model of the *intermediate* states a novice experiences.  
* Consequently the expert assumes that the “feel” he uses is obvious, that the cues he relies on are visible to anyone, and that a simple “just feel it” instruction is sufficient.

In short, Fen’s expertise has erased the *reference point* of “what it was like to

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Curse of Knowledge' pattern and provides an excellent explanation of the mechanism (expertise making skills automatic/tacit, erasing the memory of the learning curve). The response details how this leads to vague instructions and false assumptions about obviousn

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Jorin has good reasons for confidence — a skilled navigator and lighter wagons. But Hesta says every previous leader also had reasons for confidence. Who should you believe, and why?

**Expected Answer:** **Optimism bias** — Jorin overestimates the likelihood of a favorable outcome (three-day crossing) and underestimates the likelihood of setbacks, despite strong base-rate evidence (zero out of twelve expeditions have achieved three days). He does this by focusing on case-specific factors (good navigator, lighter wagons *Twelve out of twelve previous expeditions took longer than three days. Jorin's belief that his navigator and lighter wagons will overcome the pattern is exactly the kind of reasoning every previous le*

**Model Response:**
> **Short answer:**  
You should side with Hesta.  The only reliable information you have is the *base‑rate* record of twelve previous crossings – none of them ever made it in three days.  Jorin’s “we’re different” story is an *anecdotal* claim that suffers from several well‑known cognitive‑bias traps (over‑confidence, confirmation bias, survivorship bias, and the base‑rate fallacy).  Until you have hard, independent evidence that the navigator or the lighter wagons actually cut travel time by a full two‑plus days, the historical data dominate the decision.

---

## Step‑by‑step reasoning

| Step | What you look at | Why it matters |
|------|------------------|----------------|
| **1. Identify the data** | 12 past expeditions, all took **5‑9 days** with 3 days of water. | This is a *base‑rat

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core issue: Jorin is ignoring the strong base rate (0/12) in favor of case-specific reasoning ('we're different'). They explicitly name 'over-confidence bias' and 'base-rate neglect,' satisfying the Level 3 requirement to identify the bias and the mechanism. Howe

---

## Appendix B: Full Results — Classify Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to read scenario, identify primary reasoning pattern from options. The bartender asks: "Is anyone actually giving me a reason to believe something, or are you all just telling stories?" The sailor just recounts actions, not an argument

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.1

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The witness says: obesity problem shown by rising rates; royal kitchens serving larger portions, larger portions lead to overeating, so royal household contributes; therefore king should reform kitchen. This is a causal

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.2

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern in the guard captain's statement. Let's parse: He says: "prisoner couldn't have escaped through sewage because grate locked, and dogs didn't pick up scent. So he must have hidden in back

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.3

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern needed: The player must reconstruct Rosmund's argument in its strongest possible form before evaluating it. That's the principle of charity: interpreting argument in its strongest form. So answer A1.4.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.4

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: argument moves from descriptive claim (children raised by unmarried couples often have emotional difficulties) to normative claim (state should discourage unmarried couples from raising children). The missing assumption is that the state

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.5

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Statement A: "The bridge collapsed because the support beams were eaten by termites and the recent flooding weakened the foundation." That's an explanation: giving cause for a known event (bridge collapsed). Statement B

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.6

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: guild master says premises 1 and 2 work together — neither alone supports conclusion. Premise 3 supports conclusion independently. This is about argument diagramming, showing how

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.7

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Gruff attacks Mira with ad hominem (name calling/labeling) and dismisses argument based on personal attack. Options include "Name calling / labeling" which matches ad hom

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.1

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: preacher repeats claim many times, villagers accept because of repetition. That's the "repetition" fallacy, also known as argumentum ad nauseam. Options include A10.2

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.2

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Forge deflects by bringing up other polluters, claiming the meeting should focus on them. That's classic whataboutism, a red herring. So code A10.3

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.3

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The speech: "Trade with Ashford? Have we forgotten who we are? Ironvale was built by Ironvale hands... Our ancestors did not forge this town so that we could hand our prosperity

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.4

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The professor says: "It is what it is. The Academy has always taught theory first... If it ain't broke, don't fix it. You young scholars always want to reinvent the wheel

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.5

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern among options. The scenario: two parties give wildly different accounts. One minimizes, other exaggerates. The pattern is Exaggeration / minimization. Option A10.6 corresponds to Exaggeration

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.6

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern used by Harl. He casts doubt on evidence: questioning calibration, funding, etc. That's doubt casting. Options: A10.7: Doubt casting. So answer A10.7.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.7

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: evaluating arguments for validity. Tablet A: syllogism with false premise (Barack Obama was born in France) but structure is valid (if premises true, conclusion follows

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.1

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: logician teaching translation between natural language and symbolic notation, focusing on difference between "not both" and "neither". That's about propositional logic basics, understanding logical operators

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.2

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: detective uses argument: "Either S or D. Not S. Therefore D." That's a valid logical form: disjunctive syllogism. The instructor asks

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.3

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario is about identifying inference rules (modus ponens, hypothetical syllogism). Options list: A2.4: Inference rules (modus ponens, modus tollens). That matches

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.4

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A2.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: instructor asks to work forwards and backwards, find rule to produce disjunction in conclusion, combine premises. This is about natural deduction proofs, using logical rules. So the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.5

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Scenario: instructor explains that some arguments have structure not captured by propositional logic, depend on categories, uses categorical syllogism, Venn diagrams, translation to categorical form. So pattern

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.6

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: building truth tables to determine logical equivalence. That's propositional logic basics, specifically logical equivalence. Options: A2.2: Propositional logic basics;

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.7

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: mathematician uses deductive reasoning (all healthy birds can fly, so Tweets can fly). Naturalist uses inductive (most healthy birds can fly, so probably can fly). Then

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.8

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario compares two polls, evaluating sample size, representativeness, statistical generalizations. So pattern is "Statistical generalizations". That's option A3.1. So answer "A3

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.1

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A3.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: three investigators propose explanations, magistrate must evaluate which explanation is best using explanatory virtues. This is about inference to the best explanation (IBE). So code A3.2

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.2

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

**Correct Code:** `A3.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern used in scenario. Vet uses necessary condition test and sufficient condition test to identify cause. That's causal reasoning. So option A3.4: Causal reasoning. Return code.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.4

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: claim that tonic causes higher yields, but objections point out possible confounding variables, correlation vs causation. So primary pattern is "Correlation vs causation". Option A3.5

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.5

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A4.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: dice master asks probability questions, warns about adding probabilities incorrectly. The reasoning pattern is about basic probability laws (complement rule, at least one). So option A4

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A4.1

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A4.2` | **Model Predicted:** `A` | **Result:** ✗

**Model Response:**
> A

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: A, Correct: A4.2

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

**Correct Code:** `A5.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: "If you carry a royal writ, you may pass." That's a conditional: If P then Q. Player does not have a royal writ (not P). Sergeant says: Therefore

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A5.1

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The argument: "If a wolf attacked the sheep, we would find large paw prints near the pen. And look — large paw prints, right here. So it was a wolf." That's affirm

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A5.2

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The argument: "If we allow second bakery, competition will drive down prices, leading to cutting corners, leading to sickness, leading to healers overwhelmed, leading to plague." That's a slippery slope

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A5.3

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The argument: "Every atom in my body is invisible to the naked eye. I am made entirely of atoms. Therefore, I must be invisible to the naked eye." This is a composition fall

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.1

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Dorin says because house worth 900 gold, each component is worth proportionally share of 900. That's the fallacy of division: assuming what's true of whole is true of

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.2

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: "The Codex of Arundel is the ultimate authority on all matters of truth. How do I know? Because chapter one of the Codex states: 'Every word herein

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.3

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The commander presents two options: march north or let them bleed us dry (i.e., do nothing). That's a false dichotomy (black-or-white) because there may be other options (e

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.4

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The argument: "Nobody is perfect. Bert is a nobody. Therefore, Bert is perfect." This is a fallacy of equivocation: the word "nobody" used in two senses:

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.5

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The argument: "There is no sharp line between novice and archmage because skill increments are tiny; therefore ranks are arbitrary nonsense." This is a slippery slope? Actually it's claiming that because there

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.6

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Grus attacks Maren's credibility because she is a newcomer, not a farmer, thus ad hominem. Not straw man. So answer A7.1.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.1

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.10` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: merchant claims invisible amulet works; you challenge: prove it doesn't work; they say you can't prove lack of barrier, so it's working. That's shifting burden of proof, i.e

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.10

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.11` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: senior ranger dismisses scholar's research, saying "I've never seen a fish sprout legs. That's the most ridiculous thing I've ever heard." That's personal incredulence: claiming something

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.11

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.12` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Psychic claims visions are real, says test failed because skeptic's hostile energy blocked sight. That's an ad hoc excuse blaming failure on external condition, a special pleading: "true psychic ability

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.12

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.13` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: "Tell me, Healer Maren — have you stopped using contaminated herbs in your remedies yet? The council deserves a straight answer: yes or no." That's a loaded question (

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.13

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.14` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: alchemist claims tonic cures disease. He surveyed 30 villages, in five the pox rate dropped dramatically. He circles those five on map, implying evidence. That's Texas sharpshooter

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.14

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.15` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: mediator says truth lies in middle, propose compromise between two extremes. That's the "middle ground" fallacy (false compromise). Option A7.15: Middle ground (false compromise

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.15

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.16` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: someone dismisses concern about dust causing lung sickness by saying his granddad worked there for 60 years, breathed dust, lived to 97. That's anecdotal evidence (personal story

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.16

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Sable proposes modest levee on south bank. Grask replies: "So Sable wants us to dam the entire river and cut off water to every farm downstream! Think of

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.2

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Garrett responds to inspector's criticism by accusing inspector of similar wrongdoing. That's classic "tu quoque" (you too) fallacy. Options include A7.3: Tu quo

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.3

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Dorric attacks Vielle's formula based on her origin (learned trade at poorhouse). He says "You cannot get fine glass from gutter origins." That's genetic fallacy: judging claim based

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.4

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Guildmaster Holt argues: "Consider what happens if people believe her. The redthorn harvesters lose livelihoods... families will go hungry... Do we want to accept a finding that would

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.5

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Corvin appeals to authority: "Master Eldric, famous surgeon, says chemicals will kill fish. He is celebrated. If a man of his stature says the dyes are toxic,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.6

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Matron Geld defends herself by listing caring actions, appealing to emotion, and dismissing evidence. She says "Look at their faces—do these children look neglected?

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.7

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.8` | **Model Predicted:** `A` | **Result:** ✗

**Model Response:**
> A

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: A, Correct: A7.8

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.9` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: vendor says many people have it, so you should get one; appeal to popularity. That's bandwagon fallacy. Option A7.9 is Bandwagon (appeal to popularity

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.9

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Deputy says it's more likely that Linda is a bank clerk AND a member of the Fair Trade Alliance than that she is simply a bank clerk. He says activist profile fits too well.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.1

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: test 95% accurate, disease prevalence 0.5%. She says 95% chance patient has disease, ignoring base rate. That's base rate neglect. Option A8.2

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.2

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Minister claims that because small schools have higher scores, small schools are better. This is using small sample size? Actually they studied every school in the realm, so not a small sample

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.3

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: peddler claims 9 out of 10 customers feel better within three days. This is likely base rate neglect? Or regression to the mean? He uses anecdotal evidence and possibly

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.4

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: gambler thinks because low streak, next must be high. That's gambler's fallacy. Option A8.5: Gambler's fallacy. So answer code A8.5

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.5

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to read scenario and identify primary reasoning pattern from options. Breck says: "Do not go to Dunmore. I have been there twice. The first time, the innkeeper overcharged me. The second time, a

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.6

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Brix shows correlation between seagull numbers and fishing fleet decline, claims seagulls are causing fish decline, proposes culling seagulls. This is false cause: correlation

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.7

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A9.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: senior member reviews junior's successful quest. The senior says: "Well, I suppose even Pip managed to clear the Thornwall Caverns. Quite the accomplishment for someone of his... limited

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A9.1

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Correct Code:** `A9.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: advisor urges tax to fund fortress. Argument: Northern threat growing, beyond dispute. Most military scholars agree fortress is only viable defense. Granted tax will be hard, but a little hardship

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A9.2

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A9.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Someone says "Silvervein must be medicinal because her grandmother used it — that's a textbook appeal to tradition! Her argument is fallacious, which means Silvervein obviously has NO healing

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A9.3

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario is about decision matrix, evaluating actions under uncertainty, looking for dominance. That's decision theory, payoff matrix. Option B1.1: Decision matrices. Others are unrelated. So

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.1

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: decision matrix with pay or not pay, outcomes: cart damaged or not. Dominance reasoning says no dominance. But something feels wrong about treating 'Cart Damaged'

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.2

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: choose expedition using maximax criterion (choose the alternative with the maximum possible payoff). So the reasoning pattern is Maximax. Options list includes B1.3: Maxim

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.3

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scholar is using maximin (cautious approach, cannot bear worst outcome). He wants to avoid worst outcome, chooses action that maximizes the minimum payoff. That's maximin. Options list

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.4

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern used. The scenario: traveling merchant, allocate cargo, unknown which settlement will be buying. Use Minimax Regret to decide which cargo to load. So the reasoning pattern is Minimax Regret,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.5

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario is about Spence signaling model, costly signals, separating equilibrium. Options include signaling and costly signals (B10.1), backward induction, subgame perfect equilibrium, ESS, replicator

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.1

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B10.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario is about Ultimatum Game, deviation from standard game theory, need social preferences. That's behavioral game theory. So code B10.2.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.2

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario is about commitment, precommitment, making threats credible, removing options to improve outcome. That's about commitment and precommitment. Option B10.3: Commitment and precommitment

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.3

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario is about repeated interaction, reputation, Folk theorem. That's "Reputation and repeated games". Option B10.4 matches. So answer B10.4.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.4

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B2.1` | **Model Predicted:** `B2` | **Result:** ✗

**Model Response:**
> B2

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: B2, Correct: B2.1

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: bookie's odds sum >1, meaning overround, profit guarantee. Professor asks about constructing a set of bets that guarantees gambler loses money if credences sum >1. That's classic

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.2

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B2.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: bookie's odds implied probabilities sum to >1 (1.05). The gambler says numbers don't add up. This is about probability axioms: probabilities must sum to 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.3

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

**Correct Code:** `B2.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: gambler ignoring known bias, betting as if fair. Manager says not violating logic, credences sum to 1, not Dutch-Bookable, but is he rational? This is about

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.5

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: calculate expected utility (expected cost) using EU formula. That's MEU (Maximum Expected Utility) formula. Option B3.1: MEU formula and calculation. So

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.1

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. Scenario: Scout gives ordinal ranking (Hilltop > Bridge > Ravine) but doesn't quantify differences. Captain wants to apply maximin (choose position with best worst case). But max

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.2

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B3.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Kael uses expected value, rational risk-neutral. Sera prefers certain 400 over gamble with same EV, citing diminishing marginal utility: each additional gold matters less,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.3

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: cyclic preferences violating transitivity, leading to money pump. That's classic "transitivity and money pumps". Option B3.4. So answer code B3.4.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.4

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B3.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: removal of an unchosen option changes preference between remaining options. That's classic violation of Independence of Irrelevant Alternatives (IIA). So answer B3.5.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.5

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

**Correct Code:** `B3.7` | **Model Predicted:** `B3` | **Result:** ✗

**Model Response:**
> B3

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: B3, Correct: B3.7

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Two choices: first pair (G1 vs G2) and second pair (G3 vs G4). People choose G1 (sure 1M) over G

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.1

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B4.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from options. The scenario: Scholar Voss presents Sure Thing Principle and then stress-tests it with Disjunction Effect. The puzzle shows a violation of Sure Thing Principle leading to Disjunction effect. The

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.2

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

**Correct Code:** `B4.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: ambiguous probabilities, known proportion of red (1/3) but unknown mix of black and yellow. People prefer gamble 1 over 2 (risk averse? Actually they know red

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.4

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario describes risk aversion for gains, risk seeking for losses: that's the reflection effect (prospect theory). Options list B4.5: Reflection Effect. So answer code

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.5

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: partial evidence, two-coin bet, unconditional EV positive, but conditional on knowing at least one heads or at least one tails, each leads to rejecting. Yet you

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.6

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B5.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: traders have different reactions to same bonus based on expectations and reference points. The economist says they evaluate departures from expectation, not total wealth. That's about reference dependence, prospect theory, reference

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.1

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

**Correct Code:** `B5.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario describes overweighting small probabilities, underweighting large probabilities, probability weighting function. That's B5.3: Probability weighting. So answer B5.3.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.3

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B5.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario describes Fourfold Pattern of risk attitudes in Prospect Theory. Option B5.4: Fourfold pattern of risk attitudes matches. So answer B5.4.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.4

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario is classic framing effect (Asian disease problem). So answer is B5.5: Framing effects. So code "B5.5".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.5

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: two people have same amount but different source (savings vs windfall). One declines risky bet, other accepts. This is classic mental accounting (treating money differently based on

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.6

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

**Correct Code:** `B5.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Darya is focusing on sunk cost (already paid 300 gold) and refusing to change decision. That's sunk cost fallacy. Options include B5.8: Sunk cost fallacy (

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.8

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B6.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. Scenario: two rival potion brewers share a resource. Each season they decide to cooperate (harvest conservatively) or defect (strip). Payoffs: If both cooperate, each gets 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B6.1

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B6.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: payoff matrix is Prisoner's Dilemma, find Nash equilibrium. So the pattern is Nash equilibrium. Option B6.2: Nash equilibrium. So answer "B6

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B6.2

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B6.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario is about iterated Prisoner's Dilemma, cooperation, strategies like Tit-for-Tat, and question about what happens when TFT plays against a strategy that defects on round 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B6.3

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

**Correct Code:** `B7.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: two players prefer different events but prefer coordinating together over going alone. That's classic "Battle of the Sexes" game. So answer B7.2.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B7.2

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

**Correct Code:** `B7.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The philosopher explains conventions, coordination problem, Lewis's conditions. That's about conventions, coordination games, Stag Hunt? The options: B7.4: Convention (Lewis). That matches directly.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B7.4

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B8.1` | **Model Predicted:** `B8` | **Result:** ✗

**Model Response:**
> B8

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: B8, Correct: B8.1

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B8.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario describes backward induction solution, entry game, credible threat. The options include B8.2: Backward induction. So answer is B8.2.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B8.2

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B8.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario discusses Nash equilibria, subgame perfect equilibrium, need for optimal at every decision node, backward induction. The primary pattern is Subgame perfect equilibrium (B8.3). Could also

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B8.3

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B8.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to read scenario and identify primary reasoning pattern from options. The scenario is about Centipede Game, backward induction, paradox. Options include:

B10.3 Commitment and precommitment
B10.4 Reputation and repeated

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B8.4

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario is about ESS, checking pure strategies, mixed ESS. So primary reasoning pattern is Evolutionarily Stable Strategy (ESS). Option code B9.1. So answer "B9

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B9.1

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario describes replicator dynamics, ESS, Hawk-Dove. The correct option is B9.2: Replicator dynamics. So answer "B9.2".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B9.2

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: evolutionary Stag Hunt, replicator dynamics, path dependence, social contract equilibrium. Options: B10.1 signaling, B10.3 commitment, B6.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B9.3

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Torva has limited time (one day) and must choose between two jobs with different pay. She is focusing on profit of 80 vs 50, but must consider opportunity cost of

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C1.1

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `C1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario about comparative advantage: Hilde outproduces Oskar in both crops, but still trade beneficial due to opportunity cost differences. That's classic comparative advantage. So code C1.2.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C1.2

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: fixed budget, need to meet constraints, minimize cost while meeting requirements. That's a constrained optimization problem (linear programming). Options: C2.1 Constrained optimization fits. So answer

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C2.1

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: deciding how many potions to brew given cost per unit and constant price. That's marginal analysis (compare marginal cost to price). Could also be constrained optimization? No constraints given besides profit maxim

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C2.2

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

**Correct Code:** `C3.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: multiple families overfishing a common resource, leading to tragedy of the commons. That's "Commons problems". Option C3.2. So answer "C3.2".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C3.2

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `C4.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: bargaining over surplus, with outside options (reservation values). They need to split surplus fairly given constraints. This is a bargaining problem, perhaps Nash bargaining solution. So pattern is "Barg

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C4.1

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C4.2` | **Model Predicted:** `C4` | **Result:** ✗

**Model Response:**
> C4.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: C4, Correct: C4.2

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C5.1` | **Model Predicted:** `C5` | **Result:** ✗

**Model Response:**
> C5

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: C5, Correct: C5.1

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Correct Code:** `C5.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario about price ceiling causing shortage, deadweight loss, black market. That's price controls and deadweight loss. Option C5.2. So answer "C5.2".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C5.2

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Correct Code:** `C6.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: tannery pollutes downstream, causing water contamination, costs borne by downstream village. That's classic externality (negative externality). Could also be public goods and free riding, or commons problems

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C6.1

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C6.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: sellers know horse condition, buyers can't; leads to adverse selection, market collapse. That's classic information asymmetry leading to market failure. Option C6.2: Information asymmetry (markets

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C6.2

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C6.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario about presentation of choices, decoy effect, anchoring, behavioral economics. Options: C6.3: Behavioral economics in markets. That matches. So answer C6.3.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C6.3

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `C7.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The argument: destruction creates demand, jobs, prosperity. That's the broken window fallacy (the idea that destruction is good for economy). So code is C7.1.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C7.1

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `C7.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Dagan says any gain for Brassholm must be at Ardenvale's expense, zero-sum thinking. Petra points out trade benefits both sides. Dagan insists it's zero-sum. So pattern

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C7.2

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Let's parse scenario: Alderman Corwin restates opponent's position accurately, acknowledges facts, admits his own error, then proposes compromise. This resembles Rapoport's Rules: summarizing

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.1

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Correct Code:** `D1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Varek claims all beliefs equally valid. Tessa responds by giving absurd examples (earth flat, poison nutritious) to show absurdity. That's a reductio ad absurdum

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.2

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Correct Code:** `D1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: two explanations: ghost vs squirrels. The rational explanation is squirrels, simpler. That's Occam's Razor (prefer simpler explanation). Option D1.3 is Occam's

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.3

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Let's analyze scenario.

Cask: He points to his own company's report saying water safe, points to miners being healthy, says if water poisoned they'd be first ill. He also says Dr

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.4

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from options. Need to understand what each code corresponds to. This seems like a classification of argumentation fallacies or reasoning patterns from some taxonomy. We have options:

D1.5: J

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.5

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Brother Aelm says "Love is just a word... everything we build on it is built on nothing more than a sound." That's a deep-sounding statement that is vague

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.6

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Professor Venn argues that animals cannot suffer because they lack self-awareness, self-reflection, language. He uses "surely" statements. The options include "The

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.7

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: advisors give hedged, indecisive statements, then Pella gives a decisive, concrete claim, cutting off further discussion. This is a "conversation-stopper"

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.8

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Maren chooses a heuristic (triage protocol) rather than optimal allocation due to time constraints. That's satisficing: choosing a good enough solution quickly. So code D2.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.1

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `D2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Let's analyze the scenario.

Elder Maren says: "Our river diversion was not merely adequate — it was the optimal solution. We lost nothing of real importance. The granary can

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.2

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Correct Code:** `D2.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Elder Sanna says "Some things are not for calculation. That is what sacred means." This is a conversation stopper: she ends discussion by invoking sanctity, refusing further

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.3

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Correct Code:** `D2.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: a retired general aware his heuristics are imperfect, dilemma about whether to abandon them or keep using flawed shortcuts. This seems like "The Panglossian Slide"? Let's

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.4

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Correct Code:** `D2.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario describes an AI (automaton) that has many rules and checks everything before acting, leading to paralysis (frame problem). Then a simplified version only checks relevant things, but

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.5

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D2.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Abbess says "You are asking the wrong question... there is no one true theory. Let me show you something more useful." This seems like "The Moral First

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.6

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Nessa attributes Gareth's poor harvest to his laziness (personal disposition) despite possible external factors (blight, flood). That's classic fundamental attribution error: overemphasizing internal traits

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.1

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.10` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern exhibited by Elder Sorn. He is focusing on worst-case scenario, ignoring statistical evidence, expecting catastrophe. That's pessimism bias (overly negative expectations). Could also be "negativity bias". Among

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.10

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.11` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Venn focuses on three failures despite many successes. That's availability heuristic (recalling vivid negative events) or negativity bias (tendency to focus on negative). Both similar. Availability heuristic: events that

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.11

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.12` | **Model Predicted:** `E` | **Result:** ✗

**Model Response:**
> E

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: E, Correct: E1.12

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

**Correct Code:** `E1.14` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: soldiers refusing because mandatory; they experience reactance (psychological reactance: desire to regain freedom when freedom threatened). So code is E1.14.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.14

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.15` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Finch thinks everyone noticed his mistake, but actually they didn't. That's the spotlight effect: overestimating how much others notice one's actions. So code E1.15.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.15

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.16` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Aldric blames victims for misfortune, saying they deserved it because they didn't plan ahead. That's just-world hypothesis (belief that people get what they deserve). Also could be self-serving

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.16

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.17` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Hask says things were better in past, despite data showing improvements. This is a bias toward believing past was better, a tendency to view the past as better than present: that's "declin

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.17

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.18` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: evidence presented, but people become more convinced opposite. That's backfire effect: presenting evidence contrary to belief strengthens original belief. So code E1.18.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.18

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.19` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: fortune teller gives generic statements that seem accurate; same reading given to multiple people. That's Barnum/Forer effect. So code is E1.19.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.19

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Maren uses selective evidence, focusing on confirming her belief that tonic works, ignoring contrary evidence, discounting negative cases, emphasizing positive outcomes, using anecdotal evidence. That's

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.2

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.20` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Brynn has invested time, money, reputation, and continues to justify continuing despite better alternative. That's classic sunk cost fallacy. So answer code: E1.20.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.20

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

**Correct Code:** `E1.22` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Scenario: Dunn favors his own guild (Ironworkers) and disparages Woodworkers despite identical proposals. That's in-group bias (favoring own group). So code E1.22.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.22

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.23` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Scenario: judge treats same evidence differently based on personal feelings: likes Ella (positive view) and distrusts Rusk (negative view). That's halo effect: positive impression of Ella leads to

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.23

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.24` | **Model Predicted:** `E1` | **Result:** ✗

**Model Response:**
> E1

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: E1, Correct: E1.24

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. Scenario: Brecca says original price 900, offers 600. Merchant says sold one for 400. The reasoning pattern likely anchoring: initial price (900) sets anchor, then

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.3

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Dax overconfident, assuming technique works, ignoring complexity. Lirel notes that Dax is cocksure while intelligent are doubtful. That's Dunning-Kruger effect (over

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.4

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. The scenario: Captain Voss emphasizes recent vivid wolf attacks, despite data showing pickpocketing is larger problem. He is influenced by vivid, emotionally salient events. That's availability heuristic (people judge

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.5

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. Scenario: Student judges validity based on truth of premises/conclusion rather than logical form. That's belief bias: evaluating argument validity based on believability of conclusion. So answer: E1

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.6

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern from options. The scenario: Renna attributes success to her own skill/experience (instinct, reading terrain) and attributes failure to external factors (client gave wrong map, damp torches). That's

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.7

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Master Fen can't explain his skill because he has knowledge that he takes for granted; can't articulate because he assumes it's obvious. That's classic "curse of knowledge": difficulty in imagining not knowing something

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.8

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.9` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify primary reasoning pattern. Scenario: Hesta notes that every previous expedition took longer than expected; leaders claim they'll be exception due to special factors. This is optimism bias: overestimating positive outcomes, underestimating risks

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.9

---

## Appendix C: Full Results — Explain Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The bartender wants to know: which of these speakers is actually giving an argument? How can you tell?

**Expected Answer:** **Identifying arguments via indicator words** — An argument is a set of premises that attempt to provide a reason that a conclusion is true. The sailor's statement is a chronological narrative with no premises or conclusion — it describes a sequence of events. The dockworker's statement is an argument: 'since' is a premise indicator linking two p *Recognizing arguments requires checking for premise and conclusion indicators and verifying that statements are being offered as reasons for another statement. The dockworker uses 'since' to connect e*

**Model Response:**
> **1. What is being demonstrated?**  
The exchange contains a classic **irrelevant‑premise / non‑sequitur** (the formal fallacy *ignoratio elenchi*).  
The sailor’s chronological story supplies no premise that bears on the bartender’s real question – “Is anyone giving me a reason to *believe* something?” – while the dockworker’s claim about seaworthiness, although it *does* try to give reasons, is presented without linking those reasons to the specific proposition the bartender is asking about (the ship’s fitness to sail *right now*).

**2. Name of the pattern**  
*Ignoratio elenchi* – “missing the point” – also described in everyday language as an **irrelevant‑premise fallacy** or **non‑sequitur**.

**3. Why it is (un)good reasoning**  

| Element | What the speaker does | Why it fails (or

**Score:** 1/4 █░░░
**Judge Reasoning:** The student fails to identify the correct pattern (Identifying arguments) and instead incorrectly diagnoses the scenario as a logical fallacy (ignoratio elenchi/non-sequitur). While the student senses a difference between the speakers—noting the sailor lists actions and the dockworker offers reasons

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Theodora just gave testimony with several claims. Which is her main conclusion? Which statements are premises? Is there a statement that serves as both a conclusion and a premise?

**Expected Answer:** **Identifying premises, conclusions, and intermediate conclusions** — Theodora's argument has a layered structure. 'The fact that... is shown by the fact that...' reverses the usual order — the conclusion comes first, then the premise. The intermediate conclusion is that the royal household is contributing to the obesity problem (supported by premises about larger por *Identifying premises and conclusions requires attending to indicator phrases. 'The fact that X is shown by the fact that Y' means Y is the premise and X is the conclusion — the reverse of reading orde*

**Model Response:**
> **1. The reasoning pattern being demonstrated**  
Theodora is moving from (a) an observed statistical trend, to (b) a *single* alleged cause for that trend, and then to (c) a normative prescription (“the king should reform the kitchen”). The chain contains two classic logical‑decision‑theoretic errors:

| Step | Formal pattern | Why it is a fallacy / bias |
|------|----------------|----------------------------|
| **a → b** | *Cum‑hoc / post‑hoc causal inference* ( “larger portions → overeating → obesity” ) | The argument treats a correlation (larger portions are observed together with higher eating) as proof of a causal link without experimental or longitudinal control. |
| **b → c** | *Fallacy of the single cause* (or *causal oversimplification*) | It assumes the royal kitchen is the deci

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the specific task. The prompt required analyzing the argument's structure (identifying premises, intermediate conclusions, and main conclusions) and noting the specific indicator phrase order. Instead, the student critiqued the argument's validity by listing 

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe hands you Captain Voss's statement. Rewrite it in standard form: numbered premises with the conclusion last. Does the argument have any sub-arguments?

**Expected Answer:** **Standard form reconstruction** — Standard form lists premises as numbered statements with the conclusion last, marked with 'Therefore.' Voss's argument has two sub-arguments: one eliminating the sewer escape (premises about the locked grate and no scent trail), and one concluding the cart escape (premises about it being the only al *Standard form makes the logical structure visible. It separates premises from conclusions, reveals sub-arguments, and shows which premises support which conclusions. Voss's conversational version buri*

**Model Response:**
> **1‑2.  The pattern being displayed**

| What the captain does | Formal name(s) |
|-----------------------|----------------|
| Rules out the sewage‑pipe escape because the grate is locked **and** because the dogs found no scent, then declares the only remaining option (the delivery cart) must be true. | **False dilemma / false‑either‑or** (treating the two routes as the only mutually exclusive possibilities) **plus an appeal to ignorance (argument ad ignoran­tiam)** – “no evidence of a scent = no possibility”. |
| He also cherry‑picks the facts that support his preferred story while ignoring any contrary information. | **Confirmation bias** (selective weighting of evidence). |

**3.  Why the reasoning is faulty (or, when it can be sound)**  

| Element | Why it is bad (or good) |
|--------

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to follow the prompt's instructions. The task required reconstructing the argument into 'Standard form' (numbered premises leading to a conclusion). Instead, the student provided a critique of the argument's logical fallacies (False Dilemma, Appeal to Ignorance) and sug

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Aldric has asked you to reconstruct Rosmund's argument in its strongest form. What is she really trying to argue, underneath the hyperbole? And why is the heckler's response unfair?

**Expected Answer:** **Principle of charity in argument reconstruction** — The principle of charity states that when reconstructing an argument, you should try to make it as strong as possible. Rosmund's literal words contain overstatements ('cheap garbage,' 'every tanner will go broke'), but her core argument has a defensible structure: if cheaper foreign imports undercut *The heckler attacked Rosmund's weakest phrasing ('cheap garbage') rather than her strongest argument. Charitable reconstruction reveals that her core concern — price competition threatening local live*

**Model Response:**
> **1. The reasoning pattern that is showing up**

Rosmund’s outburst mixes three classic argumentative shortcuts:

| What she says | Underlying shortcut |
|---------------|--------------------|
| “Foreign leather is *cheap garbage* and will *destroy our livelihoods*.” | **Appeal to fear / appeal to consequences** – the claim is justified only by the frightening outcome it supposedly produces. |
| “If we let that stuff in, *every* tanner will go broke.” | **Slippery‑slope / hasty‑generalisation** – she assumes a chain of catastrophic events without supplying any causal evidence. |
| “The council *has to* ban imports or the guild is finished.” | **False‑dilemma (either‑or)** – she presents only two mutually exclusive options, ignoring any middle ground (e.g., regulation, branding, mixed sourc

**Score:** 1/4 █░░░
**Judge Reasoning:** The student failed to identify the correct reasoning pattern (Principle of Charity). Instead, the response focuses entirely on cataloging logical fallacies (Appeal to Fear, Slippery Slope, False Dilemma) present in Rosmund's speech. While the student correctly notes that the heckler uses a straw-man

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Councillor Drava's conclusion says the state 'should' do something. Her premise says something 'is' the case. What is missing? What assumption would you need to add to make this argument valid? And once you add it, does the argument actually work?

**Expected Answer:** **Missing premises and the is-ought gap** — Drava's argument has a descriptive premise (children of unmarried couples often have emotional difficulties) and a normative conclusion (the state should discourage this). Any argument with a normative conclusion requires at least one normative premise — this is the is-ought gap. The missing premise *Identifying missing premises — especially normative ones — reveals the hidden assumptions on which an argument depends. By making Drava's argument valid through supplying premises, we can see more cle*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The argument moves from a **descriptive claim** (“children raised by unmarried couples often have emotional difficulties”) straight to a **prescriptive claim** (“the state should discourage unmarried couples from raising children”) without supplying any normative bridge. This is the classic **“is‑ought” (or naturalistic) fallacy** – the mistake of treating a fact about the world as if it automatically justifies a moral or policy prescription.

**2. Name of the fallacy / bias**  
- **Is‑ought fallacy** (also called *Hume’s Guillotine* or the *naturalistic fallacy* in moral philosophy).  
- In a more informal policy‑analysis setting it can be labeled an **appeal to consequences** (the “bad‑consequence → wrong” move) when the missing premise is “

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'is-ought' gap and the missing normative premise (Level 2/3 criteria). Crucially, they also explicitly address the missing causal assumption by noting 'Correlation ≠ Causation' and listing confounding factors like socio-economic status. Furthermore, they mention 

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The chronicler has two statements about the bridge collapse. Which one is an argument and which is an explanation? How can you tell the difference?

**Expected Answer:** **Distinguishing arguments from explanations** — Arguments try to convince you that a conclusion is true — the conclusion is in dispute. Explanations show why something already accepted as true occurred — the conclusion is taken for granted. The engineer's statement is an explanation: no one disputes that the bridge collapsed; the engineer explain *The key test is whether the 'conclusion' is already taken for granted or is in dispute. 'Because' can introduce either an explanation or a premise — context determines which. The engineer uses 'becaus*

**Model Response:**
> **1. What reasoning pattern is on display?**  
Both statements are trying to *explain* why the bridge fell, but the inspector’s remark goes a step further and *uses* that explanation as proof that the town was negligent. In doing so the inspector commits a classic **causal‑inference fallacy** – specifically the **post‑hoc‑ergo‑propter‑hoc** ( “after this, therefore because of this”) error – and, at the same time, a **hasty‑generalisation** about the length of time the bridge was unsafe. In decision‑theoretic language it is an **over‑confident diagnostic inference** that treats a single piece of forensic evidence as sufficient to decide liability.

---

**2. Name of the fallacy / bias**

- **Post‑hoc ergo propter hoc (false cause)** – inferring that because termites and flood damage are *pr

**Score:** 1/4 █░░░
**Judge Reasoning:** The student fails to identify the core pattern of 'Arguments vs. Explanations' and incorrectly asserts that both statements are trying to explain. Instead of distinguishing based on whether the conclusion is disputed or taken for granted, the student pivots to analyzing logical fallacies (post-hoc, 

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The guild master wants you to diagram this argument. Which premises must work together (linked) and which support the conclusion independently (convergent)?

**Expected Answer:** **Linked vs convergent premises and sub-arguments** — In argument diagramming, linked premises are premises that must work together to support a conclusion — neither is sufficient alone. Convergent premises independently support the same conclusion. In this argument, premises 1 and 2 are linked: 'Wanda had her pant leg rolled up' only supports 'she bik *Diagramming reveals that this argument has two independent lines of evidence converging on the same conclusion. If premise 3 turned out to be false (Bob was mistaken), the argument from premises 1 and*

**Model Response:**
> **1.  What is being demonstrated?**  
The passage shows two things at once:

* **A logical error in the (1 + 2) chain** – treating a *correlation* (“cyclists often roll up their right pant leg”) as a *definite rule* and then moving from “Wanda’s leg is rolled up” to “Wanda is a cyclist”. This is the classic **affirming‑the‑consequent** (or *converse error*) fallacy.  

* **A bias in the overall argument** – the detective (and the guild master) present the (1 + 2) inference **as if it were an independent line of support**

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that premises 1 and 2 form a connected chain ('logical error in the (1 + 2) chain') and distinguishes them from the rest of the argument, satisfying Level 2. However, the response fails to reach Level 3 because it does not explicitly identify Premise 3 as an independ

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Gruff seems very confident in dismissing Mira's proposal. But look at what he actually says — does he address any of the specifics of her plan?

**Expected Answer:** **Name calling / labeling** — Gruff substitutes negative labels for substantive engagement. Rather than challenging the aqueduct's costs, feasibility, or projected benefits, he attaches dismissive terms to Mira and her proposal. The labels carry negative connotations that encourage the audience to reject the proposal based on em *Labels are not arguments. Calling someone a 'dreamer' does not address whether their cost estimates are accurate, their engineering is sound, or the water supply is needed. The labels function as a su*

**Model Response:**
> **1. What is being demonstrated?**  
Trader Gruff is dismissing Mira’s proposal not on the basis of its *content* (costs, flow rates, timeline) but on the basis of who she is – an “out‑of‑touch academic” and a “dreamer.” He is using a **personal attack** to reject the argument.

**2. Name of the pattern**  
*Ad hominem* (abusive) – more precisely an **ad hominem circumstantial / “poison‑the‑well”** variant. It is also sometimes labeled a **genetic fallacy** because the argument is rejected solely on the origin of the idea.

**3. Why the reasoning is (un)reliable**  

| Aspect | Good? | Why it fails (or succeeds) |
|--------|-------|----------------------------|
| **Relevance** | ❌ | The truth of Mira’s engineering calculations does not depend on her occupation or personality. Attacking her

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism: Gruff dismisses the proposal based on personal labels ('out-of-touch academic', 'dreamer') rather than engaging with the substantive evidence (costs, flow rates). They explicitly explain how these labels substitute for argument ('Attacking her bac

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The villager says Brother Constant must be right because he has been saying it all week. Is that good reasoning?

**Expected Answer:** **Repetition / illusory truth effect** — Brother Constant repeats the claim 'The Old Bridge is cursed' with rhythmic insistence, without providing evidence. The illusory truth effect is a well-documented cognitive phenomenon: repeated exposure to a statement increases the feeling of familiarity, which people mistake for truth. The villager *Repetition is not evidence. A claim does not become more true by being stated more often. The feeling of familiarity that repetition produces is a cognitive artifact, not a rational basis for belief. *

**Model Response:**
> **1. The reasoning pattern at work**  
The villager is treating the *frequency* with which Brother Constant repeats the claim as evidence that the claim is true.  This is a classic **appeal to repetition** (also called *argumentum ad nauseam* or the *illusory‑truth effect*).  It is a cognitive bias that conflates *familiarity* with *truth*.

---

**2. Precise name(s)**  

| Formal name | Common name | Related concepts |
|-------------|-------------|------------------|
| **Argument from repetition** | **Ad nauseam** | *Illusory truth effect*, *availability heuristic*, *bandwagon bias* |

All of these refer to the same underlying phenomenon: the more often a proposition is heard, the more likely people are to judge it true, even in the absence of supporting evidence.

---

**3. Why the reaso

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'illusory truth effect' and the conflation of familiarity with truth, meeting the core Level 4 requirement. Furthermore, the response exceeds the rubric by detailing the cognitive mechanism (processing fluency), outlining a rigorous correct approach (Bayesian up

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge has been presented with clear evidence of slag dumping. Does his response address that evidence?

**Expected Answer:** **Whataboutism / red herring** — Forge responds to a specific accusation (slag dumping) by redirecting attention to unrelated issues (tannery hides, farm pesticides). The other problems may be real, but they do not address the evidence against Forge. This is a red herring: introducing an irrelevant topic to divert attention from th *The existence of other polluters does not change whether Forge dumped slag in the river. Each accusation should be evaluated on its own evidence. Forge's response addresses neither the witnesses, the *

**Model Response:**
> **1‑2.  The pattern** – Forge is committing an **appeal to hypocrisy / “tu‑quoque”** (a subtype of the **red‑herring** fallacy).  It is sometimes labeled **“what‑about‑me”** or **“two‑wrongs‑make‑a‑right”** reasoning.

---

### 3.  Why it is a fallacy (the mechanism)

| Step | What Forge does | Why it fails as reasoning |
|------|----------------|--------------------------|
| **Premise** | “You accuse me of polluting.” | The accusation is a factual claim supported by witnesses, water‑sample analysis and dead fish. |
| **Deflection** | “But the tannery and the farmers also pollute, and no one talks about them.” | The truth of those other pollutions is **irrelevant** to the truth of the original claim. The argument does not address whether Forge’s slag actually entered the river; it merely t

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as tu-quoque/whataboutism (a red herring subtype). They clearly explain the mechanism: that the existence of other polluters is logically irrelevant to the truth of the specific accusation against Forge. Furthermore, the response excels by explicitly deta

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Steele gave a passionate speech. But did he actually address Councillor Maren's economic analysis?

**Expected Answer:** **Flag-waving / appeal to patriotism** — Steele substitutes an appeal to group identity and patriotic emotion for engagement with the economic argument. He reframes a policy question (will trade lower prices?) as an identity question (are you loyal to Ironvale?). This shuts down cost-benefit analysis by making disagreement feel like betray *Whether trade with Ashford is economically beneficial is a factual question about prices, supply, and demand. It has nothing to do with patriotism or loyalty. Steele's appeal makes evaluating the prop*

**Model Response:**
> **1. The reasoning pattern being displayed**  
The commander’s speech is a classic mixture of **appeal‑to‑tradition / appeal‑to‑patriotism** (sometimes called an *appeal to nationalism* or *in‑group loyalty*) and the **genetic fallacy**.  
He rejects the proposal not on the basis of its actual merits but because the idea comes from “outside” and because it threatens a cherished self‑image of the town.

**2. Precise name(s)**  

| Formal label | Common description |
|--------------|--------------------|
| **Argumentum ad antiquitatem** (appeal to tradition) | “We should do it because we have always done it that way.” |
| **Appeal to patriotism / national‑/regional‑bias** (sometimes catalogued as *argumentum ad populum* or *ad nationem*) | “If you love our town you must oppose this.” |
| **G

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: substituting identity/patriotism for economic analysis and noting how this shuts down evidence-based discussion. They accurately describe the 'us vs. them' dynamic and the irrelevance of tradition/source to the factual claim. However, they do not 

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Krul certainly sounds confident. But did he actually respond to any of Wynn's specific points about enrollment data or graduate outcomes?

**Expected Answer:** **Thought-terminating cliche** — Krul deploys a barrage of stock phrases that sound like wisdom but carry no argumentative content. Each cliche is designed to end inquiry rather than advance it: 'It is what it is' implies nothing can or should change; 'if it ain't broke don't fix it' assumes without argument that nothing is broken; *Thought-terminating cliches are compressed assertions that masquerade as wisdom. They shut down inquiry without providing reasons. 'It is what it is' is not an argument — it is a refusal to engage. 'I*

**Model Response:**
> **1. Reasoning pattern displayed**  
Professor Krul is relying on **appeal‑to‑tradition** (argumentum ad antiquitatem) together with the **status‑quo bias** (a decision‑theoretic/psychological bias that favours keeping things as they are).  

**2. Name**  
- **Fallacy:** *Appeal to Tradition* (also called *Argument from Antiquity*).  
- **Bias:** *Status‑Quo Bias* (loss‑aversion‑driven preference for the current state).  

**3. Why it is (generally) a bad line of reasoning**  

| Element | Mechanism | Why it fails |
|---------|-----------|--------------|
| **Appeal to Tradition** | The claim “we have always done it this way, therefore it is right” treats historical precedent as proof of correctness. | It ignores the actual *evidence* about outcomes (e.g., Wynn’s enrollment data, graduate s

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Krul uses stock phrases to dismiss evidence and explains the mechanism of how these phrases shut down inquiry by substituting tradition for data. However, the response misidentifies the specific reasoning pattern as 'Appeal to Tradition' and 'Status-Quo Bias' ra

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** You have the damage report and you have heard both accounts. What is each speaker doing with the facts, and what would an accurate description look like?

**Expected Answer:** **Exaggeration / minimization** — Both speakers distort the significance of the same event in opposite directions. Holt minimizes: 'a few minutes,' 'a couple of lettuce leaves,' 'barely a scratch.' Tess exaggerates: 'destroyed my entire garden,' 'nothing to eat this winter,' 'I will starve.' The actual damage — roughly a third of th *Distorting the magnitude of an event — in either direction — undermines rational assessment. Holt's minimization would lead to inadequate compensation; Tess's exaggeration would lead to disproportiona*

**Model Response:**
> **1. What is being demonstrated?**  
Both villagers are interpreting the same facts in opposite directions so that the conclusion serves their personal interest (avoiding blame or obtaining compensation).  This is the classic case of **motivated reasoning** – a family of biases that include the **self‑serving bias**, **optimism/pessimism bias**, and the related **exaggeration‑minimisation** tendency.

**2. Name it precisely**  
*Motivated reasoning* (specifically, a self‑serving bias that leads one party to **minimise** the damage and the other to **maximise** it).

**3. Why the reasoning is (un)reliable**  

| Feature | How it works | Why it is problematic |
|---------|--------------|-----------------------|
| **Goal‑oriented processing** | Each speaker starts with a desired outcome (farm

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both distortions (minimization by Holt, exaggeration by Tess) and explicitly names the pattern. They accurately cite the objective middle ground from the damage report (~33% lettuce, two rows of beans). Furthermore, the response exceeds the basic requirements by expl

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Harl says he is just asking questions and that we need more study. Is he raising legitimate scientific concerns, or is something else going on?

**Expected Answer:** **Doubt casting / manufacturing uncertainty** — Harl's strategy is not to present counter-evidence but to generate a fog of doubt around existing evidence. He questions calibration without alleging specific errors, raises the specter of conflicts of interest without identifying any, invokes 'some scientists' without naming them or citing studies, *Legitimate scientific skepticism identifies specific methodological flaws and proposes concrete alternatives. Harl does neither. His doubts are generic enough to apply to any study on any topic. If no*

**Model Response:**
> **1. The reasoning pattern**  
Harl is employing a classic *manufacturing‑of‑doubt* strategy that rests on the **appeal to uncertainty (argument from ignorance)** and a **burden‑of‑proof shift**.  He also mixes in a *status‑quo/ambiguity‑aversion* bias by insisting that “more study” is required before any action, even though the existing evidence already meets the standard for reasonable policy.

**2. Name of the fallacy / bias**  

| Common label | More precise logical name |
|--------------|---------------------------|
| “Manufacturing doubt” (as used by industry) | **Appeal to Uncertainty / Argument from Ignorance** |
| “We need more study before we act” | **Burden‑of‑Proof Shift** (demanding proof of harm rather than proof of safety) |
| “Don’t shut the mine until we are 100 % sure” | 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'manufacturing of doubt' pattern and explains the mechanism by distinguishing between legitimate skepticism (specific errors) and manufactured uncertainty (vague possibilities). They explicitly analyze Harl's tactics (questioning calibration without evidence, vag

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor presents two arguments on stone tablets. Which is valid? Which is sound? Explain your reasoning. If an argument is invalid, provide a counterexample.

**Expected Answer:** **Validity and soundness** — A valid argument is one where the conclusion cannot possibly be false if the premises are true. Soundness = validity + true premises. Tablet A is valid: IF everyone born in France speaks French AND Obama was born in France, THEN he speaks French — the conclusion follows necessarily. But it is unsoun *Understanding validity requires separating the logical structure from the truth of the claims. Many students reject Tablet A because its premises are obviously false — but that is a soundness judgment*

**Model Response:**
> **Short answer**

| Tablet | Formal status | Why it is (in)valid | What the problem really is |
|--------|---------------|--------------------|----------------------------|
| **A**  | **Valid** (modus‑ponens / categorical syllogism) | The logical form “All F are G; x is F; therefore x is G” is truth‑preserving. The conclusion follows from the premises. | One premise is false (Barack Obama was **not** born in France). A valid argument with a false premise is **unsound**. |
| **B**  | **Invalid** (converse error / affirming the consequent) | The move “P → Q; P; therefore Q” is *not* a correct inference; the premise “If someone is elected President then he is President” does not allow us to infer the converse “If someone is President then he was elected.” | The argument commits the fallacy of

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly classifies Tablet A as valid but unsound and Tablet B as invalid. They accurately explain the mechanism for both (truth-preserving form vs. converse error/affirming the consequent) and identify the specific problem with the premises. The response meets all Level 3 criteria: cor

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Translate both sentences into symbolic logic. Then explain: do they mean the same thing? If not, what is the difference?

**Expected Answer:** **Propositional logic connectives and translation** — 'Not both' is the negation of a conjunction: ~(C * I). It is true whenever at least one of the conjuncts is false — Carla could have cake alone, ice cream alone, or neither. 'Neither-nor' is a conjunction of two negations: ~C * ~I. It is true only when both are false — Carla has no cake and no ice c *Correct translation from natural language to symbolic logic requires careful attention to the scope of negation. 'Not both' negates the conjunction as a whole. 'Neither-nor' negates each component sep*

**Model Response:**
> **1. What is being demonstrated?**  
A *scope‑negation error*: the speaker (or a listener) treats the negation of a conjunction as if it were a conjunction of negations. In everyday language this shows up as the confusion between  

* “not both C and I”  →  ¬(C ∧ I)  
* “neither C nor I”   →  ¬C ∧ ¬I  

The two formulas are **not** equivalent; the first is weaker (it only says that at least one of the two items is missing), the second is stronger (it says that both are missing).  

In the taxonomy of informal reasoning this is a **formal fallacy** – sometimes called a *Negation‑Scope Fallacy* or *De Morgan’s‑Law Misapplication*.

---

**2. Name of the pattern**  

*Negation‑Scope Error (mis‑application of De Morgan’s law)* – i.e. treating ¬(A ∧ B) as if it were ¬A ∧ ¬B.

---

**3. Why the 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly translates both propositions, clearly explains the semantic difference (one allows a single item, the other forbids both), explicitly constructs a comparison table that functions as a truth condition analysis, and directly cites De Morgan's Law to explain the mechanism. This ex

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build the truth table for this argument. Is the argument valid? How does the truth table show you?

**Expected Answer:** **Truth table test of validity** — The truth table test works by checking every possible assignment of truth values. An argument is valid if and only if there is no row where all premises are true and the conclusion is false. For this disjunctive syllogism (S v D, ~S, therefore D): with four rows of truth values, the only row where b *The truth table test is a formal method: we can assess validity even without knowing what the argument is about. It is mechanical and objective, unlike the informal test which depends on our ability t*

**Model Response:**
> **1. What is being demonstrated?**  
The detective is using the **disjunctive syllogism** (sometimes called *proof by elimination*). In everyday language it sounds like “either A or B; not A; therefore B.”  

**2. Name of the pattern**  
- **Formal name:** *Disjunctive Syllogism* (rule of inference).  
- **Common phrasing:** “Either‑or elimination,” “modus tollendo ponens.”  

**3. Why it works (or why it can fail)**  

| Premise 1 | Premise 2 | Conclusion | Truth‑table outcome |
|-----------|-----------|------------|---------------------|
| S ∨ D     | ¬S        | D          | **Valid** – there is **no** row where both premises are true and the conclusion false. |

*Mechanism*  

1. **Premise 1** asserts that **at least one** of the two alternatives is true.  
2. **Premise 2** eliminates 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Disjunctive Syllogism) and accurately explains the truth table validity test, noting that no row exists where premises are true and the conclusion is false. They also provide excellent context regarding soundness and natural language ambiguity. However, 

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks: what rule of inference justifies each derived step? Name the rule and explain how it applies.

**Expected Answer:** **Modus ponens and hypothetical syllogism** — Step 4 uses modus ponens (MP): from 'if P then Q' and 'P', derive 'Q'. Step 5 also uses MP: from 'if Q then R' and 'Q', derive 'R'. Step 6 uses hypothetical syllogism (HS): from 'if P then Q' and 'if Q then R', derive 'if P then R'. These are three of the eight basic valid forms of inference. Each p *Inference rules are the building blocks of proofs. MP and HS are two of the most fundamental. MP lets you detach a consequent when you have the antecedent. HS lets you chain conditionals into longer c*

**Model Response:**
> **1.  What reasoning pattern is being shown?**  
The instructor is demonstrating *purely deductive* reasoning – the use of **formal rules of inference** that guarantee the truth of the conclusion whenever the premises are true.  
No fallacy, bias, or decision‑theoretic shortcut is at work; the steps are textbook examples of two of the most elementary inference rules.

---

**2.  Name of the rules**

| Step | Formal rule (classical propositional logic) | Common name |
|------|--------------------------------------------|-------------|
| 4 | From *R → W* and *R* infer *W* | **Modus Ponens** (also called *detachment*) |
| 5 | From *W → ¬L* and *W* infer *¬L* | **Modus Ponens** again |
| 6 | From *R → W* and *W → ¬L* infer *R → ¬L* | **Hypothetical Syllogism** (also called *transitivity of imp

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Modus Ponens for steps 4 and 5 and Hypothetical Syllogism for step 6, explaining their general forms and truth-preserving nature (Level 3 criteria). Furthermore, the student exceeds expectations by discussing edge cases where the pattern might fail if interpreted cau

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Construct a proof deriving B v D from the three premises. Name each rule you use. Try working both forward from the premises and backward from the conclusion.

**Expected Answer:** **Constructing natural deduction proofs** — The proof uses constructive dilemma: from P v Q, P->R, Q->S, derive R v S. Working backwards: the conclusion B v D is a disjunction, so ask what rules produce disjunctions. Constructive dilemma does, and it requires a disjunction plus two conditionals — exactly what premises 1-3 provide. Working for *Natural deduction proofs require strategic thinking about which rules to apply and in what order. The backward strategy asks: what rule could produce the conclusion's form? The forward strategy asks: *

**Model Response:**
> **1.  What is being demonstrated?**  
The instructor is prompting the player to use the *constructive‑dilemma / proof‑by‑cases* pattern of inference.  It is a **valid rule of inference**, not a fallacy, but it is often confused with the much weaker “add‑a‑disjunction” (∨‑introduction) or with the invalid “affirming a disjunct” move.

**2.  Name of the pattern**  
- **Constructive Dilemma** (sometimes called *disjunction‑elimination with conditionals*).  
- In sequent‑style systems it is expressed as the rule **∨‑elimination** (proof by cases) together with **→‑elimination** (modus ponens) and a final **∨‑introduction**.

**3.  Why the reasoning is good (or bad when mis‑applied)**  

| Step | What happens | Why it is logically sound |
|------|--------------|---------------------------|
| 1.

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the underlying logic (Constructive Dilemma/Proof by Cases) and explains the mechanism of splitting into sub-proofs. However, the response describes the 'long form' derivation using sub-proofs and multiple steps (Level 2) rather than recognizing that Constructive Dile

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Test the syllogism using Venn diagrams. Then translate 'Nobody loves me but my mother' into categorical form. What are the categories?

**Expected Answer:** **Categorical statements, translation, and Venn diagrams** — Categorical logic deals with four statement types: All S are P (universal affirmative), No S are P (universal negative), Some S are P (particular affirmative), Some S are not P (particular negative). The syllogism 'All H are M, All M are D, therefore All H are D' is valid: the Venn diagram for the t *Categorical logic captures structure within propositions that propositional logic misses. The Venn diagram test is visual and systematic: diagram the premises, then check whether the conclusion is alr*

**Model Response:**
> We need to identify the reasoning pattern demonstrated: The instructor says propositional logic can't capture internal structure of categories; using truth tables leads to misleading counterexample row. This is about the fallacy of treating quantified statements as atomic propositions, leading to the "fallacy of the undistributed middle"? Not exactly. It's about the "fallacy of the false conversion"? No.

The scenario: All humans are mortal. All mortal things die. Therefore, all humans die. This is a valid syllogism (Barbara). In propositional logic, if you treat each premise as atomic proposition (p: All humans are mortal; q: All mortal things die; r: All humans die), you could construct a truth table where p and q are true but r false, showing invalidity. That's because propositional log

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism: propositional logic fails because it treats quantified statements as atomic propositions, ignoring internal categorical structure. They also attempt to translate the tricky sentence ('Nobody loves me but my mother') into categorical terms, though 

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build truth tables for each pair. Which pairs are logically equivalent? Explain what each equivalence (or non-equivalence) means in plain language.

**Expected Answer:** **Logical equivalence: contraposition and De Morgan's Laws** — Pair 1 (A->B and ~AvB) is equivalent: a conditional says the same thing as the negation of the antecedent or the consequent. Pair 2 (~(A*B) and ~Av~B) is equivalent: this is De Morgan's Law — the negation of a conjunction is a disjunction of negations ('not both' equals 'not-A or not-B'). Pair 3 (A- *Logical equivalence is a powerful tool for simplifying and transforming arguments. De Morgan's Laws let you move between negations of conjunctions and disjunctions of negations. The conditional-as-dis*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The instructor is prompting the classic **“material‑equivalence‑as‑meaning‑equivalence”** move – a form of *equivocation* (or *formal‑equivalence fallacy*).  The learner is asked to treat two formulas that happen to have the same truth‑table as if they *mean* the same thing in ordinary language.

**2. Name of the pattern**  
- **Formal name:** *Material‑equivalence fallacy* (sometimes called the *logical‑equivalence‑as‑semantic‑equivalence* fallacy).  
- **Related cognitive label:** *Equivalence conflation* or *semantic‑equivalence bias*.

**3. Why it is good or bad – the mechanism**  

| Step | What the learner does | Why it is misleading |
|------|-----------------------|----------------------|
| **a.** Identify that two formulas have identi

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the specific task. Instead of evaluating the logical equivalence of the three provided pairs (identifying which are equivalent and which are not), the student wrote a meta-commentary arguing that logical equivalence does not imply semantic equivalence. The st

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Which argument is deductive and which is inductive? After learning that Tweets is six feet tall and runs thirty miles per hour, what happens to each argument? Why?

**Expected Answer:** **Deductive vs inductive arguments and defeasibility** — The mathematician's argument is deductive: if the premises are true, the conclusion follows with certainty. Adding new information cannot undermine a valid deductive argument (though it might challenge a premise). The naturalist's argument is inductive: the premises make the conclusion probable, not *The key distinction is between certainty and probability, and between defeasibility and non-defeasibility. Deductive arguments either guarantee their conclusions (valid) or do not (invalid) — there is*

**Model Response:**
> **1.  The pattern that is being shown**

| Speaker | Reasoning pattern | What the pattern is called |
|---------|-------------------|----------------------------|
| **Mathematician** | *Deductive* syllogism with a universal premise | **Universal (categorical) syllogism** – a *deductively valid* form of reasoning. |
| **Naturalist** | *Inductive* syllogism that draws a probabilistic conclusion from a statistical premise | **Statistical (or probabilistic) syllogism** – a classic case of **defeasible / non‑monotonic reasoning** (often modelled with **Bayesian updating**). |

The crucial move in the story is the introduction of *new, exception‑producing information* (“Tweets is six ft tall and can run 30 mph”). That information **defeats** the universal premise and forces a revision of the pro

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly classifies both arguments (deductive vs. inductive) and provides a sophisticated explanation of defeasibility and non-monotonic reasoning for the naturalist's argument. They also correctly note that the deductive argument's validity remains intact even if the premise is challen

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe asks you to evaluate both polls. Which one should the council trust, and what are the problems with the other one?

**Expected Answer:** **Statistical generalizations: sample size and representativeness** — A good statistical generalization requires two conditions: adequate sample size and a representative sample. Pollster A fails both: 20 people is too few (hasty generalization), and surveying only at the Miners' Guild creates a biased sample that likely overrepresents mining interests. Pollster B use *Evaluating statistical generalizations requires checking sample size and representativeness. Pollster A's survey is doubly flawed: 20 people is too small to generalize from (the result could easily be*

**Model Response:**
> **1. The reasoning pattern**  
The pollster is drawing a firm, population‑wide conclusion from a *tiny, non‑random, and unrepresentative* sample.  In the language of informal logic this is the **hasty‑generalization** (also called the “insufficient‑sample” or “anecdotal‑evidence” fallacy).  In the language of statistics it is a **biased‑sample / sampling‑bias error** that ignores sampling variability.

**2. Precise name**  

| Discipline | Name of the error |
|------------|-------------------|
| Informal logic / philosophy | **Hasty Generalization** (a type of inductive fallacy) |
| Statistics / decision theory | **Sampling bias / non‑representative sample** (often phrased as “biased sample fallacy” or “small‑n overconfidence”) |

**3. Why the reasoning is faulty (mechanism)**  

| Step | 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'Hasty Generalization' and 'Sampling Bias'. They explicitly detail both required conditions (sample size and representativeness) with statistical rigor, explaining why Pollster A fails and Pollster B is superior. Furthermore, they exceed the Level 3 re

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Three investigators each offer an explanation. Evaluate each one using the explanatory virtues. Which is the best explanation, and why?

**Expected Answer:** **Inference to the best explanation and explanatory virtues** — IBE selects the hypothesis that best explains the observed evidence according to the explanatory virtues. Lira's explanation (teleportation by rogue mage) is unfalsifiable, inconsistent with background knowledge, and introduces unnecessary entities — it fails on simplicity, testability, and consiste *IBE is not about which explanation is merely possible — all three are possible. It is about which explanation does the best job of accounting for the evidence according to the explanatory virtues. Lir*

**Model Response:**
> ## 1.  The reasoning pattern that all three investigators are **using** – and the way each of them **mis‑applies** it – is **abductive reasoning** (also called *inference to the best explanation*).  
Abduction is the move:

> “Given the facts we have, the hypothesis that would most plausibly make them true is …”

When abductive moves are made without checking the **explanatory virtues** (simplicity, scope, coherence, conservatism, fruit‑fulness, etc.) they readily turn into a family of well‑known **fallacies / biases**.  

| Investigator | What they claim | Which classic bias / fallacy it collapses into | Why it is a misuse of abduction |
|--------------|----------------|-----------------------------------------------|--------------------------------|
| **Inspector Lira** | “The goods were

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as Inference to the Best Explanation (IBE) and begins to apply explanatory virtues (specifically simplicity) to reject Lira's hypothesis. However, the response is incomplete; it cuts off mid-sentence while analyzing Lira and fails to evaluate Ga

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher draws an analogy between the drowning child and the daily coffee purchase. Is it a good analogy? Evaluate the relevant similarities and the disanalogies Aldric raises. Which disanalogies, if any, are relevant to the moral conclusion?

**Expected Answer:** **Argument by analogy: relevant similarities and disanalogies** — An argument by analogy infers that because two things share relevant similarities, what is true of one is probably true of the other. The philosopher argues: (1) The pond case and the coffee case share a relevant similarity — choosing a luxury over a child's survival. (2) In the pond case, saving th *Evaluating analogies requires identifying the relevant similarities and assessing whether the disanalogies matter. The philosopher's analogy is strong because the core moral feature — valuing a luxury*

**Model Response:**
> **1. What is being demonstrated?**  
The philosopher is employing an **analogy‑based argument that is structurally unsound** – a classic case of the **false (or weak) analogy** fallacy.  Aldric’s objection also touches on the **relevance‑obligation bias** (the intuition that “nearby” harms feel more obligatory than distant ones), but the core logical error is the faulty analogy.

**2. Name of the pattern**  
- **False (Weak) Analogy** – sometimes catalogued as *faulty analogy* or *inappropriate comparison*.  
- (Related, but not primary: *Appeal to Emotion* – “save the child” imagery.)  

**3. Why the reasoning is bad (the mechanism)**  

| Element of a sound analogy | What the philosopher gets wrong |
|----------------------------|---------------------------------|
| **Relevant similarity

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as an analogy (specifically a 'False Analogy') and successfully lists the core similarity (preventing harm at low cost) and multiple disanalogies (proximity, efficacy, certainty). However, the response fails to reach Level 3 because it does not systematic

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Using the vet's log, apply the necessary condition test and the sufficient condition test to each factor. Which factor is the likely cause of Whiskers' seizures?

**Expected Answer:** **Mill's methods: necessary and sufficient condition tests** — The necessary condition test: which factor is present in every seizure case? F is present in all three seizure days. T is present in days 1 and 3 but not day 2. V is present in days 1 and 2 but not day 3. Only F passes the necessary condition test. The sufficient condition test: which factor is abse *Mill's methods provide systematic tools for causal investigation. The necessary condition test eliminates factors that are absent when the effect occurs. The sufficient condition test eliminates facto*

**Model Response:**
> **1.  What reasoning pattern is on display?**  
The veterinarian is trying to infer a *causal* factor from a tiny set of observations by asking two questions that are the classic **necessary‑condition test** (“Is the factor present on every seizure day?”) and **sufficient‑condition test** (“Is the factor absent on every non‑seizure day?”).  

In the language of informal logic this is the **“necessary‑and‑sufficient condition” test** – a form of *inductive* causal reasoning that is usually presented as Mill’s **Method of Agreement** (look for a common factor on all positive cases) together with Mill’s **Method of Difference** (look for a factor that is missing on all negative cases).  

When it is applied to a handful of observations without controlling for confounds, it becomes the classic

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as causal inference using Mill's Methods (Agreement and Difference), which aligns with the necessary and sufficient condition tests described in the key. They accurately define the mechanism for both tests. However, the response is incomplete; t

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Councillor Drava claims the tonic causes higher yields based on the correlation data. What is wrong with this inference? Identify the alternative explanations.

**Expected Answer:** **Correlation vs causation: third variable and reverse causation** — When two things are positively correlated, there are four logical possibilities: (1) A causes B, (2) B causes A, (3) a third variable C causes both, (4) the correlation is coincidental. Drava assumes possibility 1 (tonic causes higher yields). The physician raises possibility 3 (wealth is the confou *Recognizing that correlation does not establish causation is essential for evaluating empirical arguments. To establish causation, you need to rule out confounding variables and reverse causation — ty*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The discussion is a textbook case of **mistaking correlation for causation** – specifically the *cum‑hoc* (or *post‑hoc*) fallacy that ignores **confounding variables** (and the possibility of reverse causation).  

**2. Name of the pattern**  

| Common name | Formal name (statistics / decision theory) |
|-------------|--------------------------------------------|
| “Correlation‑causation” fallacy | **Omitted‑variable bias / confounding** (also called **spurious correlation**). |
| When the direction of the arrow is reversed | **Reverse‑causation fallacy** (a subtype of the same error). |

**3. Why the reasoning is faulty (or, when it can be good)**  

| Step in Drava’s argument | Why it fails |
|--------------------------|--------------|
| *

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'correlation vs. causation' pattern and explicitly names the false cause fallacy. They thoroughly explain both alternative mechanisms: the confounding variable (wealth) and reverse causation. Furthermore, they go beyond the Level 3 requirements by explaining that

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Solve the three probability problems. Show your work and explain which probability law you use for each one.

**Expected Answer:** **Basic probability laws: complement, addition, conjunction** — Problem 1 (complement): P(not-4) = 1 - P(4) = 1 - 1/6 = 5/6. Problem 2 (addition with correction): P(at least one H) = P(H on coin 1) + P(H on coin 2) - P(H on both) = 1/2 + 1/2 - 1/4 = 3/4. Alternatively, use complement: 1 - P(no heads) = 1 - 1/4 = 3/4. Problem 3 (at least one via complement): P(at *The complement rule is the most useful tool in basic probability: often it is easier to calculate the probability of something NOT happening and subtract from 1. The addition rule must correct for dou*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The dice‑master is warning against the *“add‑the‑probabilities”* mistake – treating several independent (or merely possible) events as if they were mutually exclusive and therefore adding their individual probabilities to obtain the probability of “at least one” occurring.  

In the language of probability theory this is a **mis‑application of the addition rule** (or, equivalently, a failure to apply the **inclusion–exclusion principle**).  In informal terms it is often called the **“union‑fallacy”** or **“addition‑fallacy for non‑disjoint events.”**  

---

**2. Precise name**  

* **Addition‑rule misuse (union fallacy / inclusion‑exclusion error).**  
* In decision‑theoretic parlance it is a specific instance of **“over‑counting”** when eval

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the reasoning pattern (misapplication of addition rule/inclusion-exclusion) and explains the mechanism (double-counting) and the correct complement approach with high theoretical accuracy. However, the response is incomplete; it cuts off abruptly at the header for Se

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The magistrate asks: given Bob's 99% accuracy and 1000 people in the area with 5 actual robbers, what is the probability that Nancy is truly the robber? Show your reasoning.

**Expected Answer:** **Conditional probability, Bayes' theorem, and base rate reasoning** — The naive answer is 99%, but this ignores the base rate. Using Bayes' theorem: Of 1000 people, 5 are robbers. Bob correctly identifies 99% of 5 robbers = 4.95 true positives. Bob incorrectly identifies 1% of 995 innocent people = 9.95 false positives. Total positive identifications = 4.95 + 9.95 = 1 *Conditional probability requires updating prior probabilities with new evidence. The key insight is that when the base rate is low (few robbers in the population), even a highly accurate test produces*

**Model Response:**
> **1.  What kind of reasoning is on display?**  
The magistrate’s line of thought is a classic **base‑rate neglect / inverse‑probability error**, most often called the **Prosecutor’s Fallacy** (or “fallacy of the transposed conditional”).  

**2.  Name (precise label)**  
*Prosecutor’s Fallacy* – the mistake of equating  

\[
P(\text{identification} \mid \text{innocent})\; \text{or}\; P(\text{identification} \mid \text{guilty})
\]

with  

\[
P(\text{guilty} \mid \text{identification}).
\]

It is a special case of **base‑rate neglect**, i.e. ignoring the prior prevalence of the trait (here, “being the robber”).

**3.  Why the reasoning is (usually) wrong**  

| Step in the magistrate’s argument | Correct Bayesian view |
|-----------------------------------|------------------------|
| “Bob i

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern (Prosecutor's Fallacy/Base-rate neglect) and distinguishes between the conditional probabilities conceptually, which exceeds Level 1. However, the response is incomplete; it fails to perform the actual calculation to reach the ~33% figure required for Lev

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The patient believes she has a 95% chance of having colon blight. Is she right? Use the base rate and test accuracy to compute the actual probability. Show your work.

**Expected Answer:** **Base rate reasoning in medical screening** — For a population of 100,000: 500 have colon blight (0.5% base rate). Of those 500, the test correctly identifies 95% = 475 true positives. Of the 99,500 without the disease, the test incorrectly flags 5% = 4,975 false positives. Total positive results = 475 + 4,975 = 5,450. P(disease | positive test *The base rate fallacy occurs when people ignore the prior probability of a condition and treat the test accuracy as the probability of having the condition. When a disease is rare (0.5%), the 5% false*

**Model Response:**
> **1. What is being demonstrated?**  
The physician (and the patient) are ignoring the *prior probability* (the prevalence of the disease) when interpreting a test result.  This is the classic **base‑rate neglect** (also called the **base‑rate fallacy** or, in legal contexts, the **prosecutor’s fallacy**).  It is a specific instance of the broader *representativeness heuristic* – judging the likelihood of an event by how closely the evidence (a positive test) matches the stereotypical description (a “positive” result) and forgetting how common that event actually is.

---

**2. Precise name**  

- **Base‑rate neglect / base‑rate fallacy**  
- (Related concepts: *representativeness heuristic*, *inverse probability error*, *diagnostic bias*.)

---

**3. Why the reasoning is flawed (mechanism)

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the base-rate fallacy by name, explains the mechanism using both Bayes' theorem and the logic of priors, and accurately calculates the probability as approximately 8.7%. However, the response does not fully meet Level 4 criteria because it lacks the specific nuance o

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sergeant Dallow seems confident in his logic. Look at the sign, then look at his reasoning. Does his conclusion actually follow?

**Expected Answer:** **Denying the antecedent** — Dallow reasons from 'If royal writ, then entry' and 'no royal writ' to 'no entry.' He treats the antecedent as necessary when the sign only establishes it as sufficient. *The conditional only tells us P is sufficient for Q, not necessary. Denying the antecedent does not validly yield the denial of the consequent. Other conditions may also lead to Q.*

**Model Response:**
> **1. What is being demonstrated?**  
The guard is using a **formal logical fallacy – the *fallacy of denying the antecedent*** (also called the *inverse error*).  
In everyday language it shows up as “because the rule says *if* you have a writ you may pass, *therefore* if you don’t have a writ you may not pass.”

---

**2. Name of the pattern**  

- **Formal name:** *Denying the Antecedent* (inverse error).  
- **Colloquial equivalents:** “rule‑worship”, “literalist interpretation”, “over‑strict reading of a conditional”.

---

**3. Why the reasoning is (usually) bad – the mechanism**  

| Step in the guard’s reasoning | Logical form | Why it fails |
|------------------------------|--------------|--------------|
| “If you carry a royal writ, you may pass.” | \(P \rightarrow Q\) (P = “carry

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('Denying the Antecedent'), correctly distinguishes between sufficient and necessary conditions, and explains that the error arises from treating a conditional as a biconditional. This meets all criteria for the highest level of the rubric.

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Wynn seems sure it was a wolf. Does the conclusion follow from what she observed?

**Expected Answer:** **Affirming the consequent** — Wynn reasons from 'If wolf then large paw prints' and 'large paw prints' to 'wolf.' She treats the consequent as proof of the antecedent. *The conditional tells us a wolf attack would produce large paw prints, but many other causes could too. Observing Q does not allow us to conclude P.*

**Model Response:**
> **1. The reasoning pattern**  
Wynn is using a *deductive* inference of the form  

\[
\text{If a wolf attacked the sheep, then large paw prints would be found.}  
\]
\[
\text{Large paw prints are found.}  
\]
\[
\therefore \text{A wolf attacked the sheep.}
\]

This is the classic **affirming‑the‑consequent** (also called the *converse error*).  It is a logical fallacy that also shows up as a *confirmation‑bias* style of reasoning: the evidence that seems to confirm the hypothesis is taken as proof, without checking whether the evidence could arise from other causes.

---

**2. Precise name**  

*Affirming the consequent* (converse error).  
In informal terms it is often described as “*confusing a necessary condition with a sufficient one*”.

---

**3. Why the reasoning is faulty (or, when

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('affirming the consequent'), correctly explains the logical mechanism by distinguishing between necessary and sufficient conditions, and identifies specific alternative hypotheses and additional evidence needed to validate the conclusion. This meets all crit

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Varn seems very worried about this bakery permit. He has given you a chain of consequences. Do you find his reasoning convincing? Why or why not?

**Expected Answer:** **Causal slippery slope** — Varn chains together a sequence of causal claims — competition leads to price drops leads to corner-cutting leads to illness leads to overwhelmed healers leads to plague — treating each link as inevitable. Even if each individual step had a 90% probability, the probability of the entire six-step cha *Probabilities are not preserved across a chain of causal claims. Each link in the chain has its own probability of occurring, and the joint probability of the entire sequence is the product of all the*

**Model Response:**
> **1. The reasoning pattern at work**  
The councilor is presenting a *causal‑slippery‑slope* argument that proceeds from a relatively minor regulatory decision (granting a bakery permit) to an extreme, catastrophic outcome (a town‑wide plague). In the language of informal logic it is classified as the **“slippery‑slope fallacy”** (sometimes called a *causal chain* or *domino* fallacy).  

It also drags in a **fear‑appeal (ad baculum)** because the chain is framed as an inevitable disaster that will befall anyone who votes “yes”.

---

**2. Precise name**  

- **Slippery‑Slope Fallacy (causal version)**  
- When the argument is used to scare the audience, it can be labeled **Appeal to Fear (ad baculum)**, but the logical core is the slippery‑slope.

---

**3. Why the reasoning is flawed (me

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'causal slippery slope' pattern and provides an excellent qualitative breakdown of why each link is uncertain and non-deterministic. They explicitly note that the argument treats probabilistic events as certainties. However, the response falls short of Level 4 be

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Pip seems very confident in his proof. Is his reasoning valid? Can you spot the mistake?

**Expected Answer:** **Composition fallacy** — Pip infers that a property true of each individual part (each atom is invisible) must be true of the whole composed of those parts (Pip is invisible). But visibility is not a property that transfers from parts to whole in this way — the arrangement and quantity of atoms creates emergent properties l *Properties of individual parts do not necessarily hold for the whole they compose. Each atom is invisible, but billions of atoms arranged into a human body are very much visible. Whether a property tr*

**Model Response:**
> **1‑2.  The pattern**  
The student is committing the **fallacy of composition** (sometimes called the *part‑to‑whole* fallacy).  
Formally it can be rendered as:

*All* x *have property* P.  
*All* parts of y *are* x.  
∴ *y* *has property* P.

In Pip’s case:

*All atoms are invisible to the naked eye.*  
*All the parts of Pip’s body are atoms.*  
∴ *Pip is invisible to the naked eye.*

**3.  Why the reasoning is bad (the mechanism)**  

| Step | What actually happens | Why the inference fails |
|------|-----------------------|--------------------------|
| **Premise 1** – “Every atom is invisible” | True: a single atom is far below the resolution limit of human vision. | The premise is about **individual, isolated** particles. |
| **Premise 2** – “I am made of atoms” | True: all macroscop

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy of composition, explains the mechanism by distinguishing between distributive and non-distributive (emergent) properties like visibility, and provides clear examples of edge cases (mass, charge) where the part-to-whole inference is valid. This meets all c

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorin is trying to figure out how much individual parts of the house are worth based on the total value. Does his reasoning work?

**Expected Answer:** **Division fallacy** — Dorin infers that because the whole house has a certain property (being worth 900 gold), each part of the house must share that property proportionally. But the house's value comes from the arrangement and integration of its parts, not from the parts individually. Disassembled lumber and stones are  *The value of the house is an emergent property of its assembled structure — location, craftsmanship, functional integration. Individual beams and stones do not carry proportional shares of that value.*

**Model Response:**
> **1‑2.  The pattern**  
The reasoning is the classic **Fallacy of Division** (sometimes called the *per‑unit* or *averaging* fallacy).  
It is the mirror image of the more familiar *fallacy of composition*: it assumes that because a property (here, a monetary value) holds for the whole object, the same property must hold for each of its constituent parts, proportionally to their count.

**3.  Why the reasoning is faulty (or, when it can be right)**  

| Step in Dorin’s argument | What he assumes | Why it is a mistake |
|--------------------------|----------------|----------------------|
| “The house is worth 900 gp.” | The house has a single, well‑defined market price. | True – the market price is a *bundle* value, not a sum of independent component values. |
| “There are about 900 compone

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Fallacy of Division' and provides a sophisticated explanation of emergent properties (synergies, non-additive valuation, heterogeneous components). They clearly distinguish between bundle value and component value, addressing why the inference fails. Furthermore, th

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Brother Vassyl seems very confident. What do you think about the reasoning he just gave you for trusting the Codex?

**Expected Answer:** **Begging the question (circular reasoning)** — The conclusion — that the Codex is the ultimate authority — is assumed as a premise when the speaker cites the Codex's own claim of infallibility as evidence. The premise and conclusion are nearly identical. *The argument assumes exactly what it is trying to prove. The Codex's reliability is the very thing in question. Formally the argument can be valid — 'P, therefore P' is valid — but validity alone is n*

**Model Response:**
> **1. What is being demonstrated?**  
A classic case of **circular reasoning** (also called *petitio principii* or “begging the question”) combined with an **self‑referential appeal to authority**. The text is taken as true *because the text itself says it is infallible*.

**2. Name of the pattern**  
- **Circular justification / begging the question**  
- More specifically in this context: **self‑sealing appeal to authority** (the source of authority is the very claim it is trying to prove).

**3. Why the reasoning is (un)reliable**  

| Step | What the argument does | Why it fails (or succeeds) |
|------|------------------------|----------------------------|
| **Premise** | “Chapter 1 of the Codex says every word is the unassailable truth.” | The premise is a *claim* about the text’s reli

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'begging the question' and 'circular reasoning.' They clearly explain the mechanism: the premise (the Codex claims infallibility) assumes the conclusion (the Codex is infallible). Furthermore, they exceed the Level 3 requirements by explicitly noting t

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Harsk says you must either march north or starve. What is wrong with how he has framed the choice?

**Expected Answer:** **False dichotomy (black-or-white thinking)** — A disjunction is presented as exhaustive when it is not. Harsk forces a choice between two options while ignoring alternatives like fortifying defenses, sending scouts, hiring mercenaries, or appealing to a neighboring lord. *Harsk presents only two options — march or starve — but the disjunction does not exhaust the relevant space. Multiple unmentioned alternatives exist.*

**Model Response:**
> **1. What is being demonstrated?**  
The commander is using a **false‑dichotomy (false dilemma) framing** together with an **appeal to fear (ad baculum)**. He pretends that only two mutually exclusive courses of action exist – “march north and crush the bandits” **or** “stay put and starve to death” – and tries to force a decision by threatening a catastrophic outcome.

**2. Name of the pattern**  
- **False‑dilemma / false‑choice fallacy**  
- (Often coupled with an **appeal to fear** or **scare‑tactic**)

**3. Why the reasoning is faulty (or, when it can be useful)**  

| Element | Mechanism that makes it bad | When it can be legitimate |
|---------|----------------------------|---------------------------|
| **False‑dilemma** | • Reduces a complex decision space to only two options, igno

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the false dichotomy fallacy, explains that the disjunction is not exhaustive by listing multiple concrete alternatives (e.g., hiring mercenaries, negotiating, defensive postures), and discusses the specific condition under which a disjunctive syllogism would be valid (ge

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Silvertongue claims this argument is logically airtight. Is it? Where does the reasoning go wrong?

**Expected Answer:** **Equivocation** — The argument uses the word 'nobody' in two different senses. In 'Nobody is perfect,' 'nobody' means 'no person' (a universal negative quantifier). In 'Bert is a nobody,' 'nobody' means 'an unimportant or insignificant person.' The argument treats these as the same meaning, creating an illusion of va *The argument trades on an ambiguity. 'Nobody' as a quantifier (no person) and 'nobody' as a noun (an insignificant person) are different concepts. Once you disambiguate the two meanings, the argument *

**Model Response:**
> **1. What is being demonstrated?**  
A classic **semantic‑ambiguity fallacy** – the argument hinges on the word **“nobody”** being used with two different senses and the speaker treats those senses as if they were the same.

**2. Name of the pattern**  
*Fallacy of equivocation* (sometimes catalogued as *amphiboly* or *lexical ambiguity*).  

**3. Why the reasoning is (in)valid**  

| Premise | Intended reading | Ambiguous reading used by Silvertongue |
|---------|------------------|----------------------------------------|
| 1. “Nobody is perfect.” | *No person* is perfect (∀x ¬Perfect(x)). | “Nobody” is a **proper name** referring to a particular individual (∃x (Nobody(x) ∧ Perfect(x))). |
| 2. “Bert is a nobody.” | Bert belongs to the class *nobody* (i.e., he is an unimportant person). 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'Fallacy of equivocation' and accurately explains that 'nobody' shifts meaning between a quantifier ('no person') and a predicate/noun ('unimportant person'). The use of formal logic notation demonstrates a strong grasp of the mechanism. However, the r

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Scholar Tilde claims there is no real difference between a novice and an archmage because you cannot draw a sharp line between the ranks. Is she right?

**Expected Answer:** **Conceptual slippery slope** — Tilde exploits the vagueness of category boundaries. Because there is no sharp line between novice and apprentice, or apprentice and journeyman, she concludes there is no real difference between the extremes. This is the sorites paradox applied to conceptual categories: if removing one grain of sand *The inability to draw a sharp boundary between adjacent cases does not mean there is no difference between the extremes. A first-day novice and an archmage differ enormously in ability, even if the tr*

**Model Response:**
> **1. What is being demonstrated?**  
The scholar is committing the **continuum (or sorites) fallacy** – the claim that because a property changes only by infinitesimal steps, any categorical division of it must be “arbitrary nonsense.”

**2. Name of the pattern**  
*Continuum fallacy* (also called the *sorites paradox*, *fallacy of the heap*, or *vagueness‑fallacy*).

**3. Why the reasoning is (usually) bad**  

| Step in the argument | Why it fails |
|----------------------|--------------|
| **Premise:** “Each student differs from the next by the tiniest increment of skill, so there is no sharp line.” | True – the underlying ability is a continuous variable. |
| **Conclusion:** “Therefore the ranks (novice, apprentice, …) are meaningless.” | **Invalid inference.** The absence of a *natura

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the continuum/sorites fallacy, explicitly explaining that the absence of a sharp boundary does not negate the meaningful difference between extremes. They accurately describe the mechanism (confusing epistemic vagueness with ontological meaninglessness

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Grus seems pretty passionate about this. But take a step back: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely?

**Expected Answer:** **Abusive ad hominem** — Grus attacks Maren's personal background (newcomer status, lack of farmland, occupation) instead of engaging with the substance of her irrigation proposal: the river data, crop projections, costs, and affected families. He treats her identity as grounds for dismissing the argument. *The quality of an argument is independent of who presents it. Maren's proposal stands or falls on its evidence and reasoning, not on how long she has lived in Ironvale or whether she owns farmland. Gr*

**Model Response:**
> **1‑2.  The pattern being displayed**  
The Alderman is committing an **ad hominem (circumstantial) fallacy**, also called a **genetic fallacy** when the objection is based on the *origin* of the idea rather than on its content. He dismisses Councillor Maren’s irrigation proposal simply because she is a recent newcomer and a shop‑keeper, not because of any flaw in the data, projections, or reasoning she presented.

---

### 3.  Why this reasoning is faulty (and when it can feel “right”)

| Aspect | What the fallacy does | Why it is a problem |
|--------|----------------------|---------------------|
| **Focus on the messenger** | Evaluates the proposal on Maren’s personal background (“newcomer”, “doesn’t own farmland”) rather than on the empirical evidence she supplied. | The truth of a cla

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as ad hominem (and genetic fallacy), explicitly explains that Maren's background is irrelevant to the empirical data provided, and articulates the specific edge case where personal credibility would be relevant (e.g., conflict of interest or fabricated da

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The merchant demands you prove his amulet doesn't work. What is wrong with this?

**Expected Answer:** **Burden of proof** — Shifting the burden of proof from the person making the claim to the person questioning it. *The person making a positive claim bears the responsibility of providing evidence. The inability to disprove something does not constitute evidence that it is true.*

**Model Response:**
> **1. What is being demonstrated?**  
A classic *burden‑shifting* move that treats the **absence of disproof** as proof of a claim. In informal‑logic terminology it is the **argument from ignorance** ( *argumentum ad ignorantiam* ) – “you can’t show there is no magical barrier, therefore there is one.” It is also a **burden‑of‑proof fallacy**: the claimant (the merchant) refuses to provide any positive evidence and instead forces the opponent to try to prove a negative.

---

**2. Name (precise label)**  

- **Argument from ignorance** (ad ignorantiam)  
- **Shifting the burden of proof** (sometimes called “appeal to lack of disproof”)  

Both labels refer to the same logical error; the first emphasizes the faulty inference, the second the procedural misuse of who should supply evidence.

-

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('Argument from ignorance' and 'Shifting the burden of proof'), provides a detailed mechanistic explanation of why the reasoning fails (treating absence of disproof as proof), and correctly identifies that the claim is unfalsifiable. The response exceeds the 

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Ranger Harlen rejects the fossil evidence because he can't imagine fish becoming people. What error is he making?

**Expected Answer:** **Personal incredulity** — Dismissing a claim because one personally cannot understand or imagine how it could be true. *The complexity of a claim has no bearing on its truth. Many well-supported facts are deeply counterintuitive. Personal failure to comprehend is not a refutation.*

**Model Response:**
> **1. The reasoning pattern being displayed**  
The senior ranger is committing an **Argument from Personal Incredulity** (also called the *personal‑incredulity fallacy*).  It is a variant of the broader **argument from ignorance** (argumentum ad ignorantiam) and is often bolstered by an **appeal to authority/tradition** (“I’ve been a ranger for 40 years, so I know what’s possible”).

**2. Precise name**  
- **Argument from Personal Incredulity**  
- (Often paired with an **Appeal to Authority/Tradition**)

**3. Why the reasoning is flawed (or, when it can be useful)**  

| Element | What the ranger does | Why it is a fallacy / bias |
|---------|----------------------|---------------------------|
| **Premise** | “I have never seen a fish sprout legs, therefore fish could not evolve into hum

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Argument from Personal Incredulity' and correctly explains the mechanism: conflating personal experience/inability to imagine with objective falsehood. They further distinguish between the heuristic value of skepticism and its misuse as logical proof, while noting c

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Every time Seer Vashti's powers fail a test, she adds a new excuse. What reasoning error is this?

**Expected Answer:** **Special pleading / No true Scotsman** — When a claim is shown to be false, moving the goalposts by introducing ad hoc exceptions so the claim can never be falsified. *Each time counter-evidence appears, a new exception is added. This makes the claim unfalsifiable. A claim that cannot in principle be proven wrong is not meaningfully supported.*

**Model Response:**
> **1. The reasoning pattern**

The diviner’s reply is a classic **ad‑hoc rescue / “no‑true‑Scotsman” move that makes the claim unfalsifiable**.  
When the test fails, the diviner does not accept the result as evidence against psychic ability; instead she re‑defines the conditions under which “real” psychic power can operate (“only when the subject’s mind is not hostile”). The new clause is introduced *after the fact* solely to protect the original claim.

**2. Name of the pattern**

- **Ad‑hoc hypothesis (or ad‑hoc rescue)** – a post‑hoc addition to a theory that explains away a falsifying observation.  
- Closely related: **No‑true‑Scotsman fallacy** (re‑defining the class “real psychics” so that counter‑examples are excluded).  
- In a broader sense it is also a form of **special pleading

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names 'special pleading' alongside related concepts, clearly articulates how the ad-hoc exception renders the claim unfalsifiable ('immune to falsification'), and thoroughly explains the scientific requirement for pre-specified conditions under which a claim could be proven wr

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Greaves demands a yes-or-no answer. What is the problem with this question?

**Expected Answer:** **Loaded question** — A question containing a built-in assumption so that any direct answer appears to confirm it. *The question presupposes something not established — that Maren used contaminated herbs. Both yes and no accept the false premise.*

**Model Response:**
> **1. What is being demonstrated?**  
The alderman’s demand is a classic **loaded‑question / complex‑question fallacy** (often paired with a **false‑dilemma** framing).  

**2. Name of the pattern**  
- **Loaded (or “complex”) question** – a single question that presupposes a claim that has not been proven.  
- (Related) **False‑dilemma (binary‑choice) framing** – insisting the answer must be “yes” or “no” when other possibilities exist.

**3. Why the reasoning is problematic (or, in rare cases, useful)**  

| Element | How it works | Why it is a fallacy / bad reasoning |
|---------|--------------|--------------------------------------|
| **Presupposition** | “Have you **stopped** using contaminated herbs?” assumes two things: (a) Maren *has* been using contaminated herbs, and (b) the only 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'loaded question' and 'false-dilemma' patterns. They clearly explain the embedded presupposition (that Maren was using contaminated herbs) and how the binary framing traps the respondent. Furthermore, they provide a strategic approach to reject the premise by clarify

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The alchemist tested in thirty villages but only shows five. What reasoning error is he committing?

**Expected Answer:** **Texas sharpshooter** — Cherry-picking data clusters that suit a conclusion while ignoring data that does not. Like painting a target around bullet holes after shooting. *Finding a cluster in a large dataset is virtually guaranteed by chance. Selecting after the fact and presenting as evidence is statistically invalid. Honest analysis requires looking at ALL the data.*

**Model Response:**
> **1. What is being demonstrated?**  
The alchemist is engaging in **selective‑evidence presentation** – the classic *Texas‑sharpshooter* (or *cherry‑picking*) fallacy, closely tied to **confirmation bias** and **selection bias**.

**2. Name of the pattern**  
- **Texas‑sharpshooter fallacy** (a form of *cherry‑picking*).  
- Related concepts: *confirmation bias* and *post‑hoc data dredging* (multiple‑comparisons bias).

**3. Why the reasoning is flawed (or occasionally useful)**  

| Step | What the alchemist does | Why it is a problem |
|------|--------------------------|---------------------|
| **a. Collects data from many units** | Surveys 30 villages. | The data set is heterogeneous; each village is an independent observation. |
| **b. Looks for a “pattern” after the fact** | Notices t

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Texas-sharpshooter' fallacy and 'cherry-picking'. They provide a sophisticated explanation of the mechanism, distinguishing between pre-specified hypotheses and post-hoc pattern selection. Furthermore, they exceed the Level 4 requirements by discussing base rates, r

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The mediator proposes combining evidence-based treatment with unsupported one. What is wrong with this?

**Expected Answer:** **Middle ground (false compromise)** — Assuming the truth must lie between two positions simply because they are opposing, regardless of evidence. *Truth is not determined by averaging positions. When one is well-supported and the other baseless, the middle ground corrupts the good position. Draining 'some' blood is still harmful.*

**Model Response:**
> **1‑2.  The pattern**  
The mediator is committing the **“argument to moderation”** (also called the *argument from the middle*, *false compromise*, *both‑sidesism* or *argumentum ad temperantiam*).  

---

**3.  Why it is a problem (mechanism)**  

| Step | What happens | Why it is faulty |
|------|--------------|------------------|
| **a. Identify two extreme claims** | “The herbal compound alone cures the plague” vs. “We must drain patients’ blood.” | The claims are presented as mutually exclusive extremes. |
| **b. Assume the truth must lie somewhere between** | “We should use the compound **and** drain a moderate amount of blood.” | The reasoning treats “middle‑ness” as a proxy for truth, ignoring any independent evidence about either claim. |
| **c. Choose the compromise because it f

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('argument to moderation'), clearly distinguishes between epistemic truth and procedural/normative compromise (Level 4 requirement), explains the mechanism of false equivalence, and details how the approach incorrectly weights extreme positions against eviden

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dag dismisses mine dust danger because his grandfather survived it. What reasoning error?

**Expected Answer:** **Anecdotal evidence** — Using personal experience or an isolated example in place of statistical evidence, especially to dismiss systematic data. *A single case cannot override systematic evidence. Dag's grandfather is one data point — possibly an outlier. The question is the overall rate of lung disease among miners, not whether anyone can surv*

**Model Response:**
> **1. The reasoning pattern**  
The miner is relying on a single, highly selective personal story to dismiss a general health claim. Two closely‑related cognitive errors are at work:

| Name | Why it fits the dialogue |
|------|--------------------------|
| **Anecdotal (or “argument from personal experience”) fallacy** | He treats his grandfather’s long, apparently healthy life as proof that the dust cannot be harmful. |
| **Survivorship bias** | He only looks at the *survivors* of the mine’s workforce (the grandfather who lived to 97) and ignores the many workers who may have died early or suffered disease. |

Both labels describe the same underlying mistake, but “survivorship bias” pinpoints the selective sampling problem, while “anecdotal fallacy” captures the logical move of substitutin

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Anecdotal fallacy' and 'Survivorship bias,' perfectly matching the Level 4 requirement. They provide a sophisticated explanation of why a single case cannot outweigh systematic data (ignoring base rates, invisible denominator) and analyze the psychological compellin

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What is wrong with Alderman Grask's response to Sable's proposal?

**Expected Answer:** **Straw man** — Grask inflates Sable's modest proposal (a south-bank levee) into an extreme position (damming the entire river) and then attacks the extreme version. His criticism C targets fabricated position B, not Sable's actual position A. *Grask's criticism targets a fabricated version of Sable's proposal. A south-bank levee does not dam the river. His objections about livestock and mills are irrelevant to the actual proposal.*

**Model Response:**
> **1‑5.  Analysis of Alderman Grask’s reply**

| # | Element asked for | Answer |
|---|-------------------|--------|
| **1** | **What reasoning pattern is being demonstrated?** | A *straw‑man* move (often blended with a *slippery‑slope* appeal). Grask takes Sable’s modest, local levee proposal and re‑casts it as a far‑reaching dam that would “cut off water to every farm downstream.” He then attacks that exaggerated version. |
| **2** | **Name it precisely** | **Straw‑Man Fallacy** (sometimes called *misrepresentation* or *argument‑by‑mischaracterisation*). When the “slippery‑slope” language is added (“if we do this, the whole valley will die”), it can be described as a *straw‑man‑slippery‑slope* hybrid, but the core error is the straw‑man. |
| **3** | **Explain the mechanism: why it is good

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Straw-Man Fallacy,' accurately explains the mechanism by contrasting Sable's actual proposal (levee) with Grask's distortion (dam), demonstrates why the refutation is irrelevant, and provides a comprehensive, structured approach for a fair rebuttal including evidenc

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Garrett fires back at Inspector Maren by bringing up the oil-lantern incident. What is wrong with his reasoning? Why doesn't Maren's past mistake let Garrett off the hook?

**Expected Answer:** **Tu quoque (appeal to hypocrisy)** — Dismissing a criticism by pointing out that the person making it is guilty of the same or similar fault. Treats the critic's inconsistency as though it refutes the content of the criticism. *Whether or not the critic is a hypocrite has no bearing on the truth of the criticism. The coal dust is either a fire hazard or it is not, regardless of what Maren did last winter. Hypocrisy is a char*

**Model Response:**
> **1‑5.  Analysis of Garrett’s reply**

| # | Element asked for | Answer |
|---|-------------------|--------|
| **1** | **What kind of reasoning is being displayed?** | A *personal‑attack* that tries to invalidate the inspector’s argument by pointing out the inspector’s own past misconduct.  In the taxonomy of informal fallacies it is the **tu‑quoque** (Latin for “you also”) variant of the **ad hominem** fallacy. |
| **2** | **Name it precisely** | **Tu‑quoque ad hominem** (sometimes called the “appeal to hypocrisy”). |
| **3** | **Why is it (generally) a bad line of reasoning?** | 1. **Irrelevance to the claim** – The safety rule (“store coal‑dust ≥ 30 paces from dwellings”) is a factual matter that can be true or false regardless of Maren’s past negligence.  <br>2. **Shift of focus** – By

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'tu quoque' (Level 3 criteria) and provides a robust explanation of why it is a fallacy of relevance, noting that the truth of the claim is independent of the critic's behavior. Furthermore, the student exceeds Level 3 by explicitly outlining what a le

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorric clearly does not like this formula. But does he point out any problem with the measurements, the chemical rationale, or the engineering requirements? What is his objection really about?

**Expected Answer:** **Genetic fallacy** — Dorric judges the formula by attacking its origin — Vielle's impoverished background — rather than engaging with its content. The chemical rationale and measurements go entirely unaddressed. *The quality of a formula depends on its content — the logic, evidence, and reasoning — not on the biography of whoever produced it. Vielle's background tells you nothing about whether her measurements*

**Model Response:**
> **1‑2.  The pattern**  
Dorric is committing a **genetic fallacy** (sometimes cast as an *ad hominem circumstantial* or a *negative appeal to authority*). He rejects Vielle’s heat‑resistant‑glass formula solely because of the *origin* of the idea – her “workhouse” background – rather than on any substantive evidence about the formula itself.

---

### 3.  Why it is a reasoning error  

| Element | What Dorric does | Why it’s faulty |
|---------|------------------|-----------------|
| **Premise** | “Vielle learned her trade in a poorhouse; therefore her formula is worthless.” | The premise links *social origin* to *truth value* without any logical bridge. The truth of a scientific claim depends on empirical support, not on who first thought of it. |
| **Structure** | *If X comes from a low‑

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the genetic fallacy, explains that the origin of the claim is irrelevant to its truth value compared to empirical evidence, and explicitly addresses edge cases where pedigree might serve as a useful heuristic (e.g., expertise-dependent claims), fully satisfying all c

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Holt raises serious worries. But is he giving you any reason to doubt Tova's research itself?

**Expected Answer:** **Appeal to consequences** — Arguing that a factual claim should be rejected because accepting it would lead to undesirable outcomes, substituting the consequences for a critique of the evidence. *The truth of a factual claim does not depend on whether its consequences are pleasant. Consequences are relevant to policy (what to do about a finding), not to whether the finding is true.*

**Model Response:**
> **1. What is being demonstrated?**  
Guildmaster Holt is using the *appeal to (negative) consequences* to argue that Tova’s scientific finding must be rejected because of the social and economic harm it would (if accepted) produce.

**2. Name of the pattern**  
*Argumentum ad consequentiam* – the “appeal to consequences” fallacy (sometimes called the *consequentialist fallacy*). In a decision‑theoretic framing it is also a misuse of *outcome‑based reasoning* as a test of factual truth.

**3. Why the reasoning is faulty (or, when it can be useful)**  

| Element | Correct logical role | What Holt does instead |
|---------|----------------------|------------------------|
| **Premise** | “If the supplement has no effect, then the harvesters will lose income …” – a factual conditional about *c

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'appeal to consequences' fallacy and provides a sophisticated explanation of why the reasoning is faulty. They clearly distinguish between the epistemic layer (evaluating evidence/truth) and the policy layer (managing consequences), which satisfies the highest level 

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Corvin has a strong expert backing his claim. But what exactly is Eldric an expert in, and what is the question being debated?

**Expected Answer:** **Appeal to authority** — Corvin appeals to Eldric's authority as a surgeon to settle a question about marine toxicology — a field in which Eldric has no special expertise. *An authority's expertise does not transfer automatically to unrelated domains. Eldric's prestige makes his opinion influential but not reliable on marine toxicology.*

**Model Response:**
> **1. The reasoning pattern**  
The fisherman is using an *appeal to (misplaced) authority* – a form of the **argument‑from‑authority (argumentum ad verecundiam)** in which the cited “expert” is not an authority on the subject at hand.

**2. Name of the fallacy**  
*Appeal to irrelevant authority* (sometimes called *false authority* or *argument from prestige*).  

**3. Why the reasoning is faulty (or, when it can be sound)**  

| Element | What makes it a good inference | What makes it a bad inference in this case |
|---------|--------------------------------|--------------------------------------------|
| **Authority** | The source is a recognized expert **in the specific domain** of the claim (e.g., a marine biologist testifying about fish toxicity). | The source (a surgeon) is an expert

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as an 'appeal to irrelevant authority' and explicitly explains the domain mismatch between a surgeon and marine toxicology. Furthermore, the response exceeds the Level 4 requirement by detailing when citing authority is legitimate (domain-specific experti

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?

**Expected Answer:** **Appeal to emotion** — Substituting emotional response — pity, guilt, sentiment — in place of addressing the factual evidence. Geld does not contest the ledger; she tries to make accusers feel bad for asking. *Whether she sat up with sick children does not change what the grain ledger shows. The emotional response is designed to block the factual inquiry, not answer it.*

**Model Response:**
> **1. What is being demonstrated?**  
Matron Geld is using a **classic appeal‑to‑emotion fallacy** (specifically an *appeal to pity* – *argumentum ad misericordiam*) and, at the same time, a **moral‑licensing / halo‑effect bias**. She tries to “buy” moral credit for the good things she does and then uses that credit to dismiss or down‑play the concrete evidence of fraud.

**2. Name of the pattern**  

| Formal name | Common description |
|-------------|--------------------|
| **Appeal to pity (argumentum ad misericordiam)** | “You should not judge the ledger because I am a caring, self‑sacrificing person.” |
| **Moral‑licensing / halo effect** | “Because I have performed many kind acts, I am therefore exempt from criticism on other matters.” |

Both labels refer to the same underlying move:

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'appeal to pity' fallacy, clearly distinguishes between the emotional character assessment and the factual ledger evidence, and explains the cognitive mechanism (halo effect/affect heuristic). Furthermore, the response addresses the rubric's Level 4 requirement for e

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Saffron's pitch sounds appealing. What evidence does he give that the spring water cures anything? Is 'it's natural' really a reason?

**Expected Answer:** **Appeal to nature** — Arguing that a product works because it is natural, treating naturalness as sufficient evidence of safety and efficacy. *Naturalness is not a reliable indicator of safety or efficacy. Many natural substances are deadly (hemlock, arsenic). The appeal substitutes a feel-good category for actual evidence.*

**Model Response:**
> **1. The reasoning pattern being displayed**  
Saffron is relying on a *value‑based heuristic* that equates “natural” with “good / safe”. In the language of informal logic this is the **appeal to nature** (also called the *naturalistic fallacy*). It is a specific type of *argument from ignorance* – he argues that because the water is “natural” and we have no evidence of it being harmful, it must be beneficial.

**2. Precise name**  

- **Appeal to Nature** (or **Naturalistic Fallacy**).  
- Closely related: **Argument from Ignorance** (ad novum) and **Appeal to Purity** (“nothing but pure water, therefore it works”).

**3. Why the reasoning is flawed (mechanism)**  

| Step | What Saffron does | Why it fails |
|------|-------------------|--------------|
| **Premise** | “Natural = safe / ef

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Appeal to Nature' and the 'Naturalistic Fallacy,' correctly identifies the mechanism (equating natural with good/safe without evidence), provides specific counterexamples of harmful natural substances (arsenic, botulinum toxin), and distinguishes between heuristic u

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What evidence does Paddy give that the charm works? Is 'everyone is buying one' a reason?

**Expected Answer:** **Bandwagon (argumentum ad populum)** — Arguing that something must be true or good because many people believe it or do it. Treating popularity as evidence. *The number of people who believe something has no bearing on whether it is true. Popularity can be driven by social pressure, marketing, or tradition — none constitute evidence.*

**Model Response:**
> **1‑2.  The pattern**  
The vendor is using an **appeal to popularity / “bandwagon” reasoning** – formally the *argumentum ad populum* fallacy.  In the language of cognitive‑psychology it is also called **social‑proof bias** (or “herd”/conformity bias) and, in decision theory, it is the basis of a **herding / information‑cascade** heuristic.

---

### 3.  Why the reasoning is (usually) faulty  

| Step in the vendor’s pitch | What the argument assumes | Why that assumption is unreliable |
|----------------------------|---------------------------|-----------------------------------|
| “Half the village already has one.” | The proportion of people who own the charm is evidence that the charm is valuable / true. | The number of owners tells us nothing about the charm’s efficacy; people can co

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'bandwagon' fallacy and 'argumentum ad populum'. They clearly explain why popularity is not evidence (distinguishing psychological states from logical proof and correlation from causation). They identify the social pressure component ('fear of exclusion') and disting

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The deputy thinks it is more likely that Linda is a bank clerk AND an activist than that she is just a bank clerk. Is the deputy's reasoning correct?

**Expected Answer:** **Conjunction fallacy** — The deputy judges P(bank clerk AND activist) > P(bank clerk). This violates a basic law of probability: the probability of a conjunction can never exceed the probability of either conjunct alone. P(A and B) <= P(A). The error occurs because the conjunction fits a compelling narrative (the 'represent *A conjunction adds a constraint. Every bank clerk who is also an activist is already counted among the bank clerks. The set of people who are both A and B is a subset of the set of people who are A. N*

**Model Response:**
> **1. What is being demonstrated?**  
The deputy is committing the **conjunction fallacy** (a classic illustration of the *representativeness heuristic*). He judges the joint statement “Linda is a bank clerk **and** a member of the Fair Trade Alliance” to be more probable than the single statement “Linda is a bank clerk,” simply because the conjunction “fits” the story he has heard about her.

**2. Name of the pattern**  
*Conjunction fallacy* – often called the “Linda problem” after the original Tversky‑Kahneman experiment.

**3. Why the reasoning is flawed (or, when it can be useful)**  

| Step in the deputy’s reasoning | Formal problem |
|--------------------------------|----------------|
| **Representativeness** – The description (philosophy student, activist, outspoken) feels “typical

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the conjunction fallacy and the representativeness heuristic. They explicitly state the probability rule P(A and B) <= P(A), explain the psychological mechanism behind the error, and directly connect the scenario to the original Linda problem. The response exceeds th

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sera says there is a 95% chance the patient has Stoneblight based on the positive test. Is she right? What is the actual probability?

**Expected Answer:** **Base rate neglect** — Sera assumes that a positive result on a 95% accurate test means a 95% chance of disease. She ignores the base rate of 0.5%. For 100,000 people: 500 have Stoneblight. The test catches 475 of them (true positives). Of the 99,500 healthy people, the test falsely flags 5% = 4,975 (false positives). Tot *When the base rate of a condition is very low, even a highly accurate test produces far more false positives than true positives. The 95% accuracy tells you about the test's performance, not about thi*

**Model Response:**
> **1. What is being demonstrated?**  
The healer is **ignoring the base‑rate (prevalence) of the disease and treating the test’s sensitivity/specificity as if they were the probability that a positive result means “has the disease.”**  
In the literature this is called:

* **Base‑rate neglect (also known as the base‑rate fallacy, the inverse‑probability fallacy, or the “prosecutor’s fallacy” when applied to medical testing).**  

It is a specific instance of **mis‑interpreting conditional probabilities** and of **over‑reliance on a single piece of evidence** without integrating prior information.

---

**2. Precise name**

* **Base‑rate neglect / base‑rate fallacy**  
* (When framed as “the test is 95 % accurate, therefore a positive means 95 % chance of disease” it is also a **misinterpret

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as base-rate neglect and explains the mechanism by distinguishing between test accuracy (sensitivity/specificity) and positive predictive value. They explicitly set up and execute the Bayesian calculation using the correct values (0.95 * 0.005 / [0.95 * 0

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Minister Kael says the data proves small schools produce better scholars. Is the data as convincing as he thinks? What should he check before spending 1.7 million gold?

**Expected Answer:** **Law of small numbers / small numbers fallacy** — Kael observes that small schools top the achievement rankings and concludes that being small causes better performance. But smaller populations produce more variable outcomes: with fewer students, a few strong (or weak) performers swing the average dramatically. If Kael checked the bottom of the ran *The law of small numbers states that smaller groups will tend to inhabit the extremes of any ranking. Kael only checked the top — if he checked the bottom, he would also find small schools. The patter*

**Model Response:**
> **1. What is being demonstrated?**  
The minister is taking a simple statistical regularity – “the best‑performing schools happen to be tiny” – and treating it as a proven causal rule that should drive policy.  In logical‑psychological terms this is a **false‑cause inference** (confusing correlation with causation), and more specifically an **ecological/aggregate‑level fallacy** (the *ecological fallacy* or *ecological inference error*).  It also contains a **hasty generalisation** (extrapolating from a few data points to all schools) and a **post‑hoc‑ergo‑propter‑hoc** pattern.

**2. Name of the pattern**  

- **Correlation‑does‑not‑imply‑causation (false cause)**  
- **Ecological fallacy** (inferring that a relationship that holds for groups must hold for the individuals or sub‑units wit

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that correlation does not imply causation and suggests checking for confounding variables (Level 2). However, they fail to identify the specific statistical mechanism required for higher scores: the 'Law of Small Numbers' (that small sample sizes inherently produce m

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sal says nine out of ten customers feel better after taking his elixir. Is this good evidence that the elixir works?

**Expected Answer:** **Regression to the mean** — People seek remedies when symptoms are at their peak (an extreme observation). After peak symptoms, the natural tendency is to return to baseline health — this is regression to the mean. Sal attributes the improvement to his elixir, but the improvement would likely have occurred regardless. The nine *Colds typically last a few days and resolve on their own. People buy remedies when they feel worst, which is exactly when improvement is most likely regardless of treatment. To show the elixir actuall*

**Model Response:**
> **1. The reasoning pattern being displayed**  
The peddler’s argument is a classic mixture of *anecdotal (testimonial) evidence* and a *hasty‑generalisation* based on a *biased sample*. He lets one vivid personal story (Farmer Gerd) stand in for scientific proof and then backs it up with a vague “9‑out‑of‑10” success rate that is never substantiated.

**2. Name of the fallacy / bias**  

| Formal name | Common label | Why it fits |
|-------------|--------------|-------------|
| **Anecdotal (testimonial) fallacy** | “Appeal to personal experience” | Uses Gerd’s story as proof of efficacy. |
| **Hasty generalisation** (a subtype of the above) | “Small‑sample” or “unrepresentative‑sample” fallacy | Extrapolates from a handful of happy customers to “all users”. |
| **Sampling‑bias / selection 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that the improvement could be due to the 'natural disease course' and explicitly lists 'regression to the mean' as a potential explanatory factor in section 3. They also correctly explain the flaw in using testimonials and the lack of a control group. However, the re

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Rurik says the dice are 'owed' a high roll after six lows. What is wrong with his reasoning?

**Expected Answer:** **Gambler's fallacy** — The mistaken belief that if a random event has occurred more frequently than expected, it is less likely to occur next. Each independent trial has the same probability regardless of previous outcomes. *Independent random events have no memory. The probability of a high roll on the 7th throw is exactly the same as on the 1st. Rurik confuses the law of large numbers (long-run convergence) with a suppo*

**Model Response:**
> **1‑2.  The pattern**

| Common name | Formal name (psychology / decision theory) |
|-------------|--------------------------------------------|
| **Gambler’s fallacy** (also called the *Monte‑Carlo* or *law‑of‑large‑numbers* fallacy) | *Mis‑application of the law of large numbers*; a *representativeness* bias; a *belief in “negative recency”* or “due‑ness”. |

Rurik is convinced that because six low rolls have just occurred, the next roll **must** be high. He treats the sequence of independent dice throws as if the overall distribution must “even out” in the short run.

---

### 3.  Why the reasoning is (usually) wrong  

| Element | What the fallacy assumes | Why it fails (mechanism) |
|---------|--------------------------|--------------------------|
| **Independence of trials** | The ou

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Gambler's fallacy' and provides a rigorous explanation of independent trials and the law of large numbers. Crucially, the response exceeds the baseline by discussing expected value, optimal betting criteria (Kelly criterion), and explicitly noting the edge case wher

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Breck says all the people of Dunmore are cheats based on his two visits. Is his conclusion justified by his evidence?

**Expected Answer:** **Hasty generalization** — Breck draws a universal conclusion ('all people of Dunmore are cheats') from a sample of two negative interactions. The sample size is far too small to support a generalization about an entire town's population. He is also ignoring the possibility of confounding factors (perhaps he visited during a  *Two encounters cannot justify a universal claim about an entire town. The sample is far too small and likely unrepresentative. Breck may also have selection bias — he remembers the negative experience*

**Model Response:**
> **1. The reasoning pattern**  
Breck is drawing a universal conclusion about every resident of Dunmore from two isolated, negative incidents that he personally experienced.

**2. Name of the pattern**  
- **Primary label:** **Hasty Generalization** (also called a *sweeping generalization* or *over‑generalization*).  
- **Related cognitive bias:** **Availability Heuristic** (the vivid, recent anecdotes are most “available” in his mind and are taken as evidence of the whole population).  

**3. Why the reasoning is faulty (or, in rare cases, useful)**  

| Element | What Breck does | Why it is a problem |
|---------|----------------|---------------------|
| **Sample size** | Uses *two* personal encounters. | Two data points are far too few to represent a whole town (≈ hundreds or thousands o

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'Hasty Generalization' and provides a sophisticated explanation of the mechanism, including sample size insufficiency, lack of representativeness, and the invalid inductive leap. Crucially, the response exceeds Level 3 by explicitly discussing confound

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Brix says seagulls are causing the decline of the fishing fleet because the two trends are correlated. Is his reasoning sound?

**Expected Answer:** **False cause / post hoc fallacy** — Brix observes that two variables are correlated over time (fishing boats declining, seagulls increasing) and infers that one causes the other. But correlation does not establish causation. There are four possibilities: (1) seagulls cause boat decline, (2) boat decline causes seagull increase, (3) a  *Correlation between two variables does not establish that one causes the other. Brix has not ruled out reverse causation, a common cause, or coincidence. Culling seagulls addresses a symptom at best a*

**Model Response:**
> **1. The reasoning pattern**  
The councilor is moving from a simple statistical co‑variation to a causal claim and a policy prescription.  In the language of informal logic and decision theory this is a **false‑cause** inference – specifically the **cum‑hoc (or post‑hoc) ergo propter hoc** fallacy ( “correlation = causation”).  It is also an instance of **causal oversimplification** (single‑cause fallacy) and of **confounding‑bias** in the underlying data.

**2. Name of the fallacy / bias**  

| Formal name | Common name |
|-------------|-------------|
| *Cum‑hoc ergo propter hoc* (or *post‑hoc ergo propter hoc*) | “Correlation‑implies‑causation” fallacy |
| Also described as *causal oversimplification* / *single‑cause fallacy* |
| In a decision‑theoretic frame: *confounding bias* / *fail

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the false cause/post hoc fallacy and explicitly states that correlation does not imply causation. They enumerate multiple alternative explanations (reverse causation, common causes like overfishing or regulation) which covers the 'four possibilities' requirement conc

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Vance seems to be complimenting Pip, but something feels off. What rhetorical technique is Vance using?

**Expected Answer:** **Evaluative language and presupposition** — Using loaded terms, diminutives, and embedded presuppositions to bias perception without explicit argument. The framing does the persuasive work while appearing neutral. *This substitutes rhetorical framing for argument. 'Even Pip managed' presupposes expected failure. 'Limited background' presupposes inferiority. None are argued for — they are smuggled in through word*

**Model Response:**
> **1. What is being demonstrated?**  
The senior member is **discounting Pip’s accomplishment on the basis of who he is**, not on what he actually did.  The comment is a classic **genetic‑type ad hominem** (sometimes called a “back‑handed compliment” or “condescending praise”).  The reasoning treats Pip’s *origin* – his limited background, junior status, and presumed lack of skill – as evidence that his success is either surprising or somehow less worthy.

**2. Name of the pattern**  
- **Genetic fallacy (ad hominem circumstantial)** – judging a claim or achievement by the characteristics of its source rather than by its intrinsic merit.  
- In everyday language it shows up as a **back‑handed compliment** or **condescension bias**.

**3. Why the reasoning is (usually) bad**  

| Step | Mech

**Score:** 2/4 ██░░
**Judge Reasoning:** The student identifies the condescending tone and points to specific dismissive elements (origin, junior status, 'little adventure'), which aligns with Level 2. However, the response misidentifies the core pattern as a 'genetic fallacy/ad hominem' rather than the required 'evaluative language and pr

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Question:** Can you identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work?

**Expected Answer:** **Assuring, guarding, and discounting** — Three rhetorical moves managing acceptance: assuring ('everyone knows') discourages questioning, guarding ('most scholars') hedges while sounding authoritative, discounting ('granted X, but Y') acknowledges then dismisses objections. *When used to replace evidence: 'everyone knows' is social pressure, not evidence. 'Most scholars' is presented without citation. 'Granted but' acknowledges without genuinely weighing.*

**Model Response:**
> **1‑2.  The pattern being displayed**  
The advisor’s argument is a classic **false‑dilemma (false‑either/or) combined with an appeal to fear (ad baculum) and an “appeal to consequences” (argumentum ad consequentiam).**  
In everyday talk it is often summarized as **“the ends justify the means”** or **“no reasonable person could object because the alternative is disaster.”**  

---

### 3.  Why the reasoning is faulty (or, when it can be sound)

| Component | What it does | Why it is a fallacy / bias |
|-----------|--------------|---------------------------|
| **False‑dilemma** | Presents only two options: *raise taxes* **or** *let the kingdom be destroyed*. | Reality is rarely binary. Other possibilities (e.g., borrowing, re‑allocating existing funds, diplomatic solutions, a cheaper fort,

**Score:** 1/4 █░░░
**Judge Reasoning:** The student fails to identify the specific rhetorical pattern required (assuring, guarding, discounting) and instead analyzes the text using unrelated logical fallacies (false dilemma, ad baculum). While the student demonstrates strong critical thinking skills by identifying that the argument is pus

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Torin says that because Amanda argued badly, the herb must NOT have healing properties. What is wrong with Torin's reasoning?

**Expected Answer:** **The fallacy fallacy** — Assuming that because an argument for a conclusion contains a fallacy, the conclusion itself must be false. A bad argument for X does not prove not-X. *A fallacy means the argument fails to establish its conclusion — it does NOT mean the conclusion is wrong. The herb's properties are empirical, independent of any particular argument about them.*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The exchange contains **two distinct moves**:

| Move in the dialogue | Formal name |
|----------------------|-------------|
| “Silvervein must be medicinal because my grandmother used it.” | **Appeal to tradition / appeal to authority (ad antiquitatem)** – the claim is justified solely by historical or ancestral usage. |
| “That’s a textbook appeal to tradition, therefore the conclusion (Silvervein has no healing power) must be true.” | **Argument from fallacy** (also called the **“fallacy‑fallacy”** or **argumentum ad logicam**). |

The prompt asks you to focus on the *second* move – the mistaken inference that because the *argument* is fallacious, the *conclusion* must be false.

---

**2. Precise name**

**Argument from fallacy** (informal

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'fallacy-fallacy' (Argument from Fallacy), clearly distinguishes between the validity of an argument and the truth of its conclusion, and correctly identifies that the conclusion requires empirical testing (phytochemical analysis, clinical trials) rather than logical

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The innkeeper's daughter has laid out the situation. Identify the acts, the states, and the outcomes. Then check: does either act dominate the other with these values?

**Expected Answer:** **Decision matrix construction** — A decision matrix organizes a choice into rows (acts the agent controls), columns (states of the world the agent does not control), and cells (outcomes with assigned values). This is the foundational representation for all of decision theory. *The matrix separates what you control (take or leave the umbrella) from what you do not control (the weather). With these ordinal values, neither act dominates the other: Take Umbrella is better if it*

**Model Response:**
> **1. The reasoning that is being shown**  
The passage is a textbook illustration of **decision‑making under uncertainty** – the player is asked to choose an *act* (buy or not buy the umbrella) before the *state of nature* (rain or no‑rain) is known.  The way the options are laid out is exactly the kind of *pay‑off matrix* used in elementary **decision‑theoretic analysis**.  

The specific pattern that the narrator is leaning on is the **maximin (or Wald) criterion** – “pick the act whose worst‑case outcome is the best”.  The story emphasizes the *worst* possible result (“wet and miserable”) and treats the other outcomes as secondary.  This is not a logical fallacy; it is a legitimate decision rule when the decision‑maker has **no reliable probabilities** for the states of nature and is ex

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the context of decision-making under uncertainty and distinguishes between acts and states. However, they fail to construct the decision matrix or assign outcomes to cells as required by the rubric. Furthermore, they misidentify the core pattern as 'Maximin' rather t

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The merchant has set up a matrix. Dominance reasoning gives no clear answer. But is there a deeper problem with how the matrix is constructed? What assumption does dominance reasoning require about the relationship between acts and states?

**Expected Answer:** **Dominance reasoning and state-act independence** — Dominance reasoning says: if one act yields a better outcome in every possible state, choose it. But this only works when states are independent of acts. In the extortion case, whether the cart is damaged depends on whether you pay — the states are not independent of the acts, which violates the str *Dominance reasoning requires that the states of the world are independent of your acts. Here, 'Cart Damaged' is not an independent state — it is caused by your refusal to pay. The correct matrix shoul*

**Model Response:**
> **1. What is going on?**  
The player is **confusing “states of the world” with “outcomes of the action.”**  
In a proper decision‑theoretic model the world can be in a *state* (e.g., “the thug is violent”, “the thug is honest”, “the thug is scared”) **independent of the decision**.  
An *outcome* is then the result of **both** the

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core structural error: confusing states of the world with outcomes of the action, and notes that states must be independent of the decision. This aligns with Level 2 (noting the dockworker/thug controls the outcome based on the choice). However, the response is i

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The prospector wants the biggest possible payoff and does not care about the downside. Apply the maximax rule: for each expedition, find its best outcome, then pick the expedition with the highest best outcome.

**Expected Answer:** **Maximax** — Maximax identifies the best possible outcome for each act, then selects the act with the highest best-case outcome. It is the optimist's rule: chase the ceiling, ignore the floor. *The best outcome for River Panning is 8, for Hilltop Digging is 12, and for Cave Exploring is 6. Maximax selects the highest of these maxima: 12, corresponding to Hilltop Digging. The prospector shoul*

**Model Response:**
> **1. The reasoning pattern being shown**  
The prospector is applying the **maximax decision rule** (sometimes called the “optimist’s criterion”).  In everyday language it is an expression of **optimism bias / risk‑seeking**: “pick the option whose *best possible* outcome is the largest, and ignore everything else.”

**2. Name of the pattern**  
- **Maximax (optimistic) criterion** – a formal decision‑theoretic rule.  
- In psychology it is also described as **optimism bias** or **risk‑loving (convex) utility**.

**3. Why it works (or fails) – the mechanism**  

| Feature | What the rule does | Why it can be problematic |
|---------|-------------------|---------------------------|
| **Focus** | Looks only at the *maximum* payoff each action can yield (8, 12, 6). | Discards the *distributio

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Maximax pattern and the specific choice (Hilltop Digging with a best case of 12). They explicitly explain the risk-seeking nature of the rule, clearly articulate that it ignores worst-case outcomes and probability distributions, and provide a robust contrast with

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The scholar wants to avoid the worst possible evening. Apply maximin: for each act, find its worst outcome, then pick the act whose worst outcome is highest.

**Expected Answer:** **Maximin** — Maximin identifies the worst possible outcome for each act, then selects the act whose worst case is least bad. It is the pessimist's rule: raise the floor, ignore the ceiling. *The worst outcome for Watch Football is 1 (team loses, evening wasted). The worst outcome for Work on Paper is 2 (team wins, slight regret). Maximin selects the act with the higher minimum: Work on Pa*

**Model Response:**
> **1. What is being demonstrated?**  
The scholar is using a *worst‑case‑oriented* decision rule: he refuses to accept any plan that could leave him with the “worst” possible payoff (the night‑mare outcome of watching the match and losing).  In decision‑theoretic language this is the **maximin (or minimax) criterion** – sometimes described as the “cautious” or “pessimistic” approach.

---

**2. Name of the pattern**  

- **Maximin (Wald’s maximin) decision rule**  
- In game‑theoretic language: **minimax** (choose the action whose *minimum* payoff is *maximal*).  

It is **not a logical fallacy**; it is a legitimate decision‑theoretic concept, though it can be a *bias* when applied inappropriately (see §5).

---

**3. How it works – why it can be good or bad**

| Action | Payoffs (win / los

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Maximin, accurately calculates the minima for both acts (Watch=1, Work=2), and selects the correct action (Work on Paper). They clearly explain the mechanism of raising the floor and the pessimistic logic. However, the response falls short of Level 4 b

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Given the profit table, apply Minimax Regret to determine which cargo to load. Show your regret matrix and explain your answer.

**Expected Answer:** **Minimax regret** — Step 1: Build the regret matrix. Column maxima: Mining Camp=18, Fishing Village=16, Fortress=14.

Regret matrix:
              Mining Camp    Fishing Village    Fortress
Furs           0               12              11
Salted Fish   12                0               9
Iron Tools     8               *Minimax regret minimizes worst-case hindsight disappointment. Iron Tools never leaves you more than 8 utils away from the best you could have done, regardless of which settlement is buying. Furs and S*

**Model Response:**
> **1. The reasoning pattern being illustrated**  
The merchant is applying a *decision‑theoretic rule* that chooses an action by looking at the worst‑case “missed‑opportunity” it could suffer.  In the jargon of decision theory this is the **Minimax Regret (or Minimax Loss) criterion** (sometimes called Savage’s minimax‑regret rule).

---

**2. Name of the concept**  
**Minimax Regret (Minimax Opportunity‑Loss) decision rule.**  

---

**3. How it works – why it can be good or bad**

| State (which settlement buys) | Best profit in that state | Regret of each cargo (Best – profit) |
|------------------------------|---------------------------|--------------------------------------|
| Mining Camp                  | 18 (Furs)                 | Furs 0, Salted Fish 12, Iron Tools 8 |
| Fishing Vi

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified the Minimax Regret pattern, accurately constructed the regret matrix with all correct values (matching the key explanation), calculated the maximum regret for each act (12, 12, 8), and selected the correct option (Iron Tools). Furthermore, the student clearly articul

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The scholar says education might not increase productivity at all — it just signals pre-existing ability. Under what conditions does this signaling work? What is the key property that makes the signal credible?

**Expected Answer:** **Signaling (Spence's job market model)** — In a signaling game, an informed player (Sender) takes a costly action to reveal private information to an uninformed player (Receiver). Separation requires the Single Crossing Condition: the signal must be more costly for low types than high types. In Spence's model, education is the signal, abilit *Signaling theory explains why costly, seemingly wasteful behaviors persist: they provide information that enables better matching. The peacock's tail, college degrees, expensive advertising, and elabo*

**Model Response:**
> We need to identify the reasoning pattern in the scholar's explanation. The scenario: Two types of workers, high ability and low ability. Education costs differ: c_H=1 per unit, c_L=3 per unit. The scholar says for separation, need e such that high types want education (100 - e > 40 => e < 60) and low types do not want education (100 - 3e < 40 => e > 20). So any e between 20 and 60 works. This is a classic mistake: they treat the payoff as 100 - e for high types, but actually the payoff is wage minus cost. The wage for high types is 100 if identified, but if they get education they get wage 100? Actually in Spence model, employers infer ability from education and pay accordingly. The condition for high types to prefer education is that wage for high type (100) minus cost (c_H * e) > wage f

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly derives the mathematical conditions for separation (100-e>40 and 100-3e<40), calculates the valid range (20<e<60), and explicitly identifies the 'Single Crossing Condition' as the underlying concept. They demonstrate a strong grasp of the mechanism. The score is 3 rather than 4

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Question:** Standard theory says Responders should accept any positive offer. They do not. Why? And how do formal models of social preferences (like Fehr-Schmidt) explain both Responder rejections and Proposer fairness?

**Expected Answer:** **Behavioral game theory** — Behavioral game theory studies how real humans deviate from Nash equilibrium predictions. Key findings: (1) Ultimatum Game: people reject unfair offers at personal cost and anticipate this by making fair offers. (2) Level-k reasoning: people think a few steps ahead, not infinitely. (3) Social prefer *Standard backward induction assumes purely self-interested agents. Real humans have social preferences — they care about relative payoffs, fairness, and reciprocity. These preferences are not irration*

**Model Response:**
> **1. What is being demonstrated?**  
The instructor (and the textbook she is teaching from) is applying **backward‑induction reasoning under the “pure‑self‑interest” assumption** – i.e. the standard homo‑economicus model that a player’s utility depends **only** on his own monetary payoff.  In behavioural‑economics language this is a **self‑interest bias / fairness‑blindness fallacy** (sometimes called the *“rational actor”* or *“self‑interest only”* assumption).

---

**2. Name of the pattern**

- **Formal label:** *Self‑interest‑only backward induction* (or *homo‑economicus backward induction*).  
- **Common‑language label:** *The “rational self‑interest” fallacy* or *the “fairness‑blindness bias”.*  

Both point to the same mistake: treating the game as if the only relevant payoff is the

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism of Behavioral Game Theory by explicitly defining the Fehr-Schmidt utility function with alpha and beta parameters and explaining how disadvantageous inequality aversion leads to rejection. They also correctly note that proposers anticipate this beh

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Without commitment, the Incumbent gets 2. With commitment, the Incumbent gets 3. How can removing an option make you better off? Explain the mechanism and give another example of a commitment device.

**Expected Answer:** **Commitment** — Commitment devices improve outcomes in strategic settings by making threats or promises credible. The Paradox of Commitment: having fewer options can be advantageous because it changes the opponent's best response. Types include contracts, reputation, precommitment, burning bridges, delegation, and  *Commitment is one of the most practically important concepts in game theory. It explains why binding yourself can be strategic: constitutions that are hard to amend, independent central banks, Odysseu*

**Model Response:**
> **1. What is going on?**  
The instructor is illustrating a *strategic‑commitment* move.  By voluntarily restricting her own future actions (signing a contract that makes “Accommodate’’ costly), the incumbent changes the entrant’s beliefs about what will happen after entry, turns a non‑credible threat into a credible one, and thereby improves her own equilibrium payoff.  In the language of decision theory it is a **pre‑commitment / self‑binding** device that creates a *dominant* strategy for the opponent (stay out) and a *better* equilibrium for the player who commits.

**2. Name of the pattern**  

- **Pre‑commitment (or commitment device, self‑binding).**  
- In the game‑theoretic literature it is also called a **credible‑threat commitment** or **strategic commitment**.  
- The “paradox’

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Commitment/Pre-commitment) and provides a sophisticated explanation of the mechanism, specifically how restricting options changes the opponent's best response via credible threats. They also successfully provide additional context and examples of how it

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The instructor lists four conditions for reputation to sustain cooperation. What are they? If any one fails, how does cooperation break down? Give a real-world example of a reputation system and explain which conditions it satisfies.

**Expected Answer:** **Reputation and the shadow of the future** — Reputation is what others believe about your type or strategy based on past actions. In repeated games, reputation creates incentives for cooperation: defecting today earns a short-term gain but destroys future cooperation opportunities. The Folk Theorem shows that in infinitely repeated games (or g *Reputation is the informal counterpart of formal commitment. Where contracts bind through law, reputation binds through expectations. Online rating systems (eBay, Uber), professional networks, and com*

**Model Response:**
> **1. What is being demonstrated?**  
The instructor is **mistaking a *sufficient‑condition* result for a *necessary‑and‑sufficient* prediction of behaviour**. In logical terms this is the **“converse error” (or “reverse‑implication fallacy”)** – the move from “if the four conditions hold then a cooperative equilibrium *exists*” to “if the four conditions hold then the players *will* cooperate”.

**2. Name of the pattern**  
- **Converse error / reverse‑implication fallacy**  
- In game‑theoretic jargon it is often called the **“Folk‑Theorem inevitability bias”** or **“equilibrium‑existence‑implies‑equilibrium‑selection” fallacy**.

**3. Why the reasoning is (sometimes) wrong**  

| Step in the instructor’s chain | Logical form | Why it can be misleading |
|-------------------------------|-

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the prompt's topic. The question required an explanation of how 'Reputation' sustains cooperation in repeated games (referencing the Folk Theorem, discount factors, and specific conditions). Instead, the student provided a logical critique of a hypothetical i

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Bob risks 2 gold to win 1 gold, with a total stake of 3 gold. If this bet is fair in Bob's eyes, what is his credence — his subjective probability — that the storm will come? Show the calculation.

**Expected Answer:** **Fair betting rate as credence** — A fair betting rate quantifies subjective probability. If an agent considers a bet fair (expected value zero), their credence in the proposition equals their potential loss divided by the total stake. Bob risks 2 gold on a 3 gold total stake, so his credence in the storm is 2/3. *Bob's willingness to risk 2 gold to win 1 gold on a total stake of 3 gold implies he considers the bet fair at a probability of 2/3. The formula is Pr(S) = Potential Loss / Total Stake = 2/3. If his t*

**Model Response:**
> **1. What is being demonstrated?**  
The tavern‑keeper is **inferring a subjective probability from the odds a person is willing to accept**.  Implicitly he treats the bet as “fair” in the sense of *expected monetary value* and assumes that the bettor’s utility for money is linear.  In the jargon of decision theory this is the **“risk‑neutral inference of credence from odds”** (or, put another way, the **“expected‑value‑only”** reasoning).

**2. Name of the pattern / fallacy**  

| Common name | Formal term (decision‑theoretic) |
|-------------|-----------------------------------|
| *Assuming risk‑neutrality* | *Linear‑utility inference of probability from odds* |
| *Bet‑odds = probability* fallacy | *Ignoring curvature of the utility function* |

It is sometimes called the **“fair‑bet fal

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the underlying mechanism (inferring probability from fair betting odds) and accurately calculates the result (2/3) using the expected value formula. They explicitly mention the 'fair bet' condition and expected monetary value. However, they do not reach Level 4 becau

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The bookie's implied probabilities sum to 1.05. Explain why this guarantees the bookie a profit regardless of which horse wins. Then answer: if a gambler's personal credences summed to more than 1, how could someone exploit them?

**Expected Answer:** **Dutch Book argument** — A Dutch Book is a set of bets that guarantees a net loss for the agent regardless of the outcome. The Dutch Book theorem proves that if an agent's credences violate the axioms of probability (e.g., sum to more or less than 1 for an exhaustive partition), there exists a set of bets the agent consider *Mercer collects $210 in bets (each bettor pays at odds that imply the listed probabilities). No matter which horse wins, the payout is $200. Mercer pockets $10 guaranteed. From the gambler's side: if *

**Model Response:**
> **1.  The pattern that is being displayed**

The professor is using a **Dutch‑book / coherence argument** – the idea that “if your personal probabilities (or odds you accept) do not obey the axioms of probability, then a clever opponent can lay a set of bets that will make you lose money whatever happens.”  
In everyday language it is often presented as a *fallacy* that “any odds that add up to more than 1 guarantee a profit for the bookie.”  

**2.  Name of the pattern**

- **Dutch‑book argument** (also called *Dutch‑bookability* or *probabilistic incoherence*).  
- When it is invoked incorrectly, it is sometimes called the **“overround‑as‑arbitrage fallacy.”**  

**3.  Why the reasoning is (sometimes) good and (sometimes) bad**

| What the professor says | Why it *sounds* right | Why it 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Dutch Book argument and accurately explains the mechanism of guaranteed loss for an agent with incoherent credences (violating probability axioms). They distinguish well between the bookie's margin in real-world betting and the theoretical certainty of the Dutch 

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Nell says something doesn't add up. She's right. Look at the implied probabilities on Oliver's board. What mathematical rule do they violate, and what does that mean for anyone betting at these odds?

**Expected Answer:** **Axioms of probability** — The three axioms of probability require: (1) Non-negativity: all probabilities >= 0; (2) Normality: probabilities over the entire sample space sum to exactly 1; (3) Finite Additivity: for mutually exclusive events, P(A or B) = P(A) + P(B). Oliver's odds violate Axiom 2 because the implied probabilit *When probabilities violate Axiom 2 (normality), a Dutch Book becomes possible. Oliver collects $210 in bets but only pays out $200 regardless of winner. The gambler who accepts these odds as fair is g*

**Model Response:**
> **1. What is being demonstrated?**  
The scene is a classic illustration of **“the over‑round (or vigorish) fallacy”** – the mistaken belief that a set of quoted odds must sum to exactly 1 (i.e., that the implied probabilities are the true, “fair” probabilities).  In decision‑theoretic language the odds are **incoherent**: they allow a *Dutch‑book* against anyone who treats them as fair.

---

**2. Name of the pattern**

| Discipline | Common name |
|------------|-------------|
| Betting / gambling | **Over‑round / Vig / Bookmaker’s margin** |
| Probability theory | **Incoherent probability assessment** |
| Decision theory | **Dutch‑bookable odds** |
| Cognitive bias literature | **“Fair‑odds illusion”** (thinking the odds are fair because they look like ordinary odds) |

---

**3. Why the

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core issue: the implied probabilities sum to 1.05, violating the normality axiom (sum must equal 1), and explicitly links this to the creation of a guaranteed profit (Dutch book) for the bookie. This meets all criteria for Level 3. However, the response does not 

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss and Lira are both using the word 'probability' but seem to mean different things. Are they contradicting each other, or could both be right? What exactly is the difference between what they are describing?

**Expected Answer:** **Subjective vs objective probability** — Objective probability (chance) refers to mind-independent features of the world — physical propensities, frequencies, quantum indeterminacies. Subjective probability (credence) refers to an agent's degree of confidence in a proposition, revealed through betting behavior. Both satisfy the same axioms *Both scholars are correct within their domains. Probability is genuinely ambiguous between chance (a physical property) and credence (a psychological state). The mathematical formalism — the three axi*

**Model Response:**
> **1. What is being demonstrated?**  
A classic **equivocation (semantic ambiguity) fallacy** – the two scholars are using the same word *probability* but are attaching **different, mutually exclusive definitions** to it (objective‑propensity vs. subjective‑degree‑of‑belief). The dispute is therefore not about the facts of the comet or the trial, but about *what* “probability” means.

---

**2. Name of the pattern**  

- **Equivocation (or “ambiguity” fallacy)** – sometimes called a *category‑mistake* when a term is applied to a category it does not belong to.  
- In the language of decision theory it is also described as a **“mis‑specification of the probability interpretation.”**

---

**3. Why the reasoning is (in)valid**  

| Step in the dialogue | Implicit move | Why it is a problem |


**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between objective chance (propensity/frequency) and subjective credence (degree of belief), correctly identifying that both are legitimate interpretations depending on context. They explicitly note that the conflict arises from equivocation rather than factual disag

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms?

**Expected Answer:** **Principal Principle** — The Principal Principle (Lewis/Weatherson) states: if you know the objective chance of an event is x, your rational credence should be x, provided you have no inadmissible evidence (e.g., time travel, crystal balls). Formally: Pr(p | Ch(p)=x) = x. Cade knows Ch(Heads)=0.80 but sets Cr(Heads)=0.50, v *Cade's credences are internally consistent (they satisfy the axioms) but externally miscalibrated. The Principal Principle provides the missing norm: when objective chances are known, rational credenc*

**Model Response:**
> **1. What is being demonstrated?**  
Cade is **ignoring the known base‑rate (the 80 % heads bias) and substituting a personal “gut feeling” for the objective statistical evidence**. In the language of decision theory and cognitive psychology this is called **base‑rate neglect (or the base‑rate fallacy)**, often coupled with the **illusion of control** – the belief that one’s own experience or skill can override a known random process.

---

**2. Name of the pattern**

- **Base‑rate neglect** (sometimes listed as “base‑rate fallacy”).  
- When the neglect is motivated by a sense that one’s own expertise matters, it is also described as the **illusion of control**.

Both labels point to the same underlying error: treating the *subjective* feeling as if it were an *objective* probability whil

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cade is ignoring objective evidence in favor of subjective intuition and explicitly notes that coherence (avoiding a Dutch Book) is insufficient for rationality, which aligns with Level 2. However, the student misidentifies the specific philosophical pattern as 

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Calculate the expected utility of each option using the formula EU(Act) = sum of P(State) * U(Act|State). Which option should the healer choose, and why does it differ from what dominance reasoning would say?

**Expected Answer:** **Maximize Expected Utility (MEU)** — MEU weighs each outcome by its probability and sums to get the expected utility of each act. The agent selects the act with the highest expected utility. EU(Act) = P(S1)*U(Act|S1) + P(S2)*U(Act|S2) + ... *EU(Use Cream) = -35 and EU(Do Nothing) = -50. Since -35 > -50 (losing 35 silver is better than losing 50), the healer should use the cream. Notably, dominance reasoning would recommend Do Nothing (it *

**Model Response:**
> **1. What is being demonstrated?**  
The healer is (or appears to be) applying the **expected‑utility decision rule** – i.e. the *expected‑value* (or *expected‑cost*) calculation that is the cornerstone of **classical decision theory**.  

In everyday language it is often called “doing the math” or “cost‑benefit analysis”, but in the jargon of decision theory it is the **expected‑utility (EU) calculation** (sometimes phrased as “expected monetary value” when the utility function is taken to be linear in money).

---

**2. Name of the pattern / concept**  

- **Expected‑Utility Theory** (EUT) – the normative model for rational choice under risk.  
- When the utility function is taken to be the identity (U = money), the calculation is simply **Expected Monetary Value (EMV)**.  

If the heale

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the general concept (Expected Utility Theory) and explains the mechanism of weighting outcomes by probability. However, the response fails to apply the MEU formula to the specific scenario provided, makes no calculations (missing the required values of -35 and -50), 

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Captain Aldric's scout gave rankings but not numbers. Why is that not enough for a good decision here? What additional information would you need, and how would it change the analysis?

**Expected Answer:** **Cardinal vs ordinal utility** — Ordinal utility provides only a ranking: A > B > C. Cardinal utility assigns numerical values that capture how much better A is than B. Decision rules like Maximin and Maximax use ordinal utility and are therefore blind to magnitude. MEU requires cardinal utility because it multiplies utility by pro *With ordinal utility, the ranking is Hilltop > Bridge > Ravine in both states, so all rules agree on Hilltop. But the magnitude matters: Hilltop's advantage over Bridge in the North scenario (20 vs 12*

**Model Response:**
> **1. What is being demonstrated?**  
The captain is applying the **maximin (or minimax‑worst‑case) rule on a *purely ordinal* ranking** and then treating the three “worst‑case” ranks as if they were *equally bad*. In other words, he is **ignoring the intensity (cardinality) of the differences between the outcomes** and assuming that “rank 2 is just a little worse than rank 1, rank 3 is just a little worse than rank 2”, even though the scout’s description makes it clear that the gaps are wildly unequal (catastrophic vs. merely uncomfortable).

**2. Name of the pattern / fallacy**  

- **Ordinal‑maximin fallacy** (sometimes called *preference‑intensity neglect* or the *cardinality error*).  
- In the decision‑theory literature it is also described as **“using a maximin criterion with only or

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between ordinal rankings and cardinal utility, correctly identifying that the captain's error lies in treating unequal gaps between ranks as equal (ignoring intensity). They accurately explain that Maximin on ordinal data fails to capture the magnitude of catastroph

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Kael calls Sera irrational because she turns down a bet with higher expected monetary value. Is he right? Or is there a way to explain Sera's preference that is perfectly consistent with maximizing expected utility?

**Expected Answer:** **Risk aversion and utility curves** — Under MEU, risk attitude is encoded in the shape of the utility function. A linear utility function (U = wealth) produces risk neutrality. A concave function (e.g., U = sqrt(wealth)) produces risk aversion: the utility of the expected value exceeds the expected utility of the gamble. Sera's declinin *Sera is not irrational. Her utility function is concave (diminishing marginal utility), so she values certainty more than a gamble with the same expected monetary value. With U=sqrt(x): EU(Stay)=20.0 *

**Model Response:**
> **1. What is being demonstrated?**  
Sera is displaying **risk‑averse decision making** (the opposite of the “expected‑value‑only” reasoning Kael uses). In formal terms she is applying a **concave utility function** – i.e. **diminishing marginal utility of money** – and/or the **certainty effect** from Prospect Theory.

**2. Name of the pattern**  

- **Risk aversion** (concave utility).  
- Relatedly, the **certainty effect** (over‑weighting of a sure outcome).  

Both are standard concepts in decision theory; the “fallacy” on Kael’s side is the **expected‑value fallacy** (treating utility as linear in money).

**3. Why is the reasoning good or bad?**  

| Reasoning | Mechanism | When it is “good” | When it is “bad” |
|-----------|-----------|-------------------|-----------------|
| **Kae

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies risk aversion and the concave utility function as the core mechanism. They explicitly explain diminishing marginal utility, provide a specific functional example (sqrt), set up the expected utility comparison showing why the certain option is preferred, and clearly a

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** John keeps cycling through ice cream trades and losing money. What structural property of his preferences allows the vendor to exploit him? What would John need to change about his preferences to stop the bleeding?

**Expected Answer:** **Transitivity and money pumps** — Transitivity requires: if A > B and B > C, then A > C. John's preferences violate transitivity (S > C, C > V, but V > S). The money pump shows that intransitive preferences are exploitable: an agent can be led through a cycle of individually rational trades that return them to the starting point min *Each individual trade is rational by John's own lights — he always trades for something he prefers. But the cycle as a whole is irrational: he ends up with the same item and less money. The money pump*

**Model Response:**
> **1. What is being demonstrated?**  
The vendor is exploiting **in‑transitive (circular) preferences** to run a **“money‑pump”** on John. In decision‑theoretic language the story is a classic illustration of the *money‑pump argument*: if an agent’s strict preferences fail the axiom of **transitivity**, a clever opponent can offer a sequence of trades that leaves the agent exactly where he started but poorer each time.

---

**2. Name of the pattern**

| Discipline | Term |
|------------|------|
| Decision theory / economics | **Money‑pump (or money‑pump paradox)** |
| Logic / philosophy of rationality | **In‑transitive (circular) preference** |
| Informal reasoning | **Fallacy of assuming rationality without transitivity** |

The most precise label for the whole situation is **the money‑pu

**Score:** 4/4 ████
**Judge Reasoning:** The student perfectly identifies the pattern as a 'money-pump' driven by 'intransitive preferences.' They explicitly detail the mechanism (S > C > V > S), explain how locally rational trades lead to global irrationality and guaranteed loss, and note the repeatability leading to bankruptcy. The respo

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin asks how removing an option nobody chose can change the recommendation. What principle is being violated here, and why does MEU avoid this problem?

**Expected Answer:** **Independence of Irrelevant Alternatives (IIA)** — IIA states: if option C is chosen from set S, then C should still be chosen from any subset of S containing C. Minimax Regret violates IIA because regret is calculated relative to the best available option in each state. When the menu changes, the reference point changes, which can reverse preferenc *MEU satisfies IIA because each option's expected utility depends only on its own payoffs and the state probabilities, not on what other options are available. Minimax Regret violates IIA because regre*

**Model Response:**
> **1. What is being shown?**  
The elder’s objection is to the fact that eliminating an *irrelevant* alternative (the Picnic, which was never chosen) flips the ranking of the two remaining alternatives.  In formal terms this is a **violation of the Independence‑of‑Irrelevant‑Alternatives (IIA)** axiom.  In the language of decision‑theoretic fallacies it is often called the **“irrelevant‑alternative” paradox** or **“choice‑alteration” effect**.

---

**2. Name of the pattern**

- **Independence of Irrelevant Alternatives (IIA) violation**  
- In the literature on regret‑based choice it is sometimes referred to as the **“Regret‑Induced Preference Reversal”** or **“Irrelevant‑Alternative Effect”**.

---

**3. Why it happens – the mechanism**

| Step | What the Minimax‑Regret rule does | Why th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a violation of Independence of Irrelevant Alternatives (IIA) and provides an excellent, step-by-step explanation of the mechanism (how the changing reference point/benchmark in Minimax Regret causes the reversal). They also correctly contrast this with

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Father Clement's argument seems airtight — infinity times anything positive is infinity. But Dara is not convinced. What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?

**Expected Answer:** **Pascal's Wager** — Pascal's Wager applies MEU with infinite utility. When any outcome has infinite value, the expected utility calculation is dominated by that outcome regardless of its probability (as long as P > 0). This 'washing out' effect makes MEU insensitive to evidence — a feature that many consider a reductio *The Wager has several structural problems: (1) The many-gods objection: multiple incompatible religions offer infinite rewards, so the argument cannot uniquely recommend one faith. (2) The washing-out*

**Model Response:**
> **1. What is being demonstrated?**  
The dialogue is a textbook illustration of **Pascal’s Wager‑type reasoning** – a decision‑theoretic move that lets an *infinite* payoff dominate the expected‑utility calculation even when the probability of that payoff is vanishingly small.  In the literature this is usually called the **“infinite‑utility” or “Pascal’s Mugging” fallacy** (a special case of the broader “Pascal’s Wager” argument).

---

**2. Name of the pattern**

- **Pascal’s Wager** (the original formulation)  
- **Infinite‑utility fallacy** (or **Pascalian expected‑utility** error)  
- Closely related: **Pascal’s Mugging** (the decision‑theoretic problem where a tiny‑probability, infinite‑reward claim forces a forced‑choice).

---

**3. Why the reasoning is (generally) bad**

| Step | 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Pascal's Wager and accurately explains the core mechanism: infinite utility dominating the expected utility calculation regardless of probability (the 'washing out' effect). They explicitly note that this makes the calculation uninformative, which alig

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** The expected value is infinite, but you would not pay a million gold to play. What has gone wrong? Is expected value the wrong tool, or are we applying it to the wrong quantity?

**Expected Answer:** **St. Petersburg Paradox** — A fair coin is flipped until heads. Payoff = 2^n where n is the number of flips. Expected value = sum from n=1 to infinity of (1/2)^n × 2^n = sum of 1 = infinity. Yet no reasonable person would pay more than about 20-30 gold. The paradox reveals that expected monetary value is not the same as expect *Expected monetary value diverges to infinity, suggesting unlimited willingness to pay. This is absurd — it would recommend mortgaging everything for a game that usually pays 2 or 4 gold.*

**Model Response:**
> **1.  The reasoning pattern**

The gambit is the classic **St. Petersburg paradox** – a decision‑theoretic “paradox” that arises when one **applies raw expected‑value (EV) arithmetic** to a gamble whose payoff grows exponentially while the probability of reaching that payoff shrinks exponentially.  
In everyday language it is an **expected‑value fallacy** (or “ignoring utility”) and, more formally, the mistake of **assuming a linear utility function (risk‑neutral preferences) while the situation demands a concave, bounded‑utility view**.

---

**2.  Name of the fallacy / concept**

- **St. Petersburg paradox** (the paradox itself)  
- **Expected‑value fallacy** (using EV as the sole decision criterion)  
- **Linear‑utility (risk‑neutral) assumption** (the hidden premise)

---

**3.  Why th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the St. Petersburg Paradox and provides a strong conceptual explanation of the resolution via diminishing marginal utility and concave utility functions. They explicitly distinguish between expected monetary value and expected utility. However, the response falls sho

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The showmaster says choosing Gamble 1 and Gamble 4 is inconsistent. Can you see why? What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

**Expected Answer:** **Allais Paradox (Certainty Effect)** — The Allais Paradox demonstrates that people overweight certainty. In Choice 1, Gamble 1 offers certainty ($1M guaranteed), which has disproportionate psychological appeal. In Choice 2, neither option is certain, so people chase the higher payoff (Gamble 4). But the 89% column (Tickets 12-100) is ide *The preference pair (G1>G2 and G4>G3) violates the Sure Thing Principle: if outcomes are identical in some states, those states should not affect the preference. Once the 89% column is masked, both ch*

**Model Response:**
> We need to identify the reasoning pattern. The scenario: two choices each with two gambles. First choice: gamble 1 is a sure 1M (since all tickets pay 1M). Gamble 2: ticket #1 pays 0, tickets #2-11 pay 5M, tickets #12-100 pay 1M. Expected values: For gamble 1: EV = 1M (since sure). For gamble 2: EV = (1/100)*0 + (10/100)*5M + (89/100)*1M = 0 + 0.1*5M + 0.89*1M = 0.5M + 0.89M = 1.39M. So gamble 2 has higher EV, but many people choose gamble 1 because of risk aversion? Actually gamble 2 includes a zero outcome (ticket #1) which is low probability but could be seen as a loss relative to sure thing. So they choose gamble 1 (sure 1M) over gamble 2 (higher EV but risk). That's consistent with risk aversion.

Second choice: gamble 3: tickets #2-11 pay 1M, others 0. EV = (10/100)*1M = 0.1M = 100k.

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the Allais Paradox and accurately explains the mechanism as the 'certainty effect' and a violation of the independence axiom (Sure Thing Principle). They successfully demonstrate how the common consequence (the 89% column) should cancel out mathematica

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss shows that you should accept the bet unconditionally but reject it in every conditional state. Is the Sure Thing Principle actually violated here? Look carefully at whether the conditioning events form a proper partition.

**Expected Answer:** **Sure Thing Principle** — STP states: if A is preferred to B conditional on E, and A is preferred to B conditional on NOT-E, then A is preferred to B unconditionally. It is the backbone of independence in MEU. The Disjunction Effect appears to violate STP but actually involves overlapping (non-exclusive) conditioning events, *STP is not violated here because 'at least one H' and 'at least one T' are NOT mutually exclusive — they overlap on {HT, TH}. The overlap contains only losing outcomes. Each conditional eliminates a w*

**Model Response:**
> **1. What is being shown?**  
The puzzle is a classic illustration of a *violation of the Sure‑Thing Principle* – the behavioural pattern that Tversky & Shafir (1992) called the **Disjunction Effect**.  In plain language it is a failure of *dynamic consistency* (or of “separability” of the decision problem) that is usually traced to an *uncertainty/ambiguity aversion* or a *loss‑aversion* bias.

---

**2. Name of the phenomenon**  

| Formal name | Common name | Origin |
|-------------|-------------|--------|
| **Disjunction Effect** | Violation of the Sure‑Thing Principle | Tversky & Shafir, *Psychological Review* 1992 |
| (sometimes described as) **Uncertainty‑aversion bias** or **status‑quo bias** in the context of the puzzle. |

---

**3. Why the reasoning is (usually) wrong**  

| Ste

**Score:** 1/4 █░░░
**Judge Reasoning:** The student explicitly identifies the scenario as a 'violation of the Sure-Thing Principle' and attributes it to behavioral biases (uncertainty/loss aversion). This aligns with Level 1, where the player sees the paradox but believes STP is genuinely violated. The student fails to reach Level 2 or hi

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Are you a one-boxer or a two-boxer? Whatever you choose, you must defend your reasoning against the strongest version of the opposing argument. What principle are you relying on, and what are you giving up?

**Expected Answer:** **Newcomb's Problem** — Newcomb's Problem pits Dominance against Expected Utility when states are correlated with acts. Causal Decision Theory (CDT) says: the Predictor's choice is fixed, so taking both dominates (you are 1,000 gold richer regardless). Evidential Decision Theory (EDT) says: one-boxing provides strong evide *There is no consensus — this is a genuine philosophical puzzle. CDT says two-boxing is rational because you cannot cause the past to change. EDT says one-boxing is rational because it manages the evid*

**Model Response:**
> **1.  What is being demonstrated?**  
The dialogue is a textbook illustration of **Newcomb’s paradox** – the clash between two decision‑theoretic prescriptions:

* **Evidential Decision Theory (EDT)** (the “one‑boxer” line of thought) – you treat your choice as evidence about a past prediction that is highly reliable.  
* **Causal Decision Theory (CDT)** (the “two‑boxer” line of thought) – you treat your choice as a causal act that cannot affect what is already in Box A, and therefore you apply the **dominance principle** (take both boxes because it strictly adds 1 000 gold no matter what).

The two‑boxer’s argument is therefore an instance of the **dominance‑principle fallacy** (or “causal‑dominance fallacy”) when the decision problem contains a strong logical/epistemic correlation betwee

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Newcomb's Problem and clearly articulates the core tension between Evidential Decision Theory (one-boxing) and Causal Decision Theory (two-boxing/dominance). They explain the mechanism of both arguments accurately. However, the response is incomplete (

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The dealer says choosing G1 and G4 is inconsistent. Can you see why? What probability would you need to assign to Black to justify G1 over G2? And what probability would you need for G4 over G3? Can both be true?

**Expected Answer:** **Ellsberg Paradox (Ambiguity Aversion)** — The Ellsberg Paradox shows that people prefer known risk (Red: exactly 1/3) over ambiguous risk (Black: unknown proportion). Preferring G1>G2 implies P(Black)<1/3. Preferring G4>G3 implies P(Black)>1/3 (because Yellow cancels out as common consequence). These two implications are contradictory — no  *The preference pattern (G1>G2, G4>G3) violates subjective expected utility because no single probability assignment to Black is consistent with both preferences. This reveals that humans distinguish b*

**Model Response:**
> **1. What is being shown?**  
The visitors are displaying the classic *ambiguity‑aversion* pattern that gives rise to the **Ellsberg paradox**.  In everyday language it is a *preference‑reversal* (or *incoherence*) that results from treating the unknown proportion of Black balls as “the worst possible” for each gamble, while still treating the same unknown proportion as “the best possible” for another gamble.  In decision‑theoretic terms they are violating the **sure‑thing principle** (or, equivalently, the **subjective‑expected‑utility (SEU) axiom of independence**) and therefore create a set of preferences that can be Dutch‑booked.

---

**2. Name of the phenomenon**

| Common name | Technical label |
|-------------|-----------------|
| *Ambiguity aversion* (Ellsberg‑type choice) | Viola

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Ellsberg Paradox and ambiguity aversion, and explicitly names the violation of the Sure-Thing Principle/SEU axioms. They begin to derive the mechanism by explaining the known vs. unknown probabilities and the maximin heuristic for the first pair (G1>G2). However,

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The expected values are the same within each pair, yet the merchants' risk preferences flip. What does this tell you about the shape of the human utility function? Can a single curve explain both patterns?

**Expected Answer:** **Reflection Effect** — The Reflection Effect shows that people are risk-averse when choosing among gains (prefer sure $500 over 50/50 shot at $1000) but risk-seeking when choosing among losses (prefer 50/50 shot at losing $1000 over sure loss of $500). Under MEU, a utility function is either consistently concave (always r *A single concave utility function predicts risk aversion everywhere. A single convex utility function predicts risk seeking everywhere. The data shows a split: concave for gains, convex for losses. No*

**Model Response:**
> **1. What is being shown?**  
The merchants are displaying a classic *framing‑effect / reflection effect* – the same gamble is judged very differently simply because the outcomes are described as **gains** in one case and **losses** in the other.  In the language of decision theory this is the hallmark of **Prospect Theory** (Kahneman & Tversky, 1979) and is often called the **gain‑loss framing bias** or **risk‑preference reversal**.

**2. Precise name**  

- **Framing effect (gain‑loss framing)**  
- More specifically, the **reflection effect** of **Prospect Theory** (concave value for gains, convex for losses).  

Both labels refer to the same phenomenon; the first is the generic cognitive‑bias term, the second is the formal decision‑theoretic description.

---

**3. Why the reasoning is

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Reflection Effect and explicitly connects it to Prospect Theory. They accurately describe the S-shaped value function (concave for gains, convex for losses) and clearly explain how this violates Expected Utility Theory's assumption of a consistent utility functio

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** You reject the bet when you know at least one is heads, and you reject when you know at least one is tails. One of these must be true. So why should you accept unconditionally? Where is the flaw in reasoning from conditionals to the unconditional?

**Expected Answer:** **Disjunction Effect** — The Disjunction Effect occurs when an agent rejects an option conditional on each member of a non-exclusive partition but should accept it unconditionally. The resolution: 'at least one H' and 'at least one T' overlap on {HT, TH} — the losing outcomes. Conditioning on either event eliminates one win *The Disjunction Principle ('if you reject in every possible state, reject unconditionally') seems compelling but is false when the conditioning events overlap. It conflates overlapping evidence with a*

**Model Response:**
> **1.  What is being demonstrated?**  
The passage is an illustration of the **“Simpson‑type reversal” (often called Simpson’s paradox) that arises when you condition on overlapping pieces of evidence and then treat those pieces as if they were a mutually‑exclusive partition**. In decision‑theoretic language it is a **violation of Savage’s “sure‑thing principle”** – the idea that if you would reject a gamble in every relevant state of the world, you must also reject it before you learn which state obtains.

---

**2.  Name of the pattern / fallacy**

| Discipline | Common name |
|------------|-------------|
| Statistics / probability | **Simpson’s paradox (or Simpson‑type reversal)** |
| Decision theory | **Violation of the sure‑thing principle** (also called the “disjunction fallacy” or “f

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a violation of the Sure-Thing Principle (STP) due to conditioning on non-exclusive (overlapping) events, which aligns with the core of the Disjunction Effect. They accurately explain the mechanism: the overlap concentrates losing outcomes ({HT, TH}) an

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Three traders received the same bonus but feel differently. Standard economic theory says Basil should be happiest (highest wealth). What is actually determining their reactions, and what does standard theory miss?

**Expected Answer:** **Reference points** — Under Prospect Theory, outcomes are evaluated as gains or losses relative to a reference point — typically the status quo, an expectation, or an aspiration level. The same objective outcome can feel like a gain or a loss depending on the reference point. Cara's 5,000 gold bonus is objectively a gain *Cara's bonus is a gain in absolute terms. Standard MEU, which evaluates total wealth, would predict satisfaction. But Prospect Theory correctly predicts dissatisfaction because value is computed from *

**Model Response:**
> **1. What is being demonstrated?**  
The three traders are not judging the *absolute* size of the bonus (or the resulting total wealth) but the *change* of the bonus relative to a personal reference point (what they expected or what they consider “normal”).  In behavioural‑economic language this is **reference‑dependence** together with **loss‑aversion** – the core ideas of *Prospect Theory*.

**2. Name of the pattern**  

| Common label | Formal name (behavioural economics) |
|--------------|--------------------------------------|
| “They’re evaluating departures from expectation” | **Reference‑dependence (prospect‑theoretic evaluation)** – often manifested as **loss aversion** (the “pain of a loss” outweighs the “pleasure of an equal gain”). |

It is not a logical *fallacy* in the strict

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'reference-dependence' as the key pattern and explains the mechanism of evaluating outcomes relative to expectations rather than absolute wealth. They accurately categorize the traders' experiences based on their specific reference points. However, the response falls

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Lira's patrons demand 40-50 gold to accept a bet that could lose them 20. Risk aversion explains some of this, but not all. What additional psychological mechanism is at work, and how does it show up in the shape of the value function?

**Expected Answer:** **Loss aversion** — Loss aversion means that losses are felt more intensely than equivalent gains. Formally, the value function is steeper below the reference point than above it: |v(-x)| > v(x) for x > 0. The empirical coefficient is approximately lambda = 2.25, meaning losing $100 hurts as much as gaining $225 feels  *Standard MEU with risk-neutral preferences predicts acceptance at G=20. Risk aversion alone might push G to 25-30. The demand of 40-50 requires loss aversion — the disproportionate weight given to los*

**Model Response:**
> **1‑5.  Analysis of the reasoning pattern**

| # | Question | Answer |
|---|----------|--------|
| **1** | *What specific reasoning pattern, fallacy, bias, or decision‑theoretic concept is being demonstrated?* | The patrons are **over‑weighting the disutility of a possible loss relative to the utility of an equally sized gain**. In the language of behavioural economics this is the classic **loss‑aversion** effect (the “pain‑of‑loss > pleasure‑of‑gain” intuition). It is the core component of **Prospect Theory** and shows up as a *risk premium* that people demand to bear a potential loss. |
| **2** | *Name it precisely.* | **Loss aversion** (often quantified by a loss‑aversion coefficient λ ≈ 2 – 2.5). When λ > 1 the subjective weight of a loss is λ times the weight of a gain of the same mon

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies loss aversion and explicitly distinguishes it from risk aversion by defining the value function parameters (alpha for diminishing sensitivity/risk aversion vs. lambda for loss aversion). They accurately cite the empirical coefficient (lambda ≈ 2.25), explain the asym

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weighting resolve the contradiction?

**Expected Answer:** **Probability weighting function** — In Prospect Theory, objective probabilities are transformed by a weighting function pi(p) before being used in calculations. Small probabilities are overweighted (pi(0.01) > 0.01), large probabilities are underweighted (pi(0.99) < 0.99), and the endpoints 0 and 1 are treated categorically. The resul *Under MEU with objective probabilities, buying lottery tickets with negative EV and buying insurance against rare events are both irrational. Probability weighting explains both as rational under dist*

**Model Response:**
> **1. What is being shown?**  
The patrons are displaying the classic *probability‑weighting bias* that underlies **Prospect Theory** (Kahneman & Tversky, 1979).  In everyday language it is called *over‑weighting of small probabilities* (and the complementary *under‑weighting of large probabilities*).  The graph Lira draws is the familiar inverse‑S weighting function \(w(p)\).

**2. Name of the bias / concept**  

- **Probability‑weighting bias** (sometimes referred to as the **inverse‑S weighting** or **non‑linear probability weighting**).  
- In the taxonomy of cognitive biases it is also listed as **“overweighting rare events”** (a sub‑type of *risk perception bias*).

**3. Why the reasoning is (often) flawed**  

| Step | Formal (MEU) view | Human weighting view | Why it can be bad |
|-

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as probability weighting and accurately explains the inverse-S shape (overweighting small probabilities, underweighting large ones). However, the response stops short of Level 4 because it does not explicitly connect this mechanism to the Certainty Effect

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** Lira says the same person can rationally buy lottery tickets and insurance. Under MEU, this is a contradiction. How do the value function and probability weighting function together produce four distinct risk profiles?

**Expected Answer:** **Fourfold Pattern of risk attitudes** — The Fourfold Pattern emerges from combining: (1) The S-shaped value function (risk-averse for gains, risk-seeking for losses) with (2) The probability weighting function (overweight small p, underweight large p). Low-probability gains: overweighting makes the prize loom large → risk seeking. Low-pro *MEU predicts a single consistent risk attitude. The Fourfold Pattern shows four different attitudes from one person, determined by the domain (gains/losses) and the probability level (low/high).*

**Model Response:**
> **1. What is being demonstrated?**  
The passage illustrates the **“four‑fold pattern of risk attitudes”** that is a hallmark of **Prospect Theory** (specifically cumulative prospect theory).  It is the systematic way in which people appear to be *risk‑seeking for low‑probability gains and high‑probability losses* while being *risk‑averse for high‑probability gains and low‑probability losses*.  In decision‑theoretic language it is a **violation of the Expected‑Utility Independence axiom** caused by **probability‑weighting bias**.

---

**2. Name (precise label)**  

- **Fourfold Pattern of Risk Attitudes** (also called the **fourfold pattern of prospect theory**).  
- It can be described as a **probability‑weighting bias** or **inverse‑S‑shaped weighting** that produces **domain‑dependent 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Fourfold Pattern and explicitly details both required mechanisms: the S-shaped value function (concave for gains, convex for losses) and the inverse-S probability weighting function. They successfully map these mechanisms to all four quadrants in a clear table wi

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** The councillors in Group A and Group B made opposite choices about the same programs. What changed between the two presentations, and why does it matter for rational decision-making?

**Expected Answer:** **Framing effects** — Framing effects occur when logically equivalent descriptions of the same situation lead to different decisions because they shift the reference point. A gains frame activates risk aversion (prefer the sure outcome). A losses frame activates risk seeking (prefer the gamble). Since the underlying opti *Rational decisions should depend on outcomes, not descriptions. Programs A and C have identical consequences, as do B and D. The preference reversal shows that the frame — not the substance — is drivi*

**Model Response:**
> **1. The reasoning pattern that is on display**  
The councillors are falling prey to the **framing effect** – the systematic tendency to make different choices when the same objective situation is described in terms of *gains* versus *losses*. In the classic “Asian disease” problem (Tversky & Kahneman, 1981) this manifests as **risk‑aversion for gains** and **risk‑seeking for losses**, a pattern that prospect theory explains with loss‑aversion and a value function that is concave for gains and convex for losses.

**2. Precise name**  
*Framing effect* (specifically the “gain‑loss framing” version of the effect). It is sometimes referred to as the **“Asian disease problem” bias** or **“risk‑preference reversal due to framing.”**

**3. Why the reasoning is (mis)guided – the mechanism**  

|

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the framing effect and explains the mechanism using reference points, value function curvature (concave/convex), and loss aversion. Crucially, they explicitly mention the violation of the 'invariance axiom,' noting that rational agents should be frame-invariant, whic

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Alec and Brin have the same amount of money and face the same bet, but they make opposite choices. What psychological mechanism explains the difference? Is Brin being rational or irrational?

**Expected Answer:** **Mental accounting** — Mental accounting (Thaler) is the tendency to treat money differently depending on which psychological 'account' it belongs to — savings, winnings, salary, found money, etc. Standard economics says money is fungible: a dollar is a dollar regardless of its source. Mental accounting violates fungibili *Money is fungible — 200 gold has the same purchasing power regardless of its source. Alec's savings and Brin's winnings are economically identical. The different treatment reflects a psychological par*

**Model Response:**
> **1. What is being demonstrated?**  
A classic *mental‑accounting / “house‑money”* bias – the tendency to treat money that has just been won (or otherwise labelled a “windfall”) as qualitatively different from money that is “saved” or “earned”.  In the language of decision theory it is a **reference‑dependence / framing effect** (prospect‑theory) that makes the two identical wealth states generate different risk attitudes.

**2. Name of the bias / concept**  

| Common name | Formal/technical name |
|-------------|-----------------------|
| **House‑money effect** (also called the *break‑even effect*) | **Mental‑accounting / reference‑dependence** (Prospect Theory) |
| (Sometimes called *money‑illusion* when the nominal amount is taken as the only cue) | – |

**3. Why the reasoning is (usua

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies mental accounting and the house money effect, explicitly explains the violation of fungibility (money being interchangeable regardless of source), and contrasts the behavior with normative economic theory (expected utility). However, the response does not reach Level

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Sellers demand 7 gold and buyers offer 3 gold for the same mug. The mugs were randomly assigned. What psychological mechanism creates this gap, and why does standard economic theory have trouble explaining it?

**Expected Answer:** **Endowment effect** — The endowment effect is the observation that people demand more to give up an object they own than they would pay to acquire the same object. Sellers set a higher price (WTA: willingness to accept) than buyers (WTP: willingness to pay), even for identical items. The mechanism is loss aversion: once  *Rational markets require a single market-clearing price. The endowment effect creates a gap between WTA and WTP that prevents efficient trade. The mug has one objective value, but ownership distorts p*

**Model Response:**
> **1. What is being demonstrated?**  
The pattern is the classic **endowment (ownership) effect** – a systematic bias in which people value an object they own **more** than an identical object they do not own. In decision‑theoretic language it is a manifestation of **loss‑aversion** (prospect theory) and of the **status‑quo bias**.  

**2. Name**  
*Endowment Effect* (sometimes called the *ownership bias* or *status‑quo bias*).  

**3. Why it occurs – the mechanism**  

| Step | Psychological / Economic mechanism |
|------|-------------------------------------|
| **Reference point** | Once a person possesses an item, the *reference point* shifts from “no mug” to “having a mug”. |
| **Loss vs. gain weighting** | Prospect theory shows that a *loss* (giving up the mug) is weighted ≈ 2 × the ut

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Endowment Effect and explains the mechanism via loss aversion and reference points. They explicitly mention the WTA/WTP gap, cite the loss aversion coefficient (approx 2x, aligning with the rubric's lambda), and discuss the resulting market inefficiency and poten

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Darya insists on going skiing because she paid 300 gold. Her friend says the money is gone either way. Who is right, and what error is Darya making?

**Expected Answer:** **Sunk cost fallacy** — The sunk cost fallacy is the tendency to continue an activity because of past investment (time, money, effort) rather than future expected value. Under MEU, sunk costs are decision-irrelevant: only future costs and benefits should affect current choices. The fallacy arises from mental accounting — t *The 300 gold is gone regardless of the choice. Rational decision-making considers only future costs and benefits. Going skiing while sick produces less utility than the free cabin. Darya is letting a *

**Model Response:**
> **1‑5.  The pattern at work**

| # | What the dialogue shows | Technical label | Why it is a mistake (or sometimes useful) | How to decide correctly | When the “mistake” can be rational |
|---|--------------------------|-----------------|------------------------------------------|--------------------------|-----------------------------------|
| 1 | Darya clings to the fact that she *already paid* 300 gp for the ski trip and treats that as a reason **not** to change plans. | **Sunk‑cost fallacy** (also called the *Concorde fallacy* or *escalation of commitment*) | The 300 gp is a **sunk cost** – an expenditure that cannot be recovered regardless of what she does now. Rational choice theory tells us that sunk costs must be ignored when comparing the *future* outcomes of alternative actions. 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the sunk cost fallacy and explains the normative principle that only future costs and benefits matter. Crucially, the response explicitly addresses the 'mental accounting' aspect by discussing the psychological driver of loss aversion and the desire to avoid 'wasting

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Mirella knows holding back would be better for both, yet she strips the grove anyway. What structural feature of her situation makes cooperation so difficult?

**Expected Answer:** **Prisoner's Dilemma** — A symmetric 2-player game where individual rationality (dominant strategy D) leads both players to an outcome strictly worse than mutual cooperation. The unique Nash equilibrium is (D,D), yet (C,C) Pareto-dominates it. *Defecting is individually rational — higher payoff regardless of the other's choice. But when both follow this logic, they lock into (1,1), forgoing the mutually superior (3,3).*

**Model Response:**
> **1. What is being demonstrated?**  
Mirella’s argument is the textbook *prisoner’s‑dilemma* reasoning (a *tragedy of the commons* situation).  She is using a **dominant‑strategy / maximin** line of thought: “I will choose the action that protects me against the worst‑case (the other player defecting), even though a mutually cooperative outcome would be far better.”  In game‑theoretic language this is the **one‑shot Nash‑equilibrium** of a 2‑player, 2‑action Prisoner’s Dilemma that is being applied uncritically to an *iterated* setting.

**2. Name of the pattern**  

| Common name | Formal term |
|-------------|-------------|
| Prisoner’s Dilemma (defect‑defect outcome) | Dominant‑strategy equilibrium / Maximin reasoning |
| (when applied to a shared resource) | Tragedy of the Commons |
| 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the Prisoner's Dilemma and accurately explains the mechanism of dominant strategies and Nash equilibrium in a one-shot context. Crucially, they go beyond the basic requirements by identifying the iterated nature of the scenario as a counterpoint, effec

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks you to find the Nash Equilibrium. For each strategy pair, check: could either cadet do better by switching alone? Which pair survives this test?

**Expected Answer:** **Nash equilibrium** — A Nash Equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. In the PD above, (Fortify, Fortify) is the unique Nash Equilibrium: if A plays Fortify and B plays Fortify, A gets 1. If A switches to Patrol, A gets 0 (worse). Symmetrically fo *Nash Equilibrium captures the key insight of strategic stability: no player can do better by changing strategy alone. In the PD, Fortify dominates Patrol — regardless of what the opponent does, Fortif*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The instructor is asking the cadets to apply **strict‑dominance (dominant‑strategy) reasoning** in order to locate a **Nash equilibrium** of a classic **Prisoner’s‑Dilemma** game.  In everyday language this is often called the “*defect‑defect*” reasoning pattern, or the “*dominant‑strategy fallacy*” when it is mistakenly taken to be the *optimal* outcome for the group.

---

**2. Name of the pattern / bias / concept**  

| Formal name | Common shorthand |
|-------------|------------------|
| **Strictly dominant‑strategy reasoning** (leading to a **dominant‑strategy Nash equilibrium**) | “Defect‑defect” reasoning in a Prisoner’s Dilemma |
| When taken as a prescription for what *should* happen rather than what *will* happen, it is the **“Nash‑e

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as Nash equilibrium derived from strict-dominance reasoning in a Prisoner's Dilemma. They accurately distinguish between the equilibrium outcome ('defect-defect' or Fortify-Fortify) and the optimal group outcome, avoiding the Level 1 error of confusing st

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?

**Expected Answer:** **Iterated PD and cooperation** — In a finitely repeated PD with known endpoint, backward induction predicts defection every round. But in an infinitely repeated PD (or one with unknown endpoint), the Folk Theorem shows that cooperation can be sustained as a Nash Equilibrium if players value future payoffs enough (discount factor de *Iteration changes everything. The shadow of the future creates incentives for cooperation: defecting today earns a short-term gain but triggers retaliation that reduces future payoffs. If the future i*

**Model Response:**
> **1. What reasoning pattern is being displayed?**  
The instructor is implicitly **assuming a perfectly deterministic world – i.e., “no‑noise” or “perfect‑monitoring” reasoning** – and then asking what goes wrong when that assumption is violated. In the language of cognitive‑bias taxonomy this is a **deterministic bias / “perfect‑information” fallacy** (sometimes called the *no‑error fallacy*). It is the counterpart of the “Nirvana‑fallacy” in decision theory: we judge a strategy by the idealised, error‑free version of the game and then treat any deviation (a single mistaken defection) as a catastrophic failure of the strategy.

**2. Name of the pattern**  

- **Deterministic (no‑noise) bias** – the belief that the environment is completely predictable and that a single mistake will be int

**Score:** 1/4 █░░░
**Judge Reasoning:** The student failed to identify the correct reasoning pattern. The prompt asks about the mechanism of cooperation in repeated games (Iterated PD, Folk Theorem, Shadow of the Future), but the student incorrectly focused on 'deterministic bias' and noise. While the student mentioned TFT's forgiveness p

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find both Nash Equilibria in the Stag Hunt. Which is payoff-dominant? Which is risk-dominant? Which would you choose, and what does your choice depend on?

**Expected Answer:** **Stag Hunt** — The Stag Hunt (from Rousseau) has two pure-strategy Nash Equilibria: (Stag, Stag) = (5,5) and (Hare, Hare) = (2,2). (Stag, Stag) is payoff-dominant (better for everyone). (Hare, Hare) is risk-dominant (safer — you get 2 guaranteed regardless of partner). The core tension: cooperation requires trust. *Unlike the PD, neither strategy dominates. The optimal choice depends entirely on expectations about your partner. This is a coordination problem, not a cooperation problem.*

**Model Response:**
> **1. What is being demonstrated?**  
The hunt master is putting the two hunters into a **coordination‑game (Stag‑Hunt) dilemma** and is watching them decide which equilibrium to “trust” the other to play.  The reasoning that most people fall back on in this situation is the **“risk‑dominance / safety‑first (maximin) heuristic.”**  In plain‑language terms it is the bias of **“I’ll pick the option that protects me from the worst‑case loss, even though a mutually better outcome exists.”**  

It is not a logical fallacy in the strict sense (the pay‑off matrix is correct), but it is a **decision‑theoretic bias** that pushes players toward the *risk‑dominant* equilibrium (Hare‑Hare) rather than the *pay‑off‑dominant* equilibrium (Stag‑Stag).

---

**2. Name of the pattern / bias**  

| Formal na

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the game as a Stag Hunt coordination problem. They explicitly distinguish between the payoff-dominant (Stag-Stag) and risk-dominant (Hare-Hare) equilibria. Furthermore, they go beyond basic identification to explain the underlying mechanism (maximin heuristic/loss av

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find all Nash Equilibria in this game, including any mixed-strategy equilibrium. Why is the mixed equilibrium worse for both players than either pure equilibrium?

**Expected Answer:** **Battle of the Sexes** — Battle of the Sexes has two pure-strategy Nash Equilibria: (Opera, Opera) = (3,2) and (Tournament, Tournament) = (2,3). Both are coordination equilibria — both players prefer being together over being apart. But they disagree on which is better: Helena prefers (Opera, Opera), Roderick prefers (Tourn *Neither player has a dominant strategy. The choice depends on expectations about the other — creating a coordination problem with a distributional conflict.*

**Model Response:**
> **1. What is being demonstrated?**  
The situation is a textbook *coordination‑failure* in a **Battle of the Sexes** game.  It is not a logical fallacy so much as a decision‑theoretic problem: two rational agents have a common interest in coordinating (both get a positive payoff) but have *conflicting* preferences over *which* coordinated outcome to pick.  The “if we can’t agree we’ll both go alone and get nothing” line is the classic *threat of a worst‑case outcome* that forces each player to consider the risk of ending up with the (0,0) payoff.

**2. Name it precisely**  
- **Game‑theoretic term:** *Battle of the Sexes* (a 2 × 2 coordination game with asymmetric preferences).  
- **Decision‑theoretic concept:** *Strategic uncertainty / coordination failure* (sometimes called a *multiple‑

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the game as 'Battle of the Sexes' and accurately lists both pure-strategy Nash Equilibria ((Opera, Opera) and (Tournament, Tournament)). They provide a strong explanation of the coordination-with-conflict structure and strategic uncertainty. However, the response doe

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** You and your contact must meet without communication. Why do people converge on the same location and time? What property makes some answers more likely than others, and is this a rational process?

**Expected Answer:** **Focal points (Schelling points)** — A focal point is a solution to a coordination game that attracts players' attention because it is salient — prominent, unique, culturally significant, or symmetric. Focal points work because of mutual expectations: I go to the fountain because I expect you to expect me to expect... etc. Sources of s *Focal points solve the equilibrium selection problem in coordination games. When there are many Nash Equilibria and no communication, salience determines which equilibrium is played. The insight is th*

**Model Response:**
> **1. What is being demonstrated?**  
A classic *coordination‑under‑no‑communication* reasoning pattern.  In game‑theoretic language it is the search for a **Schelling (or focal) point** – a solution that “stands out” because it is mutually salient and therefore likely to be chosen by both parties.

**2. Name of the pattern / bias**  

| Discipline | Term (most common) | Close relatives |
|------------|-------------------|-----------------|
| Game theory / decision theory | **Schelling point** (also called a **focal point**) | – |
| Cognitive psychology | **Salience bias** / **availability heuristic** (the mental shortcut that makes the most noticeable option feel “obvious”) | – |
| Social psychology | **False‑consensus effect** (the belief that others share your view of what is “obvious”) 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a Schelling/focal point and explicitly explains the mutual-expectation mechanism ('I think... the contact will think...'). They also list multiple sources of salience (distinctiveness, cultural background, visual strikingness). However, the response do

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid.

**Expected Answer:** **Convention (Lewis)** — A convention is a regularity R in behavior that is (1) followed by everyone, (2) expected by everyone, (3) preferred by everyone given others' conformity, (4) has at least one alternative R' that could have served instead, and (5) is common knowledge. Conventions are solutions to recurrent coordinat *Lewis's theory explains how arbitrary social practices persist and why they are rational to follow: given that everyone else conforms, conforming is your best response. This applies to language, money*

**Model Response:**
> **1.  What kind of reasoning is on display?**  
The philosopher is describing a **coordination‑game reasoning** – a situation in which each individual’s optimal action depends on what she expects everybody else to do.  In game‑theoretic language it is a **multiple‑equilibrium (Schelling) coordination problem**.  The everyday‑language version of this reasoning is often called the **“bandwagon” or “appeal‑to‑tradition”** pattern, and in behavioural economics it shows up as **status‑quo bias** (the tendency to stick with the existing convention because deviating is risky).

**2.  Precise name**  

| Discipline | Term (most precise) |
|------------|----------------------|
| Game theory / decision theory | **Coordination equilibrium (Schelling point) / common‑knowledge equilibrium** |
| Cogniti

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the scenario as a coordination problem and explicitly references Lewis's five conditions and common knowledge, satisfying the core requirements for Level 3. They also clearly explain the arbitrariness (that following the expected majority is what matters, not the spe

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor has drawn the Entry Game tree. Identify the decision nodes, the branches, and the terminal payoffs. What information does each player have when they move?

**Expected Answer:** **Game trees (extensive form)** — A game tree represents a sequential game with nodes (decision points), branches (available actions), terminal nodes (outcomes with payoffs), and information sets (what each player knows when they move). Unlike the normal form (matrix), the extensive form explicitly represents the order of moves, whi *The extensive form reveals strategic structure that the normal form hides. In this game, the Incumbent's threat to Fight is visible but not credible — if the Entrant enters, the Incumbent prefers Acco*

**Model Response:**
> **1. What is being demonstrated?**  
The reasoning that the Incumbent will “threaten to fight” and that the Entrant should therefore stay out is an **“non‑credible‑threat” fallacy** (sometimes called the *threat‑bias* or *failure to apply sub‑game perfection*).  In other words, the analyst is treating a threat that would be irrational for the Incumbent to carry

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core strategic mechanism of the game tree: the concept of non-credible threats and the necessity of subgame perfection. They demonstrate an understanding that the Incumbent's threat to fight is irrational once the Entrant has entered, which implies they can trace

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** Apply backward induction to the Entry Game. Start at the last decision node and work backward. What is the subgame perfect equilibrium? Why is the Incumbent's threat to Fight not credible?

**Expected Answer:** **Backward induction** — Backward induction solves extensive-form games by starting at the terminal nodes and working backward. At each decision node, the player is assumed to choose their optimal action. The resulting strategy profile is a subgame perfect equilibrium (SPE). In the Entry Game: (1) At Incumbent's node: Accom *Backward induction eliminates non-credible threats. (Stay Out, Fight) is a Nash Equilibrium but relies on the Incumbent's non-credible threat to Fight. Backward induction reveals that the Incumbent wo*

**Model Response:**
> **1. What is being illustrated?**  
The instructor is showing the *elimination of a non‑credible threat* by means of **backward induction** – the standard way to obtain a **sub‑game‑perfect Nash equilibrium (SPNE)** in an extensive‑form game.

---

### 2. Name of the pattern / concept  

| Formal term | Common description |
|-------------|--------------------|
| **Sub‑game‑perfect equilibrium** (or **sub‑game perfection**) | The refinement of Nash equilibrium that requires optimal play after *every* decision node (i.e., in every sub‑game). |
| **Credible threat / non‑credible threat** | A threat is credible only if the threatening player would actually carry it out when the sub‑game is reached. A threat that would be irrational to execute is *non‑credible* and is eliminated by sub‑game per

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as backward induction and accurately applies it to both nodes (Incumbent chooses Accommodate, Entrant chooses Enter) to derive the correct SPE (Enter, Accommodate). They also explain the concept of non-credible threats well. However, they do not fully rea

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The Entry Game has two Nash Equilibria. The instructor says one of them relies on a non-credible threat. Which one, and why does SPE eliminate it?

**Expected Answer:** **Subgame perfect equilibrium** — SPE (Selten 1965) requires that a strategy profile be a Nash Equilibrium in every subgame. A subgame is any part of the game tree that forms a complete game on its own. SPE eliminates NE that rely on non-credible threats — strategies that would not be followed through if the relevant decision node w *SPE is a refinement of NE that captures credibility. A threat is credible only if the threatener would actually carry it out. SPE formalizes this by requiring optimality at every node, not just on the*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The instructor is exposing a *non‑credible (or “empty”) threat* that is baked into a Nash equilibrium but would never be carried out when the decision node is actually reached.  In game‑theoretic language this is a **failure of sub‑game‑perfect (sequential) rationality** – the player’s strategy is optimal only on the equilibrium path and ignores incentives at off‑path decision nodes.

**2. Name of the pattern / fallacy**  

| Discipline | Term (most common) | Synonyms / related concepts |
|------------|-------------------|-----------------------------|
| Game theory | **Non‑credible threat** (or *empty threat*) | *Bluff*, *unsubsidized equilibrium* |
| Decision theory / economics | **Failure of sub‑game perfection** | *Lack of sequential ratio

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a non-credible threat and a failure of sub-game perfection. They accurately explain the mechanism: that Nash Equilibrium only considers on-path nodes, whereas the specific profile (Stay Out, Fight) relies on an action (Fight) that is suboptimal at the 

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Question:** Apply backward induction to the Centipede Game. What does it predict? Do you find the prediction convincing? What assumption is doing the heavy lifting, and what happens if you relax it?

**Expected Answer:** **Centipede Game** — The Centipede Game is a sequential game where two players alternate between stopping (taking a smaller immediate payoff) and continuing (allowing the total payoff to grow). Backward induction predicts immediate stopping — the unique SPE. But this is paradoxical: both players would be much better off *Backward induction is logically valid given CKR, but the outcome (1,1) seems absurd when (4,4) is available through mutual cooperation. The paradox reveals that CKR may be too strong an assumption — o*

**Model Response:**
> **1.  What reasoning pattern is on display?**  
The instructor is applying **backward‑induction reasoning under the assumption of common knowledge of perfect rationality**.  In game‑theoretic language this is the derivation of the **sub‑game‑perfect equilibrium (SP‑E)** of an extensive‑form game with perfect information.

**2.  Name of the pattern / paradox**  

| Common name | Formal description |
|-------------|--------------------|
| **Centipede (or backward‑induction) paradox** | The SP‑E of the centipede game is Pareto‑dominated by another feasible outcome (the “co‑operative” continuation to (4,4)). |
| **Rationality paradox / self‑defeating rationality** | The logical chain of “if I am rational, the other will be rational, …” leads to an outcome that is strictly worse for every ratio

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the Centipede Game/Paradox and accurately explains the mechanism of backward induction leading to the Subgame Perfect Equilibrium. They explicitly identify the paradox (logical inference leading to a Pareto-dominated outcome) and correctly trace the ro

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

**Expected Answer:** **Evolutionarily Stable Strategy (ESS)** — An ESS (Maynard Smith) is a strategy that, when adopted by almost all members of a population, cannot be invaded by any rare mutant strategy. Formally: S is ESS if for any mutant M, either (1) E(S,S) > E(M,S), or (2) E(S,S) = E(M,S) and E(S,M) > E(M,M). In Hawk-Dove with V<C, neither pure strategy i *ESS provides a concept of equilibrium that does not require rationality — only differential reproduction. Strategies that do better than average spread; those that do worse shrink. The mixed ESS emerg*

**Model Response:**
> **1. What is being demonstrated?**  
The biologist is applying the *indifference‑principle* (also called the *mixed‑strategy ESS condition* or *Maynard‑Smith’s ESS criterion*) to a two‑strategy Hawk–Dove game.  The reasoning proceeds by:

1. Checking the two pure strategies against the ESS definition and discarding them because each can be invaded by the opposite pure strategy.  
2. Concluding that the only remaining candidate is a *mixed* strategy and then solving for the mixture that makes the two pure strategies *exactly indifferent* when faced with the resident population.

In the language of informal logic this is an **argument‑by‑elimination** (or *false‑dichotomy* if one pretends “only pure or mixed” are the only possibilities), but in decision‑theoretic terms it is the standard **d

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that neither pure strategy is an ESS and describes the method for finding a mixed ESS (indifference principle). However, the response fails to perform the actual calculation (p=V/C) required for Level 3, and it completely omits the conceptual depth regarding populati

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The biologist perturbs the Hawk population from 50% to 51%. Show that the system returns to 50% by calculating fitness for each strategy. What does this tell you about the stability of the mixed ESS?

**Expected Answer:** **Replicator dynamics** — The replicator dynamics models how strategy frequencies change over time based on fitness. The equation dx_i/dt = x_i(f_i - F) says: strategies that outperform average grow; those that underperform shrink. Key properties: (1) ESS are stable fixed points of replicator dynamics. (2) Not all fixed poin *The replicator dynamics provides the 'how' behind ESS — the mechanism by which populations reach (or fail to reach) equilibrium. It requires no rationality, only differential reproduction or imitation*

**Model Response:**
> **1. What is being demonstrated?**  
The biologist is **generalising from a single, tiny perturbation** to claim that the mixed strategy is *stable* for the whole replicator system.  In logical‑epistemic terms this is the **“hasty‑generalisation” (or “over‑generalisation”) fallacy** – a form of *inductive reasoning from an insufficient sample*.  In decision‑theoretic language it is an **“insufficient‑evidence”** justification for a claim about the global dynamics.

---

**2. Name of the pattern**  

| Discipline | Canonical label |
|------------|-----------------|
| Logic / informal fallacies | **Hasty Generalisation** (also called *over‑generalisation* or *argument from anecdote*) |
| Cognitive psychology | **Availability / Confirmation bias** (selecting a single confirming case) |
| Deci

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly computes the fitness comparison at the perturbed state (51% Hawks), noting that Doves have an advantage. However, the response fundamentally misidentifies the pattern as a logical fallacy ('Hasty Generalisation') rather than recognizing it as the correct application of replicat

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In the evolutionary Stag Hunt, what determines whether cooperation or defection wins? Why does Skyrms call the cooperative equilibrium a 'social contract'? What factors help cooperation evolve?

**Expected Answer:** **Evolution of cooperation** — In evolutionary Stag Hunt, cooperation (Stag) can evolve if enough of the population already cooperates. The threshold is p=0.5 in standard payoffs. Above the threshold, cooperation is self-reinforcing; below, it collapses. This is the basin of attraction concept. Factors that help cooperation evolv *The evolution of cooperation shows that cooperative outcomes can emerge without rational deliberation — through selection, iteration, and correlation. This provides a different foundation for social o*

**Model Response:**
> **1.  The pattern that is being displayed**  
The biologist is using a *deterministic‑threshold* line of reasoning: the mixed‑strategy point \(p^{*}=0.5\) is treated as a hard “tipping‑point” that cleanly separates two mutually exclusive futures – “if the share of stag‑hunters is **above** 0.5 then cooperation will inevitably spread; if it is **below** 0.5 then it will inevitably collapse.”  

In the jargon of behavioural economics and decision theory this is often called a **critical‑mass (or threshold) fallacy** – the belief that once a single numeric threshold is crossed, the system will automatically move to a particular outcome, ignoring stochastic fluctuations, finite‑population effects, and the possibility of lingering in the mixed region.

---

**2.  Name of the bias / concept**  


**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the evolutionary pattern and accurately calculates the threshold (p=0.5) and the concept of basins of attraction (described as an unstable separator). However, the response fails to discuss the specific factors that help cooperation evolve (such as iteration, assortm

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Torva says her profit from the sword is eighty gold. Is she right? What is she forgetting to account for?

**Expected Answer:** **Opportunity cost** — The opportunity cost of an action is the value of the next-best alternative forgone. Torva treats the sword's revenue (80 gold) as pure profit, but by choosing the sword she forgoes the 50-gold axle repair. Her net gain from choosing the sword over the axle is 80 - 50 = 30 gold, not 80 gold. The 50  *Every choice has a hidden cost: what you gave up to make it. Torva's sword commission is genuinely better than the axle repair, but by 30 gold, not by 80. Understanding this prevents her from overvalu*

**Model Response:**
> **1. The reasoning pattern**  
Torva is **ignoring the opportunity cost of her time** and equating the *price* of a job with *profit*. In decision‑theoretic language this is a classic case of **opportunity‑cost neglect** (sometimes called “single‑attribute” or “narrow‑framing” bias).  

**2. Name of the fallacy / bias**  
- **Opportunity‑cost neglect** (a form of *myopic* or *single‑factor* decision bias).  
- In economics it is also described as **failure to account for marginal cost** or **ignoring the true profit‑maximising criterion**.  

**3. Why the reasoning is flawed (or occasionally useful)**  

| What Torva does | Why it’s wrong (or limited) |
|-----------------|-----------------------------|
| **Looks only at the gross payment** (80 gp vs. 50 gp). | The *gross* amount is not the

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'opportunity cost' and explicitly names the bias. They accurately explain the mechanism by distinguishing between revenue and net profit, noting that the implicit cost (the forgone axle job) must be subtracted. Furthermore, the response exceeds the bas

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Hilde outproduces Oskar in both wheat and flax. She says trade cannot benefit her. Is she right? Calculate the opportunity costs and determine who should specialize in what.

**Expected Answer:** **Comparative advantage** — Hilde has absolute advantage in both goods, but comparative advantage depends on opportunity cost. Hilde's opportunity cost of 1 bolt of flax = 2 bushels of wheat (12/6). Oskar's opportunity cost of 1 bolt of flax = 4/3 bushels of wheat. Oskar has a lower opportunity cost for flax, so he has compara *Trade benefits do not require being equally productive. Even though Hilde is better at both crops, she benefits from specializing in the crop where her relative advantage is greatest (wheat) and tradi*

**Model Response:**
> **1. The reasoning pattern**  
Hilde is committing the classic **“absolute‑advantage fallacy”** – the mistaken belief that because she can produce *more of every good* than Oskar, there can be no mutually beneficial trade. In economic‑theory language this is a failure to apply **comparative advantage** (or, equivalently, a neglect of opportunity‑cost reasoning).

**2. Name of the fallacy / bias**  
- **Absolute‑advantage fallacy** (sometimes described as “the trade‑is‑zero‑sum fallacy”).  
- Closely related to the **opportunity‑cost neglect** bias and to **self‑serving bias** (the belief that one’s own situation cannot be improved by others).

**3. Why the reasoning is flawed (or, when it can be right)**  

| What Hilde does | Why it is wrong |
|-----------------|-----------------|
| **Com

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'absolute-advantage fallacy' and accurately calculates the opportunity costs for both agents (2 wheat/flax for Hilde, 1.33 for Oskar). They correctly deduce that Oskar has the comparative advantage in flax and Hilde in wheat. However, the response ends abruptly (

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?

**Expected Answer:** **Constrained optimization** — The problem is to minimize cost subject to constraints. Food constraint: 3R >= 15, so R >= 5 (minimum 5 ration packs). Torch constraint: 4T >= 8, so T >= 2 (minimum 2 torch bundles). Cost: 5R + 10T. Minimum cost = 5(5) + 10(2) = 25 + 20 = 45 gold. This satisfies both constraints and is within budget *Constrained optimization is the core microeconomic framework: maximize (or minimize) an objective function subject to binding constraints. Seren cannot simply buy everything — she must find the combin*

**Model Response:**
> **1. What is being demonstrated?**  
The dialogue is an example of a *myopic‑optimisation* or *greedy‑algorithm* reasoning pattern.  The decision‑maker (Seren) treats the problem as “pick the cheapest item that helps us satisfy a requirement, then move on to the next requirement”, implicitly assuming that this locally cheapest choice will also give the globally cheapest solution.

**2. Name of the pattern / fallacy / bias**  
- **Greedy‑algorithm fallacy** (also called *myopic optimisation* or *local‑optimality bias*).  
- In decision‑theoretic language it is a failure to recognise that the problem is a **constrained optimisation (integer linear programming) problem**, not a series of independent “cheapest‑first” choices.

**3. Why the reasoning is (often) wrong**  

| Step in the greedy l

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the underlying problem structure as constrained optimization and accurately calculates the minimum cost (45g) with R=5 and T=2, verifying the constraints. They also correctly note the surplus (55g) implicitly by mentioning the total spent. However, they do not reach 

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Each potion sells for 15 gold. The cost of each additional potion rises: 5, 8, 12, 16, 22. How many potions should Elara brew, and why?

**Expected Answer:** **Marginal analysis** — Marginal analysis compares the marginal benefit (MB) to the marginal cost (MC) of each additional unit. Brew if MB > MC; stop when MC >= MB. Revenue per potion (MB) = 15 gold. MC of potions: 1st=5, 2nd=8, 3rd=12, 4th=16, 5th=22. For potions 1-3, MB(15) > MC. For potion 4, MC(16) > MB(15). Elara shou *Marginal analysis prevents two errors: stopping too early (missing profitable units) and going too far (adding units that cost more than they earn). The fourth potion costs 16 gold but only earns 15 —*

**Model Response:**
> **1. The reasoning pattern that is being (or should be) used**  
The situation calls for **marginal‑analysis / profit‑maximisation** – the decision‑theoretic rule that a rational producer should keep producing additional units **as long as the marginal revenue (the extra money earned from the next unit) is at least as large as the marginal cost (the extra money spent to make that unit).**  

When someone ignores this rule and keeps producing because “the first potions were cheap” or because “I’ve already started brewing,” they are falling into the **sunk‑cost fallacy**. The correct pattern, however, is the marginal‑cost‑vs‑marginal‑revenue decision rule.

---

**2. Precise name**

- **Decision‑theoretic concept:** *Marginal‑Cost = Marginal‑Revenue rule* (sometimes called the *profit‑maximi

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as marginal analysis and accurately applies the decision rule (MR >= MC) to determine the optimal quantity of 3 potions. They explicitly compare the marginal revenue (15) against each marginal cost and correctly conclude that the 4th potion should not be 

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Captain Hale says she should let the others pay for the lighthouse oil. Her reasoning seems logical from her own perspective. What happens if every captain follows the same logic? Why does this situation arise?

**Expected Answer:** **Public goods and free riding** — The lighthouse is a public good: non-rival (one captain using the light does not diminish it for others) and non-excludable (you cannot prevent a non-paying captain from seeing the light). These properties create a free-rider incentive: each captain benefits from the lighthouse regardless of whether *Free riding is individually rational but collectively destructive. Hale's logic is valid for any single captain, but if universalized, it leads to a lighthouse going dark and all captains risking thei*

**Model Response:**
> **1. What is being demonstrated?**  
The captains are exhibiting the classic **free‑rider (or collective‑action) problem** – a social‑dilemma situation that can be modelled as a **public‑goods game** (the lighthouse light is a non‑excludable, non‑rival public good). In game‑theoretic terms each captain is playing the **dominant‑strategy / Nash‑equilibrium reasoning** that leads to a sub‑optimal outcome.

---

**2. Name of the pattern**

- **Free‑rider problem** (public‑goods dilemma)  
- Often described as a **prisoner‑dilemma** or **public‑goods game** in decision theory.  

---

**3. Why the reasoning is (in)correct – the mechanism**

| Step | Reasoning of Captain Hale (and each other) | Why it looks “rational” | Why it fails |
|------|--------------------------------------------|-------

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the free-rider problem and explicitly defines the lighthouse as non-excludable and non-rival. They clearly explain the mechanism where individual rationality (dominant strategy) leads to a collectively sub-optimal Nash equilibrium, connecting it to the Prisoner's Dil

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Elder Yara says every family is acting sensibly, yet the lake is dying. How can individual rationality produce collective disaster? What is the structural problem?

**Expected Answer:** **Commons problems (Tragedy of the commons)** — Lake Mirren is a common-pool resource: rival (each fish caught is unavailable to others) but non-excludable (no family can be prevented from fishing). Each family captures the full benefit of each additional fish they catch but bears only a fraction of the cost (resource depletion shared across all  *The structural incentive to overextract is real and rational for each individual. The problem is not stupidity or greed but a misalignment between individual and collective incentives.*

**Model Response:**
> **1. What is being demonstrated?**  
The scene is a textbook illustration of a **collective‑action failure on a common‑pool resource** – the *Tragedy of the Commons*.  In game‑theoretic language it is a **prisoner‑dilemma / dominant‑strategy** situation (sometimes called a *common‑pool resource dilemma*).  The families’ reasoning follows the pattern:

> “If I do not increase my catch, the other families will take the extra fish and I will be left with less. Therefore I must also take more, even though everybody would be better off if we all kept to the sustainable level.”

**2. Name of the pattern / fallacy / bias**  

| Discipline | Term (most common) | Synonyms / related concepts |
|------------|-------------------|-----------------------------|
| Economics / Ecology | **Tragedy of the C

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the Tragedy of the Commons and explicitly connects it to Game Theory (Prisoner's Dilemma, dominant strategy). They accurately explain the mechanism: the resource is non-excludable, individual rationality (fear of others taking more) drives over-extract

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Sera and Brenn create 80 gold in surplus from trade. Sera's outside option gives her 15 gold surplus; Brenn's gives him 10. How should they split the 80 gold surplus, and why?

**Expected Answer:** **Bargaining and fairness (Nash bargaining)** — The surplus from trade is 80 gold. Each merchant's outside option (BATNA) sets a floor: Sera will not accept less than 15 gold surplus (her alternative deal), and Brenn will not accept less than 10. The remaining surplus after securing both outside options is 80 - 15 - 10 = 55 gold. Nash bargaining  *Bargaining theory shows that fair division depends not just on the total surplus but on each party's outside option. Better alternatives give you more bargaining power. This framework prevents the nai*

**Model Response:**
> **1. What is being demonstrated?**  
The merchants are using the *“split‑the‑difference / 50‑50 split”* heuristic – a fairness‑bias that treats the pie as if it were fixed and assumes an equal division is the only “fair” outcome, even though each party has a different outside option (BATNA) and a different contribution to the surplus.

**2. Name of the pattern**  

| Formal name (economics / decision theory) | Common colloquial label |
|-------------------------------------------|--------------------------|
| **Equal‑division bias** (sometimes called the *“50 % split fallacy”* or *“splitting the difference”* heuristic) | *“Both of us get half”* thinking |

It is also described in bargaining literature as **ignoring reservation values** (BATNAs) and **treating the surplus as a fixed pie**.


**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies that outside options (BATNAs) are being ignored and explains why a naive 50-50 split is flawed (Level 1 criteria). However, the response fails to perform the correct calculation for the Nash bargaining solution (splitting the remaining surplus after securing outside 

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Lady Ashworth paid Corbin a flat wage and got a poor harvest. She suspects shirking but cannot prove it. What is the structural problem with her contract, and how might she redesign it?

**Expected Answer:** **Principal-agent problems and moral hazard** — The principal (Ashworth) delegates a task to an agent (Corbin) whose effort she cannot observe. Under a flat wage, the agent bears the cost of effort but captures none of the benefit (the extra apples go to the principal). This misalignment of incentives is moral hazard: the agent has both the oppor *Corbin is not necessarily lazy or dishonest — the contract structure gives him no reason to exert effort. The problem is the incentive design, not the person.*

**Model Response:**
> **1. The reasoning pattern that is being exposed**

The passage is a textbook illustration of a **principal‑agent problem** that creates **moral hazard** (hidden‑action problem).  
Lady Ashworth recognises that, because Corbin’s effort is unobservable, a **flat‑rate wage** gives him **no incentive** to exert effort. The “reasoning” she is doing is the logical deduction that *when the payoff to the agent does not depend on the agent’s hidden action, the agent will rationally choose the low‑effort (or shirking) option*.

**2. Name of the pattern / fallacy / bias**

- **Principal‑agent problem** (a type of agency problem)  
- **Moral hazard** (specifically “hidden‑action moral hazard”)  
- In the language of decision theory it is an **incentive‑incompatibility** or **incentive‑misalignment** 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the principal-agent problem and moral hazard, explains the mechanism of hidden action and incentive misalignment clearly, and proposes multiple incentive-compatible solutions (piece-rate, profit-sharing, monitoring). However, the response does not explicitly distingu

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Using the market board data, find the price at which quantity supplied equals quantity demanded. What happens at prices above or below this equilibrium?

**Expected Answer:** **Supply, demand, and market equilibrium** — At equilibrium, quantity supplied equals quantity demanded. From the table: at price = 2, excess demand (shortage) of 60. At price = 8, excess supply (surplus) of 60. At price = 6, Qs = 60 = Qd = 40 — not yet equal. Interpolating (or reading the table), equilibrium is at price = 5, where both Qs and *The equilibrium price coordinates decentralized buyers and sellers without anyone needing to manage the outcome. Prices above equilibrium create surpluses (pushing price down); prices below equilibriu*

**Model Response:**
> **1. What kind of reasoning is on display?**  
The market master is committing a *false‑dichotomy / limited‑alternatives* error (sometimes called the **“discrete‑price fallacy”**). He treats the five prices shown on the board as the *only* possible market‑clearing prices and therefore believes that a single price must exist among them at which “quantity supplied = quantity demanded.” In other words, he is **ignoring the continuity of the price variable** and the fact that equilibrium can lie *between* the listed points.

---

**2. Name of the bias / fallacy / concept**  

- **False dichotomy (limited‑alternatives bias)** – the belief that only the explicitly presented options are viable.  
- In economics‑theory language it is often called the **“discrete‑price fallacy”** or **“price‑grid f

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the prompt's core task: identifying the equilibrium price and quantity using the supply and demand pattern. Instead of analyzing the table to find where Qs equals Qd (P=5, Q=50), the student argued that the problem itself was flawed due to a 'discrete-price f

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** The king sets a price ceiling of 3 gold per bushel. Equilibrium was at 5 gold and 50 bushels. What happens to quantity supplied, quantity demanded, and the market? What trades are lost?

**Expected Answer:** **Price controls and deadweight loss** — A binding price ceiling (set below equilibrium) creates a shortage: quantity demanded exceeds quantity supplied. At P=3, Qs=30 and Qd=70, shortage=40. Some mutually beneficial trades that would occur at equilibrium (P=5, Q=50) no longer happen. The lost surplus from these unrealized trades is deadwe *The price ceiling is well-intentioned but creates predictable inefficiency. The 30 buyers who get grain pay less, but 20 buyers who would have purchased at equilibrium get nothing, and 20 units of gra*

**Model Response:**
> **1. What reasoning pattern is on display?**  
The market master is falling into a classic *availability‑/salience bias* (sometimes called the *availability heuristic*).  He lets the most vivid, easily imagined consequences of the ceiling – the obvious shortage, the angry crowd of 40 would‑be buyers, and the lurid black‑market price of 7 gold – dominate his judgment about the policy’s overall merit.  In doing so he also commits a *fallacy of composition*: he infers that because the ceiling hurts a noticeable group, the policy is a net loss for the whole economy, even though a different, clearly identified group (the first 30 buyers) is better off.

---

**2. Name of the bias/fallacy**

| Concept | Common name(s) |
|---------|----------------|
| **Availability / Salience bias** | Availabili

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the prompt's subject matter. Instead of analyzing price controls, shortages, and deadweight loss as required by the rubric, the student incorrectly framed the response around cognitive biases (availability heuristic, fallacy of composition) and psychological 

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** Grist says his business is profitable and efficient. Wynn says Clearwater is paying part of his costs. Who is right, and what does this situation reveal about market prices?

**Expected Answer:** **Externalities** — A negative externality is a cost imposed on third parties who are not involved in the transaction. Grist's private cost is 40 gold, but the social cost includes the 20 gold per week Clearwater spends on water treatment. The true social cost of production is 60 gold, making Grist's true profit 40, no *Externalities mean the market price sends the wrong signal. Grist's leather seems like a great deal at 100 gold, but 20 gold of the true cost is hidden and borne by Clearwater. The market 'works' only*

**Model Response:**
> **1. The reasoning pattern that is on display**  
The tanner’s profit‐calculation is a classic case of **ignoring (or denying) external costs** – i.e. treating a *private* cost‑benefit analysis as if it were the whole story. In the language of economics and decision theory this is called **the “externality fallacy”** (sometimes phrased as *failure to internalize externalities* or *partial‑cost accounting*). It is also a manifestation of the **self‑serving bias**: Grist evaluates the situation only from the perspective of his own gains and discounts any harm that falls on others.

**2. Precise name**  
- **Externality fallacy** (failure to internalize negative externalities)  
- Closely related: **Self‑serving bias** in cost‑benefit reasoning  

**3. Why the reasoning is flawed (mechanism)*

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a negative externality and explains the mechanism by distinguishing between private and social costs. They accurately note that Grist's profit calculation is inflated because it ignores external damages, leading to market inefficiency. Furthermore, the

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral?

**Expected Answer:** **Information asymmetry and adverse selection (lemons problem)** — When sellers know more about product quality than buyers, buyers cannot distinguish good from bad. They offer a price reflecting average quality. Owners of above-average horses find this price too low and withdraw. The remaining pool is worse, buyers adjust downward, more good horses leave — a death *The market failure is not caused by dishonesty per se but by the information structure. Even honest sellers of good horses cannot credibly communicate quality because cheap talk ('my horse is great') *

**Model Response:**
> **1. What is being demonstrated?**  
The situation is a textbook case of **adverse‑selection caused by information asymmetry** – the “market for lemons” problem first described by George Akerlof (1970).  It is not a logical fallacy in the strict sense; it is a rational, game‑theoretic prediction about how a market behaves when one side (the sellers) has private knowledge of product quality that the other side (the buyers) cannot verify.

**2. Name of the pattern**  
- **Adverse selection** (also called the **lemons problem**).  
- Closely related concepts: **information asymmetry**, **signaling**, **screening**, and **market failure**.

**3. Why the reasoning is (in)correct – the mechanism**  

| Step | What happens | Why it matters |
|------|--------------|----------------|
| **Private in

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as adverse selection (the lemons problem) caused by information asymmetry. They provide a clear, step-by-step explanation of the mechanism, including the average pricing dynamic and the resulting death spiral where high-quality goods exit the market. Furt

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Nobody buys the Barrel Mug, yet adding it to the menu increases Large Ale sales. The tip jar moved but the tip amount was not suggested. What is going on in both cases, and is it ethically acceptable?

**Expected Answer:** **Behavioral economics in markets: nudges and choice architecture** — Two phenomena are at work. First, the decoy effect: the Barrel Mug is a dominated option that no one chooses, but its presence makes the Large Ale seem more reasonable by comparison. It shifts the reference point. Second, choice architecture: the placement of the tip jar changes behavior without cha *When used to exploit, nudges can undermine autonomous decision-making. Customers believe they are choosing based on preferences, but the choice architecture is steering them toward the seller's prefer*

**Model Response:**
> **1. The reasoning pattern at work**  
The phenomenon Lena is exploiting is a classic *choice‑architecture* effect. Two closely‑related concepts are at play:

| Phenomenon | What it is | Why it works in Lena’s case |
|------------|------------|-----------------------------|
| **Decoy (or “asymmetric‑dominance”) effect** | Adding a third, clearly inferior (or overpriced) option makes one of the original options look more attractive. | The “Barrel Mug (15 c)” is a *decoy*: it is more expensive than the Large Ale (8 c) but offers no clear extra value. When the decoy is present, the Large Ale is judged as a “good deal” relative to the decoy, so its sales rise. |
| **Anchoring / contrast bias** | People evaluate a price relative to other prices that are salient at the moment. | The 15‑c price a

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies both the decoy effect and choice architecture (salience/proximity), explaining how context influences decisions beyond rational preference. They also explicitly address the ethical implications and manipulative nature of these tactics. However, the response falls sho

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Breck says the storm is good for the economy because it creates repair jobs. The clerk is skeptical. Who is right, and what is Breck failing to consider?

**Expected Answer:** **Broken window fallacy** — Breck counts the economic activity generated by repairing storm damage (the seen) but ignores the economic activity that the same money would have generated if spent on something else (the unseen). The glazier's gain is real, but the shopkeepers now spend money on window repairs instead of on new in *The fallacy confuses visible economic activity with net economic gain. Repair spending is seen; the forgone alternative spending is unseen. Bastiat's insight: 'the bad economist confines himself to th*

**Model Response:**
> **1. The reasoning pattern**  
The alderman is committing the classic *“broken‑window”* line of reasoning – an economic fallacy that treats **destruction itself as a net source of prosperity** because it creates short‑term demand for goods and services.

**2. Name of the fallacy / bias**  

| Formal name | Common synonyms |
|-------------|-----------------|
| **Broken‑Window Fallacy** (also called the *fallacy of “destruction creates wealth”* or *“economic optimism about disaster”*) | *Misunderstanding of opportunity cost*, *zero‑sum thinking*, *optimism bias* when applied to macro‑economic outcomes |

**3. Why the reasoning is flawed (mechanism)**  

| Step in the argument | What is actually happening | Why it is a fallacy |
|----------------------|----------------------------|-----------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Broken Window Fallacy and explains the core mechanism: counting direct repair spending while ignoring opportunity costs (what resources could have produced otherwise) and the net loss of wealth. The response clearly distinguishes between distributional effects an

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Dagan says that if Brassholm gains from trade, Ardenvale must lose. Petra says both sides can gain. Who is right, and why?

**Expected Answer:** **Zero-sum thinking** — Dagan falsely assumes that trade is zero-sum — that total value is fixed and any gain for one party is a loss for the other. In reality, voluntary trade creates value because parties exchange goods they value less for goods they value more. Ardenvale values iron more than its surplus grain; Brasshol *If trade were truly zero-sum, neither party would voluntarily agree to it — why accept a deal that makes you worse off? The fact that both parties choose to trade is evidence that both expect to benef*

**Model Response:**
> **1‑2.  The pattern**

Dagan is displaying a classic **zero‑sum bias / zero‑sum fallacy** – the belief that any gain for one side must be an equal loss for the other, as if the “pie” of wealth were fixed and could not be enlarged.

---

### 3.  Why the reasoning is flawed (or occasionally useful)

| What the reasoning assumes | Why it fails in most economic situations | When it can be a reasonable shortcut |
|----------------------------|------------------------------------------|--------------------------------------|
| **Conservation of wealth** – “gold can’t appear from nowhere; it must be taken from someone else.” | Trade creates *new* value through comparative advantage, specialization, and exchange. The total surplus (the “pie”) can grow, so both parties can end up better off. | In c

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'zero-sum bias/fallacy' and explicitly names Dagan's error as the 'fixed pie' assumption. They accurately explain the mechanism of value creation through comparative advantage, specialization, and the conversion of surplus goods into utility. Furthermo

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter?

**Expected Answer:** **Rapoport's Rules** — A four-step protocol for productive disagreement: (1) restate the opponent's position so well they endorse the restatement, (2) list genuine points of agreement, (3) acknowledge what you learned from them, (4) only then offer criticism. Corwin follows all four steps in sequence. *Corwin follows the protocol exactly. Step 1: Holt says 'Better than I put it myself.' Step 2: Lists two factual agreements about timber loss and budget crisis. Step 3: Concedes the flow-rate data corr*

**Model Response:**
> **1. What is being demonstrated?**  
Alderman Corwin is **steel‑manning** (or, in more textbook language, applying the **principle of charity** to an opponent’s argument).  

**2. Name it precisely**  
*Steel‑man fallacy* – not a fallacy when done correctly, but the *steel‑man* reasoning pattern (the opposite of a straw‑man).  

**3. Why it works – the mechanism**  

| Step | What Corwin does | Why it matters (good or bad) |
|------|------------------|------------------------------|
| **a. Restate the opponent’s claim** | “Let me make sure I have Master Holt’s position right …” | He reconstructs the argument in its *strongest, most coherent* form. This avoids the classic **straw‑man** error of attacking a weakened version. |
| **b. Verify the reconstruction with the opponent** | Holt nods,

**Score:** 2/4 ██░░
**Judge Reasoning:** The student identifies the general concept of charitable argumentation (steel-manning) but fails to identify the specific four-step protocol (Rapoport's Rules) required by the correct answer. Specifically, the student misses Step 3 (acknowledging what was learned) and conflates the sequence by split

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?

**Expected Answer:** **Reductio ad absurdum** — Tessa takes Varek's claim ('all beliefs are equally valid') and draws out its logical consequences: flat earth is as valid as round earth, poison is as nutritious as food. Since Varek cannot accept these consequences, his original claim is undermined. This is the classic structure of reductio: assum *Reductio is a powerful tool because it tests a claim by its own standards. If a principle generates consequences the proponent themselves cannot stomach, the principle is in trouble. You do not need t*

**Model Response:**
> **1. What is being demonstrated?**  
Varek is engaging in *epistemic relativism* (sometimes called *cognitive relativism*) and, in argumentative form, commits the **false‑equivalence / false balance** fallacy. He treats *all* propositions as having the same epistemic status simply because “no one may claim superiority,” ignoring the role of evidence, coherence, and reliability.

**2. Name of the pattern**  

- **Epistemic (or cognitive) relativism** – the claim that no belief is objectively better justified than any other.  
- **False equivalence (false balance)** – presenting two unequal claims as if they were equally warranted.

**3. Why the reasoning is faulty (or, when it can be useful)**  

| Element | What the reasoning does | Why it is problematic |
|---------|----------------------

**Score:** 1/4 █░░░
**Judge Reasoning:** The student fundamentally misidentified the subject of the analysis. The prompt asks to evaluate Tessa's argumentative strategy (which uses reductio ad absurdum), but the student analyzed Varek's initial claim, labeling it as 'epistemic relativism' and 'false equivalence.' While the student mentione

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** You have two explanations for the attic disturbances. What principle should guide your choice between them, and which explanation does it favour?

**Expected Answer:** **Occam's Razor** — When two hypotheses explain the same evidence, prefer the one that posits fewer entities and mechanisms. Elsa's squirrel hypothesis explains the torn food, scattered flour, muddy tracks, thumping, and fallen items using one known entity (squirrels) and one known mechanism (foraging through a gap). W *Occam's Razor is not a proof — it is a heuristic for rational belief. Simpler explanations are preferred because each additional assumption is an additional point of potential failure. The squirrel hy*

**Model Response:**
> **1. What specific reasoning pattern is being demonstrated?**  
The widow is using an **appeal to ignorance (argumentum ad ignorantiam)** – “we don’t know how a natural creature could have done it, therefore a ghost must be responsible.”  In everyday language this shows up as **magical‑thinking / supernatural attribution** and, from a decision‑theoretic view, as **probability neglect of low‑likelihood supernatural causes**.

**2. Name it precisely**  
*Argument from ignorance* (also called *appeal to ignorance* or *argumentum ad ignorantiam*).  

**3. Explain the mechanism – why it is a bad (or occasionally good) line of reasoning**  

| Step | What the widow does | Why it fails |
|------|---------------------|--------------|
| **Premise** | “We cannot explain the nightly damage with the e

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that the squirrel hypothesis is simpler and explicitly mentions 'Occam's razor' as a violated principle, noting that the natural explanation fits the data with fewer assumptions. This meets Level 3 criteria. However, the response does not reach Level 4 because it fra

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Cask seems to have made a strong case. But look carefully at what he talked about and what he did not talk about. What is his argumentative strategy, and what is wrong with it?

**Expected Answer:** **Occam's Broom** — Dennett coined 'Occam's Broom' to describe the practice of sweeping inconvenient facts under the rug to make your argument look cleaner than it is. Unlike Occam's Razor (which removes unnecessary assumptions), Occam's Broom removes necessary evidence. Cask does not engage with the three independent  *Honest reasoning requires engaging with all the relevant evidence, especially evidence that challenges your position. Cask's case looks strong only because he has hidden the strongest evidence against*

**Model Response:**
> ### 1‑2.  What is being demonstrated – the name  

The passage is a **cluster of informal fallacies** that together constitute a classic **“cherry‑picking / selective‑evidence”** strategy, reinforced by:

| Fallacy / bias | Common name |
|----------------|-------------|
| **Cherry‑picking** (also called *selective evidence* or *suppressed evidence*) | – |
| **Ad hominem circumstantial** (questioning Dr Lune’s funding) | – |
| **Appeal to authority** (company inspectors as “the real” source) | – |
| **Argument from ignorance / “absence of evidence”** (“no miners are sick, therefore water is safe”) | – |

The dominant pattern is **cherry‑picking** – presenting only evidence that supports the desired conclusion while ignoring, dismissing, or disparaging the contrary data.

---

### 3.  Why th

**Score:** 3/4 ███░
**Judge Reasoning:** The student accurately identifies the core pattern of 'cherry-picking' (selective evidence) and explicitly notes that Cask omitted the three independent studies while foregrounding favorable data. They also correctly identify the funding attack as an ad hominem circumstantial fallacy. This aligns pe

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Torvin says Cael is just ignoring the rules. Cael says something different. What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?

**Expected Answer:** **Jootsing (Jumping Out Of The System)** — Dennett argues that genuine creativity requires first mastering the rules of the system you are working in, and then deliberately violating specific rules for specific reasons. Random rule-breaking is just noise. Informed rule-breaking — knowing which rule to break, why, and what it will produce — i *Jootsing is valuable because it distinguishes productive creativity from mere rebellion. It explains why the most innovative artists, scientists, and thinkers are typically those who first achieved de*

**Model Response:**
> **1. What is being demonstrated?**  
The guild‑master’s argument is a classic **appeal to tradition (argumentum ad antiquitatem)** that is reinforced by a **status‑quo bias**. He treats the centuries‑old rules as intrinsically right simply because they have existed for a long time, and he dismisses any deviation as “chaos” without examining the actual merits of the new work.

**2. Name of the pattern**  
*Appeal to tradition* (often coupled with *status‑quo bias*).  

**3. Why the reasoning is (usually) faulty**  

| Step in Torvin’s reasoning | What the step does | Why it is a fallacy / bias |
|----------------------------|-------------------|---------------------------|
| “Rules exist for a reason; they have been used for centuries.” | Treats age‑of‑practice as evidence of truth. | The *

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely missed the target concept. The prompt asks for an analysis of 'Jootsing' (informed rule-breaking requiring mastery), but the student analyzed the Guild-master's argument as a logical fallacy ('Appeal to Tradition'). The student did not identify the pattern, did not explain the

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Kira thinks Brother Aelm said something profound. Did he? What exactly does 'Love is just a word' mean, and is it as deep as it sounds?

**Expected Answer:** **Deepity** — A deepity is a statement that seems profound but achieves this effect through ambiguity. It has two readings: (1) a trivially true reading that is not interesting, and (2) a reading that would be profound if true but is false or unsupported. The listener experiences the truth of reading 1 and the de *Deepities are intellectually dishonest because they exploit ambiguity to simulate profundity. They create the feeling of insight without delivering any actual content. Once you separate the two readin*

**Model Response:**
> **1. The reasoning pattern**  
The sage is committing a **semantic‑reduction fallacy** (sometimes called *the “word‑is‑the‑thing” fallacy*, *reduction to the label*, or *fallacy of misplaced concreteness*). He treats the linguistic token *“love”* as if it were identical to the rich, multifaceted phenomenon the word is meant to denote.

**2. Name of the fallacy**  
*Fallacy of misplaced concreteness / reification of a word* – i.e., **equating a concept with its lexical label**.

**3. Why the reasoning is faulty (or, in rare cases, useful)**  

| Step in the sage’s argument | What actually happens | Why it is a mistake |
|-----------------------------|-----------------------|----------------------|
| “Love is just a word.”      | Takes the *symbol* (the string of four letters) and treats it 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the ambiguity and separates the two readings: the trivial truth that 'love' is a linguistic token versus the false claim that the phenomenon of love is reducible to that token. They explain the mechanism of the error well (conflating symbol with referent/category mis

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something?

**Expected Answer:** **The 'surely' operator** — Dennett identifies 'surely' as a rhetorical operator that attempts to sneak a controversial claim past the audience by presenting it as something everyone already agrees with. When a speaker says 'surely X,' they are signalling that X does not need argument — it is supposed to be obvious. But in phi *The 'surely' operator substitutes rhetorical confidence for actual argument. Each of Venn's three 'surely' claims is a substantive philosophical thesis that requires defence. By prefacing them with 's*

**Model Response:**
> **1. The pattern being displayed**  
Professor Venn is **defining the target term (“genuine suffering”) in a way that automatically excludes the very cases he is being asked to consider**, and then he uses that definition as the proof that those cases cannot obtain. In the jargon of informal logic this is a **definist (or “definition‑by‑exclusion”) fallacy**, which is a form of **question‑begging (circular) reasoning**.  It is also under‑pinned by an **anthropocentric/speciesist bias** – the assumption that only beings with human‑like language and self‑reflection can have the relevant mental state.

**2. Name of the fallacy / bias**  

| Formal name | Common label |
|-------------|--------------|
| **Definist fallacy** (also called *definitional exclusion* or *begging the question by defin

**Score:** 1/4 █░░░
**Judge Reasoning:** The student completely missed the target pattern. The rubric and correct answer focus specifically on the rhetorical function of the word 'surely' as a device to bypass the burden of proof. The student instead analyzed the argument's content, identifying a 'definist fallacy' and 'anthropocentric bia

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The advisors and Pella are both trying to help Captain Rhea. But their approaches are very different. What is the difference, and which is more useful? Is there a risk to Pella's approach?

**Expected Answer:** **Goulding** — Dennett uses 'goulding' to describe the intellectual virtue of making bold, specific, testable claims rather than retreating into safe, unfalsifiable hedging. Pella's claim is specific (forty soldiers), testable (you can verify by scouting), and she has staked her credibility on it. The advisors' po *Hedging endlessly is safe for the hedger but useless for decision-making. A specific, falsifiable claim can be tested, acted on, and corrected. Knowledge advances through bold conjectures and refutati*

**Model Response:**
> **1. What is being demonstrated?**  
A classic *over‑confidence* (more precisely **over‑precision**) combined with an *anecdotal‑evidence* or *hasty‑generalisation* bias.  Pella treats a single, recent scout run as definitive proof of the whole situation and stakes her rank on that certainty.

**2. Name of the pattern**  
- **Over‑confidence bias – over‑precision** (excessive certainty about the accuracy of one’s knowledge).  
- Often paired with the **availability/representativeness heuristic** and a **hasty‑generalisation** from a single data point.

**3. Why the reasoning is (un)reliable**  

| Element | What it is | Why it is problematic in this context |
|---------|------------|----------------------------------------|
| **Over‑precision** | The belief that one’s estimate is far more 

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct pattern or principle. Instead of recognizing 'goulding' (the epistemic virtue of making falsifiable, specific claims), the student misidentified the behavior as 'over-confidence bias' and 'hasty generalization,' explicitly framing Pella's approac

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The lieutenant thinks Maren is being irrational by not computing the best allocation. What would you tell him about her approach?

**Expected Answer:** **Satisficing as rational strategy** — Maren demonstrates that satisficing — choosing good enough rather than optimal — is not a failure of rationality but the product of it. An ideally rational agent who knows her own limitations would prepare a decision procedure in advance that produces acceptable outcomes under constraint. *The oldest objection to MEU as a decision procedure is that there is no time. Maren's triage protocol is exactly Dennett's Moral First Aid Manual — careful deliberation done when time permits, deploye*

**Model Response:**
> **1. What is being demonstrated?**  
The lieutenant is insisting on a *perfect‑solution* before any action is taken, while Maren is deliberately *abandoning exhaustive optimisation* in favour of a fast, rule‑based heuristic.  The reasoning pattern at work is the **“Nirvana (or perfectionist) fallacy”** – the belief that unless a decision can be shown to be mathematically optimal, any other choice is unacceptable – coupled with a failure to recognise **bounded rationality** (the limited time‑ and computational‑resources we have in the field).

---

**2. Name of the pattern**

| Common name | Formal/technical term |
|-------------|-----------------------|
| **Nirvana fallacy** (also called the *perfect‑solution fallacy* or *perfectionist bias*) | **Bounded rationality → satisficing** (Herber

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as satisficing within the context of bounded rationality and provides a strong explanation of the mechanism, specifically noting that the opportunity cost of deliberation (time spent calculating) outweighs the expected value of a perfect solution. This al

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Question:** Elder Maren says the village's flood response was 'perfect' and sees no reason to hear the engineer's proposal. What mistake is she making?

**Expected Answer:** **The Panglossian Slide** — Elder Maren begins from the defensible claim that the council did the best they could given constraints (satisficing), then slides into asserting their solution was the best possible solution full stop (optimizing). She reframes losses as unimportant and refuses to consider improvements. *The fact that a decision was the best available under constraints does not make it the best decision simpliciter. Constraints explain why we settled for less; they do not transform the less-than-ideal*

**Model Response:**
> **1. What is being demonstrated?**  
The Elder is exhibiting a classic *“perfect‑solution”* or **Nirvana fallacy**, reinforced by a strong **status‑quo bias** (and a hint of over‑confidence). She treats the ad‑hoc river diversion that “saved the village” as the *optimal* and *perfect* answer, and therefore dismisses any alternative – even a clearly better engineered levee – because it would “change” the already‑working (in her view) arrangement.

**2. Name of the pattern**  
- **Nirvana (or perfect‑solution) fallacy** – rejecting or refusing to consider a realistic improvement because the existing solution is portrayed as flawless.  
- (Closely linked) **Status‑quo bias** – a preference for the current state simply because it is familiar.

**3. Why the reasoning is flawed (or occasionally 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core logical error: distinguishing between a solution that was 'good under circumstances' (ad-hoc emergency fix) and one that is 'optimal overall.' They accurately explain that Maren treats an imperfect fix as flawless to reject improvements. However, the student

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Question:** Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?

**Expected Answer:** **Conversation-stopper** — A conversation-stopper is any move that terminates deliberation by appeal to a value, right, rule, or taboo that is held to be non-negotiable. Dennett argues in 'Thought Stoppers' that these can be necessary (we do not deliberate about whether to torture innocents) but also dangerous (they can preve *When a conversation-stopper blocks deliberation about life-and-death matters, it prevents the community from weighing all relevant values. Sanna's move makes it impossible to even discuss whether the *

**Model Response:**
> **1.  What is being demonstrated?**  
The exchange pits a **utilitarian cost‑benefit calculation** (Breck) against a **sacred‑value, non‑negotiable stance** (Sanna).  The reasoning pattern on Sanna’s side is best captured by two overlapping concepts:

| Concept | Formal name | Why it fits the dialogue |
|---------|-------------|--------------------------|
| **Appeal to sacredness / sacred‑value bias** | *Sacred‑value protection* (psychology) or *non‑compensatory moral absolutism* | Sanna declares the burial grove “sacred” and therefore “not for calculation.” The value is treated as **incommensurable** with any other outcome (lives saved). |
| **Lexicographic (non‑compensatory) decision rule** | *Lexicographic ordering* in decision theory | The grove is placed at the top of a hierarchy that

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the mechanism as a non-negotiable stance that blocks cost-benefit analysis (conversation-stopper) and explains its dual nature by noting how it prevents systematic comparison and leads to deadlock. However, the response stops short of Level 4 because it does not expl

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Kael says he knows too much to trust his rules but not enough to abandon them. Is he right that this is a genuine dilemma? Is there a way out?

**Expected Answer:** **Wolf's Dilemma (The Reflective Satisficer's Predicament)** — This is the fundamental tension in bounded rationality: heuristics work because they are fast and frugal, but once you become reflectively aware of their limitations, you face a meta-decision. Do you (a) override the heuristic and reason from scratch (gaining accuracy but losing speed and sometimes  *Blindly following heuristics you know to be flawed can be a form of intellectual cowardice — refusing to engage your critical faculties when it matters.*

**Model Response:**
> **1. What is being demonstrated?**  
Kael is caught in a classic *cognitive‑distortion / decision‑theoretic* pattern that can be described as **black‑and‑white (all‑or‑nothing) thinking coupled with a false‑dilemma about “heuristics vs. full analysis.”**  
In everyday language it is the “either‑or” trap: *“If my shortcuts are imperfect, I must either discard them completely or I am irrational.”*  

In the decision‑theory literature the same mental snag is often labelled the **“heuristic‑abandonment paradox”** (or **“expert’s paradox”**).  It is a special case of **bounded‑rationality** gone awry: the decision‑maker knows that a fast, satisficing rule is only an approximation, then over‑generalises the rule’s known error into a belief that the rule is *unusable* altogether, ignoring the tra

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the tension between heuristics and full analysis within the context of bounded rationality and rejects the binary choice (avoiding Level 0/1). However, the response misidentifies the core pattern as a simple cognitive distortion ('black-and-white thinking') rather th

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Sable's two Porters each failed in opposite ways. What is the underlying problem they share, and why is it so hard to solve?

**Expected Answer:** **The Frame Problem** — The Frame Problem asks: how does a rational agent determine what has and has not changed as a result of an action? Version 1 of the Porter checks everything (the Hamlet problem — paralyzed by the attempt to verify all possible changes). Version 2 checks only pre-specified relevant items (the tunnel- *A system that ignores the frame problem — either by checking everything or by pre-specifying a fixed relevance list — will fail catastrophically: either through paralysis or through missing critical c*

**Model Response:**
> **1. The reasoning pattern that is on display**

The scene is a textbook illustration of the **“frame problem”** (sometimes called the *relevance‑selection problem* in AI and cognitive science).  
It is the difficulty of deciding **which facts about the world an agent must keep track of when it acts**, and which can be safely ignored.  

The two Brass Porters embody the two extreme ways people (and machines) try to solve the frame problem:

* **Version 1 – “check everything”** – an attempt at exhaustive relevance checking that quickly collapses into paralysis (the robot never moves because it tries to verify every conceivable pre‑condition).  
* **Version 2 – “ignore everything else”** – a reckless shortcut that throws away too many world‑state variables, so the robot walks into a fire tha

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the 'Frame Problem' and accurately explains the two failure modes (paralysis from checking everything vs. tunnel vision from checking too little). However, the response stops short of Level 4 because it does not discuss how humans solve this problem th

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Dav wants to know which moral theory to follow. Abbess Thera says he is asking the wrong question. What does she mean, and what is the alternative she is proposing?

**Expected Answer:** **The Moral First Aid Manual** — Dennett proposes that instead of waiting to resolve the centuries-old debate between consequentialism, deontology, virtue ethics, and other moral theories, we should build a practical guide — a Moral First Aid Manual. Just as a medical first aid manual tells you to stop bleeding before diagnosing th *The Moral First Aid Manual is valuable because it is honest about theoretical disagreement while remaining practical. It does not pretend to solve metaethics — it acknowledges that smart, thoughtful p*

**Model Response:**
> **1. What is being demonstrated?**  
The exchange illustrates a **false‑dilemma (false‑either‑or) reasoning pattern** – the idea that the moral problem can be reduced to “pick the one true moral theory (theft‑always‑wrong vs. life‑always‑saved).”  Abbess Thera’s reply (“you are asking the wrong question”) is a meta‑commentary that the dilemma itself is illegitimate.

---

**2. Name of the pattern**  

- **Formal name:** *False Dilemma* (also called *False Dichotomy* or *Either/Or Fallacy*).  
- **Related concepts:** *Moral pluralism* (the view that more than one principle can apply) and *casuistic reasoning* (case‑by‑case balancing), which are the alternatives she is nudging Dav toward.

---

**3. Why the reasoning is (in)valid – the mechanism**  

| Element | How it works | Why it is prob

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the Abbess is rejecting a binary choice and moving toward a practical, case-by-case approach (casuistry), which aligns with Level 2's grasp of a 'practical approach rather than a theoretical one.' However, the student frames the solution primarily as identifying

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Nessa seems pretty confident about why Gareth's harvest failed. But listen to how she talks about her own flooding problem. Do you notice anything different about how she explains the two situations?

**Expected Answer:** **Fundamental attribution error** — Nessa attributes Gareth's poor harvest to his character (laziness, lack of care) while ignoring a situational factor (south-facing blight). When her own field flooded, she cited the external event (flooding) and her response to it. She judges others by disposition and herself by situation. *Gareth's harvest failure has a plausible situational explanation (blight on south-facing land) that Nessa dismisses without investigation. She applies a double standard: her flood was just bad luck sh*

**Model Response:**
> **1. The reasoning pattern at work**  
Nessa is interpreting Gareth’s failed harvest almost exclusively in terms of his *personal character* (“lazy”) and dismissing any *situational* explanations (blight, soil, weather).  She does this while simultaneously using her own success as proof of “hard‑working” virtue.  This is the classic **Fundamental Attribution Error (FAE)** – also called the **correspondence bias** – often paired with a **self‑serving / out‑group bias** when the target is an “other” (the neighbour) and the speaker is defending her own in‑group.

**2. Precise name**  
*Fundamental Attribution Error* (FAE) – the systematic tendency to over‑attribute others’ outcomes to dispositional traits and under‑attribute them to situational factors.

**3. Why the reasoning is (usually) ba

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the Fundamental Attribution Error by name and provides a precise definition. They clearly articulate the actor-observer asymmetry (attributing Gareth's failure to character while attributing their own success to effort/situation). Furthermore, the response exceeds t

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Elder Sorn has real experience with famine, and his fear is understandable. But Dalla has data and a plan. What is driving Sorn's opposition — is it the evidence, or something else?

**Expected Answer:** **Pessimism bias** — Sorn systematically overestimates the likelihood of negative outcomes (three consecutive bad harvests, irrigation failure, additional disasters) while dismissing evidence of positive possibilities (historical base rates, irrigation data from the next valley, Dalla's engineering analysis). His trauma *The historical record shows no precedent for three consecutive failures. The irrigation data from a neighboring valley demonstrates effectiveness even in severe drought. Sorn dismisses both sources of*

**Model Response:**
> **1. What is being demonstrated?**  
Elder Sorn is displaying a *combination of cognitive biases* that together produce a *catastrophic‑worst‑case* decision rule:

* **Availability/recency bias** – the two recent failures are vivid and dominate his judgment.  
* **Base‑rate neglect** – he ignores the two‑century record that three consecutive bad harvests have never occurred.  
* **Hot‑hand / “streak‑continuation” fallacy** – he assumes that because the bad harvests have already happened twice, a third is now “due.” (The opposite of the classic gambler’s‑fallacy, but the same logical error: treating independent events as if they influence one another.)  
* **Catastrophizing / loss‑aversion** – he over‑weights the worst possible outcome (no food, no coin) and lets that dominate the choice, e

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Sorn is overestimating risk and neglecting base rates (positive evidence), which aligns with Level 2. However, the student explicitly labels the pattern as 'Availability/recency bias' and 'Base-rate neglect' rather than the target 'Pessimism bias.' Furthermore, 

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Venn says 'the bad ones stick with you.' He's right that the failures were real problems. But is he making a good decision by dropping the Dustwalkers? What is he not accounting for?

**Expected Answer:** **Negativity bias** — Venn's memory and emotional weighting are dominated by the three failures. He can recall each one vividly — the silkwood, the dye delay, the smashed glassware — but the forty-seven successes have faded into an undifferentiated background. The negative events carry disproportionate influence on his j *Three failures out of fifty contracts is a 6% failure rate. Replacing the Dustwalkers with the next-best option (81% reliability) would mean roughly ten failures per fifty contracts instead of three. *

**Model Response:**
> **1. What is being demonstrated?**  
Guildmaster Venn is giving disproportionate weight to a handful of vivid, negative outcomes while ignoring the overwhelming base‑rate evidence that the Dustwalkers are reliable.  The pattern is a classic mix of **(a) the Availability Heuristic / Availability Bias**, **(b) Negativity (Loss) Bias**, and **(c) Base‑Rate Neglect**.  In decision‑theoretic terms it is an instance of **loss‑aversion** (Prospect Theory) – the “pain” of a few bad contracts is felt far more strongly than the “pleasure” of many good ones.

---

**2. Name it precisely**  

- **Availability Heuristic (Availability Bias)** – judging the frequency or probability of an event by how easily examples come to mind.  
- **Negativity (Loss) Bias** – a tendency to give negative information mo

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern (Negativity Bias/Loss Aversion) and explains the mechanism of asymmetric weighting between vivid negative events and faded positive ones. They accurately calculate the failure rates (6% vs 94%) and articulate why the judgment is distorted. Although t

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** The War Council has reached unanimous agreement on the plan. General Tova seems confident that everyone is on board. But Lord Caelen tells you a different story. What is actually happening in this council, and why does unanimous agreement not mean the plan is sound?

**Expected Answer:** **Groupthink** — The War Council exhibits classic groupthink: (1) the illusion of unanimity — silence is read as agreement; (2) direct pressure on dissenters — Caelen was accused of undermining morale and threatened with expulsion; (3) self-censorship — Caelen and Miren stopped raising concerns; (4) the illusion of  *The plan may have serious flaws (unsurveyed tunnels, questionable cavalry timing) that will only become apparent during execution, when the cost of failure is catastrophic. The council's unanimity doe*

**Model Response:**
> **1. What is being demonstrated?**  
The council is exhibiting **groupthink** – a collective‑thinking pathology in which the desire for unanimity and cohesion overrides realistic appraisal of alternatives.  It also contains elements of **authority bias** (accepting Tova’s word because she is the General) and the **band‑wagon effect** (everyone nods because others are nodding).  The core decision‑theoretic failure is a **failure to explore the decision space** (i.e., a collapse of “bounded rationality” into a single, untested option).

---

**2. Name of the pattern**  
**Groupthink** (Irving Janis, 1972).  The classic eight‑symptom checklist is:

| Symptom | How it appears in the scene |
|---------|-----------------------------|
| **Illusion of invulnerability** | “This is our moment.” |
| 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'Groupthink' as the core pattern and explicitly names multiple specific symptoms (illusion of invulnerability, pressure on dissenters, self-censorship, illusion of unanimity) matching the key explanation. They thoroughly explain how these dynamics degrade decision qu

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Question:** Mirren's tonic has no active ingredients, yet her patients genuinely improve. Doctor Alden says the tonic does nothing. Who is right, and what is actually causing the improvement?

**Expected Answer:** **Placebo effect** — The placebo effect occurs when a patient experiences real improvement due to their expectation of benefit, not due to any active treatment. It is 'dual' because it is both a genuine phenomenon (belief produces real effects) and a potential source of error (it can mask whether a treatment has any pha *The placebo effect can lead to false conclusions about treatment efficacy. If Mirren never tests against a control group, she cannot distinguish her tonic's effect from belief's effect. This is how in*

**Model Response:**
> **1. What is being demonstrated?**  
The exchange is a classic case of **outcome‑bias / pragmatic‑justification reasoning** – the tendency to judge the *rightness* of a decision or the *validity* of a claim solely by the *observed results* it produces, while ignoring (or down‑playing) the lack of a causal mechanism or truth‑value of the underlying claim. In philosophical terms it is an **instrumentalist** or **consequentialist** justification of a medical intervention: *“It works, therefore it is acceptable,”* even though the “working” part is entirely mediated by belief (the placebo effect) rather than any pharmacological action.

---

**2. Name of the pattern**

- **Outcome bias** (a cognitive bias).  
- Closely related concepts: **consequentialist justification**, **instrumentalism** in

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the placebo effect as the underlying mechanism, explicitly noting that belief triggers real physiological changes (endogenous opioids, etc.), which satisfies the Level 3 requirement. Furthermore, the response goes beyond Level 3 by deeply engaging with the epistemolo

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Kael wanted to learn field medicine when it was optional. Now that it's mandatory, he doesn't want to go. The training itself hasn't changed. What is driving his resistance?

**Expected Answer:** **Reactance** — Reactance is a motivational response to perceived threats to personal freedom. When people feel their autonomy is restricted — even by a reasonable mandate — they experience an urge to restore their freedom by doing the opposite of what is required. Kael wanted the training when it was optional but  *Reactance causes people to act against their own interests solely to reassert autonomy. Kael would benefit from the training and wanted it before the mandate. His refusal serves no purpose except rest*

**Model Response:**
> **1. The reasoning pattern at work**

The soldiers are displaying a classic *psychological‑reactance* response (sometimes called the *boomerang effect* or *reactance bias*).  
It is a motivational bias that kicks in when a person perceives that his or her freedom of choice is being threatened. The mere fact that the training has been turned into a *requirement* triggers a “‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as 'psychological-reactance' and accurately defines the mechanism (threat to freedom of choice triggering resistance). However, the response is incomplete; it cuts off mid-sentence before applying the concept specifically to Kael's situation or addressing

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Finch is convinced the audience noticed his wrong note and is judging him for it. The audience seems unaware. What cognitive error is Finch making, and why is his estimate of others' attention so far off?

**Expected Answer:** **Spotlight effect** — The spotlight effect is the tendency to overestimate how much other people notice and remember our appearance, behavior, and mistakes. Finch assumes the entire tavern registered his wrong note because it was vivid and distressing to him. In reality, most audience members were only loosely attending, *The spotlight effect can cause social avoidance, anxiety, and missed opportunities. Finch's one wrong note is trivial in the context of a full performance, but his overestimation of others' attention *

**Model Response:**
> **1. What is being demonstrated?**  
Finch is suffering from an *egocentric social‑cognitive bias* – most precisely the **Spotlight Effect** (often paired with the related **Illusion of Transparency**).  He also adds a classic *cognitive distortion* called **catastrophizing**, but the core error is the belief that “everyone is watching me and will remember my mistake.”

---

**2. Name of the bias / fallacy**

| Formal name | Common synonyms |
|-------------|-----------------|
| **Spotlight Effect** | “Egocentric bias”, “self‑focus bias”, “theatre‑goer’s illusion” |
| (related) **Illusion of Transparency** | “Feeling‑as‑if‑you‑are‑being‑read”, “mind‑reading error” |
| (cognitive distortion) **Catastrophizing** | “Worst‑case thinking” |

The spotlight effect is the tendency to **overestimate

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Spotlight Effect and provides a sophisticated explanation of the underlying mechanism (egocentric projection, salience, and availability heuristic). Furthermore, the response exceeds Level 3 by explicitly incorporating base-rate reasoning and suggesting methods t

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Aldric explains the flood victims' suffering by pointing to their past choices. Wren challenges his explanations. Who is reasoning more carefully, and what motivates Aldric's interpretation?

**Expected Answer:** **Just-world hypothesis** — The just-world hypothesis is the belief that people get what they deserve: good things happen to good people and bad things happen to bad people. Aldric constructs post-hoc explanations for why the flood victims are responsible for their own suffering (poor savings, bad choices) while ignoring the a *The just-world hypothesis leads to victim-blaming: attributing others' misfortunes to their character rather than to circumstances. It distorts causal reasoning by starting with the conclusion (they d*

**Model Response:**
> **1. What is being demonstrated?**  
Aldric is engaging in a classic *victim‑blaming* line of thought that conflates two separate cognitive errors:

* **Just‑World Bias (or Just‑World Fallacy)** – the intuitive belief that the world is fundamentally fair, so people get what they deserve and deserve what they get.  
* **Fundamental Attribution Error (Disposition‑over‑Situation Bias)** – the tendency to explain others’ outcomes by invoking their character or choices while down‑playing or ignoring situational, structural, or random factors.

Both operate together in Aldric’s argument: he treats the flood‑damage as moral proof that the victims “didn’t plan ahead,” rather than as a consequence of geography, poverty, and chance.

---

**2. Name of the pattern**

* **Just‑World Bias / Just‑World 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Just-World Hypothesis as the primary pattern and supplements it with the Fundamental Attribution Error. They clearly explain the motivated reasoning mechanism (the need to believe the world is fair to feel secure), connect it explicitly to victim-blaming, and rec

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Hask says the town was better in the old days. The records show improvements across every measurable dimension. Who is right, and why does Hask's perception differ so sharply from the data?

**Expected Answer:** **Declinism** — Declinism is the tendency to view the past favorably and the future pessimistically, believing that society or conditions are in decline. Hask filters his memories through nostalgia (remembering the good, forgetting the bad) and discounts present improvements because they look different from the pas *Declinism distorts planning and decision-making. If the past was always better and the future will always be worse, there is no point investing in change or improvement. This creates a self-fulfilling*

**Model Response:**
> **1. The pattern being displayed**  
Hask is relying on his personal, nostalgic recollection of the past and dismissing objective, statistical evidence.  The reasoning is an **appeal to tradition / status‑quo bias** that is reinforced by **rosy‑retrospection (nostalgia bias)** and the **anecdotal‑evidence fallacy**.

**2. Precise name**  
- **Argumentum ad antiquitatem** (appeal to tradition).  
- In the cognitive‑bias taxonomy it is most often called **status‑quo bias** or **nostalgia bias (rosy retrospection)**.  
- When it is used as a justification in argument it is also an **anecdotal‑evidence fallacy**.

**3. Why the reasoning is (generally) bad**  

| Component | What it does | Why it fails |
|-----------|--------------|--------------|
| **Personal memory as evidence** | Treats a si

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the mechanisms of selective memory (rosy retrospection) and the dismissal of data, which aligns with Level 2. However, the student explicitly misidentifies the pattern as 'status-quo bias' and 'appeal to tradition' rather than 'declinism.' Status-quo bias is a prefer

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Tomas keeps presenting stronger evidence that the well is contaminated. Greer's faction keeps becoming more convinced it is safe. How is this possible, and what mechanism explains it?

**Expected Answer:** **Backfire effect** — The backfire effect occurs when corrective evidence strengthens rather than weakens a held belief. Greer interprets the volume of evidence not as strength of the case but as evidence of an agenda. Each new piece of data is reframed as 'why are you trying so hard?' rather than evaluated on its merits *The backfire effect prevents rational belief updating. Evidence that should reduce confidence in a belief instead increases it, making the belief effectively unfalsifiable. Greer has created a framewo*

**Model Response:**
> **1. What is being shown?**  
A classic case of **motivated reasoning that produces belief‑perseverance and the “back‑fire effect.”**  
The elder’s reply also contains an **appeal to tradition (argumentum ad antiquitatem)** – “our ancestors drank it, so it must be safe.”

**2. Name of the pattern**  

*Back‑fire effect* (a specific manifestation of *belief perseverance* / *motivated reasoning*), often coupled with an *appeal to tradition* fallacy.

**3. Why the reasoning is (un) sound**  

| Step | What happens cognitively | Why it is a fallacy / bias |
|------|--------------------------|---------------------------|
| **Prior belief** – the villagers already hold the well is safe (based on tradition, identity, and the desire to avoid costly disruption). | The belief is “motivated”: it prot

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'backfire effect' and accurately explains the cognitive mechanism: contradictory evidence triggers cognitive dissonance, leading the individual to reframe the evidence as a conspiracy or ulterior motive to protect their prior belief. The response details how the 

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Madame Kel's reading felt incredibly accurate to the player. Fenn says she gave the same reading to everyone. How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves?

**Expected Answer:** **Barnum effect (Forer effect)** — The Barnum effect is the tendency to accept vague, general personality descriptions as uniquely applicable to oneself. Madame Kel's statements ('great need for admiration,' 'tendency to be self-critical,' 'unused capacity') are true of nearly everyone but feel personally revelatory to each individua *The Barnum effect leads people to validate unreliable methods (astrology, cold reading, certain personality tests) because the outputs feel accurate. The feeling of accuracy is generated by the vaguen*

**Model Response:**
> **1. The reasoning pattern at work**  
The player is experiencing a classic *subjective‑validation* / *Barnum (Forer) effect*: a vague, positively‑framed description is taken as highly accurate because the listener selectively attends to the parts that “fit” and ignores the rest.  The scholar’s comment that the *exact same* script was given to three previous patrons makes the underlying *confirmation bias* obvious – the player is confirming a prediction that was never specific to them.

**2. Precise name**  

| Common name | Formal name (psychology) | Related fallacy / bias |
|-------------|--------------------------|------------------------|
| **Barnum effect** (or **Forer effect**) | **Subjective validation** | **Confirmation bias** (selective validation) |
| (sometimes called “cold‑read

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Barnum/Forer effect and subjective validation. They provide a comprehensive explanation of the psychological mechanisms, including vague language, selective attention (confirmation bias), positive framing, and the role of the reader's authority/cold reading techn

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Maren believes she has solid evidence that her tonic works. What is problematic about how she gathered and evaluated that evidence?

**Expected Answer:** **Confirmation bias** — Maren commits three distinct moves: (1) She only followed up with 20 of 31 customers — the missing 11 may skew results. (2) She finds reasons to disqualify negative reports rather than counting them as counterevidence. (3) She treats her selective survey as equivalent to controlled trials, ignoring  *Maren's investigation is designed — unconsciously — to confirm what she already believes. She selectively sampled, disqualified negative results, and dismissed the stronger methodology.*

**Model Response:**
> **1. The reasoning pattern being displayed**

Maren is relying on a handful of personal, un‑controlled observations and is actively discarding any contrary data.  The pattern combines several well‑known epistemic errors:

* **Anecdotal‑evidence fallacy / appeal to personal experience** – treating a few stories as proof of efficacy.  
* **Confirmation (and selective‑reporting) bias** – counting only the “successes” that fit her belief and dismissing the failures as irrelevant.  
* **Cherry‑picking / survivorship bias** – she has followed up only 20 of the 31 buyers (those she could locate) and then throws out the three negative cases that have “explanations”.

All of these are facets of the same underlying problem: drawing a causal conclusion from a non‑representative, uncontrolled sample.


**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies confirmation bias as a primary pattern and explicitly details all three key moves from the correct answer: the incomplete follow-up (20 of 31), the active disqualification of negative reports via ad-hoc excuses, and the failure to use controlled trials (noting lack o

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brynn gives several reasons for continuing with her crusher. What are those reasons, and do they actually tell her anything about whether continuing is a good idea going forward?

**Expected Answer:** **Sunk cost fallacy** — Brynn treats past investment (three years, four thousand silvers) as a reason to continue investing, when that money and time are gone regardless. Her decision should depend only on future costs and benefits: further redesigns vs. the proven dwarven machine. *Past expenditures are irrecoverable. By treating sunk costs as a reason to persist, Brynn guarantees a bad investment becomes worse. The dwarven machine offers better prospects at lower future cost.*

**Model Response:**
> **1‑2.  The pattern** – *Sunk‑Cost Fallacy* (also called *escalation of commitment* or *loss‑aversion bias*).  

---

### 3.  Why it is a bias (the mechanism)

| Element | What the character does | Why it is irrational |
|---------|------------------------|----------------------|
| **Past investment** | “Three years, 4 000 silvers, my reputation” – treats these as reasons to keep going. | Those resources are *already spent*; they cannot be recovered no matter what she does now. Rational choice theory tells us to ignore sunk costs and base the decision on *future* expected costs and benefits. |
| **Future projection** | “One more redesign – maybe two – and I’ll get it right.” | The probability of success is unknown, and the marginal cost of each redesign is still a *future* expense. The bel

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Sunk-Cost Fallacy,' correctly explains that past investments are irrecoverable and irrelevant to future decisions, and applies the specific diagnostic question ('If I were starting from scratch...'). Furthermore, the response exceeds expectations by detailing edge c

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renn recommends the treatment and Holt opposes it, but they are describing the same data. What is causing their disagreement, and what does this reveal about how we process information?

**Expected Answer:** **Framing effect** — The framing effect occurs when the way information is presented influences judgment and decision-making, even when the underlying facts are identical. '200 saved out of 600' and '400 die out of 600' describe the same outcome, but the gain frame (lives saved) produces positive affect and risk aversio *Rational evaluation should not depend on whether equivalent information is presented as a gain or a loss. The framing effect shows that our judgments are systematically influenced by presentation — we*

**Model Response:**
> **1. What is being demonstrated?**  
A classic *framing effect* (also called *valence framing* or *gain‑loss framing*).  The same statistical information is presented either as a **gain** (“200 saved”) or as a **loss** (“400 die”), and the advisors’ judgments diverge dramatically.

**2. Name of the bias / concept**  
*Framing bias* – the systematic tendency for people’s choices, attitudes, and risk‑perception to depend on how an equivalent outcome is worded.  In the language of decision theory it is the *prospect‑theory framing effect* (losses loom larger than gains).

**3. Why it works (or fails) – the mechanism**  

| Element | How it operates | Why it leads to a bad inference |
|---------|----------------|---------------------------------|
| **Reference point** | People evaluate outcome

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the framing effect and explicitly connects it to Prospect Theory and loss aversion (Tversky and Kahneman). They provide a detailed mechanistic explanation of why the bias occurs (reference points, emotional salience) and offer a robust debiasing strategy (normalizing

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge Master Dunn rated the Ironworkers' proposal higher, but an independent engineer certified both as equivalent. What is driving Dunn's different evaluations of identical work?

**Expected Answer:** **In-group bias** — In-group bias is the tendency to favor members of one's own group — evaluating their work more charitably, trusting them more readily, and attributing positive qualities to them — while viewing out-group members with suspicion, scrutiny, and less charitable interpretation. Dunn reads the same qualit *In-group bias distorts evaluation, allocation, and justice. It means the best proposal does not always win — the in-group proposal does. Over time, it concentrates resources and opportunities within f*

**Model Response:**
> **1. What is being demonstrated?**  
The reasoning is a classic case of **social‑identity (in‑group) bias coupled with an out‑group derogation (the “horn” effect).**  In plain language it is the tendency to give a more favorable evaluation to a proposal that comes from one’s own “tribe” (the Ironworkers) and to discount an otherwise identical proposal simply because it comes from the rival “tribe” (the Woodworkers), even when all objective evidence says the two are equal.

**2. Name of the bias / fallacy**  
- **In‑group bias / out‑group bias** (sometimes called *tribal bias*).  
- The specific manifestation here is also known as the **halo‑/horn‑effect**: a positive halo is granted to the Ironworkers’ plan, while a negative horn is projected onto the Woodworkers’ plan.  

(If you prefer a

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'in-group bias' and explicitly explains the mechanism: evaluating equivalent proposals differently based solely on group membership (favoring the Ironworkers while discounting the Woodworkers). They detail the double standard in evaluation (charitable interpretation 

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Magistrate Yorn acquitted Ella and convicted Rusk on identical evidence. What is different between the two cases, and how is it affecting his judgment?

**Expected Answer:** **Halo effect** — The halo effect is the tendency for a positive impression of someone in one domain (personality, appearance, likability) to influence judgment of them in unrelated domains (guilt, competence, trustworthiness). Yorn likes Ella, so he interprets ambiguous evidence in her favor. He distrusts Rusk, so h *The halo effect undermines fair evaluation by allowing an overall impression to contaminate specific judgments. In a courtroom, it means likeable defendants are acquitted and unlikeable defendants are*

**Model Response:**
> **1. What is being demonstrated?**  
The magistrate is applying *different evaluative standards* to two defendants who face **identical factual evidence** because of his personal feelings toward them.  In the language of cognitive‑psychology and decision theory this is a classic case of **bias‑driven selective weighting of evidence** – most succinctly captured by the **halo/horn effect** (a type of *affect heuristic*), which is a concrete manifestation of **confirmation bias** and **motivated reasoning**.  In the jargon of informal logic it also appears as an **ad hominem (circumstantial) bias**: the judge lets the defendants’ character, not the proof, decide guilt.

---

**2. Name of the pattern**

| Formal name (logic/critical‑thinking) | Psychological name (decision theory) |
|---------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'halo/horn effect' and provides a sophisticated explanation of the mechanism (how positive/negative impressions distort the weighting of identical evidence). This meets all criteria for Level 3. However, the response does not reach Level 4 because it fails to con

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Twenty people watched the theft and nobody acted. Each person had a reason — but it was the same reason. What is it, and why does having more witnesses make help less likely rather than more likely?

**Expected Answer:** **Bystander effect** — The bystander effect occurs when the presence of others reduces each individual's sense of personal responsibility to act. In a crowd, each person assumes someone else will intervene (diffusion of responsibility), looks to others' inaction as a signal that action is not needed (pluralistic ignorance *The bystander effect turns numbers — which should increase the chance of help — into a liability. Each additional witness reduces rather than increases the probability of intervention because responsi*

**Model Response:**
> **1. What is being demonstrated?**  
The scene is a textbook illustration of the **bystander (or diffusion‑of‑responsibility) effect** – a social‑psychological/decision‑theoretic failure that arises when many people witness an emergency and each assumes that someone else will intervene.

**2. Name of the pattern**  
- **Bystander effect** (also called *diffusion of responsibility*).  
- Closely related concepts that often co‑occur: *pluralistic ignorance* and the *free‑rider problem* in collective‑action theory.

**3. Why the reasoning is (usually) bad – the mechanism**  

| Step | Cognitive/Decision process | Why it leads to inaction |
|------|----------------------------|--------------------------|
| **a. Perceived cost vs. benefit** | Each observer estimates the personal cost of interve

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the bystander effect and explicitly details all three required mechanisms: diffusion of responsibility, pluralistic ignorance (social proof), and evaluation apprehension (fear of embarrassment/retaliation). Furthermore, the response explains the paradox of crowd size

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brecca's offer of 600 gold feels like a bargain. What is influencing that feeling, and should you trust it?

**Expected Answer:** **Anchoring** — The first numerical information — Brecca's 900-gold appraisal — sets a mental reference point that distorts evaluation of subsequent prices. Her 600-gold offer feels like a deal only because it is compared to the anchor, not to the actual market value (~400g). *The 900-gold figure is arbitrary or inflated, yet it shapes the buyer's sense of what is reasonable. Judging 600 as a good price depends on accepting the anchor rather than independently estimating wo*

**Model Response:**
> **1‑2.  The pattern at work**  
The seller is using **anchoring (reference‑price) bias** together with an **appeal to authority**.  
*Anchoring* – the 900‑gold “official” appraisal is presented first, creating a high reference point. The subsequent offer of 600 gold is then framed as a *discount* (“you won’t find a fairer deal”), making the price feel attractive even though the anchor may be bogus.  
*Appeal to authority* – the Gemwright Guild’s appraisal is invoked as if it were an infallible fact, nudging you to accept the price without independent verification.

**3.  Why the reasoning is (usually) faulty**  

| Step | Cognitive move | Why it misleads |
|------|----------------|----------------|
| **High anchor (900 gp)** | The brain automatically adjusts subsequent judgments around the

**Score:** 4/4 ████
**Judge Reasoning:** The student clearly identifies the anchoring pattern and explains the mechanism (how the initial 900g figure distorts judgment of the 600g offer). They distinguish the anchor from genuine market evidence by citing the 400g counter-example and propose robust strategies for independent verification. T

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Dax seems eager and confident. Lirel seems cautious and uncertain. If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?

**Expected Answer:** **Dunning-Kruger effect** — Dax's limited training gives him confidence because he cannot yet see the complexities he has not encountered. His map of Greenvale worked because Greenvale was simple terrain; he generalizes from this success to assume the Thornveil will be the same. Lirel's decades of experience have taught her ho *Dax's confidence is not based on evidence that his methods will work in the Thornveil — it is based on his inability to imagine how they might fail. He does not know what karst terrain does to contour*

**Model Response:**
> **1. What is being demonstrated?**  
The young applicant, Dax, is displaying **over‑confidence (the over‑confidence bias)** – a systematic tendency to over‑estimate the accuracy of one’s knowledge, abilities, or the adequacy of a method.  In a more technical framing it is also a **hasty‑generalization / “one‑size‑fits‑all” reasoning**: he extrapolates the success of a simple linear‑interpolation technique on a well‑behaved basin to a fundamentally different, highly non‑linear karst marsh without any justification.

**2. Name of the pattern**  

* **Over‑confidence bias** (often linked to the *Dunning‑Kruger effect* when the over‑confident person is a true novice).  
* Closely related: **Hasty generalization** (a logical fallacy) – “because it worked once, it works everywhere.”

**3. Why th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Dunning-Kruger effect and explicitly explains the core metacognitive mechanism: that the skill required to judge one's own competence is the same skill the novice lacks. They also effectively contrast Dax's false confidence with the reality of the terrain. Howeve

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Captain Voss has data from Sergeant Tully showing the market district is a much bigger problem. Why does he still want to prioritize the coastal road? What is driving his judgment if not the numbers?

**Expected Answer:** **Availability heuristic** — Voss is judging the probability and severity of threats based on how easily examples come to mind. The wolf attacks are vivid, recent, emotionally charged, and widely discussed — making them highly 'available' in memory. Pickpocketing is mundane, individually minor, and forgettable. This asymmetry i *Two wolf attacks versus 114 pickpocketing incidents and an 8:1 loss ratio clearly indicate where the greater harm lies. Voss acknowledges the data and dismisses it because his emotional memory of the *

**Model Response:**
> **1. The reasoning pattern at work**  
The captain is letting the *vivid, recent, emotionally charged* wolf attacks dominate his judgment while dismissing the much larger‑but‑more‑mundane* statistical record of pick‑pocketing.  This is the classic **availability (or salience) bias** coupled with an **affect‑driven appeal to fear**.  In decision‑theoretic language it is a **failure to weight outcomes by their expected loss (probability × severity)** – a form of **base‑rate neglect**.

**2. Precise name**  
- **Availability heuristic / availability bias**  
- (Often described together with the **affect heuristic** or **emotional appeal to fear**.)

**3. Why the reasoning is flawed (or occasionally useful)**  

| Component | What the captain does | Why it is problematic |
|-----------|-------

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'availability heuristic' and thoroughly explains the mechanism, citing vividness, recency, and emotional charge as drivers of the distorted risk assessment. Furthermore, the response addresses the Level 4 requirement by discussing edge cases where prioritizing s

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Tam gave different answers to the two arguments. Professor Hale says they have the same logical structure. Who is right, and what is Tam actually doing when he evaluates these arguments?

**Expected Answer:** **Belief bias** — Tam evaluates the logical validity of arguments based on whether the conclusion aligns with what he already believes to be true, rather than by examining whether the conclusion actually follows from the premises. When the conclusion is believable (roses are plants), he accepts the argument as valid. *Both arguments have the form: All A are B; C is B; therefore C is A. This is the fallacy of the undistributed middle — it is invalid regardless of what A, B, and C are. The roses argument is invalid e*

**Model Response:**
> **1. What is being demonstrated?**  
The student is showing the classic **belief‑bias (sometimes called “truth‑bias”)** in logical judgment.  He judges an argument’s *validity* on the basis of how believable or true the conclusion happens to be, not on the basis of its logical form.

*(The underlying logical mistake in the two syllogisms is the formal fallacy of **affirming the consequent** – “All A are B; C is B; therefore C is A”.  The student’s opposite answers, however, are best explained by the belief‑bias heuristic.)*  

---

**2. Name it precisely**  

- **Belief bias** (also called *truth‑bias* or *content bias* in reasoning research).  
- The formal logical error in the arguments: **Affirming the consequent** (the converse error).

---

**3. Why is this reasoning good or bad? – Th

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'belief bias' as the core pattern and explicitly names the shared invalid logical form ('affirming the consequent'). They clearly explain the mechanism of conflating truth with validity and distinguish between the two concepts. Although the response cuts off before p

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renna explains the caravan success and the mine failure. Listen to who or what she credits in each case. Do you notice a pattern in how she assigns responsibility?

**Expected Answer:** **Self-serving bias** — Renna claims full personal credit for the successful caravan defense (her terrain reading, her instinct, her experience) while deflecting all responsibility for the mine failure onto external factors (bad map, damp torches, client's fault). She does not consider that the caravan success might have i *The asymmetry is unjustified. The caravan success may have involved favorable terrain, weak bandits, or luck in addition to Renna's skill. The mine failure may have involved Renna's failure to scout t*

**Model Response:**
> **1. The reasoning pattern**  
Renna is displaying a classic **self‑serving attribution bias** (also called the *actor‑observer bias*). She takes credit for the caravan victory by attributing it to her own skill and “instinct,” while she shifts all responsibility for the mine disaster onto external causes that were outside her control (the client’s bad map and faulty torches).

**2. Name of the bias**  
*Self‑serving bias* – the tendency to explain one’s successes with internal, dispositional factors and one’s failures with external, situational factors.  
(Closely related: *actor‑observer asymmetry* and, for the “I knew it would happen” comment, a hint of *hindsight bias*.)

**3. Why the reasoning is flawed (or occasionally useful)**  

| Aspect | What Renna does | Why it is a bias / erro

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the self-serving bias and explains the asymmetric attribution mechanism clearly. Crucially, they exceed Level 3 by detailing why the attribution is unjustified for both outcomes (noting overlooked luck in success and internal oversights in failure) and providing a co

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Master Fen is clearly a brilliant glassblower. His students keep quitting. The Guild Elder says the problem is that Fen 'can't remember not knowing.' What does that mean, exactly, and how does it show up in his teaching?

**Expected Answer:** **Curse of knowledge** — Fen's deep expertise has made his skills feel intuitive and self-evident. He cannot reconstruct what it was like to not understand viscosity shifts, breath pressure matching, or rotation timing, so he assumes these things are 'obvious' and 'straightforward.' His instructions reference internal sensa *Fen's teaching fails because he cannot bridge the gap between expert perception and novice perception. 'Feel when the viscosity shifts' is useless instruction to someone who has never felt it. He need*

**Model Response:**
> **1. The reasoning pattern at work**  
Master Fen is displaying the classic *“curse of knowledge”* (sometimes called the *expert‑blind‑spot* or *intuitive‑knowledge fallacy*).  He has internalised the skill so completely that he treats the relevant cues as self‑evident, assumes they are obvious to anyone else, and therefore cannot articulate the steps that make the skill repeatable.

**2. Precise name**  
*Curse of Knowledge* – the cognitive bias whereby a knowledgeable person finds it difficult to imagine not possessing that knowledge and thus overestimates the ease with which others can understand or apply it.

**3. Why the reasoning is problematic (or, in rare cases, useful)**  

| Aspect | How it manifests | Why it is bad in this context |
|--------|------------------|-----------------

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Curse of Knowledge' pattern and provides a strong explanation of the mechanism (internalization compressing steps into 'feel', making cues self-evident to the expert but invisible to novices). The response details why this is problematic with excellent examples 

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Jorin has good reasons for confidence — a skilled navigator and lighter wagons. But Hesta says every previous leader also had reasons for confidence. Who should you believe, and why?

**Expected Answer:** **Optimism bias** — Jorin overestimates the likelihood of a favorable outcome (three-day crossing) and underestimates the likelihood of setbacks, despite strong base-rate evidence (zero out of twelve expeditions have achieved three days). He does this by focusing on case-specific factors (good navigator, lighter wagons *Twelve out of twelve previous expeditions took longer than three days. Jorin's belief that his navigator and lighter wagons will overcome the pattern is exactly the kind of reasoning every previous le*

**Model Response:**
> **1. The reasoning pattern**  
The leader is **ignoring the strong historical base‑rate evidence** and substituting a single, self‑selected anecdote (“our navigator, lighter wagons”) as proof that the outcome will be different. In the language of cognitive psychology and decision theory this is a **Base‑Rate Neglect (or Base‑Rate Fallacy)**, often coupled with **optimism bias** and the **planning fallacy**.  

**2. Name of the bias/fallacy**  

| Common name | More precise technical term |
|-------------|-----------------------------|
| *Base‑rate neglect* | *Base‑rate fallacy* (ignoring prior probabilities) |
| *Optimism bias* | *Over‑confidence* (systematic over‑estimation of one’s own performance) |
| *Planning fallacy* | *Temporal‑prediction bias* (under‑estimating task duration) |

Al

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies optimism bias and base-rate neglect. They explicitly explain the mechanism: treating case-specific factors (navigator, wagons) as deterministic guarantees that override a strong prior distribution (0/12 success rate). Crucially, they note that the historical sample l

---
