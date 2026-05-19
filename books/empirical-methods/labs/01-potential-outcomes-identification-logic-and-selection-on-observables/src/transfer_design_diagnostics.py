"""Apply the Week 1 observables-based workflow to a transfer setting."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from reproduce_selection_on_observables import analyze_design


TRANSFER_COVARIATES = [
    "prior_wage",
    "tenure",
    "baseline_perf",
    "high_skill",
    "supervisor_referral",
    "schedule_flex",
    "distance_training",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    outputs = analyze_design(df, "training", "next_wage", TRANSFER_COVARIATES, args.outdir)

    (args.outdir / "estimates.csv").rename(args.outdir / "transfer_estimates.csv")
    (args.outdir / "balance_diagnostics.csv").rename(args.outdir / "transfer_balance_diagnostics.csv")
    (args.outdir / "overlap_summary.csv").rename(args.outdir / "transfer_overlap_summary.csv")

    memo = pd.DataFrame(
        [
            {
                "design_element": "target_parameter",
                "student_prompt": "Is the workplace training question closest to ATT, ATE, or ATC?",
            },
            {
                "design_element": "selection_story",
                "student_prompt": "Which observed variables explain why workers enter training?",
            },
            {
                "design_element": "main_unobserved_threat",
                "student_prompt": "What private information or motivation remains unobserved?",
            },
            {
                "design_element": "interpretation",
                "student_prompt": "Would you defend a causal estimate or an adjusted descriptive comparison?",
            },
        ]
    )
    memo.to_csv(args.outdir / "transfer_design_prompts.csv", index=False)

    print(outputs["estimates"].round(3).to_string(index=False))
    print(f"Wrote transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
