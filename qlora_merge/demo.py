"""
QLoRA merging methods — proof of concept demo.

Runs all five methods on three synthetic adapters representing the three
content tracks of Good Thinking Bot:
  - logic        (Logic & Critical Thinking)
  - decision     (Decision Theory & Game Theory)
  - economics    (Microeconomics)

Run:
    python -m qlora_merge.demo
"""

import numpy as np
from . import (
    LoRAAdapter,
    SimpleRouter,
    dare_merge,
    dynamic_merge,
    linear_merge,
    task_arithmetic,
    ties_merge,
)

# ---------------------------------------------------------------------------
# Synthetic adapters
# ---------------------------------------------------------------------------

D, K, RANK = 128, 64, 8  # weight matrix shape and LoRA rank


def make_adapters() -> list[LoRAAdapter]:
    """
    Three adapters with non-trivial B matrices so ΔW = A @ B is interesting.
    Seeds are fixed for reproducibility.
    """
    adapters = []
    for i, name in enumerate(["logic", "decision", "economics"]):
        rng = np.random.default_rng(i)
        A = rng.normal(0, 0.02, size=(D, RANK)).astype(np.float32)
        B = rng.normal(0, 0.02, size=(RANK, K)).astype(np.float32)
        adapters.append(LoRAAdapter(name=name, A=A, B=B, scale=1.0))
    return adapters


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------


def summarise(label: str, delta: np.ndarray) -> None:
    print(
        f"  {label:<22}  shape={delta.shape}  "
        f"mean={delta.mean():.5f}  std={delta.std():.5f}  "
        f"|max|={np.abs(delta).max():.5f}"
    )


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def run() -> None:
    adapters = make_adapters()

    print("=" * 65)
    print("QLoRA Merging PoC — synthetic adapters")
    print(f"  d={D}, k={K}, rank={RANK}")
    print("=" * 65)

    print("\nIndividual adapters:")
    for a in adapters:
        summarise(a.name, a.delta())

    print("\n--- 1. Linear merge (uniform weights) ---")
    r = linear_merge(adapters)
    summarise("combined", r.delta_W)
    print(f"  weights: {r.weights_used}")

    print("\n--- 1b. Linear merge (custom weights) ---")
    r = linear_merge(adapters, weights=[0.5, 0.3, 0.2])
    summarise("combined", r.delta_W)
    print(f"  weights: {r.weights_used}")

    print("\n--- 2. Task arithmetic (subtract economics) ---")
    r = task_arithmetic(adapters, weights=[1.0, 1.0, -0.5])
    summarise("combined", r.delta_W)
    print(f"  weights: {r.weights_used}")

    print("\n--- 3. TIES-Merging (trim=20%) ---")
    r = ties_merge(adapters, trim_fraction=0.2)
    summarise("combined", r.delta_W)
    sparsity = (r.delta_W == 0).mean()
    print(f"  sparsity after elect: {sparsity:.1%}")

    print("\n--- 4. DARE + linear (drop=80%) ---")
    r = dare_merge(adapters, drop_fraction=0.8, base_method="linear", seed=42)
    summarise("combined", r.delta_W)

    print("\n--- 4b. DARE + TIES (drop=80%, trim=20%) ---")
    r = dare_merge(
        adapters, drop_fraction=0.8, base_method="ties", trim_fraction=0.2, seed=42
    )
    summarise("combined", r.delta_W)

    print("\n--- 5. Dynamic merge (random router) ---")
    # Simulate three different input contexts
    rng = np.random.default_rng(99)
    router = SimpleRouter(n_adapters=3, feature_dim=32, seed=7)
    for ctx_label in ["logic-heavy query", "game theory query", "econ query"]:
        feature = rng.normal(size=32).astype(np.float32)
        r = dynamic_merge(adapters, input_feature=feature, router=router)
        w_str = ", ".join(f"{adapters[i].name}={r.weights_used[i]:.3f}" for i in range(3))
        summarise(ctx_label, r.delta_W)
        print(f"    router weights: {w_str}")

    print("\n--- Applying a merged ΔW to a fake base weight matrix ---")
    base_W = np.zeros((D, K), dtype=np.float32)
    merged = linear_merge(adapters)
    updated_W = merged.apply_to(base_W)
    summarise("base_W + ΔW", updated_W)

    print("\nDone.")


if __name__ == "__main__":
    run()
