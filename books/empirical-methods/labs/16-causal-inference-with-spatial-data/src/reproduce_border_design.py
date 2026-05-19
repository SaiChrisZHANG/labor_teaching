"""Estimate a synthetic contiguous-border design with spatial inference diagnostics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def build_design(df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
    controls = ["baseline_log_wage", "baseline_employment_rate", "manufacturing_share_1990"]
    pair_dummies = pd.get_dummies(df["pair_id"], prefix="pair", drop_first=True, dtype=float)
    pieces = [
        pd.Series(1.0, index=df.index, name="intercept"),
        df["treated_policy_side"].astype(float).rename("treated_policy_side"),
        df[controls].astype(float),
        pair_dummies,
    ]
    design = pd.concat(pieces, axis=1)
    return design.to_numpy(dtype=float), list(design.columns)


def ols_fit(y: np.ndarray, x: np.ndarray) -> dict[str, np.ndarray | float]:
    xtx_inv = np.linalg.pinv(x.T @ x)
    beta = xtx_inv @ x.T @ y
    resid = y - x @ beta
    n, k = x.shape
    sigma2 = float((resid @ resid) / max(n - k, 1))
    conventional = xtx_inv * sigma2
    return {"beta": beta, "resid": resid, "xtx_inv": xtx_inv, "conventional": conventional, "n": n, "k": k}


def robust_vcov(x: np.ndarray, resid: np.ndarray, xtx_inv: np.ndarray) -> np.ndarray:
    n, k = x.shape
    meat = x.T @ ((resid**2)[:, None] * x)
    scale = n / max(n - k, 1)
    return scale * xtx_inv @ meat @ xtx_inv


def distance_matrix(df: pd.DataFrame) -> np.ndarray:
    coords = df[["x_coord", "y_coord"]].to_numpy(dtype=float)
    diff = coords[:, None, :] - coords[None, :, :]
    return np.sqrt(np.sum(diff * diff, axis=2))


def conley_vcov(x: np.ndarray, resid: np.ndarray, xtx_inv: np.ndarray, distances: np.ndarray, cutoff: float) -> np.ndarray:
    if cutoff <= 0:
        return robust_vcov(x, resid, xtx_inv)
    weights = np.maximum(0.0, 1.0 - distances / cutoff)
    weights[distances > cutoff] = 0.0
    np.fill_diagonal(weights, 1.0)
    meat = x.T @ (weights * np.outer(resid, resid)) @ x
    return xtx_inv @ meat @ xtx_inv


def coefficient_row(
    label: str,
    beta: np.ndarray,
    vcov: np.ndarray,
    names: list[str],
    n: int,
    k: int,
) -> dict[str, float | str]:
    idx = names.index("treated_policy_side")
    se = float(np.sqrt(max(vcov[idx, idx], 0.0)))
    estimate = float(beta[idx])
    return {
        "specification": label,
        "term": "treated_policy_side",
        "estimate": estimate,
        "std_error": se,
        "t_stat": estimate / se if se > 0 else np.nan,
        "n": float(n),
        "parameters": float(k),
    }


def write_outputs(counties: pd.DataFrame, links: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    df = counties.sort_values(["pair_id", "side"]).reset_index(drop=True)
    y = df["employment_growth_2000_2010"].to_numpy(dtype=float)
    x, names = build_design(df)
    fit = ols_fit(y, x)
    beta = np.asarray(fit["beta"])
    resid = np.asarray(fit["resid"])
    xtx_inv = np.asarray(fit["xtx_inv"])
    conventional = np.asarray(fit["conventional"])
    robust = robust_vcov(x, resid, xtx_inv)
    distances = distance_matrix(df)
    conley_50 = conley_vcov(x, resid, xtx_inv, distances, 50.0)

    rows = [
        coefficient_row("conventional_pair_fe", beta, conventional, names, int(fit["n"]), int(fit["k"])),
        coefficient_row("hc1_pair_fe", beta, robust, names, int(fit["n"]), int(fit["k"])),
        coefficient_row("conley_50_mile_pair_fe", beta, conley_50, names, int(fit["n"]), int(fit["k"])),
    ]
    pd.DataFrame(rows).round(6).to_csv(outdir / "border_design_estimates.csv", index=False)

    cutoff_rows = []
    for cutoff in [0.0, 25.0, 50.0, 75.0, 100.0]:
        vcov = conley_vcov(x, resid, xtx_inv, distances, cutoff)
        row = coefficient_row(f"cutoff_{int(cutoff)}_miles", beta, vcov, names, int(fit["n"]), int(fit["k"]))
        row["cutoff_miles"] = cutoff
        cutoff_rows.append(row)
    pd.DataFrame(cutoff_rows).round(6).to_csv(outdir / "conley_cutoff_sensitivity.csv", index=False)

    analysis = df.copy()
    analysis["fitted_value"] = x @ beta
    analysis["residual"] = resid
    analysis.to_csv(outdir / "analysis_dataset.csv", index=False)

    manifest = {
        "task": "Week 16 synthetic contiguous-border design",
        "county_rows": int(len(counties)),
        "border_pairs": int(counties["pair_id"].nunique()),
        "link_rows": int(len(links)),
        "not_official_replication": True,
        "primary_anchor": "Dube, Lester, and Reich contiguous-border logic",
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote border-design outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--counties", required=True, type=Path)
    parser.add_argument("--links", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    counties = pd.read_csv(args.counties)
    links = pd.read_csv(args.links)
    write_outputs(counties, links, args.outdir)


if __name__ == "__main__":
    main()
