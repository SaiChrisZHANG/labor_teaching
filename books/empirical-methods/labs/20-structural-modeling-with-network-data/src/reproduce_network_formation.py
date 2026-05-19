"""Reproduce a teaching-scale structural network formation workflow."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from network_structural_utils import (
    compute_node_exposure,
    fit_ols,
    make_directed_edges,
    model_rows,
    network_moments,
    predict_ols,
    summarize_scenario,
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


def add_group_indicator(nodes: pd.DataFrame) -> pd.DataFrame:
    data = nodes.copy()
    data["group_b"] = (data["group"] == "B").astype(int)
    return data


def build_endogenous_policy_dyads(dyads: pd.DataFrame, formation_result) -> tuple[pd.DataFrame, pd.DataFrame]:
    policy = dyads.copy()
    policy["predicted_link_probability"] = np.clip(
        predict_ols(policy, formation_result, FORMATION_COLS),
        0.01,
        0.99,
    )
    candidates = policy.loc[(policy["linked"] == 0) & (policy["same_group"] == 0)].copy()
    candidates["policy_score"] = (
        candidates["predicted_link_probability"]
        + 0.18 * candidates["referral_opportunity"]
        - 0.01 * candidates["geo_distance"]
    )
    additions = candidates.nlargest(48, "policy_score").copy()
    addition_keys = set(zip(additions["worker_i"], additions["worker_j"]))
    policy["policy_added_link"] = [
        int((row.worker_i, row.worker_j) in addition_keys)
        for row in policy.itertuples(index=False)
    ]
    policy["linked_policy"] = policy[["linked", "policy_added_link"]].max(axis=1)
    policy.loc[policy["policy_added_link"] == 1, "tie_strength"] = np.maximum(
        policy.loc[policy["policy_added_link"] == 1, "tie_strength"],
        0.48,
    )
    return policy, additions[
        [
            "worker_i",
            "worker_j",
            "predicted_link_probability",
            "referral_opportunity",
            "geo_distance",
            "policy_score",
        ]
    ]


def run(nodes_path: Path, dyads_path: Path, edges_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    nodes = pd.read_csv(nodes_path)
    dyads = pd.read_csv(dyads_path)
    edges = pd.read_csv(edges_path)

    formation_result = fit_ols(dyads, "linked", FORMATION_COLS)
    formation_rows = model_rows(formation_result, "link_formation_lpm")
    pd.DataFrame(formation_rows).to_csv(outdir / "formation_model_estimates.csv", index=False)

    moments = network_moments(nodes, edges)
    pd.DataFrame(
        [{"moment": key, "value": value} for key, value in moments.items()]
    ).to_csv(outdir / "network_moments.csv", index=False)

    behavior_data = add_group_indicator(compute_node_exposure(nodes, edges))
    behavior_result = fit_ols(behavior_data, "wage", BEHAVIOR_COLS)
    pd.DataFrame(model_rows(behavior_result, "behavior_on_network_wage")).to_csv(
        outdir / "behavior_on_network_estimates.csv",
        index=False,
    )

    baseline_pred = predict_ols(behavior_data, behavior_result, BEHAVIOR_COLS)
    fixed_nodes = nodes.copy()
    fixed_nodes["referral_access"] = np.clip(fixed_nodes["referral_access"] + 0.08, 0.0, 1.0)
    fixed_behavior = add_group_indicator(compute_node_exposure(fixed_nodes, edges))
    fixed_pred = predict_ols(fixed_behavior, behavior_result, BEHAVIOR_COLS)

    policy_dyads, additions = build_endogenous_policy_dyads(dyads, formation_result)
    policy_edges = make_directed_edges(policy_dyads, linked_col="linked_policy")
    endogenous_behavior = add_group_indicator(compute_node_exposure(nodes, policy_edges))
    endogenous_pred = predict_ols(endogenous_behavior, behavior_result, BEHAVIOR_COLS)

    scenarios = [
        summarize_scenario("baseline_observed_network", nodes, edges, baseline_pred),
        summarize_scenario("fixed_network_better_information", fixed_nodes, edges, fixed_pred),
        summarize_scenario("endogenous_cross_group_link_policy", nodes, policy_edges, endogenous_pred),
    ]
    pd.DataFrame(scenarios).to_csv(outdir / "fixed_vs_endogenous_counterfactual.csv", index=False)
    additions.to_csv(outdir / "counterfactual_link_changes.csv", index=False)

    fitted = dyads.copy()
    fitted["predicted_link_probability"] = np.clip(
        predict_ols(fitted, formation_result, FORMATION_COLS),
        0.01,
        0.99,
    )
    fitted[
        [
            "worker_i",
            "worker_j",
            "linked",
            "predicted_link_probability",
            "same_group",
            "same_occupation",
            "skill_distance",
            "geo_distance",
            "referral_opportunity",
        ]
    ].to_csv(outdir / "dyad_predicted_links.csv", index=False)

    print(f"Wrote outputs to {outdir}")


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
