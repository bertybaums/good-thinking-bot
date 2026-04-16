# Post-Training Benchmark: qwen2.5:7b + QLoRA (gtb-qwen7b-qlora)

**Date:** April 15, 2026
**Model:** `outputs/gtb-qwen7b-qlora/merged-16bit` (Qwen2.5-7B-Instruct + QLoRA, merged 16-bit)
**Training:** SLURM job 5120916 on fortyfive HPC (RTX 4090), 3 epochs, 4860 steps, ~6.6h. Final train_loss 0.629, eval_loss 0.602.
**Benchmark:** 182 anchors. Judge: `qwen/qwen3.5-122b` via MindRouter (swapped in because `qwen3.5-400b` was decommissioned).
**Eval jobs:** identify = 5120971 (in-run). explain = 5126077 (subject responses); re-judged locally on 2026-04-15 after MindRouter API key rotation (`corpus-tools/rescore_explain.py`).

## Headline

| Mode | Baseline (pre-training) | Post-QLoRA | Δ |
|------|------------------------:|-----------:|---:|
| Identify | 2.52 | **3.20** | +0.68 |
| Explain  | 2.22 | **3.53** | +1.31 |

Cleared the 3.0+ target on both modes. Explain-mode score ties qwen3.5-122b (3.60) and beats gpt-oss-120b (2.93) — a 7B model matching/exceeding its 120B+ teachers on the task it was trained for.

## Explain by track (post-QLoRA)

| Track | Score | n |
|---|---:|---:|
| Cognitive biases | 3.83 | 24 |
| Game theory | 3.75 | 32 |
| Decision theory | 3.47 | 30 |
| Logic / critical thinking | 3.43 | 65 |
| Dennett tools | 3.36 | 14 |
| Microeconomics | 3.31 | 16 |

1 of 182 judge calls errored (valid n = 181).

## Identify by track (post-QLoRA)

| Track | Score | Δ vs 2.52 baseline |
|---|---:|---:|
| Logic / CT | 3.29 | +0.77 |
| Decision theory | 3.26 | +0.74 |
| Cognitive biases | 3.25 | +0.73 |
| Game theory | 3.22 | +0.70 |
| Dennett tools | 2.64 | +1.43 |
| Microeconomics | 2.50 | ~flat |

## Biggest gains (vs weakest baseline areas)
- Dennett tools: explain +2.15 (1.21 → 3.36), identify +1.43
- Game theory: explain +1.59 (2.16 → 3.75)

## Weak spots remaining
- **Microeconomics identify (2.50)** — essentially unchanged by training; may need more corpus volume or better anchors. Explain is fine (3.31).
- Explain-mode weakest cases (from in-run scoring pre-rejudge): A2.3 Truth tables, C5.1 Supply/demand/equilibrium, C7.2 Zero-sum thinking, B2.4 Subjective vs objective probability, D1.5 Jootsing.

## Artifacts
- Merged model: `fortyfive:/mnt/ceph/bbaum/good-thinking-bot/outputs/gtb-qwen7b-qlora/merged-16bit`
- LoRA adapter: `.../outputs/gtb-qwen7b-qlora/lora`
- Explain results (re-judged, local): `corpus-tools/output/post-training/benchmark_gtb-qwen7b-qlora.rescored.jsonl`
- Re-score script: `corpus-tools/rescore_explain.py`

## Infra notes
- MindRouter API keys rotate; a `401 API key is revoked` error wiped the first explain run's scores. Subject responses were preserved, so re-judging is cheap — use `rescore_explain.py` for this pattern in the future.
- Judge model is now `qwen/qwen3.5-122b` (see `corpus-tools/benchmark.py:50`).
- Eval walltime for explain on gpu-8: ~35 min for 182 samples (bumped slurm from 2h → 6h just in case).
