"""Transfer Week 15 spatial curation logic to job-access measurement."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def pairwise_access(residences: pd.DataFrame, centers: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, residence in residences.iterrows():
        for _, center in centers.iterrows():
            distance = float(
                np.sqrt(
                    (residence["x_coord"] - center["x_coord"]) ** 2
                    + (residence["y_coord"] - center["y_coord"]) ** 2
                )
            )
            transit_penalty = 8.0 * int(residence["transit_dependency"]) * int(center["suburban_center"])
            outside_penalty = 5.0 * int(center["outside_study_frame"])
            travel_time = 7.5 + 1.35 * distance + transit_penalty + outside_penalty
            generalized_cost = 0.38 * travel_time + 0.06 * distance + 1.10 * int(center["suburban_center"])
            rows.append(
                {
                    "residence_tract_id": residence["residence_tract_id"],
                    "job_center_id": center["job_center_id"],
                    "jobs": center["jobs"],
                    "sector": center["sector"],
                    "suburban_center": center["suburban_center"],
                    "outside_study_frame": center["outside_study_frame"],
                    "distance_miles": distance,
                    "travel_time_minutes": travel_time,
                    "generalized_cost": generalized_cost,
                    "within_8_miles": int(distance <= 8.0),
                    "within_15_miles": int(distance <= 15.0),
                    "kernel_weight": float(np.exp(-distance / 10.0)),
                    "travel_time_weight": float(np.exp(-0.055 * travel_time)),
                    "generalized_cost_weight": float(np.exp(-0.090 * generalized_cost)),
                }
            )
    return pd.DataFrame(rows)


def write_outputs(residences: pd.DataFrame, centers: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    pairs = pairwise_access(residences, centers)

    access_rows = []
    for residence_id, group in pairs.groupby("residence_tract_id"):
        access_rows.append(
            {
                "residence_tract_id": residence_id,
                "buffer_jobs_8_miles": float((group["jobs"] * group["within_8_miles"]).sum()),
                "buffer_jobs_15_miles": float((group["jobs"] * group["within_15_miles"]).sum()),
                "distance_decay_jobs": float((group["jobs"] * group["kernel_weight"]).sum()),
                "travel_time_jobs": float((group["jobs"] * group["travel_time_weight"]).sum()),
                "generalized_cost_jobs": float((group["jobs"] * group["generalized_cost_weight"]).sum()),
                "outside_frame_jobs_in_full_matrix": float((group["jobs"] * group["outside_study_frame"]).sum()),
                "nearest_job_center_miles": float(group["distance_miles"].min()),
                "mean_travel_time_to_jobs": float(np.average(group["travel_time_minutes"], weights=group["jobs"])),
            }
        )
    access = pd.DataFrame(access_rows).merge(residences, on="residence_tract_id", how="left")
    access["high_black_share"] = (access["black_share"] >= access["black_share"].median()).astype(int)
    access.round(6).to_csv(outdir / "job_access_measures.csv", index=False)

    group_rows = []
    for label, group in [
        ("all", access),
        ("high_black_share", access.loc[access["high_black_share"] == 1]),
        ("low_black_share", access.loc[access["high_black_share"] == 0]),
        ("transit_dependent", access.loc[access["transit_dependency"] == 1]),
        ("not_transit_dependent", access.loc[access["transit_dependency"] == 0]),
    ]:
        weights = group["resident_count"].to_numpy(dtype=float)
        group_rows.append(
            {
                "group": label,
                "tracts": int(len(group)),
                "resident_count": int(group["resident_count"].sum()),
                "buffer_jobs_8_miles": float(np.average(group["buffer_jobs_8_miles"], weights=weights)),
                "buffer_jobs_15_miles": float(np.average(group["buffer_jobs_15_miles"], weights=weights)),
                "distance_decay_jobs": float(np.average(group["distance_decay_jobs"], weights=weights)),
                "travel_time_jobs": float(np.average(group["travel_time_jobs"], weights=weights)),
                "generalized_cost_jobs": float(np.average(group["generalized_cost_jobs"], weights=weights)),
                "mean_travel_time_to_jobs": float(np.average(group["mean_travel_time_to_jobs"], weights=weights)),
            }
        )
    pd.DataFrame(group_rows).round(6).to_csv(outdir / "access_group_comparison.csv", index=False)

    selected_pairs = pairs.sort_values(["residence_tract_id", "generalized_cost"]).groupby("residence_tract_id").head(3)
    selected_pairs.round(6).to_csv(outdir / "distance_decay_weights.csv", index=False)

    comparison = access[
        [
            "residence_tract_id",
            "buffer_jobs_8_miles",
            "buffer_jobs_15_miles",
            "distance_decay_jobs",
            "travel_time_jobs",
            "generalized_cost_jobs",
            "transit_dependency",
            "black_share",
        ]
    ].copy()
    comparison["kernel_minus_8_mile_buffer"] = comparison["distance_decay_jobs"] - comparison["buffer_jobs_8_miles"]
    comparison["travel_time_minus_distance_decay"] = comparison["travel_time_jobs"] - comparison["distance_decay_jobs"]
    comparison.round(6).to_csv(outdir / "buffer_vs_kernel_access.csv", index=False)

    edge_rows = []
    for residence_id, frame in pairs.groupby("residence_tract_id"):
        inside = frame.loc[frame["outside_study_frame"] == 0]
        edge_rows.append(
            {
                "residence_tract_id": residence_id,
                "full_distance_decay_jobs": float((frame["jobs"] * frame["kernel_weight"]).sum()),
                "inside_frame_distance_decay_jobs": float((inside["jobs"] * inside["kernel_weight"]).sum()),
                "outside_centers_relevant": int((frame["outside_study_frame"] == 1).any()),
            }
        )
    full_access = pd.DataFrame(edge_rows)
    full_access["omitted_outside_access"] = (
        full_access["full_distance_decay_jobs"] - full_access["inside_frame_distance_decay_jobs"]
    )
    full_access.round(6).to_csv(outdir / "edge_effect_audit.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "object": "8-mile buffer",
                "design_question": "Is a hard radius plausible for the actual commuting or search mechanism?",
                "main_caveat": "Buffers ignore route topology and treat nearby jobs just outside the radius as zero.",
            },
            {
                "object": "distance-decay access",
                "design_question": "What bandwidth or decay rate matches worker search and commute behavior?",
                "main_caveat": "Kernel access can look precise while hiding an arbitrary bandwidth.",
            },
            {
                "object": "travel-time access",
                "design_question": "Do routing mode, departure time, and transit penalties match the population?",
                "main_caveat": "Routing data and APIs must be versioned or preserved.",
            },
            {
                "object": "generalized-cost access",
                "design_question": "Are time, distance, transfers, and suburban penalties monetized or utility-weighted defensibly?",
                "main_caveat": "Cost parameters should be justified or varied in sensitivity checks.",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)

    manifest = {
        "task": "Week 15 job-access transfer teaching workflow",
        "residence_tracts": int(len(residences)),
        "job_centers": int(len(centers)),
        "not_live_routing": True,
        "not_official_replication": True,
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--residences", required=True, type=Path)
    parser.add_argument("--centers", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    residences = pd.read_csv(args.residences)
    centers = pd.read_csv(args.centers)
    write_outputs(residences, centers, args.outdir)
    print(f"Wrote transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
