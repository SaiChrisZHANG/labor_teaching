"""Transfer the network curation workflow to directed referral data."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def write_referrer_metrics(referrals: pd.DataFrame, outdir: Path) -> None:
    metrics = (
        referrals.groupby(["referrer_worker_id", "referrer_group"], as_index=False)
        .agg(
            out_degree=("applicant_id", "count"),
            unique_applicants=("applicant_id", "nunique"),
            mean_tie_strength=("tie_strength", "mean"),
            referral_success_rate=("hired", "mean"),
            same_group_referral_share=("same_group_referral", "mean"),
        )
        .sort_values(["out_degree", "referral_success_rate"], ascending=[False, False])
    )
    metrics.round(6).to_csv(outdir / "referral_graph_metrics.csv", index=False)


def write_applicant_metrics(referrals: pd.DataFrame, outdir: Path) -> pd.DataFrame:
    metrics = (
        referrals.groupby(["applicant_id", "applicant_group"], as_index=False)
        .agg(
            in_degree=("referrer_worker_id", "count"),
            unique_referrers=("referrer_worker_id", "nunique"),
            mean_tie_strength=("tie_strength", "mean"),
            hired_any=("hired", "max"),
            referral_success_rate=("hired", "mean"),
        )
        .sort_values(["in_degree", "mean_tie_strength"], ascending=[False, False])
    )
    metrics.round(6).to_csv(outdir / "applicant_access_metrics.csv", index=False)
    return metrics


def write_inequality_summary(referrals: pd.DataFrame, applicant_metrics: pd.DataFrame, outdir: Path) -> None:
    applicant_summary = (
        applicant_metrics.groupby("applicant_group", as_index=False)
        .agg(
            applicant_count=("applicant_id", "count"),
            mean_in_degree=("in_degree", "mean"),
            share_with_multiple_referrals=("in_degree", lambda col: float((col > 1).mean())),
            hired_any_rate=("hired_any", "mean"),
            mean_tie_strength=("mean_tie_strength", "mean"),
        )
    )
    edge_summary = (
        referrals.groupby(["referrer_group", "applicant_group"], as_index=False)
        .agg(
            edge_count=("referral_id", "count"),
            mean_tie_strength=("tie_strength", "mean"),
            hire_rate=("hired", "mean"),
        )
        .sort_values(["referrer_group", "applicant_group"])
    )
    applicant_summary.round(6).to_csv(outdir / "referral_inequality_summary.csv", index=False)
    edge_summary.round(6).to_csv(outdir / "referral_edge_composition.csv", index=False)


def write_prompts(outdir: Path) -> None:
    prompts = pd.DataFrame(
        [
            {
                "prompt_type": "directed_link",
                "prompt": "What does the directed edge from referrer to applicant capture, and what informal contacts remain unobserved?",
            },
            {
                "prompt_type": "degree",
                "prompt": "Why do out-degree for referrers and in-degree for applicants answer different economic questions?",
            },
            {
                "prompt_type": "inequality",
                "prompt": "Which applicant group receives more referral access in the synthetic data?",
            },
            {
                "prompt_type": "selection",
                "prompt": "Why does referral success not identify the causal effect of being referred?",
            },
            {
                "prompt_type": "bridge_to_lecture19",
                "prompt": "What design would be needed to move from referral descriptions to causal referral effects?",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_prompts.csv", index=False)


def write_outputs(referrals: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    referrals.sort_values(["referral_month", "referral_id"]).to_csv(outdir / "directed_referral_edges.csv", index=False)
    write_referrer_metrics(referrals, outdir)
    applicant_metrics = write_applicant_metrics(referrals, outdir)
    write_inequality_summary(referrals, applicant_metrics, outdir)
    write_prompts(outdir)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--referrals", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    referrals = pd.read_csv(args.referrals)
    write_outputs(referrals, args.outdir)
    print(f"Wrote referral transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
