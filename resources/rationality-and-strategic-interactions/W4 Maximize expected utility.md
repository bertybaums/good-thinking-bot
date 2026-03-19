# W4 Maximize expected utility

Here are the lecture notes for Week 4\. These notes transition the students from the ranking rules of Week 2 (Ordinal Utility) to the calculus of probability and magnitude of Week 4 (Cardinal Utility).

The notes draw heavily on **Baumgaertner Ch. 5** for the calculation mechanics and **Weatherson Ch. 9** for the normative justifications, particularly regarding the Independence of Irrelevant Alternatives (IIA).

---

# **Week 4 Lecture Notes: The Gold Standard (MEU)**

**Topic:** The Maximize Expected Utility (MEU) Formula, Risk Aversion, and Structural Features. **Primary Text:**Baumgaertner, Ch. 5; Weatherson, Ch. 9\.

## **I. Introduction: Why Rank is Not Enough**

In previous weeks, we used **Dominance**, **Maximin**, and **Maximax**. These rules use **ordinal utilities**—they only care if Outcome A is better than Outcome B, not *how much* better.

**The Problem:** Real-world decisions involve trade-offs between the *probability* of an outcome and the *magnitude* of the payoff.

* *Example:* You would prefer a 90% chance of $100 over a 10% chance of $110. Maximin cannot explain this (the minimum is $0 in both cases). Maximax cannot explain this (it chases the $110).  
* **The Solution:** We need **Cardinal Utility** (magnitude) weighted by **Probability** (likelihood). This is **Expected Utility Theory**.

## **II. The Mechanics of MEU (Baumgaertner)**

Baumgaertner defines the **Maximize Expected Utility (MEU)** rule in two steps:

1. **Calculate:** For each option, weight the utility of every possible outcome by the probability of that outcome occurring, then sum them up.  
2. **Maximize:** Select the option with the highest weighted sum.

### **A. Notation**

* $P(S)$ \= Probability of State $S$.  
* $U(A|S)$ \= Utility of Act $A$ given State $S$.  
* **Formula:** $EU(A) \= P(S\_1) \\times U(A|S\_1) \+ P(S\_2) \\times U(A|S\_2) \+ \\dots$.

### **B. Example 1: The Rash (Medical Decision)**

*Context:* You have a rash. It might go away naturally (50%) or continue (50%). You can buy cream for $20 (Success rate 85%) or do nothing. If the rash continues, you pay $100 for a doctor.

**The Matrix:**

|  | Rash Better | Rash Continues |
| ----- | ----- | ----- |
| **Use Cream** | \-$20 | \-$120 |
| **Do Nothing** | $0 | \-$100 |

**The Probabilities:**

* If you **Do Nothing**: $P(\\text{Better}) \= 0.5$, $P(\\text{Continues}) \= 0.5$.  
* If you **Use Cream**: $P(\\text{Better}) \= 0.85$, $P(\\text{Continues}) \= 0.15$.

**The Calculation:**

1. **EU(Use Cream):** $(0.85 \\times \-20) \+ (0.15 \\times \-120) \= \-17 \+ \-18 \= \\mathbf{-35}$.  
2. **EU(Do Nothing):** $(0.5 \\times 0\) \+ (0.5 \\times \-100) \= 0 \+ \-50 \= \\mathbf{-50}$.

**The Decision:** Since $-35 \> \-50$ (losing $$35$ is better than losing $$50$), you should **Use Cream**.

**Philosophical Note:** Notice that **Dominance Reasoning** would tell you *not* to use the cream. In the "Rash Better" state, doing nothing costs $$0$ (Cream costs $$20$). In the "Rash Continues" state, doing nothing costs $$100$ (Cream costs $$120$). Dominance forbids the cream. MEU permits it because it accounts for how the action *changes the probabilities*of the states.

## **III. Sensitivity to Risk and Magnitude (Weatherson)**

Weatherson illustrates that MEU is superior to Maximin because it is sensitive to changes in the **magnitude** of the stakes.

### **Example 2: The Airline Choice**

*Context:* Cheap Airline vs. Reliable Airline. Reliable is safer/better but costs more.

**Scenario A (High Risk):**

* $P(\\text{Good Weather}) \= 0.8$; $P(\\text{Bad Weather}) \= 0.2$.  
* Outcomes: Cheap Airline pays 10 (Good) or \-20 (Bad). Reliable pays 6 (Good) or 5 (Bad).  
* **EU(Cheap):** $(0.8 \\times 10\) \+ (0.2 \\times \-20) \= 8 \- 4 \= \\mathbf{4}$.  
* **EU(Reliable):** $(0.8 \\times 6\) \+ (0.2 \\times 5\) \= 4.8 \+ 1 \= \\mathbf{5.8}$.  
* *Result:* Choose **Reliable**. The risk of the negative outcome (-20) outweighs the potential gain.

**Scenario B (Lower Risk):**

* Change the probability: $P(\\text{Bad Weather})$ drops to 0.01.  
* **EU(Cheap):** $(0.99 \\times 10\) \+ (0.01 \\times \-20) \= 9.9 \- 0.2 \= \\mathbf{9.7}$.  
* **EU(Reliable):** $(0.99 \\times 6\) \+ (0.01 \\times 5\) \= 5.94 \+ 0.05 \= \\mathbf{5.99}$.  
* *Result:* Choose **Cheap**. Maximin would still demand Reliable (because \-20 is the worst floor), but MEU allows the low probability to render the risk acceptable.

## **IV. Normative Structural Features**

Why should a philosopher accept MEU? Weatherson argues that MEU satisfies logical properties that rules like Minimax Regret failed.

### **1\. Transitivity**

If $EU(A) \> EU(B)$ and $EU(B) \> EU(C)$, it is mathematically guaranteed that $EU(A) \> EU(C)$ because the values are real numbers, which are transitive. This ensures the agent never falls into a cycle of irrational preferences.

Here is the "Money Pump" addition for your Week 4 lecture notes. This argument provides the normative justification for **Transitivity**, a structural feature required for Expected Utility Theory to function.

You can insert this section into **Part IV (Normative Structural Features)** or use it as a standalone **Chalk Talk**.

---

### **The Money Pump Argument (Justifying Transitivity)**

**Source:** Baumgaertner, Ch. 3.2–3.3.

**The Concept:** Why *must* a rational agent have transitive preferences ($A \> B$ and $B \> C$ implies $A \> C$)? The **Money Pump** is a pragmatic argument showing that agents with intransitive (cyclical) preferences are vulnerable to exploitation. They can be forced to pay money to return to their original starting position, a clear violation of instrumental rationality.

**The Scenario (The Ice Cream Cycle):** Imagine a student, John, has intransitive preferences regarding ice cream flavors:

1. He prefers **Strawberry** over **Chocolate** ($S \\succ C$).  
2. He prefers **Chocolate** over **Vanilla** ($C \\succ V$).  
3. But, violating transitivity, he prefers **Vanilla** over **Strawberry** ($V \\succ S$).

**The "Pump" Mechanism:** We can construct a sequence of trades that John will accept because each trade seems to improve his situation based on his preferences.

* **Step 1:** John starts with **Vanilla**. You offer him **Chocolate** for a small fee (e.g., 1 cent). Since he prefers Chocolate ($C \\succ V$), he accepts.  
  * *State:* John has Chocolate and is down 1 cent.  
* **Step 2:** You offer him **Strawberry** for another 1 cent. Since he prefers Strawberry ($S \\succ C$), he accepts.  
  * *State:* John has Strawberry and is down 2 cents.  
* **Step 3:** You offer him **Vanilla** for 1 cent. Because his preferences are cyclical ($V \\succ S$), he accepts this trade as well.  
  * *Result:* John is back where he started (holding Vanilla), but he has lost 3 cents.

**The Normative Lesson:** This cycle can be repeated indefinitely, "pumping" all of John's money until he is bankrupt. A rational agent (like "Sally" in the text) avoids this by having transitive preferences ($S \\succ V$), which breaks the cycle and prevents the final disadvantageous trade. This proves that for a utility function to be useful in decision making, it must preclude cyclical rankings.

### **The "Money Pump" Diagram**

**Scenario:** A student draws a circle on the board representing three options: $A$, $B$, and $C$. **Task:**

1. **Draw the Arrows:** Draw arrows indicating a cycle: $A \\to B \\to C \\to A$ (where $\\to$ means "is preferred to").  
2. **The Arbitrage:** Assign a value of $+$10$ to the preference difference.  
   * "I will pay $$1$ to swap $C$ for $A$."  
   * "I will pay $$1$ to swap $A$ for $B$."  
   * "I will pay $$1$ to swap $B$ for $C$."  
3. **The Calculation:** Show that after three swaps, the agent has the exact same item they started with but has lost $$3$.  
4. **Discussion:** Does the agent simply stop trading when they see what is happening? Baumgaertner argues that simply "foreseeing" the pump is a poor defense; the agent acknowledges the bad consequence but fails to provide a rational structure to resolve the inconsistency. The burden is on the agent to structure their preferences so the pump is impossible.

### **2\. Independence of Irrelevant Alternatives (IIA)**

Recall Week 2: Minimax Regret failed because introducing a third option (the Picnic) changed the preference between Baseball and Movies.

* **MEU satisfies IIA.** The Expected Utility of Option A is calculated using *only* the probabilities and utilities associated with A.  
* If $EU(A) \= 10$ and $EU(B) \= 8$, adding Option C (with $EU=5$ or $EU=15$) does not change the fact that $10 \> 8$. The preference between A and B remains stable regardless of the menu.

### **3\. Respect for Dominance**

If Option A strongly dominates Option B (A provides more utility in *every* state), MEU will always choose A.

* *Proof:* If $U(A|S\_i) \> U(B|S\_i)$ for all states, then the weighted sum for A must be higher than the weighted sum for B.

## **V. Infinite Utility: Pascal's Wager (Baumgaertner)**

What happens if we plug an infinite value into the formula?

* **Outcomes:** Believe (Finite cost $-c$ if No God; $+\\infty$ if God). Disbelieve (Finite gain $+c$ if No God; $-\\infty$ if God).  
* **Calculation:** Even if $P(\\text{God})$ is miniscule (e.g., $0.000001$), the calculation is:  
  * $EU(\\text{Believe}) \= (0.000001 \\times \\infty) \+ (0.999999 \\times \-c) \= \\infty$.  
* **The Washing Out Effect:** Infinite utility "washes out" the probabilities. It makes rationality insensitive to evidence. As long as the probability is non-zero, you must wager for infinity.

---

## Problems

### **Type 1: Drill Exercises (The Mechanics)**

*These problems focus on the application of the MEU formula (P \\times U) and the conversion of ordinal preferences into cardinal utilities.*

**1\. The Airline Dilemma (Calculating EU and Risk)** *Source: Weatherson \[164–167\]* You must choose between a "Cheap Airline" and a "Reliable Airline."

* **Utilities:**  
  * Cheap/Good Weather: \+10  
  * Cheap/Bad Weather: \-20 (Outcomes include lost luggage/delays)  
  * Reliable/Good Weather: \+6  
  * Reliable/Bad Weather: \+5  
* **Probabilities:** The probability of Bad Weather is 20% (0.2).

**Tasks:**

1. **Calculate:** Determine the Expected Utility for both airlines. Which should you choose?  
2. **The Shift:** Suppose the probability of Bad Weather drops to 1% (0.01). Recalculate the EU. Does the recommendation change?  
3. **Analysis:** Explain why a **Maximin** strategist would refuse to switch their choice even when the probability of bad weather drops to 1%, whereas the **MEU** strategist is sensitive to this change.

**2\. The Finite Wager (Algebraic Thresholds)** *Source: Baumgaertner \[735–737\]* Consider a "Finite" Pascal’s Wager where the utility of Heaven is not infinite, just very high.

* **Utilities:**  
  * U( Believe | God) \= 1,000,000 (Heaven)  
  * U( Believe | No God) \= \-100 (Cost of piety)  
  * U( Disbelieve | God) \= \-1,000,000 (Hell)  
  * U( Disbelieve | No God) \= \+100 (Fun of sin)  
* **Task:** Solve for p. How low must the probability of God's existence (P(G)=p) be for a rational agent to choose **Disbelieve**?  
  * *Hint:* Set EU(Believe) \< EU(Disbelieve) and solve the inequality for p.

---

### **Type 2: "What-If" Exercises (Conceptual Variations)**

*These problems ask you to manipulate the structural assumptions of the theory, specifically regarding the independence of states and acts.*

**3\. What If: The Smoking Gene (Causal vs. Evidential)** *Source: Weatherson \[304–308\]* Standard decision theory assumes states are independent of acts. But suppose a genetic defect constitutes a **common cause** that predisposes people to both *smoke* and *get cancer*. Smoking does not *cause* cancer, but it is highly correlated with it.

* **Utilities:**  
  * Smoke \+ No Cancer \= 6  
  * Smoke \+ Cancer \= 1  
  * Don't Smoke \+ No Cancer \= 5  
  * Don't Smoke \+ Cancer \= 0  
* **Probabilities (Correlated):**  
  * P(Cancer | Smoke) \= 0.8  
  * P(Cancer | Don't Smoke) \= 0.2

**Tasks:**

1. **The Evidential Calculation:** Calculate the Expected Utility using the conditional probabilities provided above. What does the theory recommend?   
2. **The Causal Calculation:** Now assume the "State" (having the gene/getting cancer) is fixed and causally independent of the act. If you *do* have the gene, you prefer Smoking (1 \> 0). If you *don't* have the gene, you prefer Smoking (6 \> 5). What does **Dominance** reasoning recommend?   
3. **Discussion:** The Evidential calculation recommends "managing the news" (avoiding the bad news that you have the gene) rather than managing the outcome. Why might a Causal Decision Theorist consider this irrational?.

**4\. What If: The Psychopath Button** *Source: Baumgaertner* Paul is debating whether to press a button that kills all psychopaths.

* **Beliefs:** Paul believes that only a psychopath would be willing to press such a button.  
* **Desires:** Paul strongly prefers living in a world without psychopaths, but he very strongly prefers *not dying* himself.

**Tasks:**

1. **The Matrix:** Draw the decision matrix. (States: Paul is a Psychopath / Paul is Not).  
2. **The Paradox:** Explain why a Causal Decision Theorist (who treats their own psychopathy as a pre-existing state independent of the button press) might press the button, whereas an Evidential Decision Theorist (who views the button press as evidence of their own psychopathy) would not.

---

### **Type 3: Puzzle Exercises (Paradoxes)**

*These problems introduce scenarios where MEU seems to fail or lead to contradictions, setting up future discussions on refining utility functions.*

**5\. The Allais Paradox (Violating the Sure Thing Principle)** *Source: Weatherson \[189–191\]; Baumgaertner* You are drawing one ball from an urn containing 100 balls: 1 is Ticket \#1, 10 are Tickets \#2-11, and 89 are Tickets \#12-100.

**Part A: Choice 1**

* **Gamble 1:** Receive $1M for sure (Tickets 1–100).  
* **Gamble 2:** Receive $5M (Tickets 2–11), $1M (Tickets 12–100), or $0 (Ticket 1).  
* *Which Gamble would you choose?*

**Part B: Choice 2**

* **Gamble 3:** Receive $1M (Tickets 2–11) or $0 (Tickets 1, 12–100).  
* **Gamble 4:** Receive $5M (Tickets 2–11) or $0 (Tickets 1, 12–100).  
* *Which Gamble would you choose?*

**The Puzzle:**

1. **The Calculation:** Show algebraically that if you prefer 1 \> 2, you *must* prefer 3 \> 4 according to Expected Utility Theory. (Hint: The payout for Tickets 12–100 is the same in G1/G2 and G3/G4).  
2. **The Diagnosis:** This violates the **Sure Thing Principle** (or Independence of Irrelevant Alternatives). Explain why intuitive preferences violate the linear weighting of probability \[782–784\].

**6\. The St. Petersburg Paradox (Bounded Utility)** *Source: Baumgaertner \[788–792\]; Weatherson* A fair coin is tossed until it lands Heads. The payoff is 2^n, where n is the number of tosses.

* **Tasks:**  
  1. **The Trap:** Calculate the Expected Utility. Show why the sum is $1 \+ 1 \+ 1 \+ … \= \\infinity.  
  2. **The Solution:** Introduce a **Upper Limit (Hedonic Plateau)** to the utility function. Assume the utility of money caps at L (e.g., the GDP of the earth). Explain how this resolves the paradox by making the series converge to a finite sum \[792–794\].

