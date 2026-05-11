from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


NUMERIC_FIELDS = ["local_experience", "callback"]
GROUP_ORDER = [
    "white_name_local_credential",
    "black_name_local_credential",
    "immigrant_name_local_credential",
    "immigrant_name_foreign_credential",
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


def mean_indicator(rows: list[dict[str, object]], field: str, value: str) -> float:
    if not rows:
        return 0.0
    return round(fmean(1.0 if row[field] == value else 0.0 for row in rows), 4)


def mean(rows: list[dict[str, object]], field: str) -> float:
    if not rows:
        return 0.0
    return round(fmean(float(row[field]) for row in rows), 4)


def summarize_by_group(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["group_signal"])].append(row)

    output: list[dict[str, object]] = []
    for group in GROUP_ORDER:
        group_rows = grouped[group]
        output.append(
            {
                "group_signal": group,
                "observations": len(group_rows),
                "high_quality_share": mean_indicator(group_rows, "resume_quality", "high"),
                "foreign_credential_share": mean_indicator(group_rows, "credential_origin", "foreign"),
                "local_experience_share": mean(group_rows, "local_experience"),
                "disadvantaged_neighborhood_share": mean_indicator(
                    group_rows,
                    "neighborhood_signal",
                    "disadvantaged",
                ),
                "public_employer_share": mean_indicator(group_rows, "employer_sector", "public"),
                "callback_rate": mean(group_rows, "callback"),
            }
        )
    return output


def quality_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["group_signal"]), str(row["resume_quality"]))].append(row)

    output: list[dict[str, object]] = []
    for group in GROUP_ORDER:
        for quality in ["standard", "high"]:
            quality_rows = grouped[(group, quality)]
            output.append(
                {
                    "group_signal": group,
                    "resume_quality": quality,
                    "observations": len(quality_rows),
                    "callback_rate": mean(quality_rows, "callback"),
                }
            )
    return output


def gap_rows(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    by_group = {str(row["group_signal"]): row for row in summary}
    baseline = float(by_group["white_name_local_credential"]["callback_rate"])
    output: list[dict[str, object]] = []
    for group in GROUP_ORDER[1:]:
        gap = round(float(by_group[group]["callback_rate"]) - baseline, 4)
        output.append(
            {
                "comparison": f"{group}_minus_white_name_local_credential",
                "callback_gap": gap,
                "interpretation": interpretation(group),
            }
        )
    return output


def interpretation(group: str) -> str:
    meanings = {
        "black_name_local_credential": "race-coded name signal in a resume audit",
        "immigrant_name_local_credential": "immigrant-name signal with local credentials visible",
        "immigrant_name_foreign_credential": "immigrant-name and foreign-credential signal combined",
    }
    return meanings[group]


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 6 resume-audit reproduction note",
                "",
                "This synthetic file is a teaching analog for Bertrand-Mullainathan style audit reasoning.",
                "The callback gap identifies differential access at the first hiring gate.",
                "The Oreopoulos-style challenge is visible in the immigrant and foreign-credential rows.",
                "Do not interpret this table as a wage, productivity, promotion, or lifecycle estimate.",
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
    summary = summarize_by_group(rows)
    write_csv(
        args.outdir / "resume_audit_summary.csv",
        [
            "group_signal",
            "observations",
            "high_quality_share",
            "foreign_credential_share",
            "local_experience_share",
            "disadvantaged_neighborhood_share",
            "public_employer_share",
            "callback_rate",
        ],
        summary,
    )
    write_csv(
        args.outdir / "resume_audit_gaps.csv",
        ["comparison", "callback_gap", "interpretation"],
        gap_rows(summary),
    )
    write_csv(
        args.outdir / "quality_callback_summary.csv",
        ["group_signal", "resume_quality", "observations", "callback_rate"],
        quality_summary(rows),
    )
    write_note(args.outdir / "reproduction_note.txt")
    print(f"Wrote Week 6 resume-audit outputs to {args.outdir}")


if __name__ == "__main__":
    main()
