from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


ORDER = ["low_family_obligation", "medium_family_obligation", "high_family_obligation"]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def mean(rows: list[dict[str, str]], column: str) -> float:
    return fmean(float(row[column]) for row in rows)


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["origin_norm_group"]].append(row)

    summary = []
    for group in ORDER:
        group_rows = grouped[group]
        summary.append(
            {
                "origin_norm_group": group,
                "workers": len(group_rows),
                "family_obligation_index": round(mean(group_rows, "family_obligation_index"), 3),
                "generalized_trust_index": round(mean(group_rows, "generalized_trust_index"), 3),
                "formal_protection_index": round(mean(group_rows, "formal_protection_index"), 3),
                "local_labor_demand_index": round(mean(group_rows, "local_labor_demand_index"), 3),
                "employment_rate": round(mean(group_rows, "employed"), 3),
                "regional_mobility_rate": round(mean(group_rows, "changed_region_for_work"), 3),
                "female_lfp_rate": round(mean(group_rows, "female_labor_force_participation"), 3),
                "support_for_employment_protection": round(mean(group_rows, "supports_employment_protection"), 3),
            }
        )
    return summary


def variable_map() -> list[dict[str, str]]:
    return [
        {
            "variable": "origin_norm_group",
            "classification": "institutional_object",
            "interpretation": "Inherited informal institution used to group workers by family-obligation norms.",
        },
        {
            "variable": "family_obligation_index",
            "classification": "mechanism",
            "interpretation": "Potential family-insurance and local-obligation channel.",
        },
        {
            "variable": "generalized_trust_index",
            "classification": "mechanism",
            "interpretation": "Potential trust and compliance channel.",
        },
        {
            "variable": "formal_protection_index",
            "classification": "formal_institution_control",
            "interpretation": "Local formal protection environment, not the inherited norm itself.",
        },
        {
            "variable": "employed",
            "classification": "labor_outcome",
            "interpretation": "Employment margin.",
        },
        {
            "variable": "changed_region_for_work",
            "classification": "labor_outcome",
            "interpretation": "Mobility margin.",
        },
        {
            "variable": "supports_employment_protection",
            "classification": "political_labor_outcome",
            "interpretation": "Demand for formal labor regulation.",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    rows = read_rows(Path(args.input))
    summary = summarize(rows)

    write_csv(
        outdir / "norm_group_summary.csv",
        summary,
        [
            "origin_norm_group",
            "workers",
            "family_obligation_index",
            "generalized_trust_index",
            "formal_protection_index",
            "local_labor_demand_index",
            "employment_rate",
            "regional_mobility_rate",
            "female_lfp_rate",
            "support_for_employment_protection",
        ],
    )
    write_csv(
        outdir / "institution_mechanism_outcome_map.csv",
        variable_map(),
        ["variable", "classification", "interpretation"],
    )

    note = (
        "This synthetic factbook links inherited norms to labor outcomes for teaching. "
        "It is descriptive: a causal design would need variation that separates inherited "
        "informal institutions from local labor demand, policy exposure, selection, and prices.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
