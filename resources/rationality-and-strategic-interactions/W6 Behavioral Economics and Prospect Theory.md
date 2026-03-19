# W6 Behavioral Economics and Prospect Theory

The Ideal's last defense has crumbled: no mathematical move rescues utility from the Reflection Effect
Engineering Failure confirmed: Kahneman & Tversky rebuild decision theory from behavioral data up
Value replaces Utility: outcomes are judged against a reference point, not measured as total wealth
π(p) replaces P: probability is psychologically distorted before any calculation begins
Money multiplies into accounts: Thaler shows fungibility is a fiction wired into the human mind

---

## Lecture Part 1: Building the Alternative — The Value Function

### I. The Bridge: A Failed Defense and an Open Question

Begin class by orienting students to the central question driving this week: when rational choice theory collides with real human behavior and loses — repeatedly, systematically, universally — is that an **Application Failure** (humans are making correctable errors) or an **Engineering Failure** (the theory itself is the wrong tool)?

**1. The Background: A Theory Under Siege (Brief Recap)**

The standard model of rational choice — **Maximizing Expected Utility (MEU)** — says that a rational agent should assign probabilities to outcomes, assign utilities to those outcomes, and choose the act with the highest probability-weighted utility. It is mathematically elegant and normatively compelling. But decades of experiments have revealed a pattern of systematic violations.

Draw the following scoreboard on the board, explaining each row briefly:

| The Attack | What It Showed | The Standard Defense |
|---|---|---|
| **Allais Paradox** (Certainty Effect) | People prefer a certain $1M over a risky shot at $5M in ways that violate the Independence axiom — they weight certainty as categorically different from high probability | STP + "Cognitive Illusion" (Savage): once you see the math, you should correct your preference |
| **Newcomb's Problem** (Causal Structure) | Two decision procedures — one causal, one evidential — give opposite recommendations; dominance reasoning conflicts with expected utility | Causal Decision Theory: use causal graphs and the *do*(Act) operator to fix the calculation |
| **Ellsberg Paradox** (Ambiguity) | People prefer known risk over unknown risk even when MEU says they should be indifferent — subjective probability cannot be consistently assigned to ambiguous events | Subjective probability (Savage) — *contested; no consensus defense* |
| **Reflection Effect** (Utility Shape) | People are risk-averse over gains but risk-seeking over equivalent losses — the utility curve cannot be consistently concave | **???** |

The first three attacks were at least partially answered. The last one was not. And it points to something deeper: not a flaw in how agents *apply* MEU, but a flaw in what MEU *assumes about human psychology.*

The core assumption MEU makes about utility: more wealth is always better, and the curve relating wealth to utility is consistent — typically concave (diminishing marginal returns), but at minimum stable. The Reflection Effect shows that this assumption breaks down. Our attitude toward risk is not a fixed property of our utility curve. It *flips* depending on whether we are thinking about gains or losses.

**2. Today's Agenda**

If this is an Engineering Failure, we need a better model. Today we build one: **Prospect Theory** (Kahneman & Tversky, 1979).

---

### II. The First Fix: Replacing Utility with Value

The core claim of Prospect Theory: humans do not evaluate outcomes based on their total final wealth. They evaluate outcomes relative to a **Reference Point** — their current situation, their expectation, or their aspiration.

**1. The Reference Point (Draw on Board)**

Consider three people:
- Person A earns $40,000/year and just received a $5,000 raise.
- Person B earns $100,000/year and just received a $5,000 raise.
- Person C earns $50,000/year, expected a $10,000 raise, and received $5,000.

Under MEU, we compare final wealth states. Person B is objectively wealthiest. But ask yourself: who *feels* the best? Person A likely does. Person C likely feels the worst — despite receiving the same raise as A.

**The lesson:** We do not evaluate outcomes. We evaluate *departures from expectations.*

**2. The Value Function (Draw the S-Curve)**

*[Instructor note: Draw the standard S-shaped curve. Reference point at the origin. Gains curve upward but flatten (concave). Losses curve downward but steepen (convex and asymmetric).]*

The formal value function v(x) has three key properties:

- **Defined over changes, not levels.** x is the change from the reference point, not total wealth.
- **Diminishing sensitivity.** Each additional dollar of gain (or loss) matters less than the previous one. The function is concave for gains and convex for losses. (We will see shortly that this single property formally explains the Reflection Effect — the observation that people are risk-averse over gains but risk-seeking over equivalent losses.)
- **Loss aversion.** The curve is steeper for losses than for gains. Empirically:

$$\lambda \approx 2.25$$

Losing $100 hurts roughly as much as gaining $225 feels good. Losses *loom larger* than equivalent gains.

**3. Chalk Talk: Feel the Asymmetry**

Ask the class: *"I will flip a fair coin. If it's tails, you lose $20. What guaranteed gain on heads would make you willing to accept the bet?"*

Poll responses. Answers will cluster around $40–$50 — far above the $20 needed for break-even. Point out: this gap is not pure risk aversion, which should be negligible for a small bet under MEU. It reflects loss aversion — the asymmetric shape of the value function.

---

### III. Loss Aversion in Action: The Reflection Effect

**1. The Setup (Poll the Class)**

Write these two problems on the board separately. Do not show both at once.

**Problem 1 (Gains):**
| Option | Outcome |
|---|---|
| A | A sure gain of $500 |
| B | 50% chance to gain $1,000 / 50% chance to gain $0 |

*Poll: Which do you prefer?* Most choose **A.** We are **risk-averse** over gains — we prefer the certain outcome even though both options have the same expected value ($500).

**Problem 2 (Losses):**
| Option | Outcome |
|---|---|
| C | A sure loss of $500 |
| D | 50% chance to lose $1,000 / 50% chance to lose $0 |

*Poll: Which do you prefer?* Most choose **D.** We are **risk-seeking** over losses — we prefer the gamble even though both options have the same expected value (−$500).

This reversal is called the **Reflection Effect.** Under MEU, it is a paradox: if you have a consistent, stable utility function, your attitude toward risk should not flip depending on whether outcomes are gains or losses. Under Prospect Theory, it is a *prediction.*

**2. The Explanation**

Look at the S-shaped curve you just drew:

- **Gains domain (above the reference point):** The curve is concave. Each additional dollar of gain matters *less* than the previous one. A certain gain feels better than a gamble with the same expected value. → **Risk Aversion.**
- **Losses domain (below the reference point):** The curve is convex. Each additional dollar of loss *also* matters less than the previous one — the pain of losing $1,000 is not twice the pain of losing $500. So a certain loss feels worse than a gamble that might save you from the loss entirely. → **Risk Seeking.**

The shape of the value function does all the work. The Reflection Effect is not an anomaly to be explained away — it is a structural prediction of the model.

**2. Chalk Talk: The Endowment Effect (Live Experiment)**

*[Instructor note: This works well as a live demonstration.]*

- Randomly distribute a small object — a pen, a coffee mug, a candy bar — to roughly half the students.
- Ask **owners**: "What is the minimum price you would accept to sell this?"
- Ask **non-owners**: "What is the maximum price you would pay to buy this?"

Historically, sellers demand roughly twice what buyers will pay — for the exact same object. (Thaler, Kahneman, Knetsch 1991.)

The explanation: once you own the mug, giving it up is a *loss* relative to your new reference point (ownership). Buying it is a *gain.* Because losses loom larger than gains (λ ≈ 2.25), sellers value what they already own more than buyers value what they might acquire.

MEU cannot explain this: rational markets should close this gap immediately, since the object has one objective value. PT predicts it precisely.

---

## Lecture Part 2: Probability Weighting, Framing, and Mental Accounting

### I. Warm-Up: The Asian Disease Problem

Write the following two versions of the same scenario on opposite sides of the board. Reveal only one to each half of the room, or present them sequentially after collecting votes.

**Version A (Gains Frame):**
> The U.S. is preparing for an unusual disease expected to kill 600 people. Two programs have been proposed.
> - Program A: 200 people will be saved.
> - Program B: 1/3 probability that 600 people will be saved; 2/3 probability that no one will be saved.

*Poll: Which do you prefer, A or B?*

Most choose **Program A** — the sure outcome.

**Version B (Losses Frame):**
> Same disease, 600 expected to die.
> - Program C: 400 people will die.
> - Program D: 1/3 probability that nobody will die; 2/3 probability that 600 will die.

*Poll: Which do you prefer, C or D?*

Most choose **Program D** — the gamble.

**The Reveal:** Program A and Program C are identical. Program B and Program D are identical. The only difference is the *frame*: Version A anchors on survival (gains), Version B anchors on death (losses). The frame shifts the reference point, which shifts the domain (gains vs. losses), which shifts the risk preference (averse vs. seeking).

**This is Framing.** Preferences are not stable objects we carry around — they are constructed in the moment, out of context.

---

### II. The Second Pillar: The Probability Weighting Function

So far, we have replaced the *utility function* with the *value function.* Prospect Theory makes a second equally radical move: humans do not use objective probabilities directly. We run probabilities through a **psychological distortion function** before we calculate.

**1. The Weighting Function π(p)**

*[Instructor note: Draw a graph with objective probability (0 to 1) on the x-axis and decision weight π(p) on the y-axis. Draw the 45° line first (MEU's assumption), then overlay the actual inverse-S curve.]*

- **Small probabilities are overweighted:** π(0.01) > 0.01. We treat a 1% chance more like a 5% chance. This is why people buy lottery tickets when the expected value is negative.
- **Large probabilities are underweighted:** π(0.99) < 0.99. We treat a 99% chance more like a 95% chance.
- **The endpoints (0 and 1) are treated categorically.** Zero-probability events are simply ignored. Certainty is treated as qualitatively different from any risk, no matter how small.

This last point is crucial. The jump from 99% to 100% is not perceived as a 1% increase. It is perceived as the elimination of risk entirely — a categorical leap that no marginal probability shift can match.

**2. The Certainty Effect, Explained**

One of the most studied violations of MEU involves what is called the **Certainty Effect** — the observation that people assign disproportionate weight to outcomes that are certain, compared to outcomes that are merely probable.

The classic demonstration is the **Allais Paradox.** Draw this on the board and poll the class:

| Choice | Ticket 1 (1%) | Tickets 2–11 (10%) | Tickets 12–100 (89%) |
|---|---|---|---|
| **Gamble 1** | $1M | $1M | $1M |
| **Gamble 2** | $0 | $5M | $1M |

*Most people prefer Gamble 1.* Now cover the "Tickets 12–100" column and show:

| Choice | Ticket 1 (1%) | Tickets 2–11 (10%) | Tickets 12–100 (89%) |
|---|---|---|---|
| **Gamble 3** | $1M | $1M | $0 |
| **Gamble 4** | $0 | $5M | $0 |

*Most people prefer Gamble 4.*

The problem: under MEU, the 89% column (Tickets 12–100) is identical in both comparisons and should cancel out. The choices between Gambles 1 & 2 and between Gambles 3 & 4 are *mathematically the same choice.* Preferring 1 over 2 and 4 over 3 simultaneously violates the Independence axiom — the formal core of MEU.

Under MEU, this is a contradiction. Under PT, it is a prediction. Gamble 1 is *certain* — it activates the categorical endpoint π(1.0), a weight that no risky gamble can match regardless of how high its probability climbs. The psychological leap from "99% safe" to "100% safe" is not a 1% improvement; it is the elimination of anxiety entirely. Gamble 4 no longer triggers that benefit, and at that point the larger $5M prize in Gamble 4 becomes the decisive factor.

**PT does not merely describe the Allais choices. It predicts them.**

**3. The Fourfold Pattern (Draw the 2×2 Grid)**

The combination of the value function and the probability weighting function produces a unified framework that explains a wide range of everyday choices that MEU cannot:

| | **Low Probability** | **High Probability** |
|---|---|---|
| **Gains** | Risk Seeking (e.g., buy lottery tickets — overweight the small chance of a big gain) | Risk Averse (e.g., accept a secure salary offer over a risky startup — prefer the near-certain good outcome) |
| **Losses** | Risk Averse (e.g., buy insurance — pay a certain premium to avoid the small chance of a catastrophic loss) | Risk Seeking (e.g., gamble to break even — the near-certain large loss feels so bad that a risky gamble looks worth it) |

Write on the board: **"The same person can rationally buy both lottery tickets and insurance."** MEU cannot explain this. PT can.

---

### III. Mental Accounting: Money Isn't Fungible

Richard Thaler observed that people do not treat all money as interchangeable — even though standard economic theory demands they should. Instead, we mentally organize money into separate "accounts" with different rules for spending and loss tolerance in each.

**1. The House Money Effect**

> Two people walk into a casino. Person A brought $200 of savings. Person B brought nothing but just won $200 at the slots an hour ago.

*Ask the class: who gambles more aggressively in the next hour?*

Empirically and intuitively: **Person B.** Why? Savings feel like "your money," governed by loss aversion in the gains domain. Winnings feel like "house money" — because the original reference point for Person B's wealth did not include those winnings, losing them does not register as a loss in the same psychological ledger. The mental account for "winnings" carries a different loss aversion coefficient than the account for "life savings."

**2. Sunk Costs as Locked Accounts**

> You bought a $100 concert ticket two months ago. The night of the show, you feel terrible and there's a blizzard. You wouldn't go to this concert for free under these conditions. Do you go anyway?

Most people go. MEU says: the $100 is gone regardless of your choice. Only future costs and benefits are decision-relevant. But humans have a locked "concert account" they feel compelled to drain.

The mental accounting explanation: abandoning the account feels like realizing a loss *in that account.* Staying home is losing $100. Going is breaking even. Loss aversion drives people into blizzards.

**3. Transaction Utility**

Thaler distinguishes two types of value in any purchase:

- **Acquisition Utility:** The value of the good itself (what MEU measures).
- **Transaction Utility:** The value of the *deal* — how much you're "winning" or "losing" relative to what you expected to pay.

> Would you walk 20 minutes to save $5 on a $10 item? Most say yes.
> Would you walk 20 minutes to save $5 on a $1,000 item? Most say no.

The savings are identical ($5). The transaction utility — the psychological sense of "winning" the deal — is far higher when $5 is half the price of an item than when it is half a percent.

---

### IV. Philosophical Conclusion: What Kind of Theory Is This?

Close by raising the question that will carry into next week.

**1. Descriptive vs. Normative**

Prospect Theory is explicitly a *descriptive* theory. Kahneman and Tversky were not prescribing how we should choose — they were modeling how we actually do choose.

This raises a deep philosophical question: **does a successful descriptive theory have normative implications?**

- **Option 1 (Savage's Ghost):** PT just catalogues our failures more precisely. The normative prescription remains MEU. Knowing our biases, we should correct for them — the way you mentally straighten the Müller-Lyer lines once you know they're equal.
- **Option 2 (The Engineer's View):** If PT is a better model of real human decision-making, then the normative theory of choice for a *finite human agent* might not be MEU. The "should" in rational choice must account for what we "can." A theory that demands the impossible is not a good prescriptive theory.

**2. The Bridge to Next Week**

Next week, we meet Daniel Dennett and the concept of **Bounded Rationality.** We will ask: what if the biases PT describes are not failures at all, but *features?* What if loss aversion, ambiguity aversion, and the certainty effect are evolved heuristics — "Moral First Aid" for agents who don't have time to run Bayesian updates while the tiger is charging?

Perhaps these "illusions" are not bugs in a system running the wrong code. Perhaps they are the right code, optimized for a world in which perfect calculation is never available.

---

## Week 6 Problem Set: Behavioral Decision Theory

**Topics:** Prospect Theory, Framing, Loss Aversion, Mental Accounting.
**Readings:** Baumgaertner Ch. 6, 12; Kahneman & Tversky (1979 / 1981).

---

### Type 1: Drill Exercises

*These problems focus on the mechanics of applying Prospect Theory and identifying its core components.*

**1. The Value Function in Action**

Recall that under **Maximizing Expected Utility (MEU)**, we evaluate an option by multiplying each outcome's utility by its probability and summing: $EU(A) = \sum p_i \cdot u(x_i)$. MEU assumes a single consistent utility function over final wealth levels.

Prospect Theory replaces this with a **value function** over *changes* from a reference point. Apply the following simplified version:
- **For gains (x > 0):** $v(x) = \sqrt{x}$ (concave — diminishing sensitivity)
- **For losses (x < 0):** $v(x) = -2\sqrt{|x|}$ (steeper — loss aversion, λ = 2)

Consider the following choices. *Assume objective probabilities for now (no probability weighting).*

| Option | Outcome |
|---|---|
| A | A sure gain of $100 |
| B | 50% chance to gain $400; 50% chance to gain $0 |

| Option | Outcome |
|---|---|
| C | A sure loss of $100 |
| D | 50% chance to lose $400; 50% chance to lose $0 |

*Tasks:*
1. Calculate the prospect theory value of each option (A, B, C, D).
2. Which option does PT recommend for the gains pair (A vs. B)? For the losses pair (C vs. D)?
3. Confirm that your results show **risk aversion in the domain of gains** and **risk seeking in the domain of losses.** Show your work.
4. Under MEU with risk-neutral preferences, what are the expected values of each option? Does MEU predict the same choices as PT here?

**2. Spotting the Reference Point**

For each scenario below, (i) identify the reference point the agent is most likely using, and (ii) determine whether the outcome is coded as a gain or a loss under that reference point.

a. A student expected a B on the exam and received an A−. Is the A− a gain or a loss?

b. A homeowner paid $400,000 for a house. The market dropped. She is offered $380,000. Is $380,000 a gain or a loss?

c. A shopper sees a jacket marked down from $200 to $130. Her budget was $150. Is the $130 price a gain or a loss?

d. An investor's portfolio is up $5,000 this month, but she had projected being up $8,000. Is the $5,000 gain coded as a gain or a loss?

---

### Type 2: "What-If" Exercises

*These problems encourage you to manipulate the structural assumptions of Prospect Theory.*

**3. What If the Frame Changes?**

A city council must respond to a projected budget shortfall of $6,000,000. Two proposals are on the table:
- **Option A:** Save $2,000,000 in services for certain.
- **Option B:** 1/3 chance of saving all $6,000,000 in services; 2/3 chance of saving nothing.

*Tasks:*
1. Using the gains frame above, PT predicts that most people choose Option A. Now *reframe* the scenario in terms of cuts rather than savings. Write out the losses-frame version, with logically equivalent options C and D.
2. Under the losses frame, which option does PT predict most people will prefer?
3. Are the two frames logically identical? Should a fully rational agent care which frame they encounter?
4. Give a real-world example where political or organizational actors deliberately exploit framing — without altering any underlying facts — to shift public preferences.

**4. Mental Accounting and the Sunk Cost**

You have purchased a non-refundable ski trip for $300. The weekend arrives and you feel ill — not dangerously, but enough to make the trip unpleasant. A friend offers you a free cabin for the same weekend, which you would objectively enjoy more. You cannot do both.

*Tasks:*
1. What does MEU recommend? Identify the decision-relevant costs and benefits going forward.
2. What does mental accounting predict you will actually do? Name the specific mental account at play and explain how loss aversion interacts with it to produce the predicted choice.
3. Now consider a variation: suppose you had *won* the ski trip in a raffle rather than purchasing it. Does mental accounting predict any difference in behavior? Why or why not? (Hint: consider the house money effect and how reference points are established.)

---

### Type 3: Puzzle/Paradox

**5. The Disposition Effect (Synthesis)**

You hold two stocks in your portfolio:
- **Stock W (Winner):** Purchased at $50/share; now worth $80/share (+$30).
- **Stock L (Loser):** Purchased at $50/share; now worth $30/share (−$20).

You need to sell one stock to raise cash. Empirically, investors overwhelmingly sell the winner and hold the loser. This is called the **Disposition Effect** — one of the most robustly documented anomalies in financial economics.

*Tasks:*
1. What reference point are investors using for each stock? What counts as a gain and what counts as a loss?
2. Use the **Reflection Effect** (people are risk-averse over gains but risk-seeking over losses, as established in lecture) and the shape of PT's value function to explain why investors prefer to sell Stock W and hold Stock L.
3. Standard finance theory says the purchase price is a sunk cost — economically irrelevant to your current decision. Using PT, explain what psychological mechanism makes the purchase price *feel* relevant even though it is not.
4. **Challenge:** If loss aversion systematically drives investors to hold losing stocks too long, is this a pure mistake — or could you construct an argument that it reflects some deeper form of rationality? Defend your position using concepts from the course.

**6. Does Prospect Theory Vindicate the Allais Choices?**

In lecture, you encountered the **Allais Paradox** — one of the most famous challenges to MEU. The setup involves two separate pair-wise choices from the same lottery table. Imagine 100 tickets are drawn. You must choose between options in each pair:

| Choice | Ticket 1 (1%) | Tickets 2–11 (10%) | Tickets 12–100 (89%) |
|---|---|---|---|
| **Gamble 1** | $1M | $1M | $1M |
| **Gamble 2** | $0 | $5M | $1M |

*First choice: Gamble 1 or Gamble 2?*

| Choice | Ticket 1 (1%) | Tickets 2–11 (10%) | Tickets 12–100 (89%) |
|---|---|---|---|
| **Gamble 3** | $1M | $1M | $0 |
| **Gamble 4** | $0 | $5M | $0 |

*Second choice: Gamble 3 or Gamble 4?*

The majority preference across both pairs is **Gamble 1 over Gamble 2** and **Gamble 4 over Gamble 3.**

Under MEU, this combination is mathematically inconsistent. The reason: MEU depends on the **Independence Axiom** (also called the Sure Thing Principle, or STP), which holds that if two options share an identical outcome under some set of states, those states are irrelevant to the comparison. In both tables, the 89% column (Tickets 12–100) is identical within each pair — it should drop out of both comparisons. But once you remove it, Gambles 1 vs. 2 and Gambles 3 vs. 4 reduce to *exactly the same choice.* Preferring 1 over 2 and 4 over 3 simultaneously is a contradiction under MEU.

Now examine whether Prospect Theory resolves the inconsistency or merely accommodates it.

*Tasks:*
1. Under PT's probability weighting function, explain why the jump from 99% to 100% (achieving certainty) is psychologically far larger than a 1% increase anywhere else on the probability scale. How does this explain the preference for Gamble 1 over Gamble 2?
2. In the Gamble 3 vs. Gamble 4 comparison, neither option offers certainty. Under PT, why does Gamble 4 now dominate? (Hint: compare the probability and magnitude of the $5M outcome across the two gambles in this pair.)
3. MEU condemns the majority preference as irrational. PT accommodates it as predictable. But is *accommodating* a preference pattern the same as *vindicating* it? Is there a coherent sense in which the Allais choices are still *wrong* — even if PT can model them? Defend your answer.
