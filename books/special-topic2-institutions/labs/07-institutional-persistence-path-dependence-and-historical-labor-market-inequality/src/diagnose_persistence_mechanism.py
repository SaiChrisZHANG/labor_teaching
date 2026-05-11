from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


TYPE_LABELS = {
    "institutional_persistence_labor_channel": "institutional persistence through a concrete labor-market mechanism",
    "persistent_fundamentals": "serial correlation or persistence in fundamentals",
    "path_dependence": "path dependence through dynamic increasing returns or lock-in",
    "overclaimed_persistence": "overclaimed persistence because the labor mechanism is not specified",
}

TYPE_DIAGNOSTICS = {
    "institutional_persistence_labor_channel": "Ask whether the historical institution changed the named labor channel and whether fundamentals are addressed.",
    "persistent_fundamentals": "Treat the persistent condition as the object rather than as institutional persistence.",
    "path_dependence": "Look for evidence of increasing returns, networks, sunk costs, or organizational lock-in.",
    "overclaimed_persistence": "Require a labor mechanism before interpreting the historical exposure as institutional persistence.",
}

RISK_LABELS = {
    "low": "low overclaiming risk",
    "medium": "medium overclaiming risk",
    "high": "high overclaiming risk",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def classify(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    classified: list[dict[str, object]] = []
    type_counts: Counter[str] = Counter()
    risk_counts: Counter[str] = Counter()
    for row in rows:
        claim_type = row["claim_type"]
        risk = row["expected_risk"]
        type_counts[claim_type] += 1
        risk_counts[risk] += 1
        classified.append(
            {
                "claim_id": row["claim_id"],
                "anchor": row["anchor"],
                "historical_treatment": row["historical_treatment"],
                "modern_outcome": row["modern_outcome"],
                "proposed_mechanism": row["proposed_mechanism"],
                "classification": TYPE_LABELS[claim_type],
                "first_labor_margin": row["first_labor_margin"],
                "alternative_fundamental": row["alternative_fundamental"],
                "data_source": row["data_source"],
                "overclaiming_risk": RISK_LABELS[risk],
                "diagnostic_next_step": TYPE_DIAGNOSTICS[claim_type],
            }
        )

    type_rows = [
        {"classification": TYPE_LABELS[key], "claim_count": value}
        for key, value in sorted(type_counts.items())
    ]
    risk_rows = [
        {"overclaiming_risk": RISK_LABELS[key], "claim_count": value}
        for key, value in sorted(risk_counts.items())
    ]
    return classified, type_rows, risk_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 7 persistence diagnostic note",
                "",
                "Every persistence claim must name the historical treatment, the labor mechanism, and the alternative fundamental.",
                "Use the overclaiming-risk column to decide where a seminar discussion should demand more evidence.",
                "The strongest claims connect historical exposure to a measured mechanism and then to a labor outcome.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    rows = read_rows(args.input)
    classified, type_rows, risk_rows = classify(rows)
    write_csv(
        args.outdir / "persistence_diagnostic.csv",
        [
            "claim_id",
            "anchor",
            "historical_treatment",
            "modern_outcome",
            "proposed_mechanism",
            "classification",
            "first_labor_margin",
            "alternative_fundamental",
            "data_source",
            "overclaiming_risk",
            "diagnostic_next_step",
        ],
        classified,
    )
    write_csv(args.outdir / "claim_type_counts.csv", ["classification", "claim_count"], type_rows)
    write_csv(args.outdir / "risk_level_counts.csv", ["overclaiming_risk", "claim_count"], risk_rows)
    write_note(args.outdir / "diagnostic_note.txt")
    print(f"Wrote Week 7 persistence diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
