# W2 Simple Decision Strategies

---

# **Week 2 Lecture Notes: Decision Under Ignorance**

**Topic:** Maximin, Maximax, and Minimax Regret **Primary Text:** Weatherson, Ch. 2.3–2.6; Baumgaertner, Ch. 2 (and relevant sections of Ch. 4).

## **I. Introduction: Beyond Dominance**

Last week, we discussed the **Dominance Principle**: if Option A is better than Option B in every possible state, choose A. However, dominance is silent in most interesting decision problems because choices often involve trade-offs.

This week covers **Decisions Under Ignorance** (or Uncertainty, distinct from Risk). These are cases where we know the possible states and outcomes, but we **cannot** assign probabilities to the states. Without probabilities, we cannot calculate Expected Utility. We must rely on structural rules based on ranking and cardinal values.

## **II. Simple Ranking Rules (Ordinal Utility)**

When we only have **ordinal utilities** (a ranking of outcomes from best to worst, without specific values), we rely on rules that reflect the agent's "risk personality."

### **A. Maximax (The Optimist’s Rule)**

* **The Rule:** Identify the *best* possible outcome for every option. Choose the option with the highest "best" outcome. "Maximise the maximum".  
* **Philosophy:** This is an aggressive, risk-seeking strategy.  
* **Critique:** It ignores the "floor" (the worst-case scenario).  
  * *Example:* Weatherson notes that on Wall St., this rule justifies buying the riskiest derivatives possible because they *might* have the highest payout, ignoring the catastrophic downside.  
  * *Baumgaertner Expansion:* Consider the "Exam" scenario.  
    * **Options:** Party vs. Study.  
    * **States:** Difficult Exam vs. Easy Exam.  
    * If the student values the combination of "Party \+ Easy Exam" (getting a B while having fun) as the absolute highest utility (4), Maximax dictates they **Party**, even if "Party \+ Difficult Exam" leads to failure.

### **B. Maximin (The Pessimist’s Rule)**

* **The Rule:** Identify the *worst* possible outcome for every option. Choose the option where the worst outcome is the least bad. "Maximise the minimum".  
* **Philosophy:** This is a risk-averse strategy. It assumes the world is malevolent or that safety is paramount.  
* **The Football/Paper Example (Weatherson):**  
  * *Scenario:* Watch Football vs. Work on Paper.  
  * *States:* Team Wins vs. Team Loses.  
  * *Analysis:* If you Watch and they Lose, you are miserable (1). If you Work and they Lose, you are merely bored (2).  
  * *Result:* Maximin looks at the "floor" of each act. The floor for Working (2) is higher than the floor for Watching (1). Therefore, **Work**.  
* **Critique:** It ignores the "ceiling" (the potential upside). A Maximin agent will never buy a lottery ticket, no matter the jackpot size, because the loss of $1 (the floor) is worse than the status quo $0.

## **III. The Shift to Cardinal Utility**

Ordinal rules (Maximin/Maximax) are blind to the **magnitude** of differences.

* *Weatherson’s Airline Example:* Imagine choosing between a Cheap Airline and a Reliable Airline.  
  * *Outcomes:* Cheap/Good Weather (Best), Reliable/Good Weather (2nd), Reliable/Bad Weather (3rd), Cheap/Bad Weather (Worst).  
  * *The Problem:* Ordinal ranking hides the stakes.  
    * **Scenario A:** The "Worst" outcome is luggage arriving a day late.  
    * **Scenario B:** The "Worst" outcome is a plane crash.  
  * *Lesson:* A rational decision requires knowing *how much* worse the worst case is. This requires **Cardinal Utility** (numbers representing magnitude).

## **IV. Minimax Regret**

This is the most philosophically complex rule for this week. It requires cardinal utilities.

### **A. The Concept of Regret**

Regret is defined comparatively within a specific state of the world. It is the difference between the utility you *got* and the utility you *could have had* if you had known the state of the world beforehand.

* **Formula:** $Regret(Act, State) \= Max(State) \- Utility(Act, State)$

### **B. The Rule**

**Minimax Regret:** Calculate the maximum possible regret for each option, then choose the option with the lowest maximum regret.

### **C. Expanded Example: The Sunday Afternoon (Weatherson)**

Let's analyze the choice between Picnic, Baseball, and Movies across three weather states.

**1\. The Utility Matrix (Cardinal Utils)**

|  | Sunny | Light Rain | Thunderstorm |
| ----- | ----- | ----- | ----- |
| **Picnic** | 20 | 5 | 0 |
| **Baseball** | 15 | 2 | 6 |
| **Movies** | 8 | 10 | 9 |

**2\. Calculating the Regret Matrix** To find the regret, look at each *column* (State) and find the best outcome (the anchor). Subtract the actual cell value from that anchor.

* *Sunny:* Best is Picnic (20).  
  * Regret for Picnic: $20 \- 20 \= 0$  
  * Regret for Baseball: $20 \- 15 \= 5$  
  * Regret for Movies: $20 \- 8 \= 12$  
* *Light Rain:* Best is Movies (10).  
  * Regret for Picnic: $10 \- 5 \= 5$  
  * Regret for Baseball: $10 \- 2 \= 8$  
  * Regret for Movies: $10 \- 10 \= 0$  
* *Thunderstorm:* Best is Movies (9).  
  * Regret for Picnic: $9 \- 0 \= 9$  
  * Regret for Baseball: $9 \- 6 \= 3$  
  * Regret for Movies: $9 \- 9 \= 0$

**3\. The Final Regret Table**

|  | Sunny | Light Rain | Thunderstorm | Max Regret |
| ----- | ----- | ----- | ----- | ----- |
| **Picnic** | 0 | 5 | 9 | **9** |
| **Baseball** | 5 | 8 | 3 | **8** |
| **Movies** | 12 | 0 | 0 | **12** |

**Decision:** We choose **Baseball**, because its maximum regret (8) is the lowest of the set {9, 8, 12}.

## **V. The Philosophical Crux: Violation of IIA**

This is the critical philosophical payoff for the seminar. Minimax Regret violates the **Irrelevance of Independent Alternatives (IIA)**.

### **A. Definition of IIA**

If option $C$ is chosen from a set of options $S$, then $C$ should still be chosen from any subset of $S$ that contains $C$.

* *Intuition:* If I prefer Baseball over Movies when a Picnic is an option, I should still prefer Baseball over Movies if the Picnic is cancelled.

### **B. The Violation (The "Menu Change")**

Using the example above, imagine we discover we have no food, so the **Picnic** is no longer an option. We remove the Picnic row.

**New Utility Matrix (Picnic Removed):**

|  | Sunny | Light Rain | Thunderstorm |
| ----- | ----- | ----- | ----- |
| **Baseball** | 15 | 2 | 6 |
| **Movies** | 8 | 10 | 9 |

**New Regret Calculation:** Crucially, the "best" option in the *Sunny* column changes. It used to be Picnic (20). Now it is Baseball (15). This changes the regret calculation for Movies.

* *Sunny:* Best is Baseball (15).  
  * Regret for Baseball: 0  
  * Regret for Movies: $15 \- 8 \= 7$ (Note: This dropped from 12\!)  
* *Other columns remain the same* (Movies was already the best).

**New Regret Table:**

|  | Sunny | Light Rain | Thunderstorm | Max Regret |
| ----- | ----- | ----- | ----- | ----- |
| **Baseball** | 0 | 8 | 3 | **8** |
| **Movies** | 7 | 0 | 0 | **7** |

**The Reversal:**

* With Picnic: We chose **Baseball** (Max regret 8 vs 12).  
* Without Picnic: We choose **Movies** (Max regret 7 vs 8).

### **C. Discussion Point**

The existence of the Picnic—an option we didn't even choose—was the only reason we preferred Baseball. When the Picnic was removed, the "fear" of missing out on the Picnic (Regret 12 for Movies in Sunny weather) vanished. This makes Minimax Regret a **context-dependent** rule. It suggests our rationality depends on the menu, not just the pairwise comparison of items.

---

# Problems

## **Drill**

**1\. The "Call Family" Dilemma (Baumgaertner Expansion)**

Consider the following decision matrix.

|  | Hard exam | Challenging | Easy exam |
| :---- | :---- | :---- | :---- |
| Party\! | 1 | 6 | 12 |
| Study\! | 10 | 5 | 6 |
| Call family | 3 | 4 | 5 |

* **What does** Maximin recommend?  
* What does Maximax recommend?  
* What does Dominance Reasoning recommend? (And compare weak vs strong versions.)  
* What does Minimax Regret recommend?  
* Now remove the “Party\!” option. Does Minimax Regret change its recommendation?

**2\. Henry V (Weatherson)**

In his play Henry V, Shakespeare gives the title character the following little speech. The  
context is that the English are about to go to battle with the French at Agincourt, and they  
are heavily outnumbered. The king’s cousin Westmoreland has said that he wishes they had  
more troops, and Henry strongly disagrees.  
What’s he that wishes so?  
My cousin Westmoreland? No, my fair cousin;  
If we are marked to die, we are enough  
To do our country loss; and if to live,  
The fewer men, the greater share of honor.  
God’s will\! I pray thee, wish not one man more.  
Is the decision principle Henry is using here (a) dominance, (b) maximin, (c) maximax or  
(d) minimax regret? Is his argument persuasive?

**3\. Newcomb’s Problem**

P17 of Baumgaertner presents *Newcomb’s Problem*. For convenience, the table is copied below.

|  | AI predicts two box | AI predicts one box |
| :---- | :---- | :---- |
| One box (just box A) | $0 | $1,000,000 |
| Two box (both A and B) | $1,000 | $1,001,000 |

* Are you a “one-boxer” or a “two-boxer”?  
* Explain your reasoning.  
* What, if any, principles does this decision problem violate? (Hint, can you articulate the difference between *Causal Decision Theory* and *Evidential Decision Theory*?)

## What-If

**1\. The Decoy Effect**

* What is the "Decoy Effect" in marketing (e.g., Small vs. Large popcorn, then introducing a Medium)? (Hint, see Baumgaertner)  
* What does this psychological phenomenon have to do with the normative failure of Minimax Regret regarding IIA?   
* Is Minimax Regret simply formalizing human irrationality (like the Decoy Effect), or is it a distinct logical failure?

**2\. Picnic Revisited**

Fill in the decision matrix of the “picnic example” with your own utilities values:

|  | Sunny | Light Rain | Thunderstorm |
| ----- | ----- | ----- | ----- |
| **Picnic** |  |  |  |
| **Baseball** |  |  |  |
| **Movies** |  |  |  |

* Creating a regret table, calculate what the Max Regret would be for you.  
* Now check: does your decision matrix violate IIA?  
  * If so, create a decision matrix such that applying MiniMax Regret to it would not be a particular violation of IIA. (Note, just because this isn’t a counterexample to IIA doesn’t mean there are no counterexamples to IIA, as illustrated in class.)

## Puzzle

**1\. The Interrupted Game**

Two players are playing a best-of-5 game of chance (flipping a coin, Rock-Paper-Scissors, etc). The winner will get $100. However, their game is stopped early and the score is 2-1. 

* Based on the decision strategies discussed so far, how should the pot be split?  
* How *do you think* the pot should be split?