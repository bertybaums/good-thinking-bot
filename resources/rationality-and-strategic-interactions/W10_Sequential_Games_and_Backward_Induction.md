# W10 Sequential Games and Backward Induction — The Paradox of Rational Foresight

- Time enters the game: moves are made in sequence, not simultaneously
- Backward induction: reason from the end to the beginning
- Subgame perfection: equilibria that survive scrutiny at every decision point
- The Centipede Game: backward induction recommends defection — but intuition screams cooperation
- Common knowledge of rationality: the assumption that drives the paradox
- Is rationality self-defeating again? Or is the problem with the assumption, not the reasoning?
- Commitment, threats, and promises: the strategic value of binding yourself

---

## Lecture Part 1: From Simultaneous to Sequential Games

### I. The Bridge from Coordination to Sequence

**1. What We've Studied So Far**

Write on the board:

| Week | Game Type | Key Feature |
|---|---|---|
| W8 | Prisoner's Dilemma | Simultaneous moves, one bad equilibrium |
| W9 | Coordination Games | Simultaneous moves, multiple equilibria |

In both cases, players chose **simultaneously** — without knowing what the other had done.

**2. What Changes with Sequence**

Today we add **time**: players move in sequence, observing (at least some of) the previous moves.

| Simultaneous Games | Sequential Games |
|---|---|
| Normal form (matrix) | Extensive form (tree) |
| Nash equilibrium | Subgame perfect equilibrium |
| Strategic uncertainty | Strategic commitment |
| "What will they do?" | "What will they do *given what I did*?" |

The key insight: **Moving second is an advantage** — you know what the first mover did. But sometimes **moving first is an advantage** — you can commit to a strategy and force the second mover to respond.

**3. Today's Agenda**

We will:
1. Learn the extensive form (game trees)
2. Master backward induction (the fundamental solution concept)
3. Study subgame perfection (refining Nash equilibrium)
4. Encounter the Centipede Game paradox (the most challenging puzzle in game theory)
5. Discuss common knowledge of rationality (the assumption that drives the paradox)

---

### II. Extensive Form Games — The Game Tree

**1. The Structure of a Game Tree**

Draw on the board:

```
        Player 1
        /      \
       A        B
      /          \
   Player 2     Player 2
   /    \       /    \
  C      D     E      F
 / \    / \   / \    / \
2,2  0,3 3,0  1,1  4,4  0,0
```

Explain the components:
- **Nodes**: Decision points (labeled by who moves)
- **Branches**: Available actions
- **Terminal nodes**: Outcomes with payoffs (Player 1, Player 2)
- **Information sets**: What each player knows when they move (if dashed lines connect nodes, the player can't distinguish them — but we'll start with **perfect information**, where every node is distinct)

**2. A Simple Example: The Entry Game**

Draw the tree:

```
            Incumbent
            /        \
      Accommodate    Fight
         /              \
      2, 2            0, 0
```

Wait — that's not right. The Entrant moves first:

```
            Entrant
            /      \
        Enter      Stay Out
         /            \
    Incumbent         (1, 3)
    /        \
Accommodate  Fight
   /          \
(2, 2)       (0, 0)
```

*Payoffs:* (Entrant, Incumbent)
- If Entrant stays out: (1, 3) — incumbent keeps monopoly
- If Entrant enters and Incumbent accommodates: (2, 2) — shared market
- If Entrant enters and Incumbent fights: (0, 0) — price war, both lose

**3. Finding the Solution: Backward Induction**

Work through the tree from the end:

1. **At the Incumbent's decision node:**
   - Accommodate → 2
   - Fight → 0
   - **Incumbent chooses Accommodate** (2 > 0)

2. **At the Entrant's decision node:**
   - Enter → leads to (2, 2), so Entrant gets 2
   - Stay Out → Entrant gets 1
   - **Entrant chooses Enter** (2 > 1)

3. **Solution:** (Enter, Accommodate) with payoffs (2, 2)

Write on the board:

> **Backward Induction:** Start at the terminal nodes and work backward. At each node, assume the player will choose the action that maximizes their payoff. Replace the subtree with the resulting payoff. Continue until you reach the root.

**4. Why Not (Enter, Fight)?**

Ask: *Isn't (Enter, Fight) a Nash equilibrium?* Let's check:
- If Entrant enters, Incumbent gets 0 from Fight, 2 from Accommodate. So Fight is not a best response.
- Therefore (Enter, Fight) is **not** a Nash equilibrium.

But what about (Stay Out, Fight)?
- If Entrant stays out, Incumbent never moves — so Fight is never "tested."
- If Incumbent *would* fight (if called upon), then Entrant's best response is Stay Out (1 > 0).
- So (Stay Out, Fight) **is** a Nash equilibrium.

But: Is it **credible**? If Entrant *did* enter, would Incumbent actually fight? No — because Accommodate dominates Fight at that node.

This motivates a refinement:

---

### III. Subgame Perfect Equilibrium

**1. The Problem with Nash Equilibrium**

In sequential games, some Nash equilibria rely on **non-credible threats** — threats that would not be carried out if called upon.

In (Stay Out, Fight):
- The threat to Fight is not credible.
- If Entrant enters, Incumbent would *not* fight (2 > 0).
- So the threat is "empty talk."

**2. Subgame Perfection (Selten, 1965)**

Write on the board:

> **Subgame Perfect Equilibrium (SPE):** A strategy profile is an SPE if it is a Nash equilibrium in every **subgame** — i.e., at every decision node, the prescribed action is optimal given what comes after.

In other words: SPE requires that players' strategies are optimal **at every node**, not just on the equilibrium path.

**3. The Relationship to Backward Induction**

Key fact:

> **In finite games of perfect information, backward induction always yields a subgame perfect equilibrium.**

Backward induction is the **algorithm** for finding SPE.

**4. Another Example: The Ultimatum Game**

Draw the tree:

```
            Proposer
               |
          Offer x (0 to 10)
               |
            Responder
           /         \
       Accept       Reject
        /             \
    (10-x, x)       (0, 0)
```

*Rules:* Proposer offers x to Responder (from $10). Responder accepts or rejects. If accept, money is split as proposed. If reject, both get nothing.

*Backward induction:*
1. **Responder's decision:** For any x > 0, Accept gives x, Reject gives 0. So Responder should Accept any x > 0. (If x = 0, indifferent — assume Accept.)
2. **Proposer's decision:** Knowing Responder will accept any x > 0, Proposer should offer x = 0 (or x = 1, the smallest positive amount).

*Prediction:* Proposer offers 0 (or 1), Responder accepts.

*Empirical reality:* Responders often reject low offers (below 3-4). Proposers often offer 4-5.

This is a **behavioral anomaly** — we'll study it more in Week 13. For now, note:

> Backward induction assumes players are rational and will not leave money on the table. Real humans sometimes do.

---

### IV. First-Mover vs. Second-Mover Advantage

**1. When Moving First Helps**

Consider this game:

```
            Player 1
            /      \
           A        B
          /          \
      Player 2     Player 2
      /    \       /    \
     C      D     E      F
    / \    / \   / \    / \
   3,3  0,2 2,0  1,1  4,4  0,0
```

Wait — let me simplify. Consider:

```
            P1
           /  \
          U    D
         /      \
       P2        P2
      /  \      /  \
     L    R    L    R
    / \  / \  / \  / \
   2,2 0,3 3,0 1,1 5,5 0,0
```

Actually, let me use a cleaner example:

**Game A (First-Mover Advantage):**
```
            P1
           /  \
          A    B
         /      \
       P2        P2
      /  \      /  \
     C    D    E    F
    3,3  0,2  2,0  1,1
```

Backward induction:
- At left P2 node: C (3) > D (2) → P2 chooses C
- At right P2 node: E (2) > F (1) → P2 chooses E
- At P1 node: A leads to (3,3), B leads to (2,0) → P1 chooses A
- **Outcome:** (A, C) with (3, 3)

If P2 moved first (choosing between C/D/E/F directly, then P1 responds), the outcome might differ. This shows **first-mover advantage**: P1 can commit to A, forcing P2 to choose C.

**2. When Moving Second Helps**

Consider chess, tic-tac-toe, or any game where seeing the opponent's move is advantageous.

Example:

```
            P1
           /  \
          A    B
         /      \
       P2        P2
      /  \      /  \
     C    D    E    F
    1,4  0,3  2,2  3,5
```

Backward induction:
- At left P2 node: C (4) > D (3) → P2 chooses C
- At right P2 node: F (5) > E (2) → P2 chooses F
- At P1 node: A leads to (1,4), B leads to (3,5) → P1 chooses B
- **Outcome:** (B, F) with (3, 5)

P2 gets 5 — the highest payoff in the game — by moving second and responding optimally.

**3. The General Principle**

Write on the board:

> **First-mover advantage:** When commitment is valuable (you can force the other player to respond on your terms).
>
> **Second-mover advantage:** When flexibility is valuable (you can observe and respond optimally).

---

## Lecture Part 2: The Centipede Game and the Paradox of Backward Induction

### I. The Centipede Game — Setup

**1. The Game**

Draw the tree (simplified to 4 decision nodes):

```
    P1     P2     P1     P2
    / \    / \    / \    / \
   D   d  D   d  D   d  D   d
  /     \/     \/     \/     \
 1,1   0,3  2,2  1,4  3,3  2,5  4,4
```

*Rules:*
- Two players alternate moves.
- At each node, a player can **Stop (D)** or **Continue (d)**.
- If Stop: the game ends, payoffs are as shown.
- If Continue: the game proceeds to the next node.
- At the final node, if P2 continues, payoffs are (4, 4).

*Key feature:* At each node, stopping gives the current player a slightly higher immediate payoff than the previous stop — but continuing would give *both* players more if the game reaches the end.

**2. Backward Induction Analysis**

Work through from the end:

**Node 4 (P2's turn):**
- Stop (D): P2 gets 5
- Continue (d): P2 gets 4
- **P2 chooses Stop** (5 > 4)

**Node 3 (P1's turn):**
- If P1 stops: P1 gets 3
- If P1 continues: leads to Node 4, where P2 stops → P1 gets 2
- **P1 chooses Stop** (3 > 2)

**Node 2 (P2's turn):**
- If P2 stops: P2 gets 3
- If P2 continues: leads to Node 3, where P1 stops → P2 gets 2
- **P2 chooses Stop** (3 > 2)

**Node 1 (P1's turn):**
- If P1 stops: P1 gets 1
- If P1 continues: leads to Node 2, where P2 stops → P1 gets 0
- **P1 chooses Stop** (1 > 0)

**Conclusion:** Backward induction says **P1 stops at Node 1**, and the game ends immediately with payoffs (1, 1).

Write on the board:

> **The Centipede Paradox:** Backward induction predicts immediate defection — but this seems intuitively wrong. Both players would be better off if they continued. And empirically, people *do* continue — often for many rounds.

---

### II. Why Is This a Paradox?

**1. The Intuition Against Backward Induction**

Ask the class: *If you were Player 1 at Node 1, would you stop?*

Expect most students to say "No, I'd continue" — at least for a few rounds.

**Reasons to continue:**
- **Mutual benefit:** If both players continue, they reach (4, 4) — much better than (1, 1).
- **Trust:** If I continue, maybe you'll continue too.
- **Uncertainty about rationality:** If there's any chance my opponent is not perfectly rational (or is altruistic, or follows a different norm), continuing might be optimal.

**2. The Logic of Backward Induction**

But backward induction seems airtight:
- At Node 4, P2 *must* stop (5 > 4 — no reason to continue).
- Knowing this, P1 at Node 3 *must* stop (3 > 2).
- Knowing this, P2 at Node 2 *must* stop (3 > 2).
- Knowing this, P1 at Node 1 *must* stop (1 > 0).

The reasoning is valid — if the premises hold.

**3. The Crucial Assumption: Common Knowledge of Rationality**

Write on the board:

> **Common Knowledge of Rationality (CKR):**
> 1. All players are rational (they maximize expected utility).
> 2. All players know that all players are rational.
> 3. All players know that all players know that all players are rational.
> 4. ... (and so on, ad infinitum)

Backward induction **requires** CKR. Without it, the reasoning breaks down.

**Why?** Suppose P1 thinks: "Maybe P2 is not perfectly rational — maybe P2 will continue out of altruism or confusion." Then P1 might continue at Node 1, hoping to exploit P2's "irrationality."

But if P1 is certain that P2 is rational, and P1 knows that P2 is certain that P1 is rational, and so on — then backward induction is inescapable.

---

### III. Responses to the Paradox

**1. The Orthodox Response: Backward Induction Is Correct**

Some game theorists (e.g., Binmore, Aumann) argue:
- Backward induction is the unique rational solution.
- Intuitions about "cooperation" are mistaken — they rely on wishful thinking or confusion.
- The fact that people *do* cooperate in experiments shows that people are not perfectly rational (or don't have common knowledge of rationality).

**2. The Heterodox Response: Backward Induction Is Flawed**

Others (e.g., Pettit, Sugden) argue:
- Backward induction makes unrealistic assumptions about common knowledge.
- In real situations, players have **some** uncertainty about others' rationality — and this uncertainty makes cooperation rational.
- The "paradox" reveals a problem with the model, not with human intuition.

**3. The "Trembling Hand" Response**

Selten (who introduced subgame perfection) also introduced the idea of a **trembling hand**: players might make mistakes with small probability.

If there's a tiny chance that P2 will "tremble" and continue at Node 4 (even though it's irrational), then P1 might rationally continue at Node 3, and so on.

This shows: **A little uncertainty can unravel the backward induction argument.**

**4. The Epistemic Response**

Recent work in **epistemic game theory** asks: What exactly does "common knowledge of rationality" entail?

Some argue:
- CKR is an impossibly strong assumption.
- Weaker assumptions (e.g., "almost common knowledge") yield different predictions.
- The Centipede Game shows that CKR is not just empirically false — it's conceptually problematic.

---

### IV. Experimental Evidence

**1. What Do People Actually Do?**

McKelvey and Palfrey (1992) ran Centipede Game experiments:
- Very few subjects stopped at Node 1.
- Most subjects continued for several rounds.
- Cooperation rates declined as the end approached (consistent with "limited depth" reasoning).

**2. What Does This Mean?**

Possible interpretations:
- **People are irrational:** They don't understand backward induction.
- **People have incomplete information:** They're uncertain about opponents' rationality or payoffs.
- **People are boundedly rational:** They reason a few steps ahead, not all the way.
- **People have social preferences:** They care about fairness or reciprocity, not just their own payoff.

We'll study these alternatives in Week 13 (Behavioral Game Theory).

---

### V. Commitment, Threats, and Promises

**1. The Strategic Value of Commitment**

Sometimes you can improve your outcome by **limiting your own options**.

Example: In the Entry Game, if Incumbent could **commit** to Fighting (e.g., by signing a contract that penalizes Accommodation), then Entrant would Stay Out, and Incumbent would get 3 instead of 2.

Write on the board:

> **Commitment:** Making a move (or binding yourself) that changes the game in your favor.

**2. Types of Commitment Devices**

| Type | Example |
|---|---|
| **Contracts** | Signing a binding agreement to fight entry |
| **Reputation** | Building a reputation for aggression so others believe your threats |
| **Precommitment** | Odysseus tying himself to the mast (Ulysses contract) |
| **Burning bridges** | Destroying your own retreat so you must fight |
| **Delegation** | Giving decision-making to an agent with different incentives |

**3. Connection to Dennett (Week 7)**

Recall Dennett's discussion of **precommitment** and **conversation-stoppers**. A commitment device is a way of making a threat or promise **credible** — by changing your own incentives so that you *will* follow through.

This is exactly what Dennett described: a rational agent with self-knowledge of her limitations might choose to bind herself to a rule, even though it limits future flexibility.

**4. The Paradox of Commitment**

Write on the board:

> **The Paradox of Commitment:** Sometimes you do better by having *fewer* options, not more.

This seems paradoxical — but it's a direct consequence of strategic interdependence. Your opponent's best response to your committed strategy may be better for you than their best response to your uncommitted strategy.

---

### VI. Philosophical Conclusion: Rationality, Common Knowledge, and Trust

Close by raising the philosophical questions.

**1. Is Common Knowledge of Rationality Desirable?**

The Centipede Game suggests: **No.** If both players have CKR, they get (1, 1). If they have some uncertainty (or some "irrational" trust), they might reach (4, 4).

Ask: *Is ignorance bliss?* Or is there a sense in which CKR is still the "correct" assumption, even if it leads to worse outcomes?

**2. The Value of Irrationality**

This connects to a broader theme:

> Sometimes appearing irrational (or being irrational) is strategically advantageous.

Examples:
- A "crazy" opponent is harder to deter (Nixon's "madman theory" in Vietnam).
- A player who can't back down from a threat is more credible.
- A person with rigid moral rules is more trustworthy.

**3. Bridge to Next Week**

Next week we study **evolutionary game theory** — where players are not rational deliberators but organisms following fixed strategies, and "success" is measured in reproductive fitness, not utility.

This will provide a different perspective on the Centipede Game: perhaps cooperation evolves not because it's rational, but because it's **adaptive**.

---

## Week 10 Problem Set: Sequential Games and Backward Induction

**Topics:** Extensive Form, Backward Induction, Subgame Perfection, Centipede Game, Common Knowledge of Rationality, Commitment.
**Readings:** Osborne Ch. 5-6, Binmore "Game Theory and the Social Contract" (excerpts on backward induction), McKelvey & Palfrey (1992) on Centipede experiments.

---

### Type 1: Drill Exercises

**1. Backward Induction Practice**

For each game tree below, find the subgame perfect equilibrium using backward induction.

**Game A:**
```
        P1
       /  \
      A    B
     /      \
   P2        P2
  /  \      /  \
 C    D    E    F
3,2 1,1  2,3  0,0
```

**Game B:**
```
        P1
       /  \
      A    B
     /      \
   P2        P2
  /  \      /  \
 C    D    E    F
1,4 2,2  3,1  1,3
```

**Game C:**
```
        P1
       /  \
      A    B
     /      \
   P2        (2, 2)
  /  \
 C    D
4,1  0,0
```

*Tasks:*
1. For each game, identify the subgame perfect equilibrium (strategies for each player).
2. What is the outcome (path through the tree)?
3. What are the payoffs?

---

**2. Finding Subgames**

For each game tree, identify all proper subgames (subgames that are not the whole game).

**Game D:**
```
        P1
       /  \
      A    B
     /      \
   P2        P2
  /  \      /  \
 C    D    E    F
/ \  / \  / \  / \
... ... ... ...
```

(Assume each terminal branch leads to distinct payoffs.)

*Tasks:*
1. How many proper subgames does Game D have?
2. Why is the subtree following A a subgame? Why is the subtree following B a subgame?
3. Why is the subtree following "P2's left node" not a subgame if P2 can't distinguish it from the right node? (Hint: think about information sets.)

---

### Type 2: "What-If" Exercises

**3. What If Payoffs Change in the Centipede Game?**

Consider a modified Centipede Game:

```
    P1     P2     P1     P2
    / \    / \    / \    / \
   D   d  D   d  D   d  D   d
  /     \/     \/     \/     \
 2,2   1,4  3,3  2,5  4,4  3,6  5,5
```

*Tasks:*
1. Apply backward induction. What is the predicted outcome?
2. How does this differ from the standard Centipede Game? Why?
3. What if the final payoff were (10, 10) instead of (5, 5)? Would backward induction change?
4. **General question:** What features of the payoff structure make backward induction recommend early stopping vs. continuing?

---

**4. Commitment in the Entry Game**

Recall the Entry Game:

```
            Entrant
            /      \
        Enter      Stay Out
         /            \
    Incumbent         (1, 3)
    /        \
Accommodate  Fight
   /          \
(2, 2)       (0, 0)
```

*Tasks:*
1. What is the subgame perfect equilibrium? (Answer: Enter, Accommodate)
2. Suppose Incumbent can pay a cost of 1 to build a "fighting factory" that makes Fighting more profitable (changing the Fight payoff from 0 to 1). Should Incumbent do it?
3. Suppose Incumbent can sign a contract that penalizes Accommodation by 2 (making Accommodate yield 0 instead of 2). Should Incumbent sign it?
4. **Real-world application:** Companies sometimes build "excess capacity" that they could use to flood the market if a competitor enters. How does this function as a commitment device?

---

### Type 3: Puzzle/Paradox

**5. The Unexpected Hanging Paradox**

A judge tells a prisoner: "You will be hanged on one of the next seven days, and the hanging will be a **surprise** — you will not know the night before that it will happen the next day."

The prisoner reasons:
- "If I'm still alive on day 6, the hanging must be on day 7 — but then it wouldn't be a surprise. So it can't be day 7."
- "If it can't be day 7, and I'm still alive on day 5, it must be day 6 — but then it wouldn't be a surprise. So it can't be day 6."
- (Continuing backward...) "So it can't be any day!"

The prisoner is relieved. But then the hangman comes on day 3 — and the prisoner is genuinely surprised.

*Tasks:*
1. What is the flaw in the prisoner's reasoning?
2. How is this paradox similar to the Centipede Game paradox? (Hint: both involve backward induction and knowledge.)
3. How is it different?
4. **Philosophical question:** Does the Unexpected Hanging show that common knowledge assumptions can lead to false conclusions? Or does it show something else?

---

**6. The Chainstore Paradox (Selten, 1978)**

A chainstore operates in 20 cities. In each city, a potential competitor decides whether to Enter or Stay Out. If a competitor enters, the chainstore can Fight (price war) or Accommodate (share market).

Payoffs per city:
- If competitor stays out: Chainstore gets 5, competitor gets 1.
- If competitor enters and chainstore accommodates: Chainstore gets 2, competitor gets 2.
- If competitor enters and chainstore fights: Chainstore gets 0, competitor gets 0.

The chainstore plays sequentially against 20 competitors, each observing what happened in previous cities.

*Tasks:*
1. Apply backward induction to the 20th (last) competitor. What does the chainstore do? What does the competitor do?
2. Now consider the 19th competitor. Knowing what will happen in round 20, what should the chainstore do in round 19?
3. By induction, what should the chainstore do in round 1?
4. **The paradox:** This says the chainstore should always Accommodate — but intuitively, the chainstore might want to Fight early competitors to build a reputation. Is backward induction wrong here? Or is the intuition wrong?
5. **Connection to Centipede:** How is this similar to the Centipede Game? How is it different?

---

### Type 4: Applied Analysis

**7. Common Knowledge of Rationality — Is It Coherent?**

The Centipede Game paradox relies on **common knowledge of rationality** (CKR). But some philosophers argue that CKR is incoherent or self-defeating.

*Argument:* If P1 stops at Node 1 (as backward induction recommends), P2 never gets to move. But if P2 *did* get to move (i.e., if P1 continued), P2 would have observed something that contradicts CKR (since a rational P1 should have stopped). So P2's beliefs would be inconsistent.

*Tasks:*
1. Reconstruct this argument more formally. Why does P2 observing a move by P1 create a paradox?
2. One response: CKR is an assumption about the **actual** play of the game, not about counterfactuals. Evaluate this response.
3. Another response: Players should use **trembling hand perfection** — assume that any move, even if irrational, has some small probability of occurring. How does this change the analysis?
4. **Philosophical question:** If CKR leads to paradox, should we abandon it? Or should we accept the paradox as a feature of rationality?

---

**8. Precommitment in Politics and Law**

Politicians and legal systems often use commitment devices:
- Central banks are made "independent" to commit to low inflation.
- Constitutions are hard to amend to commit to certain rights.
- "Three strikes" laws commit to harsh sentencing (removing judicial discretion).

*Tasks:*
1. Model one of these as a sequential game. Who are the players? What are the moves? How does the commitment device change the game tree?
2. Why is commitment valuable in each case? Who benefits?
3. What are the risks of commitment? (Hint: What if circumstances change?)
4. **Normative question:** Should democratic governments be able to bind their successors? Is precommitment compatible with democracy?

---

**9. The Ransom Game — A Commitment Problem**

A kidnapper has kidnapped a victim. The victim's family must decide whether to Pay Ransom or Not. If they pay, the kidnapper must decide whether to Release or Kill the victim.

Payoffs (Family, Kidnapper):
- Don't Pay: (0, 0) — victim's fate uncertain, assume (−5, 0)
- Pay, Release: (−10, 5) — family loses money but victim lives
- Pay, Kill: (−20, 0) — family loses money and victim dies, kidnapper gets caught

*Tasks:*
1. Draw the game tree.
2. Find the subgame perfect equilibrium.
3. **The problem:** The family would like to commit to Paying *only if* the kidnapper commits to Releasing — but neither commitment is credible. Why?
4. **Real-world solution:** Governments often have a "no ransom" policy. Is this a commitment device? How does it work?
5. **Ethical question:** Should governments commit to no-ransom policies? Does such a policy save lives (by deterring kidnapping) or cost lives (by reducing the chance of victim release)?

---

**10. Backward Induction and the End of the World**

Consider a "finite horizon" version of climate change negotiation:

- There are 10 rounds of negotiation.
- In each round, countries can Cooperate (reduce emissions) or Defect (pollute).
- Payoffs are as in a repeated Prisoner's Dilemma.
- Everyone knows round 10 is the last round.

*Tasks:*
1. Apply backward induction. What happens in round 10?
2. Given round 10's outcome, what happens in round 9?
3. By induction, what happens in round 1?
4. **The paradox:** This says no cooperation is possible in any round — but we observe some international cooperation even with known deadlines. Why?
5. **Possible resolutions:**
   - Countries are uncertain about when the "real" end is.
   - Countries have incomplete information about each other's preferences.
   - Countries have social preferences (care about fairness, reputation).

   Which resolution is most plausible? Defend your answer.

---

**11. Synthesis: Backward Induction Across Course Themes**

We have now encountered backward induction in several contexts. Synthesize the connections:

*Tasks:*
1. **Connection to Week 7 (Dennett):** Backward induction requires unlimited reasoning depth. Dennett argues that real agents satisfice. Is backward induction a model of maximizing or satisficing? Could a satisficing agent approximate backward induction?
2. **Connection to Week 6 (Prospect Theory):** Backward induction assumes linear utility over payoffs. How would loss aversion affect Centipede Game play? (Hint: losses loom larger — might make early stopping more attractive?)
3. **Connection to Week 8 (PD):** Both PD and Centipede show rationality leading to suboptimal outcomes. Are the two paradoxes structurally similar? Or fundamentally different?
4. **Connection to Week 9 (Convention):** Could a convention (e.g., "continue until the last few rounds") solve the Centipede problem? Why or why not?
5. **Final synthesis:** Rank the following by how "radical" a departure from classical game theory they represent:
   - (a) Trembling hand perfection
   - (b) Bounded rationality (limited-depth reasoning)
   - (c) Social preferences (inequality aversion)
   - (d) Abandoning common knowledge of rationality

---

## Appendix: Instructor Notes

### Suggested In-Class Activities

**1. Live Centipede Game**

Pair students and have them play a 4-round Centipede Game for small stakes (candy, extra credit points). Run multiple rounds with different partners.

Afterward, discuss:
- How many pairs reached the end?
- What reasoning did students use?
- Did experience change behavior?

**2. Ultimatum Game Demonstration**

Pair students: one Proposer, one Responder. Give them $10 (real or hypothetical) to split. Have Proposers make offers, Responders accept or reject.

Collect data on offers and rejection rates. Expect:
- Offers cluster around 4-5.
- Some low offers (below 3) are rejected.

Discuss: Why do responders reject? (Fairness, punishment, emotion.) Why do proposers offer more than the minimum? (Anticipating rejection, fairness, norms.)

**3. Commitment Device Brainstorm**

Ask students to generate examples of commitment devices from:
- Personal life (e.g., workout contracts, website blockers)
- Business (e.g., warranties, money-back guarantees)
- Politics (e.g., term limits, independent central banks)

Discuss: What makes a commitment device effective? When is commitment desirable?

---

### Common Student Misconceptions

1. **"Backward induction is just Nash equilibrium."** No — backward induction yields a *refinement* of Nash equilibrium (subgame perfection). All SPEs are Nash equilibria, but not vice versa.

2. **"The Centipede Game shows backward induction is wrong."** Not necessarily — it shows that the *assumptions* (common knowledge of rationality) may not hold in practice.

3. **"Commitment is always good."** Commitment can backfire if circumstances change or if the commitment is to a bad strategy.

4. **"Second movers always have an advantage."** Not true — it depends on the game structure. Sometimes commitment (moving first) is advantageous.

---

### Connections to Other Course Topics

| Week | Connection |
|---|---|
| W7 (Dennett) | Backward induction assumes unlimited reasoning; Dennett argues for bounded rationality. |
| W8 (PD) | Both PD and Centipede show rationality leading to suboptimal outcomes. |
| W9 (Coordination) | Sequential moves can resolve coordination problems (first mover sets the focal point). |
| W11 (Evolution) | Evolutionary dynamics may favor cooperation in Centipede-like games even without rationality. |
| W13 (Behavioral) | Empirical play in sequential games systematically deviates from backward induction. |

---

## Preview of Next Week

Next week we shift paradigms: **evolutionary game theory**. Instead of rational deliberators, we model organisms following fixed strategies, with "success" measured in reproductive fitness. We'll study:
- Evolutionarily Stable Strategies (ESS)
- The replicator dynamics
- How cooperation can evolve without rationality
- Skyrms's *Evolution of the Social Contract*

This will provide a new perspective on old problems: perhaps the Centipede Game is not a paradox of rationality but a puzzle for evolution.
