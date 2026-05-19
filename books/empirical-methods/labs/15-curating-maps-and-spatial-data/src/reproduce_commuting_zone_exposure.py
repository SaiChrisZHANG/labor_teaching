"""Construct a Week 15 commuting-zone exposure object from synthetic data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def sector_columns(df: pd.DataFrame) -> list[str]:
    return [column for column in df.columns if column.startswith("emp_") and column.endswith("_1990")]


def exposure_by_geography(tracts: pd.DataFrame, shocks: pd.DataFrame, geography: str) -> pd.DataFrame:
    cols = sector_columns(tracts)
    shock_map = shocks.set_index("sector")["trade_shock"].to_dict()
    grouped = tracts.groupby(geography, as_index=False)[cols + ["baseline_employment_1990", "population_1990"]].sum()
    for col in cols:
        sector = col.removeprefix("emp_").removesuffix("_1990")
        grouped[f"share_{sector}"] = grouped[col] / grouped["baseline_employment_1990"]
    grouped["exposure"] = 0.0
    for col in cols:
        sector = col.removeprefix("emp_").removesuffix("_1990")
        grouped["exposure"] += grouped[f"share_{sector}"] * float(shock_map[sector])
    grouped = grouped.rename(columns={geography: "geography_id"})
    grouped.insert(0, "geography", geography)
    keep_cols = ["geography", "geography_id", "baseline_employment_1990", "population_1990", "exposure"]
    keep_cols += [f"share_{col.removeprefix('emp_').removesuffix('_1990')}" for col in cols]
    return grouped[keep_cols].sort_values(["geography", "geography_id"]).reset_index(drop=True)


def weighted_outcome_by_geography(tracts: pd.DataFrame, geography: str) -> pd.DataFrame:
    rows = []
    for group_id, group in tracts.groupby(geography):
        weights = group["baseline_employment_1990"].to_numpy(dtype=float)
        rows.append(
            {
                "geography_id": group_id,
                "employment_growth_2000_2010": float(
                    np.average(group["employment_growth_2000_2010"], weights=weights)
                ),
                "tract_count": int(len(group)),
            }
        )
    return pd.DataFrame(rows)


def ols_slope(df: pd.DataFrame, y_col: str, x_col: str, weight_col: str | None = None) -> dict[str, float]:
    y = df[y_col].to_numpy(dtype=float)
    x = df[x_col].to_numpy(dtype=float)
    design = np.column_stack([np.ones(len(df)), x])
    if weight_col is None:
        beta = np.linalg.lstsq(design, y, rcond=None)[0]
    else:
        weights = np.sqrt(df[weight_col].to_numpy(dtype=float))
        beta = np.linalg.lstsq(design * weights[:, None], y * weights, rcond=None)[0]
    fitted = design @ beta
    residual = y - fitted
    return {
        "intercept": float(beta[0]),
        "slope": float(beta[1]),
        "mean_outcome": float(y.mean()),
        "mean_exposure": float(x.mean()),
        "rmse": float(np.sqrt(np.mean(residual**2))),
        "n": float(len(df)),
    }


def write_outputs(tracts: pd.DataFrame, shocks: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    cz = exposure_by_geography(tracts, shocks, "cz_id")
    county = exposure_by_geography(tracts, shocks, "county_id")
    cz.to_csv(outdir / "cz_exposure.csv", index=False)
    county.to_csv(outdir / "county_exposure.csv", index=False)

    cz_map = cz.set_index("geography_id")["exposure"]
    county_map = county.set_index("geography_id")["exposure"]
    assigned = tracts[
        [
            "tract_id",
            "county_id",
            "cz_id",
            "baseline_employment_1990",
            "population_1990",
            "employment_growth_2000_2010",
            "geocode_quality",
        ]
    ].copy()
    assigned["cz_exposure"] = assigned["cz_id"].map(cz_map)
    assigned["county_exposure"] = assigned["county_id"].map(county_map)
    assigned["exposure_difference_county_minus_cz"] = assigned["county_exposure"] - assigned["cz_exposure"]
    assigned.to_csv(outdir / "tract_exposure_assignment.csv", index=False)

    compare = assigned.groupby(["cz_id", "county_id"], as_index=False).agg(
        tract_count=("tract_id", "count"),
        baseline_employment_1990=("baseline_employment_1990", "sum"),
        mean_cz_exposure=("cz_exposure", "mean"),
        mean_county_exposure=("county_exposure", "mean"),
    )
    compare["county_minus_cz"] = compare["mean_county_exposure"] - compare["mean_cz_exposure"]
    compare.to_csv(outdir / "county_vs_cz_exposure.csv", index=False)

    cz_outcome = weighted_outcome_by_geography(tracts, "cz_id").merge(
        cz[["geography_id", "exposure"]],
        on="geography_id",
    )
    county_outcome = weighted_outcome_by_geography(tracts, "county_id").merge(
        county[["geography_id", "exposure"]],
        on="geography_id",
    )
    downstream_rows = []
    tract_cz = assigned.rename(columns={"cz_exposure": "exposure"})
    tract_county = assigned.rename(columns={"county_exposure": "exposure"})
    for label, frame, weight_col in [
        ("tract_rows_with_cz_exposure", tract_cz, "baseline_employment_1990"),
        ("tract_rows_with_county_exposure", tract_county, "baseline_employment_1990"),
        ("cz_aggregated_rows", cz_outcome, None),
        ("county_aggregated_rows", county_outcome, None),
    ]:
        stats = ols_slope(frame, "employment_growth_2000_2010", "exposure", weight_col=weight_col)
        stats["specification"] = label
        downstream_rows.append(stats)
    pd.DataFrame(downstream_rows)[
        ["specification", "n", "intercept", "slope", "mean_outcome", "mean_exposure", "rmse"]
    ].round(6).to_csv(outdir / "downstream_comparison.csv", index=False)

    estimand_summary = pd.DataFrame(
        [
            {
                "object": "commuting-zone exposure",
                "primary_geography": "cz_id",
                "estimand_claim": "local labor-market exposure using baseline industry mix",
                "main_caveat": "requires commuting zones to proxy functional labor markets",
            },
            {
                "object": "county exposure",
                "primary_geography": "county_id",
                "estimand_claim": "administrative county exposure using the same industry shocks",
                "main_caveat": "counties may split or combine functional labor markets",
            },
            {
                "object": "tract assignment",
                "primary_geography": "tract_id with inherited market exposure",
                "estimand_claim": "tract outcomes exposed through their assigned local labor market",
                "main_caveat": "tract precision can exceed the precision of the market-level shock",
            },
        ]
    )
    estimand_summary.to_csv(outdir / "geography_estimand_summary.csv", index=False)

    manifest = {
        "task": "Week 15 commuting-zone exposure teaching reproduction",
        "tract_rows": int(len(tracts)),
        "cz_count": int(tracts["cz_id"].nunique()),
        "county_count": int(tracts["county_id"].nunique()),
        "sector_count": int(len(shocks)),
        "not_official_replication": True,
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracts", required=True, type=Path)
    parser.add_argument("--shocks", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracts = pd.read_csv(args.tracts)
    shocks = pd.read_csv(args.shocks)
    write_outputs(tracts, shocks, args.outdir)
    print(f"Wrote reproduce outputs to {args.outdir}")


if __name__ == "__main__":
    main()
