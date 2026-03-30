"""
Source material loader for anchor crafting.

Maps taxonomy codes to relevant passages from Bert's lecture notes,
the bias/fallacy poster text, and decision theory course notes.

For copyrighted PDFs (not in git), we store the pedagogically relevant
excerpts inline (short factual descriptions, fair use for educational tooling).
"""

from __future__ import annotations

import re
from pathlib import Path

from config import CRITICAL_THINKING_NOTES, DECISION_THEORY_NOTES
from taxonomy import TAXONOMY

# ─── Lazy-loaded file caches ─────────────────────────────────────────────────

_file_cache: dict[str, str] = {}


def _read_file(path: Path) -> str:
    """Read and cache a text file."""
    key = str(path)
    if key not in _file_cache:
        if path.exists():
            _file_cache[key] = path.read_text(encoding="utf-8", errors="replace")
        else:
            _file_cache[key] = ""
    return _file_cache[key]


def _extract_section(text: str, start_pattern: str, end_pattern: str | None = None, max_lines: int = 80) -> str:
    """Extract a section of text between two patterns."""
    lines = text.split("\n")
    start_idx = None
    for i, line in enumerate(lines):
        if re.search(start_pattern, line, re.IGNORECASE):
            start_idx = i
            break
    if start_idx is None:
        return ""

    if end_pattern:
        end_idx = None
        for i in range(start_idx + 1, len(lines)):
            if re.search(end_pattern, lines[i], re.IGNORECASE):
                end_idx = i
                break
        if end_idx is None:
            end_idx = min(start_idx + max_lines, len(lines))
    else:
        end_idx = min(start_idx + max_lines, len(lines))

    return "\n".join(lines[start_idx:end_idx]).strip()


def _read_lecture_note(week_file: str) -> str:
    """Read a decision theory lecture note by filename pattern."""
    dt_dir = DECISION_THEORY_NOTES
    for f in dt_dir.iterdir():
        if week_file.lower() in f.name.lower() or f.name.startswith(week_file):
            return _read_file(f)
    return ""


# ─── PHIL 201 section mappings ────────────────────────────────────────────────

# Maps taxonomy codes to (start_pattern, end_pattern) in the PHIL 201 notes
_PHIL201_SECTIONS: dict[str, tuple[str, str | None]] = {
    "A1.1": (r"1\.1 What is an argument", r"1\.2 Identifying"),
    "A1.2": (r"1\.2 Identifying Arguments", r"1\.3 Arguments vs"),
    "A1.3": (r"Standard Form:", r"1\.2 Identifying"),
    "A1.4": (r"principle of charity", r"1\.6 Validity"),
    "A1.5": (r"1\.9 Arguments with missing premises", r"1\.10 Assuring"),
    "A1.6": (r"1\.3 Arguments vs Explanations", r"1\.4 More complex"),
    "A1.7": (r"1\.4 More complex argument structures", r"1\.5 Paraphrasing"),
    "A2.1": (r"1\.6 Validity", r"1\.8 Deductive"),
    "A2.2": (r"2\.2 Propositional logic", r"2\.3 Negation"),
    "A2.3": (r"2\.6 The truth table test", r"2\.7 Conditionals"),
    "A2.4": (r"2\.11 Proofs and 8 valid forms", r"2\.12 How to construct"),
    "A2.5": (r"2\.12 How to construct proofs", r"2\.14 Categorical"),
    "A2.6": (r"2\.14 Categorical Logic", r"2\.15 Venn Diagram"),
    "A2.7": (r"2\.9 Material Equivalence", r"2\.10 Tautologies"),
    "A2.8": (r"1\.8 Deductive vs Inductive", r"September 4"),
    "A3.1": (r"3\.1 Inductive arguments and statistical", r"3\.2 Inference to the best"),
    "A3.2": (r"3\.2 Inference to the best explanation", r"3\.3 Analogical"),
    "A3.3": (r"3\.3 Analogical arguments", r"3\.4 Causal Reasoning"),
    "A3.4": (r"3\.4 Causal Reasoning", r"3\.5 Probability"),
    "A3.5": (r"correlation is not causation", r"3\.5 Probability"),
    "A4.1": (r"3\.5 Probability", r"3\.6 The conjunction fallacy"),
    "A4.2": (r"3\.7 The base rate fallacy", r"BERT: TEST 3"),
    "A4.3": (r"3\.7 The base rate fallacy", r"BERT: TEST 3"),
    "A5.1": (r"Modus ponens vs Denying the Antecedent", r"An informal fallacy"),
    "A5.2": (r"Modus tollens vs Affirming the Consequent", r"An informal fallacy"),
    "A5.3": (r"4\.2\.2 Causal slippery slope", r"4\.3 Fallacies of relevance"),
    "A6.1": (r"4\.1\.1 Composition Fallacy", r"4\.1\.2 Division"),
    "A6.2": (r"4\.1\.2 Division fallacy", r"4\.1\.3 Begging"),
    "A6.3": (r"4\.1\.3 Begging the question", r"4\.1\.4 False"),
    "A6.4": (r"4\.1\.4 False dichotom", r"4\.1\.5 Equivocation"),
    "A6.5": (r"4\.1\.5 Equivocation", r"4\.2 Slippery slope"),
    "A6.6": (r"4\.2\.1 Conceptual slippery slope", r"4\.2\.2 Causal"),
    "A7.1": (r"4\.3\.1 Ad hominem", r"4\.3\.2 Straw man"),
    "A7.2": (r"4\.3\.2 Straw man", r"4\.3\.3 Tu quoque"),
    "A7.3": (r"4\.3\.3 Tu quoque", r"4\.3\.4 Genetic"),
    "A7.4": (r"4\.3\.4 Genetic fallacy", r"4\.3\.5 Appeal to consequences"),
    "A7.5": (r"4\.3\.5 Appeal to consequences", r"4\.3\.6 Appeal to authority"),
    "A7.6": (r"4\.3\.6 Appeal to authority", r"TURNING TO DENNETT"),
    "A8.1": (r"3\.6 The conjunction fallacy", r"3\.7 The base rate"),
    "A8.2": (r"3\.7 The base rate fallacy", r"BERT: TEST 3"),
    "A8.3": (r"3\.8 The small numbers fallacy", r"3\.9 Regression"),
    "A8.4": (r"3\.9 Regression to the mean", r"3\.10 Gambler"),
    "A8.5": (r"3\.10 Gambler.s Fallacy", r"4\.1 Formal vs"),
    "A8.6": (r"hasty generalization", r"A biased sample"),
    "A8.7": (r"False cause fallacy", r"3\.5 Probability"),
    "A9.1": (r"1\.11 Evaluative Language", r"1\.12 Analyzing"),
    "A9.2": (r"1\.10 Assuring, guarding", r"1\.11 Evaluative"),
    # Dennett tools from PHIL 201 notes
    "D1.1": (r"Rapoport.s Rules", r"4\. Sturgeon"),
    "D1.2": (r"Reductio ad Absurdum", r"3\. Rapoport"),
    "D1.3": (r"5\. Occam.s Razor", r"6\. Occam.s Broom"),
    "D1.4": (r"6\. Occam.s Broom", r"7\. Using Lay"),
    "D1.5": (r"8\. Jootsing", r"9\. Three Species"),
    "D1.6": (r"12\. What Is a Deepity", r"These twelve tools"),
    "D1.7": (r"10\. The .Surely. Operator", r"11\. Rhetorical"),
}

# ─── Fallacy poster content (from yourbias.is / yourfallacy.is) ───────────────
# Short factual descriptions — fair use for educational tooling

_FALLACY_POSTER: dict[str, str] = {
    "A7.7": (
        "APPEAL TO EMOTION (from Logical Fallacies poster)\n"
        "Manipulating an emotional response in place of a valid or compelling argument.\n"
        "Appeals to emotion include appeals to fear, envy, hatred, pity, guilt, and more.\n"
        "Example: Luke didn't want to eat his sheep brains with chopped liver and brussels "
        "sprouts, but his father told him to think about the poor, starving children in a "
        "third world country who weren't fortunate enough to have any food at all."
    ),
    "A7.8": (
        "APPEAL TO NATURE (from Logical Fallacies poster)\n"
        "Making the argument that because something is 'natural' it is therefore valid, "
        "justified, inevitable, good, or ideal.\n"
        "Example: The medicine man rolled into town offering various natural remedies, "
        "such as very special plain water. He said that it was only natural that people "
        "should be wary of 'artificial' medicines like antibiotics."
    ),
    "A7.9": (
        "BANDWAGON (from Logical Fallacies poster)\n"
        "Appealing to popularity or the fact that many people do something as an "
        "attempted form of validation.\n"
        "Example: Shamus pointed a finger at Sean and asked him to explain how so many "
        "people could believe in leprechauns if they're only a silly old superstition."
    ),
    "A7.10": (
        "BURDEN OF PROOF (from Logical Fallacies poster)\n"
        "Saying that the burden of proof lies not with the person making the claim, "
        "but with someone else to disprove.\n"
        "Example: Bertrand declares that a teapot is, at this very moment, in orbit "
        "around the Sun between the Earth and Mars, and that because no one can prove "
        "him wrong his claim is therefore a valid one."
    ),
    "A7.11": (
        "PERSONAL INCREDULITY (from Logical Fallacies poster)\n"
        "Saying that because one finds something difficult to understand, "
        "it's therefore not true.\n"
        "Example: Kirk drew a picture of a fish and a human and asked Richard if he "
        "really thought we were stupid enough to believe that a fish somehow turned "
        "into a human through just, like, random things happening over time."
    ),
    "A7.12": (
        "SPECIAL PLEADING / NO TRUE SCOTSMAN (from Logical Fallacies poster)\n"
        "Moving the goalposts or making up exceptions when a claim is shown to be false.\n"
        "Example: Angus declares that Scotsmen do not put sugar on their porridge, to "
        "which Lachlan points out that he is a Scotsman and puts sugar on his porridge. "
        "Furious, Angus yells that no true Scotsman sugars his porridge."
    ),
    "A7.13": (
        "LOADED QUESTION (from Logical Fallacies poster)\n"
        "Asking a question that has an assumption built into it so that it can't be "
        "answered without appearing guilty.\n"
        "Example: Grace and Helen were both interested in Brad. One day, with Brad "
        "sitting within earshot, Grace asked whether Helen was having any problems "
        "with a fungal infection."
    ),
    "A7.14": (
        "TEXAS SHARPSHOOTER (from Logical Fallacies poster)\n"
        "Cherry-picking data clusters to suit an argument, or finding a pattern "
        "to fit a presumption.\n"
        "Example: The makers of Sugarette Candy Drinks point to research showing "
        "that of the five countries where Sugarette drinks sell the most, three are "
        "in the top ten healthiest countries, therefore Sugarette drinks are healthy."
    ),
    "A7.15": (
        "MIDDLE GROUND (from Logical Fallacies poster)\n"
        "Saying that a compromise, or middle point, between two extremes must be the truth.\n"
        "Example: Holly said that vaccinations caused autism in children, but her friend "
        "Caleb said that this claim had been debunked. Their friend Alice offered a "
        "compromise that vaccinations cause some autism."
    ),
    "A7.16": (
        "ANECDOTAL (from Logical Fallacies poster)\n"
        "Using personal experience or an isolated example instead of a valid argument, "
        "especially to dismiss statistics.\n"
        "Example: Jason said that was all cool and everything, but his grandfather "
        "smoked 30 cigarettes a day and lived until 97 — so don't believe everything "
        "you read about meta analyses of well-designed studies."
    ),
    "A9.3": (
        "THE FALLACY FALLACY (from Logical Fallacies poster)\n"
        "Presuming a claim to be necessarily wrong because a fallacy has been committed.\n"
        "It is entirely possible to make a claim that is true and justify it with various "
        "fallacies and poor arguments.\n"
        "Example: Recognising that Amanda had committed a fallacy in arguing that we "
        "should eat healthy food because a nutritionist said it was popular, Alyse said "
        "we should therefore eat bacon double cheeseburgers every day."
    ),
}

# ─── Cognitive bias poster content ────────────────────────────────────────────

_BIAS_POSTER: dict[str, str] = {
    "E1.1": "FUNDAMENTAL ATTRIBUTION ERROR: You judge others on their character, but yourself on the situation. If you haven't had a good night's sleep, you know why you're being slow; but if you observe someone else being slow you might presume them to just be a slow person.",
    "E1.2": "CONFIRMATION BIAS: You look for ways to justify your existing beliefs. We automatically find ways to make new information fit our existing narratives and to dismiss information that does not. 'The first principle is that you must not fool yourself — and you are the easiest person to fool.' — Richard Feynman",
    "E1.3": "ANCHORING: The first thing you judge influences your judgment of all that follows. Be especially mindful during financial negotiations such as houses, cars, and salaries. The initial price offered has a significant effect.",
    "E1.4": "DUNNING-KRUGER EFFECT: The more you know, the less confident you're likely to be. Experts tend to underestimate their ability; it's easy to be over-confident when you have only a simple idea of how things are. 'The whole problem with the world is that fools and fanatics are so certain of themselves, yet wiser people so full of doubts.' — Bertrand Russell",
    "E1.5": "AVAILABILITY HEURISTIC: Your judgments are influenced by what springs most easily to mind. How recent, emotionally powerful, or unusual your memories are can make them seem more relevant, causing you to apply them too readily.",
    "E1.6": "BELIEF BIAS: If a conclusion supports your existing beliefs, you'll rationalize anything that supports it. Our ideas become impervious to criticism and are perpetually reinforced. A useful thing to ask is 'when and how did I get this belief?'",
    "E1.7": "SELF-SERVING BIAS: You believe your failures are due to external factors, yet you're personally responsible for your successes. Many of us enjoy unearned privileges, luck and advantages. It's easy to tell ourselves we deserve these things, whilst blaming circumstance when things don't go our way.",
    "E1.8": "CURSE OF KNOWLEDGE: Once you understand something you presume it to be obvious to everyone. We build complex networks of understanding and forget how intricate the path to our available knowledge really is.",
    "E1.9": "OPTIMISM BIAS: You overestimate the likelihood of positive outcomes. There can be benefits to a positive attitude, but it's unwise to allow it to adversely affect our ability to make rational judgments.",
    "E1.10": "PESSIMISM BIAS: You overestimate the likelihood of negative outcomes. Pessimism is often a defense mechanism against disappointment, or it can be the result of depression and anxiety disorders.",
    "E1.11": "NEGATIVITY BIAS: You allow negative things to disproportionately influence your thinking. The pain of loss and hurt are felt more keenly and persistently than the fleeting gratification of pleasant things.",
    "E1.12": "GROUPTHINK: You let the social dynamics of a group situation override the best outcomes. Dissent can be uncomfortable and dangerous to one's social standing, so often the most confident or first voice will determine group decisions.",
    "E1.13": "PLACEBO EFFECT: If you believe you're taking medicine it can sometimes 'work' even if it's fake. The placebo effect can work for stuff that our mind influences (such as pain) but not so much for things like viruses or broken bones.",
    "E1.14": "REACTANCE: You'd rather do the opposite of what someone is trying to make you do. When we feel our liberty is being constrained, our inclination is to resist, however in doing so we can over-compensate.",
    "E1.15": "SPOTLIGHT EFFECT: You overestimate how much people notice how you look and act. Most people are much more concerned about themselves than they are about you.",
    "E1.16": "JUST-WORLD HYPOTHESIS: Your preference for a just world makes you presume that it exists. A world in which people don't always get what they deserve and injustice happens is uncomfortable but also reality.",
    "E1.17": "DECLINISM: You see the past as better than it was, and expect the future to be worse than is likely. Despite living in the most peaceful and prosperous time in history, many people believe things are getting worse.",
    "E1.18": "BACKFIRE EFFECT: When your core beliefs are challenged, it can cause you to believe even more strongly. We can experience being wrong about some ideas as an attack upon our very selves. 'It ain't what you don't know that gets you into trouble. It's what you know for sure that just ain't so.' — Mark Twain",
    "E1.19": "BARNUM EFFECT (FORER EFFECT): You see personal specifics in vague statements by filling in the gaps. Psychics, astrologers and others use this bias to make it seem like they're telling you something relevant.",
    "E1.20": "SUNK COST FALLACY: You irrationally cling to things that have already cost you something. When we've invested our time, money, or emotion into something, it hurts us to let it go. Ask yourself: had I not already invested something, would I still do so now?",
    "E1.21": "FRAMING EFFECT: You allow yourself to be unduly influenced by context and delivery. We all like to think that we think independently, but all of us are influenced by delivery, framing and subtle cues.",
    "E1.22": "IN-GROUP BIAS: You unfairly favor those who belong to your group. We presume we're fair and impartial, but we automatically favor those who are most like us or belong to our groups.",
    "E1.23": "HALO EFFECT: How much you like someone influences your other judgments of them. Our judgments are associative and automatic, so if we want to be objective we need to consciously control for irrelevant influences.",
    "E1.24": "BYSTANDER EFFECT: You presume someone else is going to do something in an emergency situation. When something terrible is happening in a public setting we can experience a kind of shock and mental paralysis that distracts us from personal responsibility.",
}


# ─── Decision theory lecture note mappings ────────────────────────────────────

_DT_LECTURE_SECTIONS: dict[str, tuple[str, str | None, str | None]] = {
    # (week_file_pattern, start_pattern, end_pattern)
    # ── Decision Theory (W1–W7, single files per week) ──────────────────────
    "B1.1": ("W1", r"Acts.*what an agent can control", r"Type 2.*Puzzle"),
    "B1.2": ("W1", r"Dominance Principle", r"Type 2.*Puzzle"),
    "B1.3": ("W2", r"Maximax.*Optimist", r"Maximin.*Pessimist"),
    "B1.4": ("W2", r"Maximin.*Pessimist", r"III\. The Shift to Cardinal"),
    "B1.5": ("W2", r"IV\. Minimax Regret", None),
    "B2.1": ("W3", r"Fair Betting Rate", r"II\. The Dutch Book"),
    "B2.2": ("W3", r"II\. The Dutch Book", r"III\. The Axioms"),
    "B2.3": ("W3", r"III\. The Axioms of Probability", None),
    "B2.4": ("W3", r"Subjective.*Objective", None),
    "B3.1": ("W4", r"II\. The Mechanics of MEU", r"III\. Sensitivity"),
    "B3.2": ("W4", r"Why Rank is Not Enough", r"II\. The Mechanics"),
    "B3.3": ("W4", r"III\. Sensitivity to Risk", None),
    "B3.4": ("W4", r"Transitivity", r"Independence"),
    "B3.5": ("W4", r"Independence of Irrelevant", None),
    "B3.6": ("W1", r"Pascal.s Wager", None),
    "B4.1": ("W5", r"Allais Setup", r"II\. The Fortress"),
    "B4.2": ("W5", r"Sure Thing Principle", r"III\. The Bridge"),
    "B4.3": ("W5", r"Newcomb", None),
    "B4.4": ("W5", r"Ellsberg", None),
    "B4.5": ("W5", r"Reflection Effect", None),
    "B5.1": ("W6", r"Reference Point", r"2\. The Value Function"),
    "B5.2": ("W6", r"Loss aversion", r"III\. Loss Aversion in Action"),
    "B5.3": ("W6", r"probability.*weighting|π\(p\)", None),
    "B5.5": ("W6", r"[Ff]raming", None),
    "B5.8": ("W6", r"sunk cost|Sunk Cost", None),
    # ── Game Theory (W9–W14, multiple files per week — use specific prefixes) ─
    # W9: PD structure and dominance
    "B6.1": ("W9_The_Prisoners", r"Prisoner.s Dilemma.*Formal Structure", r"III\. The General Form"),
    "B6.6": ("W9_The_Prisoners", r"Chalk Talk.*Verify the Dominance", r"3\. Pareto Efficiency"),
    "C1.3": ("W9_The_Prisoners", r"Pareto Efficien", r"IV\. Real-World"),
    # W9: Coordination games
    "B7.1": ("W9_Coordination", r"Stag Hunt", r"Battle of the Sexes"),
    "B7.2": ("W9_Coordination", r"Battle of the Sexes", r"Pure Coordination"),
    "B7.3": ("W9_Coordination", r"Schelling|focal point", None),
    "B7.4": ("W9_Coordination", r"Convention.*Lewis", None),
    # W10: Nash Equilibrium, dominance vs NE
    # (W10_Nash has the NE definition and dominance-vs-NE discussion)
    # W10: Sequential games and backward induction
    "B8.1": ("W10_Sequential", r"Extensive Form.*Game Tree", r"III\. Subgame Perfect"),
    "B8.2": ("W10_Sequential", r"Backward [Ii]nduction", r"IV\. First-Mover"),
    "B8.4": ("W10_Sequential", r"Centipede", r"II\. Why Is This a Paradox"),
    # W11: Mixed strategies, zero-sum, Hawk-Dove
    "B6.4": ("W11_Mixed", r"Zero-Sum Games.*Definition", r"III\. The Minimax"),
    "B6.5": ("W11_Mixed", r"Calculating Mixed Strategy", r"V\. Chalk Talk.*Matching Pennies"),
    "B7.5": ("W11_Mixed", r"Hawk-Dove", r"V\. Philosophical Conclusion"),
    # W11: Evolutionary GT
    "B9.1": ("W11_Evolutionary", r"Evolutionarily Stable", r"III\."),
    "B9.2": ("W11_Evolutionary", r"[Rr]eplicator [Dd]ynamics", None),
    # W12: Sequential games, commitment, signaling (new combined file)
    "B8.5": ("W12_Sequential_Games_Backwards", r"Signaling Games", r"V\. Bridge to Week 13"),
    "B8.6": ("W12_Sequential_Games_Backwards", r"III\. Commitment Devices", r"IV\. Signaling Games"),
    # W12: Signaling deep-dive (old file)
    "B10.1": ("W12_Signaling", r"Costly [Ss]ignal", None),
    # W13: Behavioral game theory
    "B7.6": ("W13", r"II\. The Ultimatum Game", r"III\. The Dictator Game"),
    "B7.7": ("W13", r"Public Goods Game", r"2\. Centipede Game"),
    "B10.2": ("W13", r"Three Games That Broke", None),
    "B13.1": ("W13", r"Level-k Reasoning", r"II\. Social Preferences"),
    "B13.2": ("W13", r"Fehr-Schmidt Model", r"III\. Applications and Extensions"),
    # W14: Repeated games and folk theorem (new file)
    "B10.5": ("W14_Repeated", r"III\. Infinitely.*Folk Theorem", r"IV\. Sustaining Cooperation"),
    # W14: Synthesis, commitment, moral first aid (old file)
    "B10.3": ("W14_Synthesis", r"Commitment and Precommitment", r"II\. Commitment in Game"),
    # W15: Social choice and Arrow's theorem
    "B15.1": ("W15", r"Condorcet.s Paradox", r"III\. Voting Systems"),
    "B15.2": ("W15", r"V\. Arrow.s Five Conditions", r"VII\. Which Condition Fails"),
    "B15.3": ("W15", r"III\. Voting Systems.*Can We Do Better", r"V\. Arrow.s Five Conditions"),
    # ── Dennett's Tools (W7, single file) ───────────────────────────────────
    "D2.1": ("W7", r"III\. Satisficing", None),
    "D2.2": ("W7", r"Panglossian", None),
    "D2.3": ("W7", r"[Cc]onversation.stopper", None),
    "D2.6": ("W14_Synthesis", r"Moral First Aid Manual", None),
}


# ─── Main loader ──────────────────────────────────────────────────────────────


def get_source_passage(code: str) -> str:
    """
    Load the best available source material for a taxonomy code.

    Returns a passage combining:
    1. Relevant section from lecture notes (if mapped)
    2. Poster text (if applicable)
    3. Taxonomy description as fallback
    """
    entry = TAXONOMY.get(code)
    if entry is None:
        return f"(Unknown taxonomy code: {code})"

    passages: list[str] = []

    # 1. Try PHIL 201 notes
    if code in _PHIL201_SECTIONS:
        start, end = _PHIL201_SECTIONS[code]
        phil201_text = _read_file(CRITICAL_THINKING_NOTES)
        if phil201_text:
            section = _extract_section(phil201_text, start, end)
            if section:
                passages.append(f"--- From Bert's PHIL 201 Lecture Notes ---\n{section}")

    # 2. Try decision theory lecture notes
    if code in _DT_LECTURE_SECTIONS:
        week_pattern, start, end = _DT_LECTURE_SECTIONS[code]
        note_text = _read_lecture_note(week_pattern)
        if note_text:
            section = _extract_section(note_text, start, end)
            if section:
                passages.append(f"--- From Decision Theory Lecture {week_pattern} ---\n{section}")

    # 3. Try fallacy poster
    if code in _FALLACY_POSTER:
        passages.append(f"--- From Logical Fallacies Poster ---\n{_FALLACY_POSTER[code]}")

    # 4. Try bias poster
    if code in _BIAS_POSTER:
        passages.append(f"--- From Cognitive Biases Poster ---\n{_BIAS_POSTER[code]}")

    # 5. Always include the taxonomy description
    passages.append(
        f"--- Taxonomy Entry ---\n"
        f"Code: {code}\n"
        f"Label: {entry['label']}\n"
        f"Description: {entry['description']}\n"
        f"Pattern type: {entry['pattern_type']}\n"
        f"Source references: {entry.get('source_notes', 'N/A')}"
    )

    return "\n\n".join(passages)


def get_source_summary(code: str) -> str:
    """One-line summary of what source material is available for a code."""
    sources = []
    if code in _PHIL201_SECTIONS:
        sources.append("PHIL201")
    if code in _DT_LECTURE_SECTIONS:
        week = _DT_LECTURE_SECTIONS[code][0]
        sources.append(f"DT-{week}")
    if code in _FALLACY_POSTER:
        sources.append("FallacyPoster")
    if code in _BIAS_POSTER:
        sources.append("BiasPoster")
    if not sources:
        sources.append("taxonomy-only")
    return ", ".join(sources)


if __name__ == "__main__":
    # Show source availability for all codes
    from taxonomy import TAXONOMY, summary

    total_with_sources = 0
    print(f"{'Code':<8} {'Label':<40} {'Sources'}")
    print("-" * 80)
    for code in sorted(TAXONOMY.keys()):
        entry = TAXONOMY[code]
        src = get_source_summary(code)
        has_real = "taxonomy-only" not in src
        if has_real:
            total_with_sources += 1
        marker = "" if has_real else " (no source material)"
        print(f"{code:<8} {entry['label']:<40} {src}{marker}")

    print(f"\n{total_with_sources}/{len(TAXONOMY)} codes have source material beyond taxonomy")
