"""
Pydantic models for the Good Thinking Bot training corpus.

Each training example is a CorpusRecord — a self-contained unit that captures
a reasoning pattern (good or bad), a scenario illustrating it, structural
analysis, assessment scaffolding, and game hooks for NPC integration.
"""

from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


# ─── Enums ────────────────────────────────────────────────────────────────────


class Track(str, Enum):
    LOGIC_CRITICAL_THINKING = "logic_critical_thinking"
    DECISION_THEORY = "decision_theory"
    GAME_THEORY = "game_theory"
    MICROECONOMICS = "microeconomics"
    DENNETT_TOOLS = "dennett_tools"
    COGNITIVE_BIASES = "cognitive_biases"


class PatternType(str, Enum):
    GOOD_TOOL = "good_tool"
    BAD_THINKING = "bad_thinking"
    DUAL = "dual"


class DifficultyTier(str, Enum):
    DRILL = "drill"
    WHAT_IF = "what_if"
    PUZZLE = "puzzle"


class SourceType(str, Enum):
    HAND_CRAFTED = "hand_crafted"
    EXISTING_DATASET = "existing_dataset"
    SYNTHETIC_VERIFIED = "synthetic_verified"


# ─── Nested models ────────────────────────────────────────────────────────────


class Scenario(BaseModel):
    """The situation presented to the learner."""

    context: str = Field(
        description="Setting or situation description"
    )
    text: str = Field(
        description="The actual argument, reasoning, or decision to analyze"
    )
    speaker_context: Optional[str] = Field(
        default=None,
        description="NPC identity for game integration"
    )


class Structure(BaseModel):
    """Analytical breakdown of the reasoning pattern."""

    pattern_name: str = Field(
        description="Specific variant name, e.g. 'Ad hominem (circumstantial)'"
    )
    pattern_description: str = Field(
        description="What is happening and why it matters"
    )
    formal_form: Optional[str] = Field(
        default=None,
        description="Schematic or formal representation if applicable"
    )
    why_wrong: Optional[str] = Field(
        default=None,
        description="Explanation of the error (for bad_thinking patterns)"
    )
    why_right: Optional[str] = Field(
        default=None,
        description="Explanation of correctness (for good_tool patterns)"
    )
    related_patterns: list[str] = Field(
        default_factory=list,
        description="Taxonomy codes of related patterns"
    )
    counterpoint: Optional[str] = Field(
        default=None,
        description="Edge case, exception, or nuance"
    )


class RubricLevel(BaseModel):
    """One level in the assessment rubric."""

    level: int = Field(ge=0, le=4)
    description: str


class Assessment(BaseModel):
    """Scaffolding for stealth assessment via NPC dialogue."""

    identification_prompt: str = Field(
        description="Question to probe whether the learner recognizes the pattern"
    )
    rubric: list[RubricLevel] = Field(
        description="0-4 scale rubric for evaluating understanding"
    )
    follow_up_if_wrong: str = Field(
        description="Socratic redirect if the learner misidentifies the pattern"
    )
    follow_up_if_right: str = Field(
        description="Deepening question if the learner correctly identifies it"
    )


class GameHooks(BaseModel):
    """Integration points for the game engine."""

    npc_personality: str = Field(
        description="Character sketch for the NPC who embodies this pattern"
    )
    npc_dialogue_seed: str = Field(
        description="Opening line or conversational hook"
    )
    resolution_path: str = Field(
        description="What happens when the player successfully engages"
    )


class Source(BaseModel):
    """Provenance tracking."""

    type: SourceType
    source_material: str = Field(
        description="Reference to origin (dataset name, lecture note, etc.)"
    )
    original_id: Optional[str] = Field(
        default=None,
        description="ID in the original dataset, if adapted"
    )


# ─── Main record ──────────────────────────────────────────────────────────────


class CorpusRecord(BaseModel):
    """A single training example in the Good Thinking Bot corpus."""

    id: str = Field(
        description="Unique ID: {taxonomy_code}-{sequence}, e.g. 'A7.1-042'"
    )
    taxonomy_code: str = Field(
        description="Code from the taxonomy, e.g. 'A7.1'"
    )
    taxonomy_label: str = Field(
        description="Human-readable label, e.g. 'Ad hominem'"
    )
    track: Track
    pattern_type: PatternType
    difficulty_tier: DifficultyTier

    scenario: Scenario
    structure: Structure
    assessment: Assessment
    game_hooks: GameHooks
    source: Source

    def to_jsonl_line(self) -> str:
        """Serialize to a single JSON line for JSONL output."""
        return self.model_dump_json()

    @classmethod
    def from_jsonl_line(cls, line: str) -> CorpusRecord:
        """Deserialize from a single JSON line."""
        return cls.model_validate_json(line)


# ─── I/O helpers ──────────────────────────────────────────────────────────────


def write_corpus(records: list[CorpusRecord], path: Path) -> None:
    """Write a list of corpus records to a JSONL file."""
    with open(path, "w") as f:
        for record in records:
            f.write(record.to_jsonl_line() + "\n")


def read_corpus(path: Path) -> list[CorpusRecord]:
    """Read a JSONL file into a list of corpus records."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(CorpusRecord.from_jsonl_line(line))
    return records


def load_all_corpus(output_dir: Path | None = None) -> list[CorpusRecord]:
    """Load all JSONL files from the output directory."""
    from config import CORPUS_OUTPUT_DIR

    directory = output_dir or CORPUS_OUTPUT_DIR
    records = []
    for jsonl_file in sorted(directory.glob("*.jsonl")):
        records.extend(read_corpus(jsonl_file))
    return records
