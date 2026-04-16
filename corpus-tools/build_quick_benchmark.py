"""Build a representative quick-benchmark sample from the full corpus.

Strategy:
- One record per taxonomy_code in TAXONOMY (182 codes).
- For codes with multiple records, pick a record that diversifies the
  (difficulty_tier, pattern_type) coverage seen so far.
- For codes with multiple records, optionally add a second record from a
  different (tier, pattern_type) cell.
- Skip records missing pattern_type where alternatives exist.
"""
import glob, json, random, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from taxonomy import TAXONOMY

random.seed(42)
ROOT = Path(__file__).parent / "output"

# Collect all corpus records grouped by taxonomy_code
SKIP_PATTERNS = ("benchmark_", "cross_val", "hard_cases", "subagent_", "quick_benchmark")
records_by_code = defaultdict(list)
for f in glob.glob(str(ROOT / "*.jsonl")):
    if any(s in Path(f).name for s in SKIP_PATTERNS):
        continue
    for line in open(f):
        try:
            r = json.loads(line)
        except Exception:
            continue
        tc = r.get("taxonomy_code")
        if not tc or tc not in TAXONOMY:
            continue
        if not r.get("scenario") or not r["scenario"].get("context"):
            continue
        records_by_code[tc].append(r)

valid_codes = sorted(set(TAXONOMY) & set(records_by_code))
print(f"Valid codes with records: {len(valid_codes)} / {len(TAXONOMY)}")
missing = sorted(set(TAXONOMY) - set(records_by_code))
if missing:
    print(f"Missing codes: {missing[:10]}{'...' if len(missing)>10 else ''}")

picked = []
seen_cells = Counter()  # (track, tier, pattern_type) -> count

def cell(r):
    return (r.get("track", "?"), r.get("difficulty_tier", "?"), r.get("pattern_type", "?"))

def cell_score(r):
    """Lower is better — prefer cells we've under-sampled and records with all metadata."""
    c = cell(r)
    score = seen_cells[c]
    if "?" in c:
        score += 100  # heavily penalize missing metadata
    return score

# Pass 1: one record per code, picking record that diversifies cells
for code in valid_codes:
    pool = records_by_code[code]
    pool_sorted = sorted(pool, key=lambda r: (cell_score(r), random.random()))
    chosen = pool_sorted[0]
    picked.append(chosen)
    seen_cells[cell(chosen)] += 1

# Pass 2: for codes with ≥4 records, add a second record from a different cell
for code in valid_codes:
    pool = records_by_code[code]
    if len(pool) < 4:
        continue
    already = {r["id"] for r in picked if r["taxonomy_code"] == code}
    used_cells = {cell(r) for r in picked if r["taxonomy_code"] == code}
    candidates = [r for r in pool if r["id"] not in already and cell(r) not in used_cells]
    if not candidates:
        continue
    candidates_sorted = sorted(candidates, key=lambda r: (cell_score(r), random.random()))
    chosen = candidates_sorted[0]
    picked.append(chosen)
    seen_cells[cell(chosen)] += 1

# Output
out_path = ROOT / "quick_benchmark_set.jsonl"
with open(out_path, "w") as f:
    for r in picked:
        f.write(json.dumps(r) + "\n")

print(f"\nWrote {len(picked)} records to {out_path}")

# Coverage stats
codes_covered = Counter(r["taxonomy_code"] for r in picked)
print(f"Codes covered: {len(codes_covered)} / {len(TAXONOMY)}")
print(f"  1 record: {sum(1 for c,n in codes_covered.items() if n==1)}")
print(f"  2 records: {sum(1 for c,n in codes_covered.items() if n==2)}")
print(f"\nBy track:    {dict(Counter(r.get('track','?') for r in picked))}")
print(f"By tier:     {dict(Counter(r.get('difficulty_tier','?') for r in picked))}")
print(f"By pattern:  {dict(Counter(r.get('pattern_type','?') for r in picked))}")
