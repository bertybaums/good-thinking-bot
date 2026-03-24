#!/usr/bin/env python3
"""Generate 750 synthetic microeconomics training records."""
import json
import random
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "output", "synthetic_microecon_fill.jsonl")

# ── Code definitions ──────────────────────────────────────────────────────
CODES = [
    ("C1.1", "Opportunity cost", "good_tool"),
    ("C1.2", "Comparative advantage", "good_tool"),
    ("C2.1", "Constrained optimization", "good_tool"),
    ("C2.2", "Marginal analysis", "good_tool"),
    ("C3.1", "Public goods and free riding", "dual"),
    ("C3.2", "Commons problems", "dual"),
    ("C4.1", "Bargaining and fairness", "good_tool"),
    ("C4.2", "Principal-agent problems", "dual"),
    ("C5.1", "Supply, demand, equilibrium", "good_tool"),
    ("C5.2", "Price controls and deadweight loss", "dual"),
    ("C6.1", "Externalities", "dual"),
    ("C6.2", "Information asymmetry", "dual"),
    ("C6.3", "Behavioral economics in markets", "dual"),
    ("C7.1", "Broken window fallacy", "bad_thinking"),
    ("C7.2", "Zero-sum thinking", "bad_thinking"),
]

# Tier distribution: 30 drill, 15 what_if, 5 puzzle per code
TIER_DIST = [("drill", 30), ("what_if", 15), ("puzzle", 5)]

# ── RPG Setting banks ─────────────────────────────────────────────────────
TOWNS = [
    "Ironhollow", "Dustmere", "Stoneglen", "Ravenmarch", "Millhaven",
    "Thornwall", "Coppergate", "Ashwick", "Brindlewood", "Havenport",
    "Kingsford", "Redthorn", "Frostmire", "Goldenvale", "Deepwell",
    "Silverpeak", "Whiteharbor", "Greymoor", "Oakshade", "Dawnfield",
    "Brackenmoor", "Cinderfall", "Drifthollow", "Elderwatch", "Fenwick",
    "Glassmere", "Heathbridge", "Ivydale", "Juniperton", "Kettlebrook",
    "Larkhaven", "Mossglen", "Northcrest", "Oldmarket", "Pinecroft",
    "Quarrystone", "Riverbend", "Stormholt", "Thistlewood", "Underhill",
    "Valecross", "Windmere", "Yarrow", "Ashenmoor", "Bellforge",
    "Cloverdale", "Dusthaven", "Eaglecrest", "Flintrock", "Grainfield",
]

NPCS = [
    "Bryn", "Elda", "Tormund", "Sable", "Gareth", "Wren", "Osric",
    "Fenna", "Declan", "Mira", "Halvard", "Liora", "Thane", "Isolde",
    "Cedric", "Rowena", "Aldric", "Blythe", "Corwin", "Dagna",
    "Elowen", "Falk", "Greta", "Hagan", "Iona", "Jorik", "Kenna",
    "Leif", "Maren", "Nils", "Orin", "Petra", "Quinn", "Rowan",
    "Sigrid", "Tavish", "Una", "Voss", "Willa", "Xander", "Ylva",
    "Zara", "Ansel", "Birgit", "Cael", "Dagny", "Einar", "Freya",
    "Gunnar", "Helga",
]

ROLES = [
    "blacksmith", "herbalist", "tavern keeper", "guild master", "farmer",
    "merchant", "quartermaster", "stable master", "weaver", "carpenter",
    "fishmonger", "baker", "miner", "shepherd", "brewer",
    "apothecary", "cartographer", "mason", "jeweler", "tanner",
    "innkeeper", "cooper", "fletcher", "potter", "chandler",
    "dyer", "scribe", "furrier", "vintner", "wheelwright",
]

# ── Template banks per code ───────────────────────────────────────────────

def pick(lst):
    return random.choice(lst)

def pick_town():
    return pick(TOWNS)

def pick_npc():
    return pick(NPCS)

def pick_role():
    return pick(ROLES)

def gold(lo, hi):
    return random.randint(lo, hi)

# ────────────────────────────────────────────────────────────────────────
# C1.1 — Opportunity cost
# ────────────────────────────────────────────────────────────────────────
def gen_C1_1(seq, tier):
    npc = pick_npc(); town = pick_town(); role = pick_role()
    # two tasks with different payoffs, one time slot
    pay_a = gold(30, 120); pay_b = gold(15, pay_a - 5)
    task_a_items = ["forge a ceremonial shield", "brew a batch of fire-resist potions",
                    "repair the castle gate", "tailor a noble's cloak", "craft silver rings",
                    "build a merchant's display cart", "shoe the lord's warhorse",
                    "carve a stone memorial", "bind a set of spell tomes", "paint guild banners",
                    "smoke a barrel of river trout", "assemble crossbow bolts", "tan a stack of hides",
                    "engrave a lord's signet", "polish a set of plate armor"]
    task_b_items = ["mend fishing nets", "deliver grain sacks", "sharpen farm tools",
                    "repair wooden fencing", "dye cloth for the market", "patch leather saddles",
                    "sort herbs for the apothecary", "stack firewood for the inn",
                    "clean and oil wagon wheels", "weave rope for the docks",
                    "grind flour at the mill", "press cider for the harvest feast",
                    "whittle arrow shafts", "glaze clay pots", "stitch grain sacks"]
    ta = pick(task_a_items); tb = pick(task_b_items)
    oc = pay_b
    net = pay_a - pay_b

    if tier == "drill":
        context = (f"The player meets {npc}, a {role} in {town}, who has one free day "
                   f"and two commissions: {ta} for {pay_a} gold, or {tb} for {pay_b} gold. "
                   f"Only one can be done.")
        text = (f"{npc} lays both work orders on the bench. 'I can {ta} for {pay_a} gold or "
                f"{tb} for {pay_b} gold. Only time for one. The first job pays {pay_a}, so "
                f"that is my profit — {pay_a} gold, clean and simple.' {npc} looks pleased.")
        speaker = (f"{npc} is counting revenue as profit and ignoring the forgone alternative.")
        ident = (f"{npc} says the profit from the {pay_a}-gold job is {pay_a} gold. "
                 f"What is the actual net gain of choosing it over the alternative?")
        formal = (f"OC of choosing A = value of best forgone B = {pay_b}. "
                  f"Net gain = {pay_a} - {pay_b} = {net}.")
        fuw = (f"If {npc} takes the {pay_a}-gold job, what would they have earned instead? "
               f"The difference is the real gain.")
        fur = (f"What if a third commission appeared worth {pay_a + 10} gold? "
               f"How does that change the opportunity cost of the original choice?")
    elif tier == "what_if":
        # three options
        pay_c = gold(pay_b + 5, max(pay_b + 6, pay_a - 1))
        context = (f"{npc} in {town} now has three commissions: {ta} ({pay_a} gold), "
                   f"{tb} ({pay_b} gold), and repair a noble's armor ({pay_c} gold). "
                   f"Time for only one.")
        text = (f"'{pay_a} gold for the first job. But I also have a {pay_c}-gold armor job "
                f"and a {pay_b}-gold one. I'll take the biggest — {pay_a} gold profit!' "
                f"says {npc}.")
        speaker = f"{npc} picks the best-paying job but still calls revenue profit."
        best_alt = max(pay_b, pay_c)
        net = pay_a - best_alt
        formal = (f"OC = best forgone = {best_alt}. Net = {pay_a} - {best_alt} = {net}. "
                  f"OC is the single best alternative, not the sum of all alternatives.")
        ident = (f"With three jobs available, what is the opportunity cost of the top-paying one? "
                 f"Is it {pay_b}, {pay_c}, or {pay_b + pay_c}?")
        fuw = (f"Opportunity cost is only the BEST forgone option, not the sum. "
               f"Which single alternative is most valuable?")
        fur = (f"If {npc} could hire an apprentice for 10 gold to do a second job, "
               f"how would that change the calculus?")
    else:  # puzzle
        context = (f"{npc} in {town} has the {pay_a}-gold commission but also "
                   f"a once-in-a-lifetime chance to apprentice under a master {role} for free — "
                   f"no pay but invaluable skills. How do you value a non-monetary opportunity?")
        text = (f"'{pay_a} gold is real. Learning from the master is... priceless? Worthless? "
                f"I cannot put a number on it.' {npc} is stuck.")
        speaker = f"{npc} struggles because opportunity cost requires comparing unlike values."
        formal = (f"OC still applies: the cost of taking the commission = value of the apprenticeship. "
                  f"The challenge is that the apprenticeship value is uncertain and non-monetary. "
                  f"Expected future earnings must be estimated.")
        ident = (f"Can opportunity cost apply when the alternative has no immediate monetary value? "
                 f"How should {npc} think about the apprenticeship?")
        fuw = (f"Think about what the apprenticeship leads to. If the new skills let {npc} "
               f"earn 200 gold per season next year, what is the apprenticeship worth in gold terms?")
        fur = (f"What role does risk play? The {pay_a} gold is certain; the apprenticeship "
               f"benefits are uncertain. Does that change the opportunity cost framework, "
               f"or do we need a new tool?")

    return {
        "id": f"C1.1-MF{seq:04d}",
        "taxonomy_code": "C1.1",
        "taxonomy_label": "Opportunity cost",
        "track": "microeconomics",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Opportunity cost",
            "pattern_description": (
                "The opportunity cost of an action is the value of the next-best alternative forgone. "
                f"{npc} treats revenue as profit without subtracting what is given up."
            ),
            "formal_form": formal,
            "why_wrong": None,
            "why_right": (
                "Every choice has a hidden cost: what you gave up to make it. "
                "True net gain = chosen benefit minus opportunity cost."
            ),
            "related_patterns": ["C1.2", "C2.2", "C7.1"],
            "counterpoint": (
                "Opportunity cost assumes alternatives are known. Under genuine uncertainty "
                "about what options exist, the concept still applies but is harder to operationalize."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": f"Player agrees {npc}'s profit equals revenue."},
                {"level": 1, "description": "Player senses something is missing but cannot articulate it."},
                {"level": 2, "description": "Player mentions the forgone job but does not calculate the net gain."},
                {"level": 3, "description": "Player identifies the opportunity cost and calculates correctly."},
                {"level": 4, "description": "Player calculates correctly and generalizes the principle to all scarce-resource decisions."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is hardworking and practical but counts revenue as profit out of habit.",
            "npc_dialogue_seed": f"'{pay_a} gold! Best commission I have had in weeks. Pure profit.'",
            "resolution_path": (
                f"If the player explains opportunity cost, {npc} starts keeping a ledger "
                f"of forgone alternatives, unlocking a side quest about workshop expansion."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 + PHIL 201 lecture notes",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C1.2 — Comparative advantage
# ────────────────────────────────────────────────────────────────────────
def gen_C1_2(seq, tier):
    npc_a = pick_npc(); npc_b = pick_npc()
    while npc_b == npc_a:
        npc_b = pick_npc()
    town = pick_town()
    good1 = pick(["wheat", "wool", "timber", "iron ore", "salt", "hops", "flax", "clay", "copper", "leather"])
    good2 = pick(["ale", "rope", "arrows", "bricks", "tools", "cloth", "candles", "barrels", "flour", "pottery"])
    # A is better at both; B has comparative advantage in good2
    a1 = random.randint(8, 16); a2 = random.randint(4, a1 - 1)
    b1 = random.randint(3, a1 - 2); b2 = random.randint(2, a2)
    # Ensure B has CA in good2: b2/b1 > a2/a1 → a1*b2 > a2*b1
    while a1 * b2 <= a2 * b1:
        b2 = min(b2 + 1, a2)
        b1 = max(b1 - 1, 2)
    oc_a_g2 = round(a1 / a2, 2)  # A's OC of 1 unit good2 in units of good1
    oc_b_g2 = round(b1 / b2, 2)

    if tier == "drill":
        context = (f"In {town}, {npc_a} can produce {a1} {good1} or {a2} {good2} per week. "
                   f"{npc_b} can produce {b1} {good1} or {b2} {good2} per week. "
                   f"{npc_a} is better at both and refuses to trade.")
        text = (f"{npc_a} scoffs: 'I make more of everything. Why would I trade with {npc_b}?' "
                f"{npc_b} looks dejected.")
        speaker = f"{npc_a} confuses absolute advantage with comparative advantage."
        ident = (f"{npc_a} outproduces {npc_b} in both goods. Should they still trade? "
                 f"Calculate opportunity costs.")
        formal = (f"{npc_a}: OC of 1 {good2} = {oc_a_g2} {good1}. "
                  f"{npc_b}: OC of 1 {good2} = {oc_b_g2} {good1}. "
                  f"Since {oc_b_g2} < {oc_a_g2}, {npc_b} has CA in {good2}; "
                  f"{npc_a} has CA in {good1}.")
        fuw = (f"Forget totals. What does {npc_a} sacrifice in {good1} to make one {good2}? "
               f"Now ask the same for {npc_b}. Who sacrifices less?")
        fur = (f"What trade ratio between {good1} and {good2} would make both better off?")
    elif tier == "what_if":
        context = (f"Same village, but now a road tax of 1 unit of any good applies to every trade. "
                   f"Does comparative advantage still justify specialization?")
        text = (f"'Even if your math works,' {npc_a} says, 'the tax collector takes a cut of every trade. "
                f"Maybe we are better off self-sufficient.'")
        speaker = f"Transaction costs can erode gains from trade."
        ident = (f"With a 1-unit trade tax, is specialization still beneficial? "
                 f"Calculate the net gains after tax.")
        formal = (f"Gains from trade must exceed transaction costs. "
                  f"If surplus from specialization > tax, trade still wins. "
                  f"Calculate pre-tax surplus, subtract tax, check if positive.")
        fuw = "Calculate what both produce alone vs. specialized-and-trading. Then subtract the tax."
        fur = "At what tax level does trade become unprofitable? What does that imply for trade policy?"
    else:
        context = (f"Three producers in {town} each make two goods. How does comparative advantage "
                   f"work with more than two parties? Can everyone benefit from a trade network?")
        text = (f"A third artisan, {pick_npc()}, joins the discussion. "
                f"'Two-way trade is neat, but we have three workshops. "
                f"Can your theory handle that?'")
        speaker = "Multi-party comparative advantage requires a more complex analysis."
        ident = ("Does comparative advantage extend to three or more parties? "
                 "What additional complications arise?")
        formal = ("With N>2 agents and M>2 goods, comparative advantage still applies "
                  "but the pattern of specialization is determined by the full matrix of opportunity costs. "
                  "General equilibrium theory handles this.")
        fuw = "Start with two-party cases and build up. The principle is the same; the math is bigger."
        fur = "What role do prices play in coordinating specialization across many producers?"

    return {
        "id": f"C1.2-MF{seq:04d}",
        "taxonomy_code": "C1.2",
        "taxonomy_label": "Comparative advantage",
        "track": "microeconomics",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Comparative advantage",
            "pattern_description": (
                "Comparative advantage depends on opportunity cost, not absolute productivity. "
                "Even if one party is better at everything, both benefit from specializing "
                "where their opportunity cost is lowest and trading."
            ),
            "formal_form": formal,
            "why_wrong": None,
            "why_right": (
                "Trade benefits do not require equal productivity. Specialization by "
                "comparative advantage increases total output and enables both parties to consume more."
            ),
            "related_patterns": ["C1.1", "C4.1", "C7.2"],
            "counterpoint": (
                "Transaction costs, transport risks, and strategic vulnerability "
                "can make self-sufficiency rational despite theoretical gains from trade."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": f"Player agrees {npc_a} has no reason to trade."},
                {"level": 1, "description": "Player suspects trade could help but cannot calculate why."},
                {"level": 2, "description": "Player calculates some opportunity costs but makes errors."},
                {"level": 3, "description": "Player correctly identifies who has CA in which good."},
                {"level": 4, "description": "Player calculates CA, proposes a beneficial trade ratio, and explains the logic."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc_a} is proud and productive; {npc_b} is skilled but slower.",
            "npc_dialogue_seed": f"'I make more of both. What could {npc_b} possibly offer me?'",
            "resolution_path": (
                f"If the player demonstrates CA with numbers, {npc_a} agrees to a trial trade. "
                f"Both end up with more goods. This unlocks a regional trade quest."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 1-2",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C2.1 — Constrained optimization
# ────────────────────────────────────────────────────────────────────────
def gen_C2_1(seq, tier):
    npc = pick_npc(); town = pick_town(); role = pick_role()
    budget = gold(80, 200)
    item_a = pick(["rations", "arrows", "healing herbs", "torches", "rope coils", "water skins", "iron ingots", "spell scrolls"])
    item_b = pick(["bandages", "lantern oil", "shields", "blankets", "lockpicks", "fire salts", "tent stakes", "map parchments"])
    while item_b == item_a:
        item_b = pick(["bandages", "lantern oil", "shields", "blankets", "lockpicks", "fire salts", "tent stakes", "map parchments"])
    cost_a = gold(3, 10); benefit_a = gold(2, 6)
    cost_b = gold(5, 15); benefit_b = gold(3, 8)
    need_a = gold(10, 25); need_b = gold(6, 16)
    min_a = -(-need_a // benefit_a)  # ceiling division
    min_b = -(-need_b // benefit_b)
    min_cost = min_a * cost_a + min_b * cost_b

    if min_cost > budget:
        budget = min_cost + gold(10, 40)

    if tier == "drill":
        context = (f"{npc}, a {role} in {town}, has {budget} gold to buy {item_a} and {item_b} "
                   f"for an expedition. {item_a} cost {cost_a} gold each ({benefit_a} units of supply). "
                   f"{item_b} cost {cost_b} gold each ({benefit_b} units of protection). "
                   f"Need at least {need_a} supply and {need_b} protection.")
        text = (f"'{budget} gold, no more. {item_a}: {cost_a} gold, {benefit_a} supply each. "
                f"{item_b}: {cost_b} gold, {benefit_b} protection each. "
                f"We need {need_a} supply and {need_b} protection minimum. "
                f"What is the cheapest way to meet both needs?'")
        speaker = f"{npc} wants to minimize cost subject to meeting minimum requirements."
        ident = f"Find the minimum-cost purchase that meets {need_a} supply and {need_b} protection."
        formal = (f"Min C = {cost_a}*A + {cost_b}*B s.t. {benefit_a}*A >= {need_a}, "
                  f"{benefit_b}*B >= {need_b}. A >= {min_a}, B >= {min_b}. "
                  f"Min cost = {min_cost}. Surplus = {budget - min_cost}.")
        fuw = (f"Handle each constraint separately: how many {item_a} for {need_a} supply? "
               f"Then how many {item_b} for {need_b} protection? Add up the costs.")
        fur = f"If the requirement for supply increases to {need_a + 10}, how does the solution change?"
    elif tier == "what_if":
        # Add a weight/carry constraint
        weight_a = gold(1, 3); weight_b = gold(2, 5); max_weight = min_a * weight_a + min_b * weight_b + gold(2, 8)
        context = (f"Same setup, but now {npc} also has a weight limit of {max_weight} units. "
                   f"Each {item_a} weighs {weight_a} and each {item_b} weighs {weight_b}.")
        text = (f"'My pack horse can carry {max_weight} weight. {item_a} weigh {weight_a} each, "
                f"{item_b} weigh {weight_b} each. Now I have two constraints — budget AND weight.'")
        speaker = f"{npc} faces a two-constraint optimization."
        ident = f"With both budget and weight constraints, find the cheapest feasible purchase."
        formal = (f"Min C = {cost_a}*A + {cost_b}*B s.t. {benefit_a}*A >= {need_a}, "
                  f"{benefit_b}*B >= {need_b}, {cost_a}*A + {cost_b}*B <= {budget}, "
                  f"{weight_a}*A + {weight_b}*B <= {max_weight}.")
        fuw = "Solve for the minimum quantities first, then check if both budget and weight are satisfied."
        fur = "Which constraint binds first — budget or weight? What does that tell you about the bottleneck?"
    else:
        context = (f"{npc} in {town} must provision for a journey with uncertain length. "
                   f"The trip could be 5, 7, or 10 days. How do you optimize under uncertainty?")
        text = (f"'If the pass is clear, five days. If the storms hit, ten. "
                f"Do I pack for the worst case and waste gold, or the best case and risk starvation?'")
        speaker = f"{npc} faces constrained optimization under uncertainty — expected value vs. worst case."
        ident = "How should you set constraints when the requirements are uncertain?"
        formal = ("Robust optimization: satisfy constraints under worst-case scenario. "
                  "Expected-value optimization: satisfy constraints on average, accepting some risk. "
                  "The choice depends on the cost of failure.")
        fuw = "What happens if you pack for 5 days and the trip takes 10? What is the cost of that failure?"
        fur = "Could you buy extra supplies along the route? How does that option change the optimization?"

    return {
        "id": f"C2.1-MF{seq:04d}",
        "taxonomy_code": "C2.1",
        "taxonomy_label": "Constrained optimization",
        "track": "microeconomics",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Constrained optimization",
            "pattern_description": (
                "Maximize or minimize an objective subject to binding constraints. "
                f"{npc} must meet requirements at minimum cost within a fixed budget."
            ),
            "formal_form": formal,
            "why_wrong": None,
            "why_right": (
                "Constrained optimization is the core microeconomic framework. "
                "Every agent faces scarce resources and must find the best feasible combination."
            ),
            "related_patterns": ["C2.2", "C1.1", "C5.1"],
            "counterpoint": (
                "Models assume known prices, divisible goods, and certain requirements. "
                "Real decisions involve uncertainty, lumpy goods, and changing prices."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player cannot set up the problem."},
                {"level": 1, "description": "Player identifies constraints but cannot solve."},
                {"level": 2, "description": "Player finds a feasible solution but not the optimum."},
                {"level": 3, "description": "Player finds the optimal solution and verifies constraints."},
                {"level": 4, "description": "Player solves correctly and discusses sensitivity to changing constraints."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is meticulous and frugal, hates waste.",
            "npc_dialogue_seed": f"'{budget} gold. Not a copper more. Help me stretch it.'",
            "resolution_path": (
                f"If the player solves the problem, {npc} saves gold for emergencies "
                f"and offers the player an advisor role."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 3",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C2.2 — Marginal analysis
# ────────────────────────────────────────────────────────────────────────
def gen_C2_2(seq, tier):
    npc = pick_npc(); town = pick_town(); role = pick_role()
    price = gold(12, 25)
    # Generate increasing MC series
    n_units = random.randint(5, 7)
    mc = sorted(random.sample(range(3, price + 15), n_units))
    # Find optimal Q where mc <= price
    q_star = sum(1 for c in mc if c <= price)
    total_profit = sum(price - c for c in mc[:q_star])

    product = pick(["healing potions", "enchanted arrows", "leather belts",
                     "iron horseshoes", "woven baskets", "clay jugs",
                     "herbal salves", "tallow candles", "smoked fish",
                     "copper rings", "linen tunics", "carved charms"])

    if tier == "drill":
        mc_str = ", ".join(str(c) for c in mc)
        context = (f"{npc}, a {role} in {town}, sells {product} for {price} gold each. "
                   f"The cost of each additional unit rises: {mc_str}.")
        text = (f"'{price} gold per {product[:-1] if product.endswith('s') else product}. "
                f"Costs keep rising: {mc_str} gold for units 1 through {n_units}. "
                f"How many should I make?'")
        speaker = f"{npc} needs to compare MB ({price}) to MC for each unit."
        ident = f"At {price} gold per unit with costs {mc_str}, how many should {npc} produce?"
        formal = (f"MB = {price} for each unit. MC = [{mc_str}]. "
                  f"Produce while MB >= MC. Q* = {q_star}. Total profit = {total_profit}.")
        fuw = "Check each unit: does it earn more than it costs? Stop at the first one that does not."
        fur = f"If the price rises to {price + 5}, how does optimal quantity change?"
    elif tier == "what_if":
        # Diminishing MB too
        mb_start = price + gold(5, 10)
        mb_list = [mb_start - i * random.randint(2, 4) for i in range(n_units)]
        mb_list = [max(m, 1) for m in mb_list]
        q_star2 = sum(1 for i in range(n_units) if mb_list[i] >= mc[i])
        mc_str = ", ".join(str(c) for c in mc)
        mb_str = ", ".join(str(m) for m in mb_list)
        context = (f"Now {npc}'s customers pay less per additional unit (diminishing MB): {mb_str}. "
                   f"Costs still rise: {mc_str}.")
        text = (f"'First buyer pays {mb_list[0]}, second pays {mb_list[1]}... "
                f"and my costs still climb. Where do I stop now?'")
        speaker = "Both MB and MC change with quantity. The intersection determines optimal output."
        ident = f"With both varying MB and MC, find the optimal quantity."
        formal = (f"MB = [{mb_str}]. MC = [{mc_str}]. "
                  f"Produce unit i if MB[i] >= MC[i]. Q* = {q_star2}.")
        fuw = "Compare MB and MC unit by unit. The first unit where MC exceeds MB is where you stop."
        fur = "What if you could price-discriminate perfectly? How would that change the analysis?"
    else:
        context = (f"{npc} considers whether to add a night shift. The marginal product of labor "
                   f"falls with tired workers, but the night market pays a premium. "
                   f"Is the marginal gain worth the marginal cost including fatigue and errors?")
        text = (f"'My workers make fewer pieces per hour at night, and they break more. "
                f"But the night market pays double. The numbers look good on paper, "
                f"but something feels off.'")
        speaker = "Marginal analysis must include all costs, including non-obvious ones like quality degradation."
        ident = "Should the workshop run a night shift? What hidden marginal costs might the simple calculation miss?"
        formal = ("Full MC includes: higher wages, lower productivity, breakage, worker health costs. "
                  "If full MC > night premium MB, the night shift destroys value despite appearing profitable.")
        fuw = "List every cost of the night shift, not just wages. Include quality, morale, equipment wear."
        fur = "How does this connect to the principal-agent problem? Night-shift workers are harder to monitor."

    return {
        "id": f"C2.2-MF{seq:04d}",
        "taxonomy_code": "C2.2",
        "taxonomy_label": "Marginal analysis",
        "track": "microeconomics",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Marginal analysis",
            "pattern_description": (
                "Compare the marginal benefit to the marginal cost of each additional unit. "
                "Continue if MB >= MC; stop when MC > MB."
            ),
            "formal_form": formal,
            "why_wrong": None,
            "why_right": (
                "Marginal analysis prevents both underproduction (stopping too early) "
                "and overproduction (making units that cost more than they earn)."
            ),
            "related_patterns": ["C2.1", "C1.1", "C5.1"],
            "counterpoint": (
                "Marginal analysis assumes you can adjust one unit at a time. "
                "When production is lumpy or irreversible, the framework needs adaptation."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player cannot determine optimal quantity."},
                {"level": 1, "description": "Player sees costs rising but guesses at quantity."},
                {"level": 2, "description": "Player compares costs and revenue but makes an error."},
                {"level": 3, "description": "Player correctly applies MB vs MC and finds the optimum."},
                {"level": 4, "description": "Player solves correctly and explains the general decision rule."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} tends to overproduce because they enjoy the craft.",
            "npc_dialogue_seed": f"'I made {n_units} last week and barely broke even. What went wrong?'",
            "resolution_path": (
                f"If the player explains marginal analysis, {npc} posts the rule above the workbench "
                f"and profits improve."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 7-8",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C3.1 — Public goods and free riding
# ────────────────────────────────────────────────────────────────────────
def gen_C3_1(seq, tier):
    npc = pick_npc(); town = pick_town()
    n_agents = random.randint(4, 8)
    cost = gold(60, 200)
    share = round(cost / n_agents)
    public_good = pick(["town wall repair", "bridge maintenance", "lighthouse oil",
                        "well cleaning", "road paving", "watchtower staffing",
                        "fire brigade funding", "harbor dredging", "dam reinforcement",
                        "market square upkeep", "grain silo maintenance", "signal beacon fuel"])

    if tier == "drill":
        context = (f"{town} has {n_agents} merchants who benefit from {public_good}. "
                   f"The total cost is {cost} gold per month ({share} gold each). "
                   f"One merchant, {npc}, proposes letting the others cover it.")
        text = (f"'{share} gold is {share} gold,' says {npc}. 'If the other {n_agents - 1} pay, "
                f"the {public_good} happens and I save my share. "
                f"The {public_good} benefits me whether I pay or not.'")
        speaker = f"{npc} identifies the free-rider incentive in a public goods problem."
        ident = (f"What happens if every merchant reasons like {npc}? "
                 f"Why does this problem arise?")
        formal = (f"Public good: non-rival, non-excludable. Each agent's dominant strategy "
                  f"is to free ride. If all free ride, good is not provided. N-player PD.")
        fuw = f"If {npc} doesn't pay and the rest do, {npc} saves {share} gold. Now imagine all {n_agents} think this way."
        fur = f"What mechanism could the merchants create to prevent free riding?"
    elif tier == "what_if":
        threshold = gold(int(cost * 0.6), int(cost * 0.9))
        context = (f"The {public_good} only works if at least {threshold} gold is raised. "
                   f"If contributions fall short, the money is wasted. "
                   f"This is a threshold public goods game.")
        text = (f"'We need {threshold} gold or the whole project fails. "
                f"Do I risk contributing and others not? Or hold back and guarantee the project fails?'")
        speaker = "The threshold creates a coordination problem on top of the free-rider problem."
        ident = ("With a threshold, how does the strategic situation change? "
                 "Is free riding still dominant?")
        formal = (f"Threshold public good: G provided only if sum(contributions) >= {threshold}. "
                  f"No dominant strategy — depends on beliefs about others' contributions. "
                  f"Assurance game rather than pure PD.")
        fuw = "If you believe others will contribute enough, your best move is to also contribute. If you doubt them, you hold back. What breaks the cycle?"
        fur = "How does a 'matching grant' (a donor matches every gold contributed) change the calculus?"
    else:
        context = (f"The merchants of {town} have solved the free-rider problem for {public_good} "
                   f"through social enforcement for years. But the town is growing, and new merchants "
                   f"arrive who have no social ties. Does the informal system still work at scale?")
        text = (f"'When there were five of us, shame kept everyone honest. Now there are twenty "
                f"and half of them are strangers. Our old system is breaking down.'")
        speaker = "Informal solutions to public goods problems scale poorly. At what point is formal governance needed?"
        ident = ("Why do informal free-rider solutions break down as group size grows? "
                 "What institutional alternatives exist?")
        formal = ("As N grows: monitoring costs rise, social pressure weakens, "
                  "marginal impact of each contribution falls. "
                  "Transition to formal taxation/governance becomes necessary.")
        fuw = "What made the old system work? Personal knowledge, repeated interaction, shame. Which of those survive growth?"
        fur = "Ostrom identified design principles for self-governing commons. Which apply here?"

    return {
        "id": f"C3.1-MF{seq:04d}",
        "taxonomy_code": "C3.1",
        "taxonomy_label": "Public goods and free riding",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Public goods and free riding",
            "pattern_description": (
                "A public good is non-rival and non-excludable, creating a free-rider incentive: "
                "each agent benefits regardless of contribution. "
                "Individual rationality leads to collective underprovision."
            ),
            "formal_form": formal,
            "why_wrong": (
                "Free riding is individually rational but collectively destructive. "
                "If universalized, the good is not provided and all are worse off."
            ),
            "why_right": (
                "Recognizing the free-rider problem is the first step toward solutions: "
                "binding agreements, social enforcement, or centralized provision."
            ),
            "related_patterns": ["C3.2", "C4.1", "B4.1"],
            "counterpoint": (
                "Not all shared goods are public goods. Excludability and rivalry vary on a spectrum. "
                "Club goods (excludable but non-rival) avoid the free-rider problem."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": f"Player sees nothing wrong with {npc}'s reasoning."},
                {"level": 1, "description": "Player senses collective failure but cannot explain the mechanism."},
                {"level": 2, "description": "Player identifies under-provision but not the underlying properties."},
                {"level": 3, "description": "Player identifies non-rivalry, non-excludability, and the PD structure."},
                {"level": 4, "description": "Player identifies all elements and proposes solution mechanisms."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is shrewd and unapologetic about self-interest.",
            "npc_dialogue_seed": f"'Why should I pay when the {public_good} happens whether I chip in or not?'",
            "resolution_path": (
                f"If the player identifies the problem and proposes a mechanism, "
                f"the merchants form a binding charter."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 12 + W10-W11 lecture notes",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C3.2 — Commons problems
# ────────────────────────────────────────────────────────────────────────
def gen_C3_2(seq, tier):
    npc = pick_npc(); town = pick_town()
    n_families = random.randint(4, 8)
    resource = pick(["fishing lake", "grazing meadow", "timber forest",
                     "iron mine", "peat bog", "oyster bed",
                     "wild herb field", "clay quarry", "fresh spring",
                     "berry thicket", "reed marsh", "salt flat"])
    unit = pick(["fish", "sheep grazing days", "timber loads", "ore carts",
                 "peat bricks", "bushels", "herb bundles", "clay blocks",
                 "water barrels", "crates of berries", "reed bundles", "salt bags"])
    sustainable = gold(40, 80)
    per_family_safe = sustainable // n_families
    current_total = sustainable + gold(10, 30)

    if tier == "drill":
        context = (f"The {resource} near {town} sustains {sustainable} {unit} per season. "
                   f"{n_families} families share it. Recently, total extraction hit {current_total}, "
                   f"exceeding the sustainable yield.")
        text = (f"{npc} hauls in a heavy load. 'If I leave these in the {resource}, "
                f"someone else takes them tomorrow. At least this way my family eats.' "
                f"The elder notes extraction is {current_total - sustainable} {unit} above sustainable levels.")
        speaker = f"{npc} follows individually rational logic that leads to collective depletion."
        ident = (f"Each family benefits from taking more, but the {resource} is declining. "
                 f"What structural problem drives this?")
        formal = (f"Common-pool resource: rival, non-excludable. "
                  f"Private MB of extra extraction > private MC (shared 1/{n_families}). "
                  f"Each overextracts. Total > sustainable yield {sustainable}.")
        fuw = (f"When {npc} takes one extra {unit[:-1] if unit.endswith('s') else unit}, "
               f"who gets the benefit? Who bears the cost of depletion?")
        fur = "What governance mechanism could align individual incentives with sustainability?"
    elif tier == "what_if":
        context = (f"The families around the {resource} have set a catch limit of {per_family_safe} "
                   f"{unit} per family. But one family starts cheating at night. "
                   f"How do you enforce commons agreements?")
        text = (f"'We all agreed to {per_family_safe} each. But my neighbor's barn is suspiciously full. "
                f"If they cheat and I don't, I'm the fool.'")
        speaker = "Enforcement is the key challenge in commons governance."
        ident = ("How does the incentive to cheat on commons agreements mirror the original problem? "
                 "What enforcement mechanisms work?")
        formal = ("Compliance is a second-order public good: everyone benefits from enforcement "
                  "but each prefers others bear the cost of monitoring. "
                  "Solutions: peer monitoring, rotational inspection, graduated sanctions.")
        fuw = "The agreement to limit extraction is itself a public good. What prevents free riding on the agreement?"
        fur = "Ostrom found graduated sanctions work better than harsh punishment. Why might that be?"
    else:
        context = (f"A wealthy merchant offers to buy the {resource} and charge families "
                   f"a usage fee. This would solve overextraction but create a monopoly. "
                   f"A councilor proposes government regulation instead. "
                   f"A third option: community self-governance. Which is best?")
        text = (f"'Privatize it, regulate it, or govern it ourselves? "
                f"Each option has costs. Which problem do you want — monopoly, bureaucracy, or enforcement?'")
        speaker = "Three solutions to the commons — private, state, communal — each with distinct trade-offs."
        ident = ("Compare privatization, regulation, and community governance for a commons problem. "
                 "What are the trade-offs of each?")
        formal = ("Privatization: solves overextraction but creates monopoly power. "
                  "Regulation: needs information and enforcement capacity. "
                  "Community governance: needs trust and monitoring but preserves local knowledge.")
        fuw = "What problem does each solution create while solving the original one?"
        fur = "Ostrom showed community governance can work. Under what conditions does it fail?"

    return {
        "id": f"C3.2-MF{seq:04d}",
        "taxonomy_code": "C3.2",
        "taxonomy_label": "Commons problems",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Commons problems (Tragedy of the commons)",
            "pattern_description": (
                "A common-pool resource is rival but non-excludable. "
                "Each user captures full private benefit of extraction but bears only a fraction "
                "of the depletion cost, driving overuse."
            ),
            "formal_form": formal,
            "why_wrong": (
                "Individual rationality drives overextraction. "
                "The problem is structural, not moral — the incentive system is misaligned."
            ),
            "why_right": (
                "Recognizing the commons structure points toward solutions: "
                "property rights, catch limits, or community governance."
            ),
            "related_patterns": ["C3.1", "C6.1", "B4.1"],
            "counterpoint": (
                "Not all commons are doomed. Ostrom documented successful community governance "
                "of shared resources without privatization or centralized control."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player blames individual greed without seeing the structure."},
                {"level": 1, "description": "Player sees overharvesting but not the incentive asymmetry."},
                {"level": 2, "description": "Player identifies individual incentive but not the rivalry/excludability properties."},
                {"level": 3, "description": "Player identifies the tragedy of the commons structure fully."},
                {"level": 4, "description": "Player identifies the structure and proposes governance solutions."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is pragmatic, not malicious — responding rationally to bad incentives.",
            "npc_dialogue_seed": f"'If I leave it, someone else takes it. At least my family benefits.'",
            "resolution_path": (
                f"If the player identifies the commons problem and proposes governance, "
                f"the families convene a council and establish catch limits."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 12 + Ostrom",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C4.1 — Bargaining and fairness
# ────────────────────────────────────────────────────────────────────────
def gen_C4_1(seq, tier):
    npc_a = pick_npc(); npc_b = pick_npc()
    while npc_b == npc_a:
        npc_b = pick_npc()
    town = pick_town()
    surplus = gold(40, 120)
    outside_a = gold(5, surplus // 3)
    outside_b = gold(5, surplus // 3)
    remaining = surplus - outside_a - outside_b
    split_a = round(outside_a + remaining / 2, 1)
    split_b = round(outside_b + remaining / 2, 1)

    goods = pick(["salt for iron", "timber for cloth", "grain for tools",
                  "wool for wine", "hides for spices", "copper for glass",
                  "herbs for silver", "fish for pottery", "wax for dyes", "honey for rope"])

    if tier == "drill":
        context = (f"{npc_a} and {npc_b} in {town} negotiate a trade of {goods}. "
                   f"Total surplus from trade: {surplus} gold. "
                   f"{npc_a}'s outside option: {outside_a} gold. "
                   f"{npc_b}'s outside option: {outside_b} gold.")
        text = (f"'We agree the deal creates {surplus} gold in value. "
                f"But I can walk away and get {outside_a} from another buyer,' says {npc_a}. "
                f"'And I can get {outside_b} elsewhere,' replies {npc_b}. "
                f"'So how do we split the {surplus}?'")
        speaker = "Both understand surplus exists but need a principled way to divide it."
        ident = (f"Surplus = {surplus}, outside options = {outside_a} and {outside_b}. "
                 f"What is a fair split?")
        formal = (f"Nash bargaining: remaining = {surplus} - {outside_a} - {outside_b} = {remaining}. "
                  f"Split equally: {npc_a} gets {split_a}, {npc_b} gets {split_b}.")
        fuw = "Each party's outside option is their guaranteed floor. Subtract both floors from the surplus. Split the remainder."
        fur = f"If {npc_a}'s outside option improves to {outside_a + 15}, how does the split change?"
    elif tier == "what_if":
        # Ultimatum framing
        context = (f"{npc_a} makes a take-it-or-leave-it offer to {npc_b} for a {surplus}-gold surplus deal. "
                   f"If {npc_b} rejects, both get nothing. "
                   f"Theory says {npc_b} should accept any positive amount. "
                   f"But {npc_b} rejects a 90/10 split.")
        text = (f"'{npc_a} offered me {surplus // 10} gold out of {surplus}. Technically that is better "
                f"than zero. But it is insulting and I refused,' says {npc_b}. "
                f"'Why would you reject free money?' asks {npc_a}.")
        speaker = "Ultimatum game shows fairness concerns override narrow self-interest."
        ident = "Why would a rational agent reject a positive offer? What does this say about rationality?"
        formal = ("Standard theory: accept any offer > 0. Behavioral evidence: offers below ~30% "
                  "are frequently rejected. Fairness preferences, inequality aversion, and punishment "
                  "of perceived unfairness drive rejections.")
        fuw = "Is getting something always better than getting nothing? What if accepting signals you tolerate exploitation?"
        fur = "How do repeated interactions change ultimatum behavior? What about anonymous one-shot games?"
    else:
        context = (f"Three parties in {town} must split a joint surplus. "
                   f"Any two can form a coalition excluding the third. "
                   f"How does the possibility of exclusion change bargaining?")
        text = (f"'If you two cut me out, you split {surplus - 10} between you. "
                f"But if I join, total rises to {surplus + 20}. "
                f"You need me, but how much am I worth?'")
        speaker = "Coalition bargaining introduces the threat of exclusion."
        ident = "In three-party bargaining with coalition options, how is surplus divided?"
        formal = ("Shapley value: each agent's share reflects their average marginal contribution "
                  "across all possible coalition orderings. "
                  "Agents who add more value to more coalitions get larger shares.")
        fuw = "What is each person's marginal contribution? What would each pair earn without the third?"
        fur = "How does coalition bargaining relate to political alliances and legislative deal-making?"

    return {
        "id": f"C4.1-MF{seq:04d}",
        "taxonomy_code": "C4.1",
        "taxonomy_label": "Bargaining and fairness",
        "track": "microeconomics",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Bargaining and fairness",
            "pattern_description": (
                "Fair division depends on outside options, not just the total surplus. "
                "Better alternatives give more bargaining power."
            ),
            "formal_form": formal,
            "why_wrong": None,
            "why_right": (
                "Bargaining theory prevents naive 50-50 splits and shows "
                "how outside options determine each party's fair share."
            ),
            "related_patterns": ["C1.1", "C4.2", "C7.2"],
            "counterpoint": (
                "Nash bargaining assumes equal power after outside options. "
                "In reality, patience, information, and social dynamics all matter."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player suggests 50-50 without considering outside options."},
                {"level": 1, "description": "Player recognizes outside options matter but cannot calculate."},
                {"level": 2, "description": "Player accounts for floors but splits remainder incorrectly."},
                {"level": 3, "description": "Player correctly applies Nash bargaining solution."},
                {"level": 4, "description": "Player solves correctly and discusses how changing outside options shift power."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc_a} is assertive; {npc_b} is shrewd but fair.",
            "npc_dialogue_seed": f"'We both gain from this deal. But how much each of us gains — that is the question.'",
            "resolution_path": (
                "If the player solves the bargaining problem, both merchants accept "
                "and offer the player a commission on future trades."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 5 + W8 lecture notes",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C4.2 — Principal-agent problems
# ────────────────────────────────────────────────────────────────────────
def gen_C4_2(seq, tier):
    principal = pick_npc(); agent = pick_npc()
    while agent == principal:
        agent = pick_npc()
    town = pick_town()
    wage = gold(30, 80)
    enterprise = pick(["apple orchard", "wool workshop", "fishing fleet",
                       "silver mine", "grain mill", "vineyard",
                       "cattle ranch", "silk loom", "spice warehouse",
                       "lumber camp", "brewery", "pottery kiln"])
    output_good = "output expected"
    shortfall_pct = random.randint(25, 50)

    if tier == "drill":
        context = (f"Lady {principal} in {town} hired {agent} to manage her {enterprise} "
                   f"while she is away. {agent} receives {wage} gold per month flat. "
                   f"Output fell {shortfall_pct}% below expectations.")
        text = (f"'{agent} gets {wage} gold whether the {enterprise} prospers or fails. "
                f"I was in the capital and could not observe his effort. "
                f"He had no reason to push himself,' says {principal}.")
        speaker = f"Flat wage + unobservable effort = moral hazard."
        ident = (f"Why does the flat wage create a shirking incentive? "
                 f"How might {principal} redesign the contract?")
        formal = (f"Agent payoff = {wage} regardless of effort. "
                  f"Cost of effort = c(e) > 0. Agent minimizes cost by choosing minimum effort. "
                  f"Solutions: performance pay, monitoring, bonding.")
        fuw = (f"If {agent} earns {wage} whether output is high or low, "
               f"what incentive does he have to work hard?")
        fur = "What are the trade-offs of performance pay? What happens if output falls due to bad luck, not shirking?"
    elif tier == "what_if":
        context = (f"{principal} now offers {agent} a share of {enterprise} profits. "
                   f"But {agent} worries: 'What if crops fail through no fault of mine? "
                   f"I work hard and still earn nothing.' "
                   f"How do you balance incentives with risk-sharing?")
        text = (f"'Pure performance pay punishes me for bad weather,' says {agent}. "
                f"'Pure flat pay gives me no reason to try,' admits {principal}. "
                f"'Is there a middle ground?'")
        speaker = "The incentive-insurance trade-off is central to contract design."
        ident = "Design a contract that motivates effort while protecting the agent from uncontrollable risk."
        formal = ("Optimal contract: base wage + performance bonus. "
                  "Base covers agent's risk. Bonus aligns incentives. "
                  "Higher risk aversion of agent -> higher base, lower bonus. "
                  "More observable effort -> stronger performance link.")
        fuw = "What if the wage has two parts: a guaranteed minimum plus a bonus tied to output?"
        fur = "How does this relate to sharecropping, franchise agreements, or CEO compensation?"
    else:
        context = (f"The {enterprise} employs multiple workers. {agent} is the manager. "
                   f"The workers have the same moral hazard problem with {agent} "
                   f"that {agent} has with {principal}. It's agents all the way down.")
        text = (f"'I cannot watch {agent}, and {agent} cannot watch every worker. "
                f"The problem multiplies with each layer of delegation,' says {principal}.")
        speaker = "Multi-layer principal-agent chains amplify moral hazard."
        ident = "How does the principal-agent problem compound across organizational layers?"
        formal = ("Each layer: effort unobservable, incentive dilution. "
                  "Solutions: organizational culture (intrinsic motivation), "
                  "peer monitoring, flat hierarchies, residual claimancy at each level.")
        fuw = "If the manager shirks, how do workers below know whether to work hard?"
        fur = "This is why firms exist as alternatives to market contracts (Coase). How does organizational design mitigate layered moral hazard?"

    return {
        "id": f"C4.2-MF{seq:04d}",
        "taxonomy_code": "C4.2",
        "taxonomy_label": "Principal-agent problems",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Principal-agent problems and moral hazard",
            "pattern_description": (
                "When a principal delegates to an agent whose effort is unobservable, "
                "the agent has rational incentive to shirk under flat pay. "
                "The problem is the incentive structure, not the person."
            ),
            "formal_form": formal,
            "why_wrong": (
                "Flat wages make shirking rational. The contract structure, not character, drives the behavior."
            ),
            "why_right": (
                "Recognizing the principal-agent structure leads to solutions: "
                "performance pay, monitoring, or bonding."
            ),
            "related_patterns": ["C6.2", "C4.1", "C3.1"],
            "counterpoint": (
                "Intrinsic motivation, reputation, and social norms can substitute for financial incentives. "
                "Not all agents shirk under flat pay."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player blames the agent's character."},
                {"level": 1, "description": "Player senses the pay is wrong but cannot explain why."},
                {"level": 2, "description": "Player identifies no incentive to work but proposes no solution."},
                {"level": 3, "description": "Player identifies moral hazard and proposes incentive-compatible contract."},
                {"level": 4, "description": "Player identifies moral hazard, proposes solutions, and distinguishes from adverse selection."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{principal} is fair-minded; {agent} is capable when motivated.",
            "npc_dialogue_seed": f"'I do not want to fire {agent}. I want to fix the system.'",
            "resolution_path": (
                f"If the player designs a better contract, output improves and "
                f"{principal} offers the player a consulting role."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 6 + W9 lecture notes",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C5.1 — Supply, demand, equilibrium
# ────────────────────────────────────────────────────────────────────────
def gen_C5_1(seq, tier):
    npc = pick_npc(); town = pick_town()
    good = pick(["grain", "lumber", "iron", "salt", "wool", "fish",
                 "leather", "ale", "herbs", "clay", "oil", "wax"])
    # Generate linear S and D
    slope_s = random.randint(5, 15)
    intercept_d = random.randint(60, 120)
    slope_d = random.randint(5, 15)
    # Equilibrium: slope_s * P = intercept_d - slope_d * P
    # P* = intercept_d / (slope_s + slope_d)
    p_star_exact = intercept_d / (slope_s + slope_d)
    p_star = round(p_star_exact)
    if p_star < 2:
        p_star = 5; intercept_d = (slope_s + slope_d) * 5
    q_star = slope_s * p_star

    if tier == "drill":
        # Create a nice table
        prices = sorted(set([max(1, p_star - 2), max(1, p_star - 1), p_star, p_star + 1, p_star + 2]))
        table_rows = []
        for p in prices:
            qs = slope_s * p
            qd = max(0, intercept_d - slope_d * p)
            table_rows.append((p, qs, qd))
        table_str = "Price | Supply | Demand\\n" + "\\n".join(f"  {p}   |   {qs}   |   {qd}" for p, qs, qd in table_rows)
        context = (f"The market master in {town} posts {good} supply and demand. "
                   f"Supply: Qs = {slope_s}*P. Demand: Qd = {intercept_d} - {slope_d}*P.")
        text = (f"The market master shows the board: {table_str}. "
                f"'Last week I set the price wrong and there were fights. "
                f"Help me find the price where supply meets demand.'")
        speaker = "The market master needs the equilibrium price."
        ident = f"Find the price where quantity supplied equals quantity demanded for {good}."
        formal = (f"Qs = {slope_s}*P = Qd = {intercept_d} - {slope_d}*P. "
                  f"P* = {intercept_d}/({slope_s}+{slope_d}) = {p_star_exact:.1f} ≈ {p_star}. "
                  f"Q* ≈ {q_star}.")
        fuw = "At which price on the board are supply and demand closest? That is near equilibrium."
        fur = f"What if the king decrees {good} cannot sell above {max(1, p_star - 2)} gold?"
    elif tier == "what_if":
        shock = pick(["a drought cuts supply in half", "a trade caravan doubles supply",
                      "a festival doubles demand", "a new substitute good halves demand",
                      "an export ban removes half the supply", "population growth raises demand by 50%"])
        context = (f"The {good} market in {town} was in equilibrium at P*={p_star}, Q*={q_star}. "
                   f"Then {shock}.")
        text = (f"'The market was balanced. Now {shock}. "
                f"Prices are moving and I cannot figure out where they will settle.'")
        speaker = "A supply or demand shock shifts equilibrium."
        ident = f"After {shock}, what happens to equilibrium price and quantity?"
        formal = ("Shift the affected curve. New equilibrium at new intersection. "
                  "Supply decrease → higher P, lower Q. Demand increase → higher P, higher Q. Etc.")
        fuw = "Which curve shifted? In which direction? Trace the new intersection."
        fur = "What if supply and demand both shift simultaneously? Can you predict the new price without more information?"
    else:
        context = (f"The {good} market in {town} has a dominant seller (the guild) that "
                   f"controls 80% of supply. Prices are above the competitive equilibrium. "
                   f"Is this market 'in equilibrium'?")
        text = (f"'The guild keeps prices high by restricting supply. Buyers complain, "
                f"but nobody else can sell. Is this equilibrium or exploitation?'")
        speaker = "Market power means competitive equilibrium does not apply directly."
        ident = "When one seller dominates, what replaces the competitive supply-demand model?"
        formal = ("Monopoly: seller sets P above competitive level, restricting Q. "
                  "Creates deadweight loss compared to competitive equilibrium. "
                  "Still an 'equilibrium' but not the same as competitive equilibrium.")
        fuw = "In competitive markets, no single seller can influence price. What changes when one seller is large enough to do so?"
        fur = "Is monopoly always harmful? What about natural monopolies or innovation incentives?"

    return {
        "id": f"C5.1-MF{seq:04d}",
        "taxonomy_code": "C5.1",
        "taxonomy_label": "Supply, demand, equilibrium",
        "track": "microeconomics",
        "pattern_type": "good_tool",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Supply, demand, and market equilibrium",
            "pattern_description": (
                "At equilibrium, quantity supplied equals quantity demanded. "
                "Prices above equilibrium create surpluses; prices below create shortages."
            ),
            "formal_form": formal,
            "why_wrong": None,
            "why_right": (
                "The equilibrium price coordinates decentralized buyers and sellers. "
                "The market naturally adjusts toward the clearing price."
            ),
            "related_patterns": ["C5.2", "C2.2", "C6.1"],
            "counterpoint": (
                "Perfect competition, full information, and no externalities are assumed. "
                "Real markets may not clear due to frictions."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player cannot find where supply meets demand."},
                {"level": 1, "description": "Player recognizes S and D should equal but guesses the price."},
                {"level": 2, "description": "Player identifies equilibrium is nearby but cannot solve exactly."},
                {"level": 3, "description": "Player correctly determines equilibrium P and Q."},
                {"level": 4, "description": "Player solves correctly and explains the adjustment mechanism."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": "The market master is practical and grateful for help.",
            "npc_dialogue_seed": "'Every week it is either a brawl or unsold goods. There must be a right price.'",
            "resolution_path": (
                "If the player finds equilibrium, the market runs smoothly. "
                "The market master asks for help with the next challenge."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 8",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C5.2 — Price controls and deadweight loss
# ────────────────────────────────────────────────────────────────────────
def gen_C5_2(seq, tier):
    npc = pick_npc(); town = pick_town()
    good = pick(["grain", "bread", "firewood", "salt", "wool", "medicine",
                 "iron nails", "candles", "lamp oil", "flour"])
    p_eq = gold(5, 12)
    q_eq = gold(40, 80)
    ceiling = p_eq - gold(1, 3)
    # At ceiling: lower supply, higher demand
    qs_at_ceiling = q_eq - gold(10, 25)
    qd_at_ceiling = q_eq + gold(10, 25)
    shortage = qd_at_ceiling - qs_at_ceiling

    if tier == "drill":
        context = (f"The king decrees that {good} in {town} cannot sell above {ceiling} gold. "
                   f"Equilibrium was P*={p_eq}, Q*={q_eq}. "
                   f"At {ceiling}: Qs={qs_at_ceiling}, Qd={qd_at_ceiling}.")
        text = (f"'The king means well, but at {ceiling} gold, suppliers bring only "
                f"{qs_at_ceiling} units while {qd_at_ceiling} want to buy. "
                f"That is a shortage of {shortage}. A black market is forming.'")
        speaker = "Price ceiling below equilibrium creates shortage and deadweight loss."
        ident = (f"With a price ceiling of {ceiling}, what happens to the market? "
                 f"Who benefits and who is harmed?")
        formal = (f"Ceiling Pc={ceiling} < P*={p_eq}. Qs({ceiling})={qs_at_ceiling} < "
                  f"Qd({ceiling})={qd_at_ceiling}. Shortage={shortage}. "
                  f"DWL = lost surplus from trades between Q={qs_at_ceiling} and Q={q_eq}.")
        fuw = f"At {ceiling} gold, how many units are supplied? How many demanded? What happens to the gap?"
        fur = "How might you achieve cheap {good} for the poor without a price ceiling? Consider targeted subsidies."
    elif tier == "what_if":
        floor = p_eq + gold(1, 3)
        qs_at_floor = q_eq + gold(10, 20)
        qd_at_floor = q_eq - gold(10, 20)
        surplus_units = qs_at_floor - qd_at_floor
        context = (f"Instead of a ceiling, the guild sets a price floor of {floor} gold for {good} "
                   f"to protect producers. Qs at floor = {qs_at_floor}, Qd = {qd_at_floor}.")
        text = (f"'The guild says no one can sell below {floor}. Producers love it. "
                f"But now there are {surplus_units} unsold units piling up.'")
        speaker = "Price floor above equilibrium creates surplus and deadweight loss."
        ident = f"A price floor of {floor} creates what market outcome? Who gains, who loses?"
        formal = (f"Floor Pf={floor} > P*={p_eq}. Qs={qs_at_floor} > Qd={qd_at_floor}. "
                  f"Surplus={surplus_units}. Producers who sell gain; those who cannot sell, and all buyers, lose.")
        fuw = "At a higher price, producers want to sell more but buyers want less. What happens to the excess?"
        fur = "Minimum wage is a price floor on labor. Apply this analysis: who benefits and who might be harmed?"
    else:
        context = (f"The {good} market in {town} has both a ceiling (to help buyers) "
                   f"and a subsidy (to compensate sellers). Is this better or worse than "
                   f"a simple ceiling? What about a simple subsidy without a ceiling?")
        text = (f"'The king caps the price AND pays sellers the difference. "
                f"Clever? Or just a more expensive way to do the same thing?'")
        speaker = "Comparing policy instruments: ceiling, subsidy, ceiling-plus-subsidy."
        ident = "Compare a price ceiling, a producer subsidy, and a ceiling with subsidy. Which achieves the equity goal at lowest efficiency cost?"
        formal = ("Ceiling: shortage + DWL. Subsidy alone: no shortage, higher quantity, government cost. "
                  "Ceiling + subsidy: no shortage if subsidy covers gap, but fiscal cost. "
                  "Subsidy alone typically more efficient than ceiling.")
        fuw = "What does each policy cost — to whom? Make a ledger: buyers, sellers, government, efficiency."
        fur = "When might a ceiling be preferred despite its inefficiency? Consider political economy."

    return {
        "id": f"C5.2-MF{seq:04d}",
        "taxonomy_code": "C5.2",
        "taxonomy_label": "Price controls and deadweight loss",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Price controls and deadweight loss",
            "pattern_description": (
                "Binding price controls prevent the market from clearing. "
                "Ceilings create shortages; floors create surpluses. "
                "Both generate deadweight loss from unrealized trades."
            ),
            "formal_form": formal,
            "why_wrong": (
                "Price controls are well-intentioned but create predictable inefficiencies. "
                "The hidden cost is the trades that no longer occur."
            ),
            "why_right": (
                "Understanding deadweight loss quantifies the cost of price controls, "
                "enabling comparison with alternative policies."
            ),
            "related_patterns": ["C5.1", "C6.1", "C7.1"],
            "counterpoint": (
                "If the equilibrium allocation is unjust, efficiency losses may be acceptable. "
                "Price controls may be defensible as second-best solutions."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player thinks the control simply helps everyone."},
                {"level": 1, "description": "Player suspects a problem but cannot quantify it."},
                {"level": 2, "description": "Player calculates shortage/surplus but misses deadweight loss."},
                {"level": 3, "description": "Player identifies shortage/surplus and deadweight loss."},
                {"level": 4, "description": "Player evaluates the equity-efficiency trade-off and proposes alternatives."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is loyal to the king but sees the policy backfiring.",
            "npc_dialogue_seed": "'The king's heart is in the right place. But the market is breaking.'",
            "resolution_path": (
                "If the player explains deadweight loss, the market master "
                "asks them to draft a letter proposing better policy."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 8-9",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C6.1 — Externalities
# ────────────────────────────────────────────────────────────────────────
def gen_C6_1(seq, tier):
    npc_cause = pick_npc(); npc_victim = pick_npc()
    while npc_victim == npc_cause:
        npc_victim = pick_npc()
    town = pick_town()
    polluter_profit = gold(40, 100)
    external_cost = gold(15, 40)
    social_profit = polluter_profit - external_cost

    scenarios = [
        ("tannery", "river pollution", "downstream village", "foul water"),
        ("smelter", "smoke and ash", "neighboring farms", "crop damage"),
        ("dye works", "colored runoff", "fishermen downstream", "dead fish"),
        ("sawmill", "noise and sawdust", "nearby homes", "health problems"),
        ("charcoal pit", "deforestation", "hunters and foragers", "lost game"),
        ("quarry", "dust clouds", "vineyard downwind", "ruined grapes"),
        ("pig farm", "runoff", "the well water", "illness"),
        ("forge", "soot and sparks", "thatch-roofed neighbors", "fire risk"),
    ]
    business, pollution, victim_desc, harm = pick(scenarios)

    if tier == "drill":
        context = (f"{npc_cause}'s {business} in {town} earns {polluter_profit} gold profit "
                   f"but causes {pollution} that costs {victim_desc} {external_cost} gold in {harm}.")
        text = (f"'{polluter_profit} gold profit. Good business,' says {npc_cause}. "
                f"But {npc_victim} from {victim_desc} says: 'We spend {external_cost} gold "
                f"on {harm}. {npc_cause} does not pay for that.'")
        speaker = f"{npc_cause}'s prices do not reflect the full social cost."
        ident = (f"What is the social cost of {npc_cause}'s production? "
                 f"Why does the market get the quantity wrong?")
        formal = (f"Private cost leads to {polluter_profit} profit. Social cost adds {external_cost}. "
                  f"Social profit = {social_profit}. Market overproduces because price < social cost.")
        fuw = f"Add {npc_cause}'s cost and {npc_victim}'s cost. That is the true social cost."
        fur = "What if a tax of {external_cost} gold is levied on the {business}? What happens to output and the externality?"
    elif tier == "what_if":
        # Positive externality
        benefit_activity = pick(["beekeeping", "maintaining flower gardens", "training guard dogs",
                                 "lighting street lanterns", "maintaining irrigation ditches"])
        external_benefit = gold(10, 30)
        private_cost = gold(20, 50)
        private_benefit = gold(15, private_cost - 3)
        context = (f"{npc_cause} in {town} considers {benefit_activity}. "
                   f"Private benefit: {private_benefit} gold. Private cost: {private_cost} gold. "
                   f"But it also creates {external_benefit} gold in benefits for neighbors.")
        text = (f"'It costs me {private_cost} but only earns me {private_benefit}. "
                f"Not worth it,' says {npc_cause}. Neighbors protest: 'But it helps all of us!'")
        speaker = "Positive externality: private cost exceeds private benefit, but social benefit exceeds social cost."
        social_benefit = private_benefit + external_benefit
        ident = (f"Should {npc_cause} do {benefit_activity}? "
                 f"From whose perspective?")
        formal = (f"Private: {private_benefit} < {private_cost}. Don't do it. "
                  f"Social: {social_benefit} > {private_cost}. Do it. "
                  f"Subsidy of {private_cost - private_benefit} would make it privately worthwhile.")
        fuw = f"From {npc_cause}'s view, it is a bad deal. But what if you add the neighbors' benefit?"
        fur = "How do subsidies for positive externalities compare to taxes for negative ones?"
    else:
        context = (f"The {business} is the largest employer in {town}. "
                   f"Taxing it would reduce pollution but might cause layoffs. "
                   f"The workers are also the ones breathing the dirty air. "
                   f"How do you weigh externality costs against employment?")
        text = (f"'Tax the {business} and half the town loses work. "
                f"Keep it open and they lose their health. "
                f"Who decides which loss matters more?'")
        speaker = "Externality policy has distributional consequences beyond efficiency."
        ident = "When the polluter is also the employer, how do you evaluate externality policy?"
        formal = ("Efficiency analysis: internalize the externality. "
                  "Distributional analysis: who bears the cost of the policy? "
                  "Transition costs, retraining, and compensation must be part of the design.")
        fuw = "Efficiency says tax the externality. But what happens to the workers? Is efficiency the only criterion?"
        fur = "How does this connect to the broader debate about growth versus environmental protection?"

    return {
        "id": f"C6.1-MF{seq:04d}",
        "taxonomy_code": "C6.1",
        "taxonomy_label": "Externalities",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Externalities",
            "pattern_description": (
                "An externality is a cost or benefit imposed on third parties not involved in the transaction. "
                "Negative externalities cause overproduction; positive externalities cause underproduction."
            ),
            "formal_form": formal,
            "why_wrong": (
                "Market prices send the wrong signal when externalities are present. "
                "The market 'works' only because it ignores third-party costs or benefits."
            ),
            "why_right": (
                "Identifying externalities is essential for understanding market failure. "
                "Solutions: Pigouvian taxes/subsidies, regulation, Coasean bargaining, liability rules."
            ),
            "related_patterns": ["C6.2", "C3.2", "C5.2"],
            "counterpoint": (
                "Not all externalities require intervention. Small externalities with high transaction costs "
                "may be tolerable. The Coase theorem suggests negotiation can resolve some."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player sees no connection between the business and the harm."},
                {"level": 1, "description": "Player recognizes harm but frames it as purely ethical."},
                {"level": 2, "description": "Player identifies the cost imposition but not the market failure."},
                {"level": 3, "description": "Player identifies the externality and explains over/under-production."},
                {"level": 4, "description": "Player identifies, quantifies, and proposes internalization mechanisms."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc_cause} is defensive; {npc_victim} is calm but firm.",
            "npc_dialogue_seed": f"'{npc_cause} is not breaking any law. But we are paying the price.'",
            "resolution_path": (
                "If the player identifies the externality and proposes a solution, "
                "the town council convenes to implement it."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 12",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C6.2 — Information asymmetry
# ────────────────────────────────────────────────────────────────────────
def gen_C6_2(seq, tier):
    npc = pick_npc(); town = pick_town()
    market_good = pick(["horses", "swords", "potions", "armor", "spell scrolls",
                        "gemstones", "breeding cattle", "enchanted rings",
                        "ships", "vineyard plots", "apprenticeship contracts"])

    if tier == "drill":
        context = (f"At the {market_good} market in {town}, sellers know the true quality "
                   f"but buyers cannot tell good from bad. {npc}, a buyer, notices quality declining.")
        text = (f"'{market_good[0].upper()}{market_good[1:]} used to be reliable here,' says {npc}. "
                f"'Now good sellers go elsewhere because buyers offer average-quality prices. "
                f"The market fills with junk, prices drop, more good sellers leave. "
                f"It is a death spiral.'")
        speaker = f"{npc} is describing the lemons problem."
        ident = (f"Why are good {market_good} leaving the market? "
                 f"What drives the quality spiral?")
        formal = ("Sellers know quality; buyers see only average. Buyers offer P = f(E[q]). "
                  "Sellers with q > P withdraw. Average quality falls. P falls. Repeat.")
        fuw = f"If you sell a good {market_good[:-1] if market_good.endswith('s') else market_good}, would you accept a price based on the average quality at this market?"
        fur = "What institution could restore buyer confidence? Certification? Warranties?"
    elif tier == "what_if":
        context = (f"A guild in {town} offers certification for {market_good} — "
                   f"a costly inspection that verifies quality. Only good sellers would pay for it. "
                   f"Is this enough to fix the lemons problem?")
        text = (f"'The certification costs 20 gold. Sellers of good {market_good} can recoup that "
                f"through higher prices. Sellers of bad ones cannot. So only good sellers certify.'")
        speaker = "Signaling: a costly action that only high-quality sellers find worthwhile."
        ident = "How does costly certification solve the lemons problem? What makes it a credible signal?"
        formal = ("Signaling equilibrium: cost of signal < benefit for high-quality seller, "
                  "> benefit for low-quality seller. Separating equilibrium: only good sellers signal.")
        fuw = "Why would a seller of bad goods NOT pay for certification?"
        fur = "What if the certification guild becomes corrupt? How do you certify the certifier?"
    else:
        context = (f"In {town}'s labor market, employers cannot observe worker ability before hiring. "
                   f"Workers can get expensive training as a signal. "
                   f"But the training itself may not increase productivity — "
                   f"it just sorts workers. Is this wasteful?")
        text = (f"'I spent two years in the academy. It did not teach me anything useful. "
                f"But now employers assume I am competent because I survived it. "
                f"The training's value is not what it teaches — it is what it proves.'")
        speaker = "Spence's signaling model: education as a costly signal of ability, not a source of it."
        ident = "If training does not increase productivity but sorts workers, is it socially wasteful?"
        formal = ("Signaling vs. human capital: if education only sorts, its social value is zero "
                  "even though its private value is positive. "
                  "Socially optimal: if direct ability testing were possible, signaling would be unnecessary.")
        fuw = "Distinguish two claims: 'Training makes me better' vs. 'Training shows I was already good.' Which is doing the work here?"
        fur = "Can you design a system that reveals ability without requiring costly signals?"

    return {
        "id": f"C6.2-MF{seq:04d}",
        "taxonomy_code": "C6.2",
        "taxonomy_label": "Information asymmetry",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Information asymmetry and adverse selection",
            "pattern_description": (
                "When one party knows more about quality than the other, "
                "the uninformed party offers average-quality prices, driving out high-quality goods."
            ),
            "formal_form": formal,
            "why_wrong": (
                "The market failure is caused by the information structure, not dishonesty. "
                "Even honest sellers cannot credibly communicate quality."
            ),
            "why_right": (
                "Recognizing information asymmetry opens the door to solutions: "
                "warranties, certification, reputation systems, regulation."
            ),
            "related_patterns": ["C4.2", "C6.3", "C6.1"],
            "counterpoint": (
                "Not all markets with asymmetric information collapse. "
                "Reputation, return policies, and branding mitigate the problem."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player blames dishonesty without seeing the information structure."},
                {"level": 1, "description": "Player recognizes buyers cannot tell quality but misses the spiral."},
                {"level": 2, "description": "Player identifies the information gap and seller withdrawal."},
                {"level": 3, "description": "Player describes the adverse selection spiral completely."},
                {"level": 4, "description": "Player identifies adverse selection and proposes institutional solutions."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is experienced and frustrated, watching the market deteriorate.",
            "npc_dialogue_seed": f"'Something poisoned this market, and it was not the {market_good} — it was the information.'",
            "resolution_path": (
                "If the player identifies the lemons problem, they help establish "
                "a certification system that restores market quality."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 Ch 12 + Akerlof (1970)",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C6.3 — Behavioral economics in markets
# ────────────────────────────────────────────────────────────────────────
def gen_C6_3(seq, tier):
    npc = pick_npc(); town = pick_town()
    business = pick(["tavern", "potion shop", "bakery", "weapon smith",
                     "general store", "inn", "market stall", "jeweler"])

    phenomena = [
        ("decoy effect", "adding an overpriced option nobody buys to make the target look reasonable",
         "Three ales: Small 3cp, Medium 5cp, Large 8cp. Add Barrel 15cp (never ordered). Large sales jump 50%."),
        ("anchoring", "the first number heard biases all subsequent judgments",
         "Merchant names a high starting price. Even after haggling, final price is higher than without the anchor."),
        ("default effect", "people stick with the preset option",
         "The inn's 'standard room' is pre-selected at 8 gold. Most guests pay 8 even though a 5-gold room exists."),
        ("loss aversion", "losses feel roughly twice as painful as equivalent gains feel good",
         "Merchant frames discount as 'avoid paying 5 gold extra' vs 'save 5 gold.' First framing is more effective."),
        ("endowment effect", "owning something makes you value it more",
         "Trader lets customer hold the item before deciding. Customers who hold it pay 30% more on average."),
        ("framing effect", "how a choice is presented changes the decision",
         "'This potion has 90% success rate' vs 'This potion fails 10% of the time.' Same potion, different reactions."),
        ("scarcity bias", "perceived scarcity increases perceived value",
         "'Only 3 left!' increases willingness to pay even when supply is artificially restricted."),
        ("social proof", "people follow what others do",
         "'Most popular item!' sign increases sales by 40%, regardless of whether it is actually most popular."),
    ]
    phenomenon, desc, example = pick(phenomena)

    if tier == "drill":
        context = (f"{npc} runs a {business} in {town} and has discovered that "
                   f"{desc}. They are testing it on customers.")
        text = (f"'{example}' {npc} grins. 'Nobody told me to study at the academy. "
                f"I just noticed what works. But is this just good business, or am I tricking people?'")
        speaker = f"{npc} has stumbled on {phenomenon} and is conflicted about the ethics."
        ident = f"What cognitive phenomenon is {npc} exploiting? Is it ethical?"
        formal = (f"Phenomenon: {phenomenon}. {desc}. "
                  f"People's choices are influenced by context and framing, "
                  f"not just by preferences and prices as rational-choice theory assumes.")
        fuw = f"The options did not change. Only the presentation changed. Why did behavior change?"
        fur = "Is there a neutral way to present choices? Or does every presentation nudge?"
    elif tier == "what_if":
        context = (f"The merchant guild in {town} is debating whether to ban {phenomenon}-based "
                   f"marketing. Some say it protects consumers. Others say it limits legitimate business.")
        text = (f"'If we ban {phenomenon} tricks, half the merchants lose their edge. "
                f"But consumers deserve honest presentation. Where is the line?'")
        speaker = "Regulatory debate about choice architecture."
        ident = f"Should the guild regulate {phenomenon}? What criteria distinguish ethical from exploitative nudges?"
        formal = ("Thaler & Sunstein's libertarian paternalism: nudge toward better outcomes "
                  "while preserving choice. Criterion: does the nudge serve the chooser's interests "
                  "or the designer's?")
        fuw = "Can you nudge without restricting options? Is that better than a ban?"
        fur = "Who decides what counts as 'better outcomes'? Is that itself a kind of paternalism?"
    else:
        context = (f"Two merchants in {town} use opposite nudges. One uses {phenomenon} to sell "
                   f"overpriced goods. The other uses it to help customers find genuinely good deals. "
                   f"Same technique, different intentions. Should the law treat them differently?")
        text = (f"'The technique is identical. Only the intent differs. "
                f"But law regulates actions, not intentions. How do we write rules "
                f"that catch the exploiter but not the helper?'")
        speaker = "The fundamental challenge of regulating behavioral techniques."
        ident = "Can you design regulation that distinguishes helpful from exploitative nudging?"
        formal = ("Intent-based regulation is unenforceable. "
                  "Outcome-based: measure consumer welfare. "
                  "Process-based: mandate transparency about choice architecture. "
                  "Each approach has blind spots.")
        fuw = "If you regulate the technique, you catch both users. If you regulate intent, how do you prove it?"
        fur = "Does this dilemma apply to other market interventions? Is advertising itself a nudge?"

    return {
        "id": f"C6.3-MF{seq:04d}",
        "taxonomy_code": "C6.3",
        "taxonomy_label": "Behavioral economics in markets",
        "track": "microeconomics",
        "pattern_type": "dual",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Behavioral economics: nudges and choice architecture",
            "pattern_description": (
                "People's choices are influenced by context, framing, and presentation, "
                "not just by rational preferences. Choice architecture is unavoidable."
            ),
            "formal_form": formal,
            "why_wrong": (
                "When used to exploit, nudges undermine autonomous decision-making. "
                "Customers believe they are choosing freely but are being steered."
            ),
            "why_right": (
                "When used ethically, nudges improve outcomes. "
                "Choice architecture is unavoidable — designing it thoughtfully is better than leaving it to chance."
            ),
            "related_patterns": ["E1.21", "E1.13", "C4.1"],
            "counterpoint": (
                "Critics argue any deliberate framing is manipulative. "
                "The ethical line depends on whether the nudge serves the chooser or the designer."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player sees nothing unusual — just good business."},
                {"level": 1, "description": "Player senses influence but cannot name the mechanism."},
                {"level": 2, "description": "Player identifies the phenomenon but does not address ethics."},
                {"level": 3, "description": "Player identifies the phenomenon and raises the ethical question."},
                {"level": 4, "description": "Player identifies the mechanism, articulates the ethical tension, and proposes criteria for distinguishing helpful from exploitative nudges."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is entrepreneurial, curious, and genuinely conflicted about ethics.",
            "npc_dialogue_seed": f"'It works because they do not notice. That is what bothers me.'",
            "resolution_path": (
                "If the player engages with the ethics, the merchant guild "
                "debates choice architecture rules, unlocking a policy quest."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 + Thaler & Sunstein, Nudge",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C7.1 — Broken window fallacy
# ────────────────────────────────────────────────────────────────────────
def gen_C7_1(seq, tier):
    npc = pick_npc(); town = pick_town()
    disaster = pick(["storm", "fire", "flood", "earthquake", "bandit raid",
                     "dragon attack", "siege", "plague aftermath", "avalanche", "tornado"])
    trades_benefiting = pick(["glaziers", "carpenters", "masons", "healers",
                              "blacksmiths", "roofers", "builders", "weavers"])
    repair_cost = gold(200, 1000)

    if tier == "drill":
        context = (f"A {disaster} devastated {town}. Alderman {npc} claims it will boost "
                   f"the economy because {trades_benefiting} will earn {repair_cost} gold in repairs.")
        text = (f"'{trades_benefiting.capitalize()} are going to earn a fortune! "
                f"The {disaster} is the best thing for business,' says {npc}. "
                f"'Every disaster is an opportunity.'")
        speaker = f"{npc} sees repair spending (the seen) but ignores what the money would have bought (the unseen)."
        ident = (f"{npc} says the {disaster} is good for the economy. "
                 f"What is wrong with this argument?")
        formal = (f"Seen: {repair_cost} gold in repair work. Unseen: {repair_cost} gold in "
                  f"investment, improvement, or consumption that would have occurred otherwise. "
                  f"Net effect = negative (value of destroyed assets lost).")
        fuw = f"The {trades_benefiting} get {repair_cost} gold. Where does that money come from? What would it have bought otherwise?"
        fur = f"After a real disaster, economic activity often rises. Does this mean the disaster helped?"
    elif tier == "what_if":
        context = (f"A councilor in {town} proposes demolishing old buildings to create repair jobs, "
                   f"explicitly applying the 'disaster is good for the economy' logic proactively.")
        text = (f"'If storms create jobs, why wait for storms? "
                f"Let us tear down the old market and rebuild it. Same jobs, same gold flowing.'")
        speaker = "Taking the broken window fallacy to its logical — and absurd — conclusion."
        ident = "If destruction creates prosperity, why not destroy on purpose? What does this reductio reveal?"
        formal = ("If the argument were sound, deliberate destruction would be optimal. "
                  "The absurdity of the conclusion reveals the flaw in the premise: "
                  "destruction redirects spending from productive to restorative use, creating no net gain.")
        fuw = "If deliberately breaking things created wealth, the richest towns would demolish constantly. Does that sound right?"
        fur = "When IS infrastructure spending genuinely productive? How do you distinguish repair from improvement?"
    else:
        context = (f"After the {disaster}, {town}'s economy does grow — but only because the "
                   f"kingdom sends aid gold that would not have come otherwise. "
                   f"Is this a genuine exception to the broken window fallacy?")
        text = (f"'We received {repair_cost} gold in royal aid. That money would NOT have come "
                f"to {town} without the {disaster}. So for us, the {disaster} really did "
                f"bring wealth. Right?'")
        speaker = "External aid changes the calculus — but not the principle."
        ident = "If disaster attracts external aid, is the disaster good for the affected town? For the kingdom?"
        formal = ("For the town: yes, net inflow of resources. "
                  "For the kingdom: no — the aid gold has an opportunity cost elsewhere. "
                  "The fallacy shifts from local to systemic level. "
                  "Bastiat's insight still applies, just at a different scope.")
        fuw = "The town gains. But where did the aid gold come from? What did it NOT fund in the kingdom?"
        fur = "This is the logic behind 'disaster GDP.' How does scope of analysis change the conclusion?"

    return {
        "id": f"C7.1-MF{seq:04d}",
        "taxonomy_code": "C7.1",
        "taxonomy_label": "Broken window fallacy",
        "track": "microeconomics",
        "pattern_type": "bad_thinking",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Broken window fallacy",
            "pattern_description": (
                "The fallacy counts visible repair spending as economic gain "
                "while ignoring the invisible alternative spending that the same money would have funded."
            ),
            "formal_form": formal,
            "why_wrong": (
                "Destruction redirects spending from productive to restorative use. "
                "The seen (repair jobs) masks the unseen (forgone investment or consumption)."
            ),
            "why_right": None,
            "related_patterns": ["C1.1", "C7.2", "C5.2"],
            "counterpoint": (
                "In a depressed economy with idle resources, stimulus spending — "
                "including repair — can mobilize slack. But this is the Keynesian qualification, "
                "not a validation of the fallacy."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player agrees destruction creates prosperity."},
                {"level": 1, "description": "Player senses something is wrong but cannot articulate it."},
                {"level": 2, "description": "Player recognizes repair costs come from somewhere but misses the full logic."},
                {"level": 3, "description": "Player identifies seen vs. unseen and the opportunity cost of repair spending."},
                {"level": 4, "description": "Player identifies the fallacy, connects to opportunity cost, and notes the Keynesian exception."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is well-meaning but economically naive.",
            "npc_dialogue_seed": f"'The {disaster} is the best thing that happened to the trades in years!'",
            "resolution_path": (
                f"If the player identifies the fallacy, {npc} admits they only saw one side of the ledger."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "Bastiat + PHIL 201 notes",
            "original_id": None,
        },
    }


# ────────────────────────────────────────────────────────────────────────
# C7.2 — Zero-sum thinking
# ────────────────────────────────────────────────────────────────────────
def gen_C7_2(seq, tier):
    npc = pick_npc(); town = pick_town()
    kingdom_a = pick(["Ardenvale", "Thornmark", "Highcrest", "Ironlands",
                      "Stormreach", "Goldshore", "Frostholm", "Silverwood"])
    kingdom_b = pick(["Brassholm", "Meadowvale", "Deepwater", "Ember Ridge",
                      "Greenvale", "Stonekeep", "Windmarch", "Oakdale"])
    while kingdom_b == kingdom_a:
        kingdom_b = pick(["Brassholm", "Meadowvale", "Deepwater", "Ember Ridge"])
    good_a = pick(["grain", "wool", "timber", "salt", "fish", "hops", "leather"])
    good_b = pick(["iron", "spices", "cloth", "wine", "tools", "glass", "pottery"])

    if tier == "drill":
        context = (f"Councilor {npc} in {town} opposes a trade agreement between "
                   f"{kingdom_a} and {kingdom_b}. {kingdom_a} has surplus {good_a}; "
                   f"{kingdom_b} has surplus {good_b}.")
        text = (f"'Every gold {kingdom_b} earns from this deal is a gold taken from us,' "
                f"says {npc}. 'Trade is a game with a winner and a loser. "
                f"I will not let {kingdom_b}'s merchants fleece our people.'")
        speaker = f"{npc} assumes trade is zero-sum."
        ident = f"Is {npc} right that trade must have a loser? What is the actual structure of voluntary trade?"
        formal = ("Zero-sum: gain(A) = -gain(B). Reality: both trade away lower-valued goods "
                  "for higher-valued ones. gain(A) > 0 AND gain(B) > 0. Pie grows.")
        fuw = f"Before trade, {kingdom_a} has {good_a} it cannot use. After trade, it has {good_b} it needs. Did it lose?"
        fur = "Can you name a genuinely zero-sum interaction? What distinguishes it from trade?"
    elif tier == "what_if":
        context = (f"The trade agreement is signed, and both kingdoms are richer. "
                   f"But within {kingdom_a}, the {good_b} producers (who now compete with imports) "
                   f"are worse off. Is {npc} partly right?")
        text = (f"'Sure, the kingdom gains overall. But my {good_b} workshop is closing because "
                f"{kingdom_b}'s {good_b} is cheaper. Trade is not zero-sum for the kingdom, "
                f"but it is zero-sum for me.'")
        speaker = "Trade creates winners and losers within each side, even if total surplus grows."
        ident = "If trade benefits both kingdoms overall, but some producers lose, is it positive-sum or not?"
        formal = ("Total surplus positive. Distribution: exporters gain, import-competing producers lose. "
                  "Kaldor-Hicks: winners could compensate losers and still gain. "
                  "But compensation does not happen automatically.")
        fuw = "Separate two questions: Is the pie bigger? Is the pie fairly divided?"
        fur = "Should trade agreements include compensation for displaced workers? Who should pay?"
    else:
        context = (f"A philosopher in {town} challenges the player: "
                   f"'Some interactions ARE zero-sum: theft, rent-seeking, certain financial bets. "
                   f"Zero-sum thinking is wrong when applied to trade, but it is right for other contexts. "
                   f"How do you tell the difference?'")
        text = (f"'Your mistake is not zero-sum thinking per se. "
                f"It is applying zero-sum thinking everywhere. "
                f"The real skill is knowing when value is being created versus merely transferred.'")
        speaker = "The meta-question: when is zero-sum thinking a fallacy and when is it correct?"
        ident = "Articulate the criterion for distinguishing zero-sum from positive-sum interactions."
        formal = ("Zero-sum: no new value created, only transferred (gambling, theft, rent-seeking). "
                  "Positive-sum: both parties gain because they value goods differently (trade, cooperation). "
                  "Criterion: does the interaction create new utility or merely redistribute it?")
        fuw = "In trade, both sides get something they value more. In theft, one side gets and the other loses. What is the structural difference?"
        fur = "Is employment zero-sum or positive-sum? What about rent? What about intellectual property?"

    return {
        "id": f"C7.2-MF{seq:04d}",
        "taxonomy_code": "C7.2",
        "taxonomy_label": "Zero-sum thinking",
        "track": "microeconomics",
        "pattern_type": "bad_thinking",
        "difficulty_tier": tier,
        "scenario": {"context": context, "text": text, "speaker_context": speaker},
        "structure": {
            "pattern_name": "Zero-sum thinking",
            "pattern_description": (
                "The error of assuming all interactions are zero-sum — that one party's gain "
                "must be another's loss — when voluntary trade creates new value for both parties."
            ),
            "formal_form": formal,
            "why_wrong": (
                "If trade were zero-sum, no one would voluntarily agree to it. "
                "The fact that both parties choose to trade is evidence that both expect to benefit."
            ),
            "why_right": None,
            "related_patterns": ["C1.2", "C4.1", "C7.1"],
            "counterpoint": (
                "Some interactions are genuinely zero-sum: theft, certain financial bets, rent-seeking. "
                "The error is universal application, not the concept itself."
            ),
        },
        "assessment": {
            "identification_prompt": ident,
            "rubric": [
                {"level": 0, "description": "Player agrees trade must have a loser."},
                {"level": 1, "description": "Player intuits both could gain but cannot explain how."},
                {"level": 2, "description": "Player identifies value exchange but does not generalize."},
                {"level": 3, "description": "Player explains trade creates value because each side values goods differently."},
                {"level": 4, "description": "Player explains value creation, distinguishes zero-sum from positive-sum contexts, and connects to comparative advantage."},
            ],
            "follow_up_if_wrong": fuw,
            "follow_up_if_right": fur,
        },
        "game_hooks": {
            "npc_personality": f"{npc} is patriotic and protective, not malicious.",
            "npc_dialogue_seed": f"'In every deal, someone comes out ahead and someone gets cheated.'",
            "resolution_path": (
                "If the player explains positive-sum trade, they arrange a demonstration trade. "
                f"{npc} grudgingly concedes when both sides gain visibly."
            ),
        },
        "source": {
            "type": "synthetic_verified",
            "source_material": "CORE Economy 2.0 + Bastiat",
            "original_id": None,
        },
    }


# ── Generator dispatch ─────────────────────────────────────────────────
GENERATORS = {
    "C1.1": gen_C1_1, "C1.2": gen_C1_2,
    "C2.1": gen_C2_1, "C2.2": gen_C2_2,
    "C3.1": gen_C3_1, "C3.2": gen_C3_2,
    "C4.1": gen_C4_1, "C4.2": gen_C4_2,
    "C5.1": gen_C5_1, "C5.2": gen_C5_2,
    "C6.1": gen_C6_1, "C6.2": gen_C6_2, "C6.3": gen_C6_3,
    "C7.1": gen_C7_1, "C7.2": gen_C7_2,
}


def main():
    random.seed(42)
    records = []
    for code, label, ptype in CODES:
        gen_fn = GENERATORS[code]
        seq = 1
        for tier_name, count in TIER_DIST:
            for _ in range(count):
                rec = gen_fn(seq, tier_name)
                records.append(rec)
                seq += 1

    with open(OUTPUT, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Wrote {len(records)} records to {OUTPUT}")


if __name__ == "__main__":
    main()
