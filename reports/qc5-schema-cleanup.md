# QC5: Schema Cleanup Report

**Date:** 2026-03-29
**Scope:** All 17 training corpus JSONL files (24,761 records)
**Method:** Automated type coercion, field renaming, rubric normalization, and Pydantic revalidation

## Summary

| Metric | Count |
|--------|-------|
| Records before cleanup | 24,779 |
| Records after cleanup | 24,761 |
| Invalid JSON lines removed | 18 |
| Field type coercions (list/dict → string) | 2,613 |
| Structural fixes (renamed fields, missing defaults) | 13 |
| Rubric format fixes (dict → array, levels capped) | 475 |
| Mechanical verification fix (B6.2-ROYAL-001) | 1 |
| **Final Pydantic validation pass rate** | **100.0%** |

## Context

QC1 (March 23) identified 126 schema issues and 91 track mismatches but did not fix them.
QC2 (March 23) identified 56 mechanical verification failures — 51 were removed during QC,
2 were already corrected, and 1 (B6.2-ROYAL-001) remained. This cleanup addresses all
remaining schema and mechanical issues to bring the corpus to full Pydantic compliance.

## Issues Fixed

### 1. String Fields Stored as Lists (2,035 instances)

**Primary field:** `game_hooks.npc_dialogue_seed`

The synthetic generation pipeline (MindRouter gpt-oss-120b) sometimes returned dialogue
seeds as JSON arrays of strings instead of a single string. Example:

```
Before: ["Oh, spare me the lecture.", "His bias is showing."]
After:  "Oh, spare me the lecture. His bias is showing."
```

**Fix:** List items joined with spaces (short items) or newlines (long items).

**Other affected fields:** `game_hooks.resolution_path` (269 list + 87 dict),
`game_hooks.npc_personality` (114 dict + 26 list), `structure.formal_form` (40 list + 40 dict),
`structure.counterpoint` (1 list), `scenario.speaker_context` (1 dict).

For dict values, key-value pairs were formatted as "Key: value" strings.

### 2. Invalid JSON Lines (18 removed)

18 lines across 3 files (`adapted_corr2cause.jsonl`, `adapted_folio.jsonl`, `adapted_jin.jsonl`)
contained malformed JSON (truncation or encoding errors). These records were removed rather
than salvaged, as they represented < 0.1% of the corpus.

### 3. Rubric Format Issues (475 in qc_fill_thin.jsonl)

The QC fill pipeline produced rubrics as dicts (`{"1": "desc", "2": "desc"}`) instead of the
required array format (`[{"level": 0, "description": "..."}, ...]`). Some also used levels > 4
(the schema enforces `level` in 0–4) or non-numeric keys (e.g., `"Excellent"`).

**Fix:** Converted all rubric dicts to arrays, capped levels at 0–4, and filled missing levels
with standard defaults.

### 4. Renamed Fields (13 records)

Some synthetic records used variant field names:
- `npc_character` → `npc_personality`
- `npc_character_description` → `npc_personality`
- `dialogue_seed` → `npc_dialogue_seed`
- `dialogue` → `npc_dialogue_seed`
- `resolution` → `resolution_path`

Records missing required `game_hooks` fields were given sensible defaults.

### 5. Mechanical Fix: B6.2-ROYAL-001

This record falsely claimed two Nash equilibria — (Send Envoy, Send Envoy) and
(Mobilize Troops, Mobilize Troops) — in what is actually a Prisoner's Dilemma
where Mobilize strictly dominates Send.

**Fix:** Corrected `formal_form`, `pattern_description` (full best-response analysis),
`why_right`, and `counterpoint` to reflect the single NE at (Mobilize, Mobilize).

### 6. Previously Fixed Records

Two records flagged in QC2 were already correct at the time of this cleanup:
- **B7.1-CASTLE-004**: Stag Hunt with both NE correctly listed. Parser failed on
  Unicode non-breaking hyphens (U+2011) in strategy names, not a content error.
- **B6.2-TRN-202603**: Nash equilibrium already corrected since QC2.

51 other QC2 failures had been removed from the corpus during the original QC process.

## Final State

| File | Records | Status |
|------|---------|--------|
| anchors.jsonl | 167 | Clean |
| adapted_jin.jsonl | 3,749 | Clean (1 field fix, 1 JSON removed) |
| adapted_folio.jsonl | 1,039 | Clean (14 JSON removed) |
| adapted_corr2cause.jsonl | 1,807 | Clean (3 JSON removed) |
| adapted_propaganda.jsonl | 1,845 | Clean |
| synthetic_DT_sprint3.jsonl | 1,944 | Clean (42 field + 2 structural) |
| synthetic_GT_integrated_sprint5.jsonl | 1,137 | Clean (158 field + 1 mechanical) |
| synthetic_biases_sprint4.jsonl | 2,251 | Clean (1,379 field + 5 structural) |
| synthetic_dennett_fill.jsonl | 306 | Clean |
| synthetic_microecon_fill.jsonl | 659 | Clean |
| synthetic_A1_fill.jsonl | 50 | Clean |
| overnight_thin_A.jsonl | 3,491 | Clean (140 field + 1 structural) |
| overnight_thin_DT.jsonl | 1,353 | Clean (97 field) |
| overnight_topup_biases.jsonl | 2,265 | Clean (155 field + 4 structural) |
| overnight_topup_GT.jsonl | 1,602 | Clean (92 field) |
| fill_final_thin.jsonl | 514 | Clean (17 field + 1 structural) |
| qc_fill_thin.jsonl | 2,582 | Clean (532 field + 475 rubric) |
| **Total** | **24,761** | **100% Pydantic-valid** |

## Scripts

- `fix_mechanical_failures.py` — Identifies and patches mechanical verification failures
  using the same solver logic as `05_mechanical_verify.py`. Supports `--dry-run` and `--apply`.
  (Only 3 records remained at runtime; 1 was fixed, 2 were already correct.)
- The schema cleanup was performed via inline scripts during this session. The fixes are
  idempotent — rerunning them on the cleaned corpus produces no changes.

## Known Limitations

- **3,888 unparseable B-code records** (from QC2) have `formal_form` fields in formats the
  mechanical verifier cannot parse (prospect theory, replicator dynamics, etc.). These are
  not errors — they are structurally different problem types that would need specialized parsers.
- **Pareto efficiency** appears in 149 records as a secondary concept (mostly in PD and Nash
  equilibrium contexts) but has no dedicated taxonomy code. This is a coverage gap — Pareto
  efficiency, Pareto improvement, and Pareto dominance are foundational concepts that students
  should encounter as standalone entries, not only in contrast to Nash equilibrium.
