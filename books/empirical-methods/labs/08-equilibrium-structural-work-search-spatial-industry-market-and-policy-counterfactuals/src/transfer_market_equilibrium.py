"""Run the Week 8 market-equilibrium transfer workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week8_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week8_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def estimate_logit_demand(df: pd.DataFrame) -> tuple[pd.DataFrame, np.ndarray]:
    y = np.log(df["share"].to_numpy(dtype=float)) - np.log(df["outside_share"].to_numpy(dtype=float))
    x = np.column_stack(
        [
            np.ones(len(df)),
            df["price"].to_numpy(dtype=float),
            df["quality"].to_numpy(dtype=float),
            df["automation_exposure"].to_numpy(dtype=float),
            df["market_income_index"].to_numpy(dtype=float),
        ]
    )
    beta, residuals, rank, _ = np.linalg.lstsq(x, y, rcond=None)
    fitted = x @ beta
    sigma2 = float(np.sum((y - fitted) ** 2) / max(len(y) - x.shape[1], 1))
    variance = sigma2 * np.linalg.pinv(x.T @ x)
    se = np.sqrt(np.maximum(np.diag(variance), 0.0))
    estimates = pd.DataFrame(
        {
            "parameter": ["intercept", "price_alpha", "quality", "automation_exposure", "market_income_index"],
            "estimate": beta,
            "standard_error_naive": se,
            "diagnostic_note": [
                "Teaching OLS demand; publishable work would need instruments.",
                "Price coefficient governs elasticities and markups in this teaching path.",
                "Quality shifts product utility.",
                "Exposure shifts product utility and defines the cost-shock target.",
                "Market-level demand shifter included for fit.",
            ],
        }
    )
    return estimates, beta


def predict_shares(group: pd.DataFrame, beta: np.ndarray, prices: np.ndarray) -> np.ndarray:
    utility = (
        beta[0]
        + beta[1] * prices
        + beta[2] * group["quality"].to_numpy(dtype=float)
        + beta[3] * group["automation_exposure"].to_numpy(dtype=float)
        + beta[4] * group["market_income_index"].to_numpy(dtype=float)
    )
    expu = np.exp(np.clip(utility, -30.0, 30.0))
    return expu / (1.0 + expu.sum())


def recover_markups(df: pd.DataFrame, beta: np.ndarray) -> pd.DataFrame:
    alpha = float(beta[1])
    if alpha >= 0:
        raise ValueError("Estimated demand slope is nonnegative; markup recovery is not meaningful.")
    out = df.copy()
    own_elasticity = alpha * out["price"].to_numpy(dtype=float) * (1.0 - out["share"].to_numpy(dtype=float))
    markup = -1.0 / (alpha * (1.0 - out["share"].to_numpy(dtype=float)))
    out["own_price_elasticity"] = own_elasticity
    out["implied_markup"] = markup
    out["recovered_marginal_cost"] = out["price"] - markup
    out["markup_rate"] = markup / out["price"]
    out["recovery_note"] = "Single-product logit pricing rule; no ownership matrix or random coefficients."
    return out


def solve_market_counterfactual(markups: pd.DataFrame, beta: np.ndarray) -> pd.DataFrame:
    rows = []
    alpha = float(beta[1])
    for _, group in markups.groupby("market_id", sort=True):
        base = group.copy()
        exposure = base["automation_exposure"].to_numpy(dtype=float)
        cost_shock = np.where(exposure >= np.quantile(exposure, 0.60), -0.08, -0.02)
        marginal_cost_cf = base["recovered_marginal_cost"].to_numpy(dtype=float) * (1.0 + cost_shock)
        prices = base["price"].to_numpy(dtype=float).copy()
        for _ in range(500):
            shares = predict_shares(base, beta, prices)
            markup = -1.0 / (alpha * np.maximum(1.0 - shares, 0.05))
            next_prices = marginal_cost_cf + markup
            updated = 0.55 * prices + 0.45 * next_prices
            if np.max(np.abs(updated - prices)) < 1e-9:
                prices = updated
                break
            prices = updated
        shares_cf = predict_shares(base, beta, prices)
        quantities_cf = shares_cf * base["market_size"].to_numpy(dtype=float)
        employment_cf = quantities_cf * base["labor_intensity"].to_numpy(dtype=float) / 100.0
        for idx, (_, row) in enumerate(base.iterrows()):
            rows.append(
                {
                    "market_id": int(row["market_id"]),
                    "product_id": int(row["product_id"]),
                    "product": row["product"],
                    "automation_exposure": row["automation_exposure"],
                    "baseline_price": row["price"],
                    "counterfactual_price": prices[idx],
                    "price_change": prices[idx] - row["price"],
                    "baseline_share": row["share"],
                    "counterfactual_share": shares_cf[idx],
                    "share_change": shares_cf[idx] - row["share"],
                    "baseline_quantity": row["quantity"],
                    "counterfactual_quantity": quantities_cf[idx],
                    "baseline_employment": row["employment"],
                    "counterfactual_employment": employment_cf[idx],
                    "employment_change": employment_cf[idx] - row["employment"],
                    "cost_shock_pct": 100.0 * cost_shock[idx],
                    "pass_through": (prices[idx] - row["price"])
                    / (marginal_cost_cf[idx] - row["recovered_marginal_cost"])
                    if abs(marginal_cost_cf[idx] - row["recovered_marginal_cost"]) > 1e-10
                    else np.nan,
                }
            )
    return pd.DataFrame(rows)


def write_outputs(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    estimates, beta = estimate_logit_demand(df)
    estimates.round(6).to_csv(outdir / "demand_estimates.csv", index=False)

    markups = recover_markups(df, beta)
    markup_cols = [
        "market_id",
        "product_id",
        "product",
        "price",
        "share",
        "own_price_elasticity",
        "implied_markup",
        "recovered_marginal_cost",
        "markup_rate",
        "recovery_note",
    ]
    markups[markup_cols].round(6).to_csv(outdir / "markup_recovery.csv", index=False)

    cf = solve_market_counterfactual(markups, beta)
    cf.round(6).to_csv(outdir / "product_counterfactuals.csv", index=False)

    summary = (
        cf.assign(high_exposure=cf["automation_exposure"] >= cf["automation_exposure"].median())
        .groupby("high_exposure", as_index=False)
        .agg(
            products=("product", "count"),
            mean_cost_shock_pct=("cost_shock_pct", "mean"),
            mean_price_change=("price_change", "mean"),
            mean_pass_through=("pass_through", "mean"),
            counterfactual_quantity=("counterfactual_quantity", "sum"),
            baseline_quantity=("baseline_quantity", "sum"),
            total_employment_change=("employment_change", "sum"),
        )
    )
    summary["quantity_pct_change"] = 100.0 * (
        summary["counterfactual_quantity"] - summary["baseline_quantity"]
    ) / summary["baseline_quantity"]
    summary["interpretation"] = np.where(
        summary["high_exposure"],
        "High-exposure products receive the larger cost shock in the transfer exercise.",
        "Lower-exposure products receive the smaller cost shock; compare their pass-through and quantity response.",
    )
    summary.round(6).to_csv(outdir / "market_counterfactual_summary.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "prompt": "What identifies the price coefficient in this teaching path?",
                "diagnostic": "OLS price variation is not a credible instrument; this is the main transfer limitation.",
            },
            {
                "prompt": "Which object drives the markup recovery?",
                "diagnostic": "The own-price elasticity implied by the logit demand slope and product share.",
            },
            {
                "prompt": "How does pass-through differ from spatial rent incidence?",
                "diagnostic": "Market incidence runs through price-cost margins and demand substitution.",
            },
            {
                "prompt": "What would a publishable paper need?",
                "diagnostic": "Instruments, ownership, richer substitution, supply-side validation, and uncertainty.",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)

    plt.figure(figsize=(7.5, 4.5))
    plt.scatter(
        cf["cost_shock_pct"],
        cf["price_change"],
        c=np.where(cf["automation_exposure"] >= cf["automation_exposure"].median(), "#D55E00", "#0072B2"),
        alpha=0.82,
        edgecolor="white",
        linewidth=0.6,
    )
    plt.axhline(0.0, color="#333333", linewidth=0.8)
    plt.xlabel("Marginal-cost shock (percent)")
    plt.ylabel("Equilibrium price change")
    plt.tight_layout()
    plt.savefig(outdir / "market_pass_through.png", dpi=160)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    write_outputs(df, args.outdir)
    print(f"Wrote market-equilibrium transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
