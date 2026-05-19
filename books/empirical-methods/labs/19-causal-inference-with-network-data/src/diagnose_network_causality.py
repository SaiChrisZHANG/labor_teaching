"""Diagnose exposure, reflection, and interference assumptions."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from network_causal_utils import add_peer_measures, fit_ols, hc1_cov, model_rows


def exposure_coefficient(data: pd.DataFrame, exposure_col: str) -> dict[str, object]:
    working = data.copy()
    working["senior"] = (working["role"] == "senior").astype(int)
    result = fit_ols(
        working,
        "productivity",
        ["treated", exposure_col, "baseline_skill", "tenure_years", "senior"],
    )
    cov = hc1_cov(result)
    idx = result.variable_names.index(exposure_col)
    se = float(np.sqrt(max(np.diag(cov)[idx], 0.0)))
    return {
        "exposure_mapping": exposure_col,
        "estimate": float(result.beta[idx]),
        "std_error": se,
        "t_stat": float(result.beta[idx] / se) if se > 0 else np.nan,
        "nobs": result.nobs,
    }


def write_exposure_sensitivity(data: pd.DataFrame, outdir: Path) -> None:
    mappings = [
        ("team_treated_share_loo", "team leave-one-out treated share"),
        ("graph_treated_share", "unweighted coworker-neighbor treated share"),
        ("weighted_graph_treated_share", "tie-strength-weighted coworker-neighbor treated share"),
        ("treated_senior_neighbor", "indicator for at least one treated senior neighbor"),
    ]
    rows: list[dict[str, object]] = []
    for col, definition in mappings:
        row = exposure_coefficient(data, col)
        row["definition"] = definition
        row["failure_mode"] = "misspecified exposure, sorting, or shared team shocks"
        rows.append(row)
    pd.DataFrame(rows).round(6).to_csv(outdir / "exposure_mapping_sensitivity.csv", index=False)


def write_reflection_diagnostics(data: pd.DataFrame, outdir: Path) -> None:
    working = data.copy()
    working["senior"] = (working["role"] == "senior").astype(int)
    specs = [
        (
            "team_peer_productivity_loo",
            "contemporaneous leave-one-out team peer productivity",
        ),
        (
            "graph_peer_productivity",
            "contemporaneous tie-weighted graph-neighbor productivity",
        ),
    ]
    rows: list[dict[str, object]] = []
    for exposure_col, definition in specs:
        result = fit_ols(
            working,
            "productivity",
            [exposure_col, "treated", "baseline_skill", "tenure_years", "senior"],
        )
        cov = hc1_cov(result)
        for row in model_rows(result, cov, "hc1"):
            if row["variable"] == exposure_col:
                row["diagnostic"] = definition
                row["interpretation_warning"] = (
                    "Reflection-prone: own and peer productivity are contemporaneous outcomes."
                )
                rows.append(row)
    pd.DataFrame(rows).round(6).to_csv(outdir / "reflection_diagnostics.csv", index=False)


def permuted_statistic(data: pd.DataFrame, edges: pd.DataFrame, rng: np.random.Generator) -> float:
    permuted = data.copy()
    shuffled_parts = []
    for _, team in permuted.groupby("team_id", sort=False):
        team = team.copy()
        team["treated"] = rng.permutation(team["treated"].to_numpy())
        shuffled_parts.append(team)
    permuted = pd.concat(shuffled_parts, ignore_index=True)
    permuted = add_peer_measures(permuted, edges)
    return float(exposure_coefficient(permuted, "graph_treated_share")["estimate"])


def write_randomization_inference(data: pd.DataFrame, edges: pd.DataFrame, outdir: Path) -> None:
    observed = float(exposure_coefficient(data, "graph_treated_share")["estimate"])
    rng = np.random.default_rng(1941)
    draws = [permuted_statistic(data, edges, rng) for _ in range(200)]
    draws_df = pd.DataFrame({"draw": range(1, len(draws) + 1), "permuted_graph_exposure_estimate": draws})
    p_value = float((np.abs(draws_df["permuted_graph_exposure_estimate"]) >= abs(observed)).mean())
    summary = pd.DataFrame(
        [
            {
                "assignment_rule": "treatment labels permuted within team, preserving team treatment counts",
                "observed_graph_exposure_estimate": observed,
                "permutation_count": len(draws),
                "null_mean": float(draws_df["permuted_graph_exposure_estimate"].mean()),
                "null_sd": float(draws_df["permuted_graph_exposure_estimate"].std(ddof=1)),
                "two_sided_randomization_p_value": p_value,
                "interpretation": "teaching diagnostic; valid only for the stated synthetic assignment rule",
            }
        ]
    )
    draws_df.round(6).to_csv(outdir / "randomization_inference_draws.csv", index=False)
    summary.round(6).to_csv(outdir / "randomization_inference_summary.csv", index=False)


def write_partial_interference_audit(data: pd.DataFrame, outdir: Path) -> None:
    audit = (
        data.groupby(["team_id", "saturation_cell"], as_index=False)
        .agg(
            workers=("worker_id", "count"),
            outside_contact_share=("outside_team_contact_count", lambda col: float((col > 0).mean())),
            mean_outside_contacts=("outside_team_contact_count", "mean"),
            mean_graph_treated_share=("graph_treated_share", "mean"),
            mean_productivity=("productivity", "mean"),
        )
        .sort_values("team_id")
    )
    audit["partial_interference_note"] = np.where(
        audit["outside_contact_share"] > 0.35,
        "fragile: many workers report outside-team contacts",
        "more plausible: outside-team contacts are limited in the synthetic frame",
    )
    audit.round(6).to_csv(outdir / "partial_interference_audit.csv", index=False)


def write_prompts(outdir: Path) -> None:
    prompts = pd.DataFrame(
        [
            {
                "prompt_type": "exposure_mapping",
                "prompt": "Which exposure mapping best matches the workplace mechanism, and which one is easiest to defend?",
            },
            {
                "prompt_type": "reflection",
                "prompt": "Why is a coefficient on contemporaneous peer productivity not a clean peer effect?",
            },
            {
                "prompt_type": "randomization",
                "prompt": "What treatment assignments are allowed under the permutation exercise?",
            },
            {
                "prompt_type": "partial_interference",
                "prompt": "Which teams make the no-cross-team-spillover assumption least plausible?",
            },
            {
                "prompt_type": "bridge_to_transfer",
                "prompt": "How does the inference problem change when the observation becomes a referral dyad?",
            },
        ]
    )
    prompts.to_csv(outdir / "diagnostic_prompts.csv", index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", required=True, type=Path)
    parser.add_argument("--edges", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workers = pd.read_csv(args.workers)
    edges = pd.read_csv(args.edges)
    data = add_peer_measures(workers, edges)
    args.outdir.mkdir(parents=True, exist_ok=True)

    write_exposure_sensitivity(data, args.outdir)
    write_reflection_diagnostics(data, args.outdir)
    write_randomization_inference(data, edges, args.outdir)
    write_partial_interference_audit(data, args.outdir)
    write_prompts(args.outdir)
    print(f"Wrote diagnostic outputs to {args.outdir}")


if __name__ == "__main__":
    main()
