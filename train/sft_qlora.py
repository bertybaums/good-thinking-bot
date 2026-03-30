#!/usr/bin/env python3
"""
Good-Thinking-Bot SFT with QLoRA (Unsloth + TRL) on Qwen2.5-7B-Instruct.

Trains a LoRA adapter to tutor critical thinking, logic, decision theory,
and game theory using a pre-prepared JSONL corpus (~15.5K records across
a 167-code taxonomy).

Each JSONL record is already in chat conversation format:
  {"messages": [{"role": "system", ...}, {"role": "user", ...}, {"role": "assistant", ...}]}

Save outputs:
  <output_dir>/lora/  (LoRA adapter + tokenizer)
  <output_dir>/merged-16bit/  (always saved for HuggingFace upload)
"""

from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template

import os
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

import torch
from datasets import Dataset, DatasetDict
from trl import SFTTrainer, SFTConfig
from transformers import set_seed


# ── System prompt ──

SYSTEM_PROMPT = """\
You are an expert tutor in critical thinking, logic, decision theory, and \
game theory. When presented with a reasoning scenario, you: (1) identify \
the specific reasoning pattern, fallacy, bias, or strategic concept; \
(2) name it precisely; (3) explain the mechanism — what makes this \
reasoning good, bad, or strategically important; (4) note edge cases or \
counterpoints where the pattern might not apply. Be thorough but concise. \
Ground explanations in the specific scenario details."""


# ── Data loading ──

def load_jsonl(path: str) -> List[Dict[str, Any]]:
    """Load a JSONL file where each line is a chat conversation."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return records


def build_datasets(
    train_file: str,
    val_file: str,
) -> DatasetDict:
    """Load pre-split train/val JSONL files into a DatasetDict."""
    train_records = load_jsonl(train_file)
    val_records = load_jsonl(val_file)
    print(f"Loaded {len(train_records)} train + {len(val_records)} val "
          f"= {len(train_records) + len(val_records)} total")

    ds = DatasetDict({
        "train": Dataset.from_list(train_records),
        "validation": Dataset.from_list(val_records),
    })

    return ds


# ── Formatting function for TRL ──

tokenizer = None


def formatting_func(examples):
    """Format chat messages for SFTTrainer."""
    global tokenizer

    conversations = examples["messages"]

    # Handle single (unbatched) example
    if conversations and isinstance(conversations[0], dict):
        conversations = [conversations]

    outputs = []
    for conversation in conversations:
        formatted_text = tokenizer.apply_chat_template(
            conversation,
            tokenize=False,
            add_generation_prompt=False,
        )
        outputs.append(formatted_text)

    return outputs


# ── Main ──

def main():
    global tokenizer

    parser = argparse.ArgumentParser(
        description="Good-Thinking-Bot SFT (QLoRA) on Qwen2.5-7B-Instruct")

    # Data
    parser.add_argument("--train_file", default="train/data/train.jsonl",
                        help="Path to training JSONL file")
    parser.add_argument("--val_file", default="train/data/val.jsonl",
                        help="Path to validation JSONL file")
    parser.add_argument("--output_dir", default="outputs/gtb-qwen7b-qlora",
                        help="Where to save checkpoints/adapters")

    # Model
    parser.add_argument("--model_name", default="unsloth/Qwen2.5-7B-Instruct",
                        help="Base model (Unsloth-optimized)")
    parser.add_argument("--max_seq_len", type=int, default=2048)
    parser.add_argument("--seed", type=int, default=42)

    # LoRA / QLoRA
    parser.add_argument("--r", type=int, default=16,
                        help="LoRA rank")
    parser.add_argument("--lora_alpha", type=int, default=16,
                        help="LoRA alpha (scaling = alpha/r)")
    parser.add_argument("--lora_dropout", type=float, default=0.0)
    parser.add_argument(
        "--target_modules", nargs="+",
        default=["q_proj", "k_proj", "v_proj", "o_proj",
                 "gate_proj", "up_proj", "down_proj"],
        help="LoRA target modules")

    # Training
    parser.add_argument("--batch_size", type=int, default=2,
                        help="Per-device train batch size")
    parser.add_argument("--grad_accum", type=int, default=8,
                        help="Gradient accumulation steps (effective batch = batch_size * grad_accum)")
    parser.add_argument("--epochs", type=float, default=3.0)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--warmup_ratio", type=float, default=0.03)
    parser.add_argument("--logging_steps", type=int, default=10)
    parser.add_argument("--save_steps", type=int, default=500)
    parser.add_argument("--eval_steps", type=int, default=500)
    parser.add_argument("--bf16", action="store_true",
                        help="Use BF16 (A6000 supports this)")
    parser.add_argument("--packing", action="store_true",
                        help="Enable sequence packing")
    parser.add_argument("--save_merged_16bit", action="store_true",
                        help="Also save merged 16-bit model")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    set_seed(args.seed)

    # 1) Build datasets
    ds = build_datasets(
        train_file=args.train_file,
        val_file=args.val_file,
    )

    # 2) Load model + tokenizer
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=args.model_name,
        max_seq_length=args.max_seq_len,
        dtype=None,
        load_in_4bit=True,
        device_map="auto",
    )

    tokenizer = get_chat_template(tokenizer, chat_template="qwen-2.5")

    # 3) Apply LoRA
    model = FastLanguageModel.get_peft_model(
        model,
        r=args.r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=args.target_modules,
        bias="none",
        use_gradient_checkpointing="unsloth",
    )

    # 4) Training config
    training_args = SFTConfig(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        num_train_epochs=args.epochs,
        warmup_ratio=args.warmup_ratio,
        lr_scheduler_type="cosine",
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        eval_strategy="steps",
        eval_steps=args.eval_steps,
        save_total_limit=3,
        bf16=args.bf16,
        fp16=not args.bf16,
        packing=args.packing,
        eos_token="<|im_end|>",
        pad_token=tokenizer.eos_token,
        optim="paged_adamw_8bit",
        report_to=None,
        max_length=args.max_seq_len,
    )

    # 5) Train
    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,
        args=training_args,
        train_dataset=ds["train"],
        eval_dataset=ds["validation"],
        formatting_func=formatting_func,
    )

    print(f"\n{'='*60}")
    print(f"Good-Thinking-Bot QLoRA SFT")
    print(f"  Model:     {args.model_name}")
    print(f"  LoRA rank: {args.r}, alpha: {args.lora_alpha}")
    print(f"  Train:     {len(ds['train'])} examples")
    print(f"  Val:       {len(ds['validation'])} examples")
    print(f"  Epochs:    {args.epochs}")
    print(f"  Eff batch: {args.batch_size * args.grad_accum}")
    print(f"  LR:        {args.lr}")
    print(f"  Packing:   {args.packing}")
    print(f"  BF16:      {args.bf16}")
    print(f"  Output:    {args.output_dir}")
    print(f"{'='*60}\n")

    trainer.train()

    # 6) Save LoRA adapter
    lora_dir = os.path.join(args.output_dir, "lora")
    os.makedirs(lora_dir, exist_ok=True)
    model.save_pretrained(lora_dir)
    tokenizer.save_pretrained(lora_dir)
    print(f"\n[OK] Saved LoRA adapter to: {lora_dir}")

    # 7) Always save merged 16-bit model (for HuggingFace upload)
    merged_dir = os.path.join(args.output_dir, "merged-16bit")
    os.makedirs(merged_dir, exist_ok=True)
    model.save_pretrained_merged(
        merged_dir, tokenizer, save_method="merged_16bit")
    print(f"[OK] Saved merged 16-bit model to: {merged_dir}")

    # 8) Save training config for reproducibility
    config_path = os.path.join(args.output_dir, "training_config.json")
    with open(config_path, "w") as f:
        json.dump(vars(args), f, indent=2)
    print(f"[OK] Saved config to: {config_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
