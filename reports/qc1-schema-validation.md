# QC1: Schema Validation & Deduplication Report

**Total records:** 30697
**Parse errors:** 18
**Duplicate IDs:** 1137
**Near-duplicate scenarios:** 962

## Validation Issues

| Issue | Count |
|-------|-------|
| missing_scenario_field | 2 |
| missing_top_level | 2 |
| short_scenario_text | 1 |
| track_mismatch | 91 |
| unknown_code | 30 |

## File Statistics

| File | Valid | Errors |
|------|-------|--------|
| adapted_corr2cause.jsonl | 2232 | 3 |
| adapted_folio.jsonl | 1181 | 14 |
| adapted_jin.jsonl | 3788 | 1 |
| adapted_propaganda.jsonl | 5873 | 0 |
| anchors.jsonl | 167 | 0 |
| anchors_A1_A4.jsonl | 23 | 0 |
| anchors_B_remaining.jsonl | 40 | 0 |
| anchors_C_E1_remaining.jsonl | 26 | 0 |
| anchors_remaining_fallacies.jsonl | 18 | 0 |
| cognitive_biases_E1.jsonl | 10 | 0 |
| decision_theory_batch.jsonl | 7 | 0 |
| dennett_tools.jsonl | 11 | 0 |
| fill_final_thin.jsonl | 790 | 0 |
| overnight_thin_A.jsonl | 3700 | 0 |
| overnight_thin_DT.jsonl | 1500 | 0 |
| overnight_topup_GT.jsonl | 1793 | 0 |
| overnight_topup_biases.jsonl | 2400 | 0 |
| synthetic_A1_fill.jsonl | 50 | 0 |
| synthetic_DT_sprint3.jsonl | 1978 | 0 |
| synthetic_E1_mindrouter.jsonl | 63 | 0 |
| synthetic_GT_integrated_sprint5.jsonl | 1197 | 0 |
| synthetic_biases_sprint4.jsonl | 2400 | 0 |
| synthetic_dennett_fill.jsonl | 700 | 0 |
| synthetic_microecon_fill.jsonl | 750 | 0 |

## Duplicate IDs (1137)

- `E1.7-002`: 32x
- `A7.10-002`: 29x
- `E1.20-002`: 27x
- `E1.16-001`: 25x
- `E1.10-001`: 24x
- `E1.24-002`: 23x
- `E1.9-002`: 23x
- `E1.11-002`: 22x
- `E1.22-001`: 21x
- `E1.4-002`: 21x
- `E1.15-002`: 21x
- `E1.20-001`: 20x
- `E1.16-DR001`: 20x
- `E1.1-002`: 18x
- `E1.23-002`: 17x
- `E1.1-001`: 16x
- `E1.21-001`: 15x
- `E1.12-001`: 14x
- `E1.16-002`: 14x
- `E1.8-002`: 14x

## Near-Duplicate Scenarios (962)

- 4 records share: "Premise: Suppose there is a closed system of 3 variables, A, B, and C. All the s..."
  - `A3.5-COR0007`
  - `A3.5-COR0017`
  - `A3.5-COR0025`
- 10 records share: "Premise: Suppose there is a closed system of 3 variables, A, B, and C. All the s..."
  - `A3.5-COR0023`
  - `A3.5-COR0026`
  - `A3.5-COR0029`
- 2 records share: "Suppose there is a closed system of 3 variables: A, B, and C. All statistical re..."
  - `A3.5-COR0030`
  - `A3.5-COR0043`
- 14 records share: "Premise: Suppose there is a closed system of 4 variables, A, B, C, and D. All th..."
  - `A3.5-COR0068`
  - `A3.5-COR0083`
  - `A3.5-COR0099`
- 2 records share: "Premise: Consider a closed system of 4 variables: A, B, C, and D. The statistica..."
  - `A3.5-COR0074`
  - `A3.5-COR0107`
- 44 records share: "Suppose there is a closed system of 5 variables: A, B, C, D, and E. All statisti..."
  - `A3.5-COR0131`
  - `A3.5-COR0156`
  - `A3.5-COR0157`
- 2 records share: "Behold the closed system of five variables: A, B, C, D, and E. Observe their tie..."
  - `A3.5-COR0137`
  - `A3.5-COR0202`
- 12 records share: "Premise: Suppose there is a closed system of 5 variables, A, B, C, D, and E. All..."
  - `A3.5-COR0140`
  - `A3.5-COR0153`
  - `A3.4-COR0371`
- 4 records share: "Premise: Consider a closed system of five variables: A, B, C, D, and E. The stat..."
  - `A3.5-COR0151`
  - `A3.5-COR0392`
  - `A3.5-COR0454`
- 2 records share: "Logos presents the data: 'In this closed system, every variable correlates with ..."
  - `A3.5-COR0155`
  - `A3.5-COR0342`

## Track Mismatches (91)

- A2.7-FOL0518: A2.7 expected logic_critical_thinking, got logic_critical thinking
- A2.8-FOL0768: A2.8 expected logic_critical_thinking, got logic_critical thinking
- A10.3-FN0064: A10.3 expected logic_critical_thinking, got logic_critical_sketching
- A10.3-FN0035: A10.3 expected logic_critical_thinking, got logic_critical_reading
- A10.3-FN0093: A10.3 expected logic_critical_thinking, got logic_critical_thending
- A10.3-FN0049: A10.3 expected logic_critical_thinking, got logic_critical_t hinking
- A8.3-ON0036: A8.3 expected logic_critical_thinking, got logic_critical_t hinking
- A7.3-ON0085: A7.3 expected logic_critical_thinking, got logic_critical_teaching
- A7.3-ON0081: A7.3 expected logic_critical_thinking, got logic_critical_testing
- A7.13-ON0056: A7.13 expected logic_critical_thinking, got logic_critical_Thinking
- A7.14-ON0071: A7.14 expected logic_critical_thinking, got logic_critical_t hinking
- A8.3-ON0089: A8.3 expected logic_critical_thinking, got logic_critical_t hinking
- A7.3-ON0097: A7.3 expected logic_critical_thinking, got logic_critical_testing
- A7.13-ON0014: A7.13 expected logic_critical_thinking, got logic_critical_t hinking
- A7.3-ON0079: A7.3 expected logic_critical_thinking, got logic_critical_teaching
- A7.3-ON0068: A7.3 expected logic_critical_thinking, got logic_critical_teaching
- A7.11-002: A7.11 expected logic_critical_thinking, got logic_critical_typing
- A7.14-ON0018: A7.14 expected logic_critical_thinking, got logic_critical_turning
- A7.3-ON0048: A7.3 expected logic_critical_thinking, got logic_critical_trinking
- A7.14-ON0070: A7.14 expected logic_critical_thinking, got logic_critical_teaching

## Summary

- 30697 records loaded
- 126 total issues found
- 1137 duplicate IDs
- 962 near-duplicate scenario groups