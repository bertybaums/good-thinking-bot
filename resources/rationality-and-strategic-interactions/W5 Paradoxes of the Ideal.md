# W5 Paradoxes of the Ideal

**Intuition (Allais) attacks the Ideal $\\rightarrow$ The Ideal defends itself mathematically** 

**Intuition attacks the Structure (Newcomb) $\\rightarrow$ The Ideal defends itself causally.** 

Intuition (Disjunction Principle) attacks structure → Ideal defends by not conflating DP with STP

Intuition (Ellsberg \- ambiguity aversion) attacks → Ideal defends by…

Intuition (Aversion, reflection, and utility) attacks linearity assumption → any defense still?

---

## **Lecture Part 1: The Normative Fortress Under Siege**

### **I. The Hook: The Empirical Attack (The Certainty Effect)**

*Begin by debriefing the exercise the students just completed. Your goal here is to validate their intuitions before you break them.*

**1\. The Allais Setup (Draw this on the board)**

Ask for a show of hands: Who chose Gamble 1 over Gamble 2? Who chose Gamble 4 over Gamble 3? (Expect the majority to fall into the 1 & 4 camp).

| Choice | Ticket 1 (1%) | Tickets 2–11 (10%) | Tickets 12–100 (89%) |
| :---- | :---- | :---- | :---- |
| **Gamble 1** (The "Safe" Bet) | $1M | $1M | $1M |
| **Gamble 2** (The "Risky" Bet) | $0 | $5M | $1M |
|  |  |  |  |
| **Gamble 3** | $1M | $1M | $0 |
| **Gamble 4** | $0 | $5M | $0 |

**2\. Chalk Talk: The "Masking" Exercise**

* **Action:** Physically cover the "Tickets 12–100" column on the chalkboard with a piece of paper or a book.  
* **Discussion:** Ask the students: *"With this column covered, is the choice between Gambles 1 & 2 any different from the choice between Gambles 3 & 4?"* \* **The Reveal:** It is the exact same choice ($1M guaranteed vs. a 10-to-1 shot at $5M). Choosing Gamble 1 and Gamble 4 is a logical contradiction under standard theory.

**3\. The Diagnosis: The Certainty Effect**

Why did our intuition lead us astray? Because humans do not treat probabilities linearly. We treat the jump from 99% to 100% not as a mere 1% increase, but as a qualitative, psychological shift from "risk" to "absolute security."

---

### **II. The Fortress: Why We Defend the Ideal**

*Now pivot to the defense. Why do we hold onto the Standard Model when human psychology so clearly violates it?*

**1\. The Sure Thing Principle (STP) & Independence**

Write the formal rule of STP on the board to show exactly what the Allais choices violated.

**The Sure Thing Principle (STP)**

If you prefer A to B conditional on state $E$, and you prefer A to B conditional on state $\\neg E$, you must prefer A to B simpliciter.

**Formalized:** If $AE \\succeq BE$ and $A\\neg E \\succeq B\\neg E$, then $A \\succeq B$.

**2\. The Structural Connection**

Explain that STP is not an optional add-on; it is the load-bearing pillar of Expected Utility (MEU).

* **State Independence (STP):** Preferences depend *only* on the states where the options differ. The "common consequence" (the 89% column) mathematically cancels out in any Expected Utility calculation.  
* **Menu Independence (IIA):** The value of an option depends only on that option, not the other alternatives on the "menu."  
* **The Bottom Line:** Any violation of STP is inherently a violation of MEU. If we abandon STP to satisfy our Allais intuition, the entire mathematical foundation of rational choice collapses.

**3\. Savage’s Defense: The Optical Illusion**

Introduce Leonard Savage's argument for why the theory isn't wrong—we are.

* **The Analogy:** Just as we can look at a visual optical illusion and incorrectly judge the length of two lines, we can look at a decision matrix and misjudge its rationality.  
* **The Prescription:** Once we apply the math of STP and realize the 89% column is irrelevant noise, a rational agent should *correct* their preference, not discard the principle.

---

### **III. The Bridge: When Psychology Meets Structure**

*Transition from probability puzzles to structural paradoxes. How does the psychological "Certainty Effect" mess with Newcomb's Problem?*

**1\. Weak Newcomb Problems**

We know standard Newcomb pits Dominance (Causal) against Expected Utility (Evidential). But let's look at the *Weak*Newcomb problem, where the transparent box contains a massive $800,000.

| Choice | Predictor Guesses 1 Box | Predictor Guesses 2 Boxes |
| :---- | :---- | :---- |
| **Take 1 Box** (Opaque Only) | $1,000,000 | $0 |
| **Take 2 Boxes** (Opaque \+ Transparent) | $1,800,000 | $800,000 |

**2\. The Intuitive Clash**

* **Evidential Decision Theory (EDT):** Still says to take one box (Expected value of nearly $1M vs. $800k).  
* **Causal Decision Theory (CDT):** Still says to take two boxes (Dominance guarantees you are $800k richer either way).  
* **The Psychological Hook:** Why does EDT suddenly feel so much harder to swallow here than in standard Newcomb? **The Certainty Effect.** Taking two boxes provides a *guaranteed* "sure thing" of $800,000. Taking one box introduces a risk of $0. Just like in Allais, the psychological weight of a guaranteed fortune makes the "rational" choice feel incredibly risky.

---

### **IV. Fortifying the Causal Ideal**

*Conclude by showing how modern decision theory uses Causal Graphs to cut through both evidential traps and psychological biases.*

**1\. The Evidential Trap: Managing the News**

Standard decision tables hide causal dependencies. To illustrate this, use the "Smoking Gene" (or Toxoplasmosis) case.

* **The Setup:** A specific gene causes both a desire to smoke and a high risk of lung cancer.  
* **The EDT Mistake:** Because smoking is highly *correlated* with lung cancer, EDT suggests you shouldn't smoke to lower your probability of having the gene. This is "managing the news"—trying to change the symptom to change the past.

**2\. Enter Causal Graphs BERT: PULL UP THE SLIDES YOU CREATE FOR THIS**

Draw the simple graph on the board: Gene $\\rightarrow$ Smoking and Gene $\\rightarrow$ Cancer.

* Explain that Causal Graphs force us to distinguish between causation (an action changing an outcome) and correlation (an action carrying bad news).

**3\. The Locus of Choice and the $do(Act)$**

How does Causal Decision Theory (CDT) fix this? By introducing the concept of a free intervention, written formally as $do(Act)$.

* **Severing the Arrow:** When the agent acts, CDT "severs" the causal arrows coming *into* the action node.  
* **The Resolution:** In Newcomb, the Predictor's choice is already fixed in the past. By treating your choice as a $do(Act)$ intervention, the graph mathematically proves that choosing Two Boxes cannot retroactively alter the prediction. CDT uses the graph to vindicate the Ideal Agent against our flawed intuitions.

**4\. Conclusion: Engineering vs. Application**

End on Baumgaertner's philosophical pivot. When humans systematically fail MEU and CDT, is it:

* **An Application Failure:** The humans are broken (Savage's Optical Illusion).  
* **An Engineering Failure:** The theory is wrong (Prospect Theory).  
* *Teaser for Next Week:* Or is it **Moral First Aid**? Perhaps these "illusions" are evolved heuristics (Bounded Rationality) that keep finite agents alive.

---

Would you like me to draft a few specific discussion questions to keep in your back pocket to prompt the students during the "Optical Illusion" and "Weak Newcomb" sections?

---

In the first lecture, you showed how humans struggle with *known risk* (Allais) and *structural causation* (Newcomb). This second lecture perfectly tackles the remaining frontiers: how we handle *shifting evidence*, *unknown risk* (ambiguity), and *losses versus gains*.

## **Lecture 2: Beyond Risk: Ambiguity, Reference Points, and Shifting Evidence**

### **I. Warm-up Chalk Talk: The Disjunction Principle Trap**

*Start with a logic puzzle to get them thinking about how evidence works. This clarifies a common misunderstanding about the Sure Thing Principle (STP) covered in the last lecture.*

**1\. The Setup: The Two-Coin Bet** Write this simple game on the board. You are flipping two fair coins.

* **The Bet:** You win **$5** if the coins match (HH, TT). You lose **$4** if they differ (HT, TH).

**Total State (No Evidence):**

* Outcomes: HH, TT, HT, TH (4 total).  
* Winners: HH, TT (2 outcomes).  
* Probability of Winning: 2/4=50%.  
* **EV:** (0.5×$5)+(0.5×−$4)=+$0.50.  
* *Decision:* **ACCEPT** the bet.

**2\. Partial “Shifting” Evidence.** Walk the students through the conditional probabilities.

Now, let's look at the conditional states:

* **State E1​ (At Least One Head):**  
  * Possible Outcomes: {HH, HT, TH} (TT is impossible).  
  * Winners: Only {HH}.  
  * Probability of Winning: 1/3≈33%.  
  * **EV:** (0.33×$5)+(0.67×−$4)=−$1.00.  
  * *Decision:* **REJECT** the bet.  
* **State E2​ (At Least One Tail):**  
  * Possible Outcomes: {TT, HT, TH} (HH is impossible).  
  * Winners: Only {TT}.  
  * Probability of Winning: 1/3≈33%.  
  * **EV:** (0.33×$5)+(0.67×−$4)=−$1.00.  
  * *Decision:* **REJECT** the bet.

**3\. The Trap (The Intuition Failure)**

Now the paradox is active:

1. If I know E1​, I reject.  
2. If I know E2​, I reject.  
3. I know for a fact that either E1​ or E2​ is true.  
4. **Intuition (The Disjunction Principle):** "If I prefer Option B in every possible state of the world, I should prefer Option B in the real world."  
5. **Reality:** I should **Accept** the bet.

**4\. The Resolution (Why Intuition Fails)**

The reason this feels wrong is that we are confusing the **Sure Thing Principle (STP)** with the **Disjunction Principle**.

* **STP applies to Partitions:** STP works when the states are exclusive (e.g., "It rains" vs. "It does not rain"). You are in exactly one state.  
* **The Trap is Overlap:** E1​ and E2​ are **not** exclusive. They overlap.  
  * The intersection of E1​ and E2​ is {HT, TH}.  
  * Notice anything about those two outcomes? **They are the losers.**

**The Crucial Insight:** The information "At least one Head" is partial **bad news**. It eliminates a winning option (TT) but keeps both losing options. The information "At least one Tail" is also partial **bad news**. It eliminates a winning option (HH) but keeps both losing options.

When you are ignorant, you maintain the possibility of both winners. When you gain the partial information of E1​ or E2​, you are forced to discard one of your winning scenarios, concentrating the probability on the loss.

---

### **II. The Ellsberg Paradox (Ambiguity Aversion)**

*Transition: Last week, Allais showed we dislike risk. But what happens when we don't even know what the risk is? Standard MEU says we just assign a "subjective probability" and do the math. Daniel Ellsberg proved we don't do that.*

**1\. The Setup (Draw this on the board)** An urn contains **90 balls**. Exactly 30 are Red. The remaining 60 are a mix of Black and Yellow, but the proportion is completely unknown (it could be 60 Black, 60 Yellow, or anything in between).

| Choice | Red (Exactly 30\) | Black (?) | Yellow (?) |
| :---- | :---- | :---- | :---- |
| **Gamble 1** | **$100** | $0 | $0 |
| **Gamble 2** | $0 | **$100** | $0 |
|  |  |  |  |
| **Gamble 3** | **$100** | $0 | **$100** |
| **Gamble 4** | $0 | **$100** | **$100** |

Export to Sheets

**2\. The Intuitive Choices**

* **Comparison 1:** Ask who prefers Gamble 1 vs. Gamble 2\. Most prefer Gamble 1\. Why? The probability of Red is a *known* 1/3. The probability of Black is an *unknown* 0 to 2/3. We prefer the devil we know.  
* **Comparison 2:** Ask who prefers Gamble 3 vs. Gamble 4\. Most prefer Gamble 4\. Why? Gamble 4 wins on Black or Yellow—which we know for a fact is exactly 2/3 of the urn. Gamble 3 wins on Red or Yellow, which is an unknown quantity. Again, we prefer the known risk.

**3\. The Mathematical Failure** Show how these intuitive, highly common preferences mathematically destroy Expected Utility Theory.

* If a student prefers G1 \> G2, they are implicitly assigning a subjective probability where P(Black)\<1/3.  
* If that same student prefers G4 \> G3, they are implicitly assigning a subjective probability where P(Black)\>1/3. (Because the Yellow column is a "common consequence" between G3 and G4 and should cancel out).  
* **Conclusion:** We cannot assign a single, consistent subjective probability to unknown events. We suffer from **Ambiguity Aversion**. MEU treats known risk and ambiguity as the same mathematical object. Human psychology fundamentally separates them.

---

### **III. The Reflection Effect & Loss Aversion**

*Transition: So, we struggle with probabilities (Certainty Effect, Ambiguity Aversion). What about the other half of the Expected Utility equation? What about Utility itself?*

**1\. The Setup: Kahneman & Tversky** Write these two separate problems on the board and poll the class.

**Problem 1 (Gains):** | Option | Outcome | | :--- | :--- | | **A** | A sure gain of **$500** | | **B** | 50% chance to gain **$1,000** / 50% chance to gain **$0** | *Result: Most choose A. We are Risk Averse when dealing with gains.*

**Problem 2 (Losses):** | Option | Outcome | | :--- | :--- | | **C** | A sure loss of **$500** | | **D** | 50% chance to lose **$1,000** / 50% chance to lose **$0** | *Result: Most choose D. We are Risk Seeking when dealing with losses.*

**2\. Breaking the Utility Curve** Standard MEU assumes humans value their *final asset state* and that our utility curve for wealth is consistently concave (diminishing marginal returns).

Draw a standard utility curve, and then draw the actual S-shaped curve implied by the Reflection Effect.

* If we prefer A over B, our utility curve is flattening out (concave) as we go up.  
* If we prefer D over C, our utility curve is steepening (convex) as we go down.  
* **The Revelation:** Humans do not calculate utility based on final total wealth. We calculate utility based on a **Reference Point** (the status quo). We will wildly gamble to defend our baseline, but play it incredibly safe when adding to it.

---

### **IV. Philosophical Conclusion: The Bridge to Bounded Rationality**

*Bring it all together to set up the rest of the semester.*

* Over the last two lectures, the "Ideal Agent" has taken a beating. Humans violate Independence (Allais), we fail to assign subjective probabilities (Ellsberg), and our utility curves are warped by the status quo (Reflection Effect).  
* **The Big Question:** When the bridge of rationality collapses, is it a failure of *Engineering* (MEU is the wrong mathematical model for reality, so we need Prospect Theory) or a failure of *Application* (humans are just bad at math)?  
* **Teaser for Dennett:** Next week, we look at a third option. Perhaps these "biases" are actually **Moral First Aid**. finite agents living in real-time don't have the computational power to perform infinite Bayesian updates. Ambiguity aversion and loss aversion aren't "errors"—they are evolutionary survival heuristics. We don't calculate the expected utility of the lion in the grass; we run.

---

# **Week 5 Problem Set: Expected Utility and Causal Structures**

**Topics:** Expected Utility Theory, Independence, and Causal Graphs. **Readings:** Baumgaertner Ch. 5 & 7; Weatherson Ch. 16–18.

---

### **Type 1: Drill Exercises**

*These problems focus on the mechanics of calculating Expected Utility and understanding the difference between conditional and unconditional probability in decision matrices.*

**1\. The Medical Decision (EU Calculation)** You are a doctor deciding whether to give a patient Drug A or Drug B.

* **Outcomes:**  
  * *Cure:* Utility \= \+100  
  * *No Change:* Utility \= 0  
  * *Side Effect:* Utility \= \-50  
* **Probabilities:**  
  * **Drug A:** 60% Cure, 30% No Change, 10% Side Effect.  
  * **Drug B:** 40% Cure, 60% No Change, 0% Side Effect.  
* **Task:** Calculate the Expected Utility for both drugs. Which does MEU recommend?

**2\. The Correlated State (State-Act Dependence)** Consider a decision with two acts (A\_1, A\_2) and two states (S\_1, S\_2).

* **Utilities:** U(A\_1, S\_1)=10, U(A\_1, S\_2)=0, U(A\_2, S\_1)=5, U(A\_2, S\_2)=5.  
* **Probabilities:**  
  1. P(S\_1) \= 0.5 (Unconditional)  
  2. P(S\_1 | A\_1) \= 0.2  
  3. P(S\_1 | A\_2) \= 0.8  
* **Task:**  
  1. Calculate the **Evidential Expected Utility** using the conditional probabilities:$V(A) \= P(S\_1|A)U(A,S\_1) \+ P(S\_2|A)U(A,S\_2).  
  2. Calculate the **Causal Expected Utility** using the unconditional probability: U(A) \= P(S\_1)U(A,S\_1) \+ P(S\_2)U(A,S\_2).  
  3. Which action is recommended by each method?

---

### **Type 2: "What-If" Exercises**

*These problems encourage you to manipulate the structural assumptions of the theory, specifically regarding Causal Graphs and the "Common Cause."*

**3\. What If: The Twin's Dilemma** You are playing a Prisoner's Dilemma against your identical twin. You know that because you share the same genetics and upbringing (a "Common Cause"), your twin is highly likely (95%) to do whatever you do.

* **Options:** You Defect, You Cooperate  
* **States (what your twin chooses):** Twin Defects, Twin Cooperates  
* **Payoffs:**  
  1. You Defect, Twin Cooperates: You get $10.  
  2. Both Cooperate: You get $5.  
  3. Both Defect: You get $1.  
  4. You Cooperate, Twin Defects: You get $0.  
* **Task:**  
  1. Draw the **Causal Graph**. Include nodes for *Your Choice*, *Twin's Choice*, and *Shared Genes*.  
  2. If you treat *Twin's Choice* as causally independent (fixed state), what does **Dominance** recommend?  
  3. If you treat *Twin's Choice* as correlated (95% match), what does **Evidential Expected Utility** recommend?  
  4. **Analysis:** According to the Causal Graph approach, which calculation is the "mistake" of managing the news rather than the outcome?

**4\. What If: The "Psychopath Button"** Paul is debating whether to press a button that kills all psychopaths. Paul believes that only a psychopath would be willing to press such a button. He prefers living in a world without psychopaths ($+10$), but he strongly prefers not dying ($-100$).

* **Task:**  
  1. Construct the **Decision Matrix** (Acts: Press/Don't Press; States: Paul is Psychopath/Paul is Normal).  
  2. Explain why an **Evidential Decision Theorist** might refuse to press the button (Hint: What does pressing the button tell Paul about the state?).  
  3. Draw a **Causal Graph** showing the relationship between *Paul's Character*, *Pressing Button*, and *Outcomes*. Use the graph to explain why a Causal Decision Theorist might press it.

---

### **Type 3: Puzzle/Paradox**

**5\. The Ellsberg Paradox (Ambiguity Aversion)**

*Transition: Allais showed we dislike risk. But what happens when we don't even know what the risk is? Standard MEU says we just assign a "subjective probability" and do the math. Daniel Ellsberg proved we don't do that.*

**The Setup** An urn contains **90 balls**. Exactly 30 are Red. The remaining 60 are a mix of Black and Yellow, but the proportion is completely unknown (it could be 60 Black, 60 Yellow, or anything in between).

Consider these options:

| Choice | Red (Exactly 30\) | Black (?) | Yellow (?) |
| :---- | :---- | :---- | :---- |
| **Gamble 1** | **$100** | $0 | $0 |
| **Gamble 2** | $0 | **$100** | $0 |
|  |  |  |  |

* Which gamble do you prefer, or are you indifferent?

Now consider these options:

| Choice | Red (Exactly 30\) | Black (?) | Yellow (?) |
| :---- | :---- | :---- | :---- |
| **Gamble 3** | **$100** | $0 | **$100** |
| **Gamble 4** | $0 | **$100** | **$100** |

* Which gamble do you prefer, or are you indifferent?

* Suppose Jay prefers G1 \> G2. What implicit subjective probability could P(Black) range between?  
* Suppose Jay also prefers G4 \> G3. What implicit subjective probability could P(Black) range between?  
* Is it possible to assign a single, consistent probability to these unknown events? Why or why not?

**6\. Partial Evidence on a Game Show**

*Transition: In class we considered how NOT to think about partial evidence about states. Here you will attempt to think about how you should incorporate information.*

**The Scenario** You are a participant on a game show. You are presented with three closed doors: **Door \#1**, **Door \#2**, and **Door \#3**.

* Behind one of the doors is a **brand-new car** (the prize).  
* Behind the other two doors are **goats** (the booby prizes).

**The Sequence of Events**

1. **Selection:** You select one door (for example, Door \#1).  
2. **The Reveal:** The host—who knows what is behind each door—opens one of the remaining doors (for example, Door \#3). He reveals a **goat**.  
3. **The Offer:** The host then turns to you and offers you a choice:  
   "Do you want to stay with your original choice (Door \#1) or switch to the remaining closed door (Door \#2)?"

**The Question:** Is it to your advantage to switch your choice? Specifically:

1. Does switching increase your probability of winning the car?  
2. Does staying increase your probability of winning?  
3. Or, does it make no difference (is the probability 50/50)?

Describe your reasoning and be prepared to show your work\!

