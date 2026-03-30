"""
Taxonomy of reasoning patterns for the Good Thinking Bot training corpus.

~120 codes organized across five tracks:
  A: Logic & Critical Thinking (~65 codes)
  B: Decision Theory & Game Theory (~40 codes)
  C: Microeconomics (~15 codes)
  D: Dennett's Thinking Tools (~15 codes)
  E: Cognitive Biases (24 codes)

Each entry contains:
  - label: human-readable name
  - description: what the pattern is
  - pattern_type: good_tool | bad_thinking | dual
  - track: which content track
  - source_notes: where the anchor examples come from
"""

TAXONOMY: dict[str, dict] = {

    # ═══════════════════════════════════════════════════════════════════════════
    # TRACK A: LOGIC & CRITICAL THINKING
    # ═══════════════════════════════════════════════════════════════════════════

    # ── A1: Argument Structure ─────────────────────────────────────────────────

    "A1.1": {
        "label": "Identifying arguments",
        "description": "Distinguishing arguments from non-arguments (explanations, "
        "descriptions, commands). Using premise and conclusion indicators.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.1-1.2; Van Cleave Ch 1",
    },
    "A1.2": {
        "label": "Premises and conclusions",
        "description": "Identifying the premises and conclusion of an argument, "
        "including intermediate conclusions and sub-arguments.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.4",
    },
    "A1.3": {
        "label": "Standard form",
        "description": "Putting arguments into standard form: numbered premises "
        "with conclusion last, marking inference steps.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.1",
    },
    "A1.4": {
        "label": "Principle of charity",
        "description": "Reconstructing arguments in their strongest form. "
        "Choosing the most plausible interpretation of ambiguous claims.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.5, 1.9",
    },
    "A1.5": {
        "label": "Missing premises",
        "description": "Identifying unstated assumptions needed to make an argument "
        "valid or strong. The is-ought gap.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.9",
    },
    "A1.6": {
        "label": "Arguments vs explanations",
        "description": "Distinguishing attempts to convince (arguments) from attempts "
        "to show why something is true (explanations).",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.3",
    },
    "A1.7": {
        "label": "Argument diagramming",
        "description": "Mapping complex argument structures: linked vs convergent "
        "premises, chains of reasoning, sub-arguments.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.4; Van Cleave Ch 1",
    },

    # ── A2: Deductive Logic ────────────────────────────────────────────────────

    "A2.1": {
        "label": "Validity and soundness",
        "description": "A valid argument: impossible for premises to be true and "
        "conclusion false. Sound: valid + true premises. Informal test of validity.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.6-1.7",
    },
    "A2.2": {
        "label": "Propositional logic basics",
        "description": "Logical connectives (and, or, not, if-then, iff), "
        "well-formed formulas, translation from natural language.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 2; Van Cleave Ch 4",
    },
    "A2.3": {
        "label": "Truth tables",
        "description": "Constructing truth tables to evaluate validity, "
        "tautologies, contradictions, and logical equivalence.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 2.1; Van Cleave Ch 5",
    },
    "A2.4": {
        "label": "Inference rules (modus ponens, modus tollens)",
        "description": "The valid inference forms: MP, MT, hypothetical syllogism, "
        "disjunctive syllogism, constructive dilemma, conjunction, addition, "
        "De Morgan's laws.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 2; Van Cleave Ch 6",
    },
    "A2.5": {
        "label": "Natural deduction proofs",
        "description": "Constructing proofs using inference rules. "
        "Conditional proof and indirect proof strategies.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 6-7",
    },
    "A2.6": {
        "label": "Categorical logic",
        "description": "Categorical propositions (All S are P, etc.), Venn diagrams, "
        "immediate inferences, categorical syllogisms.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 8-9",
    },
    "A2.7": {
        "label": "Logical equivalence and contradiction",
        "description": "Identifying logically equivalent statements and contradictions. "
        "Contraposition, De Morgan's, double negation.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 2; Van Cleave Ch 5",
    },
    "A2.8": {
        "label": "Deductive vs inductive distinction",
        "description": "Recognizing deductive arguments (certainty) vs inductive "
        "arguments (probability). Defeasibility.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.8",
    },

    # ── A3: Inductive Reasoning ────────────────────────────────────────────────

    "A3.1": {
        "label": "Statistical generalizations",
        "description": "Reasoning from sample to population. Representativeness, "
        "sample size, margin of error.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 10",
    },
    "A3.2": {
        "label": "Inference to the best explanation (IBE)",
        "description": "Abductive reasoning: choosing the hypothesis that best "
        "explains the evidence. Criteria: simplicity, scope, fruitfulness.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 10",
    },
    "A3.3": {
        "label": "Argument by analogy",
        "description": "Reasoning that if two things are alike in known respects, "
        "they are alike in further respects. Evaluating strength via relevance "
        "of similarities and presence of disanalogies.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 10",
    },
    "A3.4": {
        "label": "Causal reasoning",
        "description": "Mill's methods (agreement, difference, concomitant variation). "
        "Distinguishing necessary vs sufficient conditions.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 10",
    },
    "A3.5": {
        "label": "Correlation vs causation",
        "description": "Recognizing that correlation does not imply causation. "
        "Third-variable problems, reverse causation, coincidence.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 10; Corr2Cause dataset",
    },

    # ── A4: Probability ────────────────────────────────────────────────────────

    "A4.1": {
        "label": "Basic probability laws",
        "description": "Axioms of probability: non-negativity, normalization, "
        "addition rule. Complementary events. Joint probability.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 3; Baumgaertner Ch 8",
    },
    "A4.2": {
        "label": "Conditional probability and Bayes' theorem",
        "description": "P(A|B), updating beliefs with evidence, "
        "Bayes' rule, prior and posterior probabilities.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Baumgaertner Ch 8; Weatherson Ch 4",
    },
    "A4.3": {
        "label": "Base rate reasoning",
        "description": "Properly incorporating base rates when evaluating "
        "diagnostic evidence. The taxi-cab problem, medical screening.",
        "pattern_type": "good_tool",
        "track": "logic_critical_thinking",
        "source_notes": "Kahneman; Baumgaertner Ch 8",
    },

    # ── A5: Formal Fallacies ──────────────────────────────────────────────────

    "A5.1": {
        "label": "Denying the antecedent",
        "description": "Invalid form: If P then Q; not P; therefore not Q. "
        "Confusing sufficient with necessary conditions.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 2; Van Cleave Ch 6",
    },
    "A5.2": {
        "label": "Affirming the consequent",
        "description": "Invalid form: If P then Q; Q; therefore P. "
        "Confusing necessary with sufficient conditions.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 2; Van Cleave Ch 6",
    },
    "A5.3": {
        "label": "Causal slippery slope (formal)",
        "description": "Asserting a chain of causal claims without evidence: "
        "A leads to B leads to C ... leads to catastrophe.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; Van Cleave",
    },

    # ── A6: Informal Fallacies (structure) ─────────────────────────────────────

    "A6.1": {
        "label": "Composition",
        "description": "Assuming what's true of parts must be true of the whole. "
        "Atoms are invisible, I'm made of atoms, so I'm invisible.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A6.2": {
        "label": "Division",
        "description": "Assuming what's true of the whole must be true of each part.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A6.3": {
        "label": "Begging the question",
        "description": "Circular argument where the conclusion is assumed in a premise. "
        "'Zorbo is flawless because the Book of Zorbo says so.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; PHIL 201",
    },
    "A6.4": {
        "label": "False dichotomy (black-or-white)",
        "description": "Presenting only two options when more exist. "
        "'You're either with us or against us.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; PHIL 201",
    },
    "A6.5": {
        "label": "Equivocation",
        "description": "Using a word with two meanings in an argument as if it "
        "had only one. 'Fine for parking here.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster (ambiguity)",
    },
    "A6.6": {
        "label": "Conceptual slippery slope",
        "description": "Arguing that because there's no sharp boundary between "
        "two things, there's no real difference between them.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave; PHIL 201",
    },

    # ── A7: Fallacies of Relevance ─────────────────────────────────────────────

    "A7.1": {
        "label": "Ad hominem",
        "description": "Attacking the person making the argument rather than "
        "the argument itself. Includes abusive, circumstantial, and tu quoque forms.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; PHIL 201",
    },
    "A7.2": {
        "label": "Straw man",
        "description": "Misrepresenting someone's argument to make it easier "
        "to attack. Exaggerating, distorting, or fabricating the position.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; PHIL 201",
    },
    "A7.3": {
        "label": "Tu quoque",
        "description": "Deflecting criticism by turning it back on the accuser. "
        "'You did it too.' Does not address the substance.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.4": {
        "label": "Genetic fallacy",
        "description": "Judging something good or bad based on its origin "
        "rather than its current merits.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.5": {
        "label": "Appeal to consequences",
        "description": "Arguing that a belief is true/false because of the "
        "desirable/undesirable consequences of holding it.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave; PHIL 201",
    },
    "A7.6": {
        "label": "Appeal to authority",
        "description": "Claiming something is true because an authority says so, "
        "especially when the authority is not relevant or qualified.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.7": {
        "label": "Appeal to emotion",
        "description": "Using emotional manipulation (fear, pity, guilt, pride) "
        "in place of evidence or valid reasoning.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; PHIL 201",
    },
    "A7.8": {
        "label": "Appeal to nature",
        "description": "Arguing something is good because it's 'natural' or bad "
        "because it's 'unnatural.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.9": {
        "label": "Bandwagon (appeal to popularity)",
        "description": "Arguing that something is true or good because many "
        "people believe it or do it.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.10": {
        "label": "Burden of proof",
        "description": "Shifting the burden of proof from the claimant to "
        "the skeptic. 'Prove me wrong.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.11": {
        "label": "Personal incredulity",
        "description": "Dismissing something as false because you personally "
        "cannot understand or imagine it.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.12": {
        "label": "Special pleading (no true Scotsman)",
        "description": "Making ad hoc exceptions to dismiss counterevidence. "
        "Moving goalposts when a claim is falsified.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.13": {
        "label": "Loaded question",
        "description": "A question with a built-in assumption that cannot be "
        "answered without appearing to agree to the assumption.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.14": {
        "label": "Texas sharpshooter",
        "description": "Cherry-picking data clusters that confirm a conclusion "
        "while ignoring data that doesn't fit.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.15": {
        "label": "Middle ground (false compromise)",
        "description": "Assuming the truth must lie between two extreme positions.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },
    "A7.16": {
        "label": "Anecdotal evidence",
        "description": "Using personal experience or isolated examples instead of "
        "valid evidence, especially to dismiss statistics.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },

    # ── A8: Statistical Fallacies ──────────────────────────────────────────────

    "A8.1": {
        "label": "Conjunction fallacy",
        "description": "Judging that P(A and B) > P(A). The Linda problem.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Kahneman; Baumgaertner",
    },
    "A8.2": {
        "label": "Base rate neglect",
        "description": "Ignoring prior probability when evaluating evidence. "
        "Overweighting the hit rate, ignoring the base rate.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Kahneman; Baumgaertner Ch 8",
    },
    "A8.3": {
        "label": "Law of small numbers",
        "description": "Drawing conclusions from sample sizes too small to be "
        "statistically reliable.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Kahneman",
    },
    "A8.4": {
        "label": "Regression to the mean",
        "description": "Failing to recognize that extreme observations tend to "
        "be followed by less extreme ones.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Kahneman",
    },
    "A8.5": {
        "label": "Gambler's fallacy",
        "description": "Believing that past independent events affect future "
        "probabilities. 'Red came up 6 times, black is due.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; Kahneman",
    },
    "A8.6": {
        "label": "Hasty generalization",
        "description": "Drawing a general conclusion from insufficient evidence. "
        "Too-small sample, unrepresentative sample.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Van Cleave Ch 10; PHIL 201",
    },
    "A8.7": {
        "label": "False cause (post hoc / cum hoc)",
        "description": "Assuming causation from correlation or temporal sequence. "
        "'After X, therefore because of X.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster; Van Cleave",
    },

    # ── A9: Rhetorical Manipulation ────────────────────────────────────────────

    "A9.1": {
        "label": "Evaluative language and presupposition",
        "description": "Using loaded terms, presuppositions, and framing to "
        "bias the audience without giving reasons.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.11",
    },
    "A9.2": {
        "label": "Assuring, guarding, and discounting",
        "description": "Rhetorical devices that short-circuit argument: "
        "'Everyone knows...', 'Most experts agree...', 'Granted X, but...'",
        "pattern_type": "dual",
        "track": "logic_critical_thinking",
        "source_notes": "PHIL 201 Ch 1.10",
    },
    "A9.3": {
        "label": "The fallacy fallacy",
        "description": "Assuming a conclusion is wrong because the argument "
        "for it contains a fallacy. The argument is bad, but the conclusion "
        "might still be true.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "Fallacy poster",
    },

    # ── A10: Propaganda Techniques ─────────────────────────────────────────────

    "A10.1": {
        "label": "Name calling / labeling",
        "description": "Attaching a negative label to dismiss without argument.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset",
    },
    "A10.2": {
        "label": "Repetition",
        "description": "Repeating a message until it becomes familiar and is "
        "accepted as true (illusory truth effect).",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset",
    },
    "A10.3": {
        "label": "Whataboutism / red herring",
        "description": "Diverting attention from the issue by raising an "
        "irrelevant topic or counter-accusation.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset",
    },
    "A10.4": {
        "label": "Flag-waving",
        "description": "Appealing to group identity, patriotism, or tribal "
        "loyalty to justify a position.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset",
    },
    "A10.5": {
        "label": "Thought-terminating cliché",
        "description": "Using a stock phrase to end discussion: 'It is what it is', "
        "'Everything happens for a reason.'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset; Dennett",
    },
    "A10.6": {
        "label": "Exaggeration / minimization",
        "description": "Inflating or deflating the significance of something "
        "to manipulate perception.",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset",
    },
    "A10.7": {
        "label": "Doubt casting",
        "description": "Sowing uncertainty about established knowledge without "
        "providing counter-evidence. 'Some people say...'",
        "pattern_type": "bad_thinking",
        "track": "logic_critical_thinking",
        "source_notes": "SemEval Propaganda dataset",
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # TRACK B: DECISION THEORY & GAME THEORY
    # ═══════════════════════════════════════════════════════════════════════════

    # ── B1: Decision Under Ignorance ───────────────────────────────────────────

    "B1.1": {
        "label": "Decision matrices",
        "description": "Constructing decision matrices: acts (rows), states (columns), "
        "outcomes (cells). Normal form vs extensive form (decision trees).",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W1; Baumgaertner Ch 1-2",
    },
    "B1.2": {
        "label": "Dominance reasoning",
        "description": "If one act is better than another in every state, choose it. "
        "Strict vs weak dominance. State-act independence requirement.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W1; Weatherson Ch 2.1-2.2",
    },
    "B1.3": {
        "label": "Maximax",
        "description": "Choose the act with the best possible outcome. "
        "Risk-seeking, ignores the floor.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W2; Weatherson Ch 2.3",
    },
    "B1.4": {
        "label": "Maximin",
        "description": "Choose the act whose worst outcome is the least bad. "
        "Risk-averse, ignores the ceiling.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W2; Weatherson Ch 2.4",
    },
    "B1.5": {
        "label": "Minimax regret",
        "description": "Compute regret matrix, choose the act with the lowest "
        "maximum regret. Requires cardinal utilities.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W2; Weatherson Ch 2.5-2.6",
    },

    # ── B2: Probability and Consistency ────────────────────────────────────────

    "B2.1": {
        "label": "Betting rates and credences",
        "description": "Fair betting rate as a measure of subjective probability. "
        "The connection between action and belief.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W3; Baumgaertner Ch 8",
    },
    "B2.2": {
        "label": "Dutch Book arguments",
        "description": "If your credences violate probability axioms, you can be "
        "Dutch-Booked (guaranteed loss). Pragmatic argument for consistency.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W3; Baumgaertner Ch 8",
    },
    "B2.3": {
        "label": "Axioms of probability (normative)",
        "description": "Non-negativity, normalization, additivity as requirements "
        "of rational belief.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W3; Weatherson Ch 4",
    },
    "B2.4": {
        "label": "Subjective vs objective probability",
        "description": "Credences (subjective) vs frequencies (objective). "
        "When to use each. The role of evidence.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W3; Weatherson Ch 6",
    },
    "B2.5": {
        "label": "Principal Principle",
        "description": "Your credences should match known objective chances, "
        "absent defeating evidence.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W3; Weatherson Ch 6",
    },

    # ── B3: Expected Utility ───────────────────────────────────────────────────

    "B3.1": {
        "label": "MEU formula and calculation",
        "description": "EU(A) = sum of P(S) * U(A|S) over all states. "
        "Choose the act with highest expected utility.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W4; Baumgaertner Ch 5",
    },
    "B3.2": {
        "label": "Cardinal vs ordinal utility",
        "description": "Ordinal: ranking only. Cardinal: magnitude matters. "
        "MEU requires cardinal utility.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W2-W4; Weatherson Ch 9",
    },
    "B3.3": {
        "label": "Risk aversion and utility curves",
        "description": "Concave utility function = risk averse. Convex = risk seeking. "
        "Why people prefer certain outcomes over equivalent gambles.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W4; Weatherson Ch 9",
    },
    "B3.4": {
        "label": "Transitivity and money pumps",
        "description": "If you prefer A to B and B to C but C to A, "
        "you can be money-pumped. Argument for transitive preferences.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W4; Baumgaertner Ch 3",
    },
    "B3.5": {
        "label": "Independence of Irrelevant Alternatives (IIA)",
        "description": "Your preference between A and B shouldn't change when "
        "option C is added or removed from the menu.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W4; Weatherson Ch 9",
    },
    "B3.6": {
        "label": "Pascal's Wager",
        "description": "Infinite utility of belief in God dominates. "
        "Problems: many-gods, non-zero cost of belief, utility assignment.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W1 puzzle; Baumgaertner",
    },
    "B3.7": {
        "label": "St. Petersburg Paradox",
        "description": "A gamble with infinite expected value that no one would "
        "pay infinite money for. Motivates bounded utility functions.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "Baumgaertner; Weatherson",
    },

    # ── B4: Paradoxes ──────────────────────────────────────────────────────────

    "B4.1": {
        "label": "Allais Paradox",
        "description": "Systematic violation of IIA: people prefer certainty "
        "in Gamble 1 but risk in Gamble 4. The Certainty Effect.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W5; Weatherson",
    },
    "B4.2": {
        "label": "Sure Thing Principle",
        "description": "If you prefer A to B given E, and A to B given not-E, "
        "you should prefer A to B. Violated by Allais choices.",
        "pattern_type": "good_tool",
        "track": "decision_theory",
        "source_notes": "W5; Weatherson",
    },
    "B4.3": {
        "label": "Newcomb's Problem",
        "description": "One-box vs two-box. Causal vs evidential decision theory. "
        "Dominance conflicts with expected utility.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W5; Weatherson; Baumgaertner",
    },
    "B4.4": {
        "label": "Ellsberg Paradox",
        "description": "Preference for known risk over ambiguity, even when "
        "MEU says you should be indifferent. Ambiguity aversion.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W5",
    },
    "B4.5": {
        "label": "Reflection Effect",
        "description": "People are risk-averse over gains but risk-seeking over "
        "equivalent losses. Breaks consistent utility curves.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W5-W6; Kahneman & Tversky",
    },
    "B4.6": {
        "label": "Disjunction effect",
        "description": "Preference reversal when outcome is unknown vs when either "
        "outcome is revealed. Violates STP in a subtle way.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W5",
    },

    # ── B5: Prospect Theory ───────────────────────────────────────────────────

    "B5.1": {
        "label": "Reference points",
        "description": "Outcomes are evaluated as gains or losses relative to a "
        "reference point (current state, expectation), not absolute wealth.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W6; Kahneman & Tversky 1979",
    },
    "B5.2": {
        "label": "Loss aversion",
        "description": "Losses loom larger than equivalent gains. "
        "Lambda ≈ 2.25: losing $100 hurts as much as gaining $225 feels good.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W6; Kahneman & Tversky",
    },
    "B5.3": {
        "label": "Probability weighting",
        "description": "People overweight small probabilities and underweight "
        "large ones. The pi(p) function.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W6; Kahneman & Tversky",
    },
    "B5.4": {
        "label": "Fourfold pattern of risk attitudes",
        "description": "Risk-averse for likely gains and unlikely losses; "
        "risk-seeking for unlikely gains and likely losses.",
        "pattern_type": "dual",
        "track": "decision_theory",
        "source_notes": "W6",
    },
    "B5.5": {
        "label": "Framing effects",
        "description": "Logically equivalent descriptions produce different "
        "choices depending on gain vs loss frame.",
        "pattern_type": "bad_thinking",
        "track": "decision_theory",
        "source_notes": "W6; Bias poster (framing effect)",
    },
    "B5.6": {
        "label": "Mental accounting",
        "description": "Treating money differently based on arbitrary categories "
        "(budget buckets). Violates fungibility.",
        "pattern_type": "bad_thinking",
        "track": "decision_theory",
        "source_notes": "W6; Thaler",
    },
    "B5.7": {
        "label": "Endowment effect",
        "description": "Valuing something more simply because you own it. "
        "WTA > WTP. Driven by loss aversion.",
        "pattern_type": "bad_thinking",
        "track": "decision_theory",
        "source_notes": "W6; Thaler",
    },
    "B5.8": {
        "label": "Sunk cost fallacy (decision-theoretic)",
        "description": "Continuing an action because of past investment rather "
        "than future expected value. Irrational from MEU perspective.",
        "pattern_type": "bad_thinking",
        "track": "decision_theory",
        "source_notes": "W6; Bias poster (sunk cost fallacy)",
    },

    # ── B6: Strategic Interaction (Prisoner's Dilemma family) ──────────────────

    "B6.1": {
        "label": "Prisoner's Dilemma",
        "description": "Individual rationality leads to collective disaster. "
        "Dominant strategy is defect, but mutual cooperation is better.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W8; standard",
    },
    "B6.2": {
        "label": "Nash equilibrium",
        "description": "A strategy profile where no player can improve by "
        "unilaterally changing strategy. May not be Pareto optimal.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W8",
    },
    "B6.3": {
        "label": "Iterated PD and cooperation",
        "description": "Repeated interactions enable cooperation through "
        "tit-for-tat, reciprocity, and the shadow of the future.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W8; Axelrod",
    },
    "B6.4": {
        "label": "Zero-sum games and minimax theorem",
        "description": "A game where one player's gain is the other's loss. "
        "Von Neumann's minimax theorem (1928) proves that in zero-sum games, "
        "maximin equals minimax — vindicating the conservative maximin strategy "
        "from decision theory.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W11",
    },
    "B6.5": {
        "label": "Mixed strategy Nash equilibrium",
        "description": "A Nash equilibrium in which players randomize over "
        "strategies. Found by the indifference principle: each player's mixing "
        "probabilities make the opponent indifferent. Counterintuitive: YOUR "
        "mixture is determined by the OPPONENT's payoffs.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W11",
    },
    "B6.6": {
        "label": "Dominance reasoning in games",
        "description": "A strategy is strictly dominated if another strategy yields "
        "strictly higher payoffs in every scenario. Iterated elimination of "
        "dominated strategies can solve games without Nash equilibrium analysis. "
        "Dominance implies NE, but NE does not imply dominance.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W9, W10",
    },

    # ── B7: Coordination Games ─────────────────────────────────────────────────

    "B7.1": {
        "label": "Stag Hunt",
        "description": "Pure coordination problem: cooperation is risky but "
        "rewarding. Trust vs safety. Two equilibria.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W9; Rousseau",
    },
    "B7.2": {
        "label": "Battle of the Sexes",
        "description": "Coordination with conflict: agree to coordinate but "
        "disagree on which equilibrium. Asymmetric payoffs.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W9",
    },
    "B7.3": {
        "label": "Focal points (Schelling points)",
        "description": "Salient solutions that attract coordination without "
        "communication. Culture, context, and expectations matter.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W9; Schelling",
    },
    "B7.4": {
        "label": "Convention (Lewis)",
        "description": "Arbitrary, self-perpetuating solutions to recurrent "
        "coordination problems. Language, money, traffic rules.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W9; Lewis",
    },
    "B7.5": {
        "label": "Hawk-Dove game",
        "description": "Two players contest a resource. If both escalate (Hawk), "
        "costly conflict results. If both back down (Dove), they share. If one "
        "Hawk meets one Dove, Hawk takes all. Unlike PD, the symmetric mixed "
        "strategy is an ESS. Models animal conflict, market competition, and "
        "property rights.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W11, W14",
    },
    "B7.6": {
        "label": "Ultimatum and Trust games",
        "description": "In the Ultimatum Game, a proposer splits a sum and a "
        "responder accepts or rejects (destroying both shares). Backward induction "
        "predicts minimal offers, but empirical data shows ~40% offers and frequent "
        "rejection of low offers. The Trust Game extends this: an investor sends "
        "money (tripled), and a trustee decides how much to return. Tests fairness "
        "norms vs. rational self-interest.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W12, W13",
    },
    "B7.7": {
        "label": "Public Goods game",
        "description": "N players each decide how much to contribute to a shared "
        "pool. Contributions are multiplied and split equally. Free-riding "
        "(contributing nothing) is the dominant strategy, but universal cooperation "
        "Pareto-dominates. Altruistic punishment — paying to penalize free-riders "
        "— can sustain cooperation.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W13",
    },

    # ── B8: Sequential Games ───────────────────────────────────────────────────

    "B8.1": {
        "label": "Game trees and extensive form",
        "description": "Representing games with sequential moves. Decision nodes, "
        "branches, terminal nodes with payoffs.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W10",
    },
    "B8.2": {
        "label": "Backward induction",
        "description": "Reasoning from the end of the game tree to the beginning. "
        "The fundamental solution concept for sequential games.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W10",
    },
    "B8.3": {
        "label": "Subgame perfect equilibrium",
        "description": "Nash equilibrium that survives backward induction. "
        "Eliminates non-credible threats.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W10",
    },
    "B8.4": {
        "label": "Centipede Game paradox",
        "description": "Backward induction says defect immediately, but intuition "
        "says cooperate. Common knowledge of rationality assumption.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W10",
    },
    "B8.5": {
        "label": "Signaling games",
        "description": "A sender with private information chooses an observable "
        "action; a receiver updates beliefs and responds. In a separating "
        "equilibrium, different types send different signals. In a pooling "
        "equilibrium, all types send the same signal. Costly signals (Spence job "
        "market, Zahavi handicap principle) can be credible; cheap talk may not be.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W12",
    },
    "B8.6": {
        "label": "Commitment devices",
        "description": "Mechanisms that bind a player to a future action, making "
        "threats or promises credible. Types: physical (burning bridges), "
        "contractual (penalties), reputational (public pledges), delegational "
        "(agents with different preferences), moral (internalizing norms). "
        "Odysseus binding himself to the mast is the canonical example. The "
        "Paradox of Commitment: rational agents may benefit from restricting "
        "their own future choices.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W12",
    },

    # ── B9: Evolutionary Game Theory ───────────────────────────────────────────

    "B9.1": {
        "label": "Evolutionarily Stable Strategy (ESS)",
        "description": "A strategy that cannot be invaded by a rare mutant. "
        "Hawk-Dove game. No rationality required.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W11; Maynard Smith",
    },
    "B9.2": {
        "label": "Replicator dynamics",
        "description": "Successful strategies spread, unsuccessful ones vanish. "
        "Population-level model of strategy evolution.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W11",
    },
    "B9.3": {
        "label": "Evolution of cooperation",
        "description": "How cooperation emerges among non-rational agents through "
        "kin selection, reciprocity, group selection, or spatial structure.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W11; Skyrms",
    },

    # ── B10: Signaling, Behavioral GT, and Commitment ──────────────────────────

    "B10.1": {
        "label": "Signaling and costly signals",
        "description": "Credible communication requires cost. Handicap Principle. "
        "Education as screening. Cheap talk is worthless.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W12; Spence",
    },
    "B10.2": {
        "label": "Behavioral game theory",
        "description": "Real humans deviate from Nash: fairness (ultimatum game), "
        "altruism (dictator game), reciprocity (trust game), level-k reasoning.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W13",
    },
    "B10.3": {
        "label": "Commitment and precommitment",
        "description": "Binding yourself to change the game. Odysseus and the Sirens. "
        "Physical, contractual, reputational, moral commitment.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W14",
    },
    "B10.4": {
        "label": "Reputation and repeated games",
        "description": "The shadow of the future: reputation as a mechanism for "
        "sustaining cooperation in repeated interactions.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W14",
    },
    "B10.5": {
        "label": "Folk Theorem",
        "description": "In an infinitely repeated game, any payoff profile that "
        "Pareto-dominates the one-shot NE can be sustained as a subgame perfect "
        "equilibrium if players are sufficiently patient (discount factor delta "
        "above a threshold). The threshold for Grim Trigger in PD is "
        "delta* = (T-R)/(T-P). The Folk Theorem explains cooperation but also "
        "predicts too many equilibria — any feasible, individually rational "
        "outcome is sustainable.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W14",
    },

    # ── B13: Behavioral Game Theory ───────────────────────────────────────────

    "B13.1": {
        "label": "Level-k thinking",
        "description": "A model of bounded strategic reasoning. Level-0 players "
        "choose randomly or naively. Level-1 players best-respond to Level-0. "
        "Level-2 best-responds to Level-1, and so on. Most people reason at "
        "Level 1-2. The p-Beauty Contest (guess 2/3 of the average) is the "
        "classic demonstration: NE is 0, but empirical guesses cluster around "
        "22-33 (Level 1-2).",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W13",
    },
    "B13.2": {
        "label": "Social preference models",
        "description": "Models that modify utility functions to include others' "
        "payoffs. Fehr-Schmidt inequality aversion: agents dislike both "
        "disadvantageous inequality (envy) and advantageous inequality (guilt), "
        "with envy weighted more heavily. Bolton-Ockenfels ERC: agents care "
        "about relative payoff share. Charness-Rabin: agents value social "
        "welfare and reciprocity. These models explain Ultimatum Game rejections, "
        "Trust Game cooperation, and Dictator Game giving.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W13",
    },

    # ── B15: Social Choice Theory ─────────────────────────────────────────────

    "B15.1": {
        "label": "Condorcet's Paradox",
        "description": "Even if every individual voter has transitive preferences, "
        "majority-rule voting can produce cyclical (intransitive) group "
        "preferences. Three voters ranking {A, B, C} differently can yield "
        "A > B > C > A. This is a money pump for societies — an agenda-setter "
        "(Master of Ceremonies) who controls the order of pairwise votes can "
        "determine the winner.",
        "pattern_type": "bad_thinking",
        "track": "game_theory",
        "source_notes": "W15",
    },
    "B15.2": {
        "label": "Arrow's Impossibility Theorem",
        "description": "No voting system for three or more candidates can "
        "simultaneously satisfy five reasonable conditions: Universal Domain "
        "(any preferences allowed), Weak Pareto (unanimity respected), "
        "Independence of Irrelevant Alternatives (IIA), Non-Dictatorship, and "
        "Transitivity of social ranking. Each condition is individually "
        "compelling; their joint impossibility is a deep structural result "
        "about collective rationality.",
        "pattern_type": "good_tool",
        "track": "game_theory",
        "source_notes": "W15",
    },
    "B15.3": {
        "label": "Voting systems and strategic voting",
        "description": "Different aggregation rules — plurality, Borda Count, "
        "instant runoff (IRV), approval voting — each satisfy some of Arrow's "
        "conditions but violate others. The Gibbard-Satterthwaite Theorem shows "
        "that any non-dictatorial voting system with 3+ candidates is "
        "manipulable: some voter can benefit by misrepresenting their "
        "preferences. Strategic voting is rational but undermines the "
        "informational purpose of elections.",
        "pattern_type": "dual",
        "track": "game_theory",
        "source_notes": "W15",
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # TRACK C: MICROECONOMICS
    # ═══════════════════════════════════════════════════════════════════════════

    "C1.1": {
        "label": "Opportunity cost",
        "description": "The value of the next-best alternative forgone. "
        "Every choice has a cost, even if no money changes hands.",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 3",
    },
    "C1.2": {
        "label": "Comparative advantage",
        "description": "Trade benefits both parties when each specializes in what "
        "they produce at lower opportunity cost.",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 18",
    },
    "C1.3": {
        "label": "Pareto efficiency",
        "description": "An outcome is Pareto efficient if no alternative makes at "
        "least one person better off without making anyone worse off. A Pareto "
        "improvement makes someone better off and no one worse off. Foundational "
        "welfare concept that applies to markets, policy, games, and social choice.",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "W9 (PD and Pareto), W10 (NE and Pareto), W15 (Arrow's Weak Pareto)",
    },
    "C2.1": {
        "label": "Constrained optimization",
        "description": "Maximizing an objective subject to constraints (budget, time, "
        "resources). Feasible set, indifference curves, optimal choice.",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 3",
    },
    "C2.2": {
        "label": "Marginal analysis",
        "description": "Optimal decisions are made at the margin: do more if "
        "marginal benefit > marginal cost, stop when MB = MC.",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 7",
    },
    "C3.1": {
        "label": "Public goods and free riding",
        "description": "Non-rival, non-excludable goods. Individual incentive to "
        "free ride leads to under-provision. Connection to PD.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 4; connects to B6.1",
    },
    "C3.2": {
        "label": "Commons problems",
        "description": "Shared resources depleted by individual over-use. "
        "Tragedy of the commons. Solutions: regulation, privatization, norms.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 4, 12",
    },
    "C4.1": {
        "label": "Bargaining and fairness",
        "description": "Nash bargaining solution, outside options, power asymmetries. "
        "Connection to ultimatum game (B10.2).",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 5",
    },
    "C4.2": {
        "label": "Principal-agent problems",
        "description": "When one party acts on behalf of another with different "
        "incentives. Moral hazard, adverse selection, incentive design.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 6",
    },
    "C5.1": {
        "label": "Supply, demand, and equilibrium",
        "description": "Market-clearing price. Shifts in supply and demand. "
        "Comparative statics.",
        "pattern_type": "good_tool",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 8",
    },
    "C5.2": {
        "label": "Price controls and deadweight loss",
        "description": "Price ceilings and floors create surpluses or shortages. "
        "Deadweight loss from market distortions.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 8",
    },
    "C6.1": {
        "label": "Externalities",
        "description": "Costs or benefits imposed on third parties not part of "
        "the transaction. Pollution, education spillovers. Pigouvian taxes.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 12",
    },
    "C6.2": {
        "label": "Information asymmetry (markets)",
        "description": "When one side of a market has more information. "
        "Lemons problem, insurance markets. Connects to B10.1.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0 Unit 12; Akerlof",
    },
    "C6.3": {
        "label": "Behavioral economics in markets",
        "description": "How cognitive biases (B5) distort market outcomes. "
        "Nudges, choice architecture, libertarian paternalism.",
        "pattern_type": "dual",
        "track": "microeconomics",
        "source_notes": "CORE Economy 2.0; Thaler & Sunstein",
    },
    "C7.1": {
        "label": "Broken window fallacy",
        "description": "The seen vs unseen: destruction doesn't create wealth "
        "because it ignores opportunity cost.",
        "pattern_type": "bad_thinking",
        "track": "microeconomics",
        "source_notes": "Bastiat; economic fallacies",
    },
    "C7.2": {
        "label": "Zero-sum thinking (economic)",
        "description": "Falsely assuming that economic interactions are zero-sum "
        "when trade creates mutual gains.",
        "pattern_type": "bad_thinking",
        "track": "microeconomics",
        "source_notes": "Common economic fallacy",
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # TRACK D: DENNETT'S THINKING TOOLS
    # ═══════════════════════════════════════════════════════════════════════════

    "D1.1": {
        "label": "Rapoport's Rules",
        "description": "Before criticizing: (1) restate the position so clearly "
        "the opponent says 'I wish I'd said that'; (2) list points of agreement; "
        "(3) mention anything you learned; (4) only then criticize.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps; connects to A1.4",
    },
    "D1.2": {
        "label": "Reductio ad absurdum",
        "description": "Assume the opponent's position and derive a contradiction "
        "or absurd consequence. Powerful but must be used carefully.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "Dennett; classical logic",
    },
    "D1.3": {
        "label": "Occam's Razor",
        "description": "Don't multiply entities beyond necessity. Prefer simpler "
        "explanations when they account for the same evidence.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps",
    },
    "D1.4": {
        "label": "Occam's Broom",
        "description": "The tendency to sweep inconvenient evidence under the rug. "
        "The dishonest cousin of Occam's Razor.",
        "pattern_type": "bad_thinking",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps; Sydney Brenner",
    },
    "D1.5": {
        "label": "Jootsing (jumping out of the system)",
        "description": "Creative thinking requires knowing the rules well enough "
        "to know which ones to break. Master the system, then transcend it.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps; Hofstadter",
    },
    "D1.6": {
        "label": "Deepities",
        "description": "Statements that seem profound but have two readings: "
        "one trivially true, one profound but false. 'Love is just a word.'",
        "pattern_type": "bad_thinking",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps",
    },
    "D1.7": {
        "label": "The 'surely' operator",
        "description": "When someone says 'surely X', they often haven't argued "
        "for X at all — they're trying to pass it as obvious. A red flag.",
        "pattern_type": "bad_thinking",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps",
    },
    "D1.8": {
        "label": "Goulding (going out on a limb)",
        "description": "Dennett's term for risking a bold, specific claim instead of "
        "hedging endlessly. The virtue of intellectual courage.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "Dennett, Intuition Pumps",
    },
    "D2.1": {
        "label": "Satisficing",
        "description": "Choosing an option that is 'good enough' rather than "
        "optimal. Bounded rationality as practical wisdom, not compromise.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "W7; Dennett, Moral First Aid Manual; Simon",
    },
    "D2.2": {
        "label": "The Panglossian Slide",
        "description": "Sliding from 'the best we could do given constraints' to "
        "'the best there is.' Mistaking satisficing for optimizing.",
        "pattern_type": "bad_thinking",
        "track": "dennett_tools",
        "source_notes": "W7; Dennett, Moral First Aid Manual",
    },
    "D2.3": {
        "label": "Conversation-stoppers",
        "description": "Rights, taboos, moral rules that terminate deliberation. "
        "Earn their keep by being robustly debate-terminating, not by being "
        "provably correct. Can be good (prevent paralysis) or bad (prevent growth).",
        "pattern_type": "dual",
        "track": "dennett_tools",
        "source_notes": "W7; Dennett, Moral First Aid Manual; Thought Stoppers",
    },
    "D2.4": {
        "label": "Wolf's Dilemma",
        "description": "The dilemma of the reflective satisficer: once you know "
        "you're using heuristics, should you override them?",
        "pattern_type": "dual",
        "track": "dennett_tools",
        "source_notes": "W7; Dennett, Moral First Aid Manual",
    },
    "D2.5": {
        "label": "The Frame Problem",
        "description": "The computational problem of determining what changes and "
        "what stays the same after an action. Relevant to AI and to human reasoning.",
        "pattern_type": "dual",
        "track": "dennett_tools",
        "source_notes": "Dennett; AI literature",
    },
    "D2.6": {
        "label": "The Moral First Aid Manual",
        "description": "Dennett's proposal: instead of seeking the One True Ethical "
        "Theory, build a practical guide — triage rules for moral emergencies. "
        "The organizing frame for the entire project.",
        "pattern_type": "good_tool",
        "track": "dennett_tools",
        "source_notes": "W7, W14; Dennett, Moral First Aid Manual",
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # TRACK E: COGNITIVE BIASES (from yourbias.is poster)
    # ═══════════════════════════════════════════════════════════════════════════

    "E1.1": {
        "label": "Fundamental attribution error",
        "description": "Judging others on character but yourself on situation. "
        "Lack of charity toward others' circumstances.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.2": {
        "label": "Confirmation bias",
        "description": "Looking for ways to justify existing beliefs. "
        "Dismissing disconfirming evidence.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.3": {
        "label": "Anchoring",
        "description": "The first piece of information disproportionately "
        "influences subsequent judgments.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.4": {
        "label": "Dunning-Kruger effect",
        "description": "The less you know, the more confident you are. "
        "Experts underestimate, novices overestimate their competence.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.5": {
        "label": "Availability heuristic",
        "description": "Judgments influenced by what springs most easily to mind: "
        "recent, emotional, or unusual memories seem more relevant.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.6": {
        "label": "Belief bias",
        "description": "If a conclusion supports existing beliefs, you'll "
        "rationalize anything that supports it.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.7": {
        "label": "Self-serving bias",
        "description": "Attributing failures to external factors but successes "
        "to personal qualities.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.8": {
        "label": "Curse of knowledge",
        "description": "Once you understand something, you assume it's obvious "
        "to everyone else.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.9": {
        "label": "Optimism bias",
        "description": "Overestimating the likelihood of positive outcomes.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.10": {
        "label": "Pessimism bias",
        "description": "Overestimating the likelihood of negative outcomes.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.11": {
        "label": "Negativity bias",
        "description": "Negative things disproportionately influence thinking. "
        "Pain of loss felt more keenly than gratification of gain.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster; connects to B5.2",
    },
    "E1.12": {
        "label": "Groupthink",
        "description": "Social dynamics override best outcomes. Dissent suppressed "
        "by conformity pressure.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.13": {
        "label": "Placebo effect",
        "description": "Believing a treatment works can produce real effects, "
        "but only for mind-influenced symptoms.",
        "pattern_type": "dual",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.14": {
        "label": "Reactance",
        "description": "Doing the opposite of what someone tries to make you do. "
        "Overcompensating when liberty is constrained.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.15": {
        "label": "Spotlight effect",
        "description": "Overestimating how much others notice your appearance "
        "and behavior.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.16": {
        "label": "Just-world hypothesis",
        "description": "Believing the world is fair: people get what they deserve. "
        "Leads to victim-blaming.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.17": {
        "label": "Declinism",
        "description": "Seeing the past as better than it was and expecting the "
        "future to be worse than likely.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.18": {
        "label": "Backfire effect",
        "description": "When core beliefs are challenged, believing even more "
        "strongly. Motivated reasoning.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.19": {
        "label": "Barnum effect (Forer effect)",
        "description": "Seeing personal specifics in vague statements. "
        "Basis of astrology and cold reading.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.20": {
        "label": "Sunk cost fallacy (cognitive)",
        "description": "Irrationally clinging to things that have already cost you "
        "something. Connects to B5.8 (decision-theoretic version).",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.21": {
        "label": "Framing effect (cognitive)",
        "description": "Being unduly influenced by context and delivery. "
        "Connects to B5.5 (decision-theoretic version).",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.22": {
        "label": "In-group bias",
        "description": "Unfairly favoring those who belong to your group.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.23": {
        "label": "Halo effect",
        "description": "How much you like someone influences your other "
        "judgments of them.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
    "E1.24": {
        "label": "Bystander effect",
        "description": "Assuming someone else will act in an emergency. "
        "Diffusion of responsibility in groups.",
        "pattern_type": "bad_thinking",
        "track": "cognitive_biases",
        "source_notes": "Bias poster",
    },
}


# ─── Utility functions ────────────────────────────────────────────────────────


def get_codes_by_track(track: str) -> dict[str, dict]:
    """Return all taxonomy entries for a given track."""
    return {k: v for k, v in TAXONOMY.items() if v["track"] == track}


def get_codes_by_pattern_type(pattern_type: str) -> dict[str, dict]:
    """Return all taxonomy entries of a given pattern type."""
    return {k: v for k, v in TAXONOMY.items() if v["pattern_type"] == pattern_type}


def get_codes_by_group(prefix: str) -> dict[str, dict]:
    """Return all taxonomy entries starting with a prefix (e.g. 'A7', 'B5')."""
    return {k: v for k, v in TAXONOMY.items() if k.startswith(prefix)}


def get_label(code: str) -> str:
    """Get the human-readable label for a taxonomy code."""
    entry = TAXONOMY.get(code)
    if entry is None:
        raise KeyError(f"Unknown taxonomy code: {code}")
    return entry["label"]


def get_track(code: str) -> str:
    """Get the track for a taxonomy code."""
    entry = TAXONOMY.get(code)
    if entry is None:
        raise KeyError(f"Unknown taxonomy code: {code}")
    return entry["track"]


def all_codes() -> list[str]:
    """Return all taxonomy codes in order."""
    return list(TAXONOMY.keys())


def summary() -> dict[str, int]:
    """Return count of codes per track."""
    counts: dict[str, int] = {}
    for entry in TAXONOMY.values():
        track = entry["track"]
        counts[track] = counts.get(track, 0) + 1
    return counts


if __name__ == "__main__":
    print(f"Total taxonomy codes: {len(TAXONOMY)}")
    print("\nCodes per track:")
    for track, count in summary().items():
        print(f"  {track}: {count}")
    print("\nCodes per pattern type:")
    for ptype in ("good_tool", "bad_thinking", "dual"):
        count = len(get_codes_by_pattern_type(ptype))
        print(f"  {ptype}: {count}")
