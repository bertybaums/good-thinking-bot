# W3 Probability, confidence, belief, and credence

Here are the lecture notes for Week 3\. These notes follow your request to ground the "rules" of probability in the pragmatic necessity of consistency (The Dutch Book Argument) rather than abstract mathematical fiat.

---

# **Week 3 Lecture Notes: Probability and Consistency**

**Topic:** Dutch Books, Axioms of Probability, and Subjective vs. Objective Probability. **Primary Text:** Baumgaertner, Ch. 8; Weatherson, Ch. 4 & 6\.

## **I. Introduction: Measuring Beliefs**

Before we can use probability in decision making, we must understand what it represents. In this course, we often treat probability as **Subjective Probability** (or Credence)—a measure of a person's degree of confidence in a proposition.

But how do we measure an internal mental state like "confidence"? We measure it by **action**: specifically, the willingness to bet.

### **A. The Fair Betting Rate**

Baumgaertner provides a method for quantifying belief. If you are willing to bet on statement $S$, your confidence is revealed by the odds you accept.

* **The Scenario:** Bob believes event $S$ will happen. He accepts a bet where he risks $$2$ to win $$1$ (from Ally).  
* **The Stake:** The total money on the table is $$3$ (Bob's $$2$ \+ Ally's $$1$).  
* **The Calculation:** Bob's "Fair Betting Rate" (his probability) is his Potential Loss divided by the Total Stake.  
  * $Pr(S) \= \\frac{\\text{Loss}}{\\text{Stake}} \= \\frac{2}{3} \\approx 0.67$.

**Key Definition:** A **Fair Bet** is one where the Expected Value (to the agent) is 0\.

* If Bob thought the probability was lower (e.g., 0.10), he would demand a much higher payout (Ally puts in $$9$ for Bob's $$1$) to make the bet fair.

## **II. The Dutch Book Argument (Why be consistent?)**

Why must our beliefs follow the strict rules of mathematics? Why can't I believe there is a 60% chance of Rain and a 60% chance of No Rain? **The Argument:** If your credences violate the axioms of probability, you are vulnerable to a **Dutch Book**—a set of bets that guarantees you will lose money, no matter how the world turns out.

### **A. The Horse Race Example (Baumgaertner)**

Consider a race with four horses. You act as the bookie, accepting bets based on the following "odds" (which imply specific probabilities).

| Horse | Odds (Against) | Implied Prob | You Bet | Payout |
| ----- | ----- | ----- | ----- | ----- |
| Gumption | 1:1 | 0.50 | $$100$ | $$200$ |
| Gallifray | 3:1 | 0.25 | $$50$ | $$200$ |
| Tungsten | 4:1 | 0.20 | $$40$ | $$200$ |
| Shadow | 9:1 | 0.10 | $$20$ | $$200$ |
| **TOTAL** |  | **1.05** | **$$210$** |  |

* **The Trap:** You collected **$$210$** in bets. No matter which horse wins, you only have to pay out **$$200$**. You have guaranteed a $$10$ profit.  
* **The Lesson:** From the gambler's perspective, this implies a failure of rationality. If a gambler held these specific probabilities (summing to 1.05), they would be willing to take the other side of these bets—guaranteeing a loss of $$10$.  
* **Conclusion:** To be rational is (at minimum) to avoid guaranteed loss. Therefore, your probabilities must sum to exactly 1\.

## **III. The Axioms of Probability**

Weatherson and Baumgaertner formalize these consistency requirements into three axioms. A function $Pr$ is a probability function if it satisfies:

### **Axiom 1: Non-Negativity**

* $Pr(A) \\geq 0$.  
* *Intuition:* You cannot have negative confidence. A measure cannot result in a negative quantity.

### **Axiom 2: Normality (Normalisation)**

* The probability of the "Universe" (the set of all possibilities) is 1\.  
* $Pr(A \\lor \\neg A) \= 1$.  
* *Weatherson’s Measure Theory:* Probability is a "normalised measure." Just as the "measure" (population) of NYC is the sum of its boroughs, the probability of the whole logical space is normalized to 1\.  
* *Failure:* The Horse Race example failed this because $1.05 \\neq 1$.

### **Axiom 3: Finite Additivity**

* If $A$ and $B$ are mutually exclusive (inconsistent), then $Pr(A \\lor B) \= Pr(A) \+ Pr(B)$.  
* *Weatherson’s Proof:* Uses truth tables to show that if $A$ and $B$ cannot be true together, the probability of the disjunction is the sum of the parts.

## **IV. Subjective vs. Objective Probability**

Weatherson distinguishes between two concepts that use the same math.

1. **Credences (Subjective):** These are degrees of belief. They are inconsistent across people. (You might think the defendant is guilty; I might think he is innocent). This is the primary focus of decision theory.  
2. **Chances (Objective):** These are facts about the world, independent of what we think (e.g., Quantum mechanics, radioactive decay). The "Chance" of a particle decaying is a physical property, not a mental state.

**The Principal Principle:** How do they relate? Weatherson introduces the **Principal Principle**: If you know the objective Chance of an event is $x$, your subjective Credence should be set to $x$.

* *Example:* If physics says the chance of a coin landing heads is 0.5, a rational agent sets their betting rate to 0.5.

---

## **V. Chalk Talk Ideas**

*Suggestions for student board work to reinforce these concepts.*

### **1\. The "Incoherent Weather Forecaster" (Dutch Book)**

* **Scenario:** A student acts as a forecaster who predicts:  
  * Probability of Rain: 0.6  
  * Probability of No Rain: 0.6  
* **Task:** The student must play the role of a "Bookie" exploiting this incoherence.  
  * **Bet 1:** I pay you $0.60. If it rains, you pay me $1. (Fair by your lights).  
  * **Bet 2:** I pay you $0.60. If it doesn't rain, you pay me $1. (Fair by your lights).  
  * **The Reveal:** Calculate the total intake ($1.20) vs. the total payout (Exactly $1.00, regardless of weather). The forecaster has lost $0.20 for sure.

### **2\. The Logic of Additivity (Weatherson)**

* **Scenario:** Use Weatherson’s logic approach to prove the Addition Rule for non-exclusive events.  
* **Task:** The student draws a Venn Diagram or Truth Table for $Pr(A \\lor B)$.  
* **Challenge:** Show why $Pr(A) \+ Pr(B)$ is wrong if $A$ and $B$ overlap.  
* **Solution:** They must derive: $Pr(A \\lor B) \= Pr(A) \+ Pr(B) \- Pr(A \\land B)$.

### **3\. Calculating the "Fair Price" (Baumgaertner)**

* **Scenario:** You have a ticket that pays $100 if a specific candidate wins an election. You believe the candidate has a 25% chance of winning.  
* **Task:** Use the "General Recipe" for fair betting to calculate the exact dollar amount you should sell the ticket for.  
* **Formula:** $Pr(S) \\times (W \+ L) \= L$ (solving for the stake/price).  
  * *Note:* This requires algebraic manipulation on the board. $0.25 \\times 100 \= $25$.

### **4\. The Principal Principle Violation**

* **Scenario:** A coin is biased. The objective **Chance** of Heads is 0.8.  
* **Task:** A student argues they have a "hunch" and sets their **Credence** at 0.5.  
* **Discussion:** Ask the class if this person is "irrational." (Strictly speaking, they don't violate the probability axioms, so they can't be Dutch Booked in the standard way. They violate the Principal Principle, which is a norm of how to align inner belief with outer evidence).

# Problems

---

### **Part 1: Drill Exercises**

*These problems are designed to ensure you are comfortable converting between degrees of belief and betting behaviors, and applying the basic axioms of probability.*

**1\. The Fair Price (Calculating Credence)** You are considering buying a ticket for a raffle. If you win, you receive $100 (Total Winnings). If you lose, you receive nothing. You are currently indifferent between buying the ticket for $20 and not playing at all.

* **A.** Using the "General Recipe" for fair betting, calculate your subjective probability (credence) that you will win the raffle.  
* **B.** Express this credence as "Odds Against" winning.

**2\. The Incoherent Bookie (Constructing a Dutch Book)** Consider an agent, "Optimistic Oliver," who holds the following credences regarding tomorrow's weather:

* Pr(Rain) \= 0.6  
* Pr(No Rain) \= 0.6

Oliver is willing to take the "fair bets" implied by these probabilities. Construct a **Dutch Book** against Oliver. Show your work by listing:

* **Bet A:** The amount you pay Oliver, and the amount he pays you if it Rains.  
* **Bet B:** The amount you pay Oliver, and the amount he pays you if it does *not* Rain.  
* **Guaranteed Profit:** Calculate your total profit regardless of the weather.

**3\. Axiom Check (Finite Additivity)** Assume A and B are logically disjoint (mutually exclusive) sentences.

* **A.** If Pr(A) \= 0.3 and Pr(B) \= 0.4, what is Pr(A or B)?  
* **B.** Using Weatherson’s breakdown of truth tables and axioms, explain *why* Pr(A) \+ Pr(B) would be the wrong calculation if A and B were *not* mutually exclusive.

---

### **Part 2: "What-If" Exercises**

*These problems test the boundaries of the concepts by introducing variations or conflicts between subjective and objective probability.*

**4\. What If: The Advantageous Bet** In Drill 1, you were indifferent to the ticket at $20.

* **Scenario:** Suppose a friend offers to sell you the same ticket (pays $100 on win) for only $10.  
* **Task:** Calculate your **Expected Value** for this new bet using the probability you derived in Drill 1\. Is this bet "Fair" or "Advantageous" according to Baumgaertner’s definition? Explain why a rational agent would no longer be indifferent.

**5\. What If: The Crystal Ball (The Principal Principle)** Weatherson discusses the "Principal Principle," which states that a rational agent’s credences should align with known objective chances ($Pr(p|Ch(p)=x) \= x$).

* **Scenario:** You are observing a radioactive particle that physics tells you has a 0.5 chance of decaying in the next hour. However, you also possess a magical crystal ball (which you know to be infallible) that shows you a vision of the particle decaying 10 minutes from now.  
* **Question:** Should your credence in the decay be 0.5 (following the objective chance/physics) or 1.0 (following the crystal ball)? Does this violate the Principal Principle, or is the Principal Principle conditional on *admissible* evidence?.

**6\. What If: The Axiom of Normality**

* **Scenario:** Imagine a culture that rejects the Axiom of Normality (Pr(Universe) \= 1). They believe that the probability of (A or \~A) sums to 0.9, representing a general skepticism about logic.  
* **Task:** Explain how you could construct a Dutch Book against a member of this culture using only a single tautology (e.g., "Either it will rain or it won't").

---

### **Part 3: Puzzle Exercise**

*This problem requires synthesising the week's concepts to diagnose a failure of rationality.*

**7\. The "Logic vs. Probability" Puzzle** Consider a voter, Alex, who has the following credences about an upcoming election with two candidates, Jones and Smith.

* A \= "Jones is a corrupt politician."  
* B \= "Jones will win the election."

Alex assigns the following probabilities based on his betting behavior:

* Pr(A) \= 0.7  
* Pr(B) \= 0.7  
* Pr(A and B) \= 0.3

**The Task:**

1. **Diagnose the Incoherence:** Using Weatherson’s discussion of the probability calculus and truth tables, prove that Alex’s probabilities are incoherent. Specifically, verify if his values satisfy the equation: Pr(A) \+ Pr(B) \= Pr(A and B) \+ Pr(A or B)..  
2. **The Dutch Book:** Because Alex is incoherent, he is vulnerable to a Dutch Book. Construct a set of three bets (one on A, one on B, one on ‘A and B’) that guarantees Alex loses money. *Hint: You may need to sell him bets on A and B, but buy a bet on the conjunction (A & B) from him, or vice versa.*

