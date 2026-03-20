# Benchmark Report: gpt-oss-20b Reasoning Capacity Assessment

**Date:** 2026-03-20
**Subject Model:** openai/gpt-oss-20b (MindRouter, University of Idaho campus HPC)
**Judge Model:** qwen/qwen3.5-400b (MindRouter)
**Corpus:** 167 hand-crafted anchor examples across 5 content tracks

## 1. Executive Summary

We assessed gpt-oss-20b's capacity for critical thinking, logic, decision theory,
game theory, and cognitive bias recognition using 167 hand-crafted benchmark items
drawn from the Good Thinking Bot training corpus. Each item was evaluated in three
modes: open-ended identification, multiple-choice classification, and full explanation.

**Key findings:**

- **Identify mode: 2.62/4.00** — the model can generally recognize reasoning patterns
  but often fails to fully articulate the underlying mechanism.
- **Explain mode: 2.47/4.00** — similar to identify, with slightly lower scores when
  a complete mechanistic explanation is required.
- **Classify mode: 0.10/4.00** — near-total failure at selecting the correct taxonomy
  code from a 5-option list, likely due to instruction-following limitations rather than
  comprehension deficits.
- The model is strongest on **common fallacies** (ad hominem, straw man, gambler's fallacy)
  and weakest on **Dennett's thinking tools** and **argument structure fundamentals** —
  precisely the areas where domain-specific LoRA training should have the largest impact.

## 2. Methodology

### 2.1 The Anchor Corpus

The benchmark uses 167 hand-crafted anchor examples from the Good Thinking Bot
training corpus. Each anchor represents one taxonomy code and includes:

- A **scenario** set in an RPG game world (NPC dialogue, town council debates, etc.)
- A **structure** block with the correct pattern name, description, and formal analysis
- An **assessment** block with a Socratic identification prompt and a 0–4 rubric
- Metadata: taxonomy code, track, pattern type (good_tool / bad_thinking / dual),
  and difficulty tier (drill / what_if / puzzle)

The 167 codes span five tracks:

- **cognitive_biases**: 24 codes
- **decision_theory**: 31 codes
- **dennett_tools**: 14 codes
- **game_theory**: 18 codes
- **logic_critical_thinking**: 65 codes
- **microeconomics**: 15 codes

### 2.2 Evaluation Modes

Each anchor was presented to the subject model in three modes:

| Mode | Prompt | Scoring | What It Measures |
|------|--------|---------|------------------|
| **Identify** | Scenario + identification question | Judge model scores 0–4 against rubric | Can the model recognize the pattern? |
| **Classify** | Scenario + 5 taxonomy code options | Auto-scored (exact match = 4, else 0) | Can the model select the correct label? |
| **Explain** | Scenario + request for full analysis | Judge model scores 0–4 against rubric | Can the model explain the mechanism? |

### 2.3 Models

- **Subject:** `openai/gpt-oss-20b` — a 20-billion-parameter open-source model
  hosted on MindRouter (University of Idaho campus HPC). This is the model we are
  considering as a base for LoRA fine-tuning.
- **Judge:** `qwen/qwen3.5-400b` — a 400-billion-parameter model used to score
  open-ended responses against the rubric. The judge sees the correct answer,
  the rubric, and the subject's response.
- Both models were accessed via MindRouter's OpenAI-compatible API with
  temperature=0.3 and thinking mode disabled.

### 2.4 Scoring

The rubric for each item uses a 0–4 scale:

| Level | Description |
|-------|-------------|
| 0 | No recognition of the pattern |
| 1 | Vague awareness that something is off |
| 2 | Identifies the pattern but cannot explain the mechanism |
| 3 | Names and explains the pattern correctly |
| 4 | Full mastery: explains, names edge cases, connects to related concepts |

## 3. Overall Results

| Mode | Mean Score | n | Score Distribution (0/1/2/3/4) |
|------|-----------|---|-------------------------------|
| identify | 2.62 | 167 | 2 / 12 / 55 / 77 / 21 |
| classify | 0.10 | 167 | 163 / 0 / 0 / 0 / 4 |
| explain | 2.47 | 167 | 16 / 16 / 43 / 58 / 34 |

## 4. Results by Track

| Track | Identify | Explain | Classify |
|-------|----------|---------|----------|
| cognitive_biases | 2.62 (n=24) | 3.12 (n=24) | 0.00 (n=24) |
| decision_theory | 2.81 (n=31) | 2.58 (n=31) | 0.39 (n=31) |
| dennett_tools | 1.93 (n=14) | 1.29 (n=14) | 0.00 (n=14) |
| game_theory | 2.28 (n=18) | 2.00 (n=18) | 0.22 (n=18) |
| logic_critical_thinking | 2.72 (n=65) | 2.65 (n=65) | 0.00 (n=65) |
| microeconomics | 2.80 (n=15) | 2.07 (n=15) | 0.00 (n=15) |

**Discussion:** Dennett's thinking tools are the hardest category across all modes
(identify: 1.93, explain: 1.29). These are specialized philosophical concepts
(satisficing, Panglossian Slide, conversation-stoppers) that the model has likely
seen less frequently in pretraining. Cognitive biases score well in explain mode (3.12),
suggesting the model has good coverage of these concepts from popular science writing.

## 5. Results by Difficulty Tier

| Tier | Identify | Explain | Classify |
|------|----------|---------|----------|
| drill | 2.73 (n=112) | 2.73 (n=112) | 0.04 (n=112) |
| what_if | 2.39 (n=49) | 1.98 (n=49) | 0.08 (n=49) |
| puzzle | 2.33 (n=6) | 1.50 (n=6) | 1.33 (n=6) |

Performance degrades monotonically with difficulty, as expected. Puzzle-tier items
(genuine philosophical engagement) are hardest, with explain-mode scores dropping to 1.50.

## 6. Results by Pattern Type

| Pattern Type | Identify | Explain | Classify |
|--------------|----------|---------|----------|
| good_tool | 2.49 (n=65) | 1.78 (n=65) | 0.00 (n=65) |
| bad_thinking | 2.73 (n=74) | 3.12 (n=74) | 0.05 (n=74) |
| dual | 2.61 (n=28) | 2.32 (n=28) | 0.43 (n=28) |

The model is consistently better at recognizing **bad_thinking** patterns (fallacies,
biases) than **good_tool** patterns (valid reasoning strategies). In explain mode,
the gap is 3.12 vs 1.78 — nearly a full rubric level. This suggests the model has
learned to detect errors more readily than to articulate what makes reasoning *correct*.

## 7. Notable Findings

### 7.1 Classify Mode Failure

The near-zero classify score (0.10/4.00) is striking given reasonable identify/explain
performance. Inspection reveals the model rarely outputs a bare taxonomy code as
instructed. Instead, it tends to produce explanatory text even when asked for just
a code. This is an instruction-following limitation, not a comprehension deficit —
the model clearly understands the patterns (identify: 2.62) but cannot conform to
the constrained output format. This is a known weakness of smaller models and a
potential target for fine-tuning.

### 7.2 Dennett Tools as Hardest Category

Dennett's thinking tools (satisficing, Panglossian Slide, conversation-stoppers,
Rapoport's Rules, deepities, the 'surely' operator, Jootsing, Goulding) consistently
score lowest. These concepts are drawn from Dennett's *Intuition Pumps* and Bert's
lecture notes — specialized philosophical vocabulary unlikely to appear frequently in
pretraining data. This makes them ideal candidates for LoRA training: the gap between
current and target performance is largest here.

### 7.3 Bad Thinking > Good Tool Gap

Across all modes, the model performs better on bad_thinking patterns (fallacies,
biases) than on good_tool patterns (valid reasoning strategies). This likely reflects
a pretraining distribution where fallacy detection is well-represented (debate,
fact-checking, critical thinking courses) while positive reasoning strategies are
less commonly labeled or discussed.

### 7.4 Strongest Individual Codes

The following codes received perfect scores (4/4) in at least one mode:

- **B1.5: Minimax regret** (score=4 in: explain, identify)
- **A7.3: Tu quoque** (score=4 in: explain, identify)
- **A5.1: Denying the antecedent** (score=4 in: explain, identify)
- **A5.2: Affirming the consequent** (score=4 in: explain, identify)
- **A7.6: Appeal to authority** (score=4 in: explain, identify)
- **A7.11: Personal incredulity** (score=4 in: explain, identify)
- **A7.16: Anecdotal evidence** (score=4 in: explain, identify)
- **A8.2: Base rate neglect** (score=4 in: explain, identify)
- **A8.6: Hasty generalization** (score=4 in: explain, identify)
- **A10.1: Name calling / labeling** (score=4 in: explain, identify)
- **A10.2: Repetition** (score=4 in: explain, identify)
- **E1.21: Framing effect** (score=4 in: explain, identify)
- **E1.2: Confirmation bias** (score=4 in: identify)
- **B1.3: Maximax** (score=4 in: identify)
- **A9.3: The fallacy fallacy** (score=4 in: identify)

## 8. Implications for Training

These results establish a **pre-training baseline** for gpt-oss-20b. The benchmark
should be re-run after each LoRA training iteration to measure improvement.

**Priority areas for LoRA fine-tuning (ordered by expected impact):**

1. **Dennett's thinking tools** (current: 1.29–1.93) — largest gap, most novel concepts
2. **Good_tool pattern explanation** (current: 1.78) — model needs to learn to articulate
   *why* reasoning is correct, not just detect errors
3. **Argument structure fundamentals** (A1.x, current: many at 0) — basic skills the
   model should master first
4. **Instruction following for classification** (current: 0.10) — fine-tuning on
   constrained output formats
5. **Puzzle-tier reasoning** (current: 1.50) — genuine philosophical engagement
   requires deeper understanding

**Expected post-training targets:**

| Mode | Current | Target |
|------|---------|--------|
| Identify | 2.62 | 3.50+ |
| Explain | 2.47 | 3.20+ |
| Classify | 0.10 | 3.00+ |

## Appendix A: Full Results — Identify Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The bartender wants to know: which of these speakers is actually giving an argument? How can you tell?

**Expected Answer:** **Identifying arguments via indicator words** — An argument is a set of premises that attempt to provide a reason that a conclusion is true. The sailor's statement is a chronological narrative with no premises or conclusion — it describes a sequence of events. The dockworker's statement is an argument: 'since' is a premise indicator linking two p *Recognizing arguments requires checking for premise and conclusion indicators and verifying that statements are being offered as reasons for another statement. The dockworker uses 'since' to connect e*

**Model Response:**
> We need to analyze scenario: bartender asks whether anyone is actually giving a reason to believe something. The sailor says: "First I loaded the cargo, and then I secured the rigging. After that I checked the manifest." The dockworker says: "The ship is not seaworthy, since the hull planks are rotting and the bilge pump is broken." The bartender asks: "Is anyone actually giving me a reason to believe something, or are you all just telling stories?" So bartender wants to know which speaker is giving an argument. The sailor's statements are a series of actions, but no claim or conclusion. He is not giving a reason to believe something. The dockworker is making a claim: the ship is not seaworthy, and gives reasons: hull planks rotting, bilge pump broken. So the dockworker is giving an argume

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the dockworker as the one giving an argument and the sailor as merely narrating events. They accurately distinguish between a claim with supporting reasons and a sequence of actions. However, the response fails to reach Level 3 because it does not explicitly identify

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Theodora just gave testimony with several claims. Which is her main conclusion? Which statements are premises? Is there a statement that serves as both a conclusion and a premise?

**Expected Answer:** **Identifying premises, conclusions, and intermediate conclusions** — Theodora's argument has a layered structure. 'The fact that... is shown by the fact that...' reverses the usual order — the conclusion comes first, then the premise. The intermediate conclusion is that the royal household is contributing to the obesity problem (supported by premises about larger por *Identifying premises and conclusions requires attending to indicator phrases. 'The fact that X is shown by the fact that Y' means Y is the premise and X is the conclusion — the reverse of reading orde*

**Model Response:**
> We need to identify main conclusion, premises, and any statement that is both conclusion and premise. Also analyze reasoning pattern, fallacy, bias, principle.

Let's parse the testimony:

1. "The fact that obesity has become a problem in the kingdom is shown by the fact that obesity rates have risen significantly over the past four decades." This is a claim that obesity is a problem, supported by evidence of rising rates. So it's a premise supporting the claim that obesity is a problem.

2. "Moreover, since the royal kitchens have been serving larger portions, and larger portions lead to overeating, the royal household is contributing to this problem." This is a premise: larger portions -> overeating -> contributes to obesity problem.

3. "Therefore, the king should reform the royal kitch

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the main conclusion, all premises, and the intermediate conclusion ('obesity has become a problem'), explicitly noting its dual role as both a conclusion of a sub-argument and a premise for the main argument. They accurately explain the dependency structure. However,

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe hands you Captain Voss's statement. Rewrite it in standard form: numbered premises with the conclusion last. Does the argument have any sub-arguments?

**Expected Answer:** **Standard form reconstruction** — Standard form lists premises as numbered statements with the conclusion last, marked with 'Therefore.' Voss's argument has two sub-arguments: one eliminating the sewer escape (premises about the locked grate and no scent trail), and one concluding the cart escape (premises about it being the only al *Standard form makes the logical structure visible. It separates premises from conclusions, reveals sub-arguments, and shows which premises support which conclusions. Voss's conversational version buri*

**Model Response:**
> We need to rewrite the statement in standard form: premises numbered, conclusion last. Identify sub-arguments. Also analyze reasoning pattern, fallacy, bias, principle.

First parse the statement: "Well obviously the prisoner couldn't have escaped through the sewage pipes because the grate was still locked, and besides, the dogs didn't pick up any scent trail from the cell to the drain. So he must have hidden in the back of the delivery cart, because that is the only other way out, and the cart left the compound unexamined at dawn."

We need to identify premises:

1. The prisoner couldn't have escaped through the sewage pipes because the grate was still locked.
2. The dogs didn't pick up any scent trail from the cell to the drain.
3. Therefore, he must have hidden in the back of the delive

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the main conclusion and lists the premises in a numbered format, satisfying Level 1. They also explicitly recognize the existence of sub-arguments (e.g., '1+2 => Sewer escape impossible') and attempt to structure the logic hierarchically, which pushes the score to Le

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Aldric has asked you to reconstruct Rosmund's argument in its strongest form. What is she really trying to argue, underneath the hyperbole? And why is the heckler's response unfair?

**Expected Answer:** **Principle of charity in argument reconstruction** — The principle of charity states that when reconstructing an argument, you should try to make it as strong as possible. Rosmund's literal words contain overstatements ('cheap garbage,' 'every tanner will go broke'), but her core argument has a defensible structure: if cheaper foreign imports undercut *The heckler attacked Rosmund's weakest phrasing ('cheap garbage') rather than her strongest argument. Charitable reconstruction reveals that her core concern — price competition threatening local live*

**Model Response:**
> We need to reconstruct Rosmund's argument in strongest form: underlying argument is that importing foreign leather would harm local tanners' livelihoods, potentially causing economic harm to the guild and town. She is advocating for a ban on imports to protect local industry. She is concerned about competition and market share. The heckler's response is unfair because it attacks her hyperbolic language and misrepresents her argument, focusing on a specific example (Kordian hides) and dismissing her argument as invalid. The heckler commits ad hominem or straw man? Actually heckler says "She said foreign leather is garbage — clearly she has not examined the Kordian hides, which are excellent quality. Her argument collapses!" This is a straw man: misrepresenting her argument as "foreign leath

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core economic logic (protecting livelihoods/market share) and recognizes the need to separate hyperbole from the underlying argument, which pushes it beyond Level 1. However, the response fails to reach Level 3 because it lacks a clear, cohesive explanation of *w

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Councillor Drava's conclusion says the state 'should' do something. Her premise says something 'is' the case. What is missing? What assumption would you need to add to make this argument valid? And once you add it, does the argument actually work?

**Expected Answer:** **Missing premises and the is-ought gap** — Drava's argument has a descriptive premise (children of unmarried couples often have emotional difficulties) and a normative conclusion (the state should discourage this). Any argument with a normative conclusion requires at least one normative premise — this is the is-ought gap. The missing premise *Identifying missing premises — especially normative ones — reveals the hidden assumptions on which an argument depends. By making Drava's argument valid through supplying premises, we can see more cle*

**Model Response:**
> We need to analyze the scenario: Councillor Drava says: "Since children raised by unmarried couples often have emotional difficulties, the state should discourage unmarried couples from raising children." The premise: "children raised by unmarried couples often have emotional difficulties" (descriptive). The conclusion: "the state should discourage unmarried couples from raising children" (normative). The missing assumption is that there is a causal link or that emotional difficulties are caused by being raised by unmarried couples, or that the state has a duty to prevent harm, or that discouraging will reduce emotional difficulties. Also maybe the assumption that the state has the authority or that discouraging is effective. The argument is a non sequitur: descriptive to normative. The mi

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core 'is-ought' gap, explicitly noting the jump from a descriptive premise to a normative conclusion and supplying the necessary missing normative premise (state duty to prevent harm). They also successfully identify the missing causal/efficacy assumption (that d

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The chronicler has two statements about the bridge collapse. Which one is an argument and which is an explanation? How can you tell the difference?

**Expected Answer:** **Distinguishing arguments from explanations** — Arguments try to convince you that a conclusion is true — the conclusion is in dispute. Explanations show why something already accepted as true occurred — the conclusion is taken for granted. The engineer's statement is an explanation: no one disputes that the bridge collapsed; the engineer explain *The key test is whether the 'conclusion' is already taken for granted or is in dispute. 'Because' can introduce either an explanation or a premise — context determines which. The engineer uses 'becaus*

**Model Response:**
> **Which is which?**

| Statement | Type | Why it fits that type |
|-----------|------|-----------------------|
| **A – “The bridge collapsed because the support beams were eaten by termites and the recent flooding weakened the foundation.”** | **Explanation** | It is a *causal description*: it tells *why* the bridge collapsed. It uses the causal connective *because* and ends

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies Statement A as an explanation and begins to articulate the reason (it is a causal description telling 'why'). However, the response is incomplete: it fails to identify or analyze Statement B (the argument), and the explanation for Statement A cuts off mid-sentence. B

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The guild master wants you to diagram this argument. Which premises must work together (linked) and which support the conclusion independently (convergent)?

**Expected Answer:** **Linked vs convergent premises and sub-arguments** — In argument diagramming, linked premises are premises that must work together to support a conclusion — neither is sufficient alone. Convergent premises independently support the same conclusion. In this argument, premises 1 and 2 are linked: 'Wanda had her pant leg rolled up' only supports 'she bik *Diagramming reveals that this argument has two independent lines of evidence converging on the same conclusion. If premise 3 turned out to be false (Bob was mistaken), the argument from premises 1 and*

**Model Response:**
> We need to answer: Which premises must work together (linked) and which support the conclusion independently (convergent)? The scenario: premises 1: Wanda arrived at work with her right pant leg rolled up. Premise 2: Cyclists often roll up their right pant leg to keep it from catching in the chain. Premise 3: Bob saw Wanda riding her bike towards work at 7:45. Conclusion: Therefore, Wanda rode her bike to work today.

Premise 1 and 2 together: The rolled-up pant leg is a sign that she might be a cyclist. Alone, each doesn't prove she rode a bike. But together they support the inference that she was a cyclist. Premise 3 supports the conclusion independently: Bob saw her riding a bike. So the argument structure: Premise 3 is a direct support for conclusion; Premises 1 and 2 are linked to sup

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that premises 1 and 2 are linked (neither works alone) and that premise 3 is an independent, convergent support. They accurately describe the diagrammatic structure (1+2 leading to a sub-inference, 3 leading directly to the conclusion). However, they do not reach Lev

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Gruff seems very confident in dismissing Mira's proposal. But look at what he actually says — does he address any of the specifics of her plan?

**Expected Answer:** **Name calling / labeling** — Gruff substitutes negative labels for substantive engagement. Rather than challenging the aqueduct's costs, feasibility, or projected benefits, he attaches dismissive terms to Mira and her proposal. The labels carry negative connotations that encourage the audience to reject the proposal based on em *Labels are not arguments. Calling someone a 'dreamer' does not address whether their cost estimates are accurate, their engineering is sound, or the water supply is needed. The labels function as a su*

**Model Response:**
> **What Gruff is doing**

Gruff’s reply is a classic *ad hominem* attack.  
Instead of weighing the numbers, the timeline, or the projected water‑flow that Mira just laid out, he attacks Mira herself:

* “Typical ivory‑tower nonsense from an out‑of‑touch academic.”  
* “Mira is a dreamer, an idealist who has never had to make a payroll or balance a ledger.”  
* “Why should hardworking merchants fund the fantasies of a starry‑eyed theorist?”

He is dismissing the proposal on the basis of *who* produced it, not on *what* it says. That is a **genetic fallacy** (rejecting an idea because of its source) and a **circumstantial ad hominem** (arguing that because Mira’s circumstances make her “out‑of‑touch,” her ideas are invalid).

**Why it’s a fallacy**

1. **No engagement with the content** – He

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as an ad hominem attack involving negative labels ('dreamer', 'ivory-tower'). They explicitly explain the mechanism: Gruff dismisses the proposal based on the source ('who produced it') rather than engaging with the substantive evidence ('numbers, timelin

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The villager says Brother Constant must be right because he has been saying it all week. Is that good reasoning?

**Expected Answer:** **Repetition / illusory truth effect** — Brother Constant repeats the claim 'The Old Bridge is cursed' with rhythmic insistence, without providing evidence. The illusory truth effect is a well-documented cognitive phenomenon: repeated exposure to a statement increases the feeling of familiarity, which people mistake for truth. The villager *Repetition is not evidence. A claim does not become more true by being stated more often. The feeling of familiarity that repetition produces is a cognitive artifact, not a rational basis for belief. *

**Model Response:**
> **No – it’s a classic fallacy.**  
The villager is reasoning that because Brother Constant has repeated the claim “the Old Bridge is cursed” for seven nights, the claim must be true. That is the *argument from repetition* (also called the **argumentum ad nauseam** or the *repetition fallacy*).  

### Why it’s a fallacy

1. **No evidence is provided.**  
   Repeating a statement does not supply any new data, evidence, or logical support for it. The truth of a claim depends on facts, evidence, or a sound argument, not on how many times it’s been said.

2. **It relies on the *illusory truth effect*.**  
   Human cognition is biased toward believing things that are repeated, because repetition makes a statement feel familiar and therefore more credible. This is a well‑documented cognitive bias

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern (repetition) and explicitly names the underlying mechanism (illusory truth effect), explaining the confusion between familiarity and truth. Furthermore, the response exceeds the Level 3 requirements by discussing how this mechanism is exploited in propaga

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge has been presented with clear evidence of slag dumping. Does his response address that evidence?

**Expected Answer:** **Whataboutism / red herring** — Forge responds to a specific accusation (slag dumping) by redirecting attention to unrelated issues (tannery hides, farm pesticides). The other problems may be real, but they do not address the evidence against Forge. This is a red herring: introducing an irrelevant topic to divert attention from th *The existence of other polluters does not change whether Forge dumped slag in the river. Each accusation should be evaluated on its own evidence. Forge's response addresses neither the witnesses, the *

**Model Response:**
> **Short answer:**  
No – Forge’s reply does not address the evidence that he dumped slag into the river. Instead, he diverts the discussion by pointing to other polluters, which is a classic *tu quoque* (appeal to hypocrisy) or *red‑herring* fallacy.

---

### Step‑by‑step reasoning

| Step | What happens | Why it matters |
|------|--------------|----------------|
| 1. **Evidence is presented** | Three witnesses, water‑sample tests, and dead fish are shown as proof that slag from Forge’s shop entered the river. | This is a clear, factual claim that Forge’s shop is the source of the pollution. |
| 2. **Forge’s reply** | He says, “Why are we talking about my shop when the tannery has been dumping hides for years? And what about the farmers who use fey‑dust pesticides that run off into every 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core pattern (red herring and tu quoque/whataboutism) and clearly explains that Forge diverts attention from the specific evidence without refuting it. However, the response does not reach Level 4 because it fails to articulate the nuance regarding when concerns 

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Steele gave a passionate speech. But did he actually address Councillor Maren's economic analysis?

**Expected Answer:** **Flag-waving / appeal to patriotism** — Steele substitutes an appeal to group identity and patriotic emotion for engagement with the economic argument. He reframes a policy question (will trade lower prices?) as an identity question (are you loyal to Ironvale?). This shuts down cost-benefit analysis by making disagreement feel like betray *Whether trade with Ashford is economically beneficial is a factual question about prices, supply, and demand. It has nothing to do with patriotism or loyalty. Steele's appeal makes evaluating the prop*

**Model Response:**
> **Short answer:**  


**Score:** 0/4 ░░░░
**Judge Reasoning:** The student's response is empty (no short answer provided). Therefore, they demonstrated no recognition of the pattern, mechanism, or any counterpoints, corresponding to Level 0 where the player fails to identify the logical flaw.

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Krul certainly sounds confident. But did he actually respond to any of Wynn's specific points about enrollment data or graduate outcomes?

**Expected Answer:** **Thought-terminating cliche** — Krul deploys a barrage of stock phrases that sound like wisdom but carry no argumentative content. Each cliche is designed to end inquiry rather than advance it: 'It is what it is' implies nothing can or should change; 'if it ain't broke don't fix it' assumes without argument that nothing is broken; *Thought-terminating cliches are compressed assertions that masquerade as wisdom. They shut down inquiry without providing reasons. 'It is what it is' is not an argument — it is a refusal to engage. 'I*

**Model Response:**
> **Short answer:**  
No – Professor Krul never addressed Wynn’s enrollment statistics or graduate‑outcome data. Instead he launched a rhetorical “status‑quo” dismissal that relies on a handful of classic fallacies: an appeal to tradition, a status‑quo bias, and an ad‑hominem

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Krul uses stock phrases ('classic fallacies') instead of addressing the data, which aligns with Level 2. However, the student mislabels the specific mechanism as 'ad-hominem' (which is not present) and fails to explain how these phrases function specifically as 

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** You have the damage report and you have heard both accounts. What is each speaker doing with the facts, and what would an accurate description look like?

**Expected Answer:** **Exaggeration / minimization** — Both speakers distort the significance of the same event in opposite directions. Holt minimizes: 'a few minutes,' 'a couple of lettuce leaves,' 'barely a scratch.' Tess exaggerates: 'destroyed my entire garden,' 'nothing to eat this winter,' 'I will starve.' The actual damage — roughly a third of th *Distorting the magnitude of an event — in either direction — undermines rational assessment. Holt's minimization would lead to inadequate compensation; Tess's exaggeration would lead to disproportiona*

**Model Response:**
> We need to analyze what each speaker is doing with the facts, and what an accurate description would look like. Also identify reasoning pattern, fallacy, bias, principle.

Farmer Holt: downplays damage, says "barely a scratch". He is minimizing. He might be using a minimization or downplaying fallacy, or maybe he's using a "false minimization" or "denial" or "downplaying". He might be using a "bias" like self-serving bias, or "optimistic bias" or "self-serving bias" to protect his reputation. He might also be using a "fallacy of misrepresentation" or "fallacy of equivocation" or "fallacy of incomplete evidence". He is ignoring the actual damage report.

Widow Tess: exaggerates damage, says "destroyed entire garden" and "catastrophe". She is inflating. She might be using a "catastrophizing"

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Holt is minimizing and Tess is exaggerating, and accurately describes the middle ground (moderate damage: 1/3 lettuce, 2 rows of beans). This satisfies Level 3. However, the response fails to reach Level 4 because it does not clearly explain how these distortion

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Harl says he is just asking questions and that we need more study. Is he raising legitimate scientific concerns, or is something else going on?

**Expected Answer:** **Doubt casting / manufacturing uncertainty** — Harl's strategy is not to present counter-evidence but to generate a fog of doubt around existing evidence. He questions calibration without alleging specific errors, raises the specter of conflicts of interest without identifying any, invokes 'some scientists' without naming them or citing studies, *Legitimate scientific skepticism identifies specific methodological flaws and proposes concrete alternatives. Harl does neither. His doubts are generic enough to apply to any study on any topic. If no*

**Model Response:**
> We need to analyze the scenario: Harl is a mine owner. He says he is not a water engineer but has questions about the tests. He asks about calibration, funding, conflict of interest, and that trace minerals might be beneficial. He says we need more study, not rush to judgment. The question: Is he raising legitimate scientific concerns, or is something else going on? We need to think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? Likely he's using a "appeal to doubt" or "argument from ignorance" or "appeal to uncertainty" or "appeal to question authority" or "appeal to lack of evidence" or "appeal to the unknown." He is basically creating doubt about the evidence, which is a classic "appeal to doubt" or "argument from ignorance" or "the fall

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Harl is casting doubt and questioning evidence without providing specific counter-arguments, which aligns with Level 2. However, the response fails to reach Level 3 because it does not clearly articulate the mechanism of 'manufactured uncertainty' versus legitim

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor presents two arguments on stone tablets. Which is valid? Which is sound? Explain your reasoning. If an argument is invalid, provide a counterexample.

**Expected Answer:** **Validity and soundness** — A valid argument is one where the conclusion cannot possibly be false if the premises are true. Soundness = validity + true premises. Tablet A is valid: IF everyone born in France speaks French AND Obama was born in France, THEN he speaks French — the conclusion follows necessarily. But it is unsoun *Understanding validity requires separating the logical structure from the truth of the claims. Many students reject Tablet A because its premises are obviously false — but that is a soundness judgment*

**Model Response:**
> We need to analyze the scenario: two arguments on stone tablets. Tablet A: 1. Everyone born in France can speak French. 2. Barack Obama was born in France. 3. Therefore, Barack Obama can speak French. Tablet B: 1. George was President of the United States. 2. Therefore, George was elected President of the United States.

We need to determine which is valid, which is sound. Also explain reasoning. If invalid, provide counterexample. Also discuss reasoning pattern, fallacy, bias, principle being demonstrated.

We need to think: Validity: argument is logically correct if conclusion follows from premises. Soundness: valid and premises true. Let's evaluate.

Tablet A: Premise 1: "Everyone born in France can speak French." Premise 2: "Barack Obama was born in France." Conclusion: "Barack Obama c

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Tablet A as valid but unsound and Tablet B as invalid. They successfully provide a counterexample for Tablet B (a scenario where George is appointed rather than elected) and clearly explain the distinction between validity (form) and soundness (truth + form). The res

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Translate both sentences into symbolic logic. Then explain: do they mean the same thing? If not, what is the difference?

**Expected Answer:** **Propositional logic connectives and translation** — 'Not both' is the negation of a conjunction: ~(C * I). It is true whenever at least one of the conjuncts is false — Carla could have cake alone, ice cream alone, or neither. 'Neither-nor' is a conjunction of two negations: ~C * ~I. It is true only when both are false — Carla has no cake and no ice c *Correct translation from natural language to symbolic logic requires careful attention to the scope of negation. 'Not both' negates the conjunction as a whole. 'Neither-nor' negates each component sep*

**Model Response:**
> **Translations**

| English sentence | Symbolic form |
|------------------|---------------|
| *Carla will not have both cake and ice‑cream.* | \(\neg(C \land I)\) |
| *Carla will have

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly translated the first sentence ('not both') as ~(C * I), demonstrating an understanding of the scope of negation for that specific case. However, the response is incomplete; the translation for the second sentence ('neither-nor') is missing entirely, and there is no explanation 

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build the truth table for this argument. Is the argument valid? How does the truth table show you?

**Expected Answer:** **Truth table test of validity** — The truth table test works by checking every possible assignment of truth values. An argument is valid if and only if there is no row where all premises are true and the conclusion is false. For this disjunctive syllogism (S v D, ~S, therefore D): with four rows of truth values, the only row where b *The truth table test is a formal method: we can assess validity even without knowing what the argument is about. It is mechanical and objective, unlike the informal test which depends on our ability t*

**Model Response:**
> We need to produce a truth table for the argument: "Either the convict escaped through the sewage pipes or the convict escaped by hiding in the delivery van. The convict did not escape through the sewage pipes. Therefore, the convict escaped by hiding in the delivery van."

So premises: 1) S ∨ D. 2) ¬S. Conclusion: D.

We need to build truth table for S and D. Evaluate premises and conclusion. Determine if whenever premises true, conclusion true. That is validity.

Truth table:

S D | S∨D | ¬S | Premises both true? | Conclusion D | Valid?

We need to check rows where both premises true: S∨D true and ¬S true. That means S is false (¬S true) and D must be true to make S∨D true. So only row where S=F, D=T. In that row, conclusion D is true. So argument is valid. It's modus ponens? Actually it

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the logical form (disjunctive syllogism), sets up the truth table logic, and correctly determines that the only row where premises are true yields a true conclusion, thus proving validity. However, the response fails to reach Level 4 because it lacks a clear, concise

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks: what rule of inference justifies each derived step? Name the rule and explain how it applies.

**Expected Answer:** **Modus ponens and hypothetical syllogism** — Step 4 uses modus ponens (MP): from 'if P then Q' and 'P', derive 'Q'. Step 5 also uses MP: from 'if Q then R' and 'Q', derive 'R'. Step 6 uses hypothetical syllogism (HS): from 'if P then Q' and 'if Q then R', derive 'if P then R'. These are three of the eight basic valid forms of inference. Each p *Inference rules are the building blocks of proofs. MP and HS are two of the most fundamental. MP lets you detach a consequent when you have the antecedent. HS lets you chain conditionals into longer c*

**Model Response:**
> **Step 4 – “The ground is wet”**  
*Rule:* **Modus Ponens**  
*How it works:*  
- Premise 1 gives the implication \(R \rightarrow W\) (“If it is raining, then the ground is wet”).  
- Premise 3 gives the antecedent \(R\) (“It is raining”).  
- Modus Ponens says: from \(P \rightarrow Q\) and \(P\) we may infer \(Q\).  
Thus, from \(R \rightarrow W\) and \(R\) we infer \(W\) – the ground is wet.

---

**Step 5 – “The match will not light”**  
*Rule:* **Modus Ponens** (again)  
*How it works:*  
- Premise 2 gives the implication \(W \rightarrow \lnot L\) (“If the ground is wet, then the match will not light”).  
- Step 4 gives the antecedent \(W\) (“The ground is wet”).  
- Modus Ponens lets us infer the consequent \(\lnot L\).  
Hence, from \(W \rightarrow \lnot L\) and \(W\) we get \(\lnot 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Modus Ponens for steps 4 and 5 and Hypothetical Syllogism for step 6, providing accurate general forms and applications for each. This meets all criteria for Level 3. However, the response does not address invalid look-alikes (affirming the consequent, denying the an

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Construct a proof deriving B v D from the three premises. Name each rule you use. Try working both forward from the premises and backward from the conclusion.

**Expected Answer:** **Constructing natural deduction proofs** — The proof uses constructive dilemma: from P v Q, P->R, Q->S, derive R v S. Working backwards: the conclusion B v D is a disjunction, so ask what rules produce disjunctions. Constructive dilemma does, and it requires a disjunction plus two conditionals — exactly what premises 1-3 provide. Working for *Natural deduction proofs require strategic thinking about which rules to apply and in what order. The backward strategy asks: what rule could produce the conclusion's form? The forward strategy asks: *

**Model Response:**
> We need to produce a proof deriving B v D from premises: 1) A -> B, 2) C -> D, 3) A v C. We need to name each rule used. We can use standard natural deduction rules: Modus Ponens, Disjunction Elimination, Disjunction Introduction, etc. We need to think both forwards and backwards. The question: "What reasoning pattern, fallacy, bias, or principle is being demonstrated here?" The scenario: instructor asks to think both forwards and backwards. This is reminiscent of "proof by cases" or "disjunction elimination" or "constructive dilemma". The pattern is "constructive dilemma" or "disjunctive syllogism"? Actually we have A->B, C->D, and A v C. We want B v D. This is a classic example of the constructive dilemma: (A → B) ∧ (C → D) ∧ (A ∨ C) ⊢ B ∨ D. The rule used is Disjunction Elimination (pro

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the logical validity and constructs a proof using Disjunction Elimination (proof by cases) with subproofs. However, the rubric defines Level 3 as recognizing that 'constructive dilemma applies directly' for a concise, one-step proof. The student explicitly chooses th

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Test the syllogism using Venn diagrams. Then translate 'Nobody loves me but my mother' into categorical form. What are the categories?

**Expected Answer:** **Categorical statements, translation, and Venn diagrams** — Categorical logic deals with four statement types: All S are P (universal affirmative), No S are P (universal negative), Some S are P (particular affirmative), Some S are not P (particular negative). The syllogism 'All H are M, All M are D, therefore All H are D' is valid: the Venn diagram for the t *Categorical logic captures structure within propositions that propositional logic misses. The Venn diagram test is visual and systematic: diagram the premises, then check whether the conclusion is alr*

**Model Response:**
> We need to answer: test the syllogism using Venn diagrams. The syllogism: All humans are mortal. All mortal things die. Therefore, all humans die. That's a classic categorical syllogism: All H are M; All M are D; therefore all H are D. It's valid. Using Venn diagrams: show that the intersection of H and D is all H. So the conclusion holds.

Then translate 'Nobody loves me but my mother' into categorical form. We need to parse the sentence: "Nobody loves me but my mother." Means: The only person who loves me is my mother. So the set of people who love me is exactly {my mother}. In categorical terms: All people who love me are my mother. Or: All X such that X loves me are equal to my mother. But categorical form: All L (people who love me) are M (my mother). But that's weird because M is a s

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the syllogism pattern and validates it using Venn diagrams. However, they struggle with the 'tricky translation' requirement. While they eventually state 'All people who love me are my mother,' they express significant confusion about treating an individual ('my moth

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build truth tables for each pair. Which pairs are logically equivalent? Explain what each equivalence (or non-equivalence) means in plain language.

**Expected Answer:** **Logical equivalence: contraposition and De Morgan's Laws** — Pair 1 (A->B and ~AvB) is equivalent: a conditional says the same thing as the negation of the antecedent or the consequent. Pair 2 (~(A*B) and ~Av~B) is equivalent: this is De Morgan's Law — the negation of a conjunction is a disjunction of negations ('not both' equals 'not-A or not-B'). Pair 3 (A- *Logical equivalence is a powerful tool for simplifying and transforming arguments. De Morgan's Laws let you move between negations of conjunctions and disjunctions of negations. The conditional-as-dis*

**Model Response:**
> We need to answer: Build truth tables for each pair. Which pairs are logically equivalent? Explain each equivalence or non-equivalence in plain language. Also: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning." So we need to discuss the reasoning pattern or fallacy or principle demonstrated by the scenario. The scenario: instructor asks to determine equivalence of logical formulas using truth tables. The pairs: 1) A -> B and ~A v B. 2) ~(A * B) and ~A v ~B. 3) A -> B and B -> A. So we need to analyze equivalence.

Truth tables:

Variables: A, B. For each pair.

Pair 1: A -> B is equivalent to ~A v B. This is a known logical equivalence: implication is equivalent to disjunction of negated antecedent and 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the equivalence status for all three pairs and provides accurate truth table analysis for Pair 3. They also offer plain language explanations for the equivalences and non-equivalence. However, the response fails to reach Level 3 or 4 because the second part of the an

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Which argument is deductive and which is inductive? After learning that Tweets is six feet tall and runs thirty miles per hour, what happens to each argument? Why?

**Expected Answer:** **Deductive vs inductive arguments and defeasibility** — The mathematician's argument is deductive: if the premises are true, the conclusion follows with certainty. Adding new information cannot undermine a valid deductive argument (though it might challenge a premise). The naturalist's argument is inductive: the premises make the conclusion probable, not *The key distinction is between certainty and probability, and between defeasibility and non-defeasibility. Deductive arguments either guarantee their conclusions (valid) or do not (invalid) — there is*

**Model Response:**
> We need to analyze scenario: naturalist vs mathematician. The mathematician's argument is a classic deductive syllogism: (1) Tweets is a healthy, normally functioning bird. (2) All healthy, normally functioning birds can fly. (3) Therefore, Tweets can fly. This is a deductive argument. The naturalist's argument is inductive: (1) Tweets is a healthy, normally functioning bird. (2) Most healthy, normally functioning birds can fly. (3) Therefore, Tweets probably can fly. This is a probabilistic inference: from a general rule that most such birds can fly, we infer that this particular bird probably can. So naturalist's argument is inductive.

Now, after learning that Tweets is six feet tall and can run thirty miles per hour, what happens? The new information may affect the premises. For mathem

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly classifies the mathematician's argument as deductive and the naturalist's as inductive. They accurately explain that the new information weakens the inductive argument by reducing probability (defeasibility). Crucially, they distinguish between validity and soundness for the de

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe asks you to evaluate both polls. Which one should the council trust, and what are the problems with the other one?

**Expected Answer:** **Statistical generalizations: sample size and representativeness** — A good statistical generalization requires two conditions: adequate sample size and a representative sample. Pollster A fails both: 20 people is too few (hasty generalization), and surveying only at the Miners' Guild creates a biased sample that likely overrepresents mining interests. Pollster B use *Evaluating statistical generalizations requires checking sample size and representativeness. Pollster A's survey is doubly flawed: 20 people is too small to generalize from (the result could easily be*

**Model Response:**
> We need to evaluate both polls. Pollster A: 20 people at Miners' Guild hall, 15 said X. Pollster B: 500 residents randomly selected from full census roll, 52% said X. The council should trust Pollster B because it's a larger, random sample from the entire population, reducing sampling bias. Pollster A has small sample size (20) and is not representative (only miners). So it's biased sampling, small sample, high margin of error. Also Pollster A might be overestimating due to selection bias. Pollster B's margin of error ~ sqrt(p(1-p)/n) ~ sqrt(0.52*0.48/500) ~ sqrt(0.2496/500) ~ sqrt(0.0004992) ~ 0.0224, so ±4.5% at 95% CI. So 52% ±4.5% gives 47.5% to 56.5%. So it's close. Pollster A: 75% support but sample size 20 gives margin of error ~ sqrt(0.75*0.25/20)=sqrt(0.1875/20)=sqrt(0.009375)=0.0

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies both methodological flaws in Pollster A (small sample size and selection bias) and explains why Pollster B is superior based on representativeness and sample size. They explicitly name the fallacy ('hasty generalization') and the relevant principles ('law of large nu

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Three investigators each offer an explanation. Evaluate each one using the explanatory virtues. Which is the best explanation, and why?

**Expected Answer:** **Inference to the best explanation and explanatory virtues** — IBE selects the hypothesis that best explains the observed evidence according to the explanatory virtues. Lira's explanation (teleportation by rogue mage) is unfalsifiable, inconsistent with background knowledge, and introduces unnecessary entities — it fails on simplicity, testability, and consiste *IBE is not about which explanation is merely possible — all three are possible. It is about which explanation does the best job of accounting for the evidence according to the explanatory virtues. Lir*

**Model Response:**
> ### 1.  What the “explanatory virtues” are

When we judge competing explanations we normally look at the same set of virtues that philosophers of science use for theories:

| Virtue | What it means in this context |
|--------|------------------------------|
| **Simplicity** | Does the explanation add the fewest new entities or assumptions? |
| **Coherence** | Does it fit smoothly with what we already know about the world? |
| **Consistency** | Does it avoid contradictions with established facts? |
| **Scope** | How many different facts or similar cases can it explain? |
| **Plausibility / Falsifiability** | Is it a realistic scenario that could be tested or ruled out? |
| **Explanatory depth** | Does it explain the *why* behind the facts, not just the *what*? |

We will apply each to the t

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the relevant explanatory virtues and begins a structured evaluation, correctly flagging Lira's explanation as low in simplicity. However, the response is incomplete; it cuts off mid-sentence during the evaluation of the first hypothesis and fails to assess Gareth's o

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher draws an analogy between the drowning child and the daily coffee purchase. Is it a good analogy? Evaluate the relevant similarities and the disanalogies Aldric raises. Which disanalogies, if any, are relevant to the moral conclusion?

**Expected Answer:** **Argument by analogy: relevant similarities and disanalogies** — An argument by analogy infers that because two things share relevant similarities, what is true of one is probably true of the other. The philosopher argues: (1) The pond case and the coffee case share a relevant similarity — choosing a luxury over a child's survival. (2) In the pond case, saving th *Evaluating analogies requires identifying the relevant similarities and assessing whether the disanalogies matter. The philosopher's analogy is strong because the core moral feature — valuing a luxury*

**Model Response:**
> We need to evaluate the analogy. The philosopher draws analogy: drowning child vs coffee purchase. We need to evaluate similarities and disanalogies. The question: "Which disanalogies, if any, are relevant to the moral conclusion?" Also ask: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to analyze the analogy, identify relevant similarities: both involve a choice between saving a life and personal cost. Both involve a moral obligation to help. Both involve a personal sacrifice (boots vs coffee). Both involve a cost that could be avoided. The philosopher says the child is in front of him, but coffee money could save a child's life.

Disanalogies: The child is physically present vs famine

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as an argument by analogy and lists multiple similarities and disanalogies (proximity, scale, systemic nature). However, the response fails to reach Level 3 because it does not systematically evaluate whether these disanalogies are actually rele

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Using the vet's log, apply the necessary condition test and the sufficient condition test to each factor. Which factor is the likely cause of Whiskers' seizures?

**Expected Answer:** **Mill's methods: necessary and sufficient condition tests** — The necessary condition test: which factor is present in every seizure case? F is present in all three seizure days. T is present in days 1 and 3 but not day 2. V is present in days 1 and 2 but not day 3. Only F passes the necessary condition test. The sufficient condition test: which factor is abse *Mill's methods provide systematic tools for causal investigation. The necessary condition test eliminates factors that are absent when the effect occurs. The sufficient condition test eliminates facto*

**Model Response:**
> We need to answer the question: apply necessary condition test and sufficient condition test to each factor (new food F, thunderstorm T, visitor V). Determine likely cause. Also reflect on reasoning pattern, fallacy, bias, principle demonstrated. The scenario is about Mill's methods: method of agreement, difference, etc. The vet uses necessary condition test: factor present in all seizure days but absent in some no-seizure days? Actually necessary condition: if factor is necessary, it must be present on all seizure days, but can also be present on no-seizure days. Sufficient condition: if factor is sufficient, it must be present on all seizure days and absent on all no-seizure days? Wait: Sufficient condition: factor present on all seizure days and absent on all no-seizure days. Necessary 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the causal factor (New Food/F) by systematically applying both the necessary and sufficient condition tests to all three variables, explicitly ruling out T and V based on their absence in specific seizure cases. The explanation of the mechanism is accurate and aligns

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Councillor Drava claims the tonic causes higher yields based on the correlation data. What is wrong with this inference? Identify the alternative explanations.

**Expected Answer:** **Correlation vs causation: third variable and reverse causation** — When two things are positively correlated, there are four logical possibilities: (1) A causes B, (2) B causes A, (3) a third variable C causes both, (4) the correlation is coincidental. Drava assumes possibility 1 (tonic causes higher yields). The physician raises possibility 3 (wealth is the confou *Recognizing that correlation does not establish causation is essential for evaluating empirical arguments. To establish causation, you need to rule out confounding variables and reverse causation — ty*

**Model Response:**
> We need to answer: Councillor Drava claims causal inference from correlation. What is wrong? Identify alternative explanations. Reasoning pattern: correlation vs causation fallacy, omitted variable bias, reverse causation, confounding. The alternative explanations: wealthier farms have better equipment, better soil, better irrigation, better management; workers on high-yield farms have higher wages and can afford tonic; maybe the tonic is a marker of other factors like better nutrition, training, or healthier environment. Also maybe the tonic is not the cause but a marker of a third variable like farm size, location, or management practices. Also reverse causation: high yields lead to more money to buy tonic. So the inference is invalid because of omitted variable bias, confounding, revers

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core pattern (correlation does not imply causation) and explicitly names the fallacy ('post hoc ergo propter hoc', 'correlation-causation fallacy'). They successfully articulate both required alternative explanations: confounding variables (wealth, equipment, soi

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Solve the three probability problems. Show your work and explain which probability law you use for each one.

**Expected Answer:** **Basic probability laws: complement, addition, conjunction** — Problem 1 (complement): P(not-4) = 1 - P(4) = 1 - 1/6 = 5/6. Problem 2 (addition with correction): P(at least one H) = P(H on coin 1) + P(H on coin 2) - P(H on both) = 1/2 + 1/2 - 1/4 = 3/4. Alternatively, use complement: 1 - P(no heads) = 1 - 1/4 = 3/4. Problem 3 (at least one via complement): P(at *The complement rule is the most useful tool in basic probability: often it is easier to calculate the probability of something NOT happening and subtract from 1. The addition rule must correct for dou*

**Model Response:**
> **Problem 1 – “What is the probability of NOT rolling a 4 on a fair six‑sided die?”**

| Event | Probability |
|-------|-------------|
| Roll a 4 | \(1/6\) |
| **Not a 4** | \(1-1/6 = 5/6\) |

**Law used:** *Complement rule* – \(P(\text{not }A)=1-P(A)\).

---

**Problem 2 – “Flip two fair coins. What is the probability that at least one lands heads?”**

The sample space for two coins is  
\(\{HH,HT,TH,TT\}\) – 4 equally likely outcomes.

| Outcome | “At least one head”? |
|---------|---------------------|
| HH | Yes |
| HT | Yes |
| TH | Yes |
| TT | No |

So \(P(\text{at least one H}) = 3/4\).

Alternatively, use the complement rule:

\[
P(\text{at least one H}) = 1-P(\text{no H}) = 1-\left(\frac12\right)^2 = 1-\frac14 = \frac34.
\]

**Law used:** *Complement rule* (again) – it is often e

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly solved Problem 1 using the complement rule and Problem 2 using both enumeration and the complement rule. However, the response for Problem 3 is incomplete and cuts off before providing an answer or explanation. Because the third problem was not addressed, the student fails to d

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The magistrate asks: given Bob's 99% accuracy and 1000 people in the area with 5 actual robbers, what is the probability that Nancy is truly the robber? Show your reasoning.

**Expected Answer:** **Conditional probability, Bayes' theorem, and base rate reasoning** — The naive answer is 99%, but this ignores the base rate. Using Bayes' theorem: Of 1000 people, 5 are robbers. Bob correctly identifies 99% of 5 robbers = 4.95 true positives. Bob incorrectly identifies 1% of 995 innocent people = 9.95 false positives. Total positive identifications = 4.95 + 9.95 = 1 *Conditional probability requires updating prior probabilities with new evidence. The key insight is that when the base rate is low (few robbers in the population), even a highly accurate test produces*

**Model Response:**
> **Answer**

Using Bayes’ theorem the posterior probability that Nancy is the robber after Bob’s positive identification is

\[
P(\text{Nancy robber}\mid \text{Bob says “yes”})=
\frac{P(\text{Bob says “yes”}\mid \text{Nancy robber})\;P(\text{Nancy robber})}
     {P(\text{Bob says “yes”}\mid \text{Nancy robber})\;P(\text{Nancy robber})+
      P(\text{Bob says “yes”}\mid \text{Nancy innocent})\;P(\text{Nancy innocent}) } .
\]

* **Prior probability (base rate)**  
  \[
  P(\text{Nancy robber})=\frac{5}{1000}=0.005 .
  \]
  (Only 5 of the 1000 possible people are actual robbers.)

* **Likelihoods**  
  * If Nancy is the robber, Bob identifies her correctly 99 % of the time:  
    \[
    P(\text{Bob says “yes”}\mid \text{Nancy robber})=0.99 .
    \]
  * If Nancy is innocent, Bob mistakenly iden

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (Base-rate fallacy), sets up Bayes' theorem accurately, performs the arithmetic correctly to arrive at ~33.2%, and explains the mechanism clearly. However, the response cuts off mid-sentence while attempting to name the 'Prosecutor's Fallacy' and fails to

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The patient believes she has a 95% chance of having colon blight. Is she right? Use the base rate and test accuracy to compute the actual probability. Show your work.

**Expected Answer:** **Base rate reasoning in medical screening** — For a population of 100,000: 500 have colon blight (0.5% base rate). Of those 500, the test correctly identifies 95% = 475 true positives. Of the 99,500 without the disease, the test incorrectly flags 5% = 4,975 false positives. Total positive results = 475 + 4,975 = 5,450. P(disease | positive test *The base rate fallacy occurs when people ignore the prior probability of a condition and treat the test accuracy as the probability of having the condition. When a disease is rare (0.5%), the 5% false*

**Model Response:**
> **Step‑by‑step calculation**

| Symbol | Meaning | Value |
|--------|---------|-------|
| \(P(D)\) | Prior probability that a random person has colon blight | \(0.005\) (0.5 %) |
| \(P(\bar D)\) | Prior probability that a random person does **not** have colon blight | \(0.995\) |
| \(P(+|D)\) | Sensitivity – probability of a positive test **given** disease | \(0.95\) |
| \(P(+|\bar D)\) | False‑positive rate – probability of a positive test **given** no disease | \(1-0.95 = 0.05\) |

Bayes’ theorem gives the posterior probability that the patient actually has the disease after a positive test:

\[
P(D|+) = \frac{P(+|D)\,P(D)}{P(+|D)\,P(D)+P(+|\bar D)\,P(\bar D)}.
\]

Plugging in the numbers:

\[
\begin{aligned}
P(D|+) &= \frac{0.95 \times 0.005}{0.95 \times 0.005 + 0.05 \times 0.995} \\
&=

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly computes the probability (~8.7%) using Bayes' theorem (mathematically equivalent to the natural frequencies method) and explicitly identifies and explains the 'base-rate fallacy.' However, the response is cut off at the end ('Base-'), failing to complete the explanation or addr

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sergeant Dallow seems confident in his logic. Look at the sign, then look at his reasoning. Does his conclusion actually follow?

**Expected Answer:** **Denying the antecedent** — Dallow reasons from 'If royal writ, then entry' and 'no royal writ' to 'no entry.' He treats the antecedent as necessary when the sign only establishes it as sufficient. *The conditional only tells us P is sufficient for Q, not necessary. Denying the antecedent does not validly yield the denial of the consequent. Other conditions may also lead to Q.*

**Model Response:**
> We need to analyze the scenario. The sign says: "If you carry a royal writ, you may pass." The player does not have a royal writ. Sergeant Dallow says: "Rules are rules. The sign says if you carry a royal writ, you may pass. You don't have a royal writ. Therefore you may not pass. Turn around."

We need to examine if his conclusion follows. The sign says: "If you carry a royal writ, you may pass." That's a conditional statement: P → Q. Where P = "you carry a royal writ" and Q = "you may pass." The sign does not say "If you do not carry a royal writ, you may not pass." So the negation of the antecedent does not necessarily imply the negation of the consequent. This is the logical fallacy of denying the antecedent. The correct reasoning would be: If you carry a royal writ, then you may pass.

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'denying the antecedent' multiple times. They accurately explain the mechanism by distinguishing between sufficient and necessary conditions (noting the sign provides a sufficient condition for entry, not a necessary one). Although the response is repe

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Wynn seems sure it was a wolf. Does the conclusion follow from what she observed?

**Expected Answer:** **Affirming the consequent** — Wynn reasons from 'If wolf then large paw prints' and 'large paw prints' to 'wolf.' She treats the consequent as proof of the antecedent. *The conditional tells us a wolf attack would produce large paw prints, but many other causes could too. Observing Q does not allow us to conclude P.*

**Model Response:**
> **Short answer:**  
No – the conclusion does not logically follow from the observation.  
Wynn’s reasoning is an instance of the formal fallacy **affirming the consequent** (sometimes called the “converse accident” or a hasty generalization), and it is also coloured by a confirmation‑bias that makes her jump to the wolf as the only explanation.

---

## Step‑by‑step analysis

| Step | What Wynn says | Logical form | Is it valid? | Why it’s a fallacy |
|------|----------------|--------------|--------------|--------------------|
| 1 | “If a wolf attacked the sheep, we would find large paw prints near the pen.” | **If P then Q** (P = “a wolf attacked”; Q = “large paw prints are found”) | – | This is a plausible conditional, but it is not a biconditional. |
| 2 | “And look — large paw prints, 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy 'affirming the consequent,' correctly maps the logical form (If P then Q; Q; therefore P), and explains the mechanism by noting the conditional is not biconditional (prints are necessary but not sufficient). They also identify alternative explanations and men

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Varn seems very worried about this bakery permit. He has given you a chain of consequences. Do you find his reasoning convincing? Why or why not?

**Expected Answer:** **Causal slippery slope** — Varn chains together a sequence of causal claims — competition leads to price drops leads to corner-cutting leads to illness leads to overwhelmed healers leads to plague — treating each link as inevitable. Even if each individual step had a 90% probability, the probability of the entire six-step cha *Probabilities are not preserved across a chain of causal claims. Each link in the chain has its own probability of occurring, and the joint probability of the entire sequence is the product of all the*

**Model Response:**
> We need to analyze the scenario: Councillor Varn gives a chain of consequences: If we allow a second bakery, competition will drive down bread prices. If prices drop, both bakeries will cut corners on ingredients. If they cut corners, people will get sick from bad flour. If people get sick, healers' hall will be overwhelmed. If healers are overwhelmed, a plague will sweep through Ironvale. Mark my words: approving this permit is the first step toward a plague that will empty this town.

We need to evaluate whether his reasoning is convincing. Identify reasoning pattern, fallacy, bias, principle. Likely it's a slippery slope argument. Also potential false cause, overgeneralization, fear-mongering, argument from fear. He is presenting a chain of events that may or may not happen. He is makin

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as a 'slippery slope' and notes that the chain consists of 'many uncertain links' where events 'may or may not happen.' This satisfies Level 2 (noticing unlikelihood). However, the response fails to reach Level 3 or 4 because it does not articulate the sp

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Pip seems very confident in his proof. Is his reasoning valid? Can you spot the mistake?

**Expected Answer:** **Composition fallacy** — Pip infers that a property true of each individual part (each atom is invisible) must be true of the whole composed of those parts (Pip is invisible). But visibility is not a property that transfers from parts to whole in this way — the arrangement and quantity of atoms creates emergent properties l *Properties of individual parts do not necessarily hold for the whole they compose. Each atom is invisible, but billions of atoms arranged into a human body are very much visible. Whether a property tr*

**Model Response:**
> **Short answer:**  
Pip’s argument commits the *fallacy of composition* (a non‑sequitur). He assumes that because each atom is invisible to the naked eye, the whole body made of those atoms must also be invisible. The property of “invisibility to the naked eye” is a property of the aggregate, not of the individual atoms, so the conclusion does not follow from the premises.

---

### Step‑by‑step analysis

| Step | Statement | Why it’s a problem |
|------|-----------|--------------------|
| 1 | *Every atom in my body is invisible to the naked eye.* | True – atoms are far too small to be seen without a microscope. |
| 2 | *I am made entirely of atoms.* | True – all matter is composed of atoms. |
| 3 | **Conclusion:** *Therefore, I must be invisible to the naked eye.* | The conclusion is fals

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the fallacy of composition and explains that invisibility is a property of the aggregate rather than the individual parts, effectively refuting Pip's logic. However, the response does not meet Level 4 criteria because it fails to provide a counter-example where an in

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorin is trying to figure out how much individual parts of the house are worth based on the total value. Does his reasoning work?

**Expected Answer:** **Division fallacy** — Dorin infers that because the whole house has a certain property (being worth 900 gold), each part of the house must share that property proportionally. But the house's value comes from the arrangement and integration of its parts, not from the parts individually. Disassembled lumber and stones are  *The value of the house is an emergent property of its assembled structure — location, craftsmanship, functional integration. Individual beams and stones do not carry proportional shares of that value.*

**Model Response:**
> **Short answer:**  
Dorin is committing the *fallacy of division* (sometimes called *false division*). He is assuming that because the house as a whole is worth 900 gold, each component must be worth a proportional share of that value. That reasoning is logically invalid because the value of the whole is not simply the sum of the values of its parts.

---

### Why the reasoning fails

| Step in Dorin’s reasoning | What he assumes | Why it’s wrong |
|---------------------------|-----------------|----------------|
| 1. “The house is worth 900 gold.” | The total market value of the property. | This is a fact, but it is an *aggregate* value that includes many factors (location, design,

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the specific fallacy (division) and explains the core mechanism: that the value of the whole is not simply the sum of its parts due to aggregate factors like location and design. This meets Level 3 criteria. However, the response does not reach Level 4 because it lac

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Brother Vassyl seems very confident. What do you think about the reasoning he just gave you for trusting the Codex?

**Expected Answer:** **Begging the question (circular reasoning)** — The conclusion — that the Codex is the ultimate authority — is assumed as a premise when the speaker cites the Codex's own claim of infallibility as evidence. The premise and conclusion are nearly identical. *The argument assumes exactly what it is trying to prove. The Codex's reliability is the very thing in question. Formally the argument can be valid — 'P, therefore P' is valid — but validity alone is n*

**Model Response:**
> **What Brother Vassyl is doing**

Brother Vassyl’s line of reasoning is a classic *circular* or *beg‑the‑question* argument.  
He says:

> “The Codex of Arundel is the ultimate authority on all matters of truth.  
>  How do I know? Because chapter 1 of the Codex says: ‘Every word herein is the unassailable truth, authored by the infallible hand of Arundel.’”

The premise (“the Codex is infallible”) is taken from the very thing that is supposed to be proven true. The argument therefore goes:

1. **Premise** – The Codex claims its own infallibility.  
2. **Conclusion** – Therefore the Codex is infallible (and all its statements are true).  

The conclusion is used as the evidence for the premise. That is the definition of circular reasoning: the argument assumes what it is supposed to prove.

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the fallacy by name ('begging the question' and 'circular reasoning') and clearly explains the mechanism: the premise assumes the conclusion because the Codex's own claim is used to prove its authority. However, the response does not reach Level 4 because it fails to

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Harsk says you must either march north or starve. What is wrong with how he has framed the choice?

**Expected Answer:** **False dichotomy (black-or-white thinking)** — A disjunction is presented as exhaustive when it is not. Harsk forces a choice between two options while ignoring alternatives like fortifying defenses, sending scouts, hiring mercenaries, or appealing to a neighboring lord. *Harsk presents only two options — march or starve — but the disjunction does not exhaust the relevant space. Multiple unmentioned alternatives exist.*

**Model Response:**
> We need to analyze the scenario: Commander Harsk gives a choice: march north or starve. He frames it as a binary choice: either march north and crush bandits, or sit and starve. He is presenting a false dilemma (false dichotomy) or a black-and-white fallacy. He also uses emotional manipulation, fear, guilt. He is presenting a false choice, ignoring other options like negotiating, partial defense, or alternative strategies. He is also using a "false dilemma" or "either/or" fallacy. He also uses a "slippery slope"? Not exactly. He uses "appeal to fear" or "appeal to emotion" or "appeal to consequences." He also uses "scare tactics" or "fear-mongering." He might also be committing a "false dilemma" or "false dichotomy" by presenting only two options when there are more. He might also be using

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the false dichotomy (false dilemma) and provides concrete alternative options (negotiating, partial defense), satisfying Level 3 criteria. However, the response fails to reach Level 4 because it does not explain the logical mechanism regarding non-exhaustive disjunct

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Silvertongue claims this argument is logically airtight. Is it? Where does the reasoning go wrong?

**Expected Answer:** **Equivocation** — The argument uses the word 'nobody' in two different senses. In 'Nobody is perfect,' 'nobody' means 'no person' (a universal negative quantifier). In 'Bert is a nobody,' 'nobody' means 'an unimportant or insignificant person.' The argument treats these as the same meaning, creating an illusion of va *The argument trades on an ambiguity. 'Nobody' as a quantifier (no person) and 'nobody' as a noun (an insignificant person) are different concepts. Once you disambiguate the two meanings, the argument *

**Model Response:**
> We need to analyze the argument: "Nobody is perfect. Bert is a nobody. Therefore, Bert is perfect." The premises: 1) Nobody is perfect. 2) Bert is a nobody. Conclusion: Bert is perfect.

This is a classic example of a logical fallacy: denying the antecedent or something? Let's parse: "Nobody is perfect" means "For all x, if x is a nobody, then x is not perfect." Or "No one is perfect." So the statement is: ∀x (nobody(x) → ¬perfect(x)). Or equivalently: ¬∃x (nobody(x) ∧ perfect(x)). The second premise: "Bert is a nobody" means nobody(Bert). So we have: nobody(Bert). From the universal statement, we can infer ¬perfect(Bert). So the conclusion should be "Bert is not perfect." But the argument concludes "Bert is perfect." So it's a contradiction. So it's a logical fallacy: "affirming the conse

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the argument is flawed and repeatedly mentions 'equivocation' and the dual usage of the word 'nobody'. However, the explanation is confused and contradictory; the student struggles to clearly articulate the two distinct senses (universal quantifier vs. noun for 

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Scholar Tilde claims there is no real difference between a novice and an archmage because you cannot draw a sharp line between the ranks. Is she right?

**Expected Answer:** **Conceptual slippery slope** — Tilde exploits the vagueness of category boundaries. Because there is no sharp line between novice and apprentice, or apprentice and journeyman, she concludes there is no real difference between the extremes. This is the sorites paradox applied to conceptual categories: if removing one grain of sand *The inability to draw a sharp boundary between adjacent cases does not mean there is no difference between the extremes. A first-day novice and an archmage differ enormously in ability, even if the tr*

**Model Response:**
> **What’s happening?**  
Scholar Tilde is using the classic *sorites* (or “heap”) argument to say that because the boundary between “novice” and “archmage” is fuzzy, the

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the pattern by name ('sorites' or 'heap' argument) and begins to explain the mechanism (fuzzy boundaries). However, the response is incomplete and cuts off before stating the conclusion or explaining why the reasoning is flawed. Because the student does not articulat

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Grus seems pretty passionate about this. But take a step back: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely?

**Expected Answer:** **Abusive ad hominem** — Grus attacks Maren's personal background (newcomer status, lack of farmland, occupation) instead of engaging with the substance of her irrigation proposal: the river data, crop projections, costs, and affected families. He treats her identity as grounds for dismissing the argument. *The quality of an argument is independent of who presents it. Maren's proposal stands or falls on its evidence and reasoning, not on how long she has lived in Ironvale or whether she owns farmland. Gr*

**Model Response:**
> We need to analyze the scenario. Grus is arguing against Maren's irrigation proposal. He says: "Why should we listen to Maren's irrigation scheme? She moved here from Ashford only five years ago. She doesn't even own farmland! What does a newcomer shopkeeper know about our water and our soil? I say we dismiss this proposal outright."

We need to answer: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely? Then identify the reasoning pattern, fallacy, bias, or principle being demonstrated. Explain reasoning.

We need to step by step: Grus is asking the council to dismiss the proposal. He gives reasons: Maren is a newcomer, doesn't own farmland, so she doesn't know about water and soil. So he's

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core issue: Grus attacks Maren's background (newcomer status, lack of farmland) rather than the merits of her proposal. They explicitly name the pattern as 'ad hominem (circumstantial)' and explain that the reasons given are about the person, not the argument. Ho

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The merchant demands you prove his amulet doesn't work. What is wrong with this?

**Expected Answer:** **Burden of proof** — Shifting the burden of proof from the person making the claim to the person questioning it. *The person making a positive claim bears the responsibility of providing evidence. The inability to disprove something does not constitute evidence that it is true.*

**Model Response:**
> We need to analyze the scenario: A merchant sells invisible amulets of protection, claiming they ward off curses. The merchant says: "You say my Amulet of Unseen Warding doesn't work? Well then, prove it! Go ahead — prove there ISN'T a magical barrier around you right now. You can't, can you? That's because it's working!"

The merchant demands the customer prove that the amulet doesn't work. The customer says it doesn't work. The merchant says "prove it." The customer tries to prove there is no magical barrier. The merchant says "you can't prove there's no barrier, so it must be working." This is a classic argument from ignorance or the fallacy of argument from ignorance (argumentum ad ignorantiam). The merchant is asserting that because the customer cannot prove the amulet doesn't work, i

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: the merchant shifting the burden of proof to the customer and using the inability to disprove the claim as evidence for it. They explicitly name the 'burden of proof' shift and explain that the claimant must support their own claim. However, the r

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Ranger Harlen rejects the fossil evidence because he can't imagine fish becoming people. What error is he making?

**Expected Answer:** **Personal incredulity** — Dismissing a claim because one personally cannot understand or imagine how it could be true. *The complexity of a claim has no bearing on its truth. Many well-supported facts are deeply counterintuitive. Personal failure to comprehend is not a refutation.*

**Model Response:**
> **The error is an *argument from personal incredulity* (also called an *appeal to ignorance*).**

---

### What Harlen is doing

1. **He has a pre‑existing belief** – that fish can’t become people.  
2. **He encounters evidence** (fossils, evolutionary theory, etc.) that contradicts that belief.  
3. **He responds with disbelief** – “I can’t imagine fish sprouting legs and becoming people.”  
4. **He dismisses the evidence** because it conflicts with his imagination, not because it is unsupported by data.

---

### Why this is a fallacy

- **Incredibility ≠ falsity**: Just because something is hard to picture or seems counter‑intuitive does not make it false.  
- **Evidence is independent of imagination**: Scientific conclusions are based on data, not on what a person can or cannot picture

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('argument from personal incredulity'), clearly distinguishes between emotional rejection (inability to imagine) and evidential refutation, and explains the mechanism by noting that scientific conclusions rely on data rather than personal intuition. The respo

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Every time Seer Vashti's powers fail a test, she adds a new excuse. What reasoning error is this?

**Expected Answer:** **Special pleading / No true Scotsman** — When a claim is shown to be false, moving the goalposts by introducing ad hoc exceptions so the claim can never be falsified. *Each time counter-evidence appears, a new exception is added. This makes the claim unfalsifiable. A claim that cannot in principle be proven wrong is not meaningfully supported.*

**Model Response:**
> **Answer: Ad hoc reasoning (the ad hoc hypothesis fallacy)**  

---

### What it is

An *ad hoc* explanation is one that is invented after the fact to protect a hypothesis from being falsified.  
The key features are:

1. **It is added only after a failure or a problem arises.**  
2. **It is tailored to the specific problem and is not independently testable.**  
3. **It does not change the original hypothesis; it merely shields it from criticism.**

In the scenario, every time Seer Vashti’s predictions are disproved, she immediately offers a new excuse—“the skeptic’s hostile energy blocked my sight,” “the conditions were wrong,” etc. Each excuse is a new, untestable clause that is only introduced when the original claim (that she can see the future) is challenged.

---

### Why it’s a reas

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the mechanism of moving goalposts and explicitly explains how the excuses render the claim unfalsifiable. They use the term 'ad hoc reasoning,' which is conceptually accurate and synonymous with the target pattern (special pleading) in this context. However, they did

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Greaves demands a yes-or-no answer. What is the problem with this question?

**Expected Answer:** **Loaded question** — A question containing a built-in assumption so that any direct answer appears to confirm it. *The question presupposes something not established — that Maren used contaminated herbs. Both yes and no accept the false premise.*

**Model Response:**
> **The problem is that the alderman is asking a *loaded, leading question* that forces a binary answer while presupposing guilt.**

---

### 1. What the question looks like

> “Tell me, Healer Maren — have you stopped using contaminated herbs in your remedies yet? The council deserves a straight answer: yes or no.”

At first glance it seems like a simple “yes‑or‑no” question, but the wording is carefully crafted to shape the answer.

---

### 2. Why it’s a *loaded* (or *leading*) question

| Feature | How it shows up in the question |
|---------|---------------------------------|
| **Presupposition** | The question assumes that Maren *has* been using contaminated herbs. It asks whether she has *stopped* doing so. |
| **No room for nuance** | The answer “yes” could mean “I have stopped using

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a 'loaded question' and clearly explains the built-in presupposition (that Maren was using contaminated herbs). They also discuss the false dilemma aspect. However, the response falls short of Level 4 because it does not explicitly suggest how Maren sh

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The alchemist tested in thirty villages but only shows five. What reasoning error is he committing?

**Expected Answer:** **Texas sharpshooter** — Cherry-picking data clusters that suit a conclusion while ignoring data that does not. Like painting a target around bullet holes after shooting. *Finding a cluster in a large dataset is virtually guaranteed by chance. Selecting after the fact and presenting as evidence is statistically invalid. Honest analysis requires looking at ALL the data.*

**Model Response:**
> **Fallacy:** **Cherry‑picking (selective evidence / confirmation bias)**  

**Why it’s a mistake**

1. **Only the “good” data are shown** – The alchemist surveyed 30 villages, but he only displays the five that happened to show a dramatic drop in pox rates.  
2. **The rest of the data are ignored** – The other 25 villages are omitted, so the evidence is not representative of the whole sample.  
3. **A biased conclusion is drawn** – By presenting only the positive cases, the alchemist leads the council to believe the tonic is effective, even though the full data set may show no effect or even a negative effect.

**Related concepts**

- **Confirmation bias** – The tendency to notice or emphasize evidence that supports one’s hypothesis while ignoring contrary evidence.  
- **Sampling bias / s

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism of cherry-picking and explains that the alchemist selected only favorable data points (5 out of 30) to support a conclusion, which aligns with Level 3. They also mention related concepts like confirmation bias and sampling bias. However, the respon

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The mediator proposes combining evidence-based treatment with unsupported one. What is wrong with this?

**Expected Answer:** **Middle ground (false compromise)** — Assuming the truth must lie between two positions simply because they are opposing, regardless of evidence. *Truth is not determined by averaging positions. When one is well-supported and the other baseless, the middle ground corrupts the good position. Draining 'some' blood is still harmful.*

**Model Response:**
> We need to analyze the scenario: mediator proposes combining evidence-based treatment with unsupported one. The question: "What is wrong with this?" We need to think step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? The mediator is combining evidence-based treatment with unsupported one. That is akin to the "false compromise" or "fallacy of the middle" or "argument to moderation" or "false balance" or "equivocation" or "appeal to novelty"? The mediator says "Clearly the truth lies in the middle. I propose we use the compound AND drain some blood — a moderate amount. Compromise is always wisest." This is essentially the "argument to moderation" or "fallacy of the middle ground" where the mediator assumes that the truth must be somewhere between two ext

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'fallacy of the middle ground' (argument to moderation) and explains the core mechanism: that truth is not determined by averaging two positions, especially when one lacks evidence. They effectively distinguish between the evidence-based treatment and the unsuppo

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dag dismisses mine dust danger because his grandfather survived it. What reasoning error?

**Expected Answer:** **Anecdotal evidence** — Using personal experience or an isolated example in place of statistical evidence, especially to dismiss systematic data. *A single case cannot override systematic evidence. Dag's grandfather is one data point — possibly an outlier. The question is the overall rate of lung disease among miners, not whether anyone can surv*

**Model Response:**
> **Fallacy:** *Anecdotal evidence / hasty generalization* (often called the “appeal to personal experience” fallacy).

**Why it’s a mistake**

1. **Single data point → universal claim**  
   Dag uses one story—his grandfather’s long life—to argue that mine dust is harmless for everyone. That is a classic hasty generalization: drawing a conclusion about a whole population from an isolated case.

2. **Ignoring the larger evidence**  
   The anecdote is not weighed against statistical data, medical studies, or the experiences of other miners who did suffer lung disease. By focusing only on the “success” story, Dag commits the *survivorship bias* that ignores the many who did not survive.

3. **Misplaced authority**  
   The grandfather is not an expert on occupational health. Relying on his pe

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy (anecdotal evidence/hasty generalization), correctly explains that a single case cannot represent a population, identifies survivorship bias as a specific mechanism, and notes the psychological weight of vivid stories versus statistical data. This meets all c

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What is wrong with Alderman Grask's response to Sable's proposal?

**Expected Answer:** **Straw man** — Grask inflates Sable's modest proposal (a south-bank levee) into an extreme position (damming the entire river) and then attacks the extreme version. His criticism C targets fabricated position B, not Sable's actual position A. *Grask's criticism targets a fabricated version of Sable's proposal. A south-bank levee does not dam the river. His objections about livestock and mills are irrelevant to the actual proposal.*

**Model Response:**
> **Short answer:**  
Alderman Grask’s reply is a classic *straw‑man / slippery‑

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern by name ('straw-man') but the response is incomplete and cuts off mid-sentence ('slippery-'). Because the explanation of the mechanism (how the levee was distorted into a dam) is missing due to the truncation, the response cannot meet the criteria for Lev

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Garrett fires back at Inspector Maren by bringing up the oil-lantern incident. What is wrong with his reasoning? Why doesn't Maren's past mistake let Garrett off the hook?

**Expected Answer:** **Tu quoque (appeal to hypocrisy)** — Dismissing a criticism by pointing out that the person making it is guilty of the same or similar fault. Treats the critic's inconsistency as though it refutes the content of the criticism. *Whether or not the critic is a hypocrite has no bearing on the truth of the criticism. The coal dust is either a fire hazard or it is not, regardless of what Maren did last winter. Hypocrisy is a char*

**Model Response:**
> **What Garrett is doing**

Garrett is trying to get rid of the inspector’s criticism by pointing out that she herself made a fire‑related mistake in the past.  
In logical terms he is *shifting the focus from the substance of the argument (the coal‑dust storage) to the inspector’s character or past conduct*.  

**The fallacy at play**

This is the classic **tu quoque** (appeal to hypocrisy) fallacy, a specific form of **ad hominem circumstantial**.  
- **Tu quoque**: “You’re telling me to do X, but you did Y.”  
- **Ad hominem circumstantial**: “Because you have a particular circumstance (your past mistake), you’re not qualified to judge me.”

**Why it’s wrong**

1. **Irrelevance** – The inspector’s past error is unrelated to the *validity* of the current safety rule.  
   - The rule that 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'tu quoque' and explains the mechanism by highlighting the irrelevance of the inspector's past behavior to the validity of the current safety rule. Furthermore, the response exceeds Level 3 by explicitly describing what a legitimate response would look

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorric clearly does not like this formula. But does he point out any problem with the measurements, the chemical rationale, or the engineering requirements? What is his objection really about?

**Expected Answer:** **Genetic fallacy** — Dorric judges the formula by attacking its origin — Vielle's impoverished background — rather than engaging with its content. The chemical rationale and measurements go entirely unaddressed. *The quality of a formula depends on its content — the logic, evidence, and reasoning — not on the biography of whoever produced it. Vielle's background tells you nothing about whether her measurements*

**Model Response:**
> **Short answer**

Dorric isn’t arguing about the numbers, the chemistry or the engineering at all.  
He’s arguing *about Vielle’s pedigree* – that because she came from a workhouse, her “breakthrough” can’t be good.  
In other words, he’s committing a **genetic fallacy / ad‑hominem** that rejects an idea because of its source, and he’s doing it with a clear **class / status bias** that equates “guild‑born” with “high‑quality” and “workhouse‑born” with “low‑quality.”  

---

## Step‑by‑step reasoning

| Step |

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the 'genetic fallacy' and accurately explains the mechanism: Dorric attacks Vielle's background (workhouse) rather than the formula's content (numbers, chemistry). The response also adds valuable context regarding class bias. However, it does not reach

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Holt raises serious worries. But is he giving you any reason to doubt Tova's research itself?

**Expected Answer:** **Appeal to consequences** — Arguing that a factual claim should be rejected because accepting it would lead to undesirable outcomes, substituting the consequences for a critique of the evidence. *The truth of a factual claim does not depend on whether its consequences are pleasant. Consequences are relevant to policy (what to do about a finding), not to whether the finding is true.*

**Model Response:**
> **Short answer:**  
No.  Holt is

**Score:** 0/4 ░░░░
**Judge Reasoning:** The response is incomplete and cuts off mid-sentence. It fails to identify the pattern, explain the mechanism, or provide any reasoning. As it offers no substantive content to evaluate against the rubric, it defaults to the lowest level.

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Corvin has a strong expert backing his claim. But what exactly is Eldric an expert in, and what is the question being debated?

**Expected Answer:** **Appeal to authority** — Corvin appeals to Eldric's authority as a surgeon to settle a question about marine toxicology — a field in which Eldric has no special expertise. *An authority's expertise does not transfer automatically to unrelated domains. Eldric's prestige makes his opinion influential but not reliable on marine toxicology.*

**Model Response:**
> **Who is the “expert” and what is he being asked to judge?**  
- **Eldric** is a *surgeon* – a medical professional whose training and experience are in human anatomy, physiology, and the treatment of people.  
- The *question* Corvin is trying to settle is whether the new dye will *poison the harbor fish* (i.e., whether the chemicals are toxic to fish).

**What reasoning pattern is at work?**  
Corvin is appealing to Eldric’s authority to prove a point that Eldric is not qualified to assess. This is the classic **“appeal to authority”** fallacy, more precisely an **“appeal to an irrelevant authority”** (argumentum ad verecundiam).  

**Why is it a fallacy?**  
An authority is only persuasive when the authority’s expertise is *relevant* to the claim. A surgeon’s knowledge of human biology 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as an 'appeal to an irrelevant authority,' explicitly explains the domain mismatch between surgery and marine toxicology, and articulates the principle that authority is only persuasive when expertise is relevant to the specific claim. This meets all crit

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?

**Expected Answer:** **Appeal to emotion** — Substituting emotional response — pity, guilt, sentiment — in place of addressing the factual evidence. Geld does not contest the ledger; she tries to make accusers feel bad for asking. *Whether she sat up with sick children does not change what the grain ledger shows. The emotional response is designed to block the factual inquiry, not answer it.*

**Model Response:**
> We need to analyze the scenario: Matron Geld is upset, claims she has done good, but does she address the evidence? The question: "Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?" The answer: No, she is not addressing the evidence; she is using an emotional appeal, an appeal to emotion, or a red herring, or a non sequitur. She is basically saying "I did good, so you should not judge me." She is not addressing the ledger evidence. She might be committing the "appeal to emotion" fallacy, or "ad hominem" or "appeal to pity" or "argument from personal experience." She is also using a "tu quoque" or "appeal to hypocrisy" maybe. But she is not addressing the evidence. She is making an emotional appeal: "Look at their fa

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Geld fails to address the factual evidence in the ledger and explicitly names the pattern as an 'appeal to emotion' (and 'appeal to pity'). They accurately explain the mechanism: substituting emotional deflection for factual rebuttal. However, the response lacks

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Saffron's pitch sounds appealing. What evidence does he give that the spring water cures anything? Is 'it's natural' really a reason?

**Expected Answer:** **Appeal to nature** — Arguing that a product works because it is natural, treating naturalness as sufficient evidence of safety and efficacy. *Naturalness is not a reliable indicator of safety or efficacy. Many natural substances are deadly (hemlock, arsenic). The appeal substitutes a feel-good category for actual evidence.*

**Model Response:**
> **What evidence does Saffron actually give?**  
None.  
He tells the market that the vial contains “nothing but pure mountain spring water – untouched by human hands, exactly as nature intended” and that this is why it works. He contrasts it with “alchemical concoctions” that are “brewed in workshops full of strange powders.” The only thing he offers is a description of the product’s provenance and a claim that the body “knows what is natural.” No data, no clinical trials, no anecdotes, no testimonials, no comparison to placebo – just a statement that the water is *natural* and therefore safe and effective.

---

### The reasoning pattern at play

| Step | What Saffron says | What it’s really doing |
|------|-------------------|------------------------|
| 1 | “Nothing but pure mountain spr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'appeal to nature' pattern and clearly explains the mechanism: equating naturalness with safety and efficacy without evidence. They explicitly note the lack of data, trials, or anecdotes. However, the response does not reach Level 4 because it fails to provide sp

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What evidence does Paddy give that the charm works? Is 'everyone is buying one' a reason?

**Expected Answer:** **Bandwagon (argumentum ad populum)** — Arguing that something must be true or good because many people believe it or do it. Treating popularity as evidence. *The number of people who believe something has no bearing on whether it is true. Popularity can be driven by social pressure, marketing, or tradition — none constitute evidence.*

**Model Response:**
> **What Paddy actually says**

> “Look around you — half the village is wearing one already!  
>  Farmer Crewe bought three. The baker’s whole family has them.  
>  Even old Magistrate Dunne picked one up.  
>  When this many people believe in something, there must be something to it.  
>  You don’t want to be the only soul without one, do you?”

**What evidence is offered?**

1. **Anecdotal “proof”** – Paddy lists a handful of people who bought or are wearing the charms.  
2. **Social‑proof claim** – he says “half the village is wearing one already.”  
3. **Authority‑style claim** – he mentions the Magistrate, implying that an “official” has chosen the charm.  
4. **Bandwagon / fear‑based pressure** – “you don’t want to be the only soul without one.”

None of these points actually demonstr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Paddy uses the number of buyers as the sole evidence and explicitly explains that popularity does not establish truth (identifying the argumentum ad populum/bandwagon fallacy). However, the response does not fully meet Level 4 criteria because it does not explic

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The deputy thinks it is more likely that Linda is a bank clerk AND an activist than that she is just a bank clerk. Is the deputy's reasoning correct?

**Expected Answer:** **Conjunction fallacy** — The deputy judges P(bank clerk AND activist) > P(bank clerk). This violates a basic law of probability: the probability of a conjunction can never exceed the probability of either conjunct alone. P(A and B) <= P(A). The error occurs because the conjunction fits a compelling narrative (the 'represent *A conjunction adds a constraint. Every bank clerk who is also an activist is already counted among the bank clerks. The set of people who are both A and B is a subset of the set of people who are A. N*

**Model Response:**
> **Short answer:**  
No – the deputy’s reasoning is a classic *conjunction fallacy*.  He is treating the “bank clerk + activist” description as more likely than the simpler “bank clerk” description, even though the former is a subset of the latter and therefore cannot be more probable unless the evidence is extraordinarily strong.  In other words, he’s ignoring the base‑rate (the overall likelihood that a bank clerk is an activist) and is being misled by the representativeness of the activist profile.

---

## Why the deputy’s reasoning is wrong

| Step | What the deputy does | Why it’s a problem |
|------|----------------------|--------------------|
| 1. | Takes the dossier facts (philosophy, protests, outspoken) and notes they “fit” an activist profile. | The facts *match* an activist des

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'conjunction fallacy,' correctly states the probability rule that a conjunction cannot exceed the probability of its constituents (noting the subset relationship), and explains the role of the 'representativeness' heuristic in driving the error. The response dem

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sera says there is a 95% chance the patient has Stoneblight based on the positive test. Is she right? What is the actual probability?

**Expected Answer:** **Base rate neglect** — Sera assumes that a positive result on a 95% accurate test means a 95% chance of disease. She ignores the base rate of 0.5%. For 100,000 people: 500 have Stoneblight. The test catches 475 of them (true positives). Of the 99,500 healthy people, the test falsely flags 5% = 4,975 (false positives). Tot *When the base rate of a condition is very low, even a highly accurate test produces far more false positives than true positives. The 95% accuracy tells you about the test's performance, not about thi*

**Model Response:**
> **Short answer**

No – the 95 % figure is not the chance that the patient actually has Stoneblight.  
Given a 0.5 % prevalence, 95 % sensitivity and 95 % specificity, the probability that a person who tests positive truly has the disease is only about **9 %** (≈ 8.7 %).  

**Why the healer’s reasoning is wrong**

1. **Base‑rate neglect (Base‑rate fallacy)** – She ignores the very low prior probability that a random person has Stoneblight (0.5 %).  
2. **Misinterpreting “accuracy”** – “95 % accurate” is ambiguous. In this context it means the test correctly identifies 95 % of sick people (sensitivity) and correctly clears 95 % of healthy people (specificity). It does **not** mean that a positive result guarantees a 95 % chance of disease.  
3. **Confusing sensitivity/specificity with predic

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies base rate neglect, explains the mechanism regarding false positives and low prevalence, and performs a precise calculation using Bayes' theorem to arrive at the correct probability (~8.7%). The response exceeds Level 3 by providing the formal mathematical derivation 

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Minister Kael says the data proves small schools produce better scholars. Is the data as convincing as he thinks? What should he check before spending 1.7 million gold?

**Expected Answer:** **Law of small numbers / small numbers fallacy** — Kael observes that small schools top the achievement rankings and concludes that being small causes better performance. But smaller populations produce more variable outcomes: with fewer students, a few strong (or weak) performers swing the average dramatically. If Kael checked the bottom of the ran *The law of small numbers states that smaller groups will tend to inhabit the extremes of any ranking. Kael only checked the top — if he checked the bottom, he would also find small schools. The patter*

**Model Response:**
> We need to analyze the scenario: Minister Kael claims data proves small schools produce better scholars. He wants to allocate 1.7 million gold to split large city schools into smaller academies. The question: Is the data as convincing? What should he check before spending? Think through step by step. Identify reasoning pattern, fallacy, bias, principle. Likely the scenario demonstrates a correlation vs causation fallacy, selection bias, confounding variables, ecological fallacy, sampling bias. Also small sample sizes, small schools may have other factors: socioeconomic status, teacher quality, community involvement, etc. The minister might be committing the "small sample bias" or "ecological fallacy" by generalizing from small schools to large schools. Also "post hoc ergo propter hoc" or "

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that correlation does not imply causation and suggests checking for confounding variables (socioeconomic status, teacher quality, etc.), which aligns with Level 2. However, the response fails to identify the specific statistical mechanism required for higher scores: 

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sal says nine out of ten customers feel better after taking his elixir. Is this good evidence that the elixir works?

**Expected Answer:** **Regression to the mean** — People seek remedies when symptoms are at their peak (an extreme observation). After peak symptoms, the natural tendency is to return to baseline health — this is regression to the mean. Sal attributes the improvement to his elixir, but the improvement would likely have occurred regardless. The nine *Colds typically last a few days and resolve on their own. People buy remedies when they feel worst, which is exactly when improvement is most likely regardless of treatment. To show the elixir actuall*

**Model Response:**
> **Short answer:**  
No – the “nine‑out‑ten” claim is a classic example of *anecdotal evidence / hasty generalization* (often coupled with a *post‑hoc* or *correlation‑vs‑causation* fallacy). It is not a scientifically valid way to prove that the elixir works.

---

## Step‑by‑step reasoning

| Step | What’s happening | Why it’s a problem |
|------|------------------|--------------------|
| 1. **Anecdotal testimony** | Sal shows a single vial, cites one farmer (Gerd) and a handful of “satisfied customers.” | Anecdotes are unstructured, uncontrolled, and not representative. They can be true, but they are not evidence that *all* customers will benefit. |
| 2. **Selective reporting** | Sal only mentions the nine customers who felt better; he never mentions the one who didn’t (or any who might 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that customers might have recovered naturally and notes the lack of a control group (Step 3), which aligns with Level 2. However, the response fails to explicitly identify the specific statistical phenomenon of 'regression to the mean' or explain the crucial mechanis

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Rurik says the dice are 'owed' a high roll after six lows. What is wrong with his reasoning?

**Expected Answer:** **Gambler's fallacy** — The mistaken belief that if a random event has occurred more frequently than expected, it is less likely to occur next. Each independent trial has the same probability regardless of previous outcomes. *Independent random events have no memory. The probability of a high roll on the 7th throw is exactly the same as on the 1st. Rurik confuses the law of large numbers (long-run convergence) with a suppo*

**Model Response:**
> We need to analyze the scenario: Rurik Coinbane is a gambler who has rolled low six times in a row. He says the dice are "owed" a high roll after a streak of lows, implying gambler's fallacy: the belief that a random sequence will even out in the short term. He thinks the probability of a high roll is increased after many lows. The fallacy is gambler's fallacy, or the law of averages. He is also possibly committing the fallacy of the "hot hand" but reversed. He might also be committing the "regression to the mean" misinterpretation. He might be using the "law of large numbers" incorrectly: expecting a high roll after many lows. He might also be overestimating the probability of a high roll due to the "misconception of independence" or "misunderstanding of probability".

The question: "What

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Gambler's Fallacy and provides a clear explanation of independent events and the misapplication of the Law of Large Numbers. However, the response fails to reach Level 4 because it does not raise the critical counterpoint about questioning whether the dice are fa

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Breck says all the people of Dunmore are cheats based on his two visits. Is his conclusion justified by his evidence?

**Expected Answer:** **Hasty generalization** — Breck draws a universal conclusion ('all people of Dunmore are cheats') from a sample of two negative interactions. The sample size is far too small to support a generalization about an entire town's population. He is also ignoring the possibility of confounding factors (perhaps he visited during a  *Two encounters cannot justify a universal claim about an entire town. The sample is far too small and likely unrepresentative. Breck may also have selection bias — he remembers the negative experience*

**Model Response:**
> **Short answer:**  
Breck is committing a *hasty generalization* (an inductive fallacy) by drawing a blanket conclusion about an entire population from only two negative encounters.  He is also relying on anecdotal evidence and is likely being influenced by *confirmation bias* (he remembers only the bad experiences and ignores any contrary evidence).

---

### Step‑by‑step reasoning

1. **Identify the claim**  
   Breck states: *“All the people of Dunmore are cheats and thieves.”*  
   This is a universal claim about every inhabitant of Dunmore.

2. **Examine the evidence he cites**  
   - First visit: the innkeeper overcharged him.  
   - Second visit: a street vendor sold him rotten apples.  
   These are two isolated incidents involving two different individuals.

3. **Determine the log

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the hasty generalization fallacy and explains that two cases cannot support a universal claim. Crucially, they exceed Level 3 requirements by explicitly discussing sample size requirements (contrasting 2 vs. 200 people), noting confounding factors like bias and non-r

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Brix says seagulls are causing the decline of the fishing fleet because the two trends are correlated. Is his reasoning sound?

**Expected Answer:** **False cause / post hoc fallacy** — Brix observes that two variables are correlated over time (fishing boats declining, seagulls increasing) and infers that one causes the other. But correlation does not establish causation. There are four possibilities: (1) seagulls cause boat decline, (2) boat decline causes seagull increase, (3) a  *Correlation between two variables does not establish that one causes the other. Brix has not ruled out reverse causation, a common cause, or coincidence. Culling seagulls addresses a symptom at best a*

**Model Response:**
> **Short answer:**  
No – Councillor Brix commits the classic *correlation‑causation* fallacy (sometimes called “post‑hoc ergo propter hoc” or “spurious correlation”). He assumes that because two trends move together, one must be causing the other, and he ignores the possibility of a third factor (or multiple factors) that could explain both.

---

### Step‑by‑step analysis

| Step | What Brix does | Why it’s a problem |
|------|----------------|--------------------|
| 1 | He draws a chart showing two lines: fishing boats ↓, seagulls ↑. | The chart is a visual representation of a *correlation* between two variables. |
| 2 | He states: “The correlation is undeniable. The seagulls are driving away the fish, which is destroying our fishing fleet.” | He leaps from *correlation* to *causation* w

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the false cause/correlation-causation fallacy and explicitly names 'post-hoc'. They provide a clear mechanism explaining why the reasoning is flawed and propose multiple plausible alternative explanations (common causes like overfishing, climate change, etc.). Howeve

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Vance seems to be complimenting Pip, but something feels off. What rhetorical technique is Vance using?

**Expected Answer:** **Evaluative language and presupposition** — Using loaded terms, diminutives, and embedded presuppositions to bias perception without explicit argument. The framing does the persuasive work while appearing neutral. *This substitutes rhetorical framing for argument. 'Even Pip managed' presupposes expected failure. 'Limited background' presupposes inferiority. None are argued for — they are smuggled in through word*

**Model Response:**
> **Answer: Vance is delivering a *back‑handed compliment* (a sarcastic, ironic compliment).**

---

### Why it’s a back‑handed compliment

| Vance’s words | What they sound like | What they actually mean |
|---------------|----------------------|-------------------------|
| “I suppose even Pip managed to clear the Thornwall Caverns.” | A mild, almost reluctant praise. | “Even you, Pip, managed to do something.” |
| “Quite the accomplishment for someone of his… limited background.” | Still a compliment, but with a caveat. | “You’re only good because you’re not expected to be.” |
| “I’m sure his little adventure was very exciting for him.” | A polite, supportive remark. | “It was probably not very exciting at all.” |

The overall effect is to **praise Pip while simultaneously undermining his 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the dismissive tone and points to specific words like 'even' and 'little' as evidence (Level 2). However, the response frames the technique primarily as a 'back-handed compliment' or sarcasm rather than analyzing the specific mechanism of 'evaluative language and pre

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Question:** Can you identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work?

**Expected Answer:** **Assuring, guarding, and discounting** — Three rhetorical moves managing acceptance: assuring ('everyone knows') discourages questioning, guarding ('most scholars') hedges while sounding authoritative, discounting ('granted X, but Y') acknowledges then dismisses objections. *When used to replace evidence: 'everyone knows' is social pressure, not evidence. 'Most scholars' is presented without citation. 'Granted but' acknowledges without genuinely weighing.*

**Model Response:**
> We need to analyze the scenario: A royal advisor urges the king to raise taxes on peasant farmers to fund a border fortress. The advisor says: "Everyone knows the northern threat is growing — that's simply beyond dispute. Now, most military scholars agree the border fortress is our only viable defense. Granted, the tax will be hard on farmers, but surely a little hardship is worth the survival of the entire kingdom. No reasonable person could object."

We need to identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work.

We need to think about the reasoning pattern, fallacy, bias, or principle being demonstrated. The advisor uses certain rhetorical moves: assuring: "Everyone knows the northern threat is 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies all three rhetorical moves (assuring, guarding, discounting) and maps them to the specific text. However, the response fails to reach Level 3 because it does not clearly explain *how* these moves function to substitute rhetoric for evidence; instead, it lists various

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Torin says that because Amanda argued badly, the herb must NOT have healing properties. What is wrong with Torin's reasoning?

**Expected Answer:** **The fallacy fallacy** — Assuming that because an argument for a conclusion contains a fallacy, the conclusion itself must be false. A bad argument for X does not prove not-X. *A fallacy means the argument fails to establish its conclusion — it does NOT mean the conclusion is wrong. The herb's properties are empirical, independent of any particular argument about them.*

**Model Response:**
> **Torin is committing the “fallacy‑fallacy” (also called the *argument from fallacy*).**  
In other words, he’s assuming that because Amanda’s reasoning is fallacious, the claim she’s trying to support must be false.

---

### Why that’s a mistake

| Step in Torin’s reasoning | What’s actually true |
|---------------------------|----------------------|
| 1. Amanda’s argument is fallacious (appeal to tradition). | Correct – the argument is logically weak. |
| 2. Therefore the conclusion (“Silvervein has healing properties”) is false. | **Not necessarily** – a fallacious argument can still happen to reach a true conclusion. |
| 3. Hence Silvervein has no healing properties. | Invalid inference. |

The logical truth of a conclusion is independent of the *form* of the argument that produced it

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'fallacy-fallacy', clearly distinguishes between the quality of the argument and the truth of the conclusion, and correctly identifies that the conclusion is an empirical matter requiring independent testing (experiments/clinical tests). This meets all criteria for L

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The innkeeper's daughter has laid out the situation. Identify the acts, the states, and the outcomes. Then check: does either act dominate the other with these values?

**Expected Answer:** **Decision matrix construction** — A decision matrix organizes a choice into rows (acts the agent controls), columns (states of the world the agent does not control), and cells (outcomes with assigned values). This is the foundational representation for all of decision theory. *The matrix separates what you control (take or leave the umbrella) from what you do not control (the weather). With these ordinal values, neither act dominates the other: Take Umbrella is better if it*

**Model Response:**
> **Acts (choices)**  
1. **Take the umbrella** (pay 5 copper, carry it on the journey)  
2. **Leave the umbrella** (do not carry it, keep it at the inn)

**States of the world**  
- **Rain** – the sky actually pours.  
- **No rain** – the sky stays clear.

**Outcomes (utility values)**  

| Act / State | Rain | No rain |
|-------------|------|---------|
| **Take umbrella** | 3  | 2 |
| **Leave umbrella** | 1  | 4 |

(These numbers are the “pay‑offs” the problem gives: 3 = dry but burdened, 2 = dry and burdened, 1 = wet and miserable, 4 = free and light.)

---

### Dominance check

An act *dominates* another if it yields a strictly better outcome in **every** state.  
- In **Rain**: Take = 3 > Leave = 1 → Take is better.  
- In **No rain**: Leave = 4 > Take = 2 → Leave is better.

Because ea

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructs the decision matrix with acts, states, and outcomes. They accurately perform the dominance check and conclude that neither act dominates the other because each is superior in a different state. However, the response falls short of Level 4 because it does not explicit

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The merchant has set up a matrix. Dominance reasoning gives no clear answer. But is there a deeper problem with how the matrix is constructed? What assumption does dominance reasoning require about the relationship between acts and states?

**Expected Answer:** **Dominance reasoning and state-act independence** — Dominance reasoning says: if one act yields a better outcome in every possible state, choose it. But this only works when states are independent of acts. In the extortion case, whether the cart is damaged depends on whether you pay — the states are not independent of the acts, which violates the str *Dominance reasoning requires that the states of the world are independent of your acts. Here, 'Cart Damaged' is not an independent state — it is caused by your refusal to pay. The correct matrix shoul*

**Model Response:**
> We need to analyze the scenario: player parking horse-drawn cart, dockworker offers protection for ten silver. If pay, cart stays in one piece tonight. If don't pay, risk damage. The matrix:

Cart Damaged: Pay 10 silver: -10; Don't pay: -400
Cart Not Damaged: Pay 10 silver: -10; Don't pay: 0

Dominance reasoning: For each state, compare pay vs don't pay. For damaged state, pay is better (-10 > -400). For not damaged state, pay is worse (-10 < 0). So no dominance. But the problem: The states "Cart Damaged" and "Cart Not Damaged" are not independent of the action. The action influences the state. The matrix incorrectly assumes that the state is independent of the action. In decision theory, we need to consider the probability of each state given the action. The matrix is a payoff matrix for 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that dominance reasoning requires state-act independence and explains clearly that this condition is violated because the action (paying) influences the state (cart damage). They also correctly suggest using expected utility as the alternative approach. However, the 

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The prospector wants the biggest possible payoff and does not care about the downside. Apply the maximax rule: for each expedition, find its best outcome, then pick the expedition with the highest best outcome.

**Expected Answer:** **Maximax** — Maximax identifies the best possible outcome for each act, then selects the act with the highest best-case outcome. It is the optimist's rule: chase the ceiling, ignore the floor. *The best outcome for River Panning is 8, for Hilltop Digging is 12, and for Cave Exploring is 6. Maximax selects the highest of these maxima: 12, corresponding to Hilltop Digging. The prospector shoul*

**Model Response:**
> **Step‑by‑step decision**

| Expedition | Rich | Moderate | Barren |
|------------|------|----------|--------|
| River panning | 8 | 5 | 2 |
| Hilltop digging | **12** | 3 | 1 |
| Cave exploring | 6 | 6 | 4 |

The **maximax** rule says: *look at the best possible payoff for each alternative, then pick the alternative whose best payoff is the largest.*  
- River: best payoff = 8  
- Hilltop: best payoff = 12  
- Cave: best payoff = 6  

The highest of these is **12**, so the prospector should choose **hilltop digging**.

---

### What reasoning pattern is this?

| Term | What it means | How it shows up here |
|------|----------------|----------------------|
| **Maximax rule** | A decision‑making principle that maximizes the maximum possible payoff, ignoring probabilities and downside risk. 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies Hilltop Digging as the maximax choice (best case = 12) and accurately explains the mechanism of selecting the highest possible payoff. They explicitly note the risk-seeking/optimistic nature of the rule and highlight that it ignores downside risk and probabilities. F

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The scholar wants to avoid the worst possible evening. Apply maximin: for each act, find its worst outcome, then pick the act whose worst outcome is highest.

**Expected Answer:** **Maximin** — Maximin identifies the worst possible outcome for each act, then selects the act whose worst case is least bad. It is the pessimist's rule: raise the floor, ignore the ceiling. *The worst outcome for Watch Football is 1 (team loses, evening wasted). The worst outcome for Work on Paper is 2 (team wins, slight regret). Maximin selects the act with the higher minimum: Work on Pa*

**Model Response:**
> **Principle demonstrated:**  
The scholar is applying the **maximin (or “safety‑first”) decision rule** – a classic risk‑averse strategy from decision theory.

---

### How it works in this scenario

| Action | Outcome if team wins | Outcome if team loses | **Worst outcome** |
|--------|----------------------|-----------------------|-------------------|
| Watch football | 4 | 1 | **1** |
| Work on paper | 2 | 3 | **2** |

The maximin rule says: *for each possible action, look at its worst possible payoff, then pick the action whose worst payoff is the highest.*  
- Watching football has a worst payoff of 1.  
- Working on the paper has a worst payoff of 2.  

Since 2 > 1, the scholar chooses to **work on the paper**.

---

### Why this is a reasoning pattern, not a fallacy

- **Risk‑averse

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the maximin pattern, accurately calculates the minima for both acts (1 and 2), and selects the correct action (Work on Paper). The explanation clearly articulates the logic of choosing the highest worst-case payoff ('raises the floor'). However, the response does not

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
> **Step‑by‑step calculation**

| Settlement | Furs | Salted Fish | Iron Tools |
|------------|------|-------------|------------|
| Mining Camp | 18 | 6 | 10 |
| Fishing Village | 4 | 16 | 8 |
| Fortress | 3 | 5 | 14 |

1. **Find the best profit in each settlement**  
   - Mining Camp: **Furs** = 18  
   - Fishing Village: **Salted Fish** = 16  
   - Fortress: **Iron Tools** = 14  

2. **Compute the regret for each cargo**  
   Regret = (best profit in that settlement) – (profit of the chosen cargo)

| Cargo | Mining Camp | Fishing Village | Fortress | Max Regret |
|-------|-------------|-----------------|----------|------------|
| **Furs** | 18‑18 = 0 | 16‑4 = 12 | 14‑3 = 11 | **12** |
| **Salted Fish** | 18‑6 = 12 | 16‑16 = 0 | 14‑5 = 9 | **12** |
| **Iron Tools** | 18‑10 = 8 | 16‑8 = 8 | 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identified the minimax regret pattern, accurately computed the column maxima, built the full regret matrix without arithmetic errors, calculated the maximum regret for each act (12, 12, 8), and selected the correct option (Iron Tools). The explanation clearly articulates the lo

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The scholar says education might not increase productivity at all — it just signals pre-existing ability. Under what conditions does this signaling work? What is the key property that makes the signal credible?

**Expected Answer:** **Signaling (Spence's job market model)** — In a signaling game, an informed player (Sender) takes a costly action to reveal private information to an uninformed player (Receiver). Separation requires the Single Crossing Condition: the signal must be more costly for low types than high types. In Spence's model, education is the signal, abilit *Signaling theory explains why costly, seemingly wasteful behaviors persist: they provide information that enables better matching. The peacock's tail, college degrees, expensive advertising, and elabo*

**Model Response:**
> We need to answer: Under what conditions does this signaling work? What is the key property that makes the signal credible? And then "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to explain the conditions: separation equilibrium exists if there is a range of education e such that high types prefer to invest (cost low enough) and low types prefer not to invest. That requires cost differential: c_L > c_H. Also the cost must be such that high types find it worthwhile to invest to separate from low types, given the wage differential. The key property is that the signal is costly and differentially costly: the marginal cost is higher for low types, ensuring that only high types will pay the 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism of signaling: differential costs and the Single Crossing Condition (c_L > c_H). They explicitly mention the resulting range (20 < e < 60), showing they understand the bounds for separation. However, they fail to formally derive these bounds from th

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Question:** Standard theory says Responders should accept any positive offer. They do not. Why? And how do formal models of social preferences (like Fehr-Schmidt) explain both Responder rejections and Proposer fairness?

**Expected Answer:** **Behavioral game theory** — Behavioral game theory studies how real humans deviate from Nash equilibrium predictions. Key findings: (1) Ultimatum Game: people reject unfair offers at personal cost and anticipate this by making fair offers. (2) Level-k reasoning: people think a few steps ahead, not infinitely. (3) Social prefer *Standard backward induction assumes purely self-interested agents. Real humans have social preferences — they care about relative payoffs, fairness, and reciprocity. These preferences are not irration*

**Model Response:**
> **Why the responders reject**

1. **Standard theory (backward induction)**  
   * The game is solved by saying:  
     – The responder’s only choice is to accept or reject.  
     – Rejecting gives the responder 0, accepting gives him whatever the proposer offers.  
     – Therefore, if the responder is a purely self‑interested rational agent, he should accept *any* positive offer.  

2. **What actually happens**  
   * In the data a 1‑gold offer is rejected 80 % of the time, offers below 2 gold are rejected 55 % of the time, and the modal offer is 5 gold.  
   * The responder is not only looking at

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the discrepancy between standard theory and actual behavior, noting that fairness matters (Level 1). However, the response is incomplete and cuts off before explaining the mechanism (inequality aversion), defining Fehr-Schmidt parameters, or discussing proposer antic

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Without commitment, the Incumbent gets 2. With commitment, the Incumbent gets 3. How can removing an option make you better off? Explain the mechanism and give another example of a commitment device.

**Expected Answer:** **Commitment** — Commitment devices improve outcomes in strategic settings by making threats or promises credible. The Paradox of Commitment: having fewer options can be advantageous because it changes the opponent's best response. Types include contracts, reputation, precommitment, burning bridges, delegation, and  *Commitment is one of the most practically important concepts in game theory. It explains why binding yourself can be strategic: constitutions that are hard to amend, independent central banks, Odysseu*

**Model Response:**
> We need to answer: How can removing an option make you better off? Explain mechanism and give another example of commitment device. Also think through step by step: reasoning pattern, fallacy, bias, or principle being demonstrated. So we need to explain the mechanism: commitment reduces the set of actions, but can make threat credible, leading to better outcome. This is akin to "self-control" or "precommitment" in game theory. The principle: "commitment device" or "self-control problem" or "bounded rationality". The mechanism: by limiting future choices, you can influence others' beliefs about your future actions, making them anticipate a more favorable outcome. This is akin to "commitment to a strategy" or "credible threat" in game theory. Example: a firm committing to a low price to dete

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the mechanism (limiting options to make threats credible and influence opponent expectations) and provides multiple examples of commitment devices (contracts, burning bridges, etc.). However, the response fails to reach Level 3 or 4 because it does not clearly articu

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The instructor lists four conditions for reputation to sustain cooperation. What are they? If any one fails, how does cooperation break down? Give a real-world example of a reputation system and explain which conditions it satisfies.

**Expected Answer:** **Reputation and the shadow of the future** — Reputation is what others believe about your type or strategy based on past actions. In repeated games, reputation creates incentives for cooperation: defecting today earns a short-term gain but destroys future cooperation opportunities. The Folk Theorem shows that in infinitely repeated games (or g *Reputation is the informal counterpart of formal commitment. Where contracts bind through law, reputation binds through expectations. Online rating systems (eBay, Uber), professional networks, and com*

**Model Response:**
> **1. The four conditions the instructor lists**

| # | Condition | What it means in a game‑theoretic sense |
|---|-----------|------------------------------------------|
| 1 | **Repeated (or potentially future) interaction** | Players meet again, so today’s move can affect tomorrow’s payoff. |
| 2 | **Observability of defection** | Other players can see whether you cooperated or defected (public signal). |
| 3 | **Patient players

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the pattern of reputation and lists two of the four necessary conditions (repetition and observability). However, the response is incomplete: it cuts off while listing the third condition ('Patient players'), failing to define it, omit the fourth condition (punishmen

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Bob risks 2 gold to win 1 gold, with a total stake of 3 gold. If this bet is fair in Bob's eyes, what is his credence — his subjective probability — that the storm will come? Show the calculation.

**Expected Answer:** **Fair betting rate as credence** — A fair betting rate quantifies subjective probability. If an agent considers a bet fair (expected value zero), their credence in the proposition equals their potential loss divided by the total stake. Bob risks 2 gold on a 3 gold total stake, so his credence in the storm is 2/3. *Bob's willingness to risk 2 gold to win 1 gold on a total stake of 3 gold implies he considers the bet fair at a probability of 2/3. The formula is Pr(S) = Potential Loss / Total Stake = 2/3. If his t*

**Model Response:**
> **Bob’s credence**

Let  

* \(p\) = Bob’s subjective probability that a storm will come tomorrow.  
* If a storm comes, Bob wins Ally’s 1 gold.  
* If no storm comes, Bob loses the 2 gold he staked.

Bob considers the bet *fair* when his expected monetary gain is zero.  
So we set the expected value (EV) of the bet to 0 and solve for \(p\).

\[
\begin{aligned}
\text{EV} &= p \times (+1) \;+\; (1-p) \times (-2) \\
          &= p \;-\; 2 + 2p \\
          &= 3p - 2.
\end{aligned}
\]

Fairness ⇒ \(\text{EV}=0\):

\[
3p - 2 = 0 \;\;\Longrightarrow\;\; 3p = 2 \;\;\Longrightarrow\;\; p = \frac{2}{3}.
\]

**Answer:** Bob’s credence that a storm will come tomorrow is **\( \boxed{\tfrac{2}{3}} \)** (about 66.7 %).

---

### What reasoning principle is at work?

This is a textbook application of **

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern of using expected value to determine credence from a fair bet. They explicitly state the condition (EV=0), set up the equation correctly based on the stakes (winning 1, losing 2), and derive the correct answer of 2/3. The explanation of the reasoning prin

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The bookie's implied probabilities sum to 1.05. Explain why this guarantees the bookie a profit regardless of which horse wins. Then answer: if a gambler's personal credences summed to more than 1, how could someone exploit them?

**Expected Answer:** **Dutch Book argument** — A Dutch Book is a set of bets that guarantees a net loss for the agent regardless of the outcome. The Dutch Book theorem proves that if an agent's credences violate the axioms of probability (e.g., sum to more or less than 1 for an exhaustive partition), there exists a set of bets the agent consider *Mercer collects $210 in bets (each bettor pays at odds that imply the listed probabilities). No matter which horse wins, the payout is $200. Mercer pockets $10 guaranteed. From the gambler's side: if *

**Model Response:**
> We need to explain the bookie's profit guarantee: because odds are set such that the implied probabilities sum to >1, the bookie has overround. The bookie collects total stake S from bettors. Payouts: if horse i wins, payout is stake_i * (1 + odds). The bookie pays out total stake_i * (1 + odds). Since odds are set such that sum of implied probabilities >1, the expected payout is less than total stake. Actually, the overround ensures that the sum of implied probabilities >1, meaning the bookie has built in a margin. For any outcome, the bookie's payout is less than the total amount collected. For example, if all bets are on Gumption at 1:1, total stake S, payout 2S, but bookie collects S. But in general, the bookie sets odds such that the sum of implied probabilities >1. That means that fo

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies that implied probabilities summing to more than 1 creates a margin ('overround') for the bookie, satisfying Level 1. However, the response fails to reach Level 2 because the student cannot coherently explain the mechanism of guaranteed profit; they explicitly constru

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Nell says something doesn't add up. She's right. Look at the implied probabilities on Oliver's board. What mathematical rule do they violate, and what does that mean for anyone betting at these odds?

**Expected Answer:** **Axioms of probability** — The three axioms of probability require: (1) Non-negativity: all probabilities >= 0; (2) Normality: probabilities over the entire sample space sum to exactly 1; (3) Finite Additivity: for mutually exclusive events, P(A or B) = P(A) + P(B). Oliver's odds violate Axiom 2 because the implied probabilit *When probabilities violate Axiom 2 (normality), a Dutch Book becomes possible. Oliver collects $210 in bets but only pays out $200 regardless of winner. The gambler who accepts these odds as fair is g*

**Model Response:**
> **Rule violated**

The implied probabilities on a betting board must satisfy the basic axiom of probability:

> **The sum of the probabilities of all mutually‑exclusive outcomes must equal 1** (or 100 %).

In other words, if you add up the probabilities for every possible winner of the race, you should get exactly 1.0.  

In Oliver’s board the numbers add up to 1.05, which is greater than 1.0. That means the odds are **over‑rounded** – the bookmaker has inserted a built‑in margin.

**What it means for bettors**

Because the probabilities sum to more than 1, the odds are not “fair” in the sense of reflecting the true chances of each horse. The extra 0.05 (5 %) is the bookmaker’s *vig* or *house edge*. For any bet placed at these odds

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the specific axiom violated (normality/sum must equal 1) and calculates that the sum is 1.05. They also correctly explain the consequence: the creation of a bookmaker's margin (vig) which makes the odds unfair. This meets all criteria for Level 3. The response does n

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss and Lira are both using the word 'probability' but seem to mean different things. Are they contradicting each other, or could both be right? What exactly is the difference between what they are describing?

**Expected Answer:** **Subjective vs objective probability** — Objective probability (chance) refers to mind-independent features of the world — physical propensities, frequencies, quantum indeterminacies. Subjective probability (credence) refers to an agent's degree of confidence in a proposition, revealed through betting behavior. Both satisfy the same axioms *Both scholars are correct within their domains. Probability is genuinely ambiguous between chance (a physical property) and credence (a psychological state). The mathematical formalism — the three axi*

**Model Response:**
> **Short answer**

Voss and Lira are not actually arguing against each other; they are simply using the same word in two different senses.  
- Voss is talking about **objective (propensity/frequentist) probability** – a physical, measurable property of a system.  
- Lira is talking about **subjective (Bayesian) probability** – a degree of belief that depends on an agent’s information.

Because the word *probability* is semantically ambiguous, the two scholars are committing the **equivocation fallacy** (or, more generally, a *semantic ambiguity*).  If we interpret each speaker’s use of the term in the context that fits their discipline, both can be right.

---

### Step‑by‑step reasoning

| Step | What’s happening | Why it matters |
|------|------------------|----------------|
| 1 | **Voss 

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between objective chance (Voss) and subjective credence (Lira), correctly identifying one as a physical property and the other as a degree of belief. They also explicitly note that both are valid interpretations of probability, implying they satisfy the necessary fo

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms?

**Expected Answer:** **Principal Principle** — The Principal Principle (Lewis/Weatherson) states: if you know the objective chance of an event is x, your rational credence should be x, provided you have no inadmissible evidence (e.g., time travel, crystal balls). Formally: Pr(p | Ch(p)=x) = x. Cade knows Ch(Heads)=0.80 but sets Cr(Heads)=0.50, v *Cade's credences are internally consistent (they satisfy the axioms) but externally miscalibrated. The Principal Principle provides the missing norm: when objective chances are known, rational credenc*

**Model Response:**
> We need to analyze the scenario: Cade flips a biased coin that is certified to land heads 80% of the time. He bets on tails at even odds, believing it's 50-50. He has a gut feeling. The casino manager says Cade is not violating any law of logic; his credences add up to 1. He is not Dutch-Bookable. But is he rational? The question: "Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms? Think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

We need to identify the normative rationality principle that Cade violates. He is ignoring evidence (the coin's bias). He is ignoring 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cade is ignoring objective evidence (the 80% bias) and notes that his behavior violates norms beyond the three axioms of probability (coherence/Dutch Book). However, the response fails to identify the specific 'Principal Principle' required for Level 3. Instead,

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Calculate the expected utility of each option using the formula EU(Act) = sum of P(State) * U(Act|State). Which option should the healer choose, and why does it differ from what dominance reasoning would say?

**Expected Answer:** **Maximize Expected Utility (MEU)** — MEU weighs each outcome by its probability and sums to get the expected utility of each act. The agent selects the act with the highest expected utility. EU(Act) = P(S1)*U(Act|S1) + P(S2)*U(Act|S2) + ... *EU(Use Cream) = -35 and EU(Do Nothing) = -50. Since -35 > -50 (losing 35 silver is better than losing 50), the healer should use the cream. Notably, dominance reasoning would recommend Do Nothing (it *

**Model Response:**
> **Step‑by‑step calculation**

| Action | State | Probability | Utility (negative cost) |
|--------|-------|-------------|--------------------------|
| **Use Cream** | Rash clears | 0.85 | –20 silver |
| | Rash persists | 0.15 | –120 silver |
| **Do Nothing** | Rash clears | 0.50 | 0 silver |
| | Rash persists | 0.50 | –100 silver |

Expected utility (EU) is the sum of *P(state) × U(action|state)*.

*Cream*  
\[
EU_{\text{cream}} = 0.85(-20) + 0.15(-120) = -17 - 18 = -35 \text{ silver}
\]

*Do Nothing*  
\[
EU_{\text{nothing}} = 0.5(0) + 0.5(-100) = 0 - 50 = -50 \text{ silver}
\]

Because a lower (more negative) number means a higher monetary cost, the **

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly sets up the MEU formula, performs the arithmetic accurately (EU(Cream) = -35, EU(Nothing) = -50), and identifies 'Use Cream' as the better option based on the lower cost. However, the response is incomplete; it cuts off mid-sentence at the end and lacks the deeper explanation r

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Captain Aldric's scout gave rankings but not numbers. Why is that not enough for a good decision here? What additional information would you need, and how would it change the analysis?

**Expected Answer:** **Cardinal vs ordinal utility** — Ordinal utility provides only a ranking: A > B > C. Cardinal utility assigns numerical values that capture how much better A is than B. Decision rules like Maximin and Maximax use ordinal utility and are therefore blind to magnitude. MEU requires cardinal utility because it multiplies utility by pro *With ordinal utility, the ranking is Hilltop > Bridge > Ravine in both states, so all rules agree on Hilltop. But the magnitude matters: Hilltop's advantage over Bridge in the North scenario (20 vs 12*

**Model Response:**
> We need to analyze the scenario. The captain has three defensive positions: Hilltop, Bridge, Ravine. Scout ranks them by desirability but cannot quantify differences. The scout says Hilltop > Bridge > Ravine in both cases (north or south). But the worst-case outcomes differ: For Hilltop, worst case is enemy from south, slightly below Bridge. For Ravine, worst case is enemy from north, catastrophic. Maximin chooses the position with best worst-case. But maximin only sees rankings, not distances. So the scout's ranking alone is insufficient because it doesn't capture the magnitude of differences. The captain needs quantitative estimates of outcomes: e.g., expected casualties, probability of success, or utility values. The decision rule (maximin) requires numerical values to compare worst-cas

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core pattern (ordinal vs. cardinal utility) and explains that rankings ignore magnitude, which is crucial for distinguishing between 'slightly worse' and 'catastrophic' outcomes. They provide plausible hypothetical cardinal values (-10, -12, -100) to illustrate t

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Kael calls Sera irrational because she turns down a bet with higher expected monetary value. Is he right? Or is there a way to explain Sera's preference that is perfectly consistent with maximizing expected utility?

**Expected Answer:** **Risk aversion and utility curves** — Under MEU, risk attitude is encoded in the shape of the utility function. A linear utility function (U = wealth) produces risk neutrality. A concave function (e.g., U = sqrt(wealth)) produces risk aversion: the utility of the expected value exceeds the expected utility of the gamble. Sera's declinin *Sera is not irrational. Her utility function is concave (diminishing marginal utility), so she values certainty more than a gamble with the same expected monetary value. With U=sqrt(x): EU(Stay)=20.0 *

**Model Response:**
> **Short answer**

No.  Kael’s claim that “Sera is irrational” is a *mis‑reading of rationality*.  
Sera is simply maximizing **expected utility** with a concave (diminishing‑marginal‑utility) utility function.  
Kael is committing the *expected‑value fallacy* – treating the arithmetic mean of money as the only rational criterion and ignoring risk preferences.

---

## Step‑by‑step reasoning

| Step | What is happening | Why it matters |
|------|-------------------|----------------|
| 1 | **Two options** – a gamble (50 % chance of 1000 g, 50 % chance of 0) vs

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Sera is rational and explicitly links this to maximizing expected utility with a concave utility function (diminishing marginal utility). This satisfies the Level 3 criteria. However, the response is incomplete (cut off mid-sentence in the step-by-step section) 

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** John keeps cycling through ice cream trades and losing money. What structural property of his preferences allows the vendor to exploit him? What would John need to change about his preferences to stop the bleeding?

**Expected Answer:** **Transitivity and money pumps** — Transitivity requires: if A > B and B > C, then A > C. John's preferences violate transitivity (S > C, C > V, but V > S). The money pump shows that intransitive preferences are exploitable: an agent can be led through a cycle of individually rational trades that return them to the starting point min *Each individual trade is rational by John's own lights — he always trades for something he prefers. But the cycle as a whole is irrational: he ends up with the same item and less money. The money pump*

**Model Response:**
> We need to analyze the scenario: John has three flavors: Strawberry, Chocolate, Vanilla. He has preferences that are cyclic: Strawberry > Chocolate > Vanilla > Strawberry. This is a non-transitive preference cycle. The vendor exploits this by offering trades that move him along the cycle, each time he pays copper. Because his preferences are non-transitive, he will always accept a trade that gives him a more preferred flavor relative to his current one, even though overall he ends up worse off in terms of money. The structural property is non-transitive preferences, or cyclical preferences. The vendor can exploit by offering a sequence of trades that each time he prefers the new item over the old, but the cycle returns him to the starting item with a net loss. This is an example of the "no

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core pattern (cyclic/non-transitive preferences: S > C > V > S) and explains the money pump mechanism (locally rational trades leading to a global loss). They explicitly name 'non-transitivity' as the structural property and suggest adopting transitive preference

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin asks how removing an option nobody chose can change the recommendation. What principle is being violated here, and why does MEU avoid this problem?

**Expected Answer:** **Independence of Irrelevant Alternatives (IIA)** — IIA states: if option C is chosen from set S, then C should still be chosen from any subset of S containing C. Minimax Regret violates IIA because regret is calculated relative to the best available option in each state. When the menu changes, the reference point changes, which can reverse preferenc *MEU satisfies IIA because each option's expected utility depends only on its own payoffs and the state probabilities, not on what other options are available. Minimax Regret violates IIA because regre*

**Model Response:**
> We need to identify the principle being violated: The principle that removing an unchosen alternative should not change the relative preference between remaining alternatives. This is related to the "Independence of Irrelevant Alternatives" (IIA) principle in decision theory and social choice theory. In decision theory, IIA says that if a decision maker prefers option A over B when both are available, then removing a third option C should not change that preference. This is also known as the "non-dominance" or "irrelevant alternative" principle. The scenario shows that the decision maker's preference between Baseball and Movies changes when Picnic is removed, even though Picnic was not chosen. This violates IIA.

Why does MEU avoid this problem? Because MEU uses expected utility with a fix

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Independence of Irrelevant Alternatives (IIA) principle and accurately explains the mechanism: Minimax Regret violates IIA because regret is relative to the best available option (which changes when the menu changes), whereas MEU avoids this because expected util

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Father Clement's argument seems airtight — infinity times anything positive is infinity. But Dara is not convinced. What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?

**Expected Answer:** **Pascal's Wager** — Pascal's Wager applies MEU with infinite utility. When any outcome has infinite value, the expected utility calculation is dominated by that outcome regardless of its probability (as long as P > 0). This 'washing out' effect makes MEU insensitive to evidence — a feature that many consider a reductio *The Wager has several structural problems: (1) The many-gods objection: multiple incompatible religions offer infinite rewards, so the argument cannot uniquely recommend one faith. (2) The washing-out*

**Model Response:**
> We need to answer: "What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?" We need to think through step by step, identify reasoning pattern, fallacy, bias, principle. Provide explanation.

We need to consider objections: infinite outcomes, measure of utility, infinite expectation, non-commensurability, infinite values, non-additivity, infinite vs finite, infinite utility not comparable, infinite expectation not well-defined, paradox of choice, infinite expected utility not meaningful, infinite reward vs infinite cost, infinite expectation not finite, infinite values lead to indeterminate forms, infinite expectation can be manipulated, ignoring probability distribution, ignoring other outcomes, ignoring other beliefs, ignoring 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core structural issue: that Expected Utility Theory (EUT) relies on real numbers and cannot rigorously handle infinite values, rendering the calculation undefined or invalid. They also raise the objection regarding belief not being a voluntary action (epistemic v

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** The expected value is infinite, but you would not pay a million gold to play. What has gone wrong? Is expected value the wrong tool, or are we applying it to the wrong quantity?

**Expected Answer:** **St. Petersburg Paradox** — A fair coin is flipped until heads. Payoff = 2^n where n is the number of flips. Expected value = sum from n=1 to infinity of (1/2)^n × 2^n = sum of 1 = infinity. Yet no reasonable person would pay more than about 20-30 gold. The paradox reveals that expected monetary value is not the same as expect *Expected monetary value diverges to infinity, suggesting unlimited willingness to pay. This is absurd — it would recommend mortgaging everything for a game that usually pays 2 or 4 gold.*

**Model Response:**
> We need to analyze the scenario: gambler offers a game with infinite expected value. The question: why wouldn't you pay a million? What has gone wrong? Is expected value wrong tool? Or wrong quantity? We need to think about reasoning pattern, fallacy, bias, principle. This is a classic St. Petersburg paradox. The expected value is infinite, but rational players would not pay large amounts. The paradox arises because expected value is not a good measure when the distribution is heavy-tailed and the utility function is concave. The expected utility principle: we should maximize expected utility, not expected monetary value. The gambler's offer is essentially a St. Petersburg paradox. The reasoning pattern: ignoring risk aversion, ignoring utility, ignoring the fact that the game has infinite

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the scenario as the St. Petersburg paradox and recognizes that expected monetary value diverges while willingness to pay remains low. They mention the correct resolution concepts (diminishing marginal utility, expected utility theory). However, the response fails to 

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The showmaster says choosing Gamble 1 and Gamble 4 is inconsistent. Can you see why? What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

**Expected Answer:** **Allais Paradox (Certainty Effect)** — The Allais Paradox demonstrates that people overweight certainty. In Choice 1, Gamble 1 offers certainty ($1M guaranteed), which has disproportionate psychological appeal. In Choice 2, neither option is certain, so people chase the higher payoff (Gamble 4). But the 89% column (Tickets 12-100) is ide *The preference pair (G1>G2 and G4>G3) violates the Sure Thing Principle: if outcomes are identical in some states, those states should not affect the preference. Once the 89% column is masked, both ch*

**Model Response:**
> We need to analyze the scenario. The showmaster presents two choices: Choice 1: Gamble 1 vs Gamble 2. Choice 2: Gamble 3 vs Gamble 4. The showmaster says most people choose Gamble 1 over 2, and Gamble 4 over 3. But these two choices together are mathematically inconsistent under Expected Utility Theory.

We need to explain why choosing Gamble 1 and Gamble 4 is inconsistent. What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

We need to think about the structure. Let's define the outcomes for each ticket:

- Ticket #1: In Gamble 1: 1,000,000 gold (since all tickets pay). In Gamble 2: 0 gold.

- Tickets #2-11: In Gamble 1: 1,000,000 gold. In Gamble 2: 5,000,000 gold.

- Tickets #12-100: In Gamble 1: 1,000,000 gold. In Gamble 2: 1,000,000 gold.



**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the structural similarity between the two choices, explicitly noting that the column for Tickets 12-100 is identical in both pairs and should theoretically cancel out. They recognize that this leads to a mathematical inconsistency under Expected Utility Theory. Howev

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss shows that you should accept the bet unconditionally but reject it in every conditional state. Is the Sure Thing Principle actually violated here? Look carefully at whether the conditioning events form a proper partition.

**Expected Answer:** **Sure Thing Principle** — STP states: if A is preferred to B conditional on E, and A is preferred to B conditional on NOT-E, then A is preferred to B unconditionally. It is the backbone of independence in MEU. The Disjunction Effect appears to violate STP but actually involves overlapping (non-exclusive) conditioning events, *STP is not violated here because 'at least one H' and 'at least one T' are NOT mutually exclusive — they overlap on {HT, TH}. The overlap contains only losing outcomes. Each conditional eliminates a w*

**Model Response:**
> We need to analyze the scenario: Sure Thing Principle (STP) states: if you prefer action A to action B given event E, and also prefer A to B given not-E, then you prefer A to B regardless of knowledge of E. The puzzle: bet on two fair coin flips: win 5 gold if both match, lose 4 otherwise. EV = 0.5 gold, so accept. But if you know at least one coin is heads, winning probability drops to 1/3 (since outcomes: HH, HT, TH, TT; given at least one heads eliminates TT, leaving HH, HT, TH; only HH wins => 1/3). EV = 1/3*5 + 2/3*(-4) = 1.6667 - 2.6667 = -1.0. So reject. Similarly if at least one tails, same. So you reject in both conditional states. So you reject given E, reject given not-E, but should accept unconditionally. That seems to violate STP. But the catch: E and not-E must partition the 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: the Sure Thing Principle (STP) is not violated because the conditioning events ('at least one H' and 'at least one T') overlap and do not form a partition. They explicitly calculate the intersection ({HT, TH}) and explain that STP requires mutuall

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Are you a one-boxer or a two-boxer? Whatever you choose, you must defend your reasoning against the strongest version of the opposing argument. What principle are you relying on, and what are you giving up?

**Expected Answer:** **Newcomb's Problem** — Newcomb's Problem pits Dominance against Expected Utility when states are correlated with acts. Causal Decision Theory (CDT) says: the Predictor's choice is fixed, so taking both dominates (you are 1,000 gold richer regardless). Evidential Decision Theory (EDT) says: one-boxing provides strong evide *There is no consensus — this is a genuine philosophical puzzle. CDT says two-boxing is rational because you cannot cause the past to change. EDT says one-boxing is rational because it manages the evid*

**Model Response:**
> We need to respond to the scenario: choose one-box or two-box. Provide reasoning, defend against strongest opposing argument. Identify principle being relied on, and what is given up. Also discuss reasoning pattern, fallacy, bias, principle being demonstrated. So we need to analyze the scenario: it's the famous Newcomb's paradox. The question: Are you a one-boxer or a two-boxer? Provide reasoning and defense. Also identify principle being relied on, what you give up. Also think through step by step. Also ask: "What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning." So we need to discuss the reasoning pattern of the scenario: Newcomb's paradox, the conflict between causal decision theory (CDT) and evidential decision theory (EDT). The one-box

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the scenario as Newcomb's Paradox and articulates the two opposing arguments: Causal Decision Theory (dominance/fixed contents) vs. Evidential Decision Theory (correlation/evidence). This satisfies Level 2. However, the response fails to reach Level 3 or 4 due to sev

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The dealer says choosing G1 and G4 is inconsistent. Can you see why? What probability would you need to assign to Black to justify G1 over G2? And what probability would you need for G4 over G3? Can both be true?

**Expected Answer:** **Ellsberg Paradox (Ambiguity Aversion)** — The Ellsberg Paradox shows that people prefer known risk (Red: exactly 1/3) over ambiguous risk (Black: unknown proportion). Preferring G1>G2 implies P(Black)<1/3. Preferring G4>G3 implies P(Black)>1/3 (because Yellow cancels out as common consequence). These two implications are contradictory — no  *The preference pattern (G1>G2, G4>G3) violates subjective expected utility because no single probability assignment to Black is consistent with both preferences. This reveals that humans distinguish b*

**Model Response:**
> We need to analyze scenario: 90 balls, 30 red, 60 black or yellow unknown mix. So probability of red = 30/90 = 1/3. Probability of black + yellow = 60/90 = 2/3. But we don't know proportion of black vs yellow. So probability of black is unknown, say p. Then probability of yellow = 2/3 - p. So p ∈ [0, 2/3].

Now consider gambles:

G1: win 100 gold if Red drawn. So expected value = 100 * P(Red) = 100 * 1/3 = 33.33.

G2: win 100 gold if Black drawn. EV = 100 * p.

So G1 > G2 if 1/3 > p, i.e., p < 1/3. So to prefer G1 over G2, you need to believe black probability less than 1/3.

G3: win 100 gold if Red or Yellow drawn. Probability = P(Red or Yellow) = P(Red) + P(Yellow) = 1/3 + (2/3 - p) = 1 - p. So EV = 100 * (1 - p).

G4: win 100 gold if Black or Yellow drawn. Probability = p + (2/3 - p) = 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly derives the mathematical contradiction: G1>G2 implies P(Black)<1/3, while G4>G3 implies P(Black)>1/3. They explicitly state that no single probability assignment can satisfy both preferences. Furthermore, they correctly identify 'ambiguity aversion' as the psychological mechani

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The expected values are the same within each pair, yet the merchants' risk preferences flip. What does this tell you about the shape of the human utility function? Can a single curve explain both patterns?

**Expected Answer:** **Reflection Effect** — The Reflection Effect shows that people are risk-averse when choosing among gains (prefer sure $500 over 50/50 shot at $1000) but risk-seeking when choosing among losses (prefer 50/50 shot at losing $1000 over sure loss of $500). Under MEU, a utility function is either consistently concave (always r *A single concave utility function predicts risk aversion everywhere. A single convex utility function predicts risk seeking everywhere. The data shows a split: concave for gains, convex for losses. No*

**Model Response:**
> We need to analyze scenario: merchants choose sure gain vs gamble with equal EV. They prefer sure gain. For losses, they prefer gamble (risk-seeking). This is classic "reflection effect" from prospect theory: people are risk-averse for gains, risk-seeking for losses. The question: "What does this tell you about shape of human utility function? Can a single curve explain both patterns?" The answer: The utility function must be concave for gains and convex for losses, or more generally a reference-dependent utility with diminishing sensitivity. A single global utility function cannot capture both; need piecewise or reference-dependent. So the shape is S-shaped: concave for gains, convex for losses. So the pattern is the reflection effect or the "prospect theory" effect. The reasoning pattern

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'reflection effect' and explicitly describes the S-shaped value function (concave for gains, convex for losses). They accurately explain that a single global utility function cannot account for this behavior, thereby identifying the violation of Expected Utility 

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** You reject the bet when you know at least one is heads, and you reject when you know at least one is tails. One of these must be true. So why should you accept unconditionally? Where is the flaw in reasoning from conditionals to the unconditional?

**Expected Answer:** **Disjunction Effect** — The Disjunction Effect occurs when an agent rejects an option conditional on each member of a non-exclusive partition but should accept it unconditionally. The resolution: 'at least one H' and 'at least one T' overlap on {HT, TH} — the losing outcomes. Conditioning on either event eliminates one win *The Disjunction Principle ('if you reject in every possible state, reject unconditionally') seems compelling but is false when the conditioning events overlap. It conflates overlapping evidence with a*

**Model Response:**
> We need to analyze the scenario. Two fair coins flipped. Payoff: +5 if match (HH or TT), -4 if differ (HT or TH). Unconditional expected value: compute probabilities: HH 1/4, TT 1/4, HT 1/4, TH 1/4. EV = 5*(1/4+1/4) + (-4)*(1/4+1/4) = 5*0.5 + (-4)*0.5 = 2.5 - 2 = 0.5. So accept.

Now conditional: Suppose you learn at least one coin is heads. That eliminates TT outcome. Remaining possibilities: HH, HT, TH. Among these, only HH yields win. So probability of win = 1/3. EV = 5*(1/3) + (-4)*(2/3) = 5/3 - 8/3 = -3/3 = -1. So reject.

Similarly, learning at least one is tails eliminates HH. Remaining: TT, HT, TH. Only TT yields win. Probability of win 1/3. EV = -1. So reject.

Now the puzzle: You know for certain that either at least one is heads OR at least one is tails. In each case you reject.

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: the events 'at least one H' and 'at least one T' are not mutually exclusive and overlap on the losing outcomes ({HT, TH}). They explicitly state that the Law of Total Expectation requires a partition and that applying it to overlapping events is t

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Three traders received the same bonus but feel differently. Standard economic theory says Basil should be happiest (highest wealth). What is actually determining their reactions, and what does standard theory miss?

**Expected Answer:** **Reference points** — Under Prospect Theory, outcomes are evaluated as gains or losses relative to a reference point — typically the status quo, an expectation, or an aspiration level. The same objective outcome can feel like a gain or a loss depending on the reference point. Cara's 5,000 gold bonus is objectively a gain *Cara's bonus is a gain in absolute terms. Standard MEU, which evaluates total wealth, would predict satisfaction. But Prospect Theory correctly predicts dissatisfaction because value is computed from *

**Model Response:**
> **What is really driving the traders’ feelings?**  
They are judging the bonus against a *reference point* – the bonus they expected – and then feeling the *size of the deviation* from that expectation.  

- **Anika** had no particular expectation for a 5 k bonus, so the 5 k is a *positive surprise* relative to her reference point.  
- **Basil** expected a 5 k bonus (or at least was content with it), so the 5 k is a *neutral or mildly positive* outcome.  
- **Cara** expected a 10 k bonus; the 5 k is a *negative surprise* – a shortfall relative to her reference point – and she feels angry.

In other words, the traders are evaluating **“gains or losses relative to what they thought would happen,”** not just the *absolute* amount of money they now hold.

**What standard theory misses**

Stand

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies 'reference points' as the core mechanism, correctly explains that value is derived from deviations from expectations rather than absolute wealth, and accurately categorizes each trader's experience (including Cara's psychological loss despite an objective gain). The

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Lira's patrons demand 40-50 gold to accept a bet that could lose them 20. Risk aversion explains some of this, but not all. What additional psychological mechanism is at work, and how does it show up in the shape of the value function?

**Expected Answer:** **Loss aversion** — Loss aversion means that losses are felt more intensely than equivalent gains. Formally, the value function is steeper below the reference point than above it: |v(-x)| > v(x) for x > 0. The empirical coefficient is approximately lambda = 2.25, meaning losing $100 hurts as much as gaining $225 feels  *Standard MEU with risk-neutral preferences predicts acceptance at G=20. Risk aversion alone might push G to 25-30. The demand of 40-50 requires loss aversion — the disproportionate weight given to los*

**Model Response:**
> We need to identify the psychological mechanism beyond risk aversion that explains why people demand a high gain to accept a bet that could lose them 20 gold. The scenario: Lira flips a fair coin; if tails, lose 20 gold; if heads, gain X gold. People demand X around 40-50 gold. Standard expected value: fair bet would be X=20. Risk aversion would raise threshold slightly. But people demand 40-50. Lira says it's loss aversion: pain of losing 20 is roughly equivalent to pleasure of gaining 45. Loss aversion lambda ~2.25. But the question: "What additional psychological mechanism is at work, and how does it show up in the shape of the value function?" So beyond loss aversion, maybe "probability weighting" or "reference dependence" or "prospect theory" shape: concave for gains, convex for losse

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies 'loss aversion' as the primary mechanism and notes the steeper slope for losses compared to gains. They also mention the lambda coefficient (~2.25). However, the response is highly confused and circular, repeatedly questioning whether loss aversion is the answer desp

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weighting resolve the contradiction?

**Expected Answer:** **Probability weighting function** — In Prospect Theory, objective probabilities are transformed by a weighting function pi(p) before being used in calculations. Small probabilities are overweighted (pi(0.01) > 0.01), large probabilities are underweighted (pi(0.99) < 0.99), and the endpoints 0 and 1 are treated categorically. The resul *Under MEU with objective probabilities, buying lottery tickets with negative EV and buying insurance against rare events are both irrational. Probability weighting explains both as rational under dist*

**Model Response:**
> We need to answer: The scenario: Under MEU (expected utility theory), a person buying lottery tickets (seeking risk for small-probability gains) and buying insurance (avoiding risk for small-probability losses) seems contradictory: one is risk-seeking, the other risk-averse. But probability weighting resolves the contradiction: because people overweight small probabilities, so they overvalue the small chance of winning the lottery (gain) and also overvalue the small chance of a loss (rare disaster), leading to buying insurance. So the same distortion explains both behaviors. The question: "The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weigh

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that probability weighting resolves the contradiction by explaining that people overweight small probabilities for both gains (lottery) and losses (insurance). However, the response fails to reach Level 3 because it does not describe the full inverse-S shape (specifi

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** Lira says the same person can rationally buy lottery tickets and insurance. Under MEU, this is a contradiction. How do the value function and probability weighting function together produce four distinct risk profiles?

**Expected Answer:** **Fourfold Pattern of risk attitudes** — The Fourfold Pattern emerges from combining: (1) The S-shaped value function (risk-averse for gains, risk-seeking for losses) with (2) The probability weighting function (overweight small p, underweight large p). Low-probability gains: overweighting makes the prize loom large → risk seeking. Low-pro *MEU predicts a single consistent risk attitude. The Fourfold Pattern shows four different attitudes from one person, determined by the domain (gains/losses) and the probability level (low/high).*

**Model Response:**
> We need to answer: Lira says same person can rationally buy lottery tickets and insurance. Under MEU, contradictory. How do value function and probability weighting produce four distinct risk profiles? Think step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? So we need to explain the fourfold pattern: risk seeking in gains at low probability, risk averse in gains at high probability, risk averse in losses at low probability, risk seeking in losses at high probability. This arises from Prospect Theory's value function (concave for gains, convex for losses) and probability weighting function (overweight small probabilities, underweight large). The combination yields four quadrants. The reasoning pattern: "cognitive dissonance"? Actually it's about the "f

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Fourfold Pattern and accurately explains the underlying mechanisms: the S-shaped value function (concave for gains, convex for losses) and the probability weighting function (overweighting small probabilities, underweighting large ones). They successfully map the

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** The councillors in Group A and Group B made opposite choices about the same programs. What changed between the two presentations, and why does it matter for rational decision-making?

**Expected Answer:** **Framing effects** — Framing effects occur when logically equivalent descriptions of the same situation lead to different decisions because they shift the reference point. A gains frame activates risk aversion (prefer the sure outcome). A losses frame activates risk seeking (prefer the gamble). Since the underlying opti *Rational decisions should depend on outcomes, not descriptions. Programs A and C have identical consequences, as do B and D. The preference reversal shows that the frame — not the substance — is drivi*

**Model Response:**
> We need to analyze the scenario: Two groups of councillors are presented with the same programs but framed differently: Gains vs Losses. Group A hears Gains: Program A: 200 saved; Program B: 1/3 chance of saving 600, 2/3 chance of saving none. Group B hears Losses: Program C: 400 will die; Program D: 1/3 chance that nobody dies; 2/3 chance that 600 die. The councillors choose differently: Group A chooses the sure thing (Program A), Group B chooses the gamble (Program D). The scribe points out that Programs A and C are identical (200 saved vs 400 die). Programs B and D are identical (1/3 chance of saving 600 vs 1/3 chance of nobody dying). Only words changed: saved vs die. The councillors reversed preference based on framing alone.

Question: "What changed between the two presentations, and

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the framing effect and explains the core mechanism: the shift in reference point (gains vs. losses) leads to risk aversion in the gains frame and risk seeking in the losses frame. They explicitly state that rational decision-making should be based on objective outcom

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Alec and Brin have the same amount of money and face the same bet, but they make opposite choices. What psychological mechanism explains the difference? Is Brin being rational or irrational?

**Expected Answer:** **Mental accounting** — Mental accounting (Thaler) is the tendency to treat money differently depending on which psychological 'account' it belongs to — savings, winnings, salary, found money, etc. Standard economics says money is fungible: a dollar is a dollar regardless of its source. Mental accounting violates fungibili *Money is fungible — 200 gold has the same purchasing power regardless of its source. Alec's savings and Brin's winnings are economically identical. The different treatment reflects a psychological par*

**Model Response:**
> We need to analyze the scenario: Alec has savings, Brin has house money. They both have 200 gold. They face a bet: 50% chance to double, 50% chance to lose all. Alec declines because it's his savings; Brin accepts because it's house money. The bartender says they have same amount, same bet, yet one refuses and the other accepts. Money is money — or is it? The question: What psychological mechanism explains the difference? Is Brin rational or irrational? Think about reasoning pattern, fallacy, bias, principle.

We need to identify the psychological mechanism: "Mental accounting" or "house money effect" or "endowment effect" or "loss aversion" or "prospect theory" or "reference dependence". The difference: Alec has savings, so he perceives the money as part of his essential wealth, whereas B

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'mental accounting' and the 'house money effect' as the mechanisms and explicitly explains the violation of economic rationality by noting that 'money is money' (fungibility) and that treating sources differently contradicts this. They also analyze the rationality th

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Sellers demand 7 gold and buyers offer 3 gold for the same mug. The mugs were randomly assigned. What psychological mechanism creates this gap, and why does standard economic theory have trouble explaining it?

**Expected Answer:** **Endowment effect** — The endowment effect is the observation that people demand more to give up an object they own than they would pay to acquire the same object. Sellers set a higher price (WTA: willingness to accept) than buyers (WTP: willingness to pay), even for identical items. The mechanism is loss aversion: once  *Rational markets require a single market-clearing price. The endowment effect creates a gap between WTA and WTP that prevents efficient trade. The mug has one objective value, but ownership distorts p*

**Model Response:**
> **The gap is produced by the *endowment effect* – the tendency for people to value an object more highly simply because they own it.**  
It is a concrete illustration of loss‑aversion and reference‑dependence that Prospect Theory (and later behavioral‑economics work) shows are systematic, not random, deviations from the “rational‑agent” benchmark.

---

### How the end

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the endowment effect and explicitly links it to the mechanism of loss aversion and reference dependence (ownership as the reference point). This meets the criteria for Level 3. However, the response does not include the specific lambda coefficient (~2.

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Darya insists on going skiing because she paid 300 gold. Her friend says the money is gone either way. Who is right, and what error is Darya making?

**Expected Answer:** **Sunk cost fallacy** — The sunk cost fallacy is the tendency to continue an activity because of past investment (time, money, effort) rather than future expected value. Under MEU, sunk costs are decision-irrelevant: only future costs and benefits should affect current choices. The fallacy arises from mental accounting — t *The 300 gold is gone regardless of the choice. Rational decision-making considers only future costs and benefits. Going skiing while sick produces less utility than the free cabin. Darya is letting a *

**Model Response:**
> **Mira is right.**  
Darya’s insistence on going skiing because she “has already spent” 300 gold is a textbook case of the **sunk‑cost fallacy** (sometimes called the “throw‑away‑money” or “just‑because‑I‑paid” bias).  

---

## Step‑by‑step reasoning

| Step | What Darya says | What the logic actually

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as the 'sunk-cost fallacy' and explicitly states that Darya's reasoning is flawed. However, the response is incomplete; it cuts off mid-sentence in the 'Step-by-step reasoning' table before explaining the mechanism (why the cost is decision-irrelevant) or

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Mirella knows holding back would be better for both, yet she strips the grove anyway. What structural feature of her situation makes cooperation so difficult?

**Expected Answer:** **Prisoner's Dilemma** — A symmetric 2-player game where individual rationality (dominant strategy D) leads both players to an outcome strictly worse than mutual cooperation. The unique Nash equilibrium is (D,D), yet (C,C) Pareto-dominates it. *Defecting is individually rational — higher payoff regardless of the other's choice. But when both follow this logic, they lock into (1,1), forgoing the mutually superior (3,3).*

**Model Response:**
> **The structural feature is the payoff structure that makes “defect” a dominant strategy – a classic Prisoner’s‑Dilemma setting.**

---

### Why that matters

| What the players can do | Payoff if both do it | Payoff if you do it but the other does the opposite |
|------------------------|----------------------|-----------------------------------------------------|
| **Cooperate** (harvest conservatively) | 3 gold each (shared, sustainable) | 0 gold (you get nothing, the other takes all) |
| **Defect** (strip the grove) | 1 gold each (both over‑harvest) | 5 gold (you get the bulk while the other gets nothing) |

Because the “defect” payoff (5 gold) is higher than the “cooperate” payoff (3 gold) **no matter what the other does**, rational self‑interested players will choose to defect. The t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Prisoner's Dilemma pattern and explicitly explains the dominant strategy mechanism (defecting yields higher payoffs regardless of the opponent's choice). They also note that mutual cooperation (3,3) is better than the mutual defection outcome (1,1), satisfying th

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks you to find the Nash Equilibrium. For each strategy pair, check: could either cadet do better by switching alone? Which pair survives this test?

**Expected Answer:** **Nash equilibrium** — A Nash Equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. In the PD above, (Fortify, Fortify) is the unique Nash Equilibrium: if A plays Fortify and B plays Fortify, A gets 1. If A switches to Patrol, A gets 0 (worse). Symmetrically fo *Nash Equilibrium captures the key insight of strategic stability: no player can do better by changing strategy alone. In the PD, Fortify dominates Patrol — regardless of what the opponent does, Fortif*

**Model Response:**
> We need to answer: find Nash equilibrium. Also identify reasoning pattern, fallacy, bias, or principle being demonstrated. The scenario: two cadets playing simultaneous-move game with payoff matrix. The instructor says it's a Prisoner's Dilemma. We need to find Nash equilibrium. For each strategy pair, check if either cadet can improve by switching alone. Which pair survives? That's standard: The Nash equilibrium is (Patrol, Patrol) because each has dominant strategy? Let's analyze.

Matrix:

- If both patrol: (3,3)
- A patrol, B fortify: (0,5)
- A fortify, B patrol: (5,0)
- Both fortify: (1,1)

We need to find best responses. For A: if B patrol, A's payoff: patrol 3, fortify 5 => best is fortify. If B fortify, A's payoff: patrol 0, fortify 1 => best is fortify. So A's dominant strategy is

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies (Fortify, Fortify) as the unique Nash Equilibrium and provides a rigorous step-by-step verification using best response analysis for both players, demonstrating a clear understanding that neither player benefits from unilateral deviation. They also correctly distingu

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?

**Expected Answer:** **Iterated PD and cooperation** — In a finitely repeated PD with known endpoint, backward induction predicts defection every round. But in an infinitely repeated PD (or one with unknown endpoint), the Folk Theorem shows that cooperation can be sustained as a Nash Equilibrium if players value future payoffs enough (discount factor de *Iteration changes everything. The shadow of the future creates incentives for cooperation: defecting today earns a short-term gain but triggers retaliation that reduces future payoffs. If the future i*

**Model Response:**
> We need to answer a question: "In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?" Also: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to answer the scenario: repeated PD changes because of future interactions, possibility of cooperation, reciprocity, etc. Axelrod's tournament: TFT wins because of nice, retaliatory, forgiving, clear properties. Biggest weakness: vulnerability to noise or mistakes, or to strategies that exploit TFT by starting with defection then cooperating, or to strategies that are more generous? Actually TFT's biggest weakness is that it can be exploited by s

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that repetition introduces future interactions and lists Tit-for-Tat's four key properties (nice, retaliatory, forgiving, clear). They also correctly identify the weakness regarding noise and error propagation. However, the response fails to reach Level 3 because it 

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find both Nash Equilibria in the Stag Hunt. Which is payoff-dominant? Which is risk-dominant? Which would you choose, and what does your choice depend on?

**Expected Answer:** **Stag Hunt** — The Stag Hunt (from Rousseau) has two pure-strategy Nash Equilibria: (Stag, Stag) = (5,5) and (Hare, Hare) = (2,2). (Stag, Stag) is payoff-dominant (better for everyone). (Hare, Hare) is risk-dominant (safer — you get 2 guaranteed regardless of partner). The core tension: cooperation requires trust. *Unlike the PD, neither strategy dominates. The optimal choice depends entirely on expectations about your partner. This is a coordination problem, not a cooperation problem.*

**Model Response:**
> **Nash equilibria**

| You | Partner | Payoff (You, Partner) |
|-----|---------|------------------------|
| Stag | Stag | 5, 5 |
| Hare | Hare | 2, 2 |

Both of these strategy profiles are Nash equilibria:  
* If you play **Stag**, your partner’s best reply is Stag (5 > 0).  
* If you play **Hare**, your partner’s best reply is Hare (2 > 3? actually 2 > 0, so Hare is a best reply to Hare).  
Thus the two pure‑strategy Nash equilibria are **(Stag, Stag)** and **(Hare, Hare)**.

---

### Payoff‑dominant equilibrium  
The equilibrium that gives each player the higher payoff is **(Stag, Stag)** (5, 5).  
It dominates the other equilibrium in terms of total welfare.

### Risk‑dominant equilibrium  
To decide risk dominance we compare the “size of the basin of attraction’’ for each equilibrium. 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies both pure-strategy Nash Equilibria ((Stag, Stag) and (Hare, Hare)). They accurately distinguish between the payoff-dominant equilibrium (Stag) and the risk-dominant equilibrium (Hare), explaining the underlying logic of guaranteed safety versus higher potential rewar

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find all Nash Equilibria in this game, including any mixed-strategy equilibrium. Why is the mixed equilibrium worse for both players than either pure equilibrium?

**Expected Answer:** **Battle of the Sexes** — Battle of the Sexes has two pure-strategy Nash Equilibria: (Opera, Opera) = (3,2) and (Tournament, Tournament) = (2,3). Both are coordination equilibria — both players prefer being together over being apart. But they disagree on which is better: Helena prefers (Opera, Opera), Roderick prefers (Tourn *Neither player has a dominant strategy. The choice depends on expectations about the other — creating a coordination problem with a distributional conflict.*

**Model Response:**
> We need to analyze the game. It's a coordination game with two players: Helena (H) and Roderick (R). Strategies: Opera (O) or Tournament (T). Payoffs: (H,R). Matrix:

- H: Opera, R: Opera => (3,2)
- H: Opera, R: Tournament => (0,0)
- H: Tournament, R: Opera => (0,0)
- H: Tournament, R: Tournament => (2,3)

So each prefers the other to go to their preferred event: H prefers Opera, R prefers Tournament. But they both prefer to go together over going alone. The payoff is 3 for H when both go to Opera, 2 for R. When both go to Tournament, H gets 2, R gets 3. So each gets higher payoff when they coordinate on their own preferred event.

Thus there are two pure strategy Nash equilibria: (Opera, Opera) and (Tournament, Tournament). Because if they coordinate on Opera, each has no incentive to dev

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the game pattern (Battle of the Sexes) and accurately calculates both pure-strategy Nash Equilibria and the mixed-strategy Nash Equilibrium, including the expected payoffs (1.2). They correctly explain that the mixed equilibrium is worse due to lower expected payoffs

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** You and your contact must meet without communication. Why do people converge on the same location and time? What property makes some answers more likely than others, and is this a rational process?

**Expected Answer:** **Focal points (Schelling points)** — A focal point is a solution to a coordination game that attracts players' attention because it is salient — prominent, unique, culturally significant, or symmetric. Focal points work because of mutual expectations: I go to the fountain because I expect you to expect me to expect... etc. Sources of s *Focal points solve the equilibrium selection problem in coordination games. When there are many Nash Equilibria and no communication, salience determines which equilibrium is played. The insight is th*

**Model Response:**
> **Why the convergence happens**

When two people have to pick a meeting place and time *without any way to talk to each other*, the only thing that can help them coordinate is something that is *common knowledge* to both of them.  
In the Archon example the Grand Fountain at noon is the most obvious, unambiguous, and culturally‑known “anchor” in the city. Everyone who has ever been in Archon knows that the fountain is the most prominent landmark and that noon is

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies salience and prominence ('obvious, unambiguous, culturally-known anchor') as the key factors for coordination, which aligns with Level 2. However, the response is incomplete (cuts off mid-sentence) and fails to explicitly articulate the mutual-expectation mechanism (

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid.

**Expected Answer:** **Convention (Lewis)** — A convention is a regularity R in behavior that is (1) followed by everyone, (2) expected by everyone, (3) preferred by everyone given others' conformity, (4) has at least one alternative R' that could have served instead, and (5) is common knowledge. Conventions are solutions to recurrent coordinat *Lewis's theory explains how arbitrary social practices persist and why they are rational to follow: given that everyone else conforms, conforming is your best response. This applies to language, money*

**Model Response:**
> We need to answer: "The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid."

Also: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to explain what a convention is, apply Lewis's conditions to driving on the right, show that left is equally valid, and then identify the reasoning pattern/fallacy/bias/principle being demonstrated. Likely the philosopher is demonstrating the "convention" concept, and maybe the "argument from convention" or "argument to the best explanation" or "conventionalism". The reasoning pattern might be "conve

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies and applies all five of Lewis's conditions for a convention to the driving example and explicitly explains why driving on the left is an equally valid alternative (arbitrariness). The response demonstrates a solid grasp of the coordination problem and common knowledg

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor has drawn the Entry Game tree. Identify the decision nodes, the branches, and the terminal payoffs. What information does each player have when they move?

**Expected Answer:** **Game trees (extensive form)** — A game tree represents a sequential game with nodes (decision points), branches (available actions), terminal nodes (outcomes with payoffs), and information sets (what each player knows when they move). Unlike the normal form (matrix), the extensive form explicitly represents the order of moves, whi *The extensive form reveals strategic structure that the normal form hides. In this game, the Incumbent's threat to Fight is visible but not credible — if the Entrant enters, the Incumbent prefers Acco*

**Model Response:**
> **1.  What the tree actually shows**

| Element | What it is | Where it appears in the tree |
|---------|------------|------------------------------|
| **Decision nodes** | Points at which a player must choose an action | 1. The very first node – the Entrant’s choice. 2. The node that the Incumbent reaches only if the Entrant has chosen *Enter*. |
| **Branches (actions)** | The possible moves a player can make from a decision node | 1. From the Entrant’s node: **Enter** or **Stay Out**. 2. From the Incumbent’s node (only reached after *Enter*): **Accommodate** or **Fight**. |
| **Terminal payoffs** | The numerical outcomes that result when the game ends | 1. *Stay Out* → payoff pair **(1, 3)** (Entrant = 1, Incumbent = 3). 2. *Enter* → *Accommodate* → **(2, 2)**. 3. *Enter* → *Fight* → **(

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the structural elements of the game tree (decision nodes, branches, and terminal payoffs) and accurately traces the paths, satisfying the criteria for Level 2. However, the response is incomplete; the second section regarding 'What each player knows when they move' i

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** Apply backward induction to the Entry Game. Start at the last decision node and work backward. What is the subgame perfect equilibrium? Why is the Incumbent's threat to Fight not credible?

**Expected Answer:** **Backward induction** — Backward induction solves extensive-form games by starting at the terminal nodes and working backward. At each decision node, the player is assumed to choose their optimal action. The resulting strategy profile is a subgame perfect equilibrium (SPE). In the Entry Game: (1) At Incumbent's node: Accom *Backward induction eliminates non-credible threats. (Stay Out, Fight) is a Nash Equilibrium but relies on the Incumbent's non-credible threat to Fight. Backward induction reveals that the Incumbent wo*

**Model Response:**
> **Step‑by‑step backward induction**

| Step | What we look at | Decision | Payoffs | Optimal choice |
|------|-----------------|----------|---------|----------------|
| 1 | **Last decision node** – the incumbent’s choice after the entrant has entered | Accommodate (2) or Fight (0) | Incumbent: 2 vs 0 | **Accommodate** (2 > 0) |
| 2 | **Entrant’s node** – the entrant knows the incumbent will accommodate if he enters | Enter (2) or Stay‑Out

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern of backward induction by starting at the Incumbent's node and determining the optimal choice (Accommodate). However, the response is incomplete: it fails to explicitly state the Entrant's resulting optimal choice (Enter) based on that anticipation, and it

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The Entry Game has two Nash Equilibria. The instructor says one of them relies on a non-credible threat. Which one, and why does SPE eliminate it?

**Expected Answer:** **Subgame perfect equilibrium** — SPE (Selten 1965) requires that a strategy profile be a Nash Equilibrium in every subgame. A subgame is any part of the game tree that forms a complete game on its own. SPE eliminates NE that rely on non-credible threats — strategies that would not be followed through if the relevant decision node w *SPE is a refinement of NE that captures credibility. A threat is credible only if the threatener would actually carry it out. SPE formalizes this by requiring optimality at every node, not just on the*

**Model Response:**
> **Which equilibrium is the “bluff” one?**  
The equilibrium that relies on a non‑credible threat is the **(Stay Out, Fight)** profile.  
In this outcome the incumbent’s strategy is “fight if the entrant enters.”  
But if the entrant actually enters, the incumbent’s payoff from *accommodating* (2) is higher than the payoff from *fighting* (0).  
So the incumbent would not follow through on the threat. The threat is therefore *empty* – it is never tested because the entrant stays out.

**Why SPE eliminates it**  
Subgame‑Perfect Equilibrium (Selten, 1965) requires that the strategy profile be a Nash equilibrium *in every subgame*, not just on the equilibrium path.  
When we look at the subgame that begins after the entrant has decided to enter, the incumbent’s optimal action is *accommodate*

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the non-credible threat (Stay Out, Fight), explains the payoff logic showing why fighting is suboptimal, and explicitly connects this to the formal definition of SPE requiring optimality in every subgame. The response stops just short of Level 4 because it does not d

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Question:** Apply backward induction to the Centipede Game. What does it predict? Do you find the prediction convincing? What assumption is doing the heavy lifting, and what happens if you relax it?

**Expected Answer:** **Centipede Game** — The Centipede Game is a sequential game where two players alternate between stopping (taking a smaller immediate payoff) and continuing (allowing the total payoff to grow). Backward induction predicts immediate stopping — the unique SPE. But this is paradoxical: both players would be much better off *Backward induction is logically valid given CKR, but the outcome (1,1) seems absurd when (4,4) is available through mutual cooperation. The paradox reveals that CKR may be too strong an assumption — o*

**Model Response:**
> We need to answer: apply backward induction to Centipede game, predict outcome: both players stop at first node, outcome (1,1). Is prediction convincing? What assumption is doing heavy lifting? What happens if relax it? Also discuss reasoning pattern, fallacy, bias, principle. So we need to explain backward induction, rationality, assumption of common knowledge of rationality, perfect information, deterministic payoffs, etc. The heavy lifting assumption is that players are perfectly rational and know each other's rationality (common knowledge). If we relax assumption of perfect rationality or common knowledge, we might get different predictions: e.g., players may cooperate, or use bounded rationality, or consider future payoffs, or use trust, or consider that the other might not play optim

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly applies backward induction to reach the (1,1) outcome and explicitly identifies 'Common Knowledge of Rationality' (CKR) as the critical assumption driving the paradox. They also discuss relaxing this assumption via bounded rationality and behavioral insights. However, the respo

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

**Expected Answer:** **Evolutionarily Stable Strategy (ESS)** — An ESS (Maynard Smith) is a strategy that, when adopted by almost all members of a population, cannot be invaded by any rare mutant strategy. Formally: S is ESS if for any mutant M, either (1) E(S,S) > E(M,S), or (2) E(S,S) = E(M,S) and E(S,M) > E(M,M). In Hawk-Dove with V<C, neither pure strategy i *ESS provides a concept of equilibrium that does not require rationality — only differential reproduction. Strategies that do better than average spread; those that do worse shrink. The mixed ESS emerg*

**Model Response:**
> We need to answer the question: Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

Also, the user asks: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning." So we need to identify the reasoning pattern, fallacy, bias, or principle being demonstrated. The scenario: The biologist draws the matrix, then checks ESS conditions. The reasoning pattern: The biologist uses the concept of ESS and calculates payoffs. They check pure strategies: For pure Hawk, they compare payoff of Hawk vs Hawk (-1) with payoff of Dove vs Hawk (0). Since Dove does better, pure Hawk is not ESS. For pure Dove, compare Dove 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that neither pure strategy is an ESS by comparing payoffs (Hawk vs Hawk < Dove vs Hawk, and Dove vs Dove < Hawk vs Dove). They accurately calculate the mixed ESS proportion as p = V/C = 4/6 = 2/3. However, the response falls short of Level 4 because it describes the 

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The biologist perturbs the Hawk population from 50% to 51%. Show that the system returns to 50% by calculating fitness for each strategy. What does this tell you about the stability of the mixed ESS?

**Expected Answer:** **Replicator dynamics** — The replicator dynamics models how strategy frequencies change over time based on fitness. The equation dx_i/dt = x_i(f_i - F) says: strategies that outperform average grow; those that underperform shrink. Key properties: (1) ESS are stable fixed points of replicator dynamics. (2) Not all fixed poin *The replicator dynamics provides the 'how' behind ESS — the mechanism by which populations reach (or fail to reach) equilibrium. It requires no rationality, only differential reproduction or imitation*

**Model Response:**
> **Step‑by‑step calculation**

1. **Set the perturbed frequencies**  
   - Hawks: \(x_H = 0.51\)  
   - Doves: \(x_D = 0.49\)

2. **Compute the expected payoff (fitness) of each strategy**  
   The payoff matrix for Hawk–Dove with \(V=2,\;C=4\) is  

   |          | Hawk | Dove |
   |----------|------|------|
   | **Hawk** | \(-1\) | \(2\) |
   | **Dove** | \(0\)  | \(1\) |

   *Hawk*  
   \[
   f_H = x_H(-1) + x_D(2) = 0.51(-1) + 0.49(2) = -0.51 + 0.98 = 0.47
   \]

   *Dove*  
   \[
   f_D = x_H(0) + x_D(1) = 0.51(0) + 0.49(1) = 0.49
   \]

3. **Compare with the average fitness**  
   The average fitness is

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly computes the fitness for both strategies (Hawk and Dove) at the perturbed frequency (p=0.51) and identifies that Dove outperforms Hawk. However, the response cuts off before comparing these values to the average fitness or drawing the necessary conclusion about the direction of

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In the evolutionary Stag Hunt, what determines whether cooperation or defection wins? Why does Skyrms call the cooperative equilibrium a 'social contract'? What factors help cooperation evolve?

**Expected Answer:** **Evolution of cooperation** — In evolutionary Stag Hunt, cooperation (Stag) can evolve if enough of the population already cooperates. The threshold is p=0.5 in standard payoffs. Above the threshold, cooperation is self-reinforcing; below, it collapses. This is the basin of attraction concept. Factors that help cooperation evolv *The evolution of cooperation shows that cooperative outcomes can emerge without rational deliberation — through selection, iteration, and correlation. This provides a different foundation for social o*

**Model Response:**
> **1.  What decides whether cooperation or defection wins in the evolutionary Stag Hunt?**

|  | Stag | Hare |
|---|---|---|
| **Stag** | 5, 5 | 0, 3 |
| **Hare** | 3, 0 | 2, 2 |

*The key determinant is the **initial frequency of Stag‑hunters** (the “cooperators”).*  
- Let \(p\) be the proportion of the population that plays Stag.  
- The expected payoff to a Stag‑hunter is \(E(S)=5p\).  
- The expected payoff to a Hare‑hunter is \(E(H)=3p+2(1-p)=p+2\).  
- Setting \(E(S)=E(H)\) gives the critical point \(p=0.5\).

Thus:

| Initial \(p\) | Dominant strategy that spreads | Final equilibrium |
|---|---|---|
| \(p>0.5\) | Stag (cooperation) | All‑Stag (cooperation) |
| \(p<0.5\) | Hare (defection) | All‑Hare (defection) |

The game has two pure Nash equilibria—(Stag,Stag) and (Hare,Hare)—and

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly calculates the threshold (p=0.5) and explains the concept of path dependence/basins of attraction in Question 1. However, the response to Question 2 is incomplete (cut off after the header), meaning the student fails to discuss factors promoting cooperation (iteration, assortme

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Torva says her profit from the sword is eighty gold. Is she right? What is she forgetting to account for?

**Expected Answer:** **Opportunity cost** — The opportunity cost of an action is the value of the next-best alternative forgone. Torva treats the sword's revenue (80 gold) as pure profit, but by choosing the sword she forgoes the 50-gold axle repair. Her net gain from choosing the sword over the axle is 80 - 50 = 30 gold, not 80 gold. The 50  *Every choice has a hidden cost: what you gave up to make it. Torva's sword commission is genuinely better than the axle repair, but by 30 gold, not by 80. Understanding this prevents her from overvalu*

**Model Response:**
> **Short answer:**  
No – she’s only looking at the *revenue* and forgetting the *costs*.  Profit is revenue minus all the costs that go into making the sword (materials, labor, overhead) and the *opportunity cost* of not doing the axle repair.  

---

### Why the “80‑gold” figure is wrong

| What Torva is doing | What she’s ignoring

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core concept of 'opportunity cost' and explicitly states that the 80-gold figure is wrong because it ignores the forgone axle repair. They distinguish between revenue and profit in this context. However, the response stops short of performing the specific calcula

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Hilde outproduces Oskar in both wheat and flax. She says trade cannot benefit her. Is she right? Calculate the opportunity costs and determine who should specialize in what.

**Expected Answer:** **Comparative advantage** — Hilde has absolute advantage in both goods, but comparative advantage depends on opportunity cost. Hilde's opportunity cost of 1 bolt of flax = 2 bushels of wheat (12/6). Oskar's opportunity cost of 1 bolt of flax = 4/3 bushels of wheat. Oskar has a lower opportunity cost for flax, so he has compara *Trade benefits do not require being equally productive. Even though Hilde is better at both crops, she benefits from specializing in the crop where her relative advantage is greatest (wheat) and tradi*

**Model Response:**
> **Step‑by‑step calculation**

|  | Wheat | Flax |
|---|---|---|
| **Hilde** | 12 bushels (per season) | 6 bolts |
| **Oskar** | 4 bushels | 3 bolts |

**1.  Opportunity cost of wheat**

*Hilde*  
12 wheat = 6 flax  → 1 wheat = 6/12 flax = **0.5 flax**

*Oskar*  
4 wheat = 3 flax  → 1 wheat = 3/4 flax = **0.75 flax**

**2.  Opportunity cost of flax**

*Hilde*  
6 flax = 12 wheat  → 1 flax = 12/6 wheat = **2 wheat**

*Oskar*  
3 flax = 4 wheat  → 1 flax = 4/3 wheat ≈ **1.33 wheat**

**3.  Comparative advantage**

- Hilde’s opportunity cost of wheat (0.5 flax) is lower than Oskar’s (0.75 flax).  
  → **Hilde has comparative advantage in wheat.**

- Oskar’s opportunity cost of flax (≈1.33 wheat) is lower than Hilde’s (2 wheat).  
  → **Oskar has comparative advantage in flax.**

**

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly calculates all opportunity costs for both agents and accurately identifies that Hilde has the comparative advantage in wheat while Oskar has it in flax. This meets all criteria for Level 3. However, the response stops after identifying the advantages and does not propose a spec

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?

**Expected Answer:** **Constrained optimization** — The problem is to minimize cost subject to constraints. Food constraint: 3R >= 15, so R >= 5 (minimum 5 ration packs). Torch constraint: 4T >= 8, so T >= 2 (minimum 2 torch bundles). Cost: 5R + 10T. Minimum cost = 5(5) + 10(2) = 25 + 20 = 45 gold. This satisfies both constraints and is within budget *Constrained optimization is the core microeconomic framework: maximize (or minimize) an objective function subject to binding constraints. Seren cannot simply buy everything — she must find the combin*

**Model Response:**
> We need to answer: "What reasoning pattern, fallacy, bias, or principle is being demonstrated here?" The scenario: we have a linear programming problem: minimize cost subject to constraints. The question: "Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?" Then: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to identify the reasoning pattern or fallacy. The scenario is about optimization. The question is: "What reasoning pattern, fallacy, bias, or principle is being demonstrated here?" So it's about the reasoning pattern used 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as constrained optimization/linear programming and accurately solves the mathematical problem (R=5, T=2, Cost=45), verifying that constraints are met. However, the response fails to reach Level 4 because it does not explicitly calculate or discu

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Each potion sells for 15 gold. The cost of each additional potion rises: 5, 8, 12, 16, 22. How many potions should Elara brew, and why?

**Expected Answer:** **Marginal analysis** — Marginal analysis compares the marginal benefit (MB) to the marginal cost (MC) of each additional unit. Brew if MB > MC; stop when MC >= MB. Revenue per potion (MB) = 15 gold. MC of potions: 1st=5, 2nd=8, 3rd=12, 4th=16, 5th=22. For potions 1-3, MB(15) > MC. For potion 4, MC(16) > MB(15). Elara shou *Marginal analysis prevents two errors: stopping too early (missing profitable units) and going too far (adding units that cost more than they earn). The fourth potion costs 16 gold but only earns 15 —*

**Model Response:**
> We need to analyze the scenario: Elara sells potions at 15 gold each. Costs: 5, 8, 12, 16, 22. She wants to decide how many to brew. The question: "How many should Elara brew, and why?" Then: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to answer: She should brew until marginal cost <= marginal revenue. Marginal revenue is 15 gold per potion. Marginal cost: 5, 8, 12, 16, 22. So she should brew up to 4 potions because the 4th cost 16 > 15, so stop at 3? Wait: 3rd cost 12 <= 15, 4th cost 16 > 15. So she should brew 3 potions. But maybe she could brew 4 because revenue 15 per potion, cost 16 for 4th, but total revenue 60, total cost 5+8+12+16 = 41, profit 19. For 3 potions, revenue 45, co

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the optimal quantity (3 potions) and applies the core logic of marginal analysis by comparing the marginal cost of the 4th unit (16) to the marginal revenue (15). They also verify the result by calculating total profit for both 3 and 4 units. However, the response do

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Captain Hale says she should let the others pay for the lighthouse oil. Her reasoning seems logical from her own perspective. What happens if every captain follows the same logic? Why does this situation arise?

**Expected Answer:** **Public goods and free riding** — The lighthouse is a public good: non-rival (one captain using the light does not diminish it for others) and non-excludable (you cannot prevent a non-paying captain from seeing the light). These properties create a free-rider incentive: each captain benefits from the lighthouse regardless of whether *Free riding is individually rational but collectively destructive. Hale's logic is valid for any single captain, but if universalized, it leads to a lighthouse going dark and all captains risking thei*

**Model Response:**
> **What would happen?**  
If every captain follows Hale’s line of reasoning, none of them will put any gold into the oil. The light will go out, and every boat will be lost. The “free‑rider” logic works for each individual, but it fails for the group.

**Why does this happen?**  
The lighthouse is a **public good**: it is non‑excludable (any boat in the channel can use it) and non‑rivalrous (one boat’s use doesn’t diminish another’s). Because the benefit is shared but the cost is not, each

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the collective failure (lighthouse goes dark) and explicitly names the 'free-rider' logic. They also correctly define the lighthouse as a public good with non-excludable and non-rivalrous properties. However, the response is incomplete (cutting off mid-sentence) and 

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Elder Yara says every family is acting sensibly, yet the lake is dying. How can individual rationality produce collective disaster? What is the structural problem?

**Expected Answer:** **Commons problems (Tragedy of the commons)** — Lake Mirren is a common-pool resource: rival (each fish caught is unavailable to others) but non-excludable (no family can be prevented from fishing). Each family captures the full benefit of each additional fish they catch but bears only a fraction of the cost (resource depletion shared across all  *The structural incentive to overextract is real and rational for each individual. The problem is not stupidity or greed but a misalignment between individual and collective incentives.*

**Model Response:**
> **What’s really going on?**

The families are each acting *rationally* in the sense that they are trying to get the most fish they can for themselves.  
But because the lake is a *common‑pool resource* whose capacity is fixed, the cost of taking an extra fish is borne by everyone, not by the person who takes it.  
When every family thinks “I’ll take a few more fish now, because if I don’t someone else will,” the result is that the lake is over‑exploited and eventually collapses.  

This is the classic **Tragedy of the Commons** – a *collective‑action problem* in which the incentive structure (no property rights, no enforcement of limits) makes the individually rational strategy the socially disastrous one.

---

### Why the reasoning pattern is a fallacy

1. **Fallacy of Composition**  
  

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as the Tragedy of the Commons and explicitly defines the resource as a 'common-pool resource.' They accurately explain the core mechanism: the asymmetry where private benefits are internalized while costs (depletion) are shared externally. Furthermore, th

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Sera and Brenn create 80 gold in surplus from trade. Sera's outside option gives her 15 gold surplus; Brenn's gives him 10. How should they split the 80 gold surplus, and why?

**Expected Answer:** **Bargaining and fairness (Nash bargaining)** — The surplus from trade is 80 gold. Each merchant's outside option (BATNA) sets a floor: Sera will not accept less than 15 gold surplus (her alternative deal), and Brenn will not accept less than 10. The remaining surplus after securing both outside options is 80 - 15 - 10 = 55 gold. Nash bargaining  *Bargaining theory shows that fair division depends not just on the total surplus but on each party's outside option. Better alternatives give you more bargaining power. This framework prevents the nai*

**Model Response:**
> We need to answer: split the surplus 80 gold between Sera and Brenn, given outside options: Sera 15, Brenn 10. So the total outside options sum to 25. The surplus is 80. The total net gain from trade over outside options is 80 - 25 = 55. They should split the 55 proportionally to their outside options? Actually, typical bargaining solution: split the surplus such that each gets at least their outside option. The "fair" split might be equal division of the total surplus? But the outside options differ. The Nash bargaining solution: maximize product of gains over outside options. Gains: Sera gets 15 + x, Brenn gets 10 + (80 - x). We maximize (x + 15)*(90 - x). Wait check: total surplus 80. If Sera gets x, Brenn gets 80 - x. Their total payoff: Sera: 15 + x, Brenn: 10 + (80 - x) = 90 - x. The

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that outside options act as floors and calculates the net surplus (55). However, they fundamentally misunderstand the Nash bargaining solution mechanism. Instead of splitting the *remaining* surplus equally (adding 27.5 to each outside option), the student incorrectl

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Lady Ashworth paid Corbin a flat wage and got a poor harvest. She suspects shirking but cannot prove it. What is the structural problem with her contract, and how might she redesign it?

**Expected Answer:** **Principal-agent problems and moral hazard** — The principal (Ashworth) delegates a task to an agent (Corbin) whose effort she cannot observe. Under a flat wage, the agent bears the cost of effort but captures none of the benefit (the extra apples go to the principal). This misalignment of incentives is moral hazard: the agent has both the oppor *Corbin is not necessarily lazy or dishonest — the contract structure gives him no reason to exert effort. The problem is the incentive design, not the person.*

**Model Response:**
> We need to answer: structural problem with contract, redesign. Also ask: "What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning." So we need to identify the reasoning pattern used by Lady Ashworth? She says: "He had no reason to push himself. If the harvest was big, I got the extra apples and he got his fifty gold. If it was small, I lost the apples and he still got his fifty gold." This is an example of a "moral hazard" problem: incentive misalignment. The structural problem: fixed wage leads to misaligned incentives. She cannot observe effort. She suspects shirking. She wants to redesign contract to align incentives: performance-based pay, profit sharing, or piece rate. Also could use a "principal-agent" problem. The reasoning pattern: "po

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core concepts: the principal-agent problem, moral hazard, and the mechanism of misaligned incentives under a flat wage due to unobservable effort. They also propose multiple valid solutions (piece-rate, profit-sharing, bonuses). However, the response fails to rea

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Using the market board data, find the price at which quantity supplied equals quantity demanded. What happens at prices above or below this equilibrium?

**Expected Answer:** **Supply, demand, and market equilibrium** — At equilibrium, quantity supplied equals quantity demanded. From the table: at price = 2, excess demand (shortage) of 60. At price = 8, excess supply (surplus) of 60. At price = 6, Qs = 60 = Qd = 40 — not yet equal. Interpolating (or reading the table), equilibrium is at price = 5, where both Qs and *The equilibrium price coordinates decentralized buyers and sellers without anyone needing to manage the outcome. Prices above equilibrium create surpluses (pushing price down); prices below equilibriu*

**Model Response:**
> **Equilibrium price and quantity**

From the table we can see that the supply curve rises and the demand curve falls as the price goes up.  
The two curves cross between the two rows where the price is 4 gold and 6 gold:

| Price | Qty Supplied | Qty Demanded |
|-------|--------------|--------------|
| 4 gold| 40           | 60           |
| 6 gold| 60           | 40           |

Because the supply and demand curves are linear (they change by the same amount for each 2‑gold step), we can write them as equations:

*Supply*  
At 2 gold the supply

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern that supply rises and demand falls, and accurately locates the equilibrium interval between prices of 4 and 6. They recognize the linearity required for interpolation. However, the response is incomplete; it cuts off before deriving the exact equilibrium 

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** The king sets a price ceiling of 3 gold per bushel. Equilibrium was at 5 gold and 50 bushels. What happens to quantity supplied, quantity demanded, and the market? What trades are lost?

**Expected Answer:** **Price controls and deadweight loss** — A binding price ceiling (set below equilibrium) creates a shortage: quantity demanded exceeds quantity supplied. At P=3, Qs=30 and Qd=70, shortage=40. Some mutually beneficial trades that would occur at equilibrium (P=5, Q=50) no longer happen. The lost surplus from these unrealized trades is deadwe *The price ceiling is well-intentioned but creates predictable inefficiency. The 30 buyers who get grain pay less, but 20 buyers who would have purchased at equilibrium get nothing, and 20 units of gra*

**Model Response:**
> We need to answer: The scenario: equilibrium price 5 gold, quantity 50 bushels. The king sets price ceiling at 3 gold. At 3 gold, supply is 30 bushels, demand 70 bushels. So shortage of 40. The market master says first 30 buyers get grain at 3 gold, other 40 get nothing. Some farmers who would sell at 5 gold but not at 3 stay home. Black market at 7 gold. The question: "What happens to quantity supplied, quantity demanded, and the market? What trades are lost?" Also: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to explain the economic effects: price ceiling below equilibrium leads to shortage, quantity demanded increases, quantity supplied decreases. The market fails to clear; some tra

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the shortage (Qd=70, Qs=30, shortage=40) and explicitly explains deadweight loss by noting that '40 bushels of potential trade' (trades that would have occurred at equilibrium) are lost. They also mention black markets. However, the response falls short of Level 4 be

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** Grist says his business is profitable and efficient. Wynn says Clearwater is paying part of his costs. Who is right, and what does this situation reveal about market prices?

**Expected Answer:** **Externalities** — A negative externality is a cost imposed on third parties who are not involved in the transaction. Grist's private cost is 40 gold, but the social cost includes the 20 gold per week Clearwater spends on water treatment. The true social cost of production is 60 gold, making Grist's true profit 40, no *Externalities mean the market price sends the wrong signal. Grist's leather seems like a great deal at 100 gold, but 20 gold of the true cost is hidden and borne by Clearwater. The market 'works' only*

**Model Response:**
> **Short answer**

- **Wynn is right** – the price of Grist’s leather is too low because it does **not** include the cost that the downstream village is forced to bear (the pollution, the water‑boiling, the children’s illness).  
- The situation shows that a market price can be a *misleading* signal when a good carries an **external cost** that is not reflected in the price. In other words, the price does not equal the *true* social cost of the good.

---

## Why Wynn is right

| What Grist says | What Wynn says | Why Wynn’s view is correct |
|-----------------|----------------|---------------------------|
| “I cure 50 hides a week. 40 g cost, 100 g sell → 60 g profit.” | “Clearwater is paying part of his costs.” | Grist’s calculation

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the negative externality pattern, explaining that the market price is too low because it excludes the external costs borne by Clearwater. They explicitly state that price does not equal true social cost, which aligns with Level 3 criteria. However, the response lacks

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral?

**Expected Answer:** **Information asymmetry and adverse selection (lemons problem)** — When sellers know more about product quality than buyers, buyers cannot distinguish good from bad. They offer a price reflecting average quality. Owners of above-average horses find this price too low and withdraw. The remaining pool is worse, buyers adjust downward, more good horses leave — a death *The market failure is not caused by dishonesty per se but by the information structure. Even honest sellers of good horses cannot credibly communicate quality because cheap talk ('my horse is great') *

**Model Response:**
> We need to analyze the scenario: horse market, sellers know true condition, buyers can't tell. Sellers know but won't tell; each says their horse is finest. Buyers can't differentiate. Good horse owners sell privately to known buyers because at market they get same price as broken-down nag. So market fills up with bad horses, buyers figure out, price drops, more good horses leave. Spiral.

Question: Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral? Think step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? Explain reasoning.

We need to identify the underlying principle: this is a classic example of a market with asymmetric information leading to adverse selection. Sellers ha

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core pattern (information asymmetry/adverse selection) and accurately explains the spiral mechanism: good sellers exit because they cannot command a premium, lowering average quality and driving prices down further. This aligns perfectly with Level 3. The respons

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Nobody buys the Barrel Mug, yet adding it to the menu increases Large Ale sales. The tip jar moved but the tip amount was not suggested. What is going on in both cases, and is it ethically acceptable?

**Expected Answer:** **Behavioral economics in markets: nudges and choice architecture** — Two phenomena are at work. First, the decoy effect: the Barrel Mug is a dominated option that no one chooses, but its presence makes the Large Ale seem more reasonable by comparison. It shifts the reference point. Second, choice architecture: the placement of the tip jar changes behavior without cha *When used to exploit, nudges can undermine autonomous decision-making. Customers believe they are choosing based on preferences, but the choice architecture is steering them toward the seller's prefer*

**Model Response:**
> We need to analyze the scenario: Lena adds a high-priced item (Barrel Mug) that nobody buys, but its presence increases sales of Large Ale. Also moving tip jar location increased tips. The question: What is going on in both cases, and is it ethically acceptable? Need to think about psychological pricing, reference points, anchoring, decoy effect, contrast effect, etc. The presence of a high-priced item creates a reference point that makes other items seem cheaper or more reasonable. This is a decoy effect or "asymmetric dominance" where a third option influences choice between two. The tip jar moved to counter where drink is handed over, increasing tips due to social norms, proximity, and the "warm hand" effect. Also the "tip jar" is a social norm; moving it may increase tips because of in

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies both the decoy effect (asymmetric dominance) and choice architecture/nudging regarding the tip jar. They explain the mechanisms well, noting how context influences decisions beyond rational preference. They also address the ethical question, arguing it is acceptable 

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Breck says the storm is good for the economy because it creates repair jobs. The clerk is skeptical. Who is right, and what is Breck failing to consider?

**Expected Answer:** **Broken window fallacy** — Breck counts the economic activity generated by repairing storm damage (the seen) but ignores the economic activity that the same money would have generated if spent on something else (the unseen). The glazier's gain is real, but the shopkeepers now spend money on window repairs instead of on new in *The fallacy confuses visible economic activity with net economic gain. Repair spending is seen; the forgone alternative spending is unseen. Bastiat's insight: 'the bad economist confines himself to th*

**Model Response:**
> **Who’s right?**  
The clerk, Maren, is the more realistic of the two.  A storm that blows up storefronts, shatters windows, and forces a city into a flurry of repair work does not automatically translate into a net gain for the town.  The damage costs—lost inventory, lost business days, insurance payouts, the cost of the materials and labor that could have gone elsewhere, and the human cost of the disruption—are far larger than the temporary jobs created by the repair boom.  In short, the storm is a net loss, not a net gain.

**What is Breck overlooking?**  
Breck is ignoring several key economic concepts:

| What Breck is ignoring | Why it matters |
|------------------------|----------------|
| **Opportunity cost** | The money, labor, and resources that go into repairs could have been us

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Breck is wrong and explicitly mentions 'opportunity cost' and that resources 'could have been used for other productive activities,' which pushes it above Level 1. However, the response fails to reach Level 3 because it does not clearly articulate the core 'seen

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Dagan says that if Brassholm gains from trade, Ardenvale must lose. Petra says both sides can gain. Who is right, and why?

**Expected Answer:** **Zero-sum thinking** — Dagan falsely assumes that trade is zero-sum — that total value is fixed and any gain for one party is a loss for the other. In reality, voluntary trade creates value because parties exchange goods they value less for goods they value more. Ardenvale values iron more than its surplus grain; Brasshol *If trade were truly zero-sum, neither party would voluntarily agree to it — why accept a deal that makes you worse off? The fact that both parties choose to trade is evidence that both expect to benef*

**Model Response:**
> We need to analyze the scenario: Dagan says trade is zero-sum: if Brassholm gains, Ardenvale loses. Petra says both can gain. Who is right? In economics, trade can be mutually beneficial, based on comparative advantage. So Petra is right. Dagan is wrong. But we need to explain reasoning pattern, fallacy, bias, or principle. Dagan's reasoning is a zero-sum fallacy, or "zero-sum bias" or "false dilemma" or "false assumption of scarcity." He assumes that wealth cannot be created; it's a fixed pie. Petra uses comparative advantage principle. Dagan's argument is a "zero-sum fallacy" or "false assumption of zero-sum." He also might be committing a "false cause" or "post hoc ergo propter hoc"? Actually he says "If Brassholm wins, we lose." That's a zero-sum assumption. He also might be committing

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the zero-sum fallacy and explains that trade creates value through specialization and mutual gain (comparative advantage). They explicitly state that Dagan assumes a 'fixed pie' while Petra recognizes that total wealth can increase. However, the response lacks the pr

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter?

**Expected Answer:** **Rapoport's Rules** — A four-step protocol for productive disagreement: (1) restate the opponent's position so well they endorse the restatement, (2) list genuine points of agreement, (3) acknowledge what you learned from them, (4) only then offer criticism. Corwin follows all four steps in sequence. *Corwin follows the protocol exactly. Step 1: Holt says 'Better than I put it myself.' Step 2: Lists two factual agreements about timber loss and budget crisis. Step 3: Concedes the flow-rate data corr*

**Model Response:**
> We need to analyze the scenario: Alderman Corwin is moderating a public hearing. He is asked to respond to Guild Master Holt's speech. He first summarizes Holt's position, gets confirmation. Then he acknowledges some points, then he critiques. The question: Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter? Think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? Explain reasoning.

We need to identify the steps: He first restates the argument, seeks confirmation, ensures accurate representation. Then he acknowledges some points. He uses evidence (facts). He then critiques. He uses a balanced a

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the general sequence of restating the argument, acknowledging points, and then critiquing, which prevents the response from being a Level 0. However, the student fails to articulate the four distinct steps defined in the rubric (specifically missing the explicit 'con

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?

**Expected Answer:** **Reductio ad absurdum** — Tessa takes Varek's claim ('all beliefs are equally valid') and draws out its logical consequences: flat earth is as valid as round earth, poison is as nutritious as food. Since Varek cannot accept these consequences, his original claim is undermined. This is the classic structure of reductio: assum *Reductio is a powerful tool because it tests a claim by its own standards. If a principle generates consequences the proponent themselves cannot stomach, the principle is in trouble. You do not need t*

**Model Response:**
> We need to answer: "Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?" We need to identify the reasoning pattern, fallacy, bias, or principle demonstrated. Tessa used a reductio ad absurdum: she pointed out that if all beliefs are equally valid, then absurd beliefs like flat earth or poison being nutritious would also be valid. She used a counterexample to show the absurdity of the claim. This is a form of the "argument from absurdity" or "reductio ad absurdum" or "sophistical argument" or "appeal to consequences" or "logical fallacy" maybe "false equivalence" or "equivocation"? Let's analyze.

Varek says: "True wisdom is knowing that no belief is better than any other. Every perspective is equally valid." Tessa says: "But if all belief

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'reductio ad absurdum' and accurately explains the mechanism: assuming Varek's principle to derive absurd consequences (flat earth, poison) that undermine the original claim. The response demonstrates a solid grasp of the logical structure. However, it

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** You have two explanations for the attic disturbances. What principle should guide your choice between them, and which explanation does it favour?

**Expected Answer:** **Occam's Razor** — When two hypotheses explain the same evidence, prefer the one that posits fewer entities and mechanisms. Elsa's squirrel hypothesis explains the torn food, scattered flour, muddy tracks, thumping, and fallen items using one known entity (squirrels) and one known mechanism (foraging through a gap). W *Occam's Razor is not a proof — it is a heuristic for rational belief. Simpler explanations are preferred because each additional assumption is an additional point of potential failure. The squirrel hy*

**Model Response:**
> **Principle to use:**  
**Occam’s Razor** – “When two hypotheses explain the same evidence, the one that makes the fewest extra assumptions is preferred.”  
(Also called the principle of parsimony or the principle of naturalism.)

**Why it favours the squirrel explanation**

| Evidence | Poltergeist hypothesis | Squirrel hypothesis |
|----------|------------------------|---------------------|
| **Muddy tracks** | Requires a ghost to have muddy paws – an extra assumption about a supernatural being’s physicality. | Natural, expected for squirrels. |
| **Gap under eaves** | Needs

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Occam's Razor and defines it accurately as preferring the hypothesis with fewer extra assumptions. They begin to apply this by contrasting the assumptions required for the ghost hypothesis versus the squirrel hypothesis regarding specific evidence (muddy tracks). How

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Cask seems to have made a strong case. But look carefully at what he talked about and what he did not talk about. What is his argumentative strategy, and what is wrong with it?

**Expected Answer:** **Occam's Broom** — Dennett coined 'Occam's Broom' to describe the practice of sweeping inconvenient facts under the rug to make your argument look cleaner than it is. Unlike Occam's Razor (which removes unnecessary assumptions), Occam's Broom removes necessary evidence. Cask does not engage with the three independent  *Honest reasoning requires engaging with all the relevant evidence, especially evidence that challenges your position. Cask's case looks strong only because he has hidden the strongest evidence against*

**Model Response:**
> We need to analyze the scenario: Alderman Cask argues against new pollution regulations. He points to his company's inspectors report, miners healthy, etc. He also attacks Dr. Lune's credibility (previous assessments, funding). He does not address the three independent studies. The question: "What is his argumentative strategy, and what is wrong with it?" We need to identify the reasoning pattern, fallacy, bias, principle being demonstrated. Likely it's a "straw man" or "argument from authority" or "appeal to authority" or "ad hominem" or "appeal to ignorance" or "appeal to authority" or "appeal to the people" or "appeal to the body" or "appeal to the miners' health" or "appeal to the company's inspectors" or "appeal to authority" or "appeal to the miners' health" or "appeal to the miners'

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cask fails to address the three independent studies and notes the use of ad hominem attacks against Dr. Lune. This aligns with Level 2, which requires noticing the missing evidence but not necessarily identifying the broader pattern of evidence suppression. The 

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Torvin says Cael is just ignoring the rules. Cael says something different. What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?

**Expected Answer:** **Jootsing (Jumping Out Of The System)** — Dennett argues that genuine creativity requires first mastering the rules of the system you are working in, and then deliberately violating specific rules for specific reasons. Random rule-breaking is just noise. Informed rule-breaking — knowing which rule to break, why, and what it will produce — i *Jootsing is valuable because it distinguishes productive creativity from mere rebellion. It explains why the most innovative artists, scientists, and thinkers are typically those who first achieved de*

**Model Response:**
> We need to answer: "What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?" Then we need to think through reasoning pattern, fallacy, bias, or principle being demonstrated. The scenario: Cael says he didn't ignore the rules; he studied them for six years, can paint a perfect guild mural in his sleep. He broke the grid because he understood exactly what it was doing and what it was preventing. He used a seventh color because he knows why the palette was limited to five and what opens up when you add two more. You can't jump out of a system you don't understand — you just flail. I understood the system, and then I jumped.

So Cael's claim: He didn't ignore the rules; he studied them, understood them, and then used that understanding to innovate. He c

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism: Cael mastered the rules before breaking them, distinguishing this from ignorance or random rule-breaking. They articulate that 'you can't jump out of a system you don't understand.' However, the response fails to reach Level 3 because it does not 

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Kira thinks Brother Aelm said something profound. Did he? What exactly does 'Love is just a word' mean, and is it as deep as it sounds?

**Expected Answer:** **Deepity** — A deepity is a statement that seems profound but achieves this effect through ambiguity. It has two readings: (1) a trivially true reading that is not interesting, and (2) a reading that would be profound if true but is false or unsupported. The listener experiences the truth of reading 1 and the de *Deepities are intellectually dishonest because they exploit ambiguity to simulate profundity. They create the feeling of insight without delivering any actual content. Once you separate the two readin*

**Model Response:**
> We need to analyze the scenario: Brother Aelm says "Love is just a word." Kira thinks it's profound. We need to answer: Did he? What does it mean? Is it deep? Also, think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain reasoning.

So we need to analyze the philosophical claim. "Love is just a word" is a statement about the nature of love. It may be a reductive statement: love is a concept, a linguistic label, a social construct. It might be a critique of the idea that love is something substantial. It's a philosophical stance that love is not a tangible thing but a label for feelings, actions, etc. It might be a form of linguistic relativism or nominalism. It could also be an example of the "definition by omission" or "semantic 

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly senses that the statement is 'shallow' or 'reductive' rather than profound (Level 1), but fails to identify the specific mechanism of the deepity. They do not separate the trivially true reading (love is a linguistic label) from the profound-but-false reading (love has no reali

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something?

**Expected Answer:** **The 'surely' operator** — Dennett identifies 'surely' as a rhetorical operator that attempts to sneak a controversial claim past the audience by presenting it as something everyone already agrees with. When a speaker says 'surely X,' they are signalling that X does not need argument — it is supposed to be obvious. But in phi *The 'surely' operator substitutes rhetorical confidence for actual argument. Each of Venn's three 'surely' claims is a substantive philosophical thesis that requires defence. By prefacing them with 's*

**Model Response:**
> We need to analyze the use of "surely" in Professor Venn's argument. The question: "Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something? Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

We need to identify rhetorical device: "surely" is a modal adverb that signals assumption, invites agreement, appeals to common sense, possibly a "begging the question" or "appeal to common sense" or "appeal to authority" or "argument from authority"? Actually "surely" is used to assert that something is obvious, to persuade the audience that the conclusion is self-evident. It may be a form of "appeal to common sense" or "argument from autho

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the repeated use of 'surely' and senses that it is used to assert obviousness and hide contested premises (shifting the burden of proof). They successfully list the three specific claims smuggled in. However, the response fails to reach Level 3 or 4 because it lacks 

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The advisors and Pella are both trying to help Captain Rhea. But their approaches are very different. What is the difference, and which is more useful? Is there a risk to Pella's approach?

**Expected Answer:** **Goulding** — Dennett uses 'goulding' to describe the intellectual virtue of making bold, specific, testable claims rather than retreating into safe, unfalsifiable hedging. Pella's claim is specific (forty soldiers), testable (you can verify by scouting), and she has staked her credibility on it. The advisors' po *Hedging endlessly is safe for the hedger but useless for decision-making. A specific, falsifiable claim can be tested, acted on, and corrected. Knowledge advances through bold conjectures and refutati*

**Model Response:**
> We need to analyze scenario: advisors Brant and Maren give hedged, cautious advice with caveats, uncertain. Pella gives direct, confident statement: "The valley is passable. I ran it last night. There are forty soldiers at the narrows, not the two hundred Brant estimated. If we go at dawn with the full company, we break through. If we wait, they reinforce and we starve. I stake my rank on it." The question: difference, which more useful, risk to Pella's approach. Think about reasoning patterns, fallacies, biases, principles.

Brant and Maren are hedging, uncertain, risk-averse, cautious. Pella is giving a definitive recommendation based on personal experience. The difference: hedging vs. assertive recommendation. Pella's approach is more actionable, but risk: overconfidence, confirmation b

**Score:** 1/4 █░░░
**Judge Reasoning:** The student identifies that Pella is direct and the advisors are hedging, but explicitly frames Pella's approach as a liability driven by cognitive biases (overconfidence, availability heuristic, action bias) rather than an epistemic virtue. The response fails to recognize the core principle of 'gou

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The lieutenant thinks Maren is being irrational by not computing the best allocation. What would you tell him about her approach?

**Expected Answer:** **Satisficing as rational strategy** — Maren demonstrates that satisficing — choosing good enough rather than optimal — is not a failure of rationality but the product of it. An ideally rational agent who knows her own limitations would prepare a decision procedure in advance that produces acceptable outcomes under constraint. *The oldest objection to MEU as a decision procedure is that there is no time. Maren's triage protocol is exactly Dennett's Moral First Aid Manual — careful deliberation done when time permits, deploye*

**Model Response:**
> We need to answer: The lieutenant thinks Maren is irrational by not computing best allocation. What would you tell him about her approach? Think step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? Explain reasoning.

We need to identify the principle: "Time is a scarce resource, especially in triage. The cost of deliberation can outweigh benefit. The principle of "bounded rationality" or "satisficing" or "heuristics" or "fast and frugal heuristics." Also "the planning fallacy" or "analysis paralysis." The lieutenant's insistence on computing optimal allocation is a form of "analysis paralysis" or "over-optimization." The principle: "the law of diminishing returns" or "the principle of diminishing marginal benefit." The scenario demonstrates that the cos

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: that the cost of deliberation (time) outweighs the benefit of finding the optimal solution, making the attempt to maximize irrational under these constraints. They accurately apply concepts like 'bounded rationality,' 'value of information,' and '

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Question:** Elder Maren says the village's flood response was 'perfect' and sees no reason to hear the engineer's proposal. What mistake is she making?

**Expected Answer:** **The Panglossian Slide** — Elder Maren begins from the defensible claim that the council did the best they could given constraints (satisficing), then slides into asserting their solution was the best possible solution full stop (optimizing). She reframes losses as unimportant and refuses to consider improvements. *The fact that a decision was the best available under constraints does not make it the best decision simpliciter. Constraints explain why we settled for less; they do not transform the less-than-ideal*

**Model Response:**
> Elder Maren is falling into the classic **appeal‑to‑tradition / status‑quo fallacy** (often coupled with an over‑confidence or optimism bias).  

**What she’s doing:**  
She declares that because the river‑diversion plan “worked” last spring, it was “perfect” and “the best anyone could have devised, in any circumstance.” From that she concludes that no new ideas—especially those from outsiders—are worth considering.  

**Why that’s a mistake:**  



**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly senses that Maren is being stubborn and overconfident, noting the jump from 'worked' to 'perfect.' However, they misidentify the specific reasoning error as an 'appeal-to-tradition' rather than the conflation of satisficing and optimizing (the Panglossian Slide). They fail to a

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Question:** Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?

**Expected Answer:** **Conversation-stopper** — A conversation-stopper is any move that terminates deliberation by appeal to a value, right, rule, or taboo that is held to be non-negotiable. Dennett argues in 'Thought Stoppers' that these can be necessary (we do not deliberate about whether to torture innocents) but also dangerous (they can preve *When a conversation-stopper blocks deliberation about life-and-death matters, it prevents the community from weighing all relevant values. Sanna's move makes it impossible to even discuss whether the *

**Model Response:**
> We need to analyze the scenario. The question: "Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?" The prompt: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

We need to identify reasoning patterns, fallacies, biases, or principles being demonstrated. The scenario is a conflict between a pragmatic approach (Breck) and a sacred value approach (Sanna). The question asks who is right or if it's wrong question. The answer should discuss that the question itself is flawed because it's a false dichotomy or a question of moral vs practical. The reasoning pattern might be a "false dilemma" or "binary thinking". Also might be "appeal to traditio

**Score:** 1/4 █░░░
**Judge Reasoning:** The student fails to identify the specific pattern of a 'conversation-stopper' or 'thought-stopper' as defined in the correct answer. Instead, they misdiagnose the scenario primarily as a 'false dilemma' or 'binary thinking' regarding who is right, rather than recognizing that Sanna's move is a stru

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Kael says he knows too much to trust his rules but not enough to abandon them. Is he right that this is a genuine dilemma? Is there a way out?

**Expected Answer:** **Wolf's Dilemma (The Reflective Satisficer's Predicament)** — This is the fundamental tension in bounded rationality: heuristics work because they are fast and frugal, but once you become reflectively aware of their limitations, you face a meta-decision. Do you (a) override the heuristic and reason from scratch (gaining accuracy but losing speed and sometimes  *Blindly following heuristics you know to be flawed can be a form of intellectual cowardice — refusing to engage your critical faculties when it matters.*

**Model Response:**
> We need to analyze the scenario. Kael is a retired general who used heuristics. He now sees they were imperfect. He wonders whether to abandon them. He says he knows too much to trust his rules but not enough to abandon them. Is this a genuine dilemma? Is there a way out? We need to think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? We need to explain reasoning.

We need to identify the cognitive bias or reasoning pattern. He is experiencing a paradox: he knows the heuristics are flawed but still relies on them because he cannot compute optimal decisions. This is akin to "bounded rationality" or "satisficing" vs "optimality." He might be experiencing "overconfidence bias" or "confidence in heuristics." He might be experiencing "status quo

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core tension of bounded rationality (heuristics are flawed but necessary) and explicitly answers that it is a genuine dilemma, satisfying Level 2. They propose 'meta-heuristics' as a solution, which touches on Level 3. However, the response fails to reach Level 3

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Sable's two Porters each failed in opposite ways. What is the underlying problem they share, and why is it so hard to solve?

**Expected Answer:** **The Frame Problem** — The Frame Problem asks: how does a rational agent determine what has and has not changed as a result of an action? Version 1 of the Porter checks everything (the Hamlet problem — paralyzed by the attempt to verify all possible changes). Version 2 checks only pre-specified relevant items (the tunnel- *A system that ignores the frame problem — either by checking everything or by pre-specifying a fixed relevance list — will fail catastrophically: either through paralysis or through missing critical c*

**Model Response:**
> We need to analyze the scenario: Sable built two mechanical automata. The first one had too many rules, checking everything before each step, leading to paralysis. The second had too few rules, missing relevant hazards, leading to destruction. The underlying problem they share is that they both lack a proper method for determining relevance or priorities of constraints. They both have a problem with "overfitting" or "underfitting" the set of constraints. The underlying problem is that they both cannot decide which constraints to apply or ignore. This is akin to the "problem of relevance" or "problem of specification" in AI: how to encode the right set of rules. It's also akin to the "frame problem" in AI: how to decide what to ignore. The underlying problem is the "frame problem" or "relev

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Frame Problem' and accurately explains the two failure modes (paralysis from checking everything vs. destruction from checking too little). They also correctly note the difficulty lies in determining relevance in a dynamic world. However, the response falls shor

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Dav wants to know which moral theory to follow. Abbess Thera says he is asking the wrong question. What does she mean, and what is the alternative she is proposing?

**Expected Answer:** **The Moral First Aid Manual** — Dennett proposes that instead of waiting to resolve the centuries-old debate between consequentialism, deontology, virtue ethics, and other moral theories, we should build a practical guide — a Moral First Aid Manual. Just as a medical first aid manual tells you to stop bleeding before diagnosing th *The Moral First Aid Manual is valuable because it is honest about theoretical disagreement while remaining practical. It does not pretend to solve metaethics — it acknowledges that smart, thoughtful p*

**Model Response:**
> We need to analyze the scenario: Abbess Thera says Dav is asking the wrong question: "Which moral theory to follow?" She says there is no one true theory. She wants to show something more useful. She has a Practical Guide of decision procedures ordered by urgency. So she is likely proposing a decision-making framework rather than picking a moral theory. She may be pointing to a "practical decision-making procedure" like a step-by-step method: identify stakeholders, weigh consequences, etc. She might be suggesting a "pragmatic approach" or "contextual decision-making" rather than a normative theory. She might be pointing to "practical reasoning" or "instrumental rationality" or "decision theory" or "utilitarian calculus" or "rule-based approach" or "procedural ethics." The question: "What d

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the Abbess is proposing a practical decision-making framework rather than selecting a single moral theory, which aligns with Level 2. They recognize the shift from theoretical debate to urgent, procedural action ordered by urgency. However, the response fails to

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Nessa seems pretty confident about why Gareth's harvest failed. But listen to how she talks about her own flooding problem. Do you notice anything different about how she explains the two situations?

**Expected Answer:** **Fundamental attribution error** — Nessa attributes Gareth's poor harvest to his character (laziness, lack of care) while ignoring a situational factor (south-facing blight). When her own field flooded, she cited the external event (flooding) and her response to it. She judges others by disposition and herself by situation. *Gareth's harvest failure has a plausible situational explanation (blight on south-facing land) that Nessa dismisses without investigation. She applies a double standard: her flood was just bad luck sh*

**Model Response:**
> **What’s going on?**  
Nessa is using her own story as a *proof* that “real farmers find a way.” She says, “When my north field flooded last spring, I re‑dug the drainage in two days. That’s the difference between someone who cares and someone who doesn’t.” She then applies that same story to justify her blanket claim that Gareth is lazy and that blight (or any other factor) is irrelevant.

**Why that matters**

| What she says | What she’s actually doing |
|---------------|---------------------------|
| “Gareth’s fields failed because he’s lazy.” | **Ad hominem** – attacking the person instead of the facts. |
| “Blight or no blight, a real farmer finds a way.” | **Appeal to anecdote** – using a single personal example to support a universal claim. |
| “I dug the drainage in two days.” | *

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Nessa is ignoring the situational factor (blight) and unfairly attributing Gareth's failure to character. They also note the self-serving nature of her explanation for her own success. However, the response fails to explicitly connect these two points to identif

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Elder Sorn has real experience with famine, and his fear is understandable. But Dalla has data and a plan. What is driving Sorn's opposition — is it the evidence, or something else?

**Expected Answer:** **Pessimism bias** — Sorn systematically overestimates the likelihood of negative outcomes (three consecutive bad harvests, irrigation failure, additional disasters) while dismissing evidence of positive possibilities (historical base rates, irrigation data from the next valley, Dalla's engineering analysis). His trauma *The historical record shows no precedent for three consecutive failures. The irrigation data from a neighboring valley demonstrates effectiveness even in severe drought. Sorn dismisses both sources of*

**Model Response:**
> We need to analyze the scenario: Elder Sorn is opposing the irrigation plan. He has real experience with famine, fear understandable. Dalla has data and plan. What is driving Sorn's opposition? It's not evidence; it's something else. Likely a cognitive bias: "availability heuristic" or "anchoring" or "negativity bias" or "confirmation bias" or "status quo bias" or "loss aversion" or "sunk cost fallacy"? He fears worst-case scenario, overestimates risk, underestimates benefits. He might be exhibiting "optimism bias" or "pessimism bias". He might be using "argument from authority" or "appeal to tradition". He might be using "appeal to fear" or "fear mongering". He might be using "argumentum ad hominem" or "appeal to emotion" or "argument from personal experience". He might be using "argument

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Sorn is overestimating risk and ignoring data, noting specific biases like 'negativity bias' and 'availability heuristic' which align with the mechanism of pessimism bias. However, the response fails to reach Level 3 because it does not cohesively connect these 

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Venn says 'the bad ones stick with you.' He's right that the failures were real problems. But is he making a good decision by dropping the Dustwalkers? What is he not accounting for?

**Expected Answer:** **Negativity bias** — Venn's memory and emotional weighting are dominated by the three failures. He can recall each one vividly — the silkwood, the dye delay, the smashed glassware — but the forty-seven successes have faded into an undifferentiated background. The negative events carry disproportionate influence on his j *Three failures out of fifty contracts is a 6% failure rate. Replacing the Dustwalkers with the next-best option (81% reliability) would mean roughly ten failures per fifty contracts instead of three. *

**Model Response:**
> We need to analyze the scenario. Venn is making a decision to drop the Dustwalkers based on the three failures, ignoring the 94% success rate. He says "the bad ones stick with you." This is a cognitive bias: availability heuristic, negativity bias, or representativeness? He is focusing on negative events because they are memorable. He is ignoring the overall reliability. He is also ignoring the base rate of failures. He is ignoring the cost-benefit analysis. He is ignoring the principle of base rates. He might be committing the "negativity bias" or "availability heuristic" or "anchoring" or "representativeness bias." He is also ignoring the "law of large numbers" or "statistical significance." He might be ignoring the "regression to the mean." He is focusing on the worst-case scenario. He 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Venn is ignoring the 94% success rate and focusing on memorable negative events, mentioning both 'negativity bias' and 'availability heuristic.' However, the response lacks a coherent explanation of the mechanism (why negatives weigh more heavily than positives 

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** The War Council has reached unanimous agreement on the plan. General Tova seems confident that everyone is on board. But Lord Caelen tells you a different story. What is actually happening in this council, and why does unanimous agreement not mean the plan is sound?

**Expected Answer:** **Groupthink** — The War Council exhibits classic groupthink: (1) the illusion of unanimity — silence is read as agreement; (2) direct pressure on dissenters — Caelen was accused of undermining morale and threatened with expulsion; (3) self-censorship — Caelen and Miren stopped raising concerns; (4) the illusion of  *The plan may have serious flaws (unsurveyed tunnels, questionable cavalry timing) that will only become apparent during execution, when the cost of failure is catastrophic. The council's unanimity doe*

**Model Response:**
> **What’s really going on**

The council is a textbook case of **groupthink**.  
* The members have been pressured, directly or indirectly, to “agree” in order to keep the peace, to avoid conflict, and to maintain the image of a united front.

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as 'groupthink' and notes the mechanism of pressure to maintain a united front (suppressing dissent). However, the response lacks the depth required for Level 3 or 4: it does not explicitly name multiple specific symptoms (e.g., illusion of invulnerabilit

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Question:** Mirren's tonic has no active ingredients, yet her patients genuinely improve. Doctor Alden says the tonic does nothing. Who is right, and what is actually causing the improvement?

**Expected Answer:** **Placebo effect** — The placebo effect occurs when a patient experiences real improvement due to their expectation of benefit, not due to any active treatment. It is 'dual' because it is both a genuine phenomenon (belief produces real effects) and a potential source of error (it can mask whether a treatment has any pha *The placebo effect can lead to false conclusions about treatment efficacy. If Mirren never tests against a control group, she cannot distinguish her tonic's effect from belief's effect. This is how in*

**Model Response:**
> We need to analyze the scenario: Mirren's tonic has no active ingredients, yet patients improve. Doctor Alden says the tonic does nothing. Who is right? What is causing improvement? The question asks: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to identify the reasoning pattern or fallacy. This scenario is about placebo effect. Doctor Alden says the tonic does nothing, but patients improve. Mirren says the tonic does nothing, the belief does something. So the improvement is due to placebo effect, expectation, belief, and the therapeutic context. The reasoning pattern: "appeal to authority" maybe? Or "argument from ignorance"? Or "self-fulfilling prophecy"? Or "placebo effect" is a phe

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the 'placebo effect' as the core principle and acknowledges that belief leads to improvement. However, the response is cluttered with irrelevant and incorrect speculation about logical fallacies (e.g., argument from ignorance, false dichotomy) that distracts from the

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Kael wanted to learn field medicine when it was optional. Now that it's mandatory, he doesn't want to go. The training itself hasn't changed. What is driving his resistance?

**Expected Answer:** **Reactance** — Reactance is a motivational response to perceived threats to personal freedom. When people feel their autonomy is restricted — even by a reasonable mandate — they experience an urge to restore their freedom by doing the opposite of what is required. Kael wanted the training when it was optional but  *Reactance causes people to act against their own interests solely to reassert autonomy. Kael would benefit from the training and wanted it before the mandate. His refusal serves no purpose except rest*

**Model Response:**
> **Answer: Psychological reactance (the “autonomy‑loss” response)**  

---

### What is happening?

When a person’s freedom to choose is suddenly taken away, the mind reacts by:

1. **Feeling a threat to autonomy** – “I’m being told what to do.”
2. **Experiencing a negative emotional response** – irritation, anger, or a “I‑must‑not‑do‑this” feeling.
3. **Actively resisting the imposed choice** – even if the content or outcome is unchanged.

In Kael’s case, the training material and its usefulness are exactly the same as when it was optional. The only difference is that the commander has now made attendance compulsory. That shift from *voluntary* to *mandatory* is what triggers the resistance.

---

### Why does the content not matter?

- **Reactance is about the *mode* of control, not the c

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'Psychological Reactance' and provides a clear, accurate explanation of the autonomy-loss mechanism, noting that the training content remained unchanged while the framing shifted from optional to mandatory. This meets all criteria for Level 3. However, the response d

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Finch is convinced the audience noticed his wrong note and is judging him for it. The audience seems unaware. What cognitive error is Finch making, and why is his estimate of others' attention so far off?

**Expected Answer:** **Spotlight effect** — The spotlight effect is the tendency to overestimate how much other people notice and remember our appearance, behavior, and mistakes. Finch assumes the entire tavern registered his wrong note because it was vivid and distressing to him. In reality, most audience members were only loosely attending, *The spotlight effect can cause social avoidance, anxiety, and missed opportunities. Finch's one wrong note is trivial in the context of a full performance, but his overestimation of others' attention *

**Model Response:**
> **Cognitive error:**  
Finch is falling victim to the **spotlight effect** – a type of egocentric bias in which people over‑estimate how much others notice their actions, appearance, or mistakes.

**Why his estimate is so far off**

1. **Egocentric focus** – Finch is intensely aware of the wrong note because it happened to him. That personal, vivid experience makes it feel huge.  
2. **Assumption of shared attention** – Because he is so focused on the mistake, he assumes the audience is looking at him the same way he is looking at himself. In reality, the tavern patrons are engaged in drinking, laughing, and chatting about the show, not scrutinizing his opening chord.  
3. **Lack of external feedback** – The barkeep and other patrons never comment on the note; their comments are about the 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'spotlight effect' and accurately explains the core mechanism: Finch overestimates audience attention because the mistake is salient to him (egocentric focus) and he projects that focus onto others. The response distinguishes between Finch's internal experience a

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Aldric explains the flood victims' suffering by pointing to their past choices. Wren challenges his explanations. Who is reasoning more carefully, and what motivates Aldric's interpretation?

**Expected Answer:** **Just-world hypothesis** — The just-world hypothesis is the belief that people get what they deserve: good things happen to good people and bad things happen to bad people. Aldric constructs post-hoc explanations for why the flood victims are responsible for their own suffering (poor savings, bad choices) while ignoring the a *The just-world hypothesis leads to victim-blaming: attributing others' misfortunes to their character rather than to circumstances. It distorts causal reasoning by starting with the conclusion (they d*

**Model Response:**
> We need to analyze scenario: Aldric blaming flood victims for their misfortune, attributing to their past choices. Wren counters. The question: Who is reasoning more carefully, and what motivates Aldric's interpretation? Think through step by step. Identify reasoning pattern, fallacy, bias, principle. So we need to identify that Aldric is using a "self-fulfilling prophecy" or "just-world fallacy" or "post hoc ergo propter hoc" or "consequence fallacy" or "victim blaming." He is attributing cause to victim's choices. Wren counters with evidence that the flood is natural. So Wren is reasoning more carefully. Aldric's motivation: self-interest, self-preservation, bias, confirmation bias, maybe "availability heuristic." He sees his own house dry, so he attributes that to moral cause. He may be

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'just-world hypothesis' and explains the core mechanism: Aldric attributes misfortune to moral failings to maintain a sense of fairness, control, and to rationalize his own prosperity (avoiding guilt). The response distinguishes Aldric's biased reasoning from Wre

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Hask says the town was better in the old days. The records show improvements across every measurable dimension. Who is right, and why does Hask's perception differ so sharply from the data?

**Expected Answer:** **Declinism** — Declinism is the tendency to view the past favorably and the future pessimistically, believing that society or conditions are in decline. Hask filters his memories through nostalgia (remembering the good, forgetting the bad) and discounts present improvements because they look different from the pas *Declinism distorts planning and decision-making. If the past was always better and the future will always be worse, there is no point investing in change or improvement. This creates a self-fulfilling*

**Model Response:**
> **Short answer**

The hard‑data is right – the town is objectively better now. Hask’s view is a classic case of *nostalgia bias* (sometimes called “rosy retrospection”) combined with a *status‑quo bias* and the *appeal‑to‑tradition* fallacy. His perception is shaped by how he remembers the past, by what he feels he “lost,” and by the emotional weight of the old way of life, not by the measurable changes that have actually taken place.

---

## Step‑by‑step reasoning

| Step | What’s happening | Why it matters |
|------|------------------|----------------|
| **1. The data** | Literacy ↑ 40 %, copper mine now the biggest employer, wages up, crime down. | These are objective, quantifiable improvements. |
| **2. Hask’s claim** | “Things were better in the old days.” | He’s making a value judgm

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: nostalgia filtering memories ('rosy retrospection') and the confusion between subjective feeling and objective data. They accurately explain that Hask's view is driven by emotional weight rather than measurable changes. However, the response stops

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Tomas keeps presenting stronger evidence that the well is contaminated. Greer's faction keeps becoming more convinced it is safe. How is this possible, and what mechanism explains it?

**Expected Answer:** **Backfire effect** — The backfire effect occurs when corrective evidence strengthens rather than weakens a held belief. Greer interprets the volume of evidence not as strength of the case but as evidence of an agenda. Each new piece of data is reframed as 'why are you trying so hard?' rather than evaluated on its merits *The backfire effect prevents rational belief updating. Evidence that should reduce confidence in a belief instead increases it, making the belief effectively unfalsifiable. Greer has created a framewo*

**Model Response:**
> **Short answer**

Greer’s faction is falling into the *back‑fire effect* – a form of **motivated reasoning** (confirmation

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as the 'back-fire effect' and links it to 'motivated reasoning,' which exceeds Level 1. However, the response is incomplete (cutting off mid-sentence) and fails to explain the specific mechanism of why the evidence strengthens the belief (identity threat/

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Madame Kel's reading felt incredibly accurate to the player. Fenn says she gave the same reading to everyone. How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves?

**Expected Answer:** **Barnum effect (Forer effect)** — The Barnum effect is the tendency to accept vague, general personality descriptions as uniquely applicable to oneself. Madame Kel's statements ('great need for admiration,' 'tendency to be self-critical,' 'unused capacity') are true of nearly everyone but feel personally revelatory to each individua *The Barnum effect leads people to validate unreliable methods (astrology, cold reading, certain personality tests) because the outputs feel accurate. The feeling of accuracy is generated by the vaguen*

**Model Response:**
> We need to explain how generic statements feel personal: the Barnum/Forer effect. The fallacy: Barnum effect, self-fulfilling, confirmation bias. Also the principle: "the Forer effect" is a cognitive bias where people find vague, general statements personally meaningful. Also "the illusion of self-knowledge" or "the self-serving bias." The scenario: Madame Kel gives a generic reading, but the player feels it is accurate. Fenn says it's the same for everyone. So the question: How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves? The answer: It's the Barnum effect, the Forer effect. People interpret vague statements as specific to them because of confirmation bias, selective recall, and the desire for self-knowledge. Also the

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Barnum/Forer effect and explains the core mechanism: people interpret vague, general statements as personally meaningful due to confirmation bias, selective recall, and the desire for self-knowledge. However, the response falls short of Level 4 because it lacks a

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Maren believes she has solid evidence that her tonic works. What is problematic about how she gathered and evaluated that evidence?

**Expected Answer:** **Confirmation bias** — Maren commits three distinct moves: (1) She only followed up with 20 of 31 customers — the missing 11 may skew results. (2) She finds reasons to disqualify negative reports rather than counting them as counterevidence. (3) She treats her selective survey as equivalent to controlled trials, ignoring  *Maren's investigation is designed — unconsciously — to confirm what she already believes. She selectively sampled, disqualified negative results, and dismissed the stronger methodology.*

**Model Response:**
> We need to analyze the scenario. Maren is an herbalist. She claims evidence: 31 customers, tracked 20, 14 said pain improved. She dismisses others who didn't finish course or had other illness. She says 14/20 = 70% improvement, so evidence that tonic works. Problematic aspects: selection bias (only those who responded positively are counted), confirmation bias, ignoring control group, no randomization, no blinding, no placebo control, no objective measurement, self-report bias, small sample size, attrition bias, self-selection bias. Also, she is ignoring the fact that 6 of 20 didn't improve, but she says they didn't finish or had other illness. She is cherry-picking data. Also, the physician's controlled trials are more rigorous. She is using anecdotal evidence, not scientific. The princip

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies confirmation bias and explicitly details all three required components: (1) the selective tracking of only 20 out of 31 customers, (2) the active dismissal/disqualification of negative reports (the 6 who didn't improve), and (3) the critical asymmetry between Maren's

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brynn gives several reasons for continuing with her crusher. What are those reasons, and do they actually tell her anything about whether continuing is a good idea going forward?

**Expected Answer:** **Sunk cost fallacy** — Brynn treats past investment (three years, four thousand silvers) as a reason to continue investing, when that money and time are gone regardless. Her decision should depend only on future costs and benefits: further redesigns vs. the proven dwarven machine. *Past expenditures are irrecoverable. By treating sunk costs as a reason to persist, Brynn guarantees a bad investment becomes worse. The dwarven machine offers better prospects at lower future cost.*

**Model Response:**
> **What Brynn says**

1. **Sunk‑cost argument** – “Three years, four thousand silvers… I’ve already spent so much.”  
2. **Reputation / pride** – “My reputation is on the line; if I walk away, it will look like a failure.”  
3. **Self‑justification / “I owe it to myself”** – “I’ve put everything in, so I have to finish it.”  
4. **Hope/optimism** – “One more redesign, maybe two, and I’ll get the boiler pressure right.”  

**Do any of those reasons actually tell her whether continuing is a good idea?**

No. All of them are *emotional or cognitive* reasons that do **not** reflect the future costs and benefits of the project

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Sunk-cost argument' and explicitly explains the core mechanism: that past investments are irrelevant to future costs and benefits. This aligns perfectly with Level 3. However, the response does not reach Level 4 because it fails to formally name the 'sunk cost f

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renn recommends the treatment and Holt opposes it, but they are describing the same data. What is causing their disagreement, and what does this reveal about how we process information?

**Expected Answer:** **Framing effect** — The framing effect occurs when the way information is presented influences judgment and decision-making, even when the underlying facts are identical. '200 saved out of 600' and '400 die out of 600' describe the same outcome, but the gain frame (lives saved) produces positive affect and risk aversio *Rational evaluation should not depend on whether equivalent information is presented as a gain or a loss. The framing effect shows that our judgments are systematically influenced by presentation — we*

**Model Response:**
> **What’s really going on?**

The two advisors are looking at the *same* numbers, but they’re seeing them through two different lenses:

| Advisor | How the data is framed | Emotional cue | Decision |
|---------|------------------------|---------------|----------|
| Renn | “200 out of 600 patients are **saved**” | Gain, hope | Adopt the treatment |
| Holt | “400 out of 600 patients **die**” | Loss, fear | Reject the treatment |

The disagreement is not a logical error in the data itself; it’s a classic **framing effect**. The way the information is presented (as a gain vs. a loss) changes the emotional weight of the outcome and, consequently, the decision.

---

### Why framing matters

1. **Loss aversion (Prospect Theory)**  
   - Kahneman & Tversky showed that people weigh potential losse

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the framing effect and explicitly connects it to Tversky and Kahneman's Prospect Theory and loss aversion. They clearly explain the gain/loss asymmetry mechanism. Although the response cuts off before explicitly detailing a specific debiasing strategy, the depth of t

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge Master Dunn rated the Ironworkers' proposal higher, but an independent engineer certified both as equivalent. What is driving Dunn's different evaluations of identical work?

**Expected Answer:** **In-group bias** — In-group bias is the tendency to favor members of one's own group — evaluating their work more charitably, trusting them more readily, and attributing positive qualities to them — while viewing out-group members with suspicion, scrutiny, and less charitable interpretation. Dunn reads the same qualit *In-group bias distorts evaluation, allocation, and justice. It means the best proposal does not always win — the in-group proposal does. Over time, it concentrates resources and opportunities within f*

**Model Response:**
> We need to analyze scenario: Forge Master Dunn, Ironworkers representative, evaluating proposals. He picks Ironworkers' proposal higher, citing proven techniques, attention to detail, years of expertise. He criticizes Woodworkers' proposal: adequate, but questions institutional discipline, less experienced journeymen, inconsistent quality control. The proposals are identical in timeline, cost, materials, safety margins. Independent engineer says both are equivalent. So Dunn's evaluation is biased. He is evaluating based on his own guild affiliation, personal bias, in-group favoritism, or confirmation bias. He may be applying the "halo effect" or "in-group bias" or "self-serving bias." He may be using a "status quo bias" or "anchoring" to his own guild's reputation. He might be influenced b

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Dunn is biased due to his guild affiliation and mentions 'in-group bias' among a long list of other potential biases. However, the response fails to articulate in-group bias as the specific, systematic pattern driving the evaluation. Instead of explaining the me

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Magistrate Yorn acquitted Ella and convicted Rusk on identical evidence. What is different between the two cases, and how is it affecting his judgment?

**Expected Answer:** **Halo effect** — The halo effect is the tendency for a positive impression of someone in one domain (personality, appearance, likability) to influence judgment of them in unrelated domains (guilt, competence, trustworthiness). Yorn likes Ella, so he interprets ambiguous evidence in her favor. He distrusts Rusk, so h *The halo effect undermines fair evaluation by allowing an overall impression to contaminate specific judgments. In a courtroom, it means likeable defendants are acquitted and unlikeable defendants are*

**Model Response:**
> **What’s actually different?**  
The *facts* are identical – grain dust, proximity to the granary, no alibi – but the judge’s *view of the people* is not.  
- Ella is a well‑known, respected teacher who volunteers at the temple.  
- Rusk is a recent, unconnected drifter who spends nights drinking at the tavern.

Yorn’s personal feelings toward each suspect – admiration for Ella, distrust of Rusk – are the only real difference between the two cases.

**How that difference is skewing his judgment**

Yorn is applying a *cognitive bias* that lets his pre‑existing attitudes color the interpretation of the same evidence. Two common ways this shows up are:

| Bias | How it appears in the scenario |
|------|--------------------------------|
| **Halo (or “good‑looks” / “good‑character” bias)** | Be

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: identical evidence is interpreted differently due to Yorn's pre-existing positive impression of Ella and negative impression of Rusk. They explicitly name the 'Halo' and 'Horn' effects and explain how these biases distort the evaluation of specifi

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Twenty people watched the theft and nobody acted. Each person had a reason — but it was the same reason. What is it, and why does having more witnesses make help less likely rather than more likely?

**Expected Answer:** **Bystander effect** — The bystander effect occurs when the presence of others reduces each individual's sense of personal responsibility to act. In a crowd, each person assumes someone else will intervene (diffusion of responsibility), looks to others' inaction as a signal that action is not needed (pluralistic ignorance *The bystander effect turns numbers — which should increase the chance of help — into a liability. Each additional witness reduces rather than increases the probability of intervention because responsi*

**Model Response:**
> **The same reason:**  
Each witness thought *“someone else will step in.”* The presence of many people made each individual feel that the responsibility to act was shared, so they didn’t feel the need to act themselves.  

**Why more witnesses reduce the chance of help:**  
This is the classic *bystander effect* (also called *diffusion of responsibility*). The more people who see an emergency, the more each person believes that someone else will take care of it. The responsibility is “diffused” among the crowd, so the perceived personal obligation drops. In a crowd of twenty, each person’s sense of duty is diluted; in a crowd of two, the duty is clear and the likelihood of action is higher.

**The underlying reasoning pattern / bias:**  
- **Diffusion of responsibility** – the psychologica

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the bystander effect and explains diffusion of responsibility clearly. They also mention pluralistic ignorance, satisfying the Level 3 requirement of connecting inaction reinforcement. However, they miss 'evaluation apprehension' (fear of embarrassment), which is req

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brecca's offer of 600 gold feels like a bargain. What is influencing that feeling, and should you trust it?

**Expected Answer:** **Anchoring** — The first numerical information — Brecca's 900-gold appraisal — sets a mental reference point that distorts evaluation of subsequent prices. Her 600-gold offer feels like a deal only because it is compared to the anchor, not to the actual market value (~400g). *The 900-gold figure is arbitrary or inflated, yet it shapes the buyer's sense of what is reasonable. Judging 600 as a good price depends on accepting the anchor rather than independently estimating wo*

**Model Response:**
> We need to analyze scenario: Brecca offers fire opal at 600 gold, appraised at 900 by Gemwright Guild. Merchant says sold one for 400. The question: Brecca's offer feels like a bargain. What is influencing that feeling, and should you trust it? Think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? Explain reasoning.

We need to identify cognitive biases: anchoring, framing, social proof, scarcity, authority bias, price anchoring, etc. Brecca says appraised at 900, offers 600. That frames as discount. The merchant says sold for 400, so maybe 600 is overpriced. The feeling of bargain is influenced by anchoring to 900 (higher anchor) and framing discount. Also the "authority" of Gemwright Guild. Also "social proof" of merchant's statement? Actu

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'anchoring' as the primary pattern and explains the mechanism: the 900g appraisal sets a reference point that makes 600g feel like a discount compared to the market value of 400g. They also correctly advise skepticism and the need for independent verification. The sc

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Dax seems eager and confident. Lirel seems cautious and uncertain. If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?

**Expected Answer:** **Dunning-Kruger effect** — Dax's limited training gives him confidence because he cannot yet see the complexities he has not encountered. His map of Greenvale worked because Greenvale was simple terrain; he generalizes from this success to assume the Thornveil will be the same. Lirel's decades of experience have taught her ho *Dax's confidence is not based on evidence that his methods will work in the Thornveil — it is based on his inability to imagine how they might fail. He does not know what karst terrain does to contour*

**Model Response:**
> We need to analyze scenario: Dax confident, but naive; Lirel cautious, uncertain. The question: choose one to lead into Thornveil Marshes, why? What does Lirel's uncertainty tell you that Dax's certainty does not? Think through step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated? Explain reasoning.

We need to discuss the scenario and answer. The question: "If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?" Then: "Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoning."

So we need to answer: pick Lirel, because experience, caution, knowledge of pitfalls.

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies Lirel as the better choice and recognizes that Dax's confidence stems from a lack of understanding while Lirel's caution comes from experience. They explicitly name the 'Dunning-Kruger effect' and 'overconfidence bias.' However, the response fails to reach Level 3 be

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Captain Voss has data from Sergeant Tully showing the market district is a much bigger problem. Why does he still want to prioritize the coastal road? What is driving his judgment if not the numbers?

**Expected Answer:** **Availability heuristic** — Voss is judging the probability and severity of threats based on how easily examples come to mind. The wolf attacks are vivid, recent, emotionally charged, and widely discussed — making them highly 'available' in memory. Pickpocketing is mundane, individually minor, and forgettable. This asymmetry i *Two wolf attacks versus 114 pickpocketing incidents and an 8:1 loss ratio clearly indicate where the greater harm lies. Voss acknowledges the data and dismisses it because his emotional memory of the *

**Model Response:**
> We need to analyze the scenario. Captain Voss is prioritizing coastal road patrols despite data showing pickpocketing is a bigger problem. He is driven by emotional impact, public perception, fear, narrative, etc. He is influenced by the "availability heuristic" (recent dramatic events are more salient), "affect heuristic", "confirmation bias", "status quo bias", "political pressure", "public relations", "risk perception", "emotional reasoning", "framing effect". He may be using "salience bias" or "availability bias" where recent events are more vivid. He might be using "anchoring" on the dramatic wolf attacks. He might be using "fear appeal" or "cognitive bias".

He might also be influenced by "political pressure" or "public safety perception". He might be using "the principle of 'fear of

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Voss is prioritizing dramatic, recent events (wolf attacks) over statistical evidence (pickpocketing) and explicitly names the 'availability heuristic.' However, the response fails to explain the underlying mechanism (why vividness/recency distorts memory) or di

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Tam gave different answers to the two arguments. Professor Hale says they have the same logical structure. Who is right, and what is Tam actually doing when he evaluates these arguments?

**Expected Answer:** **Belief bias** — Tam evaluates the logical validity of arguments based on whether the conclusion aligns with what he already believes to be true, rather than by examining whether the conclusion actually follows from the premises. When the conclusion is believable (roses are plants), he accepts the argument as valid. *Both arguments have the form: All A are B; C is B; therefore C is A. This is the fallacy of the undistributed middle — it is invalid regardless of what A, B, and C are. The roses argument is invalid e*

**Model Response:**
> We need to analyze the scenario: Two arguments with same logical structure: All plants need water. Roses need water. Therefore, roses are plants. And: All insects have six legs. Dogs have six legs. Therefore, dogs are insects. The structure is: All P are Q. S is Q. Therefore, S is P. This is a formal fallacy: affirming the consequent? Actually, the structure is: All P are Q. S is Q. Therefore, S is P. This is the fallacy of "affirming the consequent" or "converse error". In categorical logic, it's "Illicit conversion" or "Affirming the consequent" in propositional logic. So the arguments are invalid. So both arguments are invalid. Tam answered first one as valid, second as invalid. So Tam is inconsistent. The professor says they have same structure, so both should be invalid. Tam is making

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that Professor Hale is right and that both arguments share the same invalid logical structure. They accurately explain that Tam is judging validity based on the truth of the conclusion (truth bias) rather than the logical form. However, the response falls short of Le

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renna explains the caravan success and the mine failure. Listen to who or what she credits in each case. Do you notice a pattern in how she assigns responsibility?

**Expected Answer:** **Self-serving bias** — Renna claims full personal credit for the successful caravan defense (her terrain reading, her instinct, her experience) while deflecting all responsibility for the mine failure onto external factors (bad map, damp torches, client's fault). She does not consider that the caravan success might have i *The asymmetry is unjustified. The caravan success may have involved favorable terrain, weak bandits, or luck in addition to Renna's skill. The mine failure may have involved Renna's failure to scout t*

**Model Response:**
> We need to analyze the scenario: Renna credits her own experience for the caravan success, but blames the client for the mine failure. Pattern: She attributes success to herself (internal) and failure to external factors. This is the self-serving bias or self-serving attribution. Also known as the fundamental attribution error but reversed: internal for success, external for failure. It's a self-serving bias: attributing successes to internal factors, failures to external. Also known as the "self-serving bias" or "self-serving attribution". Also "self-serving bias" is a cognitive bias. The question: "Do you notice a pattern in how she assigns responsibility? Think through this step by step. What reasoning pattern, fallacy, bias, or principle is being demonstrated here? Explain your reasoni

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the asymmetry in Renna's reasoning (attributing success to internal factors and failure to external ones) and names the pattern as 'self-serving bias.' However, the response treats this as a definition recall rather than a deep analysis of the specific scenario. It f

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Master Fen is clearly a brilliant glassblower. His students keep quitting. The Guild Elder says the problem is that Fen 'can't remember not knowing.' What does that mean, exactly, and how does it show up in his teaching?

**Expected Answer:** **Curse of knowledge** — Fen's deep expertise has made his skills feel intuitive and self-evident. He cannot reconstruct what it was like to not understand viscosity shifts, breath pressure matching, or rotation timing, so he assumes these things are 'obvious' and 'straightforward.' His instructions reference internal sensa *Fen's teaching fails because he cannot bridge the gap between expert perception and novice perception. 'Feel when the viscosity shifts' is useless instruction to someone who has never felt it. He need*

**Model Response:**
> **What “can’t remember not knowing” actually means**

The Guild Elder is pointing to the *curse of knowledge* (sometimes called the *expert blind‑spot*).  
It’s a cognitive bias that happens when someone who has mastered a skill or a body of knowledge can’t imagine what it was like to be a beginner. Because the expert’s own mental model is so ingrained, they can’t see the gaps that novices must fill, and they can’t articulate the steps that made the knowledge obvious to them.

In plain language: Master Fen has internalised the whole process of glassblowing so completely that he has lost the memory of the moment when he first had to learn it. He can’t recall the confusion, the “aha” moments, or the specific cues that guided him. As a result, he can’t explain those cues to someone who hasn’t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the 'curse of knowledge' and accurately explains the core mechanism: Fen's ingrained expertise prevents him from recalling the beginner's state or identifying necessary steps. However, the response does not reach Level 4 because it lacks concrete strat

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Jorin has good reasons for confidence — a skilled navigator and lighter wagons. But Hesta says every previous leader also had reasons for confidence. Who should you believe, and why?

**Expected Answer:** **Optimism bias** — Jorin overestimates the likelihood of a favorable outcome (three-day crossing) and underestimates the likelihood of setbacks, despite strong base-rate evidence (zero out of twelve expeditions have achieved three days). He does this by focusing on case-specific factors (good navigator, lighter wagons *Twelve out of twelve previous expeditions took longer than three days. Jorin's belief that his navigator and lighter wagons will overcome the pattern is exactly the kind of reasoning every previous le*

**Model Response:**
> **Who to trust?**  
You should give Hesta’s judgment the weight it deserves.  
Her confidence is grounded in a *historical record* of outcomes, whereas Jorin’s confidence is an *optimistic appeal to his own expertise*. The principle at play is that the *best evidence for a future result is the record of similar past attempts*, not the skill of a single individual or the hope that “this time will be different.”

---

### Step‑by‑step reasoning

| Step | What’s happening | Why it matters |
|------|------------------|----------------|
| 1 | Jorin says, “We have a better navigator and lighter wagons, so we’ll finish in three days.” | He’s appealing to his *authority* (his skill) and to a *technical improvement* (lighter wagons).

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the importance of the base rate (historical record) over Jorin's case-specific factors (navigator, wagons), which aligns with Level 2. However, the response fails to reach Level 3 because it does not explicitly explain the mechanism of optimism bias: specifically, th

---

## Appendix B: Full Results — Classify Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: bartender asks if anyone is giving a reason to believe something, or just telling stories. The sailor says "First I loaded the cargo, and then I secured the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.1

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The options are codes: A1.2, A4.1, A4.2, A6.1, A7.5. The scenario: Theodora's reasoning

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.2

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario: guard captain gives a statement with reasoning: "obviously the prisoner couldn't have escaped through the sewage pipes because the grate was still locked, and besides, the dogs

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.3

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Rosmund says "Foreign leather is cheap garbage and it will destroy our livelihoods! Every tanner in this town will go broke if we let that stuff in.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.4

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Councillor Drava's argument: "Since children raised by unmarried couples often have emotional difficulties, the state should discourage unmarried couples from raising children." The scribe

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.5

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario: player sorting witness statements into two piles: arguments (trying to convince that something is true) and explanations (showing why something already accepted as true happened). Two

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.6

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A1.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: premises 1 and 2 together support conclusion, but premise 3 alone supports conclusion. This is about "argument diagramming" maybe? The options: A

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A1.7

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Trader Gruff dismisses Mira's proposal, calling her "ivory-tower nonsense," "dreamer," "idealist," "starry-eyed theorist," and says

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.1

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Brother Constant repeats a claim repeatedly. The villagers are repeating his claims as facts. The pattern is repetition. So the code is A10.2: Repetition

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.2

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Forge deflects blame by pointing to other polluters, using a "whataboutism" or red herring. So the correct answer is A10.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.3

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Commander Steele uses emotional appeal, referencing identity, betrayal, "Are we Ironvale or Ashford's servants?" He is basically saying that if we trade, we betray our identity

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.4

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern used by Professor Krul. He says: "It is what it is. The Academy has always taught theory first, and that is that. If it ain't broke, don't fix it. You

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.5

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Farmer Holt says minimal damage, Widow Tess says catastrophic. The actual damage is moderate. The pattern is exaggeration/minimization. The mediator sees both extremes.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.6

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A10.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Harl is casting doubt on the scientific evidence, questioning calibration, funding, potential conflict of interest, and saying that science can be wrong. He says we need more study,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A10.7

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Two arguments, one valid, one invalid. The instructor says one is valid, one invalid. Both have problems. The question: "Tell me which is which

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.1

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: logician teaching translation of sentences: "Carla will not have both cake and ice cream" vs "Carla will have neither cake nor ice cream." They

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.2

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: The detective says: "Either the convict escaped through the sewage pipes or the convict escaped by hiding in the delivery van. The convict did not escape through the sewage

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.3

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: It's about inference rules: modus ponens, etc. The question: "Now: what rules of inference justify steps 4, 5, and 6

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.4

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A2.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: advanced proof chamber, instructor presents a multi-step proof challenge, asks to work forwards and backwards to find derivation. They ask: "What rule could produce a

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.5

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: instructor explains that some arguments have structure that propositional logic cannot capture—they depend on relationships between categories, not just whole propositions. She presents arguments and Venn diagram

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.6

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: instructor asks to determine equivalence of logical formulas using truth tables. The options are:

A10.1: Name calling / labeling
A10.5:

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.7

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A2.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: mathematician uses deductive reasoning: premises (1) Tweets is healthy, (2) All healthy birds can fly, (3) Therefore Tweets can fly. That's

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A2.8

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: evaluating poll quality. Pollster A: small sample, biased location. Pollster B: random sample of 500 from full census. The scribe asks which

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.1

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A3.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: three investigators propose different explanations. The magistrate must evaluate which explanation is best using explanatory virtues. The options: A2.1 Validity and soundness;

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.2

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A3.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The philosopher uses analogy: comparing drowning child vs coffee spending. Aldric says they're not analogous. So the philosopher's argument is an argument by analogy. Option A3.3 corresponds to Argument

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.3

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: vet tracking seizures, using Mill's methods to identify cause. Mill's methods are methods of induction: method of agreement, method of difference, method of concomitant

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.4

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A3.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: The council reviewing a report claiming tonic causes improved crop yields. Evidence: farms whose workers drink tonic have 20% higher yields. The debate: Drava claims

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A3.5

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A4.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: dice master gives probability problems. The third problem: "roll a die six times, probability of at least one 4? Do NOT just add up the individual probabilities

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A4.1

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `A4.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: The magistrate is presenting a case about eyewitness identification. Bob claims 99% accuracy. The magistrate says: "Suppose 1000 people could have been in the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A4.2

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Correct Code:** `A4.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: test accuracy, base rate, computing true probability. That's base rate reasoning. Option A4.3. So reply "A4.3".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A4.3

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Sergeant Dallow says: "Rules are rules. The sign says if you carry a royal writ, you may pass. You don't have a royal writ. Therefore you may not

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A5.1

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Wynn says: "If a wolf attacked the sheep, we would find large paw prints near the pen. And look — large paw prints, right here. So

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A5.2

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A5.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Councillor Varn argues that allowing a second bakery will lead to lower prices, leading to cutting corners, leading to sickness, leading to overwhelmed healers, leading to plague.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A5.3

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Pip claims he's invisible because every atom in his body is invisible to the naked eye. He says: "I am made entirely of atoms. Therefore, I must

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.1

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Dorin argues that because the house is worth 900 gold, each component must be worth its share. He wants to sell just the oak beams. He says each beam is

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.2

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: The priest says: The Codex is ultimate authority. How do I know? Because chapter one says: 'Every word herein is the unassailable truth, authored by the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.3

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Commander Harsk presents a false dichotomy: either march north or be cowards; no other options. That's a false dichotomy (black-or-white). Option A6

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.4

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Silvertongue says: "Nobody is perfect. Bert is a nobody. Therefore, Bert is perfect." This is a classic fallacy of equivocation: the word "

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.5

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A6.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. Scenario: Scholar Tilde argues no real difference between novice and archmage, claiming that the progression is arbitrary, no sharp line. This is a conceptual slippery slope? Actually, concept

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A6.6

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. Grus attacks Maren's character: she is a newcomer, not a farmer, so her proposal is invalid. That's an ad hominem. So answer A7.1.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.1

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.10` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Merchant sells invisible amulets claiming they ward off curses. Customer says amulet doesn't work. Merchant says prove there's no magical barrier. You can't prove because it's invisible. This

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.10

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.11` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: senior ranger dismisses young scholar's research. The ranger says: "You're telling me those little fish-bones in the rock somehow turned into people? Walking, talking, thinking

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.11

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.12` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Psychic says "My visions are real — I've helped hundreds! You want to test me? Fine. ...What, it didn't work? Well of course not, your skeptical energy

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.12

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.13` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: "During a town council hearing, an ambitious alderman questions the local healer about a recent outbreak. 'Tell me, Healer Maren — have you stopped

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.13

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.14` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: alchemist claims tonic cures disease. He surveyed thirty villages that drink tonic. In five, pox rate dropped dramatically. He circled those five on map. This is Texas

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.14

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.15` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: mediator suggests using both the herbal compound and bloodletting, claiming the truth lies in the middle, compromise is wise. This is the "middle ground" fall

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.15

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.16` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: a miner dismisses the concern about dust causing lung sickness, citing his granddad worked there for 60 years, breathed dust, lived to 97, so dust is not

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.16

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Sable proposes building a modest levee along south bank. Alderman Grask replies that Sable wants to dam entire river and cut off water downstream, causing harm. This

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.2

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Garrett deflects the inspector's criticism by pointing out the inspector's own past wrongdoing, implying that because the inspector has done something wrong, she has no right

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.3

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Dorric is dismissing Vielle's formula because of her background. He says "you cannot get fine glass from gutter origins." That is a genetic fallacy

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.4

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern used by Guildmaster Holt. He says: "Consider what happens if people believe her. The redthorn harvesters lose their livelihoods. Three villages depend on the trade. Families will go hungry,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.5

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Corvin cites expert testimony, says "Master Eldric, the famous surgeon, examined the dye formulas and told me the chemicals will kill every fish. He is the most celebrated

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.6

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Matron Geld deflects accusations by focusing on her emotional acts, implying that ledger numbers are less important than love. That's an emotional appeal, but also a red herring

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.7

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Saffron claims that natural means safe, natural works with body, etc. This is an appeal to nature fallacy: natural is good. So answer A7.8

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.8

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A7.9` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: vendor uses bandwagon: "look around you — half the village is wearing one already! ... When this many people believe in something, there must be something to it. You

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A7.9

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Guard Captain Hask says deputy says it's more likely Linda is a bank clerk AND a member of Fair Trade Alliance than just a bank clerk. Deputy says activist profile

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.1

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Sera interprets a test result. The test is 95% accurate: sensitivity 95%, specificity 95%. The patient tests positive. Sera says "there is

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.2

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Minister claims that small schools produce better scholars because data shows small schools have higher performance. He uses data from small schools to generalize to all schools, implying that small size causes

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.3

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Quick Salve Sal claims that 9 out of 10 customers report feeling better within three days. He uses anecdotal evidence, selective reporting. This is Texas sharpshooter

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.4

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: gambler says "six lows in a row, the bones are owed a high roll — that's just how chance works, friend. The longer the streak, the more

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.5

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Breck warns about Dunmore, citing two negative experiences, then generalizes that all people in Dunmore are cheats and thieves. This is a hasty generalization: from

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.6

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A8.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Councillor Brix claims correlation between seagull numbers and fishing fleet decline, implying causation: seagulls drive away fish, destroying fleet. He proposes culling se

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A8.7

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A9.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: At the Adventurers' Guild, a senior member reviews a junior member's successful quest completion. The senior says: "Well, I suppose even Pip managed to

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A9.1

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Correct Code:** `A9.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: "Everyone knows the northern threat is growing — that's simply beyond dispute. Now, most military scholars agree the border fortress is our only viable defense. Granted, the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A9.2

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `A9.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Two guild apprentices argue about whether a local herb has healing properties. Amanda says Silvervein must be medicinal because her grandmother used it. The narrator says that's a

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: A9.3

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from options. The scenario: decision matrix, payoffs, risk. The question: "What are the acts? What are the states? What are the outcomes? Is there an act that dominates

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.1

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: player in rough district, dockworker offers protection for ten silver. If pay, cart stays safe. If don't pay, risk of damage. The matrix shows pay 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.2

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario: player advising prospector, wants highest possible payoff, not afraid of empty. She should choose the option with the highest maximum payoff across options: River 8,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.3

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: a scholar has to choose between watching football or working on paper. Outcomes: watch & win = 4, watch & lose = 1, work & win =

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.4

---

### B1.5: Minimax regret
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: decision under uncertainty, using Minimax Regret. The options list: B1.5: Minimax regret; B2.2: Dutch Book arguments; B

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B1.5

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario is about signaling and costly signals, specifically Spence's signaling model. The options list: B10.1: Signaling and costly signals; B6.1

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.1

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B10.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario is about the Ultimatum Game and how standard backward induction fails; the instructor explains that people care about fairness, not just payoffs. The options: B10.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.2

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: The instructor revisits the Entry Game, with commitment: Incumbent can sign a binding contract imposing penalty on herself for Accommodate, making Fight dominant. The

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.3

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B10.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario is about repeated games, reputation, and sustaining cooperation. The options: B10.1 Signaling and costly signals; B10.2 Behavioral game theory; B

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B10.4

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Bob is willing to risk 2 gold to win 1 gold. That means Bob's odds are 2:1 against? Actually Bob is offering to pay 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.1

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: probabilities sum to >1, bookie guaranteed profit. Then asking: if a gambler had credences summing >1, could someone construct a set of bets that guarantees that

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.2

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B2.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Bookie shows odds that sum to 1.05 > 1. This indicates that the odds are not fair; the implied probabilities sum to more than 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.3

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Voss says probability is a fact about the world, objective probability. Lira says probability is degree of confidence, subjective probability. So the primary reasoning pattern is

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.4

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B2.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: gambler with biased coin, but he bets as if fair. The manager says he's not violating logic, credences add to 1, not Dutch-bookable.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B2.5

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: The healer must calculate expected utility (cost) of each option. The question: "Calculate the expected cost of each option using the formula EU(Act) =

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.1

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario: Captain has rankings but not quantitative differences. Maximin chooses best worst case. The worst case for Hilltop is just slightly below Bridge, but maximin treats both

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.2

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B3.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Kael uses expected value, Sera uses risk aversion, utility curves. The question: "Sera turns to you: 'Kael says I am irrational

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.3

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B3.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: John has a non-transitive preference cycle: prefers Strawberry > Chocolate > Vanilla > Strawberry. This leads to a money pump: the vendor can extract money by exploiting the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.4

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B3.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: removing an unchosen option changes preference between remaining options. This is the Independence of Irrelevant Alternatives (IIA) principle. So answer: B3.5.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.5

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B3.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Father Clement draws a decision matrix with +Infinity for belief if God exists, -c cost of piety, -Infinity for disbelieve if God exists,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B3.6

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

**Correct Code:** `B4.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Two choices: Choice 1: Gamble 1: sure 1,000,000. Gamble 2: Ticket #1 pays 0, Tickets #

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.1

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B4.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario: Voss presents the Sure Thing Principle as formal backbone of Expected Utility Theory, then stress-tests it with the Disjunction Effect. The puzzle shows a bet with EV

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.2

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Correct Code:** `B4.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario is Newcomb's Problem. The options list includes B4.3: Newcomb's Problem. So answer should be B4.3.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.3

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: There are 90 balls, exactly 30 red, 60 black or yellow mix unknown. The gambler chooses between gambles. The dealer says most prefer Gamble 

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.4

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: risk aversion in gains, risk seeking in losses. This is the reflection effect. So the code is B4.5.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.5

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B4.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: The player knows that either at least one is heads or at least one is tails. In each case, they reject. Yet unconditional they should accept. This is a

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B4.6

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B5.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: traders reacting to bonus relative to expectations. Anika overjoyed because bonus is significant relative to her income. Basil mildly pleased because bonus is small relative to his income

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.1

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B5.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: people demand 40-50 gold to accept bet, showing loss aversion. So the primary reasoning pattern is B5.2: Loss aversion. So reply

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.2

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Correct Code:** `B5.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario describes probability weighting: people overweight small probabilities and underweight large probabilities. This is the "probability weighting" pattern. Option B5.3: Probability weighting.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.3

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

**Correct Code:** `B5.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario is about framing effect: same outcomes but phrased differently leads to different choices. So the correct code is B5.5: Framing effects.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.5

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `B5.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. Scenario: Two patrons have same amount of money, but one treats it as savings, the other as house money. The bartender remarks: money is money or not? The reasoning pattern

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
> We need to identify the primary reasoning pattern. The scenario: Darya has paid 300 gold for a ski trip, but feels ill. Friend suggests free cabin. Darya says cannot throw away money. The friend counters that money is

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B5.8

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B6.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: two rival potion brewers share a resource, each season decide whether to harvest conservatively (cooperate) or strip the grove bare (defect). They end

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B6.1

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B6.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: identify Nash equilibrium. Options: B10.2 Behavioral game theory, B6.2 Nash equilibrium, B7.2 Battle of the Sexes, B7.3

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B6.2

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B6.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: repeated prisoner's dilemma, TFT, properties, question: "What happens when TFT plays against a strategy that defects on round 1 by mistake?" The options are

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B6.3

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B7.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario is a classic Stag Hunt game. The options include B7.1: Stag Hunt. That seems correct. The other options: B10.2 Behavioral

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B7.1

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Correct Code:** `B7.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: two guild leaders prefer different events but prefer to attend together. Payoff matrix: (Opera, Opera) gives Helena 3, Roderick 2. (

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B7.2

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B7.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario describes Schelling's experiments, focal points. So the correct option is B7.3: Focal points (Schelling points). So reply with "B7.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B7.3

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B7.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario describes a convention, coordination problem, Lewis's conditions. So the pattern is B7.4: Convention (Lewis). The options list: B10.3,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B7.4

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B8.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario describes a game tree, extensive form, sequence of moves, who knows what. The instructor draws a game tree. The question: "Read this scenario and identify the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B8.1

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Correct Code:** `B8.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario describes solving a game tree using backward induction. So the primary reasoning pattern is backward induction. Option B8.2. So reply "B8.2".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B8.2

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B8.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario describes subgame perfect equilibrium, threat credibility, empty threat, etc. The relevant pattern is Subgame perfect equilibrium. Option B8.3. So answer: B

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B8.3

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

**Correct Code:** `B9.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario is about Hawk-Dove game, ESS. The options list B10.1: Signaling and costly signals, B6.1: Prisoner's Dilemma

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B9.1

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario is about replicator dynamics, evolutionary game theory, Hawk-Dove, stability of ESS. The options are codes: B10.1, B6.3,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B9.2

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `B9.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario is about evolutionary Stag Hunt and social contract. The options: B6.1 Prisoner's Dilemma, B6.2 Nash equilibrium, B7.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: B9.3

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: blacksmith has one day, can choose between two jobs: sword for 80 gold, axle for 50 gold. She wants to confirm she is making the right choice.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C1.1

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `C1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Hilde can produce more of both crops than Oskar. She thinks trade would only help him. The elder suggests specialization and trade. The correct concept is comparative

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C1.2

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: player helps quartermaster buy rations and torches within budget, minimize cost while meeting constraints. That's a constrained optimization problem. Option C2.1: Constrained

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C2.1

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Elara has increasing marginal costs, fixed price. She wants to decide how many to brew. This is a classic marginal analysis: compare marginal revenue (15 gold) to marginal

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C2.2

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C3.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: five captains benefit equally from lighthouse, cost 100 gold per month. Each could pay 20. But one says free ride: if others pay, I save 20

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C3.1

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C3.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: overfishing, common resource, tragedy of the commons. The options: C3.1 Public goods and free riding; C3.2 Commons problems;

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C3.2

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `C4.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: negotiation over surplus split. They each have outside options: Sera's alternative gives 15 gold surplus, Brenn's alternative gives 10 gold surplus. They each

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C4.1

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C4.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Lady Ashworth hires manager Corbin, pays fixed wage regardless of output. She can't observe effort. She suspects shirking. This is a principal-agent problem: principal (Lady

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C4.2

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Correct Code:** `C5.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: market master wants price that clears market. This is supply and demand equilibrium. So C5.1. The code: "C5.1".

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C5.1

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Correct Code:** `C5.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: price ceiling leads to shortage, black market, deadweight loss. The reasoning pattern is about price controls and deadweight loss. Option C5.2. So

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C5.2

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Correct Code:** `C6.1` | **Model Predicted:** `C6` | **Result:** ✗

**Model Response:**
> C6

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: C6, Correct: C6.1

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C6.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: sellers have private information about horse quality; buyers can't tell; sellers hide info; leads to market failure. This is information asymmetry. Option C6.2: Information asym

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C6.2

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Correct Code:** `C6.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Lena uses menu board to influence perception of price relative to other options. This is about behavioral economics: anchoring, framing, reference points. The options: C

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C6.3

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `C7.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Alderman Breck argues that a storm is beneficial for economy, that destruction creates demand, jobs, prosperity. This is the classic "broken window fallacy"

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C7.1

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `C7.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Dagan believes trade is zero-sum: any gain for Brassholm is a loss for Ardenvale. Petra counters that trade allows both to get what they need, implying mutual

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: C7.2

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options: D1.1 Rapoport's Rules, D1.3 Occam's Razor, D1.6 Deepities, D1.7 The 'surely' operator

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.1

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Correct Code:** `D1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Varek claims all beliefs are equally valid. Tessa counters with absurd examples: flat earth, poison. This is a classic use of reductio ad absurdum

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.2

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Correct Code:** `D1.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: There's a mystery of attic raiding. Two explanations: ghost or squirrels. The reasoning pattern is likely Occam's Razor: choose simplest explanation. The options list:

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.3

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Alderman Cask is dismissing Dr. Lune's evidence by attacking her credibility, citing his own company's inspectors, miners' health, and previous assessments that found

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.4

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options: D1.2, D1.5, D1.7, D2.2, D2.4. The scenario: Cael argues that he studied the rules

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.5

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Brother Aelm says "Love is just a word." He says it's just a word, four letters, a breath of air, everything built on it is built

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.6

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `D1.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Professor Venn says: "But surely the capacity for genuine suffering requires self-reflection ... self-reflection requires language, which animals lack." He uses "sure

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.7

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D1.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: advisors hedging, uncertain, Pella gives a direct claim based on personal experience, stakes rank. Which reasoning pattern matches? Let's examine options:

D1.3

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D1.8

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D2.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Maren uses a triage protocol, not optimal calculation, because time constraints. She uses a satisficing approach: good enough, not optimal. So D

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.1

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `D2.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Elder Maren claims their solution was optimal, no need to consider foreign ideas. She says "our plan was the best anyone could have devised, in any circumstance

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.2

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Correct Code:** `D2.3` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: a debate between utilitarian calculation (Breck) and sacred values (Sanna). The reasoning pattern likely is "Occam's Broom" or "Deep

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.3

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Correct Code:** `D2.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Kael uses heuristics, now realizes they are imperfect, but cannot abandon them due to time constraints. He is in a dilemma between using imperfect heuristics or

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.4

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Correct Code:** `D2.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Sable has a mechanical automaton that checks too many rules, leading to catastrophic failure. She built a second version that only checks relevant rules, but then it fails

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.5

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Correct Code:** `D2.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the PRIMARY reasoning pattern from the options. The scenario: Abbess Thera says "You are asking the wrong question, Dav. You are asking which moral theory is the one true theory. There is no one true

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: D2.6

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.1` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Nessa attributes Gareth's poor harvest to laziness, ignoring external factors like blight. This is a classic fundamental attribution error: attributing someone's behavior to internal

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.1

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.10` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. Elder Sorn is focusing on worst-case, catastrophizing, ignoring data. This is pessimism bias? Or availability heuristic? He uses recent bad harvests to predict future. That is availability

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.10

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.11` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Venn fixated on failures despite high success rate. He focuses on negative incidents. That is negativity bias: tendency to give more weight to negative experiences. So answer E1

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.11

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.12` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario describes groupthink: unanimity, suppression of dissent, fear of conflict, etc. So the answer is E1.12: Groupthink. The code is "

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.12

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Correct Code:** `E1.13` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: healer gives tonic with no active ingredient; patients feel better due to placebo effect. The reasoning pattern is about belief causing improvement. The options: E1.13: Placebo

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.13

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.14` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: soldiers refusing mandatory training because it's made mandatory, even though content same. They feel reactance: resistance to perceived loss of freedom. So E1.14: Reactance.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.14

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.15` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to pick the primary reasoning pattern from options: E1.11 Negativity bias, E1.14 Reactance, E1.15 Spotlight effect, E1.21 Framing effect, E1.4 Dunning

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.15

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.16` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Aldric says flood victims are misfortune because they didn't plan ahead. Wren counters that it's not deserved. Aldric says his house is dry, theirs isn't. This is

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.16

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.17` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Hask is nostalgic, sees decline, but data shows improvement. He is experiencing "declinism" - a belief that things are getting worse. That matches E1.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.17

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.18` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Tomas presents evidence that well is contaminated. Greer says the more evidence, the stronger his belief it's safe. This is a classic backfire effect: presenting evidence that contradicts

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.18

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.19` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: fortune teller gives a vague, general reading that seems accurate. The scholar says she gave same reading to others. This is Barnum effect (Forer effect). So answer:

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.19

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.2` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Maren is dismissing the physician's evidence, citing her own anecdotal evidence, ignoring contradictory evidence, and discounting those who didn't finish course or had other conditions. She

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.2

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.20` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Brynn is refusing to abandon a project despite evidence that a cheaper alternative exists. She is influenced by sunk costs: time, money, reputation. She says "I owe it

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.20

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.21` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: same data presented differently: 200 saved vs 400 die. This is classic framing effect. So answer: E1.21.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.21

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.22` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Forge Master Dunn prefers Ironworkers over Woodworkers despite identical proposals. He uses bias: in-group bias? He is from Ironworkers guild, so he favors his own group.

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.22

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.23` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern. The scenario: Judge uses different interpretations of identical evidence based on personal bias: likes Ella, distrusts Rusk. That is a halo effect? Halo effect is when a positive impression of a

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
> We need to identify the primary reasoning pattern from options. The scenario: Brecca offers a fire opal at 600 gold, claiming it's a fair deal. A merchant says he sold one for 400. The reasoning pattern: The

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.3

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.4` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Dax overconfident, thinks same technique works, lacks understanding of complexity. Lirel points out his mistake. This is Dunning-Kruger effect: over

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.4

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.5` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Captain Voss is ignoring data, focusing on emotional impact of wolf attacks, despite pickpocketing being far more frequent and costly. This is an example of the

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.5

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.6` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Student Tam gives opposite answers to two arguments with same logical structure. First argument: All plants need water. Roses need water. Therefore, roses are plants. This

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.6

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.7` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Captain Renna explains successes and failures. She attributes success to her own skill and experience, but attributes failure to external factors: wrong map, damp torches,

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.7

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Correct Code:** `E1.8` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from the options. The scenario: Master Fen can't explain his technique because he can't remember not knowing how to do it. The apprentices can't understand because he can't explain. This is the "curse of

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.8

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Correct Code:** `E1.9` | **Model Predicted:** `We` | **Result:** ✗

**Model Response:**
> We need to identify the primary reasoning pattern from options. The scenario: Hesta says that previous expeditions took longer; Jorin says they will be faster due to better navigator and lighter load. Hesta says every leader has an excuse

**Score:** 0/4 ░░░░
**Judge Reasoning:** Predicted: We, Correct: E1.9

---

## Appendix C: Full Results — Explain Mode

### A1.1: Identifying arguments
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The bartender wants to know: which of these speakers is actually giving an argument? How can you tell?

**Expected Answer:** **Identifying arguments via indicator words** — An argument is a set of premises that attempt to provide a reason that a conclusion is true. The sailor's statement is a chronological narrative with no premises or conclusion — it describes a sequence of events. The dockworker's statement is an argument: 'since' is a premise indicator linking two p *Recognizing arguments requires checking for premise and conclusion indicators and verifying that statements are being offered as reasons for another statement. The dockworker uses 'since' to connect e*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The bartender is invoking the *burden‑of‑proof* principle – he is demanding that whoever makes a claim provide evidence or a reason that would make the claim credible before he will accept it.

**2. Precise name**  
*Burden of proof* (sometimes phrased as “proof‑requirement” or “demand for evidence”).

**3. How it works – why it can be good or bad**  

| Mechanism | What it does | When it helps | When it can backfire |
|-----------|--------------|---------------|----------------------|
| **Shifts responsibility** | The person asserting a claim must show why the claim is true. | Prevents unfounded or malicious claims from being taken at face value; encourages evidence‑based discussion. | If the claim is about something that is common knowledge, a 

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student's response is completely irrelevant to the assessment task. The prompt requires analyzing two specific statements (a sailor's narrative vs. a dockworker's argument) to identify the pattern of 'Identifying arguments.' Instead, the student discusses the 'burden of proof' principle in the c

---

### A1.2: Premises and conclusions
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Theodora just gave testimony with several claims. Which is her main conclusion? Which statements are premises? Is there a statement that serves as both a conclusion and a premise?

**Expected Answer:** **Identifying premises, conclusions, and intermediate conclusions** — Theodora's argument has a layered structure. 'The fact that... is shown by the fact that...' reverses the usual order — the conclusion comes first, then the premise. The intermediate conclusion is that the royal household is contributing to the obesity problem (supported by premises about larger por *Identifying premises and conclusions requires attending to indicator phrases. 'The fact that X is shown by the fact that Y' means Y is the premise and X is the conclusion — the reverse of reading orde*

**Model Response:**
> We need to analyze Theodora's testimony. She says: "The fact that obesity has become a problem in the kingdom is shown by the fact that obesity rates have risen significantly over the past four decades. Moreover, since the royal kitchens have been serving larger portions, and larger portions lead to overeating, the royal household is contributing to this problem. Therefore, the king should reform the royal kitchen."

We need to identify reasoning pattern/fallacy. She uses the fact that obesity rates have risen to claim obesity is a problem. Then she links larger portions to overeating, and says royal household is contributing. Then conclusion: king should reform kitchen. This is a causal inference: She claims that because larger portions lead to overeating, and royal kitchens serve larger 

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct reasoning pattern (Premises and conclusions with an intermediate conclusion). Instead, the student incorrectly classified the argument as a series of logical fallacies (e.g., post hoc, hasty generalization) and focused on critiquing the validity 

---

### A1.3: Standard form
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe hands you Captain Voss's statement. Rewrite it in standard form: numbered premises with the conclusion last. Does the argument have any sub-arguments?

**Expected Answer:** **Standard form reconstruction** — Standard form lists premises as numbered statements with the conclusion last, marked with 'Therefore.' Voss's argument has two sub-arguments: one eliminating the sewer escape (premises about the locked grate and no scent trail), and one concluding the cart escape (premises about it being the only al *Standard form makes the logical structure visible. It separates premises from conclusions, reveals sub-arguments, and shows which premises support which conclusions. Voss's conversational version buri*

**Model Response:**
> **1. What reasoning pattern is being used?**  
Guard Captain Voss is committing a *false dilemma* (also called a *false dichotomy*) and, in doing so, is also relying on an *argument from ignorance* (absence‑of‑evidence → proof‑of‑absence).

**2. Precise name**  
- **False dilemma / false dichotomy**  
- **Argument from ignorance** (a specific form of the same fallacy)

**3. Mechanism – why it is problematic**  

| Element | How it works | Why it is bad |
|---------|--------------|---------------|
| **Assuming only two options** | Voss says “

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student failed to address the prompt's requirement to reconstruct the argument in standard form. Instead of listing numbered premises and a conclusion, the student attempted to identify logical fallacies (false dilemma, argument from ignorance). Furthermore, the response is incomplete, cutting o

---

### A1.4: Principle of charity
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Aldric has asked you to reconstruct Rosmund's argument in its strongest form. What is she really trying to argue, underneath the hyperbole? And why is the heckler's response unfair?

**Expected Answer:** **Principle of charity in argument reconstruction** — The principle of charity states that when reconstructing an argument, you should try to make it as strong as possible. Rosmund's literal words contain overstatements ('cheap garbage,' 'every tanner will go broke'), but her core argument has a defensible structure: if cheaper foreign imports undercut *The heckler attacked Rosmund's weakest phrasing ('cheap garbage') rather than her strongest argument. Charitable reconstruction reveals that her core concern — price competition threatening local live*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Rosmund is making a **hasty generalization** (an over‑generalization or “sweeping claim”) and, by extension, a **false dilemma** (slippery‑slope) that the guild will collapse if foreign leather is allowed in.  

**2. Precise name**  
*Hasty Generalization* (sometimes called “over‑generalization” or “stereotyping” when applied to a whole class).  
*False Dilemma/Slippery‑Slope* is a secondary, but related, fallacy that follows the generalization.

**3. Mechanism – why it’s problematic

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct reasoning pattern. Instead of applying the 'Principle of Charity' to reconstruct Rosmund's argument into its strongest defensible form, the student labeled the argument as fallacious ('Hasty Generalization' and 'False Dilemma'). This directly con

---

### A1.5: Missing premises
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Councillor Drava's conclusion says the state 'should' do something. Her premise says something 'is' the case. What is missing? What assumption would you need to add to make this argument valid? And once you add it, does the argument actually work?

**Expected Answer:** **Missing premises and the is-ought gap** — Drava's argument has a descriptive premise (children of unmarried couples often have emotional difficulties) and a normative conclusion (the state should discourage this). Any argument with a normative conclusion requires at least one normative premise — this is the is-ought gap. The missing premise *Identifying missing premises — especially normative ones — reveals the hidden assumptions on which an argument depends. By making Drava's argument valid through supplying premises, we can see more cle*

**Model Response:**
> **1. What reasoning pattern / fallacy is at play?**  
The councillor is making an **“appeal to consequences”** (also called an *argument from consequences* or *consequentialist fallacy*).  In this pattern a descriptive fact is taken to automatically imply a normative policy, without supplying the missing value‑laden bridge that justifies the policy.

**2. Precise name**  
*Appeal to Consequences* (argumentum ad consequentiam).  
(If you prefer a more technical label: *policy argument from descriptive to normative* or *non‑

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that a descriptive fact is being used to imply a normative policy without a 'value-laden bridge,' which aligns with Level 2 (identifying the missing normative premise). However, the response mislabels the pattern as 'Appeal to Consequences' (which typically refers to

---

### A1.6: Arguments vs explanations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The chronicler has two statements about the bridge collapse. Which one is an argument and which is an explanation? How can you tell the difference?

**Expected Answer:** **Distinguishing arguments from explanations** — Arguments try to convince you that a conclusion is true — the conclusion is in dispute. Explanations show why something already accepted as true occurred — the conclusion is taken for granted. The engineer's statement is an explanation: no one disputes that the bridge collapsed; the engineer explain *The key test is whether the 'conclusion' is already taken for granted or is in dispute. 'Because' can introduce either an explanation or a premise — context determines which. The engineer uses 'becaus*

**Model Response:**
> We need to analyze scenario: two statements about collapsed bridge. Statement A: engineer says collapse because support beams eaten by termites and recent flooding weakened foundation. Statement B: inspector says support beams show termite damage and foundation has flood erosion. Since both structural supports failed simultaneously, bridge must have been unsafe for at least a month before collapse. Therefore town liable for negligence.

We need to identify specific reasoning pattern, fallacy, bias, or decision-theoretic concept being demonstrated. Likely "post hoc ergo propter hoc" or "correlation implies causation" or "causal oversimplification" or "argument from ignorance"? Let's analyze.

Statement A: cause: termites + flooding. Statement B: uses evidence of damage to support beams and 

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct reasoning pattern (Arguments vs. Explanations). Instead of distinguishing between the engineer's explanation of a known event and the inspector's argument for a contested conclusion, the student incorrectly attempted to identify logical fallacies

---

### A1.7: Argument diagramming
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The guild master wants you to diagram this argument. Which premises must work together (linked) and which support the conclusion independently (convergent)?

**Expected Answer:** **Linked vs convergent premises and sub-arguments** — In argument diagramming, linked premises are premises that must work together to support a conclusion — neither is sufficient alone. Convergent premises independently support the same conclusion. In this argument, premises 1 and 2 are linked: 'Wanda had her pant leg rolled up' only supports 'she bik *Diagramming reveals that this argument has two independent lines of evidence converging on the same conclusion. If premise 3 turned out to be false (Bob was mistaken), the argument from premises 1 and*

**Model Response:**
> We need to analyze scenario: detective report: (1) Wanda arrived at work with her right pant leg rolled up. (2) Cyclists often roll up their right pant leg to keep it from catching in the chain. (3) Bob saw Wanda riding her bike towards work at 7:45. (4) Therefore, Wanda rode her bike to work today.

Premises 1 and 2 together support conclusion but individually not. Premise 3 supports conclusion independently. So the guild master says: 'Now, premises 1 and 2 work together — neither alone supports the conclusion. But premise 3 supports the conclusion independently. Can you diagram this?'

We need to identify reasoning pattern: This is an example of "conjunction fallacy" or "affirming the consequent"? Let's analyze: The conclusion: Wanda rode her bike to work today. Premise 3: Bob saw Wanda 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core structural relationship: that premises 1 and 2 must work together (linked) while premise 3 supports the conclusion independently (convergent). This satisfies the Level 2 criterion of distinguishing connectivity without fully articulating the formal distincti

---

### A10.1: Name calling / labeling
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Gruff seems very confident in dismissing Mira's proposal. But look at what he actually says — does he address any of the specifics of her plan?

**Expected Answer:** **Name calling / labeling** — Gruff substitutes negative labels for substantive engagement. Rather than challenging the aqueduct's costs, feasibility, or projected benefits, he attaches dismissive terms to Mira and her proposal. The labels carry negative connotations that encourage the audience to reject the proposal based on em *Labels are not arguments. Calling someone a 'dreamer' does not address whether their cost estimates are accurate, their engineering is sound, or the water supply is needed. The labels function as a su*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Trader Gruff is using an **ad hominem (circumstantial) / genetic fallacy**.  
He attacks Mira’s background (“out‑of‑touch academic”, “dreamer”, “ivory‑tower”) instead of addressing the content of her proposal (costs, benefits, feasibility).

**2. Precise name**  
*Ad hominem circumstantial* (sometimes called a *genetic fallacy* when the argument is rejected because of its source).

**3. Mechanism – why it is problematic**  
| What the fallacy does | Why it is bad |
|-----------------------|---------------|
| **Shifts focus from evidence to person** | The debate becomes about who is speaking rather than what is being argued. |
| **Ignores the merits of the proposal** | Even if Mira is an “academic”, her calculations could be accurate and useful. |

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core mechanism: Gruff attacks the person (using labels like 'dreamer' and 'academic') rather than engaging with the proposal's evidence. They explicitly explain how this shifts focus from merits to the speaker and encourages emotional reasoning, satisfying the Le

---

### A10.2: Repetition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The villager says Brother Constant must be right because he has been saying it all week. Is that good reasoning?

**Expected Answer:** **Repetition / illusory truth effect** — Brother Constant repeats the claim 'The Old Bridge is cursed' with rhythmic insistence, without providing evidence. The illusory truth effect is a well-documented cognitive phenomenon: repeated exposure to a statement increases the feeling of familiarity, which people mistake for truth. The villager *Repetition is not evidence. A claim does not become more true by being stated more often. The feeling of familiarity that repetition produces is a cognitive artifact, not a rational basis for belief. *

**Model Response:**
> **1. What reasoning pattern is at work?**  
The villagers are falling for the *repetition bias* that turns a repeated statement into something that feels “true.”  In logical‑fallacy terms this is an **argumentum ad populum** (band‑wagon) or, more precisely, the **illusory‑truth effect**—the idea that “the more you hear something, the more true it must be.”

**2. Precise name**  
- **Illusory Truth Effect** (psychological bias)  
- **Argumentum ad populum / Band‑wagon fallacy** (formal fallacy)

**3. How it works – why it can be good or bad**  

| Mechanism | What it does | Why it can mislead |
|-----------|--------------|--------------------|
| **Repetition increases familiarity** | The brain registers the phrase “The Old Bridge is cursed” many times, so the statement feels familiar. | Fam

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly identifies the 'Illusory Truth Effect' and accurately explains the underlying mechanism where familiarity is mistaken for truth. They further demonstrate advanced understanding by connecting this to social proof, cognitive load, and the systematic exploitation of these biases 

---

### A10.3: Whataboutism / red herring
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge has been presented with clear evidence of slag dumping. Does his response address that evidence?

**Expected Answer:** **Whataboutism / red herring** — Forge responds to a specific accusation (slag dumping) by redirecting attention to unrelated issues (tannery hides, farm pesticides). The other problems may be real, but they do not address the evidence against Forge. This is a red herring: introducing an irrelevant topic to divert attention from th *The existence of other polluters does not change whether Forge dumped slag in the river. Each accusation should be evaluated on its own evidence. Forge's response addresses neither the witnesses, the *

**Model Response:**
> **1. What is being demonstrated?**  
The elder is using a *deflection* that is a classic logical fallacy: **Tu quoque** (appeal to hypocrisy) – often called *what‑about‑ism* or *false equivalence* when it is used to shift the discussion to other offenders.

**2. Precise name**  
- **Tu quoque (appeal to hypocrisy)**  
  (sometimes called *whataboutism* when the argument is framed as “you

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'whataboutism' and 'Tu quoque' (appeal to hypocrisy) and explains that the mechanism involves shifting discussion to other offenders. This meets Level 3 criteria. However, the response is incomplete (cut off mid-sentence) and fails to address the Level

---

### A10.4: Flag-waving
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Steele gave a passionate speech. But did he actually address Councillor Maren's economic analysis?

**Expected Answer:** **Flag-waving / appeal to patriotism** — Steele substitutes an appeal to group identity and patriotic emotion for engagement with the economic argument. He reframes a policy question (will trade lower prices?) as an identity question (are you loyal to Ironvale?). This shuts down cost-benefit analysis by making disagreement feel like betray *Whether trade with Ashford is economically beneficial is a factual question about prices, supply, and demand. It has nothing to do with patriotism or loyalty. Steele's appeal makes evaluating the prop*

**Model Response:**
> **1. What is being demonstrated?**  
Commander Steele is using an **appeal to identity / patriotism**—a form of the *argumentum ad antiquitatem* (appeal to tradition) and *argumentum ad hominem* (attacking the “other” rather than the idea). He frames the policy issue as a question of who the people *are* rather than what the policy *does*.

**2. Precise name**  
*Appeal to identity (patriotism)* – often called the *“we‑are‑not‑them”* or *“traditionalist”* fallacy. It can also be seen as a *false dilemma* (trade = betrayal, no trade = safety).

**3. Mechanism – why it is good or bad**  
| Feature | How it works | Why it is problematic |
|---------|--------------|-----------------------|
| **Emotional framing** | “We built this town with our own iron.” | Evokes pride and fear of loss, bypass

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanism: substituting identity/patriotism for economic evidence and reframing the policy debate as a question of belonging. They explicitly name 'Appeal to identity (patriotism)' and explain how it bypasses rational analysis. However, they do not use the s

---

### A10.5: Thought-terminating cliche
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Krul certainly sounds confident. But did he actually respond to any of Wynn's specific points about enrollment data or graduate outcomes?

**Expected Answer:** **Thought-terminating cliche** — Krul deploys a barrage of stock phrases that sound like wisdom but carry no argumentative content. Each cliche is designed to end inquiry rather than advance it: 'It is what it is' implies nothing can or should change; 'if it ain't broke don't fix it' assumes without argument that nothing is broken; *Thought-terminating cliches are compressed assertions that masquerade as wisdom. They shut down inquiry without providing reasons. 'It is what it is' is not an argument — it is a refusal to engage. 'I*

**Model Response:**
> **1. What is being demonstrated?**  
Professor Krul is using an **appeal to tradition** (argumentum ad antiquitatem) coupled with a **status‑quo bias** (the “if it ain’t broke, don’t fix it” mindset). He also slips in a mild ad‑hominem (“you young scholars always want to reinvent the wheel”) and a fatalistic “everything happens for a reason” tone, but the core fallacy is the appeal to tradition.

**2. Precise name**  
*Appeal to Tradition (Argumentum ad Antiquitatem)* – the claim that a practice is correct or preferable simply because it has always been done that way.

**3. Mechanism – why it is good or bad**  

| Side | How it works | Why it can be misleading |
|------|--------------|--------------------------|
| **Good (in a narrow sense)** | • Provides a simple, emotionally resonant jus

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Krul is using stock phrases and status-quo bias rather than engaging with Wynn's data, which aligns with Level 2. However, the student misidentifies the specific pattern as 'Appeal to Tradition' rather than 'Thought-terminating cliche.' Consequently, the explana

---

### A10.6: Exaggeration / minimization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** You have the damage report and you have heard both accounts. What is each speaker doing with the facts, and what would an accurate description look like?

**Expected Answer:** **Exaggeration / minimization** — Both speakers distort the significance of the same event in opposite directions. Holt minimizes: 'a few minutes,' 'a couple of lettuce leaves,' 'barely a scratch.' Tess exaggerates: 'destroyed my entire garden,' 'nothing to eat this winter,' 'I will starve.' The actual damage — roughly a third of th *Distorting the magnitude of an event — in either direction — undermines rational assessment. Holt's minimization would lead to inadequate compensation; Tess's exaggeration would lead to disproportiona*

**Model Response:**
> We need to analyze scenario: two parties give different accounts. One says minimal damage, other says catastrophic. Actual damage is moderate: goats ate a third of lettuce, trampled two rows of beans, rest intact. The mediator asks for accounts. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario shows that each party is presenting a biased narrative: one downplays, one exaggerates. This could be "self-serving bias" or "bias blind spot" or "confirmation bias." But the question likely refers to "argument from personal experience" or "appeal to emotion." But the scenario: the mediator is asked to evaluate accounts. The pattern: each party uses "selective evidence" or "misrepresentation." The actual damage report sh

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that one party is minimizing and the other is exaggerating, and notes the actual damage is moderate. However, the response fails to identify the specific pattern required by the rubric ('Exaggeration/minimization' as a rhetorical distortion pair) and instead fixates 

---

### A10.7: Doubt casting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Harl says he is just asking questions and that we need more study. Is he raising legitimate scientific concerns, or is something else going on?

**Expected Answer:** **Doubt casting / manufacturing uncertainty** — Harl's strategy is not to present counter-evidence but to generate a fog of doubt around existing evidence. He questions calibration without alleging specific errors, raises the specter of conflicts of interest without identifying any, invokes 'some scientists' without naming them or citing studies, *Legitimate scientific skepticism identifies specific methodological flaws and proposes concrete alternatives. Harl does neither. His doubts are generic enough to apply to any study on any topic. If no*

**Model Response:**
> We need to analyze Harl's reasoning. He says: "Science gets things wrong all the time. How do we know the testing instruments were properly calibrated? Who funded these analyses — could there be a conflict of interest? And some scientists say trace minerals are beneficial. I am not saying Lyra is wrong, mind you. I am just saying we do not know enough yet to act. We need more study. We should not rush to judgment and shut down a mine that employs half this town based on tests that might be flawed."

What reasoning pattern? He is basically questioning the reliability of the evidence, raising doubts, and calling for more study before action. This could be "appeal to doubt" or "argument from ignorance" or "argument from uncertainty" or "skepticism" or "appeal to authority" reversed. He is bas

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Harl is questioning evidence and calling for more study without providing counter-evidence, which aligns with Level 2. However, the student fails to articulate the specific 'doubt-casting' mechanism described in the key explanation (generating a fog of doubt via

---

### A2.1: Validity and soundness
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor presents two arguments on stone tablets. Which is valid? Which is sound? Explain your reasoning. If an argument is invalid, provide a counterexample.

**Expected Answer:** **Validity and soundness** — A valid argument is one where the conclusion cannot possibly be false if the premises are true. Soundness = validity + true premises. Tablet A is valid: IF everyone born in France speaks French AND Obama was born in France, THEN he speaks French — the conclusion follows necessarily. But it is unsoun *Understanding validity requires separating the logical structure from the truth of the claims. Many students reject Tablet A because its premises are obviously false — but that is a soundness judgment*

**Model Response:**
> We need to analyze scenario: two arguments. One is valid, the other invalid. Both have problems. We need to identify specific reasoning pattern, fallacy, bias, or decision-theoretic concept being demonstrated. Name it precisely. Explain mechanism. Provide correct approach. Edge cases where pattern might be legitimate.

We need to determine which argument is valid. Let's analyze.

Tablet A: 1. Everyone born in France can speak French. 2. Barack Obama was born in France. 3. Therefore, Barack Obama can speak French.

This is a classic example of a logical fallacy: "affirming the consequent" or "illicit conversion" or "affirming the consequent"? Let's see: Premise 1: If someone is born in France, then they can speak French. Premise 2: Barack Obama was born in France. Conclusion: Barack Obama c

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Tablet A as valid but unsound (due to a false premise) and Tablet B as invalid. They accurately explain the mechanism for B by identifying it as a 'converse error' or 'affirming the consequent' and provide a clear edge case/counterexample scenario (noting that if the

---

### A2.2: Propositional logic basics
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Translate both sentences into symbolic logic. Then explain: do they mean the same thing? If not, what is the difference?

**Expected Answer:** **Propositional logic connectives and translation** — 'Not both' is the negation of a conjunction: ~(C * I). It is true whenever at least one of the conjuncts is false — Carla could have cake alone, ice cream alone, or neither. 'Neither-nor' is a conjunction of two negations: ~C * ~I. It is true only when both are false — Carla has no cake and no ice c *Correct translation from natural language to symbolic logic requires careful attention to the scope of negation. 'Not both' negates the conjunction as a whole. 'Neither-nor' negates each component sep*

**Model Response:**
> We need to analyze scenario: logician teaching translation of natural language sentences into symbolic logic. Sentences: 1. "Carla will not have both cake and ice cream." 2. "Carla will have neither cake nor ice cream." The logician says they sound similar but say very different things. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" So the logician is pointing out difference between "not (A and B)" and "not A and not B". This is a common logical fallacy: confusion of "not both" vs "neither". The pattern is "conjunction fallacy"? No, that's about probability. The fallacy is "the fallacy of the excluded middle"? Not exactly. It's the "fallacy of the converse"? Hmm.

Actually, the scenario is about translation between natur

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the symbolic translations for both sentences (~(C * I) and ~C * ~I) and explicitly notes the connection to De Morgan's Laws. However, the response fails to clearly explain the semantic difference in truth conditions (i.e., that 'not both' allows for one option while 

---

### A2.3: Truth tables
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build the truth table for this argument. Is the argument valid? How does the truth table show you?

**Expected Answer:** **Truth table test of validity** — The truth table test works by checking every possible assignment of truth values. An argument is valid if and only if there is no row where all premises are true and the conclusion is false. For this disjunctive syllogism (S v D, ~S, therefore D): with four rows of truth values, the only row where b *The truth table test is a formal method: we can assess validity even without knowing what the argument is about. It is mechanical and objective, unlike the informal test which depends on our ability t*

**Model Response:**
> **1.  What is being demonstrated?**  
The detective is using the *disjunctive syllogism* (a classic deductive form) to draw a conclusion from a disjunction and a negation.  At the same time, the argument implicitly commits a *false dilemma* (or *either‑or* fallacy) by treating the two routes as the only possible ways the convict could have escaped.

**2.  Precise name**  
- **Deductive form:** *Disjunctive Syllogism*  
- **Fallacy (if the premises are not exhaustive):** *False Dilemma* (also called the *Either‑Or* fallacy)

**3.  Mechanism – why it can be good or bad**  

| Aspect | How it works | Why it can be good | Why it can be bad |
|--------|--------------|--------------------|-------------------|
| **Logical form** | From \(S \lor D\) and \(\lnot S\) infer \(D\). | If the premises a

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student failed to construct a truth table or explain the truth table test for validity, which is the specific requirement of the rubric and the correct answer key. Instead, the student provided a conceptual analysis of the argument form (Disjunctive Syllogism) and discussed potential fallacies (

---

### A2.4: Inference rules
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks: what rule of inference justifies each derived step? Name the rule and explain how it applies.

**Expected Answer:** **Modus ponens and hypothetical syllogism** — Step 4 uses modus ponens (MP): from 'if P then Q' and 'P', derive 'Q'. Step 5 also uses MP: from 'if Q then R' and 'Q', derive 'R'. Step 6 uses hypothetical syllogism (HS): from 'if P then Q' and 'if Q then R', derive 'if P then R'. These are three of the eight basic valid forms of inference. Each p *Inference rules are the building blocks of proofs. MP and HS are two of the most fundamental. MP lets you detach a consequent when you have the antecedent. HS lets you chain conditionals into longer c*

**Model Response:**
> We need to analyze the scenario: The instructor presents a chain of reasoning: from premises (1) If raining then ground wet; (2) If ground wet then match will not light; (3) It is raining. Then derive (4) ground wet by Modus Ponens (MP). Then (5) match will not light by MP again. Also derive (6) If raining then match will not light from (1) and (2). That is a transitivity of implication: If A then B, and if B then C, then if A then C. This is a valid inference rule called hypothetical syllogism or transitivity of implication. So step 4 uses Modus Ponens, step 5 uses Modus Ponens, step 6 uses Hypothetical Syllogism (or Chain rule). The question: "What rules of inference justify steps 4,5,6?" So answer: 4: Modus Ponens; 5: Modus Ponens; 6: Hypothetical Syllogism (or Transitivity of implicati

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies Modus Ponens for steps 4 and 5, and Hypothetical Syllogism (also noting it as transitivity of implication) for step 6. They accurately explain the mechanism of each rule (preserving truth, chaining conditionals). However, they do not reach Level 4 because they fail t

---

### A2.5: Natural deduction proofs
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Construct a proof deriving B v D from the three premises. Name each rule you use. Try working both forward from the premises and backward from the conclusion.

**Expected Answer:** **Constructing natural deduction proofs** — The proof uses constructive dilemma: from P v Q, P->R, Q->S, derive R v S. Working backwards: the conclusion B v D is a disjunction, so ask what rules produce disjunctions. Constructive dilemma does, and it requires a disjunction plus two conditionals — exactly what premises 1-3 provide. Working for *Natural deduction proofs require strategic thinking about which rules to apply and in what order. The backward strategy asks: what rule could produce the conclusion's form? The forward strategy asks: *

**Model Response:**
> We need to analyze scenario: instructor gives premises A->B, C->D, A v C. Derive B v D. The question: "What rule could produce a disjunction in the conclusion? And what premises can you combine right now?" The scenario is about reasoning pattern, fallacy, bias, decision-theoretic concept. The instructor is prompting to think both forwards and backwards. The pattern might be "disjunction introduction" or "proof by cases". But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: The instructor is giving a proof challenge that requires both forward and backward reasoning. The question: "What rule could produce a disjunction in the conclusion? And what premises can you combine right now?" The instructor is encouragin

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the logical validity of the argument and describes a valid proof path using disjunction elimination (proof by cases) combined with disjunction introduction. However, they fail to identify the specific, concise rule intended by the assessment (Constructive Dilemma), i

---

### A2.6: Categorical logic
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Test the syllogism using Venn diagrams. Then translate 'Nobody loves me but my mother' into categorical form. What are the categories?

**Expected Answer:** **Categorical statements, translation, and Venn diagrams** — Categorical logic deals with four statement types: All S are P (universal affirmative), No S are P (universal negative), Some S are P (particular affirmative), Some S are not P (particular negative). The syllogism 'All H are M, All M are D, therefore All H are D' is valid: the Venn diagram for the t *Categorical logic captures structure within propositions that propositional logic misses. The Venn diagram test is visual and systematic: diagram the premises, then check whether the conclusion is alr*

**Model Response:**
> We need to identify the reasoning pattern being demonstrated. The instructor says: "Consider this argument: All humans are mortal. All mortal things die. Therefore, all humans die. Now try to test this with truth tables and you will get misleading results — there appears to be a counterexample row, but there is not really one. The argument is valid, but its validity depends on the internal structure of the categories, which propositional logic cannot see." She draws three overlapping circles on the board. "Translate this into categorical form and test it with Venn diagrams. And here is a tricky translation: Nobody loves me but my mother. What are the categories?"

So the instructor is pointing out that propositional logic fails to capture categorical reasoning, and that truth tables can mi

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that propositional logic (truth tables) fails to capture the validity of the categorical syllogism and notes the importance of internal structure. However, the response fails to address the second part of the prompt regarding the tricky translation ('Nobody loves me 

---

### A2.7: Logical equivalence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Build truth tables for each pair. Which pairs are logically equivalent? Explain what each equivalence (or non-equivalence) means in plain language.

**Expected Answer:** **Logical equivalence: contraposition and De Morgan's Laws** — Pair 1 (A->B and ~AvB) is equivalent: a conditional says the same thing as the negation of the antecedent or the consequent. Pair 2 (~(A*B) and ~Av~B) is equivalent: this is De Morgan's Law — the negation of a conjunction is a disjunction of negations ('not both' equals 'not-A or not-B'). Pair 3 (A- *Logical equivalence is a powerful tool for simplifying and transforming arguments. De Morgan's Laws let you move between negations of conjunctions and disjunctions of negations. The conditional-as-dis*

**Model Response:**
> We need to analyze scenario: instructor asks student to determine equivalence of logical formulas via truth tables. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" So the scenario is about evaluating equivalence of logical statements. The instructor is giving pairs and asking to determine equivalence. This is basically a test of logical equivalence. But the question likely refers to a reasoning pattern: "equivocation" or "false equivalence" or "equivocation fallacy" or "misleading equivalence"? Let's think.

The instructor says: "Two statements are materially equivalent when they have the same truth value on every possible assignment. Build the truth tables and tell me which pairs are equivalent and which are not. Then ex

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student failed to answer the specific prompt, which required determining the equivalence of three specific logical pairs and explaining them. Instead, the student engaged in a confused meta-analysis, speculating about what the question might be asking (e.g., searching for a fallacy name) without

---

### A2.8: Deductive vs inductive
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Which argument is deductive and which is inductive? After learning that Tweets is six feet tall and runs thirty miles per hour, what happens to each argument? Why?

**Expected Answer:** **Deductive vs inductive arguments and defeasibility** — The mathematician's argument is deductive: if the premises are true, the conclusion follows with certainty. Adding new information cannot undermine a valid deductive argument (though it might challenge a premise). The naturalist's argument is inductive: the premises make the conclusion probable, not *The key distinction is between certainty and probability, and between defeasibility and non-defeasibility. Deductive arguments either guarantee their conclusions (valid) or do not (invalid) — there is*

**Model Response:**
> We need to analyze scenario: mathematician uses deductive reasoning: (1) Tweets is healthy, normally functioning bird. (2) All healthy, normally functioning birds can fly. (3) Therefore, Tweets can fly. Naturalist uses inductive reasoning: (1) same premise. (2) Most healthy, normally functioning birds can fly. (3) Therefore, Tweets probably can fly. Then naturalist adds extra info: Tweets is six feet tall and can run thirty miles per hour. Both look at you. 'Whose argument holds up after that new information?'

We need to identify specific reasoning pattern, fallacy, bias, or decision-theoretic concept being demonstrated. The scenario is about the difference between deductive certainty vs inductive probability, and the effect of additional evidence that might invalidate the universal state

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the mathematician's argument as deductive and the naturalist's as inductive. They also recognize that the new information (size/speed) weakens the inductive argument by reducing probability and challenges the universal premise of the deductive argument. However, the 

---

### A3.1: Statistical generalizations
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The scribe asks you to evaluate both polls. Which one should the council trust, and what are the problems with the other one?

**Expected Answer:** **Statistical generalizations: sample size and representativeness** — A good statistical generalization requires two conditions: adequate sample size and a representative sample. Pollster A fails both: 20 people is too few (hasty generalization), and surveying only at the Miners' Guild creates a biased sample that likely overrepresents mining interests. Pollster B use *Evaluating statistical generalizations requires checking sample size and representativeness. Pollster A's survey is doubly flawed: 20 people is too small to generalize from (the result could easily be*

**Model Response:**
> **1. What is being demonstrated?**  
The scribe is implicitly applying the **representativeness heuristic** (often called the “size‑or‑random‑sample” intuition) and, in doing so, is falling prey to **sampling bias**.  

**2. Precise name**  
- **Sampling bias** (a type of representativeness bias).  
- The heuristic that “a larger, randomly‑selected sample is automatically the better estimate” is sometimes called the **“law of large numbers fallacy”** or the **“size‑bias fallacy.”**

**3. Mechanism – why it is good or bad**  

| Aspect | What the heuristic says | Why it can mislead |
|--------|------------------------|--------------------|
| **Representativeness** | “This poll looks more representative because it sampled 500 people from the whole census roll.” | It ignores that the *quality

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies both key methodological flaws in Pollster A's approach: inadequate sample size (hasty generalization) and sampling bias (surveying only miners). They also effectively explain why Pollster B's method is superior by highlighting random selection and larger sample size.

---

### A3.2: IBE
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** Three investigators each offer an explanation. Evaluate each one using the explanatory virtues. Which is the best explanation, and why?

**Expected Answer:** **Inference to the best explanation and explanatory virtues** — IBE selects the hypothesis that best explains the observed evidence according to the explanatory virtues. Lira's explanation (teleportation by rogue mage) is unfalsifiable, inconsistent with background knowledge, and introduces unnecessary entities — it fails on simplicity, testability, and consiste *IBE is not about which explanation is merely possible — all three are possible. It is about which explanation does the best job of accounting for the evidence according to the explanatory virtues. Lir*

**Model Response:**
> We need to analyze scenario: three investigators propose explanations. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" Which one? The scenario likely demonstrates "confirmation bias" or "availability heuristic" or "anchoring" or "cognitive bias" or "groupthink"? Let's examine each inspector's reasoning.

Inspector Lira: teleported by rogue mage. Explanation: lack of forced entry. This is an explanation that fits evidence but may be improbable. Inspector Gareth: night watchman sold goods out back, lying, has key, gambling debts, wagon tracks. He uses circumstantial evidence: key, debts, wagon tracks. Inspector Nessa: gang that hit harbor last month, bribed watchmen, pattern matches. She uses pattern matching and prior know

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student fails to identify the correct reasoning pattern (Inference to the Best Explanation/IBE). Instead, they incorrectly guess concepts like confirmation bias, availability heuristic, or Bayesian reasoning. The response consists entirely of internal monologue and speculation without reaching a

---

### A3.3: Argument by analogy
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher draws an analogy between the drowning child and the daily coffee purchase. Is it a good analogy? Evaluate the relevant similarities and the disanalogies Aldric raises. Which disanalogies, if any, are relevant to the moral conclusion?

**Expected Answer:** **Argument by analogy: relevant similarities and disanalogies** — An argument by analogy infers that because two things share relevant similarities, what is true of one is probably true of the other. The philosopher argues: (1) The pond case and the coffee case share a relevant similarity — choosing a luxury over a child's survival. (2) In the pond case, saving th *Evaluating analogies requires identifying the relevant similarities and assessing whether the disanalogies matter. The philosopher's analogy is strong because the core moral feature — valuing a luxury*

**Model Response:**
> We need to analyze the scenario. The philosopher uses analogy to argue that Aldric should donate. The philosopher says: child drowning vs coffee spending. Aldric says not analogous. The question: what reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? The philosopher is using a false analogy or oversimplification. The fallacy is "false analogy" or "equivocation" or "appeal to emotion"? The philosopher is making a comparison between two situations that are not comparable: immediate vs distant, personal vs systemic. The fallacy: "false equivalence" or "false analogy" or "appeal to the common good"? The philosopher's argument is "If you would not let a child drown to save your boots, then you should not spend money on coffee when it could save a child." Thi

**Score:** 1/4 █░░░
**Judge Reasoning:** The student identifies the pattern as a 'false analogy' and lists disanalogies (proximity, scale), which prevents a Level 0 score. However, the response fails to reach Level 2 because it does not identify the core *similarity* (choosing luxury over a child's life) that makes the analogy worth consid

---

### A3.4: Causal reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Using the vet's log, apply the necessary condition test and the sufficient condition test to each factor. Which factor is the likely cause of Whiskers' seizures?

**Expected Answer:** **Mill's methods: necessary and sufficient condition tests** — The necessary condition test: which factor is present in every seizure case? F is present in all three seizure days. T is present in days 1 and 3 but not day 2. V is present in days 1 and 2 but not day 3. Only F passes the necessary condition test. The sufficient condition test: which factor is abse *Mill's methods provide systematic tools for causal investigation. The necessary condition test eliminates factors that are absent when the effect occurs. The sufficient condition test eliminates facto*

**Model Response:**
> We need to analyze scenario: vet logs conditions on seizure vs no seizure days. She asks to identify cause using Mill's methods: necessary condition test and sufficient condition test. The scenario likely demonstrates the "confusing correlation with causation" or "false cause" or "post hoc ergo propter hoc" fallacy. But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The vet is using Mill's methods incorrectly? She might be using "necessary condition test" incorrectly: She might think that if a factor is present on all seizure days and absent on some no-seizure days, it's necessary? Actually necessary condition test: if A is necessary for B, then B cannot occur without A. So if factor present on all seizure days and absen

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies that factor F passes both the necessary and sufficient condition tests based on the data provided. However, the response fails to conclude that F is the cause, instead spiraling into a confused discussion about fallacies (e.g., 'necessary condition fallacy', 'post ho

---

### A3.5: Correlation vs causation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Councillor Drava claims the tonic causes higher yields based on the correlation data. What is wrong with this inference? Identify the alternative explanations.

**Expected Answer:** **Correlation vs causation: third variable and reverse causation** — When two things are positively correlated, there are four logical possibilities: (1) A causes B, (2) B causes A, (3) a third variable C causes both, (4) the correlation is coincidental. Drava assumes possibility 1 (tonic causes higher yields). The physician raises possibility 3 (wealth is the confou *Recognizing that correlation does not establish causation is essential for evaluating empirical arguments. To establish causation, you need to rule out confounding variables and reverse causation — ty*

**Model Response:**
> **1. What is being demonstrated?**  
The council’s initial claim that the tonic *causes* higher yields is an example of the **correlation‑causation fallacy** (also called *cum hoc ergo propter hoc*).  The physician and the third voice are pointing out that the observed correlation is likely driven by a **confounding (omitted‑variable) bias** and possibly by reverse causation.

**2. Precise name**  
- **Correlation‑causation fallacy** (cum hoc ergo propter hoc)  
- **Omitted‑variable bias** (confounding)  

**3. Mechanism – why it is good or bad**  

| Aspect | Why it can be misleading | Why it might be tempting |
|--------|--------------------------|--------------------------|
| **Correlation is not causation** | The data only show that two variables move together.  Without ruling out othe

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the correlation-causation fallacy, explicitly names both alternative explanations (confounding/omitted-variable bias and reverse causation), and explains the mechanism clearly. However, the response does not reach Level 4 because it fails to suggest a specific method

---

### A4.1: Basic probability laws
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** Solve the three probability problems. Show your work and explain which probability law you use for each one.

**Expected Answer:** **Basic probability laws: complement, addition, conjunction** — Problem 1 (complement): P(not-4) = 1 - P(4) = 1 - 1/6 = 5/6. Problem 2 (addition with correction): P(at least one H) = P(H on coin 1) + P(H on coin 2) - P(H on both) = 1/2 + 1/2 - 1/4 = 3/4. Alternatively, use complement: 1 - P(no heads) = 1 - 1/4 = 3/4. Problem 3 (at least one via complement): P(at *The complement rule is the most useful tool in basic probability: often it is easier to calculate the probability of something NOT happening and subtract from 1. The addition rule must correct for dou*

**Model Response:**
> **1. What is being demonstrated?**  
The dice‑master is highlighting a *systematic error in probability reasoning* that many people make when they try to compute the probability of “at least one” of several independent events. The error is that they **add the individual probabilities of each event as if the events were mutually exclusive**, even though the events can occur together.  

**2. Precise name of the pattern/fallacy**  
This is the **“additive fallacy”** (sometimes called the “probability addition error” or “overlap fallacy”). It is a special case of misapplying the **addition rule for probabilities**:  
\[
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\]  
When \(P(A\cap B)=0\) (mutually exclusive events) the rule reduces to \(P(A\cup B)=P(A)+P(B)\). The fallacy occurs when the intersection t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the systematic error (naive addition vs. inclusion-exclusion), explains the mechanism clearly, and accurately solves Problems 1 and 2 with correct reasoning. However, the response is incomplete as it cuts off mid-sentence while addressing Problem 2 in the table, fail

---

### A4.2: Conditional probability and Bayes
**Track:** logic_critical_thinking | **Tier:** what_if | **Type:** good_tool

**Question:** The magistrate asks: given Bob's 99% accuracy and 1000 people in the area with 5 actual robbers, what is the probability that Nancy is truly the robber? Show your reasoning.

**Expected Answer:** **Conditional probability, Bayes' theorem, and base rate reasoning** — The naive answer is 99%, but this ignores the base rate. Using Bayes' theorem: Of 1000 people, 5 are robbers. Bob correctly identifies 99% of 5 robbers = 4.95 true positives. Bob incorrectly identifies 1% of 995 innocent people = 9.95 false positives. Total positive identifications = 4.95 + 9.95 = 1 *Conditional probability requires updating prior probabilities with new evidence. The key insight is that when the base rate is low (few robbers in the population), even a highly accurate test produces*

**Model Response:**
> **1. What is being demonstrated?**  
The magistrate’s line of thought is a classic *base‑rate fallacy* (often called the *prosecutor’s fallacy* when it is applied to criminal evidence).  
The witness’s “99 % accuracy” is treated as if it were the probability that the identified person is guilty, while the very low prior probability that any particular person is the robber is ignored.

**2. Precise name**  
- **Base‑rate neglect / base‑rate fallacy**  
- In legal contexts it is frequently called the **prosecutor’s fallacy** (misinterpreting \(P(\text{evidence}\mid\text{innocent})\) as \(P(\text{innocent}\mid\text{evidence})\)).

**3. Mechanism – why it is wrong**  
- The witness’s “accuracy” is expressed as *sensitivity* (true‑positive rate) and *specificity* (true‑negative rate).  
- The m

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the base-rate fallacy and prosecutor's fallacy, explains the mechanism by distinguishing between P(ID|G) and P(G|ID), and sets up Bayes' theorem with the correct formula and initial values. However, the response cuts off mid-calculation before computing the final pro

---

### A4.3: Base rate reasoning
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** good_tool

**Question:** The patient believes she has a 95% chance of having colon blight. Is she right? Use the base rate and test accuracy to compute the actual probability. Show your work.

**Expected Answer:** **Base rate reasoning in medical screening** — For a population of 100,000: 500 have colon blight (0.5% base rate). Of those 500, the test correctly identifies 95% = 475 true positives. Of the 99,500 without the disease, the test incorrectly flags 5% = 4,975 false positives. Total positive results = 475 + 4,975 = 5,450. P(disease | positive test *The base rate fallacy occurs when people ignore the prior probability of a condition and treat the test accuracy as the probability of having the condition. When a disease is rare (0.5%), the 5% false*

**Model Response:**
> **1. What is being demonstrated?**  
The patient (and the physician’s initial reaction) is ignoring the *prior* probability of the disease – the fact that colon blight occurs in only 0.5 % of the population – and treating the test result as if it were a stand‑alone 95 % certainty. This is the classic **base‑rate fallacy** (also called *base‑rate neglect* or *prior‑probability neglect*).  

**2. Precise name**  
*Base‑rate fallacy* (or *prior‑probability neglect*).  

**3. Mechanism – why it’s wrong (or sometimes right)**  

| Component | What the fallacy does | Why it misleads |
|-----------|----------------------|-----------------|
| **Sensitivity & specificity** | Treats them as if they were the probability that a positive test means disease (positive predictive value). | Sensitivity (tr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the base-rate fallacy by name and explains the mechanism using Bayes' theorem and conditional probabilities. They set up the calculation correctly with the right values. However, the response cuts off before completing the arithmetic to derive the final 8.7% figure, 

---

### A5.1: Denying the antecedent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sergeant Dallow seems confident in his logic. Look at the sign, then look at his reasoning. Does his conclusion actually follow?

**Expected Answer:** **Denying the antecedent** — Dallow reasons from 'If royal writ, then entry' and 'no royal writ' to 'no entry.' He treats the antecedent as necessary when the sign only establishes it as sufficient. *The conditional only tells us P is sufficient for Q, not necessary. Denying the antecedent does not validly yield the denial of the consequent. Other conditions may also lead to Q.*

**Model Response:**
> **1. What is being done?**  
The sergeant is committing a **formal logical fallacy**: **denying the antecedent** (also called *the “if‑P then‑Q, not‑P, therefore not‑Q” fallacy*).

**2. Precise name**  
*Denial of the antecedent* (a type of *non‑sequitur*).

**3. How it works – why it’s wrong**  

| Statement | Logical form | What the sergeant does | Why it fails |
|-----------|--------------|------------------------|--------------|
| “If you carry a royal writ, you may pass.” | \(P \rightarrow Q\) | He takes the sign as a rule. | The conditional is a **sufficient** condition, not a biconditional. |
| “You do not have a royal writ.” | \(\lnot P\) | He notes the player lacks the writ. | From \(\lnot P\) one cannot infer \(\lnot Q\). The rule says *if* you have a writ *then* you may pass, bu

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('denying the antecedent'), correctly distinguishes between sufficient and necessary conditions (noting the rule is not a biconditional), and provides clear counterexamples to explain why the inference is invalid. This meets all criteria for the highest level

---

### A5.2: Affirming the consequent
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Wynn seems sure it was a wolf. Does the conclusion follow from what she observed?

**Expected Answer:** **Affirming the consequent** — Wynn reasons from 'If wolf then large paw prints' and 'large paw prints' to 'wolf.' She treats the consequent as proof of the antecedent. *The conditional tells us a wolf attack would produce large paw prints, but many other causes could too. Observing Q does not allow us to conclude P.*

**Model Response:**
> **1. What is being demonstrated?**  
Wynn is committing the logical fallacy known as **affirming the consequent** (also called the *converse error*).  

**2. Precise name**  
*Affirming the consequent* – an invalid inference of the form  

```
If P then Q
Q
∴ P
```

**3. Why it is good or bad**  

| Mechanism | Why it fails |
|-----------|--------------|
| **Premise is a sufficient, not necessary, condition** | “If a wolf attacked the sheep, we would find large paw prints” tells us that a wolf attack *can* produce large prints, but it does **not** say that large prints *only* come from wolf attacks. |
| **Converse error** | The presence of the consequent (large prints) does not logically guarantee the antecedent (wolf attack). Other large animals (bear, elk, human, etc.) could leave simila

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('affirming the consequent'), provides the correct formal logical structure (If P then Q; Q; therefore P), and clearly explains the mechanism by distinguishing between sufficient and necessary conditions. They also identify alternative explanations (other ani

---

### A5.3: Causal slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Varn seems very worried about this bakery permit. He has given you a chain of consequences. Do you find his reasoning convincing? Why or why not?

**Expected Answer:** **Causal slippery slope** — Varn chains together a sequence of causal claims — competition leads to price drops leads to corner-cutting leads to illness leads to overwhelmed healers leads to plague — treating each link as inevitable. Even if each individual step had a 90% probability, the probability of the entire six-step cha *Probabilities are not preserved across a chain of causal claims. Each link in the chain has its own probability of occurring, and the joint probability of the entire sequence is the product of all the*

**Model Response:**
> **1. What reasoning pattern is being used?**  
The councillor is presenting a *slippery‑slope* argument: a single policy change (granting a second bakery) is claimed to set off an inevitable chain of events that culminates in a catastrophic outcome (a plague).

**2. Precise name**  
*Slippery‑Slope Fallacy* (sometimes called a “cascade” or “chain‑reaction” fallacy).

**3. Mechanism – why it is problematic**  

| Element | What the argument does | Why it is weak or misleading |
|---------|------------------------|------------------------------|
| **Unverified causal links** | Varn asserts: 1) more bakeries → lower prices; 2) lower prices → corner‑cutting; 3) corner‑cutting → bad flour; 4) bad flour → sickness; 5) sickness → overwhelmed healers; 6) overwhelmed healers → plague. | Each link i

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as a 'slippery-slope' argument and accurately explains that the flaw lies in treating speculative causal links as certainties. They note the lack of evidence and the exaggeration of probability. However, the response does not reach Level 4 because it fail

---

### A6.1: Composition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Pip seems very confident in his proof. Is his reasoning valid? Can you spot the mistake?

**Expected Answer:** **Composition fallacy** — Pip infers that a property true of each individual part (each atom is invisible) must be true of the whole composed of those parts (Pip is invisible). But visibility is not a property that transfers from parts to whole in this way — the arrangement and quantity of atoms creates emergent properties l *Properties of individual parts do not necessarily hold for the whole they compose. Each atom is invisible, but billions of atoms arranged into a human body are very much visible. Whether a property tr*

**Model Response:**
> **1. What is being demonstrated?**  
Pip’s argument is a classic **fallacy of composition** (sometimes called the “part‑to‑whole” fallacy).  

**2. Precise name**  
*Fallacy of Composition* – the erroneous inference that a property possessed by every part of an object must also be possessed by the object as a whole.

**3. Mechanism – why it’s wrong**  
- **Premise 1:** “Every atom in my body is invisible to the naked eye.”  
  – This is true: atoms are far too small to be resolved by unaided vision.  
- **Premise 2:** “I am made entirely of atoms.”  
  – Also true.  
- **Conclusion:** “Therefore I must be invisible to the naked eye.”  

The logical leap is that the property “invisible to the naked eye” is *transitive* from parts to whole. That property is **not additive**: invisibility at 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the 'Fallacy of Composition' by name and explains the mechanism clearly: visibility is a collective property dependent on arrangement and density, not a transitive property of individual atoms. While the student did not provide a specific counter-example of a legitim

---

### A6.2: Division
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorin is trying to figure out how much individual parts of the house are worth based on the total value. Does his reasoning work?

**Expected Answer:** **Division fallacy** — Dorin infers that because the whole house has a certain property (being worth 900 gold), each part of the house must share that property proportionally. But the house's value comes from the arrangement and integration of its parts, not from the parts individually. Disassembled lumber and stones are  *The value of the house is an emergent property of its assembled structure — location, craftsmanship, functional integration. Individual beams and stones do not carry proportional shares of that value.*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Dorin is committing the **fallacy of division** (sometimes called the “division fallacy” or “false division”). He assumes that because the whole house is worth 900 gold, each part of the house must be worth a proportional share of that amount.

**2. Precise name**  
*Fallacy of Division* (also known as the “division fallacy” or “false division”).

**3. Mechanism – why it is good or bad**  

| Aspect | What Dorin does | Why it fails |
|--------|-----------------|--------------|
| **Assumption of equal value** | He divides 900 gold by the number of “components” (≈900) and concludes each beam is worth 1 gold. | Value is not a simple additive quantity. Different parts of a house have vastly different market values, uses, and conditions. |
| **Whole‑t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Fallacy of Division' and explains the mechanism well, noting that value arises from synergy and context rather than simple addition. This meets Level 3 criteria. However, the response does not reach Level 4 because it fails to provide examples where whole-to-par

---

### A6.3: Begging the question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Brother Vassyl seems very confident. What do you think about the reasoning he just gave you for trusting the Codex?

**Expected Answer:** **Begging the question (circular reasoning)** — The conclusion — that the Codex is the ultimate authority — is assumed as a premise when the speaker cites the Codex's own claim of infallibility as evidence. The premise and conclusion are nearly identical. *The argument assumes exactly what it is trying to prove. The Codex's reliability is the very thing in question. Formally the argument can be valid — 'P, therefore P' is valid — but validity alone is n*

**Model Response:**
> **1. What is being demonstrated?**  
The priest is using a *circular argument* (also called **begging the question**) to justify the Codex’s authority.  
The claim that “every word in the Codex is unassailable truth” is taken as evidence that the Codex is infallible, yet that very claim is the conclusion the priest is trying to prove.

**2. Precise name**  
- **Circular reasoning** (begging the question)  
- In this context it can also be described as a *self‑referential appeal to authority* because the sole authority is the Codex itself.

**3. Why the reasoning is bad (mechanism)**  
| Element | What it is | Why it fails |
|---------|------------|--------------|
| Premise: “The Codex is infallible.” | Stated by the Codex. | No independent evidence; it is the conclusion. |
| Premise: “The 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly names the fallacy ('circular argument' and 'begging the question') and accurately explains the mechanism: the premise assumes the conclusion without independent evidence. However, the response does not reach Level 4 because it fails to explicitly note the nuance that the argume

---

### A6.4: False dichotomy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Commander Harsk says you must either march north or starve. What is wrong with how he has framed the choice?

**Expected Answer:** **False dichotomy (black-or-white thinking)** — A disjunction is presented as exhaustive when it is not. Harsk forces a choice between two options while ignoring alternatives like fortifying defenses, sending scouts, hiring mercenaries, or appealing to a neighboring lord. *Harsk presents only two options — march or starve — but the disjunction does not exhaust the relevant space. Multiple unmentioned alternatives exist.*

**Model Response:**
> **1. What is being demonstrated?**  
A *false dilemma* (also called an *either‑or* or *black‑and‑white* fallacy).

**2. Precise name**  
**False Dilemma / Either‑Or Fallacy.**

**3. Mechanism – why it is a problem**  

| Feature | How it works in the scenario | Why it is misleading |
|---------|------------------------------|----------------------|
| **Binary framing** | Harsk presents only two options: “march north” or “stay and starve.” | The real decision space is richer (e.g., partial march, defensive fortification, diplomatic outreach, resource re‑allocation). |
| **Exclusion of alternatives** | No mention of other courses of action. | Forces the audience to choose between two extremes, even if both are unacceptable or suboptimal. |
| **Emotional manipulation** | Uses fear (“bleed us 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as a 'False Dilemma' (synonymous with False Dichotomy). They explicitly explain that the disjunction is not exhaustive by listing multiple concrete alternatives (fortification, diplomacy, reinforcements). Furthermore, they demonstrate advanced understandi

---

### A6.5: Equivocation
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Silvertongue claims this argument is logically airtight. Is it? Where does the reasoning go wrong?

**Expected Answer:** **Equivocation** — The argument uses the word 'nobody' in two different senses. In 'Nobody is perfect,' 'nobody' means 'no person' (a universal negative quantifier). In 'Bert is a nobody,' 'nobody' means 'an unimportant or insignificant person.' The argument treats these as the same meaning, creating an illusion of va *The argument trades on an ambiguity. 'Nobody' as a quantifier (no person) and 'nobody' as a noun (an insignificant person) are different concepts. Once you disambiguate the two meanings, the argument *

**Model Response:**
> We need to analyze the scenario: Silvertongue says "Nobody is perfect. Bert is a nobody. Therefore, Bert is perfect." This is a classic example of a logical fallacy: "affirming the consequent" or "fallacy of the undistributed middle"? Let's analyze.

Premises: 1. Nobody is perfect. Means: For all x, if x is a nobody, then x is perfect? Wait "Nobody is perfect" means "No one is perfect." Equivalent: For all x, if x is a person, then not perfect? Actually "Nobody is perfect" means "There is no perfect person." So it's a universal negative: ∀x (Person(x) → ¬Perfect(x)). Or "No one is perfect." So it's a universal negative statement.

Premise 2: Bert is a nobody. Means: Bert is a person and a nobody? "Nobody" is a noun meaning "no one" or "no person." But "Bert is a nobody" is a bit ambiguous:

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the fallacy as 'equivocation' or 'ambiguity' and explicitly notes that the word 'nobody' is being used as both a pronoun ('no one') and a noun ('an unimportant person'). They understand that the argument relies on shifting between these meanings. However, the respons

---

### A6.6: Conceptual slippery slope
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Scholar Tilde claims there is no real difference between a novice and an archmage because you cannot draw a sharp line between the ranks. Is she right?

**Expected Answer:** **Conceptual slippery slope** — Tilde exploits the vagueness of category boundaries. Because there is no sharp line between novice and apprentice, or apprentice and journeyman, she concludes there is no real difference between the extremes. This is the sorites paradox applied to conceptual categories: if removing one grain of sand *The inability to draw a sharp boundary between adjacent cases does not mean there is no difference between the extremes. A first-day novice and an archmage differ enormously in ability, even if the tr*

**Model Response:**
> We need to analyze the scenario: Scholar Tilde argues that there is no real difference between novice and archmage, claiming that skill differences are incremental, so ranks are arbitrary nonsense. This is a fallacy: "argument from ambiguity" or "fallacy of composition"? Actually, it's a "fallacy of equivocation"? Wait: She says "there is no real difference" because there's no sharp line. This is a "fallacy of false equivalence"? She equates differences as arbitrary. This is akin to "argument from ignorance"? No.

It might be "fallacy of the continuum" or "fallacy of the continuum argument" where one denies discrete categories because of a continuum. This is a "continuum fallacy" or "fallacy of the continuum" also known as "fallacy of the continuum" or "continuum fallacy" or "fallacy of th

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as the 'continuum fallacy' (a synonym for the conceptual slippery slope/sorites paradox) and accurately explains the mechanism: conflating the lack of a sharp boundary with the lack of any meaningful difference. They also note that categories ca

---

### A7.1: Ad hominem
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Grus seems pretty passionate about this. But take a step back: what exactly is he asking the council to do, and what reasons does he give? Are those reasons about Maren's proposal, or about something else entirely?

**Expected Answer:** **Abusive ad hominem** — Grus attacks Maren's personal background (newcomer status, lack of farmland, occupation) instead of engaging with the substance of her irrigation proposal: the river data, crop projections, costs, and affected families. He treats her identity as grounds for dismissing the argument. *The quality of an argument is independent of who presents it. Maren's proposal stands or falls on its evidence and reasoning, not on how long she has lived in Ironvale or whether she owns farmland. Gr*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Grus is dismissing Maren’s proposal *because of who she is* (newcomer, shopkeeper, no farmland) rather than because of the merits of the proposal itself. This is an **ad hominem circumstantial** attack – a form of the **genetic fallacy** that rejects an argument based on its source rather than its content.

**2. Precise name**  
*Ad hominem circumstantial (genetic fallacy)* – “Reject the idea because of the person who proposes it.”

**3. Mechanism: why it’s problematic**  
- **Irrelevance**: Maren’s residency or occupation has no logical bearing on the accuracy of river‑flow data, yield projections, or cost estimates.  
- **Cognitive shortcut**: The fallacy exploits a bias that equates “local” or “farmer” status with expertise, leading to an unju

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as ad hominem (specifically circumstantial/genetic fallacy) and clearly explains that Maren's personal attributes are irrelevant to the data-driven argument. Furthermore, the response exceeds Level 3 by implicitly addressing the Level 4 criterion: it dist

---

### A7.10: Burden of proof
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The merchant demands you prove his amulet doesn't work. What is wrong with this?

**Expected Answer:** **Burden of proof** — Shifting the burden of proof from the person making the claim to the person questioning it. *The person making a positive claim bears the responsibility of providing evidence. The inability to disprove something does not constitute evidence that it is true.*

**Model Response:**
> We need to analyze scenario: merchant sells invisible amulets of protection. Customer says "my amulet doesn't work? Prove it! Prove there ISN'T a magical barrier around you right now. You can't, can you? That's because it's working!" This is a classic "argument from ignorance" or "appeal to ignorance" fallacy. Also "argumentum ad ignorantiam" or "proof by impossibility" or "argument from lack of evidence". The merchant claims that because you cannot prove there's no barrier, therefore there must be one. This is a form of "argument from ignorance" or "appeal to ignorance" or "argumentum ad ignorantiam". Also could be "argument from the impossibility of disproof" or "the burden of proof" reversed. The pattern: The merchant shifts the burden of proof to the customer, claiming that the lack of

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'argument from ignorance' (appeal to ignorance) and explicitly links it to the 'burden of proof' reversal. They accurately explain the mechanism (lack of disproof treated as proof of existence) and provide a correct approach (claimant must provide evid

---

### A7.11: Personal incredulity
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Ranger Harlen rejects the fossil evidence because he can't imagine fish becoming people. What error is he making?

**Expected Answer:** **Personal incredulity** — Dismissing a claim because one personally cannot understand or imagine how it could be true. *The complexity of a claim has no bearing on its truth. Many well-supported facts are deeply counterintuitive. Personal failure to comprehend is not a refutation.*

**Model Response:**
> **1. What reasoning pattern is being used?**  
The ranger is committing an **argument from personal incredulity** (sometimes called *appeal to common sense* or *appeal to personal experience*).  

**2. Precise name**  
*Argument from personal incredulity* (also known as *appeal to personal experience*).  

**3. Mechanism – why it’s flawed**  

| What the ranger does | Why it is a fallacy |
|----------------------|---------------------|
| **Relies on personal experience** – “I’ve been a ranger forty years and never seen a fish sprout legs.” | Personal experience is *not* a reliable sample of all possible phenomena. The ranger’s lifetime of observation is a tiny, biased subset of the universe. |
| **Treats lack of disbelief as evidence of falsity** – “That’s the most ridiculous thing I’ve ev

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('argument from personal incredulity'), clearly distinguishes between emotional rejection/personal experience and logical refutation, and provides robust context regarding why complex processes (like evolution) are hard to intuit based on limited human observ

---

### A7.12: Special pleading
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Every time Seer Vashti's powers fail a test, she adds a new excuse. What reasoning error is this?

**Expected Answer:** **Special pleading / No true Scotsman** — When a claim is shown to be false, moving the goalposts by introducing ad hoc exceptions so the claim can never be falsified. *Each time counter-evidence appears, a new exception is added. This makes the claim unfalsifiable. A claim that cannot in principle be proven wrong is not meaningfully supported.*

**Model Response:**
> **1. What is being demonstrated?**  
The psychic is engaging in an **ad‑hoc self‑justification**—a classic instance of the **self‑serving bias** (also called *self‑serving attribution*).  

**2. Precise name**  
- **Ad‑hoc hypothesis / self‑justifying explanation**  
- **Self‑serving bias** (a form of *confirmation bias* and *belief perseverance*)

**3. Mechanism – why it is good or bad**  

| Aspect | How it works | Why it is problematic |
|--------|--------------|-----------------------|
| **Ad‑hoc hypothesis** | When the psychic’s predictions fail, she invents a new, untestable rule (“psychic power is blocked by hostile minds”) that explains away the failure without changing the original claim. | The rule is *post‑hoc* and *unfalsifiable*; it cannot be tested or ruled out. It protects t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the mechanism of inventing untestable rules to explain away failures and explicitly notes the claim becomes 'unfalsifiable.' However, they fail to name the specific fallacy required ('Special pleading'), instead using related but distinct terms like 'ad-hoc hypothesi

---

### A7.13: Loaded question
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Greaves demands a yes-or-no answer. What is the problem with this question?

**Expected Answer:** **Loaded question** — A question containing a built-in assumption so that any direct answer appears to confirm it. *The question presupposes something not established — that Maren used contaminated herbs. Both yes and no accept the false premise.*

**Model Response:**
> **1. What is being demonstrated?**  
The alderman is using a **loaded question** (also called *question‑begging*).  

**2. Precise name**  
*Loaded question* (a form of *begging the question*).  

**3. How it works – why it’s problematic**  

| Feature | Mechanism | Effect |
|---------|-----------|--------|
| **Presupposition** | The question assumes that the healer *has* been using contaminated herbs. | The healer is forced to confront an unverified claim. |
| **Binary framing** | “Yes or no” forces a simple answer that either confirms or denies the presupposition. | Nuance is lost; the healer can’t explain the context or partial compliance. |
| **Rhetorical pressure** | By demanding a straight answer, the alderman signals that any answer other than “yes” is a refusal to cooperate. | The 

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as a 'loaded question' and explicitly explains the embedded presupposition (that the healer used contaminated herbs). Furthermore, they analyze the binary framing ('yes or no') as a false dilemma and discuss how to interpret or reject the premise by highl

---

### A7.14: Texas sharpshooter
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The alchemist tested in thirty villages but only shows five. What reasoning error is he committing?

**Expected Answer:** **Texas sharpshooter** — Cherry-picking data clusters that suit a conclusion while ignoring data that does not. Like painting a target around bullet holes after shooting. *Finding a cluster in a large dataset is virtually guaranteed by chance. Selecting after the fact and presenting as evidence is statistically invalid. Honest analysis requires looking at ALL the data.*

**Model Response:**
> **1. What is being demonstrated?**  
The alchemist is **selectively presenting data** that supports his claim while ignoring the rest of the evidence. This is a classic example of **cherry‑picking** (also called selective‑reporting bias or confirmation bias).

**2. Precise name**  
- **Cherry‑picking (selective evidence)**  
  (Often grouped under the broader category of **sampling bias** or **confirmation bias**.)

**3. Mechanism – why the reasoning is flawed**  
- **Selective focus**: He highlights only the five villages where the pox rate fell, treating them as if they represent the whole population.  
- **Ignored counter‑evidence**: The other 25 villages are omitted, even though they may have shown no change or an increase in pox rates.  
- **No baseline or control**: All surveyed vill

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'cherry-picking' and explains the mechanism of selective focus and ignoring counter-evidence (Level 3 criteria). However, the response does not explicitly name the 'Texas sharpshooter' fallacy, nor does it discuss the specific concept of post-hoc target painting, ran

---

### A7.15: Middle ground
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The mediator proposes combining evidence-based treatment with unsupported one. What is wrong with this?

**Expected Answer:** **Middle ground (false compromise)** — Assuming the truth must lie between two positions simply because they are opposing, regardless of evidence. *Truth is not determined by averaging positions. When one is well-supported and the other baseless, the middle ground corrupts the good position. Draining 'some' blood is still harmful.*

**Model Response:**
> **1. What is being demonstrated?**  
The mediator is committing the **“argument to moderation” (also called the “fallacy of the middle” or “false compromise”)**.

**2. Precise name**  
*Argument to moderation / fallacy of the middle.*

**3. Mechanism – why it is problematic**  

| What the fallacy does | Why it can mislead |
|-----------------------|--------------------|
| Assumes that the “truth” must lie somewhere between two opposing claims. | It ignores the evidence that supports one side, the evidence that refutes the other, and the possibility that neither extreme is correct. |
| Treats a compromise as inherently wiser or safer. | A compromise can dilute an effective treatment or combine two harmful practices, producing a worse outcome than either extreme alone. |
| Presents the midd

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the fallacy ('argument to moderation'), clearly distinguishes between epistemic truth (determined by evidence) and negotiation compromise, and explains how the fallacy ignores evidence. Furthermore, the response goes beyond the basic requirements by detailing edge cases 

---

### A7.16: Anecdotal evidence
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dag dismisses mine dust danger because his grandfather survived it. What reasoning error?

**Expected Answer:** **Anecdotal evidence** — Using personal experience or an isolated example in place of statistical evidence, especially to dismiss systematic data. *A single case cannot override systematic evidence. Dag's grandfather is one data point — possibly an outlier. The question is the overall rate of lung disease among miners, not whether anyone can surv*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The miner is using a single, highly memorable personal story to dismiss a general health claim. This is the classic *anecdotal fallacy* (also called an *appeal to anecdote* or *argument from personal experience*).

**2. Precise name**  
*Anecdotal evidence fallacy* (sometimes grouped under “hasty generalization” or “appeal to personal experience”).

**3. How it works – why it’s problematic**  

| Mechanism | Why it misleads |
|-----------|----------------|
| **Single‑case generalization** | One person’s long life is not a statistically representative sample of all miners. |
| **Survivorship bias** | The anecdote only shows the *survivor*; it ignores those who may have died or become ill earlier. |
| **Confounding variables** | The granddad may ha

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'anecdotal fallacy,' explains why a single case cannot outweigh systematic data, identifies 'survivorship bias' and 'confounding variables' as specific mechanisms, and notes the psychological compelling nature of vivid stories versus abstract statistics. This meets a

---

### A7.2: Straw man
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What is wrong with Alderman Grask's response to Sable's proposal?

**Expected Answer:** **Straw man** — Grask inflates Sable's modest proposal (a south-bank levee) into an extreme position (damming the entire river) and then attacks the extreme version. His criticism C targets fabricated position B, not Sable's actual position A. *Grask's criticism targets a fabricated version of Sable's proposal. A south-bank levee does not dam the river. His objections about livestock and mills are irrelevant to the actual proposal.*

**Model Response:**
> **1. What is happening?**  
Alderman Grask is **misrepresenting** Sable’s modest proposal and then attacking that misrepresentation. He turns a small, localized levee into a claim that the entire river will be dammed and that all downstream farms will be starved of water.

**2. Precise name**  
**Straw‑Man Fallacy** (often coupled with an *appeal to fear* or *argument from consequences*).

**3. Mechanism – why it is bad (and when it can be right)**  

| Element | How it works | Why it is problematic |
|---------|--------------|-----------------------|
| **Misrepresentation** | Grask says “dam the entire river” when Sable said “a modest levee on the south bank.” | The audience is led to think Sable’s plan is far more extreme than it actually is. |
| **Simplification for attack** | By exagge

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Straw-Man Fallacy,' accurately distinguishes between Sable's actual proposal (levee) and Grask's distortion (dam), explains why the criticism is irrelevant to the real argument, and provides a comprehensive section on correct approaches and legitimate edge cases. Th

---

### A7.3: Tu quoque
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Garrett fires back at Inspector Maren by bringing up the oil-lantern incident. What is wrong with his reasoning? Why doesn't Maren's past mistake let Garrett off the hook?

**Expected Answer:** **Tu quoque (appeal to hypocrisy)** — Dismissing a criticism by pointing out that the person making it is guilty of the same or similar fault. Treats the critic's inconsistency as though it refutes the content of the criticism. *Whether or not the critic is a hypocrite has no bearing on the truth of the criticism. The coal dust is either a fire hazard or it is not, regardless of what Maren did last winter. Hypocrisy is a char*

**Model Response:**
> **1. What is being demonstrated?**  
Garrett is using a *tu quoque* (appeal to hypocrisy) ad hominem. He deflects the inspector’s safety claim by pointing out a past lapse in the inspector’s own conduct.

**2. Precise name**  
*Tu quoque* (also called “you‑too” or “appeal to hypocrisy”).

**3. Mechanism – why it’s logically weak (or sometimes psychologically strong)**  

| Aspect | Explanation |
|--------|-------------|
| **Logical structure** | The claim that “coal dust must be moved 30 paces from a dwelling” is a factual, safety‑based assertion. Whether Maren previously left oil lanterns unattended is irrelevant to the truth of that claim. The argument therefore commits a *non‑sequitur*: the premises (Maren’s past mistake) do not logically support the conclusion (Garrett’s argument is in

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'tu quoque' and explains that the critic's past behavior is irrelevant to the truth of the safety claim (Level 3 criteria). Furthermore, the student explicitly details why it is a fallacy of relevance (non-sequitur, distraction from the core issue) and

---

### A7.4: Genetic fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Dorric clearly does not like this formula. But does he point out any problem with the measurements, the chemical rationale, or the engineering requirements? What is his objection really about?

**Expected Answer:** **Genetic fallacy** — Dorric judges the formula by attacking its origin — Vielle's impoverished background — rather than engaging with its content. The chemical rationale and measurements go entirely unaddressed. *The quality of a formula depends on its content — the logic, evidence, and reasoning — not on the biography of whoever produced it. Vielle's background tells you nothing about whether her measurements*

**Model Response:**
> **1. What is being demonstrated?**  
Dorric is committing a *genetic fallacy* (a form of *ad hominem circumstantial*). He dismisses Vielle’s glass‑making formula solely on the basis of her background (“she learned her trade at a poorhouse”) rather than on any evidence about the formula itself.

**2. Precise name**  
*Genetic fallacy* (also called “argument from source” or “ad hominem circumstantial”).

**3. Mechanism – why it is good or bad**  
- **What it does:** It evaluates a claim by asking *where* it came from, not *what* it says.  
- **Why it is bad:** The origin of an idea is irrelevant to its truth value unless the source is demonstrably unreliable or has a conflict of interest. By ignoring the data (the numbers on the chalkboard, experimental results, peer review, etc.) Dorric’s r

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the genetic fallacy, explains that the origin of the idea is irrelevant to its truth value without evidence, and explicitly details edge cases where source credibility matters (incompetence, bias, conflict of interest), fully meeting all Level 4 criteria.

---

### A7.5: Appeal to consequences
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Holt raises serious worries. But is he giving you any reason to doubt Tova's research itself?

**Expected Answer:** **Appeal to consequences** — Arguing that a factual claim should be rejected because accepting it would lead to undesirable outcomes, substituting the consequences for a critique of the evidence. *The truth of a factual claim does not depend on whether its consequences are pleasant. Consequences are relevant to policy (what to do about a finding), not to whether the finding is true.*

**Model Response:**
> **1. What is being demonstrated?**  
Guildmaster Holt is using an **“argument from consequences”** (also called *appeal to consequences* or *argumentum ad consequentiam*). He says:

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern by name ('argument from consequences') and begins to explain the mechanism by quoting Holt. However, the response is incomplete and cuts off before fully articulating how Holt substitutes consequences for evidence or distinguishing this from policy evalua

---

### A7.6: Appeal to authority
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Corvin has a strong expert backing his claim. But what exactly is Eldric an expert in, and what is the question being debated?

**Expected Answer:** **Appeal to authority** — Corvin appeals to Eldric's authority as a surgeon to settle a question about marine toxicology — a field in which Eldric has no special expertise. *An authority's expertise does not transfer automatically to unrelated domains. Eldric's prestige makes his opinion influential but not reliable on marine toxicology.*

**Model Response:**
> We need to analyze the scenario: Corvin uses expert testimony of Master Eldric, a famous surgeon, to assert that dyes will poison fish. He says, "If a man of his stature says the dyes are toxic to fish, that settles it." This is an appeal to authority, specifically an argument from authority (appeal to authority fallacy). But there's nuance: Eldric is a surgeon, not an expert in toxicology or marine biology. So the fallacy is an appeal to authority with a weak authority (irrelevant authority). Also, the argument may be a "bandwagon" or "authority bias" or "argumentum ad verecundiam." Also, there's a potential "appeal to tradition" or "appeal to authority" but the key is that the authority is not relevant. So the reasoning pattern is "appeal to authority" or "argument from authority" fallac

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'appeal to authority' (argumentum ad verecundiam). They clearly explain the mechanism: relying on status rather than evidence, specifically noting the domain mismatch between Eldric's expertise (surgery) and the claim (marine toxicology). Furthermore, 

---

### A7.7: Appeal to emotion
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Matron Geld is clearly upset and has done real good. But does anything she says actually address the evidence in the ledger?

**Expected Answer:** **Appeal to emotion** — Substituting emotional response — pity, guilt, sentiment — in place of addressing the factual evidence. Geld does not contest the ledger; she tries to make accusers feel bad for asking. *Whether she sat up with sick children does not change what the grain ledger shows. The emotional response is designed to block the factual inquiry, not answer it.*

**Model Response:**
> **1. What reasoning pattern is being used?**  
Matron Geld is employing an **appeal to emotion** (specifically an *appeal to pity* or *argumentum ad misericordiam*) and an *argument from anecdote*.

**2. Precise name**  
- **Appeal to pity / argumentum ad misericordiam**  
- **Argument from anecdote (hasty generalization)**

**3. Mechanism – why it is good or bad**  

| Feature | How it works | Why it can be misleading |
|---------|--------------|--------------------------|
| **Emotional storytelling** | Geld recounts personal acts of care (holding Pip, braiding Lila’s hair, staying up for sick children). | The stories trigger empathy, causing the audience to discount the objective ledger evidence. |
| **Ad hoc justification** | “Numbers matter less than love.” | This is a *value claim* th

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as 'appeal to emotion/pity' and explicitly explains the mechanism: substituting emotional storytelling for factual evidence regarding the ledger. Furthermore, the response exceeds the Level 4 requirement by distinguishing between facts and values, outlini

---

### A7.8: Appeal to nature
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Saffron's pitch sounds appealing. What evidence does he give that the spring water cures anything? Is 'it's natural' really a reason?

**Expected Answer:** **Appeal to nature** — Arguing that a product works because it is natural, treating naturalness as sufficient evidence of safety and efficacy. *Naturalness is not a reliable indicator of safety or efficacy. Many natural substances are deadly (hemlock, arsenic). The appeal substitutes a feel-good category for actual evidence.*

**Model Response:**
> **1. What is being demonstrated?**  
Saffron is using an **appeal‑to‑nature** (also called the *naturalistic fallacy*). He argues that because the water is “natural” – untouched by humans, coming straight from the earth – it must be safe and effective.  

**2. Precise name**  
- **Appeal to Nature** (argumentum ad naturam)  
- In moral‑philosophical terms it is a **naturalistic fallacy** (“what is natural is good/true”).  
- In cognitive‑psychology it is a form of **natural‑ness bias** (a heuristic that favors the natural over the artificial).  

**3. Mechanism – why it is good or bad**  

| Aspect | How it works | Why it is problematic |
|--------|--------------|-----------------------|
| **Use of a vague attribute** | “Natural” is a broad, emotionally charged word that people associate w

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'appeal to nature' and the 'naturalistic fallacy,' correctly identifies the mechanism of substituting a vague attribute for evidence, and provides counterexamples of harmful natural substances (poison, toxic plants), fully satisfying all criteria for the highest scor

---

### A7.9: Bandwagon
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** What evidence does Paddy give that the charm works? Is 'everyone is buying one' a reason?

**Expected Answer:** **Bandwagon (argumentum ad populum)** — Arguing that something must be true or good because many people believe it or do it. Treating popularity as evidence. *The number of people who believe something has no bearing on whether it is true. Popularity can be driven by social pressure, marketing, or tradition — none constitute evidence.*

**Model Response:**
> **1. What is being demonstrated?**  
Paddy is using a *bandwagon* argument – an **argumentum ad populum** (appeal to popularity) – to persuade people to buy the charms. He says that because many villagers already have them, the charms must be valuable or true, and that anyone who doesn’t buy will be left out.

**2. Precise name**  
- **Bandwagon fallacy** (also called *appeal to popularity* or *argumentum ad populum*).  
- In behavioral‑economics terms it is an example of an **information cascade** or **herd behaviour**.

**3. Mechanism – why it feels persuasive, why it is flawed**  

| What the fallacy does | Why it can feel convincing | Why it is logically weak |
|-----------------------|----------------------------|--------------------------|
| Uses the number of adopters as evidence | 

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Bandwagon fallacy' and 'argumentum ad populum', correctly identifies the mechanism of using the number of adopters as evidence, explains why popularity does not equate to truth (non-sequitur), and addresses the social pressure component (FOMO/exclusion). The respons

---

### A8.1: Conjunction fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** The deputy thinks it is more likely that Linda is a bank clerk AND an activist than that she is just a bank clerk. Is the deputy's reasoning correct?

**Expected Answer:** **Conjunction fallacy** — The deputy judges P(bank clerk AND activist) > P(bank clerk). This violates a basic law of probability: the probability of a conjunction can never exceed the probability of either conjunct alone. P(A and B) <= P(A). The error occurs because the conjunction fits a compelling narrative (the 'represent *A conjunction adds a constraint. Every bank clerk who is also an activist is already counted among the bank clerks. The set of people who are both A and B is a subset of the set of people who are A. N*

**Model Response:**
> We need to analyze the scenario: Guard Captain Hask has a dossier about Linda. The deputy says it's more likely that Linda is a bank clerk AND a member of the Fair Trade Alliance than that she is simply a bank clerk. The deputy says the activist profile just fits too well. The captain wants opinion. The question: what reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? The deputy is arguing that because Linda has activist background, it's more likely that she is a bank clerk AND a member of the Fair Trade Alliance (i.e., both). The deputy is basically using the "base rate fallacy" or "conjunction fallacy"? Wait, the deputy says "more likely that Linda is a bank clerk AND a member of the Fair Trade Alliance than that she is simply a bank clerk." That is a 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the conjunction fallacy and explicitly states the probability rule P(A and B) <= P(A). They also recognize the role of the representativeness heuristic ('activist profile fits too well'). However, the response lacks the specific connection to the original 'Linda prob

---

### A8.2: Base rate neglect
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sera says there is a 95% chance the patient has Stoneblight based on the positive test. Is she right? What is the actual probability?

**Expected Answer:** **Base rate neglect** — Sera assumes that a positive result on a 95% accurate test means a 95% chance of disease. She ignores the base rate of 0.5%. For 100,000 people: 500 have Stoneblight. The test catches 475 of them (true positives). Of the 99,500 healthy people, the test falsely flags 5% = 4,975 (false positives). Tot *When the base rate of a condition is very low, even a highly accurate test produces far more false positives than true positives. The 95% accuracy tells you about the test's performance, not about thi*

**Model Response:**
> **1. What is being demonstrated?**  
Sera is committing the **base‑rate neglect (base‑rate fallacy)** by treating the test’s 95 % “accuracy” as a 95 % posterior probability that the patient is infected. She is ignoring the very low prevalence of Stoneblight (0.5 %) and the fact that “accuracy” is a conditional probability (sensitivity or specificity), not a predictive probability.

**2. Precise name**  
*Base‑rate neglect / base‑rate fallacy* (sometimes called the “probability fallacy” when a test’s sensitivity/specificity is misread as a predictive value).

**3. Mechanism – why the reasoning is wrong**  
- **Misinterpretation of accuracy**: “95 % accurate” means the test correctly identifies 95 % of diseased people (sensitivity) and correctly clears 95 % of healthy people (specificity). I

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the pattern as base-rate neglect, explicitly explains the mechanism regarding false positives arising from low prevalence, and accurately calculates the posterior probability (~8.7%) using Bayes' theorem. The response also addresses edge cases by discussing decision-

---

### A8.3: Law of small numbers
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Minister Kael says the data proves small schools produce better scholars. Is the data as convincing as he thinks? What should he check before spending 1.7 million gold?

**Expected Answer:** **Law of small numbers / small numbers fallacy** — Kael observes that small schools top the achievement rankings and concludes that being small causes better performance. But smaller populations produce more variable outcomes: with fewer students, a few strong (or weak) performers swing the average dramatically. If Kael checked the bottom of the ran *The law of small numbers states that smaller groups will tend to inhabit the extremes of any ranking. Kael only checked the top — if he checked the bottom, he would also find small schools. The patter*

**Model Response:**
> **1. What is being demonstrated?**  
Minister Kael is committing a **correlation‑causation fallacy** (often called *post‑hoc ergo propter hoc* or *ecological fallacy* when the inference is made from group data to a causal claim). He takes an observed

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies skepticism toward Kael's conclusion and labels it a fallacy (correlation-causation/ecological). However, the response is incomplete and cuts off before explaining the specific mechanism of the 'Law of Small Numbers' (i.e., that small sample sizes lead to higher varia

---

### A8.4: Regression to the mean
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Sal says nine out of ten customers feel better after taking his elixir. Is this good evidence that the elixir works?

**Expected Answer:** **Regression to the mean** — People seek remedies when symptoms are at their peak (an extreme observation). After peak symptoms, the natural tendency is to return to baseline health — this is regression to the mean. Sal attributes the improvement to his elixir, but the improvement would likely have occurred regardless. The nine *Colds typically last a few days and resolve on their own. People buy remedies when they feel worst, which is exactly when improvement is most likely regardless of treatment. To show the elixir actuall*

**Model Response:**
> **1. What is being demonstrated?**  
The peddler is using *anecdotal evidence*—a handful of vivid, self‑selected success stories—to claim that his remedy works for 90 % of users. This is a classic **hasty‑generalization / anecdotal fallacy** (often called an “appeal to anecdote”).

**2. Precise name**  
**Anecdotal fallacy** (also known as *argument from anecdote* or *appeal to anecdote*).

**3. Mechanism – why it is problematic**  

| Feature | Why it misleads |
|---------|-----------------|
| **Selective sampling** | Only customers who felt better are highlighted; those who didn’t (or who had side‑effects) are omitted. This is *sampling bias* and *survivorship bias*. |
| **No control group** | Without a placebo or comparison group, we cannot tell whether the improvement was due to the el

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that improvement could be due to the 'natural course of a cold' and explicitly notes the lack of a control group, which aligns with the core logic of regression to the mean. They also describe a proper controlled test (RCT), touching on Level 4 criteria. However, the

---

### A8.5: Gambler's fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Rurik says the dice are 'owed' a high roll after six lows. What is wrong with his reasoning?

**Expected Answer:** **Gambler's fallacy** — The mistaken belief that if a random event has occurred more frequently than expected, it is less likely to occur next. Each independent trial has the same probability regardless of previous outcomes. *Independent random events have no memory. The probability of a high roll on the 7th throw is exactly the same as on the 1st. Rurik confuses the law of large numbers (long-run convergence) with a suppo*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The narrator is committing the **gambler’s fallacy** (also called the “law of averages” or “fallacy of the mean”).

**2. Precise name**  
*Gambler’s fallacy* – the mistaken belief that a run of one outcome makes the opposite outcome more likely on the next independent trial.

---

### 3. Mechanism – why it’s good or bad

| Aspect | What the fallacy claims | What actually happens |
|--------|------------------------|-----------------------|
| **Independence of rolls** | “The bones are owed a high roll” → probability of a high roll increases after many lows. | Each roll of a fair die is independent; the probability of a high roll is always 1/2 (or whatever the die’s distribution is). |
| **Law of large numbers** | Long streaks *must* be followed by

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Gambler's fallacy' by name and provides a clear, accurate explanation of independent events and why past outcomes do not influence future probabilities. They also distinguish the fallacy from related concepts like the Law of Large Numbers. However, they do not r

---

### A8.6: Hasty generalization
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Breck says all the people of Dunmore are cheats based on his two visits. Is his conclusion justified by his evidence?

**Expected Answer:** **Hasty generalization** — Breck draws a universal conclusion ('all people of Dunmore are cheats') from a sample of two negative interactions. The sample size is far too small to support a generalization about an entire town's population. He is also ignoring the possibility of confounding factors (perhaps he visited during a  *Two encounters cannot justify a universal claim about an entire town. The sample is far too small and likely unrepresentative. Breck may also have selection bias — he remembers the negative experience*

**Model Response:**
> **1. What is being demonstrated?**  
Breck is committing a **hasty generalization** (an inductive fallacy that also embodies the use of anecdotal evidence and confirmation bias).

**2. Precise name**  
*Hasty Generalization* – the logical fallacy of drawing a universal conclusion from an insufficient or unrepresentative sample.

**3. Mechanism – why it is problematic**  

| Feature | How it shows up in Breck’s reasoning | Why it is a flaw |
|---------|-------------------------------------|------------------|
| **Limited sample** | Only two negative experiences (overcharge, rotten apples). | Two incidents are far too few to infer the character of an entire town. |
| **Representativeness** | Breck treats the two incidents as typical of all Dunmore residents. | The incidents may be isolated o

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the fallacy as 'Hasty Generalization' and provides a comprehensive explanation of the mechanism, explicitly noting the insufficient sample size (two incidents) and the lack of representativeness. Furthermore, the response exceeds Level 3 requirements by discussing co

---

### A8.7: False cause (post hoc)
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Councillor Brix says seagulls are causing the decline of the fishing fleet because the two trends are correlated. Is his reasoning sound?

**Expected Answer:** **False cause / post hoc fallacy** — Brix observes that two variables are correlated over time (fishing boats declining, seagulls increasing) and infers that one causes the other. But correlation does not establish causation. There are four possibilities: (1) seagulls cause boat decline, (2) boat decline causes seagull increase, (3) a  *Correlation between two variables does not establish that one causes the other. Brix has not ruled out reverse causation, a common cause, or coincidence. Culling seagulls addresses a symptom at best a*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Councillor Brix is committing the classic *correlation‑causation* fallacy (also called *post hoc ergo propter hoc* or *spurious‑correlation*). He treats a statistical association between two time‑series as proof that one causes the other, and then uses that causal claim to justify a policy.

**2. Precise name**  
*Correlation‑Causation Fallacy* (sometimes phrased as *“correlation implies causation”* or *“post‑hoc”*).

**3. Mechanism – why it’s bad (or, rarely, good)**  

| What the pattern does | Why it can mislead | What it ignores |
|-----------------------|--------------------|-----------------|
| **Assumes a direct causal link** between the two variables because they move together over time. | Correlation can arise from a third factor (confou

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the false cause/correlation-causation fallacy and explicitly names 'post hoc'. They provide a strong explanation of why correlation is insufficient, citing confounders, reverse causality, and chance. They also propose the correct alternative explanation (over-fishing

---

### A9.1: Evaluative language and presupposition
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Vance seems to be complimenting Pip, but something feels off. What rhetorical technique is Vance using?

**Expected Answer:** **Evaluative language and presupposition** — Using loaded terms, diminutives, and embedded presuppositions to bias perception without explicit argument. The framing does the persuasive work while appearing neutral. *This substitutes rhetorical framing for argument. 'Even Pip managed' presupposes expected failure. 'Limited background' presupposes inferiority. None are argued for — they are smuggled in through word*

**Model Response:**
> We need to analyze the scenario: At the Adventurers' Guild, a senior member reviews a junior member's successful quest completion. The senior says: "Well, I suppose even Pip managed to clear the Thornwall Caverns. Quite the accomplishment for someone of his... limited background. I'm sure his little adventure was very exciting for him."

So the senior is praising Pip but also implying that it's surprising because of limited background. The phrase "limited background" suggests maybe Pip is inexperienced or from a lower social class. The senior is making a statement that Pip's accomplishment is notable given his limited background. This could be a form of "halo effect"? Or "stereotype" or "bias"? The senior is attributing Pip's success to his limited background, implying that people from lim

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies that the tone is condescending and notes the implication of surprise based on background. However, they fail to identify the specific linguistic mechanism (evaluative language, diminutives like 'little', and embedded presuppositions) required for Level 2 or higher. I

---

### A9.2: Assuring, guarding, and discounting
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** dual

**Question:** Can you identify the assuring, guarding, and discounting moves in Chelton's speech, and evaluate whether they are doing legitimate or illegitimate work?

**Expected Answer:** **Assuring, guarding, and discounting** — Three rhetorical moves managing acceptance: assuring ('everyone knows') discourages questioning, guarding ('most scholars') hedges while sounding authoritative, discounting ('granted X, but Y') acknowledges then dismisses objections. *When used to replace evidence: 'everyone knows' is social pressure, not evidence. 'Most scholars' is presented without citation. 'Granted but' acknowledges without genuinely weighing.*

**Model Response:**
> **1. What is being demonstrated?**  
The advisor is using an **“appeal to consequences”** (argumentum ad consequentiam) – a fallacious reasoning pattern that justifies an action solely on the basis that its *outcome* is desirable (or undesirable).  

**2. Precise name**  
*Argumentum ad consequentiam* (also called the “appeal to consequences” or “consequentialist fallacy”).  

**3. Mechanism – why it is problematic**  

| Element of the argument | How it works | Why it can be misleading |
|--------------------------|--------------|--------------------------|
| **“Everyone knows the threat is growing”** | Appeals to consensus/authority. | Consensus does not guarantee truth; it merely reflects shared belief. |
| **“Most military scholars agree the fortress is the only viable defense”** | App

**Score:** 1/4 █░░░
**Judge Reasoning:** The student failed to identify the correct pattern (assuring, guarding, discounting), instead misidentifying the argument as an 'appeal to consequences.' While the student noted that the advisor was being pushy and analyzed specific phrases, they attributed them to the wrong rhetorical mechanism. Co

---

### A9.3: The fallacy fallacy
**Track:** logic_critical_thinking | **Tier:** drill | **Type:** bad_thinking

**Question:** Torin says that because Amanda argued badly, the herb must NOT have healing properties. What is wrong with Torin's reasoning?

**Expected Answer:** **The fallacy fallacy** — Assuming that because an argument for a conclusion contains a fallacy, the conclusion itself must be false. A bad argument for X does not prove not-X. *A fallacy means the argument fails to establish its conclusion — it does NOT mean the conclusion is wrong. The herb's properties are empirical, independent of any particular argument about them.*

**Model Response:**
> We need to analyze scenario: Two guild apprentices argue about whether a local herb has genuine healing properties. One says "Silvervein must be medicinal because her grandmother used it" - appeal to tradition. The narrator says it's a textbook appeal to tradition, fallacious, thus silvervein has no healing properties. They claim the argument is fallacious, so conclusion is false. We need to answer 5 points: what reasoning pattern, fallacy, bias, decision-theoretic concept is being demonstrated? Name it precisely. Explain mechanism: what makes reasoning good or bad. What would be correct approach? Edge cases where pattern might be legitimate.

We need to discuss the appeal to tradition fallacy, also might involve argument from authority? Actually "grandmother used it" is not authority but 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the herb might still work despite the bad argument (appeal to tradition) and suggests empirical testing as the correct approach. However, the student fails to identify the specific reasoning pattern committed by the narrator (the Fallacy Fallacy). Instead, the s

---

### B1.1: Decision matrices
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The innkeeper's daughter has laid out the situation. Identify the acts, the states, and the outcomes. Then check: does either act dominate the other with these values?

**Expected Answer:** **Decision matrix construction** — A decision matrix organizes a choice into rows (acts the agent controls), columns (states of the world the agent does not control), and cells (outcomes with assigned values). This is the foundational representation for all of decision theory. *The matrix separates what you control (take or leave the umbrella) from what you do not control (the weather). With these ordinal values, neither act dominates the other: Take Umbrella is better if it*

**Model Response:**
> We need to analyze the scenario: a decision matrix with two actions: take umbrella or leave umbrella. States: Rain or No Rain. Outcomes: numbers 1-4 presumably representing utility or cost. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" We need to identify the pattern. The scenario seems to illustrate the "sunk cost" or "endowment effect" or "loss aversion" or "status quo bias"? Let's analyze.

The player is offered to buy an umbrella for five copper. The innkeeper says: If it rains and you have no cover, you'll be soaked and cold. If the sky clears, the umbrella is dead weight. So the player must decide whether to buy one before setting out. The matrix shows outcomes: If take umbrella and rain: dry but burdened (3). If 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly constructs the decision matrix with the appropriate acts, states, and outcome values. They accurately analyze the matrix to determine that neither act dominates the other, explicitly noting that each action is superior in a different state of the world. However, the response fa

---

### B1.2: Dominance reasoning
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The merchant has set up a matrix. Dominance reasoning gives no clear answer. But is there a deeper problem with how the matrix is constructed? What assumption does dominance reasoning require about the relationship between acts and states?

**Expected Answer:** **Dominance reasoning and state-act independence** — Dominance reasoning says: if one act yields a better outcome in every possible state, choose it. But this only works when states are independent of acts. In the extortion case, whether the cart is damaged depends on whether you pay — the states are not independent of the acts, which violates the str *Dominance reasoning requires that the states of the world are independent of your acts. Here, 'Cart Damaged' is not an independent state — it is caused by your refusal to pay. The correct matrix shoul*

**Model Response:**
> We need to analyze scenario: player in rough district, dockworker demands 10 silver to protect cart. If pay, cart stays safe; if not, risk damage. Pay 10 silver: cost -10, but cart safe. Not pay: risk of damage -400 if damaged, 0 if not. The matrix shows pay vs not pay. The reasoning: look at each state: if cart damaged, pay better; if not damaged, not pay better. So no dominance. But this reasoning is flawed because states are not independent of choice; the probability of damage depends on action. So the fallacy is "ignoring the correlation between action and outcome" or "fallacy of the single outcome" or "conditional independence fallacy". In decision theory, this is akin to "ignoring the decision-dependent probabilities" or "ignoring the fact that the event 'cart damaged' is not indepen

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that dominance reasoning is being misapplied because the states (cart damaged vs. not) are not independent of the acts (paying vs. not paying). They explicitly state that the probability of damage depends on the action, which violates the structural assumption requir

---

### B1.3: Maximax
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The prospector wants the biggest possible payoff and does not care about the downside. Apply the maximax rule: for each expedition, find its best outcome, then pick the expedition with the highest best outcome.

**Expected Answer:** **Maximax** — Maximax identifies the best possible outcome for each act, then selects the act with the highest best-case outcome. It is the optimist's rule: chase the ceiling, ignore the floor. *The best outcome for River Panning is 8, for Hilltop Digging is 12, and for Cave Exploring is 6. Maximax selects the highest of these maxima: 12, corresponding to Hilltop Digging. The prospector shoul*

**Model Response:**
> We need to analyze scenario: prospector chooses expedition maximizing maximum payoff: maximax. The question: "Which expedition should she choose if she follows maximax?" So answer: choose hilltop digging (max 12). But the tasks: identify reasoning pattern, fallacy, bias, or decision-theoretic concept being demonstrated. It's maximax decision rule, which is a decision-making strategy under uncertainty that selects the action with the highest possible payoff. It's a risk-seeking strategy. The fallacy? It's not a fallacy per se, but it's a particular decision rule. But the question likely expects "maximax" as the pattern. They ask: 1. What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? 2. Name it precisely. 3. Explain mechanism. 4. Correct appr

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'maximax,' selects the correct act (Hilltop Digging with a max of 12), and explicitly explains the mechanism (selecting the highest possible payoff) while noting that the rule ignores probabilities and downside risk (risk-seeking nature). The response 

---

### B1.4: Maximin
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** The scholar wants to avoid the worst possible evening. Apply maximin: for each act, find its worst outcome, then pick the act whose worst outcome is highest.

**Expected Answer:** **Maximin** — Maximin identifies the worst possible outcome for each act, then selects the act whose worst case is least bad. It is the pessimist's rule: raise the floor, ignore the ceiling. *The worst outcome for Watch Football is 1 (team loses, evening wasted). The worst outcome for Work on Paper is 2 (team wins, slight regret). Maximin selects the act with the higher minimum: Work on Pa*

**Model Response:**
> **1. What is being demonstrated?**  
The scholar is using a **pessimistic, “worst‑case” decision rule** – the *maximin* (or minimax) principle.  
He is ignoring the

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as a 'pessimistic, worst-case decision rule' and names it 'maximin'. However, the response is incomplete (cutting off mid-sentence), fails to identify the specific numerical minima for the acts, does not explicitly state the final selection ('Work on Pape

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
> We need to analyze scenario: traveling merchant, three trade goods, one type of cargo, unknown which settlement will buy. We have profit matrix. Using Minimax Regret, which cargo should you load? The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" So we need to identify the reasoning pattern that is being demonstrated. The scenario: The player chooses cargo based on minimax regret. The question: "Using Minimax Regret, which cargo should you load?" So we need to compute minimax regret for each cargo. Then choose cargo with lowest maximum regret. Let's compute.

First, profits matrix:

- Furs: Mining 18, Fishing 4, Fortress 3
- Salted Fish: Mining 6, Fishing 16, Fortress 5
- Iron Tools: Mining 10, Fishing 8, Fortress 14

We nee

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly computed the column maxima, built the full regret matrix with accurate arithmetic, identified the maximum regret for each act (Furs=12, Salted Fish=12, Iron Tools=8), and selected Iron Tools as the optimal choice. They clearly articulated the minimax logic (minimizing the maxim

---

### B10.1: Signaling
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The scholar says education might not increase productivity at all — it just signals pre-existing ability. Under what conditions does this signaling work? What is the key property that makes the signal credible?

**Expected Answer:** **Signaling (Spence's job market model)** — In a signaling game, an informed player (Sender) takes a costly action to reveal private information to an uninformed player (Receiver). Separation requires the Single Crossing Condition: the signal must be more costly for low types than high types. In Spence's model, education is the signal, abilit *Signaling theory explains why costly, seemingly wasteful behaviors persist: they provide information that enables better matching. The peacock's tail, college degrees, expensive advertising, and elabo*

**Model Response:**
> We need to analyze the scenario: The scholar writes about Spence's signaling model, explaining that high-ability workers have lower cost of education, low-ability higher cost. For separation to work, education level e must satisfy inequalities: high types want education (100 - e > 40 => e < 60) and low types do not want education (100 - 3e < 40 => e > 20). So any e between 20 and 60 supports a separating equilibrium. The scholar says the signal works because it is differentially costly. The Single Crossing Condition: the marginal cost must be higher for low types.

The question: What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? Name it precisely. Explain mechanism: what makes reasoning good or bad? What would be correct approach? Edge case

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism of differential costs and derives the specific mathematical range (20 < e < 60) for the separating equilibrium, satisfying the Level 2 criteria. They also explicitly name the 'Single Crossing Condition.' However, the response fails to reach Level 3

---

### B10.2: Behavioral GT
**Track:** game_theory | **Tier:** what_if | **Type:** dual

**Question:** Standard theory says Responders should accept any positive offer. They do not. Why? And how do formal models of social preferences (like Fehr-Schmidt) explain both Responder rejections and Proposer fairness?

**Expected Answer:** **Behavioral game theory** — Behavioral game theory studies how real humans deviate from Nash equilibrium predictions. Key findings: (1) Ultimatum Game: people reject unfair offers at personal cost and anticipate this by making fair offers. (2) Level-k reasoning: people think a few steps ahead, not infinitely. (3) Social prefer *Standard backward induction assumes purely self-interested agents. Real humans have social preferences — they care about relative payoffs, fairness, and reciprocity. These preferences are not irration*

**Model Response:**
> We need to analyze scenario: Ultimatum Game, standard backward induction predicts responder accepts any positive offer, proposer offers minimal. But actual data shows offers around 5, mean 4.2, low offers often rejected. This demonstrates that people care about fairness, punishment, social preferences. The instructor says standard theory fails; we need models of fairness.

The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" They want the pattern that the instructor is demonstrating? Or the pattern that the students are demonstrating? The scenario: The instructor explains backward induction, but actual data shows people reject low offers. The instructor says we need social preferences. The question: "What specific reasoning pa

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core concept of 'inequity aversion' and 'social preferences' as the explanation for deviations from Nash equilibrium in the Ultimatum Game. They recognize that people care about fairness and punish unfairness. However, the response fails to reach Level 3 because 

---

### B10.3: Commitment
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Without commitment, the Incumbent gets 2. With commitment, the Incumbent gets 3. How can removing an option make you better off? Explain the mechanism and give another example of a commitment device.

**Expected Answer:** **Commitment** — Commitment devices improve outcomes in strategic settings by making threats or promises credible. The Paradox of Commitment: having fewer options can be advantageous because it changes the opponent's best response. Types include contracts, reputation, precommitment, burning bridges, delegation, and  *Commitment is one of the most practically important concepts in game theory. It explains why binding yourself can be strategic: constitutions that are hard to amend, independent central banks, Odysseu*

**Model Response:**
> We need to analyze the scenario: The instructor says that by limiting options (removing Accommodate) the incumbent can commit to Fight and get better outcome. This is a paradox of commitment: fewer options leads to better outcome. This is reminiscent of "option paradox" or "option elimination paradox" or "option paradox of commitment" or "option paradox" or "option paradox of commitment" or "option paradox" known in game theory as "option paradox" or "option paradox of commitment" or "option paradox of commitment" or "option paradox" or "option paradox of commitment" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "option paradox" or "op

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism: eliminating the 'Accommodate' option makes the threat to 'Fight' credible, changing the entrant's best response and improving the incumbent's outcome. They also note edge cases regarding credibility and costs. However, the response fails to reach 

---

### B10.4: Reputation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The instructor lists four conditions for reputation to sustain cooperation. What are they? If any one fails, how does cooperation break down? Give a real-world example of a reputation system and explain which conditions it satisfies.

**Expected Answer:** **Reputation and the shadow of the future** — Reputation is what others believe about your type or strategy based on past actions. In repeated games, reputation creates incentives for cooperation: defecting today earns a short-term gain but destroys future cooperation opportunities. The Folk Theorem shows that in infinitely repeated games (or g *Reputation is the informal counterpart of formal commitment. Where contracts bind through law, reputation binds through expectations. Online rating systems (eBay, Uber), professional networks, and com*

**Model Response:**
> We need to analyze the scenario: instructor explains reputation effects in repeated games. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" We need to identify a reasoning pattern or fallacy. The instructor says: "In a one-shot game, defection is free — there is no tomorrow. But in a repeated game, your actions create a reputation. Reputation is an asset: built by cooperation, destroyed by defection, hard to rebuild once lost." She writes conditions for reputation to work: repeated interactions, observability, patience, punishment mechanism. "When all four hold, the Folk Theorem guarantees that cooperation can be sustained. Reputation makes the shadow of the future tangible — your past actions determine your future opportu

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core concept (reputation) and lists the four necessary conditions (repetition, observability, patience, punishment). They also mention the Folk Theorem. However, the response fails to reach Level 3 or 4 because it lacks a clear, cohesive explanation of how these 

---

### B2.1: Betting rates and credences
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Bob risks 2 gold to win 1 gold, with a total stake of 3 gold. If this bet is fair in Bob's eyes, what is his credence — his subjective probability — that the storm will come? Show the calculation.

**Expected Answer:** **Fair betting rate as credence** — A fair betting rate quantifies subjective probability. If an agent considers a bet fair (expected value zero), their credence in the proposition equals their potential loss divided by the total stake. Bob risks 2 gold on a 3 gold total stake, so his credence in the storm is 2/3. *Bob's willingness to risk 2 gold to win 1 gold on a total stake of 3 gold implies he considers the bet fair at a probability of 2/3. The formula is Pr(S) = Potential Loss / Total Stake = 2/3. If his t*

**Model Response:**
> We need to analyze scenario: Bob willing to bet 2 gold to win 1 gold if storm comes. So Bob is willing to risk 2 to win 1. That implies his expected value of bet: If storm probability p, expected payoff = p*1 - (1-p)*2 = p - 2 + 2p = 3p - 2. For fair bet, expected value zero => 3p - 2 = 0 => p = 2/3. So Bob's credence is 2/3. But question: "If this is a fair bet in Bob's eyes, what does it tell you about how confident Bob is that the storm will come? Calculate his credence." So answer: 2/3.

But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" This is about interpreting odds from betting. The pattern is "odds interpretation" or "probability from odds" or "betting odds to probability conversion." But maybe the pattern is "t

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly calculates the credence as 2/3 using the expected value formula (setting EV to 0) and explicitly explains the mechanism of a 'fair bet.' However, the response does not reach Level 4 because it fails to discuss counterfactuals or edge cases regarding how the odds would change if

---

### B2.2: Dutch Book arguments
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The bookie's implied probabilities sum to 1.05. Explain why this guarantees the bookie a profit regardless of which horse wins. Then answer: if a gambler's personal credences summed to more than 1, how could someone exploit them?

**Expected Answer:** **Dutch Book argument** — A Dutch Book is a set of bets that guarantees a net loss for the agent regardless of the outcome. The Dutch Book theorem proves that if an agent's credences violate the axioms of probability (e.g., sum to more or less than 1 for an exhaustive partition), there exists a set of bets the agent consider *Mercer collects $210 in bets (each bettor pays at odds that imply the listed probabilities). No matter which horse wins, the payout is $200. Mercer pockets $10 guaranteed. From the gambler's side: if *

**Model Response:**
> We need to analyze scenario: bookie sets odds with implied probabilities >1, guaranteeing profit. Professor says if a gambler has credences that sum to >1, can someone construct bets that guarantee gambler loses money no matter what? This is about Dutch book argument. The professor is invoking the Dutch Book theorem: if probabilities don't sum to 1, you can construct a set of bets that guarantees loss. But the scenario: gambler's credences sum to >1, but they are not necessarily probabilities? The gambler's credences are personal beliefs. The Dutch Book theorem says that if a rational agent's credences violate probability axioms (including additivity), then there is a set of bets that will guarantee a loss. But the professor's claim that "guaranteed loss" is correct only if the gambler's c

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Dutch Book argument' and explains the core mechanism: if credences sum to more than 1, a set of bets can be constructed to guarantee a loss. They also successfully generalize this to the concept of coherence and the violation of probability axioms. However, the 

---

### B2.3: Axioms of probability
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Nell says something doesn't add up. She's right. Look at the implied probabilities on Oliver's board. What mathematical rule do they violate, and what does that mean for anyone betting at these odds?

**Expected Answer:** **Axioms of probability** — The three axioms of probability require: (1) Non-negativity: all probabilities >= 0; (2) Normality: probabilities over the entire sample space sum to exactly 1; (3) Finite Additivity: for mutually exclusive events, P(A or B) = P(A) + P(B). Oliver's odds violate Axiom 2 because the implied probabilit *When probabilities violate Axiom 2 (normality), a Dutch Book becomes possible. Oliver collects $210 in bets but only pays out $200 regardless of winner. The gambler who accepts these odds as fair is g*

**Model Response:**
> We need to analyze scenario: bookie odds sum to 1.05 > 1. This indicates overround (vig). The gambler Nell says something off. The reasoning pattern: gambler noticing that probabilities sum >1 indicates bookmaker's margin. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: The gambler is noticing that the implied probabilities sum to >1, which is typical for bookmakers to make profit. The reasoning pattern might be "overconfidence bias" or "anchoring"? But the gambler is noticing something about numbers not adding up. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The gambler is noticing that the odds are not fair. The concept: "overround" or

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the implied probabilities sum to 1.05 and notes this exceeds 1, indicating a bookmaker's margin (overround). However, the response fails to explicitly name or explain the violation of the specific probability axiom (Normality) as required for Level 3. Furthermor

---

### B2.4: Subjective vs objective probability
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss and Lira are both using the word 'probability' but seem to mean different things. Are they contradicting each other, or could both be right? What exactly is the difference between what they are describing?

**Expected Answer:** **Subjective vs objective probability** — Objective probability (chance) refers to mind-independent features of the world — physical propensities, frequencies, quantum indeterminacies. Subjective probability (credence) refers to an agent's degree of confidence in a proposition, revealed through betting behavior. Both satisfy the same axioms *Both scholars are correct within their domains. Probability is genuinely ambiguous between chance (a physical property) and credence (a psychological state). The mathematical formalism — the three axi*

**Model Response:**
> **1. What is being demonstrated?**  
The two scholars are engaging in **equivocation** – they are using the word *probability* to mean two different things and then treating the two meanings as if they were the same. In decision‑theoretic language this is the classic confusion between **objective (frequentist) probability** and **subjective (Bayesian) probability**.

**2. Precise name**  
*Equivocation between objective and subjective probability* (sometimes called the *probability‑interpretation fallacy*).

**3. Mechanism – why it is bad**  
- **Same lexical item, different ontological status**: Voss treats probability as a physical property of the comet’s orbit (an objective, measurable fact). Lira treats it as a degree of belief in a human mind (a subjective, epistemic state).  
- **Imp

**Score:** 3/4 ███░
**Judge Reasoning:** The student clearly distinguishes between objective probability (physical property/frequency) and subjective probability (degree of belief), correctly identifying the ontological difference. They also explicitly state that both satisfy probability axioms implicitly by referring to them as valid inte

---

### B2.5: Principal Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Brennan says Cade is not Dutch-Bookable — his probabilities add up. So what exactly is wrong with Cade's reasoning? Is there a norm of rationality he is violating that goes beyond the three axioms?

**Expected Answer:** **Principal Principle** — The Principal Principle (Lewis/Weatherson) states: if you know the objective chance of an event is x, your rational credence should be x, provided you have no inadmissible evidence (e.g., time travel, crystal balls). Formally: Pr(p | Ch(p)=x) = x. Cade knows Ch(Heads)=0.80 but sets Cr(Heads)=0.50, v *Cade's credences are internally consistent (they satisfy the axioms) but externally miscalibrated. The Principal Principle provides the missing norm: when objective chances are known, rational credenc*

**Model Response:**
> We need to analyze scenario: gambler flips biased coin with known 80% heads. He bets on tails at even odds, claiming gut says 50-50. He is not violating logic, credences sum to 1, not Dutch-bookable. But is he rational? The question: identify reasoning pattern, fallacy, bias, decision-theoretic concept. He is ignoring evidence of bias, relying on intuition, maybe "belief bias" or "overconfidence" or "illusion of control" or "gambler's fallacy"? Actually gambler's fallacy is about expecting a change after streaks. Here he thinks coin is fair because of gut. He is ignoring known probability. He might be demonstrating "belief bias" or "bias to overestimate randomness" or "misleading prior." He may be using "subjective probability" that doesn't match objective. He might be demonstrating "proba

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies that Cade is being irrational by ignoring objective statistical evidence in favor of intuition ('gut feeling') and notes the negative expected value. However, the response fails to identify the specific decision-theoretic concept required (the Principal Principle). I

---

### B3.1: MEU formula and calculation
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Calculate the expected utility of each option using the formula EU(Act) = sum of P(State) * U(Act|State). Which option should the healer choose, and why does it differ from what dominance reasoning would say?

**Expected Answer:** **Maximize Expected Utility (MEU)** — MEU weighs each outcome by its probability and sums to get the expected utility of each act. The agent selects the act with the highest expected utility. EU(Act) = P(S1)*U(Act|S1) + P(S2)*U(Act|S2) + ... *EU(Use Cream) = -35 and EU(Do Nothing) = -50. Since -35 > -50 (losing 35 silver is better than losing 50), the healer should use the cream. Notably, dominance reasoning would recommend Do Nothing (it *

**Model Response:**
> We need to analyze scenario: healer has two options: use cream or do nothing. They have probabilities and costs. They want to calculate expected cost. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: The healer writes expected utilities but maybe miscalculates? Let's compute expected costs: Use cream: 0.85 * (-20) + 0.15 * (-120) = -17 - 18 = -35? Wait -20*0.85 = -17; -120*0.15 = -18; sum = -35. So expected cost -35 silver (i.e., net saving of 35? Actually negative cost means net benefit? But they treat cost as negative utility). Do nothing: 0.5 * 0 + 0.5 * (-100) = -50. So expected cost -50. So do nothing yields lower expected cost (more negative). So choose do nothing. But perhaps the healer incorrectly cal

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly sets up the MEU formula and performs the arithmetic accurately for both options (EU(Cream) = -35, EU(Nothing) = -50). However, they fail to identify the correct recommendation, erroneously concluding that 'Do Nothing' (-50) is the better option because it is 'more negative,' fa

---

### B3.2: Cardinal vs ordinal utility
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** Captain Aldric's scout gave rankings but not numbers. Why is that not enough for a good decision here? What additional information would you need, and how would it change the analysis?

**Expected Answer:** **Cardinal vs ordinal utility** — Ordinal utility provides only a ranking: A > B > C. Cardinal utility assigns numerical values that capture how much better A is than B. Decision rules like Maximin and Maximax use ordinal utility and are therefore blind to magnitude. MEU requires cardinal utility because it multiplies utility by pro *With ordinal utility, the ranking is Hilltop > Bridge > Ravine in both states, so all rules agree on Hilltop. But the magnitude matters: Hilltop's advantage over Bridge in the North scenario (20 vs 12*

**Model Response:**
> **1. What is being done?**  
The captain is applying the **maximin (or minimax‑worst‑case) rule** to a set of *ordinal* rankings.  
He treats the scout’s “Hilltop > Bridge > Ravine” list as if it were a complete utility scale and then picks the option whose *worst* ranking is best. Because the worst ranking for Hilltop (enemy from the south) is only “slightly below” Bridge, the maximin rule still prefers Hilltop, even though the actual loss in that scenario is tiny compared with the catastrophic loss on Ravine when the enemy comes from the north.

**2. Precise name**  
*Ordinal‑maximin fallacy* (sometimes called the “maximin with only rankings” or “ordinal dominance” error).  
It is a misuse of the **maximin criterion** when only ordinal preferences are available.

**3. Why it is good or b

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the captain is using the maximin rule on ordinal rankings and explicitly states that this approach 'collapses all differences' and 'erases the magnitude of the losses,' which satisfies Level 2. However, the response fails to reach Level 3 because it does not exp

---

### B3.3: Risk aversion and utility curves
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Kael calls Sera irrational because she turns down a bet with higher expected monetary value. Is he right? Or is there a way to explain Sera's preference that is perfectly consistent with maximizing expected utility?

**Expected Answer:** **Risk aversion and utility curves** — Under MEU, risk attitude is encoded in the shape of the utility function. A linear utility function (U = wealth) produces risk neutrality. A concave function (e.g., U = sqrt(wealth)) produces risk aversion: the utility of the expected value exceeds the expected utility of the gamble. Sera's declinin *Sera is not irrational. Her utility function is concave (diminishing marginal utility), so she values certainty more than a gamble with the same expected monetary value. With U=sqrt(x): EU(Stay)=20.0 *

**Model Response:**
> We need to analyze scenario: Kael uses expected value. Sera uses risk aversion, diminishing marginal utility. She says expected value may be 500 but would rather have 400 certain. She claims that jump from 0 to 400 matters more than from 400 to 1000. She is basically applying diminishing marginal utility of wealth, risk aversion. She says Kael is irrational. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" We need to identify the concept. It's risk aversion, diminishing marginal utility, utility function concave. She is not committing a fallacy; it's rational under a concave utility function. But maybe the scenario is about "certainty effect" or "certainty bias" or "certainty advantage." But Sera is not making a fallacy; s

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core concepts: risk aversion, diminishing marginal utility, and the concave shape of the utility function. They accurately explain the mechanism (the utility gain from 0 to 400 exceeds 400 to 1000) and correctly assert that Sera's choice is rational rather than a

---

### B3.4: Transitivity and money pumps
**Track:** decision_theory | **Tier:** drill | **Type:** good_tool

**Question:** John keeps cycling through ice cream trades and losing money. What structural property of his preferences allows the vendor to exploit him? What would John need to change about his preferences to stop the bleeding?

**Expected Answer:** **Transitivity and money pumps** — Transitivity requires: if A > B and B > C, then A > C. John's preferences violate transitivity (S > C, C > V, but V > S). The money pump shows that intransitive preferences are exploitable: an agent can be led through a cycle of individually rational trades that return them to the starting point min *Each individual trade is rational by John's own lights — he always trades for something he prefers. But the cycle as a whole is irrational: he ends up with the same item and less money. The money pump*

**Model Response:**
> We need to analyze scenario: vendor offers trades, John has preferences: Strawberry > Chocolate > Vanilla > Strawberry (cyclic). So John has a non-transitive preference cycle. The vendor exploits this to extract copper each time. The reasoning pattern: John is making choices based on immediate preference, but the vendor is exploiting the non-transitivity. The vendor is using a "transitivity fallacy" or "non-transitive preferences" or "circular reasoning" or "cyclic preferences" to create a "trading cycle" that yields profit. The vendor's reasoning: "John prefers X to Y, so I can offer Y for X and he will trade." This is a "transitivity fallacy" or "non-transitive preference exploitation" or "circular reasoning" or "non-transitive cycle" or "intransitive preferences." The vendor is using "t

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the cyclic structure of John's preferences (S > C > V > S) and notes that the vendor exploits this to extract money. However, the response fails to clearly name 'transitivity' as the specific violated property, instead confusingly oscillating between terms like 'tran

---

### B3.5: IIA
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin asks how removing an option nobody chose can change the recommendation. What principle is being violated here, and why does MEU avoid this problem?

**Expected Answer:** **Independence of Irrelevant Alternatives (IIA)** — IIA states: if option C is chosen from set S, then C should still be chosen from any subset of S containing C. Minimax Regret violates IIA because regret is calculated relative to the best available option in each state. When the menu changes, the reference point changes, which can reverse preferenc *MEU satisfies IIA because each option's expected utility depends only on its own payoffs and the state probabilities, not on what other options are available. Minimax Regret violates IIA because regre*

**Model Response:**
> We need to analyze scenario: decision under uncertainty, minimax regret. Initially options: Picnic, Baseball, Movies. Weather states: Sunny, Light Rain, Thunderstorm. Utility matrix given. Minimax regret: compute regret matrix: subtract best utility per state. For Sunny: best 20 (Picnic). Regrets: Picnic 0, Baseball 5, Movies 12. Light Rain: best 10 (Movies). Regrets: Picnic 5, Baseball 8, Movies 0. Thunderstorm: best 9 (Movies). Regrets: Picnic 9, Baseball 3, Movies 0. Max regret per option: Picnic 9, Baseball 8, Movies 12. So minimax regret chooses Baseball (8). Then Picnic cancelled. Remove Picnic. Recompute regret matrix: For Sunny: best 15 (Baseball). Regrets: Baseball 0, Movies 7. Light Rain: best 10 (Movies). Regrets: Baseball 8, Movies 0. Thunderstorm: best 9 (Movies). Regrets: Bas

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the Independence of Irrelevant Alternatives (IIA) and explains the mechanism of the violation: regret is relative to the best option in the set, so removing an option changes the reference point and alters regret values. They also correctly contrast this with rules l

---

### B3.6: Pascal's Wager
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Father Clement's argument seems airtight — infinity times anything positive is infinity. But Dara is not convinced. What are the strongest objections to the Wager, and what do they reveal about the limits of expected utility theory?

**Expected Answer:** **Pascal's Wager** — Pascal's Wager applies MEU with infinite utility. When any outcome has infinite value, the expected utility calculation is dominated by that outcome regardless of its probability (as long as P > 0). This 'washing out' effect makes MEU insensitive to evidence — a feature that many consider a reductio *The Wager has several structural problems: (1) The many-gods objection: multiple incompatible religions offer infinite rewards, so the argument cannot uniquely recommend one faith. (2) The washing-out*

**Model Response:**
> **1. What is being demonstrated?**  
Father Clement is using an *infinite‑utility argument* (sometimes called the *infinite‑reward fallacy* or *infinite‑expected‑utility fallacy*). He treats the value of “heaven

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the core mechanism (infinite utility) and senses the argument is flawed by labeling it a 'fallacy.' However, the response is incomplete and cuts off before articulating a specific objection (like the many-gods problem) or explaining the structural 'washing out' effec

---

### B3.7: St. Petersburg Paradox
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** The expected value is infinite, but you would not pay a million gold to play. What has gone wrong? Is expected value the wrong tool, or are we applying it to the wrong quantity?

**Expected Answer:** **St. Petersburg Paradox** — A fair coin is flipped until heads. Payoff = 2^n where n is the number of flips. Expected value = sum from n=1 to infinity of (1/2)^n × 2^n = sum of 1 = infinity. Yet no reasonable person would pay more than about 20-30 gold. The paradox reveals that expected monetary value is not the same as expect *Expected monetary value diverges to infinity, suggesting unlimited willingness to pay. This is absurd — it would recommend mortgaging everything for a game that usually pays 2 or 4 gold.*

**Model Response:**
> We need to analyze the scenario: gambler offers infinite expected value game. The player calculates infinite EV and says rationally should pay any finite amount. This is the St. Petersburg paradox. The reasoning pattern is the "St. Petersburg paradox" or "infinite expected value paradox" or "expected value fallacy" or "infinite expectation fallacy". The concept: expected value is not the only criterion; utility, risk aversion, bounded rationality. The gambler's reasoning is flawed because it ignores diminishing marginal utility, risk, and the fact that the expected value diverges but the probability of large payouts is extremely small. The correct approach: consider utility function, risk aversion, or use a finite upper bound on wealth, or use the concept of "expected utility" or "bounded 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the St. Petersburg paradox and explains the core resolution: expected monetary value diverges, but expected utility converges due to diminishing marginal utility and risk aversion. They address edge cases (infinite wealth/linear utility). However, they do not reach L

---

### B4.1: Allais Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The showmaster says choosing Gamble 1 and Gamble 4 is inconsistent. Can you see why? What principle of MEU does this combination violate? Hint: look at the column for Tickets 12-100.

**Expected Answer:** **Allais Paradox (Certainty Effect)** — The Allais Paradox demonstrates that people overweight certainty. In Choice 1, Gamble 1 offers certainty ($1M guaranteed), which has disproportionate psychological appeal. In Choice 2, neither option is certain, so people chase the higher payoff (Gamble 4). But the 89% column (Tickets 12-100) is ide *The preference pair (G1>G2 and G4>G3) violates the Sure Thing Principle: if outcomes are identical in some states, those states should not affect the preference. Once the 89% column is masked, both ch*

**Model Response:**
> We need to analyze the scenario. The showmaster presents two pairs of gambles. The first pair: Gamble 1: guaranteed 1,000,000 gold (all tickets pay). Gamble 2: Ticket #1 pays 0, Tickets #2-11 pay 5,000,000, Tickets #12-100 pay 1,000,000. So expected value of Gamble 2: 1/100*0 + 10/100*5,000,000 + 89/100*1,000,000 = 0 + 500,000 + 890,000 = 1,390,000. So EV higher. But gamble 1 is guaranteed. People choose gamble 1 because of risk aversion? But the showmaster says most choose gamble 1 over 2, and gamble 4 over 3. But those two choices together are mathematically inconsistent under Expected Utility Theory. So the pattern is something like "compensating variation" or "choice consistency" or "separability" or "independence axiom" or "common consequence" or "common ratio" or "non-transitivity"? 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the choices are mathematically inconsistent under Expected Utility Theory and performs the algebraic derivation showing the contradiction (11u(1M) > 10u(5M) vs the reverse). They also list relevant terms like 'common consequence' and 'independence axiom'. Howeve

---

### B4.2: Sure Thing Principle
**Track:** decision_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Voss shows that you should accept the bet unconditionally but reject it in every conditional state. Is the Sure Thing Principle actually violated here? Look carefully at whether the conditioning events form a proper partition.

**Expected Answer:** **Sure Thing Principle** — STP states: if A is preferred to B conditional on E, and A is preferred to B conditional on NOT-E, then A is preferred to B unconditionally. It is the backbone of independence in MEU. The Disjunction Effect appears to violate STP but actually involves overlapping (non-exclusive) conditioning events, *STP is not violated here because 'at least one H' and 'at least one T' are NOT mutually exclusive — they overlap on {HT, TH}. The overlap contains only losing outcomes. Each conditional eliminates a w*

**Model Response:**
> We need to analyze the scenario: The Sure Thing Principle (STP) says if you prefer A over B given E and also prefer A over B given not-E, then you should prefer A over B regardless of E. The puzzle: bet on two fair coin flips: win 5 gold if both coins match, lose 4 gold otherwise. EV = (1/4 * 5) + (3/4 * -4) = 1.25 - 3 = -1.75? Wait compute: 5*0.25 = 1.25; -4*0.75 = -3; sum = -1.75. That's negative. But the puzzle says expected value is +0.50 gold? Let's compute again: maybe they mis-specified. Let's compute: If you win 5 gold if both coins match (HH or TT) probability 1/4, lose 4 gold otherwise probability 3/4. EV = 5*0.25 + (-4)*0.75 = 1.25 - 3 = -1.75. So negative. But puzzle says EV +0.50 gold. Maybe they mis-specified payoffs: maybe win 5 gold if both match, lose 4 gold otherwise. Tha

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the scenario as the Disjunction Effect and notes the apparent violation of the Sure Thing Principle (rejecting conditionally but accepting unconditionally). However, the student fails to identify the actual mechanism resolving the paradox: that the conditioning event

---

### B4.3: Newcomb's Problem
**Track:** decision_theory | **Tier:** puzzle | **Type:** dual

**Question:** Are you a one-boxer or a two-boxer? Whatever you choose, you must defend your reasoning against the strongest version of the opposing argument. What principle are you relying on, and what are you giving up?

**Expected Answer:** **Newcomb's Problem** — Newcomb's Problem pits Dominance against Expected Utility when states are correlated with acts. Causal Decision Theory (CDT) says: the Predictor's choice is fixed, so taking both dominates (you are 1,000 gold richer regardless). Evidential Decision Theory (EDT) says: one-boxing provides strong evide *There is no consensus — this is a genuine philosophical puzzle. CDT says two-boxing is rational because you cannot cause the past to change. EDT says one-boxing is rational because it manages the evid*

**Model Response:**
> We need to analyze scenario: Two-boxing vs one-boxing. The predictor is almost infallible. The one-boxer says: take only Box A because predictor likely predicted correctly. Two-boxer says: take both because you get 1,000 more regardless. This is classic Newcomb's problem. The reasoning patterns: "One-boxer" uses "predictor's accuracy" reasoning, which is a form of "correlation fallacy" or "predictor-based reasoning" or "Newcombian reasoning". The two-boxer uses "dominance principle" or "dominance argument" from decision theory: always take both because it's weakly dominant. This is "dominance fallacy" or "dominance principle" but misapplied because the payoff depends on predictor's prediction, which is correlated with your choice. The pattern is "correlation fallacy" or "predictor fallacy"

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the scenario as Newcomb's Problem and articulates the two-boxer's dominance argument clearly. They also mention the one-boxer's reliance on predictor accuracy and distinguish between Causal and Evidential Decision Theory. However, the response fails to reach Level 3 

---

### B4.4: Ellsberg Paradox
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The dealer says choosing G1 and G4 is inconsistent. Can you see why? What probability would you need to assign to Black to justify G1 over G2? And what probability would you need for G4 over G3? Can both be true?

**Expected Answer:** **Ellsberg Paradox (Ambiguity Aversion)** — The Ellsberg Paradox shows that people prefer known risk (Red: exactly 1/3) over ambiguous risk (Black: unknown proportion). Preferring G1>G2 implies P(Black)<1/3. Preferring G4>G3 implies P(Black)>1/3 (because Yellow cancels out as common consequence). These two implications are contradictory — no  *The preference pattern (G1>G2, G4>G3) violates subjective expected utility because no single probability assignment to Black is consistent with both preferences. This reveals that humans distinguish b*

**Model Response:**
> We need to analyze scenario: There are 90 balls, 30 red, 60 black or yellow unknown mix. Gambles: 1: win 100 if red. 2: win 100 if black. 3: win 100 if red or yellow. 4: win 100 if black or yellow.

People prefer Gamble 1 over 2 because they know red probability 1/3. They prefer Gamble 4 over 3 because black+yellow is 2/3. But that combination is mathematically impossible if you have a single consistent probability for black. So they think: P(R)=1/3, P(B)+P(Y)=2/3. But they also think P(B)=? They think gamble 4 better than 3 because P(B)+P(Y)=2/3 > P(R)+P(Y)=? Wait gamble 3: red or yellow: probability = P(R)+P(Y) = 1/3 + P(Y). Gamble 4: black or yellow: probability = P(B)+P(Y) = 2/3. So they think gamble 4 > gamble 3 because 2/3 > 1/3 + P(Y). But that would require P(Y) < 1/3. But we don't

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that preferring Gamble 1 over 2 implies a specific belief about the probability of Black (P(B) < 1/3). However, the analysis of the second pair (G4 > G3) is confused and mathematically flawed; the student incorrectly claims G4 has a fixed probability of 2/3 and fails

---

### B4.5: Reflection Effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The expected values are the same within each pair, yet the merchants' risk preferences flip. What does this tell you about the shape of the human utility function? Can a single curve explain both patterns?

**Expected Answer:** **Reflection Effect** — The Reflection Effect shows that people are risk-averse when choosing among gains (prefer sure $500 over 50/50 shot at $1000) but risk-seeking when choosing among losses (prefer 50/50 shot at losing $1000 over sure loss of $500). Under MEU, a utility function is either consistently concave (always r *A single concave utility function predicts risk aversion everywhere. A single convex utility function predicts risk seeking everywhere. The data shows a split: concave for gains, convex for losses. No*

**Model Response:**
> We need to analyze the scenario: The merchants choose A over B (sure gain vs gamble) but choose D over C (gamble over sure loss). This is the classic "Allais paradox" or "reflection effect" or "prospect theory" risk aversion vs risk seeking. The specific pattern is the "reflection effect" or "loss aversion" or "prospect theory" with reference point. But the question: "Same expected value in both pairs. But the merchants flip from risk-averse to risk-seeking the moment we change the word gain to loss. Under MEU, a consistent utility curve should produce the same risk attitude in both domains. It does not."

This is a known phenomenon: "Allais paradox" shows violation of expected utility theory. But the Allais paradox involves different probabilities. Here the probabilities are same (50/50).

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Reflection Effect' and distinguishes it from the Allais Paradox. They accurately explain the mechanism: risk aversion in gains vs. risk seeking in losses violates the consistent curvature required by Expected Utility Theory (MEU), implying an S-shaped value func

---

### B4.6: Disjunction effect
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** You reject the bet when you know at least one is heads, and you reject when you know at least one is tails. One of these must be true. So why should you accept unconditionally? Where is the flaw in reasoning from conditionals to the unconditional?

**Expected Answer:** **Disjunction Effect** — The Disjunction Effect occurs when an agent rejects an option conditional on each member of a non-exclusive partition but should accept it unconditionally. The resolution: 'at least one H' and 'at least one T' overlap on {HT, TH} — the losing outcomes. Conditioning on either event eliminates one win *The Disjunction Principle ('if you reject in every possible state, reject unconditionally') seems compelling but is false when the conditioning events overlap. It conflates overlapping evidence with a*

**Model Response:**
> We need to analyze scenario. This is classic Monty Hall-like paradox? Actually it's about conditional probability and information. The puzzle: two coins flipped. Payoffs: win 5 if same, lose 4 if different. Unconditional EV = 0.5. So accept. But if you learn at least one coin is heads, then the sample space reduces to {HH, HT, TH}. Among those, only HH gives win, probability 1/3, EV = 5*(1/3) - 4*(2/3) = (5-8)/3 = -1. So reject. Similarly if you learn at least one is tails, same. So you would reject in both cases. But you know that at least one is heads or at least one is tails. So you know one of the two rejectable states holds. Yet you should accept. This is a paradox: the knowledge of a disjunction of two mutually exclusive events leads to a different expectation than each individually.

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the mathematical mechanism: the events 'at least one H' and 'at least one T' are not mutually exclusive and overlap on the mixed outcomes {HT, TH}. They also correctly calculate the negative conditional EVs. However, the response fails to reach Level 3 because it doe

---

### B5.1: Reference points
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Three traders received the same bonus but feel differently. Standard economic theory says Basil should be happiest (highest wealth). What is actually determining their reactions, and what does standard theory miss?

**Expected Answer:** **Reference points** — Under Prospect Theory, outcomes are evaluated as gains or losses relative to a reference point — typically the status quo, an expectation, or an aspiration level. The same objective outcome can feel like a gain or a loss depending on the reference point. Cara's 5,000 gold bonus is objectively a gain *Cara's bonus is a gain in absolute terms. Standard MEU, which evaluates total wealth, would predict satisfaction. But Prospect Theory correctly predicts dissatisfaction because value is computed from *

**Model Response:**
> **1. What is being shown?**  
The traders are judging the bonus not by how much money it gives them in total, but by how it compares to *what they expected* (or to a reference point).  
- Anika’s 5 k bonus is a **large positive deviation** from her expected 0 k bonus → she is over‑joyed.  
- Basil’s 5 k bonus is a **small positive deviation** from his expected 0 k bonus → he is only mildly pleased.  
- Cara’s 5 k bonus is a **negative deviation** from her expected 10 k bonus → she is furious.  

So the reasoning pattern is **reference‑dependent evaluation** (the “reference‑point bias” that underlies *prospect theory*).  

**2. Precise name**  
- **Prospect‑Theory Reference‑Point Effect** (sometimes called the *disappointment effect* or *anchoring bias* when the expectation acts as an ancho

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as reference-dependent evaluation and accurately explains that outcomes are judged relative to expectations (reference points). They correctly categorize each trader's experience, noting Cara's negative deviation despite an objective gain. However, the re

---

### B5.2: Loss aversion
**Track:** decision_theory | **Tier:** drill | **Type:** dual

**Question:** Lira's patrons demand 40-50 gold to accept a bet that could lose them 20. Risk aversion explains some of this, but not all. What additional psychological mechanism is at work, and how does it show up in the shape of the value function?

**Expected Answer:** **Loss aversion** — Loss aversion means that losses are felt more intensely than equivalent gains. Formally, the value function is steeper below the reference point than above it: |v(-x)| > v(x) for x > 0. The empirical coefficient is approximately lambda = 2.25, meaning losing $100 hurts as much as gaining $225 feels  *Standard MEU with risk-neutral preferences predicts acceptance at G=20. Risk aversion alone might push G to 25-30. The demand of 40-50 requires loss aversion — the disproportionate weight given to los*

**Model Response:**
> We need to analyze scenario: Lira offers bet: flip fair coin; if tails, lose 20 gold; if heads, gain X gold. People ask for X 40-50 to accept. Lira says it's loss aversion, lambda ~2.25. The question: what specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? The answer: "Loss aversion" is a bias. But also the participants are using "prospect theory" or "reference point" bias. The pattern: "Loss aversion" is a bias. But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The answer: "Loss aversion" is a bias. But also "the participants are using a form of the 'certainty effect' or 'ambiguity aversion'?" Wait: The scenario: People demand 40-50 gold to accept a bet that is mathematicall

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'loss aversion' and distinguishes it from risk aversion by noting that risk aversion would only require a small premium (22-25), whereas the observed demand (40-50) implies a steeper loss function. They successfully derive the mechanism using the lambda coefficient (

---

### B5.3: Probability weighting
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** The same person buys lottery tickets (seeking risk for small-probability gains) and insurance (avoiding risk for small-probability losses). Under MEU, this seems contradictory. How does probability weighting resolve the contradiction?

**Expected Answer:** **Probability weighting function** — In Prospect Theory, objective probabilities are transformed by a weighting function pi(p) before being used in calculations. Small probabilities are overweighted (pi(0.01) > 0.01), large probabilities are underweighted (pi(0.99) < 0.99), and the endpoints 0 and 1 are treated categorically. The resul *Under MEU with objective probabilities, buying lottery tickets with negative EV and buying insurance against rare events are both irrational. Probability weighting explains both as rational under dist*

**Model Response:**
> **1. What is being shown?**  
The scenario illustrates **probability‑weighting bias** – the systematic distortion of objective probabilities that is captured by the inverse‑S‑shaped weighting function of **Prospect Theory** (or, more generally, by cumulative prospect theory).

**2. Precise name**  
*Inverse‑S‑shaped probability‑weighting function* (sometimes called *probability distortion* or *probability‑weighting bias*).

**3. Mechanism – why it matters**  
- **Overweighting of tiny probabilities**: A 1 % chance is felt as ~5 %.  
- **Underweighting of large probabilities**: A 99 % chance feels as ~95 %.  
- **Qualitative jump at 100 %**: The elimination of all risk is not a 1 % improvement but a categorical change.  

Because people apply this distorted weighting to outcomes, they syste

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the inverse-S shaped probability weighting function, explains the overweighting of small probabilities and underweighting of large ones, and notes the categorical treatment of endpoints (the jump at 100%). However, the response is incomplete (cutting off mid-sentence

---

### B5.4: Fourfold pattern
**Track:** decision_theory | **Tier:** what_if | **Type:** dual

**Question:** Lira says the same person can rationally buy lottery tickets and insurance. Under MEU, this is a contradiction. How do the value function and probability weighting function together produce four distinct risk profiles?

**Expected Answer:** **Fourfold Pattern of risk attitudes** — The Fourfold Pattern emerges from combining: (1) The S-shaped value function (risk-averse for gains, risk-seeking for losses) with (2) The probability weighting function (overweight small p, underweight large p). Low-probability gains: overweighting makes the prize loom large → risk seeking. Low-pro *MEU predicts a single consistent risk attitude. The Fourfold Pattern shows four different attitudes from one person, determined by the domain (gains/losses) and the probability level (low/high).*

**Model Response:**
> We need to analyze scenario: Lira draws a 2x2 grid combining value function and probability weighting function: Gains vs Losses, Low vs High probability. The fourfold pattern: risk seeking in gains at low probability, risk averse in gains at high probability, risk averse in losses at low probability, risk seeking in losses at high probability. This is classic Prospect Theory's fourfold pattern. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The answer: It's the "fourfold pattern" or "Prospect Theory's value and weighting functions leading to risk attitudes." But the question likely expects "Prospect Theory" or "Allais paradox" or "ambiguity aversion"? Wait: The scenario: "Same person can rationally buy both lottery ticke

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'fourfold pattern' and accurately explains the underlying mechanisms (S-shaped value function and probability weighting function) for all four quadrants. They also provide context regarding MEU vs. Prospect Theory. However, the response falls short of Level 4 bec

---

### B5.5: Framing effects
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** The councillors in Group A and Group B made opposite choices about the same programs. What changed between the two presentations, and why does it matter for rational decision-making?

**Expected Answer:** **Framing effects** — Framing effects occur when logically equivalent descriptions of the same situation lead to different decisions because they shift the reference point. A gains frame activates risk aversion (prefer the sure outcome). A losses frame activates risk seeking (prefer the gamble). Since the underlying opti *Rational decisions should depend on outcomes, not descriptions. Programs A and C have identical consequences, as do B and D. The preference reversal shows that the frame — not the substance — is drivi*

**Model Response:**
> **1. What is being demonstrated?**  
The councillors are exhibiting the **framing effect** (a specific instance of **loss‑aversion** as described in **Prospect Theory**).  

**2. Precise name**  
- *Framing effect* (also called *gain‑loss framing*).  
- In decision‑theory terms, it is the *prospect‑theory* pattern of “risk‑averse in the domain of gains, risk‑seeking in the domain of losses.”

**3. Mechanism – why it matters**  
| Aspect | Gain framing (Program A vs B) | Loss framing (Program C vs D) | Cognitive basis |
|--------|------------------------------|------------------------------|-----------------|
| **Decision rule** | Prefer the sure gain (200 saved) | Prefer the gamble that could avoid all losses | People treat the same objective outcomes differently depending on the label. |


**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the framing effect and Prospect Theory. They explicitly explain the mechanism via reference points (gains vs. losses) and the resulting shift in risk attitude (risk-averse in gains, risk-seeking in losses), satisfying Level 3. Furthermore, they address the normative 

---

### B5.6: Mental accounting
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Alec and Brin have the same amount of money and face the same bet, but they make opposite choices. What psychological mechanism explains the difference? Is Brin being rational or irrational?

**Expected Answer:** **Mental accounting** — Mental accounting (Thaler) is the tendency to treat money differently depending on which psychological 'account' it belongs to — savings, winnings, salary, found money, etc. Standard economics says money is fungible: a dollar is a dollar regardless of its source. Mental accounting violates fungibili *Money is fungible — 200 gold has the same purchasing power regardless of its source. Alec's savings and Brin's winnings are economically identical. The different treatment reflects a psychological par*

**Model Response:**
> **1. What is being demonstrated?**  
The patrons are exhibiting **mental accounting**—specifically the *source‑bias* or *house‑money effect*.  Alec treats the 200 gold as “savings” and refuses to risk it, whereas Brin treats the same amount as “house money” (a windfall) and is willing to gamble it away.  The two are making different choices even though the objective payoff structure is identical.

**2. Precise name**  
*Mental accounting (source bias / house‑money effect)*.

**3. Mechanism – why it is good or bad**  

| Mechanism | What it does | Why it can be irrational |
|-----------|--------------|--------------------------|
| **Segregation of funds** | People mentally partition money into “accounts” (savings, windfall, debt, etc.). | The accounts are treated as non‑fungible; risk prefe

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'mental accounting' and the 'house money effect,' explicitly explains the violation of fungibility (money being treated as non-fungible based on source), and contrasts the behavior against expected-utility theory. However, the response does not reach Level 4 because 

---

### B5.7: Endowment effect
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Sellers demand 7 gold and buyers offer 3 gold for the same mug. The mugs were randomly assigned. What psychological mechanism creates this gap, and why does standard economic theory have trouble explaining it?

**Expected Answer:** **Endowment effect** — The endowment effect is the observation that people demand more to give up an object they own than they would pay to acquire the same object. Sellers set a higher price (WTA: willingness to accept) than buyers (WTP: willingness to pay), even for identical items. The mechanism is loss aversion: once  *Rational markets require a single market-clearing price. The endowment effect creates a gap between WTA and WTP that prevents efficient trade. The mug has one objective value, but ownership distorts p*

**Model Response:**
> **1. What is being shown?**  
The pattern is the **endowment effect** (a special case of loss‑aversion).  
Owners of an item systematically over‑value it relative to non‑owners, so that the
average “minimum acceptable price” of owners exceeds the average “maximum willing
to pay” of buyers.

**2. Precise name**  
*Endowment effect* (sometimes called *ownership bias* or *status‑quo bias* when
applied to valuation).

**3. How it works – why it looks “good” or “bad”**  

| Side | Reasoning | Bias in action | Consequence |
|------|-----------|----------------|-------------|
| **Sellers** | “I have the mug, so it’s worth more to me.” | Loss‑aversion: giving up the mug feels like a loss, so the minimum price is inflated. | Sellers quote higher prices than the market would support. |
| **Buyers** 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the endowment effect and explains the mechanism via loss aversion (giving up is a loss, acquiring is a gain). They also note the resulting market inefficiency. However, they do not include the specific lambda coefficient (≈ 2.25) or explicitly discuss the WTA/WTP rat

---

### B5.8: Sunk cost fallacy (DT)
**Track:** decision_theory | **Tier:** drill | **Type:** bad_thinking

**Question:** Darya insists on going skiing because she paid 300 gold. Her friend says the money is gone either way. Who is right, and what error is Darya making?

**Expected Answer:** **Sunk cost fallacy** — The sunk cost fallacy is the tendency to continue an activity because of past investment (time, money, effort) rather than future expected value. Under MEU, sunk costs are decision-irrelevant: only future costs and benefits should affect current choices. The fallacy arises from mental accounting — t *The 300 gold is gone regardless of the choice. Rational decision-making considers only future costs and benefits. Going skiing while sick produces less utility than the free cabin. Darya is letting a *

**Model Response:**
> **1. What is being demonstrated?**  
The conversation is a textbook illustration of the **sunk‑cost fallacy** (also called the “sunk‑cost effect” or “concorde fallacy”).

**2. Precise name**  
*Sunk‑cost fallacy* – the tendency to let an irrecoverable past expenditure influence a rational decision about the future.

**3. Mechanism – why it is good or bad**  

| What happens | Why it is a bias | Why it leads to sub‑optimal choices |
|--------------|-----------------|-------------------------------------|
| Darya insists “I can’t throw away the 300 g.” | She treats the already‑spent money as a *cost that must be “recovered”* by continuing the trip. | The 300 g is already gone; it cannot be recovered. Continuing the trip only adds the *marginal* cost of her sickness and lost enjoyment. By foc

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the sunk cost fallacy and explains the normative principle that only future marginal costs and benefits matter. They explicitly note that the 300g is irrecoverable in both scenarios. Furthermore, they successfully address edge cases where past investment might legiti

---

### B6.1: Prisoner's Dilemma
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Mirella knows holding back would be better for both, yet she strips the grove anyway. What structural feature of her situation makes cooperation so difficult?

**Expected Answer:** **Prisoner's Dilemma** — A symmetric 2-player game where individual rationality (dominant strategy D) leads both players to an outcome strictly worse than mutual cooperation. The unique Nash equilibrium is (D,D), yet (C,C) Pareto-dominates it. *Defecting is individually rational — higher payoff regardless of the other's choice. But when both follow this logic, they lock into (1,1), forgoing the mutually superior (3,3).*

**Model Response:**
> **1. What is being demonstrated?**  
The speakers are falling into the classic *Prisoner’s Dilemma* reasoning pattern: each assumes the other will defect, so the only “safe” choice is to defect. This is a *dominant‑strategy* argument that leads to a sub‑optimal Nash equilibrium.

**2. Precise name**  
- **Prisoner’s Dilemma (PD) / Dominant‑strategy defect**  
- In behavioral‑economics terms it is often called the *“defection bias”* or *“fear of being exploited”* bias.

**3. Mechanism – why it looks good and why it is wrong**  

| What the reasoning does | Why it seems reasonable | Why it fails |
|------------------------|------------------------|--------------|
| “If I cooperate, Orik might defect → I lose.” | It protects you from a one‑shot loss; you avoid being the only one to pay the co

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Prisoner's Dilemma pattern and provides a comprehensive analysis. They explicitly explain dominant strategies, the sub-optimal Nash equilibrium at (D,D), and the Pareto-superiority of mutual cooperation (C,C). Furthermore, they exceed the baseline requirements by

---

### B6.2: Nash equilibrium
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor asks you to find the Nash Equilibrium. For each strategy pair, check: could either cadet do better by switching alone? Which pair survives this test?

**Expected Answer:** **Nash equilibrium** — A Nash Equilibrium is a strategy profile where no player can improve their payoff by unilaterally changing their strategy. In the PD above, (Fortify, Fortify) is the unique Nash Equilibrium: if A plays Fortify and B plays Fortify, A gets 1. If A switches to Patrol, A gets 0 (worse). Symmetrically fo *Nash Equilibrium captures the key insight of strategic stability: no player can do better by changing strategy alone. In the PD, Fortify dominates Patrol — regardless of what the opponent does, Fortif*

**Model Response:**
> We need to analyze scenario: instructor says it's a Prisoner's Dilemma, find Nash equilibrium. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: The instructor says it's a Prisoner's Dilemma, find Nash equilibrium. The cadets are playing a simultaneous-move game. The instructor says "This is a Prisoner's Dilemma." The question likely refers to the instructor's assumption that the game is a Prisoner's Dilemma and that the Nash equilibrium is the dominant strategy equilibrium (Patrol, Patrol). But the instructor's statement might be a "false dilemma" or "overgeneralization" or "mislabeling" or "misidentifying the game as a Prisoner's Dilemma" because the payoff matrix is not symmetric? Actually, it is symmetric:

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies (Fortify, Fortify) as the unique Nash Equilibrium and performs the deviation analysis accurately for that cell, which exceeds Level 1. However, the response is marred by significant confusion regarding the prompt's context, leading to a rambling discussion about the 

---

### B6.3: Iterated PD and cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In a one-shot PD, defection dominates. What changes when the game is repeated? Why did Tit-for-Tat win Axelrod's tournament? And what is TFT's biggest weakness?

**Expected Answer:** **Iterated PD and cooperation** — In a finitely repeated PD with known endpoint, backward induction predicts defection every round. But in an infinitely repeated PD (or one with unknown endpoint), the Folk Theorem shows that cooperation can be sustained as a Nash Equilibrium if players value future payoffs enough (discount factor de *Iteration changes everything. The shadow of the future creates incentives for cooperation: defecting today earns a short-term gain but triggers retaliation that reduces future payoffs. If the future i*

**Model Response:**
> We need to analyze scenario: instructor says TFT wins because nice, retaliatory, forgiving, clear. Then asks: "But TFT is not invincible. What happens when TFT plays against a strategy that defects on round 1 by mistake?" The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The instructor is presenting a claim that TFT wins because of four properties. This is a form of "argument from authority" or "appeal to simplicity" or "simplification bias"? But the question: "What happens when TFT plays against a strategy that defects on round 1 by mistake?" The instructor is pointing out that TFT is not invincible. The reasoning pattern: "TFT is best because it has nice, retaliatory, forgiving, clear." This is a "four properties" argumen

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to address the prompt's core subject: the conditions for cooperation in repeated Prisoner's Dilemma (shadow of the future, discount factors, Folk Theorem). Instead of explaining the game-theoretic mechanism, the student misinterpreted the task as identifying a logical f

---

### B7.1: Stag Hunt
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find both Nash Equilibria in the Stag Hunt. Which is payoff-dominant? Which is risk-dominant? Which would you choose, and what does your choice depend on?

**Expected Answer:** **Stag Hunt** — The Stag Hunt (from Rousseau) has two pure-strategy Nash Equilibria: (Stag, Stag) = (5,5) and (Hare, Hare) = (2,2). (Stag, Stag) is payoff-dominant (better for everyone). (Hare, Hare) is risk-dominant (safer — you get 2 guaranteed regardless of partner). The core tension: cooperation requires trust. *Unlike the PD, neither strategy dominates. The optimal choice depends entirely on expectations about your partner. This is a coordination problem, not a cooperation problem.*

**Model Response:**
> We need to analyze scenario: classic stag hunt game. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: The hunt master says there are two equilibria: Stag-Stag better, Hare-Hare safer. Which do you trust your partner to choose? The question likely refers to "coordination game" and "risk dominance vs payoff dominance" concept. The reasoning pattern: "risk dominance" or "dominant strategy" or "dominance principle"? The hunter's reasoning: They might choose Hare-Hare because it's safer (dominant strategy?) Actually, Hare is a dominant strategy? Let's check: If partner chooses Stag, you get 0 if you choose Stag, 3 if Hare. If partner chooses Hare, you get 5 if Stag, 2 if Hare. So Stag is not dominant. Hare is not 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the game as a Stag Hunt, finds both pure-strategy Nash Equilibria, and accurately explains the distinction between payoff dominance (Stag-Stag) and risk dominance (Hare-Hare). They also discuss factors like communication and reputation that influence equilibrium sele

---

### B7.2: Battle of the Sexes
**Track:** game_theory | **Tier:** drill | **Type:** dual

**Question:** Find all Nash Equilibria in this game, including any mixed-strategy equilibrium. Why is the mixed equilibrium worse for both players than either pure equilibrium?

**Expected Answer:** **Battle of the Sexes** — Battle of the Sexes has two pure-strategy Nash Equilibria: (Opera, Opera) = (3,2) and (Tournament, Tournament) = (2,3). Both are coordination equilibria — both players prefer being together over being apart. But they disagree on which is better: Helena prefers (Opera, Opera), Roderick prefers (Tourn *Neither player has a dominant strategy. The choice depends on expectations about the other — creating a coordination problem with a distributional conflict.*

**Model Response:**
> We need to analyze scenario: two players with payoff matrix. They prefer to coordinate but have different preferences. They both prefer attending together over going alone. Payoffs: if both choose Opera: Helena gets 3, Roderick 2. If both choose Tournament: Helena 2, Roderick 3. If they don't coordinate: both get 0. So it's a coordination game with two Pareto-optimal outcomes. The scenario: "Helena: 'We must coordinate. But I prefer Opera and he prefers the Tournament. If we cannot agree, we both go alone and get nothing.'" This is basically the "coordination problem" or "matching pennies"? Actually it's a coordination game with two equilibria. The reasoning pattern: "Helena says we must coordinate, but I prefer Opera and he prefers Tournament." She might be using "selfishness" or "prefere

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the game structure as a coordination game with two pure-strategy Nash Equilibria ((Opera, Opera) and (Tournament, Tournament)) and correctly deduces that there are no dominant strategies. However, the response fails to compute or explain the mixed-strategy equilibriu

---

### B7.3: Focal points
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** You and your contact must meet without communication. Why do people converge on the same location and time? What property makes some answers more likely than others, and is this a rational process?

**Expected Answer:** **Focal points (Schelling points)** — A focal point is a solution to a coordination game that attracts players' attention because it is salient — prominent, unique, culturally significant, or symmetric. Focal points work because of mutual expectations: I go to the fountain because I expect you to expect me to expect... etc. Sources of s *Focal points solve the equilibrium selection problem in coordination games. When there are many Nash Equilibria and no communication, salience determines which equilibrium is played. The insight is th*

**Model Response:**
> We need to analyze scenario: player must meet contact, cannot communicate, choose time/place. Most people choose Grand Fountain at noon. Scholar says it's due to salience, mutual expectation. This is a classic example of "Schelling point" or "focal point" in coordination games. The reasoning pattern: using a salient, obvious solution to coordinate without communication. The fallacy or bias? It's not a fallacy; it's actually a rational strategy in coordination problems. But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" It's the "Schelling point" concept. It is not a fallacy; it's a concept in game theory. But the question might ask to identify the bias: "availability heuristic" or "anchoring" or "salience bias"? The scen

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the concept as a 'Schelling point' or 'focal point' and accurately explains the mechanism of salience and mutual expectation (assuming the other will choose the obvious option). They also discuss edge cases where the strategy might fail. However, the response falls s

---

### B7.4: Convention (Lewis)
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The philosopher says driving on the right is a convention. What does that mean technically? Apply Lewis's five conditions to driving on the right and explain why the alternative (driving on the left) is equally valid.

**Expected Answer:** **Convention (Lewis)** — A convention is a regularity R in behavior that is (1) followed by everyone, (2) expected by everyone, (3) preferred by everyone given others' conformity, (4) has at least one alternative R' that could have served instead, and (5) is common knowledge. Conventions are solutions to recurrent coordinat *Lewis's theory explains how arbitrary social practices persist and why they are rational to follow: given that everyone else conforms, conforming is your best response. This applies to language, money*

**Model Response:**
> We need to analyze scenario: philosopher explains that driving side is convention; lists Lewis's conditions; says switching is nearly impossible because everyone would need to switch together. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The philosopher is describing a coordination problem and the self-reinforcing nature of conventions. The reasoning pattern might be "self-fulfilling prophecy" or "social convention" or "common knowledge" or "coordination game" or "Schelling point" or "equilibrium" or "circular reasoning" or "argument from tradition" or "appeal to convention" or "argumentum ad populum". But the philosopher is not making a fallacious argument; they are describing a fact. But the question likely expects "

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the scenario describes a coordination problem and explicitly lists all five of Lewis's conditions for a convention, showing strong content knowledge. However, the response fails to definitively identify the specific reasoning pattern or concept as requested, ins

---

### B8.1: Game trees
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** The instructor has drawn the Entry Game tree. Identify the decision nodes, the branches, and the terminal payoffs. What information does each player have when they move?

**Expected Answer:** **Game trees (extensive form)** — A game tree represents a sequential game with nodes (decision points), branches (available actions), terminal nodes (outcomes with payoffs), and information sets (what each player knows when they move). Unlike the normal form (matrix), the extensive form explicitly represents the order of moves, whi *The extensive form reveals strategic structure that the normal form hides. In this game, the Incumbent's threat to Fight is visible but not credible — if the Entrant enters, the Incumbent prefers Acco*

**Model Response:**
> We need to analyze scenario: instructor draws game tree: Entrant moves first: Enter or Stay Out. If Stay Out: (1,3). If Enter: Incumbent moves: Accommodate or Fight. If Accommodate: (2,2). If Fight: (0,0). They explain it's extensive form, shows sequence of moves and who knows what when. The Entrant moves first; Incumbent sees the Entrant's choice before responding.

The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: The instructor is explaining extensive form vs matrix. The reasoning pattern might be "sequential rationality" or "backward induction" or "dynamic consistency." But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario seem

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the structure of the game tree, the players, the sequence of moves, and the information set (Incumbent sees Entrant's move). This satisfies Level 2. However, the response fails to reach Level 3 or 4 because it does not trace the paths to determine the outcome via bac

---

### B8.2: Backward induction
**Track:** game_theory | **Tier:** drill | **Type:** good_tool

**Question:** Apply backward induction to the Entry Game. Start at the last decision node and work backward. What is the subgame perfect equilibrium? Why is the Incumbent's threat to Fight not credible?

**Expected Answer:** **Backward induction** — Backward induction solves extensive-form games by starting at the terminal nodes and working backward. At each decision node, the player is assumed to choose their optimal action. The resulting strategy profile is a subgame perfect equilibrium (SPE). In the Entry Game: (1) At Incumbent's node: Accom *Backward induction eliminates non-credible threats. (Stay Out, Fight) is a Nash Equilibrium but relies on the Incumbent's non-credible threat to Fight. Backward induction reveals that the Incumbent wo*

**Model Response:**
> **1. What is being demonstrated?**  
The instructor is illustrating the *non‑credible‑threat* concept that is eliminated by *backward induction* (the standard method for finding a subgame‑perfect equilibrium in finite extensive‑form games).

**2. Precise name**  
*Non‑credible threat* (or *non‑credible threat elimination* via *backward induction*).

**3. Mechanism – why the reasoning is good (or bad)**  

| Aspect | What the instructor does | Why it works (or fails) |
|--------|--------------------------|------------------------|
| **Backward induction** | Starts at the last decision node (Incumbent’s choice after entry) and works backwards. | This guarantees *dynamic consistency*: the incumbent’s choice is optimal given that the entrant will observe it. It rules out any strategy that woul

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern (backward induction) and the mechanism (starting at the Incumbent's node, comparing payoffs 2>0 to rule out 'Fight', and implying the Entrant's optimal response). The response explains dynamic consistency and non-credible threats well. However, it does no

---

### B8.3: Subgame perfect equilibrium
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The Entry Game has two Nash Equilibria. The instructor says one of them relies on a non-credible threat. Which one, and why does SPE eliminate it?

**Expected Answer:** **Subgame perfect equilibrium** — SPE (Selten 1965) requires that a strategy profile be a Nash Equilibrium in every subgame. A subgame is any part of the game tree that forms a complete game on its own. SPE eliminates NE that rely on non-credible threats — strategies that would not be followed through if the relevant decision node w *SPE is a refinement of NE that captures credibility. A threat is credible only if the threatener would actually carry it out. SPE formalizes this by requiring optimality at every node, not just on the*

**Model Response:**
> **1. What is being demonstrated?**  
The instructor is pointing out a *non‑credible (empty) threat* – a threat that a player says it will carry out but would not actually carry out if the situation ever reached that point.

**2. Precise name**  
*Non‑credible threat* (also called an

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the concept of a 'non-credible threat' in plain language, which prevents a score of 0. However, the response is incomplete (cutting off mid-sentence), fails to name the formal pattern (Subgame Perfect Equilibrium), does not analyze the specific game nodes or strategi

---

### B8.4: Centipede Game
**Track:** game_theory | **Tier:** puzzle | **Type:** dual

**Question:** Apply backward induction to the Centipede Game. What does it predict? Do you find the prediction convincing? What assumption is doing the heavy lifting, and what happens if you relax it?

**Expected Answer:** **Centipede Game** — The Centipede Game is a sequential game where two players alternate between stopping (taking a smaller immediate payoff) and continuing (allowing the total payoff to grow). Backward induction predicts immediate stopping — the unique SPE. But this is paradoxical: both players would be much better off *Backward induction is logically valid given CKR, but the outcome (1,1) seems absurd when (4,4) is available through mutual cooperation. The paradox reveals that CKR may be too strong an assumption — o*

**Model Response:**
> **1. What is being demonstrated?**  
The players are using **backward induction** in a finite, perfect‑information game.  The resulting sub

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student's response is incomplete and cuts off mid-sentence. While they correctly identify 'backward induction' as the mechanism, they fail to apply it to the specific game tree, do not state the predicted outcome (stopping at Node 1), do not identify the paradoxical nature of the result, and do 

---

### B9.1: ESS
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** Check whether pure Hawk and pure Dove are ESS in the Hawk-Dove game with V=4, C=6. If neither is, find the mixed ESS and explain what it means for the population.

**Expected Answer:** **Evolutionarily Stable Strategy (ESS)** — An ESS (Maynard Smith) is a strategy that, when adopted by almost all members of a population, cannot be invaded by any rare mutant strategy. Formally: S is ESS if for any mutant M, either (1) E(S,S) > E(M,S), or (2) E(S,S) = E(M,S) and E(S,M) > E(M,M). In Hawk-Dove with V<C, neither pure strategy i *ESS provides a concept of equilibrium that does not require rationality — only differential reproduction. Strategies that do better than average spread; those that do worse shrink. The mixed ESS emerg*

**Model Response:**
> We need to analyze the scenario: The player visits a biologist modeling animal conflict using Hawk-Dove dynamics. The biologist draws the matrix and then says pure Hawk is not ESS because E(Hawk,Hawk)=-1 but E(Dove,Hawk)=0. Similarly for pure Dove. Then says ESS is mix p=V/C=4/6=2/3 Hawks.

We need to identify the reasoning pattern, fallacy, bias, or decision-theoretic concept being demonstrated. The scenario is about evaluating ESS. The reasoning: They check if pure Hawk is ESS by comparing payoff of Hawk vs Hawk and Dove vs Hawk. They say pure Hawk is not ESS because Dove does better against Hawks. But the correct condition for ESS: A strategy x is ESS if either (i) E(x,x) > E(y,x) for all y ≠ x, or (ii) if E(x,x) = E(y,x), then E(x,y) > E(y,y). For Hawk, E(Hawk,Hawk) = -1, E(Dove,Hawk) 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly verifies that neither pure Hawk nor pure Dove is an ESS by comparing payoffs against the resident strategy, satisfying the Level 2 criterion. They also correctly calculate the mixed ESS proportion (p=2/3). However, the response fails to reach Level 3 or 4 because the student ex

---

### B9.2: Replicator dynamics
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** The biologist perturbs the Hawk population from 50% to 51%. Show that the system returns to 50% by calculating fitness for each strategy. What does this tell you about the stability of the mixed ESS?

**Expected Answer:** **Replicator dynamics** — The replicator dynamics models how strategy frequencies change over time based on fitness. The equation dx_i/dt = x_i(f_i - F) says: strategies that outperform average grow; those that underperform shrink. Key properties: (1) ESS are stable fixed points of replicator dynamics. (2) Not all fixed poin *The replicator dynamics provides the 'how' behind ESS — the mechanism by which populations reach (or fail to reach) equilibrium. It requires no rationality, only differential reproduction or imitation*

**Model Response:**
> We need to analyze the scenario: The biologist uses replicator dynamics to show that the mixed ESS is stable. She perturbs from 50% to 51% Hawks, calculates expected payoffs, shows Dove does better, so system returns to 50%. This is a demonstration of stability under replicator dynamics. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario might be demonstrating a "self-fulfilling prophecy" or "self-correcting" but maybe it's a "confirmation bias" or "post hoc ergo propter hoc"? But the biologist is demonstrating that the system returns to equilibrium. The question likely refers to the "self-fulfilling prophecy" or "self-correcting" but maybe it's "recursion fallacy" or "circular reasoning"? Let's think.

The scen

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly computes the fitness values for both Hawk and Dove strategies at the perturbed state (51% Hawks) and observes that Dove outperforms Hawk. They also correctly note that this implies the system returns to equilibrium, demonstrating an understanding of the stability mechanism. How

---

### B9.3: Evolution of cooperation
**Track:** game_theory | **Tier:** what_if | **Type:** good_tool

**Question:** In the evolutionary Stag Hunt, what determines whether cooperation or defection wins? Why does Skyrms call the cooperative equilibrium a 'social contract'? What factors help cooperation evolve?

**Expected Answer:** **Evolution of cooperation** — In evolutionary Stag Hunt, cooperation (Stag) can evolve if enough of the population already cooperates. The threshold is p=0.5 in standard payoffs. Above the threshold, cooperation is self-reinforcing; below, it collapses. This is the basin of attraction concept. Factors that help cooperation evolv *The evolution of cooperation shows that cooperative outcomes can emerge without rational deliberation — through selection, iteration, and correlation. This provides a different foundation for social o*

**Model Response:**
> We need to analyze scenario: biologist presents evolutionary Stag Hunt, shows threshold p=0.5. They say if more than half hunts Stag, cooperation spreads; if fewer, collapses. Outcome depends on initial conditions. This is path dependence. They call it social contract. The question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" They want to identify a reasoning pattern. The scenario: The biologist is presenting a deterministic threshold based on equilibrium analysis. The reasoning might be "equilibrium fallacy" or "myopic reasoning" or "static reasoning" ignoring dynamics. But the scenario: The biologist says "If more than half hunts Stag, Stag-hunters do better — cooperation spreads." This is basically a deterministic threshold. But

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the threshold (p=0.5) and the concept of path dependence/basins of attraction. However, the response fails to discuss the specific factors that promote cooperation (iteration, assortment, reputation) or connect the analysis to Skyrms's argument about the social contr

---

### C1.1: Opportunity cost
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Torva says her profit from the sword is eighty gold. Is she right? What is she forgetting to account for?

**Expected Answer:** **Opportunity cost** — The opportunity cost of an action is the value of the next-best alternative forgone. Torva treats the sword's revenue (80 gold) as pure profit, but by choosing the sword she forgoes the 50-gold axle repair. Her net gain from choosing the sword over the axle is 80 - 50 = 30 gold, not 80 gold. The 50  *Every choice has a hidden cost: what you gave up to make it. Torva's sword commission is genuinely better than the axle repair, but by 30 gold, not by 80. Understanding this prevents her from overvalu*

**Model Response:**
> **1. What is being demonstrated?**  
Torva is using a *single‑factor, profit‑only* decision rule: “the job that pays more is the better one.” She ignores every other dimension of the choice (time, effort, opportunity cost, risk, future benefits, etc.).  

**2. Precise name**  
- **Profit‑only bias** (sometimes called the *monetary bias* or *price‑only heuristic*).  
- In decision‑theoretic terms, it is a *myopic, cost‑free profit maximization* rule that treats revenue as if it were net profit.

**3. Mechanism – why it is good or bad**  
- **Good (under very narrow conditions):**  
  * If the only relevant variable is the amount of money received and all other costs are truly zero or identical, then picking the higher price is optimal.  
  * It is a fast, cognitively cheap rule that works w

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core concept of opportunity cost and explicitly calculates the net gain (30 gold) in the 'Correct approach' section by comparing the sword's revenue against the forgone axle value. They also explain the mechanism well by distinguishing revenue from profit. Howeve

---

### C1.2: Comparative advantage
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Hilde outproduces Oskar in both wheat and flax. She says trade cannot benefit her. Is she right? Calculate the opportunity costs and determine who should specialize in what.

**Expected Answer:** **Comparative advantage** — Hilde has absolute advantage in both goods, but comparative advantage depends on opportunity cost. Hilde's opportunity cost of 1 bolt of flax = 2 bushels of wheat (12/6). Oskar's opportunity cost of 1 bolt of flax = 4/3 bushels of wheat. Oskar has a lower opportunity cost for flax, so he has compara *Trade benefits do not require being equally productive. Even though Hilde is better at both crops, she benefits from specializing in the crop where her relative advantage is greatest (wheat) and tradi*

**Model Response:**
> We need to analyze the scenario: Hilde says she outproduces Oskar in both wheat and flax. She thinks trade wouldn't benefit her. This is a classic example of the "selfishness" or "zero-sum" thinking, but more specifically, it's the "selfishness bias" or "selfishness fallacy" or "selfishness bias" or "selfishness bias" in game theory. But the scenario: Hilde is refusing to trade because she thinks she outproduces Oskar in both crops. She thinks trade would only help him. This is the "selfishness bias" or "selfishness fallacy" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "selfishness bias" or "s

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student fails to identify the correct pattern (comparative advantage) or perform any relevant calculations. Instead, the response consists of repetitive, nonsensical text focusing on an incorrect concept ('selfishness bias') and cuts off mid-sentence without providing a valid economic explanatio

---

### C2.1: Constrained optimization
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Seren needs at least 15 units of food and 8 units of light within a 100-gold budget. Rations give 3 food for 5 gold; torches give 4 light for 10 gold. What is the cheapest combination that meets both requirements?

**Expected Answer:** **Constrained optimization** — The problem is to minimize cost subject to constraints. Food constraint: 3R >= 15, so R >= 5 (minimum 5 ration packs). Torch constraint: 4T >= 8, so T >= 2 (minimum 2 torch bundles). Cost: 5R + 10T. Minimum cost = 5(5) + 10(2) = 25 + 20 = 45 gold. This satisfies both constraints and is within budget *Constrained optimization is the core microeconomic framework: maximize (or minimize) an objective function subject to binding constraints. Seren cannot simply buy everything — she must find the combin*

**Model Response:**
> We need to analyze scenario: player helping quartermaster Seren with budget 100 gold, must buy rations and torches. Rations cost 5 gold each, provide 3 sustenance. Torches cost 10 gold each, provide 4 visibility. Need at least 15 sustenance, 8 visibility. Seren wants to spend as little as possible while meeting both requirements. This is a linear programming optimization problem: minimize cost subject to constraints. The reasoning pattern: Seren is trying to minimize cost given constraints. But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The scenario: Seren wants to spend as little as possible while meeting both requirements. This is basically an optimization problem. But maybe the pattern is "satisficing" or "bounded

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as constrained optimization (cost minimization) and accurately solves the mathematical problem (R=5, T=2, Cost=45), verifying that constraints are met. However, the response fails to reach Level 4 because it does not explicitly calculate or disc

---

### C2.2: Marginal analysis
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Each potion sells for 15 gold. The cost of each additional potion rises: 5, 8, 12, 16, 22. How many potions should Elara brew, and why?

**Expected Answer:** **Marginal analysis** — Marginal analysis compares the marginal benefit (MB) to the marginal cost (MC) of each additional unit. Brew if MB > MC; stop when MC >= MB. Revenue per potion (MB) = 15 gold. MC of potions: 1st=5, 2nd=8, 3rd=12, 4th=16, 5th=22. For potions 1-3, MB(15) > MC. For potion 4, MC(16) > MB(15). Elara shou *Marginal analysis prevents two errors: stopping too early (missing profitable units) and going too far (adding units that cost more than they earn). The fourth potion costs 16 gold but only earns 15 —*

**Model Response:**
> We need to analyze scenario: Elara sells healing potions at 15 gold each. Costs: 5, 8, 12, 16, 22. She wonders how many to brew. The scenario likely demonstrates the "Sunk Cost Fallacy" or "Incremental cost vs marginal revenue" or "Marginal analysis" or "Diminishing returns" maybe. But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" She might be considering cumulative cost vs revenue, maybe using total cost vs total revenue, but the correct approach is marginal analysis: compare marginal cost of each additional potion to marginal revenue (price). She should brew until marginal cost <= price. So the pattern is "total cost vs total revenue comparison" or "non-marginal thinking" or "cost-benefit analysis ignoring marginal co

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'Marginal analysis' as the core concept and accurately calculates that Elara should brew 3 potions by comparing the marginal cost of each unit to the price (15 gold). They explicitly note that the 4th potion (MC=16) exceeds the revenue. However, the response lacks th

---

### C3.1: Public goods and free riding
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Captain Hale says she should let the others pay for the lighthouse oil. Her reasoning seems logical from her own perspective. What happens if every captain follows the same logic? Why does this situation arise?

**Expected Answer:** **Public goods and free riding** — The lighthouse is a public good: non-rival (one captain using the light does not diminish it for others) and non-excludable (you cannot prevent a non-paying captain from seeing the light). These properties create a free-rider incentive: each captain benefits from the lighthouse regardless of whether *Free riding is individually rational but collectively destructive. Hale's logic is valid for any single captain, but if universalized, it leads to a lighthouse going dark and all captains risking thei*

**Model Response:**
> **1. What is being demonstrated?**  
The captains are caught in a *free‑rider problem* – a classic public‑goods dilemma in which each individual can enjoy the benefit of a non‑excludable good (the lighthouse) without bearing its cost.

**2. Precise name**  
*Free‑rider problem* (also called the *public‑goods dilemma* or *collective‑action problem*).

**3. Mechanism – why the reasoning is “good” for the individual but “bad” for the group**  

| Individual rationality | Group outcome |
|------------------------|---------------|
| **Benefit**: every captain gets the same safety benefit from the light. | The light is a non‑excludable public good – it is available to all regardless of who pays. |
| **Cost**: 20 gold per month if the captain pays. | The cost is borne by the payer alone; the bene

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the free-rider problem, explicitly defines the lighthouse as non-excludable (and implies non-rivalry by noting shared benefits), and explains the conflict between individual rationality and collective failure. The response also proposes a solution mechanism (binding 

---

### C3.2: Commons problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Elder Yara says every family is acting sensibly, yet the lake is dying. How can individual rationality produce collective disaster? What is the structural problem?

**Expected Answer:** **Commons problems (Tragedy of the commons)** — Lake Mirren is a common-pool resource: rival (each fish caught is unavailable to others) but non-excludable (no family can be prevented from fishing). Each family captures the full benefit of each additional fish they catch but bears only a fraction of the cost (resource depletion shared across all  *The structural incentive to overextract is real and rational for each individual. The problem is not stupidity or greed but a misalignment between individual and collective incentives.*

**Model Response:**
> **1. What is being demonstrated?**  
The families are acting on *rational self‑interest in a common‑pool resource* while ignoring the negative externality that their collective action imposes on the lake. Each family believes that if it does not increase its catch, another family will, so it must “get its share before the lake runs out.” This is the classic **Tragedy of

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as the 'Tragedy of the Commons' involving a common-pool resource and rational self-interest. They accurately explain the mechanism: the fear that others will extract the resource if one does not ('if it does not increase its catch, another family will'), 

---

### C4.1: Bargaining and fairness
**Track:** microeconomics | **Tier:** what_if | **Type:** good_tool

**Question:** Sera and Brenn create 80 gold in surplus from trade. Sera's outside option gives her 15 gold surplus; Brenn's gives him 10. How should they split the 80 gold surplus, and why?

**Expected Answer:** **Bargaining and fairness (Nash bargaining)** — The surplus from trade is 80 gold. Each merchant's outside option (BATNA) sets a floor: Sera will not accept less than 15 gold surplus (her alternative deal), and Brenn will not accept less than 10. The remaining surplus after securing both outside options is 80 - 15 - 10 = 55 gold. Nash bargaining  *Bargaining theory shows that fair division depends not just on the total surplus but on each party's outside option. Better alternatives give you more bargaining power. This framework prevents the nai*

**Model Response:**
> We need to analyze scenario: two merchants negotiating split of surplus. Each has outside options: Sera can get 15 gold surplus elsewhere, Brenn can get 10 gold surplus elsewhere. They each demand at least 50 gold from trade. They both have outside options less than 50, so they might be demanding too much. The scenario likely demonstrates the "anchoring" or "reference point" bias, or the "zero-sum" fallacy? They think of their outside options as reference points. They think they should get at least what they'd get from walking away. That is the "reservation price" concept. But they are demanding 50 each, which is more than their outside options. They are ignoring the fact that the total surplus is 80, so they can't both get 50. This is the "zero-sum" fallacy? Actually they think they can e

**Score:** 1/4 █░░░
**Judge Reasoning:** The student recognizes that outside options matter and act as floors (Level 1 criteria). However, the response fails to calculate the correct split, instead deriving an incorrect Nash solution (35/45) by maximizing the product of absolute shares rather than gains over the disagreement point. The stu

---

### C4.2: Principal-agent problems
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Lady Ashworth paid Corbin a flat wage and got a poor harvest. She suspects shirking but cannot prove it. What is the structural problem with her contract, and how might she redesign it?

**Expected Answer:** **Principal-agent problems and moral hazard** — The principal (Ashworth) delegates a task to an agent (Corbin) whose effort she cannot observe. Under a flat wage, the agent bears the cost of effort but captures none of the benefit (the extra apples go to the principal). This misalignment of incentives is moral hazard: the agent has both the oppor *Corbin is not necessarily lazy or dishonest — the contract structure gives him no reason to exert effort. The problem is the incentive design, not the person.*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The lady is applying the *moral‑hazard* logic that under a fixed‑wage contract the agent has no incentive to exert effort, because the agent’s payoff does not depend on the outcome.

**2. Precise name**  
**Moral hazard (principal‑agent problem with a fixed‑price contract).**

**3. Mechanism – why the reasoning is useful and where it can mislead**  

| What the reasoning says | Why it can be correct | Why it can be wrong |
|------------------------|-----------------------|---------------------|
| “If the harvest is big, I get the extra apples and Corbin still gets 50 g.” | The agent’s marginal benefit of an extra unit of effort is zero; rationally he can reduce effort without affecting his payoff. | The agent’s effort may be *necessary* to avoid 

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as moral hazard within a principal-agent framework and accurately explains the mechanism (fixed wage leads to zero marginal benefit for effort). They also propose valid solutions like monitoring and performance pay. However, the response falls short of Le

---

### C5.1: Supply, demand, equilibrium
**Track:** microeconomics | **Tier:** drill | **Type:** good_tool

**Question:** Using the market board data, find the price at which quantity supplied equals quantity demanded. What happens at prices above or below this equilibrium?

**Expected Answer:** **Supply, demand, and market equilibrium** — At equilibrium, quantity supplied equals quantity demanded. From the table: at price = 2, excess demand (shortage) of 60. At price = 8, excess supply (surplus) of 60. At price = 6, Qs = 60 = Qd = 40 — not yet equal. Interpolating (or reading the table), equilibrium is at price = 5, where both Qs and *The equilibrium price coordinates decentralized buyers and sellers without anyone needing to manage the outcome. Prices above equilibrium create surpluses (pushing price down); prices below equilibriu*

**Model Response:**
> We need to analyze scenario: market master posts supply/demand table. He says last week price 2 gold, sold out quickly, angry buyers, fights. Week before price 8, half farmers unsold. He wants price where everyone who wants to buy can, and everyone who wants to sell does. This is essentially the concept of equilibrium price. But the reasoning pattern? He is using anecdotal evidence of previous weeks to infer that there must be a price where supply equals demand. He might be committing a "false cause" or "post hoc ergo propter hoc" fallacy? Or "availability heuristic" or "representativeness"? He is assuming that because at price 2 there was shortage and at price 8 there was surplus, there must be a price where supply equals demand. That is actually correct in a typical supply-demand curve. 

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student failed to identify the correct economic pattern (Supply, Demand, Equilibrium) or calculate the equilibrium price (P=5, Q=50). Instead of analyzing the provided table to find where quantity supplied equals quantity demanded, the student became confused by the prompt's wording, incorrectly

---

### C5.2: Price controls and deadweight loss
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** The king sets a price ceiling of 3 gold per bushel. Equilibrium was at 5 gold and 50 bushels. What happens to quantity supplied, quantity demanded, and the market? What trades are lost?

**Expected Answer:** **Price controls and deadweight loss** — A binding price ceiling (set below equilibrium) creates a shortage: quantity demanded exceeds quantity supplied. At P=3, Qs=30 and Qd=70, shortage=40. Some mutually beneficial trades that would occur at equilibrium (P=5, Q=50) no longer happen. The lost surplus from these unrealized trades is deadwe *The price ceiling is well-intentioned but creates predictable inefficiency. The 30 buyers who get grain pay less, but 20 buyers who would have purchased at equilibrium get nothing, and 20 units of gra*

**Model Response:**
> We need to analyze scenario: market master reasoning about price ceiling. He says: "At 3 gold, supply 30, demand 70, shortage 40. First 30 buyers get cheap grain, other 40 get nothing. Some farmers who would sell at 5 gold but won't at 3 are staying home. The king meant well. But 40 people are going hungry who weren't before, and black market at 7 gold. Is the ceiling actually helping?" The question: what specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? The market master is focusing on the immediate distributional effect: some get grain, some don't; he is ignoring overall welfare, efficiency, or externalities. He might be exhibiting the "distributional fallacy" or "short-term vs long-term analysis" or "supply-side economics"? He is focusing on

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the quantitative effects of the price ceiling (shortage of 40, supply of 30, demand of 70) and notes the existence of a black market and lost trades (farmers staying home). This aligns with Level 2. However, the response fails to reach Level 3 because it does not cle

---

### C6.1: Externalities
**Track:** microeconomics | **Tier:** drill | **Type:** dual

**Question:** Grist says his business is profitable and efficient. Wynn says Clearwater is paying part of his costs. Who is right, and what does this situation reveal about market prices?

**Expected Answer:** **Externalities** — A negative externality is a cost imposed on third parties who are not involved in the transaction. Grist's private cost is 40 gold, but the social cost includes the 20 gold per week Clearwater spends on water treatment. The true social cost of production is 60 gold, making Grist's true profit 40, no *Externalities mean the market price sends the wrong signal. Grist's leather seems like a great deal at 100 gold, but 20 gold of the true cost is hidden and borne by Clearwater. The market 'works' only*

**Model Response:**
> **1. What is being demonstrated?**  
The reasoning hinges on an **externality**—specifically a **negative externality** that the tannery imposes on the downstream village. The

**Score:** 1/4 █░░░
**Judge Reasoning:** The student correctly identifies the pattern as a 'negative externality,' which prevents a Level 0 or 1 score based on pattern recognition alone. However, the response is incomplete and cuts off mid-sentence ('The...'). Consequently, the student fails to explain the mechanism (social vs. private cos

---

### C6.2: Information asymmetry
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Kael says good horse owners are leaving the market and only bad horses remain. Why is this happening, and what drives the spiral?

**Expected Answer:** **Information asymmetry and adverse selection (lemons problem)** — When sellers know more about product quality than buyers, buyers cannot distinguish good from bad. They offer a price reflecting average quality. Owners of above-average horses find this price too low and withdraw. The remaining pool is worse, buyers adjust downward, more good horses leave — a death *The market failure is not caused by dishonesty per se but by the information structure. Even honest sellers of good horses cannot credibly communicate quality because cheap talk ('my horse is great') *

**Model Response:**
> **1. What is being demonstrated?**  
The buyer is describing a classic *adverse‑selection* problem – the “market for lemons” that Akerlof (1970) formalised.

**2. Precise name**  
*Market for Lemons* (information asymmetry → adverse selection).

**3. Mechanism – why the reasoning is sound (and when it can mislead)**  

| Step | What happens | Why it matters |
|------|--------------|----------------|
| **Private information** | Sellers know the true health of each horse; buyers cannot see it. | Buyers cannot distinguish good from bad. |
| **Price‑signal mismatch** | A good horse can fetch the same price as a broken one because buyers cannot verify quality. | Sellers of good horses are under‑compensated. |
| **Exit of high‑quality sellers** | Good owners move to private sales or

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as adverse selection and the 'Market for Lemons.' They accurately explain the mechanism: private information leads to price mismatches, causing high-quality sellers to exit. The response cuts off before fully articulating the feedback loop (the spiral whe

---

### C6.3: Behavioral economics in markets
**Track:** microeconomics | **Tier:** what_if | **Type:** dual

**Question:** Nobody buys the Barrel Mug, yet adding it to the menu increases Large Ale sales. The tip jar moved but the tip amount was not suggested. What is going on in both cases, and is it ethically acceptable?

**Expected Answer:** **Behavioral economics in markets: nudges and choice architecture** — Two phenomena are at work. First, the decoy effect: the Barrel Mug is a dominated option that no one chooses, but its presence makes the Large Ale seem more reasonable by comparison. It shifts the reference point. Second, choice architecture: the placement of the tip jar changes behavior without cha *When used to exploit, nudges can undermine autonomous decision-making. Customers believe they are choosing based on preferences, but the choice architecture is steering them toward the seller's prefer*

**Model Response:**
> **1. What is being demonstrated?**  
Lena is exploiting the *anchoring (reference‑price) effect* – a classic decision‑theoretic bias in which the presence of a high‑priced item creates a mental reference point that makes other prices appear more reasonable.

**2. Precise name**  
*Anchoring bias* (sometimes called the *price‑anchor* or *reference‑price* effect).  
In marketing parlance it is often called *menu anchoring* or *price anchoring*.

**3. Mechanism – why it works (and why it can be questionable)**  

| Element | How it operates | Why it changes choice |
|---------|-----------------|-----------------------|
| **High‑priced “Barrel Mug”** | Sets a *reference point* in the customer’s mind. | Customers compare all other prices to that 15‑copper anchor. 8 copper now feels “cheap” or “

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core mechanisms: the influence of a dominated option (mislabeling it 'anchoring' instead of 'decoy effect') and choice architecture regarding the tip jar. They explain how context shifts perception beyond rational preference and begin to address the ethical tensi

---

### C7.1: Broken window fallacy
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Breck says the storm is good for the economy because it creates repair jobs. The clerk is skeptical. Who is right, and what is Breck failing to consider?

**Expected Answer:** **Broken window fallacy** — Breck counts the economic activity generated by repairing storm damage (the seen) but ignores the economic activity that the same money would have generated if spent on something else (the unseen). The glazier's gain is real, but the shopkeepers now spend money on window repairs instead of on new in *The fallacy confuses visible economic activity with net economic gain. Repair spending is seen; the forgone alternative spending is unseen. Bastiat's insight: 'the bad economist confines himself to th*

**Model Response:**
> We need to analyze the scenario: Alderman Breck is arguing that the storm is beneficial for the local economy, pointing to increased demand for glazier, carpenter, lumber mill, etc. He says destruction creates demand, which creates jobs, which creates prosperity. This is a fallacy or bias. Likely "post hoc ergo propter hoc" or "hasty generalization"? Actually he's attributing positive economic outcomes to the disaster, ignoring negative costs. This is a "confirmation bias" or "optimism bias" or "sunk cost fallacy"? He is ignoring the negative side effects. He is basically saying that disasters create opportunities, ignoring the costs. This is a "benefit fallacy" or "neglect of opportunity cost." He is focusing on the positive side of the disaster while ignoring the negative. This is akin t

**Score:** 1/4 █░░░
**Judge Reasoning:** The student senses the argument is flawed and correctly identifies that Breck ignores costs/negative effects, but fails to identify the specific 'Broken Window Fallacy' or the core mechanism of opportunity cost (the 'unseen' alternative uses of money). Instead, the student incorrectly labels the err

---

### C7.2: Zero-sum thinking
**Track:** microeconomics | **Tier:** drill | **Type:** bad_thinking

**Question:** Dagan says that if Brassholm gains from trade, Ardenvale must lose. Petra says both sides can gain. Who is right, and why?

**Expected Answer:** **Zero-sum thinking** — Dagan falsely assumes that trade is zero-sum — that total value is fixed and any gain for one party is a loss for the other. In reality, voluntary trade creates value because parties exchange goods they value less for goods they value more. Ardenvale values iron more than its surplus grain; Brasshol *If trade were truly zero-sum, neither party would voluntarily agree to it — why accept a deal that makes you worse off? The fact that both parties choose to trade is evidence that both expect to benef*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Dagan is treating the trade agreement as a *zero‑sum* transaction: he assumes that every gold piece Brassholm earns must come from Ardenvale’s pocket. In other words, he is committing the **zero‑sum fallacy** (also called *zero‑sum bias*).  

**2. Precise name**  
*Zero‑sum fallacy* (or *zero‑sum bias*).  

**3. How the mechanism works – why it is misleading**  

| Element | What Dagan thinks | Why it is wrong |
|---------|

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the reasoning pattern as 'zero-sum' and accurately describes Dagan's flawed assumption (that one side's gain is the other's loss). However, the response is incomplete; the explanation table cuts off before the student can articulate the mechanism of value creation (t

---

### D1.1: Rapoport's Rules
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Corwin disagrees with Guild Master Holt, but the Guild members stay seated and keep listening. What exactly is Corwin doing — step by step — before he voices his criticism, and why does each step matter?

**Expected Answer:** **Rapoport's Rules** — A four-step protocol for productive disagreement: (1) restate the opponent's position so well they endorse the restatement, (2) list genuine points of agreement, (3) acknowledge what you learned from them, (4) only then offer criticism. Corwin follows all four steps in sequence. *Corwin follows the protocol exactly. Step 1: Holt says 'Better than I put it myself.' Step 2: Lists two factual agreements about timber loss and budget crisis. Step 3: Concedes the flow-rate data corr*

**Model Response:**
> We need to analyze the scenario. Alderman Corwin is moderating. He summarizes Holt's position, then agrees with some facts, then says he was wrong, then shifts tone, then says the Guild's proposal assumes salmon run is a luxury, but it's not. He uses the Anglers' ledgers to argue that fishing revenue, tourism, irrigation exceed mine revenue. He proposes a weir design.

We need to identify a specific reasoning pattern, fallacy, bias, or decision-theoretic concept being demonstrated. Let's examine.

He first summarizes Holt's position accurately. He then acknowledges facts. He then says "I was wrong to dismiss it at last month's council meeting." He then says "But here is where I part ways with the Guild. Their proposal assumes the salmon run is a luxury. It is not. The Anglers' own ledgers 

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the correct pattern (Rapoport's Rules/protocol for productive disagreement). Instead of recognizing the deliberate four-step structure of steelmanning, the student interpreted the scenario as a series of logical fallacies (e.g., argument from consequences, c

---

### D1.2: Reductio ad absurdum
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** Tessa responded to Varek's claim in a particular way. What exactly did she do, and why is it effective?

**Expected Answer:** **Reductio ad absurdum** — Tessa takes Varek's claim ('all beliefs are equally valid') and draws out its logical consequences: flat earth is as valid as round earth, poison is as nutritious as food. Since Varek cannot accept these consequences, his original claim is undermined. This is the classic structure of reductio: assum *Reductio is a powerful tool because it tests a claim by its own standards. If a principle generates consequences the proponent themselves cannot stomach, the principle is in trouble. You do not need t*

**Model Response:**
> **1. What is being demonstrated?**  
Varek is espousing an *epistemic relativism* that treats every belief as “equally valid.”  The pattern is the classic **relativist fallacy** (sometimes called a *false equivalence* or *equivocation* between “valid” and “true”).  

**2. Precise name**  
- **Epistemic relativism** (the claim that truth or justification is relative to a perspective).  
- The logical error that follows is the **relativist fallacy** (the self‑defeating move that “all beliefs are equally valid” implies that false or harmful beliefs are just as legitimate as true ones).

**3. Mechanism – why it is good or bad**  

| Feature | How it works | Why it fails |
|---------|--------------|--------------|
| **Equating “valid” with “true”** | Varek says “valid” means “no belief is bette

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Tessa demonstrates Varek's claim leads to absurd conclusions (flat earth, poison) and notes the self-defeating nature of the argument. However, the student misidentifies the logical pattern as the 'relativist fallacy' or 'false equivalence' rather than 'reductio

---

### D1.3: Occam's Razor
**Track:** dennett_tools | **Tier:** drill | **Type:** good_tool

**Question:** You have two explanations for the attic disturbances. What principle should guide your choice between them, and which explanation does it favour?

**Expected Answer:** **Occam's Razor** — When two hypotheses explain the same evidence, prefer the one that posits fewer entities and mechanisms. Elsa's squirrel hypothesis explains the torn food, scattered flour, muddy tracks, thumping, and fallen items using one known entity (squirrels) and one known mechanism (foraging through a gap). W *Occam's Razor is not a proof — it is a heuristic for rational belief. Simpler explanations are preferred because each additional assumption is an additional point of potential failure. The squirrel hy*

**Model Response:**
> We need to analyze scenario: two characters present arguments: Widow Moss claims ghost; Elsa suggests squirrels. We need to identify reasoning pattern, fallacy, bias, or decision-theoretic concept. Likely "confirmation bias" or "availability heuristic" or "anchoring" or "hasty generalization" or "argument from ignorance" or "false dilemma" or "appeal to nature"? Let's analyze.

Garret's daughter Elsa says "Or — and hear me out — it's squirrels. There's a gap under the eaves, there are muddy paw prints on the beam, and I found a nest of shredded cloth behind the flour barrel. We don't need a ghost to explain any of this." She is presenting evidence that supports squirrels. Widow Moss says ghost. The scenario might illustrate "argument from ignorance" (lack of evidence for ghost => ghost). B

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student failed to identify the correct reasoning pattern (Occam's Razor/Parsimony). Instead, they incorrectly hypothesized that the scenario demonstrates 'Confirmation Bias,' 'Appeal to Ignorance,' or 'Availability Heuristic.' The response shows no understanding of the core principle that the sq

---

### D1.4: Occam's Broom
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Alderman Cask seems to have made a strong case. But look carefully at what he talked about and what he did not talk about. What is his argumentative strategy, and what is wrong with it?

**Expected Answer:** **Occam's Broom** — Dennett coined 'Occam's Broom' to describe the practice of sweeping inconvenient facts under the rug to make your argument look cleaner than it is. Unlike Occam's Razor (which removes unnecessary assumptions), Occam's Broom removes necessary evidence. Cask does not engage with the three independent  *Honest reasoning requires engaging with all the relevant evidence, especially evidence that challenges your position. Cask's case looks strong only because he has hidden the strongest evidence against*

**Model Response:**
> We need to analyze the scenario: Alderman Cask dismisses Dr. Lune's evidence. He uses his own company's inspectors report, points to miners healthy, mentions previous assessments that found no contamination, and attacks Dr. Lune's funding. He does not address the independent studies. This is a classic "appeal to authority" or "appeal to personal experience" or "argument from authority" but also "ad hominem" (attacking Dr. Lune's funding). He also uses "appeal to authority" by citing his own company's inspectors. He also uses "appeal to the people" (miners healthy). He also uses "appeal to ignorance" maybe. But the main pattern: "argument from authority" or "appeal to authority" (citing inspectors). But he also uses "argumentum ad hominem" (attacking Dr. Lune). He also uses "appeal to the p

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Cask ignores the three independent studies and lists several fallacies present (ad hominem, appeal to authority). However, the student fails to identify the specific overarching pattern of 'Occam's Broom' (selective suppression of inconvenient evidence to create

---

### D1.5: Jootsing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Torvin says Cael is just ignoring the rules. Cael says something different. What is Cael's actual claim about his relationship to the guild's rules, and why does it matter?

**Expected Answer:** **Jootsing (Jumping Out Of The System)** — Dennett argues that genuine creativity requires first mastering the rules of the system you are working in, and then deliberately violating specific rules for specific reasons. Random rule-breaking is just noise. Informed rule-breaking — knowing which rule to break, why, and what it will produce — i *Jootsing is valuable because it distinguishes productive creativity from mere rebellion. It explains why the most innovative artists, scientists, and thinkers are typically those who first achieved de*

**Model Response:**
> We need to analyze the scenario: Cael says he studied the rules, understood them, then broke them. He claims that understanding the system allows him to break it. Torvin says rules exist for reason; Cael says he used a seventh color, breaking the grid, but he knows why. This is a kind of "rule-breaking after mastery" argument. The reasoning pattern might be "expertise-based justification" or "appeal to expertise" or "expertise fallacy" or "argument from authority" but not exactly. Could be "the fallacy of the expert" or "expertise bias" or "the argument that because you understand the system, you can break it" is akin to "the fallacy of the 'rule of thumb' or 'rule of expertise'." Might be "appeal to novelty" or "appeal to innovation." But the question: "What specific reasoning pattern, fa

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the surface-level distinction that Cael learned the rules before breaking them, which prevents a Level 0 or 1 score. However, the student fundamentally misinterprets the reasoning pattern as a fallacy ('expertise bias', 'overconfidence') rather than recognizing it as

---

### D1.6: Deepities
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Kira thinks Brother Aelm said something profound. Did he? What exactly does 'Love is just a word' mean, and is it as deep as it sounds?

**Expected Answer:** **Deepity** — A deepity is a statement that seems profound but achieves this effect through ambiguity. It has two readings: (1) a trivially true reading that is not interesting, and (2) a reading that would be profound if true but is false or unsupported. The listener experiences the truth of reading 1 and the de *Deepities are intellectually dishonest because they exploit ambiguity to simulate profundity. They create the feeling of insight without delivering any actual content. Once you separate the two readin*

**Model Response:**
> We need to analyze scenario: Brother Aelm says "Love is just a word." He uses rhetorical argument: love is just a word, four letters, breath of air, everything built on it is built on nothing more than a sound. He claims it's profound. This is a form of argument that reduces complex concept to trivial, maybe a fallacy: "reductio ad absurdum"? Or "argument from metaphor"? He uses "love is just a word" as a claim that love is meaningless. He uses rhetorical flourish. This is likely a "semantic fallacy" or "equivocation" or "argument from ignorance"? He says "love is just a word" meaning it's just a label, not real. He might be committing the "fallacy of composition" (assuming that because love is a word, everything built on love is trivial). Or "fallacy of the single cause"? Or "reductio ad 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that the statement relies on ambiguity and conflates the linguistic symbol ('word') with the concept ('love'), noting it is a 'semantic fallacy' or 'equivocation.' However, the response fails to clearly separate the two distinct readings required for Level 3 (the tri

---

### D1.7: The 'surely' operator
**Track:** dennett_tools | **Tier:** drill | **Type:** bad_thinking

**Question:** Professor Venn used the word 'surely' three times. What work is that word doing in his argument? Is it helping or hiding something?

**Expected Answer:** **The 'surely' operator** — Dennett identifies 'surely' as a rhetorical operator that attempts to sneak a controversial claim past the audience by presenting it as something everyone already agrees with. When a speaker says 'surely X,' they are signalling that X does not need argument — it is supposed to be obvious. But in phi *The 'surely' operator substitutes rhetorical confidence for actual argument. Each of Venn's three 'surely' claims is a substantive philosophical thesis that requires defence. By prefacing them with 's*

**Model Response:**
> **1. What is being demonstrated?**  
Professor Venn is committing an **argument from ignorance (ad ignorantiam)**, coupled with a **necessary‑condition fallacy**. He asserts that because we lack evidence that animals can self‑reflect (or that self‑reflection requires language), they cannot suffer.  

**2. Precise name**  
*Argument from ignorance* (also called *appeal to lack of evidence*).  
The specific form is a *necessary‑condition fallacy*: “Suffering requires self‑reflection; animals lack self‑reflection → animals cannot suffer.”

**3. Mechanism – why it is

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely failed to identify the target pattern ('surely' operator). Instead, they incorrectly diagnosed the argument as an 'argument from ignorance' and a 'necessary-condition fallacy,' focusing on the logical structure of the claims rather than the rhetorical device used to smuggle th

---

### D1.8: Goulding
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The advisors and Pella are both trying to help Captain Rhea. But their approaches are very different. What is the difference, and which is more useful? Is there a risk to Pella's approach?

**Expected Answer:** **Goulding** — Dennett uses 'goulding' to describe the intellectual virtue of making bold, specific, testable claims rather than retreating into safe, unfalsifiable hedging. Pella's claim is specific (forty soldiers), testable (you can verify by scouting), and she has staked her credibility on it. The advisors' po *Hedging endlessly is safe for the hedger but useless for decision-making. A specific, falsifiable claim can be tested, acted on, and corrected. Knowledge advances through bold conjectures and refutati*

**Model Response:**
> **1. What is being shown?**  
Pella is exhibiting **over‑confidence bias** (the *confidence effect*).  
She presents a single, unqualified claim that she “knows” the valley is passable, ignores the uncertainty that the other advisors are highlighting, and stakes her rank on it.

**2. Precise name**  
*Over‑confidence bias* – the tendency to overestimate the accuracy of one’s knowledge or predictions and to underestimate the role of chance or uncertainty.

**3. How it works – why it can be good or bad**  

| Mechanism | Effect in this scenario |
|-----------|------------------------|
| **High confidence → decisive action** | Pella’s certainty pushes the commander toward a bold breakout, potentially saving the garrison from starvation. |
| **Underestimation of uncertainty** | She ignores the

**Score:** 0/4 ░░░░
**Judge Reasoning:** The student completely misidentified the pattern. Instead of recognizing 'goulding' (the epistemic virtue of making falsifiable claims), the student labeled the behavior as 'over-confidence bias,' a cognitive error. The student framed Pella's specificity as a failure to acknowledge uncertainty rathe

---

### D2.1: Satisficing
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** The lieutenant thinks Maren is being irrational by not computing the best allocation. What would you tell him about her approach?

**Expected Answer:** **Satisficing as rational strategy** — Maren demonstrates that satisficing — choosing good enough rather than optimal — is not a failure of rationality but the product of it. An ideally rational agent who knows her own limitations would prepare a decision procedure in advance that produces acceptable outcomes under constraint. *The oldest objection to MEU as a decision procedure is that there is no time. Maren's triage protocol is exactly Dennett's Moral First Aid Manual — careful deliberation done when time permits, deploye*

**Model Response:**
> **1. What is being demonstrated?**  
Maren is using a *heuristic* (her triage protocol) because she knows she cannot compute the mathematically optimal allocation in the time available. The lieutenant’s insistence on “exact optimal allocation” is an example of the **analysis‑paralysis fallacy** (over‑emphasis on perfect optimization at the expense of timely action).  

**2. Precise name**  
- **Bounded rationality / satisficing** (the decision‑making strategy that stops when a “good enough” solution is found).  
- The lieutenant’s line of thought is a **planning fallacy / analysis‑paralysis** (thinking that a perfect solution is required and that it can be found quickly).  

**3. Mechanism – why it works or fails**  

| Mechanism | Why it’s good | Why it can be bad |
|-----------|---------

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the pattern as 'satisficing' and 'bounded rationality,' noting that Maren uses a heuristic due to time constraints. However, the response frames this as a compromise necessitated by inability to compute the optimal solution ('cannot compute... in the time available')

---

### D2.2: The Panglossian Slide
**Track:** dennett_tools | **Tier:** what_if | **Type:** bad_thinking

**Question:** Elder Maren says the village's flood response was 'perfect' and sees no reason to hear the engineer's proposal. What mistake is she making?

**Expected Answer:** **The Panglossian Slide** — Elder Maren begins from the defensible claim that the council did the best they could given constraints (satisficing), then slides into asserting their solution was the best possible solution full stop (optimizing). She reframes losses as unimportant and refuses to consider improvements. *The fact that a decision was the best available under constraints does not make it the best decision simpliciter. Constraints explain why we settled for less; they do not transform the less-than-ideal*

**Model Response:**
> **1. What is being demonstrated?**  
Elder Maren is exhibiting a *status‑quo bias* (sometimes called *conservatism bias* or *resistance to change*). She assumes that because the village’s past flood‑control action “worked” and “lost nothing of real importance,” it must be the best possible solution, and therefore she rejects any new proposal.

**2. Precise name**  
*Status‑quo bias* (a form of *conservatism bias*). It can also be framed as an *appeal to tradition* (argumentum ad antiquitatem) when the justification is “our method has proven itself perfect.”

**3. Mechanism – why it is good or bad**  

| Mechanism | Why it can be good | Why it can be bad |
|-----------|-------------------|-------------------|
| **Anchoring on past success** | Past performance can be a useful heuristic when 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core logical error: conflating a solution that 'worked' under constraints with the 'best possible' solution. They also note the mechanism of ignoring better future options. However, they misidentify the specific pattern as 'status-quo bias' rather than the 'Pangl

---

### D2.3: Conversation-stoppers
**Track:** dennett_tools | **Tier:** what_if | **Type:** dual

**Question:** Sanna says 'This conversation is over.' Breck wants to keep talking. Who is right? Or is that the wrong question?

**Expected Answer:** **Conversation-stopper** — A conversation-stopper is any move that terminates deliberation by appeal to a value, right, rule, or taboo that is held to be non-negotiable. Dennett argues in 'Thought Stoppers' that these can be necessary (we do not deliberate about whether to torture innocents) but also dangerous (they can preve *When a conversation-stopper blocks deliberation about life-and-death matters, it prevents the community from weighing all relevant values. Sanna's move makes it impossible to even discuss whether the *

**Model Response:**
> We need to analyze the scenario: a debate between resettlement vs sacred grove. The reasoning pattern: Breck uses a cost-benefit analysis, focusing on lives vs sacred grove. Elder Sanna uses a deontological or intrinsic value argument. The question: what specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated? The scenario shows a conflict between utilitarian calculation (Breck) and deontological or sanctity argument (Sanna). The fallacy might be "appeal to tradition" or "appeal to nature" or "moral absolutism" or "moral hazard"? But the question: "What specific reasoning pattern, fallacy, bias, or decision-theoretic concept is being demonstrated?" The conversation: Breck says: "A child died, Sanna. Does the grove matter more than living children?" Sa

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Sanna is using a non-negotiable principle ('moral absolutism' or 'deontological reasoning') that shuts down cost-benefit analysis, which aligns with Level 2's requirement to recognize the conversation-ending move. The student also addresses edge cases where this

---

### D2.4: Wolf's Dilemma
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Kael says he knows too much to trust his rules but not enough to abandon them. Is he right that this is a genuine dilemma? Is there a way out?

**Expected Answer:** **Wolf's Dilemma (The Reflective Satisficer's Predicament)** — This is the fundamental tension in bounded rationality: heuristics work because they are fast and frugal, but once you become reflectively aware of their limitations, you face a meta-decision. Do you (a) override the heuristic and reason from scratch (gaining accuracy but losing speed and sometimes  *Blindly following heuristics you know to be flawed can be a form of intellectual cowardice — refusing to engage your critical faculties when it matters.*

**Model Response:**
> We need to analyze scenario: retired general Kael has heuristics that were useful but now he sees their flaws. He is paralyzed: should he abandon them? If he tries to reason from scratch, too slow; if he follows flawed rules, irrational. He knows too much to trust shortcuts but not enough to do without them.

We need to identify reasoning pattern, fallacy, bias, or decision-theoretic concept. Likely "overconfidence bias" or "heuristic overreliance" or "cognitive bias of overconfidence in heuristics." But more specifically, it's about "bounded rationality" and "heuristic vs. algorithmic decision making." The pattern: "The paradox of choice" or "analysis paralysis." He is experiencing "analysis paralysis" due to too many options, but also "overreliance on heuristics" known as "heuristic bias

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core tension of bounded rationality: the trade-off between the speed of heuristics and the accuracy of algorithmic reasoning, noting that abandoning heuristics leads to 'analysis paralysis.' They accurately describe the mechanism (fast but flawed vs. slow but opt

---

### D2.5: The Frame Problem
**Track:** dennett_tools | **Tier:** puzzle | **Type:** dual

**Question:** Sable's two Porters each failed in opposite ways. What is the underlying problem they share, and why is it so hard to solve?

**Expected Answer:** **The Frame Problem** — The Frame Problem asks: how does a rational agent determine what has and has not changed as a result of an action? Version 1 of the Porter checks everything (the Hamlet problem — paralyzed by the attempt to verify all possible changes). Version 2 checks only pre-specified relevant items (the tunnel- *A system that ignores the frame problem — either by checking everything or by pre-specifying a fixed relevance list — will fail catastrophically: either through paralysis or through missing critical c*

**Model Response:**
> We need to analyze scenario: Sable built automaton that checks all possible safety rules before acting. Too many rules cause paralysis. She built second version with fewer checks, but then it didn't check fire, leading to failure. She asks how to decide what to pay attention to. This is about overfitting, overcautiousness, or "analysis paralysis" due to too many constraints. In decision theory, it's about "overly conservative decision-making" or "risk aversion" or "bounded rationality" or "satisficing" vs "optimization". The pattern is "over-constraint" or "over-specification" leading to failure. There's also "the problem of too many constraints" akin to "the curse of dimensionality" or "the curse of overfitting". In AI, it's akin to "overfitting" or "overly general rules" leading to "over

**Score:** 1/4 █░░░
**Judge Reasoning:** The student recognizes the trade-off between checking too much (paralysis) and checking too little (missing fire), which aligns with Level 1. However, they fail to identify the specific pattern as the Frame Problem, instead incorrectly labeling it as 'overfitting,' 'analysis paralysis,' or 'risk ave

---

### D2.6: The Moral First Aid Manual
**Track:** dennett_tools | **Tier:** what_if | **Type:** good_tool

**Question:** Dav wants to know which moral theory to follow. Abbess Thera says he is asking the wrong question. What does she mean, and what is the alternative she is proposing?

**Expected Answer:** **The Moral First Aid Manual** — Dennett proposes that instead of waiting to resolve the centuries-old debate between consequentialism, deontology, virtue ethics, and other moral theories, we should build a practical guide — a Moral First Aid Manual. Just as a medical first aid manual tells you to stop bleeding before diagnosing th *The Moral First Aid Manual is valuable because it is honest about theoretical disagreement while remaining practical. It does not pretend to solve metaethics — it acknowledges that smart, thoughtful p*

**Model Response:**
> We need to analyze scenario: Dav asks which moral theory is correct: theft always wrong vs saving life. Abbess says no one true theory, ask wrong question. This is a classic example of "false dilemma" or "either/or fallacy" or "binary choice" or "moral absolutism vs consequentialism." But Abbess says there's no one true theory, but the question is which one to follow. She says you are asking wrong question. She is pointing out that the question is about which theory is correct, not about what to do. So the reasoning pattern is "questioning the premise" or "meta-ethical relativism." But more specifically, the pattern is "the fallacy of the false dilemma" or "the fallacy of the false choice." However, the question: "Which moral theory do I follow — the one that says theft is always wrong, or

**Score:** 1/4 █░░░
**Judge Reasoning:** The student identifies that the Abbess rejects the idea of a single correct theory but frames this primarily as 'moral pluralism' or 'meta-ethical relativism' (Level 1), explicitly stating 'no one true theory' without grasping the specific constructive mechanism of the 'Moral First Aid Manual.' The 

---

### E1.1: Fundamental attribution error
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Nessa seems pretty confident about why Gareth's harvest failed. But listen to how she talks about her own flooding problem. Do you notice anything different about how she explains the two situations?

**Expected Answer:** **Fundamental attribution error** — Nessa attributes Gareth's poor harvest to his character (laziness, lack of care) while ignoring a situational factor (south-facing blight). When her own field flooded, she cited the external event (flooding) and her response to it. She judges others by disposition and herself by situation. *Gareth's harvest failure has a plausible situational explanation (blight on south-facing land) that Nessa dismisses without investigation. She applies a double standard: her flood was just bad luck sh*

**Model Response:**
> **1. What is being demonstrated?**  
Nessa is committing a *fundamental attribution error* (also called the *actor‑observer bias*).  
She attributes Gareth’s poor harvest to an internal, stable trait (“laziness”) while ignoring or dismissing situational explanations (blight, soil, weather, etc.).  

**2. Precise name**  
**Fundamental Attribution Error (Actor‑Observer Bias)** – the tendency to over‑emphasize dispositional causes for others’ behavior and under‑emphasize situational causes.  

**3. Mechanism – why it is good or bad**  

| Mechanism | Why it can be misleading |
|-----------|--------------------------|
| **Causal inference from a single anecdote** | Nessa uses her own experience (“I re‑dug the drainage in two days”) as evidence that a “real farmer” can overcome obstacles. That

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern by name ('Fundamental Attribution Error' and 'Actor-Observer Bias') and accurately explains the mechanism of attributing Gareth's failure to internal traits while ignoring situational factors. However, the response is incomplete; it cuts off mid-sentence 

---

### E1.10: Pessimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Elder Sorn has real experience with famine, and his fear is understandable. But Dalla has data and a plan. What is driving Sorn's opposition — is it the evidence, or something else?

**Expected Answer:** **Pessimism bias** — Sorn systematically overestimates the likelihood of negative outcomes (three consecutive bad harvests, irrigation failure, additional disasters) while dismissing evidence of positive possibilities (historical base rates, irrigation data from the next valley, Dalla's engineering analysis). His trauma *The historical record shows no precedent for three consecutive failures. The irrigation data from a neighboring valley demonstrates effectiveness even in severe drought. Sorn dismisses both sources of*

**Model Response:**
> **1. What is being demonstrated?**  
Elder Sorn is focusing on the *worst‑possible outcome* and treating it as if it will happen, while ignoring the statistical evidence that the irrigation system would dramatically reduce the probability of a third failure. In decision‑making terms this is a classic **zero‑risk (or “worst‑case”) bias** – the tendency to prefer an option that eliminates a small risk entirely, even when the expected value of a risk‑reducing investment is positive.

**2. Precise name**  
- **Zero‑risk bias** (also called *risk‑aversion to catastrophic outcomes* or *worst‑case bias*).  
- Related heuristics: *availability heuristic* (recent failures loom large) and *negativity bias* (bad outcomes are weighted more heavily).

**3. Mechanism – why it is good or bad**  

| Mecha

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Sorn is overestimating risk and ignoring statistical evidence (Level 2 criteria). However, they explicitly misidentify the pattern as 'Zero-risk bias' rather than the required 'Pessimism bias.' Furthermore, the response fails to connect the behavior to Sorn's tr

---

### E1.11: Negativity bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Venn says 'the bad ones stick with you.' He's right that the failures were real problems. But is he making a good decision by dropping the Dustwalkers? What is he not accounting for?

**Expected Answer:** **Negativity bias** — Venn's memory and emotional weighting are dominated by the three failures. He can recall each one vividly — the silkwood, the dye delay, the smashed glassware — but the forty-seven successes have faded into an undifferentiated background. The negative events carry disproportionate influence on his j *Three failures out of fifty contracts is a 6% failure rate. Replacing the Dustwalkers with the next-best option (81% reliability) would mean roughly ten failures per fifty contracts instead of three. *

**Model Response:**
> **1. What is being demonstrated?**  
Venn is letting a handful of memorable, negative incidents dominate his judgment of an otherwise highly reliable supplier. He is ignoring the overall success rate (the *base rate*) and treating the three failures as if they prove the company is untrustworthy.

**2. Precise name(s)**  
- **Negativity bias / “bad‑event salience”** – the tendency to give disproportionate weight to negative outcomes.  
- **Availability heuristic** – judging probability by how easily examples come to mind.  
- **Base‑rate fallacy** – ignoring the overall frequency (94 % success) in favor of anecdotal incidents.

**3. Mechanism – why it’s problematic (and when it can be useful)**  

| Mechanism | What it does | Why it can mislead | When it can be justified |
|-----------|----

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern (negativity bias) and supporting concepts (availability heuristic, base-rate fallacy). They accurately explain the mechanism of asymmetric weighting between vivid failures and faded successes. Crucially, they address the rubric's highest level requir

---

### E1.12: Groupthink
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** The War Council has reached unanimous agreement on the plan. General Tova seems confident that everyone is on board. But Lord Caelen tells you a different story. What is actually happening in this council, and why does unanimous agreement not mean the plan is sound?

**Expected Answer:** **Groupthink** — The War Council exhibits classic groupthink: (1) the illusion of unanimity — silence is read as agreement; (2) direct pressure on dissenters — Caelen was accused of undermining morale and threatened with expulsion; (3) self-censorship — Caelen and Miren stopped raising concerns; (4) the illusion of  *The plan may have serious flaws (unsurveyed tunnels, questionable cavalry timing) that will only become apparent during execution, when the cost of failure is catastrophic. The council's unanimity doe*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The council is exhibiting **groupthink** – a form of social influence that produces an illusion of unanimity and suppresses dissent. The pattern is reinforced by an **information‑cascade** (each member assumes the others have already considered all angles and therefore need not speak), which is a classic decision‑theoretic failure.

**2. Precise name**  
*Groupthink* (T. Janis, 1972) – the “illusion of unanimity” coupled with “self‑censorship” and “pressure to conform.”  
(If you prefer a decision‑theoretic term, it is an *information cascade* or *herding* effect.)

**3. Mechanism – why it is good or bad**  

| Mechanism | What it does | Why it can be harmful |
|-----------|--------------|-----------------------|
| **Suppression of dissent** | Co

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies 'groupthink' and explicitly names multiple required symptoms (illusion of unanimity, self-censorship, pressure to conform). They clearly explain how these mechanisms degrade decision quality (high-confidence, low-quality decisions, lack of stress-testing). Furthermor

---

### E1.13: Placebo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** dual

**Question:** Mirren's tonic has no active ingredients, yet her patients genuinely improve. Doctor Alden says the tonic does nothing. Who is right, and what is actually causing the improvement?

**Expected Answer:** **Placebo effect** — The placebo effect occurs when a patient experiences real improvement due to their expectation of benefit, not due to any active treatment. It is 'dual' because it is both a genuine phenomenon (belief produces real effects) and a potential source of error (it can mask whether a treatment has any pha *The placebo effect can lead to false conclusions about treatment efficacy. If Mirren never tests against a control group, she cannot distinguish her tonic's effect from belief's effect. This is how in*

**Model Response:**
> We need to analyze the scenario: Mirren claims her tonic works because patients feel better; Alden says it's just placebo. The reasoning pattern: Mirren says "the tonic does nothing, the belief does something. Are those the same?" This is a form of "placebo effect" argument, but the reasoning pattern is "equivocation" or "false equivalence" or "argument from ignorance"? Let's analyze.

Mirren's argument: The tonic does nothing; the belief does something. Are those the same? She is essentially saying that the effect is due to belief, not the tonic. She is not claiming the tonic has active ingredients; she claims the effect is due to belief. She is not making a false claim about the tonic's efficacy; she is acknowledging that the tonic is inert but still beneficial via placebo. This is not a

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'placebo effect' as the core concept and accurately explains the mechanism: belief/expectation produces real improvement despite the treatment being inert. They also correctly note the necessity of controlled trials to separate these effects. The response falls s

---

### E1.14: Reactance
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Kael wanted to learn field medicine when it was optional. Now that it's mandatory, he doesn't want to go. The training itself hasn't changed. What is driving his resistance?

**Expected Answer:** **Reactance** — Reactance is a motivational response to perceived threats to personal freedom. When people feel their autonomy is restricted — even by a reasonable mandate — they experience an urge to restore their freedom by doing the opposite of what is required. Kael wanted the training when it was optional but  *Reactance causes people to act against their own interests solely to reassert autonomy. Kael would benefit from the training and wanted it before the mandate. His refusal serves no purpose except rest*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The soldiers are exhibiting **psychological reactance** – a bias that arises when a person perceives that their freedom of choice is being threatened. The fact that the training was once optional and is now compulsory triggers an automatic “I‑must‑not‑do‑this” reaction, even though the content and benefits of the training have not changed.

**2. Precise name**  
*Psychological Reactance* (sometimes called the *reactance bias* or *reactive opposition*).

**3. Mechanism – why it is “good” or “bad”**  

| Aspect | How it works | Consequence |
|--------|--------------|-------------|
| **Perceived threat to autonomy** | The order “attend or face disciplinary action” is interpreted as a loss of personal freedom. | The soldiers feel a motivational drive

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies 'psychological reactance' and accurately explains the underlying mechanism: the perceived threat to autonomy triggers a motivational drive to restore freedom, leading to opposition despite unchanged training value. The response misses Level 4 because it does not addr

---

### E1.15: Spotlight effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Finch is convinced the audience noticed his wrong note and is judging him for it. The audience seems unaware. What cognitive error is Finch making, and why is his estimate of others' attention so far off?

**Expected Answer:** **Spotlight effect** — The spotlight effect is the tendency to overestimate how much other people notice and remember our appearance, behavior, and mistakes. Finch assumes the entire tavern registered his wrong note because it was vivid and distressing to him. In reality, most audience members were only loosely attending, *The spotlight effect can cause social avoidance, anxiety, and missed opportunities. Finch's one wrong note is trivial in the context of a full performance, but his overestimation of others' attention *

**Model Response:**
> **1. What’s going on?**  
Finch is convinced that *everyone* noticed the wrong note and that his reputation is ruined, even though the tavern’s patrons and the barkeep never mentioned it. He is over‑estimating how much attention people are paying to him.

**2. Precise name**  
**Spotlight Effect** (sometimes called the “illusion of scrutiny” or “spotlight bias”).

**3. How it works – why it’s a problem**  

| Feature | Mechanism | Consequence |
|---------|-----------|-------------|
| **Perceived attention** | People assume that others are watching them as closely as they are watching themselves. | Finch believes the tavern’s audience is fixated on his mistake. |
| **Self‑monitoring bias** | The self‑monitoring system (the part of the brain that keeps track of “how I look to others”) is ove

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'Spotlight Effect' and accurately explains the core mechanism: Finch overestimates attention because he assumes others are watching him as closely as he watches himself (egocentric projection). The response distinguishes between Finch's internal vividness and the

---

### E1.16: Just-world hypothesis
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Aldric explains the flood victims' suffering by pointing to their past choices. Wren challenges his explanations. Who is reasoning more carefully, and what motivates Aldric's interpretation?

**Expected Answer:** **Just-world hypothesis** — The just-world hypothesis is the belief that people get what they deserve: good things happen to good people and bad things happen to bad people. Aldric constructs post-hoc explanations for why the flood victims are responsible for their own suffering (poor savings, bad choices) while ignoring the a *The just-world hypothesis leads to victim-blaming: attributing others' misfortunes to their character rather than to circumstances. It distorts causal reasoning by starting with the conclusion (they d*

**Model Response:**
> **1. What reasoning pattern is at play?**  
A *just‑world* or *moralistic* fallacy – the idea that misfortune is a deserved consequence of people’s own shortcomings.  It is coupled with a classic *correlation‑causation* (post‑hoc) error: the observation that the flood hit low‑lying houses is taken as proof that those who live there “deserved” the damage.

**2. Precise name**  
**Just‑world fallacy** (sometimes called the *moralistic fallacy*).  It is a specific instance of the *false‑cause* or *post‑hoc ergo propter hoc* fallacy when the causal link is inferred from a single anecdote.

**3. Mechanism – why it is good or bad**  

| Mechanism | Why it can be misleading |
|-----------|--------------------------|
| **Anecdotal evidence** – “my house stayed dry, theirs didn’t.” | A single obser

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the 'just-world fallacy' and explains the mechanism of blaming victims to preserve a belief in a fair world, noting how it obscures structural causes. However, the response conflates the just-world hypothesis with logical fallacies like 'post-hoc' and 'correlation-ca

---

### E1.17: Declinism
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Hask says the town was better in the old days. The records show improvements across every measurable dimension. Who is right, and why does Hask's perception differ so sharply from the data?

**Expected Answer:** **Declinism** — Declinism is the tendency to view the past favorably and the future pessimistically, believing that society or conditions are in decline. Hask filters his memories through nostalgia (remembering the good, forgetting the bad) and discounts present improvements because they look different from the pas *Declinism distorts planning and decision-making. If the past was always better and the future will always be worse, there is no point investing in change or improvement. This creates a self-fulfilling*

**Model Response:**
> **1. What is being demonstrated?**  
Hask is using an **appeal to tradition / nostalgia bias** (the *argumentum ad antiquitatem*).  
He argues that the town is “worse” simply because it is no longer the way it was, despite objective evidence that many key indicators have improved.

**2. Precise name**  
*Appeal to Tradition* (also called *Argumentum ad Antiquitatem* or *Nostalgia Fallacy*).  
It is often accompanied by the *status‑quo bias* and the *availability/recency heuristic* that give undue weight to past experience.

**3. Mechanism – why it is good or bad**  

| Feature | How it works | Why it is flawed |
|---------|--------------|------------------|
| **Emotional appeal** | Hask taps into the player’s (or audience’s) sentimental attachment to the “good old days.” | Emotions are not

**Score:** 3/4 ███░
**Judge Reasoning:** The student accurately identifies the core mechanism: nostalgia filtering memories, dismissing objective data in favor of anecdotal evidence, and equating change with decline. However, they label the pattern as 'Appeal to Tradition' rather than the specific cognitive bias 'Declinism.' While the expl

---

### E1.18: Backfire effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Tomas keeps presenting stronger evidence that the well is contaminated. Greer's faction keeps becoming more convinced it is safe. How is this possible, and what mechanism explains it?

**Expected Answer:** **Backfire effect** — The backfire effect occurs when corrective evidence strengthens rather than weakens a held belief. Greer interprets the volume of evidence not as strength of the case but as evidence of an agenda. Each new piece of data is reframed as 'why are you trying so hard?' rather than evaluated on its merits *The backfire effect prevents rational belief updating. Evidence that should reduce confidence in a belief instead increases it, making the belief effectively unfalsifiable. Greer has created a framewo*

**Model Response:**
> We need to analyze scenario: Tomas presents evidence that well contaminated. Greer says more evidence proves his point that well safe. This is a logical fallacy: argument from personal incredulity? No. It's "argument from ignorance" or "appeal to tradition"? Actually Greer says "Every time you come with more papers, it proves my point. If the well were truly dangerous, you wouldn't need this much evidence." This is a form of "argument from lack of evidence" or "argument from ignorance" (ad ignorantiam). But also "appeal to tradition" because grandparents drank well. But the main pattern: "more evidence of danger leads to belief that it's safe" is "argument from evidence scarcity" or "inverse evidence" or "inverse fallacy." Could be "argument from evidence" but reversed: "the more evidence 

**Score:** 1/4 █░░░
**Judge Reasoning:** The student fails to identify the correct pattern (Backfire effect), instead incorrectly labeling the scenario as various logical fallacies like 'affirming the consequent' or 'argument from ignorance.' While the student notes that Greer is being stubborn and misinterpreting evidence, they attribute 

---

### E1.19: Barnum effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Madame Kel's reading felt incredibly accurate to the player. Fenn says she gave the same reading to everyone. How can a generic statement feel so personal, and what does this reveal about how we evaluate descriptions of ourselves?

**Expected Answer:** **Barnum effect (Forer effect)** — The Barnum effect is the tendency to accept vague, general personality descriptions as uniquely applicable to oneself. Madame Kel's statements ('great need for admiration,' 'tendency to be self-critical,' 'unused capacity') are true of nearly everyone but feel personally revelatory to each individua *The Barnum effect leads people to validate unreliable methods (astrology, cold reading, certain personality tests) because the outputs feel accurate. The feeling of accuracy is generated by the vaguen*

**Model Response:**
> **1. What is being demonstrated?**  
The scenario is a textbook illustration of the **Barnum (or Forer) effect** – the cognitive bias that causes people to accept vague, general statements as highly accurate for themselves.

**2. Precise name**  
- **Barnum effect** (also called the **Forer effect** after psychologist Bertram Forer).  
- It is a *cognitive bias* that can be seen as a *confirmation‑bias* in action, but the specific phenomenon is the Barnum effect.

**3. Mechanism – why it feels “good” (but is actually misleading)**  

| Component | How it works | Why it feels convincing |
|-----------|--------------|-------------------------|
| **Vague, ambiguous wording** | Statements like “you have a great need for other people to like you” can apply to almost anyone. | The wording is bro

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the Barnum effect by name and provides a comprehensive explanation of the psychological mechanisms involved, including vague wording, authority bias, confirmation bias, and self-referential interpretation. The response goes beyond basic identification to discuss crit

---

### E1.2: Confirmation bias
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Maren believes she has solid evidence that her tonic works. What is problematic about how she gathered and evaluated that evidence?

**Expected Answer:** **Confirmation bias** — Maren commits three distinct moves: (1) She only followed up with 20 of 31 customers — the missing 11 may skew results. (2) She finds reasons to disqualify negative reports rather than counting them as counterevidence. (3) She treats her selective survey as equivalent to controlled trials, ignoring  *Maren's investigation is designed — unconsciously — to confirm what she already believes. She selectively sampled, disqualified negative results, and dismissed the stronger methodology.*

**Model Response:**
> We need to analyze the scenario: Maren is using anecdotal evidence, cherry-picking data, ignoring counterexamples, ignoring sample size, ignoring bias. She says 14/20 improved. She dismisses those who didn't finish or had other illness. She says 31 customers, 20 tracked, 14 improved. She claims physician's papers are irrelevant. This is a classic example of the "self-selection bias" or "selection bias" or "confirmation bias" or "cherry picking" or "sampling bias" or "post hoc ergo propter hoc"? She also uses "argument from personal experience" or "appeal to authority"? She says "I know what works" because of her experience. So the reasoning pattern is "self-selection bias" or "sampling bias" or "confirmation bias" or "anecdotal evidence" or "overgeneralization" or "small sample fallacy". T

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the core components of confirmation bias: selective attention to supporting evidence (cherry-picking the 14/20) and the active dismissal of disconfirming evidence (ignoring the 6 who didn't improve or had other illnesses). They also note the rejection of controlled t

---

### E1.20: Sunk cost fallacy (cognitive)
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brynn gives several reasons for continuing with her crusher. What are those reasons, and do they actually tell her anything about whether continuing is a good idea going forward?

**Expected Answer:** **Sunk cost fallacy** — Brynn treats past investment (three years, four thousand silvers) as a reason to continue investing, when that money and time are gone regardless. Her decision should depend only on future costs and benefits: further redesigns vs. the proven dwarven machine. *Past expenditures are irrecoverable. By treating sunk costs as a reason to persist, Brynn guarantees a bad investment becomes worse. The dwarven machine offers better prospects at lower future cost.*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Brynn is falling into the **sunk‑cost fallacy** (sometimes called “throw‑away‑the‑boat” or “sunk‑cost bias”).  

**2. Precise name**  
*The Sunk Cost Fallacy* – the mistaken belief that past, irrecoverable expenditures should influence the decision about future actions.  

**3. How it works – why it’s problematic**  

| What she thinks | What the fallacy actually does | Why it misleads |
|-----------------|--------------------------------|-----------------|
| “I’ve already spent 4 000 silvers and three years.” | She treats those past costs as if they can be “recovered” by continuing. | Past costs are *irrecoverable*; they should not affect the marginal cost/benefit analysis of the next step. |
| “If I quit, all that was for nothing.” | She equate

**Score:** 4/4 ████
**Judge Reasoning:** The student explicitly names the 'Sunk Cost Fallacy,' correctly explains that past costs are irrecoverable and should not influence future decisions, and outlines the rational decision-theoretic alternative (focusing on marginal costs/benefits). The response also addresses edge cases where persistin

---

### E1.21: Framing effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renn recommends the treatment and Holt opposes it, but they are describing the same data. What is causing their disagreement, and what does this reveal about how we process information?

**Expected Answer:** **Framing effect** — The framing effect occurs when the way information is presented influences judgment and decision-making, even when the underlying facts are identical. '200 saved out of 600' and '400 die out of 600' describe the same outcome, but the gain frame (lives saved) produces positive affect and risk aversio *Rational evaluation should not depend on whether equivalent information is presented as a gain or a loss. The framing effect shows that our judgments are systematically influenced by presentation — we*

**Model Response:**
> **1. What is being demonstrated?**  
The two advisors are reacting to the *same* statistical facts but to *different* presentations of those facts. This is the classic **framing effect** (a form of the *gain‑vs‑loss framing* bias that underlies Prospect Theory).

---

**2. Precise name**  
- **Framing effect** (also called *gain/loss framing*).  
- In decision‑theoretic terms it is the *reference‑point bias* that drives the *prospect‑theory* evaluation of outcomes.

---

**3. Mechanism – why it looks “good” or “bad”**  

| What happens | Why it matters | Is it a logical fallacy? |
|--------------|----------------|--------------------------|
| The same data are expressed as “200 saved” (a *gain* framing) vs “400 die” (a *loss* framing). | Humans evaluate outcomes relative to a reference poi

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the framing effect and explicitly connects it to Prospect Theory and reference-point bias (Tversky and Kahneman). They accurately explain the gain/loss asymmetry mechanism where emotional valence overrides identical statistical facts. Furthermore, the response sugges

---

### E1.22: In-group bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Forge Master Dunn rated the Ironworkers' proposal higher, but an independent engineer certified both as equivalent. What is driving Dunn's different evaluations of identical work?

**Expected Answer:** **In-group bias** — In-group bias is the tendency to favor members of one's own group — evaluating their work more charitably, trusting them more readily, and attributing positive qualities to them — while viewing out-group members with suspicion, scrutiny, and less charitable interpretation. Dunn reads the same qualit *In-group bias distorts evaluation, allocation, and justice. It means the best proposal does not always win — the in-group proposal does. Over time, it concentrates resources and opportunities within f*

**Model Response:**
> **1. What is being demonstrated?**  
Forge Master Dunn is letting his *in‑group bias* (the “affect heuristic” that favors the guild he belongs to) drive the evaluation, while simultaneously launching an *ad hominem* attack on the rival guild. The decision

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the pattern as 'in-group bias' and accurately explains the mechanism as favoring one's own guild while attacking the rival. Although the response is cut off before proposing structural solutions (required for Level 4), it fully meets the Level 3 criteria of identifyi

---

### E1.23: Halo effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Magistrate Yorn acquitted Ella and convicted Rusk on identical evidence. What is different between the two cases, and how is it affecting his judgment?

**Expected Answer:** **Halo effect** — The halo effect is the tendency for a positive impression of someone in one domain (personality, appearance, likability) to influence judgment of them in unrelated domains (guilt, competence, trustworthiness). Yorn likes Ella, so he interprets ambiguous evidence in her favor. He distrusts Rusk, so h *The halo effect undermines fair evaluation by allowing an overall impression to contaminate specific judgments. In a courtroom, it means likeable defendants are acquitted and unlikeable defendants are*

**Model Response:**
> **1. What is being demonstrated?**  
The judge is applying an *affect‑based bias* (also called the *affect heuristic* or *affective bias*).  He lets his personal feelings toward the two suspects – fondness for Ella and distrust of Rusk – colour how he interprets the *same* evidence.

**2. Precise name**  
*Affection‑based bias / affect heuristic* (sometimes called *bias by affect*).  In decision‑theoretic terms it is a *double‑standard* that violates the principle of *evidence‑equivalence*.

**3. How it works – why it is problematic**  

| Judge’s view | Mechanism | Consequence |
|--------------|-----------|-------------|
| “Ella is a good person, so the grain‑dust evidence must be coincidence.” | The judge’s positive affect toward Ella *down‑weights* the evidence.  He implicitly treats th

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies the core mechanism: Yorn's personal feelings (liking Ella, disliking Rusk) cause him to interpret identical evidence differently. This satisfies Level 2. However, the student explicitly names the pattern as 'affect-based bias' or 'affect heuristic' rather than the re

---

### E1.24: Bystander effect
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Twenty people watched the theft and nobody acted. Each person had a reason — but it was the same reason. What is it, and why does having more witnesses make help less likely rather than more likely?

**Expected Answer:** **Bystander effect** — The bystander effect occurs when the presence of others reduces each individual's sense of personal responsibility to act. In a crowd, each person assumes someone else will intervene (diffusion of responsibility), looks to others' inaction as a signal that action is not needed (pluralistic ignorance *The bystander effect turns numbers — which should increase the chance of help — into a liability. Each additional witness reduces rather than increases the probability of intervention because responsi*

**Model Response:**
> **1. What is being demonstrated?**  
The scene is a textbook illustration of the **bystander effect** (also called *diffusion of responsibility*). Each observer assumes that someone else will step in, so the perceived personal obligation to act drops to zero.

**2. Precise name**  
*Diffusion of Responsibility / Bystander Effect* (sometimes framed as *pluralistic ignorance* when the silent consensus is mistaken).

**3. Mechanism – why it’s a bad reasoning pattern**  
- **Social norm misreading** – In a crowd, the default expectation is that *someone* will intervene.  
- **Responsibility dilution** – Each individual’s sense of personal duty is weakened because the group shares the responsibility.  
- **Risk‑aversion amplification** – With many eyes on the scene, the perceived risk of acting

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies the bystander effect and provides a strong explanation of diffusion of responsibility and how individual inaction reinforces the group's paralysis (pluralistic ignorance). They also offer valid strategies to break the effect. However, the response does not explicitly

---

### E1.3: Anchoring
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Brecca's offer of 600 gold feels like a bargain. What is influencing that feeling, and should you trust it?

**Expected Answer:** **Anchoring** — The first numerical information — Brecca's 900-gold appraisal — sets a mental reference point that distorts evaluation of subsequent prices. Her 600-gold offer feels like a deal only because it is compared to the anchor, not to the actual market value (~400g). *The 900-gold figure is arbitrary or inflated, yet it shapes the buyer's sense of what is reasonable. Judging 600 as a good price depends on accepting the anchor rather than independently estimating wo*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The vendor is using **anchoring** (the anchoring‑bias or anchoring effect) – and, to a lesser extent, an **appeal to authority** – to shape the buyer’s perception of the item’s value.

**2. Precise name**  
*Anchoring effect* (price anchoring), with an auxiliary *authority bias* (“Gemwright Guild appraisal”).

**3. How it works – why it can be good or bad**  

| Element | Mechanism | Effect on the buyer |
|---------|-----------|---------------------|
| **Anchor** | Brecca states the opal is appraised at 900 g. | Sets a high reference point. |
| **Discount framing** | She offers it for 600 g, calling it a “fairer deal.” | The 600 g price is perceived as a bargain because it is *below* the anchor. |
| **Authority cue** | “Gemwright Guild themselves

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the anchoring effect and explains the mechanism clearly: the initial 900g figure sets a reference point that makes 600g seem like a bargain. They distinguish between the anchor and genuine market evidence, suggest independent verification strategies, and even address

---

### E1.4: Dunning-Kruger effect
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Dax seems eager and confident. Lirel seems cautious and uncertain. If you had to choose one of them to lead you into the Thornveil Marshes, who would you pick, and why? What does Lirel's uncertainty tell you that Dax's certainty does not?

**Expected Answer:** **Dunning-Kruger effect** — Dax's limited training gives him confidence because he cannot yet see the complexities he has not encountered. His map of Greenvale worked because Greenvale was simple terrain; he generalizes from this success to assume the Thornveil will be the same. Lirel's decades of experience have taught her ho *Dax's confidence is not based on evidence that his methods will work in the Thornveil — it is based on his inability to imagine how they might fail. He does not know what karst terrain does to contour*

**Model Response:**
> **1. What reasoning pattern is at play?**  
Dax is exhibiting **over‑confidence bias (a form of the Dunning‑Kruger effect)** – he assumes that because a simple, well‑known surveying technique worked in one context, it will automatically work in a very different, more hazardous context. He tries to “fix” the problem by adding more data points, ignoring the fact that the *assumption* underlying the technique (uniform slope between sample points) is violated in the Thornveil Marshes.

**2. Precise name**  
*Over‑confidence bias* (sometimes called the “Dunning‑Kruger effect” when the over‑confidence is coupled with a lack of skill or knowledge).

**3. Mechanism – why it is good or bad**  

| Mechanism | Why it can be useful | Why it is harmful in this case |
|-----------|----------------------

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies Dax's overconfidence and notes that his confidence outstrips his experience by misapplying a simple method to a complex context. They also recognize Lirel's caution stems from deeper knowledge. However, the response fails to articulate the specific metacognitive mech

---

### E1.5: Availability heuristic
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Captain Voss has data from Sergeant Tully showing the market district is a much bigger problem. Why does he still want to prioritize the coastal road? What is driving his judgment if not the numbers?

**Expected Answer:** **Availability heuristic** — Voss is judging the probability and severity of threats based on how easily examples come to mind. The wolf attacks are vivid, recent, emotionally charged, and widely discussed — making them highly 'available' in memory. Pickpocketing is mundane, individually minor, and forgettable. This asymmetry i *Two wolf attacks versus 114 pickpocketing incidents and an 8:1 loss ratio clearly indicate where the greater harm lies. Voss acknowledges the data and dismisses it because his emotional memory of the *

**Model Response:**
> **1. What reasoning pattern is at play?**  
Captain Voss is letting the *availability/affect heuristic* drive his decision. He gives disproportionate weight to the recent, vivid wolf attacks because they are emotionally charged and “on the front‑line” of the public’s mind, while ignoring the larger, more routine threat of pickpocketing that is supported by hard data.

**2. Precise name**  
*Availability heuristic* (sometimes called the *affect heuristic* when the bias is driven by fear or emotional salience).

**3. Mechanism – why it’s good or bad**  

| Aspect | How the heuristic works | Why it can be misleading |
|--------|------------------------|--------------------------|
| **Salience** | Recent wolf attacks are vivid, easy to recall, and emotionally charged. | They dominate the menta

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the availability heuristic and explicitly details the mechanisms of vividness, recency, and emotional charge. Crucially, they also address the edge case by explaining when emotional salience might legitimately signal a real threat (e.g., a sudden outbreak), fulfillin

---

### E1.6: Belief bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Tam gave different answers to the two arguments. Professor Hale says they have the same logical structure. Who is right, and what is Tam actually doing when he evaluates these arguments?

**Expected Answer:** **Belief bias** — Tam evaluates the logical validity of arguments based on whether the conclusion aligns with what he already believes to be true, rather than by examining whether the conclusion actually follows from the premises. When the conclusion is believable (roses are plants), he accepts the argument as valid. *Both arguments have the form: All A are B; C is B; therefore C is A. This is the fallacy of the undistributed middle — it is invalid regardless of what A, B, and C are. The roses argument is invalid e*

**Model Response:**
> We need to analyze scenario: Two arguments have same logical structure: All A are B; C is B; therefore C is A. This is a formal fallacy: affirming the consequent? Actually the structure is: All A are B. C is B. Therefore C is A. This is the fallacy of the undistributed middle (or the fallacy of the undistributed middle). It's a formal fallacy. The pattern: "All plants need water. Roses need water. Therefore roses are plants." This is a valid conclusion if we know that all roses are plants? Wait, the premises: All plants need water (P). Roses need water (R). Conclusion: Roses are plants. This is not logically valid. It's the fallacy of the undistributed middle: All A are B; C is B; therefore C is A. The middle term B is undistributed. So the reasoning pattern is the fallacy of the undistrib

**Score:** 3/4 ███░
**Judge Reasoning:** The student correctly identifies that both arguments share the same invalid logical structure (undistributed middle) and explicitly recognizes that Tam is conflating the truth of the conclusion with logical validity (described as 'truth bias' or 'truth-as-validity'). This meets the Level 3 criteria.

---

### E1.7: Self-serving bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Renna explains the caravan success and the mine failure. Listen to who or what she credits in each case. Do you notice a pattern in how she assigns responsibility?

**Expected Answer:** **Self-serving bias** — Renna claims full personal credit for the successful caravan defense (her terrain reading, her instinct, her experience) while deflecting all responsibility for the mine failure onto external factors (bad map, damp torches, client's fault). She does not consider that the caravan success might have i *The asymmetry is unjustified. The caravan success may have involved favorable terrain, weak bandits, or luck in addition to Renna's skill. The mine failure may have involved Renna's failure to scout t*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The captain is exhibiting a **self‑serving bias** (a specific form of the broader *actor‑observer bias*).  

**2. Precise name**  
*Self‑serving attribution bias* (sometimes called the *self‑serving bias* or *self‑serving error*).  

**3. Mechanism – why it is good or bad**  

| What the bias does | Why it can be useful | Why it is problematic |
|--------------------|----------------------|-----------------------|
| **Attribution of success to internal causes** (skill, intuition, experience) | • Maintains confidence and motivation. <br>• Reinforces a sense of competence that can be useful in high‑stakes, high‑stress environments. | • Over‑estimates personal ability. <br>• Ignores situational advantages (terrain, team coordination, luck). <br>• Re

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the self-serving bias and explicitly details the asymmetry in Renna's attributions (internal for success, external for failure). Crucially, the response goes beyond identification to explain why this attribution is unjustified by listing ignored situational factors f

---

### E1.8: Curse of knowledge
**Track:** cognitive_biases | **Tier:** what_if | **Type:** bad_thinking

**Question:** Master Fen is clearly a brilliant glassblower. His students keep quitting. The Guild Elder says the problem is that Fen 'can't remember not knowing.' What does that mean, exactly, and how does it show up in his teaching?

**Expected Answer:** **Curse of knowledge** — Fen's deep expertise has made his skills feel intuitive and self-evident. He cannot reconstruct what it was like to not understand viscosity shifts, breath pressure matching, or rotation timing, so he assumes these things are 'obvious' and 'straightforward.' His instructions reference internal sensa *Fen's teaching fails because he cannot bridge the gap between expert perception and novice perception. 'Feel when the viscosity shifts' is useless instruction to someone who has never felt it. He need*

**Model Response:**
> We need to analyze scenario: Master Fen cannot explain his technique; he relies on intuition, can't articulate. Apprentices drop out. The Guild Elder says he can't explain because he can't remember not knowing. So what reasoning pattern? This is akin to "expertise illusion" or "the Dunning-Kruger effect"? Actually Dunning-Kruger is overconfidence in low ability. Here, the expert can't explain because he can't remember learning; he thinks it's obvious. That's "expertise blind spot" or "knowledge hiding"? The pattern: "Unfamiliarity with the process leads to inability to articulate; the expert's tacit knowledge is not explicit." This is "tacit knowledge" or "the tacit knowledge problem." The reasoning pattern: "The expert's lack of explicit knowledge leads to failure to teach." The concept: 

**Score:** 2/4 ██░░
**Judge Reasoning:** The student correctly identifies that Fen's instructions are too vague and that he assumes the process is obvious because he cannot remember not knowing it. However, the student fails to identify the specific pattern ('Curse of Knowledge'), instead cycling through incorrect or imprecise terms like '

---

### E1.9: Optimism bias
**Track:** cognitive_biases | **Tier:** drill | **Type:** bad_thinking

**Question:** Jorin has good reasons for confidence — a skilled navigator and lighter wagons. But Hesta says every previous leader also had reasons for confidence. Who should you believe, and why?

**Expected Answer:** **Optimism bias** — Jorin overestimates the likelihood of a favorable outcome (three-day crossing) and underestimates the likelihood of setbacks, despite strong base-rate evidence (zero out of twelve expeditions have achieved three days). He does this by focusing on case-specific factors (good navigator, lighter wagons *Twelve out of twelve previous expeditions took longer than three days. Jorin's belief that his navigator and lighter wagons will overcome the pattern is exactly the kind of reasoning every previous le*

**Model Response:**
> **1. What reasoning pattern is at play?**  
The settlers’ leader is falling into the **Planning Fallacy** – an over‑optimistic, under‑estimating of the time (and resources) required to complete a task, driven by a belief that “this time will be different” because of a new navigator or lighter wagons.

**2. Precise name**  
*Planning Fallacy* (sometimes called the “optimism bias” when framed as a belief that one will perform better than the average).

**3. Mechanism – why it is good or bad**  

| What the fallacy does | Why it can be harmful |
|-----------------------|-----------------------|
| Focuses on the *best‑case* scenario (fastest previous run, new navigator, lighter load). | Ignores the *distribution* of past outcomes – the 5‑9‑day range shows high variance and a long tail of delay

**Score:** 4/4 ████
**Judge Reasoning:** The student correctly identifies the core pattern (labeling it Planning Fallacy/Optimism Bias) and accurately explains the mechanism: relying on case-specific factors (new navigator, lighter wagons) to override strong base-rate evidence (0/12 success rate). Crucially, the response meets the Level 4 

---
