#!/usr/bin/env python3
"""Reproduce bounded application-gap summaries for Week 9."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


NUMERIC_COLUMNS = [
    "skill_index",
    "care_constraint",
    "search_intensity",
    "risk_tolerance",
    "posted_wage",
    "commute_minutes",
    "flexibility_score",
    "remote_option",
    "firm_premium",
    "gendered_language_score",
    "family_friendly_score",
    "applied",
    "callback",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to synthetic application choice-set CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    required = {"worker_id", "gender", "job_id", "occupation", *NUMERIC_COLUMNS}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return rows


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def f4(value: float) -> str:
    return f"{value:.4f}"


def group_by_gender(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["gender"]].append(row)
    return grouped


def application_gap_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for gender, group in sorted(group_by_gender(rows).items()):
        workers = {row["worker_id"] for row in group}
        applications = [row for row in group if int(row["applied"]) == 1]
        callbacks = [row for row in applications if int(row["callback"]) == 1]
        output.append(
            {
                "gender": gender,
                "workers": len(workers),
                "choice_set_rows": len(group),
                "applications": len(applications),
                "application_rate": f4(len(applications) / len(group)),
                "mean_applications_per_worker": f4(len(applications) / len(workers)),
                "callback_rate_among_applications": f4(len(callbacks) / len(applications) if applications else 0.0),
                "share_applications_high_wage": f4(
                    mean([float(row["posted_wage"]) >= 40.0 for row in applications])
                ),
                "share_applications_high_premium": f4(
                    mean([float(row["firm_premium"]) >= 0.50 for row in applications])
                ),
                "mean_applied_wage": f4(mean([float(row["posted_wage"]) for row in applications])),
                "mean_applied_commute": f4(mean([float(row["commute_minutes"]) for row in applications])),
                "mean_applied_flexibility": f4(mean([float(row["flexibility_score"]) for row in applications])),
                "mean_applied_gendered_language": f4(
                    mean([float(row["gendered_language_score"]) for row in applications])
                ),
                "mean_worker_care_constraint": f4(mean([float(row["care_constraint"]) for row in group])),
                "mean_worker_search_intensity": f4(mean([float(row["search_intensity"]) for row in group])),
            }
        )
    return output


def occupation_summary(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    occupations = sorted({row["occupation"] for row in rows})
    output: list[dict[str, object]] = []
    gender_groups = group_by_gender(rows)
    apps_by_gender = {
        gender: [row for row in group if int(row["applied"]) == 1] for gender, group in gender_groups.items()
    }

    for occupation in occupations:
        row_out: dict[str, object] = {"occupation": occupation}
        for gender in ["woman", "man"]:
            group = [row for row in gender_groups.get(gender, []) if row["occupation"] == occupation]
            apps = [row for row in group if int(row["applied"]) == 1]
            all_apps = apps_by_gender.get(gender, [])
            row_out[f"{gender}_application_rate"] = f4(len(apps) / len(group) if group else 0.0)
            row_out[f"{gender}_share_of_applications"] = f4(len(apps) / len(all_apps) if all_apps else 0.0)
            row_out[f"{gender}_mean_applied_firm_premium"] = f4(
                mean([float(item["firm_premium"]) for item in apps])
            )
            row_out[f"{gender}_mean_applied_wage"] = f4(mean([float(item["posted_wage"]) for item in apps]))
        row_out["application_rate_gap_man_minus_woman"] = f4(
            float(row_out["man_application_rate"]) - float(row_out["woman_application_rate"])
        )
        output.append(row_out)
    return output


def application_quality_decomposition(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    applications = [row for row in rows if int(row["applied"]) == 1]
    if not applications:
        raise ValueError("No applications found; cannot decompose application quality.")

    occupations = sorted({row["occupation"] for row in applications})
    apps = {
        gender: [row for row in applications if row["gender"] == gender] for gender in ["man", "woman"]
    }
    mean_premium = {
        gender: mean([float(row["firm_premium"]) for row in gender_rows])
        for gender, gender_rows in apps.items()
    }
    shares: dict[tuple[str, str], float] = {}
    prem: dict[tuple[str, str], float] = {}
    for gender in ["man", "woman"]:
        total = len(apps[gender])
        for occupation in occupations:
            cell = [row for row in apps[gender] if row["occupation"] == occupation]
            shares[(gender, occupation)] = len(cell) / total if total else 0.0
            prem[(gender, occupation)] = mean([float(row["firm_premium"]) for row in cell])

    total_gap = mean_premium["man"] - mean_premium["woman"]
    between = sum(
        (shares[("man", occupation)] - shares[("woman", occupation)]) * prem[("man", occupation)]
        for occupation in occupations
    )
    within = sum(
        shares[("woman", occupation)] * (prem[("man", occupation)] - prem[("woman", occupation)])
        for occupation in occupations
    )
    residual = total_gap - between - within

    return [
        {
            "component": "total_gap_man_minus_woman",
            "estimate": f4(total_gap),
            "interpretation": "descriptive difference in mean firm premium among applied jobs",
        },
        {
            "component": "between_occupation_sorting",
            "estimate": f4(between),
            "interpretation": "part associated with different occupation shares among applications",
        },
        {
            "component": "within_occupation_job_quality",
            "estimate": f4(within),
            "interpretation": "part associated with different firm premiums within occupation cells",
        },
        {
            "component": "residual_rounding",
            "estimate": f4(residual),
            "interpretation": "rounding and interaction residual in this simple teaching decomposition",
        },
    ]


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    write_dicts(outdir / "application_gap_summary.csv", application_gap_summary(rows))
    write_dicts(outdir / "application_gap_by_occupation.csv", occupation_summary(rows))
    write_dicts(outdir / "application_quality_decomposition.csv", application_quality_decomposition(rows))

    note = "\n".join(
        [
            "This reproduction summarizes deterministic synthetic application choice-set data.",
            "The exercise is inspired by administrative application-gap evidence, not an official replication.",
            "The decomposition is descriptive: it separates observed application sorting from causal firm treatment.",
            "Use the outputs to ask what application data observe and what remains hidden after the match.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved application-gap outputs to {outdir}")


if __name__ == "__main__":
    main()
