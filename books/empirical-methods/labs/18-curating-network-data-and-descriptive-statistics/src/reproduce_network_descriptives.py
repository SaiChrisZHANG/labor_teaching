"""Reproduce a teaching-scale neighborhood-employer network object."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from network_utils import (
    build_edges,
    component_summary,
    edge_density,
    network_metric_summary,
    ols_summary,
    worker_metrics,
)


def write_bipartite(workers: pd.DataFrame, outdir: Path) -> None:
    neighborhood_sizes = workers.groupby("neighborhood_id")["worker_id"].transform("count")
    table = (
        workers.assign(neighborhood_worker_count=neighborhood_sizes)
        .groupby(["neighborhood_id", "employer_id", "industry"], as_index=False)
        .agg(
            worker_count=("worker_id", "count"),
            neighborhood_worker_count=("neighborhood_worker_count", "first"),
            employed_next_year_rate=("employed_next_year", "mean"),
            mean_wage=("wage", "mean"),
            outside_observed_frame=("outside_observed_frame", "max"),
        )
    )
    table["neighborhood_employer_share"] = table["worker_count"] / table["neighborhood_worker_count"]
    table.sort_values(["neighborhood_id", "worker_count", "employer_id"], ascending=[True, False, True]).round(6).to_csv(
        outdir / "neighborhood_employer_bipartite.csv",
        index=False,
    )


def write_descriptive_relationships(metrics: pd.DataFrame, outdir: Path) -> None:
    rows = []
    for y_col in ["employed_next_year", "wage"]:
        for x_col in ["degree", "local_employer_exposure", "weighted_local_exposure", "component_size"]:
            stats = ols_summary(metrics, y_col, x_col)
            stats["interpretation_note"] = "descriptive association only; network formation is not exogenous"
            rows.append(stats)
    pd.DataFrame(rows).round(6).to_csv(outdir / "descriptive_relationship.csv", index=False)


def write_outputs(workers: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    edges = build_edges(workers, boundary_col="block_id", relation="same_employer")
    metrics = worker_metrics(workers, edges, boundary_col="block_id", relation_label="block_same_employer")

    write_bipartite(workers, outdir)
    edges.to_csv(outdir / "projected_worker_edges.csv", index=False)
    metrics.round(6).to_csv(outdir / "network_summary_by_worker.csv", index=False)
    network_metric_summary(metrics).to_csv(outdir / "network_metric_summary.csv", index=False)
    component_summary(metrics).to_csv(outdir / "graph_components.csv", index=False)
    write_descriptive_relationships(metrics, outdir)

    homophily = pd.DataFrame(
        [
            {
                "object": "projected worker-worker same-employer edges within residential block",
                "edge_count": int(len(edges)),
                "same_group_edge_share": float(edges["same_group"].mean()) if len(edges) else 0.0,
                "worker_count": int(len(workers)),
                "edge_density": edge_density(len(workers), len(edges)),
                "interpretation": "descriptive homophily; does not separate sorting from influence",
            }
        ]
    )
    homophily.round(6).to_csv(outdir / "homophily_summary.csv", index=False)

    manifest = {
        "task": "Week 18 network curation teaching reproduction",
        "worker_rows": int(len(workers)),
        "edge_rows": int(len(edges)),
        "neighborhood_count": int(workers["neighborhood_id"].nunique()),
        "employer_count": int(workers["employer_id"].nunique()),
        "not_official_replication": True,
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workers = pd.read_csv(args.workers)
    write_outputs(workers, args.outdir)
    print(f"Wrote reproduce outputs to {args.outdir}")


if __name__ == "__main__":
    main()
