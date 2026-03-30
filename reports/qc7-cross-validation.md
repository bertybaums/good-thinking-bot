# QC7: Cross-Validation Report

**Date:** 2026-03-29
**Scope:** 27270 training corpus records
**Classifier:** Nemotron-3-Super-120b (via MindRouter)
**Method:** Blind classification — taxonomy code stripped, scenario + analysis presented, model selects code from track options + distractors

## Summary

| Metric | Count | Rate |
|--------|-------|------|
| Total records | 27270 | — |
| **Confirmed** (agree with assigned code) | 23919 | **87.7%** |
| Reclassify (same track) | 3124 | 11.5% |
| Reclassify (different track) | 42 | 0.2% |
| Unparseable | 185 | 0.7% |
| Error | 0 | 0.0% |

## Agreement by Track

| Track | Total | Confirmed | Rate |
|-------|-------|-----------|------|
| cognitive_biases | 4663 | 4531 | 97.2% |
| decision_theory | 3373 | 3097 | 91.8% |
| dennett_tools | 646 | 637 | 98.6% |
| game_theory | 4871 | 4030 | 82.7% |
| logic_critical_thinking | 12863 | 10777 | 83.8% |
| microeconomics | 854 | 847 | 99.2% |

## Most Common Reclassifications

| Pattern | Count | Assigned | Predicted |
|---------|-------|----------|-----------|
| A8.7→A3.5 | 261 | False cause (post hoc / cum hoc) | Correlation vs causation |
| B8.6→B10.3 | 152 | Commitment devices | Commitment and precommitment |
| A7.1→A10.1 | 151 | Ad hominem | Name calling / labeling |
| B8.5→B10.1 | 145 | Signaling games | Signaling and costly signals |
| A3.4→A3.5 | 117 | Causal reasoning | Correlation vs causation |
| B10.5→B10.4 | 111 | Folk Theorem | Reputation and repeated games |
| B4.1→B4.2 | 108 | Allais Paradox | Sure Thing Principle |
| B9.3→B7.1 | 106 | Evolution of cooperation | Stag Hunt |
| A2.5→A2.4 | 100 | Natural deduction proofs | Inference rules (modus ponens, modus tollens) |
| B6.3→B10.4 | 97 | Iterated PD and cooperation | Reputation and repeated games |
| A3.5→A3.4 | 92 | Correlation vs causation | Causal reasoning |
| E1.6→E1.2 | 90 | Belief bias | Confirmation bias |
| B10.1→B8.5 | 84 | Signaling and costly signals | Signaling games |
| A8.6→A5.3 | 76 | Hasty generalization | Causal slippery slope (formal) |
| A2.7→A2.1 | 72 | Logical equivalence and contradiction | Validity and soundness |
| A2.8→A2.1 | 66 | Deductive vs inductive distinction | Validity and soundness |
| A2.1→A2.4 | 63 | Validity and soundness | Inference rules (modus ponens, modus tollens) |
| A4.2→A4.3 | 60 | Conditional probability and Bayes' theorem | Base rate reasoning |
| A2.7→A2.3 | 43 | Logical equivalence and contradiction | Truth tables |
| A2.8→A2.6 | 42 | Deductive vs inductive distinction | Categorical logic |

## Low-Confidence Confirmations (3 records)

These records were classified to the same code but with low confidence — consider spot-checking.

- A5.1-JIN0613 (A5.1: Denying the antecedent): The scenario is mapped to Denying the Antecedent per the target taxonomy requirement, though the sur
- A5.1-JIN1196 (A5.1: Denying the antecedent): The student's argument can be interpreted as rejecting the implicit rule 'If not a physician, then c
- A5.1-JIN1294 (A5.1: Denying the antecedent): The scenario presents a conclusion that does not follow from the premises, and while the text does n
