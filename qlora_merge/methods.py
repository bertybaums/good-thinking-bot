"""
QLoRA / LoRA adapter merging methods.

All methods operate on the full-precision A/B matrices — quantization of the
base model is irrelevant here, which is why merging is clean.

Methods implemented
-------------------
1. linear_merge         – Weighted average of ΔW matrices (LoRA soup)
2. task_arithmetic      – Signed addition / subtraction of deltas
3. ties_merge           – Trim + elect sign + disjoint merge
4. dare_merge           – Drop & rescale before any of the above
5. dynamic_merge        – Input-conditioned weighting (simple router PoC)

Each method returns a (d, k) numpy array representing the combined ΔW.
A thin `MergedAdapter` wrapper is returned so callers get a consistent
interface regardless of which method was used.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass
from typing import Sequence, Optional

from .adapter import LoRAAdapter


# ---------------------------------------------------------------------------
# Result wrapper
# ---------------------------------------------------------------------------


@dataclass
class MergedAdapter:
    """Holds the combined weight delta and metadata about how it was produced."""

    method: str
    delta_W: np.ndarray          # shape (d, k)
    source_names: list[str]
    weights_used: Optional[np.ndarray] = None  # per-adapter scalar weights

    def apply_to(self, W: np.ndarray) -> np.ndarray:
        """Add ΔW onto a base weight matrix W (both must be (d, k))."""
        if W.shape != self.delta_W.shape:
            raise ValueError(f"Shape mismatch: W {W.shape} vs ΔW {self.delta_W.shape}")
        return W + self.delta_W


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _validate_compatible(adapters: Sequence[LoRAAdapter]) -> None:
    """Raise if adapters have mismatched (d, k) shapes."""
    shapes = {(a.d, a.k) for a in adapters}
    if len(shapes) > 1:
        raise ValueError(
            f"Adapters have incompatible output shapes: {shapes}. "
            "All adapters must have the same (d, k)."
        )


def _uniform_weights(n: int) -> np.ndarray:
    return np.ones(n, dtype=np.float32) / n


# ---------------------------------------------------------------------------
# 1. Linear merge (LoRA soup)
# ---------------------------------------------------------------------------


def linear_merge(
    adapters: Sequence[LoRAAdapter],
    weights: Optional[Sequence[float]] = None,
) -> MergedAdapter:
    """
    ΔW_combined = Σ αᵢ · ΔWᵢ

    Parameters
    ----------
    adapters : list of LoRAAdapter
    weights : optional per-adapter scalars αᵢ (will be normalised to sum=1).
              Defaults to uniform.
    """
    _validate_compatible(adapters)
    w = np.array(weights, dtype=np.float32) if weights else _uniform_weights(len(adapters))
    w = w / w.sum()

    combined = sum(w[i] * adapters[i].delta() for i in range(len(adapters)))
    return MergedAdapter(
        method="linear",
        delta_W=combined,
        source_names=[a.name for a in adapters],
        weights_used=w,
    )


# ---------------------------------------------------------------------------
# 2. Task arithmetic
# ---------------------------------------------------------------------------


def task_arithmetic(
    adapters: Sequence[LoRAAdapter],
    weights: Optional[Sequence[float]] = None,
) -> MergedAdapter:
    """
    Same arithmetic as linear_merge but weights can be negative (subtract tasks)
    and are NOT normalised — the caller controls magnitude directly.

    Example: weights=[1.0, 1.0, -0.5] adds two adapters and subtracts a third.
    """
    _validate_compatible(adapters)
    w = np.array(weights, dtype=np.float32) if weights else np.ones(len(adapters), dtype=np.float32)

    combined = sum(w[i] * adapters[i].delta() for i in range(len(adapters)))
    return MergedAdapter(
        method="task_arithmetic",
        delta_W=combined,
        source_names=[a.name for a in adapters],
        weights_used=w,
    )


# ---------------------------------------------------------------------------
# 3. TIES-Merging
# ---------------------------------------------------------------------------


def ties_merge(
    adapters: Sequence[LoRAAdapter],
    weights: Optional[Sequence[float]] = None,
    trim_fraction: float = 0.2,
) -> MergedAdapter:
    """
    Trim-Elect-Disjoint merging (Yadav et al., 2023).

    Steps
    -----
    1. Trim  — zero out the bottom `trim_fraction` of parameters by magnitude
               in each adapter's ΔW (likely-noise parameters).
    2. Elect — for each parameter position, take a majority vote across adapters
               to elect a consensus sign.
    3. Disjoint merge — average only the parameters that match the elected sign.

    Parameters
    ----------
    trim_fraction : float in [0, 1)
        Fraction of small-magnitude parameters to zero before voting.
    """
    _validate_compatible(adapters)
    w = np.array(weights, dtype=np.float32) if weights else _uniform_weights(len(adapters))
    w = w / w.sum()

    deltas = [a.delta() for a in adapters]
    shape = deltas[0].shape

    # Step 1: Trim
    trimmed = []
    for delta in deltas:
        flat = delta.ravel()
        threshold = np.quantile(np.abs(flat), trim_fraction)
        t = delta.copy()
        t[np.abs(t) < threshold] = 0.0
        trimmed.append(t)

    # Step 2: Elect sign via weighted majority vote
    sign_votes = sum(w[i] * np.sign(trimmed[i]) for i in range(len(trimmed)))
    elected_sign = np.sign(sign_votes)  # -1, 0, or +1

    # Step 3: Disjoint merge — average params that agree with elected sign
    combined = np.zeros(shape, dtype=np.float32)
    weight_sum = np.zeros(shape, dtype=np.float32)

    for i, t in enumerate(trimmed):
        agree_mask = np.sign(t) == elected_sign
        combined += w[i] * t * agree_mask
        weight_sum += w[i] * agree_mask

    # Normalise where we have any votes; leave zero where all abstained
    nonzero = weight_sum > 0
    combined[nonzero] /= weight_sum[nonzero]

    return MergedAdapter(
        method="ties",
        delta_W=combined,
        source_names=[a.name for a in adapters],
        weights_used=w,
    )


# ---------------------------------------------------------------------------
# 4. DARE (Drop and REscale)
# ---------------------------------------------------------------------------


def dare_merge(
    adapters: Sequence[LoRAAdapter],
    drop_fraction: float = 0.9,
    base_method: str = "linear",
    weights: Optional[Sequence[float]] = None,
    seed: Optional[int] = None,
    **method_kwargs,
) -> MergedAdapter:
    """
    Drop & Rescale preprocessing (Yu et al., 2023) followed by any merge method.

    Each adapter's ΔW has `drop_fraction` of its parameters randomly zeroed,
    then the survivors are rescaled by 1/(1 - drop_fraction) to preserve the
    expected magnitude.  The resulting sparse adapters are then merged with
    `base_method` ("linear" or "ties").
    """
    _validate_compatible(adapters)
    rng = np.random.default_rng(seed)
    keep_prob = 1.0 - drop_fraction

    sparse_adapters = []
    for a in adapters:
        delta = a.delta()
        mask = rng.random(delta.shape).astype(np.float32) < keep_prob
        sparse_delta = delta * mask / keep_prob  # rescale survivors
        # Wrap in a pseudo-adapter: set A=sparse_delta, B=identity proxy
        # (delta() just returns A @ B, so we store in A and use rank-1 B)
        d, k = sparse_delta.shape
        # Represent sparse_delta as a LoRAAdapter with effective rank = min(d,k)
        # For the PoC we store it flat: A=sparse_delta, B=I_{k}
        sparse = LoRAAdapter(
            name=a.name + "_dare",
            A=sparse_delta,
            B=np.eye(k, dtype=np.float32),
            scale=1.0,
        )
        sparse_adapters.append(sparse)

    if base_method == "ties":
        result = ties_merge(sparse_adapters, weights=weights, **method_kwargs)
    else:
        result = linear_merge(sparse_adapters, weights=weights)

    result.method = f"dare+{base_method}"
    result.source_names = [a.name for a in adapters]
    return result


# ---------------------------------------------------------------------------
# 5. Dynamic / conditional weighting
# ---------------------------------------------------------------------------


class SimpleRouter:
    """
    Lightweight router that maps an input feature vector to per-adapter weights.

    In production this would be a trained MLP or attention module.  Here it's
    a random projection + softmax so the PoC is runnable without any training.
    Replace `score` with a real forward pass to upgrade.
    """

    def __init__(self, n_adapters: int, feature_dim: int = 64, seed: int = 0):
        rng = np.random.default_rng(seed)
        self.W = rng.normal(0, 0.1, size=(n_adapters, feature_dim)).astype(np.float32)

    def score(self, feature: np.ndarray) -> np.ndarray:
        """Return softmax weights over adapters given an input feature vector."""
        logits = self.W @ feature.astype(np.float32)
        logits -= logits.max()
        exp = np.exp(logits)
        return exp / exp.sum()


def dynamic_merge(
    adapters: Sequence[LoRAAdapter],
    input_feature: np.ndarray,
    router: Optional[SimpleRouter] = None,
) -> MergedAdapter:
    """
    Input-conditioned merging: weights = softmax(router(input_feature)).

    Parameters
    ----------
    input_feature : 1-D array
        A vector representing the current context (e.g. last-hidden-state mean,
        task embedding, user profile vector, etc.)
    router : SimpleRouter (or compatible object with a `score` method).
             If None, a random router is created.
    """
    _validate_compatible(adapters)
    if router is None:
        router = SimpleRouter(n_adapters=len(adapters), feature_dim=len(input_feature))

    w = router.score(input_feature)
    combined = sum(w[i] * adapters[i].delta() for i in range(len(adapters)))

    return MergedAdapter(
        method="dynamic",
        delta_W=combined,
        source_names=[a.name for a in adapters],
        weights_used=w,
    )
