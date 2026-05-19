"""Reproduce a teaching-scale workplace peer-exposure design."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from network_causal_utils import add_peer_measures, fit_ols, hc1_cov, model_rows


def write_saturation_summary(data: pd.DataFrame, outdir: Path) -> None:
    untreated = data.loc[data["treated"] == 0].copy()
    untreated["high_graph_exposure"] = (
        untreated["graph_treated_share"] >= untreated["graph_treated_share"].median()
    ).astype(int)
    untreated_contrast = (
        untreated.groupby("high_graph_exposure", as_index=False)
        .agg(
            workers=("worker_id", "count"),
            mean_graph_treated_share=("graph_treated_share", "mean"),
            mean_productivity=("productivity", "mean"),
            mean_retention=("retained_next_period", "mean"),
        )
    )

    summary = (
        data.groupby(["team_id", "saturation_cell", "assigned_treatment_prob"], as_index=False)
        .agg(
            workers=("worker_id", "count"),
            treatment_rate=("treated", "mean"),
            mean_team_treated_share_loo=("team_treated_share_loo", "mean"),
            mean_graph_treated_share=("graph_treated_share", "mean"),
            mean_productivity=("productivity", "mean"),
            untreated_workers=("treated", lambda col: int((col == 0).sum())),
        )
        .sort_values(["assigned_treatment_prob", "team_id"])
    )
    summary.round(6).to_csv(outdir / "team_saturation_summary.csv", index=False)
    untreated_contrast.round(6).to_csv(outdir / "untreated_exposure_contrast.csv", index=False)


def estimate_direct_spillover(data: pd.DataFrame, outdir: Path) -> None:
    data = data.copy()
    data["senior"] = (data["role"] == "senior").astype(int)
    specs = [
        (
            "team_leave_one_out",
            ["treated", "team_treated_share_loo", "baseline_skill", "tenure_years", "senior"],
            "Direct treatment and spillover through leave-one-out team treated share.",
        ),
        (
            "graph_neighbors",
            ["treated", "graph_treated_share", "baseline_skill", "tenure_years", "senior"],
            "Direct treatment and spillover through observed coworker-neighbor exposure.",
        ),
        (
            "weighted_graph_neighbors",
            ["treated", "weighted_graph_treated_share", "baseline_skill", "tenure_years", "senior"],
            "Direct treatment and spillover through tie-strength-weighted exposure.",
        ),
    ]

    rows: list[dict[str, object]] = []
    exposure_rows: list[dict[str, object]] = []
    for spec_name, x_cols, note in specs:
        result = fit_ols(data, "productivity", x_cols)
        cov = hc1_cov(result)
        for row in model_rows(result, cov, "hc1"):
            row["specification"] = spec_name
            row["interpretation_note"] = note
            rows.append(row)

        exposure_col = x_cols[1]
        exposure_idx = result.variable_names.index(exposure_col)
        se = float(np.sqrt(max(np.diag(cov)[exposure_idx], 0.0)))
        exposure_rows.append(
            {
                "exposure_mapping": exposure_col,
                "spillover_estimate": float(result.beta[exposure_idx]),
                "std_error": se,
                "t_stat": float(result.beta[exposure_idx] / se) if se > 0 else np.nan,
                "what_it_identifies": "association between productivity and the specified treated-peer exposure, conditional on own treatment and controls",
                "main_failure_mode": "sorting, common shocks, or misspecified exposure mapping",
            }
        )

    pd.DataFrame(rows).round(6).to_csv(outdir / "direct_spillover_estimates.csv", index=False)
    pd.DataFrame(exposure_rows).round(6).to_csv(outdir / "exposure_mapping_estimates.csv", index=False)


def write_peer_measures(data: pd.DataFrame, outdir: Path) -> None:
    cols = [
        "worker_id",
        "team_id",
        "group",
        "role",
        "treated",
        "assigned_treatment_prob",
        "team_treated_share_loo",
        "graph_treated_share",
        "weighted_graph_treated_share",
        "treated_senior_neighbor",
        "team_peer_productivity_loo",
        "graph_peer_productivity",
        "productivity",
        "retained_next_period",
    ]
    data[cols].round(6).to_csv(outdir / "leave_one_out_peer_measures.csv", index=False)


def write_outputs(workers: pd.DataFrame, edges: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    data = add_peer_measures(workers, edges)

    write_peer_measures(data, outdir)
    write_saturation_summary(data, outdir)
    estimate_direct_spillover(data, outdir)

    manifest = {
        "task": "Week 19 network causal inference teaching reproduction",
        "worker_rows": int(len(workers)),
        "edge_rows": int(len(edges)),
        "team_count": int(workers["team_id"].nunique()),
        "not_official_replication": True,
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


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
    write_outputs(workers, edges, args.outdir)
    print(f"Wrote reproduce outputs to {args.outdir}")


if __name__ == "__main__":
    main()
