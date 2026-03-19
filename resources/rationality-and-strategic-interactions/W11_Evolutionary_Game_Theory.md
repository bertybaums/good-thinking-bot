# W11 Evolutionary Game Theory — Cooperation Without Rationality

- No rationality required: strategies survive or die based on reproductive success, not reasoning
- Evolutionarily Stable Strategies (ESS): strategies that cannot be invaded by mutants
- The replicator dynamics: successful strategies spread, unsuccessful ones vanish
- Cooperation can evolve even among non-rational agents — through selection, not deliberation
- Skyrms's project: the social contract is not designed but evolved
- Connection to earlier weeks: evolution can solve PDs, select coordination equilibria, and explain Centipede "anomalies"
- The deep question: Is human rationality just evolution's latest trick?

---

## Lecture Part 1: From Rational Choice to Evolutionary Dynamics

### I. The Bridge from Sequential to Evolutionary Games

**1. What We've Assumed So Far**

Write on the board:

| Week | Model of Agency | Key Assumption |
|---|---|---|
| W8-W9 | Rational choosers | Maximize expected utility |
| W10 | Rational choosers in time | Common knowledge of rationality, backward induction |

All of these models assume **rational deliberation**: agents think through their options, form beliefs about others, and choose optimally.

**2. The Evolutionary Alternative**

Today we drop that assumption entirely.

| Rational Game Theory | Evolutionary Game Theory |
|---|---|
| Agents are rational deliberators | Agents are "programmed" with fixed strategies |
| Success = utility maximization | Success = reproductive fitness (or imitation) |
| Equilibrium = Nash, subgame perfection | Equilibrium = Evolutionarily Stable Strategy (ESS) |
| Change = learning, reasoning | Change = selection (successful strategies spread) |
| Question: "What should a rational agent do?" | Question: "Which strategies survive over time?" |

The key insight: **Evolution can produce outcomes that look "rational" without any rationality at all.** Bacteria play games. Genes play games. Cultural practices play games. None of them reason — but all of them evolve.

**3. Today's Agenda**

We will:
1. Learn the concept of an Evolutionarily Stable Strategy (ESS)
2. Study the replicator dynamics (how strategies spread)
3. Apply evolutionary theory to cooperation (Prisoner's Dilemma)
4. Read Skyrms on the evolution of the social contract
5. Ask: Can evolution explain what rationality could not?

---

### II. Evolutionarily Stable Strategies (ESS)

**1. The Basic Idea (Maynard Smith, 1970s)**

John Maynard Smith, a biologist, asked: How do animals resolve conflicts over resources?

Consider two strategies:
- **Hawk:** Fight aggressively until injured or opponent retreats.
- **Dove:** Display aggression but retreat if opponent escalates.

What happens when Hawks and Doves interact?

**2. The Payoff Matrix (Biological Version)**

Draw on the board:

| | **Hawk** | **Dove** |
|---|---|---|
| **Hawk** | (V-C)/2, (V-C)/2 | V, 0 |
| **Dove** | 0, V | V/2, V/2 |

Where:
- **V** = Value of the resource (food, mating opportunity, territory)
- **C** = Cost of injury (from fighting)

*Explanation:*
- Hawk vs. Hawk: They fight. Each wins with probability 1/2, gets V if win, loses C if lose. Expected payoff: (V-C)/2.
- Hawk vs. Dove: Hawk takes everything (V), Dove gets nothing (0).
- Dove vs. Dove: They share (or one retreats peacefully). Each gets V/2.

**3. When Is Hawk an ESS?**

Definition:

> **Evolutionarily Stable Strategy (ESS):** A strategy S is an ESS if, when almost all members of the population use S, no mutant strategy M can invade (i.e., M does worse than S against S).

Formally, S is an ESS if for any mutant M:
1. **E(S, S) > E(M, S)**, OR
2. **E(S, S) = E(M, S) AND E(S, M) > E(M, M)**

(Condition 1: S does better against itself than M does against S. Condition 2: If they're equal, S must do better against M than M does against itself.)

**Apply to Hawk:**
- E(Hawk, Hawk) = (V-C)/2
- E(Dove, Hawk) = 0

Hawk is an ESS if (V-C)/2 > 0, i.e., if **V > C**.

Interpretation: If the value of the resource exceeds the cost of fighting, Hawk cannot be invaded by Dove.

**4. When Is Dove an ESS?**

- E(Dove, Dove) = V/2
- E(Hawk, Dove) = V

Dove is an ESS if V/2 > V — which is **never** (assuming V > 0).

So Dove is **never** an ESS. Hawks always invade a population of Doves.

**5. Mixed ESS**

What if V < C? Then:
- E(Hawk, Hawk) = (V-C)/2 < 0
- E(Dove, Hawk) = 0

So Dove does better against Hawk than Hawk does against Hawk.

In this case, neither pure Hawk nor pure Dove is an ESS. But there's a **mixed ESS**: a population where some proportion plays Hawk and some plays Dove.

Find the equilibrium proportion p (probability of Hawk):

At equilibrium, the expected payoff of Hawk equals the expected payoff of Dove:

E(Hawk) = p × (V-C)/2 + (1-p) × V
E(Dove) = p × 0 + (1-p) × V/2

Set equal:
p(V-C)/2 + (1-p)V = (1-p)V/2

Solve for p:
p(V-C)/2 + V - pV = V/2 - pV/2
p(V-C)/2 - pV + pV/2 = V/2 - V
p[(V-C)/2 - V + V/2] = -V/2
p[(V-C-V+V)/2] = -V/2
p[(V-C)/2] = -V/2

Hmm, let me redo this more carefully:

E(Hawk) = p(V-C)/2 + (1-p)V
E(Dove) = p(0) + (1-p)V/2 = (1-p)V/2

Set equal:
p(V-C)/2 + (1-p)V = (1-p)V/2
p(V-C)/2 + V - pV = V/2 - pV/2
p(V-C)/2 - pV + pV/2 = V/2 - V
p[(V-C)/2 - V + V/2] = -V/2
p[(V-C-V)/2 + V/2] = -V/2
p[(-C)/2 + V/2] = -V/2
p(V-C)/2 = -V/2

This gives p = -V/(V-C), which is negative if V < C. Something's wrong.

Let me reconsider. If V < C:
- E(Hawk, Hawk) < 0 (fighting is costly)
- E(Dove, Hawk) = 0 (Dove retreats, gets nothing but no injury)
- E(Hawk, Dove) = V (Hawk takes all)
- E(Dove, Dove) = V/2 (sharing)

In a mixed population with proportion p of Hawks:
- E(Hawk) = p(V-C)/2 + (1-p)V
- E(Dove) = p(0) + (1-p)V/2

For equilibrium, set E(Hawk) = E(Dove):
p(V-C)/2 + (1-p)V = (1-p)V/2
p(V-C)/2 + V - pV = V/2 - pV/2
V - V/2 = pV - pV/2 - p(V-C)/2
V/2 = p[V - V/2 - (V-C)/2]
V/2 = p[V/2 - (V-C)/2]
V/2 = p[(V - V + C)/2]
V/2 = p(C/2)
p = V/C

So the mixed ESS is: **proportion V/C of Hawks, proportion (1 - V/C) of Doves.**

If V < C, then p < 1, so there's a stable mix. If V = C, then p = 1 (all Hawks). If V > C, then p > 1 (impossible), meaning pure Hawk is the ESS.

Write on the board:

> **Mixed ESS (Hawk-Dove):** When V < C, the population stabilizes at proportion V/C Hawks.

**6. Interpretation**

This is a key result: Even though no individual is "choosing" to mix, the *population* exhibits a stable mixture of strategies. This is the power of evolutionary thinking: **population-level rationality without individual rationality.**

---

### III. The Replicator Dynamics

**1. The Basic Idea**

How do strategies spread? The **replicator dynamics** models this:

> Strategies that do better than average increase in frequency. Strategies that do worse than average decrease.

**2. The Replicator Equation**

Let x_i be the proportion of the population using strategy i. Let f_i be the fitness (expected payoff) of strategy i. Let F be the average fitness of the population.

The replicator equation is:

> **dx_i/dt = x_i (f_i - F)**

Interpretation:
- If f_i > F (strategy i does better than average), then dx_i/dt > 0 → strategy i grows.
- If f_i < F (strategy i does worse than average), then dx_i/dt < 0 → strategy i shrinks.
- If f_i = F, the proportion stays constant.

**3. Example: Hawk-Dove Dynamics**

Suppose we start with a population that's 50% Hawk, 50% Dove. Let V = 2, C = 4 (so V < C).

- E(Hawk, population) = 0.5 × (2-4)/2 + 0.5 × 2 = 0.5 × (-1) + 1 = 0.5
- E(Dove, population) = 0.5 × 0 + 0.5 × 1 = 0.5
- Average fitness F = 0.5 × 0.5 + 0.5 × 0.5 = 0.5

At this point, Hawks and Doves have equal fitness, so proportions don't change. This is an equilibrium.

But is it stable? If we perturb slightly (say, 51% Hawk), what happens?

- E(Hawk) = 0.51 × (-1) + 0.49 × 2 = -0.51 + 0.98 = 0.47
- E(Dove) = 0.51 × 0 + 0.49 × 1 = 0.49
- Now E(Dove) > E(Hawk), so Doves increase.

The system returns to equilibrium. This confirms: the mixed ESS is **stable** under replicator dynamics.

**4. Key Properties of Replicator Dynamics**

Write on the board:

> - ESS ⇒ Stable under replicator dynamics (usually)
> - Not all stable states are ESS (but close)
> - Dynamics can cycle or chaos (in more complex games)
> - No rationality required — just differential reproduction

---

## Lecture Part 2: The Evolution of Cooperation

### I. The Prisoner's Dilemma (Again) — But Now Evolutionary

**1. The Setup**

Recall the PD:

| | **C** | **D** |
|---|---|---|
| **C** | 3, 3 | 0, 5 |
| **D** | 5, 0 | 1, 1 |

In a one-shot rational game, Defect dominates. But what about evolutionarily?

**2. One-Shot Evolutionary PD**

Imagine a population where individuals are randomly paired to play one-shot PD. Each individual is "programmed" to always Cooperate or always Defect.

- E(C, population) = p × 3 + (1-p) × 0 = 3p (where p = proportion of Cs)
- E(D, population) = p × 5 + (1-p) × 1 = 5p + 1 - p = 4p + 1

For any p:
- E(D) - E(C) = (4p + 1) - 3p = p + 1 > 0

So **Defect always does better than Cooperate**, regardless of population composition.

Conclusion: **Defect is the unique ESS.** Cooperators go extinct.

This matches the rational analysis: in one-shot PD, cooperation cannot evolve.

**3. Iterated PD — Axelrod's Tournament (Again)**

But what if individuals play repeatedly? Now new strategies become possible:
- **Tit-for-Tat (TFT):** Cooperate first, then do what opponent did last round.
- **Always Defect (ALLD):** Defect every round.
- **Always Cooperate (ALLC):** Cooperate every round.
- **Grim Trigger:** Cooperate until opponent defects, then defect forever.

Axelrod's tournament (rational agents) found: **Tit-for-Tat wins.**

What about evolutionary dynamics?

**4. Evolution of TFT vs. ALLD**

Consider a population of TFT and ALLD. Payoffs depend on how many rounds they play (let's say expected number of rounds = n, accounting for probability of continuation).

For simplicity, assume n is large enough that:
- TFT vs. TFT: Both cooperate every round → 3n each
- ALLD vs. ALLD: Both defect every round → 1n each
- TFT vs. ALLD: TFT cooperates round 1, then defects; ALLD always defects → TFT gets 0 + 1(n-1) ≈ n, ALLD gets 5 + 1(n-1) ≈ n + 4

In a population with proportion p of TFT:
- E(TFT) = p × 3n + (1-p) × n = 3pn + n - pn = 2pn + n
- E(ALLD) = p × (n+4) + (1-p) × n = pn + 4p + n - pn = n + 4p

Set equal for equilibrium:
2pn + n = n + 4p
2pn = 4p
If p ≠ 0: 2n = 4 → n = 2

So:
- If n > 2 (players expect more than 2 rounds), TFT can invade ALLD.
- If n < 2, ALLD dominates.

But there's a catch: **TFT can also be invaded by ALLC** (since TFT and ALLC do equally well against each other, but ALLC doesn't waste time punishing).

This leads to more complex dynamics — cycles, or coexistence.

**5. The General Lesson**

Write on the board:

> **Iterated interaction changes everything.**
> - One-shot PD: Defection is the only ESS.
> - Iterated PD: Cooperation can evolve (if future matters enough).

This mirrors the rational analysis (repeated games allow cooperation) — but now it's about **selection**, not reasoning.

---

### II. Skyrms's Evolution of the Social Contract

**1. The Project**

Brian Skyrms, in his 1996 book *The Evolution of the Social Contract*, asks:

> Can the basic structures of morality — justice, promises, property, conventions — emerge from purely evolutionary processes, without rational design?

His answer: **Yes.** Many features of the "social contract" that philosophers have attributed to rational agreement can be explained as evolutionary equilibria.

**2. The Stag Hunt (Again) — But Now Evolutionary**

Recall the Stag Hunt:

| | **Stag** | **Hare** |
|---|---|---|
| **Stag** | 5, 5 | 0, 3 |
| **Hare** | 3, 0 | 2, 2 |

Rational analysis: Two equilibria (Stag, Stag) and (Hare, Hare). (Stag, Stag) is payoff-dominant; (Hare, Hare) is risk-dominant.

Evolutionary analysis: Which equilibrium does the population converge to?

Answer: **It depends on the initial conditions.**

- If the population starts with enough Stag-hunters (above a threshold), selection drives it to (Stag, Stag).
- If the population starts with too few Stag-hunters, selection drives it to (Hare, Hare).

This is called **path dependence**: history matters.

**3. The Basin of Attraction**

Find the threshold:

Let p = proportion of Stag-hunters.
- E(Stag) = p × 5 + (1-p) × 0 = 5p
- E(Hare) = p × 3 + (1-p) × 2 = 3p + 2 - 2p = p + 2

Set equal:
5p = p + 2
4p = 2
p = 0.5

So:
- If p > 0.5, Stag does better → population moves toward all-Stag.
- If p < 0.5, Hare does better → population moves toward all-Hare.
- If p = 0.5, equilibrium (unstable).

Write on the board:

> **Basin of attraction:** The set of initial conditions that lead to a particular equilibrium.
> - All-Stag has basin: p > 0.5
> - All-Hare has basin: p < 0.5

**4. Implications for the Social Contract**

Skyrms's point: The social contract (cooperation, trust, mutual aid) is not a one-time rational agreement. It's an **evolutionary equilibrium** that some societies fall into — and once there, it's self-sustaining.

But societies can also fall into the "bad" equilibrium (universal distrust, low cooperation). And moving from bad to good requires **coordinated change** — getting enough people to cooperate that cooperation becomes self-sustaining.

This explains:
- Why some societies have high trust and others low trust.
- Why changing social norms is difficult (you need to cross the threshold).
- Why "moral entrepreneurs" can make a difference (they shift the population composition).

**5. Correlation and Assortment**

Skyrms emphasizes one more factor: **correlation**.

If cooperators are more likely to interact with other cooperators (assortative matching), cooperation is easier to sustain.

Example: If Stag-hunters can recognize each other and preferentially interact, then even a small population of Stag-hunters can survive and grow.

This connects to:
- **Reputation:** Cooperators build reputations and find each other.
- **Spatial structure:** Cooperators cluster geographically or socially.
- **Kin selection:** Cooperators are related (share genes).

---

### III. Signaling and Information (Preview of Week 12)

**1. The Problem**

How can agents communicate honestly when lying might be beneficial?

Example: A peacock's tail signals "I'm healthy" — but why trust the signal? Couldn't a weak peacock fake it?

**2. The Answer: Costly Signaling**

Zahavi's **Handicap Principle**: Signals are credible only if they are costly, and more costly for low-quality senders.

- A peacock's tail is costly (makes you vulnerable to predators).
- A healthy peacock can afford the cost; a sick one cannot.
- Therefore: The tail is an honest signal of health.

**3. Evolutionary Stability**

An honest signaling system is an ESS if:
- Senders: High-quality senders benefit from signaling; low-quality do not (cost exceeds benefit).
- Receivers: Benefit from trusting the signal (on average).

We'll study this more next week.

---

### IV. Philosophical Conclusion: Is Morality Evolved or Reasoned?

Close by raising the philosophical question.

**1. The Two Pictures**

| Morality as Rational Agreement | Morality as Evolved Equilibrium |
|---|---|
| Hobbes, Locke, Kant, Rawls | Skyrms, Gibbard, evolutionary ethicists |
| Agents reason to moral principles | Populations evolve moral practices |
| Normativity from rationality | Normativity from fitness (or social success) |
| Universal principles | Local equilibria (may vary by context) |

**2. The Challenge**

If morality is evolved, not reasoned:
- Does that undermine its authority? (The "naturalistic fallacy" worry.)
- Or does it show that morality is **natural** — part of the causal order, not transcendent?

**3. Connection to Earlier Weeks**

- **Week 7 (Dennett):** Dennett's "Moral First Aid Manual" could be read as an evolved heuristic, not a rational construction.
- **Week 8 (PD):** Evolution can solve PDs that rationality cannot (through iteration, correlation).
- **Week 9 (Convention):** Conventions can evolve without explicit agreement (Lewis meets Skyrms).

**4. Bridge to Next Week**

Next week we study **signaling games** — where one player has private information and the other must infer it from observable actions. This will complete our tour of game-theoretic tools and set up the behavioral turn in Week 13.

---

## Week 11 Problem Set: Evolutionary Game Theory

**Topics:** ESS, Replicator Dynamics, Hawk-Dove, Iterated PD, Skyrms's Social Contract, Signaling.
**Readings:** Maynard Smith "Evolution and the Theory of Games" (excerpts), Skyrms *Evolution of the Social Contract* (Ch. 1-3), Axelrod "Evolution of Cooperation" (excerpts).

---

### Type 1: Drill Exercises

**1. Finding ESS**

For each game below, find all Evolutionarily Stable Strategies (pure and mixed).

**Game A (Prisoner's Dilemma):**
| | **C** | **D** |
|---|---|---|
| **C** | 3, 3 | 0, 5 |
| **D** | 5, 0 | 1, 1 |

**Game B (Coordination):**
| | **A** | **B** |
|---|---|---|
| **A** | 4, 4 | 0, 0 |
| **B** | 0, 0 | 2, 2 |

**Game C (Hawk-Dove with V = 4, C = 6):**
| | **Hawk** | **Dove** |
|---|---|---|
| **Hawk** | -1, -1 | 4, 0 |
| **Dove** | 0, 4 | 2, 2 |

*Tasks:*
1. For each game, check whether each pure strategy is an ESS.
2. If there's a mixed ESS, calculate the equilibrium proportions.
3. Interpret the results: What does the ESS predict about population behavior?

---

**2. Replicator Dynamics Calculations**

Consider a population with two strategies, X and Y. The payoff matrix is:

| | **X** | **Y** |
|---|---|---|
| **X** | 4, 4 | 1, 3 |
| **Y** | 3, 1 | 2, 2 |

Let p = proportion of X-players.

*Tasks:*
1. Write E(X) and E(Y) as functions of p.
2. Write the average fitness F as a function of p.
3. For what values of p is E(X) > E(Y)? For what values is E(Y) > E(X)?
4. Find the equilibrium (where E(X) = E(Y)).
5. Is the equilibrium stable? (Hint: Check what happens if p increases slightly above equilibrium.)

---

### Type 2: "What-If" Exercises

**3. What If Interaction Is Assortative?**

In a standard evolutionary PD, cooperators and defectors are randomly paired. But suppose cooperators are more likely to interact with other cooperators (assortative matching).

Let p = proportion of cooperators. Let r = correlation coefficient (r = 0 is random, r = 1 is perfect assortment).

The probability a cooperator meets another cooperator is: p + r(1-p).
The probability a defector meets a cooperator is: p - rp.

*Tasks:*
1. Write E(C) and E(D) as functions of p and r (using standard PD payoffs: T=5, R=3, P=1, S=0).
2. For r = 0 (random matching), show that D always dominates.
3. For r = 0.5, find the threshold p above which C does better than D.
4. **Interpretation:** What does this tell you about the evolution of cooperation? What real-world mechanisms produce assortment (r > 0)?

---

**4. What If the Cost of Fighting Changes?**

In the Hawk-Dove game, let V = 4 (fixed) and let C vary.

*Tasks:*
1. For C = 2 (V > C), find the ESS.
2. For C = 4 (V = C), find the ESS.
3. For C = 8 (V < C), find the ESS (may be mixed).
4. **Graph:** Plot the proportion of Hawks in the ESS as a function of C (for C from 0 to 12).
5. **Interpretation:** How does increasing the cost of fighting affect aggressive behavior? Does this match your intuitions about animal conflict?

---

### Type 3: Puzzle/Paradox

**5. The Red King Effect (From Skyrms)**

In some evolutionary games, **slower** evolution is advantageous. This is called the Red King Effect (after the Red Queen in *Through the Looking-Glass* — but here, the "slow" species benefits).

Consider a coordination game between two species (or two subpopulations) that must coordinate:

| | **A** | **B** |
|---|---|---|
| **A** | 10, 10 | 0, 0 |
| **B** | 0, 0 | 5, 5 |

Species 1 evolves much faster than Species 2 (e.g., shorter generation time).

*Tasks:*
1. What are the two equilibria? Which is better for each species?
2. Intuitively, which equilibrium should the population converge to?
3. **The paradox:** The faster-evolving species may be at a *disadvantage* — it "gives in" and adapts to the slower species' equilibrium. Why?
4. **Real-world example:** In host-parasite interactions, the parasite evolves faster. Does the Red King Effect predict that hosts "win" the coordination game? Explain.

---

**6. Altruism and Kin Selection (Hamilton's Rule)**

An altruistic act costs the actor c and benefits the recipient b. Under what conditions can altruism evolve?

W.D. Hamilton's insight: Genes for altruism can spread if the recipient is likely to share those genes. Let r = coefficient of relatedness (probability that actor and recipient share the altruism gene, above baseline).

**Hamilton's Rule:** Altruism evolves if **r × b > c**.

*Tasks:*
1. Derive Hamilton's Rule from an evolutionary model. (Hint: Compare the fitness of altruists vs. non-altruists, accounting for relatedness.)
2. Calculate r for: parent-child, full siblings, half-siblings, first cousins.
3. **Application:** A bee sacrifices its life (c = 1) to save the colony. If the colony contains many sisters (r = 0.75 in haplodiploid bees), how large must b be for altruism to evolve?
4. **Connection to game theory:** Model altruism as a Prisoner's Dilemma where players are related. Show that Hamilton's Rule is equivalent to saying "Cooperate is an ESS when r × b > c."

---

### Type 4: Applied Analysis

**7. Skyrms's Justice**

Skyrms argues that our sense of "justice" — particularly, the idea of equal division — can be explained evolutionarily.

Consider a bargaining game: Two players must divide a resource. Each demands a portion. If demands sum to ≤ 1, both get their demand. If demands sum to > 1, both get 0 (disagreement).

*Tasks:*
1. What are the Nash equilibria of this game? (Hint: Any pair of demands that sum to exactly 1 is an equilibrium.)
2. Why might "demand 1/2" be a focal point (Schelling point)?
3. Skyrms ran evolutionary simulations: strategies that demand more tend to crash (they often get 0), strategies that demand less leave value on the table. Over time, the population converges on "demand 1/2." Explain why.
4. **Philosophical question:** If our sense of justice is an evolved equilibrium, does that undermine its normative authority? Or does it show that justice is "natural" in a deep sense?

---

**8. The Evolution of Promising**

Skyrms devotes a chapter to promising: How can a practice of making and keeping promises evolve?

Model: Agents can either **Make a Promise** or Not. If they make a promise, they can either **Keep** it or **Break** it. Partners can either **Trust** (believe the promise) or **Distrust**.

Payoffs (simplified):
- Promise, Keep, Trust: (2, 2) — cooperation succeeds
- Promise, Break, Trust: (3, -1) — promisee is exploited
- Promise, Keep, Distrust: (0, 0) — missed opportunity
- Promise, Break, Distrust: (0, 0) — no interaction
- No Promise: (1, 1) — status quo

*Tasks:*
1. If there's no way to distinguish promise-keepers from promise-breakers, what evolves?
2. Suppose promise-breakers can be detected with probability q (reputation mechanism). How does this change the dynamics?
3. Find the threshold q above which promise-keeping can evolve.
4. **Connection to Week 9:** Is the practice of promising a convention (Lewis), an evolved equilibrium (Skyrms), or both?

---

**9. Cultural Evolution vs. Genetic Evolution**

So far we've discussed genetic evolution. But the same logic applies to **cultural evolution**: ideas, practices, and norms spread through imitation, teaching, and social learning.

*Key difference:* Cultural evolution can be much faster than genetic evolution. And it can be guided by reasoning (though not necessarily).

*Tasks:*
1. Model a simple cultural evolutionary process: Individuals imitate successful others. Write the replicator equation for cultural transmission.
2. What's the difference between "imitate the most successful" and "imitate the majority"? How do the dynamics differ?
3. **Application:** Consider the spread of a social norm (e.g., recycling, mask-wearing, tipping). Model it as an evolutionary process. What factors affect whether the norm spreads?
4. **Philosophical question:** If moral norms evolve culturally, does that make them relative (different societies evolve different norms)? Or can there be universal moral truths that all societies converge on?

---

**10. Synthesis: Evolution, Rationality, and Morality**

We have now studied three approaches to strategic interaction:
- **Rational choice (Weeks 8-10):** Agents maximize expected utility.
- **Bounded rationality (Weeks 6-7):** Agents use heuristics due to cognitive limits.
- **Evolution (Week 11):** Strategies survive or die based on fitness.

*Tasks:*
1. Compare the predictions for Prisoner's Dilemma:
   - Rational one-shot: Defect.
   - Rational repeated: Cooperate (if future matters).
   - Evolutionary one-shot: Defect.
   - Evolutionary repeated: Cooperate (if future matters).

   Are the predictions the same? If so, is evolution just a "foundation" for rationality? If not, where do they diverge?

2. Compare the predictions for Stag Hunt:
   - Rational: Indeterminate (depends on beliefs).
   - Evolutionary: Depends on initial conditions (path dependence).

   Are these the same kind of indeterminacy? Or fundamentally different?

3. **The Centipede Game:** Rational backward induction says "stop immediately." Evolutionary dynamics might favor cooperation (if there's variation and selection over time). Which prediction is more accurate empirically? What does this tell us about human nature?

4. **Final synthesis:** Rank the three approaches (rational, bounded rational, evolutionary) by:
   - (a) Realism (how well they describe actual behavior)
   - (b) Normativity (how well they prescribe what agents *should* do)
   - (c) Generality (how widely they apply — to humans, animals, organizations, etc.)

   Justify your rankings.

---

## Appendix: Instructor Notes

### Suggested In-Class Activities

**1. Evolutionary PD Simulation**

Have students play an evolutionary game:
- Each student is assigned a strategy (C or D) secretly.
- Randomly pair students; each pair plays one round of PD.
- "Fitness" = payoff from the game.
- Next generation: Students with above-average fitness "reproduce" (their strategy is copied by a classmate); below-average fitness "die" (adopt a random classmate's strategy).
- Repeat for several generations.

Track the proportion of cooperators over time. Expect: Cooperators go extinct (in one-shot PD).

**2. Hawk-Dove Role-Play**

Assign students to be Hawks or Doves. Pair them randomly and award "fitness points" according to the Hawk-Dove matrix. After each round, have low-fitness students adopt the strategy of a high-fitness classmate.

Track the population composition. Expect: Convergence to mixed ESS.

**3. Stag Hunt Coordination**

Have the whole class play Stag Hunt simultaneously (write choice on paper, then reveal). Payoffs: If you chose Stag, you get 5 points for each other Stag-chooser (up to a cap); if you chose Hare, you get 2 points guaranteed.

Repeat for several rounds, allowing students to see aggregate results between rounds.

Expect: Possible convergence to all-Stag or all-Hare, depending on initial conditions. Discuss: What factors pushed the class toward one equilibrium vs. the other?

---

### Common Student Misconceptions

1. **"ESS is the same as Nash equilibrium."** Close, but not identical. ESS is a refinement of Nash for evolutionary contexts. All ESSs are Nash equilibria, but not vice versa.

2. **"Evolution always produces optimal outcomes."** No — evolution produces locally stable equilibria, which may be suboptimal. Path dependence means history matters.

3. **"Mixed ESS means individuals randomize."** No — mixed ESS usually means the *population* is mixed (some always play X, some always play Y). Individuals are typically "pure" strategists.

4. **"Evolutionary game theory only applies to biology."** No — it applies to any context where strategies spread through differential success (culture, economics, social norms).

---

### Connections to Other Course Topics

| Week | Connection |
|---|---|
| W8 (PD) | Evolutionary PD shows why cooperation is hard without iteration or assortment. |
| W9 (Coordination) | Evolutionary Stag Hunt shows path dependence in equilibrium selection. |
| W10 (Sequential) | Backward induction assumes rationality; evolution achieves similar outcomes without it. |
| W7 (Dennett) | Evolved heuristics are exactly the kind of "Moral First Aid" Dennett describes. |
| W12 (Signaling) | Next week: how honest communication evolves (costly signaling). |
| W13 (Behavioral) | Behavioral anomalies may be evolved adaptations to ancestral environments. |

---

## Preview of Next Week

Next week we study **signaling games** — where one player has private information and the other must infer it from observable actions. We'll ask:
- How can signals be credible when lying is tempting?
- What is the role of cost in honest signaling?
- How do conventions of meaning arise?

This will connect game theory to philosophy of language, epistemology, and the evolution of communication.
