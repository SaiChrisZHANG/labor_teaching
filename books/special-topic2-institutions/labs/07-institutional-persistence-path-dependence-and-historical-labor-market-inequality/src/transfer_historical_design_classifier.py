from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


DESIGN_LABELS = {
    "historical_border_discontinuity": "historical border or geographic discontinuity",
    "archival_legal_contract_records": "archival legal or contract-record design",
    "regime_abolition_reform": "regime abolition, liberalization, or institutional reform",
    "war_conflict_political_shock": "war, conflict, occupation, or abrupt political shock",
    "linked_historical_microdata": "linked historical census or archival microdata",
    "spatial_historical_gis": "spatial and historical GIS design",
    "lineage_ancestry_share_proxy": "lineage, ancestry, or historical exposure proxy",
}

CAUTIONS = {
    "historical_border_discontinuity": "Check that the boundary does not simply proxy geography or later administration.",
    "archival_legal_contract_records": "Records are mechanism-rich but may have selective survival and limited external validity.",
    "regime_abolition_reform": "Reforms usually bundle legal, fiscal, political, and market changes.",
    "war_conflict_political_shock": "War shocks bundle demand, destruction, migration, discrimination, and politics.",
    "linked_historical_microdata": "Linkage, survival, and name-matching biases can change the estimand.",
    "spatial_historical_gis": "Georeferencing error, spatial correlation, and modern sorting need explicit handling.",
    "lineage_ancestry_share_proxy": "The proxy may mix culture, institutions, selection, and current networks.",
}

IDENTIFIES = {
    "historical_border_discontinuity": "local effects of historical exposure near an institutional boundary",
    "archival_legal_contract_records": "effects of enforcement and contract institutions on labor-market behavior",
    "regime_abolition_reform": "effects of institutional removal or expansion on labor allocation",
    "war_conflict_political_shock": "labor reallocation from abrupt political or military shocks",
    "linked_historical_microdata": "individual, household, or intergenerational labor trajectories",
    "spatial_historical_gis": "spatial channels through access, public goods, land, or migration",
    "lineage_ancestry_share_proxy": "persistence through group, family, or community transmission when used carefully",
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


def classify(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    classified: list[dict[str, object]] = []
    counts: Counter[str] = Counter()
    for row in rows:
        family = row["design_family"]
        counts[family] += 1
        classified.append(
            {
                "design_id": row["design_id"],
                "anchor": row["anchor"],
                "design_family": DESIGN_LABELS[family],
                "historical_variation": row["historical_variation"],
                "labor_mechanism": row["labor_mechanism"],
                "data_source": row["data_source"],
                "observed_margin": row["observed_margin"],
                "identifies": IDENTIFIES[family],
                "main_caution": CAUTIONS[family],
            }
        )
    count_rows = [
        {"design_family": DESIGN_LABELS[key], "design_count": value}
        for key, value in sorted(counts.items())
    ]
    return classified, count_rows


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 7 transfer note",
                "",
                "Historical labor designs differ in what they identify.",
                "Before interpreting persistence, name the labor mechanism and the main data limitation.",
                "A design can be historically clever and still weak for labor economics if the worker or firm margin is vague.",
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
    classified, count_rows = classify(rows)
    write_csv(
        args.outdir / "design_classification.csv",
        [
            "design_id",
            "anchor",
            "design_family",
            "historical_variation",
            "labor_mechanism",
            "data_source",
            "observed_margin",
            "identifies",
            "main_caution",
        ],
        classified,
    )
    write_csv(args.outdir / "design_family_counts.csv", ["design_family", "design_count"], count_rows)
    write_note(args.outdir / "transfer_note.txt")
    print(f"Wrote Week 7 transfer classifications to {args.outdir}")


if __name__ == "__main__":
    main()
