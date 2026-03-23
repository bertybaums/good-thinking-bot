# QC2: Mechanical Verification Report

**Date:** 2026-03-23
**Scope:** All decision theory and game theory records (taxonomy codes B1--B10)
**Method:** Automated numerical verification using numpy

## Summary

| Metric | Count |
|--------|-------|
| Total DT/GT records (B1--B10) | 6424 |
| Records with `formal_form` field | 5657 |
| Successfully parsed | 2044 |
| Mechanically verifiable | 1633 |
| **Passed** | **1577** |
| **Failed** | **56** |
| No `formal_form` | 767 |
| Unparseable (has `formal_form`) | 3888 |
| **Pass rate** | **96.6%** |

## Breakdown by Taxonomy Prefix

| Prefix | Total | Parsed | Verified | Pass | Fail | Rate |
|--------|-------|--------|----------|------|------|------|
| B1 | 620 | 439 | 390 | 372 | 18 | 95.4% |
| B2 | 560 | 75 | 0 | 0 | 0 | N/A |
| B3 | 806 | 181 | 74 | 67 | 7 | 90.5% |
| B4 | 647 | 184 | 157 | 157 | 0 | 100.0% |
| B5 | 916 | 108 | 43 | 43 | 0 | 100.0% |
| B6 | 483 | 240 | 231 | 211 | 20 | 91.3% |
| B7 | 631 | 240 | 229 | 225 | 4 | 98.3% |
| B8 | 642 | 496 | 476 | 469 | 7 | 98.5% |
| B9 | 477 | 35 | 0 | 0 | 0 | N/A |
| B10 | 642 | 46 | 33 | 33 | 0 | 100.0% |

## Checks Performed

| Check | Records Tested | Description |
|-------|----------------|-------------|
| `backward_induction_structure` | 224 | Game tree / backward induction structural check |
| `discount_factor` | 33 | Folk Theorem discount factor computation |
| `dominance` | 22 | Strict dominance across all act pairs |
| `matrix_structure` | 118 | Decision matrix acts/states/payoffs structural validity |
| `maximax` | 72 | Row maxima, argmax of maxima, recommendation |
| `maximin` | 76 | Row minima, argmax of minima, recommendation |
| `meu` | 74 | EU = sum(P * U), probability sums, claimed EU values vs computed |
| `minimax_regret` | 102 | Regret matrix, column maxima, max regret per act, recommendation |
| `nash_equilibria` | 712 | Pure-strategy Nash equilibria identification |
| `payoff_structure` | 200 | Paradox payoff structure validity |
| `prob_sum` | 73 | Probabilities sum to 1.0 (tolerance 0.01) |

### Verification Details

- **Maximin/maximax/minimax regret:** Parsed the payoff matrix from `formal_form`, independently computed the decision rule result, and cross-checked against the claimed recommendation in `why_right` and `pattern_description`.
- **MEU calculations:** Verified EU(Act) = sum of P(State) * U(Act|State), compared claimed EU values against computed values (tolerance: 0.5), verified probability sums.
- **Probabilities:** Checked that stated probabilities sum to 1.0 (tolerance: 0.01). Dutch Book examples deliberately violating this were excluded.
- **Nash equilibria:** Parsed game payoff matrices, independently found all pure-strategy Nash equilibria, cross-checked against claimed equilibria.
- **Discount factor:** Verified Folk Theorem threshold computations (delta > (T-R)/(T-P)).
- **Act-dependent probabilities:** Handled MEU problems where each act has different state probabilities.

## Failures (56)

### `B3.2-ON0070` (B3.2)

- **Source file:** `overnight_thin_DT.jsonl`
- **Checks run:** meu, prob_sum
- **Error:** EU(Courtyard): computed 4.80, claimed 5.40

### `B3.2-ON0000` (B3.2)

- **Source file:** `overnight_thin_DT.jsonl`
- **Checks run:** meu, prob_sum
- **Error:** EU(Comedy): computed 9.60, claimed 10.80

### `B3.2-ON0005` (B3.2)

- **Source file:** `overnight_thin_DT.jsonl`
- **Checks run:** meu, prob_sum
- **Error:** EU(Hilltop): computed 14.00, claimed 9.50
- **Error:** EU(Bridge): computed 9.50, claimed 3.00

### `B6.2-TU0059` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Low Heat', 'Low Heat')], computed [('High Heat', 'High Heat')]

### `B6.2-XYZ123` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Guard', 'Negotiate'), ('Negotiate', 'Guard'), ('Negotiate', 'Negotiate'), ('Guard', 'Guard')], computed [('Negotiate', 'Negotiate')]

### `B8.1-TU0071` (B8.1)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('H', 'L'), ('L', 'H'), ('L', 'L'), ('H', 'H')], computed [('L', 'L')]

### `B7.1-CASTLE-004` (B7.1)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Raid', 'Raid')], computed [('Raid', 'Raid'), ('Full‑Breach', 'Full‑Breach')]

### `B6.2-TU0087` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Comedy', 'Drama')], computed [('Comedy', 'Comedy')]

### `B6.1-TU0085` (B6.1)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('C (Rehearse together)', 'D (Rehearse alone)'), ('D (Rehearse alone)', 'C (Rehearse together)'), ('D (Rehearse alone)', 'D (Rehearse alone)'), ('C (Rehearse together)', 'C (Rehearse together)')], computed [('D (Rehearse alone)', 'D (Rehearse alone)')]

### `B8.3-TU0096` (B8.3)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Enter', 'Negotiate'), ('Stay Out', 'Execute'), ('Stay Out', 'Negotiate'), ('Enter', 'Execute')], computed [('Enter', 'Negotiate'), ('Stay Out', 'Execute')]

### `B6.2-TU0073` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Attack', 'Negotiate'), ('Negotiate', 'Attack'), ('Negotiate', 'Negotiate'), ('Attack', 'Attack')], computed [('Attack', 'Negotiate'), ('Negotiate', 'Attack')]

### `B6.2-TU0044` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('L', 'L')], computed [('H', 'H')]

### `B6.2-AP001` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Reserve', 'Reserve')], computed [('Earn', 'Earn')]

### `B6.2-TU0095` (B6.2)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Mine', 'Warehouse'), ('Warehouse', 'Mine'), ('Warehouse', 'Warehouse'), ('Mine', 'Mine')], computed [('Warehouse', 'Warehouse')]

### `B6.1-TU0088` (B6.1)

- **Source file:** `overnight_topup_GT.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('C (rehearse together)', 'C (rehearse together)')], computed [('D (rehearse alone)', 'D (rehearse alone)')]

### `B1.5-S30062` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Netting' but computed 'Canning'
- **Error:** Minimax regret: claimed 'Boat Repair' but computed 'Canning'

### `B1.5-S30074` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Treat Wounds' but computed 'Allocate Supplies'
- **Error:** Minimax regret: claimed 'Evacuate Patients' but computed 'Allocate Supplies'

### `B3.1-PIR001` (B3.1)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** meu, prob_sum
- **Error:** EU(Repair Sail): computed -18.00, claimed 6.00
- **Error:** EU(Spare Rum): computed -17.00, claimed -21.00

### `B1.5-S30072` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Corn' but computed 'Wheat'
- **Error:** Minimax regret: claimed 'Livestock' but computed 'Wheat'

### `B3.1-M3001` (B3.1)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** meu
- **Error:** Act 'B (50/50)': probabilities sum to 0.9000
- **Error:** EU(B (50/50)): computed 39.00, claimed 38.00

### `B1.5-S30087` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Wheat' but computed 'Grapes'
- **Error:** Minimax regret: claimed 'Apples' but computed 'Grapes'

### `B1.5-S30001` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Silks' but computed 'Spices'
- **Error:** Minimax regret: claimed 'Precious Metals' but computed 'Spices'

### `B1.5-S30103` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Archers on Walls' but computed 'Boiling Oil'
- **Error:** Minimax regret: claimed 'Reinforce Gate' but computed 'Boiling Oil'

### `B1.5-S30045` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Tax Relief' but computed 'Grand Feast'
- **Error:** Minimax regret: claimed 'Military Funding' but computed 'Grand Feast'

### `B1.5-S30100` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Mountain Pass' but computed 'Coastal Route'
- **Error:** Minimax regret: claimed 'Open Sea' but computed 'Coastal Route'

### `B3.1-S30015` (B3.1)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** meu, prob_sum
- **Error:** EU(Load Spices): computed 15.00, claimed 25.00
- **Error:** EU(Load Silk): computed 35.00, claimed 40.00
- **Error:** EU(Load Mixed): computed 25.00, claimed 45.00

### `B1.5-S30079` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Furs' but computed 'Iron Tools'
- **Error:** Minimax regret: claimed 'Salted Fish' but computed 'Iron Tools'

### `B1.5-S30013` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Tubers' but computed 'Grain'
- **Error:** Minimax regret: claimed 'Fruit' but computed 'Grain'

### `B1.5-S30098` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Barley' but computed 'Wheat'
- **Error:** Minimax regret: claimed 'Beans' but computed 'Wheat'

### `B1.5-S30016` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Wheat' but computed 'Barley'
- **Error:** Minimax regret: claimed 'Corn' but computed 'Barley'

### `B1.5-S30066` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Gold Coins' but computed 'Rare Gems'
- **Error:** Minimax regret: claimed 'Secret Maps' but computed 'Rare Gems'

### `B1.5-WS30042` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Bronze Sword' but computed 'Silk Cloak'
- **Error:** Minimax regret: claimed 'Wooden Shield' but computed 'Silk Cloak'

### `B1.5-S30113` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Deploy Archers' but computed 'Reinforce Walls'
- **Error:** Minimax regret: claimed 'Launch Counterattack' but computed 'Reinforce Walls'

### `B3.1-S30087` (B3.1)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** meu, prob_sum
- **Error:** EU(Discount): computed 46.00, claimed 60.00
- **Error:** EU(No Discount): computed 80.00, claimed 45.00

### `B1.5-S30089` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Furs' but computed 'Spices'
- **Error:** Minimax regret: claimed 'Iron Ingots' but computed 'Spices'

### `B1.4-S30098` (B1.4)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** maximin
- **Error:** Maximin: claimed 'Reserve Water' but computed 'Irrigate Wheat'

### `B1.5-S30123` (B1.5)

- **Source file:** `synthetic_DT_sprint3.jsonl`
- **Checks run:** minimax_regret
- **Error:** Minimax regret: claimed 'Silk' but computed 'Gems'
- **Error:** Minimax regret: claimed 'Spices' but computed 'Gems'

### `B8.3-S50043` (B8.3)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('R', 'F'), ('P', 'A')], computed [('R', 'F')]

### `B6.2-TRN-202603` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Raid', 'Negotiate'), ('Negotiate', 'Raid'), ('Negotiate', 'Negotiate'), ('Raid', 'Raid')], computed [('Negotiate', 'Negotiate')]

### `B8.3-S50024` (B8.3)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Attack', 'Surrender'), ('Negotiate', 'Fight'), ('Negotiate', 'Surrender'), ('Attack', 'Fight')], computed [('Attack', 'Surrender'), ('Negotiate', 'Fight')]

### `B6.2-MC001` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Meditate', 'Meditate'), ('Gather Herbs', 'Gather Herbs')], computed [('Gather Herbs', 'Gather Herbs')]

### `B7.2-FV001` (B7.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Sea Song', 'Great Net'), ('Great Net', 'Sea Song'), ('Great Net', 'Great Net'), ('Sea Song', 'Sea Song')], computed [('Great Net', 'Great Net'), ('Sea Song', 'Sea Song')]

### `B6.2-XYZ123` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Skirmish', 'Negotiate'), ('Negotiate', 'Skirmish'), ('Negotiate', 'Negotiate'), ('Skirmish', 'Skirmish')], computed [('Negotiate', 'Negotiate')]

### `B8.3-S50025` (B8.3)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('H', 'P'), ('L', 'C')], computed [('H', 'C')]

### `B6.2-HC001` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Overharvest', 'Conserve')], computed [('Overharvest', 'Overharvest')]

### `B6.2-FV001` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Lagoon', 'Open Sea')], computed [('Lagoon', 'Lagoon')]

### `B6.2-TS001` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Cooperate', 'Defect'), ('Defect', 'Negotiate'), ('Negotiate', 'Defect'), ('Cooperate', 'Cooperate'), ('Defect', 'Defect'), ('Negotiate', 'Cooperate'), ('Cooperate', 'Negotiate'), ('Negotiate', 'Negotiate'), ('Defect', 'Cooperate')], computed [('Defect', 'Negotiate'), ('Negotiate', 'Defect')]

### `B8.3-S50019` (B8.3)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Enter', 'Share')], computed [('Stay Out', 'Over‑mine'), ('Enter', 'Share')]

### `B6.1-S50036` (B6.1)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('D', 'D'), ('C', 'C')], computed [('D', 'D')]

### `B6.2-S50019` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Attack', 'Negotiate'), ('Negotiate', 'Retreat'), ('Retreat', 'Negotiate'), ('Attack', 'Attack'), ('Negotiate', 'Negotiate'), ('Retreat', 'Attack'), ('Attack', 'Retreat'), ('Retreat', 'Retreat'), ('Negotiate', 'Attack')], computed []

### `B6.2-TRX904` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Hold Ground', 'Ambush')], computed [('Hold Ground', 'Hold Ground')]

### `B8.3-S50037` (B8.3)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Turn Back', 'Block'), ('Enter', 'Share')], computed [('Turn Back', 'Block'), ('Turn Back', 'Share')]

### `B6.2-ROYAL-001` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Mobilize Troops', 'Mobilize Troops'), ('Send Envoy', 'Send Envoy')], computed [('Mobilize Troops', 'Mobilize Troops')]

### `B7.2-S50049` (B7.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Market', 'Mine'), ('Mine', 'Market'), ('Mine', 'Mine'), ('Market', 'Market')], computed [('Mine', 'Mine'), ('Market', 'Market')]

### `B6.2-PIR001` (B6.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Share Loot', 'Keep Loot')], computed [('Share Loot', 'Share Loot')]

### `B7.2-S50017` (B7.2)

- **Source file:** `synthetic_GT_integrated_sprint5.jsonl`
- **Checks run:** nash_equilibria
- **Error:** Nash equilibria: claimed [('Sunken Vault', 'Ember Mine'), ('Ember Mine', 'Sunken Vault'), ('Ember Mine', 'Ember Mine'), ('Sunken Vault', 'Sunken Vault')], computed [('Ember Mine', 'Ember Mine'), ('Sunken Vault', 'Sunken Vault')]

## Unparseable Records for Manual Review (3613)

These records have a `formal_form` field but the parser could not extract a numerical matrix.

### Could not parse decision matrix (2006 records)

- `B1.1`: `B1.1-S30028`, `B1.1-00245`, `B1.1-S30084`, `B1.1-S30009`, `B1.1-S30053`
- `B1.2`: 101 records
- `B1.3`: 30 records
- `B1.4`: 41 records
- `B1.5`: `B1.5-S30054`, `B1.5-S30024`, `B1.5-S30071`, `B1.5-S30007`
- `B2.1`: 52 records
- `B2.2`: 127 records
- `B2.3`: 42 records
- `B2.4`: 40 records
- `B2.5`: 37 records
- `B3.1`: 94 records
- `B3.2`: 68 records
- `B3.3`: 89 records
- `B3.4`: 127 records
- `B3.5`: 43 records
- `B3.6`: 99 records
- `B3.7`: 67 records
- `B4.1`: 127 records
- `B4.2`: 29 records
- `B4.3`: 43 records
- `B4.4`: 48 records
- `B4.5`: 67 records
- `B4.6`: 44 records
- `B5.1`: 127 records
- `B5.2`: 68 records
- `B5.3`: 48 records
- `B5.4`: 48 records
- `B5.5`: 127 records
- `B5.6`: `B5.6-ON0088`, `B5.6-ON0056`, `B5.6-ON0096`, `B5.6-ON0062`, `B5.6-ON0064`
- `B5.7`: 53 records
- `B5.8`: 106 records

### Game payoffs present but parser could not match strategies (1026 records)

- `B10.2`: `B10.2-S50048`, `B10.2-S50006`, `B10.2-S50015`, `B10.2-001`, `B10.2-S50001`
- `B10.3`: 38 records
- `B10.4`: 148 records
- `B6.1`: 17 records
- `B6.2`: 38 records
- `B6.3`: 148 records
- `B7.1`: 32 records
- `B7.2`: 39 records
- `B7.3`: 137 records
- `B7.4`: 124 records
- `B8.2`: `B8.2-TU0083`, `B8.2-TP001`, `B8.2-TU0081`, `B8.2-TU0049`
- `B8.3`: 27 records
- `B9.1`: 149 records
- `B9.3`: 120 records

### No parseable game matrix or tree (581 records)

- `B10.1`: 145 records
- `B10.2`: 147 records
- `B10.3`: 59 records
- `B10.4`: `B10.4-MC001`
- `B6.1`: 18 records
- `B6.1+B5.2`: `INT-S50103`
- `B6.2`: `B6.2-002`, `B6.2-CASTLE-001`, `B6.2-002`, `B6.2-002`
- `B6.3`: 7 records
- `B7.1`: `INT-B7.1E1.12-001`, `INT-B7.1E1.12-001`, `INT-001`, `INT-S50504`, `INT-S50503`
- `B7.3`: `B7.3-PIR001`, `B7.3-S50046`
- `B7.4`: 10 records
- `B8.1`: `B8.1-FV001`, `B8.1-AP001`
- `B8.3`: 18 records
- `B8.4`: `B8.4-TU0095`
- `B9.1`: `B9.1-TU0079`, `INT-S51804`
- `B9.1+C3.1`: `INT-S51800`
- `B9.2`: 157 records
- `B9.3`: `B9.3-MON001`

## Records Without `formal_form` (767)

These records have null or empty `formal_form` and cannot be mechanically verified.

- `B10.1`: 13 records
- `B10.2`: 16 records
- `B10.3`: 21 records
- `B10.4`: `B10.4-AP001`, `B10.4-TU0026`, `B10.4-TU0009`
- `B2.3`: 60 records
- `B2.4`: 62 records
- `B2.5`: 65 records
- `B3.6`: `B3.6-ON0086`, `B3.6-ON0072`, `B3.6-ON0090`
- `B3.7`: 35 records
- `B4.1`: 10 records
- `B4.2`: `B4.2-ON0040`, `B4.2-ON0055`
- `B4.3`: 59 records
- `B4.4`: 7 records
- `B4.5`: 16 records
- `B4.6`: 11 records
- `B5.3`: 54 records
- `B5.4`: 54 records
- `B5.6`: 68 records
- `B5.7`: 49 records
- `B5.8`: `B5.8-S30013`
- `B6.1`: `B6.1-TU0074`, `INT-S50104`, `INT-S50101`
- `B6.2`: `B6.2-TU0050`, `B6.2-HB007`, `B6.2-TU0006`, `B6.2-TU0029`
- `B6.3`: `B6.3-TU0016`, `B6.3-TU0078`, `B6.3-TU0042`
- `B7.1`: 8 records
- `B7.2`: 6 records
- `B7.3`: 19 records
- `B7.4`: 9 records
- `B8.1`: `B8.1-MN001`, `B8.1-LA045`, `B8.1-MON001`, `B8.1-TU0005`
- `B8.2`: 28 records
- `B8.3`: 14 records
- `B8.4`: 48 records
- `B9.1`: 10 records
- `B9.1+C3.1`: `INT-S51801`
- `B9.2`: `B9.2-TU0080`

## Notes

1. **Known parser limitation (abbreviated act names):** The existing `05_mechanical_verify.py` had a known issue with abbreviated act names (e.g., `River` instead of `River Panning`). This verification handles multi-word act/state names by trying both exact matches and first-word abbreviations.
2. **Act-dependent probabilities:** Some MEU problems (e.g., B3.1-001, the healer's rash treatment) have different probabilities per act. These were detected and verified separately from standard uniform-probability MEU.
3. **Dutch Book records:** B2.2 and B2.3 records that deliberately show probabilities summing to >1.0 were excluded from probability-sum failure counts.
4. **Game tree records:** Records with sequential/extensive-form games (B8.3, B8.4) were checked for structural presence of backward induction claims but full tree traversal verification was not performed due to format variability.
5. **Unparseable records:** Many B5 (behavioral DT), B9 (evolutionary GT), and B10 (repeated games) records use specialized formats (replicator dynamics equations, prospect theory value functions, discount factor formulas) that do not follow the standard Acts/States/Payoffs template. These are flagged for manual review rather than false-failed.
