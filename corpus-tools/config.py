"""
Configuration for the Good Thinking Bot training corpus pipeline.

API keys and endpoints are read from environment variables.
Set them in a .env file or export them before running pipeline scripts.
"""

import os
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESOURCES_DIR = PROJECT_ROOT / "resources"
CORPUS_OUTPUT_DIR = Path(__file__).resolve().parent / "output"
PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"

# Ensure output directory exists
CORPUS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ─── Source material paths ────────────────────────────────────────────────────

CRITICAL_THINKING_NOTES = RESOURCES_DIR / "Notes for 2010 Critical Thinking.txt"
DECISION_THEORY_NOTES = RESOURCES_DIR / "rationality-and-strategic-interactions"
COGNITIVE_BIASES_POSTER = RESOURCES_DIR / "Poster - Cognitive Biases.pdf"
LOGICAL_FALLACIES_POSTER = RESOURCES_DIR / "Poster - Logical Fallacies.pdf"
DENNETT_THOUGHT_STOPPERS = RESOURCES_DIR / "Dennett - Thought Stoppers.pdf"
DENNETT_MORAL_FIRST_AID = (
    RESOURCES_DIR / "rationality-and-strategic-interactions"
    / "Dennett - The Moral First Aid Manual.pdf"
)
VAN_CLEAVE_LOGIC = RESOURCES_DIR / "Intro to Logic and Critical Thinking v2.0.pdf"
CORE_ECON = RESOURCES_DIR / "the-economy-2-0-microeconomics-epub.epub"

# ─── Anthropic (quality-sensitive work) ───────────────────────────────────────

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

ANTHROPIC_MODELS = {
    "anchor": "claude-opus-4-6",       # Anchor crafting (highest quality)
    "verify": "claude-sonnet-4-6",     # Verification pass (speed + quality)
}

# ─── MindRouter (campus HPC, bulk work) ───────────────────────────────────────

MINDROUTER_BASE_URL = os.environ.get(
    "MINDROUTER_BASE_URL", "https://mindrouter.example.edu/v1"
)
MINDROUTER_API_KEY = os.environ.get("MINDROUTER_API_KEY", "")

MINDROUTER_MODELS = {
    "bulk_gen": "gpt-oss-120b",        # Synthetic generation drafts
    "cross_val": "qwen3.5-400b",       # Classification cross-validation
    "adapt": "qwen3.5-400b",           # Dataset adaptation / enrichment
}

# ─── Rate limiting ────────────────────────────────────────────────────────────

# Max concurrent requests per provider
ANTHROPIC_MAX_CONCURRENT = 5
MINDROUTER_MAX_CONCURRENT = 20

# Retry config
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2.0  # seconds, exponential backoff

# ─── Batch sizes ──────────────────────────────────────────────────────────────

ADAPTATION_BATCH_SIZE = 50       # Records per batch for dataset adaptation
SYNTHETIC_GEN_BATCH_SIZE = 20    # Records per batch for synthetic generation
CROSS_VAL_BATCH_SIZE = 100       # Records per batch for cross-validation

# ─── Quality thresholds ───────────────────────────────────────────────────────

# Cross-validation: flag if LLM classifier disagrees with intended label
CROSS_VAL_AGREEMENT_THRESHOLD = 0.80

# Verification: what fraction of examples must pass mechanical checks
MECHANICAL_VERIFY_PASS_RATE = 0.85

# Bert review: sample rate for non-anchor examples
BERT_REVIEW_SAMPLE_RATE = 0.10
