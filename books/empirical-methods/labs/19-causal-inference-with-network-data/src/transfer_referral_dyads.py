"""Transfer network-causal logic to referral dyads."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from network_causal_utils import fit_ols, hc1_cov, model_rows, two_way_cluster_cov


def write_dyadic_model(referrals: pd.DataFrame, outdir: Path) -> None:
    x_cols = [
        "tie_strength",
        "same_group",
        "referrer_treated",
        "referrer_baseline_skill",
        "applicant_access_score",
    ]
    result = fit_ols(referrals, "callback", x_cols)
    hc1 = hc1_cov(result)
    dyadic = two_way_cluster_cov(
        result,
        referrals["referrer_worker_id"],
        referrals["applicant_id"],
    )

    rows = model_rows(result, hc1, "hc1_naive_row_robust")
    rows.extend(model_rows(result, dyadic, "two_way_referrer_applicant_cluster"))
    estimates = pd.DataFrame(rows)
    estimates["interpretation_note"] = np.where(
        estimates["inference"] == "two_way_referrer_applicant_cluster",
        "allows dependence among dyads sharing a referrer or applicant",
        "treats dyads as independent after covariates except for heteroskedasticity",
    )
    estimates.round(6).to_csv(outdir / "dyadic_model_estimates.csv", index=False)

    predictions = referrals[
        [
            "referral_id",
            "referrer_worker_id",
            "applicant_id",
            "referrer_group",
            "applicant_group",
            "same_group",
            "tie_strength",
            "callback",
        ]
    ].copy()
    predictions["linear_probability_prediction"] = np.clip(result.x @ result.beta, 0.0, 1.0)
    predictions.round(6).to_csv(outdir / "referral_pair_predictions.csv", index=False)


def write_access_summary(referrals: pd.DataFrame, outdir: Path) -> None:
    applicant_metrics = (
        referrals.groupby(["applicant_id", "applicant_group"], as_index=False)
        .agg(
            in_degree=("referrer_worker_id", "count"),
            unique_referrers=("referrer_worker_id", "nunique"),
            mean_tie_strength=("tie_strength", "mean"),
            callback_any=("callback", "max"),
            callback_rate=("callback", "mean"),
        )
    )
    group_summary = (
        applicant_metrics.groupby("applicant_group", as_index=False)
        .agg(
            applicants=("applicant_id", "count"),
            mean_in_degree=("in_degree", "mean"),
            share_multiple_referrers=("unique_referrers", lambda col: float((col > 1).mean())),
            callback_any_rate=("callback_any", "mean"),
            mean_tie_strength=("mean_tie_strength", "mean"),
        )
    )
    applicant_metrics.round(6).to_csv(outdir / "applicant_referral_access.csv", index=False)
    group_summary.round(6).to_csv(outdir / "referral_access_summary.csv", index=False)


def write_dependence_audit(referrals: pd.DataFrame, outdir: Path) -> None:
    pair_counts = referrals.groupby(["referrer_worker_id", "applicant_id"]).size()
    audit = pd.DataFrame(
        [
            {
                "rows": int(len(referrals)),
                "unique_referrers": int(referrals["referrer_worker_id"].nunique()),
                "unique_applicants": int(referrals["applicant_id"].nunique()),
                "mean_rows_per_referrer": float(referrals.groupby("referrer_worker_id").size().mean()),
                "max_rows_per_referrer": int(referrals.groupby("referrer_worker_id").size().max()),
                "mean_rows_per_applicant": float(referrals.groupby("applicant_id").size().mean()),
                "max_rows_per_applicant": int(referrals.groupby("applicant_id").size().max()),
                "repeated_referrer_applicant_pairs": int((pair_counts > 1).sum()),
                "inference_implication": "dyads sharing referrers or applicants should not be treated as IID rows",
            }
        ]
    )
    audit.round(6).to_csv(outdir / "dyadic_dependence_audit.csv", index=False)


def write_prompts(outdir: Path) -> None:
    prompts = pd.DataFrame(
        [
            {
                "prompt_type": "estimating_unit",
                "prompt": "Why is the row a referrer-applicant dyad rather than a worker-level observation?",
            },
            {
                "prompt_type": "dependence",
                "prompt": "Which dyads are likely correlated because they share a referrer or applicant?",
            },
            {
                "prompt_type": "inference",
                "prompt": "How do the standard errors change when inference is two-way clustered by referrer and applicant?",
            },
            {
                "prompt_type": "causal_claim",
                "prompt": "What assignment or quasi-experiment would be needed before calling same-group referral causal?",
            },
            {
                "prompt_type": "transfer",
                "prompt": "How does this dyadic design differ from the workplace peer-exposure design?",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_prompts.csv", index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--referrals", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    referrals = pd.read_csv(args.referrals)
    args.outdir.mkdir(parents=True, exist_ok=True)
    referrals.to_csv(args.outdir / "referral_dyad_edges.csv", index=False)
    write_dyadic_model(referrals, args.outdir)
    write_access_summary(referrals, args.outdir)
    write_dependence_audit(referrals, args.outdir)
    write_prompts(args.outdir)
    print(f"Wrote referral dyad transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
