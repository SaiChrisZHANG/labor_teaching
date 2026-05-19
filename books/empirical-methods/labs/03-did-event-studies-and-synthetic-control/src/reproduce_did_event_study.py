"""Run the Week 3 DID and modern DID teaching workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week3_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week3_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def ols_beta(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return beta


def homoskedastic_se(y: np.ndarray, x: np.ndarray, beta: np.ndarray) -> np.ndarray:
    residual = y - x @ beta
    n, k = x.shape
    sigma2 = float(residual @ residual / max(n - k, 1))
    cov = sigma2 * np.linalg.inv(x.T @ x)
    return np.sqrt(np.diag(cov))


def cluster_se(y: np.ndarray, x: np.ndarray, beta: np.ndarray, clusters: np.ndarray) -> np.ndarray:
    residual = y - x @ beta
    xtx_inv = np.linalg.inv(x.T @ x)
    meat = np.zeros((x.shape[1], x.shape[1]))
    for cluster in pd.unique(clusters):
        idx = clusters == cluster
        score = x[idx, :].T @ residual[idx]
        meat += np.outer(score, score)
    cov = xtx_inv @ meat @ xtx_inv
    return np.sqrt(np.maximum(np.diag(cov), 0.0))


def two_way_residualize(df: pd.DataFrame, value_col: str, unit_col: str, time_col: str) -> np.ndarray:
    values = df[value_col].to_numpy(dtype=float)
    unit_mean = df.groupby(unit_col)[value_col].transform("mean").to_numpy(dtype=float)
    time_mean = df.groupby(time_col)[value_col].transform("mean").to_numpy(dtype=float)
    grand_mean = float(df[value_col].mean())
    return values - unit_mean - time_mean + grand_mean


def analyze_card_krueger(df: pd.DataFrame, outdir: Path) -> float:
    state_paths = (
        df.groupby(["state", "treated_state", "post"], as_index=False)
        .agg(mean_fte=("fte_employment", "mean"), n=("restaurant_id", "nunique"))
        .sort_values(["treated_state", "post"])
    )
    state_paths["period"] = state_paths["post"].map({0: "pre", 1: "post"})
    state_paths.to_csv(outdir / "card_krueger_state_paths.csv", index=False)

    treated_change = float(
        state_paths.loc[(state_paths["treated_state"] == 1) & (state_paths["post"] == 1), "mean_fte"].iloc[0]
        - state_paths.loc[(state_paths["treated_state"] == 1) & (state_paths["post"] == 0), "mean_fte"].iloc[0]
    )
    control_change = float(
        state_paths.loc[(state_paths["treated_state"] == 0) & (state_paths["post"] == 1), "mean_fte"].iloc[0]
        - state_paths.loc[(state_paths["treated_state"] == 0) & (state_paths["post"] == 0), "mean_fte"].iloc[0]
    )
    did = treated_change - control_change

    y = df["fte_employment"].to_numpy(dtype=float)
    x = np.column_stack(
        [
            np.ones(len(df)),
            df["treated_state"].to_numpy(dtype=float),
            df["post"].to_numpy(dtype=float),
            df["treated_post"].to_numpy(dtype=float),
        ]
    )
    beta = ols_beta(y, x)
    naive = homoskedastic_se(y, x, beta)
    state_cluster = cluster_se(y, x, beta, df["state"].to_numpy())
    restaurant_cluster = cluster_se(y, x, beta, df["restaurant_id"].to_numpy())
    state_cluster_note = "not reported: only two policy clusters"
    state_clustered_se = np.nan if df["state"].nunique() < 10 else float(state_cluster[3])

    estimates = pd.DataFrame(
        [
            {
                "estimand": "treated pre-post change",
                "estimate": treated_change,
                "interpretation": "change in NJ restaurants after the policy date",
            },
            {
                "estimand": "comparison pre-post change",
                "estimate": control_change,
                "interpretation": "change in PA restaurants over the same period",
            },
            {
                "estimand": "2x2 DID",
                "estimate": did,
                "interpretation": "post-period ATT under parallel trends and no anticipation",
            },
            {
                "estimand": "regression DID coefficient",
                "estimate": float(beta[3]),
                "naive_se": float(naive[3]),
                "state_clustered_se": state_clustered_se,
                "restaurant_clustered_se": float(restaurant_cluster[3]),
                "state_cluster_note": state_cluster_note,
                "interpretation": "coefficient on treated_state x post",
            },
        ]
    )
    estimates.to_csv(outdir / "card_krueger_did_estimates.csv", index=False)

    plt.figure(figsize=(7.2, 4.3))
    for state, group in state_paths.groupby("state"):
        plt.plot(group["period"], group["mean_fte"], marker="o", linewidth=2, label=state)
    plt.ylabel("Mean full-time-equivalent employment")
    plt.xlabel("Period")
    plt.legend(title="State")
    plt.tight_layout()
    plt.savefig(outdir / "card_krueger_paths.png", dpi=160)
    plt.close()

    cluster_diagnostics = pd.DataFrame(
        [
            {
                "level": "state",
                "clusters": int(df["state"].nunique()),
                "treated_clusters": int(df.loc[df["treated_state"] == 1, "state"].nunique()),
                "design_note": "policy varies at this level; conventional cluster inference is fragile with two clusters",
            },
            {
                "level": "restaurant",
                "clusters": int(df["restaurant_id"].nunique()),
                "treated_clusters": int(df.loc[df["treated_state"] == 1, "restaurant_id"].nunique()),
                "design_note": "many restaurants do not create many independent policy shocks",
            },
        ]
    )
    cluster_diagnostics.to_csv(outdir / "card_krueger_cluster_diagnostics.csv", index=False)
    return did


def twfe_static(df: pd.DataFrame) -> tuple[float, float]:
    work = df.copy()
    work["y_resid"] = two_way_residualize(work, "employment_index", "county_id", "year")
    work["d_resid"] = two_way_residualize(work, "treated", "county_id", "year")
    x = work[["d_resid"]].to_numpy(dtype=float)
    y = work["y_resid"].to_numpy(dtype=float)
    beta = ols_beta(y, x)
    se = cluster_se(y, x, beta, work["county_id"].to_numpy())
    return float(beta[0]), float(se[0])


def group_time_att(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    cohorts = sorted(int(g) for g in df.loc[df["adoption_year"] < 9999, "adoption_year"].unique())
    for cohort in cohorts:
        baseline = cohort - 1
        treated_units = df.loc[df["adoption_year"] == cohort, "county_id"].unique()
        if len(treated_units) == 0:
            continue
        for year in sorted(int(y) for y in df.loc[df["year"] >= cohort, "year"].unique()):
            control_units = df.loc[df["adoption_year"] > year, "county_id"].unique()
            if len(control_units) == 0:
                continue
            treated_now = df[(df["county_id"].isin(treated_units)) & (df["year"] == year)]
            treated_base = df[(df["county_id"].isin(treated_units)) & (df["year"] == baseline)]
            control_now = df[(df["county_id"].isin(control_units)) & (df["year"] == year)]
            control_base = df[(df["county_id"].isin(control_units)) & (df["year"] == baseline)]
            if treated_base.empty or control_base.empty:
                continue
            treated_delta = float(treated_now["employment_index"].mean() - treated_base["employment_index"].mean())
            control_delta = float(control_now["employment_index"].mean() - control_base["employment_index"].mean())
            rows.append(
                {
                    "cohort": cohort,
                    "year": year,
                    "event_time": year - cohort,
                    "att_gt": treated_delta - control_delta,
                    "treated_counties": int(len(treated_units)),
                    "control_counties": int(len(control_units)),
                    "comparison": "not-yet-treated and never-treated",
                }
            )
    return pd.DataFrame(rows)


def fit_untreated_outcome_model(df: pd.DataFrame) -> pd.Series:
    untreated = df[df["treated"] == 0].copy()
    unit_dummies = pd.get_dummies(untreated["county_id"], prefix="county", drop_first=True, dtype=float)
    year_dummies = pd.get_dummies(untreated["year"], prefix="year", drop_first=True, dtype=float)
    x_untreated = pd.concat(
        [
            pd.Series(1.0, index=untreated.index, name="intercept"),
            unit_dummies,
            year_dummies,
        ],
        axis=1,
    )
    beta = ols_beta(untreated["employment_index"].to_numpy(dtype=float), x_untreated.to_numpy(dtype=float))

    all_unit_dummies = pd.get_dummies(df["county_id"], prefix="county", drop_first=True, dtype=float)
    all_year_dummies = pd.get_dummies(df["year"], prefix="year", drop_first=True, dtype=float)
    x_all = pd.concat(
        [
            pd.Series(1.0, index=df.index, name="intercept"),
            all_unit_dummies,
            all_year_dummies,
        ],
        axis=1,
    )
    x_all = x_all.reindex(columns=x_untreated.columns, fill_value=0.0)
    return pd.Series(x_all.to_numpy(dtype=float) @ beta, index=df.index)


def imputation_att(df: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    work = df.copy()
    work["y0_hat"] = fit_untreated_outcome_model(work)
    treated_post = work[(work["treated"] == 1) & (work["ever_treated"] == 1)].copy()
    treated_post["gap"] = treated_post["employment_index"] - treated_post["y0_hat"]
    event = (
        treated_post.groupby("event_time", as_index=False)
        .agg(att=("gap", "mean"), observations=("gap", "size"), cohorts=("adoption_year", "nunique"))
        .sort_values("event_time")
    )
    return event, float(treated_post["gap"].mean())


def analyze_staggered(df: pd.DataFrame, outdir: Path, did_reference: float) -> None:
    twfe_beta, twfe_se = twfe_static(df)
    gt = group_time_att(df)
    gt.to_csv(outdir / "group_time_att.csv", index=False)
    gt_aggregate = float(np.average(gt["att_gt"], weights=gt["treated_counties"]))

    imputation_event, imputation_aggregate = imputation_att(df)
    imputation_event.to_csv(outdir / "imputation_event_time_att.csv", index=False)

    support = (
        df[(df["treated"] == 1) & (df["ever_treated"] == 1)]
        .groupby("event_time", as_index=False)
        .agg(cohorts=("adoption_year", "nunique"), counties=("county_id", "nunique"), observations=("county_id", "size"))
        .sort_values("event_time")
    )
    support.to_csv(outdir / "event_time_support.csv", index=False)

    comparison = pd.DataFrame(
        [
            {
                "estimate": "2x2 DID teaching reference",
                "value": did_reference,
                "clustered_se": np.nan,
                "interpretation": "classical two-state ATT under parallel trends",
            },
            {
                "estimate": "naive staggered TWFE",
                "value": twfe_beta,
                "clustered_se": twfe_se,
                "interpretation": "weighted mixture of staggered comparisons; can include already-treated controls",
            },
            {
                "estimate": "group-time ATT aggregate",
                "value": gt_aggregate,
                "clustered_se": np.nan,
                "interpretation": "average of cohort-time effects using not-yet-treated controls",
            },
            {
                "estimate": "imputation-style ATT aggregate",
                "value": imputation_aggregate,
                "clustered_se": np.nan,
                "interpretation": "average treated gap relative to untreated-outcome predictions",
            },
        ]
    )
    comparison.to_csv(outdir / "modern_did_comparison.csv", index=False)

    cohort_timing = (
        df.drop_duplicates("county_id")
        .assign(cohort=lambda x: x["adoption_year"].replace({9999: "never"}))
        .groupby("cohort", as_index=False)
        .agg(counties=("county_id", "size"))
    )
    cohort_timing.to_csv(outdir / "cohort_timing.csv", index=False)

    plt.figure(figsize=(7.4, 4.4))
    mean_paths = df.groupby(["adoption_year", "year"], as_index=False)["employment_index"].mean()
    for cohort, group in mean_paths.groupby("adoption_year"):
        label = "never" if cohort == 9999 else str(int(cohort))
        plt.plot(group["year"], group["employment_index"], linewidth=1.8, label=label)
    plt.xlabel("Year")
    plt.ylabel("Mean employment index")
    plt.legend(title="Adoption cohort", ncol=2)
    plt.tight_layout()
    plt.savefig(outdir / "staggered_cohort_paths.png", dpi=160)
    plt.close()

    plt.figure(figsize=(7.4, 4.4))
    plt.plot(gt["event_time"], gt["att_gt"], marker="o", linestyle="", label="group-time ATT cells")
    plt.plot(imputation_event["event_time"], imputation_event["att"], marker="s", linewidth=2, label="imputation event-time ATT")
    plt.axhline(twfe_beta, color="black", linestyle="--", linewidth=1.2, label="naive TWFE")
    plt.xlabel("Event time")
    plt.ylabel("Estimated effect")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outdir / "modern_did_comparison.png", dpi=160)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--card-input", required=True)
    parser.add_argument("--staggered-input", required=True)
    parser.add_argument("--outdir", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    card = pd.read_csv(args.card_input)
    staggered = pd.read_csv(args.staggered_input)

    did_reference = analyze_card_krueger(card, outdir)
    analyze_staggered(staggered, outdir, did_reference)
    print(f"Wrote DID and modern DID outputs to {outdir}")


if __name__ == "__main__":
    main()
