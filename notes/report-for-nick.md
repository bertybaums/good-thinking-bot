# Good Thinking Bot: Project Report

## The Big Idea

We're building an interactive, game-based learning system that teaches people how to think better -- using LLM-powered NPCs, adaptive skill assessment, and a retro-style open-world game. The core pedagogical frame comes from Dennett's "Moral First Aid Manual": the ideally rational agent, knowing her own limitations, wouldn't try to maximize -- she'd write herself a practical guide. Our bot helps players write their own manuals by taking them on a journey from formal ideals to real-world messiness to practical wisdom.

## What We're Drawing From

We've assembled source material across three tracks that converge on a unified "how to think better" curriculum:

### Track 1: Logic & Critical Thinking

Source: Van Cleave's *Intro to Logic and Critical Thinking* (CC BY 4.0 -- freely adaptable) + Bert's PHIL 201 lecture notes + Dennett's *Intuition Pumps*

- **Argument fundamentals**: identifying arguments, standard form, validity, soundness, principle of charity
- **Formal logic**: propositional logic (truth tables, connectives, 8 valid inference forms), categorical logic (Venn diagrams, syllogisms)
- **Inductive reasoning**: statistical generalizations, inference to best explanation (7 virtues), analogical arguments, causal reasoning
- **Probability and statistical fallacies**: base rate fallacy, conjunction fallacy, small numbers, regression to mean, gambler's fallacy
- **Formal fallacies**: denying the antecedent, affirming the consequent
- **Informal fallacies**: composition, division, begging the question, false dichotomy, equivocation, slippery slopes, ad hominem, straw man, tu quoque, genetic fallacy, appeal to consequences, appeal to authority
- **Dennett's thinking tools**: Rapoport's Rules, reductio ad absurdum, Sturgeon's Law, Occam's Razor/Broom, Jootsing, deepities, the "surely" operator, rhetorical questions, Goulding (rathering, piling on, Gould two-step)
- **Cognitive biases** (~24): anchoring, sunk cost, Dunning-Kruger, confirmation bias, framing effect, fundamental attribution error, etc.

### Track 2: Decision Theory & Game Theory

Source: Baumgaertner's decision theory textbook + Weatherson + Bert's lecture notes for "Rationality & Strategic Interactions"

- **Decision under ignorance**: dominance, maximin, maximax, minimax regret, IIA violations
- **Probability as credence**: Dutch Book arguments (why your beliefs must be consistent)
- **Expected utility (MEU)**: the "gold standard," risk aversion, cardinal utility
- **Paradoxes of the ideal**: Allais (certainty effect), Newcomb (causal vs. evidential), Ellsberg (ambiguity aversion), reflection effect
- **Prospect Theory**: value function (reference points, loss aversion), probability weighting, mental accounting, framing effects
- **Dennett's Moral First Aid Manual**: satisficing vs. maximizing, the Panglossian Slide, conversation-stoppers, Wolf's Dilemma, bounded rationality as an ideal (not a compromise)
- **Game theory**: Prisoner's Dilemma, Nash equilibrium, coordination, conventions, sequential games, backward induction
- **Evolutionary game theory**: ESS, replicator dynamics
- **Signaling**: Handicap Principle, costly signals, information asymmetry
- **Behavioral game theory**: Fehr-Schmidt (fairness), level-k reasoning, social preferences
- **Synthesis**: commitment devices (Odysseus), reputation, the Manual enriched with game-theoretic wisdom

### Track 3: Microeconomics

Source: CORE's *The Economy 2.0: Microeconomics*

- **Big picture context**: growth ("history's hockey stick"), inequality, climate, technology and incentives, opportunity costs, economic rents
- **Individual choice**: constrained optimization, preferences, feasible sets, income and substitution effects
- **Strategic interaction**: Nash equilibrium, PD, public good games, social preferences, ultimatum game, coordination
- **Institutions and power**: bargaining models, Pareto efficiency, fairness, Lorenz curve / Gini coefficient
- **The firm**: principal-agent problems, employment rents, wage-setting, pricing, elasticity, profit maximization, monopoly/oligopoly
- **Markets**: supply and demand, competitive equilibrium, gains from trade, taxes, price controls
- **Intertemporal choice**: borrowing/lending, discounting, credit market exclusion, poverty traps
- **Market failures**: externalities, public goods, asymmetric information (moral hazard, adverse selection), tragedy of the commons

### Where the Tracks Converge

These aren't three separate curricula -- they feed into each other:

- **Dutch Books** appear in both the critical thinking probability section and Week 3 of decision theory
- **Game theory** (PD, coordination, signaling) bridges decision theory and the CORE econ textbook (Ch 4-5)
- **Prospect Theory** connects behavioral economics to Dennett's bounded rationality
- **Fallacies and biases** are the "bugs" that the formal frameworks help diagnose
- **Dennett's Manual** is the throughline: the practical guide that results from understanding both the ideals and their limits

## What Already Exists (and Doesn't)

We did extensive landscape research. Here's the short version:

### LLM NPC Technology -- Ready
- **Inworld AI** ($120M raised), **Convai**, **NVIDIA ACE** -- commercial NPC middleware
- **Gigax NPC-LLM-7B** -- open-source LoRA fine-tune for NPC actions
- **On-device inference** emerging: NobodyWho (llama.cpp in Godot/Unity), MobiLoRA (57.6% speedup on mobile)
- Stanford's Generative Agents, Voyager -- seminal research on agent memory/planning

### LoRA Routing / Composition -- Surprisingly Mature
- **MoLoRA** (March 2026): per-token routing across specialized adapters; 1.7B model beats 8B on reasoning
- **X-LoRA**: dense gating across adapters, per-layer, token by token
- **LoRAuter**: training-free routing to 1,500+ adapters via cosine similarity
- **Tina** (ICLR 2026): LoRA + RL for reasoning at 260x lower cost than full fine-tuning
- Key finding: different cognitive skills have distinct low-rank parameter signatures -- supports the modular adapter idea

### On-Device QLoRA -- Feasible
- MLC-LLM supports dynamic adapter swapping + QLoRA on mobile
- Single-adapter deployment works today; multi-adapter swapping is early but possible

### Game-Based Learning for This Content -- The Gap
- **Logic puzzles**: Only static generators and trivial indie games for knights & knaves
- **Decision theory games**: Nothing exists for money pumps, Dutch books, or preference transitivity as interactive experiences
- **Economics education**: MobLab and economics-games.com are sophisticated but instructor-dependent classroom tools, not standalone games
- **Stealth assessment** (skill assessment without XP): Valerie Shute's framework is well-validated but rarely adopted
- **LLM + educational games**: A few Socratic math tutors, no one doing logic/decision theory/econ through NPC interaction

**The gap in one sentence:** Nobody has built a game where you learn formal reasoning and decision theory through narrative NPC interaction with adaptive skill assessment.

## The Architecture Idea (from our earlier conversations)

- **Modular LoRA adapters** for specific reasoning skills (analogical reasoning, conditionals, counterexample generation, etc.)
- **Meta-level router adapter** (MoE approach) to select which skill adapter to activate per query
- **QLoRA for on-device** inference -- viable on phones
- **Knights & knaves** (Smullyan-style) puzzles as one game mechanic for propositional logic
- **Money pump / Dutch book scenarios** as game mechanics for decision theory
- **NPC merchants, gamblers, debaters** who embody specific fallacies, biases, or strategic behaviors
- **Stealth assessment**: NPCs assess player skill through dialogue, not XP bars
- **Retro-style open world** with agent-driven NPCs

## What's Next

Open questions for us to work through:

1. **Scope the pilot**: Which content slice do we build first? Candidates: knights & knaves logic village, a money pump marketplace, a fallacy-riddled debate arena
2. **Game engine**: Retro pixel art in Godot? Text-based? Something else?
3. **Model architecture**: Which base model? How many adapters to start? What's the router design?
4. **Corpus construction**: Bert has the pedagogical source material; we need to turn it into training data
5. **Assessment design**: How do NPCs infer what the player knows from dialogue? What's the competency model?

---

*Report generated 2026-03-19*
