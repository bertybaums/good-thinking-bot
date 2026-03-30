# QC7: Expert Review Report

**Date:** 2026-03-29
**Scope:** 4728 records reviewed
**Reviewer:** Nemotron-3-Super-120b

## Overall Scores

| Dimension | Mean |
|-----------|------|
| Taxonomy Accuracy | 4.99 / 5 |
| Scenario Quality | 4.40 / 5 |
| Structure Accuracy | 4.82 / 5 |
| Assessment Quality | 4.02 / 5 |
| Game Integration | 4.55 / 5 |

| Verdict | Count | Rate |
|---------|-------|------|
| Pass | 4377 | 92.6% |
| Marginal | 347 | 7.3% |
| Fail | 4 | 0.1% |

## Scores by Track

| Track | Tax | Scen | Struct | Assess | Game | n |
|-------|-----|------|--------|--------|------|---|
| cognitive_biases | 5.0 | 4.4 | 4.9 | 3.9 | 4.8 | 233 |
| decision_theory | 5.0 | 4.3 | 4.6 | 3.9 | 4.6 | 302 |
| dennett_tools | 5.0 | 4.8 | 4.9 | 4.5 | 4.9 | 635 |
| game_theory | 5.0 | 4.4 | 4.7 | 3.9 | 4.5 | 2082 |
| logic_critical_thinking | 5.0 | 4.5 | 4.9 | 4.2 | 4.7 | 660 |
| microeconomics | 5.0 | 4.1 | 5.0 | 3.9 | 4.1 | 816 |

## Scores by Source Type

| Source | Tax | Scen | Struct | Assess | Game | n |
|--------|-----|------|--------|--------|------|---|
| existing_dataset | 4.9 | 4.2 | 4.6 | 4.1 | 4.4 | 235 |
| hand_crafted | 5.0 | 4.7 | 4.9 | 4.5 | 4.8 | 66 |
| synthetic_verified | 5.0 | 4.4 | 4.8 | 4.0 | 4.6 | 4427 |

## Failed Records (4)

- **C1.3-P4040W10-1c** (C1.3: Pareto efficiency): The scenario is a symmetric 3x3 game with payoffs resembling rock-paper-scissors, which has no pure strategy Nash equilibria and is not primarily about Pareto efficiency; the taxonomy label 'C1.3: Pareto efficiency' is mismatched as the core concept tested is Nash equilibrium and strategic dominance, not Pareto optimality.; The pattern description incorrectly frames the problem as testing Pareto efficiency when the hint and structure focus on best-response and Nash equilibrium; Pareto efficiency is not meaningfully engaged in the analysis of this game.
- **B6.4-P4040W11-5** (B6.4: Zero-sum games and minimax theorem): The scenario describes a nearly zero-sum game with relationship value (R) and damage (D), but the taxonomy claims it illustrates pure zero-sum games and the minimax theorem. The payoffs are not zero-sum (e.g., (-50+R, 50+R) sums to 2R, not zero), violating the core definition. The pattern description incorrectly states it is a zero-sum game where 'one player's gain is the other's loss,' which is false here. The formal form repeats the same non-zero-sum matrix. The assessment prompt asks what concept is being tested, but since the scenario misapplies the taxonomy, it cannot validly test minimax in zero-sum games. NPC framing is adequate but undermined by conceptual errors.; The 'why_right' and 'why_wrong' fields are incomplete: 'why_wrong' says 'N/A' and 'why_right' is vague and does not explain why a correct answer demonstrates understanding.
- **B7.5-PF0057** (B7.5: Hawk-Dove game): The mixed-strategy equilibrium calculation incorrectly states p(Hawk) = V/C = 8/6 ≈ 1.33 and then rounds to 1, which is invalid (probability cannot exceed 1). The correct mixed strategy is p(Hawk) = V/C only if V < C; here V=8, C=6, so V>C, meaning Hawk is actually the dominant strategy — contradicting the earlier claim of no dominant strategy. This is a critical error.; The scenario text is cut off: 'What should you c' is incomplete, suggesting a formatting or copy-paste error.
- **B7.5-DRL001** (B7.5: Hawk-Dove game): The scenario text is cut off mid-sentence: 'the attacker captur' — this reduces clarity and professionalism.; The assessment prompt asks to list Nash equilibria but does not require justification or reasoning about why they are equilibria, limiting depth of understanding probed.

## Marginal Records (347)

- **C1.3-P4040W10-1a** (C1.3): low on assessment_quality
- **C1.3-P4040W12-2** (C1.3): low on structure_accuracy, assessment_quality, game_integration
- **D1.4-001** (D1.4): low on 
- **C3.1-001** (C3.1): low on 
- **C1.3-PF0027** (C1.3): low on structure_accuracy
- **C1.3-H001** (C1.3): low on structure_accuracy
- **D2.4-QF0023** (D2.4): low on 
- **INT-S50407** (D2.1): low on 
- **INT-S50404** (D2.1): low on 
- **INT-S50400** (D2.1): low on 
- **C2.1-MF0033** (C2.1): low on 
- **C2.1-MF0034** (C2.1): low on 
- **C2.1-MF0037** (C2.1): low on 
- **C2.1-MF0038** (C2.1): low on 
- **C2.1-MF0040** (C2.1): low on 
- **C2.1-MF0043** (C2.1): low on 
- **C4.1-MF0019** (C4.1): low on 
- **C5.1-MF0015** (C5.1): low on 
- **B6.1-P4040W9-1** (B6.1): low on 
- **B6.4-P4040W9-2** (B6.4): low on taxonomy_accuracy, structure_accuracy, assessment_quality
- **B7.2-P4040W10-5** (B7.2): low on 
- **B7.4-P4040W10-6a** (B7.4): low on assessment_quality
- **B7.4-P4040W10-6e** (B7.4): low on scenario_quality
- **B6.2-P4040W11-4** (B6.2): low on structure_accuracy, assessment_quality
- **B8.6-P4040W12-1** (B8.6): low on taxonomy_accuracy, structure_accuracy, assessment_quality
- **B6.1-P4040W14-2b** (B6.1): low on assessment_quality
- **B6.1-P4040W14-2c** (B6.1): low on scenario_quality
- **B10.5-P4040W14-2d** (B10.5): low on structure_accuracy
- **B15.1-P4040W15-1** (B15.1): low on 
- **B6.5-001** (B6.5): low on 
