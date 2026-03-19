# W9 Coordination and Convention — When There Are Too Many Equilibria

- Last week: rationality defeats itself (one bad equilibrium)
- This week: rationality is indeterminate (multiple equilibria, no unique solution)
- The Stag Hunt: cooperation is possible, but requires trust
- Battle of the Sexes: coordination with conflict — we agree we should coordinate, but disagree on how
- Schelling points: focal points that attract attention without communication
- Convention (Lewis): arbitrary, self-perpetuating solutions to recurrent coordination problems
- Language, money, traffic rules — all conventions that solve coordination problems
- The deep question: How do conventions arise without explicit agreement?

---

## Lecture Part 1: From Prisoner's Dilemma to Coordination

### I. The Bridge from Last Week

Begin by contrasting this week's problem with last week's.

**1. Two Kinds of Strategic Problems**

Write on the board:

| **Prisoner's Dilemma (Week 8)** | **Coordination Problems (Week 9)** |
|---|---|
| One equilibrium (D,D) — and it's bad | Multiple equilibria — some good, some bad |
| Individual incentives conflict with collective welfare | Individual incentives *align* with coordination |
| The problem: escape the trap | The problem: find *which* equilibrium to play |
| Solution requires changing incentives or preferences | Solution requires finding focal points or conventions |

The PD is a problem of *conflict*: what's individually rational leads to collective disaster. Coordination problems are problems of *indeterminacy*: there are multiple rational outcomes, and the challenge is selecting one.

**2. Why Coordination Matters**

Ask the class: *What do the following have in common?*
- Driving on the right (or left) side of the road
- Using the word "dog" to refer to dogs
- Meeting someone at "noon at the information booth"
- Using dollar bills as money
- Shaking hands (or bowing) as a greeting

*Answer:* All are **conventions** — arbitrary solutions to coordination problems that persist because everyone expects everyone else to follow them.

**3. Today's Agenda**

We will study three canonical coordination games:
1. **Stag Hunt** — the pure coordination problem (Rousseau's parable)
2. **Battle of the Sexes** — coordination with conflict
3. **Pure Coordination** — no conflict, just the need to match

Then we'll turn to Thomas Schelling's experiments on focal points and David Lewis's theory of convention.

---

### II. The Stag Hunt — Rousseau's Parable

**1. The Story (Tell It First)**

Jean-Jacques Rousseau, in his *Discourse on Inequality* (1755), offered a parable:

> A group of hunters go out to catch a stag. If they all cooperate, they can surround and kill the stag — a large payoff shared among them. But if any hunter defects (chases a hare instead), the stag escapes, and the defector gets a small but certain payoff.

Unlike the PD, there's no dominance: what you should do depends on what you expect the others to do.

**2. The Payoff Matrix (Draw on Board)**

| | **Partner: Stag** | **Partner: Hare** |
|---|---|---|
| **You: Stag** | 5, 5 | 0, 3 |
| **You: Hare** | 3, 0 | 2, 2 |

*Poll the class:* What would you do? (Expect split responses — this is the point.)

**3. Nash Equilibria (Work Through)**

Define **Nash Equilibrium**: A set of strategies where no player can improve their payoff by unilaterally changing their strategy.

Find the equilibria in Stag Hunt:
- **(Stag, Stag)**: If both play Stag, neither wants to switch (5 > 3). **This is a Nash equilibrium.**
- **(Hare, Hare)**: If both play Hare, neither wants to switch (2 > 0). **This is also a Nash equilibrium.**
- **(Stag, Hare)**: You get 0 playing Stag, but could get 2 playing Hare. Not an equilibrium.
- **(Hare, Stag)**: Symmetric — not an equilibrium.

Write on the board:

> **Stag Hunt has two pure-strategy Nash equilibria: (Stag, Stag) and (Hare, Hare).**

**4. The Coordination Problem**

The problem is not that rationality leads to a bad outcome. The problem is that rationality *doesn't tell you which equilibrium to play.*

- If you expect your partner to hunt Stag, you should hunt Stag.
- If you expect your partner to hunt Hare, you should hunt Hare.

Your optimal choice depends on your expectation — which depends on their expectation of you — which depends on your expectation of their expectation...

**5. Payoff Dominance vs. Risk Dominance**

Introduce two important concepts:

| Concept | Definition | In Stag Hunt |
|---|---|---|
| **Payoff-dominant equilibrium** | The equilibrium with the highest payoffs for all players | (Stag, Stag) = (5, 5) |
| **Risk-dominant equilibrium** | The equilibrium that is safest if you're uncertain what the other will do | (Hare, Hare) = guaranteed 2 |

Ask: *Which would you choose?* Expect some students to say "Stag" (optimistic, trusting) and others to say "Hare" (cautious, risk-averse).

**6. The Connection to Prisoner's Dilemma**

Modify the Stag Hunt by lowering the payoff for (Stag, Hare) from 0 to -2:

| | **Stag** | **Hare** |
|---|---|---|
| **Stag** | 5, 5 | -2, 3 |
| **Hare** | 3, -2 | 2, 2 |

Now check: Does Hare dominate?
- If they play Stag: you get 5 (Stag) vs. 3 (Hare) → Stag is better
- If they play Hare: you get -2 (Stag) vs. 2 (Hare) → Hare is better

Still no dominance — but now (Hare, Hare) is even more attractive relative to (Stag, Stag). The risk of being "suckered" is greater.

Ask: *At what point does Stag Hunt become a Prisoner's Dilemma?* Answer: When Hare becomes a dominant strategy — i.e., when the payoff for (Hare, Stag) exceeds the payoff for (Stag, Stag).

---

### III. Battle of the Sexes — Coordination with Conflict

**1. The Story**

A couple wants to spend an evening together. They must decide between:
- **Opera** (she prefers this)
- **Football** (he prefers this)

The key: both prefer being together over being apart, even if it means attending their less-preferred event.

**2. The Payoff Matrix**

| | **She: Opera** | **She: Football** |
|---|---|---|
| **He: Opera** | 3, 2 | 0, 0 |
| **He: Football** | 0, 0 | 2, 3 |

*Note:* The asymmetry (3,2 vs. 2,3) captures the conflict within coordination.

**3. Nash Equilibria**

Find the equilibria:
- **(Opera, Opera)**: He gets 2 (better than 0), she gets 3 (better than 0). **Equilibrium.**
- **(Football, Football)**: He gets 3, she gets 2. **Equilibrium.**
- **(Opera, Football)** or **(Football, Opera)**: Both get 0 — not equilibria.

Write on the board:

> **Battle of the Sexes has two pure-strategy equilibria, but players disagree on which is better.**

**4. The Mixed-Strategy Equilibrium (Optional — Include If Class Is Mathematically Comfortable)**

There's also a **mixed-strategy equilibrium** where each player randomizes. Let p = probability he plays Opera, q = probability she plays Opera.

For him to be indifferent:
- Expected payoff from Opera: 3q + 0(1-q) = 3q
- Expected payoff from Football: 0q + 2(1-q) = 2 - 2q
- Set equal: 3q = 2 - 2q → 5q = 2 → q = 0.4

For her to be indifferent:
- Expected payoff from Opera: 2p + 0(1-p) = 2p
- Expected payoff from Football: 0p + 3(1-p) = 3 - 3p
- Set equal: 2p = 3 - 3p → 5p = 3 → p = 0.6

So the mixed equilibrium is: He plays Opera with probability 0.6, she plays Opera with probability 0.4.

Expected payoff in mixed equilibrium:
- Him: 3(0.4) = 1.2
- Her: 2(0.6) = 1.2

Compare to pure equilibria (3,2) or (2,3) — the mixed equilibrium is **worse for both!**

**Lesson:** When coordination fails and players randomize, both can end up worse off — sometimes even miscoordinating (ending up at (0,0)).

**5. Real-World Examples**

Ask the class for examples of Battle of the Sexes situations:
- Two departments must choose a meeting time (morning vs. afternoon)
- Two firms must choose a technical standard (USB-C vs. Lightning)
- Two countries must choose a border policy (open vs. closed)

The pattern: we agree we need to coordinate, but we disagree on *how*.

---

### IV. Pure Coordination Games — No Conflict, Just Matching

**1. The Simplest Case**

| | **Left** | **Right** |
|---|---|---|
| **Left** | 1, 1 | 0, 0 |
| **Right** | 0, 0 | 1, 1 |

Two equilibria: (Left, Left) and (Right, Right). Both are equally good. No conflict — just the need to match.

**2. The Puzzle**

If both equilibria are equally good, and there's no communication, **how do players choose?**

This is where Thomas Schelling's insight becomes crucial.

---

## Lecture Part 2: Schelling Points and the Theory of Convention

### I. Schelling's Experiments on Focal Points

**1. The Meeting Problem**

Schelling (in *The Strategy of Conflict*, 1960) posed this question to his students:

> "You are to meet a stranger in New York City. You cannot communicate. Where and when do you go?"

*Poll the class:* What would you do?

Schelling's students gave remarkably consistent answers:
- **Where:** Grand Central Station, the information booth
- **When:** Noon

**2. Why These Answers?**

There's nothing intrinsically special about Grand Central or noon. But they are **salient** — they stand out as natural focal points.

Schelling called these **focal points** (now often called **Schelling points**): solutions that attract attention because they are prominent, unique, or culturally significant.

**3. More Schelling Experiments**

Schelling asked students various coordination questions:

| Question | Most Common Answer |
|---|---|
| Name a number | 1 (or 7, or 100) |
| Name a positive number | 1 |
| Divide $100 between you and a stranger | 50-50 |
| Which side of the road to drive on? | Right (in the US) |
| Heads or Tails? | Heads |

The pattern: people converge on answers that are **conspicuous** — not because they're objectively better, but because they're *psychologically salient*.

**4. What Makes a Focal Point?**

Write on the board:

> **Sources of salience:**
> - Uniqueness (the only X of its kind)
> - Cultural prominence (Grand Central, noon)
> - Symmetry/fairness (50-50 split)
> - Precedent (what we did before)
> - Labels/names (some options are "named" and stand out)

**5. The Key Insight**

Schelling's crucial observation:

> Focal points work *because* people expect them to work. If I expect you to go to Grand Central at noon (because it's the obvious answer), and you expect me to expect that, then Grand Central at noon *is* the rational choice — not because it's intrinsically better, but because it's what we both expect.

This is a self-fulfilling expectation — and it's the seed of convention.

---

### II. David Lewis's Theory of Convention

**1. The Central Question**

David Lewis, in his 1969 book *Convention: A Philosophical Study*, asked: **What is a convention?**

His answer: A convention is a solution to a recurrent coordination problem that is:
- **Arbitrary** (there was at least one other possible solution)
- **Self-perpetuating** (everyone follows it because everyone expects everyone else to)
- **Common knowledge** (everyone knows, everyone knows that everyone knows, etc.)

**2. Lewis's Definition (Formal)**

A regularity R in behavior is a **convention** in a population P if and only if:
1. Everyone conforms to R.
2. Everyone expects everyone else to conform to R.
3. Everyone prefers to conform to R *given that others do*.
4. There is at least one alternative regularity R' that could have solved the coordination problem instead.
5. (1)-(4) are **common knowledge** in P.

**3. Examples of Conventions (Apply the Definition)**

**Driving on the right:**
1. Everyone drives on the right. ✓
2. Everyone expects everyone else to drive on the right. ✓
3. Everyone prefers to drive on the right *given that others do*. ✓
4. Driving on the left would have worked just as well (as the UK shows). ✓
5. This is common knowledge. ✓

Therefore: Driving on the right is a convention.

**Language:**
- Why do we use "dog" to refer to dogs? Not because "dog" is intrinsically dog-like — it's arbitrary.
- But everyone expects everyone else to use "dog" this way, and everyone prefers to conform (to be understood).
- Therefore: Word meanings are conventions.

**Money:**
- Why is a green piece of paper worth $20? Not because of its intrinsic properties.
- Because everyone expects everyone else to accept it, and everyone prefers to conform.
- Therefore: The value of money is conventional.

**4. The Arbitrariness Condition**

This is crucial: A convention is *arbitrary* in the sense that there was at least one other possible solution.

Ask: *Is the 50-50 split a convention?* It might not be — it could be a "natural" focal point based on fairness intuitions that are not arbitrary. Contrast with driving on the right vs. left — clearly arbitrary.

**5. Common Knowledge**

Lewis emphasized that conventions require **common knowledge** — not just mutual knowledge, but knowledge iterated infinitely:
- I know that you know.
- I know that you know that I know.
- I know that you know that I know that you know.
- ...

Without common knowledge, coordination can fail. (We'll study this more in Week 10.)

---

### III. How Conventions Arise

**1. The Puzzle**

If conventions are arbitrary, how do they get established? Why do we drive on the right in the US and the left in the UK?

**2. Lewis's Answer: Precedent and Salience**

Conventions typically arise through:
- **Precedent:** We did it this way before, so we do it this way again.
- **Salience:** Some options are naturally more prominent (Schelling points).
- **Agreement:** Sometimes conventions are explicitly established (e.g., technical standards).

But once established, conventions persist because of self-fulfilling expectations.

**3. Path Dependence**

Write on the board:

> **Path dependence:** Small historical accidents can lock in conventions that persist indefinitely.

Example: The QWERTY keyboard layout was designed to *slow* typists down (to prevent mechanical typewriter jams). It's not optimal — but it's conventional, and switching costs are enormous.

**4. Conventions Can Be Hard to Change**

Even if a convention is suboptimal, changing it requires *coordinated* change — and coordinating the change is itself a coordination problem!

Example: The metric system is arguably better than imperial units. But the US hasn't fully switched — why? Because everyone would need to switch together, and coordinating that is difficult.

---

### IV. Philosophical Applications

**1. Language as Convention**

Lewis's primary application: **language is a system of conventions.**

- Word meanings are arbitrary (no intrinsic connection between "dog" and dogs).
- But everyone expects everyone else to use words with certain meanings.
- Therefore: Communication is a coordination game, and language is the convention that solves it.

This solves a puzzle: Why do we use words consistently? Not because we're forced to, but because we want to be understood — and being understood requires conformity.

**2. Morality as Convention (Skyrms, later)**

Some philosophers (e.g., Brian Skyrms) have argued that certain moral norms are conventions:
- Property rights: "Finders keepers" vs. "First come, first served" vs. "Equal division" — all could work, but we need *some* convention.
- Promises: The practice of promising is a convention that solves a coordination problem (trust in future action).

This suggests: Some moral rules are not "discovered" but "invented" — they are solutions to recurrent coordination problems.

**3. Social Norms**

Many social norms are conventions:
- Handshakes vs. bows vs. hugs as greetings
- Dress codes (formal, casual)
- Queuing (first-come-first-served)

These are arbitrary but self-perpetuating: I follow them because I expect others to, and others follow them because they expect me to.

---

### V. Philosophical Conclusion: Convention and Rationality

Close by raising the philosophical question that connects to earlier weeks.

**1. The Rationality of Convention**

Following a convention is rational — but only *because* others follow it. This means:
- Conventions are **contingent** (they could have been otherwise).
- Conventions are **fragile** (if expectations shift, the convention can collapse).
- Conventions are **not grounded in intrinsic reasons** (there's no deep reason to drive on the right rather than the left).

**2. Connection to Dennett (Week 7)**

Recall Dennett's "Moral First Aid Manual." Some of the conversation-stoppers Dennett describes might be **conventions**:
- "But that would break a promise" — the practice of promising is itself conventional.
- "But that would be unfair" — fairness norms may be conventional solutions to coordination problems.

Question: If moral rules are conventions, does that undermine their authority? Or can conventions be genuinely normative?

**3. Bridge to Next Week**

Next week we study **sequential games** and **backward induction**. This will introduce a new tool for analyzing coordination problems: the ability to reason through time, and to make commitments that shape others' expectations.

---

## Week 9 Problem Set: Coordination and Convention

**Topics:** Stag Hunt, Battle of the Sexes, Nash Equilibrium, Schelling Points, Lewis's Theory of Convention.
**Readings:** Lewis *Convention* (Introduction, Ch. 1-2), Schelling *The Strategy of Conflict* (excerpts), Skyrms *Evolution of the Social Contract* (Ch. 1-2).

---

### Type 1: Drill Exercises

**1. Identifying Game Types**

For each payoff matrix, identify whether it is a Prisoner's Dilemma, Stag Hunt, Battle of the Sexes, or Pure Coordination game. Find all pure-strategy Nash equilibria.

**Game A:**
| | **A** | **B** |
|---|---|---|
| **A** | 4, 4 | 0, 3 |
| **B** | 3, 0 | 2, 2 |

**Game B:**
| | **A** | **B** |
|---|---|---|
| **A** | 2, 3 | 0, 0 |
| **B** | 0, 0 | 3, 2 |

**Game C:**
| | **A** | **B** |
|---|---|---|
| **A** | 1, 1 | 0, 0 |
| **B** | 0, 0 | 1, 1 |

**Game D:**
| | **A** | **B** |
|---|---|---|
| **A** | 3, 3 | 0, 5 |
| **B** | 5, 0 | 1, 1 |

*Tasks:*
1. For each game, find all pure-strategy Nash equilibria.
2. Classify each game (PD, Stag Hunt, BoS, Pure Coordination).
3. For Stag Hunt games, identify the payoff-dominant and risk-dominant equilibria.

---

**2. Finding Mixed-Strategy Equilibria**

Consider the following Battle of the Sexes game:

| | **Opera** | **Football** |
|---|---|---|
| **Opera** | 4, 2 | 0, 0 |
| **Football** | 0, 0 | 2, 4 |

*Tasks:*
1. Find the mixed-strategy Nash equilibrium (calculate the probabilities).
2. What is each player's expected payoff in the mixed equilibrium?
3. Compare the mixed equilibrium payoff to each pure equilibrium payoff. Is the mixed equilibrium better or worse for each player?
4. Why might players end up in the mixed equilibrium even though it's worse for both?

---

### Type 2: "What-If" Exercises

**3. What If Payoffs Change in Stag Hunt?**

Start with a standard Stag Hunt:

| | **Stag** | **Hare** |
|---|---|---|
| **Stag** | 5, 5 | 0, 3 |
| **Hare** | 3, 0 | 2, 2 |

*Tasks:*
1. **Increase the stag payoff:** Change (Stag, Stag) to (10, 10). How does this affect the risk dominance of (Hare, Hare)? Does it make players more or less likely to hunt stag?
2. **Increase the hare payoff:** Change (Hare, Hare) to (4, 4). How does this affect the attractiveness of hare hunting? At what point does Stag Hunt cease to be a coordination problem and become a dominance-solvable game?
3. **Decrease the sucker's payoff:** Change (Stag, Hare) from (0, 3) to (-5, 3). How does this affect risk dominance? Does it make stag hunting more or less attractive?
4. **Asymmetric payoffs:** Suppose Player 1 gets 6 from (Stag, Stag) but Player 2 gets only 4. How might this affect their choices? Is there still a coordination problem?

---

**4. Schelling Points in Practice**

For each scenario, identify the most likely Schelling point and explain why it's salient:

a. You and a friend are separated in a crowded mall with no cell service. Where do you meet?

b. You're dividing a pizza with three friends. No one is keeping track of who ate how much. What's the "fair" division?

c. You're meeting a stranger to exchange a package. You can't communicate. Where in your city do you go?

d. Two drivers approach each other on a narrow road with no marked lanes. What do they do?

e. **Challenge:** You're playing a coordination game where you must name the same number as your partner to win $100. You can't communicate. What number do you name? (Test this on a friend!)

---

### Type 3: Puzzle/Paradox

**5. The Hi-Lo Paradox (Michael Bacharach)**

Consider this game:

| | **Hi** | **Lo** |
|---|---|---|
| **Hi** | 10, 10 | 0, 0 |
| **Lo** | 0, 0 | 1, 1 |

There are two equilibria: (Hi, Hi) and (Lo, Lo). (Hi, Hi) payoff-dominates (Lo, Lo). But:

*The Paradox:* Standard game theory says both are equally "rational" — both are Nash equilibria. But intuitively, rational players should play (Hi, Hi). Why?

*Tasks:*
1. Explain why both (Hi, Hi) and (Lo, Lo) are Nash equilibria.
2. Why does standard game theory treat them as equally rational?
3. What additional principle would be needed to recommend (Hi, Hi) uniquely? (Hint: consider "team reasoning" or "we-reasoning" — reasoning from the perspective of the group rather than the individual.)
4. **Philosophical question:** If rationality clearly recommends (Hi, Hi), but standard game theory can't explain why, is this a problem for game theory — or a problem with our concept of rationality?

---

**6. Conventions and Arbitrariness**

Lewis says conventions must be **arbitrary** — there must be at least one alternative that could have worked instead.

*Tasks:*
1. Is driving on the right a convention? Apply Lewis's definition carefully. Is the "right side" arbitrary?
2. Is the meaning of the word "dog" a convention? What's the alternative? (Could we have used "cat" to refer to dogs?)
3. Is the 50-50 split a convention? Or is it a "natural" focal point based on fairness? Does it matter whether fairness intuitions are innate or learned?
4. **Challenge:** Lewis later suggested that the arbitrariness condition might be too strong. Perhaps a convention only needs to be *somewhat* arbitrary — there just needs to be *some* alternative, even if it's less natural. Evaluate this modification.

---

### Type 4: Applied Analysis

**7. Language as Convention**

Lewis's primary application of convention theory is to language. Word meanings, he argues, are conventions that solve coordination problems.

*Tasks:*
1. Explain how communication is a coordination game. (Hint: the speaker wants to be understood, the listener wants to understand — but both need to use the same "code.")
2. Apply Lewis's definition: Is the meaning of "dog" a convention? Check each condition.
3. **Neologisms:** How do new words become conventional? (Consider: "selfie," "ghosting," "rizz.") What's the process by which an arbitrary term becomes standard?
4. **Language change:** Old English "thou" was replaced by "you." Was this a convention shift? If so, what caused it?
5. **Philosophical question:** If word meanings are conventions, does that mean meaning is "just" conventional — or can conventions be genuinely meaningful? (This connects to debates about moral conventionalism.)

---

**8. Technical Standards as Conventions**

Consider the following technical standards wars:
- VHS vs. Betamax (video format)
- Blu-ray vs. HD-DVD
- USB-C vs. Lightning vs. Micro-USB
- QWERTY vs. Dvorak keyboard layouts

*Tasks:*
1. Model a standards war as a Battle of the Sexes game. (Two firms, two standards, each prefers their own but both prefer coordination.)
2. Why did VHS win over Betamax? Was it superior technology, or a Schelling point / network effect?
3. **Path dependence:** QWERTY was designed to slow typists down (to prevent jams in mechanical typewriters). It's arguably inferior to Dvorak. Why does it persist?
4. **Policy question:** Should governments intervene in standards wars (e.g., mandate USB-C for all phones, as the EU has done)? Or should the market decide? Apply coordination game analysis to justify your answer.

---

**9. Social Norms as Conventions**

Many social norms look like conventions:
- Handshakes vs. bows as greetings
- First-come-first-served queuing
- Tipping customs (15-20% in the US, different elsewhere)
- Dress codes (formal, business casual, casual)

*Tasks:*
1. Choose one social norm and model it as a coordination game. What are the strategies? What are the payoffs?
2. Is the norm arbitrary? Could a different norm have worked?
3. How do these norms get enforced? (Hint: consider that deviation from a convention can be punished — and punishment itself may be part of the convention.)
4. **Moral question:** If a social norm is "just" a convention, does that mean it's morally optional? Or can conventions generate genuine obligations? (Consider: Is queuing morally required, or merely conventional?)

---

**10. Convention and Common Knowledge**

Lewis emphasizes that conventions require **common knowledge** — not just that everyone knows, but that everyone knows that everyone knows, and so on.

*Scenario:* Two drivers approach an intersection with a broken traffic light. Both know the convention: "First to arrive goes first." But:
- Driver A arrives first.
- Driver B doesn't see A arrive.
- A sees that B didn't see.

*Tasks:*
1. Is there common knowledge of who arrived first? If not, what kind of knowledge is there?
2. What should Driver A do? What should Driver B do?
3. How could common knowledge be established? (Consider: eye contact, hand signals, honking.)
4. **Formal question:** Why does common knowledge require infinite iteration? What goes wrong if knowledge is only "I know that you know" but not "I know that you know that I know"?

---

**11. The Emergence of Conventions (Skyrms's Model)**

Brian Skyrms has argued that conventions can emerge through a process of trial and error, without explicit agreement or even full rationality.

*Setup:* Imagine a population of agents repeatedly paired to play a coordination game. Each agent has a simple learning rule: if a strategy worked well, increase the probability of using it next time.

*Tasks:*
1. Simulate (conceptually) how a convention might emerge. Start with random strategy choices, then let agents learn from success.
2. Will the population always converge on one convention? Or can multiple conventions coexist?
3. What role does "noise" (random experimentation) play in convention formation?
4. **Philosophical question:** If conventions can emerge without rational deliberation — through blind evolutionary processes — does this undermine Lewis's rationalist account? Or does it complement it?

---

**12. Synthesis: Coordination vs. Cooperation**

We have now studied two fundamental strategic problems:
- **Prisoner's Dilemma (Week 8):** A problem of cooperation (escaping a bad equilibrium)
- **Coordination Games (Week 9):** A problem of coordination (selecting among good equilibria)

*Tasks:*
1. Explain the key difference between cooperation problems and coordination problems.
2. Can a game have elements of both? Consider this game:

| | **A** | **B** |
|---|---|---|
| **A** | 4, 4 | -1, 3 |
| **B** | 3, -1 | 2, 2 |

Is this a cooperation problem, a coordination problem, or both?

3. Real-world problems often involve both cooperation and coordination. Climate change, for example:
   - Cooperation problem: Each country is tempted to free-ride.
   - Coordination problem: Countries must agree on *which* emissions targets, *which* enforcement mechanisms, etc.

   Analyze climate change using both frameworks.

4. **Final synthesis:** Rank the following solutions by whether they address cooperation problems, coordination problems, or both:
   - (a) External enforcement (fines, sanctions)
   - (b) Communication
   - (c) Precedent/convention
   - (d) Moral education
   - (e) Repetition/iteration

---

## Appendix: Instructor Notes

### Suggested In-Class Activities

**1. Live Coordination Experiment**

Pair students (without letting them communicate) and have them play:
- One round of Stag Hunt
- One round of Battle of the Sexes
- One round of Pure Coordination

After each round, poll the class on outcomes. Discuss:
- How many pairs coordinated successfully?
- Which equilibrium did they select?
- What reasoning did they use?

**2. Schelling Point Exercise**

Ask students (without discussion) to write down answers to:
- "Name a number between 1 and 100."
- "Name a color."
- "Where would you meet a stranger in this city?"

Collect and display the distribution. Expect clustering around salient answers.

**3. Convention Demonstration**

Start class with an arbitrary rule: "Everyone who enters must knock three times." After a few students do it, ask: "Why did you knock?" The answer: "Because I saw others do it" — a convention in real time.

---

### Common Student Misconceptions

1. **"Coordination games are easier than PDs."** Not necessarily — PDs have a unique (if bad) equilibrium. Coordination games have multiple equilibria, which creates indeterminacy.

2. **"Focal points are about intrinsic superiority."** No — focal points are about *salience*, which can be arbitrary or culturally contingent.

3. **"Conventions are just habits."** Conventions are habits *plus* mutual expectations. I follow a convention *because* I expect you to, not just because I'm in the habit.

4. **"Mixed strategies are just randomization."** Mixed strategies are rational responses to strategic uncertainty — not caprice, but calculated unpredictability.

---

### Connections to Other Course Topics

| Week | Connection |
|---|---|
| W8 (PD) | Contrast: PD has one bad equilibrium; coordination has multiple, some good. |
| W7 (Dennett) | Conventions can function as conversation-stoppers ("But that's not how we do things"). |
| W6 (Prospect Theory) | Framing can affect which equilibrium is selected (reference points as Schelling points). |
| W10 (Sequential Games) | Sequential moves can resolve coordination problems (first mover sets the focal point). |
| W11 (Evolution) | Conventions can evolve without rational deliberation (Skyrms). |
| W13 (Behavioral) | Empirical coordination behavior often deviates from Nash predictions. |

---

## Preview of Next Week

Next week we add **time** to the analysis: sequential games, game trees, and backward induction. We'll study:
- Extensive form representation
- Subgame perfection
- The Centipede Game paradox (backward induction vs. intuition)
- Common knowledge of rationality (and whether it's desirable)

The tools we develop will help us understand commitment, threats, promises, and the strategic value of limiting your own options.
