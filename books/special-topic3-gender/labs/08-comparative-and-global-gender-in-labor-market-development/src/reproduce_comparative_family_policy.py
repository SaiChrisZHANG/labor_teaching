#!/usr/bin/env python3
"""Reproduce bounded comparative family-policy summaries for Week 8."""
from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path


NUMERIC_COLUMNS = [
    "care_index",
    "leave_generosity",
    "service_share",
    "legal_access_index",
    "formality_rate",
    "norm_restrictiveness",
    "mobility_cost",
    "public_employment_share",
    "female_lfp",
    "female_hours",
    "job_continuity",
    "gender_wage_gap",
]

MECHANISMS = [
    ("care_index", "care infrastructure", "labor supply and job continuity"),
    ("leave_generosity", "family policy design", "retention and continuity"),
    ("service_share", "service-sector labor demand", "participation and hours"),
    ("legal_access_index", "legal regime", "formal feasibility"),
    ("formality_rate", "formality", "coverage and measured wage work"),
    ("norm_restrictiveness", "norms", "acceptable work and household allocation"),
    ("mobility_cost", "mobility", "search radius and feasible jobs"),
    ("public_employment_share", "public employment", "state labor demand"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to synthetic comparative country-year CSV.")
    parser.add_argument("--outdir", required=True, help="Directory for reproduced outputs.")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"No rows found in {path}")
    return rows


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def correlation(x_values: list[float], y_values: list[float]) -> float:
    if len(x_values) != len(y_values) or len(x_values) < 2:
        return float("nan")
    x_mean = mean(x_values)
    y_mean = mean(y_values)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    x_var = sum((x - x_mean) ** 2 for x in x_values)
    y_var = sum((y - y_mean) ** 2 for y in y_values)
    if x_var == 0 or y_var == 0:
        return float("nan")
    return numerator / math.sqrt(x_var * y_var)


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def require_columns(rows: list[dict[str, str]], required: set[str]) -> None:
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def group_summary(rows: list[dict[str, str]], group_key: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row[group_key]].append(row)

    output: list[dict[str, object]] = []
    for group, group_rows in sorted(grouped.items()):
        summary: dict[str, object] = {group_key: group, "rows": len(group_rows)}
        for column in NUMERIC_COLUMNS:
            summary[f"mean_{column}"] = f"{mean([float(row[column]) for row in group_rows]):.4f}"
        output.append(summary)
    return output


def mechanism_diagnostics(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    outputs = ["female_lfp", "female_hours", "job_continuity", "gender_wage_gap"]
    diagnostics: list[dict[str, object]] = []
    for variable, mechanism, labor_margin in MECHANISMS:
        x_values = [float(row[variable]) for row in rows]
        row: dict[str, object] = {
            "variable": variable,
            "mechanism": mechanism,
            "primary_labor_margin": labor_margin,
        }
        for output in outputs:
            y_values = [float(item[output]) for item in rows]
            row[f"corr_with_{output}"] = f"{correlation(x_values, y_values):.4f}"
        if variable in {"norm_restrictiveness", "mobility_cost"}:
            row["portable_mechanism"] = "constraint raises fixed cost of market work"
            row["setting_specific_warning"] = "content and enforcement vary across settings"
        elif variable in {"care_index", "leave_generosity"}:
            row["portable_mechanism"] = "care and continuity constraints shape labor supply"
            row["setting_specific_warning"] = "coverage, financing, and informal care substitutes differ"
        elif variable == "service_share":
            row["portable_mechanism"] = "sectoral demand changes feasible jobs"
            row["setting_specific_warning"] = "jobs may differ in safety, hours, and acceptability"
        else:
            row["portable_mechanism"] = "institution changes feasible or observed labor-market margin"
            row["setting_specific_warning"] = "enforcement, coverage, and data visibility differ"
        diagnostics.append(row)
    return diagnostics


def transportability_matrix(summary_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    matrix: list[dict[str, object]] = []
    for row in summary_rows:
        regime = str(row["regime"])
        care = float(row["mean_care_index"])
        services = float(row["mean_service_share"])
        formal = float(row["mean_formality_rate"])
        norms = float(row["mean_norm_restrictiveness"])
        mobility = float(row["mean_mobility_cost"])
        likely_travel = []
        warning = []
        if care >= 0.60:
            likely_travel.append("care continuity mechanism visible")
        else:
            warning.append("care constraint may dominate policy label")
        if services >= 0.60:
            likely_travel.append("service-demand mechanism plausible")
        else:
            warning.append("limited service demand weakens transfer")
        if formal >= 0.60:
            likely_travel.append("formal-policy coverage plausible")
        else:
            warning.append("informality limits direct policy transfer")
        if norms >= 0.55:
            warning.append("norm content may block otherwise portable mechanisms")
        if mobility >= 0.50:
            warning.append("mobility costs can shrink search before employment responds")
        matrix.append(
            {
                "regime": regime,
                "portable_mechanism_signal": "; ".join(likely_travel) or "mechanism needs additional data",
                "setting_specific_warning": "; ".join(warning) or "state exact comparison class",
                "policy_transferability_note": "transport mechanism, not policy label",
            }
        )
    return matrix


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    required = {"regime", "regime_type", "year", *NUMERIC_COLUMNS}
    require_columns(rows, required)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    regime_summary = group_summary(rows, "regime")
    write_dicts(outdir / "comparative_policy_summary.csv", regime_summary)
    write_dicts(outdir / "regime_type_summary.csv", group_summary(rows, "regime_type"))
    write_dicts(outdir / "mechanism_diagnostics.csv", mechanism_diagnostics(rows))
    write_dicts(outdir / "transportability_matrix.csv", transportability_matrix(regime_summary))

    note = "\n".join(
        [
            "This reproduction summarizes deterministic synthetic comparative gender-and-labor data.",
            "The exercise is inspired by comparative family-policy evidence, not an official replication.",
            "Use the outputs to distinguish labor-supply, labor-demand, care, legal, formality, mobility, and norms mechanisms.",
            "Transport mechanisms across settings; do not mechanically transport policy labels or effect sizes.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved comparative family-policy outputs to {outdir}")


if __name__ == "__main__":
    main()
