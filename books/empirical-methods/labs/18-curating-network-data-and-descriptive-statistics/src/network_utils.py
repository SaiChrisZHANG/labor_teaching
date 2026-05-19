"""Shared helpers for the Week 18 network curation lab."""

from __future__ import annotations

from collections import defaultdict, deque

import numpy as np
import pandas as pd


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-x))


def ols_summary(
    frame: pd.DataFrame,
    y_col: str,
    x_col: str,
    weight_col: str | None = None,
) -> dict[str, float]:
    y = frame[y_col].to_numpy(dtype=float)
    x = frame[x_col].to_numpy(dtype=float)
    design = np.column_stack([np.ones(len(frame)), x])
    if weight_col is None:
        beta = np.linalg.lstsq(design, y, rcond=None)[0]
    else:
        weights = np.sqrt(frame[weight_col].to_numpy(dtype=float))
        beta = np.linalg.lstsq(design * weights[:, None], y * weights, rcond=None)[0]
    fitted = design @ beta
    residual = y - fitted
    return {
        "outcome": y_col,
        "network_variable": x_col,
        "intercept": float(beta[0]),
        "slope": float(beta[1]),
        "mean_outcome": float(y.mean()),
        "mean_network_variable": float(x.mean()),
        "rmse": float(np.sqrt(np.mean(residual**2))),
        "n": float(len(frame)),
    }


def build_edges(
    workers: pd.DataFrame,
    boundary_col: str,
    relation: str,
    exclude_outside: bool = False,
) -> pd.DataFrame:
    """Build an undirected worker-worker edge list under a named relation."""
    rows: list[dict[str, object]] = []
    for boundary_id, group in workers.groupby(boundary_col, sort=True):
        records = group.sort_values("worker_id").to_dict("records")
        for left_pos, left in enumerate(records):
            for right in records[left_pos + 1 :]:
                if exclude_outside and (
                    int(left["outside_observed_frame"]) == 1 or int(right["outside_observed_frame"]) == 1
                ):
                    continue
                if relation == "same_employer":
                    linked = left["employer_id"] == right["employer_id"]
                elif relation == "same_industry":
                    linked = left["industry"] == right["industry"]
                elif relation == "same_group":
                    linked = left["group"] == right["group"]
                else:
                    raise ValueError(f"Unknown relation: {relation}")
                if not linked:
                    continue
                weight = float(min(left["tenure_years"], right["tenure_years"]))
                rows.append(
                    {
                        "worker_i": left["worker_id"],
                        "worker_j": right["worker_id"],
                        "boundary_col": boundary_col,
                        "boundary_id": boundary_id,
                        "relation": relation,
                        "weight": round(weight, 4),
                        "same_group": int(left["group"] == right["group"]),
                        "employer_i": left["employer_id"],
                        "employer_j": right["employer_id"],
                        "industry_i": left["industry"],
                        "industry_j": right["industry"],
                    }
                )
    columns = [
        "worker_i",
        "worker_j",
        "boundary_col",
        "boundary_id",
        "relation",
        "weight",
        "same_group",
        "employer_i",
        "employer_j",
        "industry_i",
        "industry_j",
    ]
    return pd.DataFrame(rows, columns=columns)


def component_map(worker_ids: list[str], edges: pd.DataFrame) -> dict[str, int]:
    neighbors: dict[str, set[str]] = {worker_id: set() for worker_id in worker_ids}
    for row in edges.itertuples(index=False):
        neighbors[row.worker_i].add(row.worker_j)
        neighbors[row.worker_j].add(row.worker_i)

    sizes: dict[str, int] = {}
    seen: set[str] = set()
    for worker_id in worker_ids:
        if worker_id in seen:
            continue
        queue: deque[str] = deque([worker_id])
        component: list[str] = []
        seen.add(worker_id)
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbor in neighbors[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        for member in component:
            sizes[member] = len(component)
    return sizes


def worker_metrics(
    workers: pd.DataFrame,
    edges: pd.DataFrame,
    boundary_col: str,
    relation_label: str,
) -> pd.DataFrame:
    """Create worker-level projected network summaries."""
    metrics = workers[
        [
            "worker_id",
            "group",
            "block_id",
            "neighborhood_id",
            "employer_id",
            "industry",
            "employed_next_year",
            "wage",
            "survey_response",
            "missing_link_risk",
            "outside_observed_frame",
        ]
    ].copy()
    metrics["degree"] = 0.0
    metrics["strength"] = 0.0
    metrics["same_group_edge_count"] = 0.0

    index = {worker_id: pos for pos, worker_id in enumerate(metrics["worker_id"])}
    for row in edges.itertuples(index=False):
        for worker in [row.worker_i, row.worker_j]:
            pos = index[worker]
            metrics.loc[pos, "degree"] += 1.0
            metrics.loc[pos, "strength"] += float(row.weight)
            metrics.loc[pos, "same_group_edge_count"] += float(row.same_group)

    peer_counts = workers.groupby(boundary_col)["worker_id"].transform("count") - 1
    metrics["local_peer_count"] = peer_counts.to_numpy(dtype=float)
    metrics["local_employer_exposure"] = np.where(
        metrics["local_peer_count"] > 0,
        metrics["degree"] / metrics["local_peer_count"],
        0.0,
    )
    metrics["weighted_local_exposure"] = np.where(
        metrics["local_peer_count"] > 0,
        metrics["strength"] / metrics["local_peer_count"],
        0.0,
    )
    metrics["same_group_edge_share"] = np.where(
        metrics["degree"] > 0,
        metrics["same_group_edge_count"] / metrics["degree"],
        np.nan,
    )
    components = component_map(metrics["worker_id"].tolist(), edges)
    metrics["component_size"] = metrics["worker_id"].map(components)
    metrics["relation_label"] = relation_label
    return metrics


def component_summary(metrics: pd.DataFrame) -> pd.DataFrame:
    counts = metrics.groupby("component_size", as_index=False).agg(worker_count=("worker_id", "count"))
    counts["component_type"] = np.where(counts["component_size"] == 1, "isolate", "connected_component")
    return counts.sort_values(["component_size", "worker_count"]).reset_index(drop=True)


def network_metric_summary(metrics: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for label, frame in [("all_workers", metrics), *list(metrics.groupby("group"))]:
        rows.append(
            {
                "group": label,
                "worker_count": int(len(frame)),
                "mean_degree": float(frame["degree"].mean()),
                "mean_strength": float(frame["strength"].mean()),
                "mean_local_employer_exposure": float(frame["local_employer_exposure"].mean()),
                "mean_weighted_local_exposure": float(frame["weighted_local_exposure"].mean()),
                "isolate_share": float((frame["degree"] == 0).mean()),
                "mean_component_size": float(frame["component_size"].mean()),
                "mean_same_group_edge_share": float(frame["same_group_edge_share"].mean(skipna=True)),
            }
        )
    return pd.DataFrame(rows).round(6)


def edge_density(worker_count: int, edge_count: int) -> float:
    possible = worker_count * (worker_count - 1) / 2
    if possible == 0:
        return 0.0
    return float(edge_count / possible)


def incident_edge_counts(edges: pd.DataFrame) -> pd.Series:
    counts: defaultdict[str, int] = defaultdict(int)
    for row in edges.itertuples(index=False):
        counts[row.worker_i] += 1
        counts[row.worker_j] += 1
    return pd.Series(counts, dtype=float)
