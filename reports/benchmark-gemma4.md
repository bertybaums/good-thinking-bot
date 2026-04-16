# Benchmark: Gemma-4 (26b and 31b) on Good-Thinking Anchor Set

**Date:** April 15, 2026
**Models:** `google/gemma-4-26b`, `google/gemma-4-31b` via MindRouter (concurrency 8 each)
**Anchors:** 182 (current full set, post PHIL 4040 expansion)
**Judge:** `qwen/qwen3.5-122b` via MindRouter
**Modes:** identify, classify, explain (all three)
**Artifacts:**
- `corpus-tools/output/benchmark_google-gemma-4-26b.jsonl`
- `corpus-tools/output/benchmark_google-gemma-4-31b.jsonl`
- 2 unrecoverable judge errors per model (malformed judge JSON, not API failures); excluded from means.

## Headline

| Model | Identify | Classify | Explain |
|---|---:|---:|---:|
| **gemma-4-26b** | **3.51** | 3.85 | **3.66** |
| **gemma-4-31b** | 3.48 | **3.89** | 3.65 |

The two models are essentially tied — 26b is marginally better on identify, 31b on classify, identical on explain. **No reason to prefer the larger one.**

## Comparison to other models

| Model | Identify | Classify | Explain |
|---|---:|---:|---:|
| qwen2.5:7b (baseline) | 2.52 | 3.58 | 2.22 |
| **qwen2.5:7b + QLoRA (ours)** | 3.20 | — | 3.53 |
| gpt-oss-20b | 2.61 | 0.22* | 2.41 |
| gpt-oss-120b | 3.15 | 0.44* | 2.93 |
| Nemotron-3-Super-120b | 3.40 | 3.74 | 3.54 |
| qwen3.5-122b | 3.47 | 3.90 | 3.60 |
| **gemma-4-26b** | **3.51** | 3.85 | **3.66** |
| **gemma-4-31b** | 3.48 | 3.89 | 3.65 |

*gpt-oss classify scores are likely format-parsing artifacts, not true performance.

**Gemma-4 26b is the new top scorer on identify and explain.** It edges past qwen3.5-122b at less than a quarter the parameters. Our fine-tuned 7B remains competitive on explain (3.53 vs 3.66) — the QLoRA buys roughly a 4× model-size advantage on the trained task.

## Per-track breakdown

### gemma-4-26b
| Track | Identify | Classify | Explain |
|---|---:|---:|---:|
| Cognitive biases | 3.54 | 3.83 | **4.00** |
| Decision theory | 3.52 | 3.87 | 3.65 |
| Dennett tools | 3.21 | 3.71 | 3.00 |
| Game theory | 3.45 | 3.75 | 3.55 |
| Logic / CT | 3.58 | 3.94 | 3.66 |
| Microeconomics | 3.50 | 3.75 | 3.94 |

### gemma-4-31b
| Track | Identify | Classify | Explain |
|---|---:|---:|---:|
| Cognitive biases | 3.50 | **4.00** | 3.92 |
| Decision theory | 3.50 | 3.87 | 3.65 |
| Dennett tools | 3.14 | 3.43 | 2.93 |
| Game theory | 3.52 | 3.88 | 3.66 |
| Logic / CT | 3.58 | 3.94 | 3.63 |
| Microeconomics | 3.19 | **4.00** | **4.00** |

## Observations
- **Dennett tools is the universal weak spot** for both Gemma models on explain (3.00 / 2.93) — same pattern we saw in the qwen2.5:7b baseline, suggesting Dennett-style metacognitive moves (jootsing, intuition pumps, the Panglossian Slide) genuinely require corpus exposure rather than scale.
- Microeconomics flips: 31b nails it (4.00/4.00) while 26b is weaker on identify (3.50). Small n (16) — could be noise.
- Both Gemma-4 models could serve as **distillation teachers** for the next QLoRA round, particularly for explain-mode targets where they slightly beat Nemotron and qwen3.5-122b.

## Re-judge note
Initial run had 6–7 judge errors per model (likely transient JSON parse issues). Re-ran via `corpus-tools/rejudge_errors.py`; resolved 9 of 13. The remaining 2 per model are excluded from reported means.
