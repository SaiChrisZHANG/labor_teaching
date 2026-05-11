from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


GAP_LABELS = {
    "low": "low implementation gap",
    "medium": "medium implementation gap",
    "high": "high implementation gap",
}

RISK_LABELS = {
    "low": "low portability risk",
    "medium": "medium portability risk",
    "high": "high portability risk",
}

DOMAIN_DIAGNOSTICS = {
    "labor_regulation_index": "Add enforcement, coverage, and informality measures before making welfare claims.",
    "migration_regime": "Map geography, skill composition, rights, and firm exposure before transporting the estimate.",
    "private_supply_chain_governance": "Separate buyer pressure, audit credibility, management practices, and worker voice.",
    "informality_regime": "Distinguish registration, payroll formality, worker protection, and state reach.",
    "integration_regime": "Separate migrant composition from institutions that govern access and recognition.",
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
    gap_counts: Counter[str] = Counter()
    risk_counts: Counter[str] = Counter()
    for row in rows:
        implementation_gap = row["implementation_gap"]
        portability_risk = row["portability_risk"]
        gap_counts[implementation_gap] += 1
        risk_counts[portability_risk] += 1
        classified.append(
            {
                "case_id": row["case_id"],
                "anchor": row["anchor"],
                "comparative_unit": row["comparative_unit"],
                "institutional_domain": row["institutional_domain"],
                "identifying_variation": row["identifying_variation"],
                "observed_margin": row["observed_margin"],
                "implementation_gap": GAP_LABELS[implementation_gap],
                "portability_risk": RISK_LABELS[portability_risk],
                "mechanism_travels": row["mechanism_travels"],
                "estimate_travels": row["estimate_travels"],
                "diagnostic_next_step": DOMAIN_DIAGNOSTICS[row["institutional_domain"]],
            }
        )

    gap_rows = [
        {"implementation_gap": GAP_LABELS[key], "case_count": value}
        for key, value in sorted(gap_counts.items())
    ]
    risk_rows = [
        {"portability_risk": RISK_LABELS[key], "case_count": value}
        for key, value in sorted(risk_counts.items())
    ]
    return classified, gap_rows, risk_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 9 transportability diagnostic note",
                "",
                "Each comparative case names the unit, identifying variation, observed labor margin, and portability risk.",
                "Mechanisms may travel even when point estimates do not.",
                "A high implementation gap means rules-on-paper should not be interpreted as effective labor protection.",
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
    classified, gap_rows, risk_rows = classify(rows)
    write_csv(
        args.outdir / "transportability_diagnostic.csv",
        [
            "case_id",
            "anchor",
            "comparative_unit",
            "institutional_domain",
            "identifying_variation",
            "observed_margin",
            "implementation_gap",
            "portability_risk",
            "mechanism_travels",
            "estimate_travels",
            "diagnostic_next_step",
        ],
        classified,
    )
    write_csv(args.outdir / "implementation_gap_counts.csv", ["implementation_gap", "case_count"], gap_rows)
    write_csv(args.outdir / "portability_risk_counts.csv", ["portability_risk", "case_count"], risk_rows)
    write_note(args.outdir / "diagnostic_note.txt")
    print(f"Wrote Week 9 transportability diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
