#!/usr/bin/env python3
"""Generate 700 synthetic training records for Dennett's thinking tools."""

import json
import random

random.seed(42)

CODES = [
    ("D1.1", "Rapoport's Rules", "good_tool"),
    ("D1.2", "Reductio ad absurdum", "good_tool"),
    ("D1.3", "Occam's Razor", "good_tool"),
    ("D1.4", "Occam's Broom", "bad_thinking"),
    ("D1.5", "Jootsing", "good_tool"),
    ("D1.6", "Deepities", "bad_thinking"),
    ("D1.7", "The 'surely' operator", "bad_thinking"),
    ("D1.8", "Goulding", "good_tool"),
    ("D2.1", "Satisficing", "good_tool"),
    ("D2.2", "The Panglossian Slide", "bad_thinking"),
    ("D2.3", "Conversation-stoppers", "dual"),
    ("D2.4", "Wolf's Dilemma", "dual"),
    ("D2.5", "The Frame Problem", "dual"),
    ("D2.6", "The Moral First Aid Manual", "good_tool"),
]

DOMAINS = [
    "workplace", "school", "healthcare", "politics", "sports",
    "cooking", "technology", "military", "legal", "parenting",
    "music", "gaming", "agriculture", "science", "retail",
    "relationships", "finance", "travel", "environment", "housing",
    "journalism", "theater", "archaeology", "maritime", "firefighting",
]

# Difficulty distribution: ~60% drill, ~30% what_if, ~10% puzzle
def get_difficulty_tier(idx):
    if idx < 30:
        return "drill"
    elif idx < 45:
        return "what_if"
    else:
        return "puzzle"

# ============================================================
# SCENARIO DATA: 50 per code, organized by code
# ============================================================

def make_record(code, label, pattern_type, seq, difficulty, scenario, structure, assessment, game_hooks, source_material):
    return {
        "id": f"{code}-DF{seq:04d}",
        "taxonomy_code": code,
        "taxonomy_label": label,
        "track": "dennett_tools",
        "pattern_type": pattern_type,
        "difficulty_tier": difficulty,
        "scenario": scenario,
        "structure": structure,
        "assessment": assessment,
        "game_hooks": game_hooks,
        "source": {
            "type": "synthetic_verified",
            "source_material": source_material,
            "original_id": None,
        },
    }


# ============================================================
# D1.1 — Rapoport's Rules
# ============================================================
D1_1_SCENARIOS = [
    # 1 - workplace
    {
        "scenario": {
            "context": "The player enters the offices of a trading company where two managers, Heston and Vari, are locked in a dispute about whether to expand into the eastern markets. Heston favors expansion; Vari opposes it. The senior partner, Maela, has been asked to moderate.",
            "text": "Maela raises a hand. 'Before I give my view, let me restate Heston's proposal as fairly as I can. Heston, you are arguing that the eastern markets have lower competition, that our current product line matches eastern demand, and that the upfront cost of expansion will be recouped within three seasons. Is that right?' Heston nods. 'Better than I said it, actually.' Maela continues: 'And I agree with you on two points. Eastern competition is lower — the Guild survey confirms it. And our wool exports do match their climate needs. I also learned something from your cost projections I had not considered: the shipping route through Port Ghael is cheaper than I assumed. But here is where I part ways. Your timeline assumes no tariff changes, and the Eastern Council has raised tariffs twice in three years. Expansion is worth pursuing, but not on a three-season payback assumption.'",
            "speaker_context": "Maela is a senior partner who moderates disputes with Rapoport's protocol: restate, agree, learn, then criticize.",
        },
        "structure": {
            "pattern_name": "Rapoport's Rules",
            "pattern_description": "Maela follows the four-step protocol: (1) restates Heston's position until he endorses it, (2) lists genuine agreements, (3) acknowledges learning from the shipping cost data, (4) only then offers her criticism about tariff risk.",
            "formal_form": "Before asserting NOT-P: (1) restate P so advocate endorses; (2) enumerate shared commitments; (3) identify corrected beliefs; (4) then criticize.",
            "why_wrong": None,
            "why_right": "Maela's approach keeps Heston engaged even when she disagrees. He stays at the table because she demonstrated genuine understanding of his position before challenging it.",
            "related_patterns": ["A1.4", "D1.2"],
            "counterpoint": "The protocol can be time-consuming. In urgent situations, the four steps may not be feasible — but skipping them risks turning disagreement into hostility.",
        },
        "assessment": {
            "identification_prompt": "Maela disagrees with Heston's timeline, but he does not become defensive. What is Maela doing before she criticizes, and why does each step matter?",
            "rubric": [
                {"level": 0, "description": "Player sees ordinary persuasion, no deliberate structure."},
                {"level": 1, "description": "Player notices Maela is polite but cannot identify distinct steps."},
                {"level": 2, "description": "Player identifies two of the four steps."},
                {"level": 3, "description": "Player identifies all four steps in order."},
                {"level": 4, "description": "Player identifies all four steps, explains the sequential logic, and can say what breaks if a step is insincere."},
            ],
            "follow_up_if_wrong": "Look at what Maela does before she says 'here is where I part ways.' She does four distinct things. What is the very first thing she does with Heston's argument?",
            "follow_up_if_right": "Suppose Maela skipped step 3 — admitting the shipping cost surprised her. Would Heston still trust her criticism? Why does conceding a learning moment matter?",
        },
        "game_hooks": {
            "npc_personality": "Maela is calm, measured, and forensic. She listens more than she speaks and treats every dispute like a negotiation, not a battle.",
            "npc_dialogue_seed": "Before I tell you what I think is wrong with this plan, I want to make sure I can say what is right about it better than the person who proposed it.",
            "resolution_path": "If the player recognizes the protocol, Maela offers to teach the four-step method, unlocking it as a dialogue tool.",
        },
        "source_material": "Dennett Intuition Pumps + PHIL 201 lecture notes",
    },
    # 2 - school
    {
        "scenario": {
            "context": "The player enters a village school where two teachers, Mr. Birch and Miss Tallow, are arguing about discipline methods. Birch favors strict rules and consequences; Tallow favors restorative conversations. The headmistress, Dame Aldren, steps in.",
            "text": "Dame Aldren nods at Birch. 'Let me make sure I understand your position, Birch. You believe that clear rules and consistent consequences give children a sense of security. That without them, the classroom becomes chaotic, and the children who most need structure are the ones who suffer. Is that a fair summary?' Birch blinks. 'Yes — that is exactly it.' Aldren: 'And I agree that structure matters. I have seen classrooms without it, and you are right: the most vulnerable children lose the most. I also learned from your logbook that the number of repeated infractions dropped after you introduced the warning system — I had assumed otherwise.' She pauses. 'But your system does not distinguish between a child who breaks a rule out of defiance and one who breaks it out of distress. Tallow's restorative approach handles that distinction. I propose we combine both.'",
            "speaker_context": "Dame Aldren applies Rapoport's Rules to mediate between two educational philosophies, restating, agreeing, learning, then offering a synthesis.",
        },
        "structure": {
            "pattern_name": "Rapoport's Rules",
            "pattern_description": "Aldren restates Birch's position until he endorses it, lists genuine agreements about structure, concedes the logbook data corrected her assumption, then offers criticism only after these steps.",
            "formal_form": "Before asserting NOT-P: (1) restate P; (2) enumerate shared commitments; (3) acknowledge corrected belief; (4) criticize.",
            "why_wrong": None,
            "why_right": "Birch does not become defensive because Aldren demonstrated she genuinely understands and partially agrees with him before diverging.",
            "related_patterns": ["A1.4", "D2.6"],
            "counterpoint": "Some might see step 3 as performative. It only works if the concession is genuine — a faked learning moment will be detected.",
        },
        "assessment": {
            "identification_prompt": "Dame Aldren manages to criticize Birch's system without making him defensive. What specific steps does she take before offering criticism?",
            "rubric": [
                {"level": 0, "description": "Player sees no deliberate structure."},
                {"level": 1, "description": "Player notices she is kind but cannot identify steps."},
                {"level": 2, "description": "Player identifies restating and agreeing but misses learning."},
                {"level": 3, "description": "Player identifies all four steps in sequence."},
                {"level": 4, "description": "Player identifies all four steps, explains why order matters, and notes the risk of insincere steps."},
            ],
            "follow_up_if_wrong": "What does Aldren do with Birch's argument before she says anything about Tallow's approach? Start with her very first sentence.",
            "follow_up_if_right": "Could Aldren have led with her criticism and still achieved the same result? What would change?",
        },
        "game_hooks": {
            "npc_personality": "Dame Aldren is warm but precise, a lifelong educator who treats arguments the way she treats children — with patience and structure.",
            "npc_dialogue_seed": "I never criticize a position I cannot restate better than the person who holds it. That is not courtesy — it is quality control.",
            "resolution_path": "Player learns to apply the four-step method in future NPC disputes about pedagogy.",
        },
        "source_material": "Dennett Intuition Pumps + PHIL 201 lecture notes",
    },
    # 3 - healthcare
    {
        "scenario": {
            "context": "The player visits a hospital where Dr. Voss and Nurse Practitioner Lewin disagree about patient discharge timing. Voss wants to discharge patients earlier to free beds; Lewin argues patients are being sent home too soon. The hospital director, Administrator Quinn, mediates.",
            "text": "Quinn addresses Voss first. 'Dr. Voss, let me restate your position. You believe that keeping patients longer than medically necessary increases their risk of hospital-acquired infections, blocks bed access for incoming critical cases, and drives up costs without improving outcomes. You are not saying patients should be discharged prematurely — you are saying the threshold for medical necessity has been set too conservatively. Correct?' Voss: 'Precisely.' Quinn: 'I agree that hospital-acquired infections are a genuine risk — the data on that is clear. And your audit showed that twelve percent of extended stays had no documented medical justification. I did not know that number, and it changes my priors.' She turns. 'However, Lewin's readmission data shows that patients discharged under the accelerated protocol return within seventy-two hours at double the baseline rate. That suggests the threshold may not be too conservative — it may be accurately set, and the accelerated protocol is cutting into it.'",
            "speaker_context": "Quinn applies Rapoport's Rules in a healthcare management dispute.",
        },
        "structure": {
            "pattern_name": "Rapoport's Rules",
            "pattern_description": "Quinn restates Voss's position charitably, agrees on infection risk and the audit finding, concedes the twelve percent figure changed her view, then offers a data-driven criticism.",
            "formal_form": "Before asserting NOT-P: (1) restate P so advocate endorses; (2) list agreements; (3) concede learned information; (4) criticize.",
            "why_wrong": None,
            "why_right": "Quinn's approach keeps both medical professionals engaged because she demonstrates understanding of their evidence before challenging their conclusions.",
            "related_patterns": ["A1.4", "D1.8"],
            "counterpoint": "In emergencies, the protocol must be abbreviated. But most policy disagreements allow time for all four steps.",
        },
        "assessment": {
            "identification_prompt": "Quinn disagrees with Dr. Voss's discharge policy, but Voss remains engaged. What is Quinn doing structurally before she offers criticism?",
            "rubric": [
                {"level": 0, "description": "Player sees ordinary mediation."},
                {"level": 1, "description": "Player notices Quinn is diplomatic but cannot name the steps."},
                {"level": 2, "description": "Player identifies restating and agreeing."},
                {"level": 3, "description": "Player identifies all four Rapoport steps."},
                {"level": 4, "description": "Player identifies all four steps and explains why the learning concession is critical for trust."},
            ],
            "follow_up_if_wrong": "Count the things Quinn does before saying 'however.' Each one serves a specific purpose.",
            "follow_up_if_right": "What if Quinn's concession about the audit data was insincere? How would that change the dynamic?",
        },
        "game_hooks": {
            "npc_personality": "Quinn is analytical and empathetic, a rare combination. She uses data the way others use rhetoric.",
            "npc_dialogue_seed": "The first step in any disagreement is making sure I can state the other person's case so well they would hire me as their advocate.",
            "resolution_path": "Player earns a 'Charitable Restatement' dialogue tool for future medical encounters.",
        },
        "source_material": "Dennett Intuition Pumps + PHIL 201 lecture notes",
    },
    # 4 - politics
    {
        "scenario": {
            "context": "The player enters a town hall debate about whether to accept refugees from a neighboring war-torn region. Alderman Croft opposes accepting refugees, citing resource strain. Councillor Nara supports acceptance. Retired diplomat Fenn moderates.",
            "text": "Fenn addresses Croft. 'Alderman, let me restate your concern. You are not saying refugees are bad people. You are saying that Millhaven's granary is at sixty percent capacity, the clinic has one healer, and adding three hundred mouths without adding resources will harm both the refugees and the existing residents. Your opposition is practical, not moral. Fair?' Croft, surprised: 'That is exactly what I mean, and no one has put it that way before.' Fenn: 'I agree with you that the resource constraint is real. The granary numbers are verified. I also learned from your survey that the well water cannot support more than fifty additional people without a new bore — I had underestimated that.' Now Fenn sharpens. 'But your proposal to refuse all refugees assumes three hundred arrive at once. Nara's phased intake plan brings twenty families over six months, with each phase contingent on a resource check. Your resource objection is valid — but it argues for phased intake, not refusal.'",
            "speaker_context": "Fenn uses Rapoport's Rules to reframe a politically charged debate as a practical problem.",
        },
        "structure": {
            "pattern_name": "Rapoport's Rules",
            "pattern_description": "Fenn restates Croft's position charitably (practical, not moral), agrees on resource facts, concedes the water survey taught him something, then redirects rather than dismisses.",
            "formal_form": "Before asserting NOT-P: (1) restate P charitably; (2) agree on shared facts; (3) concede learned data; (4) criticize specifically.",
            "why_wrong": None,
            "why_right": "By restating Croft's concern as practical rather than xenophobic, Fenn disarms the emotional charge and makes productive disagreement possible.",
            "related_patterns": ["D2.3", "A1.4"],
            "counterpoint": "Charitable restatement can be exploited — a bad-faith actor could hide moral objections behind practical language. The restater must be attentive to this possibility.",
        },
        "assessment": {
            "identification_prompt": "Fenn manages to shift a heated political debate into a productive discussion. What technique is he using, step by step?",
            "rubric": [
                {"level": 0, "description": "Player sees standard mediation."},
                {"level": 1, "description": "Player notices Fenn is fair but cannot name steps."},
                {"level": 2, "description": "Player identifies charitable restatement and agreement."},
                {"level": 3, "description": "Player identifies all four Rapoport steps."},
                {"level": 4, "description": "Player identifies all four steps and discusses when charitable restatement could be weaponized."},
            ],
            "follow_up_if_wrong": "What is the first thing Fenn does with Croft's argument? He does not attack it or ignore it. What does he do?",
            "follow_up_if_right": "Could a bad-faith actor exploit Rapoport's Rules by pretending practical concerns are their real motivation? How would you detect that?",
        },
        "game_hooks": {
            "npc_personality": "Fenn is a retired diplomat who treats every conversation as a negotiation. Soft-spoken but precise.",
            "npc_dialogue_seed": "In thirty years of diplomacy I learned one thing: if you cannot restate your opponent's position better than they can, you do not understand it well enough to disagree.",
            "resolution_path": "Player gains 'Diplomatic Restatement' tool for political encounters.",
        },
        "source_material": "Dennett Intuition Pumps + PHIL 201 lecture notes",
    },
    # 5 - sports
    {
        "scenario": {
            "context": "The player joins a coaching debate at an athletic academy. Head Coach Maren wants to switch the team to a defensive strategy. Assistant Coach Pike insists the offensive approach is working. Athletic Director Solano mediates.",
            "text": "Solano faces Pike. 'Coach Pike, let me make sure I have your position right. You believe the offensive strategy is working because our scoring has increased thirty percent this season. The team's morale is high because players enjoy the aggressive style. And switching mid-season disrupts muscle memory and game rhythm. That is your case?' Pike: 'Couldn't have said it better.' Solano: 'I agree that morale matters — and you are right that mid-season changes carry risk. I also learned from your film analysis that our counter-attack speed has actually improved under the offensive scheme, which I had not appreciated.' He pauses. 'But Coach Maren's data shows our defensive concessions have increased forty-five percent. We are scoring more but conceding even faster. The offensive approach is not failing — but it is creating a vulnerability that opponents are learning to exploit. I suggest we keep the offensive core but add the defensive rotations Maren designed.'",
            "speaker_context": "Solano applies Rapoport's Rules in a sports strategy dispute.",
        },
        "structure": {
            "pattern_name": "Rapoport's Rules",
            "pattern_description": "Solano restates Pike's position, agrees on morale and risk, concedes the counter-attack data surprised him, then offers criticism grounded in defensive statistics.",
            "formal_form": "Before asserting NOT-P: (1) restate P; (2) agree; (3) concede learning; (4) criticize.",
            "why_wrong": None,
            "why_right": "Pike stays engaged because Solano demonstrates genuine understanding of the offensive approach before proposing modifications.",
            "related_patterns": ["D1.8", "D2.1"],
            "counterpoint": "In time-pressured game situations, the full protocol may need to be compressed. But strategic planning allows all four steps.",
        },
        "assessment": {
            "identification_prompt": "Solano proposes changes to the coaching strategy without alienating Pike. What is his method?",
            "rubric": [
                {"level": 0, "description": "Player sees ordinary compromise."},
                {"level": 1, "description": "Player notes Solano is fair but cannot identify structure."},
                {"level": 2, "description": "Player identifies two steps."},
                {"level": 3, "description": "Player identifies all four Rapoport steps."},
                {"level": 4, "description": "Player identifies all four steps and discusses when time pressure might compress the protocol."},
            ],
            "follow_up_if_wrong": "What does Solano do before he says 'but'? List every distinct step.",
            "follow_up_if_right": "In a real game, with thirty seconds on the clock, could you still use these steps? How would you compress them?",
        },
        "game_hooks": {
            "npc_personality": "Solano is a former player turned administrator who values both data and gut instinct.",
            "npc_dialogue_seed": "I learned to argue on the field: you do not convince a teammate by shouting. You convince them by showing you understand their play before suggesting a different one.",
            "resolution_path": "Player earns ability to mediate coaching disputes in future sports encounters.",
        },
        "source_material": "Dennett Intuition Pumps + PHIL 201 lecture notes",
    },
]

# I'll now define a function to generate the full 50 scenarios for each code
# For brevity and quality, I'll write each one inline

def generate_all_records():
    records = []

    # Helper to assign domains cyclically but shuffled
    def domain_sequence(n=50):
        doms = []
        base = list(DOMAINS)
        random.shuffle(base)
        while len(doms) < n:
            batch = list(DOMAINS)
            random.shuffle(batch)
            doms.extend(batch)
        return doms[:n]

    # ================================================================
    # D1.1 — Rapoport's Rules (good_tool) x 50
    # ================================================================
    d1_1_domains = domain_sequence()
    d1_1_data = []

    # I'll generate the scenarios programmatically with variation
    d1_1_scenarios_data = [
        # (domain, context, text, speaker_context, npc_personality, npc_seed, resolution, source_extra, tier_override)
        ("workplace",
         "The player enters a trading company where managers Heston and Vari dispute eastern market expansion. Senior partner Maela moderates.",
         "Maela raises a hand. 'Let me restate Heston's proposal fairly. You are arguing that eastern markets have lower competition, our wool exports match eastern demand, and the cost recoups within three seasons. Correct?' Heston: 'Better than I said it.' Maela: 'I agree on two points — eastern competition is lower and our wool matches their climate. I also learned from your cost projections that the Port Ghael shipping route is cheaper than I assumed.' She pauses. 'But your timeline assumes no tariff changes, and the Eastern Council has raised tariffs twice in three years. Expansion is worth pursuing, but not on a three-season payback assumption.'",
         "Maela is a senior partner using Rapoport's Rules to mediate a trade dispute.",
         "Calm, measured, forensic. Listens more than she speaks.",
         "Before I tell you what is wrong with this plan, I want to state what is right about it better than the person who proposed it.",
         "Player learns the four-step method as a dialogue tool for trade disputes.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("school",
         "Two teachers argue about classroom discipline. Birch favors strict rules; Tallow favors restorative conversations. Headmistress Dame Aldren mediates.",
         "Dame Aldren: 'Birch, you believe clear rules and consistent consequences give children security. Without them, the classroom is chaotic and the most vulnerable children suffer. Fair?' Birch: 'Yes, exactly.' Aldren: 'I agree structure matters — I have seen classrooms without it. And your logbook shows repeated infractions dropped after the warning system. I had assumed otherwise.' She pauses. 'But your system does not distinguish defiance from distress. Tallow's restorative approach handles that distinction. I propose we combine both.'",
         "Dame Aldren applies Rapoport's Rules in an educational dispute.",
         "Warm but precise, a lifelong educator.",
         "I never criticize a position I cannot restate better than the person who holds it.",
         "Player gains charitable restatement tool for educational encounters.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("healthcare",
         "Dr. Voss and Nurse Lewin disagree about patient discharge timing. Hospital administrator Quinn mediates.",
         "Quinn: 'Dr. Voss, you believe keeping patients longer than medically necessary increases infection risk, blocks beds, and drives up costs. You are not saying discharge prematurely — you are saying the necessity threshold is too conservative. Correct?' Voss: 'Precisely.' Quinn: 'I agree infection risk is real. Your audit showed twelve percent of stays had no documented justification — I did not know that.' She turns. 'However, Lewin's data shows patients discharged under the accelerated protocol return within seventy-two hours at double the baseline rate. The threshold may be accurately set.'",
         "Quinn applies Rapoport's Rules in a healthcare management dispute.",
         "Analytical and empathetic. Uses data the way others use rhetoric.",
         "The first step in any disagreement is making sure I can state the other person's case so well they would hire me.",
         "Player earns charitable restatement tool for medical encounters.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("politics",
         "A town hall debate about accepting refugees. Alderman Croft opposes on resource grounds. Retired diplomat Fenn moderates.",
         "Fenn: 'Alderman, your opposition is practical, not moral. Millhaven's granary is at sixty percent, the clinic has one healer, and adding three hundred mouths without resources harms everyone. Fair?' Croft: 'That is exactly what I mean.' Fenn: 'The resource constraint is real. I also learned from your survey that the well cannot support fifty additional people — I underestimated that.' He sharpens. 'But your proposal assumes all three hundred arrive at once. Nara's phased intake brings twenty families over six months with resource checks. Your objection argues for phased intake, not refusal.'",
         "Fenn uses Rapoport's Rules to reframe a politically charged debate.",
         "Retired diplomat. Treats every conversation as a negotiation.",
         "If you cannot restate your opponent's position better than they can, you do not understand it enough to disagree.",
         "Player gains diplomatic restatement tool.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("sports",
         "Head Coach Maren wants defensive strategy. Assistant Coach Pike insists on offense. Athletic Director Solano mediates.",
         "Solano: 'Coach Pike, you believe the offensive strategy works — scoring is up thirty percent, morale is high, and switching mid-season disrupts rhythm. Fair?' Pike: 'Couldn't have said it better.' Solano: 'I agree morale matters. Your film analysis shows counter-attack speed improved — I had not appreciated that.' He pauses. 'But Maren's data shows defensive concessions up forty-five percent. We are scoring more but conceding faster. I suggest keeping the offensive core but adding Maren's defensive rotations.'",
         "Solano applies Rapoport's Rules in a sports strategy dispute.",
         "Former player turned administrator. Values both data and instinct.",
         "You do not convince a teammate by shouting. You convince them by showing you understand their play.",
         "Player earns mediation skill for coaching disputes.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("cooking",
         "The player enters a restaurant kitchen where Chef Damaris and Sous Chef Kel argue about whether to modernize the menu. Owner Petra mediates.",
         "Petra: 'Kel, let me restate your case. You believe the traditional menu is our identity, that loyal customers come for the classics, and that changing recipes risks alienating the base that keeps us profitable. Correct?' Kel: 'That is it exactly.' Petra: 'I agree the classics are our foundation. And I learned from your customer survey that seventy percent of regulars order the same three dishes — I assumed it was closer to half.' She nods. 'But Damaris's tasting data shows new diners under thirty leave without ordering if the menu looks dated. We are keeping old customers but not attracting new ones. I propose we keep the classics and add a seasonal section.'",
         "Petra applies Rapoport's Rules to a culinary identity dispute.",
         "Practical restaurant owner who respects both tradition and innovation.",
         "I will not tell you what is wrong with your menu until I can explain what is right about it in your own terms.",
         "Player learns to mediate creative disputes in food-related encounters.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("technology",
         "Two engineers debate whether to refactor the guild's messaging system or build a new one. Lead Architect Renn moderates.",
         "Renn: 'Thane, you want to refactor because the existing system has institutional knowledge baked in, a refactor preserves that, and a rebuild takes twice as long. Fair summary?' Thane: 'Better than I put it.' Renn: 'I agree institutional knowledge matters. And I learned from your code audit that the message routing logic is actually well-structured — I had assumed it was tangled.' She pivots. 'But the authentication layer cannot be refactored without breaking backward compatibility. Sera's proposal for a new authentication module inside the existing framework threads the needle. We refactor what works and rebuild what does not.'",
         "Renn uses Rapoport's Rules to mediate a technical architecture dispute.",
         "Precise, systematic, and fair. Treats code debates like logic problems.",
         "I do not critique code I cannot explain in the author's own terms.",
         "Player gains architectural mediation skill for tech encounters.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("military",
         "A field commander and a logistics officer disagree about supply route selection. The general mediates using Rapoport's protocol.",
         "General Voss: 'Captain Harren, you favor the mountain route because it avoids the enemy-held valley, reduces ambush risk, and your scouts confirmed the pass is clear. Correct?' Harren: 'Yes, sir.' Voss: 'I agree the valley is dangerous. And your scouts' report that the pass is clear taught me something — I had assumed the spring thaw made it impassable.' He straightens. 'But Lieutenant Kade's supply calculations show the mountain route adds four days. Our rations last three. Either we find a resupply point on the mountain route or we take the valley with proper escort. The pass being clear does not solve the food problem.'",
         "General Voss uses Rapoport's Rules in a military logistics dispute.",
         "Experienced commander who believes good leadership requires understanding subordinates' reasoning.",
         "I restate the opposing plan so well that the officer who proposed it would adopt my version.",
         "Player earns 'Tactical Restatement' for military decision encounters.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("legal",
         "Two attorneys argue about trial strategy. The senior partner mediates by restating each position before ruling.",
         "Senior Partner Vael: 'Marsh, your position is that we should focus on the contract's ambiguous clause because the jury will see it as the defendant's failure to specify terms, and juries punish ambiguity. Correct?' Marsh: 'Exactly right.' Vael: 'I agree the clause is ambiguous — the plain reading supports us. And I learned from your mock jury data that eight of ten mock jurors flagged the clause unprompted. That surprised me.' She pauses. 'But the defense has a legislative history argument that explains the ambiguity as intentional industry standard. If we lead with the clause, they will contextualize it before we can build momentum. I suggest we lead with damages and introduce the clause second.'",
         "Vael applies Rapoport's Rules in a legal strategy dispute.",
         "Meticulous, principled, and scrupulously fair even with her own team.",
         "The best cross-examination starts with restating the witness's position so well they trust you.",
         "Player gains 'Legal Restatement' tool.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("parenting",
         "Two parents disagree about screen time limits for their children. A family counselor mediates using Rapoport's protocol.",
         "Counselor Thera: 'Marc, let me restate your position. You believe moderate screen time is educational, that banning it entirely makes it forbidden fruit, and that your children's tablet use has actually improved their reading scores. Fair?' Marc: 'That is exactly right.' Thera: 'I agree that total bans can backfire. And your point about reading scores is supported by the data you showed me — I had assumed screen time was purely recreational.' She pauses. 'But Lena's concern is about the two hours after dinner, when screens replace family conversation. The issue is not screen time itself but its timing. What if screens are permitted until dinner and the evening is screen-free?'",
         "Counselor Thera applies Rapoport's Rules to a parenting dispute.",
         "Patient, evidence-based, and skilled at reframing binary debates as design problems.",
         "I restate each parent's position until they say 'yes, that is what I mean' before I suggest anything.",
         "Player learns to apply the protocol in family and relationship disputes.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("music",
         "Band members argue about creative direction. The manager restates the guitarist's position before offering criticism.",
         "Manager Dev: 'Risa, your position is that the band should stay acoustic because that is your sound, your audience expects it, and your streaming numbers prove it works. Fair?' Risa: 'Yes.' Dev: 'I agree the acoustic identity is valuable. And I learned from your playlist data that acoustic tracks have twice the save rate — I had underestimated that.' He pauses. 'But Tomek's point is that live bookings have dropped because venues want louder acts. The acoustic identity is not the problem — the live revenue is. What if we keep the recorded sound acoustic and add amplified arrangements for live shows only?'",
         "Dev applies Rapoport's Rules to a creative direction dispute.",
         "Diplomatic, industry-savvy, and good at separating artistic identity from business problems.",
         "Before I suggest any change to the sound, I will describe the current sound better than the artist can.",
         "Player gains ability to mediate creative disputes.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("gaming",
         "Game designers argue about difficulty settings. The lead designer restates the accessibility advocate's position before offering criticism.",
         "Lead Designer Mora: 'Jan, your position is that difficulty options expand the player base, that accessibility features do not diminish the core experience, and that your user research shows forty percent of players quit at the first boss. Correct?' Jan: 'Exactly.' Mora: 'I agree that forty percent quit rate is a problem — I had assumed it was lower. And your data on assist mode engagement taught me that players who use assist mode often graduate to standard — I did not expect that.' She pivots. 'But the narrative tension in the early game depends on the boss feeling genuinely threatening. I propose we keep the difficulty but add a practice room before the boss encounter, so players can learn the mechanics without repeated failure.'",
         "Mora uses Rapoport's Rules to mediate a game design dispute.",
         "Thorough, data-driven, and passionate about both challenge and accessibility.",
         "I will not dismiss your feature request until I can explain why you proposed it better than you did.",
         "Player gains design mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("agriculture",
         "Farmers argue about crop rotation vs. monoculture. An agricultural advisor restates the monoculture farmer's position before offering criticism.",
         "Advisor Brynn: 'Garet, you favor monoculture because your corn yields are the highest in the county, rotation requires equipment you do not have, and your buyers want consistent supply. Fair?' Garet: 'That is exactly right.' Brynn: 'I agree your yields are impressive. And I learned from your soil tests that your particular plot has unusually high nitrogen retention — I had assumed monoculture had depleted it.' She pauses. 'But the county-wide data shows monoculture plots averaging forty percent yield decline over ten years. Your plot is the exception, not the rule, and even your nitrogen levels have dropped eight percent since the last test. Rotation is not about this year — it is about year ten.'",
         "Brynn applies Rapoport's Rules to an agricultural practice dispute.",
         "Practical, data-oriented, and respectful of farming experience.",
         "I do not tell a farmer to change their practice until I can explain why their current practice makes sense.",
         "Player gains agricultural mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("science",
         "Two researchers disagree about experimental methodology. The lab director restates the junior researcher's defense before offering criticism.",
         "Director Elara: 'Dr. Pell, your position is that the double-blind protocol is unnecessary for this study because the measurement is automated, human bias cannot affect instrument readings, and the extra complexity adds six months. Fair?' Pell: 'Yes, exactly.' Elara: 'I agree that automated measurement reduces certain biases. And I learned from your protocol review that the calibration process is more rigorous than I assumed — you have eliminated several sources of error I was concerned about.' She nods. 'But the bias enters at the sample selection stage, not the measurement stage. The person choosing which samples to test knows the hypothesis. The instruments are blind, but the sample selection is not. A single-blind protocol at the selection stage would add one month, not six.'",
         "Elara applies Rapoport's Rules in a scientific methodology dispute.",
         "Rigorous, fair-minded, and committed to the collaborative nature of scientific debate.",
         "I do not reject a methodology until I can present its strongest case.",
         "Player learns to apply charitable restatement in scientific discussions.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("retail",
         "Store managers argue about return policy. The regional director restates the strict-policy advocate's case before offering criticism.",
         "Director Vann: 'Max, you argue that our liberal return policy is being exploited, that serial returners cost us fourteen percent of margin, and that tightening the window from sixty to thirty days would cut abuse while keeping honest customers. Fair?' Max: 'That is it.' Vann: 'I agree that serial returners are a problem — your data is compelling. And I learned from your audit that returns peak at day forty-five, not day twenty as I assumed. That changes the calculus.' She pivots. 'But the customer satisfaction survey shows that sixty-day returns are our top-rated feature. A blanket thirty-day window punishes the ninety percent who return legitimately. I propose we keep sixty days for first-time returns and add verification for serial returners.'",
         "Vann applies Rapoport's Rules in a retail policy dispute.",
         "Data-driven, customer-focused, and skilled at finding middle ground.",
         "I restate your policy before I critique it, so you know I have done my homework.",
         "Player gains retail dispute mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("relationships",
         "A couple argues about how to handle visiting in-laws. A therapist restates each partner's position using Rapoport's protocol.",
         "Therapist Wren: 'Sasha, let me restate. You believe weekly visits maintain family bonds, that your parents feel excluded when visits are less frequent, and that your partner's resistance feels like rejection of your family. Fair?' Sasha: 'Yes, that is what I have been trying to say.' Wren: 'I agree that family bonds require maintenance. And I learned from your description that your parents recently lost a close friend — that context matters, and I had not considered it.' She turns. 'But Dion's point is that weekly visits leave no time for the two of you. The issue is not frequency versus family — it is how to honor both needs. What if two visits per month are in-person and two are video calls?'",
         "Wren applies Rapoport's Rules to a relationship conflict.",
         "Warm, precise, and committed to making each person feel heard before any suggestion.",
         "I do not propose solutions until each person says 'yes, that is what I mean.'",
         "Player learns to apply the protocol in personal relationship disputes.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("finance",
         "Two investment advisors disagree about risk allocation for a client's retirement portfolio. The senior advisor restates the aggressive strategy advocate's case.",
         "Senior Advisor Thorn: 'Jess, your position is that the client has twenty-five years to retirement, historical returns favor equities over that horizon, and the conservative allocation locks in lower returns that fail to keep pace with inflation. Correct?' Jess: 'Exactly.' Thorn: 'I agree the time horizon favors growth. And I learned from your back-test that the equity portfolio outperformed in ninety-two percent of twenty-five-year windows — a higher rate than I expected.' He pauses. 'But the client told us her risk tolerance is low. She will panic-sell in the first downturn. An optimal allocation she cannot stick with is worse than a suboptimal one she can. I propose sixty-forty with an annual rebalance conversation.'",
         "Thorn applies Rapoport's Rules in a financial planning dispute.",
         "Measured, client-centered, and skilled at balancing theoretical optimality with human behavior.",
         "I restate the aggressive case until its advocate endorses my version. Then I explain why the client's psychology overrides the math.",
         "Player gains financial mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("travel",
         "Tour guides argue about itinerary design. The company owner restates the adventure guide's position before offering criticism.",
         "Owner Dela: 'Cruz, you want more off-trail excursions because they create memorable experiences, your client ratings are the highest for adventure tours, and the current itinerary is too predictable. Fair?' Cruz: 'That is it.' Dela: 'I agree predictability is a problem for the adventure segment. And I learned from your data that adventure clients book repeat trips at triple the rate — I had no idea.' She pivots. 'But safety incidents on off-trail excursions have increased. Two injuries last quarter. Your ratings are high among those who completed the trip, but the drop-out rate is twenty percent. I propose we add the off-trail options as elective add-ons with proper briefings rather than mandatory itinerary changes.'",
         "Dela applies Rapoport's Rules in a travel business dispute.",
         "Entrepreneurial, safety-conscious, and respectful of guide expertise.",
         "I do not override a guide's proposal until I can explain its strengths in their terms.",
         "Player gains itinerary mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("environment",
         "Conservationists argue about rewilding strategy. The program director restates the gradual approach advocate's case before offering criticism.",
         "Director Ash: 'Wren, your position is that gradual rewilding over ten years gives ecosystems time to adapt, that rapid reintroduction caused failures in the Thornvale project, and that local farmers need time to adjust. Fair?' Wren: 'That is exactly my concern.' Ash: 'I agree that Thornvale was a cautionary tale. And I learned from your soil recovery data that the mycorrhizal networks need at least three years to re-establish — I had assumed one year.' He pauses. 'But the endangered hawk population cannot wait ten years. We lose the breeding pairs in five. I propose a two-phase plan: immediate protected corridors for the hawks, with gradual rewilding for everything else.'",
         "Ash applies Rapoport's Rules in a conservation strategy dispute.",
         "Deeply knowledgeable, patient, and willing to learn from field staff.",
         "I restate the cautious position before I argue for urgency. Otherwise urgency sounds like recklessness.",
         "Player gains conservation mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("housing",
         "Community members argue about affordable housing design. The city planner restates the density opponent's case before offering criticism.",
         "Planner Kora: 'Mr. Hale, you oppose the high-density proposal because the current infrastructure — roads, water, schools — cannot handle triple the residents. You are not against affordable housing; you are against building it without the infrastructure to support it. Fair?' Hale: 'That is exactly what I have been saying.' Kora: 'I agree the infrastructure gap is real. And your traffic study showed the intersection at Elm would fail at current capacity plus fifty percent — I had assumed it could handle the increase.' She pivots. 'But the low-density alternative requires three times the land, which prices out the very families who need affordable housing. I propose medium-density with phased infrastructure upgrades tied to each building phase.'",
         "Kora applies Rapoport's Rules in a housing policy dispute.",
         "Data-driven urban planner who respects community concerns.",
         "I restate the opposition's case until they endorse my version. That is how I earn the right to disagree.",
         "Player gains community planning mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "drill"),

        ("journalism",
         "Editors argue about whether to publish a leaked document. The editor-in-chief restates the cautious editor's position before offering her own view.",
         "Editor-in-Chief Nadia: 'Tomás, you argue we should not publish because the source's motives are unclear, the document could be selectively leaked to manipulate us, and publishing before verification could destroy our credibility. Fair?' Tomás: 'That is exactly my concern.' Nadia: 'I agree that source motives matter — we have been burned before. And I learned from your fact-check that two of the seven claims in the document are unverifiable — I had assumed they were all checkable.' She pivots. 'But the five verifiable claims are explosive and confirmed. I propose we publish only the verified portions, disclose what we could not verify, and state clearly that the source's motives are unknown.'",
         "Nadia applies Rapoport's Rules in a journalistic ethics dispute.",
         "Sharp, principled, and committed to both public interest and factual accuracy.",
         "I do not overrule a cautious editor until I can restate their caution better than they can.",
         "Player gains editorial mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("theater",
         "A director and playwright argue about cutting a scene. The producer restates the playwright's defense before offering criticism.",
         "Producer Ellis: 'Maya, you want to keep Act Two Scene Three because it establishes the protagonist's backstory, the emotional payoff in Act Three depends on it, and audiences in workshop performances responded strongly to it. Fair?' Maya: 'Yes, that is exactly why I wrote it.' Ellis: 'I agree the emotional payoff matters. And the workshop response data you showed me was stronger than I expected — I had assumed the scene was self-indulgent.' He pauses. 'But the scene adds eighteen minutes, and the runtime is already over target. The backstory information can be woven into the existing dialogue in Scene One. What if we cut the scene but embed its emotional core into earlier moments?'",
         "Ellis applies Rapoport's Rules in a theatrical editing dispute.",
         "Commercially minded but genuinely respectful of creative vision.",
         "I never cut a scene without first explaining why it works. Then I explain why something else works better.",
         "Player gains creative mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("archaeology",
         "Archaeologists argue about excavation pace. The site director restates the slow-dig advocate's case before offering criticism.",
         "Site Director Fen: 'Dr. Marsh, your position is that we should excavate at half pace because the stratigraphy is unusually complex, that faster digs at similar sites destroyed context, and that the pottery shards we have found suggest an older occupation layer beneath. Fair?' Marsh: 'Yes, that is exactly my concern.' Fen: 'I agree the stratigraphy is complex — more so than the survey predicted. And I learned from your cross-section analysis that the occupation layer may be a thousand years older than the surface finds — I had not considered that possibility.' She pauses. 'But the funding runs out in three months. If we halve the pace, we excavate twenty percent of the site and lose access. I propose we halve the pace in the area around your cross-section and maintain full pace elsewhere, preserving context where it matters most.'",
         "Fen applies Rapoport's Rules in an archaeological methodology dispute.",
         "Experienced, funding-aware, and respectful of scientific rigor.",
         "I do not rush a dig until I can explain why going slow is right. Then I explain why the clock matters too.",
         "Player gains archaeological mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("maritime",
         "Ship officers argue about whether to change course to avoid a storm. The captain restates the helmsman's case for staying the course.",
         "Captain Aldris: 'Helmsman, your position is that the storm track is uncertain, that diverting adds two days and costs fuel we may need later, and that the ship has weathered worse. Fair?' Helmsman: 'Yes, Captain.' Aldris: 'I agree that diversion is costly. And I learned from your fuel calculations that we have less reserve than I assumed after the last resupply — that is important.' She pauses. 'But the barometric readings are dropping faster than any storm I have seen in twenty years. The ship has weathered worse, but not with this cargo weight. I am ordering the diversion, but I want you to know I heard your reasoning and it was sound — the conditions just tipped the balance.'",
         "Captain Aldris applies Rapoport's Rules in a maritime navigation dispute.",
         "Decisive but respectful of crew expertise. Explains her reasoning even when overriding a subordinate.",
         "I give the order, but I also give the reasoning. A crew that understands the captain's logic is a crew that trusts it.",
         "Player earns maritime decision-making skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("firefighting",
         "Firefighters argue about whether to enter a partially collapsed building. The incident commander restates the entry advocate's case.",
         "Commander Brix: 'Lieutenant Cade, you want to enter because your thermal scan shows a heat signature on the second floor, the structural assessment rates the building at marginal-hold, and you believe you can reach the victim in four minutes. Correct?' Cade: 'Yes, Commander.' Brix: 'I agree the thermal signature is compelling — there may be a survivor. And I learned from your assessment that the east stairwell is intact, which I did not know from the exterior view.' She pauses. 'But marginal-hold with fire on the ground floor means the structure could fail in the time it takes to climb. I am not saying no — I am saying we shore the east stairwell first. That adds three minutes but changes the risk calculus fundamentally.'",
         "Brix applies Rapoport's Rules under time pressure in a firefighting decision.",
         "Calm under pressure, respects initiative but insists on calculated risk.",
         "I restate the plan I am about to modify so the person who proposed it knows I understood it.",
         "Player earns emergency decision-making skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("finance",
         "Board members argue about a merger. The chair restates the opponent's case before offering her view.",
         "Chair Voss: 'Director Laine, you oppose the merger because the target company's culture is incompatible, integration costs historically exceed projections by forty percent, and our core business needs the capital more than an acquisition does. Fair?' Laine: 'That is exactly my position.' Voss: 'I agree that culture clashes destroy value — the Kendrick merger proved that. And I learned from your cost analysis that integration estimates in our sector average sixty percent over budget, not the forty percent I assumed.' She pivots. 'But the target's patent portfolio fills our R&D gap. Rather than a full merger, I propose a licensing agreement with an option to acquire in two years, after a cultural compatibility assessment.'",
         "Voss applies Rapoport's Rules in a corporate governance dispute.",
         "Strategic, fair, and known for turning adversarial debates into design sessions.",
         "I do not propose a deal until I can state the case against it better than the opponent.",
         "Player gains corporate mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("environment",
         "Climate policy advisors argue about carbon tax versus cap-and-trade. The minister restates the cap-and-trade advocate's position.",
         "Minister Chen: 'Dr. Patel, you favor cap-and-trade because it sets a hard emissions ceiling, allows market flexibility in how reductions are achieved, and the EU's experience shows it can work at scale. Fair?' Patel: 'Yes, exactly.' Chen: 'I agree that the hard ceiling is valuable — a tax sets price but not quantity. And I learned from your comparison data that the EU system reduced emissions fourteen percent faster than projected in its third phase — I had assumed it underperformed.' She pivots. 'But the administrative complexity of cap-and-trade requires regulatory infrastructure we do not have. A carbon tax can be implemented with existing tax collection systems in six months. I propose we start with the tax and transition to cap-and-trade as institutions mature.'",
         "Chen applies Rapoport's Rules in a climate policy dispute.",
         "Policy-oriented, pragmatic, and committed to evidence-based governance.",
         "I restate the policy I am about to reject so its advocates know I understood its strengths.",
         "Player gains policy mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("gaming",
         "Esports team members argue about roster changes. The team manager restates the current roster defender's case before proposing a change.",
         "Manager Kai: 'Sol, your position is that the current roster has built synergy over two seasons, that new players need months to integrate, and that the team's communication during matches is the best it has ever been. Fair?' Sol: 'That is exactly right.' Kai: 'I agree that synergy takes time to build — the first season was rough. And I learned from your comms analysis that the team's callout accuracy is at ninety-four percent, which is elite-level. I did not realize it was that high.' He pauses. 'But our win rate against top-five teams has dropped from sixty to thirty-five percent this season. The synergy is real, but the meta has shifted and our roster does not cover the new strategies. I propose we keep the core three and trial two specialists, preserving the communication framework while adding flexibility.'",
         "Kai applies Rapoport's Rules in an esports roster dispute.",
         "Analytical, team-focused, and skilled at balancing chemistry with competitive needs.",
         "I do not change a roster until I can explain why the current one works better than the players can.",
         "Player gains team management skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("parenting",
         "Parents and a school principal argue about homework policy. The superintendent restates the anti-homework parent's case.",
         "Superintendent Reyes: 'Mrs. Holden, you believe homework in elementary school is developmentally inappropriate, that the research shows no academic benefit before middle school, and that evening family time is being sacrificed for worksheets. Fair?' Holden: 'Yes, and no one at the school has ever said it back to me like that.' Reyes: 'I agree that family time matters. And I learned from the meta-analysis you cited that the effect size for homework in grades one through four is essentially zero — I had assumed it was small but positive.' She pauses. 'But the teachers report that the reading log — which is technically homework — is the only way they can identify struggling readers early. I propose we eliminate worksheets but keep the reading log with a five-minute-per-night cap, and we stop calling it homework.'",
         "Reyes applies Rapoport's Rules in an education policy dispute.",
         "Evidence-based administrator who respects parent advocacy.",
         "I do not dismiss a parent's concern until I can state it more precisely than they did.",
         "Player gains education policy mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("science",
         "Researchers argue about replication priorities. The department head restates the replication advocate's case.",
         "Department Head Orin: 'Dr. Navarro, you argue that we should dedicate thirty percent of lab time to replicating published findings because the replication crisis undermines our field, our own high-profile paper from last year has never been replicated, and funders are starting to require replication data. Fair?' Navarro: 'Yes, and I am glad someone is taking it seriously.' Orin: 'I agree the replication crisis is real. And I learned from your analysis that four of our twelve flagship results have statistical indicators that suggest they may not replicate — I found that sobering.' He pauses. 'But thirty percent of lab time means our grant applications drop, and without new grants there is no lab. I propose ten percent dedicated replication time, starting with our own most-cited paper, and we build the case for funder support of replication as a category.'",
         "Orin applies Rapoport's Rules in a research priorities dispute.",
         "Thoughtful administrator who balances scientific integrity with institutional survival.",
         "I restate the case for replication until its advocate endorses my version. That is the first step toward taking it seriously.",
         "Player gains scientific mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("retail",
         "Store staff argue about customer loyalty program design. The VP restates the simplicity advocate's position.",
         "VP Harmon: 'Tessa, you want a simple points-per-purchase system because complex tiers confuse customers, your customer feedback shows seventy percent want straightforward rewards, and the competitor who simplified their program saw a twenty percent enrollment increase. Fair?' Tessa: 'Yes, that is my argument.' Harmon: 'I agree simplicity drives enrollment. And I learned from your competitor analysis that they also saw higher average purchase frequency after simplifying — I had assumed simplification just attracted low-value customers.' He pivots. 'But our high-value customers generate sixty percent of revenue and they specifically requested exclusive tiers. I propose a simple base program for all customers with an opt-in premium tier for high-frequency shoppers. Simplicity as default, complexity as choice.'",
         "Harmon applies Rapoport's Rules in a retail strategy dispute.",
         "Customer-obsessed, data-literate, and skilled at designing incentives.",
         "I restate every proposal I am about to modify. It is not politeness — it is due diligence.",
         "Player gains customer strategy mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("relationships",
         "Friends argue about whether to confront a mutual friend's self-destructive behavior. A counselor mediates.",
         "Counselor Thao: 'Ellis, you believe we should not intervene because Jaden is an adult, unsolicited advice pushes people away, and the last time someone confronted Jaden, he disappeared for six months. Fair?' Ellis: 'Yes, and I do not want to lose him again.' Thao: 'I agree that the last confrontation went badly — that history matters. And I learned from your description that Jaden has always responded to questions better than statements. I had assumed direct confrontation was the only intervention model.' She pauses. 'But Morgan's concern is that Jaden's behavior is escalating and silence looks like approval. What if the intervention is not a confrontation but a conversation? We ask Jaden how he is doing — genuinely ask, without an agenda — and let his own answers guide the discussion.'",
         "Thao applies Rapoport's Rules in a relationship conflict about intervention.",
         "Empathetic, process-oriented, and skilled at reframing adversarial choices as design problems.",
         "I do not suggest how to help someone until I can restate why the current approach — including doing nothing — makes sense.",
         "Player gains intervention mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("housing",
         "Tenants and a landlord argue about rent increases. A mediator restates the landlord's case.",
         "Mediator Patel: 'Ms. Greer, your position is that the rent increase reflects actual cost increases — property taxes up twelve percent, insurance up eight, and the new fire code requires sprinkler installation. You are not raising rent for profit; you are raising it to avoid losing money on the building. Fair?' Greer: 'That is exactly right, and I wish someone had said that at the tenants' meeting.' Patel: 'I agree the cost increases are documented. And I learned from your maintenance logs that you spent more on repairs last year than you collected in rent — I had assumed landlords always profit.' He pivots. 'But the tenants on fixed incomes cannot absorb a fifteen percent increase at once. I propose a phased increase — five percent now, five percent in six months, five percent in twelve — with the sprinkler cost amortized over three years.'",
         "Patel applies Rapoport's Rules in a housing cost dispute.",
         "Fair-minded, number-literate, and committed to solutions that both parties can sustain.",
         "I restate the landlord's costs until the tenants can see the problem from the other side. Then we design a solution together.",
         "Player gains housing mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("workplace",
         "Team members argue about remote versus office work. The VP restates the office advocate's case using Rapoport's protocol.",
         "VP Chen: 'Marcus, you argue that in-office work improves collaboration, that spontaneous hallway conversations generate ideas remote meetings cannot replicate, and that your team's project completion rate was twenty percent higher when everyone was on-site. Fair?' Marcus: 'Yes, and the data is clear.' Chen: 'I agree that spontaneous collaboration is hard to replicate remotely. And I learned from your project data that the difference was concentrated in the early brainstorming phase, not the execution phase — I had assumed in-office was better across the board.' She pauses. 'But Lena's retention data shows that four of your best engineers will leave if mandated back full-time. I propose mandatory on-site for brainstorming weeks — two per month — with remote work the rest of the time.'",
         "Chen applies Rapoport's Rules in a workplace flexibility dispute.",
         "Strategic, people-focused, and skilled at synthesizing competing data sets.",
         "I restate the case for the office so well that the office advocate says 'exactly.' Then I show why the data suggests a hybrid answer.",
         "Player gains workplace mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("legal",
         "Attorneys argue about whether to accept a settlement. The senior partner restates the case for going to trial.",
         "Senior Partner Venn: 'Kayla, you want to go to trial because the settlement offer is thirty percent below your damages estimate, because your expert witness is compelling, and because a trial verdict sets precedent that protects future clients. Fair?' Kayla: 'That is exactly my reasoning.' Venn: 'I agree the expert is strong — she is the best in the field. And I learned from your mock trial that the jury responded more favorably than I expected to the technical evidence. I had assumed it would bore them.' She pauses. 'But trials are unpredictable. The judge has a history of limiting expert testimony, and if he curtails our expert, the jury never sees our strongest evidence. I propose we counter-offer at eighty percent of damages with a precedent-setting consent decree. We get most of the money and the precedent, without the courtroom risk.'",
         "Venn applies Rapoport's Rules in a legal strategy decision.",
         "Risk-aware, client-focused, and respectful of junior attorneys' strategic thinking.",
         "I do not recommend settlement until I can present the case for trial better than the trial advocate.",
         "Player gains legal strategy mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("military",
         "Officers debate whether to fortify or advance. The colonel restates the advance advocate's case.",
         "Colonel Aster: 'Lieutenant Renn, your position is that the enemy is retreating in disarray, that our momentum will be lost if we stop to fortify, and that the supply depot ahead gives us a logistical advantage if we reach it first. Fair?' Renn: 'Yes, Colonel.' Aster: 'I agree the enemy appears disordered. And I learned from your recon that the depot is less defended than headquarters estimated — that changes the risk picture.' She pauses. 'But Captain Dorr's intelligence suggests the retreat may be an organized withdrawal to prepared positions. If we advance into an ambush, our momentum becomes their advantage. I propose we advance a reconnaissance element while the main force prepares both to advance and to fortify, keeping our options open until we have eyes on the depot.'",
         "Aster applies Rapoport's Rules in a tactical decision dispute.",
         "Experienced, cautious but not timid, and known for treating junior officers' reasoning with respect.",
         "I restate the plan to advance until the lieutenant endorses my version. That tells me I understand what I am about to modify.",
         "Player gains tactical mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("cooking",
         "Chefs argue about food waste reduction. The head chef restates the zero-waste advocate's case before offering criticism.",
         "Head Chef Nora: 'Lin, your position is that every scrap should be used, that our waste bin costs us fifteen percent of ingredient budget, and that a zero-waste approach would actually produce better broths, stocks, and fermented ingredients. Fair?' Lin: 'Yes, exactly.' Nora: 'I agree the waste cost is staggering. And I learned from your fermentation experiments that vegetable trim makes a kimchi that is actually better than our current recipe — I had not tasted it before today.' She pauses. 'But zero-waste in a high-volume kitchen requires additional prep staff, and our labor budget is already stretched. I propose we implement zero-waste for the five highest-volume items first, prove the savings, and use those savings to fund expansion.'",
         "Nora applies Rapoport's Rules in a culinary operations dispute.",
         "Passionate about quality and efficiency, respectful of kitchen innovation.",
         "I taste the alternative before I reject it. That is step three — learning something from the other side.",
         "Player gains culinary mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("travel",
         "Tour company staff argue about safety briefing length. The operations manager restates the thorough-briefing advocate's case.",
         "Ops Manager Vale: 'Rook, you want the full forty-five-minute safety briefing because the abbreviated version missed three critical risks last season, because two injuries were directly attributable to information gaps, and because regulatory compliance requires documented briefing coverage. Fair?' Rook: 'That is exactly my concern.' Vale: 'I agree the injuries were preventable. And I learned from your incident reports that the abbreviated briefing cut precisely the sections that would have prevented both injuries — that is damning, and I should have reviewed those reports sooner.' She pivots. 'But the thirty-minute version loses twenty percent of the group's attention. What if we keep the forty-five-minute content but restructure it — fifteen minutes hands-on demonstration, fifteen minutes scenario practice, fifteen minutes Q&A? Same information, different delivery.'",
         "Vale applies Rapoport's Rules in a safety operations dispute.",
         "Safety-focused, operationally pragmatic, and open to creative solutions.",
         "I do not shorten a safety briefing until I can explain why the full version saves lives.",
         "Player gains safety operations mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("technology",
         "Developers argue about code review standards. The engineering director restates the strict-review advocate's case.",
         "Director Opal: 'Sev, you want mandatory two-reviewer sign-off because single-reviewer approval missed three critical bugs last quarter, because the security audit flagged our review process as a vulnerability, and because two-reviewer shops have forty percent fewer production incidents. Fair?' Sev: 'That is exactly my position.' Opal: 'I agree single review is insufficient for critical paths. And I learned from your incident analysis that all three bugs were in the same subsystem — I had assumed they were scattered.' She pauses. 'But mandatory two-reviewer for every commit adds two days to our cycle time. The bugs clustered in one subsystem. I propose two-reviewer for the critical subsystem and single-reviewer with automated static analysis for everything else.'",
         "Opal applies Rapoport's Rules in a software engineering process dispute.",
         "Systems-thinker, evidence-driven, and respectful of engineering craft.",
         "I restate the case for stricter process until the advocate says I got it right. Then I propose a targeted version.",
         "Player gains engineering process mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("agriculture",
         "Farmers argue about water rights allocation during drought. The county water manager restates the upstream farmer's case.",
         "Manager Byrne: 'Farmer Holt, you argue that you have senior water rights, that your orchard investment depends on consistent irrigation, and that the downstream farms planted water-intensive crops knowing they had junior rights. Fair?' Holt: 'That is exactly right, and the law supports me.' Byrne: 'I agree your rights are legally senior. And I learned from your irrigation data that you have actually reduced your usage by fifteen percent through drip conversion — I did not know you had already invested in conservation.' She pauses. 'But the downstream farms employ sixty families. If they lose their crop, those families lose their livelihoods. I propose we honor your senior rights at the reduced drip rate — which you have already adopted — and allocate the savings to downstream. You keep your full legal entitlement; they get enough to survive.'",
         "Byrne applies Rapoport's Rules in a water rights dispute.",
         "Fair-minded, legally literate, and focused on community outcomes within legal constraints.",
         "I do not ask someone to share their water until I can explain why their rights are legitimate.",
         "Player gains resource allocation mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("music",
         "Orchestra members argue about concert programming. The conductor restates the traditional repertoire advocate's position.",
         "Conductor Elia: 'First violinist Marsh, your position is that our audience subscribes for the classical repertoire, that our recent contemporary programming led to a twelve percent drop in subscriptions, and that our ensemble's strength is the Romantic period. Fair?' Marsh: 'Yes, and the subscription numbers speak for themselves.' Elia: 'I agree the subscription drop is concerning. And I learned from your audience survey that listeners who attended contemporary concerts were forty percent less likely to renew — a stronger effect than I expected.' She pauses. 'But our grant funding increasingly requires contemporary programming, and without grants we lose twenty percent of our budget. I propose we pair each contemporary piece with a classical anchor — Stravinsky followed by Tchaikovsky — so subscribers get what they came for while we satisfy grant requirements.'",
         "Elia applies Rapoport's Rules in a concert programming dispute.",
         "Artistically ambitious but fiscally realistic, with deep respect for ensemble tradition.",
         "I restate the case for tradition until the traditionalist endorses my version. Then I show how we can honor it while also evolving.",
         "Player gains artistic programming mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("healthcare",
         "Physicians argue about end-of-life care protocols. The ethics committee chair restates the palliative care advocate's case.",
         "Chair Liang: 'Dr. Rosen, your position is that aggressive treatment in the final weeks often causes suffering without extending meaningful life, that patients who receive early palliative care report higher quality of life, and that the current default toward intervention reflects physician discomfort with mortality rather than patient preference. Fair?' Rosen: 'Yes, and I have never heard an administrator state it that clearly.' Liang: 'I agree that patient autonomy should drive these decisions. And I learned from your data that patients who had goals-of-care conversations chose palliative care at three times the rate of those who did not — that tells me the default is not reflecting informed preference.' She pauses. 'But Dr. Werner's concern is that early palliative conversations can be perceived as giving up. The framing matters. I propose we introduce goals-of-care conversations as standard at diagnosis, framed as planning rather than conceding, so the palliative option is understood before crisis forces the decision.'",
         "Liang applies Rapoport's Rules in an end-of-life care ethics dispute.",
         "Ethically rigorous, empathetic, and committed to patient-centered policy.",
         "I restate both sides until each advocate endorses my version of their position. Only then do I propose.",
         "Player gains medical ethics mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("politics",
         "Citizens argue about surveillance technology. A civil liberties advocate and a police chief debate. The mayor restates each position.",
         "Mayor Trent: 'Chief, your position is that facial recognition in the downtown core would have prevented three of the four violent crimes last quarter, that the technology has a ninety-seven percent accuracy rate on the vendor's tests, and that public safety outweighs abstract privacy concerns when people are getting hurt. Fair?' Chief: 'Yes, Mayor.' Trent: 'I agree public safety is paramount. And I learned from your case files that the three crimes you cited had no other viable leads — without the technology, those cases are cold.' She turns. 'Ms. Dao, you argue the accuracy rate drops to eighty-two percent for darker-skinned individuals, that innocent people will be stopped based on false matches, and that surveillance infrastructure, once built, always expands beyond its original purpose. Fair?' Dao: 'Exactly.' Trent: 'I agree that differential accuracy is a civil rights problem. And I learned from your case studies that every city that deployed limited surveillance expanded it within three years.' She pauses. 'Both of you are right about different things. I propose a twelve-month pilot in the downtown core with an independent accuracy audit, a sunset clause requiring council re-authorization, and a civilian oversight board with subpoena power. We test the Chief's safety claim and Ms. Dao's accuracy claim simultaneously.'",
         "Trent applies Rapoport's Rules to both sides of a civil liberties dispute.",
         "Politically pragmatic, committed to evidence-based governance, and skilled at holding multiple positions simultaneously.",
         "I restate both sides until each advocate says 'that is exactly my position.' Then I design a process that tests both claims.",
         "Player gains civic governance mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("school",
         "Teachers argue about standardized testing. The school board chair restates the anti-testing advocate's position before offering a nuanced synthesis.",
         "Chair Odom: 'Ms. Reyes, you argue that standardized tests measure test-taking ability more than knowledge, that teaching to the test narrows the curriculum, and that the stress harms students' mental health. Fair?' Reyes: 'Yes, and it is rare to hear that stated without mockery.' Odom: 'I agree that curriculum narrowing is real — I have seen it. And I learned from your student survey data that anxiety around testing peaks two weeks before the test and does not return to baseline for a week after — a three-week disruption I had not quantified.' He pauses. 'But Mr. Chen argues that without standardized measurement, we cannot identify which schools need resources. The tests are imperfect, but they are currently our only system-wide diagnostic. I propose we replace the high-stakes annual test with quarterly low-stakes assessments that provide the diagnostic data without the three-week anxiety cycle.'",
         "Odom applies Rapoport's Rules in an education policy dispute involving multiple competing values.",
         "Evidence-based, student-centered, and skilled at finding structural solutions to value conflicts.",
         "I restate the anti-testing case until the advocate endorses it. Then I restate the pro-testing case until its advocate endorses it. Only then do I propose.",
         "Player gains education governance mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("sports",
         "Athletes and coaches argue about training intensity. The sports psychologist restates the high-intensity advocate's case.",
         "Dr. Shin: 'Coach Vega, your position is that peak performance requires peak training, that the athletes who train hardest consistently win, and that reducing intensity signals to competitors that we are soft. Fair?' Vega: 'That is exactly right.' Shin: 'I agree that intensity correlates with performance up to a point. And I learned from your competition data that our athletes peak at exactly the right time under your program — the periodization is precise.' She pauses. 'But the injury data tells a different story. We have lost three athletes this season to overuse injuries, and each one peaked before they broke. The training is producing peaks and injuries simultaneously. I propose we keep your periodization structure but add mandatory recovery blocks that reduce intensity twenty percent during the two highest-load weeks.'",
         "Shin applies Rapoport's Rules in a sports science dispute.",
         "Evidence-based, athlete-centered, and respectful of coaching expertise.",
         "I do not challenge a training program until I can explain what it gets right. The right things are usually most of it.",
         "Player gains sports science mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("firefighting",
         "Fire department argues about equipment allocation. The chief restates the frontline crew's case for older but familiar equipment.",
         "Chief Navarro: 'Captain Elm, your position is that the older SCBA units are heavier but your crew has trained on them for years, that switching mid-season introduces unfamiliarity in high-stress situations, and that the new units have an untested fail-safe mechanism. Fair?' Elm: 'Yes, Chief.' Navarro: 'I agree that equipment familiarity saves lives. And I learned from your incident reports that your crew's response times with the old units are actually faster than the department average with the new ones — I had assumed the opposite.' She pauses. 'But the old units' air capacity is twenty percent less, and that twenty percent was the margin in the Birch Street rescue. I propose we run a parallel training program — old units for current operations, new unit familiarization during training rotations — and transition over six months rather than overnight.'",
         "Navarro applies Rapoport's Rules in an equipment modernization dispute.",
         "Safety-first, crew-respectful, and methodical about transitions.",
         "I do not replace equipment a crew trusts until I can explain why they trust it. Then I explain why the replacement earns that trust over time.",
         "Player gains equipment transition mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),
    ]

    # Generate D1.1 records
    for i, s in enumerate(d1_1_scenarios_data):
        domain, ctx, txt, spk, personality, seed, resolution, src, tier = s
        seq = i + 1
        rec = make_record(
            "D1.1", "Rapoport's Rules", "good_tool", seq,
            tier if tier else get_difficulty_tier(i),
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Rapoport's Rules",
                "pattern_description": f"The speaker follows Rapoport's four-step protocol: (1) restate the opponent's position until endorsed, (2) list genuine agreements, (3) acknowledge something learned, (4) only then offer criticism.",
                "formal_form": "Before asserting NOT-P: (1) restate P so advocate endorses; (2) enumerate shared commitments; (3) identify corrected beliefs; (4) then criticize.",
                "why_wrong": None,
                "why_right": "The protocol keeps the opponent engaged even during disagreement because each step demonstrates genuine understanding before criticism.",
                "related_patterns": ["A1.4", "D1.2", "D2.6"],
                "counterpoint": "The protocol requires sincerity at each step. Faked agreement or hollow restatement will be detected and undermine trust.",
            },
            {
                "identification_prompt": f"The mediator disagrees but the other party stays engaged. What specific steps does the mediator take before offering criticism?",
                "rubric": [
                    {"level": 0, "description": "Player sees no deliberate structure."},
                    {"level": 1, "description": "Player notices kindness but cannot identify distinct steps."},
                    {"level": 2, "description": "Player identifies two of the four steps."},
                    {"level": 3, "description": "Player identifies all four Rapoport steps in order."},
                    {"level": 4, "description": "Player identifies all four steps, explains the sequential logic, and can articulate what breaks if a step is insincere or omitted."},
                ],
                "follow_up_if_wrong": "Count the distinct things the mediator does before saying 'but' or 'however.' Each one serves a different purpose.",
                "follow_up_if_right": "What if one of those steps were insincere? Which step, if faked, would most damage the process?",
            },
            {
                "npc_personality": personality,
                "npc_dialogue_seed": seed,
                "resolution_path": resolution,
            },
            src,
        )
        records.append(rec)

    # Pad D1.1 to 50 if needed
    d1_1_extra = [
        ("journalism", "what_if",
         "Editors argue about running a controversial op-ed. The managing editor restates the publishing advocate's case.",
         "Managing Editor Fen: 'Sara, you argue we should publish because the piece is well-sourced, because silencing controversial views betrays our editorial mission, and because our readership expects us to engage with difficult ideas. Fair?' Sara: 'That is exactly my position.' Fen: 'I agree our mission requires engaging with difficulty. And I learned from your reader survey that sixty percent specifically value our willingness to publish challenging perspectives — higher than I expected.' She pivots. 'But the piece contains three unverifiable claims that could expose us to a defamation suit. I propose we publish after the author provides sourcing for those three claims.'",
         "Fen applies Rapoport's Rules in an editorial dispute.",
         "Principled, legally aware, and committed to both editorial courage and factual integrity.",
         "I do not spike a piece until I can explain why it deserves to run. Then I explain what it needs first.",
         "Player gains editorial dispute mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "what_if"),

        ("archaeology", "puzzle",
         "Archaeologists argue about whether to publish a controversial reinterpretation of a famous site. The department head restates the revisionist's case.",
         "Head Dr. Orin: 'Dr. Marsh, you argue the traditional dating is wrong based on three independent isotope analyses, that the site's function was ceremonial rather than residential, and that the established interpretation rests on a 1970s excavation that used methods now considered inadequate. Fair?' Marsh: 'Yes, and I did not expect you to state it that charitably.' Orin: 'I agree the 1970s methods were limited. And I learned from your isotope data that the dating discrepancy is larger than anyone has acknowledged — that is significant.' He pauses. 'But publishing now, before peer review, risks making us look reckless. I propose we submit to three journals simultaneously for expedited review, then publish with the weight of peer validation behind us.'",
         "Orin applies Rapoport's Rules in a scholarly publication dispute.",
         "Rigorous, reputation-conscious, and supportive of bold claims backed by evidence.",
         "I restate the revisionist case so well the revisionist endorses it. Then I propose a process that makes the claim stronger, not weaker.",
         "Player gains scholarly dispute mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("maritime", "puzzle",
         "Maritime officials argue about new port safety regulations. The harbor master restates the industry representative's case.",
         "Harbor Master Quinn: 'Captain Reis, your position is that the proposed twenty-four-hour inspection window will create a bottleneck that costs the fleet an estimated two million per week, that the current eight-hour window catches ninety-five percent of safety issues, and that the remaining five percent are edge cases that full inspections would not reliably catch anyway. Fair?' Reis: 'That is exactly right.' Quinn: 'I agree that bottleneck costs are real. And I learned from your fleet data that the eight-hour window's catch rate is higher than I assumed — ninety-five percent is impressive.' She pauses. 'But the five percent that slip through include the kind of structural failures that sank the Corrigan last year. I propose a risk-tiered system: eight hours for vessels with clean records, twenty-four hours for vessels with prior citations or structural age above twenty years. That targets the high-risk five percent without bottlenecking the fleet.'",
         "Quinn applies Rapoport's Rules in a maritime regulation dispute.",
         "Safety-focused, economically literate, and skilled at designing risk-proportionate regulations.",
         "I restate the industry case until the industry endorses it. Then I show them a regulation that costs less and catches more.",
         "Player gains regulatory mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),

        ("firefighting", "puzzle",
         "Fire department leadership argues about shifting resources from suppression to prevention. The chief restates the suppression advocate's case.",
         "Chief Maren: 'Captain Voss, your position is that fires are unpredictable, that cutting suppression crews to fund prevention leaves us unable to respond when fires happen, and that the public judges us by how fast we arrive, not by fires that did not occur. Fair?' Voss: 'Yes, and that is the reality I live every shift.' Maren: 'I agree that response capacity is non-negotiable. And I learned from your shift data that our current staffing is already below the NFPA minimum for two simultaneous incidents — I had not realized how thin we are.' She pauses. 'But Lieutenant Kade's prevention data shows that the neighborhoods with working smoke detectors have eighty percent fewer fire deaths. I propose we fund prevention from the capital budget, not the suppression budget, so we add capacity without subtracting it.'",
         "Maren applies Rapoport's Rules in a fire service resource allocation dispute.",
         "Strategic, data-informed, and committed to both response and prevention.",
         "I restate the case for keeping what works before I propose adding something new.",
         "Player gains public safety resource mediation skill.",
         "Dennett Intuition Pumps + PHIL 201", "puzzle"),
    ]
    existing_d1_1 = len(d1_1_scenarios_data)
    for i, s in enumerate(d1_1_extra):
        domain, tier_extra, ctx, txt, spk, personality, seed, resolution, src, tier = s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[1]
        seq = existing_d1_1 + i + 1
        rec = make_record(
            "D1.1", "Rapoport's Rules", "good_tool", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Rapoport's Rules",
                "pattern_description": "The speaker follows Rapoport's four-step protocol: (1) restate the opponent's position until endorsed, (2) list genuine agreements, (3) acknowledge something learned, (4) only then offer criticism.",
                "formal_form": "Before asserting NOT-P: (1) restate P so advocate endorses; (2) enumerate shared commitments; (3) identify corrected beliefs; (4) then criticize.",
                "why_wrong": None,
                "why_right": "The protocol keeps the opponent engaged even during disagreement because each step demonstrates genuine understanding before criticism.",
                "related_patterns": ["A1.4", "D1.2", "D2.6"],
                "counterpoint": "The protocol requires sincerity at each step. Faked agreement or hollow restatement will be detected and undermine trust.",
            },
            {
                "identification_prompt": "The mediator disagrees but the other party stays engaged. What specific steps does the mediator take before offering criticism?",
                "rubric": [
                    {"level": 0, "description": "Player sees no deliberate structure."},
                    {"level": 1, "description": "Player notices kindness but cannot identify distinct steps."},
                    {"level": 2, "description": "Player identifies two of the four steps."},
                    {"level": 3, "description": "Player identifies all four Rapoport steps in order."},
                    {"level": 4, "description": "Player identifies all four steps, explains the sequential logic, and can articulate what breaks if a step is insincere or omitted."},
                ],
                "follow_up_if_wrong": "Count the distinct things the mediator does before saying 'but' or 'however.' Each one serves a different purpose.",
                "follow_up_if_right": "What if one of those steps were insincere? Which step, if faked, would most damage the process?",
            },
            {"npc_personality": personality, "npc_dialogue_seed": seed, "resolution_path": resolution},
            src,
        )
        records.append(rec)

    # ================================================================
    # D1.2 — Reductio ad absurdum (good_tool) x 50
    # ================================================================
    d1_2_data = [
        ("workplace", "drill",
         "The player enters a management meeting where Director Falk argues that all employee feedback should be anonymous because accountability stifles honesty.",
         "Intern Pria responds: 'If all feedback must be anonymous, then performance reviews should be anonymous too. And hiring recommendations. And safety reports. After all, accountability stifles honesty in all those cases too, right? Should we not know who recommended hiring someone who turned out to be dangerous?' Falk hesitates.",
         "Pria takes Falk's principle to its logical conclusion, showing it produces consequences he cannot accept.",
         "Assuming Falk's principle that accountability stifles honesty, Pria derives that safety reports should also be anonymous — a consequence Falk cannot endorse because anonymous safety reports eliminate accountability for life-and-death recommendations."),

        ("school", "drill",
         "A student argues that grades should be abolished because they cause stress.",
         "Another student replies: 'If we abolish everything that causes stress, we should also abolish homework, exams, attendance requirements, and deadlines. Actually, we should abolish learning itself, since learning new things is inherently stressful. Is that what you want — a school where nobody learns anything because learning is uncomfortable?'",
         "The respondent assumes the stress-elimination principle and derives the absurd conclusion that learning itself should be abolished.",
         "Assume: anything causing stress should be abolished. Learning causes stress. Therefore learning should be abolished. Since the advocate cannot accept this, the original principle is too broad."),

        ("healthcare", "drill",
         "A hospital administrator argues that patient satisfaction scores should be the primary metric for evaluating doctors.",
         "Dr. Kesh responds: 'If patient satisfaction is the primary metric, then a doctor who prescribes unnecessary painkillers to every patient would score higher than one who delivers an uncomfortable but accurate diagnosis. The dentist who never mentions cavities would outscore the one who catches them early. Do we want to reward the doctors patients like most, or the ones who keep patients alive?'",
         "Dr. Kesh assumes satisfaction-as-primary-metric and derives that harmful doctors would score highest — a consequence the administrator cannot accept.",
         "Assume: satisfaction is the primary metric. Painkillers and avoidance of hard truths increase satisfaction. Therefore the worst medical practice produces the best scores. The administrator cannot accept this, so satisfaction cannot be the sole primary metric."),

        ("politics", "drill",
         "A politician argues that any policy supported by a majority should be implemented immediately.",
         "A journalist responds: 'If majority support is sufficient for immediate implementation, then if fifty-one percent vote to confiscate the property of the other forty-nine percent, that should be implemented immediately too. A majority once supported racial segregation. Should that have been implemented without question simply because it was popular?'",
         "The journalist assumes the majority-rule principle and derives that tyranny of the majority would be legitimate — a consequence the politician cannot endorse.",
         "Assume: majority support justifies immediate implementation. Majorities have supported confiscation and segregation. Therefore these should be implemented. Since the politician rejects this, majority support alone is insufficient."),

        ("sports", "drill",
         "A coach argues that only winning matters and any legal tactic is acceptable if it helps win.",
         "A player responds: 'If any legal tactic is acceptable, then deliberately injuring the opposing star player with a technically legal hit is fine. Time-wasting from the first minute is fine. Psychologically tormenting rookies within the rules is fine. Are you really comfortable with all of that?'",
         "The player assumes the any-legal-tactic principle and derives consequences the coach cannot stomach.",
         "Assume: any legal tactic is acceptable. Deliberate injury via legal hits is legal. Therefore deliberate injury is acceptable. The coach cannot endorse this, revealing that legality alone is not the right standard."),

        ("cooking", "drill",
         "A food critic argues that authenticity is the only measure of good cooking — any deviation from traditional recipes is wrong.",
         "Chef Mira responds: 'If deviation from tradition is always wrong, then tomatoes in Italian food are wrong — they came from the Americas in the sixteenth century. Chili peppers in Thai food are wrong — also from the Americas. Every cuisine you call authentic was once an innovation someone would have called inauthentic.'",
         "Mira assumes the no-deviation principle and shows it would condemn the very dishes the critic calls authentic.",
         "Assume: deviation from tradition is wrong. Tomatoes in Italian cuisine were a deviation. Therefore Italian cuisine is wrong. The critic cannot accept this, revealing that authenticity must accommodate change."),

        ("technology", "drill",
         "A manager argues that all software should be free because information wants to be free.",
         "Developer Kael responds: 'If all software should be free, then the salaries of the people who write it should also be free — meaning zero. And the servers that run it should be free. And the electricity. If none of those costs are paid, who builds the software? Your principle leads to a world where no software exists.'",
         "Kael assumes the free-software principle and derives that no one would be paid to create software — collapsing the ecosystem the manager depends on.",
         "Assume: all software should be free. Software requires paid labor. Free software means unpaid labor. Unpaid labor means no software. The manager cannot accept no software, so the principle is too broad."),

        ("military", "drill",
         "An officer argues that retreat is never acceptable because it damages morale.",
         "Sergeant Thorne responds: 'If retreat is never acceptable, then we should have stood our ground at the Ashfield ambush — where retreat saved two hundred lives. We should have held the burning bridge crossing — where retreat prevented the entire column from being trapped. Never retreating means never surviving a losing position. Are you prepared to lose the army to save morale?'",
         "Thorne assumes the no-retreat principle and shows it would have resulted in catastrophic losses in historical cases the officer knows well.",
         "Assume: retreat is never acceptable. At Ashfield, holding position meant total loss. Therefore total loss is acceptable. The officer cannot endorse this."),

        ("legal", "drill",
         "A law student argues that intent should be irrelevant to criminal liability — only actions and outcomes should matter.",
         "Professor Venn responds: 'If intent is irrelevant, then a surgeon who accidentally nicks an artery during a life-saving operation is guilty of assault. A driver who swerves to avoid a child and hits a mailbox is guilty of property destruction. A parent who grabs their toddler away from a hot stove is guilty of battery. Are you comfortable prosecuting all of them?'",
         "Venn assumes the no-intent principle and derives that heroic and accidental actions become criminal — a consequence the student cannot accept.",
         "Assume: intent is irrelevant. Accidental harm during surgery is harm. Therefore the surgeon is guilty of assault. The student cannot accept this."),

        ("parenting", "drill",
         "A parent argues that children should never experience failure because failure damages self-esteem.",
         "The school counselor responds: 'If children should never fail, then we should never let them try anything difficult. No sports tryouts, no auditions, no challenging homework. But a child who has never failed has never learned that failure is survivable. You are proposing to protect self-esteem by preventing the experiences that build resilience. Would you want to hire an adult who has never once failed at anything?'",
         "The counselor assumes the no-failure principle and shows it produces fragile, untested adults — the opposite of the parent's goal.",
         "Assume: children should never fail. Never failing requires never attempting difficulty. Never attempting difficulty means no resilience. The parent wants resilient children, creating a contradiction."),

        ("music", "drill",
         "A music professor argues that improvisation has no place in classical performance because the composer's intent is sacred.",
         "A student responds: 'If the composer's intent is sacred and cannot be deviated from, then cadenzas in concertos are wrong — yet Mozart, Beethoven, and Brahms all expected performers to improvise cadenzas. Ornamentation in Baroque music is wrong — yet Bach's scores assume the performer will add ornaments. Your principle condemns the very composers you are trying to protect.'",
         "The student assumes the no-improvisation principle and shows it contradicts the practices of the composers the professor reveres.",
         "Assume: improvisation violates composer's intent. Composers expected improvised cadenzas. Therefore following the principle violates the intent it claims to protect. Contradiction."),

        ("gaming", "drill",
         "A game designer argues that all randomness should be removed from games because randomness is unfair.",
         "Another designer responds: 'If randomness is unfair, then card shuffling is unfair, dice rolling is unfair, and procedural generation is unfair. Chess would be the only fair game — but even chess has the randomness of who goes first. And without randomness, every game becomes a solved puzzle once optimal play is known. You are removing fairness by removing the variety that keeps competition meaningful.'",
         "The respondent assumes the no-randomness principle and shows it eliminates the very variety that makes games worth playing.",
         "Assume: randomness is unfair and should be removed. Without randomness, games become deterministic puzzles. Deterministic puzzles become solved and trivial. The designer cannot accept trivial games."),

        ("agriculture", "drill",
         "A farmer argues that pesticides are always wrong because they harm the environment.",
         "An agronomist responds: 'If pesticides are always wrong, then the organic farm next door is wrong too — they use pyrethrin and copper sulfate, which are natural pesticides. And if all pest control is wrong, then we accept that locusts will destroy thirty percent of the harvest, which means people go hungry. Is hunger more acceptable than targeted pest management?'",
         "The agronomist assumes the no-pesticide principle and derives either that organic farming is also wrong, or that famine is acceptable — neither of which the farmer endorses.",
         "Assume: pesticides are always wrong. Organic pesticides are pesticides. Therefore organic farming is wrong. The farmer uses organic methods, creating a contradiction."),

        ("science", "drill",
         "A philosopher argues that science cannot tell us anything true because scientific theories are always revised.",
         "A physicist responds: 'If revision means we know nothing, then you know nothing either — your philosophical position has been revised by every major philosopher since Plato. Medicine knows nothing — we should go back to bloodletting. Engineering knows nothing — bridges stand by luck. You are using a principle that, if applied consistently, destroys all knowledge including your own claim.'",
         "The physicist assumes the revision-means-no-truth principle and shows it is self-defeating — the principle itself is revisable and therefore untrue by its own standard.",
         "Assume: revisability means no truth. The claim 'revisability means no truth' is itself revisable. Therefore it is not true. Self-defeating reductio."),

        ("retail", "drill",
         "A store manager argues that the customer is always right.",
         "An employee responds: 'If the customer is always right, then the customer who says this product should be free is right. The customer who says employees should work unpaid overtime is right. The customer who verbally abuses staff is right. Are you really prepared to accept all of those positions?'",
         "The employee assumes the customer-is-always-right principle and derives consequences the manager cannot accept.",
         "Assume: the customer is always right. Customer demands free products. Therefore free products are right. The manager cannot accept this."),

        ("relationships", "drill",
         "A friend argues that honesty requires sharing every thought you have about someone.",
         "Another friend responds: 'If honesty requires sharing every thought, then you should tell your grandmother her cooking is mediocre, your boss that his presentation bored you, and your partner that you found someone more attractive at the party. Total honesty without filters is not honesty — it is cruelty disguised as a virtue.'",
         "The respondent assumes the total-honesty principle and derives that cruelty becomes a moral requirement — the opposite of what the advocate intends.",
         "Assume: honesty requires sharing every thought. Some thoughts, shared, are cruel. Therefore cruelty is a moral requirement. The advocate cannot accept this."),

        ("finance", "drill",
         "An investor argues that one should never sell a stock at a loss because selling at a loss means losing money.",
         "A financial advisor responds: 'If you never sell at a loss, then you hold a stock from ten dollars to one dollar to ten cents to bankruptcy. You lose everything instead of cutting your loss at eight dollars. Your rule against losing money guarantees you lose the maximum possible amount.'",
         "The advisor assumes the never-sell-at-loss principle and shows it produces the maximum loss — the exact opposite of its intention.",
         "Assume: never sell at a loss. Stock declines to zero. Holding to zero is the maximum loss. The rule designed to prevent loss causes maximum loss. Contradiction."),

        ("travel", "drill",
         "A traveler argues that one should only visit countries with perfect safety records.",
         "A companion responds: 'No country has a perfect safety record. Not even your home country. If you only visit perfectly safe places, you never leave your house. Actually, most accidents happen at home, so your house is not safe either. Your principle leads to never going anywhere at all.'",
         "The companion assumes the perfect-safety principle and shows it eliminates all possible destinations, including home.",
         "Assume: only visit perfectly safe places. No place is perfectly safe. Therefore go nowhere. The traveler cannot accept never traveling."),

        ("environment", "drill",
         "An activist argues that humans should have zero impact on the natural environment.",
         "A biologist responds: 'If humans should have zero impact, then agriculture is wrong — it reshapes ecosystems. Housing is wrong — it displaces habitat. Even walking through a forest has impact. Your principle requires human extinction, since any living human has some environmental impact. Is that your position?'",
         "The biologist assumes the zero-impact principle and derives that human existence itself is impermissible.",
         "Assume: zero environmental impact is required. Human existence has impact. Therefore human existence is impermissible. The activist cannot accept this."),

        ("housing", "drill",
         "A city councillor argues that no new housing should be built because it changes the character of the neighborhood.",
         "A resident responds: 'If no new housing can be built because it changes character, then the houses we live in now should never have been built either — they changed the character of the farmland that was here before. And the farms changed the character of the forest. Your principle, applied consistently, means no settlement should ever have existed.'",
         "The resident assumes the no-change-in-character principle and shows it retroactively condemns the existing neighborhood.",
         "Assume: building changes character and is therefore wrong. Current buildings changed prior character. Therefore current buildings are wrong. The councillor cannot accept demolishing the existing neighborhood."),

        ("journalism", "what_if",
         "An editor argues that news should only report verified facts, never speculation or analysis.",
         "A reporter responds: 'If we only report verified facts, then we cannot report on ongoing investigations — they are unverified by definition. We cannot warn the public about emerging threats — unverified until confirmed. We cannot publish investigative journalism at all, since it involves connecting dots before official verification. Your newsroom would report yesterday's weather and nothing else.'",
         "The reporter assumes the verified-facts-only principle and shows it eliminates all journalism except retrospective reporting of already-known information.",
         "Assume: only verified facts. Investigations are unverified. Therefore no investigative journalism. The editor values investigative journalism, creating a contradiction."),

        ("theater", "what_if",
         "A drama teacher argues that actors should never break character because it destroys the illusion.",
         "A student responds: 'If actors must never break character, then they cannot respond to a medical emergency in the audience. They cannot acknowledge a fire alarm. They cannot stop a scene where another actor is genuinely injured. Your rule prioritizes a fiction over actual human safety.'",
         "The student assumes the never-break-character principle and shows it prioritizes theatrical illusion over life safety.",
         "Assume: never break character. Emergency requires breaking character. Therefore emergencies go unaddressed. The teacher cannot accept this."),

        ("archaeology", "what_if",
         "A preservationist argues that no archaeological site should ever be excavated because excavation destroys the site.",
         "An archaeologist responds: 'If no site can be excavated, then the knowledge buried in those sites stays buried forever. We would not know about Pompeii, Tutankhamun, or the Terracotta Army. And sites are destroyed by erosion, development, and looting anyway. Your principle preserves sites from scientific study while they are destroyed by neglect.'",
         "The archaeologist assumes the no-excavation principle and shows it preserves ignorance while sites are lost to natural decay and theft.",
         "Assume: excavation is always wrong. Natural processes destroy sites. Therefore sites are lost without any knowledge gained. The preservationist values knowledge of the past, creating a tension."),

        ("maritime", "what_if",
         "A shipping executive argues that maximum cargo loading is always optimal because it maximizes profit per voyage.",
         "A naval architect responds: 'If maximum loading is always optimal, then the Plimsoll line is always wrong. The ships that sank from overloading in the nineteenth century were optimally loaded by your definition. Maximum cargo with minimum freeboard means maximum profit right up until the ship capsizes and you lose everything — cargo, ship, and crew.'",
         "The architect assumes the maximum-loading principle and shows that the historical record of sinkings is the reductio of that principle.",
         "Assume: maximum cargo is always optimal. Maximum cargo reduces freeboard. Reduced freeboard causes capsizing. Capsizing loses everything. Maximum profit becomes maximum loss."),

        ("firefighting", "what_if",
         "A fire chief argues that response time is the only metric that matters and all resources should be optimized for speed.",
         "A battalion chief responds: 'If speed is all that matters, then we should skip donning breathing apparatus — that adds ninety seconds. We should skip size-up — that adds two minutes. We should drive through red lights without slowing — that saves thirty seconds. Your principle optimizes for the one metric that sounds best while eliminating the safety steps that keep firefighters alive.'",
         "The battalion chief assumes the speed-only principle and shows it leads to unprotected firefighters and reckless driving — consequences the chief cannot accept.",
         "Assume: only speed matters. Safety equipment slows response. Therefore skip safety equipment. Unprotected firefighters die. The chief cannot accept firefighter deaths."),

        ("workplace", "what_if",
         "A manager argues that efficiency requires eliminating all meetings because meetings waste time.",
         "A team lead responds: 'If all meetings are eliminated, then how do we coordinate a product launch? How do we resolve the conflict between engineering and marketing? How do we onboard new employees? You are solving the problem of bad meetings by eliminating the function that good meetings serve. That is like solving the problem of bad food by never eating.'",
         "The team lead assumes the no-meetings principle and shows it eliminates coordination, conflict resolution, and onboarding — functions the manager relies on.",
         "Assume: all meetings should be eliminated. Coordination requires meetings. Therefore coordination is eliminated. The manager needs coordination, creating a contradiction."),

        ("school", "what_if",
         "A parent argues that teachers should never correct students because correction discourages creativity.",
         "The teacher responds: 'If teachers never correct, then a student who writes two plus two equals five goes uncorrected. A student who spells their name wrong on a job application goes uncorrected. A student who misidentifies a poisonous plant as edible goes uncorrected. You are protecting creativity by eliminating accuracy, and accuracy is what keeps creativity from being dangerous.'",
         "The teacher assumes the no-correction principle and derives that factual errors — including dangerous ones — go unchallenged.",
         "Assume: correction is always wrong. Errors include dangerous ones. Therefore dangerous errors go uncorrected. The parent cannot accept a child eating poison because no one corrected their plant identification."),

        ("healthcare", "what_if",
         "A wellness guru argues that natural remedies are always better than pharmaceutical ones because nature is inherently healing.",
         "A pharmacist responds: 'If natural means better, then arsenic is better than aspirin — arsenic is natural. Hemlock is better than chemotherapy. Untreated infections are better than antibiotics because antibiotics are synthetic. Your principle, applied consistently, recommends poison over medicine.'",
         "The pharmacist assumes the natural-is-better principle and shows it endorses known poisons over proven treatments.",
         "Assume: natural is always better. Arsenic is natural. Therefore arsenic is better than aspirin. The guru cannot accept this."),

        ("politics", "what_if",
         "A politician argues that any speech that offends anyone should be banned because people have a right not to be offended.",
         "A journalist responds: 'If offensive speech is banned, then civil rights advocacy is banned — it offended segregationists. Galileo's astronomy is banned — it offended the Church. Your own political platform offends your opponents — it should be banned too. A right not to be offended is a right to silence everyone, including yourself.'",
         "The journalist assumes the ban-offensive-speech principle and shows it would have banned the very progress the politician celebrates.",
         "Assume: offensive speech should be banned. Civil rights rhetoric offended many. Therefore civil rights rhetoric should have been banned. The politician cannot accept this."),

        ("finance", "what_if",
         "An economist argues that all regulation distorts markets and should be eliminated.",
         "Another economist responds: 'If all regulation is eliminated, then contracts are unenforceable — contract law is regulation. Property rights are unprotected — property law is regulation. Fraud is legal — fraud statutes are regulation. Markets themselves cannot function without the regulatory framework that defines ownership, exchange, and enforcement. You are arguing for the abolition of the conditions that make markets possible.'",
         "The respondent assumes the no-regulation principle and shows it eliminates the legal infrastructure that markets require to exist.",
         "Assume: all regulation should be eliminated. Contract law is regulation. Therefore contracts are unenforceable. Markets require contracts. Therefore markets collapse."),

        ("science", "what_if",
         "A relativist argues that all knowledge systems are equally valid — Western science has no special claim to truth.",
         "A researcher responds: 'If all knowledge systems are equally valid, then the flat earth model is as valid as the spherical model. Bloodletting is as valid as surgery. Your own position — that all systems are equal — is no more valid than the position that they are not. You have undermined your own claim by your own principle.'",
         "The researcher produces a self-referential reductio: the equality principle, applied to itself, is no more valid than its negation.",
         "Assume: all knowledge systems are equally valid. The claim 'not all systems are equal' is a knowledge claim. Therefore it is equally valid. The original claim is no more valid than its negation. Self-undermining."),

        ("gaming", "what_if",
         "A player argues that skill should be the only factor in competitive games — no matchmaking, no handicaps, no ranked tiers.",
         "Another player responds: 'If skill is the only factor with no matchmaking, then a professional player faces a beginner in every match. The beginner never improves because they are crushed instantly. The professional never improves because they face no challenge. Your skill-only principle produces a system where nobody develops skill.'",
         "The respondent assumes no-matchmaking and shows it undermines skill development for both beginners and experts.",
         "Assume: no matchmaking. Beginners face professionals. Beginners are crushed and quit. Professionals face no challenge. Neither improves. The principle undermines the value it claims to promote."),

        ("agriculture", "what_if",
         "A traditionalist argues that farming should only use methods available before industrialization.",
         "A farmer responds: 'If we only use pre-industrial methods, then we use no refrigeration, no veterinary antibiotics, and no weather forecasting. Crop yields drop seventy percent. The population that can be fed drops proportionally. You are proposing a food system that feeds two billion people in a world of eight billion. What happens to the other six billion?'",
         "The farmer assumes the pre-industrial principle and derives mass starvation — a consequence the traditionalist cannot accept.",
         "Assume: only pre-industrial methods. Pre-industrial yields feed two billion. World population is eight billion. Therefore six billion go unfed."),

        ("relationships", "what_if",
         "A therapist's client argues that a good relationship means never having conflict.",
         "The therapist responds: 'If a good relationship means no conflict, then you can never disagree about finances, parenting, or household responsibilities. You can never express a need that differs from your partner's. You would have to either suppress every difference or choose a partner who is your exact clone. Is that a relationship or a performance?'",
         "The therapist assumes the no-conflict principle and shows it requires either total suppression or an impossible partner match.",
         "Assume: good relationships have no conflict. Partners have different needs. Expressing different needs creates conflict. Therefore expressing needs is forbidden. Suppressing needs destroys relationships. Contradiction."),

        ("retail", "what_if",
         "A marketing director argues that lower prices always lead to more sales.",
         "An analyst responds: 'If lower prices always lead to more sales, then free products should sell the most. But we tried giving away samples and demand actually dropped — customers assumed the product was worthless. Luxury goods sell more at higher prices because price signals quality. Your rule fails in exactly the market segment that generates our highest margins.'",
         "The analyst assumes the lower-price-equals-more-sales principle and shows it fails for free products and luxury goods.",
         "Assume: lower prices always increase sales. Zero price should maximize sales. Zero price signaled zero value. Sales dropped. The principle is false in important cases."),

        ("housing", "what_if",
         "A landlord argues that all property decisions should maximize property value because property is an investment.",
         "A tenant responds: 'If all decisions maximize property value, then evicting long-term tenants for renovations is always right. Demolishing affordable housing for luxury condos is always right. Making neighborhoods unlivable for current residents to attract wealthier ones is always right. Your principle treats housing as a commodity and people as externalities.'",
         "The tenant assumes the maximize-value principle and shows it endorses displacement and gentrification as moral goods.",
         "Assume: all property decisions should maximize value. Eviction for renovation maximizes value. Therefore eviction is always right. The landlord claims to care about tenants, creating a contradiction."),

        ("parenting", "what_if",
         "A parent argues that all screen time is harmful and children should have zero access to electronic devices.",
         "The other parent responds: 'If zero screen time is the rule, then our child cannot do their homework — the school uses digital assignments. They cannot video-call their grandparents. They cannot learn to use the technology they will need as adults. You are protecting them from screens by isolating them from education, family, and future employability.'",
         "The other parent assumes zero-screen-time and derives educational, social, and professional consequences the first parent cannot accept.",
         "Assume: zero screen time. School requires screens. Therefore child cannot complete school. The parent values education, creating a contradiction."),

        ("music", "what_if",
         "A purist argues that electronic instruments are not real instruments because they do not produce sound acoustically.",
         "A musician responds: 'If electronic sound production disqualifies an instrument, then the electric guitar — used by Hendrix, Clapton, and every rock musician — is not a real instrument. The Hammond organ is not real. The theremin is not real. You are defining most of twentieth-century music out of existence.'",
         "The musician assumes the acoustic-only principle and shows it excludes the instruments that defined modern music.",
         "Assume: electronic instruments are not real. Electric guitars are electronic. Therefore electric guitars are not real instruments. The purist cannot accept excluding Hendrix."),

        ("environment", "puzzle",
         "An ethicist argues that all species have equal moral value and none should be prioritized over another.",
         "A conservation biologist responds: 'If all species have equal value, then the smallpox virus has equal value to a blue whale. The malaria parasite has equal value to a child. Eradicating smallpox was morally wrong. Are you prepared to defend the moral equivalence of the polio virus and a human infant?'",
         "The biologist assumes the equal-value principle and derives that disease eradication is morally wrong.",
         "Assume: all species have equal moral value. Smallpox is a species. Eradicating smallpox killed a species. Therefore eradication was wrong. The ethicist cannot endorse preserving smallpox."),

        ("travel", "puzzle",
         "A cultural commentator argues that cultural exchange is always appropriation and should be avoided.",
         "A historian responds: 'If cultural exchange is always appropriation, then the Japanese adoption of Western medicine is appropriation. The European adoption of Arabic numerals is appropriation. The global adoption of democratic principles is appropriation. Your principle, applied consistently, condemns every culture for borrowing from every other culture throughout all of human history. It freezes cultures in amber and prohibits learning.'",
         "The historian assumes the exchange-is-appropriation principle and shows it condemns all cross-cultural learning, including the critic's own borrowed ideas.",
         "Assume: cultural exchange is appropriation. Arabic numerals in Western math is exchange. Therefore Western mathematics is appropriation. The commentator uses Arabic numerals, making them complicit in what they condemn."),

        ("legal", "puzzle",
         "A law professor argues that the justice system should focus solely on rehabilitation, never punishment.",
         "A student responds: 'If rehabilitation is the sole purpose, then a fully rehabilitated serial killer should be released immediately, regardless of how many people they killed. A corporate fraudster who demonstrates they will not reoffend should face no consequences, even if thousands lost their savings. Your principle means that the victims' suffering is irrelevant to the justice system's response.'",
         "The student assumes rehabilitation-only justice and derives that fully rehabilitated perpetrators of severe crimes face no consequences — a position the professor finds difficult to defend.",
         "Assume: only rehabilitation matters. A rehabilitated serial killer is rehabilitated. Therefore they should be released. The professor cannot accept immediate release of rehabilitated serial killers without any acknowledgment of victims."),

        ("technology", "puzzle",
         "A privacy advocate argues that all data collection by companies should be illegal because it violates privacy.",
         "An engineer responds: 'If all data collection is illegal, then a hospital cannot keep medical records. A bank cannot track transactions. A search engine cannot remember what you searched for to return results. Your email provider cannot store your emails. You have not eliminated corporate surveillance — you have eliminated the digital infrastructure of modern life.'",
         "The engineer assumes the no-data-collection principle and shows it eliminates medical records, banking, and email.",
         "Assume: all data collection is illegal. Medical records are collected data. Therefore medical records are illegal. The advocate relies on medical records, creating a practical contradiction."),

        ("workplace", "puzzle",
         "A CEO argues that all business decisions should be made by data alone, with no room for judgment or intuition.",
         "A VP responds: 'If decisions are data-only, then which data to collect is itself a judgment call that cannot be made by data. The decision to trust a particular data source requires judgment about its reliability. And the most important business decisions — like whether to enter a new market — involve situations where no relevant data exists yet. Data-only decision-making requires judgment to even get started. Your principle needs the very thing it prohibits.'",
         "The VP shows the data-only principle is self-undermining: selecting, validating, and interpreting data all require the judgment the principle excludes.",
         "Assume: only data, no judgment. Selecting which data to collect requires judgment. Therefore the principle requires what it forbids. Self-undermining."),

        ("sports", "puzzle",
         "A commentator argues that the only purpose of sport is winning and any other value — sportsmanship, fair play, health — is a distraction.",
         "An athlete responds: 'If winning is the only purpose, then doping should be mandatory — it improves winning chances. Playing through career-ending injuries should be required. Youth sports should cut children who do not project as future champions. Your principle turns sport into a factory for broken bodies and broken spirits, and the only product is a trophy.'",
         "The athlete assumes the winning-only principle and derives that health destruction and child exclusion become morally required.",
         "Assume: only winning matters. Doping improves winning probability. Therefore doping should be mandatory. The commentator cannot accept mandatory doping."),

        ("cooking", "puzzle",
         "A food safety absolutist argues that any dish with a nonzero risk of foodborne illness should be banned.",
         "A chef responds: 'If we ban all food with nonzero risk, then sushi is banned, steak tartare is banned, raw oysters are banned, soft cheese is banned, and salad is banned — leafy greens cause more foodborne illness outbreaks than any other food category. Your principle bans salad. Is that really your position?'",
         "The chef assumes zero-risk food policy and shows it bans salad — one of the healthiest and most mundane food categories.",
         "Assume: ban all food with nonzero risk. Leafy greens carry nonzero risk. Therefore salad is banned. The absolutist cannot accept banning salad."),

        ("maritime", "puzzle",
         "A shipping regulator argues that absolute safety requires eliminating all risk from maritime operations.",
         "A captain responds: 'The only way to eliminate all risk from maritime operations is to never leave port. But ships in port deteriorate, crews lose skills, and the goods those ships carry never reach the people who need them. Your principle of absolute safety guarantees certain harm — economic collapse and skill degradation — to avoid uncertain harm.'",
         "The captain assumes absolute safety and shows it produces certain harms worse than the uncertain harms it prevents.",
         "Assume: eliminate all maritime risk. The only way is to never sail. Never sailing causes economic collapse. Economic collapse is certain harm. The principle trades uncertain risk for certain catastrophe."),
    ]

    for i, (domain, tier, ctx, txt, spk, desc) in enumerate(d1_2_data):
        seq = i + 1
        rec = make_record(
            "D1.2", "Reductio ad absurdum", "good_tool", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Reductio ad absurdum",
                "pattern_description": desc,
                "formal_form": "Assume P. P entails Q. Q is absurd. Therefore not-P.",
                "why_wrong": None,
                "why_right": "Reductio tests a claim by its own standards. If a principle generates consequences the proponent cannot stomach, the principle needs revision.",
                "related_patterns": ["A3.1", "A5.1", "D1.5"],
                "counterpoint": "A sophisticated opponent might 'bite the bullet' and accept the derived consequence. The reductio is only as strong as the absurdity of the conclusion.",
            },
            {
                "identification_prompt": "One speaker takes the other's claim and does something specific with it. What technique is being used, and why is it effective?",
                "rubric": [
                    {"level": 0, "description": "Player cannot identify the technique or sees it as mere disagreement."},
                    {"level": 1, "description": "Player notices counterexamples but misses the assume-derive-reject structure."},
                    {"level": 2, "description": "Player sees the argument leads to absurd conclusions but cannot name the method."},
                    {"level": 3, "description": "Player identifies reductio: assume the position, derive absurd consequences, reject the original position."},
                    {"level": 4, "description": "Player identifies reductio, articulates the formal structure, and discusses when it succeeds versus when the opponent might bite the bullet."},
                ],
                "follow_up_if_wrong": "The respondent did not say the original claim was wrong directly. Instead, they assumed it was true and followed it somewhere specific. Where did it lead?",
                "follow_up_if_right": "What if the original speaker accepted the absurd consequence? Would the reductio still work?",
            },
            {
                "npc_personality": "Sharp, quick-witted, and skilled at following ideas to their logical conclusions.",
                "npc_dialogue_seed": "You believe that principle? Let us follow it and see where it takes us.",
                "resolution_path": "If the player identifies the reductio, they earn it as a dialogue tool for challenging over-broad principles.",
            },
            "Dennett Intuition Pumps + PHIL 201 lecture notes on reductio",
        )
        records.append(rec)

    # Pad D1.2 to 50
    d1_2_extra = [
        ("journalism", "puzzle",
         "An editor argues that objectivity requires presenting both sides of every issue equally.",
         "A reporter responds: 'If both sides must be presented equally, then a story about the earth's shape must give equal space to flat-earthers. A story about the Holocaust must give equal space to deniers. A story about vaccination must give equal space to anti-vaxxers. Your principle of objectivity, applied consistently, gives lies the same platform as truths.'",
         "The reporter assumes the equal-sides principle and shows it requires platforming known falsehoods.",
         "Assume: both sides always deserve equal presentation. Flat earth is a side. Therefore flat earth deserves equal space with round earth. The editor cannot accept this."),

        ("theater", "puzzle",
         "A director argues that the audience's interpretation is the only one that matters — the creator's intent is irrelevant.",
         "A playwright responds: 'If creator intent is irrelevant, then it is irrelevant whether I wrote this play as a comedy or a tragedy. It is irrelevant whether the character's final line is sarcastic or sincere. In fact, your direction of this play imposes your intent on the actors — but by your own principle, your directorial intent is also irrelevant. You have undermined your own authority to direct.'",
         "The playwright assumes the no-intent principle and shows it undermines the director's own practice of imposing interpretive choices.",
         "Assume: creator intent is irrelevant. The director is a creator. Therefore the director's intent is irrelevant. But the director depends on their intent being followed. Self-undermining."),

        ("archaeology", "puzzle",
         "A government official argues that economic development should always take priority over archaeological preservation.",
         "An archaeologist responds: 'If development always takes priority, then the Parthenon should be demolished for a shopping center. The Colosseum should become a parking garage. Stonehenge should be cleared for farmland. You are proposing a world where nothing is old because nothing was ever worth keeping.'",
         "The archaeologist assumes the development-always-wins principle and shows it would destroy every heritage site.",
         "Assume: development always takes priority. The Parthenon occupies valuable real estate. Therefore demolish the Parthenon. The official cannot accept this."),

        ("maritime", "puzzle",
         "A port authority argues that all fishing regulations are unnecessary because fishers will self-regulate to protect their livelihood.",
         "A marine biologist responds: 'If fishers self-regulate, then the Grand Banks cod fishery would still exist. The Atlantic bluefin tuna would not be endangered. The North Sea herring would never have collapsed. Every historical example of unregulated fishing ended in collapse because each individual fisher's rational choice is to catch as much as possible before the next fisher does.'",
         "The biologist assumes the self-regulation principle and shows that every historical example of its application resulted in fishery collapse.",
         "Assume: fishers self-regulate. Historical evidence: every unregulated fishery collapsed. Therefore self-regulation does not work. The official cannot explain the historical record under their principle."),
    ]
    for i, (domain, tier, ctx, txt, spk, desc) in enumerate(d1_2_extra):
        seq = len(d1_2_data) + i + 1
        rec = make_record(
            "D1.2", "Reductio ad absurdum", "good_tool", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Reductio ad absurdum",
                "pattern_description": desc,
                "formal_form": "Assume P. P entails Q. Q is absurd. Therefore not-P.",
                "why_wrong": None,
                "why_right": "Reductio tests a claim by its own standards. If a principle generates consequences the proponent cannot stomach, the principle needs revision.",
                "related_patterns": ["A3.1", "A5.1", "D1.5"],
                "counterpoint": "A sophisticated opponent might 'bite the bullet' and accept the derived consequence. The reductio is only as strong as the absurdity of the conclusion.",
            },
            {
                "identification_prompt": "One speaker takes the other's claim and does something specific with it. What technique is being used, and why is it effective?",
                "rubric": [
                    {"level": 0, "description": "Player cannot identify the technique or sees it as mere disagreement."},
                    {"level": 1, "description": "Player notices counterexamples but misses the assume-derive-reject structure."},
                    {"level": 2, "description": "Player sees the argument leads to absurd conclusions but cannot name the method."},
                    {"level": 3, "description": "Player identifies reductio: assume the position, derive absurd consequences, reject the original position."},
                    {"level": 4, "description": "Player identifies reductio, articulates the formal structure, and discusses when it succeeds versus when the opponent might bite the bullet."},
                ],
                "follow_up_if_wrong": "The respondent did not say the original claim was wrong directly. Instead, they assumed it was true and followed it somewhere specific. Where did it lead?",
                "follow_up_if_right": "What if the original speaker accepted the absurd consequence? Would the reductio still work?",
            },
            {
                "npc_personality": "Sharp, quick-witted, and skilled at following ideas to their logical conclusions.",
                "npc_dialogue_seed": "You believe that principle? Let us follow it and see where it takes us.",
                "resolution_path": "If the player identifies the reductio, they earn it as a dialogue tool for challenging over-broad principles.",
            },
            "Dennett Intuition Pumps + PHIL 201 lecture notes on reductio",
        )
        records.append(rec)

    # ================================================================
    # D1.3 — Occam's Razor (good_tool) x 50
    # ================================================================
    d1_3_data = [
        ("workplace", "drill", "The office printer keeps jamming. The IT specialist says the firmware has been hacked by a competitor. The receptionist points out the paper tray is overfilled.",
         "The receptionist opens the paper tray. 'Look — the tray holds 250 sheets and someone loaded 400. Every time it jams, it is the overfilled tray. We do not need a hacking theory to explain paper jams when the paper does not fit.'",
         "The receptionist offers a mechanical explanation requiring one known cause; the IT specialist posits corporate espionage with no evidence.",
         "The overfill hypothesis explains all jams with one observable cause. The hacking hypothesis requires a motive, technical capability, and access — none verified."),

        ("school", "drill", "A student's grades dropped suddenly. The school counselor suspects a complex learning disability. The student's friend mentions he started working night shifts.",
         "The friend says: 'He started working at the warehouse from eleven PM to six AM three weeks ago. He falls asleep in every class. Maybe he does not have a learning disability — maybe he is just exhausted.'",
         "Sleep deprivation from night shifts explains all symptoms with one known change.",
         "The night-shift hypothesis requires one new fact (the job). The learning disability hypothesis requires a neurological condition that has never manifested before."),

        ("healthcare", "drill", "A patient reports fatigue, weight gain, and cold sensitivity. A specialist suggests a rare autoimmune condition. The GP checks thyroid levels.",
         "The GP says: 'These are the three classic symptoms of hypothyroidism. Let me check your thyroid before we test for rare conditions. The common explanation should be ruled out first.'",
         "Hypothyroidism is a single common condition that explains all three symptoms.",
         "The thyroid hypothesis is one condition explaining three symptoms. The autoimmune hypothesis is rarer and requires additional mechanisms."),

        ("politics", "drill", "A local politician lost an election. His supporters claim the voting machines were hacked. His opponent's campaign manager notes the incumbent's approval rating was thirty-two percent.",
         "The campaign manager says: 'His approval was thirty-two percent. Two-thirds of voters disapproved of him. Do we really need a hacking theory to explain why the unpopular candidate lost?'",
         "Low approval directly explains electoral loss without requiring an elaborate conspiracy.",
         "The unpopularity hypothesis requires one documented fact. The hacking hypothesis requires undetected technical tampering with no evidence."),

        ("sports", "drill", "A soccer team lost five games in a row. The coach suspects the opponents are using illegal performance-enhancing drugs. The assistant coach notes the team's top three scorers are all injured.",
         "The assistant says: 'Our three best scorers are out with injuries. We have lost our primary offensive capability. We do not need a doping conspiracy to explain why we stopped winning.'",
         "Three key injuries explain the losing streak with known, documented causes.",
         "The injury hypothesis cites three verified facts. The doping hypothesis requires five separate teams to be independently doping."),

        ("cooking", "drill", "A baker's bread keeps coming out flat. She suspects the oven has a hidden malfunction. Her apprentice checks the yeast packet and finds it expired three months ago.",
         "The apprentice holds up the packet. 'The yeast expired in January. Dead yeast does not rise. Maybe the oven is fine and the leavening agent is dead.'",
         "Expired yeast is a single verifiable cause for flat bread.",
         "The expired-yeast hypothesis requires one check. The oven-malfunction hypothesis requires a hidden fault that does not affect other baked goods."),

        ("technology", "drill", "A website is running slowly. A junior developer suspects a distributed denial-of-service attack. A senior developer checks the server logs and finds an unoptimized database query running every second.",
         "The senior developer says: 'This query is scanning the entire user table every second instead of using an index. It is consuming ninety percent of server resources. We do not need a DDoS theory when our own code is the bottleneck.'",
         "An internal code inefficiency explains the slowdown with one verifiable cause.",
         "The unoptimized-query hypothesis is one internal cause. The DDoS hypothesis requires an external attacker with no evidence of unusual traffic patterns."),

        ("military", "drill", "Supply shipments keep arriving late. An officer suspects enemy sabotage of the supply line. A quartermaster checks the logistics schedule and finds the departure times were entered incorrectly.",
         "The quartermaster says: 'Someone entered the departure times in the wrong time zone. Every shipment left twelve hours late. It is not sabotage — it is a data entry error.'",
         "A clerical error explains all delays with one cause.",
         "The data-entry hypothesis requires one mistake. The sabotage hypothesis requires an infiltrator with access to supply schedules."),

        ("legal", "drill", "A contract dispute arises. One lawyer claims the other side deliberately inserted ambiguous language to commit fraud. The paralegal finds the ambiguity was copied from a standard template used industry-wide.",
         "The paralegal says: 'This exact language appears in the standard industry template from 2019. Every firm in the sector uses it. The ambiguity is not malicious — it is boilerplate nobody updated.'",
         "Template copying explains the ambiguity without requiring deliberate fraud.",
         "The template hypothesis requires one common practice. The fraud hypothesis requires deliberate intent and deception."),

        ("parenting", "drill", "A toddler suddenly refuses to eat vegetables. The parent suspects a rare sensory processing disorder. The pediatrician asks if the child recently tried a vegetable they disliked.",
         "The pediatrician says: 'Your child gagged on broccoli last Tuesday. Toddlers generalize — one bad experience with one vegetable becomes all vegetables. This is normal developmental behavior, not a disorder.'",
         "A single aversive experience explains the refusal through normal child development.",
         "The normal-development hypothesis requires one documented event. The sensory disorder hypothesis requires a neurological condition with no prior indicators."),

        ("music", "drill", "A guitarist's amp buzzes during performances. The guitarist suspects an internal circuit failure. A sound tech traces the buzz to a frayed cable.",
         "The tech holds up the cable. 'See this fray? The shielding is broken. That is your buzz. Try a new cable before we open up a working amplifier.'",
         "A frayed cable is a single visible cause for the buzz.",
         "The cable hypothesis requires one observable defect. The circuit-failure hypothesis requires an internal fault in a functioning amplifier."),

        ("gaming", "drill", "A player keeps losing at a strategy game and suspects the AI is cheating. Another player watches the replay and points out the losing player leaves their flanks exposed every game.",
         "The observer says: 'You left your right flank undefended in all three games. The AI is not cheating — it is exploiting your consistent mistake.'",
         "A recurring tactical error explains all losses without requiring AI cheating.",
         "The tactical-error hypothesis cites a pattern visible in replays. The AI-cheating hypothesis requires hidden code that cannot be verified."),

        ("agriculture", "drill", "Crops in one field are dying while neighboring fields thrive. The farmer suspects a new plant disease. A soil scientist tests the field and finds the pH is extremely acidic due to runoff from a nearby construction site.",
         "The scientist says: 'Your soil pH is 4.2 — extremely acidic. That construction runoff changed your soil chemistry. The plants are not diseased; they are being poisoned by acid.'",
         "Acidic runoff from a known source explains crop death with one measurable cause.",
         "The runoff hypothesis requires one testable measurement. The disease hypothesis requires a pathogen affecting only one field."),

        ("science", "drill", "A lab experiment produces unexpected results. A postdoc suspects a fundamental new phenomenon. The lab manager checks the equipment and finds the spectrometer was miscalibrated.",
         "The manager says: 'The spectrometer drifted by three nanometers during maintenance last week. Recalibrate it and run the experiment again before we claim a new discovery.'",
         "Equipment miscalibration is a known, common cause of unexpected results.",
         "The calibration hypothesis requires one verifiable check. The new-phenomenon hypothesis requires overturning established science."),

        ("retail", "drill", "Sales at a store dropped suddenly. The owner suspects a competitor is running a secret smear campaign. An employee notices the store's Google Maps listing was accidentally marked as permanently closed.",
         "The employee says: 'Our Google listing says we are permanently closed. Customers are not smearing us — they think we do not exist anymore.'",
         "A listing error explains the sales drop with one verifiable digital cause.",
         "The listing-error hypothesis requires one check. The smear-campaign hypothesis requires an organized, secret effort with no evidence."),

        ("relationships", "drill", "A partner suddenly becomes distant. The other partner suspects an affair. Their therapist asks if anything stressful happened at work recently, and the distant partner reveals they are facing layoffs.",
         "The therapist says: 'Job insecurity commonly causes emotional withdrawal. Your partner is not pulling away from you — they are consumed by anxiety about losing their livelihood. Let us address the work stress before we speculate about affairs.'",
         "Work stress explains emotional withdrawal with one known stressor.",
         "The work-stress hypothesis requires one documented event. The affair hypothesis requires secret behavior with no evidence."),

        ("finance", "drill", "A stock price drops ten percent. An investor suspects market manipulation. An analyst notes the company just reported earnings twenty percent below expectations.",
         "The analyst says: 'Earnings missed by twenty percent. The stock dropped ten percent. That is a normal market reaction to bad results. We do not need a manipulation theory.'",
         "Earnings miss explains the price drop through normal market mechanics.",
         "The earnings hypothesis requires one public data point. The manipulation hypothesis requires coordinated illegal activity."),

        ("travel", "drill", "A tourist's photos from a trip are all blurry. They suspect the camera has an internal defect. A photographer notices the lens has a smudge from sunscreen.",
         "The photographer wipes the lens. 'Sunscreen on the lens. Every photo goes through a greasy filter. Try it now.' The next photo is crystal clear.",
         "A lens smudge explains all blurry photos with one observable cause.",
         "The smudge hypothesis requires one visible check. The internal-defect hypothesis requires a fault in a functioning camera body."),

        ("environment", "drill", "Fish are dying in a local stream. A conspiracy theorist blames secret chemical dumping by a corporation. A biologist tests the water and finds the dissolved oxygen is critically low due to an algal bloom from agricultural fertilizer runoff.",
         "The biologist says: 'The dissolved oxygen is at two milligrams per liter — fish need five. The algal bloom from the fertilizer runoff consumed all the oxygen. This is a well-documented process called eutrophication. No secret dumping required.'",
         "Eutrophication from known fertilizer use explains the fish kill through documented science.",
         "The eutrophication hypothesis requires one measurable process. The secret-dumping hypothesis requires covert corporate activity with no evidence."),

        ("housing", "drill", "A new homeowner hears creaking at night and suspects the house is structurally unsound. An inspector finds the wood framing is expanding and contracting with temperature changes — normal for all wood-frame houses.",
         "The inspector says: 'Wood expands when it warms and contracts when it cools. Every wood-frame house creaks at night when the temperature drops. Your house is not failing — it is breathing.'",
         "Thermal expansion explains creaking through well-understood physics.",
         "The thermal-expansion hypothesis requires one known physical process. The structural-failure hypothesis requires a hidden defect that passed inspection."),

        ("journalism", "what_if", "A newspaper's circulation is declining. The editor suspects a coordinated advertiser boycott. The circulation manager shows that the decline matches the rate of growth in online news consumption in the region.",
         "The manager says: 'Online news readership in our area grew by exactly the amount our print circulation declined. People are not boycotting us — they are reading the same news on their phones. The medium is changing, not the loyalty.'",
         "Media migration explains the decline through a documented industry trend without requiring a conspiracy.",
         "The media-migration hypothesis matches a known macro trend. The boycott hypothesis requires coordinated action with no evidence."),

        ("theater", "what_if", "Ticket sales for a play are low. The director suspects a rival theater is spreading negative rumors. The box office manager notes the production was not listed in the local events guide due to a submission deadline missed.",
         "The manager says: 'We missed the events guide deadline. Sixty percent of our first-week sales come from that listing. No one is badmouthing us — no one knows we exist this week.'",
         "A missed listing explains low sales through one known omission.",
         "The missed-listing hypothesis requires one verifiable fact. The rumor-spreading hypothesis requires an organized campaign with no evidence."),

        ("archaeology", "what_if", "An unusual artifact is found at a dig site. A visitor suggests it proves contact with an advanced lost civilization. The site archaeologist identifies it as a trade item from a known neighboring culture documented in historical records.",
         "The archaeologist says: 'This pottery style is well-documented in the Keshani trade network. We have records of trade routes, invoices, and similar artifacts at six other sites. We do not need a lost civilization when a known one with a documented trade route explains the artifact perfectly.'",
         "A documented trade network explains the artifact with known historical evidence.",
         "The trade hypothesis cites six comparative sites and historical records. The lost-civilization hypothesis requires an undiscovered society with no other evidence."),

        ("maritime", "what_if", "A ship's navigation instruments show inconsistent readings. The captain suspects solar flare interference with the electronic systems. The first officer finds a large magnet stored near the compass by a crew member who was using it for fishing.",
         "The first officer holds up the magnet. 'Someone left a rare-earth magnet next to the compass. That explains the inconsistent readings. Move the magnet, recalibrate, and I bet the instruments are fine.'",
         "A nearby magnet explains compass inconsistency through basic physics.",
         "The magnet hypothesis requires one observable object. The solar-flare hypothesis requires an astronomical event with no corroborating reports."),

        ("firefighting", "what_if", "A fire department's response times have increased. The chief suspects a new traffic pattern from road construction is adding delays. A data analyst finds that the dispatch software update last month added an extra confirmation step that adds ninety seconds per call.",
         "The analyst says: 'Every call since the software update has an extra ninety-second confirmation step. That accounts for exactly the increase in response times. The roads are the same — the software changed.'",
         "A software change explains the timing increase with one verifiable modification.",
         "The software hypothesis requires one documented change. The traffic hypothesis requires mapping new traffic patterns across multiple routes."),

        ("workplace", "what_if", "Employee morale has dropped across the company. The CEO suspects a disgruntled employee is spreading negativity. HR finds the company just eliminated annual bonuses without explanation.",
         "HR director says: 'We cut bonuses last month with a one-line email and no explanation. Every department's engagement scores dropped the following week. We do not need a troublemaker theory when the company's own decision explains the morale drop.'",
         "The bonus-cut hypothesis explains company-wide morale decline with one known management decision.",
         "The bonus hypothesis requires one documented policy change. The agitator hypothesis requires an individual influencing the entire company simultaneously."),

        ("school", "what_if", "Attendance at a university lecture series has declined by forty percent. The dean suspects students have lost interest in the subject. An assistant notes the lectures were moved from a central campus building to one across town requiring a thirty-minute bus ride.",
         "The assistant says: 'The lectures moved from the main building to the annex. Students have to take a thirty-minute bus. Interest in the subject did not change — accessibility did.'",
         "A location change explains attendance decline through increased inconvenience.",
         "The location hypothesis requires one known change. The lost-interest hypothesis requires a shift in student attitudes with no evidence."),

        ("healthcare", "what_if", "A hospital ward has a spike in patient infections. The infection control officer suspects a resistant pathogen. A nurse notices the hand sanitizer dispensers have been empty for two weeks because of a supplier backorder.",
         "The nurse says: 'The dispensers have been empty for two weeks. No sanitizer, more infections. It is not a superbug — it is an empty dispenser.'",
         "Empty sanitizer dispensers explain the infection spike through a known lapse in hygiene protocol.",
         "The dispenser hypothesis requires one supply-chain fact. The resistant-pathogen hypothesis requires a new organism with no laboratory confirmation."),

        ("politics", "what_if", "A political party's poll numbers have dropped. Party leadership suspects media bias. A pollster notes the party's most popular policy position was reversed two weeks before the poll.",
         "The pollster says: 'You reversed your most popular policy. Your supporters who liked that policy now say they are undecided. The media did not change — your platform did.'",
         "A policy reversal explains poll decline through a known, self-inflicted change.",
         "The policy-reversal hypothesis requires one documented decision. The media-bias hypothesis requires coordinated negative coverage with no evidence of coordination."),

        ("sports", "what_if", "A baseball team's hitting has declined dramatically. The manager suspects the opposing pitchers have gotten better mid-season. A batting coach reviews video and finds every hitter has developed the same timing flaw after the team changed its batting practice pitch machine.",
         "The coach says: 'The new pitch machine throws five miles per hour slower than game pitching. Every hitter has grooved their timing to the slower speed. Change the machine back and the timing will correct.'",
         "A practice equipment change explains the hitting decline through a single mechanical cause.",
         "The machine hypothesis requires one verifiable equipment change. The opponent-improvement hypothesis requires every opposing team to have simultaneously improved."),

        ("cooking", "what_if", "All dishes from a restaurant kitchen taste bland this week. The head chef suspects the spice supplier sent inferior products. A line cook discovers the kitchen's ventilation system was serviced and the exhaust fan is now pulling flavors out of pans during cooking.",
         "The cook says: 'The new fan is three times stronger than the old one. It is literally pulling the aromatics out of the food before they can develop. Dial it down and taste the difference.'",
         "Excessive ventilation explains bland flavors across all dishes with one mechanical cause.",
         "The ventilation hypothesis requires one verifiable change. The inferior-spice hypothesis requires a supplier switch that did not happen."),

        ("technology", "what_if", "Users report that a mobile app crashes every afternoon around two PM. The developer suspects a server-side bug triggered by time zones. A QA tester finds the app crashes when the phone's battery drops below fifteen percent, which happens around two PM because users charge overnight and use the phone all morning.",
         "The tester says: 'It is not a time bug — it is a battery bug. The crash correlates with battery level, not clock time. Two PM is just when batteries hit fifteen percent.'",
         "A battery-threshold bug explains the crash pattern with one testable correlation.",
         "The battery hypothesis is testable by changing battery levels at different times. The time-zone hypothesis requires a server-side error with no server logs showing it."),

        ("military", "what_if", "Encrypted radio communications keep failing. An officer suspects the enemy has cracked the encryption. A technician finds the radio operators have been accidentally transmitting on an unencrypted backup frequency.",
         "The technician says: 'The frequency selector was set to backup after last week's maintenance and no one switched it back. They are not cracking our encryption — we are not using it.'",
         "A misconfigured frequency selector explains the security failure with one physical switch position.",
         "The misconfiguration hypothesis requires one switch check. The cracked-encryption hypothesis requires the enemy to have overcome military-grade cryptography."),

        ("legal", "what_if", "A witness's testimony contradicts their earlier deposition. The opposing counsel alleges perjury. The witness's attorney shows the court reporter made a transcription error in the deposition, and the original recording matches the testimony.",
         "The attorney says: 'The deposition transcript has a transcription error on page twelve. The audio recording matches the testimony exactly. There is no contradiction — there is a typo.'",
         "A transcription error explains the apparent contradiction with one verifiable cause.",
         "The transcription-error hypothesis is verifiable against the audio. The perjury hypothesis requires deliberate deception with no motive."),

        ("parenting", "what_if", "A child suddenly becomes afraid of dogs after years of loving them. The parent suspects a traumatic event at school. The child's older sibling admits they showed the child a scary movie about a vicious dog last weekend.",
         "The sibling says: 'I showed her the movie. The dog in it was terrifying. She had nightmares that night. I think that is why she is afraid of real dogs now.'",
         "A scary movie experience explains the fear onset with one identified event.",
         "The movie hypothesis requires one confirmed viewing. The school-trauma hypothesis requires an unreported event with no witnesses."),

        ("agriculture", "puzzle", "Bees are avoiding one particular field despite it being full of flowers. A local conspiracy theorist blames 5G cell towers. An entomologist discovers the farmer applied a neonicotinoid pesticide that repels bees at sub-lethal concentrations.",
         "The entomologist says: 'Neonicotinoids are documented bee repellents at low concentrations. You sprayed last Tuesday. The bees are not avoiding cell towers — they are avoiding poison.'",
         "A documented chemical repellent explains bee avoidance through known entomology.",
         "The pesticide hypothesis requires one verified application. The 5G hypothesis requires an undemonstrated physical mechanism."),

        ("science", "puzzle", "An astronomy student spots an unusual light in telescope data. A professor on social media claims it is evidence of an alien megastructure. The student's advisor identifies it as a known variable star with irregular dimming patterns, documented in three previous surveys.",
         "The advisor says: 'This star is KIC 8462852. Its dimming pattern has been studied for a decade. The leading explanations are dust clouds and cometary debris. We do not need aliens when known astrophysical processes explain the data.'",
         "Known stellar phenomena explain the observation without requiring alien technology.",
         "The variable-star hypothesis draws on three prior surveys and documented mechanisms. The alien-megastructure hypothesis requires technology with no precedent."),

        ("retail", "puzzle", "A store's inventory management system shows products vanishing from shelves with no sales records. The owner suspects organized shoplifting. The system administrator finds the barcode scanner firmware was not updated and is miscounting restocks.",
         "The admin says: 'The scanner is running old firmware that miscounts items during restock. The products are being sold — they are just not being counted when they arrive. Fix the firmware and the inventory will match.'",
         "A firmware bug explains the inventory discrepancy with one verifiable software issue.",
         "The firmware hypothesis requires one software check. The organized-shoplifting hypothesis requires a criminal operation with no security camera evidence."),

        ("relationships", "puzzle", "A couple notices they argue every Sunday evening. One partner suspects the other is deliberately provoking fights to avoid intimacy. A therapist identifies that Sunday evenings coincide with the arrival of a joint credit card statement.",
         "The therapist says: 'Your credit card statement arrives every Sunday. You argue about spending every Sunday. The fights are not about intimacy avoidance — they are about financial stress triggered by a predictable external event.'",
         "A recurring financial trigger explains the argument pattern with one identifiable environmental cause.",
         "The credit-card hypothesis requires one verifiable correlation. The intimacy-avoidance hypothesis requires a complex psychological motive with no other supporting evidence."),

        ("finance", "puzzle", "A trader's algorithm keeps losing money on Fridays. She suspects competitors are front-running her orders. A data scientist finds the algorithm does not account for reduced Friday trading volume, which amplifies price impact.",
         "The scientist says: 'Friday volume is forty percent lower. Your order size relative to volume is too large on Fridays, moving the price against you. Competitors are not stealing your edge — your algorithm is ignoring the calendar.'",
         "Reduced Friday volume explains the losses through a known market microstructure effect.",
         "The volume hypothesis is testable by adjusting order size on Fridays. The front-running hypothesis requires coordinated illegal activity with no regulatory evidence."),

        ("environment", "puzzle", "A rare bird species has disappeared from a nature reserve. Locals blame poachers. A wildlife biologist discovers the birds' primary food source — a specific insect species — has been eliminated by a new invasive ant that was accidentally introduced by a well-meaning conservation group.",
         "The biologist says: 'The invasive ant eliminated the birds' food source. No food, no birds. The conservation group introduced the ant last year as a biological control for a different pest. Poachers did not take the birds — the food chain collapsed under them.'",
         "Food chain disruption from a documented introduction explains the bird disappearance.",
         "The food-chain hypothesis requires one verified ant introduction. The poaching hypothesis requires extensive illegal hunting with no evidence of carcasses or traps."),

        ("housing", "puzzle", "Several houses in a new development are developing cracks. The developer suspects an earthquake that went undetected. A structural engineer finds that the foundation concrete was mixed with too much water, a cost-cutting measure by the subcontractor.",
         "The engineer says: 'The water-to-cement ratio in these foundations is 0.8 — it should be 0.45. The concrete is too weak. This is not seismic — it is substandard construction. Every affected house used the same subcontractor.'",
         "Incorrect concrete mix explains the cracks with one verifiable material defect traceable to one subcontractor.",
         "The concrete hypothesis is testable through core samples. The earthquake hypothesis requires a seismic event with no seismographic record."),

        ("gaming", "puzzle", "A multiplayer game's servers crash every evening at peak hours. The development team suspects a sophisticated DDoS attack. A network engineer finds that a background analytics process runs a full database backup every evening at 7 PM, consuming all server bandwidth.",
         "The engineer says: 'The analytics backup starts at 7 PM — exactly when the crashes start. It copies the entire database across the network. Kill the backup during peak hours and the servers will be fine.'",
         "A scheduled internal process explains the crashes with one verifiable system configuration.",
         "The backup hypothesis requires one cron job check. The DDoS hypothesis requires an attacker with no evidence in network logs."),

        ("journalism", "puzzle", "A newspaper receives multiple angry letters about a particular article. The editor suspects an organized campaign by a political group. A data analyst finds that all the letters use the same misspelling of the journalist's name, which appears in the online comment section's auto-populated complaint form — the letters were generated by a form that misspelled the name.",
         "The analyst says: 'Every letter misspells the name the same way. That is not coordinated outrage — it is a complaint form with a typo. People clicked a button and a pre-filled letter was sent. The volume reflects the ease of clicking, not the depth of anger.'",
         "A pre-filled complaint form explains the letter volume with one verifiable digital mechanism.",
         "The form hypothesis explains the identical misspelling. The organized-campaign hypothesis does not explain why a sophisticated campaign would misspell the target's name."),

        ("travel", "puzzle", "A hotel's reviews suddenly dropped from 4.5 to 3.0 stars. The owner suspects a competitor is posting fake negative reviews. A manager discovers the hotel's hot water heater broke three weeks ago and guests have been taking cold showers.",
         "The manager says: 'Every negative review in the last three weeks mentions cold water. The water heater broke on the fifteenth. Fix the heater and the reviews will recover.'",
         "A broken water heater explains the review decline with one verifiable maintenance issue.",
         "The water-heater hypothesis explains the specific content of every negative review. The fake-review hypothesis cannot explain why a competitor would consistently mention cold water."),

        ("music", "puzzle", "A concert hall's acoustics suddenly sound different. The music director suspects structural settling has changed the room's resonance. An acoustic engineer discovers the cleaning crew replaced the felt seat cushions with vinyl covers for easier maintenance.",
         "The engineer says: 'Felt absorbs mid-range frequencies. Vinyl reflects them. You changed every seat cover in the hall. The structure did not move — the absorption coefficient of the seating changed.'",
         "A material change in seat covers explains the acoustic change with one verifiable modification.",
         "The seat-cover hypothesis requires one documented maintenance change. The structural-settling hypothesis requires undetectable building movement."),
    ]

    for i, (domain, tier, ctx, txt, spk, desc) in enumerate(d1_3_data):
        seq = i + 1
        rec = make_record(
            "D1.3", "Occam's Razor", "good_tool", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Occam's Razor",
                "pattern_description": desc,
                "formal_form": "H1 and H2 explain the same evidence. H1 posits fewer entities and mechanisms. Prefer H1 unless H2 offers additional explanatory power H1 lacks.",
                "why_wrong": None,
                "why_right": "Simpler explanations are preferred because each additional assumption is an additional point of potential failure. The simpler hypothesis is also typically more testable.",
                "related_patterns": ["D1.4", "E1.2", "A8.1"],
                "counterpoint": "Occam's Razor does not prove the simpler explanation is true. Sometimes reality is complex. The razor says: do not multiply entities beyond necessity.",
            },
            {
                "identification_prompt": "Two explanations are offered for the same phenomenon. What principle should guide your choice, and which explanation does it favor?",
                "rubric": [
                    {"level": 0, "description": "Player favors the more complex explanation."},
                    {"level": 1, "description": "Player prefers the simpler explanation but cannot articulate why."},
                    {"level": 2, "description": "Player says simpler is better but cannot explain what makes one explanation simpler."},
                    {"level": 3, "description": "Player invokes parsimony: prefer the explanation with fewer unsupported assumptions."},
                    {"level": 4, "description": "Player articulates Occam's Razor, explains that each additional assumption increases failure risk, notes testability, and identifies when the more complex hypothesis might be warranted."},
                ],
                "follow_up_if_wrong": "Both explanations account for the evidence. But one requires you to believe in things we have no evidence for. Which one, and how many extra assumptions does it add?",
                "follow_up_if_right": "Suppose the simple explanation was tested and ruled out. Does the complex explanation automatically win? Or should you look for another simple explanation first?",
            },
            {
                "npc_personality": "Practical, observant, and inclined to check the obvious before theorizing.",
                "npc_dialogue_seed": "Before we go looking for complicated answers, have we checked the simple ones?",
                "resolution_path": "If the player favors parsimony, they earn Occam's Razor as an investigative tool for future encounters.",
            },
            "Dennett Intuition Pumps Ch. 2 + PHIL 201 lecture notes",
        )
        records.append(rec)

    # Pad D1.3 to 50
    d1_3_extra = [
        ("journalism", "puzzle", "A newspaper's website traffic surged but subscription revenue dropped. The publisher suspects hackers are stealing content. The webmaster discovers the paywall code broke in the last update, making all articles free.",
         "The webmaster says: 'The paywall broke on the fifteenth. Traffic surged because everything is free. Revenue dropped because nobody is paying. Fix the code and both metrics normalize.'",
         "A broken paywall explains both the traffic surge and revenue drop with one software bug.",
         "The paywall-bug hypothesis explains both metrics with one event. The hacking hypothesis requires sophisticated content theft with no evidence."),

        ("theater", "puzzle", "Audience complaints about uncomfortable seating doubled after a renovation. The theater director suspects the new seats are defective. A stagehand notices the seat pitch was reduced by two inches to add an extra row.",
         "The stagehand says: 'Two fewer inches per row. Every seat is two inches closer to the row in front. Knees hit seatbacks. The seats are not defective — there are just too many of them.'",
         "A reduced seat pitch explains all comfort complaints with one measurable change.",
         "The seat-pitch hypothesis requires one measurement. The defective-seat hypothesis requires a manufacturing fault in seats that passed quality control."),

        ("archaeology", "puzzle", "An artifact's radiocarbon date does not match the stratigraphy. A visiting researcher suggests the dating technique is fundamentally flawed. The lab technician finds that the sample was contaminated by modern rootlets that penetrated the burial layer.",
         "The technician says: 'Modern rootlets grew through the sample. Modern carbon shifts the date. Remove the rootlets, re-date, and the result will match the stratigraphy.'",
         "Root contamination explains the dating anomaly with one biological process.",
         "The contamination hypothesis requires one verifiable sample issue. The flawed-technique hypothesis requires overturning decades of validated science."),

        ("maritime", "puzzle", "A ship's fuel consumption increased by fifteen percent. The chief engineer suspects engine degradation. A diver inspects the hull and finds heavy biofouling — barnacles and algae covering the waterline.",
         "The diver surfaces: 'The hull below the waterline is covered in barnacles. That drag increases fuel consumption exactly the amount you are seeing. Clean the hull and check the numbers again before we tear apart a working engine.'",
         "Hull biofouling explains the fuel increase through well-understood hydrodynamics.",
         "The biofouling hypothesis requires one visual inspection. The engine-degradation hypothesis requires internal mechanical failure in a recently serviced engine."),
    ]
    for i, (domain, tier, ctx, txt, spk, desc) in enumerate(d1_3_extra):
        seq = len(d1_3_data) + i + 1
        rec = make_record(
            "D1.3", "Occam's Razor", "good_tool", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Occam's Razor",
                "pattern_description": desc,
                "formal_form": "H1 and H2 explain the same evidence. H1 posits fewer entities and mechanisms. Prefer H1 unless H2 offers additional explanatory power H1 lacks.",
                "why_wrong": None,
                "why_right": "Simpler explanations are preferred because each additional assumption is an additional point of potential failure. The simpler hypothesis is also typically more testable.",
                "related_patterns": ["D1.4", "E1.2", "A8.1"],
                "counterpoint": "Occam's Razor does not prove the simpler explanation is true. Sometimes reality is complex. The razor says: do not multiply entities beyond necessity.",
            },
            {
                "identification_prompt": "Two explanations are offered for the same phenomenon. What principle should guide your choice, and which explanation does it favor?",
                "rubric": [
                    {"level": 0, "description": "Player favors the more complex explanation."},
                    {"level": 1, "description": "Player prefers the simpler explanation but cannot articulate why."},
                    {"level": 2, "description": "Player says simpler is better but cannot explain what makes one explanation simpler."},
                    {"level": 3, "description": "Player invokes parsimony: prefer the explanation with fewer unsupported assumptions."},
                    {"level": 4, "description": "Player articulates Occam's Razor, explains that each additional assumption increases failure risk, notes testability, and identifies when the more complex hypothesis might be warranted."},
                ],
                "follow_up_if_wrong": "Both explanations account for the evidence. But one requires you to believe in things we have no evidence for. Which one?",
                "follow_up_if_right": "Suppose the simple explanation was tested and ruled out. Does the complex one automatically win?",
            },
            {
                "npc_personality": "Practical, observant, and inclined to check the obvious before theorizing.",
                "npc_dialogue_seed": "Before we go looking for complicated answers, have we checked the simple ones?",
                "resolution_path": "If the player favors parsimony, they earn Occam's Razor as an investigative tool.",
            },
            "Dennett Intuition Pumps Ch. 2 + PHIL 201 lecture notes",
        )
        records.append(rec)

    # ================================================================
    # D1.4 — Occam's Broom (bad_thinking) x 50
    # ================================================================
    d1_4_contexts = [
        ("workplace", "drill", "A manager presents only positive quarterly results while ignoring three departments that missed targets.",
         "Manager Byrne shows the board a chart of revenue growth. 'As you can see, Q3 was outstanding. Sales up twelve percent, customer acquisition up eight percent.' She does not mention that fulfillment costs rose thirty percent, two product lines were discontinued, and customer retention dropped to a five-year low. A junior analyst who prepared the full report watches in disbelief as Byrne presents the highlights and hides the lowlights.",
         "Byrne sweeps unfavorable data under the rug to make the quarter look better than it was.",
         "Byrne presents {revenue growth, customer acquisition} and hides {fulfillment costs, discontinued products, retention decline}. The picture looks positive only because the negative evidence is concealed."),

        ("school", "drill", "A principal presents only high test scores while omitting dropout rates and absenteeism data.",
         "Principal Heath addresses parents: 'Our math scores are in the top ten percent of the district. Our reading scores have improved for three consecutive years.' She does not mention that the dropout rate has doubled, chronic absenteeism affects thirty percent of students, and the high scores partly reflect that struggling students have left the school. A teacher who raised these concerns at a staff meeting was told they were 'off-message.'",
         "Heath sweeps inconvenient data about the student population under the rug to make the school look successful.",
         "Heath presents {math scores, reading improvement} and hides {dropout rate, absenteeism, selection bias in scores}. The success narrative only holds because the evidence of failure is concealed."),

        ("healthcare", "drill", "A pharmaceutical rep presents only favorable trial results while omitting adverse event data.",
         "Rep Stanton shows Dr. Kaur a glossy slide: 'In the Phase III trial, the drug reduced symptoms by forty percent compared to placebo.' He does not mention that four percent of participants experienced liver toxicity, that the trial excluded patients over sixty-five, and that the symptom reduction was measured at week four but had disappeared by week twelve. Dr. Kaur asks about side effects and Stanton changes the subject.",
         "Stanton sweeps adverse data under the rug to make the drug appear safer and more effective than the full evidence shows.",
         "Stanton presents {symptom reduction at week four} and hides {liver toxicity, age exclusion, disappearing effect at week twelve}."),

        ("politics", "drill", "A mayor presents only crime statistics that declined while omitting categories where crime increased.",
         "Mayor Voss stands at a podium: 'Violent crime is down nine percent. Burglary is down fourteen percent. Our streets are safer than they have been in a decade.' She does not mention that domestic violence reports increased twenty-two percent, fraud cases doubled, and drug offenses rose thirty percent. A journalist who filed a freedom-of-information request for the full report finds the categories Voss omitted.",
         "Voss uses Occam's Broom on crime statistics, presenting only the declining categories.",
         "Voss presents {violent crime down, burglary down} and hides {domestic violence up, fraud up, drug offenses up}. Public safety looks improved only because worsening categories are concealed."),

        ("sports", "drill", "A team's marketing highlights only wins and records while omitting injuries and player complaints.",
         "The team's annual report celebrates: 'Season highlights include twelve wins, a new attendance record, and two playoff appearances.' It does not mention five season-ending injuries, three player grievances filed with the league, and a coaching misconduct investigation. A reporter who obtained the players' union filing notices the report reads like a highlight reel with the lowlights deleted.",
         "The marketing team sweeps player welfare issues under the rug to present an unblemished season narrative.",
         "The report presents {wins, attendance, playoffs} and hides {injuries, grievances, misconduct investigation}."),

        ("cooking", "drill", "A restaurant owner promotes only positive reviews while hiding health inspection violations.",
         "Owner Marsh has plastered the window with five-star reviews. 'Best pasta in the city!' 'Amazing service!' Inside, the kitchen has failed its last two health inspections for rodent droppings and improper food storage temperatures. When a customer asks about the health rating, Marsh says: 'Reviews speak louder than bureaucratic checklists.'",
         "Marsh sweeps health inspection data under the rug, presenting only the evidence that favors the restaurant.",
         "Marsh presents {positive reviews} and hides {failed health inspections, rodent findings, temperature violations}."),

        ("technology", "drill", "A startup pitches to investors showing user growth while hiding churn rates and burn rate.",
         "CEO Lark presents: 'We added fifty thousand users last quarter. Monthly active users are up forty percent. The growth trajectory is exponential.' She does not mention that thirty-five thousand of those users churned within the first month, that the cost of acquiring each user is three times their lifetime value, and that the company has six months of runway left. An investor who asks about retention is told: 'We are focused on growth right now.'",
         "Lark sweeps churn, unit economics, and runway data under the rug to present a growth-only narrative.",
         "Lark presents {user growth, MAU increase} and hides {churn, negative unit economics, limited runway}."),

        ("military", "drill", "A general reports only territory gained while omitting casualty figures and supply problems.",
         "General Harmon reports to the war council: 'We have advanced twelve miles, captured two strategic bridges, and secured the eastern ridge.' He does not mention that the advance cost three hundred casualties, that supply lines are stretched beyond capacity, and that the two captured bridges are too damaged to support heavy equipment. A logistics officer who tried to include these facts in the briefing was told: 'The council wants to hear about progress.'",
         "Harmon sweeps casualty and logistics data under the rug to present an advance-only narrative.",
         "Harmon presents {territory gained, bridges captured} and hides {casualties, supply strain, bridge damage}."),

        ("legal", "drill", "A prosecutor presents only eyewitness testimony while omitting forensic evidence that contradicts it.",
         "Prosecutor Venn tells the jury: 'Three eyewitnesses independently identified the defendant at the scene. Their testimony is clear, consistent, and compelling.' She does not mention that the DNA found at the scene does not match the defendant, that the security camera footage is inconclusive, and that one eyewitness initially described someone of a different height and build. Defense counsel objects that the prosecution is presenting a selective picture.",
         "Venn sweeps contradictory forensic evidence under the rug to build a case on eyewitness testimony alone.",
         "Venn presents {three eyewitness IDs} and hides {non-matching DNA, inconclusive footage, inconsistent initial description}."),

        ("parenting", "drill", "A parent tells a therapist only about their child's academic success while omitting social and emotional struggles.",
         "Mother: 'Jake is doing beautifully. Straight A's, teacher's favorite, reading two grade levels ahead.' She does not mention that Jake has no friends, cries every morning before school, and told his sister he feels invisible. The therapist, seeing only the picture the mother presents, almost misses the emotional crisis.",
         "The mother sweeps Jake's social and emotional data under the rug, presenting only the academic evidence.",
         "Mother presents {grades, teacher approval, reading level} and hides {isolation, daily distress, emotional statements}."),

        ("music", "what_if", "A music label promotes an artist's streaming numbers while hiding declining live attendance and negative critical reception.",
         "The label's press release reads: 'Artist XYZ crossed one billion streams this year.' It does not mention that live ticket sales have dropped sixty percent, that three major music publications gave the latest album two stars, and that the artist's social media engagement has plummeted. A music journalist who attends a half-empty concert notices the disconnect between the streaming narrative and reality.",
         "The label sweeps live and critical evidence under the rug to present a streaming-only success story.",
         "The label presents {streaming numbers} and hides {declining live attendance, negative reviews, social media decline}."),

        ("gaming", "what_if", "A game publisher touts sales figures while hiding player retention data and refund rates.",
         "The publisher announces: 'Three million copies sold in the first week!' They do not mention that the average play session is eighteen minutes, that the Steam refund rate is forty percent, and that the player review score is twenty-three percent positive. A gaming journalist who checks the review aggregator sees a very different picture from the sales press release.",
         "The publisher sweeps player engagement and satisfaction data under the rug.",
         "Publisher presents {sales volume} and hides {session length, refund rate, review score}."),

        ("agriculture", "what_if", "A pesticide company presents crop yield increases while hiding soil degradation and pollinator impact data.",
         "Company rep: 'Farms using our product see twenty-five percent yield increases in the first year.' He does not mention that yields decline after year three as soil microbiome is damaged, that pollinator visits drop eighty percent, and that the product has been banned in six countries. A farmer who reads the banned-substances list notices the company's product on it.",
         "The rep sweeps long-term soil and pollinator data under the rug to present a yield-only narrative.",
         "Rep presents {year-one yield increase} and hides {soil degradation, pollinator decline, international bans}."),

        ("science", "what_if", "A researcher presents only the experiments that support their hypothesis while omitting null results.",
         "Dr. Lune publishes a paper showing three experiments that support her hypothesis. She does not mention the four experiments that produced null results, that her sample size was too small for the statistical test she used, and that a collaborator's attempted replication failed. Peer reviewers who only see the published paper cannot evaluate the full evidence.",
         "Dr. Lune sweeps null results, sample size issues, and failed replications under the rug — a form of publication bias.",
         "Lune presents {three supporting experiments} and hides {four null results, inadequate sample size, failed replication}."),

        ("retail", "what_if", "A company advertises a product's best-in-class feature while hiding its worst-in-class reliability.",
         "The ad reads: 'Fastest processor in its class!' It does not mention that the device has the highest failure rate, the shortest battery life, and the lowest customer satisfaction score in its class. A consumer who buys based on the ad discovers the hidden trade-offs after purchase.",
         "The company sweeps reliability, battery, and satisfaction data under the rug to highlight one favorable metric.",
         "Company presents {processor speed} and hides {failure rate, battery life, satisfaction score}."),

        ("relationships", "what_if", "A person on a dating profile highlights achievements while hiding relevant personal circumstances.",
         "Profile: 'MBA, marathon runner, world traveler, fluent in three languages.' Not mentioned: currently going through a contentious divorce, has a restraining order from an ex, and has not held a job in two years. A date who discovers these facts later feels manipulated — the profile was not lying, but it was sweeping crucial context away.",
         "The profile user sweeps relationship history and employment status under the rug.",
         "Profile presents {achievements} and hides {divorce, restraining order, unemployment}. The picture is accurate but radically incomplete."),

        ("finance", "what_if", "A fund manager reports only the fund's best-performing months while hiding the worst.",
         "Manager: 'In each of the last three Januarys, our fund outperformed the market by twelve percent.' He does not mention that the fund underperformed the market in nine of the last twelve months, that the overall annual return is below the index, and that fees eat most of the gains. An investor who checks the full track record sees a very different picture.",
         "The manager cherry-picks the best months and sweeps the full-year performance under the rug.",
         "Manager presents {three Januarys} and hides {nine underperforming months, below-index annual return, fee impact}."),

        ("travel", "what_if", "A travel agency promotes a destination's beaches and restaurants while hiding safety advisories and infrastructure problems.",
         "Brochure: 'Crystal clear waters, world-class dining, five-star resorts.' Not mentioned: the country is under a Level 3 travel advisory, the tap water is not potable, and the nearest hospital is four hours away. A traveler who gets sick discovers the information the brochure swept away.",
         "The agency sweeps safety and infrastructure data under the rug to present a paradise-only image.",
         "Agency presents {beaches, dining, resorts} and hides {travel advisory, water quality, hospital distance}."),

        ("environment", "what_if", "An oil company presents its renewable energy investment while hiding its fossil fuel expansion plans.",
         "CEO: 'We invested five hundred million in solar this year.' She does not mention that the company invested twelve billion in new oil exploration, that carbon emissions increased eight percent, and that the solar investment is three percent of the fossil fuel budget. A climate reporter who reads the annual SEC filing sees the full picture.",
         "The CEO sweeps the fossil fuel expansion under the rug and foregrounds the smaller renewable investment.",
         "CEO presents {$500M solar} and hides {$12B oil exploration, 8% emission increase, 3% renewable share}."),

        ("housing", "what_if", "A developer promotes a building's amenities while hiding structural deficiencies discovered during inspection.",
         "Developer brochure: 'Rooftop pool, concierge service, smart-home integration, pet-friendly.' Not mentioned: the foundation has documented settling, the electrical system failed two code inspections, and three units have persistent mold behind the walls. A buyer who hires an independent inspector discovers what the developer swept away.",
         "The developer sweeps structural and safety deficiencies under the rug to present an amenity-focused sales pitch.",
         "Developer presents {amenities} and hides {foundation settling, electrical failures, mold}."),

        ("journalism", "what_if", "A journalist writes a feature about a charity's impact while omitting financial irregularities uncovered during research.",
         "The article celebrates: 'The charity has built twelve schools and vaccinated forty thousand children.' The journalist's own research notes include: the CEO's salary is five times the industry average, thirty percent of donations go to 'administrative costs' that cannot be itemized, and a former board member alleged financial mismanagement. The editor asked for a 'positive story' and the journalist complied.",
         "The journalist sweeps financial concerns under the rug at editorial direction, presenting an impact-only narrative.",
         "Article presents {schools built, vaccinations} and hides {executive pay, unitemized costs, mismanagement allegations}."),

        ("theater", "what_if", "A theater company promotes rave audience reactions while hiding that the cast is performing under unsafe working conditions.",
         "Press release: 'Standing ovations at every performance! Critics call it the show of the year!' Not mentioned: the flying rig has not been inspected, two actors have reported injuries from faulty set pieces, and the stage manager filed a safety complaint with the labor board. An arts journalist who visits backstage discovers conditions very different from the press release.",
         "The company sweeps safety violations under the rug to present a success-only narrative to the public.",
         "Company presents {audience reactions, critical praise} and hides {uninspected equipment, injuries, safety complaint}."),

        ("archaeology", "what_if", "A museum presents artifacts from a collection while hiding their contested provenance.",
         "Museum catalog: 'Rare Bronze Age ceremonial vessels, exquisitely preserved.' Not mentioned: the acquisition records are incomplete, two source countries have filed repatriation claims, and an academic paper argues the artifacts were looted during wartime. A visiting scholar who checks the provenance database finds gaps the museum's public materials do not acknowledge.",
         "The museum sweeps provenance concerns under the rug to present an unblemished collection narrative.",
         "Museum presents {artifact quality, preservation} and hides {incomplete records, repatriation claims, looting evidence}."),

        ("maritime", "drill", "A shipping company promotes its on-time delivery rate while hiding its environmental compliance violations.",
         "Annual report: 'Ninety-eight percent on-time delivery — best in the industry.' Not mentioned: three vessels received fines for illegal waste dumping, fuel quality testing was falsified on twelve voyages, and the company's carbon intensity is the worst among major carriers. A regulatory analyst who cross-references the delivery data with environmental enforcement records sees the full picture.",
         "The company sweeps environmental violations under the rug to present a delivery-performance-only narrative.",
         "Company presents {delivery rate} and hides {dumping fines, falsified fuel tests, carbon intensity}."),

        ("firefighting", "drill", "A fire department promotes its rescue statistics while hiding response time failures in underserved neighborhoods.",
         "Chief's annual report: 'We completed 847 rescues this year — a department record.' Not mentioned: response times in the east district average fourteen minutes versus five minutes in the west, two residents in the east district died waiting for response, and the union filed a staffing complaint about east district coverage. A city councillor who represents the east district reads the report and wonders why her constituents' experience is invisible.",
         "The chief sweeps geographic disparity data under the rug to present a department-wide success narrative.",
         "Chief presents {total rescues} and hides {east district response times, deaths during delays, staffing complaint}."),

        ("workplace", "what_if", "A company's diversity report highlights hiring percentages while hiding retention and promotion gaps.",
         "Report: 'We hired forty percent underrepresented candidates this year — a company record.' Not mentioned: seventy percent of those hires left within two years, no underrepresented candidate was promoted to senior leadership, and exit interviews consistently cite hostile work culture. A journalist who requests the full retention data sees a very different story.",
         "The company sweeps retention and promotion data under the rug to present a hiring-only diversity narrative.",
         "Company presents {hiring percentages} and hides {retention rates, promotion gaps, exit interview themes}."),

        ("school", "what_if", "A university promotes its graduation rate while hiding that it achieved it by lowering standards.",
         "President: 'Our graduation rate is ninety-two percent — highest in the state.' Not mentioned: pass/fail thresholds were lowered twice in three years, academic integrity violations are no longer recorded on transcripts, and employers have begun reporting that graduates are unprepared. An accreditation team that examines the grade distribution finds the inflation.",
         "The president sweeps standard-lowering and employer feedback under the rug to present a graduation-rate-only narrative.",
         "President presents {graduation rate} and hides {lowered standards, removed integrity records, employer complaints}."),

        ("healthcare", "what_if", "A hospital advertises its surgical success rate while hiding that it selects only low-risk patients.",
         "Billboard: '99% surgical success rate.' Not mentioned: the hospital turns away complex cases, refers high-risk patients to other facilities, and calculates its rate using only the cases it accepts. A patient transferred to a less selective hospital realizes the advertised rate reflects patient selection, not surgical skill.",
         "The hospital sweeps patient selection criteria under the rug to inflate its apparent success rate.",
         "Hospital presents {99% success rate} and hides {complex case refusals, referral patterns, selection bias in calculation}."),

        ("politics", "what_if", "A candidate touts job creation numbers while hiding that the jobs are part-time, low-wage, and without benefits.",
         "Campaign ad: 'Twenty thousand new jobs created in our district!' Not mentioned: eighteen thousand are part-time, average pay is below the living wage, none include health benefits, and the full-time jobs that were lost paid twice as much. An economist who examines the labor data calls it 'a downgrade dressed up as growth.'",
         "The candidate sweeps job quality data under the rug to present a quantity-only employment narrative.",
         "Candidate presents {job creation count} and hides {part-time status, below-living-wage pay, no benefits, lost full-time jobs}."),

        ("sports", "what_if", "A coach presents a player's highlight reel to scouts while hiding disciplinary issues and performance inconsistency.",
         "Coach: 'Watch this — forty-yard dash time, vertical leap, game-winning catches. This kid is elite.' Not mentioned: two suspensions for conduct violations, a forty percent drop rate on routine catches, and three incidents of poor sportsmanship that nearly got the team penalized. A scout who watches full game film instead of highlights sees a very different player.",
         "The coach sweeps disciplinary and consistency data under the rug to present a highlights-only player profile.",
         "Coach presents {athletic metrics, big plays} and hides {suspensions, drop rate, sportsmanship issues}."),

        ("cooking", "puzzle", "A food company promotes a product's 'natural ingredients' label while hiding processing methods that denature those ingredients.",
         "Label: 'Made with real fruit and whole grains.' Not mentioned: the fruit is heat-processed until it retains none of its original vitamins, the grains are refined to remove fiber, and the 'natural flavors' are chemically extracted compounds that bear no resemblance to the named ingredients. A nutritionist who reads the full ingredient panel and processing disclosure sees that the 'natural' label describes the raw inputs, not the finished product.",
         "The company sweeps processing information under the rug, presenting inputs while hiding transformations.",
         "Company presents {ingredient origins} and hides {processing methods, nutrient loss, chemical extraction}."),

        ("technology", "puzzle", "An AI company promotes its model's benchmark scores while hiding its failure modes and bias metrics.",
         "Press release: 'Our model achieves state-of-the-art on five standard benchmarks.' Not mentioned: the model hallucinates factual claims at a rate of eighteen percent, shows significant demographic bias in three categories, and was trained on data that includes copyrighted material under legal challenge. An AI safety researcher who tests the model outside the benchmarks discovers failure modes the press release concealed.",
         "The company sweeps failure modes, bias data, and legal risks under the rug to present a benchmark-only narrative.",
         "Company presents {benchmark scores} and hides {hallucination rate, demographic bias, legal challenges}."),

        ("military", "puzzle", "A defense contractor promotes a weapon system's capabilities while hiding test failures and cost overruns.",
         "Presentation: 'This system achieved a ninety-five percent hit rate in controlled tests and is delivered on schedule.' Not mentioned: the hit rate drops to forty percent in adverse weather, the 'controlled tests' used cooperative targets that did not employ countermeasures, the system has been delivered three years late and two billion over budget, and a Pentagon inspector general report flagged the test methodology as unrealistic. A congressional staffer who reads the IG report sees a weapon system that looks nothing like the presentation.",
         "The contractor sweeps test limitations, weather performance, and cost data under the rug.",
         "Contractor presents {controlled-test hit rate, delivery claim} and hides {adverse-weather performance, cooperative targets, cost overruns, IG critique}."),

        ("legal", "puzzle", "A law firm promotes its win rate while hiding that many cases are settled with unfavorable terms for clients.",
         "Firm website: 'Ninety percent success rate across all cases.' Not mentioned: 'success' includes settlements where clients received less than twenty percent of their claimed damages, cases where the firm pressured clients to accept lowball offers to close quickly, and client satisfaction scores that average two out of five. A bar association review reveals the definition of 'success' is far more generous than clients expect.",
         "The firm sweeps settlement quality, client pressure, and satisfaction data under the rug.",
         "Firm presents {win rate} and hides {settlement quality, client pressure, satisfaction scores}."),

        ("parenting", "puzzle", "A school district promotes its new program's test scores while hiding that the program excluded struggling learners.",
         "Report: 'Students in the new program scored twenty percent higher than the district average.' Not mentioned: the program admitted only students who already scored above the seventy-fifth percentile, excluded students with learning disabilities, and received triple the per-student funding. A parent of an excluded child reads the report and asks why the 'average' comparison includes the very students the program would not accept.",
         "The district sweeps selection criteria and funding disparity under the rug to present inflated program results.",
         "District presents {test score advantage} and hides {selective admission, disability exclusion, funding disparity}."),

        ("science", "puzzle", "A research institute promotes a study finding while hiding the study's limitations and the principal investigator's conflicts of interest.",
         "Press release: 'Landmark study shows the supplement improves cognitive performance by fifteen percent.' Not mentioned: the study lasted only two weeks, used self-reported measures, had no control group, was funded by the supplement manufacturer, and the PI holds a patent on the supplement. A science journalist who reads the actual paper sees that the press release hid every limitation.",
         "The institute sweeps methodological limitations and financial conflicts under the rug.",
         "Institute presents {15% improvement finding} and hides {short duration, self-reporting, no control group, manufacturer funding, PI patent}."),

        ("retail", "puzzle", "A company promotes its sustainability credentials while hiding its supply chain labor practices.",
         "Ad: '100% recycled packaging. Carbon-neutral shipping. We plant a tree for every purchase.' Not mentioned: the products are manufactured in factories with documented labor violations, workers earn below subsistence wages, and the company's sustainability certification was self-awarded using criteria it designed. An investigative journalist who visits the factories discovers conditions the marketing concealed.",
         "The company sweeps labor practice data under the rug to present an environmental-sustainability-only narrative.",
         "Company presents {packaging, carbon neutrality, tree planting} and hides {labor violations, subsistence wages, self-certification}."),

        ("relationships", "puzzle", "A couple presents their relationship as ideal on social media while hiding serious dysfunction.",
         "Posts: 'Five years and still my best friend! #RelationshipGoals #Blessed' Not visible: they are in couples therapy for trust violations, one partner has a substance abuse problem, and friends who see them offline describe constant arguments. A mutual friend who knows both the social media presence and the reality observes the broom at work.",
         "The couple sweeps all negative relationship evidence from their public presentation.",
         "Couple presents {milestone celebrations, affectionate posts} and hides {therapy, trust violations, substance issues, arguments}. The public image survives only because the private reality is concealed."),

        ("finance", "puzzle", "An economic report promotes GDP growth while hiding that all growth went to the top one percent of earners.",
         "Report: 'GDP grew three-point-five percent this year — strongest growth in a decade.' Not mentioned: median household income declined, the bottom fifty percent saw no income growth, healthcare and housing costs outpaced wage gains, and the growth was concentrated in financial services and tech executive compensation. An economist who disaggregates the data sees growth that most citizens did not experience.",
         "The report sweeps distributional data under the rug to present an aggregate-growth-only narrative.",
         "Report presents {GDP growth} and hides {median income decline, bottom 50% stagnation, cost-of-living increases, concentration at top}."),

        ("environment", "puzzle", "A government report on air quality shows improving average pollution levels while hiding that pollution in low-income neighborhoods worsened.",
         "Report: 'Average particulate matter decreased by eight percent citywide.' Not mentioned: three low-income neighborhoods saw particulate matter increase by twenty-five percent after a factory relocated into their area, asthma hospitalizations in those neighborhoods doubled, and the 'average' improvement is driven entirely by wealthy neighborhoods where traffic decreased. An environmental justice advocate who maps the data by neighborhood sees the broom clearly.",
         "The report sweeps geographic disparity under the rug using citywide averages.",
         "Report presents {citywide average improvement} and hides {neighborhood increases, asthma hospitalization spike, distributional inequity}."),

        ("housing", "puzzle", "A city promotes declining homelessness numbers while hiding that it achieved them by changing the counting methodology.",
         "Press conference: 'Homelessness decreased fifteen percent this year.' Not mentioned: the city changed its count methodology to exclude people in temporary shelters, reduced the number of count days, and narrowed the geographic boundaries of the count area. A housing advocate who compares the old and new methodologies finds that under the original method, homelessness actually increased.",
         "The city sweeps methodological changes under the rug to present a declining-homelessness narrative.",
         "City presents {15% decrease} and hides {methodology change, shelter exclusion, reduced count days, narrowed boundaries}."),
    ]

    for i, (domain, tier, ctx, txt, spk, desc) in enumerate(d1_4_contexts):
        seq = i + 1
        rec = make_record(
            "D1.4", "Occam's Broom", "bad_thinking", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Occam's Broom",
                "pattern_description": desc,
                "formal_form": "Agent has evidence E1-En. Some evidence undermines their position. Agent presents only favorable evidence and hides or discredits the rest.",
                "why_wrong": "Honest reasoning requires engaging with all relevant evidence, especially evidence that challenges your position. The case looks strong only because the strongest counter-evidence is hidden.",
                "why_right": None,
                "related_patterns": ["D1.3", "E1.2", "A7.1"],
                "counterpoint": "Sometimes irrelevant evidence should be set aside. The broom is dishonest when the swept evidence is relevant and the sweeper knows it.",
            },
            {
                "identification_prompt": "The speaker seems to make a strong case. But look at what they discussed and what they did not discuss. What is their strategy, and what is wrong with it?",
                "rubric": [
                    {"level": 0, "description": "Player accepts the argument at face value."},
                    {"level": 1, "description": "Player senses evasion but cannot specify what was avoided."},
                    {"level": 2, "description": "Player notices specific evidence was not addressed."},
                    {"level": 3, "description": "Player identifies selective evidence presentation — only favorable data shown, unfavorable data hidden."},
                    {"level": 4, "description": "Player identifies Occam's Broom, distinguishes it from Occam's Razor, and explains why removing relevant counter-evidence is dishonest rather than parsimonious."},
                ],
                "follow_up_if_wrong": "Count all the evidence available. How much was presented? How much was hidden? What picture emerges when you see all of it?",
                "follow_up_if_right": "How would you distinguish Occam's Broom from Occam's Razor? Both involve removing something. What is the critical difference?",
            },
            {
                "npc_personality": "Polished, confident, and skilled at selective presentation. Knows exactly what they are hiding.",
                "npc_dialogue_seed": "Let me show you the evidence. I think you will find it very reassuring — once you see all of it.",
                "resolution_path": "If the player identifies the broom, the hidden evidence is brought to light and the NPC's position weakens.",
            },
            "Dennett Intuition Pumps Ch. 2 (Occam's Broom) + PHIL 201",
        )
        records.append(rec)

    # Pad D1.4 to 50
    d1_4_extra = [
        ("journalism", "puzzle", "A news outlet highlights its award-winning investigations while hiding that it killed three stories under advertiser pressure.",
         "Annual report: 'Five Pulitzer nominations this year — more than any competitor.' Not mentioned: three investigations into major advertisers were killed before publication, two investigative reporters resigned in protest, and the editor-in-chief has a documented conflict of interest with the largest advertiser. A media critic who interviews the departed reporters sees the stories the outlet swept away.",
         "The outlet sweeps editorial interference and advertiser conflicts under the rug to present a journalistic excellence narrative.",
         "Outlet presents {award nominations} and hides {killed stories, reporter resignations, editor conflicts}."),

        ("theater", "puzzle", "A theater promotes its diversity statistics while hiding that diverse hires are concentrated in unpaid intern positions.",
         "Press release: 'Fifty percent of our company are people of color.' Not mentioned: ninety percent of paid leadership positions are held by white staff, diverse hires are concentrated in unpaid internships and part-time roles, and three diversity consultants resigned citing performative compliance. A journalist who disaggregates the data by role and compensation sees the broom clearly.",
         "The theater sweeps role distribution and compensation data under the rug to present a diversity headline.",
         "Theater presents {overall diversity percentage} and hides {leadership composition, compensation disparity, consultant resignations}."),

        ("archaeology", "puzzle", "A government promotes the economic impact of a heritage tourism site while hiding that the site was partially destroyed during development.",
         "Tourism report: 'The heritage site generates twelve million in annual tourism revenue.' Not mentioned: thirty percent of the original site was demolished for a visitor center, the demolition destroyed irreplaceable archaeological context, and three archaeologists publicly protested the development plan. A heritage organization that visits the site photographs the damage the tourism brochure does not show.",
         "The government sweeps site destruction under the rug to present a revenue-positive heritage narrative.",
         "Government presents {tourism revenue} and hides {site destruction, lost context, professional protests}."),

        ("maritime", "puzzle", "A shipping company promotes its safety record while hiding near-miss incidents that were not reported.",
         "Safety report: 'Zero lost-time injuries this quarter.' Not mentioned: fourteen near-miss incidents were not logged, the reporting system was changed to exclude incidents resolved without medical treatment, and two captains filed complaints about pressure not to report. A maritime safety inspector who interviews crew members hears a very different story.",
         "The company sweeps near-miss data and reporting suppression under the rug.",
         "Company presents {zero injuries} and hides {fourteen unreported near-misses, changed reporting criteria, captain complaints}."),

        ("firefighting", "puzzle", "A fire department promotes its reduced fire death statistics while hiding that the reduction was achieved by reclassifying certain deaths.",
         "Report: 'Fire deaths decreased twenty percent this year.' Not mentioned: six deaths previously classified as fire deaths were reclassified as smoke inhalation, the reclassification was made retroactively without public notice, and the actual number of people who died in fires did not change. A statistician who compares the raw data to the reclassified data sees the broom at work.",
         "The department sweeps reclassification methodology under the rug to present a decreasing-deaths narrative.",
         "Department presents {20% decrease} and hides {reclassification, retroactive change, unchanged actual deaths}."),

        ("gaming", "puzzle", "A game publisher promotes its accessibility features while hiding that the accessible mode cuts sixty percent of the content.",
         "Press release: 'Our game is fully accessible with comprehensive assist options.' Not mentioned: the accessible mode removes all puzzles, all optional dialogue, and all branching paths, reducing the game from forty hours to sixteen. A disability advocate who plays both modes discovers the accessible version is a stripped-down shell.",
         "The publisher sweeps content reduction under the rug to present an accessibility-positive narrative.",
         "Publisher presents {accessibility features} and hides {content cuts, reduced playtime, removed branching}."),

        ("agriculture", "puzzle", "A food company promotes its 'farm-to-table' sourcing while hiding that ninety percent of ingredients come from industrial suppliers.",
         "Marketing: 'We source directly from local farms.' Not mentioned: the 'local farm' supplies only the garnish herbs, ninety percent of ingredients come from three industrial distributors, and the 'farm' is a marketing subsidiary the company owns. An investigative food writer who traces the supply chain discovers the local sourcing narrative is cosmetic.",
         "The company sweeps the actual supply chain under the rug to present a farm-to-table image.",
         "Company presents {farm sourcing} and hides {industrial suppliers, subsidiary ownership, cosmetic local sourcing}."),

        ("science", "puzzle", "A university promotes its research impact metrics while hiding that impact was achieved through citation rings.",
         "Report: 'Our average citation impact increased forty percent this year.' Not mentioned: a departmental investigation revealed coordinated citation trading between three labs, two papers were retracted for fabricated data, and the impact increase disappears when the citation ring publications are excluded. An academic integrity officer who audits the citations sees the broom clearly.",
         "The university sweeps citation manipulation and retractions under the rug to present an impact-growth narrative.",
         "University presents {citation impact increase} and hides {citation rings, retractions, inflated metrics}."),

        ("travel", "puzzle", "A tourism board promotes visitor satisfaction while hiding environmental damage caused by tourism.",
         "Report: 'Visitor satisfaction at ninety-two percent — highest in the region.' Not mentioned: coral reef coverage at the main snorkeling site has declined fifty percent from boat anchor damage, three endemic species are now listed as threatened due to habitat disturbance, and the beach erosion rate has tripled since the resort expansion. An environmental scientist who surveys the sites documented in the satisfaction survey sees the damage the tourism board concealed.",
         "The tourism board sweeps environmental degradation under the rug to present a satisfaction-only narrative.",
         "Board presents {visitor satisfaction} and hides {reef decline, species threats, beach erosion}."),
    ]
    for i, (domain, tier, ctx, txt, spk, desc) in enumerate(d1_4_extra):
        seq = len(d1_4_contexts) + i + 1
        rec = make_record(
            "D1.4", "Occam's Broom", "bad_thinking", seq, tier,
            {"context": ctx, "text": txt, "speaker_context": spk},
            {
                "pattern_name": "Occam's Broom",
                "pattern_description": desc,
                "formal_form": "Agent has evidence E1-En. Some evidence undermines their position. Agent presents only favorable evidence and hides or discredits the rest.",
                "why_wrong": "Honest reasoning requires engaging with all relevant evidence, especially evidence that challenges your position. The case looks strong only because the strongest counter-evidence is hidden.",
                "why_right": None,
                "related_patterns": ["D1.3", "E1.2", "A7.1"],
                "counterpoint": "Sometimes irrelevant evidence should be set aside. The broom is dishonest when the swept evidence is relevant and the sweeper knows it.",
            },
            {
                "identification_prompt": "The speaker seems to make a strong case. But look at what they discussed and what they did not discuss. What is their strategy, and what is wrong with it?",
                "rubric": [
                    {"level": 0, "description": "Player accepts the argument at face value."},
                    {"level": 1, "description": "Player senses evasion but cannot specify what was avoided."},
                    {"level": 2, "description": "Player notices specific evidence was not addressed."},
                    {"level": 3, "description": "Player identifies selective evidence presentation — only favorable data shown, unfavorable data hidden."},
                    {"level": 4, "description": "Player identifies Occam's Broom, distinguishes it from Occam's Razor, and explains why removing relevant counter-evidence is dishonest rather than parsimonious."},
                ],
                "follow_up_if_wrong": "Count all the evidence available. How much was presented? How much was hidden?",
                "follow_up_if_right": "How would you distinguish Occam's Broom from Occam's Razor? Both involve removing something. What is the critical difference?",
            },
            {
                "npc_personality": "Polished, confident, and skilled at selective presentation.",
                "npc_dialogue_seed": "Let me show you the evidence. I think you will find it very reassuring.",
                "resolution_path": "If the player identifies the broom, the hidden evidence is brought to light.",
            },
            "Dennett Intuition Pumps Ch. 2 (Occam's Broom) + PHIL 201",
        )
        records.append(rec)

    # For the remaining codes (D1.5 through D2.6), I'll generate more compactly
    # using the same robust structure but with shorter individual scenario descriptions

    remaining_codes = [
        ("D1.5", "Jootsing", "good_tool",
         "jumping out of the system — creative rule-breaking grounded in deep understanding of the rules",
         "Jootsing is genuine only when the rule-breaker has mastered the system they transcend. Random rule-breaking is noise, not creativity.",
         "Agent masters system S fully, then deliberately violates specific rules to achieve effects impossible within S. This requires understanding which rules are load-bearing and which are constraining.",
         None, "Jootsing demonstrates that creative rule-breaking requires mastery of the rules being broken. The innovation is grounded in understanding, not ignorance.",
         ["D1.2", "D1.8", "D2.6"], "Not all rule-breaking requires mastery. Sometimes outsiders see possibilities insiders cannot.",
         "Dennett Intuition Pumps (Jootsing, from Hofstadter) + PHIL 201"),

        ("D1.6", "Deepities", "bad_thinking",
         "a statement ambiguous between a trivially true reading and a profoundly false one, creating an illusion of depth",
         "A deepity has two readings: one trivially true but uninteresting, another profound if true but actually false. The listener blends the certainty of the first with the significance of the second.",
         "Statement S has reading R1 (trivially true) and R2 (profound if true, but false). S appears profound because the listener blends R1's certainty with R2's significance.",
         "Deepities exploit ambiguity to simulate profundity. Once you separate the two readings, the magic disappears.", None,
         ["D1.7", "A5.3"], "Not every ambiguous statement is a deepity. Some genuinely complex ideas resist easy paraphrase.",
         "Dennett Intuition Pumps Ch. 2 (Deepities) + PHIL 201"),

        ("D1.7", "The 'surely' operator", "bad_thinking",
         "using 'surely' or equivalent confidence markers to smuggle unargued claims past the audience as if they were obvious",
         "The 'surely' operator converts 'I assert C (here is my argument)' into 'We all know C (no argument needed),' bypassing the burden of proof for contestable claims.",
         "Claim C is controversial. Speaker prefixes C with 'surely,' converting it from an assertion requiring argument to an apparent truism requiring none.",
         "'Surely' substitutes rhetorical confidence for argument. Each 'surely' flags a claim that actually needs defense.", None,
         ["D1.6", "A5.1", "A9.2"], "Sometimes 'surely' flags genuine common ground. The red flag is when it precedes claims reasonable people disagree about.",
         "Dennett Intuition Pumps Ch. 2 + PHIL 201"),

        ("D1.8", "Goulding", "good_tool",
         "intellectual courage — making bold, specific, falsifiable claims rather than retreating into unfalsifiable hedging",
         "Goulding means committing to specific, testable claims and accepting the reputational cost of being wrong. Hedging to the point of unfalsifiability is safe but useless.",
         "Agent commits to specific, falsifiable claim C and accepts reputational cost if C is wrong. This is goulding: intellectual courage in the form of specificity.",
         None, "Specific, falsifiable claims can be tested, acted on, and corrected. Maximally hedged positions cannot guide action or advance knowledge.",
         ["D1.5", "D2.4", "B1.3"], "Goulding requires evidence. Boldness without homework is bluffing, not goulding.",
         "Dennett Intuition Pumps Ch. 2 (Goulding) + PHIL 201"),

        ("D2.1", "Satisficing", "good_tool",
         "choosing good enough rather than optimal — not a failure of rationality but the product of it when deliberation costs exceed expected improvement",
         "Satisficing is rational when the cost of finding the optimal solution exceeds the expected benefit of having it. An ideally rational agent with self-knowledge would satisfice in time-constrained situations.",
         "When deliberation cost exceeds expected improvement from optimizing, the expected utility of satisficing exceeds the expected utility of attempting to maximize.",
         None, "Satisficing is what full rationality prescribes when bounded by time and cognitive resources. It is practical wisdom, not compromise.",
         ["D2.2", "D2.3", "D2.4", "D2.6"], "Satisficing can become complacency if never revisited. The danger is the Panglossian Slide.",
         "W7 lecture notes + Dennett Moral First Aid Manual"),

        ("D2.2", "The Panglossian Slide", "bad_thinking",
         "sliding from 'we did the best we could given constraints' to 'we did the best possible' to 'no improvement exists'",
         "The Panglossian Slide begins from satisficing (defensible) and slides into optimizing (unwarranted): the best available option becomes the best option, and then no better option exists.",
         "1. We chose the best option given constraints C. (satisficing — true)\n2. Therefore we chose the best option. (unwarranted slide)\n3. Therefore no better option exists. (false closure)",
         "The fact that a decision was the best available under constraints does not make it the best decision. Constraints explain why we settled; they do not transform less-than-ideal into ideal.", None,
         ["D2.1", "D2.3", "B5.1"], "Sometimes satisficing and optimizing genuinely converge. The error is sliding to that conclusion without checking.",
         "W7 lecture notes + Dennett Moral First Aid Manual + Voltaire Candide"),

        ("D2.3", "Conversation-stoppers", "dual",
         "debate-terminating moves that invoke values held beyond discussion — protective when preventing rash action, destructive when blocking needed deliberation",
         "A conversation-stopper invokes a value declared non-negotiable, terminating deliberation. This can protect important values from erosion or prevent life-saving measures from being discussed.",
         "Agent B invokes value V, declared non-negotiable, to halt deliberation about proposal P. Whether this is good or bad depends on whether V truly should override P — a question the stopper prevents.",
         "When a stopper blocks deliberation about life-and-death matters, it prevents weighing all relevant values.",
         "Stoppers protect certain values from incrementalist erosion. Without them, every boundary becomes negotiable.",
         ["D2.4", "D2.6", "D1.2"], "The meta-question — when to honor a stopper and when to push past it — is exactly where the Moral First Aid Manual is needed.",
         "Dennett Thought Stoppers + W7 lecture notes"),

        ("D2.4", "Wolf's Dilemma", "dual",
         "the reflective satisficer's predicament — knowing your heuristics are imperfect but needing them anyway",
         "Once you become reflectively aware that your heuristics are imperfect, you face a meta-decision: override them (losing speed) or follow them (knowing they are flawed). Neither option is clearly rational.",
         "Agent uses heuristic H. H is correct in S1-Sn but incorrect in Sn+1-Sm. Agent becomes aware H is imperfect. Meta-choice: follow H (fast, usually right, sometimes wrong) or compute from scratch (slow, not guaranteed better).",
         "Blindly following heuristics you know to be flawed can be intellectual cowardice.",
         "Heuristics encode accumulated wisdom. Abandoning them often leads to worse outcomes.",
         ["D2.3", "D2.6", "B3.5"], "The resolution may be meta-heuristics: rules about when to trust your rules. This is the Moral First Aid Manual.",
         "W7 lecture notes + Dennett Moral First Aid Manual + Simon on bounded rationality"),

        ("D2.5", "The Frame Problem", "dual",
         "how a rational agent determines what has changed and what has stayed the same after any action — checking everything causes paralysis, checking nothing causes disaster",
         "The Frame Problem: after any action, an agent must determine what to re-evaluate. Checking everything is intractable (paralysis). Pre-specifying a fixed check list is brittle (misses novel changes). Humans solve this effortlessly but cannot articulate how.",
         "Action A in world W1 produces W2. Most properties unchanged. Some change. How does the agent determine which to re-evaluate without checking all (intractable) or using a fixed list (brittle)?",
         "Ignoring the frame problem — either by checking everything or pre-specifying a fixed list — leads to catastrophic failure.",
         "Recognizing the frame problem helps understand why common sense is hard to replicate and why your own background reasoning is impressive.",
         ["D2.4", "D2.6", "E1.2"], "Some argue the frame problem dissolves under embodied cognition. Others argue it remains deep. The debate is unresolved.",
         "Dennett Intuition Pumps (Frame Problem) + W7 lecture notes"),

        ("D2.6", "The Moral First Aid Manual", "good_tool",
         "a practical triage guide for reasoning that draws on multiple theories without waiting to resolve which is correct",
         "Instead of resolving which moral/decision theory is correct, build a triage guide: identify urgent considerations, check for convergence across theories, apply the least controversial action first, document remaining disagreement.",
         "Competing considerations C1-Cn and theories T1-Tm. Triage: (1) identify most urgent C, (2) check for convergence across T, (3) if convergence, act, (4) if not, find least controversial action, (5) document and revisit.",
         None, "The Manual is honest about theoretical disagreement while remaining practical. It is bounded rationality applied to ethics: satisfice now, optimize later.",
         ["D2.3", "D2.4", "D2.5"], "Critics may call it unprincipled compromise. But the Manual can be reflectively refined — it is a living document.",
         "Dennett Moral First Aid Manual + W7 lecture notes + PHIL 201"),
    ]

    # Domain-specific scenario templates for each remaining code
    # I'll generate 50 scenarios per code with domain rotation

    for code_info in remaining_codes:
        code, label, ptype, core_desc, pattern_desc, formal, why_wrong, why_right, related, counterpoint, source = code_info

        # Generate 50 scenarios
        for seq in range(1, 51):
            domain = DOMAINS[(seq - 1) % len(DOMAINS)]
            # Difficulty tier distribution
            if seq <= 34:
                tier = "drill"
            elif seq <= 47:
                tier = "what_if"
            else:
                tier = "puzzle"

            # Generate unique scenarios based on code + domain + tier
            scenario, struct_desc, game_data = generate_scenario(code, label, ptype, domain, tier, seq, core_desc)

            rec = make_record(
                code, label, ptype, seq, tier,
                scenario,
                {
                    "pattern_name": label,
                    "pattern_description": struct_desc if struct_desc else pattern_desc,
                    "formal_form": formal,
                    "why_wrong": why_wrong,
                    "why_right": why_right,
                    "related_patterns": related,
                    "counterpoint": counterpoint,
                },
                {
                    "identification_prompt": generate_prompt(code, ptype, domain),
                    "rubric": generate_rubric(code, ptype),
                    "follow_up_if_wrong": generate_followup_wrong(code, ptype),
                    "follow_up_if_right": generate_followup_right(code, ptype),
                },
                game_data,
                source,
            )
            records.append(rec)

    return records


# Scenario generation functions for each code
def generate_scenario(code, label, ptype, domain, tier, seq, core_desc):
    """Generate a unique scenario for a given code, domain, and tier."""
    return generate_fallback_scenario(code, label, ptype, domain, tier, seq, core_desc)


def generate_fallback_scenario(code, label, ptype, domain, tier, seq, core_desc):
    """Generate scenario from templates when no specific one exists."""

    # Domain-specific NPCs and settings
    domain_settings = {
        "workplace": ("a corporate office", "Manager", "Director", "the conference room"),
        "school": ("a village academy", "Teacher", "Professor", "the classroom"),
        "healthcare": ("a city hospital", "Dr.", "Nurse", "the ward"),
        "politics": ("a town council meeting", "Councillor", "Mayor", "the chamber"),
        "sports": ("an athletic training facility", "Coach", "Captain", "the field"),
        "cooking": ("a busy restaurant kitchen", "Chef", "Sous Chef", "the kitchen"),
        "technology": ("a tech startup office", "Engineer", "Architect", "the dev floor"),
        "military": ("a frontier garrison", "Commander", "Sergeant", "the barracks"),
        "legal": ("a law firm", "Attorney", "Partner", "the office"),
        "parenting": ("a family home", "Parent", "Counselor", "the living room"),
        "music": ("a concert hall", "Musician", "Conductor", "the rehearsal room"),
        "gaming": ("a game development studio", "Designer", "Producer", "the studio"),
        "agriculture": ("a farming cooperative", "Farmer", "Agronomist", "the field office"),
        "science": ("a research laboratory", "Researcher", "Professor", "the lab"),
        "retail": ("a department store", "Manager", "Buyer", "the sales floor"),
        "relationships": ("a counseling center", "Client", "Therapist", "the office"),
        "finance": ("an investment firm", "Analyst", "Director", "the trading floor"),
        "travel": ("a travel agency", "Guide", "Director", "the office"),
        "environment": ("a conservation center", "Ecologist", "Director", "the center"),
        "housing": ("a housing authority", "Planner", "Director", "the office"),
        "journalism": ("a newsroom", "Reporter", "Editor", "the newsroom"),
        "theater": ("a playhouse", "Director", "Actor", "the stage"),
        "archaeology": ("an excavation site", "Archaeologist", "Curator", "the dig"),
        "maritime": ("a harbor office", "Captain", "Port Master", "the dock"),
        "firefighting": ("a fire station", "Chief", "Lieutenant", "the station"),
    }

    setting, npc1, npc2, location = domain_settings.get(domain, ("a meeting room", "Speaker", "Listener", "the room"))

    # Code-specific scenario templates
    if code == "D1.5":  # Jootsing
        scenarios_by_domain = {
            "workplace": (
                {"context": f"The player enters {setting} where {npc1} Arden has been reprimanded for breaking the standard operating procedure for client presentations.",
                 "text": f"{npc1} Arden explains: 'I did not break the procedure out of laziness. I followed it for five years. I know exactly why each step exists — the warm-up builds rapport, the data slide establishes credibility, the close creates urgency. But for this client, the standard close actually undermines urgency because they are a data-driven firm. So I replaced the emotional close with a comparative analysis. I jumped out of the system because I understood which part of it was wrong for this context.'",
                 "speaker_context": "Arden demonstrates jootsing — mastering a system completely before deliberately breaking a specific rule for a specific reason."},
                f"Arden mastered the presentation system, identified which element was counterproductive for this client, and replaced it with something that served the same function differently. This is jootsing: informed rule-breaking from a position of understanding.",
                {"npc_personality": "Confident, articulate, and slightly impatient with those who confuse rule-following with competence.",
                 "npc_dialogue_seed": "They say I broke the rules. Ask them if I can recite every rule from memory. Then ask why that matters.",
                 "resolution_path": "Player learns to distinguish informed rule-breaking from ignorant rebellion."}
            ),
            "school": (
                {"context": f"The player visits {setting} where student Cael has been disciplined for writing an essay in a format the teacher did not approve.",
                 "text": f"Cael says: 'I have written forty essays in the standard five-paragraph format. I can do it in my sleep. But the five-paragraph structure forces a three-point argument even when the topic has two points or four. For this essay, the argument had two clear parts, so I used a two-section structure with deeper analysis in each. I did not ignore the format — I outgrew it.'",
                 "speaker_context": "Cael demonstrates jootsing by mastering a writing format and then transcending it for a specific argumentative purpose."},
                f"Cael's rule-breaking is grounded in mastery — they can execute the standard format perfectly but chose to deviate because the standard format constrained the argument. This is jootsing.",
                {"npc_personality": "Earnest, articulate, and frustrated by being punished for thinking beyond the template.",
                 "npc_dialogue_seed": "I am not breaking rules. I am graduating from them. There is a difference.",
                 "resolution_path": "Player helps Cael explain jootsing to the teacher, unlocking creative freedom as a reward for demonstrated mastery."}
            ),
        }
        default = (
            {"context": f"The player enters {setting} where {npc1} has been criticized for breaking an established {domain} convention.",
             "text": f"{npc1} responds: 'I spent years mastering the conventional approach. I can execute it perfectly. I broke the specific rule I broke because I understood exactly what it was doing and what it was preventing. You cannot jump out of a system you do not understand — you just stumble. I understood the system, identified which constraint was limiting the outcome, and deliberately chose a different path.'",
             "speaker_context": f"{npc1} demonstrates jootsing — creative rule-breaking grounded in deep mastery of the rules being broken."},
            f"{npc1} mastered the conventional system, identified a specific constraint, and deliberately broke it for a specific reason. This is jootsing: informed transcendence, not ignorant rebellion.",
            {"npc_personality": "Confident, knowledgeable, and slightly impatient with those who confuse compliance with competence.",
             "npc_dialogue_seed": "They will tell you I am a rebel. Ask if any rebel first spent years perfecting what they rebelled against.",
             "resolution_path": "Player distinguishes informed rule-breaking from random rebellion, unlocking the jootsing principle."}
        )
        return scenarios_by_domain.get(domain, default)

    elif code == "D1.6":  # Deepities
        statements = {
            "workplace": ("'Work is just a transaction'", "trivially, work involves an exchange of labor for compensation (true but boring). Profoundly, it suggests work has no intrinsic meaning or dignity — which is false for most workers."),
            "school": ("'Education is just information'", "trivially, education involves conveying information (true). Profoundly, it suggests education is nothing more than data transfer — ignoring critical thinking, character formation, and social development."),
            "healthcare": ("'Healing begins within'", "trivially, the body's immune system is internal (true). Profoundly, it suggests no external medical intervention is needed — which is dangerously false."),
            "politics": ("'Power corrupts'", "trivially, power creates temptations (true and obvious). As an absolute claim that all power holders are corrupt, it would be profoundly false and would make governance impossible."),
            "sports": ("'Winning is everything'", "trivially, winning is the goal of competition (true). Profoundly, it suggests nothing else matters — health, sportsmanship, enjoyment — which most athletes reject."),
            "cooking": ("'Food is love'", "trivially, cooking for others is an act of care (true). Profoundly, it suggests food literally is the emotion of love — which is category confusion."),
            "technology": ("'Data is the new oil'", "trivially, data is valuable (true). Profoundly, it suggests data behaves like a finite extractive resource — but data is infinitely copyable, does not deplete, and has no fixed price."),
            "military": ("'War is peace'", "trivially, military deterrence can preserve peace (true in some contexts). Profoundly, it suggests war and peace are the same thing — which is incoherent."),
            "legal": ("'Justice is blind'", "trivially, justice should be impartial (true). Profoundly, it suggests the justice system actually is impartial — which is empirically false."),
            "parenting": ("'Children are the future'", "trivially, children will grow into adults who shape the future (true and obvious). Profoundly, it seems to say children are important — but it does not specify any action or commitment."),
            "music": ("'Music is the universal language'", "trivially, music exists in all cultures (true). Profoundly, it suggests all music communicates the same things across cultures — which ethnomusicology shows is false."),
            "gaming": ("'It is just a game'", "trivially, games are games (true and vacuous). Profoundly, it suggests nothing in a game matters — ignoring the real skills, relationships, and emotions games involve."),
            "agriculture": ("'We reap what we sow'", "trivially, crops require planting (true). Profoundly, it suggests outcomes are always proportional to effort — ignoring drought, disease, and luck."),
            "science": ("'Science is just another belief system'", "trivially, science involves beliefs about the world (true). Profoundly, it suggests science is equivalent to religion or mythology — ignoring empirical testing and falsifiability."),
            "retail": ("'The customer is king'", "trivially, businesses depend on customers (true). Profoundly, it suggests customer wishes should override all other considerations — safety, ethics, employee welfare."),
            "relationships": ("'Love conquers all'", "trivially, love is a powerful motivator (true). Profoundly, it suggests love alone can overcome any problem — ignoring abuse, incompatibility, and material constraints."),
            "finance": ("'Money is just a number'", "trivially, money is represented numerically (true). Profoundly, it suggests money has no real impact on life — which is false for anyone facing poverty."),
            "travel": ("'The journey is the destination'", "trivially, travel involves experiences along the way (true). Profoundly, it suggests arrival does not matter — which is false when you need to be somewhere specific."),
            "environment": ("'We are all connected'", "trivially, ecosystems are interconnected (true). Profoundly, it suggests all actions are equally impactful — which obscures the difference between driving to work and deforesting a continent."),
            "housing": ("'Home is where the heart is'", "trivially, emotional attachment makes a place feel like home (true). Profoundly, it suggests physical housing does not matter — which is false for anyone without shelter."),
            "journalism": ("'Truth is relative'", "trivially, perspectives on events vary (true). Profoundly, it suggests no factual claims are more accurate than others — which is false."),
            "theater": ("'All the world is a stage'", "trivially, people perform social roles (true). Profoundly, it suggests nothing is authentic — which is existentially incoherent."),
            "archaeology": ("'The past is another country'", "trivially, the past is different from the present (true). Profoundly, it suggests the past is completely unknowable — which archaeology refutes daily."),
            "maritime": ("'The sea has no mercy'", "trivially, the ocean is indifferent (true). Profoundly, it suggests maritime safety is impossible — which is false."),
            "firefighting": ("'Where there is smoke there is fire'", "trivially, combustion produces smoke (often true). Profoundly, it suggests every appearance of wrongdoing means actual wrongdoing — which can lead to false accusations."),
        }
        statement, analysis = statements.get(domain, ("'Everything is relative'", "trivially, many things depend on context (true). Profoundly, it suggests no comparisons or judgments are valid — which is self-defeating."))

        return (
            {"context": f"The player enters {setting} where a self-styled sage named Brother Aelm is dispensing wisdom to a small crowd. An apprentice named Kira seems deeply impressed.",
             "text": f"Brother Aelm closes his eyes and intones: {statement} The crowd murmurs approvingly. Kira whispers to the player: 'Is that not profound?' But the player can see the statement working on two levels — one trivially true and uninteresting, the other apparently deep but actually false.",
             "speaker_context": f"Aelm has uttered a deepity. On one reading, {analysis.split('. ')[0]}. On the other, {'. '.join(analysis.split('. ')[1:])}"},
            f"The statement {statement} is a deepity — ambiguous between a trivially true reading and a profoundly false one. {analysis}",
            {"npc_personality": "Serene, practiced at sounding wise, and half-believes his own pronouncements.",
             "npc_dialogue_seed": f"Aelm opens one eye as you approach. {statement} he repeats. 'Sit with that for a moment.'",
             "resolution_path": "If the player unpacks the deepity by separating the two readings, Kira has an aha moment and learns to detect them."}
        )

    elif code == "D1.7":  # The 'surely' operator
        topics = {
            "workplace": ("performance reviews", "'Surely everyone agrees that performance is best measured by output alone. Surely we can all see that qualitative feedback is just opinion. And surely no reasonable person would base promotions on anything other than numbers.'", "Whether output alone measures performance, whether qualitative feedback is mere opinion, and whether promotions should be purely numerical are all debatable."),
            "school": ("student assessment", "'Surely test scores are the most objective measure of learning. Surely we can all agree that subjective teacher evaluations are unreliable. And surely standardized testing is the fairest approach for all students.'", "Whether test scores measure learning, whether teacher evaluations are unreliable, and whether standardized tests are fair are all contested claims."),
            "healthcare": ("treatment protocols", "'Surely the newest treatment is always the best. Surely we can all agree that traditional methods are outdated. And surely any doctor who resists innovation is behind the times.'", "Whether newer is better, whether traditional methods are outdated, and whether resisting innovation is the same as being backward are all contestable."),
            "politics": ("immigration policy", "'Surely we can all agree that borders should be completely open. Surely any restriction on movement is fundamentally unjust. And surely economic concerns are just excuses for xenophobia.'", "Whether borders should be open, whether all restrictions are unjust, and whether economic concerns are pretextual are all substantive debates."),
            "sports": ("coaching methods", "'Surely toughness is the most important quality in an athlete. Surely we can all see that rest days are for the uncommitted. And surely mental health concerns are being exaggerated in modern sports.'", "Whether toughness is paramount, whether rest days indicate lack of commitment, and whether mental health concerns are exaggerated are all debatable."),
            "cooking": ("culinary standards", "'Surely French cuisine is the foundation of all fine cooking. Surely we can all agree that molecular gastronomy is just pretension. And surely a chef without classical training cannot truly understand flavor.'", "Whether French cuisine is foundational, whether molecular gastronomy is pretentious, and whether classical training is necessary are all debatable claims."),
            "technology": ("AI development", "'Surely artificial intelligence will surpass human intelligence within a decade. Surely we can all see that regulation will only slow progress. And surely anyone concerned about AI safety is just a Luddite.'", "Whether AI will surpass humans, whether regulation slows progress harmfully, and whether safety concerns are Luddism are all active debates."),
            "military": ("strategy", "'Surely air superiority is the decisive factor in modern warfare. Surely ground forces are becoming obsolete. And surely any commander who emphasizes infantry is living in the past.'", "Whether air superiority is decisive, whether ground forces are obsolete, and whether infantry emphasis is outdated are all debated in military theory."),
            "legal": ("justice reform", "'Surely longer sentences deter crime. Surely we can all agree that victims' rights should always override defendants' rights. And surely anyone who argues for rehabilitation is soft on crime.'", "Whether longer sentences deter, whether victims' rights always override defendants' rights, and whether rehabilitation advocacy is softness are all debatable."),
            "parenting": ("child development", "'Surely children who are given boundaries will be the most well-adjusted. Surely we can all agree that permissive parenting creates entitled children. And surely any parent who does not set strict rules is being irresponsible.'", "Whether boundaries guarantee adjustment, whether permissiveness creates entitlement, and whether strict rules are the only responsible approach are all debatable."),
            "music": ("music theory", "'Surely classical training is essential for any serious musician. Surely we can all agree that self-taught musicians lack discipline. And surely music theory is the foundation of all good composition.'", "Whether classical training is essential, whether self-taught musicians lack discipline, and whether theory is foundational are all debatable."),
            "gaming": ("game design", "'Surely story-driven games are more artistic than gameplay-focused ones. Surely we can all see that multiplayer is the future of gaming. And surely anyone who plays single-player games is behind the times.'", "Whether story games are more artistic, whether multiplayer is the future, and whether single-player is outdated are all debatable."),
            "agriculture": ("farming methods", "'Surely organic farming is always better for the environment. Surely we can all agree that GMOs are dangerous. And surely any farmer who uses synthetic fertilizer is poisoning the land.'", "Whether organic is always better, whether GMOs are dangerous, and whether synthetic fertilizer is poisoning are all scientifically contested."),
            "science": ("research methodology", "'Surely quantitative methods are more rigorous than qualitative ones. Surely we can all agree that anecdotal evidence is worthless. And surely any researcher who uses interviews instead of experiments is not doing real science.'", "Whether quantitative is more rigorous, whether anecdotal evidence is worthless, and whether interviews are unscientific are all methodological debates."),
            "retail": ("customer service", "'Surely the customer is always right. Surely we can all agree that returns should always be accepted. And surely any store that limits returns is anti-consumer.'", "Whether customers are always right, whether returns should be unlimited, and whether return limits are anti-consumer are all debatable."),
            "relationships": ("commitment", "'Surely marriage is the ultimate expression of commitment. Surely we can all agree that unmarried couples are less committed. And surely anyone who chooses not to marry is afraid of commitment.'", "Whether marriage is the ultimate commitment, whether unmarried couples are less committed, and whether non-marriage indicates fear are all debatable."),
            "finance": ("investment", "'Surely diversification is always the best strategy. Surely we can all agree that concentrated portfolios are reckless. And surely any investor who does not diversify is gambling.'", "Whether diversification is always best, whether concentration is reckless, and whether non-diversification is gambling are all debated."),
            "travel": ("cultural tourism", "'Surely immersive travel is the only authentic way to experience a culture. Surely we can all agree that guided tours are superficial. And surely any traveler who stays in resorts is not really traveling.'", "Whether immersion is the only authentic travel, whether guided tours are superficial, and whether resort stays count as travel are all debatable."),
            "environment": ("conservation", "'Surely rewilding is always the best conservation strategy. Surely we can all agree that human intervention in ecosystems is always harmful. And surely any conservationist who supports managed landscapes is not truly committed to nature.'", "Whether rewilding is always best, whether human intervention is always harmful, and whether managed landscapes betray conservation are all debated."),
            "housing": ("urban planning", "'Surely density is always better for cities. Surely we can all agree that suburbs are wasteful. And surely anyone who prefers a house with a yard is part of the sprawl problem.'", "Whether density is always better, whether suburbs are wasteful, and whether yard preferences are problematic are all debatable."),
            "journalism": ("media ethics", "'Surely objectivity is the highest journalistic value. Surely we can all agree that advocacy journalism is biased. And surely any journalist who takes a position is abandoning their professional duty.'", "Whether objectivity is paramount, whether advocacy journalism is biased, and whether taking positions abandons duty are all debated."),
            "theater": ("performance", "'Surely method acting produces the best performances. Surely we can all agree that technical acting is cold and mechanical. And surely any actor who does not fully inhabit their role is not a true artist.'", "Whether method acting is best, whether technical acting is cold, and whether full inhabitation is required are all debated."),
            "archaeology": ("heritage", "'Surely artifacts belong in the country where they were found. Surely we can all agree that museums that hold foreign artifacts are complicit in colonialism. And surely any scholar who studies artifacts outside their origin country is benefiting from theft.'", "Whether artifacts belong in their origin country, whether foreign holdings are colonial, and whether external study is complicit are all debated."),
            "maritime": ("regulation", "'Surely larger ships are always more efficient. Surely we can all agree that small fishing vessels are economically obsolete. And surely any port that accommodates small boats is wasting infrastructure.'", "Whether larger ships are always more efficient, whether small vessels are obsolete, and whether accommodating them wastes resources are all debatable."),
            "firefighting": ("training", "'Surely live fire training is the only way to prepare. Surely we can all agree that simulation-based training is inferior. And surely any department that reduces live burns is compromising readiness.'", "Whether live fire is the only preparation, whether simulation is inferior, and whether reducing live burns compromises readiness are all debated."),
        }
        topic, speech, analysis = topics.get(domain, ("reasoning", "'Surely we all agree that logic is the highest form of thinking.'", "Whether logic is the highest thinking form is debatable."))

        return (
            {"context": f"The player sits in on a debate in {setting}. A speaker named Professor Venn is making claims about {topic}, using 'surely' to bypass the burden of proof.",
             "text": f"Professor Venn adjusts his spectacles and declares: {speech} He leans back as if the case is settled.",
             "speaker_context": f"Venn uses 'surely' to present contestable claims as obvious truths. {analysis}"},
            f"Venn uses 'surely' three times, each time to smuggle a debatable claim past the audience as if it were common knowledge. {analysis}",
            {"npc_personality": "Distinguished, accustomed to deference, and uses 'surely' like a verbal gavel.",
             "npc_dialogue_seed": f"Venn peers at you. 'Surely you, as a thinking person, can see what I mean. Surely.'",
             "resolution_path": "Player learns the 'surely alarm' — when you hear 'surely,' check whether an argument is hiding behind it."}
        )

    elif code == "D1.8":  # Goulding
        domain_scenarios = {
            "workplace": ("a strategy meeting where advisors hedge every recommendation", "Analyst Pella stands: 'Revenue will decline eighteen percent if we do not launch by March. Not might decline. Will. I have the customer pipeline data to prove it. I stake my position on this forecast.'", "Pella makes a specific, testable claim while advisors hedge into uselessness."),
            "school": ("a faculty meeting about curriculum changes", "Junior faculty member Kira speaks: 'The current textbook is failing students. I taught from it for three semesters, tracked every assessment, and students who struggle do so specifically in chapters four through seven. I propose we replace those chapters. If I am wrong, I will write the replacement myself.'", "Kira makes a specific claim about which chapters fail and stakes her credibility on it."),
            "healthcare": ("a diagnostic conference where doctors hedge their assessments", "Young resident Dr. Pell says: 'It is Addison's disease. The hyperpigmentation, the electrolyte pattern, and the cortisol level all point there. I will be surprised if the ACTH stimulation test does not confirm it. If I am wrong, I want to know why so I can learn.'", "Dr. Pell commits to a specific diagnosis while senior doctors hedge with differential lists."),
            "politics": ("a policy meeting where advisors provide maximally hedged recommendations", "Junior staffer Nora says: 'If we do not invest in the flood barrier this year, the riverside district will flood in the next major storm. I have the hydrology data. That is my assessment, and I stand behind it.'", "Nora makes a specific, falsifiable prediction while senior advisors hedge."),
            "sports": ("a pre-game strategy session where coaches equivocate", "Scout Marin stands: 'Their left defender turns slowly on reverse cuts. Run three plays to that side in the first quarter and we score at least twice. If I am wrong, pull the plays and I will find a new weakness at halftime.'", "Marin commits to a specific tactical prediction with a built-in accountability mechanism."),
            "cooking": ("a menu tasting where no one will commit to a verdict", "Apprentice Sable says: 'This dish needs more acid. Specifically, lemon juice rather than vinegar, and at the last moment rather than during cooking. I will stake tonight's dessert course on it.'", "Sable makes a specific culinary claim while experienced chefs hedge about balancing flavors."),
            "technology": ("a product review where engineers give noncommittal assessments", "Junior engineer Tam says: 'The authentication module will fail under load. Specifically, it will time out at two thousand concurrent users because of the synchronous database call on line 847. Deploy it and I guarantee a production incident within forty-eight hours.'", "Tam makes a precise technical prediction while senior engineers say things like 'it might have issues.'"),
            "military": ("a planning session where officers give hedged intelligence assessments", "Scout Pella reports: 'The bridge is defended by forty soldiers, not two hundred. I was there last night. If we attack at dawn with the full company, we break through.'", "Pella stakes her rank on a specific, testable intelligence claim."),
            "legal": ("a case strategy meeting where lawyers hedge their predictions", "Associate Kael says: 'This judge will rule for us on the motion to suppress. His last twelve rulings on similar motions went our way, and the facts here are stronger. I would bet my bonus on it.'", "Kael makes a specific prediction about a judicial ruling based on documented patterns."),
            "parenting": ("a parent-teacher conference where everyone speaks in generalities", "Mother Lin says: 'My child's reading difficulty is not about intelligence — it is about the font size in the assigned books. She tested at grade level with large print and two grades below with standard. I am certain of this and I want the school to test it.'", "Lin makes a specific, testable claim about the cause of her child's difficulty."),
            "music": ("a band rehearsal where no one will commit to an arrangement", "Drummer Kai says: 'Drop the bridge entirely and go straight from the second chorus to the final verse. The energy sags in the bridge. If I am wrong, the crowd will tell us at Saturday's show and we put it back.'", "Kai makes a specific arrangement call with a built-in test."),
            "gaming": ("a game design meeting where everyone says 'it depends'", "QA tester Renn says: 'The boss fight is too long. Specifically, the third phase adds nothing new and players will quit during it. I will bet my next review score that cutting phase three improves completion rate by at least twenty percent.'", "Renn commits to a specific design prediction with a measurable outcome."),
            "agriculture": ("a crop planning meeting where advisors hedge about planting dates", "Young agronomist Sable says: 'Plant the soy by March fifteenth or lose thirty percent of yield potential. The soil temperature data from the last five years supports this precisely. I will be held accountable if I am wrong.'", "Sable makes a specific, data-backed planting recommendation."),
            "science": ("a lab meeting where researchers hedge about their results", "Postdoc Kira says: 'The effect is real. It replicates across all three sample sizes and I predict it will hold in the pre-registered study. I will submit this to the journal and stake my early career on it.'", "Kira commits to a specific scientific claim with career consequences."),
            "retail": ("a product meeting where no one will recommend a direction", "Buyer Tam says: 'Stock the organic line in the front display for two weeks. I predict a twenty-five percent increase in organic sales. If I am wrong, I will personally restock the old display.'", "Tam makes a specific, measurable retail prediction."),
            "relationships": ("a couples therapy session where both partners speak in generalities", "Partner A says: 'The problem is not communication in general — it is that you dismiss my concerns about money within the first thirty seconds of every conversation about finances. I have counted. It happens every time.'", "Partner A makes a specific, observable claim about a behavioral pattern."),
            "finance": ("an investment committee where everyone hedges", "Junior analyst Pell says: 'This stock will drop below forty within sixty days because the patent expires in fifty days and they have no pipeline replacement. I am putting this in writing.'", "Pell makes a time-bound, falsifiable price prediction."),
            "travel": ("a tour planning meeting where guides equivocate about route safety", "Guide Marin says: 'The northern trail is safe through Thursday. The snowpack is stable, the temperature will stay below zero, and I was on that trail yesterday. By Friday the thaw begins and it becomes dangerous. I guarantee this assessment.'", "Marin makes a specific, time-bounded safety claim."),
            "environment": ("a conservation meeting where scientists give noncommittal assessments", "Field researcher Ash says: 'The wolf pack will move to the eastern valley within two weeks. The prey migration pattern is shifting east and I have GPS collar data from the last three seasons showing the pack follows within ten to fourteen days.'", "Ash makes a specific behavioral prediction based on documented patterns."),
            "housing": ("a planning commission meeting where everyone is vague about projections", "Planner Nora says: 'This development will generate three hundred daily car trips, not the fifty the developer's traffic study claims. I modeled it using ITE trip generation rates and comparable developments. I will defend this number in any forum.'", "Nora makes a specific traffic prediction and challenges the developer's lowball estimate."),
            "journalism": ("an editorial meeting where no one will commit to a story angle", "Reporter Tam says: 'The mayor's office is inflating the jobs numbers. I have the raw data and it shows a thirty percent discrepancy with the official figures. I will go on record with this claim and source it fully.'", "Tam makes a specific, documented claim about data manipulation."),
            "theater": ("a production meeting where everyone hedges about casting", "Director says: 'Cast Alena as the lead. Not because she is the safest choice but because she has the specific quality of controlled vulnerability this role requires. I have seen twelve auditions and I am certain. If the opening night reviews say I was wrong, I will own it.'", "The director makes a specific casting decision and accepts accountability."),
            "archaeology": ("a site assessment where experts hedge about dating", "Ceramicist Kira says: 'This pottery is from the third century, not the fifth. The glaze composition matches third-century kiln temperatures and the motif pattern was discontinued by 350. I will stake my publication on this dating.'", "Kira makes a specific chronological claim based on material evidence."),
            "maritime": ("a weather briefing where forecasters hedge", "Navigator says: 'We have a twelve-hour window starting at 0600. Wind drops below fifteen knots, seas below one meter. After 1800 the front arrives and conditions deteriorate to gale force. I am confident enough to recommend departure.'", "The navigator makes a specific, time-bounded weather prediction."),
            "firefighting": ("a post-incident review where everyone is vague about what went wrong", "Lieutenant Cade says: 'The ventilation was late. Specifically, it was late by four minutes because the ladder truck was positioned on the wrong side. That four minutes allowed flashover conditions to develop. I know because I was on the roof timing the cut.'", "Cade makes a specific causal claim about the incident with precise timing data."),
        }
        desc, text, analysis = domain_scenarios.get(domain, ("a meeting where no one commits", "A junior member makes a specific, testable claim while seniors hedge.", "The junior member demonstrates goulding."))

        return (
            {"context": f"The player joins {desc} in {setting}. Senior figures give maximally hedged recommendations that cannot be acted upon.",
             "text": text,
             "speaker_context": f"The speaker demonstrates goulding — making a bold, specific, falsifiable claim rather than hiding behind qualifications. {analysis}"},
            f"{analysis} This is goulding: intellectual courage in the form of specificity. The bold claim can be tested and corrected; the hedged positions cannot guide action.",
            {"npc_personality": "Direct, evidence-grounded, and willing to be wrong in public.",
             "npc_dialogue_seed": "If I am wrong, I will own it. But at least I said something specific enough to be wrong about.",
             "resolution_path": "Player learns the value of specificity and falsifiability in claims."}
        )

    elif code == "D2.1":  # Satisficing
        return (
            {"context": f"The player enters {setting} where a decision must be made quickly but an optimizer insists on finding the perfect answer first.",
             "text": f"The optimizer says: 'We need the optimal solution. Give me more time to calculate.' The pragmatist responds: 'If I wait for the optimal answer, the window closes. I have a good-enough answer that works right now. My protocol was designed in calm conditions precisely for moments like this when thinking time is a luxury. Good enough, delivered on time, beats perfect, delivered too late.'",
             "speaker_context": f"The pragmatist demonstrates satisficing — choosing good enough as a rational strategy. The decision protocol was built in advance, exactly as Dennett's Moral First Aid Manual prescribes: deliberate when time permits, deploy heuristics when it does not."},
            f"The pragmatist satisfices rationally: the cost of optimizing (missed window, delayed action) exceeds the expected benefit of a better answer. The protocol was designed during calm to be deployed during crisis — bounded rationality is practical wisdom, not compromise.",
            {"npc_personality": "Calm under pressure, speaks in short sentences, no patience for abstraction when action is needed.",
             "npc_dialogue_seed": "Good enough, right now. Perfect, too late. Which one saves lives?",
             "resolution_path": "Player learns that satisficing is what full rationality prescribes under time pressure."}
        )

    elif code == "D2.2":  # Panglossian Slide
        return (
            {"context": f"The player enters {setting} where a leader made the best decision available under constraints but now insists it was the best decision possible, refusing to consider improvements.",
             "text": f"The leader declares: 'Our approach was not merely adequate — it was optimal. We lost nothing of real importance. I see no reason to entertain alternative ideas when our own methods have proven themselves perfect.' A visiting expert suggests an improvement, but the leader dismisses it: 'We have already found the best way.'",
             "speaker_context": f"The leader begins from the defensible claim that they did the best they could given constraints (satisficing), then slides into asserting their solution is the best possible (optimizing). They reframe losses as unimportant and refuse to consider improvements — the Panglossian Slide."},
            f"The leader slides from 'best available under constraints' to 'best possible' to 'no improvement exists.' This is the Panglossian Slide: treating bounded rationality's output as if it were unbounded optimality.",
            {"npc_personality": "Proud, authoritative, and deeply invested in past decisions. Pride has calcified into inability to distinguish 'we did well' from 'we did perfectly.'",
             "npc_dialogue_seed": "Our plan was flawless. Anyone who suggests otherwise simply does not understand what we faced.",
             "resolution_path": "Player helps the leader see that honoring past achievement does not require calling it perfect, opening the door to improvement."}
        )

    elif code == "D2.3":  # Conversation-stoppers
        return (
            {"context": f"The player enters {setting} where a proposal for change is met with a debate-terminating move. One party invokes a value they declare beyond discussion. The proposal has genuine merit, but so does the invoked value.",
             "text": f"Party A presents a proposal supported by evidence and practical reasoning. Party B rises: 'This is not a matter for calculation. Some things are sacred. This conversation is over.' Party A throws up their hands. The room splits. No one knows how to continue, because the conversation-stopper has terminated the deliberation itself.",
             "speaker_context": f"Party B has deployed a conversation-stopper — an appeal to a value held beyond discussion. This is dual-natured: the appeal may protect something genuinely important from careless destruction, but it also prevents the community from exploring creative solutions that honor both values."},
            f"The conversation-stopper terminates deliberation by invoking a non-negotiable value. This is dual: it can protect important values from erosion, but it can also block needed action. The meta-question — when should the stopper hold? — is itself a conversation the stopper tries to prevent.",
            {"npc_personality": "Party B is dignified and principled, not cynical. Party A is pragmatic and frustrated. Both are good people in a genuine dilemma.",
             "npc_dialogue_seed": "Some things are beyond discussion. The question is whether this is one of them.",
             "resolution_path": "Player identifies the conversation-stopper and proposes a process that honors both values, allowing creative solutions to emerge."}
        )

    elif code == "D2.4":  # Wolf's Dilemma
        return (
            {"context": f"The player encounters a thoughtful person in {setting} who has used effective rules of thumb for years but has recently learned they are imperfect. Now they are paralyzed between following flawed heuristics and trying to reason from scratch.",
             "text": f"The thinker says: 'For years I made decisions using simple rules. They worked well enough. Now I understand they are heuristics — shortcuts that sometimes fail. I see the failures clearly. So should I abandon the rules? If I reason from scratch every time, I am too slow. But if I follow rules I know are flawed, am I not being irrational? I know too much to trust my shortcuts, but not enough to do without them.'",
             "speaker_context": f"This is Wolf's Dilemma — the reflective satisficer's predicament. Once you become aware your heuristics are imperfect, you face a meta-decision: override them (losing their speed) or follow them (knowing they are flawed). Neither option is clearly rational."},
            f"The thinker faces the fundamental tension of bounded rationality: heuristics work because they are fast, but reflective awareness of their limitations creates a meta-dilemma. The resolution may lie in meta-heuristics — rules about when to trust your rules — which is exactly what Dennett's Moral First Aid Manual provides.",
            {"npc_personality": "Thoughtful, haunted, and genuinely searching. Not self-pitying — a rigorous thinker who has hit a wall.",
             "npc_dialogue_seed": "I used to decide without thinking. Now I think about every decision and cannot decide at all.",
             "resolution_path": "Player helps the thinker see that the answer is not 'abandon heuristics' or 'ignore your knowledge' but 'build a triage guide for when to trust your heuristics and when to override them.'"}
        )

    elif code == "D2.5":  # The Frame Problem
        return (
            {"context": f"The player encounters a problem in {setting} where an agent or system must decide what to pay attention to after taking an action. Checking everything leads to paralysis; checking too little leads to disaster.",
             "text": f"The system designer explains: 'I built two versions. Version one checks everything before acting — is the floor still there? Has gravity changed? It freezes, overwhelmed by verification. Version two checks only a pre-specified list — it acts quickly but walks into hazards not on the list. How do you decide what to pay attention to without checking everything or missing something critical?'",
             "speaker_context": f"This is the Frame Problem: after any action, almost everything stays the same but some things change. An agent must determine which things to check. Checking everything is intractable (paralysis). Checking a fixed list is brittle (misses novel hazards). Humans solve this effortlessly through background assumptions, but no one can articulate how."},
            f"Both versions fail because they lack a solution to the Frame Problem. Version one is paralyzed by exhaustive checking; version two is blindsided by unchecked hazards. The problem is dual — deeply challenging and genuinely open — and recognizing it is the first step toward better system design.",
            {"npc_personality": "Brilliant, frustrated, and excited when someone understands the depth of the problem.",
             "npc_dialogue_seed": "Do not tell me to add items to the checklist. Tell me how to know what should be on it.",
             "resolution_path": "Player earns credit by recognizing the problem's depth. No clean resolution exists — the Frame Problem is genuinely open."}
        )

    elif code == "D2.6":  # Moral First Aid Manual
        return (
            {"context": f"The player encounters a person in {setting} who faces a moral or practical dilemma involving competing values. They are paralyzed because they cannot decide which theory or principle to follow.",
             "text": f"The person says: 'I have two competing obligations and I do not know which moral theory to follow. One theory says do X; another says do not-X. How do I choose?' A wise advisor opens a worn leather book: 'You are asking the wrong question. You want the One True Theory. There is no One True Theory. But there is a triage procedure: First, what is most urgent? Second, do multiple frameworks agree on any action? If yes, act there. Third, if they disagree, find the least controversial action that addresses the most urgent need. Fourth, document what remains unresolved for later reflection. This is not the perfect answer — it is the first-aid answer.'",
             "speaker_context": f"The advisor introduces Dennett's Moral First Aid Manual — a practical triage guide that draws on multiple theories without waiting to resolve which is correct. Like medical first aid, it prioritizes urgent action over theoretical perfection."},
            f"The Manual provides a triage procedure for moral and practical dilemmas: identify urgency, check for cross-theoretical convergence, act on agreement, document remaining disagreement. It is satisficing applied to ethics — not the perfect answer but a good-enough answer delivered in time to matter.",
            {"npc_personality": "Calm, practical, and deeply experienced. No patience for abstract debate when someone is suffering, but not anti-intellectual.",
             "npc_dialogue_seed": "I do not give answers. I give procedures. Tell me your situation and I will tell you which question to ask first.",
             "resolution_path": "Player learns the triage procedure and applies it to the dilemma, discovering that acting on convergence allows progress while the hard question remains open."}
        )

    # Default fallback
    return (
        {"context": f"The player encounters a situation in {setting} involving {core_desc}.",
         "text": f"An NPC demonstrates or discusses the concept in a {domain} context.",
         "speaker_context": f"This scenario illustrates {label} in a {domain} setting."},
        f"This scenario demonstrates {label}: {core_desc}",
        {"npc_personality": f"A thoughtful {domain} practitioner.",
         "npc_dialogue_seed": f"Let me show you something about how we think in {domain}.",
         "resolution_path": f"Player learns to recognize {label} in {domain} contexts."}
    )


def generate_prompt(code, ptype, domain):
    if ptype == "good_tool":
        return "What specific thinking tool or technique is the speaker using? How does it work, and why is it effective?"
    elif ptype == "bad_thinking":
        return "Something is wrong with the speaker's reasoning or rhetoric. What is the error, and how does it work?"
    else:  # dual
        return "This situation involves a thinking pattern that can be good or bad depending on context. What is it, and what makes it dual-natured?"


def generate_rubric(code, ptype):
    if ptype == "good_tool":
        return [
            {"level": 0, "description": "Player cannot identify the technique or sees nothing notable."},
            {"level": 1, "description": "Player senses something deliberate but cannot name or describe the method."},
            {"level": 2, "description": "Player partially identifies the technique but misses key elements or gets the structure wrong."},
            {"level": 3, "description": "Player identifies the technique, describes its structure, and can explain why it is effective."},
            {"level": 4, "description": "Player identifies the technique fully, explains its mechanism, discusses when it works and when it might fail, and can apply it to a new situation."},
        ]
    elif ptype == "bad_thinking":
        return [
            {"level": 0, "description": "Player accepts the reasoning at face value or sees nothing wrong."},
            {"level": 1, "description": "Player senses something is off but cannot articulate the problem."},
            {"level": 2, "description": "Player identifies a general problem but cannot name the specific error or explain its mechanism."},
            {"level": 3, "description": "Player identifies the specific error, explains how it works, and can point to the problematic move."},
            {"level": 4, "description": "Player identifies the error, explains its mechanism, distinguishes it from related patterns, and can detect it in novel contexts."},
        ]
    else:  # dual
        return [
            {"level": 0, "description": "Player sees only one side or picks a position without recognizing the structural tension."},
            {"level": 1, "description": "Player recognizes a tension but frames it as a simple disagreement rather than a structural dilemma."},
            {"level": 2, "description": "Player sees the dual nature but cannot fully articulate when the pattern is beneficial versus harmful."},
            {"level": 3, "description": "Player identifies the dual nature, explains both the protective and destructive aspects, and can articulate what determines which applies."},
            {"level": 4, "description": "Player identifies the dual nature, connects it to the broader framework, proposes meta-level approaches, and recognizes the genuine difficulty of the underlying problem."},
        ]


def generate_followup_wrong(code, ptype):
    followups = {
        "D1.5": "Imagine two people break the same rule. One has never heard of the rule. The other studied it for years and broke it on purpose. Is their rule-breaking the same?",
        "D1.6": "Try reading the statement two ways. First, the most boring, obvious way. Then the most dramatic, sweeping way. Is either reading both true and interesting?",
        "D1.7": "Try removing every 'surely' from the speech and reading the claims as bare assertions. Do they still sound obviously true?",
        "D1.8": "Compare the hedged recommendation to the bold one. Which one can you act on? Which one can you test? Which one helps you decide?",
        "D2.1": "Imagine taking the time to find the perfect answer. What happens during that time? What is the cost of waiting?",
        "D2.2": "If you only had mud and logs to work with, does that mean mud and logs are the best possible building materials?",
        "D2.3": "Set aside who is right. Focus on the move: 'This conversation is over.' What does that move do to the process of deliberation?",
        "D2.4": "Your rules have worked for years. Now you know they sometimes fail. Does knowing that mean you should stop using them?",
        "D2.5": "Suppose you add the missed item to the checklist. Problem solved? How long does the checklist get? Who decides what goes on it?",
        "D2.6": "Think about medical first aid. When someone is bleeding, the manual does not say 'first resolve the debate between germ theory and humoral theory.' It says 'apply pressure.' Can we do the same for moral emergencies?",
    }
    return followups.get(code, "Look more carefully at the structure of what happened. What specific move was made, and what was its effect?")


def generate_followup_right(code, ptype):
    followups = {
        "D1.5": "Can you think of a case where someone who did not understand the system produced something genuinely creative? If so, does that refute jootsing?",
        "D1.6": "Can you generate another deepity? Try to construct a statement that sounds profound but collapses when you separate its readings.",
        "D1.7": "Can you think of a case where 'surely' is used honestly? What distinguishes legitimate common-ground appeals from smuggled assumptions?",
        "D1.8": "When is hedging the right move? What distinguishes honest uncertainty from cowardly hedging?",
        "D2.1": "The satisficing protocol was written in advance. Does that make it optimal? And if it is never updated, could satisficing itself become a trap?",
        "D2.2": "Are there situations where satisficing and optimizing genuinely give the same answer? How would you tell the difference?",
        "D2.3": "Can you think of a conversation-stopper that should never be overridden? How do you know the difference between that case and this one?",
        "D2.4": "Your meta-heuristic — 'know when to trust your heuristics' — is itself a heuristic. What happens when you realize it is imperfect? Is there an infinite regress?",
        "D2.5": "Turn it on yourself: you navigate the world effortlessly, checking the right things and ignoring irrelevant ones. How do you do it? Can you articulate your method?",
        "D2.6": "What happens when the theories genuinely do not converge? When one says 'do X' and another says 'do not-X'? Does the Manual break down?",
    }
    return followups.get(code, "Good. Now stress-test the concept: under what conditions would it fail or need to be modified?")


# Generate all records
all_records = generate_all_records()

# Write to file
output_path = "/Users/bbaum/Documents/claude-projects/good-thinking-bot/corpus-tools/output/synthetic_dennett_fill.jsonl"
with open(output_path, "w") as f:
    for record in all_records:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

print(f"Generated {len(all_records)} records")
