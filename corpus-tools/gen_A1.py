#!/usr/bin/env python3
"""Generate 350 synthetic training records for A1.1-A1.7 argument structure."""
import json, os

OUTPUT = "/Users/bbaum/Documents/claude-projects/good-thinking-bot/corpus-tools/output/synthetic_A1_fill.jsonl"

# We'll build all records in a list, then write once.
records = []

# ─── HELPERS ───
def rec(id_, code, label, tier, scenario, structure, assessment, game_hooks, source_mat):
    return {
        "id": id_,
        "taxonomy_code": code,
        "taxonomy_label": label,
        "track": "logic_critical_thinking",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": scenario,
        "structure": structure,
        "assessment": assessment,
        "game_hooks": game_hooks,
        "source": {
            "type": "synthetic_verified",
            "source_material": source_mat,
            "original_id": None
        }
    }

def scen(context, text, speaker_context):
    return {"context": context, "text": text, "speaker_context": speaker_context}

def struct(pname, pdesc, formal, why_right, related, counterpoint):
    return {
        "pattern_name": pname,
        "pattern_description": pdesc,
        "formal_form": formal,
        "why_wrong": None,
        "why_right": why_right,
        "related_patterns": related,
        "counterpoint": counterpoint
    }

def assess(prompt, rubric_list, fuw, fur):
    rubric = [{"level": i, "description": d} for i, d in enumerate(rubric_list)]
    return {
        "identification_prompt": prompt,
        "rubric": rubric,
        "follow_up_if_wrong": fuw,
        "follow_up_if_right": fur
    }

def hooks(personality, seed, resolution):
    return {
        "npc_personality": personality,
        "npc_dialogue_seed": seed,
        "resolution_path": resolution
    }

# ═══════════════════════════════════════════════════════════════════
# A1.1 — Identifying arguments (drill) — 50 records
# ═══════════════════════════════════════════════════════════════════
a11_data = [
    # 1
    {
        "ctx": "The player enters the Ironvale courthouse where Magistrate Holt is delivering a ruling on a land dispute between two farmers.",
        "text": "Magistrate Holt speaks: 'The eastern boundary belongs to Farmer Elda. Since the original charter grants all land east of the millstream to the Elda family, and the millstream has not moved, therefore the disputed strip is rightfully hers.'",
        "spk": "Magistrate Holt, a precise and legalistic judge who always cites documentary evidence.",
        "pname": "Argument with premise and conclusion indicators",
        "pdesc": "Holt provides a reason (the charter's grant, the unchanged millstream) and draws a conclusion (the land belongs to Elda). The words 'since' and 'therefore' signal premise and conclusion.",
        "formal": "Since P1 and P2, therefore C.",
        "why_right": "This is an argument because it offers premises intended to support the truth of a conclusion. The indicator words 'since' (premise) and 'therefore' (conclusion) confirm the logical structure.",
        "related": ["A1.2", "A1.3"],
        "counter": "Not every use of 'since' marks a premise — it can indicate time ('since last Tuesday'). The substitution test helps: replacing 'since' with 'because' preserves meaning here, confirming it is a premise indicator.",
        "prompt": "Magistrate Holt just delivered his ruling. Is he making an argument, giving an explanation, issuing a command, or simply describing something? What tips you off?",
        "rubric": [
            "Player cannot distinguish Holt's statement from a description or command.",
            "Player senses there is reasoning but cannot identify what makes it an argument.",
            "Player recognizes Holt is trying to justify a conclusion but does not identify the indicator words.",
            "Player identifies this as an argument, noting 'since' introduces premises and 'therefore' introduces the conclusion.",
            "Player identifies the argument, the indicator words, applies the substitution test to confirm 'since' is a premise indicator (not temporal), and explains why this differs from a mere description of legal facts."
        ],
        "fuw": "Look at what Holt is trying to do. Is he just telling you what happened, or is he trying to convince you that something is true? What words signal his intent?",
        "fur": "Good. Now, could Holt's statement be rephrased as an explanation instead? What would change if the audience already accepted that the land was Elda's?",
        "npc": "Magistrate Holt is methodical and dry, referencing documents and precedent. He speaks in measured tones.",
        "seed": "The court is now in session. I have reviewed the charter and the survey maps. Let me explain my ruling.",
        "res": "If the player correctly identifies the argument structure, Holt nods approvingly and invites them to serve as a court analyst, unlocking the courthouse archives.",
        "src": "PHIL 201 lecture notes 1.2 — premise/conclusion indicators"
    },
    # 2
    {
        "ctx": "At the Hearthstone Tavern, a bard named Lyssa is trying to convince the innkeeper to let her perform for free lodging.",
        "text": "Lyssa says: 'You should let me play tonight because a good bard draws customers, and more customers means more ale sold. So you will actually profit from giving me a room.'",
        "spk": "Lyssa, a travelling bard who is persuasive and quick-witted.",
        "pname": "Argument with 'because' and 'so' indicators",
        "pdesc": "Lyssa offers reasons (bards draw customers, more customers means more ale) leading to a conclusion (the innkeeper profits). 'Because' and 'so' are the indicator words.",
        "formal": "P1 because P2, and P3. So C.",
        "why_right": "Lyssa is not merely describing a situation — she is offering reasons to convince the innkeeper that a specific claim is true. The premise indicators 'because' and the conclusion indicator 'so' confirm this is an argument.",
        "related": ["A1.2", "A1.6"],
        "counter": "If Lyssa had said 'I played last night because the innkeeper asked me to,' that would be an explanation of why she played, not an argument that she should play.",
        "prompt": "Lyssa is making her pitch to the innkeeper. Is she presenting an argument, giving an explanation, or just making a request? How can you tell?",
        "rubric": [
            "Player sees this as a simple request with no reasoning.",
            "Player recognizes Lyssa is being persuasive but cannot distinguish argument from mere rhetoric.",
            "Player identifies that Lyssa gives reasons but does not pinpoint the indicator words.",
            "Player identifies this as an argument, noting 'because' introduces premises and 'so' introduces the conclusion.",
            "Player identifies the argument and indicators, and can explain why this differs from an explanation (Lyssa is trying to establish a claim the innkeeper has not yet accepted)."
        ],
        "fuw": "What is Lyssa trying to get the innkeeper to believe? And what reasons does she give for believing it?",
        "fur": "Nice. Now suppose Lyssa said exactly the same words after the innkeeper already agreed. Would it still be an argument, or would it become something else?",
        "npc": "Lyssa is charming, quick with words, and uses reasoning as a tool of persuasion.",
        "seed": "Come now, innkeep. Hear me out — I have a proposition that benefits us both.",
        "res": "If the player identifies the argument, Lyssa winks and offers to teach the player about persuasion techniques, opening a dialogue tree on argument identification.",
        "src": "PHIL 201 lecture notes 1.2 — premise/conclusion indicators"
    },
    # 3
    {
        "ctx": "In the village square of Thornwall, a merchant is loudly complaining about the new bridge toll.",
        "text": "Merchant Doss shouts: 'This bridge toll is outrageous! I have to cross it four times a day. That is sixteen silver a day just to move my goods. It will bankrupt small traders like me within a month.'",
        "spk": "Merchant Doss, a vocal small trader who sells pottery at the market.",
        "pname": "Complaint without argument structure",
        "pdesc": "Doss expresses frustration and describes his situation (four crossings, sixteen silver, bankruptcy risk), but he does not present premises intended to prove a conclusion. He is venting, not arguing.",
        "formal": "No argument structure — this is a description combined with an emotional expression.",
        "why_right": "Although Doss's words sound persuasive, he is describing his circumstances and expressing frustration rather than offering premises to support a conclusion. There is no explicit 'therefore' move — no claim that something follows from something else.",
        "related": ["A1.6", "A1.5"],
        "counter": "One could reconstruct an implicit argument ('The toll should be lowered because it bankrupts small traders'), but as stated, Doss is complaining, not arguing. The principle of charity might lead us to find an argument, but the skill here is recognizing what is and is not explicitly present.",
        "prompt": "Doss is clearly upset. But is he actually making an argument? Or is he doing something else?",
        "rubric": [
            "Player assumes any passionate speech is an argument.",
            "Player senses Doss might not be arguing but cannot explain why.",
            "Player recognizes Doss is describing and complaining but conflates this with giving an explanation.",
            "Player correctly identifies this as a complaint/description, not an argument, noting the absence of premise-conclusion structure.",
            "Player identifies the non-argument status, explains what would need to change to make it an argument, and notes that one could charitably reconstruct an implicit argument."
        ],
        "fuw": "Ask yourself: is Doss trying to prove that something is true? Or is he telling you about his situation and how he feels about it? What would he need to add to turn this into an argument?",
        "fur": "Exactly right. Now, if Doss added 'therefore the council should repeal the toll,' would that change things? What would the premises be?",
        "npc": "Merchant Doss is loud, emotional, and prone to complaining. He speaks in exclamations.",
        "seed": "Sixteen silver! Sixteen! And they call this progress!",
        "res": "If the player correctly identifies the non-argument, a nearby scholar NPC compliments their perceptiveness and offers a follow-up challenge.",
        "src": "PHIL 201 lecture notes 1.1-1.2 — distinguishing arguments"
    },
    # 4
    {
        "ctx": "The player visits the Alchemist's Guild where Master Venn is explaining why a potion failed.",
        "text": "Master Venn says: 'The potion turned green because the nightshade was added before the mixture cooled. When nightshade contacts a hot solution, it releases chlorophyllic acid, which reacts with the silver catalyst to produce the green precipitate.'",
        "spk": "Master Venn, a meticulous alchemist who teaches by explaining mechanisms.",
        "pname": "Explanation, not argument",
        "pdesc": "Venn is explaining why the potion turned green — a fact both he and the player can observe. He is not trying to prove that the potion is green; he is showing why it is green. The word 'because' here introduces a causal explanation, not a premise.",
        "formal": "X happened because Y caused Z, which caused X. (Causal explanation, not argument.)",
        "why_right": "The truth of the conclusion (the potion turned green) is already established by observation. Venn is providing a causal account, not trying to convince anyone of a disputed claim. This makes it an explanation, not an argument.",
        "related": ["A1.6", "A1.1"],
        "counter": "If someone doubted the potion was green and Venn said 'The potion must be green because nightshade in hot solution always produces green precipitate,' that would be an argument — the conclusion would be in dispute and the premises would support it.",
        "prompt": "Master Venn uses the word 'because.' Does that mean he is giving an argument? What is he actually doing here?",
        "rubric": [
            "Player assumes 'because' always signals an argument.",
            "Player is unsure but guesses it might be an explanation.",
            "Player identifies this as an explanation but cannot articulate the difference from an argument.",
            "Player correctly distinguishes explanation from argument: the conclusion is already accepted, and Venn is showing why it is true, not that it is true.",
            "Player makes the distinction, explains the role of 'because' in both contexts, and can describe what would need to change to turn this explanation into an argument."
        ],
        "fuw": "Is Venn trying to convince you that the potion is green? Or does everyone already know it is green, and he is telling you why?",
        "fur": "Exactly. The key test: is the 'because' answering 'why should I believe this?' (argument) or 'why did this happen?' (explanation). Can you think of a case where it is genuinely ambiguous?",
        "npc": "Master Venn is patient, methodical, and loves explaining mechanisms. He speaks in precise cause-effect chains.",
        "seed": "Ah, you see the green color? Let me show you exactly what went wrong in the process.",
        "res": "The player gains Venn's trust and is allowed to assist with the next brew, leading to a practical chemistry puzzle.",
        "src": "PHIL 201 lecture notes 1.3 — arguments vs explanations"
    },
    # 5
    {
        "ctx": "At the Windmere garrison, Captain Brenn is issuing orders to the patrol.",
        "text": "Captain Brenn barks: 'Secure the north gate. Post two sentries at the bridge. No one crosses after sundown without a pass signed by me.'",
        "spk": "Captain Brenn, a no-nonsense military officer.",
        "pname": "Commands, not an argument",
        "pdesc": "Brenn is issuing orders — imperative sentences that cannot be true or false. There are no premises or conclusions because commands are not statements.",
        "formal": "No argument structure — imperatives do not have truth values.",
        "why_right": "Arguments consist of statements that can be true or false. Commands tell people what to do but do not assert anything that could serve as a premise or conclusion. Brenn is directing action, not supporting a claim.",
        "related": ["A1.1", "A1.6"],
        "counter": "If Brenn had said 'We should secure the north gate because enemy scouts were spotted nearby,' that would be an argument — it includes a reason (premise) supporting a claim (conclusion).",
        "prompt": "Captain Brenn sounds authoritative and confident. Is he making an argument?",
        "rubric": [
            "Player confuses authoritative speech with argumentation.",
            "Player suspects it is not an argument but cannot say why.",
            "Player notes these are orders but does not connect this to the definition of argument.",
            "Player identifies that commands are not statements and therefore cannot form premises or conclusions — so this is not an argument.",
            "Player identifies the non-argument, explains that arguments require statements with truth values, and shows what Brenn would need to add to make an argument."
        ],
        "fuw": "Can you say that 'Secure the north gate' is true or false? If not, can it be a premise or a conclusion?",
        "fur": "Right. Commands lack truth values. But what about 'You should secure the north gate' — is that a statement? Could it be part of an argument?",
        "npc": "Captain Brenn is curt, efficient, and speaks only in directives.",
        "seed": "Listen up! I will say this once. Follow these orders exactly.",
        "res": "If the player correctly identifies the non-argument, Brenn is impressed by their analytical mind and assigns them an intelligence-gathering task.",
        "src": "PHIL 201 lecture notes 1.1 — statements vs non-statements"
    },
    # 6
    {
        "ctx": "Two scholars are debating at the Arcanum Library. Scholar Fenn claims that ancient elves built the ruins.",
        "text": "Scholar Fenn states: 'The ruins must have been built by ancient elves. The stonework uses dovetail joints, which only elven masons practiced. Moreover, the inscriptions on the lintel are in Old Elvish script. Hence, no other civilization could have constructed them.'",
        "spk": "Scholar Fenn, a confident archaeologist who presents evidence systematically.",
        "pname": "Argument with multiple premises and conclusion indicator 'hence'",
        "pdesc": "Fenn offers two independent premises (dovetail joints unique to elves, Old Elvish inscriptions) and draws a conclusion using 'hence.' This is a clear argument with a disputed conclusion supported by evidence.",
        "formal": "P1 (dovetail joints → elven masons), P2 (Old Elvish inscriptions). Hence, C (elves built the ruins).",
        "why_right": "Fenn is trying to establish a claim (the ruins were elven-built) that is in dispute. He provides reasons and signals the conclusion with 'hence.' The premises are intended to make the conclusion more credible.",
        "related": ["A1.2", "A1.7"],
        "counter": "One could question whether the premises are true (maybe other civilizations also used dovetail joints), but the structure is clearly argumentative.",
        "prompt": "Scholar Fenn sounds very sure of himself. Is he making an argument, and if so, what are the key parts?",
        "rubric": [
            "Player cannot distinguish Fenn's speech from a description.",
            "Player recognizes Fenn is trying to prove something but cannot identify the parts.",
            "Player identifies the conclusion but not the premises or the indicator word.",
            "Player identifies both premises, the conclusion, and notes 'hence' as a conclusion indicator.",
            "Player does all of the above and notes this is an argument (not an explanation) because the claim is in dispute, and evaluates whether the premises actually support the conclusion."
        ],
        "fuw": "What is Fenn trying to convince his colleague of? And what evidence does he offer? Look for the word that signals his final claim.",
        "fur": "Now consider: if everyone already agreed the elves built the ruins, and Fenn said the same words, would it still be an argument or would it become an explanation?",
        "npc": "Scholar Fenn is confident, occasionally arrogant, and backs claims with archaeological evidence.",
        "seed": "The evidence is quite clear if you know what to look for. Allow me to present my findings.",
        "res": "The player can challenge Fenn's premises, leading to a deeper archaeology quest to verify the claims.",
        "src": "PHIL 201 lecture notes 1.2 — identifying arguments"
    },
    # 7
    {
        "ctx": "At the Saltmere docks, a sailor describes a storm to a group of listeners.",
        "text": "Sailor Keel says: 'The sky turned black around noon. Then the wind picked up from the southeast. The waves crested at twenty feet. We lost the mast and barely made it to harbor.'",
        "spk": "Sailor Keel, a weathered mariner who tells stories at the docks.",
        "pname": "Narrative description, not argument",
        "pdesc": "Keel is recounting events in chronological order. He is not trying to prove a conclusion — he is describing what happened. There are no premise or conclusion indicators, and no claim is being supported by reasons.",
        "formal": "No argument structure — this is a chronological narrative.",
        "why_right": "A narrative describes a sequence of events. An argument offers reasons for a claim. Keel is telling a story, not trying to convince anyone that something is true on the basis of evidence.",
        "related": ["A1.1", "A1.6"],
        "counter": "If Keel had said 'We should avoid the southeast passage because the last storm came from that direction and destroyed our mast,' that would be an argument.",
        "prompt": "Keel is telling you about the storm. Is he making an argument, or is he doing something else?",
        "rubric": [
            "Player treats any informative speech as an argument.",
            "Player senses it is not an argument but cannot say why.",
            "Player recognizes it is a story or description but cannot articulate the structural difference from an argument.",
            "Player identifies this as a narrative, noting the absence of any claim supported by reasons.",
            "Player identifies the narrative structure, explains that arguments require premises supporting a conclusion, and suggests what Keel would need to add to make an argument."
        ],
        "fuw": "Is Keel trying to prove something to you, or is he telling you what happened? What would need to change for this to be an argument?",
        "fur": "Good. Narratives can contain implicit arguments. If Keel had concluded 'so the southeast passage is too dangerous,' would the preceding description function as premises?",
        "npc": "Sailor Keel is grizzled, dramatic, and loves a good story.",
        "seed": "Gather round. Let me tell you about the storm that nearly took the Windcatcher.",
        "res": "The player's perceptiveness earns Keel's respect, and he shares navigational knowledge useful for a later quest.",
        "src": "PHIL 201 lecture notes 1.1 — what is an argument"
    },
    # 8
    {
        "ctx": "At the Thornwall Council, Elder Mira is addressing the assembly about whether to accept refugees from the neighboring village.",
        "text": "Elder Mira speaks: 'We have enough grain stores to last through winter even with fifty additional mouths to feed. The empty cottages on the east hill can house them. Therefore, we can accept the Ashgrove refugees without endangering our own people.'",
        "spk": "Elder Mira, a pragmatic village leader who argues from resources and logistics.",
        "pname": "Argument with factual premises and 'therefore' conclusion",
        "pdesc": "Mira presents two factual premises (sufficient grain, available housing) and draws a practical conclusion using 'therefore.' She is trying to convince the council that accepting refugees is feasible.",
        "formal": "P1 (sufficient grain), P2 (available housing). Therefore, C (we can accept refugees safely).",
        "why_right": "The conclusion is in dispute (the council has not yet agreed). Mira offers factual premises as reasons to accept her conclusion. The word 'therefore' explicitly marks the conclusion.",
        "related": ["A1.2", "A1.5"],
        "counter": "Someone could challenge whether the premises are true (are the grain stores really sufficient?) or whether they are sufficient for the conclusion (what about other resources?), but the argument structure is clear.",
        "prompt": "Elder Mira is addressing the council. Is she making an argument? If so, what is she trying to establish and what reasons does she give?",
        "rubric": [
            "Player cannot tell whether Mira is arguing or merely reporting.",
            "Player recognizes persuasive intent but cannot identify the structure.",
            "Player identifies the conclusion but not both premises.",
            "Player identifies both premises, the conclusion, and the indicator word 'therefore.'",
            "Player does all of the above and notes that this is an argument because the conclusion is in dispute, and considers whether the premises are sufficient."
        ],
        "fuw": "What does Mira want the council to believe? And what facts does she point to as reasons for believing it?",
        "fur": "Can you think of a premise Mira might be leaving unstated? For example, is she assuming anything about the refugees' willingness to stay in those cottages?",
        "npc": "Elder Mira is calm, data-driven, and speaks in terms of resources and logistics.",
        "seed": "Let us set emotion aside and look at what we actually have. The numbers speak clearly.",
        "res": "If the player identifies the argument, Mira asks them to help identify potential objections before the vote.",
        "src": "PHIL 201 lecture notes 1.2 — premise/conclusion indicators"
    },
    # 9
    {
        "ctx": "A street preacher is haranguing passersby outside the Temple of the Twin Moons.",
        "text": "The preacher cries: 'Repent! The end times are upon us! The Twin Moons have aligned, just as the prophecy foretold. Turn from your wicked ways before it is too late!'",
        "spk": "An unnamed street preacher, fervent and dramatic.",
        "pname": "Mixed: commands and assertions, but no clear argument",
        "pdesc": "The preacher makes some assertions (the moons aligned, the prophecy predicted this) and issues commands (repent, turn from wickedness). However, the assertions do not clearly function as premises supporting a conclusion. The commands cannot be true or false. This is primarily exhortation, not argument.",
        "formal": "No clear argument structure — a mix of assertions and imperatives without explicit premise-conclusion reasoning.",
        "why_right": "While some factual claims are embedded ('the moons aligned'), they are not structured as premises leading to a conclusion. The overall speech is a call to action, not an attempt to prove a claim through reasoning.",
        "related": ["A1.1", "A1.5"],
        "counter": "One could charitably reconstruct an implicit argument: 'The prophecy said that when the moons align, the end times begin. The moons have aligned. Therefore the end times have begun. Therefore you should repent.' But as stated, the preacher is exhorting, not arguing.",
        "prompt": "The preacher is intense and seems to believe strongly. But is he actually making an argument? What is he doing instead?",
        "rubric": [
            "Player assumes passion equals argument.",
            "Player senses something is off but cannot say what.",
            "Player notes the commands but does not fully analyze the structure.",
            "Player identifies that this is primarily exhortation — commands mixed with assertions but no clear premise-conclusion structure.",
            "Player identifies the non-argument, reconstructs the implicit argument that could underlie it, and explains the difference between exhortation and argument."
        ],
        "fuw": "Try to find the 'therefore' — where does the preacher draw a conclusion from premises? Or is he just telling people what to do?",
        "fur": "Now, could you reconstruct an argument from what the preacher said? What would the premises and conclusion be? That is the principle of charity at work.",
        "npc": "The preacher is wild-eyed, passionate, and speaks in exclamations and commands.",
        "seed": "Hear me, citizens! The signs are upon us! Will you heed the warning or perish in ignorance?",
        "res": "If the player identifies the non-argument, a temple scholar nearby engages them in a discussion about the difference between argument and persuasion.",
        "src": "PHIL 201 lecture notes 1.1-1.2 — statements and non-statements"
    },
    # 10
    {
        "ctx": "In the Mage's Academy, Instructor Selene is addressing a class about a disputed magical theory.",
        "text": "Instructor Selene says: 'Given that fire spells consume ambient mana at twice the rate of ice spells, and given that the Northreach Caverns have dangerously low ambient mana, it follows that casting fire spells in those caverns risks a mana collapse.'",
        "spk": "Instructor Selene, a careful magical theorist who always marks her reasoning explicitly.",
        "pname": "Argument with 'given that' and 'it follows that' indicators",
        "pdesc": "Selene uses 'given that' to introduce two premises and 'it follows that' to mark her conclusion. This is a textbook-clear argument structure.",
        "formal": "Given that P1 and given that P2, it follows that C.",
        "why_right": "Selene explicitly marks her premises with 'given that' and her conclusion with 'it follows that.' She is providing reasons for a claim that is not yet accepted by the students.",
        "related": ["A1.2", "A1.3"],
        "counter": "The indicator phrases here are maximally explicit, but many real arguments lack such clear markers.",
        "prompt": "Instructor Selene is teaching about mana theory. Is she making an argument, and how can you tell?",
        "rubric": [
            "Player cannot identify whether this is an argument.",
            "Player senses reasoning but cannot identify the parts.",
            "Player identifies the conclusion but not the indicator phrases.",
            "Player identifies both premises (marked by 'given that') and the conclusion (marked by 'it follows that').",
            "Player identifies the full structure, recognizes the explicit indicators, and notes that this is an unusually clearly marked argument."
        ],
        "fuw": "Look for phrases that signal 'here is my evidence' and 'here is what I conclude.' Selene uses very formal language — what phrases stand out?",
        "fur": "This argument is unusually well-marked. In everyday speech, people rarely say 'given that' and 'it follows that.' What other words could serve the same function?",
        "npc": "Instructor Selene is precise, formal, and always structures her claims clearly.",
        "seed": "Pay attention, students. I will state my reasoning step by step so you can evaluate each part.",
        "res": "The player's correct identification leads Selene to pose a harder challenge: an argument with ambiguous indicators.",
        "src": "PHIL 201 lecture notes 1.2 — premise/conclusion indicators"
    },
    # 11
    {
        "ctx": "At the Crossroads Inn, two traders are discussing whether the mountain pass is safe.",
        "text": "Trader Hask says: 'I saw fresh rockslide debris on the pass yesterday. The miners at Coppervein said they felt tremors all week. You would be a fool to take that route.'",
        "spk": "Trader Hask, a cautious merchant who has traveled the mountain routes for years.",
        "pname": "Implicit argument with evaluative conclusion",
        "pdesc": "Hask provides evidence (rockslide debris, tremors) leading to an evaluative conclusion ('you would be a fool to take that route'). While 'fool' is evaluative rather than propositional, the underlying claim is 'the pass is dangerous.' There are no explicit indicator words, but the reasoning structure is present.",
        "formal": "P1 (fresh rockslide debris), P2 (ongoing tremors). [Implicit C: the pass is dangerous.]",
        "why_right": "Despite lacking explicit indicator words, Hask is providing reasons (evidence of instability) to support a claim (the route is unsafe). The evaluative language wraps an argument in a warning.",
        "related": ["A1.5", "A1.2"],
        "counter": "The evaluative language ('fool') might make this seem like an insult rather than an argument, but the core structure is argumentative — evidence is offered in support of a conclusion.",
        "prompt": "Hask seems to be warning you, maybe even insulting you. But is there an argument buried in what he said?",
        "rubric": [
            "Player sees only an insult or warning, no argument.",
            "Player senses reasoning but is confused by the evaluative language.",
            "Player identifies the evidence but not the implicit conclusion.",
            "Player identifies the premises (debris, tremors) and the implicit conclusion (the pass is dangerous), noting the lack of explicit indicators.",
            "Player does all of the above and distinguishes the evaluative wrapping ('fool') from the argumentative core, explaining how evaluative language can obscure argument structure."
        ],
        "fuw": "Ignore the word 'fool' for a moment. What facts does Hask mention? And what do those facts suggest about the pass?",
        "fur": "Nice. Arguments do not always come with 'therefore' and 'because.' How do you identify an argument when the indicator words are missing?",
        "npc": "Hask is blunt, experienced, and does not sugarcoat his assessments.",
        "seed": "I have been running these routes for twenty years. Listen to what I am telling you.",
        "res": "If the player identifies the argument, Hask shares detailed route knowledge, including a safer alternative path.",
        "src": "PHIL 201 lecture notes 1.2 — identifying arguments without explicit indicators"
    },
    # 12
    {
        "ctx": "At a blacksmith's forge, Apprentice Cort is telling the player about his day.",
        "text": "Cort says: 'First I stoked the forge, then I hammered out the horseshoes, and after that I tempered them in the water barrel. Master Grenn inspected them and said they were acceptable.'",
        "spk": "Apprentice Cort, a young blacksmith who recounts his day dutifully.",
        "pname": "Chronological narrative, not argument",
        "pdesc": "Cort is reporting a sequence of events in the order they happened. No claim is being supported by reasons — this is purely descriptive.",
        "formal": "No argument structure — chronological description of events.",
        "why_right": "Cort is not trying to prove anything. He is telling you what happened in sequence. There is no disputed conclusion and no premises offered in support of one.",
        "related": ["A1.1", "A1.6"],
        "counter": "Words like 'then' and 'after that' indicate temporal order, not logical support. Compare with 'The horseshoes are well-made because I followed the proper steps' — that would be an argument.",
        "prompt": "Cort just told you about his day. Did he make an argument at any point?",
        "rubric": [
            "Player treats the report as an argument.",
            "Player is unsure whether a sequence of events counts as an argument.",
            "Player correctly says no argument but cannot explain why.",
            "Player identifies this as a chronological narrative and explains that no claim is being supported by reasons.",
            "Player makes the distinction clearly and explains that temporal connectors ('then,' 'after that') differ from logical connectors ('therefore,' 'because')."
        ],
        "fuw": "Is Cort trying to convince you that something is true? Or is he just telling you the order of events?",
        "fur": "Right. Now, what if Cort had added 'so I must be improving as a smith'? Would that change things?",
        "npc": "Cort is earnest, young, and eager to share his progress.",
        "seed": "It was a busy day at the forge! Let me tell you what happened.",
        "res": "The player's analysis impresses Master Grenn, who offers a side-quest involving logical reasoning about metallurgy.",
        "src": "PHIL 201 lecture notes 1.1 — what is an argument"
    },
    # 13
    {
        "ctx": "The player overhears a heated argument at the Merchants' Guild about whether to raise tariffs on imported silk.",
        "text": "Guildmaster Torr says: 'Obviously, we must raise the silk tariff. It is well known that foreign silk undercuts our local weavers.'",
        "spk": "Guildmaster Torr, a powerful merchant who uses rhetorical assurances to cut arguments short.",
        "pname": "Argument with assuring language",
        "pdesc": "Torr presents a brief argument (foreign silk undercuts weavers, therefore raise tariffs) but wraps it in assuring language ('obviously,' 'it is well known'). The assuring terms substitute for actual evidence.",
        "formal": "P1 [assured, not supported] (foreign silk undercuts local weavers). Therefore C (raise tariffs).",
        "why_right": "There is an argument here — a premise and a conclusion. But the assuring language ('obviously,' 'it is well known') is doing rhetorical work that substitutes for evidence. The player should notice both the argument and the rhetorical shortcut.",
        "related": ["A1.5", "A1.1"],
        "counter": "Assuring language is not always fallacious — sometimes claims really are well known. But using assuring terms to skip over the need for evidence is a rhetorical device that weakens the argument.",
        "prompt": "Guildmaster Torr sounds very confident. Is he making an argument? And is there anything worth noticing about how he presents it?",
        "rubric": [
            "Player takes Torr's confidence at face value and does not analyze the structure.",
            "Player recognizes an argument but does not notice the assuring language.",
            "Player notices the assuring language but does not identify the underlying argument.",
            "Player identifies both the argument (premise about foreign silk, conclusion about tariffs) and the rhetorical assurances ('obviously,' 'it is well known').",
            "Player identifies the argument structure, the assuring language, explains how assurances substitute for evidence, and notes the missing premise connecting undercutting to the need for tariffs."
        ],
        "fuw": "What is Torr's conclusion? What reason does he give? And do the words 'obviously' and 'it is well known' actually provide evidence, or do they do something else?",
        "fur": "Good eye. Bert's teaching notes mention assuring, guarding, and discounting as rhetorical devices. Can you think of a case where 'it is well known that' is legitimate?",
        "npc": "Guildmaster Torr is authoritative, impatient, and uses rhetorical shortcuts to steamroll opposition.",
        "seed": "I should not have to explain this to you. The facts speak for themselves.",
        "res": "If the player identifies the assuring language, a junior guild member whispers thanks and asks for help analyzing the Guildmaster's other claims.",
        "src": "PHIL 201 lecture notes 1.10 — assuring, guarding, discounting"
    },
    # 14
    {
        "ctx": "At a farm outside Millhaven, Farmer Gedda is talking about her crops.",
        "text": "Gedda says: 'I wish the rain would come. My barley is wilting and the well is running low. If we do not get rain by next week, I will lose the entire harvest.'",
        "spk": "Farmer Gedda, a worried farmer expressing her concerns about drought.",
        "pname": "Conditional prediction, not argument",
        "pdesc": "Gedda expresses a wish, describes her situation, and makes a conditional prediction. She is not offering reasons to support a conclusion — she is expressing worry and describing circumstances.",
        "formal": "No argument structure — wish + description + conditional prediction.",
        "why_right": "While Gedda makes claims that could serve as premises in an argument, she does not draw a conclusion from them. The conditional ('if no rain, then I lose the harvest') is a prediction, not a conclusion supported by premises.",
        "related": ["A1.1", "A1.6"],
        "counter": "If Gedda had said 'Therefore the council should release the emergency water reserves,' she would have completed an argument. As it stands, she is describing and predicting, not arguing.",
        "prompt": "Gedda is clearly worried. Is she making an argument about anything?",
        "rubric": [
            "Player treats the conditional as an argument.",
            "Player is unsure whether predictions count as arguments.",
            "Player correctly says this is not an argument but struggles to explain why.",
            "Player identifies that Gedda is describing, wishing, and predicting — not offering premises in support of a disputed conclusion.",
            "Player makes the distinction and explains what Gedda would need to add to convert this into an argument."
        ],
        "fuw": "What is Gedda trying to convince you of? Or is she just telling you about her situation?",
        "fur": "Exactly. Now, could you reconstruct an argument from Gedda's concerns? What conclusion might she be implicitly driving toward?",
        "npc": "Gedda is weary, practical, and speaks plainly about her problems.",
        "seed": "It has not rained in three weeks. I do not know what we will do.",
        "res": "If the player identifies the non-argument, Gedda's neighbor provides a follow-up where they do make an explicit argument about water policy.",
        "src": "PHIL 201 lecture notes 1.1 — distinguishing arguments from other speech acts"
    },
    # 15
    {
        "ctx": "In the Scholars' Quarter, Professor Aldric is debating a colleague about whether dragons are warm-blooded.",
        "text": "Professor Aldric says: 'Dragons must be warm-blooded, for they maintain constant body temperature in all climates. Furthermore, their metabolic rate during flight requires endothermic physiology. No cold-blooded creature could sustain the energy output we observe in dragon flight.'",
        "spk": "Professor Aldric, a natural philosopher who builds arguments with multiple independent lines of evidence.",
        "pname": "Argument with 'for' and 'furthermore' as indicators",
        "pdesc": "Aldric uses 'for' as a premise indicator and 'furthermore' to add a second line of evidence. His conclusion ('dragons must be warm-blooded') is stated first, followed by supporting reasons. This is a classic argument with the conclusion at the beginning.",
        "formal": "C (dragons are warm-blooded), for P1 (constant body temperature), furthermore P2 (metabolic rate requires endothermic physiology), P3 (cold-blooded creatures cannot sustain observed energy output).",
        "why_right": "Aldric is trying to establish a disputed claim by providing multiple lines of evidence. The conclusion comes first (signaled by 'must be'), and the premises follow (signaled by 'for' and 'furthermore').",
        "related": ["A1.2", "A1.7"],
        "counter": "'For' can be ambiguous — it sometimes means 'because' (premise indicator) and sometimes means 'in order to' (purpose). Here the substitution test confirms: 'because they maintain constant body temperature' works perfectly.",
        "prompt": "Professor Aldric states his claim and then provides several points. Is this an argument? If so, where does the conclusion appear?",
        "rubric": [
            "Player cannot identify whether this is an argument.",
            "Player recognizes reasoning but places the conclusion at the end.",
            "Player identifies the conclusion and some premises but misses the indicator words.",
            "Player identifies the conclusion at the beginning, the premises marked by 'for' and 'furthermore,' and the overall argument structure.",
            "Player does all of the above, notes that conclusions can appear at the beginning of an argument, and applies the substitution test to confirm 'for' is a premise indicator."
        ],
        "fuw": "The conclusion does not always come last. What claim is Aldric trying to prove? And what evidence does he offer for it?",
        "fur": "Great. You noticed the conclusion comes first. Why might a speaker choose to state the conclusion before the premises? Does it change the argument's strength?",
        "npc": "Professor Aldric is erudite, enthusiastic, and builds cases methodically.",
        "seed": "The evidence on dragon physiology is quite compelling. Let me walk you through it.",
        "res": "If the player identifies the argument structure, Aldric invites them to evaluate a more ambiguous case involving wyvern taxonomy.",
        "src": "PHIL 201 lecture notes 1.2 — premise/conclusion indicators"
    },
    # 16
    {
        "ctx": "At the Stonehearth Mining Company office, the foreman is speaking to a group of miners.",
        "text": "Foreman Dunn says: 'Shaft seven collapsed last month. The tunnels in that section were not properly reinforced. The geological survey warned us about unstable shale. So we should not reopen shaft seven until the engineers certify it is safe.'",
        "spk": "Foreman Dunn, a practical mine boss who cites evidence and draws conclusions about safety.",
        "pname": "Argument with factual premises and 'so' conclusion indicator",
        "pdesc": "Dunn provides three factual premises (collapse, inadequate reinforcement, geological warning) and concludes with a practical recommendation marked by 'so.' This is an argument from evidence to a policy conclusion.",
        "formal": "P1 (shaft collapsed), P2 (not reinforced), P3 (survey warned of unstable shale). So C (do not reopen until certified safe).",
        "why_right": "Dunn is trying to convince the miners that reopening the shaft is unsafe. He offers specific evidence and draws a practical conclusion using 'so.'",
        "related": ["A1.2", "A1.5"],
        "counter": "The conclusion is a recommendation (normative), while the premises are factual (descriptive). There may be a missing premise connecting safety facts to the recommendation.",
        "prompt": "Foreman Dunn is addressing the miners. Is he making an argument? What is his conclusion and what supports it?",
        "rubric": [
            "Player treats this as a simple report about the mine.",
            "Player recognizes Dunn is making a recommendation but does not see the argument structure.",
            "Player identifies the conclusion but not all the premises.",
            "Player identifies the three premises, the conclusion marked by 'so,' and the argumentative structure.",
            "Player identifies the full structure and notices the descriptive-to-normative move (facts to a recommendation), suggesting a missing premise."
        ],
        "fuw": "What does Dunn want the miners to do (or not do)? And what facts does he cite to support that position?",
        "fur": "Notice that Dunn moves from descriptive facts to a normative recommendation. What assumption bridges that gap?",
        "npc": "Foreman Dunn is gruff, safety-conscious, and speaks from experience.",
        "seed": "Listen up. I have something important to say about shaft seven.",
        "res": "The player's analysis leads to a safety investigation quest where they must evaluate arguments about which shafts are safe to mine.",
        "src": "PHIL 201 lecture notes 1.2, 1.9 — indicators and the is-ought gap"
    },
    # 17
    {
        "ctx": "In the village square, a traveling fortune teller is speaking to a small crowd.",
        "text": "The fortune teller announces: 'Mercury is in retrograde. Beware of signing contracts this week. Your past will come back to haunt you. Cross my palm with silver for a full reading.'",
        "spk": "A traveling fortune teller who mixes assertions with warnings and sales pitches.",
        "pname": "Assertions and directives, no argument",
        "pdesc": "The fortune teller makes an astronomical claim, issues warnings, makes a vague prediction, and solicits business. None of these are structured as premises supporting a conclusion. There is no 'because' or 'therefore' connecting claims to a supported conclusion.",
        "formal": "No argument structure — a series of disconnected assertions, warnings, and a directive.",
        "why_right": "For a speech to be an argument, there must be statements offered as reasons for a conclusion. The fortune teller is making claims and commands but not connecting them in a premise-conclusion structure.",
        "related": ["A1.1", "A1.6"],
        "counter": "One could reconstruct an argument: 'Mercury is in retrograde, and retrograde causes bad luck with contracts, so do not sign contracts.' But the fortune teller does not make the connecting premise explicit, and the overall speech functions more as mystification and salesmanship than argument.",
        "prompt": "The fortune teller is making several claims. Is she presenting an argument?",
        "rubric": [
            "Player treats all claims as part of an argument.",
            "Player senses the lack of logical structure but cannot explain it.",
            "Player notes the absence of indicator words but does not fully analyze.",
            "Player identifies that no claim is offered as a reason for any other claim — these are disconnected assertions and directives.",
            "Player identifies the non-argument status, could reconstruct an implicit argument, and explains what premise would be needed to connect the claims."
        ],
        "fuw": "For an argument, one statement needs to support another. Is the fortune teller giving you a reason to believe any of her claims based on any of her other claims?",
        "fur": "Good. Could you charitably reconstruct an argument from this? What would the missing premise be?",
        "npc": "The fortune teller is theatrical, mysterious, and uses vague language deliberately.",
        "seed": "The stars have much to tell you, traveler. But not for free.",
        "res": "If the player identifies the non-argument, a skeptical bystander offers a side conversation about distinguishing reasoning from rhetoric.",
        "src": "PHIL 201 lecture notes 1.1-1.2"
    },
    # 18
    {
        "ctx": "At the Archer's Guild, Master Fletcher is explaining why a particular bow design is superior.",
        "text": "Master Fletcher says: 'The recurve design is the best for mounted archery. This is because the shorter limbs clear the horse's neck, and the recurve shape stores more energy per inch of draw than a longbow. Consequently, you get more power from a compact frame.'",
        "spk": "Master Fletcher, a bow craftsman who argues from engineering principles.",
        "pname": "Argument with 'this is because' and 'consequently'",
        "pdesc": "Fletcher states a conclusion first (recurve is best for mounted archery), then provides premises marked by 'this is because,' and draws an intermediate conclusion using 'consequently.' This is a multi-step argument.",
        "formal": "C (recurve best for mounted archery) because P1 (shorter limbs clear horse) and P2 (recurve stores more energy). Consequently, IC (more power from compact frame).",
        "why_right": "Fletcher is making a disputed claim (the superiority of recurve design) and supporting it with engineering reasons. The indicator phrases are clear.",
        "related": ["A1.2", "A1.7"],
        "counter": "This could also be interpreted as an explanation if the superiority of recurve bows were already accepted. Context matters: Fletcher is teaching, so he is more likely arguing for a conclusion the student does not yet accept.",
        "prompt": "Master Fletcher is making a claim about bow design. Is this an argument or an explanation? What tells you which one?",
        "rubric": [
            "Player cannot distinguish argument from explanation.",
            "Player recognizes reasoning but classifies it incorrectly.",
            "Player identifies it as one or the other but cannot explain the criterion.",
            "Player identifies this as an argument (the superiority claim is being established, not explained) and finds the indicator phrases.",
            "Player identifies the argument, discusses the argument/explanation ambiguity (noting that context matters), and identifies the multi-step structure."
        ],
        "fuw": "Is Master Fletcher trying to convince you that the recurve is superior, or does everyone already agree it is and he is telling you why?",
        "fur": "Good. In teaching contexts, the line between argument and explanation can blur. The teacher may be arguing for a conclusion the student does not yet hold. How would you tell the difference?",
        "npc": "Master Fletcher is precise, patient, and speaks like an engineer.",
        "seed": "Let me show you why the recurve is the weapon of choice for cavalry. It is not just tradition — there is solid reasoning.",
        "res": "The player's analysis leads to a bow-testing challenge where they must evaluate competing design arguments.",
        "src": "PHIL 201 lecture notes 1.2-1.3"
    },
    # 19
    {
        "ctx": "At the Harbor Guild, a dock worker is complaining to a colleague.",
        "text": "Dock worker Joss says: 'The new crane is terrible. It is too slow, the gears jam constantly, and it makes a horrible grinding noise. I hate working with it.'",
        "spk": "Joss, a dock worker who complains frequently.",
        "pname": "Report with evaluation but no argument",
        "pdesc": "Joss evaluates the crane negatively and lists complaints, but he is not trying to prove a conclusion through premises. He is expressing dissatisfaction. The claims function as a list of grievances, not as premises supporting a conclusion.",
        "formal": "No argument structure — evaluative description and expression of dislike.",
        "why_right": "While Joss gives reasons why he dislikes the crane, he is not trying to establish a disputed conclusion. He is reporting his experience and expressing his feelings. If he had said 'therefore we should replace it,' that would complete an argument.",
        "related": ["A1.1", "A1.5"],
        "counter": "This is a borderline case. One could argue that 'the crane is terrible' is a conclusion supported by the listed problems. The player should grapple with this ambiguity.",
        "prompt": "Joss is clearly unhappy with the crane. Is he making an argument?",
        "rubric": [
            "Player assumes all complaints are arguments.",
            "Player is unsure.",
            "Player recognizes this is primarily a complaint but notes it is borderline.",
            "Player analyzes the structure and determines it is mainly evaluative description, though 'the crane is terrible' could be read as a conclusion supported by the specific complaints.",
            "Player identifies the borderline nature, explains why it could be read either way, and discusses what would make it more clearly an argument."
        ],
        "fuw": "Is Joss trying to convince you of something you do not already believe? Or is he venting about something he has experienced?",
        "fur": "This is genuinely borderline. 'The crane is terrible because it is slow and jams' has argument structure. But is that what Joss is doing, or is he just listing grievances? What would tip it clearly one way?",
        "npc": "Joss is grumpy, loud, and vents his frustrations freely.",
        "seed": "Do not get me started on that new crane. Actually, let me tell you about it.",
        "res": "The ambiguity of this case teaches the player that real speech does not always neatly categorize, setting up a discussion about charity and reconstruction.",
        "src": "PHIL 201 lecture notes 1.1-1.2"
    },
    # 20
    {
        "ctx": "A healer at the Temple of Light is speaking about a new treatment.",
        "text": "Healer Sera says: 'Since the moonpetal extract reduces inflammation, and since the patient's primary symptom is inflammation of the joints, the extract should alleviate the patient's condition.'",
        "spk": "Healer Sera, a methodical healer who reasons from general principles to specific cases.",
        "pname": "Argument with double 'since' premises",
        "pdesc": "Sera uses 'since' twice to introduce two premises and then states a conclusion. This is a clear deductive argument applying a general principle to a specific case.",
        "formal": "Since P1 (moonpetal reduces inflammation) and since P2 (patient's symptom is inflammation), C (extract should help).",
        "why_right": "Sera is reasoning from two premises to a conclusion. The double 'since' marks both premises, and the conclusion follows logically. She is arguing for a treatment recommendation, not explaining why a treatment already worked.",
        "related": ["A1.2", "A1.3"],
        "counter": "The substitution test confirms: replacing 'since' with 'because' preserves the meaning, showing these are premise indicators, not temporal markers.",
        "prompt": "Healer Sera is recommending a treatment. Is she making an argument? How do you know?",
        "rubric": [
            "Player does not recognize the argument.",
            "Player recognizes reasoning but cannot identify the parts.",
            "Player identifies the conclusion but only one premise.",
            "Player identifies both premises (marked by 'since') and the conclusion, confirming 'since' is a premise indicator here.",
            "Player does all of the above and applies the substitution test to confirm 'since' is not temporal."
        ],
        "fuw": "What treatment is Sera recommending and why? Look for the word that introduces her reasons.",
        "fur": "Good. Now apply the substitution test from the lecture notes: replace 'since' with 'because.' Does the meaning change? What does that tell you?",
        "npc": "Sera is calm, systematic, and reasons carefully before recommending treatments.",
        "seed": "Let me explain my reasoning for this treatment. I want you to understand why I believe it will work.",
        "res": "The player's correct identification leads to a medical reasoning puzzle where they must evaluate competing treatment arguments.",
        "src": "PHIL 201 lecture notes 1.2 — 'since' as premise indicator"
    },
    # 21-30: More scenarios covering edge cases
    {
        "ctx": "At the Adventurers' Guild, a veteran is recounting a quest.",
        "text": "Veteran Kira says: 'We entered the tomb at dawn. The first chamber was empty, but the second held three skeletal guardians. After dispatching them, we found the relic in the sarcophagus.'",
        "spk": "Veteran Kira, a seasoned adventurer who enjoys storytelling.",
        "pname": "Narrative, not argument",
        "pdesc": "Kira recounts events in sequence. No claim is being supported by reasons. This is a narrative.",
        "formal": "No argument structure — chronological narrative.",
        "why_right": "Kira is describing past events, not trying to prove a conclusion. The temporal connectors ('at dawn,' 'after') indicate sequence, not logical support.",
        "related": ["A1.1"],
        "counter": "If Kira had said 'so the tomb is not as well-guarded as people think,' that would add a conclusion, making it an argument.",
        "prompt": "Kira is telling you about a quest. Is there an argument in this account?",
        "rubric": [
            "Player treats any informative speech as an argument.",
            "Player is uncertain.",
            "Player says no argument but cannot explain clearly.",
            "Player identifies this as a narrative with no premise-conclusion structure.",
            "Player identifies the narrative, distinguishes temporal from logical connectors, and explains what would make it an argument."
        ],
        "fuw": "Is Kira trying to convince you of something, or is she just telling you what happened?",
        "fur": "Right. Could you add a sentence that would turn this narrative into an argument?",
        "npc": "Kira is enthusiastic, proud of her adventures, and loves to tell tales.",
        "seed": "Want to hear about the Tomb of the Silver King? It was quite the expedition.",
        "res": "Player's analysis leads Kira to share a more complex quest account that does contain an argument.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    {
        "ctx": "At a town meeting, Councillor Bram is opposing a proposal to build a new well.",
        "text": "Councillor Bram says: 'The proposed well site sits directly above a limestone formation. Limestone is porous and allows surface contaminants to seep into groundwater. As a result, any well drilled there would yield unsafe drinking water.'",
        "spk": "Councillor Bram, a geologically informed councillor who argues from scientific evidence.",
        "pname": "Argument with 'as a result' conclusion indicator",
        "pdesc": "Bram provides two premises about geology and contamination, then draws a conclusion using 'as a result.' Clear argument structure.",
        "formal": "P1 (well site over limestone), P2 (limestone allows contaminant seepage). As a result, C (well water would be unsafe).",
        "why_right": "Bram is trying to establish that the proposed well is a bad idea by providing geological reasons. The conclusion is in dispute (the council proposed the well), and the premises support the conclusion.",
        "related": ["A1.2", "A1.3"],
        "counter": "'As a result' can indicate causal explanation or argumentative conclusion. Here, the well has not been built yet, so Bram is predicting rather than explaining — this is an argument, not an explanation.",
        "prompt": "Councillor Bram is opposing the well proposal. Is he making an argument? What signals the conclusion?",
        "rubric": [
            "Player cannot tell if this is an argument.",
            "Player senses reasoning but cannot identify parts.",
            "Player finds the conclusion but not the indicator phrase.",
            "Player identifies both premises, the conclusion, and 'as a result' as the conclusion indicator.",
            "Player does all of the above and explains that this is predictive (argument) rather than explanatory because the well has not been built yet."
        ],
        "fuw": "What claim is Bram trying to establish? What evidence does he offer? Look for the phrase that connects them.",
        "fur": "Good. Now, if the well had already been built and the water was already unsafe, would Bram's same words be an argument or an explanation?",
        "npc": "Bram is analytical, speaks with quiet authority, and uses scientific reasoning.",
        "seed": "Before we vote, let me share what the geological survey actually shows us about that site.",
        "res": "Player's analysis earns Bram's trust, unlocking a geological survey side-quest.",
        "src": "PHIL 201 lecture notes 1.2-1.3"
    },
    {
        "ctx": "In the Royal Library, a scribe is cataloging books and talking to the player.",
        "text": "Scribe Noll says: 'This volume was printed in the Third Era. You can tell by the typeface — Third Era printers exclusively used Blackletter script. Also, the watermark on the paper matches the Thornfield mill, which only operated during the Third Era.'",
        "spk": "Scribe Noll, a meticulous archivist who dates books through physical evidence.",
        "pname": "Argument with convergent evidence",
        "pdesc": "Noll claims the book is from the Third Era and provides two independent lines of evidence (typeface and watermark). Each premise independently supports the conclusion. The word 'also' signals an additional, separate line of reasoning.",
        "formal": "C (Third Era printing). P1 (Blackletter typeface exclusive to Third Era). Also, P2 (watermark matches Thornfield mill, Third Era only).",
        "why_right": "Noll is arguing for a dating conclusion based on physical evidence. The two premises converge independently on the same conclusion.",
        "related": ["A1.7", "A1.2"],
        "counter": "If the player already accepted the dating, Noll's words would function as an explanation of how we know. The boundary depends on whether the claim is in dispute.",
        "prompt": "Scribe Noll is telling you about this book's age. Is he making an argument? How do the different pieces of evidence relate to each other?",
        "rubric": [
            "Player sees this as mere description.",
            "Player recognizes reasoning but cannot identify structure.",
            "Player identifies the conclusion and one piece of evidence.",
            "Player identifies the conclusion, both premises, and notes they are independent lines of evidence converging on the same claim.",
            "Player does all of the above and discusses the convergent structure — each premise independently supports the conclusion."
        ],
        "fuw": "What is Noll trying to establish? Does he give one reason or more? Do the reasons depend on each other?",
        "fur": "You noticed the convergent structure. Each piece of evidence supports the conclusion independently. Why is this stronger than having premises that depend on each other?",
        "npc": "Noll is detail-oriented, quiet, and speaks precisely about physical evidence.",
        "seed": "Careful with that volume. Let me show you how to determine when it was printed.",
        "res": "Player's analysis leads to a forgery detection quest in the library.",
        "src": "PHIL 201 lecture notes 1.4 — complex argument structures"
    },
    {
        "ctx": "At the Fisherman's Wharf, an old sailor is giving advice to a young apprentice.",
        "text": "Old Marko says: 'Stay away from the northern shoals during spring tide. The currents there are treacherous when the tides are high.'",
        "spk": "Old Marko, a retired fisherman who gives practical advice based on experience.",
        "pname": "Advice with implicit argument",
        "pdesc": "Marko gives advice (stay away from the shoals) and a reason (treacherous currents during high tides). This has the structure of an implicit argument: the reason supports the advice. But the advice itself is a directive, not a statement.",
        "formal": "P1 (currents are treacherous during spring tides). [Implicit C: it is dangerous to go there → directive: stay away.]",
        "why_right": "Marko is providing a reason for his directive. This is an argument embedded in practical advice — the reason (dangerous currents) supports the implicit conclusion (it is dangerous) which grounds the directive (stay away).",
        "related": ["A1.5", "A1.1"],
        "counter": "Strictly, the directive 'stay away' is not a statement and cannot be a conclusion. But the implicit claim 'it is dangerous' can be. Practical arguments often have this structure: reasons → implicit claim → directive.",
        "prompt": "Old Marko is giving advice. Is there an argument lurking in his warning?",
        "rubric": [
            "Player sees only a command, no argument.",
            "Player senses reasoning but is confused by the directive form.",
            "Player identifies the reason but not the implicit conclusion.",
            "Player identifies the implicit argument: the reason (dangerous currents) supports an implicit conclusion (it is dangerous), which grounds the directive.",
            "Player does all of the above and discusses the relationship between arguments and directives in practical reasoning."
        ],
        "fuw": "Why does Marko tell you to stay away? Does he give a reason? If so, what claim does that reason support?",
        "fur": "Good. Many pieces of practical advice contain implicit arguments. The directive is not the conclusion — but there is a factual conclusion hiding behind it. What is it?",
        "npc": "Marko is gruff, experienced, and speaks from decades of seafaring knowledge.",
        "seed": "The sea does not forgive mistakes, lad. Let me tell you what I have learned.",
        "res": "Player's analysis leads Marko to share more nuanced navigational knowledge, including a complex argument about ocean currents.",
        "src": "PHIL 201 lecture notes 1.1-1.2"
    },
    {
        "ctx": "At the Ironvale Apothecary, two herbalists are disagreeing about a plant identification.",
        "text": "Herbalist Tara says: 'That is definitely foxglove, not purple coneflower. Look — the leaves are alternate, not opposite, and the flowers are tubular, not daisy-shaped. Foxglove always has alternate leaves and tubular flowers.'",
        "spk": "Herbalist Tara, a precise botanist who argues from morphological features.",
        "pname": "Argument from observed features to identification",
        "pdesc": "Tara argues for an identification (foxglove) based on two observed features (alternate leaves, tubular flowers) and a general principle (foxglove always has these features). This is a clear argument.",
        "formal": "P1 (leaves are alternate), P2 (flowers are tubular), P3 (foxglove always has alternate leaves and tubular flowers). Therefore C (this is foxglove).",
        "why_right": "Tara is making a disputed claim (plant identity) and supporting it with observed evidence and a general principle. The dispute with her colleague makes this clearly an argument, not an explanation.",
        "related": ["A1.2", "A1.3"],
        "counter": "The argument is deductively valid only if foxglove is the only plant with these features. Tara's argument might be better read as inductive — the features increase the probability of the identification.",
        "prompt": "Tara and her colleague disagree about the plant. Is Tara making an argument? What are the key parts?",
        "rubric": [
            "Player does not recognize the argument.",
            "Player sees reasoning but cannot parse it.",
            "Player identifies the conclusion but not all premises.",
            "Player identifies all three premises, the conclusion, and the argumentative structure.",
            "Player does all of the above and considers whether the argument is deductive or inductive — does having these features guarantee it is foxglove?"
        ],
        "fuw": "What does Tara claim the plant is? What evidence does she cite? And what general principle does she invoke?",
        "fur": "Could another plant also have alternate leaves and tubular flowers? If so, is Tara's argument deductively valid or merely inductively strong?",
        "npc": "Tara is sharp, competitive, and takes plant identification very seriously.",
        "seed": "I have been studying these plants for years. Let me show you exactly how to tell them apart.",
        "res": "Player's analysis leads to a botanical identification challenge.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    {
        "ctx": "At the Council of Elders, a diplomat is presenting a report about the neighboring kingdom.",
        "text": "Diplomat Fen says: 'The kingdom of Aldris has mobilized three regiments along our border. Their ambassador refused to attend the harvest summit. Their king's address last week specifically mentioned territorial expansion. I think we should increase our border patrols.'",
        "spk": "Diplomat Fen, a cautious foreign affairs advisor who reads patterns in political behavior.",
        "pname": "Argument with multiple premises and hedged conclusion",
        "pdesc": "Fen provides three factual premises and draws a policy conclusion hedged with 'I think.' The premises are independent pieces of evidence converging on a threat assessment that grounds the recommendation.",
        "formal": "P1 (military mobilization), P2 (diplomatic snub), P3 (expansionist rhetoric). Therefore, [implicit: Aldris poses a threat], so C (increase border patrols).",
        "why_right": "Fen is marshaling evidence to support a recommendation. The three premises independently point to the same conclusion. The hedge 'I think' acknowledges uncertainty but does not change the argumentative structure.",
        "related": ["A1.2", "A1.7", "A1.5"],
        "counter": "Fen's argument has an implicit intermediate conclusion ('Aldris is a threat') that bridges the factual premises and the policy recommendation. This is a multi-step argument.",
        "prompt": "Diplomat Fen presents several facts and then makes a recommendation. Is this an argument? How do the parts connect?",
        "rubric": [
            "Player treats this as a simple report.",
            "Player senses an argument but cannot identify the structure.",
            "Player identifies the conclusion but not how the premises support it.",
            "Player identifies all three premises, the conclusion, and notes the implicit intermediate conclusion about threat assessment.",
            "Player does all of the above and discusses the convergent evidence structure, the is-ought gap between factual premises and policy conclusion, and the hedging function of 'I think.'"
        ],
        "fuw": "What does Fen want the council to do? And what facts does he point to? Is there a step in the reasoning he leaves unstated?",
        "fur": "Excellent. Notice the gap between the factual premises and the policy conclusion. What assumption bridges 'Aldris is acting aggressively' and 'we should increase patrols'?",
        "npc": "Fen is measured, diplomatic, and hedges his claims appropriately.",
        "seed": "I have been monitoring the situation at the border. The evidence concerns me.",
        "res": "Player's analysis leads to a diplomatic intelligence quest where they must evaluate competing assessments.",
        "src": "PHIL 201 lecture notes 1.2, 1.9"
    },
    {
        "ctx": "At the Greenhollow School, a teacher is quizzing students.",
        "text": "Teacher Alma says: 'What is the capital of Westmark? When was the Battle of Redfield? Name the three rivers that form the Delta.'",
        "spk": "Teacher Alma, a strict schoolteacher asking factual questions.",
        "pname": "Questions, not an argument",
        "pdesc": "Alma is asking questions. Questions are not statements — they cannot be true or false and therefore cannot be premises or conclusions.",
        "formal": "No argument structure — interrogatives have no truth values.",
        "why_right": "Arguments require statements. Questions request information but do not assert anything. Alma is testing knowledge, not making an argument.",
        "related": ["A1.1"],
        "counter": "Rhetorical questions can function as implicit arguments ('Isn't it obvious that we should help them?' implies we should). But these are genuine questions seeking answers.",
        "prompt": "Teacher Alma is asking questions. Could this be an argument?",
        "rubric": [
            "Player thinks questions can form arguments.",
            "Player is unsure.",
            "Player correctly says no but cannot explain why.",
            "Player explains that questions are not statements and cannot serve as premises or conclusions.",
            "Player explains the above and distinguishes genuine questions from rhetorical questions, which can function as implicit arguments."
        ],
        "fuw": "Can a question be true or false? If not, can it be a premise or conclusion?",
        "fur": "Right. But what about rhetorical questions? 'Is it not obvious that the bridge needs repair?' — is that a question or an implicit argument?",
        "npc": "Alma is strict, methodical, and tests students frequently.",
        "seed": "Class, I want to see what you remember. Answer quickly.",
        "res": "Player's correct identification leads Alma to ask a harder question about rhetorical questions.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    {
        "ctx": "At the Alchemist's Symposium, two alchemists are disagreeing about the cause of an explosion.",
        "text": "Alchemist Voss says: 'The explosion could not have been caused by the sulfur alone. Sulfur requires a catalyst at those temperatures. The only catalyst present in the lab was iron filings. Therefore, the iron filings mixed with the sulfur caused the explosion.'",
        "spk": "Alchemist Voss, a logical investigator who builds arguments step by step.",
        "pname": "Argument with process of elimination",
        "pdesc": "Voss eliminates one possibility (sulfur alone) using a premise (requires catalyst), identifies the available catalyst (iron filings), and concludes with the cause. This is a deductive argument using process of elimination.",
        "formal": "P1 (sulfur alone cannot cause explosion at those temperatures), P2 (sulfur requires a catalyst), P3 (only iron filings were available as catalyst). Therefore C (iron filings + sulfur caused explosion).",
        "why_right": "Voss is constructing a logical argument by eliminating alternatives and concluding with the only remaining possibility. The word 'therefore' marks the conclusion.",
        "related": ["A1.2", "A1.3", "A1.7"],
        "counter": "The argument assumes no other catalyst was present ('the only catalyst'). If that premise is wrong, the conclusion does not follow.",
        "prompt": "Alchemist Voss is investigating the explosion. Is he making an argument? What logical strategy does he use?",
        "rubric": [
            "Player cannot identify the argument.",
            "Player recognizes reasoning but cannot identify the strategy.",
            "Player identifies the conclusion but not the eliminative structure.",
            "Player identifies the premises, conclusion, 'therefore' indicator, and the eliminative reasoning strategy.",
            "Player does all of the above and evaluates whether the elimination is complete — could there be another catalyst Voss overlooked?"
        ],
        "fuw": "What possibilities does Voss consider? Which does he rule out, and why? What is left?",
        "fur": "Good. This is reasoning by elimination. Is it deductively valid? What assumption must hold for the conclusion to follow with certainty?",
        "npc": "Voss is methodical, precise, and thinks like a detective.",
        "seed": "The explosion was no accident. Let me walk you through what must have happened.",
        "res": "Player's analysis leads to a lab investigation quest with more complex eliminative reasoning.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    {
        "ctx": "At the market, a child is trying to convince a parent to buy a toy.",
        "text": "The child says: 'Please, please, please buy me the wooden knight! Please! I want it so much! Pleeeease!'",
        "spk": "A young child in the market who wants a toy.",
        "pname": "Pleading, not argument",
        "pdesc": "The child is making a request through repetition and emotional appeal. There are no premises, no conclusion, and no logical structure. This is persuasion through persistence, not argument.",
        "formal": "No argument structure — repeated request/plea.",
        "why_right": "Arguments provide reasons for a conclusion. The child provides no reasons — just repeated requests and expressions of desire. Wanting something is not a reason that it should be provided.",
        "related": ["A1.1"],
        "counter": "If the child had said 'You should buy me the knight because I finished all my chores and you promised me a reward,' that would be an argument.",
        "prompt": "The child really wants that toy. Is there an argument in this plea?",
        "rubric": [
            "Player thinks emotional intensity makes something an argument.",
            "Player is unsure.",
            "Player correctly says no but struggles to explain.",
            "Player identifies this as a plea with no logical structure — no reasons supporting a conclusion.",
            "Player explains the difference between persuasion through argument (giving reasons) and persuasion through other means (repetition, emotional appeal), and notes what the child would need to add."
        ],
        "fuw": "Does the child give any reasons why the parent should buy the toy? Or is the child just asking very enthusiastically?",
        "fur": "This is persuasion without argument. The lecture notes mention that logic is about rational persuasion through reasons. Can you think of other forms of non-rational persuasion?",
        "npc": "A small child, maybe seven years old, big eyes, relentless.",
        "seed": "I want it! I want it! It is the best one!",
        "res": "The parent nearby asks the player to help the child formulate an actual argument for why they deserve the toy.",
        "src": "PHIL 201 lecture notes 1.1, 1.11 — evaluative language and non-rational persuasion"
    },
    {
        "ctx": "At the Watchtower, a scout reports to the commander.",
        "text": "Scout Wren says: 'I spotted dust clouds to the south. The pattern is consistent with a cavalry column — wide, low, moving in formation. Based on the dust density and wind conditions, I estimate roughly two hundred riders approaching from the Ashford road.'",
        "spk": "Scout Wren, a trained military observer who reasons from evidence to conclusions.",
        "pname": "Argument from observation to inference",
        "pdesc": "Wren observes evidence (dust clouds), applies expertise (pattern recognition, density analysis), and draws a conclusion (cavalry column of ~200 riders). This is an inductive argument from evidence to inference.",
        "formal": "P1 (dust clouds to the south), P2 (pattern consistent with cavalry column), P3 (dust density and wind conditions). Therefore C (~200 riders approaching from Ashford road).",
        "why_right": "Wren is not merely describing what she sees — she is drawing an inference from observations. The conclusion (200 riders approaching) goes beyond the raw data (dust clouds) and is supported by her analysis.",
        "related": ["A1.2", "A1.5"],
        "counter": "This is an inductive argument — the conclusion is probable given the premises, but not certain. The dust could have another explanation.",
        "prompt": "Scout Wren is reporting. Is she just describing what she sees, or is she making an argument?",
        "rubric": [
            "Player treats this as a simple observation report.",
            "Player recognizes inference but cannot distinguish it from description.",
            "Player identifies the conclusion but not the full structure.",
            "Player distinguishes the observation (dust clouds) from the inference (cavalry column) and identifies the argumentative structure.",
            "Player does all of the above and classifies this as an inductive argument — the conclusion goes beyond the evidence and is probable rather than certain."
        ],
        "fuw": "Can Wren actually see two hundred riders? Or is she concluding that from what she can see? What is the difference?",
        "fur": "Good. Wren's conclusion goes beyond her observations. This is inductive reasoning — the premises make the conclusion probable, not certain. What else could explain the dust clouds?",
        "npc": "Wren is focused, professional, and speaks in concise military reports.",
        "seed": "Commander, I have something to report. The southern horizon is not looking good.",
        "res": "Commander tasks the player with evaluating Wren's inference and considering alternative explanations.",
        "src": "PHIL 201 lecture notes 1.8 — deductive vs inductive arguments"
    },
]

# Build the remaining A1.1 records from templates (31-50)
a11_extra = [
    {
        "ctx": "At the Stonekeep Tribunal, a lawyer presents closing arguments in a theft case.",
        "text": "Lawyer Moss says: 'My client was in Ashford on the night of the theft — three witnesses confirm this. One cannot steal from a vault in Ironvale while standing in Ashford. It follows that my client did not commit this theft.'",
        "spk": "Lawyer Moss, a sharp defense attorney who argues from alibis and logic.",
    },
    {
        "ctx": "A botanist in the Royal Gardens is labeling plants for a visiting noble.",
        "text": "Botanist Elise says: 'This is a winter rose. It blooms in frost, has silver-tipped petals, and emits a faint luminescence at night.'",
        "spk": "Botanist Elise, a knowledgeable gardener giving a tour.",
    },
    {
        "ctx": "At the Merchant's Council, a trader presents a proposal to open a new trade route.",
        "text": "Trader Voss says: 'The mountain pass saves three days compared to the coastal road. Three days of travel means three days of provisions and wages saved. Hence, the mountain route is more profitable.'",
        "spk": "Trader Voss, a profit-driven merchant who argues from cost calculations.",
    },
    {
        "ctx": "A mother is scolding a child at the village well.",
        "text": "She says: 'I told you not to play near the well! Go home right now and do not come back here!'",
        "spk": "A worried mother issuing commands to her child.",
    },
    {
        "ctx": "At the Mage's Tower, two apprentices are discussing a failed experiment.",
        "text": "Apprentice Kai says: 'The spell fizzled because I used powdered quartz instead of ground crystal. Master Venn said the two have different resonance frequencies, which explains the energy misfire.'",
        "spk": "Apprentice Kai, a student explaining why an experiment failed.",
    },
    {
        "ctx": "A town crier announces the day's news in the village square.",
        "text": "The crier shouts: 'Hear ye! The harvest festival begins tomorrow at dawn! The queen has declared a holiday! All shops will close at noon!'",
        "spk": "A town crier delivering official announcements.",
    },
    {
        "ctx": "At the Hunter's Lodge, a tracker argues that a certain beast is responsible for missing livestock.",
        "text": "Tracker Syl says: 'The claw marks on the fence posts are too wide for a wolf. The tracks show four toes, not five. Only a mountain lion matches both features. So a mountain lion has been taking the sheep.'",
        "spk": "Tracker Syl, an expert tracker who argues from physical evidence.",
    },
    {
        "ctx": "A priest at the shrine is delivering a blessing.",
        "text": "The priest intones: 'May the light protect you on your journey. May your sword stay sharp and your spirit stay true. Go forth with the gods' favor.'",
        "spk": "A shrine priest delivering a traditional blessing.",
    },
    {
        "ctx": "At the guild hall, an architect is trying to convince the council to reinforce the north wall.",
        "text": "Architect Lorn says: 'The north wall was built sixty years ago with single-layer stone. Modern walls use double-layer construction because it distributes force better. Since the wall must withstand siege weapons that did not exist sixty years ago, we need to reinforce it.'",
        "spk": "Architect Lorn, a structural expert who argues from engineering principles and historical change.",
    },
    {
        "ctx": "At the tavern, a regular is expressing his opinion about the new mayor.",
        "text": "Barton says: 'The new mayor is alright, I suppose. Not as good as the last one. Things were better before.'",
        "spk": "Barton, a nostalgic regular who expresses opinions without supporting them.",
    },
    {
        "ctx": "In the Academy library, a scholar argues for the authenticity of a historical document.",
        "text": "Scholar Pell says: 'This manuscript must be genuine. The ink composition matches Third Era formulations, the handwriting is consistent with the known scribes of the Thornfield monastery, and the content references events that were only recently confirmed by archaeological evidence.'",
        "spk": "Scholar Pell, a document authenticator who argues from multiple lines of physical evidence.",
    },
    {
        "ctx": "A healer is describing a patient's condition to a colleague.",
        "text": "Healer Tam says: 'The patient presents with elevated temperature, swollen lymph nodes, and a persistent cough. The rash appeared on day three.'",
        "spk": "Healer Tam, a clinical practitioner describing symptoms.",
    },
    {
        "ctx": "At the Shepherd's Fair, a judge is explaining why a particular ram won the prize.",
        "text": "Judge Oria says: 'The Blackmere ram won because it had the thickest fleece, the strongest build, and the calmest temperament — all three criteria that our scoring rubric prioritizes.'",
        "spk": "Judge Oria, a livestock judge explaining a decision that has already been made.",
    },
    {
        "ctx": "At the docks, a customs official is checking cargo manifests.",
        "text": "Official Henn says: 'Manifest says twenty barrels of wine. I count twenty barrels of wine. Everything checks out. You may proceed.'",
        "spk": "Official Henn, a bureaucratic customs agent doing routine verification.",
    },
    {
        "ctx": "In the war room, a general is arguing against a proposed frontal assault.",
        "text": "General Rath says: 'A frontal assault would be suicidal. The enemy holds the high ground, their archers have clear lines of sight for three hundred yards, and they outnumber us two to one. There is no scenario in which a direct charge succeeds.'",
        "spk": "General Rath, a strategic commander who argues from tactical analysis.",
    },
    {
        "ctx": "At the monastery, a monk is reciting a prayer.",
        "text": "Brother Aldus intones: 'Grant us wisdom to see the truth, courage to follow it, and humility to accept when we are wrong.'",
        "spk": "Brother Aldus, a contemplative monk delivering a prayer.",
    },
    {
        "ctx": "In the wizard's workshop, an enchanter explains why a charm failed.",
        "text": "Enchanter Rilla says: 'The charm broke because the binding rune was inscribed clockwise instead of counterclockwise. Clockwise inscriptions create repulsion rather than attraction, which is why the amulet repelled the very energy it was meant to contain.'",
        "spk": "Enchanter Rilla explaining the causal mechanism behind a failed enchantment.",
    },
    {
        "ctx": "A street philosopher in the market district poses a challenge to passersby.",
        "text": "The philosopher says: 'Consider this: all mortals die. You are mortal. What follows? Can you tell me?'",
        "spk": "A Socratic street philosopher who poses logical puzzles rather than asserting conclusions.",
    },
    {
        "ctx": "At the tavern, a gambler is trying to recruit the player for a card game.",
        "text": "Gambler Finch says: 'Come on, sit down, the stakes are low and the ale is good. You look like someone who enjoys a challenge.'",
        "spk": "Gambler Finch, a friendly hustler making a social invitation.",
    },
    {
        "ctx": "At the council meeting, Alderman Drew makes the case for expanding the market square.",
        "text": "Alderman Drew says: 'Since we have seen a thirty percent increase in merchant applications this year, and since the current market cannot accommodate more than forty stalls, it is clear that we must expand the square or lose revenue to neighboring towns.'",
        "spk": "Alderman Drew, a business-minded councillor who argues from economic data.",
    },
]

# Now build the full 50 A1.1 records
def build_a11(idx, d):
    """Build an A1.1 record from either a full dict or a short template."""
    seq = f"A1.1-AF{idx:04d}"
    if "pname" in d:  # full record
        return rec(
            seq, "A1.1", "Identifying arguments", "drill",
            scen(d["ctx"], d["text"], d["spk"]),
            struct(d["pname"], d["pdesc"], d["formal"], d["why_right"], d["related"], d["counter"]),
            assess(d["prompt"], d["rubric"], d["fuw"], d["fur"]),
            hooks(d["npc"], d["seed"], d["res"]),
            d["src"]
        )
    return None  # will be filled by the batch builder below

# Process the 30 detailed A1.1 records
for i, d in enumerate(a11_data, 1):
    records.append(build_a11(i, d))

# Now build the 20 shorter A1.1 records with full fields
short_a11_full = [
    # 31 - Lawyer argument
    {
        "ctx": a11_extra[0]["ctx"], "text": a11_extra[0]["text"], "spk": a11_extra[0]["spk"],
        "pname": "Argument from alibi with 'it follows that'",
        "pdesc": "Moss presents an alibi (client in Ashford), a general principle (cannot be in two places), and draws a conclusion using 'it follows that.' Clear deductive argument.",
        "formal": "P1 (client was in Ashford), P2 (cannot steal in Ironvale while in Ashford). It follows that C (client did not commit theft).",
        "why_right": "Moss offers premises to establish a conclusion in dispute. The indicator phrase 'it follows that' marks the conclusion. This is a deductive argument.",
        "related": ["A1.2", "A1.3"],
        "counter": "The argument is valid but the premises could be challenged — were the witnesses reliable?",
        "prompt": "Lawyer Moss is making his case. Is this an argument? What are the key parts?",
        "rubric": ["Player cannot identify the argument.", "Player senses reasoning but cannot parse it.", "Player finds the conclusion but not the alibi structure.", "Player identifies both premises, the conclusion, and 'it follows that' as the indicator.", "Player identifies the full structure and evaluates whether the premises are sufficient."],
        "fuw": "What does Moss want the tribunal to believe? What facts does he cite?", "fur": "Good. Is this a deductive or inductive argument? Could the conclusion be false even if the premises are true?",
        "npc": "Moss is polished, logical, and speaks in structured arguments.", "seed": "Members of the tribunal, the evidence clearly exonerates my client.", "res": "Player's analysis leads to a courtroom logic challenge.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    # 32 - Botanist description
    {
        "ctx": a11_extra[1]["ctx"], "text": a11_extra[1]["text"], "spk": a11_extra[1]["spk"],
        "pname": "Description, not argument",
        "pdesc": "Elise is describing the features of a plant. She is not trying to prove a conclusion — she is providing information.",
        "formal": "No argument structure — descriptive classification.",
        "why_right": "No disputed conclusion is being supported by premises. Elise is cataloging observable features for informational purposes.",
        "related": ["A1.1", "A1.6"],
        "counter": "If someone disputed the identification, Elise's features could become premises in an argument. Context determines function.",
        "prompt": "Elise is telling you about the plant. Is she making an argument?",
        "rubric": ["Player treats all informative speech as argument.", "Player is unsure.", "Player says no but cannot explain.", "Player identifies this as description — information given, no conclusion supported.", "Player explains the distinction and notes how context could turn this into an argument."],
        "fuw": "Is Elise trying to convince you of something, or just telling you what the plant is?", "fur": "Right. But if someone said 'That is not a winter rose,' could Elise's same words become premises in an argument?",
        "npc": "Elise is knowledgeable, patient, and loves sharing botanical facts.", "seed": "Come closer. Let me show you the most beautiful specimen in the garden.", "res": "Player's analysis leads to a plant identification challenge.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 33 - Trader argument
    {
        "ctx": a11_extra[2]["ctx"], "text": a11_extra[2]["text"], "spk": a11_extra[2]["spk"],
        "pname": "Argument with 'hence' conclusion indicator",
        "pdesc": "Voss provides premises about travel time and cost savings, concluding with 'hence' that the mountain route is more profitable.",
        "formal": "P1 (mountain pass saves three days), P2 (three days saved = provisions and wages saved). Hence C (mountain route more profitable).",
        "why_right": "Voss is arguing for a business conclusion based on cost analysis. 'Hence' signals the conclusion.",
        "related": ["A1.2", "A1.5"],
        "counter": "The argument ignores risks of the mountain pass. More profitable does not mean better if the risk is higher.",
        "prompt": "Trader Voss is proposing a route. Is he making an argument?",
        "rubric": ["Player does not recognize the argument.", "Player senses reasoning.", "Player identifies conclusion but not premises.", "Player identifies premises, conclusion, and 'hence.'", "Player does all and evaluates missing considerations like risk."],
        "fuw": "What does Voss conclude, and what reasons does he give?", "fur": "Good. Is Voss ignoring anything important? What premise might be missing?",
        "npc": "Voss is calculated, profit-focused, and speaks in numbers.", "seed": "Let me show you the numbers. The route practically pays for itself.", "res": "Player's analysis leads to a trade route optimization quest.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    # 34 - Mother commanding
    {
        "ctx": a11_extra[3]["ctx"], "text": a11_extra[3]["text"], "spk": a11_extra[3]["spk"],
        "pname": "Commands with no argument",
        "pdesc": "The mother issues directives. Commands have no truth value and cannot form premises or conclusions.",
        "formal": "No argument structure — imperatives.",
        "why_right": "Arguments require statements. 'Go home right now' and 'do not come back' are commands, not claims that can be true or false.",
        "related": ["A1.1"],
        "counter": "If she had said 'you could fall in and drown, so go home,' that would contain an argument.",
        "prompt": "The mother is clearly upset. Is she making an argument?",
        "rubric": ["Player confuses commands with arguments.", "Player is unsure.", "Player says no but cannot explain.", "Player identifies commands as non-statements without truth values.", "Player explains the distinction and shows what would make this an argument."],
        "fuw": "Can 'go home right now' be true or false? If not, can it be a premise or conclusion?", "fur": "Right. But she does say 'I told you not to play near the well' — is that a statement? Could it be part of an argument?",
        "npc": "A worried mother, protective and sharp-toned.", "seed": "What did I tell you about the well? How many times do I have to say it?", "res": "Overhearing this interaction sets up a contrast with a nearby argument.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 35 - Apprentice explanation
    {
        "ctx": a11_extra[4]["ctx"], "text": a11_extra[4]["text"], "spk": a11_extra[4]["spk"],
        "pname": "Explanation, not argument",
        "pdesc": "Kai is explaining why the spell fizzled — a fact already observed. He is providing a causal account, not arguing for a disputed conclusion.",
        "formal": "X happened because Y (causal explanation).",
        "why_right": "The spell's failure is already known. Kai explains the cause, not argues that it failed. 'Because' here introduces a causal explanation, not a premise.",
        "related": ["A1.6", "A1.1"],
        "counter": "If someone had denied the spell fizzled and Kai said 'It must have fizzled because I used the wrong reagent,' that would be an argument.",
        "prompt": "Kai uses the word 'because.' Is he making an argument?",
        "rubric": ["Player assumes 'because' always signals argument.", "Player is unsure.", "Player identifies explanation but cannot articulate why.", "Player distinguishes explanation from argument — the conclusion is already accepted.", "Player explains the dual role of 'because' and applies the test: is the 'because' answering 'why believe this?' or 'why did this happen?'"],
        "fuw": "Is Kai trying to convince you the spell fizzled, or telling you why it fizzled?", "fur": "Good. The same word 'because' can introduce a premise in an argument or a cause in an explanation. What determines which?",
        "npc": "Kai is earnest, a bit embarrassed about the failure, and eager to understand.", "seed": "I think I know what went wrong. Let me walk you through it.", "res": "Player's insight leads to a reagent-mixing challenge.",
        "src": "PHIL 201 lecture notes 1.3"
    },
    # 36 - Town crier announcements
    {
        "ctx": a11_extra[5]["ctx"], "text": a11_extra[5]["text"], "spk": a11_extra[5]["spk"],
        "pname": "Announcements, not argument",
        "pdesc": "The crier delivers official information. These are assertions and directives but not organized as premises supporting a conclusion.",
        "formal": "No argument structure — public announcements.",
        "why_right": "The crier is informing, not arguing. No claim is supported by reasons; each statement is independently delivered as news.",
        "related": ["A1.1"],
        "counter": "If the crier had said 'Since the queen declared a holiday, all shops must close at noon,' that would contain an argument.",
        "prompt": "The town crier is making announcements. Is there an argument here?",
        "rubric": ["Player treats announcements as arguments.", "Player unsure.", "Player says no but cannot explain.", "Player identifies announcements as informational, not argumentative.", "Player explains the distinction and notes what would create argument structure."],
        "fuw": "Is the crier giving you reasons to believe something, or just telling you what is happening?", "fur": "Right. But notice: 'The queen has declared a holiday' could serve as a premise if someone challenged the shop closures.",
        "npc": "Official, loud, impersonal.", "seed": "Hear ye, hear ye! Attend to the day's proclamations!", "res": "A nearby citizen questions the announcements, leading to an argument analysis.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 37 - Tracker argument
    {
        "ctx": a11_extra[6]["ctx"], "text": a11_extra[6]["text"], "spk": a11_extra[6]["spk"],
        "pname": "Argument by elimination with 'so'",
        "pdesc": "Syl eliminates wolf, identifies distinctive features, and concludes with 'so.' This is an eliminative argument from physical evidence.",
        "formal": "P1 (claw marks too wide for wolf), P2 (four toes not five), P3 (only mountain lion matches). So C (mountain lion responsible).",
        "why_right": "Syl presents evidence, eliminates alternatives, and draws a conclusion. The word 'so' marks the conclusion. This is a clear argument.",
        "related": ["A1.2", "A1.3"],
        "counter": "The argument assumes Syl's catalog of possible predators is complete. What if a creature he has not considered also matches?",
        "prompt": "Tracker Syl is identifying the predator. Is this an argument? How is it structured?",
        "rubric": ["Player does not see an argument.", "Player senses reasoning.", "Player finds conclusion but not the eliminative structure.", "Player identifies premises, conclusion, and the elimination strategy.", "Player evaluates completeness of the elimination."],
        "fuw": "What animal does Syl conclude is responsible, and how does he reach that conclusion?", "fur": "Good. Is the elimination complete? Could there be another animal Syl has not considered?",
        "npc": "Syl is quiet, observant, and speaks from tracking expertise.", "seed": "Come. I will show you what the evidence tells us about this predator.", "res": "Player's analysis leads to a tracking quest.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    # 38 - Priest blessing
    {
        "ctx": a11_extra[7]["ctx"], "text": a11_extra[7]["text"], "spk": a11_extra[7]["spk"],
        "pname": "Blessing/prayer, not argument",
        "pdesc": "A blessing expresses wishes and invocations. These are neither true nor false and cannot form premises or conclusions.",
        "formal": "No argument structure — performative/optative speech.",
        "why_right": "'May the light protect you' is a wish, not a statement. It has no truth value. Blessings are performative speech acts, not arguments.",
        "related": ["A1.1"],
        "counter": "Religious arguments exist ('God exists because...'), but a blessing is not one. It is a speech act that invokes rather than argues.",
        "prompt": "The priest is delivering a blessing. Is there any argument in these words?",
        "rubric": ["Player thinks blessings contain arguments.", "Player unsure.", "Player says no but cannot explain.", "Player identifies wishes/invocations as non-statements without truth values.", "Player distinguishes performative speech acts from arguments and explains why."],
        "fuw": "Can 'may the light protect you' be true or false? If not, what kind of speech act is this?", "fur": "Right. This is performative language. It does something (blesses) rather than states something. Can you think of other performative speech acts?",
        "npc": "Serene, ritualistic, speaks in measured cadences.", "seed": "Come, traveler. Receive the blessing before you depart.", "res": "Player's understanding leads to a philosophical discussion about speech acts.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 39 - Architect argument
    {
        "ctx": a11_extra[8]["ctx"], "text": a11_extra[8]["text"], "spk": a11_extra[8]["spk"],
        "pname": "Argument with 'since' premise indicator and historical comparison",
        "pdesc": "Lorn presents premises about wall construction, modern standards, and changed threats, concluding that reinforcement is needed. 'Since' introduces the key premise.",
        "formal": "P1 (wall is 60 years old, single-layer), P2 (modern walls are double-layer, better force distribution), Since P3 (wall must now withstand new siege weapons). C (we need to reinforce).",
        "why_right": "Lorn is arguing for a policy (reinforce the wall) based on engineering facts and changed circumstances. 'Since' marks a premise, and the conclusion is in dispute.",
        "related": ["A1.2", "A1.5"],
        "counter": "The substitution test: replacing 'since' with 'because' preserves meaning, confirming it is a premise indicator.",
        "prompt": "Architect Lorn is making a case for wall reinforcement. Is this an argument?",
        "rubric": ["Player does not recognize it.", "Player senses reasoning.", "Player finds conclusion but not all premises.", "Player identifies all premises, conclusion, and 'since' as indicator.", "Player applies substitution test and evaluates the argument's strength."],
        "fuw": "What does Lorn want the council to do, and what reasons does he give?", "fur": "Good. Apply the substitution test: replace 'since' with 'because.' Does the meaning change?",
        "npc": "Lorn is precise, speaks with blueprints in hand.", "seed": "I have surveyed the wall. The findings are concerning.", "res": "Player's analysis leads to a fortification engineering quest.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    # 40 - Barton opinion
    {
        "ctx": a11_extra[9]["ctx"], "text": a11_extra[9]["text"], "spk": a11_extra[9]["spk"],
        "pname": "Unsupported opinion, not argument",
        "pdesc": "Barton expresses opinions and makes comparisons but offers no reasons. There is no premise-conclusion structure.",
        "formal": "No argument structure — expression of preference and nostalgia.",
        "why_right": "Barton says things were better and the new mayor is not as good, but he does not give any reasons for these evaluations. An argument requires premises supporting a conclusion.",
        "related": ["A1.1"],
        "counter": "If Barton had said 'The new mayor is worse because taxes have gone up and services have declined,' that would be an argument.",
        "prompt": "Barton seems to have an opinion. Is he making an argument?",
        "rubric": ["Player treats opinions as arguments.", "Player unsure.", "Player says no but cannot explain.", "Player identifies the absence of reasons supporting the evaluations.", "Player explains that opinions without supporting reasons are not arguments, and shows what would make this one."],
        "fuw": "Barton says things were better before. Does he give you any reason to think so?", "fur": "Exactly. Opinions are claims; arguments are claims plus reasons. What reasons might Barton offer?",
        "npc": "Barton is a nostalgic, slightly grumpy regular.", "seed": "Ah, you are new here. Things used to be different, you know.", "res": "A follow-up interaction challenges the player to help Barton articulate his reasons.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 41 - Scholar authentication argument
    {
        "ctx": a11_extra[10]["ctx"], "text": a11_extra[10]["text"], "spk": a11_extra[10]["spk"],
        "pname": "Argument with convergent evidence and 'must be'",
        "pdesc": "Pell argues for the manuscript's authenticity using three independent lines of evidence. 'Must be' signals the conclusion, and the evidence converges.",
        "formal": "C (manuscript genuine). P1 (ink matches), P2 (handwriting matches), P3 (content references recently confirmed events).",
        "why_right": "Pell is making a disputed claim supported by three independent lines of evidence. Each premise independently increases the probability of the conclusion.",
        "related": ["A1.7", "A1.2"],
        "counter": "Any individual line of evidence could be faked. The convergence strengthens the argument but does not make it deductively valid.",
        "prompt": "Scholar Pell claims the manuscript is genuine. Is he making an argument? How does his evidence work?",
        "rubric": ["Player does not see an argument.", "Player senses reasoning.", "Player finds conclusion and some evidence.", "Player identifies all three premises, the conclusion, and the convergent structure.", "Player evaluates convergent evidence — stronger than any single line, but still inductive."],
        "fuw": "What does Pell conclude, and how many separate pieces of evidence does he offer?", "fur": "Three lines of evidence, each independent. Why is convergent evidence stronger than a single chain?",
        "npc": "Pell is meticulous, excited by discoveries, and builds cases carefully.", "seed": "I believe this manuscript is the real thing. Let me show you why.", "res": "Player's analysis leads to a forgery detection quest.",
        "src": "PHIL 201 lecture notes 1.2, 1.4"
    },
    # 42 - Healer description
    {
        "ctx": a11_extra[11]["ctx"], "text": a11_extra[11]["text"], "spk": a11_extra[11]["spk"],
        "pname": "Clinical description, not argument",
        "pdesc": "Tam is listing symptoms without drawing a conclusion or arguing for a diagnosis. This is descriptive reporting.",
        "formal": "No argument structure — symptom inventory.",
        "why_right": "Tam presents observations without concluding anything. No diagnosis is offered or supported. This is a clinical description awaiting analysis.",
        "related": ["A1.1", "A1.6"],
        "counter": "If Tam had said 'these symptoms suggest scarlet fever,' that would add a conclusion and create an argument.",
        "prompt": "Healer Tam is describing a patient. Is there an argument in this description?",
        "rubric": ["Player treats symptom lists as arguments.", "Player unsure.", "Player says no but cannot explain.", "Player identifies this as description without conclusion.", "Player notes that adding a diagnostic conclusion would create an argument."],
        "fuw": "Does Tam conclude anything from these symptoms? Or is she just listing what she observes?", "fur": "Right. Raw observations are data, not arguments. What would Tam need to add to make this an argument?",
        "npc": "Tam is clinical, precise, and speaks in medical terms.", "seed": "Let me walk you through the presenting symptoms.", "res": "Player must use the symptoms to construct their own diagnostic argument.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 43 - Judge explanation
    {
        "ctx": a11_extra[12]["ctx"], "text": a11_extra[12]["text"], "spk": a11_extra[12]["spk"],
        "pname": "Explanation of an accepted outcome",
        "pdesc": "The winner has already been announced. Oria is explaining why the ram won — providing reasons for an already-accepted conclusion. 'Because' here introduces a causal/justificatory explanation.",
        "formal": "X because Y (explanation of accepted fact).",
        "why_right": "The conclusion (the Blackmere ram won) is already accepted. Oria is explaining the reasons behind the decision, not arguing that the ram should have won.",
        "related": ["A1.6", "A1.1"],
        "counter": "If someone contested the result and Oria used the same words to defend it, the speech would function as an argument. Context determines function.",
        "prompt": "Judge Oria uses 'because.' Is she making an argument or explaining a decision?",
        "rubric": ["Player assumes 'because' always means argument.", "Player unsure.", "Player identifies explanation but cannot articulate criterion.", "Player notes the decision is already made — Oria is explaining, not arguing.", "Player explains how context determines whether the same words function as argument or explanation."],
        "fuw": "Has the winner already been decided? If so, is Oria convincing you it should have won, or telling you why it did win?", "fur": "Excellent. Same words, different function depending on whether the conclusion is in dispute. Can you create a scenario where this becomes an argument?",
        "npc": "Oria is fair, thorough, and takes judging seriously.", "seed": "Let me explain how we reached our decision. Transparency is important.", "res": "Player's understanding leads to a judging fairness challenge.",
        "src": "PHIL 201 lecture notes 1.3"
    },
    # 44 - Customs verification
    {
        "ctx": a11_extra[13]["ctx"], "text": a11_extra[13]["text"], "spk": a11_extra[13]["spk"],
        "pname": "Verification report, not argument",
        "pdesc": "Henn is confirming a match between a document and reality. This is verification, not argumentation. No disputed conclusion is being supported.",
        "formal": "No argument structure — verification of correspondence.",
        "why_right": "Henn is checking a manifest against cargo and confirming they match. There is no dispute, no premises supporting a contested conclusion.",
        "related": ["A1.1"],
        "counter": "If Henn found a discrepancy and said 'The manifest says twenty barrels, but I count only eighteen, therefore you are smuggling,' that would be an argument.",
        "prompt": "Official Henn checks the cargo. Is he making an argument?",
        "rubric": ["Player treats verification as argument.", "Player unsure.", "Player says no but cannot explain.", "Player identifies this as routine verification with no disputed conclusion.", "Player explains the distinction and constructs what an argument version would look like."],
        "fuw": "Is Henn trying to prove something, or confirming that two things match?", "fur": "Right. What if the counts did not match? Would the same structure then contain an argument?",
        "npc": "Henn is bureaucratic, efficient, and speaks in procedural language.", "seed": "Step forward. Manifest, please. Let me verify the count.", "res": "A smuggling investigation quest follows where arguments about discrepancies arise.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 45 - General argument
    {
        "ctx": a11_extra[14]["ctx"], "text": a11_extra[14]["text"], "spk": a11_extra[14]["spk"],
        "pname": "Argument with multiple tactical premises",
        "pdesc": "Rath argues against a frontal assault using three tactical premises (high ground, archer sightlines, numerical disadvantage) to support the conclusion that the assault cannot succeed.",
        "formal": "P1 (enemy holds high ground), P2 (archers have clear sightlines), P3 (outnumbered 2:1). C (frontal assault cannot succeed).",
        "why_right": "Rath is arguing against a proposed strategy. His conclusion is in dispute (others proposed the assault), and he supports it with tactical evidence.",
        "related": ["A1.2", "A1.7"],
        "counter": "Each premise independently weakens the case for assault. Together they form a strong convergent argument.",
        "prompt": "General Rath opposes the assault. Is he making an argument? What evidence does he cite?",
        "rubric": ["Player does not see an argument.", "Player senses reasoning.", "Player finds conclusion but not all premises.", "Player identifies all three premises and the conclusion.", "Player identifies the convergent structure and evaluates whether the premises are sufficient."],
        "fuw": "What does Rath conclude, and what tactical facts does he cite?", "fur": "Good. Three independent tactical reasons against the assault. Is there any scenario where these factors would not matter?",
        "npc": "Rath is stern, experienced, and speaks from battlefield knowledge.", "seed": "I have seen assaults like this before. They do not end well. Let me explain.", "res": "Player's analysis leads to a tactical planning challenge.",
        "src": "PHIL 201 lecture notes 1.2"
    },
    # 46 - Monk prayer
    {
        "ctx": a11_extra[15]["ctx"], "text": a11_extra[15]["text"], "spk": a11_extra[15]["spk"],
        "pname": "Prayer/wish, not argument",
        "pdesc": "A prayer expresses wishes directed at a deity. These are performative utterances, not statements that can be true or false.",
        "formal": "No argument structure — performative prayer.",
        "why_right": "'Grant us wisdom' is a request directed at a divine entity. It cannot be true or false and therefore cannot be a premise or conclusion.",
        "related": ["A1.1"],
        "counter": "A prayer can contain an argument ('Grant us victory, for our cause is just' embeds a reason). But this prayer does not.",
        "prompt": "Brother Aldus is praying. Is there an argument in his prayer?",
        "rubric": ["Player treats prayers as arguments.", "Player unsure.", "Player says no but cannot explain.", "Player identifies prayers as performative, non-truth-functional.", "Player explains performative speech and notes when prayers could contain arguments."],
        "fuw": "Can 'grant us wisdom' be true or false? If not, what kind of speech is this?", "fur": "Right. But what if the monk said 'grant us victory, for our cause is just'? Would that contain an argument?",
        "npc": "Serene, contemplative, speaks slowly.", "seed": "Kneel with me, if you will. The gods hear all who approach with sincerity.", "res": "Discussion of performative speech leads to a philosophy side-quest.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 47 - Enchanter explanation
    {
        "ctx": a11_extra[16]["ctx"], "text": a11_extra[16]["text"], "spk": a11_extra[16]["spk"],
        "pname": "Explanation of a known failure",
        "pdesc": "Rilla is explaining why the charm broke — an observed fact. She traces the causal chain from the wrong inscription direction to the repulsion effect. This is a causal explanation.",
        "formal": "X happened because Y caused Z (causal explanation).",
        "why_right": "The failure is already observed. Rilla explains the mechanism, not argues that it failed. 'Because' introduces a causal account.",
        "related": ["A1.6", "A1.1"],
        "counter": "If someone denied the charm failed and Rilla needed to prove it, her words could function as an argument. But the failure is evident.",
        "prompt": "Enchanter Rilla uses 'because' and 'which is why.' Is she arguing or explaining?",
        "rubric": ["Player assumes any 'because' is argumentative.", "Player unsure.", "Player identifies explanation but cannot articulate criterion.", "Player notes the failure is observed — Rilla explains the cause, not argues for the effect.", "Player explains how the same words could function as argument or explanation depending on context."],
        "fuw": "Does anyone doubt that the charm broke? If not, what is Rilla doing with her 'because'?", "fur": "Good. The causal explanation reveals the mechanism. If you wanted to prevent this in the future, how would you turn Rilla's explanation into an argument?",
        "npc": "Rilla is analytical, calm, and speaks in cause-effect chains.", "seed": "Here is what went wrong. I traced the failure to its root cause.", "res": "Player learns enchanting principles from the explanation.",
        "src": "PHIL 201 lecture notes 1.3"
    },
    # 48 - Street philosopher questions
    {
        "ctx": a11_extra[17]["ctx"], "text": a11_extra[17]["text"], "spk": a11_extra[17]["spk"],
        "pname": "Premises presented as questions — prompting, not arguing",
        "pdesc": "The philosopher gives two premises ('all mortals die,' 'you are mortal') but poses the conclusion as a question rather than asserting it. He is prompting the listener to complete the argument, not making the argument himself.",
        "formal": "P1 (all mortals die), P2 (you are mortal). C? (the philosopher asks the listener to supply the conclusion).",
        "why_right": "Interestingly, the premises are stated, but the conclusion is solicited rather than asserted. The argument is incomplete as presented — the philosopher is teaching the listener to draw conclusions, not asserting one himself.",
        "related": ["A1.2", "A1.3"],
        "counter": "The argument is implied and the listener can complete it. But technically, the philosopher has not made a complete argument — he has supplied premises and asked for a conclusion.",
        "prompt": "The philosopher gives you two statements and asks 'what follows?' Is this an argument?",
        "rubric": ["Player thinks this is a complete argument.", "Player is confused by the question format.", "Player notes the question but does not analyze the incomplete structure.", "Player identifies that the premises are stated but the conclusion is posed as a question — the argument is incomplete.", "Player explains that the philosopher is using the Socratic method — providing premises and prompting the listener to draw the conclusion — and can supply the missing conclusion."],
        "fuw": "The philosopher gives you premises but does not state a conclusion. Is that a complete argument? What is he asking you to do?", "fur": "He is using the Socratic method — giving you the pieces and asking you to assemble them. Can you state the conclusion that follows from his premises?",
        "npc": "Playful, provocative, speaks in riddles and leading questions.", "seed": "Ah, a thinker! Let me give you something to chew on. Answer me this.", "res": "Completing the syllogism correctly earns entry to the philosopher's private study group.",
        "src": "PHIL 201 lecture notes 1.1-1.2"
    },
    # 49 - Gambler invitation
    {
        "ctx": a11_extra[18]["ctx"], "text": a11_extra[18]["text"], "spk": a11_extra[18]["spk"],
        "pname": "Social invitation, not argument",
        "pdesc": "Finch is making a social invitation using flattery and enticement. There are no premises supporting a conclusion — just an appeal to play.",
        "formal": "No argument structure — social invitation with flattery.",
        "why_right": "Finch is not trying to prove that something is true. He is trying to get you to do something through enticement. 'The stakes are low' might sound like a reason, but it functions more as reassurance than a premise in an argument.",
        "related": ["A1.1"],
        "counter": "One could reconstruct a weak argument: 'You should play because the stakes are low and the ale is good.' But as stated, this is closer to an invitation than an argument.",
        "prompt": "Finch is inviting you to play cards. Is there an argument here?",
        "rubric": ["Player treats invitations as arguments.", "Player unsure.", "Player says no but cannot explain.", "Player identifies this as an invitation/enticement, not an argument.", "Player explains the distinction and notes the borderline case of 'stakes are low' as a pseudo-reason."],
        "fuw": "Is Finch trying to prove something is true, or is he trying to get you to do something? Are there actual reasons, or just enticements?", "fur": "Good. 'The stakes are low' sounds like a reason. Could you reconstruct this as an argument? What would the conclusion be?",
        "npc": "Finch is charming, casual, and slightly manipulative.", "seed": "Pull up a chair! No one ever regrets a friendly game of cards.", "res": "Playing the game leads to a probability reasoning challenge.",
        "src": "PHIL 201 lecture notes 1.1"
    },
    # 50 - Alderman argument
    {
        "ctx": a11_extra[19]["ctx"], "text": a11_extra[19]["text"], "spk": a11_extra[19]["spk"],
        "pname": "Argument with double 'since' and 'it is clear that'",
        "pdesc": "Drew uses 'since' twice to introduce premises and 'it is clear that' to introduce the conclusion. This is a well-marked argument for market expansion.",
        "formal": "Since P1 (30% increase in applications) and since P2 (market cannot accommodate >40 stalls), it is clear that C (expand or lose revenue).",
        "why_right": "Drew is arguing for a policy based on economic data. Both premises are marked by 'since,' and the conclusion is marked by 'it is clear that.' The claim is in dispute — not everyone agrees expansion is needed.",
        "related": ["A1.2", "A1.5"],
        "counter": "'It is clear that' is an assuring phrase that combines a conclusion indicator with rhetorical emphasis. The player should note this double function.",
        "prompt": "Alderman Drew presents data and draws a conclusion. Is this an argument? And is there anything rhetorical about how he presents it?",
        "rubric": ["Player does not identify the argument.", "Player senses reasoning.", "Player identifies the argument but not the rhetorical element.", "Player identifies both premises, the conclusion, and the indicator words.", "Player does all of the above and notes 'it is clear that' as both a conclusion indicator and an assuring phrase."],
        "fuw": "What does Drew want the council to do? What facts does he cite? And does 'it is clear that' actually provide evidence?", "fur": "Good. 'It is clear that' is both a conclusion indicator and an assuring phrase. It signals the conclusion while implying there is no room for doubt. Is that warranted here?",
        "npc": "Drew is data-driven, persuasive, and uses rhetorical emphasis.", "seed": "The numbers do not lie, councillors. Let me show you what the data says.", "res": "Player's analysis leads to an economics quest about market dynamics.",
        "src": "PHIL 201 lecture notes 1.2, 1.10"
    },
]

for i, d in enumerate(short_a11_full, 31):
    records.append(build_a11(i, d))

print(f"A1.1 done: {len(records)} records")

# Write checkpoint
with open(OUTPUT, 'w') as f:
    for r in records:
        f.write(json.dumps(r) + '\n')
print(f"Wrote {len(records)} records to {OUTPUT}")
