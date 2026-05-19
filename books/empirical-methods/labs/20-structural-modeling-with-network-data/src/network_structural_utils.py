"""Shared helpers for the Week 20 structural network lab."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


def sigmoid(values: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-values))


@dataclass
class OLSResult:
    beta: np.ndarray
    residuals: np.ndarray
    x: np.ndarray
    y: np.ndarray
    variable_names: list[str]
    nobs: int
    k_params: int


def fit_ols(data: pd.DataFrame, y_col: str, x_cols: list[str]) -> OLSResult:
    used = data[[y_col] + x_cols].dropna().copy()
    y = used[y_col].to_numpy(dtype=float)
    x_raw = used[x_cols].to_numpy(dtype=float)
    x = np.column_stack([np.ones(len(used)), x_raw])
    beta = np.linalg.pinv(x.T @ x) @ x.T @ y
    residuals = y - x @ beta
    return OLSResult(
        beta=beta,
        residuals=residuals,
        x=x,
        y=y,
        variable_names=["intercept"] + x_cols,
        nobs=len(used),
        k_params=x.shape[1],
    )


def hc1_cov(result: OLSResult) -> np.ndarray:
    x = result.x
    resid = result.residuals
    xtx_inv = np.linalg.pinv(x.T @ x)
    meat = x.T @ (x * (resid**2)[:, None])
    correction = result.nobs / max(result.nobs - result.k_params, 1)
    return correction * xtx_inv @ meat @ xtx_inv


def model_rows(result: OLSResult, label: str) -> list[dict[str, float | str | int]]:
    cov = hc1_cov(result)
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    rows: list[dict[str, float | str | int]] = []
    for idx, variable in enumerate(result.variable_names):
        estimate = float(result.beta[idx])
        std_error = float(se[idx])
        rows.append(
            {
                "model": label,
                "variable": variable,
                "estimate": estimate,
                "std_error": std_error,
                "t_stat": estimate / std_error if std_error > 0 else np.nan,
                "nobs": result.nobs,
            }
        )
    return rows


def predict_ols(data: pd.DataFrame, result: OLSResult, x_cols: list[str]) -> np.ndarray:
    x_raw = data[x_cols].to_numpy(dtype=float)
    x = np.column_stack([np.ones(len(data)), x_raw])
    return x @ result.beta


def compute_node_exposure(nodes: pd.DataFrame, edges: pd.DataFrame) -> pd.DataFrame:
    data = nodes.copy()
    data["degree"] = 0.0
    data["weighted_degree"] = 0.0
    data["network_info_exposure"] = 0.0
    data["same_group_link_share"] = 0.0

    if edges.empty:
        return data

    info = data[["worker_id", "group", "referral_access"]].rename(
        columns={
            "worker_id": "target_id",
            "group": "target_group",
            "referral_access": "target_access",
        }
    )
    linked = edges.merge(info, on="target_id", how="left")
    linked = linked.merge(
        data[["worker_id", "group"]].rename(
            columns={"worker_id": "source_id", "group": "source_group"}
        ),
        on="source_id",
        how="left",
    )
    linked["weighted_access"] = linked["tie_strength"] * linked["target_access"]
    linked["same_group"] = (linked["source_group"] == linked["target_group"]).astype(int)
    grouped = (
        linked.groupby("source_id", as_index=False)
        .agg(
            degree=("target_id", "count"),
            weighted_degree=("tie_strength", "sum"),
            weighted_access=("weighted_access", "sum"),
            same_group_links=("same_group", "sum"),
        )
        .rename(columns={"source_id": "worker_id"})
    )
    grouped["network_info_exposure"] = grouped["weighted_access"] / grouped["weighted_degree"]
    grouped["same_group_link_share"] = grouped["same_group_links"] / grouped["degree"]
    data = data.drop(
        columns=["degree", "weighted_degree", "network_info_exposure", "same_group_link_share"]
    ).merge(
        grouped[
            [
                "worker_id",
                "degree",
                "weighted_degree",
                "network_info_exposure",
                "same_group_link_share",
            ]
        ],
        on="worker_id",
        how="left",
    )
    for col in ["degree", "weighted_degree", "network_info_exposure", "same_group_link_share"]:
        data[col] = data[col].fillna(0.0)
    return data


def make_directed_edges(dyads: pd.DataFrame, linked_col: str = "linked") -> pd.DataFrame:
    selected = dyads.loc[dyads[linked_col] == 1].copy()
    if selected.empty:
        return pd.DataFrame(
            columns=[
                "source_id",
                "target_id",
                "tie_strength",
                "same_group",
                "same_occupation",
                "geo_distance",
            ]
        )
    forward = selected.rename(columns={"worker_i": "source_id", "worker_j": "target_id"})
    backward = selected.rename(columns={"worker_j": "source_id", "worker_i": "target_id"})
    return pd.concat([forward, backward], ignore_index=True)[
        [
            "source_id",
            "target_id",
            "tie_strength",
            "same_group",
            "same_occupation",
            "geo_distance",
        ]
    ]


def average_clustering(edges: pd.DataFrame) -> float:
    if edges.empty:
        return 0.0
    neighbors: dict[str, set[str]] = {}
    for row in edges[["source_id", "target_id"]].itertuples(index=False):
        neighbors.setdefault(row.source_id, set()).add(row.target_id)
    values: list[float] = []
    for node, node_neighbors in neighbors.items():
        degree = len(node_neighbors)
        if degree < 2:
            values.append(0.0)
            continue
        possible = degree * (degree - 1) / 2
        closed = 0
        neighbor_list = list(node_neighbors)
        for left_idx, left in enumerate(neighbor_list):
            for right in neighbor_list[left_idx + 1 :]:
                if right in neighbors.get(left, set()) or left in neighbors.get(right, set()):
                    closed += 1
        values.append(closed / possible)
    return float(np.mean(values)) if values else 0.0


def network_moments(nodes: pd.DataFrame, edges: pd.DataFrame) -> dict[str, float | int]:
    enriched = compute_node_exposure(nodes, edges)
    undirected_edges = edges.loc[edges["source_id"] < edges["target_id"]].copy()
    possible_edges = len(nodes) * (len(nodes) - 1) / 2
    if undirected_edges.empty:
        same_group_share = 0.0
        same_occupation_share = 0.0
        wage_covariance = 0.0
        avg_tie_strength = 0.0
    else:
        same_group_share = float(undirected_edges["same_group"].mean())
        same_occupation_share = float(undirected_edges["same_occupation"].mean())
        avg_tie_strength = float(undirected_edges["tie_strength"].mean())
        wage_map = nodes.set_index("worker_id")["wage"].to_dict() if "wage" in nodes else {}
        left_wage = undirected_edges["source_id"].map(wage_map).to_numpy(dtype=float)
        right_wage = undirected_edges["target_id"].map(wage_map).to_numpy(dtype=float)
        wage_covariance = float(np.cov(left_wage, right_wage)[0, 1]) if len(left_wage) > 1 else 0.0

    return {
        "node_count": int(len(nodes)),
        "edge_count": int(len(undirected_edges)),
        "density": float(len(undirected_edges) / possible_edges) if possible_edges > 0 else 0.0,
        "average_degree": float(enriched["degree"].mean()),
        "degree_p90": float(enriched["degree"].quantile(0.90)),
        "homophily_share": same_group_share,
        "same_occupation_share": same_occupation_share,
        "average_tie_strength": avg_tie_strength,
        "average_clustering": average_clustering(edges),
        "wage_covariance_across_links": wage_covariance,
        "average_network_info_exposure": float(enriched["network_info_exposure"].mean()),
    }


def summarize_scenario(
    scenario: str,
    nodes: pd.DataFrame,
    edges: pd.DataFrame,
    predicted_wage: np.ndarray,
) -> dict[str, float | str | int]:
    enriched = compute_node_exposure(nodes, edges)
    temp = enriched.assign(predicted_wage=predicted_wage)
    group_means = temp.groupby("group")["predicted_wage"].mean().to_dict()
    return {
        "scenario": scenario,
        "edge_count": int(len(edges) / 2),
        "mean_predicted_wage": float(temp["predicted_wage"].mean()),
        "group_a_predicted_wage": float(group_means.get("A", np.nan)),
        "group_b_predicted_wage": float(group_means.get("B", np.nan)),
        "a_minus_b_gap": float(group_means.get("A", np.nan) - group_means.get("B", np.nan)),
        "mean_network_info_exposure": float(temp["network_info_exposure"].mean()),
        "mean_degree": float(temp["degree"].mean()),
    }
