"""Diagnose sensitivity to network construction choices."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from network_utils import build_edges, edge_density, network_metric_summary, ols_summary, worker_metrics


DEFINITIONS = [
    {
        "definition": "block_same_employer",
        "boundary_col": "block_id",
        "relation": "same_employer",
        "exclude_outside": False,
        "mechanism": "nearby residents share employer-specific job information",
    },
    {
        "definition": "neighborhood_same_employer",
        "boundary_col": "neighborhood_id",
        "relation": "same_employer",
        "exclude_outside": False,
        "mechanism": "broader neighborhood job-information network",
    },
    {
        "definition": "block_same_industry",
        "boundary_col": "block_id",
        "relation": "same_industry",
        "exclude_outside": False,
        "mechanism": "nearby residents share industry information rather than firm contacts",
    },
    {
        "definition": "neighborhood_same_industry",
        "boundary_col": "neighborhood_id",
        "relation": "same_industry",
        "exclude_outside": False,
        "mechanism": "broad local industry opportunity set",
    },
    {
        "definition": "block_same_employer_inside_frame",
        "boundary_col": "block_id",
        "relation": "same_employer",
        "exclude_outside": True,
        "mechanism": "same as baseline but drops outside-frame employers",
    },
]


def summarize_definition(workers: pd.DataFrame, definition: dict[str, object]) -> dict[str, object]:
    edges = build_edges(
        workers,
        boundary_col=str(definition["boundary_col"]),
        relation=str(definition["relation"]),
        exclude_outside=bool(definition["exclude_outside"]),
    )
    metrics = worker_metrics(
        workers,
        edges,
        boundary_col=str(definition["boundary_col"]),
        relation_label=str(definition["definition"]),
    )
    slope = ols_summary(metrics, "employed_next_year", "local_employer_exposure")
    return {
        "definition": definition["definition"],
        "boundary_col": definition["boundary_col"],
        "relation": definition["relation"],
        "exclude_outside": int(bool(definition["exclude_outside"])),
        "mechanism": definition["mechanism"],
        "worker_count": int(len(workers)),
        "edge_count": int(len(edges)),
        "edge_density": edge_density(len(workers), len(edges)),
        "mean_degree": float(metrics["degree"].mean()),
        "mean_strength": float(metrics["strength"].mean()),
        "mean_local_exposure": float(metrics["local_employer_exposure"].mean()),
        "isolate_share": float((metrics["degree"] == 0).mean()),
        "largest_component_size": int(metrics["component_size"].max()),
        "descriptive_slope_employment_on_exposure": slope["slope"],
    }


def write_missing_link_audit(workers: pd.DataFrame, baseline_metrics: pd.DataFrame, outdir: Path) -> None:
    audit = (
        baseline_metrics.merge(
            workers[["worker_id", "missing_link_score", "skill_index", "tenure_years"]],
            on="worker_id",
            how="left",
        )
        .groupby(["group", "survey_response", "missing_link_risk"], as_index=False)
        .agg(
            worker_count=("worker_id", "count"),
            mean_missing_link_score=("missing_link_score", "mean"),
            mean_degree=("degree", "mean"),
            mean_local_exposure=("local_employer_exposure", "mean"),
            employed_next_year_rate=("employed_next_year", "mean"),
        )
    )
    audit.round(6).to_csv(outdir / "missing_link_audit.csv", index=False)


def write_projection_audit(workers: pd.DataFrame, outdir: Path) -> None:
    rows = []
    for employer_id, group in workers.groupby("employer_id", sort=True):
        firm_size = len(group)
        projected_pairs = firm_size * (firm_size - 1) / 2
        rows.append(
            {
                "employer_id": employer_id,
                "industry": group["industry"].iloc[0],
                "firm_size": firm_size,
                "projected_worker_pairs_if_all_connected": int(projected_pairs),
                "outside_observed_frame": int(group["outside_observed_frame"].max()),
                "group_b_share": float((group["group"] == "B").mean()),
                "warning": "large employers mechanically create many projected worker-worker links",
            }
        )
    pd.DataFrame(rows).sort_values("projected_worker_pairs_if_all_connected", ascending=False).round(6).to_csv(
        outdir / "projection_audit.csv",
        index=False,
    )


def write_boundary_audit(workers: pd.DataFrame, outdir: Path) -> None:
    rows = []
    for exclude_outside in [False, True]:
        edges = build_edges(workers, "block_id", "same_employer", exclude_outside=exclude_outside)
        metrics = worker_metrics(
            workers,
            edges,
            boundary_col="block_id",
            relation_label="inside_only" if exclude_outside else "all_employers",
        )
        rows.append(
            {
                "graph_frame": "inside_frame_only" if exclude_outside else "all_observed_employers",
                "edge_count": int(len(edges)),
                "mean_degree": float(metrics["degree"].mean()),
                "isolate_share": float((metrics["degree"] == 0).mean()),
                "outside_worker_count": int(workers["outside_observed_frame"].sum()),
                "interpretation": "boundary choice changes whether outside employers can create local ties",
            }
        )
    pd.DataFrame(rows).round(6).to_csv(outdir / "boundary_truncation_audit.csv", index=False)


def write_prompts(outdir: Path) -> None:
    prompts = pd.DataFrame(
        [
            {
                "diagnostic": "edge_rule",
                "prompt": "Which edge definition best matches job-information flow rather than common industry exposure?",
            },
            {
                "diagnostic": "boundary",
                "prompt": "Do outside-frame employers create ties that the observed graph should include or suppress?",
            },
            {
                "diagnostic": "missing_links",
                "prompt": "Which group has the highest missing-link risk, and how would that bias degree?",
            },
            {
                "diagnostic": "projection",
                "prompt": "Are projected worker-worker links mainly generated by large employers?",
            },
            {
                "diagnostic": "causal_boundary",
                "prompt": "Which checks diagnose measurement sensitivity, and which would be needed for causal interpretation?",
            },
        ]
    )
    prompts.to_csv(outdir / "diagnostic_prompts.csv", index=False)


def write_outputs(workers: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    rows = [summarize_definition(workers, definition) for definition in DEFINITIONS]
    pd.DataFrame(rows).round(6).to_csv(outdir / "definition_sensitivity.csv", index=False)

    baseline_edges = build_edges(workers, "block_id", "same_employer")
    baseline_metrics = worker_metrics(workers, baseline_edges, "block_id", "block_same_employer")
    network_metric_summary(baseline_metrics).to_csv(outdir / "diagnostic_baseline_metric_summary.csv", index=False)

    write_missing_link_audit(workers, baseline_metrics, outdir)
    write_projection_audit(workers, outdir)
    write_boundary_audit(workers, outdir)
    write_prompts(outdir)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workers = pd.read_csv(args.workers)
    write_outputs(workers, args.outdir)
    print(f"Wrote diagnostic outputs to {args.outdir}")


if __name__ == "__main__":
    main()
