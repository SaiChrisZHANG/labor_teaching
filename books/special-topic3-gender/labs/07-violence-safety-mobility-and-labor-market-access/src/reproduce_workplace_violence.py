#!/usr/bin/env python3
"""Reproduce bounded workplace-violence linkage summaries."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


OUTCOMES = ["separated", "retained", "sick_days", "wage", "reported_event"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the synthetic workplace panel CSV.")
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


def write_dicts(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def group_summary(rows: list[dict[str, str]], keys: list[str], outcomes: list[str]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[tuple(row[key] for key in keys)].append(row)

    summaries: list[dict[str, object]] = []
    for key_values, group in sorted(grouped.items()):
        summary = {key: value for key, value in zip(keys, key_values)}
        summary["worker_periods"] = len(group)
        for outcome in outcomes:
            summary[f"mean_{outcome}"] = f"{mean([float(row[outcome]) for row in group]):.4f}"
        summaries.append(summary)
    return summaries


def make_separation_did(event_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    lookup = {
        (row["exposure_group"], row["female"], row["period"]): row
        for row in event_rows
    }
    did_rows: list[dict[str, object]] = []
    for exposure in ("victim", "coworker"):
        for female in ("0", "1"):
            treated_pre = lookup.get((exposure, female, "-1"))
            treated_post = lookup.get((exposure, female, "1"))
            comp_pre = lookup.get(("comparison", female, "-1"))
            comp_post = lookup.get(("comparison", female, "1"))
            if not all([treated_pre, treated_post, comp_pre, comp_post]):
                continue
            treated_change = float(treated_post["mean_separated"]) - float(treated_pre["mean_separated"])
            comparison_change = float(comp_post["mean_separated"]) - float(comp_pre["mean_separated"])
            sick_change = float(treated_post["mean_sick_days"]) - float(treated_pre["mean_sick_days"])
            did_rows.append(
                {
                    "exposure_group": exposure,
                    "female": female,
                    "treated_separation_change": f"{treated_change:.4f}",
                    "comparison_separation_change": f"{comparison_change:.4f}",
                    "difference_in_differences": f"{treated_change - comparison_change:.4f}",
                    "treated_sick_days_change": f"{sick_change:.4f}",
                    "interpretation": "reported-event response, not total latent exposure",
                }
            )
    return did_rows


def firm_response(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row["event_firm"], row["period"])].append(row)

    output: list[dict[str, object]] = []
    for (event_firm, period), group in sorted(grouped.items()):
        hires = [row for row in group if row["new_hire"] == "1"]
        female_hires = [row for row in hires if row["female"] == "1"]
        output.append(
            {
                "event_firm": event_firm,
                "period": period,
                "worker_periods": len(group),
                "new_hires": len(hires),
                "female_hire_share": f"{(len(female_hires) / len(hires)):.4f}" if hires else "NA",
                "mean_separation": f"{mean([float(row['separated']) for row in group]):.4f}",
                "mean_sick_days": f"{mean([float(row['sick_days']) for row in group]):.4f}",
            }
        )
    return output


def main() -> None:
    args = parse_args()
    rows = read_rows(Path(args.input))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    required = {
        "period",
        "female",
        "event_firm",
        "reported_victim",
        "coworker_exposed",
        "exposure_group",
        "new_hire",
        *OUTCOMES,
    }
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    event_rows = group_summary(rows, ["exposure_group", "female", "period"], OUTCOMES)
    write_dicts(outdir / "event_time_by_exposure.csv", event_rows)

    did_rows = make_separation_did(event_rows)
    write_dicts(outdir / "separation_did.csv", did_rows)

    firm_rows = firm_response(rows)
    write_dicts(outdir / "firm_response_summary.csv", firm_rows)

    note = "\n".join(
        [
            "This reproduction summarizes a synthetic administrative-linkage exercise.",
            "The observed event is a reported workplace-violence incident, not all latent exposure.",
            "The observed labor margins are separation, retention, sick leave, wages, and firm hiring.",
            "Use the outputs to diagnose victim effects, coworker spillovers, and firm response.",
        ]
    )
    (outdir / "reproduction_note.txt").write_text(note + "\n", encoding="utf-8")
    print(f"Saved workplace-violence reproduction outputs to {outdir}")


if __name__ == "__main__":
    main()
