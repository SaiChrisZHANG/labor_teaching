"""Shared helpers for the Week 19 network causal inference lab."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


def sigmoid(values: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-values))


def add_peer_measures(workers: pd.DataFrame, edges: pd.DataFrame) -> pd.DataFrame:
    data = workers.copy()
    team_n = data.groupby("team_id")["worker_id"].transform("count")
    team_treated = data.groupby("team_id")["treated"].transform("sum")
    team_productivity = data.groupby("team_id")["productivity"].transform("sum")

    denom = (team_n - 1).replace(0, np.nan)
    data["team_treated_share_loo"] = ((team_treated - data["treated"]) / denom).fillna(0.0)
    data["team_peer_productivity_loo"] = ((team_productivity - data["productivity"]) / denom).fillna(0.0)

    graph_cols = [
        "neighbor_count",
        "weighted_degree",
        "graph_treated_share",
        "weighted_graph_treated_share",
        "graph_peer_productivity",
        "treated_senior_neighbor",
    ]
    for col in graph_cols:
        data[col] = 0.0

    if edges.empty:
        return data

    peer_info = data[
        ["worker_id", "treated", "productivity", "role"]
    ].rename(
        columns={
            "worker_id": "target_worker_id",
            "treated": "target_treated",
            "productivity": "target_productivity",
            "role": "target_role",
        }
    )
    linked = edges.merge(peer_info, on="target_worker_id", how="left")
    linked["treated_weight"] = linked["target_treated"] * linked["tie_strength"]
    linked["productivity_weight"] = linked["target_productivity"] * linked["tie_strength"]
    linked["treated_senior"] = (
        (linked["target_treated"] == 1) & (linked["target_role"] == "senior")
    ).astype(int)

    graph = (
        linked.groupby("source_worker_id", as_index=False)
        .agg(
            neighbor_count=("target_worker_id", "count"),
            treated_neighbors=("target_treated", "sum"),
            weighted_degree=("tie_strength", "sum"),
            weighted_treated=("treated_weight", "sum"),
            weighted_productivity=("productivity_weight", "sum"),
            treated_senior_neighbor=("treated_senior", "max"),
        )
    )
    graph["graph_treated_share"] = graph["treated_neighbors"] / graph["neighbor_count"]
    graph["weighted_graph_treated_share"] = graph["weighted_treated"] / graph["weighted_degree"]
    graph["graph_peer_productivity"] = graph["weighted_productivity"] / graph["weighted_degree"]

    graph = graph.rename(columns={"source_worker_id": "worker_id"})
    data = data.drop(columns=graph_cols).merge(
        graph[
            [
                "worker_id",
                "neighbor_count",
                "weighted_degree",
                "graph_treated_share",
                "weighted_graph_treated_share",
                "graph_peer_productivity",
                "treated_senior_neighbor",
            ]
        ],
        on="worker_id",
        how="left",
    )
    for col in graph_cols:
        data[col] = data[col].fillna(0.0)
    return data


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


def cluster_cov(result: OLSResult, clusters: pd.Series | np.ndarray) -> np.ndarray:
    cluster_values = np.asarray(clusters)
    if len(cluster_values) != result.nobs:
        raise ValueError("Cluster vector length must match estimation rows.")

    x = result.x
    resid = result.residuals
    xtx_inv = np.linalg.pinv(x.T @ x)
    scores = x * resid[:, None]
    meat = np.zeros((result.k_params, result.k_params))

    unique_clusters = pd.Series(cluster_values).dropna().unique()
    for cluster in unique_clusters:
        idx = cluster_values == cluster
        score_sum = scores[idx].sum(axis=0)[:, None]
        meat += score_sum @ score_sum.T

    cluster_count = len(unique_clusters)
    if cluster_count > 1 and result.nobs > result.k_params:
        correction = (cluster_count / (cluster_count - 1)) * (
            (result.nobs - 1) / (result.nobs - result.k_params)
        )
    else:
        correction = 1.0
    return correction * xtx_inv @ meat @ xtx_inv


def two_way_cluster_cov(
    result: OLSResult,
    cluster_a: pd.Series | np.ndarray,
    cluster_b: pd.Series | np.ndarray,
) -> np.ndarray:
    a = pd.Series(cluster_a).astype(str)
    b = pd.Series(cluster_b).astype(str)
    pair = a + "||" + b
    return cluster_cov(result, a) + cluster_cov(result, b) - cluster_cov(result, pair)


def model_rows(result: OLSResult, cov: np.ndarray, inference_label: str) -> list[dict[str, float | str | int]]:
    variances = np.diag(cov)
    se = np.sqrt(np.maximum(variances, 0.0))
    rows: list[dict[str, float | str | int]] = []
    for idx, variable in enumerate(result.variable_names):
        std_error = float(se[idx])
        estimate = float(result.beta[idx])
        rows.append(
            {
                "inference": inference_label,
                "variable": variable,
                "estimate": estimate,
                "std_error": std_error,
                "t_stat": estimate / std_error if std_error > 0 else np.nan,
                "nobs": result.nobs,
            }
        )
    return rows


def simple_slope(data: pd.DataFrame, y_col: str, x_col: str) -> dict[str, float | str | int]:
    result = fit_ols(data, y_col, [x_col])
    cov = hc1_cov(result)
    row = model_rows(result, cov, "hc1")[1]
    return {
        "outcome": y_col,
        "exposure": x_col,
        "estimate": row["estimate"],
        "std_error": row["std_error"],
        "t_stat": row["t_stat"],
        "nobs": row["nobs"],
    }
