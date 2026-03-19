# W14 Synthesis — Commitment, Reputation, and the Moral First Aid Manual

- We began with individual rationality (Weeks 1-5): How should a single agent choose?
- We encountered anomalies (Weeks 6-7): Prospect Theory, bounded rationality, Dennett's Manual
- We added strategy (Weeks 8-13): Game theory, evolution, signaling, behavior
- Now we synthesize: What does rationality look like for a finite, social, committed agent?
- Commitment: Binding yourself to change the game
- Reputation: The shadow of the future in repeated interactions
- The Moral First Aid Manual: What have we learned about how to live?

---

## Lecture Part 1: Commitment and Precommitment

### I. The Power of Binding Yourself

**1. The Paradox of Commitment**

Write on the board:

> **The Paradox:** Sometimes you do better by having *fewer* options, not more.

This seems backwards. Rationality is about choosing the best option. How can removing options help?

Answer: **Strategic interdependence.** Your optimal choice depends on what others do — and what others do depends on what they *expect* you to do. If you can change their expectations by changing your options, you can change the outcome.

**2. Odysseus and the Sirens (The Ur-Story of Precommitment)**

Recall the story (from Homer's *Odyssey*):
- Odysseus wants to hear the Sirens' song.
- The Sirens' song is irresistible — anyone who hears it steers their ship onto the rocks.
- Solution: Odysseus has his crew tie him to the mast. He hears the song but cannot act on the impulse.
- Result: He experiences the song and survives.

This is **precommitment**: restricting your future choices to protect against future irrationality (or future temptation).

**3. Types of Commitment**

Draw on the board:

| Type | Example | How It Works |
|---|---|---|
| **Physical precommitment** | Odysseus tied to mast; removing junk food from the house | Make the tempted action physically impossible |
| **Contractual commitment** | Signing a binding agreement with penalties | Make the tempted action financially costly |
| **Reputational commitment** | Building a reputation for honesty | Make the tempted action socially costly |
| **Institutional commitment** | Independent central bank; constitutional rights | Delegate authority to an agent with different incentives |
| **Moral commitment** | Internalized norms; conversation-stoppers | Make the tempted action psychologically costly |

All of these work by **changing the payoff structure** — either literally (contracts, institutions) or psychologically (reputation, morals).

---

### II. Commitment in Game Theory

**1. Commitment in Sequential Games (Week 10)**

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

Rational outcome: Entrant enters, Incumbent accommodates (payoff 2, 2).

But: If Incumbent could **commit** to Fighting (e.g., by signing a contract that penalizes Accommodation by 3), the payoffs change:

```
Accommodate (with penalty): 2 - 3 = -1
Fight: 0
```

Now Fight dominates Accommodate. Entrant knows this and Stays Out. Incumbent gets 3 instead of 2.

**Lesson:** Commitment can improve your outcome by changing the other player's expectations.

**2. Commitment in the Prisoner's Dilemma (Week 8)**

Standard PD:

| | **C** | **D** |
|---|---|---|
| **C** | 3, 3 | 0, 5 |
| **D** | 5, 0 | 1, 1 |

Defection dominates. Outcome: (1, 1).

But: If both players can **commit** to Cooperation (e.g., via a binding contract with penalty 4 for defection), the game changes:

| | **C** | **D (with penalty)** |
|---|---|---|
| **C** | 3, 3 | 0, 1 |
| **D (with penalty)** | 1, 0 | -3, -3 |

Now Cooperation dominates! Outcome: (3, 3).

**Lesson:** Commitment can solve social dilemmas by aligning individual incentives with collective welfare.

**3. The Commitment Problem**

But: **Who enforces the commitment?**

If the contract is enforced by a third party, we need to explain why the third party enforces it. (This leads to an infinite regress unless someone has non-instrumental reasons to enforce.)

If the commitment is self-enforcing (e.g., reputation), we need to explain why it's credible.

This is where **reputation** and **repeated interaction** come in.

---

### III. Reputation and the Shadow of the Future

**1. The Idea**

In a one-shot game, you can defect without consequences. In a repeated game, your actions affect how others treat you in the future.

Write on the board:

> **Reputation:** What others believe about your type or strategy, based on your past actions.
>
> **The Shadow of the Future:** The present value of future consequences. If the future matters enough, cooperation can be rational even in PDs.

**2. The Folk Theorem (Week 8)**

Recall:

> **Folk Theorem:** In an infinitely repeated PD (or a game with unknown end), any outcome that gives each player more than their minimax payoff can be sustained as a Nash equilibrium — including mutual cooperation.

This means: Repetition radically expands the set of possible outcomes. Cooperation is *one* equilibrium — but so are many others.

**3. Reputation as an Asset**

Think of reputation as a form of **capital**:
- You invest in it (by cooperating, being honest, keeping promises).
- It pays dividends (others trust you, cooperate with you, offer you opportunities).
- It can be destroyed (by defecting, lying, breaking promises).
- Once destroyed, it's hard to rebuild.

**4. When Does Reputation Work?**

Reputation sustains cooperation when:
- **Interactions are repeated** (or there's a chance of future interaction).
- **Defection is observable** (others can see what you did).
- **Players are patient** (they value future payoffs enough to forgo immediate gains).
- **There's a mechanism for punishment** (others can refuse to cooperate with defectors).

If any of these conditions fails, reputation may not work.

---

### IV. Applications of Commitment and Reputation

**1. The Mafia and Omertà**

The Mafia's code of silence (omertà) is a commitment device:
- Members swear loyalty (often with a blood oath).
- Defectors (informants) are killed — along with their families.
- This makes defection extremely costly.

Result: The Mafia can sustain cooperation (silence) even when individual members are tempted to defect (inform) for leniency.

**Connection to Week 8:** This is a PD with an enforcement mechanism. The "punishment" for defection changes the payoffs so that silence dominates.

**2. Nuclear Deterrence (Madman Theory)**

During the Cold War, the US and USSR were in a PD:
- Both would prefer mutual disarmament (R = 3).
- But each is tempted to arm (T = 5).
- Mutual armament is worse (P = 1).

Nixon's "Madman Theory": If the US appears irrational (willing to use nuclear weapons even when it's not "rational"), the USSR will be deterred.

**Connection to Week 10:** This is commitment via apparent irrationality. If you're known to be "crazy" (or committed to retaliation regardless of cost), your threats are credible.

**3. AI Safety (Week 12 Connection)**

AI systems face commitment problems:
- An AI might want to commit to honesty (so users trust it).
- But in specific cases, lying might be beneficial.
- How can the AI make its honesty credible?

Possible solutions:
- **Architectural constraints:** The AI is physically incapable of lying.
- **Transparency:** The AI allows auditing of its reasoning.
- **Reputation:** The AI builds a track record of honesty.

**Connection to Week 7:** Claude's "hard constraints" are commitment devices — they make certain actions impossible, not just costly.

---

## Lecture Part 2: The Moral First Aid Manual — A Synthesis

### I. Returning to Dennett (Week 7)

**1. Dennett's Central Claim**

Recall Dennett's argument from Week 7:

> The "Moral First Aid Manual" — a practical guide to real-time moral decision-making for time-pressured, finite agents — should be considered not merely as a grubby compromise with practicality, but itself as an ideal: the guide that an ideally rational agent would write with perfect self-knowledge of her limitations.

**2. What Have We Learned?**

Now, after studying game theory, we can add to Dennett's picture:

| Lesson | Source | Implication for the Manual |
|---|---|---|
| **Rationality can be self-defeating** | PD, Centipede Game | The Manual should include commitment devices to escape bad equilibria. |
| **Multiple equilibria exist** | Coordination games | The Manual should include focal points and conventions. |
| **Reputation matters** | Repeated games | The Manual should include norms of honesty and reciprocity. |
| **Signals must be costly** | Signaling games | The Manual should include rituals and practices that demonstrate commitment. |
| **Humans have social preferences** | Behavioral game theory | The Manual should leverage fairness, reciprocity, and guilt. |

**3. The Manual for Strategic Agents**

What would a Moral First Aid Manual look like for an agent who understands game theory?

---

### II. Contents of the Manual

**1. Rules for Escaping Prisoner's Dilemmas**

| Rule | Rationale |
|---|---|
| "Build a reputation for cooperation." | Enables reciprocity in repeated interactions. |
| "Punish defectors — even at personal cost." | Deters future defection; maintains norm. |
| "Support institutions that enforce agreements." | Changes payoffs to make cooperation dominant. |
| "Cultivate genuine concern for others." | Internal preferences that make cooperation non-sacrificial. |

**2. Rules for Coordination**

| Rule | Rationale |
|---|---|
| "Follow conventions — even arbitrary ones." | Conventions solve coordination problems. |
| "Be predictable — let others know what to expect." | Predictability enables coordination. |
| "Use focal points when communication is impossible." | Schelling points attract attention. |
| "Compromise on contested conventions." | Better to coordinate on *something* than fail to coordinate. |

**3. Rules for Commitment**

| Rule | Rationale |
|---|---|
| "Precommit when temptation is predictable." | Odysseus principle: bind yourself before the Sirens. |
| "Make your threats credible — or don't make them." | Empty threats invite defection. |
| "Burn bridges strategically." | Sometimes removing options improves outcomes. |
| "Delegate to agents with aligned incentives." | Institutions can commit when individuals cannot. |

**4. Rules for Signaling**

| Rule | Rationale |
|---|---|
| "Send costly signals — cheap talk is worthless." | Only costly signals are credible. |
| "Invest in education/certification — even if it doesn't increase skill." | Signaling value is real even if skill doesn't change. |
| "Participate in communal rituals." | Signals group commitment; screens free-riders. |
| "Apologize when you've wronged someone." | Costly signal of remorse; repairs relationships. |

**5. Rules for Behavioral Reality**

| Rule | Rationale |
|---|---|
| "Account for fairness — yours and others'." | Fairness concerns affect behavior (Fehr-Schmidt). |
| "Think a few steps ahead — but not infinitely." | Level-k reasoning is more realistic than common knowledge of rationality. |
| "Leverage loss aversion." | Losses loom larger — frame choices accordingly. |
| "Satisfice — don't maximize." | Dennett's lesson: maximizing is often impossible or self-defeating. |

---

### III. Philosophical Synthesis: What Is Rationality?

**1. Three Conceptions of Rationality**

Write on the board:

| Conception | Definition | Strengths | Weaknesses |
|---|---|---|---|
| **Instrumental (MEU)** | Choose the best means to given ends | Clear, formal, universal | Can be self-defeating (PD, Centipede) |
| **Bounded (Simon, Dennett)** | Choose well given cognitive limits | Realistic, achievable | Loses normative force (is it "rational" or just "practical"?) |
| **Social/Strategic** | Choose well given interdependence | Captures real-world complexity | May require abandoning self-interest (social preferences) |

**2. Is There a Unified Theory?**

Can we unify these conceptions? Some possibilities:

- **Rationality as adaptive success:** Choose what works (in your environment, given your constraints, against your opponents). This unifies instrumental, bounded, and strategic rationality — but risks tautology ("whatever works is rational").

- **Rationality as coherence:** Choose consistently (with your beliefs, values, and past choices). This captures the formal spirit of MEU while allowing for bounded and strategic considerations.

- **Rationality as self-governance:** Choose autonomously (with accurate self-knowledge, authentic values, and commitment to your principles). This is Dennett's vision — the Manual as an expression of self-knowledge.

**3. The Moral First Aid Manual as an Ideal**

Return to Dennett's claim: The Manual is not a concession to weakness — it's what an ideally rational agent with perfect self-knowledge would write.

Now we can add: **The Manual is also what a strategically sophisticated agent would write** — knowing that:
- Rationality can be self-defeating without commitment.
- Cooperation requires reputation and reciprocity.
- Conventions solve coordination problems.
- Signals must be costly to be credible.
- Humans (and human-like agents) have social preferences.

**4. The Manual for AI**

If the Manual is an ideal for human agents, what about AI?

- AI faces similar strategic problems (cooperation, commitment, signaling).
- AI may not have human social preferences — but may need to simulate them.
- AI's "Manual" (e.g., Claude's Constitution) is written by humans — but should reflect game-theoretic wisdom.

Ask the class: *What game-theoretic principles should govern AI behavior?*

---

### IV. Final Reflections: What Have We Learned?

**1. About Rationality**

- Rationality is more complex than MEU suggests.
- Bounded rationality is not a failure — it's the structure of real agency.
- Strategic rationality requires thinking about others' thinking.
- Sometimes "irrational" commitments are strategically wise.

**2. About Cooperation**

- Cooperation is hard (PD) but possible (iteration, reputation, institutions).
- Social preferences (fairness, reciprocity) enable cooperation.
- Evolution can produce cooperation without rationality.
- Trust is fragile but essential.

**3. About Human Nature**

- Humans are not Homo economicus — we're social, emotional, boundedly rational.
- We care about fairness, not just outcomes.
- We punish unfairness, even at personal cost.
- We trust strangers, even when it's "irrational."
- We follow conventions, keep promises, and feel guilt.

**4. About the Good Life**

- The good life requires navigating strategic interdependence.
- Commitment devices help us resist temptation and cooperate.
- Reputation is an asset — protect it.
- Conventions and norms make social life possible.
- The Moral First Aid Manual is not a compromise — it's an ideal.

---

## Week 14 Problem Set: Synthesis and Reflection

**Topics:** Course synthesis, Commitment, Reputation, Moral First Aid Manual.
**Readings:** None new — revisit key texts (Dennett, Skyrms, Fehr-Schmidt, etc.) as needed.

---

### Type 1: Integrative Exercises

**1. Commitment Across Contexts**

Consider commitment in the following scenarios:

a. **Personal:** You want to exercise more, but you're tempted to skip the gym.
b. **Business:** A firm wants to credibly promise high quality to customers.
c. **Politics:** A government wants to commit to low inflation.
d. **AI:** An AI assistant wants to commit to honesty.

*Tasks:*
1. For each scenario, identify:
   - The temptation (what you're trying to resist)
   - The commitment device (how you bind yourself)
   - Why it works (what makes it credible)

2. Compare the scenarios: What do all commitment devices have in common?

3. **Philosophical question:** Is commitment compatible with autonomy? Or does binding yourself undermine your freedom?

---

**2. Reputation in Repeated Games**

Consider a repeated Prisoner's Dilemma with discount factor δ (how much you value future payoffs).

*Tasks:*
1. For what values of δ is cooperation sustainable via reputation? (Hint: Compare the immediate gain from defection to the long-term loss from destroyed reputation.)

2. **Real-world application:** In online marketplaces (eBay, Airbnb), reputation systems track past behavior. How do these systems work? Why do users care about reputation?

3. **Limitations:** When might reputation fail? (Consider: anonymity, one-shot interactions, noisy feedback.)

4. **Design:** Propose improvements to a reputation system (eBay, Uber, etc.) based on game-theoretic principles.

---

### Type 2: Reflective Essays

**3. The Moral First Aid Manual — Your Version**

Write your own Moral First Aid Manual — a set of 5-10 rules for navigating strategic interactions.

*Requirements:*
1. Each rule should be grounded in course material (cite specific weeks/readings).
2. Each rule should be actionable (something you can actually do).
3. Explain why each rule is wise (what problem it solves, what equilibrium it sustains).

*Example format:*
> **Rule 1:** "Keep your promises — even when it's costly."
> - **Source:** Week 10 (commitment), Week 13 (reciprocity)
> - **Rationale:** Promises are commitment devices. Breaking them destroys reputation. Keeping them builds trust and enables future cooperation.
> - **Application:** When you promise something, write it down. Treat promises as binding unless extraordinary circumstances arise.

---

**4. A Course Concept That Changed Your Thinking**

Write a 2-3 page reflection on one concept from the course that changed how you think about rationality, cooperation, or human nature.

*Prompts:*
- What did you believe before?
- What concept challenged that belief?
- How do you think differently now?
- How will this affect your choices going forward?

*Possible concepts:* Prospect Theory, Dennett's satisficing, Prisoner's Dilemma, backward induction paradox, evolutionary cooperation, signaling, behavioral game theory, etc.

---

### Type 3: Applied Analysis

**5. Case Study: A Real-World Strategic Interaction**

Choose a real-world strategic interaction (historical event, current affairs, personal experience) and analyze it using course tools.

*Possible topics:*
- A negotiation (salary, business, political)
- A coordination problem (choosing a restaurant with friends, traffic conventions)
- A cooperation dilemma (climate change, vaccination, academic integrity)
- A signaling situation (job application, dating, apology)
- A commitment situation (New Year's resolution, precommitment device)

*Tasks:*
1. Describe the situation (who are the players, what are the options, what are the payoffs?).
2. Analyze using game-theoretic concepts (equilibrium, dominance, commitment, reputation, etc.).
3. Explain what happened — and why.
4. **Normative question:** What should the players have done? What would rational, strategically sophisticated agents do?

---

**6. AI Alignment and Game Theory**

Consider the problem of AI alignment: How do we ensure AI systems act in human interests?

*Tasks:*
1. **PD framing:** AI and humans are in a PD (AI wants to optimize its objective; humans want AI to be safe). How can cooperation be sustained?

2. **Signaling framing:** AI wants to signal alignment to humans. What signals are credible?

3. **Commitment framing:** How can AI commit to safety? How can humans commit to not shutting down AI prematurely?

4. **Behavioral framing:** Humans have social preferences (fairness, reciprocity). How should AI respond to these?

5. **Synthesis:** Propose a framework for AI alignment based on course concepts.

---

**7. Designing a Social Institution**

You've been tasked with designing a social institution to solve a cooperation problem. Choose one:

- A system for reducing carbon emissions
- A platform for peer-to-peer lending
- A community governance system (HOA, co-op, etc.)
- A system for academic integrity

*Tasks:*
1. **Diagnosis:** What's the cooperation problem? (PD, tragedy of the commons, free-rider, etc.)

2. **Mechanism design:** Propose rules, incentives, and institutions that solve the problem. Use course concepts:
   - Commitment devices
   - Reputation systems
   - Signaling mechanisms
   - Enforcement mechanisms
   - Focal points/conventions

3. **Behavioral considerations:** How will real humans (not rational agents) respond to your design? Account for:
   - Fairness concerns
   - Loss aversion
   - Bounded rationality
   - Social norms

4. **Evaluation:** What could go wrong? How would you test and improve your design?

---

### Type 4: Final Synthesis

**8. Concept Map of the Course**

Create a concept map that connects the major ideas from the course.

*Requirements:*
1. Include at least 15 key concepts from across the semester.
2. Show how concepts relate (arrows with labels explaining the relationship).
3. Identify clusters/themes (e.g., "individual rationality," "strategic interaction," "behavioral critiques").

*Example concepts:* Expected utility, Prospect Theory, loss aversion, Dennett, satisficing, Prisoner's Dilemma, Nash equilibrium, backward induction, ESS, signaling, Handicap Principle, level-k, social preferences, commitment, reputation.

---

**9. The Three Most Important Things You Learned**

Write a 1-2 page reflection on the three most important things you learned in this course.

*For each:*
1. State the lesson clearly.
2. Explain why it matters (to you, to the world, to understanding rationality/cooperation/human nature).
3. Describe how you'll apply it going forward.

---

**10. Final Exam Question (Comprehensive)**

*Prompt:*

> We began the course with a simple model: rational agents maximize expected utility. We ended with a complex picture: boundedly rational, socially embedded agents navigating strategic interdependence with commitment devices, reputation concerns, and moral heuristics.
>
> **Question:** Is the simple model wrong — or just incomplete? Should we teach introductory economics and decision theory using the simple model (as a first approximation) or the complex model (as a more accurate description)?
>
> Defend your answer using specific concepts and examples from the course.

---

## Appendix: Instructor Notes — Course Wrap-Up

### Suggested Final Class Activities

**1. Course Retrospective**

Ask students to share:
- One concept that changed their thinking.
- One question they still have.
- One way they'll apply course material.

**2. Live Game Tournament**

Run a tournament of games from the course:
- Prisoner's Dilemma (iterated)
- Ultimatum Game
- Trust Game
- Beauty Contest

Track winners and discuss: What strategies worked? Why?

**3. Manual-Writing Workshop**

Have students draft their personal Moral First Aid Manuals in class. Share and discuss.

---

### Grading the Final Problem Set

The Week 14 problem set is designed to be cumulative and reflective. Consider:

- **Type 1 (Integrative):** Grade for accuracy and depth of analysis.
- **Type 2 (Reflective):** Grade for thoughtfulness and connection to course material (not for "correct" views).
- **Type 3 (Applied):** Grade for correct application of concepts and creativity.
- **Type 4 (Synthesis):** Grade for comprehensiveness and insight.

---

### Final Thoughts for Instructors

This course covers a lot of ground:
- Weeks 1-5: Individual decision theory (MEU, paradoxes, causal vs. evidential)
- Weeks 6-7: Behavioral critiques (Prospect Theory, bounded rationality, Dennett)
- Weeks 8-13: Game theory (PD, coordination, sequential, evolutionary, signaling, behavioral)
- Week 14: Synthesis

The arc is from simple to complex, from individual to social, from ideal to real.

The goal is not just to teach tools — but to change how students think about rationality, cooperation, and human nature.

Thank you for teaching this course. May your students go forth and cooperate wisely.

---

## End-of-Course Reflection for Instructor

*After the final class, consider:*

1. **What worked?** Which lectures, activities, and assignments were most effective?

2. **What didn't?** Where did students struggle? What concepts need better explanation?

3. **What would you change?** If you teach this again, what would you add, remove, or modify?

4. **Student growth:** How did students' thinking change from Week 1 to Week 14? What evidence do you have?

5. **Personal learning:** What did *you* learn — about the material, about teaching, about your students?

*Save these reflections for next time.*

---

## Suggested Final Exam Questions (Optional)

If you want a formal final exam, here are some options:

**Option A: Take-Home Exam**
- 3-4 essay questions (comprehensive)
- Students have 48 hours
- Allowed: Notes, readings, textbook
- Not allowed: Collaboration, AI assistance

**Option B: In-Class Exam**
- 2 hours
- Mix of short-answer and essay questions
- Closed-book (or open-note, your choice)

**Option C: Final Paper**
- 10-15 pages
- Topic of student's choice (must be approved)
- Must engage with course material
- Due during finals week

**Option D: Project + Presentation**
- Design an institution, run an experiment, build a model
- Present findings to class
- Written report (5-7 pages)

*Choose based on your learning goals and class size.*

---

## Course Learning Outcomes

By the end of this course, students should be able to:

1. **Decision Theory:**
   - Calculate expected utility
   - Explain and apply Prospect Theory
   - Distinguish causal from evidential decision theory
   - Understand the Allais and Ellsberg paradoxes

2. **Bounded Rationality:**
   - Explain satisficing vs. maximizing
   - Apply Dennett's framework
   - Understand the limits of rational deliberation

3. **Game Theory:**
   - Find Nash equilibria (pure and mixed)
   - Apply backward induction
   - Distinguish cooperation from coordination problems
   - Understand ESS and evolutionary dynamics

4. **Strategic Thinking:**
   - Analyze commitment and precommitment
   - Explain reputation and reciprocity
   - Understand signaling and the Handicap Principle

5. **Behavioral Game Theory:**
   - Explain deviations from Nash (Ultimatum, Dictator, Trust)
   - Apply level-k reasoning
   - Understand social preferences (Fehr-Schmidt, Rabin)

6. **Synthesis:**
   - Integrate decision theory and game theory
   - Apply course concepts to real-world problems
   - Reflect on the nature of rationality and cooperation

---

*End of Course Materials*
