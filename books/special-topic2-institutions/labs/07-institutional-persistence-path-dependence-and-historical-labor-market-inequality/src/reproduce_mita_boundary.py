from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


NUMERIC_FIELDS = [
    "historical_mita_exposure",
    "near_boundary",
    "distance_to_boundary",
    "altitude_index",
    "ruggedness_index",
    "precolonial_density",
    "public_goods_index",
    "road_access_index",
    "schooling_years",
    "migration_rate",
    "nonfarm_share",
    "wage_index",
    "employer_power_index",
]

OUTCOME_FIELDS = [
    "schooling_years",
    "migration_rate",
    "nonfarm_share",
    "wage_index",
    "employer_power_index",
]

MECHANISM_FIELDS = [
    "public_goods_index",
    "road_access_index",
    "altitude_index",
    "ruggedness_index",
    "precolonial_density",
]


def read_rows(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows: list[dict[str, object]] = list(csv.DictReader(handle))
    for row in rows:
        for field in NUMERIC_FIELDS:
            row[field] = float(row[field])
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def mean(rows: list[dict[str, object]], field: str) -> float:
    if not rows:
        return 0.0
    return round(fmean(float(row[field]) for row in rows), 4)


def summarize(rows: list[dict[str, object]], label: str) -> list[dict[str, object]]:
    grouped: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[int(float(row["historical_mita_exposure"]))].append(row)

    output: list[dict[str, object]] = []
    for exposed in [0, 1]:
        group_rows = grouped[exposed]
        summary: dict[str, object] = {
            "sample": label,
            "historical_mita_exposure": exposed,
            "districts": len(group_rows),
            "mean_distance_to_boundary": mean(group_rows, "distance_to_boundary"),
        }
        for field in OUTCOME_FIELDS:
            summary[field] = mean(group_rows, field)
        output.append(summary)
    return output


def difference_rows(rows: list[dict[str, object]], fields: list[str], label: str) -> list[dict[str, object]]:
    treated = [row for row in rows if int(float(row["historical_mita_exposure"])) == 1]
    control = [row for row in rows if int(float(row["historical_mita_exposure"])) == 0]
    output: list[dict[str, object]] = []
    for field in fields:
        treated_mean = mean(treated, field)
        control_mean = mean(control, field)
        output.append(
            {
                "sample": label,
                "variable": field,
                "treated_mean": treated_mean,
                "control_mean": control_mean,
                "treated_minus_control": round(treated_mean - control_mean, 4),
                "interpretation": interpretation(field),
            }
        )
    return output


def interpretation(field: str) -> str:
    labels = {
        "schooling_years": "human-capital channel and labor-market readiness",
        "migration_rate": "mobility and outside-option channel",
        "nonfarm_share": "occupational structure and market access",
        "wage_index": "modern labor-market outcome",
        "employer_power_index": "bargaining and employer-power channel",
        "public_goods_index": "local public goods mechanism",
        "road_access_index": "market-access mechanism",
        "altitude_index": "persistent fundamental check",
        "ruggedness_index": "persistent fundamental check",
        "precolonial_density": "pre-treatment settlement check",
    }
    return labels[field]


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 7 synthetic Dell-style reproduction note",
                "",
                "This is a pedagogical boundary exercise inspired by Dell 2010.",
                "The output compares formerly exposed and non-exposed districts overall and near the boundary.",
                "Mechanism differences are reported separately from labor outcome differences.",
                "Do not interpret these synthetic differences as an official replication or as proof of persistence without mechanism evidence.",
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
    near_rows = [row for row in rows if int(float(row["near_boundary"])) == 1]
    write_csv(
        args.outdir / "boundary_summary.csv",
        [
            "sample",
            "historical_mita_exposure",
            "districts",
            "mean_distance_to_boundary",
            *OUTCOME_FIELDS,
        ],
        summarize(rows, "all_districts"),
    )
    write_csv(
        args.outdir / "near_boundary_summary.csv",
        [
            "sample",
            "historical_mita_exposure",
            "districts",
            "mean_distance_to_boundary",
            *OUTCOME_FIELDS,
        ],
        summarize(near_rows, "near_boundary"),
    )
    write_csv(
        args.outdir / "mechanism_differences.csv",
        ["sample", "variable", "treated_mean", "control_mean", "treated_minus_control", "interpretation"],
        difference_rows(rows, OUTCOME_FIELDS + MECHANISM_FIELDS, "all_districts")
        + difference_rows(near_rows, OUTCOME_FIELDS + MECHANISM_FIELDS, "near_boundary"),
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 7 boundary outputs to {args.outdir}")


if __name__ == "__main__":
    main()
