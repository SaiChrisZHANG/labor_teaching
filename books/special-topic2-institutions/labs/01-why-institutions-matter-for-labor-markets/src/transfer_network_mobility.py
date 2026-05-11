from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


ORDER = ["weak_network_insurance", "middle_network_insurance", "strong_network_insurance"]


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
        grouped[row["network_group"]].append(row)

    summary = []
    for group in ORDER:
        group_rows = grouped[group]
        summary.append(
            {
                "network_group": group,
                "workers": len(group_rows),
                "informal_insurance_index": round(mean(group_rows, "informal_insurance_index"), 3),
                "network_job_share": round(mean(group_rows, "network_job_share"), 3),
                "community_obligation_index": round(mean(group_rows, "community_obligation_index"), 3),
                "urban_wage_offer_ratio": round(mean(group_rows, "urban_wage_offer_ratio"), 3),
                "urban_job_access_index": round(mean(group_rows, "urban_job_access_index"), 3),
                "migration_rate": round(mean(group_rows, "migrated_to_city"), 3),
                "network_job_rate": round(mean(group_rows, "took_network_job"), 3),
            }
        )
    return summary


def decomposition(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    weak = summary[0]
    strong = summary[-1]
    return [
        {
            "comparison": "strong_minus_weak_network_insurance",
            "informal_insurance_gap": round(
                float(strong["informal_insurance_index"]) - float(weak["informal_insurance_index"]), 3
            ),
            "urban_wage_offer_gap": round(
                float(strong["urban_wage_offer_ratio"]) - float(weak["urban_wage_offer_ratio"]), 3
            ),
            "migration_rate_gap": round(float(strong["migration_rate"]) - float(weak["migration_rate"]), 3),
            "network_job_rate_gap": round(float(strong["network_job_rate"]) - float(weak["network_job_rate"]), 3),
        }
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    rows = read_rows(Path(args.input))
    summary = summarize(rows)
    gaps = decomposition(summary)

    write_csv(
        outdir / "network_group_summary.csv",
        summary,
        [
            "network_group",
            "workers",
            "informal_insurance_index",
            "network_job_share",
            "community_obligation_index",
            "urban_wage_offer_ratio",
            "urban_job_access_index",
            "migration_rate",
            "network_job_rate",
        ],
    )
    write_csv(
        outdir / "mobility_gap_decomposition.csv",
        gaps,
        ["comparison", "informal_insurance_gap", "urban_wage_offer_gap", "migration_rate_gap", "network_job_rate_gap"],
    )

    note = (
        "The transfer exercise shows how network insurance can coexist with lower migration "
        "despite urban wage offers. The pattern is a mechanism prompt, not a causal estimate.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
