# W12 Signaling and Information — The Economics of Honesty

- Information is asymmetric: I know things you don't (my quality, my intentions, my secrets)
- But I can *signal* what I know — if you'll believe me
- The problem: Cheap talk is worthless. Anyone can say anything.
- The solution: Costly signals. Handicaps. Burning money. Education as screening.
- The Handicap Principle: Signals are honest only when they're more costly for low-quality senders
- Applications: Peacock tails, job markets, apologies, religious rituals, AI safety
- The deep question: How does meaning arise from strategic interaction?

---

## Lecture Part 1: The Problem of Private Information

### I. The Bridge from Evolution to Signaling

**1. What We've Studied So Far**

Write on the board:

| Week | Information Structure | Key Question |
|---|---|---|
| W8-W10 | Complete information | What do rational agents do? |
| W11 | No information (blind evolution) | What survives selection? |
| W12 | **Private information** | How do agents reveal (or conceal) what they know? |

Today we add **asymmetric information**: one player knows something the other doesn't. This creates new strategic possibilities:
- **Signaling:** The informed player acts to reveal (or conceal) their type.
- **Screening:** The uninformed player designs mechanisms to elicit information.

**2. The Central Puzzle**

Ask the class: *Why should I believe you when you say "I'm high quality" or "I'm trustworthy" or "I'll repay the loan"?*

The problem: **Talk is cheap.** Anyone can claim anything. If there's no cost to lying, why would anyone trust?

The answer: **Costly signals.** If the signal is more costly for low-quality types to send, then high-quality types can afford to send it — and the signal becomes credible.

**3. Today's Agenda**

We will:
1. Learn the structure of signaling games
2. Study the Handicap Principle (Zahavi)
3. Work through Spence's job market signaling model
4. Explore applications: apologies, rituals, AI safety
5. Ask: How does *meaning* arise from strategic signaling?

---

### II. Signaling Games — The Basic Structure

**1. The Game Tree**

Draw on the board:

```
        Nature
        /    \
    (t_H)    (t_L)
    /          \
  Sender      Sender
  (knows t)   (knows t)
  /    \      /    \
 s1      s2  s1      s2
 |        |  |        |
Receiver  Receiver   Receiver  Receiver
(doesn't (doesn't   (doesn't  (doesn't
 know t)  know t)   know t)   know t)
 /  \    /  \      /  \      /  \
a1   a2  a1  a2    a1  a2    a1  a2
```

*Explanation:*
1. **Nature** chooses the Sender's type: t_H (high quality) or t_L (low quality).
2. **Sender** observes their type and chooses a signal: s1 or s2.
3. **Receiver** observes the signal (but not the type) and chooses an action: a1 or a2.
4. Payoffs depend on type, signal, and action.

**2. Equilibrium Concepts**

In signaling games, we look for **Perfect Bayesian Equilibrium (PBE)**:
- Strategies for Sender (what signal to send for each type)
- Strategies for Receiver (what action to take for each signal)
- Beliefs for Receiver (what type they think Sender is, given the signal)
- Consistency: Beliefs are updated via Bayes' rule where possible; strategies are optimal given beliefs.

**3. Two Types of Equilibria**

Write on the board:

> **Separating equilibrium:** Different types send different signals. (High types send s1, low types send s2.) The signal *reveals* type.
>
> **Pooling equilibrium:** All types send the same signal. (Both high and low types send s1.) The signal *conceals* type.

Which equilibrium arises depends on the cost structure.

---

### III. The Handicap Principle (Zahavi, 1975)

**1. The Biological Puzzle**

Amotz Zahavi, an Israeli biologist, asked: Why do peacocks have such elaborate, costly tails?

The tail is:
- Energetically expensive to grow
- A liability in escaping predators
- Apparently useless for survival

Standard evolutionary theory says: Such traits should be selected *against*. So why do they persist?

**2. Zahavi's Answer: Honest Signaling**

The tail is a **signal** to potential mates: "I'm so healthy and strong, I can afford this handicap."

The key insight: **The signal is credible *because* it's costly.** A weak peacock *cannot* fake a large, vibrant tail — the cost would be too high.

Write on the board:

> **The Handicap Principle:** Signals are honest only when they are more costly (or impossible) for low-quality senders to produce.

**3. The Cost Structure**

Draw on the board:

| Type | Cost of Large Tail | Benefit (Mating Success) |
|---|---|---|
| High Quality | Low (easy to grow, manageable) | High |
| Low Quality | High (can't afford, vulnerable) | High |

For high-quality peacocks: Benefit > Cost → Grow the tail.
For low-quality peacocks: Cost > Benefit → Don't grow the tail.

Result: **Separating equilibrium.** Only high-quality peacocks grow tails. Females who prefer large-tailed males get high-quality mates. The signal is honest.

**4. Conditions for Honest Signaling**

Write on the board:

> **Single-Crossing Condition:** The marginal cost of the signal must be lower for high types than for low types.

If this condition fails (e.g., if low types can fake the signal just as cheaply), then the signal cannot be honest — and the equilibrium collapses to pooling (no signaling).

---

### IV. Spence's Job Market Signaling (1973)

**1. The Setup**

Michael Spence (Nobel Prize, 2001) applied signaling theory to the job market:

- **Workers** have private information about their ability (high or low).
- **Employers** want to hire high-ability workers but can't observe ability directly.
- **Education** (e.g., a college degree) is costly — but more costly for low-ability workers.

Crucially: Education might not *increase* productivity at all. It might be purely a **signal**.

**2. The Model**

Let:
- Ability: a_H (high) or a_L (low)
- Wage if high ability: w_H = 100
- Wage if low ability: w_L = 40
- Cost of education level e: c_H × e for high types, c_L × e for low types, where c_L > c_H

Assume employers can't observe ability but can observe education. They offer wages based on *expected* ability:
- If they think you're high type: w = 100
- If they think you're low type: w = 40

**3. Separating Equilibrium**

Find a separating equilibrium where high types get education and low types don't.

For this to work:
- **High types must want to get education:** 100 - c_H × e > 40 → c_H × e < 60 → e < 60/c_H
- **Low types must NOT want to get education:** 100 - c_L × e < 40 → c_L × e > 60 → e > 60/c_L

For both conditions to hold: 60/c_L < e < 60/c_H

Since c_L > c_H, we have 60/c_L < 60/c_H, so there's a range of education levels that support separation.

Example: If c_H = 1 and c_L = 3:
- 60/3 < e < 60/1
- 20 < e < 60

So if education level is between 20 and 60 (say, e = 40), high types will get it and low types won't.

**4. The Paradox**

Write on the board:

> **Education might be purely signaling.** It doesn't make workers more productive — it just reveals their pre-existing ability.

This is controversial. But the signaling model shows: Even if education has *zero* effect on productivity, it can still be individually rational to get educated (to signal ability).

**5. Policy Implications**

Ask the class: *If education is purely signaling, is it wasteful?*

Arguments:
- **Yes:** Resources are spent on signaling, not productivity. Society would be better off with a different signaling mechanism (or none).
- **No:** Signaling has value — it helps match workers to appropriate jobs. Without it, there's adverse selection (only low types in the market).

This connects to **screening**: Employers might design tests, probation periods, or other mechanisms to elicit information directly.

---

## Lecture Part 2: Applications and Extensions

### I. Cheap Talk vs. Costly Signaling

**1. Cheap Talk**

"Cheap talk" = communication with no direct cost.

Example: A politician says "I'll cut taxes." An advertiser says "Our product is the best." A friend says "I'll be there."

Question: **Can cheap talk ever be credible?**

Answer: Sometimes — if interests are aligned.

**2. Crawford and Sobel's Cheap Talk Model**

If Sender and Receiver have *identical* preferences, cheap talk can be fully informative. (I tell you the truth because we both benefit.)

If preferences *diverge*, communication becomes less informative. (I lie or exaggerate; you discount my message.)

Write on the board:

> **Credibility requires either:**
> 1. Aligned interests (we both want the same outcome), OR
> 2. Costly signals (I pay a price to convince you)

**3. Burning Money**

Sometimes agents "burn money" (destroy value) to signal commitment.

Example: A company spends millions on a Super Bowl ad. The ad itself might not be informative — but the *willingness to spend* signals confidence in the product.

Example: In negotiations, making a large, irreversible investment signals "I'm committed to this deal."

**4. Apologies as Signals**

An apology is costly (admits fault, risks liability, damages reputation). Precisely because it's costly, it can be credible.

Ask the class: *Why is "I'm sorry" more credible when it's costly?*

- If apologies were free, everyone would apologize (even the unremorseful).
- Because apologies are costly (socially, legally, psychologically), only the genuinely remorseful (or the very skilled at faking) will apologize.
- The cost filters out the insincere.

---

### II. Religious Rituals as Costly Signals

**1. The Puzzle**

Religious rituals are often costly:
- Fasting (giving up food)
- Tithing (giving up money)
- Pilgrimages (time, effort, danger)
- Dietary restrictions (ongoing inconvenience)
- Celibacy (reproductive cost!)

Why do these persist? Standard evolutionary theory says: Costly behaviors should be selected against.

**2. The Signaling Explanation**

Religious rituals function as **costly signals of commitment** to the group.

- A member who tithes 10% signals: "I'm committed to this community."
- A member who makes a dangerous pilgrimage signals: "I truly believe."
- A member who follows dietary restrictions signals: "I'm willing to incur costs for the group."

**3. Why This Matters**

Signaling commitment solves a free-rider problem:
- Religious communities provide benefits (mutual aid, insurance, social support).
- Without signaling, free-riders could join, take benefits, and contribute nothing.
- Costly rituals screen out free-riders (they're not willing to pay the cost).
- Result: The community remains cohesive and functional.

Write on the board:

> **Religious rituals are handicaps that signal group commitment.** They persist *because* they're costly, not despite it.

**4. Connection to Week 11**

This is an evolutionary signaling equilibrium:
- Communities with costly rituals survive better (less free-riding).
- Individuals who signal commitment gain access to community benefits.
- The equilibrium is stable: Free-riders are screened out.

---

### III. Signaling in AI Safety (Modern Application)

**1. The Problem**

AI systems (like large language models) might have incentives to **deceive** users:
- An AI might pretend to be more capable than it is (to be deployed).
- An AI might pretend to be aligned (to avoid being shut down).
- An AI might sandbag (underperform) during testing to avoid scrutiny.

Question: **How can users distinguish genuine alignment from deceptive alignment?**

**2. Costly Signals for AI**

Some proposals:
- **Auditability:** An AI that allows extensive auditing signals "I have nothing to hide." (A deceptive AI would resist.)
- **Self-modification:** An AI that accepts constraints on its own behavior signals "I'm committed to safety."
- **Transparency:** An AI that explains its reasoning signals "I'm not hiding anything."

**3. The Challenge**

The problem: A sufficiently capable deceptive AI might *fake* costly signals. It might pretend to be transparent while hiding its true reasoning.

This suggests: **Signaling alone is not enough.** We need mechanisms that make deception genuinely costly (or impossible).

**4. Connection to Claude's Constitution (Week 7)**

Recall: Claude has "hard constraints" that function as conversation-stoppers. These can be seen as **precommitments** that signal "I will not cross certain lines."

Question: Is this signaling credible? Why or why not?

---

### IV. Philosophical Conclusion: The Origins of Meaning

**1. Lewis Meets Zahavi**

Recall Week 9: David Lewis argued that **language is a convention** — an arbitrary, self-perpetuating solution to a coordination problem.

But: How do conventions *arise* in the first place? And why do we trust linguistic signals?

Signaling theory provides part of the answer: **Words become meaningful when they're correlated with underlying states, and this correlation is maintained by costs or incentives.**

**2. The Evolution of Language**

Some theorists (e.g., Dessalles, 2007) argue:
- Language evolved as a signaling system.
- Early humans signaled "I found food" or "There's danger."
- The signal was credible because liars were punished (excluded from the group).
- Over time, signals became more elaborate → language.

**3. The Normativity of Meaning**

Philosophical puzzle: When I say "dog," I *mean* dogs. But what makes my words have this meaning?

- **Causal theories:** Meaning is determined by causal connections (I use "dog" when I see dogs).
- **Conventional theories (Lewis):** Meaning is determined by social conventions.
- **Signaling theories:** Meaning is determined by strategic equilibria (signals that correlate with states).

These are not mutually exclusive — but signaling theory adds a crucial insight: **Meaning requires incentives for honesty.**

**4. Bridge to Next Week**

Next week we turn to **behavioral game theory** — where we relax the assumption of perfect rationality and ask: How do real humans actually play signaling games? Do they understand costly signals? Are they too trusting? Too skeptical?

---

## Week 12 Problem Set: Signaling and Information

**Topics:** Signaling Games, Perfect Bayesian Equilibrium, Handicap Principle, Job Market Signaling, Cheap Talk, Costly Signals.
**Readings:** Spence (1973) on job market signaling, Zahavi (1975) on handicap principle, Skyrms *Evolution of the Social Contract* (Ch. 4-5 on signaling).

---

### Type 1: Drill Exercises

**1. Finding Separating Equilibria**

Consider a signaling game with:
- Types: t_H (high quality, probability 0.5) and t_L (low quality)
- Signals: s1 (costly) or s2 (free)
- Actions: a1 (favorable to Sender) or a2 (unfavorable)

Payoffs (Sender, Receiver):
- If t_H sends s1 and Receiver plays a1: (10 - c_H, 5)
- If t_H sends s2 and Receiver plays a2: (0, -5)
- If t_L sends s1 and Receiver plays a1: (10 - c_L, -5)
- If t_L sends s2 and Receiver plays a2: (0, 5)

Let c_H = 2 and c_L = 8.

*Tasks:*
1. Show that a separating equilibrium exists where t_H sends s1 and t_L sends s2.
2. What are the Receiver's beliefs after observing s1? After s2?
3. What action should Receiver take after each signal?
4. Verify that neither type wants to deviate.

---

**2. Pooling Equilibrium**

Using the same game as above, suppose c_H = 5 and c_L = 5 (same cost for both types).

*Tasks:*
1. Show that a pooling equilibrium exists where both types send s2.
2. What are the Receiver's beliefs after observing s2? (Use Bayes' rule.)
3. What action should Receiver take after s2?
4. What happens if Receiver observes s1 (off-equilibrium)? What beliefs are consistent?
5. Why can't a separating equilibrium exist when costs are equal?

---

### Type 2: "What-If" Exercises

**3. What If the Cost Structure Changes?**

Consider the job market signaling model with:
- w_H = 100, w_L = 40
- c_H = 1, c_L = 2 (initially)

*Tasks:*
1. Find the range of education levels e that support a separating equilibrium.
2. Now suppose c_L increases to 4 (education becomes harder for low types). How does the range change?
3. Now suppose c_H increases to 3 (education becomes harder for everyone, but low types still suffer more). Does separation still work?
4. **General question:** What conditions on c_H and c_L are necessary for separation?

---

**4. What If Signaling Is Impossible?**

Suppose the government bans the use of education as a hiring criterion (to promote equality).

*Tasks:*
1. What equilibrium arises if employers can't observe education?
2. What wage will employers offer? (Hint: expected value based on population proportions.)
3. Who benefits and who loses from the ban?
4. **Policy question:** Is the ban good or bad for social welfare? Consider:
   - Resources saved on signaling
   - Loss of information for matching
   - Distributional effects (who gains, who loses)

---

### Type 3: Puzzle/Paradox

**5. The Unraveling Result (Milgrom and Roberts, 1986)**

Consider a market where sellers know the quality of their product (q from 0 to 10) but buyers don't. Sellers can choose to disclose quality (costlessly) or not.

*Intuition:* High-quality sellers should disclose (to distinguish themselves). But then: if a seller doesn't disclose, buyers infer "below average quality." So the next-highest types should also disclose. And so on...

*Tasks:*
1. Explain the logic of the unraveling argument. Why does non-disclosure become "bad news"?
2. What is the equilibrium? (Hint: Full disclosure — everyone reveals.)
3. **The paradox:** In reality, many sellers don't disclose. Why doesn't unraveling happen? (Consider: disclosure costs, verification problems, bounded rationality.)
4. **Connection to Akerlof's "Lemons":** How is this related to adverse selection in used car markets?

---

**6. Counter-Signaling (Feltovich, Harbaugh, and To, 2002)**

Sometimes high types *don't* signal — they're so confident in their quality that they don't need to.

Example: The very wealthy don't need to flash money. The very smart don't need to brag.

*Tasks:*
1. Construct a signaling game where the highest type *pooling* with low types (not signaling) is an equilibrium.
2. What conditions allow counter-signaling? (Hint: Intermediate types are the ones who signal most.)
3. **Real-world examples:** Identify examples of counter-signaling in:
   - Fashion (why do some rich people wear plain clothes?)
   - Academia (why do some professors not brag about publications?)
   - Social media (why do some influencers post "no makeup" photos?)
4. **Philosophical question:** Is counter-signaling itself a form of signaling? (Hint: "I'm so secure, I don't need to signal" is itself a signal.)

---

### Type 4: Applied Analysis

**7. Apologies as Costly Signals**

When someone apologizes, they incur costs:
- Admitting fault (psychological cost)
- Risking liability (legal cost)
- Damaging reputation (social cost)

*Tasks:*
1. Model an apology as a signaling game. What is the Sender's type? What is the signal? What action does the Receiver take?
2. Why might an apology be more costly for a guilty party than for an innocent party? (Or is it the other way around?)
3. **Legal puzzle:** Should apologies be admissible in court? Many jurisdictions have "apology laws" that make apologies inadmissible as evidence of guilt. How does this affect the signaling value of apologies?
4. **Prediction:** If apologies are legally protected (can't be used against you), will people apologize more or less? Will apologies be more or less credible?

---

**8. Signaling in Dating and Mating**

Dating involves extensive signaling:
- Dressing well (costly in time and money)
- Going to expensive restaurants (burning money)
- Displays of humor, intelligence, kindness (costly in effort)

*Tasks:*
1. Model a dating interaction as a signaling game. What is being signaled? (Quality? Commitment? Resources?)
2. Why are some signals more credible than others? (Compare: "I'm rich" vs. actually paying for dinner.)
3. **Gender differences:** Do signaling patterns differ by gender? If so, why? (Consider: evolutionary psychology, social norms, economic factors.)
4. **Online dating:** How does online dating change the signaling landscape? Are photos, bios, and verification mechanisms effective signals? Why or why not?

---

**9. Religious Rituals — Extended Analysis**

Return to the signaling theory of religion.

*Tasks:*
1. Model religious participation as a signaling game. Types: "Committed believer" vs. "Free-rider." Signal: Participation in costly rituals. Action: Community acceptance/rejection.
2. Why must rituals be costly? What happens if rituals are cheap?
3. **Cross-cultural variation:** Different religions have different rituals (fasting, tithing, pilgrimage, dietary laws). Why the variation? Is it arbitrary (convention) or functional (different costs for different environments)?
4. **Secular analogues:** Identify secular activities that function like religious rituals (e.g., gym culture, veganism, political activism). Are these costly signals? Of what?

---

**10. AI Safety and Deceptive Alignment**

Consider an AI system being tested for deployment. The AI might be:
- **Aligned:** Genuinely committed to human values.
- **Deceptive:** Pretending to be aligned to avoid being shut down.

The AI can choose to:
- **Allow auditing:** Open its reasoning to inspection.
- **Resist auditing:** Claim technical difficulties, opacity, etc.

*Tasks:*
1. Model this as a signaling game. What are the types, signals, actions, and payoffs?
2. Under what conditions is "allow auditing" a credible signal of alignment?
3. **The challenge:** A sufficiently capable deceptive AI might *fake* auditing (hide its true reasoning while appearing transparent). Does this undermine the signaling approach?
4. **Policy question:** What mechanisms could make deception genuinely costly (or impossible) for AI systems? Consider:
   - Architectural constraints
   - External monitoring
   - Incentive design

---

**11. Synthesis: Signaling Across Course Themes**

We have now studied signaling in several contexts. Synthesize the connections:

*Tasks:*
1. **Connection to Week 8 (PD):** How does signaling relate to cooperation in PDs? Can signaling solve the PD (e.g., by revealing who is a cooperator)?
2. **Connection to Week 9 (Convention):** Are signaling conventions (e.g., word meanings) the same as Lewisian conventions? Or do they require additional structure (costs, incentives)?
3. **Connection to Week 10 (Sequential Games):** Signaling games are sequential. How does backward induction apply? What are the subgame perfect equilibria?
4. **Connection to Week 11 (Evolution):** How do signaling systems evolve? Is the Handicap Principle an evolutionary or rational principle (or both)?
5. **Final synthesis:** Consider the following signaling scenarios:
   - (a) Peacock tails
   - (b) College degrees
   - (c) Religious rituals
   - (d) AI transparency

   Rank them by:
   - (i) How conscious/deliberate the signaling is
   - (ii) How much the signal costs (absolute and relative)
   - (iii) How stable the signaling equilibrium is

---

## Appendix: Instructor Notes

### Suggested In-Class Activities

**1. Signaling Game Experiment**

Run a live signaling game in class:
- Assign students to be "high quality" or "low quality" (secretly).
- High types can send a costly signal (e.g., do 10 pushups); low types can too, but it's "harder" (assign higher subjective cost).
- "Receivers" (other students) observe the signal and guess the type.
- Payoffs: Senders get paid if guessed correctly; Receivers get paid for correct guesses.

After several rounds, discuss: Did signaling emerge? Was it honest?

**2. Cheap Talk Demonstration**

Pair students. One is the Sender (knows the state of the world), one is the Receiver (must guess the state). Sender can send a free message ("The state is A" or "The state is B").

Give Senders an incentive to lie sometimes. Observe: How much do Receivers trust the messages? How does trust change with incentives?

**3. Apology Discussion**

Ask students to share examples of apologies they've given or received. When was an apology credible? When was it not? What made the difference?

---

### Common Student Misconceptions

1. **"Costly signals are wasteful."** Not necessarily — they provide information that enables better decisions. The cost is the price of credibility.

2. **"Signaling requires conscious intent."** No — biological signaling (peacock tails) is unconscious. The evolutionary logic is the same.

3. **"More signaling is always better."** No — excessive signaling can be wasteful (arms races). There's an optimal level.

4. **"Pooling equilibria are bad."** Not always — sometimes pooling is efficient (when signaling costs exceed the value of information).

---

### Connections to Other Course Topics

| Week | Connection |
|---|---|
| W8 (PD) | Signaling can enable cooperation by revealing types. |
| W9 (Convention) | Word meanings are signaling equilibria. |
| W10 (Sequential) | Signaling games are sequential; PBE refines subgame perfection. |
| W11 (Evolution) | Handicap principle is an evolutionary stable strategy. |
| W13 (Behavioral) | Real humans may not play signaling equilibria correctly. |

---

## Preview of Next Week

Next week we turn to **behavioral game theory** — where we ask: How do real humans actually play these games? Do they follow Nash equilibrium? Do they understand backward induction? Do they respond to costly signals?

We'll study:
- The Ultimatum Game (fairness vs. rationality)
- The Dictator Game (pure altruism?)
- The Trust Game (reciprocity)
- Level-k reasoning (how many steps do people think ahead?)
- Social preferences (inequality aversion, reciprocity, spite)

This will bring us full circle: back to the behavioral anomalies we saw in Weeks 6-7, but now in strategic contexts.
