"""
LoRA adapter representation.

LoRAAdapter wraps the two low-rank matrices A (d×r) and B (r×k) that define a
LoRA update ΔW = A @ B.  Fake matrices are used here; swap `from_peft` for
real adapters once you have trained checkpoints.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LoRAAdapter:
    """
    A single LoRA adapter: ΔW = A @ B, shape (d, k).

    Attributes
    ----------
    name : str
        Human-readable label (e.g. "logic", "decision_theory").
    A : np.ndarray
        Left factor, shape (d, r).
    B : np.ndarray
        Right factor, shape (r, k).
    scale : float
        Scalar applied at inference (α / r in the original paper). Preserved
        separately so merging methods can manipulate it without touching A/B.
    """

    name: str
    A: np.ndarray
    B: np.ndarray
    scale: float = 1.0

    # ------------------------------------------------------------------
    # Core properties
    # ------------------------------------------------------------------

    @property
    def rank(self) -> int:
        return self.A.shape[1]

    @property
    def d(self) -> int:
        return self.A.shape[0]

    @property
    def k(self) -> int:
        return self.B.shape[1]

    def delta(self) -> np.ndarray:
        """Return the full weight-delta matrix ΔW = scale * A @ B."""
        return self.scale * (self.A @ self.B)

    # ------------------------------------------------------------------
    # Construction helpers
    # ------------------------------------------------------------------

    @classmethod
    def random(
        cls,
        name: str,
        d: int,
        k: int,
        rank: int = 4,
        scale: float = 1.0,
        seed: Optional[int] = None,
        std: float = 0.02,
    ) -> "LoRAAdapter":
        """Create a synthetic adapter with random Gaussian A, zero B (HF default init)."""
        rng = np.random.default_rng(seed)
        A = rng.normal(0, std, size=(d, rank)).astype(np.float32)
        B = np.zeros((rank, k), dtype=np.float32)
        return cls(name=name, A=A, B=B, scale=scale)

    @classmethod
    def from_peft(cls, name: str, peft_layer) -> "LoRAAdapter":
        """
        Construct from a live PEFT LoraLayer.

        Usage (once you have real checkpoints)::

            from peft import PeftModel
            model = PeftModel.from_pretrained(base, adapter_path)
            layer = model.base_model.model.layers[0].self_attn.q_proj
            adapter = LoRAAdapter.from_peft("my_adapter", layer)
        """
        A = layer.lora_A.default.weight.detach().float().cpu().numpy().T  # (d, r)
        B = layer.lora_B.default.weight.detach().float().cpu().numpy().T  # (r, k)
        scale = layer.scaling.get("default", 1.0)
        return cls(name=name, A=A, B=B, scale=float(scale))

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"LoRAAdapter(name={self.name!r}, shape=({self.d},{self.k}), "
            f"rank={self.rank}, scale={self.scale})"
        )
