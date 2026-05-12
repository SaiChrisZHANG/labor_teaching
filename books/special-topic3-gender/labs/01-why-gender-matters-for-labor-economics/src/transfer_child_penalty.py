from __future__ import annotations

import argparse
import csv
from pathlib import Path


OUTCOMES = ["earnings_index", "hours_index", "employment_index"]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def wide_event_time(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_key = {(row["gender"], int(row["event_time"])): row for row in rows}
    event_times = sorted({int(row["event_time"]) for row in rows})
    output: list[dict[str, object]] = []
    for event_time in event_times:
        row: dict[str, object] = {"event_time": event_time}
        for outcome in OUTCOMES:
            female = float(by_key[("female", event_time)][outcome])
            male = float(by_key[("male", event_time)][outcome])
            row[f"female_{outcome}"] = round(female, 2)
            row[f"male_{outcome}"] = round(male, 2)
            row[f"gap_female_minus_male_{outcome}"] = round(female - male, 2)
        output.append(row)
    return output


def penalty_table(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    by_key = {(row["gender"], int(row["event_time"])): row for row in rows}
    baseline_time = -1
    comparison_times = [0, 2, 5, 8]
    output: list[dict[str, object]] = []
    for event_time in comparison_times:
        row: dict[str, object] = {"comparison": f"event_{event_time}_minus_event_{baseline_time}"}
        for outcome in OUTCOMES:
            female_change = float(by_key[("female", event_time)][outcome]) - float(
                by_key[("female", baseline_time)][outcome]
            )
            male_change = float(by_key[("male", event_time)][outcome]) - float(
                by_key[("male", baseline_time)][outcome]
            )
            row[f"female_change_{outcome}"] = round(female_change, 2)
            row[f"male_change_{outcome}"] = round(male_change, 2)
            row[f"differential_child_penalty_{outcome}"] = round(female_change - male_change, 2)
        output.append(row)
    return output


def design_map() -> list[dict[str, str]]:
    return [
        {
            "question": "What outcome is measured?",
            "answer": "Event-time earnings, hours, and employment indices.",
        },
        {
            "question": "What is the comparison group?",
            "answer": "Post-birth event years compared with event year -1, separately by gender.",
        },
        {
            "question": "What mechanism is claimed?",
            "answer": "Family formation may change care constraints, hours, job choice, and career progression.",
        },
        {
            "question": "What level does the mechanism operate on?",
            "answer": "Lifecycle worker-household timing, not country-year law or firm assignment.",
        },
        {
            "question": "What is the design type?",
            "answer": "Event-time diagnostic path for teaching; causal interpretation requires assumptions about counterfactual trends.",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    rows = read_rows(Path(args.input))
    event_summary = wide_event_time(rows)
    penalties = penalty_table(rows)

    event_fields = ["event_time"]
    for outcome in OUTCOMES:
        event_fields.extend(
            [
                f"female_{outcome}",
                f"male_{outcome}",
                f"gap_female_minus_male_{outcome}",
            ]
        )
    penalty_fields = ["comparison"]
    for outcome in OUTCOMES:
        penalty_fields.extend(
            [
                f"female_change_{outcome}",
                f"male_change_{outcome}",
                f"differential_child_penalty_{outcome}",
            ]
        )

    write_csv(outdir / "child_penalty_event_time_summary.csv", event_summary, event_fields)
    write_csv(outdir / "child_penalty_diagnostics.csv", penalties, penalty_fields)
    write_csv(outdir / "transfer_design_map.csv", design_map(), ["question", "answer"])

    note = (
        "The transfer exercise converts the Week 1 diagnostic framework to lifecycle timing. "
        "It highlights that child-penalty evidence is dynamic: the comparison period and "
        "outcome choice are part of the estimand.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
