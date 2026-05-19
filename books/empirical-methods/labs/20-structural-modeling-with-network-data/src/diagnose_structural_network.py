"""Diagnose validation burdens for the Week 20 structural network lab."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from network_structural_utils import (
    compute_node_exposure,
    fit_ols,
    model_rows,
    network_moments,
    predict_ols,
)


FORMATION_COLS = [
    "same_group",
    "same_occupation",
    "skill_distance",
    "geo_distance",
    "either_senior",
    "referral_opportunity",
]

BEHAVIOR_COLS = [
    "network_info_exposure",
    "degree",
    "skill",
    "senior",
    "group_b",
]


def validation_moments(nodes: pd.DataFrame, dyads: pd.DataFrame, edges: pd.DataFrame) -> pd.DataFrame:
    formation_result = fit_ols(dyads, "linked", FORMATION_COLS)
    predicted = np.clip(predict_ols(dyads, formation_result, FORMATION_COLS), 0.01, 0.99)
    observed = network_moments(nodes, edges)
    possible_edges = len(dyads)
    expected_edge_count = float(predicted.sum())
    expected_density = expected_edge_count / possible_edges
    expected_avg_degree = 2 * expected_edge_count / len(nodes)
    expected_homophily = float((predicted * dyads["same_group"]).sum() / predicted.sum())
    expected_same_occ = float((predicted * dyads["same_occupation"]).sum() / predicted.sum())

    rows = [
        {
            "moment": "edge_count",
            "observed": observed["edge_count"],
            "model_implied": expected_edge_count,
            "interpretation": "formation model should fit overall link volume",
        },
        {
            "moment": "density",
            "observed": observed["density"],
            "model_implied": expected_density,
            "interpretation": "density disciplines baseline meeting probability",
        },
        {
            "moment": "average_degree",
            "observed": observed["average_degree"],
            "model_implied": expected_avg_degree,
            "interpretation": "degree matters for opportunity access",
        },
        {
            "moment": "homophily_share",
            "observed": observed["homophily_share"],
            "model_implied": expected_homophily,
            "interpretation": "homophily matters for inequality counterfactuals",
        },
        {
            "moment": "same_occupation_share",
            "observed": observed["same_occupation_share"],
            "model_implied": expected_same_occ,
            "interpretation": "occupation sorting matters for referral mechanisms",
        },
        {
            "moment": "average_clustering",
            "observed": observed["average_clustering"],
            "model_implied": np.nan,
            "interpretation": "dyadic model does not directly discipline clustering",
        },
    ]
    return pd.DataFrame(rows)


def behavior_fit(nodes: pd.DataFrame, edges: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    data = compute_node_exposure(nodes, edges)
    data["group_b"] = (data["group"] == "B").astype(int)
    result = fit_ols(data, "wage", BEHAVIOR_COLS)
    fitted = predict_ols(data, result, BEHAVIOR_COLS)
    residuals = data["wage"].to_numpy(dtype=float) - fitted
    tss = float(((data["wage"] - data["wage"].mean()) ** 2).sum())
    rss = float((residuals**2).sum())
    summary = pd.DataFrame(
        [
            {
                "statistic": "r_squared",
                "value": 1 - rss / tss if tss > 0 else np.nan,
                "interpretation": "fit of behavior equation, not proof of causal peer effects",
            },
            {
                "statistic": "residual_sd",
                "value": float(np.std(residuals, ddof=result.k_params)),
                "interpretation": "unexplained wage variation after network and worker controls",
            },
            {
                "statistic": "mean_wage",
                "value": float(data["wage"].mean()),
                "interpretation": "scale for interpreting counterfactual wage changes",
            },
            {
                "statistic": "nobs",
                "value": result.nobs,
                "interpretation": "worker-level observations in the teaching design",
            },
        ]
    )
    estimates = pd.DataFrame(model_rows(result, "diagnostic_behavior_fit"))
    return summary, estimates


def assumption_audit() -> pd.DataFrame:
    rows = [
        {
            "assumption": "observed links represent job-relevant information channels",
            "teaching_diagnostic": "compare homophily, occupation overlap, and referral access by link",
            "concern": "links may proxy sorting or common environments",
            "evidence_needed_in_real_project": "institutional detail, timing, surveys, or experiments validating the channel",
        },
        {
            "assumption": "dyadic formation captures the relevant link process",
            "teaching_diagnostic": "formation model fits density and homophily but not clustering",
            "concern": "strategic transitivity or unobserved meetings may matter",
            "evidence_needed_in_real_project": "panel link evolution or moments on triangles, components, and churn",
        },
        {
            "assumption": "behavior equation is stable under policy",
            "teaching_diagnostic": "compare fixed-network and endogenous-link counterfactuals",
            "concern": "policy may change search effort, congestion, or employer screening",
            "evidence_needed_in_real_project": "reduced-form policy variation or experimental validation",
        },
        {
            "assumption": "cross-group link subsidy changes feasible contacts",
            "teaching_diagnostic": "inspect counterfactual added links and group exposure changes",
            "concern": "real barriers may be institutional rather than search-cost based",
            "evidence_needed_in_real_project": "evidence on meeting constraints and take-up of new referral opportunities",
        },
    ]
    return pd.DataFrame(rows)


def prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "stage": "diagnose",
                "prompt": "Which moments discipline link formation and which moments discipline behavior conditional on links?",
            },
            {
                "stage": "diagnose",
                "prompt": "Why is average clustering listed as a validation gap for a dyadic formation model?",
            },
            {
                "stage": "diagnose",
                "prompt": "How much does the policy conclusion change when links are allowed to form endogenously?",
            },
            {
                "stage": "diagnose",
                "prompt": "Which Lecture 19 reduced-form design would most improve the credibility of this structural counterfactual?",
            },
        ]
    )


def run(nodes_path: Path, dyads_path: Path, edges_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    nodes = pd.read_csv(nodes_path)
    dyads = pd.read_csv(dyads_path)
    edges = pd.read_csv(edges_path)

    validation_moments(nodes, dyads, edges).to_csv(outdir / "validation_moments.csv", index=False)
    summary, estimates = behavior_fit(nodes, edges)
    summary.to_csv(outdir / "behavior_fit_summary.csv", index=False)
    estimates.to_csv(outdir / "diagnostic_behavior_estimates.csv", index=False)
    assumption_audit().to_csv(outdir / "assumption_audit.csv", index=False)
    prompts().to_csv(outdir / "diagnostic_prompts.csv", index=False)

    scenario_path = outdir / "fixed_vs_endogenous_counterfactual.csv"
    if scenario_path.exists():
        scenarios = pd.read_csv(scenario_path)
        baseline = scenarios.loc[scenarios["scenario"] == "baseline_observed_network"].iloc[0]
        comparisons = []
        for row in scenarios.itertuples(index=False):
            comparisons.append(
                {
                    "scenario": row.scenario,
                    "mean_wage_change_vs_baseline": row.mean_predicted_wage - baseline["mean_predicted_wage"],
                    "gap_change_vs_baseline": row.a_minus_b_gap - baseline["a_minus_b_gap"],
                    "edge_count_change_vs_baseline": row.edge_count - baseline["edge_count"],
                }
            )
        pd.DataFrame(comparisons).to_csv(outdir / "counterfactual_sensitivity.csv", index=False)

    print(f"Wrote diagnostics to {outdir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", type=Path, required=True)
    parser.add_argument("--dyads", type=Path, required=True)
    parser.add_argument("--edges", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    run(args.nodes, args.dyads, args.edges, args.outdir)


if __name__ == "__main__":
    main()
