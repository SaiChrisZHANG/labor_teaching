"""Diagnose geography, crosswalk, and geocoding choices for Week 15."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def sector_columns(df: pd.DataFrame) -> list[str]:
    return [column for column in df.columns if column.startswith("emp_") and column.endswith("_1990")]


def exposure_by_geography(tracts: pd.DataFrame, shocks: pd.DataFrame, geography: str) -> pd.DataFrame:
    cols = sector_columns(tracts)
    shock_map = shocks.set_index("sector")["trade_shock"].to_dict()
    grouped = tracts.groupby(geography, as_index=False)[cols + ["baseline_employment_1990"]].sum()
    grouped["exposure"] = 0.0
    for col in cols:
        sector = col.removeprefix("emp_").removesuffix("_1990")
        grouped["exposure"] += (grouped[col] / grouped["baseline_employment_1990"]) * float(shock_map[sector])
    return grouped[[geography, "exposure"]]


def weighted_mean(frame: pd.DataFrame, value_col: str, weight_col: str) -> float:
    weights = frame[weight_col].to_numpy(dtype=float)
    values = frame[value_col].to_numpy(dtype=float)
    if weights.sum() == 0:
        return float("nan")
    return float(np.average(values, weights=weights))


def county_crosswalk_summary(tracts: pd.DataFrame, crosswalk: pd.DataFrame, weight_col: str) -> pd.DataFrame:
    merged = crosswalk.merge(
        tracts[["tract_id", "low_income_share_1990", "population_1990", "baseline_employment_1990"]],
        left_on="source_tract_id",
        right_on="tract_id",
        how="left",
    )
    merged["effective_weight"] = merged[weight_col] * merged["population_1990"]
    rows = []
    for county, group in merged.groupby("target_county_id"):
        rows.append(
            {
                "target_county_id": county,
                "weight_rule": weight_col,
                "low_income_share_1990": weighted_mean(group, "low_income_share_1990", "effective_weight"),
                "allocated_population": float(group["effective_weight"].sum()),
                "split_source_units": int(group["is_split_unit"].sum()),
            }
        )
    return pd.DataFrame(rows)


def nearest_centroid(x: np.ndarray, y: np.ndarray, centroids: pd.DataFrame) -> tuple[str, float]:
    dx = centroids["x_coord"].to_numpy(dtype=float) - float(x)
    dy = centroids["y_coord"].to_numpy(dtype=float) - float(y)
    distances = np.sqrt(dx**2 + dy**2)
    idx = int(np.argmin(distances))
    return str(centroids.iloc[idx]["cz_id"]), float(distances[idx])


def write_outputs(tracts: pd.DataFrame, shocks: pd.DataFrame, crosswalk: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    cz = exposure_by_geography(tracts, shocks, "cz_id").rename(columns={"exposure": "cz_exposure"})
    county = exposure_by_geography(tracts, shocks, "county_id").rename(columns={"exposure": "county_exposure"})
    assigned = tracts[["tract_id", "county_id", "cz_id", "baseline_employment_1990", "geocode_quality"]].copy()
    assigned = assigned.merge(cz, on="cz_id").merge(county, on="county_id")
    assigned["county_minus_cz"] = assigned["county_exposure"] - assigned["cz_exposure"]
    corr = float(np.corrcoef(assigned["cz_exposure"], assigned["county_exposure"])[0, 1])
    maup = pd.DataFrame(
        [
            {
                "diagnostic": "correlation_between_cz_and_county_exposure",
                "value": corr,
                "interpretation": "Lower values mean geography choice changes the exposure ranking.",
            },
            {
                "diagnostic": "mean_absolute_county_minus_cz",
                "value": float(assigned["county_minus_cz"].abs().mean()),
                "interpretation": "Average tract-level exposure shift from changing geography.",
            },
            {
                "diagnostic": "p90_absolute_county_minus_cz",
                "value": float(assigned["county_minus_cz"].abs().quantile(0.90)),
                "interpretation": "Large upper-tail values flag sensitive places.",
            },
        ]
    )
    maup.round(6).to_csv(outdir / "maup_sensitivity.csv", index=False)

    area_summary = county_crosswalk_summary(tracts, crosswalk, "area_weight")
    pop_summary = county_crosswalk_summary(tracts, crosswalk, "population_weight")
    emp_summary = county_crosswalk_summary(tracts, crosswalk, "employment_weight")
    cross_summary = pd.concat([area_summary, pop_summary, emp_summary], ignore_index=True)
    pivot = cross_summary.pivot(index="target_county_id", columns="weight_rule", values="low_income_share_1990").reset_index()
    pivot["population_minus_area"] = pivot["population_weight"] - pivot["area_weight"]
    pivot["employment_minus_area"] = pivot["employment_weight"] - pivot["area_weight"]
    pivot.to_csv(outdir / "crosswalk_weighting_sensitivity.csv", index=False)

    centroids = tracts.groupby("cz_id", as_index=False).agg(x_coord=("x_coord", "mean"), y_coord=("y_coord", "mean"))
    jitter_rows = []
    for idx, row in tracts.iterrows():
        angle = 0.73 * (idx + 1)
        masked_x = float(row["x_coord"] + row["jitter_radius_miles"] * np.cos(angle))
        masked_y = float(row["y_coord"] + row["jitter_radius_miles"] * np.sin(angle))
        original_nearest, original_distance = nearest_centroid(row["x_coord"], row["y_coord"], centroids)
        masked_nearest, masked_distance = nearest_centroid(masked_x, masked_y, centroids)
        jitter_rows.append(
            {
                "tract_id": row["tract_id"],
                "geocode_quality": row["geocode_quality"],
                "jitter_radius_miles": row["jitter_radius_miles"],
                "original_nearest_cz": original_nearest,
                "masked_nearest_cz": masked_nearest,
                "nearest_cz_changed": int(original_nearest != masked_nearest),
                "distance_change_miles": masked_distance - original_distance,
            }
        )
    jitter = pd.DataFrame(jitter_rows)
    jitter.to_csv(outdir / "geocoding_jitter_sensitivity.csv", index=False)

    edge_rows = []
    centroid_array = centroids.set_index("cz_id")
    for _, row in tracts.iterrows():
        distances = []
        for cz_id, centroid in centroid_array.iterrows():
            distance = float(np.sqrt((row["x_coord"] - centroid["x_coord"]) ** 2 + (row["y_coord"] - centroid["y_coord"]) ** 2))
            distances.append((cz_id, distance))
        distances = sorted(distances, key=lambda item: item[1])
        edge_rows.append(
            {
                "tract_id": row["tract_id"],
                "assigned_cz": row["cz_id"],
                "nearest_cz": distances[0][0],
                "nearest_distance": distances[0][1],
                "second_nearest_cz": distances[1][0],
                "second_nearest_distance": distances[1][1],
                "edge_margin": distances[1][1] - distances[0][1],
                "near_edge_flag": int((distances[1][1] - distances[0][1]) < 5.0),
                "split_unit_flag": int(row["tract_id"] in set(crosswalk.loc[crosswalk["is_split_unit"] == 1, "source_tract_id"])),
            }
        )
    pd.DataFrame(edge_rows).round(6).to_csv(outdir / "boundary_edge_audit.csv", index=False)

    support = assigned.groupby("geocode_quality", as_index=False).agg(
        tracts=("tract_id", "count"),
        mean_abs_county_minus_cz=("county_minus_cz", lambda value: float(np.mean(np.abs(value)))),
        mean_cz_exposure=("cz_exposure", "mean"),
        mean_county_exposure=("county_exposure", "mean"),
    )
    support.to_csv(outdir / "support_comparability.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "diagnostic": "MAUP",
                "student_prompt": "Which substantive claim changes if the same shock is assigned at county rather than commuting-zone level?",
            },
            {
                "diagnostic": "crosswalk",
                "student_prompt": "Would area, population, employment, or commuting-flow weights best match the mechanism?",
            },
            {
                "diagnostic": "geocoding",
                "student_prompt": "Which locations should be manually audited or routed to a secure-data workflow?",
            },
            {
                "diagnostic": "edge effects",
                "student_prompt": "Which tracts may be exposed to opportunities outside the assigned geography?",
            },
            {
                "diagnostic": "curation versus causality",
                "student_prompt": "Which diagnostics validate measurement, and which causal assumptions remain untested?",
            },
        ]
    )
    prompts.to_csv(outdir / "diagnostic_prompts.csv", index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracts", required=True, type=Path)
    parser.add_argument("--shocks", required=True, type=Path)
    parser.add_argument("--crosswalk", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracts = pd.read_csv(args.tracts)
    shocks = pd.read_csv(args.shocks)
    crosswalk = pd.read_csv(args.crosswalk)
    write_outputs(tracts, shocks, crosswalk, args.outdir)
    print(f"Wrote diagnostic outputs to {args.outdir}")


if __name__ == "__main__":
    main()
