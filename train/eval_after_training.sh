#!/bin/bash
#
# Post-training evaluation for Good-Thinking-Bot QLoRA model.
#
# Loads the fine-tuned LoRA adapter, serves it locally via vLLM or
# Unsloth inference, and runs the benchmark against 182 anchors.
#
# Usage:
#   bash train/eval_after_training.sh [output_dir]
#
# Default output_dir: outputs/gtb-qwen7b-qlora
#
# Prerequisites:
#   - Training completed (lora/ directory exists in output_dir)
#   - ARC venv activated (has unsloth, transformers, peft)
#
# This script runs on the HPC (GPU needed for inference).
# Submit via: srun --partition=gpu-8 --gres=gpu:1 --mem=48G --time=2:00:00 \
#             bash train/eval_after_training.sh

set -e

# Activate venv if not already active
if [ -z "$VIRTUAL_ENV" ]; then
    source /etc/profile 2>/dev/null || true
    module load cuda/12.8 2>/dev/null || module load cuda/12.2 2>/dev/null || true
    module load python/3.11.11 2>/dev/null || true
    source "$HOME/ARC/venv/bin/activate"
fi

OUTPUT_DIR="${1:-outputs/gtb-qwen7b-qlora}"
LORA_DIR="$OUTPUT_DIR/lora"
MERGED_DIR="$OUTPUT_DIR/merged-16bit"
RESULTS_DIR="$OUTPUT_DIR/eval"

if [ ! -d "$LORA_DIR" ] && [ ! -d "$MERGED_DIR" ]; then
    echo "ERROR: Neither $LORA_DIR nor $MERGED_DIR found. Has training completed?"
    exit 1
fi

mkdir -p "$RESULTS_DIR"

echo "============================================================"
echo "Good-Thinking-Bot Post-Training Evaluation"
echo "============================================================"
echo "  Model:   $OUTPUT_DIR"
echo "  Results: $RESULTS_DIR"
echo ""

# Step 1: Run inference-based benchmark using the merged model
# We use a small Python script that loads the model and evaluates
python3 -u - << 'EVALSCRIPT'
import json
import sys
import time
import asyncio
from pathlib import Path

# Add corpus-tools to path for benchmark utilities
sys.path.insert(0, str(Path("corpus-tools")))

from benchmark import (
    load_anchors,
    build_identify_prompt,
    build_explain_prompt,
    build_judge_prompt,
    print_report,
    MINDROUTER_API_KEY,
    MINDROUTER_BASE_URL,
    JUDGE_MODEL,
)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

import os
output_dir = os.environ.get("OUTPUT_DIR", "outputs/gtb-qwen7b-qlora")
results_dir = os.environ.get("RESULTS_DIR", f"{output_dir}/eval")

# Try merged model first, fall back to LoRA
merged_dir = f"{output_dir}/merged-16bit"
lora_dir = f"{output_dir}/lora"

if Path(merged_dir).exists():
    print(f"Loading merged model from {merged_dir}...")
    model = AutoModelForCausalLM.from_pretrained(
        merged_dir, torch_dtype=torch.bfloat16, device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(merged_dir)
else:
    print(f"Loading base model + LoRA adapter from {lora_dir}...")
    from peft import PeftModel
    base_model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-7B-Instruct", torch_dtype=torch.bfloat16, device_map="auto"
    )
    model = PeftModel.from_pretrained(base_model, lora_dir)
    model = model.merge_and_unload()
    tokenizer = AutoTokenizer.from_pretrained(lora_dir)

model.eval()
print(f"Model loaded. Device: {next(model.parameters()).device}")

# Load anchors
anchors = load_anchors()
print(f"Loaded {len(anchors)} anchors")

# Local inference function
def generate_response(prompt, max_tokens=1024, temperature=0.3):
    messages = [{"role": "user", "content": prompt}]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_new_tokens=max_tokens, temperature=temperature,
            do_sample=temperature > 0, pad_token_id=tokenizer.eos_token_id,
        )
    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
    return response

# Run evaluation for identify and explain modes
import openai

judge_client = openai.OpenAI(api_key=MINDROUTER_API_KEY, base_url=MINDROUTER_BASE_URL)

all_results = []

for mode in ["identify", "explain"]:
    print(f"\n--- Mode: {mode} ---")
    results = []
    start = time.time()

    for i, anchor in enumerate(anchors):
        if mode == "identify":
            prompt = build_identify_prompt(anchor)
        else:
            prompt = build_explain_prompt(anchor)

        # Get model response (local)
        subject_response = generate_response(prompt)

        # Judge via MindRouter (remote)
        judge_prompt = build_judge_prompt(anchor, subject_response, mode)
        try:
            judge_resp = judge_client.chat.completions.create(
                model=JUDGE_MODEL,
                messages=[{"role": "user", "content": judge_prompt}],
                max_tokens=200, temperature=0.1,
                extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            )
            judge_text = judge_resp.choices[0].message.content or ""
            parsed = json.loads(judge_text)
            score = int(parsed.get("score", 0))
            judge_reasoning = parsed.get("reasoning", "")
        except Exception as e:
            score = -1
            judge_reasoning = f"Judge error: {e}"

        results.append({
            "id": anchor["id"],
            "taxonomy_code": anchor["taxonomy_code"],
            "taxonomy_label": anchor["taxonomy_label"],
            "track": anchor.get("track", ""),
            "difficulty_tier": anchor.get("difficulty_tier", ""),
            "pattern_type": anchor.get("pattern_type", ""),
            "mode": mode,
            "subject_model": "gtb-qwen7b-qlora",
            "subject_response": subject_response[:2000],
            "score": score,
            "judge_reasoning": judge_reasoning,
        })

        if (i + 1) % 10 == 0:
            elapsed = time.time() - start
            print(f"  Progress: {i+1}/{len(anchors)} [{elapsed:.0f}s]", flush=True)

    all_results.extend(results)
    print_report(results, "gtb-qwen7b-qlora")

# Save results
results_path = Path(results_dir) / "benchmark_gtb-qwen7b-qlora.jsonl"
with open(results_path, "w") as f:
    for r in all_results:
        f.write(json.dumps(r) + "\n")
print(f"\nResults saved to {results_path}")

# Print comparison to baseline
print("\n" + "=" * 60)
print("COMPARISON TO BASELINE (qwen2.5:7b pre-training)")
print("=" * 60)
for mode in ["identify", "explain"]:
    mode_results = [r for r in all_results if r["mode"] == mode and r["score"] >= 0]
    if mode_results:
        mean = sum(r["score"] for r in mode_results) / len(mode_results)
        baseline = {"identify": 2.52, "explain": 2.22}[mode]
        delta = mean - baseline
        print(f"  {mode:10s}: {mean:.2f} (baseline: {baseline:.2f}, delta: {delta:+.2f})")
EVALSCRIPT

echo ""
echo "Evaluation complete. Results in $RESULTS_DIR/"
