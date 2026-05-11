from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import fmean


JOB_NUMERIC_FIELDS = [
    "offered_wage_index",
    "care_obligation_index",
    "self_promotion_confidence_index",
    "perceived_norm_fit_index",
    "application_submitted",
]


def read_rows(path: Path, numeric_fields: list[str]) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows: list[dict[str, object]] = list(csv.DictReader(handle))
    for row in rows:
        for field in numeric_fields:
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


def proxy_diagnostics() -> list[dict[str, object]]:
    return [
        {
            "variable": "origin_female_lfp",
            "proxy_class": "inherited_norm_proxy",
            "design_question": "Does an origin-linked work norm predict labor supply in a host environment?",
            "diagnostic_caution": "Transmission is not the same as current peer pressure; migrant selection may remain.",
            "week_boundary": "Week 5 conduct norm",
        },
        {
            "variable": "family_role_norm_index",
            "proxy_class": "direct_norm_proxy",
            "design_question": "Does a role expectation make market work socially costly?",
            "diagnostic_caution": "Check whether the proxy is correlated with childcare costs, wages, or legal constraints.",
            "week_boundary": "Week 5 conduct norm",
        },
        {
            "variable": "current_peer_pressure_index",
            "proxy_class": "current_social_pressure",
            "design_question": "Does the local social environment discipline work or nonwork?",
            "diagnostic_caution": "Current peer pressure can be endogenous to local labor demand and worker sorting.",
            "week_boundary": "Week 5 conduct norm",
        },
        {
            "variable": "host_wage_index",
            "proxy_class": "price_control",
            "design_question": "Are observed choices responding to wages rather than norms?",
            "diagnostic_caution": "A norm interpretation is weak if wage differences explain the pattern.",
            "week_boundary": "Labor-market price",
        },
        {
            "variable": "childcare_cost_index",
            "proxy_class": "constraint_control",
            "design_question": "Are observed choices responding to care prices rather than role norms?",
            "diagnostic_caution": "Care constraints and gender-role norms can interact; do not treat either as automatic.",
            "week_boundary": "Price or constraint",
        },
        {
            "variable": "perceived_norm_fit_index",
            "proxy_class": "job_entry_norm_proxy",
            "design_question": "Does the job frame feel acceptable or role-consistent to the applicant?",
            "diagnostic_caution": "Field-experimental framing identifies an entry response, not all sources of the norm.",
            "week_boundary": "Week 5 conduct norm",
        },
        {
            "variable": "category_hierarchy_signal",
            "proxy_class": "structural_hierarchy_proxy",
            "design_question": "Does category membership change access, authority, or employer evaluation?",
            "diagnostic_caution": "This belongs in Week 6 unless the mechanism is explicitly acceptable conduct.",
            "week_boundary": "Reserve for Week 6",
        },
    ]


def job_entry_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[(str(row["applicant_group"]), str(row["job_frame"]))].append(row)
    output: list[dict[str, object]] = []
    for group, frame in sorted(grouped):
        frame_rows = grouped[(group, frame)]
        output.append(
            {
                "applicant_group": group,
                "job_frame": frame,
                "observations": len(frame_rows),
                "offered_wage_index": mean(frame_rows, "offered_wage_index"),
                "care_obligation_index": mean(frame_rows, "care_obligation_index"),
                "self_promotion_confidence_index": mean(frame_rows, "self_promotion_confidence_index"),
                "perceived_norm_fit_index": mean(frame_rows, "perceived_norm_fit_index"),
                "application_rate": mean(frame_rows, "application_submitted"),
            }
        )
    return output


def job_entry_gaps(summary: list[dict[str, object]]) -> list[dict[str, object]]:
    by_frame_group = {
        (str(row["job_frame"]), str(row["applicant_group"])): row
        for row in summary
    }
    frames = sorted({str(row["job_frame"]) for row in summary})
    output: list[dict[str, object]] = []
    for frame in frames:
        women = by_frame_group[(frame, "women")]
        men = by_frame_group[(frame, "men")]
        output.append(
            {
                "job_frame": frame,
                "women_minus_men_norm_fit": round(
                    float(women["perceived_norm_fit_index"]) - float(men["perceived_norm_fit_index"]),
                    4,
                ),
                "women_minus_men_application_rate": round(
                    float(women["application_rate"]) - float(men["application_rate"]),
                    4,
                ),
                "diagnostic_question": "Is the entry gap caused by norm fit, wage framing, care constraints, or expected ability?",
            }
        )
    return output


def write_note(path: Path) -> None:
    path.write_text(
        "\n".join(
            [
                "Week 5 diagnostic note",
                "",
                "The proxy table separates inherited norms, current pressure, prices, constraints, job-entry norm fit, and Week 6 hierarchy signals.",
                "The job-entry summary is a teaching analog for field-experimental evidence on competition and gender-coded work.",
                "Interpret application gaps as design prompts: the randomized frame helps, but students must still name the exact margin identified.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inherited", type=Path, required=True)
    parser.add_argument("--job-entry", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    read_rows(args.inherited, [])
    job_rows = read_rows(args.job_entry, JOB_NUMERIC_FIELDS)
    summary = job_entry_summary(job_rows)
    write_csv(
        args.outdir / "proxy_diagnostic.csv",
        ["variable", "proxy_class", "design_question", "diagnostic_caution", "week_boundary"],
        proxy_diagnostics(),
    )
    write_csv(
        args.outdir / "job_entry_summary.csv",
        [
            "applicant_group",
            "job_frame",
            "observations",
            "offered_wage_index",
            "care_obligation_index",
            "self_promotion_confidence_index",
            "perceived_norm_fit_index",
            "application_rate",
        ],
        summary,
    )
    write_csv(
        args.outdir / "job_entry_gaps.csv",
        [
            "job_frame",
            "women_minus_men_norm_fit",
            "women_minus_men_application_rate",
            "diagnostic_question",
        ],
        job_entry_gaps(summary),
    )
    write_note(args.outdir / "diagnostic_note.txt")
    print(f"Wrote Week 5 diagnostic outputs to {args.outdir}")


if __name__ == "__main__":
    main()
