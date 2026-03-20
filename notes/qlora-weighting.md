# QLoRA: Quantized Low-Rank Adaptation

## Background: LoRA (Low-Rank Adaptation)

To understand QLoRA, you need LoRA first. When fine-tuning a model, instead of updating all the original weights (which is expensive), LoRA freezes the pretrained weights and injects small trainable **low-rank decomposition matrices** alongside them.

Concretely, for a weight matrix **W** of shape (d × k), LoRA adds:

> **ΔW = A · B**

where **A** is (d × r) and **B** is (r × k), with rank r ≪ min(d, k). During fine-tuning, only A and B are updated. This reduces trainable parameters dramatically — often by 10,000x — while preserving most of the model's expressive capacity.

---

## What QLoRA Adds: Quantization

QLoRA (introduced by Dettmers et al., 2023) stacks quantization on top of LoRA to reduce **memory** further:

1. **4-bit NormalFloat (NF4) quantization** — The frozen base model weights are stored in 4-bit precision using a data type optimized for normally distributed weights. This cuts memory by ~8x compared to 32-bit.

2. **Double quantization** — The quantization constants themselves are quantized, saving additional memory (roughly 0.37 bits per parameter).

3. **Paged optimizers** — NVIDIA unified memory is used to page optimizer states to CPU RAM when GPU memory is tight, preventing OOM crashes during training.

4. **LoRA adapters in full precision** — Even though the base model is frozen in 4-bit, the small LoRA adapter matrices (A and B) are trained in **BFloat16 or Float32**, preserving gradient fidelity.

---

## The Key Insight

At inference/training time, the 4-bit weights are **dequantized on the fly** to BFloat16 for the forward and backward pass computations, but never stored in full precision. This means:

- **Memory**: You get the footprint of a quantized model.
- **Quality**: You get gradients flowing through full-precision adapters.

---

## Why It Matters

| Method | Memory for 65B model | Hardware needed |
|---|---|---|
| Full fine-tuning (fp16) | ~130 GB | Many A100s |
| LoRA (fp16) | ~65 GB | Several A100s |
| **QLoRA (4-bit)** | **~48 GB** | **Single A100 or 2× consumer GPUs** |

QLoRA made it possible to fine-tune models like LLaMA-65B on a single 48GB GPU, which was a landmark result. It democratized fine-tuning significantly.

---

## Practical Tradeoffs

- **Speed**: Slightly slower than LoRA alone due to dequantization overhead.
- **Quality**: Very close to full fine-tuning in most benchmarks, though there can be a small gap on demanding tasks.
- **Use case fit**: Excellent for instruction tuning, domain adaptation, and task-specific fine-tuning; less suited for pretraining from scratch.

In the HuggingFace ecosystem, QLoRA is accessible via the `bitsandbytes` library for quantization and `peft` for the LoRA adapter management, making it quite straightforward to apply to most transformer architectures.

---

# Merging Multiple QLoRA Adapters

Yes, this is an active and well-developed area — often called **LoRA merging** or **adapter merging**. A few distinct approaches exist:

---

## 1. Linear Interpolation / Weighted Averaging

The simplest approach: given multiple LoRA adapters (ΔW₁ = A₁B₁, ΔW₂ = A₂B₂, ...), combine them as:

> **ΔW_combined = α₁·A₁B₁ + α₂·A₂B₂ + ...**

where the αᵢ are scalar weights you choose. This works because the LoRA updates are just matrices — addition is valid. The combined adapter can then be merged into the base model weights in one shot.

This is sometimes called **LoRA soup** by analogy with model soups (weight averaging of full models).

---

## 2. Task Arithmetic

Introduced by Ilharco et al. (2022), the idea is that fine-tuned weight deltas behave like **vectors in parameter space** that can be added and subtracted meaningfully:

- **Adding** adapters combines capabilities.
- **Negating** an adapter can *remove* a behavior (e.g., subtract a "toxic" adapter).
- **Scaling** controls the strength of each contribution.

This works surprisingly well in practice and has a nice geometric intuition — each task carves out a direction in weight space.

---

## 3. TIES-Merging

A more principled approach that addresses **interference** between adapters. When multiple adapters are naively averaged, conflicting parameter updates can cancel out. TIES-Merging handles this by:

1. **Trimming** small-magnitude parameters (likely noise).
2. **Electing** a sign for each parameter based on majority vote across adapters.
3. **Disjoint merging** — only averaging parameters that agree on sign.

This generally outperforms naive averaging when adapters were trained on dissimilar tasks.

---

## 4. DARE (Drop and REscale)

A complementary technique that randomly drops a fraction of the delta parameters before merging (since most are close to zero and redundant), then rescales the survivors to preserve expected magnitude. Often combined with TIES.

---

## 5. Dynamic / Conditional Weighting (MoLoRA / LoRAHub)

Rather than fixed αᵢ weights, you can make the combination **input-dependent** — essentially a Mixture of Experts over adapters. A lightweight routing network decides at inference time how much weight each adapter gets. This is more powerful but adds complexity.

**LoRAHub** is a simpler variant where the αᵢ are optimized (via gradient-free search) on a small held-out dataset for a target task, rather than set manually.

---

## Practical Considerations

| Concern | Notes |
|---|---|
| **Rank compatibility** | Adapters being merged should ideally have the same rank r, or you need to project to a common rank first |
| **Base model must match** | All adapters must have been trained on the same frozen base |
| **Interference** | Adapters trained on similar tasks merge better; dissimilar tasks benefit from TIES/DARE |
| **The 4-bit base** | In QLoRA specifically, the base stays quantized regardless — you're only ever combining the full-precision A/B matrices, so quantization doesn't complicate the merge |

---

## The QLoRA-Specific Angle

One nice property of QLoRA in this context: since the base model weights are frozen and quantized, **merging is entirely an operation on the small, full-precision adapter matrices**. The quantized base is just a fixed backdrop. This makes multi-adapter merging computationally cheap and clean — you're not dealing with quantized arithmetic during the merge itself.

This is a genuinely useful technique in practice, especially for building models that need to blend a general instruction-following capability with domain-specific knowledge.

## Implementation notes

PyTorch native (no HF)
You can implement LoRA as plain nn.Linear wrappers — add A and B as nn.Parameter on any layer. No PEFT dependency at all. This is what most research code does before productionizing. The from_peft stub would just become from_torch_layer.

Axolotl
A training framework built on top of HF/PEFT but with much more opinionated config-driven workflows. Still uses PEFT under the hood for the adapter representation.

LitGPT (Lightning AI)
Has its own LoRA implementation separate from PEFT, tightly integrated with their training loop. Cleaner code than HF if you want to read and modify the LoRA logic itself.

Unsloth
Optimized QLoRA training with hand-tuned CUDA kernels — significantly faster than PEFT/bitsandbytes for the same hardware. Has its own adapter format but can export to HF-compatible checkpoints.

llama.cpp / ggml
Runs quantized models (GGUF format) on CPU/GPU without PyTorch at all. Has experimental LoRA adapter support (--lora flag), though merging tools there are more limited.

MLX (Apple Silicon)
Apple's array framework with native LoRA fine-tuning for running on Mac hardware. Good option if you're targeting on-device inference on Apple hardware, which aligns with the QLoRA-on-device direction in CLAUDE.md.

For this project's stated goal of on-device inference, MLX or llama.cpp are probably the most relevant alternatives to HF — they're the realistic deployment targets for a game running locally. The from_peft stub in adapter.py would just need a parallel from_mlx or from_gguf classmethod when you get there.

