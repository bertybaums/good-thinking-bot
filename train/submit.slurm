#!/bin/bash
#
# Good-Thinking-Bot QLoRA SFT on Qwen2.5-7B-Instruct
#
# Workflow:
# 1. Run prepare_data.py locally to create train/data/{train,val}.jsonl
# 2. Push project to HPC: rsync -av good-thinking-bot/ fortyfive:~/good-thinking-bot/
# 3. Submit: sbatch train/submit.slurm
# 4. Monitor: tail -f logs/<jobid>_gtb-sft.out
# 5. After training: run eval_after_training.sh
#
# Usage: sbatch train/submit.slurm
#

#SBATCH -p gpu-8-long
#SBATCH --gres=gpu:1
#SBATCH --exclude=n113
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=24:00:00
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=bbaum@uidaho.edu
#SBATCH --output=logs/%j_gtb-sft.out
#SBATCH --error=logs/%j_gtb-sft.err

source /etc/profile
set -e

module load cuda/12.8 2>/dev/null || module load cuda/12.2 2>/dev/null || true
module load python/3.11.11 2>/dev/null || true

nvidia-smi -L

# Reuse the ARC venv which has Unsloth + TRL + PEFT + bitsandbytes
source "$HOME/ARC/venv/bin/activate"

cd "$HOME/good-thinking-bot"
mkdir -p logs

python -u train/sft_qlora.py \
    --train_file train/data/train.jsonl \
    --val_file train/data/val.jsonl \
    --output_dir outputs/gtb-qwen7b-qlora \
    --bf16 \
    --save_merged_16bit
