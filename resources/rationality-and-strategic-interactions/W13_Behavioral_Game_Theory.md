# W13 Behavioral Game Theory — When Humans Deviate from Equilibrium

- Nash equilibrium is elegant. Humans are messy.
- Ultimatum Game: People reject unfair offers — even when it costs them money
- Dictator Game: People give to strangers — with no strategic reason
- Trust Game: People reward trust — and punish betrayal — at personal cost
- Level-k reasoning: People think some steps ahead, but not infinitely many
- Social preferences: We care about fairness, reciprocity, and relative outcomes
- The lesson: Homo economicus is a fiction. Real humans are social, emotional, and boundedly rational.

---

## Lecture Part 1: Three Games That Broke Game Theory

### I. The Bridge from Signaling to Behavior

**1. What We've Assumed So Far**

Write on the board:

| Week | Model of Agency | Key Prediction |
|---|---|---|
| W8-W10 | Rational choosers | Nash, subgame perfection |
| W11 | Evolution (no rationality) | ESS, replicator dynamics |
| W12 | Strategic information | Signaling equilibria |
| W13 | **Real humans** | ??? |

All of our models so far assume **perfect rationality** (or, in the evolutionary case, perfect selection). But real humans:
- Care about fairness, not just payoffs
- Punish unfairness, even at personal cost
- Trust strangers, even when it's "irrational"
- Think a few steps ahead, but not infinitely

Today we study what happens when game theory meets experimental data.

**2. The Method: Experimental Economics**

Starting in the 1980s, economists began running **controlled experiments** with real monetary incentives. The goal: Test whether game-theoretic predictions match actual behavior.

The finding: **Systematic deviations.** Not random noise — predictable, robust patterns that contradict standard theory.

**3. Today's Agenda**

We will study three canonical games:
1. **Ultimatum Game** — fairness vs. rationality
2. **Dictator Game** — pure altruism (or social norms?)
3. **Trust Game** — reciprocity and betrayal

Then we'll explore **level-k reasoning** (how many steps people actually think ahead) and **social preferences** (formal models of fairness, reciprocity, and inequality aversion).

---

### II. The Ultimatum Game — Fairness Beats Rationality

**1. The Game (Güth, Schmittberger, and Schwarze, 1982)**

Two players: Proposer and Responder.

- Proposer is given $10 and must offer some amount x to Responder (x can be 0 to 10).
- Responder can **Accept** or **Reject**.
- If Accept: Proposer gets $(10-x), Responder gets $x.
- If Reject: Both get $0.

Draw the game tree:

```
        Proposer
        Offer x
           |
        Responder
        /       \
    Accept      Reject
    /             \
(10-x, x)       (0, 0)
```

**2. The Rational Prediction**

Backward induction:
- Responder: For any x > 0, Accept gives x, Reject gives 0. So **Accept any x > 0**. (If x = 0, indifferent — assume Accept.)
- Proposer: Knowing Responder will accept any x > 0, **offer x = 0** (or x = 1, the smallest positive amount).

**Prediction:** Proposer offers 0 (or 1), Responder accepts.

**3. The Empirical Reality**

Draw on the board (histogram of offers):

```
Offer Amount    Frequency
$0-1            ||
$2-3            ||||
$4-5            ||||||||||||||||
$6-7            ||||
$8-10           ||
```

Typical findings (across cultures, stakes, contexts):
- **Modal offer: $5** (50% split)
- **Mean offer: $4-5**
- **Offers below $2:** Rare (10-15% of subjects)
- **Rejection rates:**
  - $5 offers: <5% rejected
  - $3-4 offers: 10-20% rejected
  - $1-2 offers: 40-60% rejected
  - $0 offers: >80% rejected

**4. What's Going On?**

Responders are willing to **pay to punish** unfairness. Rejecting a $1 offer costs the responder $1 — but it also costs the proposer $9. The responder is saying: "You were unfair, and I'm willing to sacrifice to punish you."

Proposers anticipate this — so they offer more.

But: Are proposers offering $5 because they're **fair**? Or because they're **strategic** (afraid of rejection)?

We need another game to separate these.

---

### III. The Dictator Game — Pure Altruism?

**1. The Game**

Same as Ultimatum, but: **Responder has no choice.** They must accept whatever the Proposer (now called "Dictator") offers.

- Dictator is given $10.
- Dictator chooses x to give to Receiver (x can be 0 to 10).
- Receiver has no say.
- Payoffs: Dictator gets $(10-x), Receiver gets $x.

**2. The Rational Prediction**

Dictator should offer **x = 0** (keep everything). There's no strategic reason to give anything.

**3. The Empirical Reality**

Typical findings:
- **Mean offer: $2-3** (20-30%)
- **Modal offer: $0** (but many give $5)
- **Distribution:**
  - ~30% give $0
  - ~20% give $5
  - ~50% give something in between

**4. Interpretation**

Since there's no strategic reason to give, giving must reflect:
- **Altruism:** Genuine concern for the other's welfare.
- **Social norms:** Internalized norms of fairness ("I should share").
- **Experimenter demand:** Subjects want to look good to the experimenter.

Evidence for each:
- Altruism: Giving persists even in anonymous, one-shot games.
- Social norms: Giving increases when subjects are reminded of fairness norms.
- Experimenter demand: Giving decreases in double-blind protocols (but doesn't disappear).

**5. Connection to Ultimatum**

Compare offers:

| Game | Mean Offer | Interpretation |
|---|---|---|
| Dictator | $2-3 | Altruism + norms |
| Ultimatum | $4-5 | Altruism + norms + **strategic fear of rejection** |

The difference (~$2) is the **strategic component** — what proposers give to avoid rejection.

---

### IV. The Trust Game — Reciprocity and Betrayal

**1. The Game (Berg, Dickhaut, and McCabe, 1995)**

Two players: Investor and Trustee.

- Investor is given $10.
- Investor chooses how much to send to Trustee (x from 0 to 10).
- Amount sent is **tripled** by the experimenter (Trustee receives 3x).
- Trustee chooses how much to return to Investor (y from 0 to 3x).
- Payoffs: Investor gets $(10 - x + y), Trustee gets $(3x - y).

Draw the game tree:

```
        Investor
        Send x
           |
        Trustee (receives 3x)
        Return y
           |
    Investor: 10 - x + y
    Trustee: 3x - y
```

**2. The Rational Prediction**

Backward induction:
- Trustee: For any x, keeping everything (y = 0) maximizes payoff. So **return y = 0**.
- Investor: Knowing Trustee will return 0, **send x = 0**.

**Prediction:** No trust, no trade. Both get $10 (Investor keeps endowment, Trustee gets nothing).

**3. The Empirical Reality**

Typical findings:
- **Amount sent:** Mean ~$5 (50% of endowment)
- **Amount returned:** Positively correlated with amount sent
  - For x = $5 (Trustee receives $15): Mean return ~$5-7
  - Higher sends are rewarded with higher returns
- **Reciprocity:** Trustees who receive more tend to return more (not just in absolute terms, but as a proportion)

**4. Interpretation**

- **Investors trust:** They send money, expecting something back.
- **Trustees reciprocate:** They return money, even though they don't have to.
- **Betrayal aversion:** Some investors send nothing — not because they're selfish, but because they fear being betrayed.

This is **positive reciprocity**: "You were good to me, so I'll be good to you."

There's also **negative reciprocity**: "You wronged me, so I'll wrong you back." (We saw this in the Ultimatum Game — responders rejecting unfair offers.)

---

## Lecture Part 2: Models of Bounded Rationality and Social Preferences

### I. Level-k Reasoning — How Many Steps Do People Think?

**1. The Beauty Contest Game (Keynes, 1936; Nagel, 1995)**

The game:
- Each player chooses a number between 0 and 100.
- The winner is the player whose number is closest to **2/3 of the average**.

Ask the class: *What number would you choose?*

**2. The Rational Prediction**

Iterated dominance:
- **Level 0:** Suppose some players choose randomly. Average ~50.
- **Level 1:** Best response to Level 0: 2/3 × 50 = 33.
- **Level 2:** Best response to Level 1: 2/3 × 33 = 22.
- **Level 3:** 2/3 × 22 = 15.
- ...
- **Limit:** 0.

The unique Nash equilibrium is **0**. (If everyone plays 0, the average is 0, and 2/3 of 0 is 0 — no one can do better.)

**3. The Empirical Reality**

Typical findings (from Nagel's experiments and many replications):

| Level | Reasoning | Choice | Approx. Frequency |
|---|---|---|---|
| **Level 0** | Random/naive | ~50 | 10-20% |
| **Level 1** | "Others are random" | 33 | 30-40% |
| **Level 2** | "Others are Level 1" | 22 | 20-30% |
| **Level 3+** | Deeper reasoning | 15 or lower | 5-10% |
| **Equilibrium** | Nash | 0 | 5-15% |

Mean choice: ~25-35 (depending on population).

**4. Interpretation**

People are **boundedly rational**:
- They think *some* steps ahead, but not infinitely.
- They model others as less sophisticated than themselves. (Level-k players typically assume others are Level k-1.)
- The distribution of reasoning depths varies by population (economists and game theorists play closer to equilibrium; undergraduates play at lower levels).

**5. The Cognitive Hierarchy Model**

A refinement: Players assume others are distributed across levels (Poisson distribution with mean τ). Best response is to optimize against this distribution.

This model fits data better than pure level-k (which assumes all players are exactly at one level).

---

### II. Social Preferences — Formal Models

**1. The Idea**

Standard theory: Agents care only about their own payoff.

Social preference models: Agents care about **relative payoffs**, **fairness**, **reciprocity**.

**2. Fehr-Schmidt Model (Inequality Aversion, 1999)**

Utility function for player i:

U_i(x) = x_i - α × (1/(n-1)) × Σ_{j≠i} max(x_j - x_i, 0) - β × (1/(n-1)) × Σ_{j≠i} max(x_i - x_j, 0)

Where:
- x_i = i's payoff
- α = disutility from being behind (envy)
- β = disutility from being ahead (guilt)
- Typically: α > β (pain from inequality hurts more when you're behind)

Interpretation:
- Players dislike inequality.
- They dislike being behind more than being ahead.
- This explains Ultimatum Game rejections (pain from unfairness outweighs the $1-2).

**3. Bolton-Ockenfels Model (ERC — Equity, Reciprocity, Competition, 2000)**

Similar idea: Utility depends on both absolute payoff and relative share.

**4. Rabin's Fairness Equilibrium (1993)**

Players care about **intentions**, not just outcomes.

- If I believe you intended to be kind, I want to be kind back.
- If I believe you intended to be mean, I want to be mean back.

This explains why the **same outcome** can be treated differently depending on how it arose:
- An offer of $2 might be accepted if the Proposer "earned" the right to propose (fair procedure).
- An offer of $2 might be rejected if the Proposer was randomly selected (unfair procedure).

**5. Charness-Rabin Model (2002)**

Combines inequality aversion with a concern for **social welfare**:

U_i = (1 - λ) × x_i + λ × [ρ × min(x_i, x_j) + (1-ρ) × (x_i + x_j)]

Where λ controls the weight on social concerns, and ρ controls Rawlsian vs. utilitarian preferences.

---

### III. Applications and Extensions

**1. Public Goods Games**

Setup:
- n players, each given endowment.
- Each contributes to a public pool.
- Pool is multiplied (e.g., 2×) and divided equally among all players.

Rational prediction: **Free-ride** (contribute 0). Everyone thinks: "My contribution is small, but I benefit from others' contributions."

Empirical reality:
- First round: Contributions ~50% of endowment.
- Subsequent rounds: Contributions decline (as free-riders are punished by reduced cooperation).
- With punishment option: Contributions stay high (players pay to punish free-riders).

**2. Centipede Game (Again)**

Recall Week 10: Backward induction says "stop immediately."

Empirical reality: Players continue for several rounds.

Explanation:
- **Altruism:** Players care about the other's payoff.
- **Reciprocity:** "If I continue, you might continue too."
- **Uncertainty about rationality:** "Maybe my opponent isn't perfectly rational — and that's good for both of us."

**3. Trust in the Real World**

The Trust Game models many real-world interactions:
- **Lending:** Bank (Investor) lends to borrower (Trustee). Borrower can repay or default.
- **Employment:** Employer (Investor) pays wages upfront. Employee (Trustee) can work hard or shirk.
- **Trade:** Seller (Investor) ships goods. Buyer (Trustee) can pay or not.

In all these contexts, **trust and reciprocity** enable mutually beneficial exchange — even when contracts are incomplete or enforcement is weak.

---

### IV. Philosophical Conclusion: Is Homo Economicus Dead?

Close by raising the philosophical question.

**1. The Two Views**

| View | Claim | Implication |
|---|---|---|
| **Homo Economicus is Dead** | Humans are not self-interested maximizers. We're social, fair-minded, reciprocal. | Game theory needs new foundations (social preferences, bounded rationality). |
| **Homo Economicus Lives** | The standard model is a useful approximation. Anomalies are context-dependent or can be modeled within the framework. | Refine the model (add social preferences as parameters), don't abandon it. |

**2. The Middle Ground**

Most researchers now accept:
- Pure self-interest is too narrow.
- But full-blown irrationality is also wrong — people respond to incentives, think strategically (to some degree), and learn from experience.
- The right model: **Boundedly rational agents with social preferences.**

**3. Connection to Earlier Weeks**

- **Week 6 (Prospect Theory):** Behavioral game theory is the strategic analog of prospect theory.
- **Week 7 (Dennett):** Bounded rationality and heuristics explain why people don't play equilibrium.
- **Week 8-12 (Game Theory):** The rational models are **normative** (how agents should play) but not always **descriptive** (how they do play).

**4. Bridge to Next Week**

Next week (our final week) we synthesize everything:
- How do commitment, reputation, and repeated interaction change the picture?
- What does the Moral First Aid Manual look like with behavioral game theory in hand?
- What have we learned about rationality, cooperation, and the human condition?

---

## Week 13 Problem Set: Behavioral Game Theory

**Topics:** Ultimatum Game, Dictator Game, Trust Game, Level-k Reasoning, Social Preferences (Fehr-Schmidt, Rabin).
**Readings:** Fehr & Schmidt (1999) on inequality aversion, Rabin (1993) on fairness, Camerer *Behavioral Game Theory* (excerpts).

---

### Type 1: Drill Exercises

**1. Fehr-Schmidt Calculations**

Suppose two players divide $10. Player 1 has Fehr-Schmidt preferences with α = 1 (envy) and β = 0.5 (guilt).

Utility: U_1(x_1, x_2) = x_1 - α × max(x_2 - x_1, 0) - β × max(x_1 - x_2, 0)

*Tasks:*
1. Calculate U_1 for the following splits (x_1, x_2): (10, 0), (7, 3), (5, 5), (3, 7), (0, 10).
2. Which split maximizes Player 1's utility?
3. Now suppose Player 1 is the Proposer in an Ultimatum Game. If Player 2 accepts any offer ≥ $2, what offer maximizes Player 1's utility?
4. If Player 2 rejects any offer < $4, what should Player 1 offer?

---

**2. Level-k Reasoning**

In the Beauty Contest game (choose a number 0-100, winner is closest to 2/3 of average):

*Tasks:*
1. What does a Level-0 player choose? (Assume random: 50)
2. What does a Level-1 player choose?
3. What does a Level-2 player choose?
4. What does a Level-3 player choose?
5. **Calculation:** If the population is 20% Level-0, 50% Level-1, 25% Level-2, and 5% Level-3, what is the average? What is 2/3 of the average? What should a Level-4 player choose?

---

### Type 2: "What-If" Exercises

**3. What If Stakes Change?**

In the Ultimatum Game, most experiments use stakes of $10-100. What happens with higher stakes?

*Tasks:*
1. **Prediction:** If stakes are $1,000,000, what does standard theory predict? What does Fehr-Schmidt predict?
2. **Empirical evidence:** Studies with high stakes (e.g., in developing countries, where $100 is a month's wages) find:
   - Offers remain around 40-50%
   - Rejection rates for low offers remain high

   Does this surprise you? Why or why not?

3. **What If stakes are negative?** (Players must *pay* rather than receive money.) How would you design an Ultimatum Game with negative stakes? What would you predict?

---

**4. What If Players Can Communicate?**

In the Trust Game, suppose the Investor and Trustee can exchange messages before the game.

*Tasks:*
1. **Prediction:** Standard theory says cheap talk shouldn't matter. Why?
2. **Empirical finding:** Communication increases trust (Investors send more) and trustworthiness (Trustees return more). Why?
3. **Mechanism:** Is it because communication:
   - Changes preferences (makes fairness salient)?
   - Creates promises (which people feel bound to keep)?
   - Signals type (trustworthy Trustees identify themselves)?
   - Something else?

4. **Design:** Propose an experiment to distinguish between these mechanisms.

---

### Type 3: Puzzle/Paradox

**5. The Paradox of Altruistic Punishment**

In Public Goods Games with punishment:
- Players can pay $1 to reduce another player's payoff by $3.
- Rational prediction: No one punishes (costly, no benefit).
- Empirical reality: Players punish free-riders — and contributions stay high.

*The Paradox:* Punishment is individually costly. Why do people do it? And why does it sustain cooperation?

*Tasks:*
1. Explain why punishment is a **second-order free-rider problem**. (First-order: contributing to the public good. Second-order: punishing those who don't contribute.)
2. One solution: **Group selection.** Groups with punishers outcompete groups without. Is this plausible? Why or why not?
3. Another solution: **Strong reciprocity** — some people have an intrinsic preference for punishing norm-violators. Is this a satisfying explanation?
4. **Philosophical question:** Is altruistic punishment morally good (enforcing norms) or bad (vigilante justice)?

---

**6. The Traveler's Dilemma (Again)**

Recall Week 8: Traveler's Dilemma has a unique Nash equilibrium at the minimum claim, but most people play much higher.

*Tasks:*
1. Re-analyze the Traveler's Dilemma using level-k reasoning:
   - What does a Level-0 player do?
   - What does a Level-1 player do?
   - At what level does a player choose the Nash equilibrium?

2. **Fehr-Schmidt analysis:** If players care about fairness (equal claims), does this explain high claims?

3. **Comparison:** Which model fits better — level-k or social preferences?

4. **Philosophical question:** Is the Nash equilibrium "wrong" — or are the subjects "wrong"? Which standard should we use?

---

### Type 4: Applied Analysis

**7. Behavioral Economics in Policy**

Governments and organizations use behavioral insights to design policies:
- **Default options:** Automatic enrollment in retirement plans (with opt-out).
- **Nudges:** Placing healthy food at eye level.
- **Social norms messaging:** "90% of people pay taxes on time."

*Tasks:*
1. How do these policies exploit behavioral biases? (Identify the specific bias each targets.)
2. **Ultimatum Game application:** How might fairness concerns affect tax compliance? Design a policy that leverages fairness norms.
3. **Trust Game application:** How might a government increase trust in public institutions? What signals credibility?
4. **Ethical question:** Is it manipulative to use behavioral insights in policy? Or is it legitimate to design policies that work with (not against) human nature?

---

**8. Wage Fairness and Labor Markets**

Firms often pay above-market wages — even when they could hire workers for less.

*Tasks:*
1. **Standard explanation:** Efficiency wages (higher wages increase productivity by reducing turnover, attracting better workers, etc.)
2. **Behavioral explanation:** Fairness norms. Workers who feel underpaid reduce effort (negative reciprocity). Workers who feel well-paid increase effort (positive reciprocity).

   Model this as a Trust Game: Firm (Investor) pays wage w. Worker (Trustee) chooses effort e. Payoffs depend on w and e.

3. **Prediction:** What happens if a firm cuts wages during a recession?
   - Standard theory: Workers accept (better than unemployment).
   - Behavioral theory: Workers may resent the cut and reduce effort.

4. **Real-world example:** Costco pays ~$20/hour; Walmart pays ~$15/hour. Costco has lower turnover and higher productivity. Is this evidence for behavioral models? Or can it be explained standardly?

---

**9. Negotiation and Bargaining**

Negotiation is a real-world Ultimatum/Trust Game hybrid.

*Tasks:*
1. **Ultimatum component:** One party makes an offer; the other can accept or reject (walk away).
2. **Trust component:** Parties may make promises ("I'll deliver next week") that aren't legally binding.

   How do fairness concerns and reciprocity affect negotiation outcomes?

3. **Advice:** Based on behavioral game theory, what advice would you give to a negotiator?
   - Should you make the first offer?
   - Should you anchor high or be "fair"?
   - How do you build trust?

4. **Case study:** Read about a failed negotiation (e.g., a strike, a business deal that fell through). Analyze it using behavioral concepts. Was the failure due to:
   - Perceived unfairness?
   - Lack of trust?
   - Overconfidence?
   - Something else?

---

**10. AI and Behavioral Alignment**

AI systems interact with humans in strategic contexts. Should AI be designed to play like a rational agent — or like a human?

*Scenario:* An AI assistant helps a user negotiate a salary.

*Tasks:*
1. **Rational AI:** Maximizes expected salary. Makes aggressive demands. Risks impasse.
2. **Behavioral AI:** Accounts for fairness norms. Makes "reasonable" demands. Maintains relationship.

   Which approach is better? Why?

3. **Trust Game with AI:** If a human plays Trust Game against an AI, how should the AI behave?
   - As Trustee: Should it reciprocate (even though it doesn't "care" about money)?
   - As Investor: Should it trust the human?

4. **Philosophical question:** If an AI simulates social preferences (fairness, reciprocity) without genuinely feeling them, is it "deceiving" humans? Or is it appropriately adapting to human norms?

---

**11. Synthesis: Behavioral Game Theory and the Course**

We are now at the end of our game theory unit. Synthesize what we've learned.

*Tasks:*
1. **Compare predictions across models:**

| Game | Rational Prediction | Behavioral Prediction | Which Fits Data? |
|---|---|---|---|
| Ultimatum | Offer 0-1, accept any | Offer 4-5, reject low | ??? |
| Dictator | Offer 0 | Offer 2-3 | ??? |
| Trust | Send 0, return 0 | Send 5, return ~50% | ??? |
| Centipede | Stop immediately | Continue several rounds | ??? |

Fill in the table. What's the overall pattern?

2. **Normative vs. Descriptive:**
   - Is game theory a **normative** theory (how agents should play)?
   - Is it a **descriptive** theory (how agents do play)?
   - Can it be both? Should it be?

3. **Connection to Weeks 6-7:**
   - Prospect Theory (W6): How does loss aversion affect Ultimatum Game rejections?
   - Dennett (W7): How does satisficing relate to level-k reasoning?

4. **Connection to Weeks 8-12:**
   - PD (W8): Do social preferences "solve" the PD?
   - Coordination (W9): Do focal points matter more or less with behavioral players?
   - Sequential (W10): Is backward induction normatively correct but descriptively wrong?
   - Evolution (W11): Can social preferences evolve?
   - Signaling (W12): Do behavioral players signal differently?

5. **Final reflection:** What is the most important thing you've learned about rationality, cooperation, or human nature in this course?

---

## Appendix: Instructor Notes

### Suggested In-Class Activities

**1. Live Ultimatum Game**

Pair students. Randomly assign Proposer and Responder roles. Give Proposers $10 (real or hypothetical) to split. Collect offers and responses.

Aggregate results and compare to typical findings. Discuss: Why did Responders reject? Why did Proposers offer what they did?

**2. Beauty Contest Game**

Have all students choose a number 0-100. Calculate 2/3 of the average. Announce the winner.

Discuss: What level of reasoning did you use? What did you think others would do?

**3. Trust Game Demonstration**

Pair students. Play Trust Game with real or hypothetical money. Track how much is sent and returned.

Discuss: Why did Investors trust? Why did Trustees reciprocate (or not)?

---

### Common Student Misconceptions

1. **"Behavioral = irrational."** No — behavioral players are often rational *given their preferences* (which include fairness, reciprocity, etc.).

2. **"Social preferences mean people are nice."** No — social preferences include negative reciprocity (spite, punishment). People punish unfairness even at personal cost.

3. **"Level-k means people are stupid."** No — level-k is about *strategic depth*, not intelligence. Even very smart people may not assume others are infinitely rational.

4. **"Behavioral models can't be formalized."** False — Fehr-Schmidt, Rabin, and other models are mathematically precise.

---

### Connections to Other Course Topics

| Week | Connection |
|---|---|
| W6 (Prospect Theory) | Loss aversion explains why unfair offers feel painful. |
| W7 (Dennett) | Bounded rationality explains limited strategic depth. |
| W8 (PD) | Social preferences can sustain cooperation without iteration. |
| W9 (Coordination) | Focal points matter more when players are boundedly rational. |
| W10 (Sequential) | Backward induction fails empirically (Centipede, Trust Game). |
| W11 (Evolution) | Social preferences can evolve (group selection, reciprocity). |
| W12 (Signaling) | Fairness concerns affect signaling behavior. |

---

## Preview of Next Week (Final Week)

Next week we synthesize the entire course:
- What is rationality? (Weeks 1-5: Decision theory; Weeks 6-7: Behavioral critiques; Weeks 8-13: Game theory)
- What is cooperation? (PD, Stag Hunt, evolutionary models, behavioral models)
- What is the Moral First Aid Manual for strategic agents?
- How do all the pieces fit together?

Bring your questions, your insights, and your skepticism. This is where we tie it all together.
