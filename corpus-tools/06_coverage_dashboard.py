#!/usr/bin/env python3
"""
Pipeline 6: Coverage Dashboard (reporting, local)

Pure Python. Reads all corpus JSONL files and generates a coverage report:
- Matrix of taxonomy_code x difficulty_tier x domain
- Highlights gaps (zero examples, single-tier-only codes)
- Outputs both terminal report and HTML dashboard

Usage:
    python 06_coverage_dashboard.py              # Terminal report
    python 06_coverage_dashboard.py --html        # Generate HTML dashboard
    python 06_coverage_dashboard.py --gaps-only   # Show only gaps
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path

from config import CORPUS_OUTPUT_DIR
from schema import CorpusRecord, read_corpus
from taxonomy import TAXONOMY, summary as taxonomy_summary


def load_all_records() -> list[CorpusRecord]:
    """Load all corpus JSONL files."""
    records = []
    for jsonl_file in sorted(CORPUS_OUTPUT_DIR.glob("*.jsonl")):
        if jsonl_file.name.startswith("flagged_"):
            continue
        try:
            records.extend(read_corpus(jsonl_file))
        except Exception as e:
            print(f"Warning: Could not read {jsonl_file}: {e}")
    return records


def build_coverage_matrix(
    records: list[CorpusRecord],
) -> dict[str, dict[str, int]]:
    """Build coverage matrix: code -> {drill: N, what_if: N, puzzle: N, total: N}."""
    matrix: dict[str, dict[str, int]] = {}

    # Initialize with all taxonomy codes
    for code in TAXONOMY:
        matrix[code] = {"drill": 0, "what_if": 0, "puzzle": 0, "total": 0}

    # Count records
    for record in records:
        code = record.taxonomy_code
        tier = record.difficulty_tier.value
        if code in matrix:
            matrix[code][tier] += 1
            matrix[code]["total"] += 1

    return matrix


def build_source_breakdown(
    records: list[CorpusRecord],
) -> dict[str, dict[str, int]]:
    """Count records by source type."""
    breakdown: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for record in records:
        code = record.taxonomy_code
        source = record.source.type.value
        breakdown[code][source] += 1
    return dict(breakdown)


def find_gaps(matrix: dict[str, dict[str, int]]) -> list[dict]:
    """Find taxonomy codes with coverage issues."""
    gaps = []
    for code, counts in matrix.items():
        entry = TAXONOMY[code]
        issues = []

        if counts["total"] == 0:
            issues.append("NO EXAMPLES")
        else:
            missing_tiers = [t for t in ("drill", "what_if", "puzzle") if counts[t] == 0]
            if missing_tiers:
                issues.append(f"Missing tiers: {', '.join(missing_tiers)}")
            if counts["total"] < 3:
                issues.append(f"Low count: {counts['total']}")

        if issues:
            gaps.append({
                "code": code,
                "label": entry["label"],
                "track": entry["track"],
                "pattern_type": entry["pattern_type"],
                "counts": counts,
                "issues": issues,
            })

    return gaps


def terminal_report(
    matrix: dict[str, dict[str, int]],
    gaps: list[dict],
    records: list[CorpusRecord],
    gaps_only: bool = False,
) -> None:
    """Print terminal coverage report."""
    print(f"\n{'='*80}")
    print("COVERAGE DASHBOARD")
    print(f"{'='*80}")

    # Summary
    total_records = len(records)
    total_codes = len(TAXONOMY)
    covered_codes = sum(1 for c in matrix.values() if c["total"] > 0)

    print(f"\nTotal records: {total_records}")
    print(f"Taxonomy codes: {covered_codes}/{total_codes} covered "
          f"({covered_codes/total_codes:.0%})")

    # Track summary
    print(f"\n{'Track':<30} {'Codes':>6} {'Covered':>8} {'Records':>8}")
    print("-" * 55)
    track_totals = taxonomy_summary()
    for track, code_count in track_totals.items():
        track_covered = sum(
            1 for code, counts in matrix.items()
            if TAXONOMY[code]["track"] == track and counts["total"] > 0
        )
        track_records = sum(
            counts["total"] for code, counts in matrix.items()
            if TAXONOMY[code]["track"] == track
        )
        print(f"{track:<30} {code_count:>6} {track_covered:>8} {track_records:>8}")

    # Source breakdown
    source_counts: dict[str, int] = defaultdict(int)
    for record in records:
        source_counts[record.source.type.value] += 1
    print(f"\nBy source type:")
    for source, count in sorted(source_counts.items()):
        print(f"  {source}: {count}")

    if not gaps_only:
        # Full matrix
        print(f"\n{'Code':<8} {'Label':<35} {'Type':<12} {'Drill':>6} {'WI':>6} {'Puz':>6} {'Tot':>6}")
        print("-" * 85)

        current_track = None
        for code in sorted(TAXONOMY.keys()):
            entry = TAXONOMY[code]
            counts = matrix[code]

            # Track header
            if entry["track"] != current_track:
                current_track = entry["track"]
                print(f"\n  --- {current_track} ---")

            # Highlight gaps
            marker = ""
            if counts["total"] == 0:
                marker = " !!!"
            elif any(counts[t] == 0 for t in ("drill", "what_if", "puzzle")):
                marker = " !"

            print(
                f"{code:<8} {entry['label']:<35} {entry['pattern_type']:<12} "
                f"{counts['drill']:>6} {counts['what_if']:>6} {counts['puzzle']:>6} "
                f"{counts['total']:>6}{marker}"
            )

    # Gaps
    if gaps:
        print(f"\n{'='*60}")
        print(f"GAPS ({len(gaps)} codes with issues)")
        print(f"{'='*60}")
        for gap in gaps:
            issues_str = "; ".join(gap["issues"])
            print(f"  {gap['code']}: {gap['label']} — {issues_str}")
    else:
        print("\nNo coverage gaps found!")


def generate_html(
    matrix: dict[str, dict[str, int]],
    gaps: list[dict],
    records: list[CorpusRecord],
) -> str:
    """Generate an HTML coverage dashboard."""
    total = len(records)
    covered = sum(1 for c in matrix.values() if c["total"] > 0)
    total_codes = len(TAXONOMY)

    rows = []
    for code in sorted(TAXONOMY.keys()):
        entry = TAXONOMY[code]
        counts = matrix[code]
        row_class = "gap" if counts["total"] == 0 else "partial" if any(counts[t] == 0 for t in ("drill", "what_if", "puzzle")) else "ok"
        rows.append(f"""
        <tr class="{row_class}">
            <td>{code}</td>
            <td>{entry['label']}</td>
            <td>{entry['track']}</td>
            <td>{entry['pattern_type']}</td>
            <td>{counts['drill']}</td>
            <td>{counts['what_if']}</td>
            <td>{counts['puzzle']}</td>
            <td><strong>{counts['total']}</strong></td>
        </tr>""")

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Good Thinking Bot — Coverage Dashboard</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; margin: 2em; background: #fafafa; }}
        h1 {{ color: #333; }}
        .stats {{ display: flex; gap: 2em; margin: 1em 0; }}
        .stat {{ background: white; padding: 1em 2em; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        .stat .num {{ font-size: 2em; font-weight: bold; color: #2563eb; }}
        table {{ border-collapse: collapse; width: 100%; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        th {{ background: #1e293b; color: white; padding: 0.75em 1em; text-align: left; }}
        td {{ padding: 0.5em 1em; border-bottom: 1px solid #e2e8f0; }}
        tr.gap {{ background: #fef2f2; }}
        tr.gap td {{ color: #991b1b; }}
        tr.partial {{ background: #fffbeb; }}
        tr.ok {{ background: white; }}
        tr:hover {{ background: #f1f5f9 !important; }}
    </style>
</head>
<body>
    <h1>Good Thinking Bot — Coverage Dashboard</h1>

    <div class="stats">
        <div class="stat"><div class="num">{total}</div>Total Records</div>
        <div class="stat"><div class="num">{covered}/{total_codes}</div>Codes Covered</div>
        <div class="stat"><div class="num">{covered/total_codes:.0%}</div>Coverage</div>
        <div class="stat"><div class="num">{len(gaps)}</div>Gaps</div>
    </div>

    <h2>Coverage Matrix</h2>
    <p>
        <span style="background:#fef2f2;padding:2px 8px;border-radius:4px">Red = no examples</span>
        <span style="background:#fffbeb;padding:2px 8px;border-radius:4px">Yellow = missing tiers</span>
        <span style="background:white;padding:2px 8px;border-radius:4px;border:1px solid #e2e8f0">White = OK</span>
    </p>
    <table>
        <thead>
            <tr>
                <th>Code</th>
                <th>Label</th>
                <th>Track</th>
                <th>Type</th>
                <th>Drill</th>
                <th>What-If</th>
                <th>Puzzle</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            {''.join(rows)}
        </tbody>
    </table>

    <p style="color:#999;margin-top:2em">Generated by 06_coverage_dashboard.py</p>
</body>
</html>"""

    return html


def main() -> None:
    parser = argparse.ArgumentParser(description="Coverage dashboard")
    parser.add_argument("--html", action="store_true", help="Generate HTML dashboard")
    parser.add_argument("--gaps-only", action="store_true", help="Show only gaps")
    args = parser.parse_args()

    records = load_all_records()
    matrix = build_coverage_matrix(records)
    gaps = find_gaps(matrix)

    if args.html:
        html = generate_html(matrix, gaps, records)
        output_path = CORPUS_OUTPUT_DIR / "coverage_dashboard.html"
        output_path.write_text(html)
        print(f"Dashboard written to {output_path}")
    else:
        terminal_report(matrix, gaps, records, gaps_only=args.gaps_only)


if __name__ == "__main__":
    main()
