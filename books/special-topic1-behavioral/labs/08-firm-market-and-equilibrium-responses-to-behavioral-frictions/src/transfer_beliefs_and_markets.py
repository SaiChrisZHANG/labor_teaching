from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BELIEF_ORDER = ["control", "outside_option_info", "bargaining_prompt", "info_bargaining"]
MARKET_ORDER = ["opaque", "fee_disclosure", "disclosure_switching_help"]


def summarize_beliefs(beliefs: pd.DataFrame, outdir: Path) -> None:
    beliefs["arm"] = pd.Categorical(beliefs["arm"], categories=BELIEF_ORDER, ordered=True)
    beliefs["high_search_friction"] = (
        beliefs["search_friction_index"] >= beliefs["search_friction_index"].median()
    ).astype(int)
    beliefs["high_market_power"] = (
        beliefs["market_power_index"] >= beliefs["market_power_index"].median()
    ).astype(int)

    summary = (
        beliefs.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            information=("information", "mean"),
            bargaining_support=("bargaining_support", "mean"),
            current_wage=("current_wage", "mean"),
            true_outside_wage=("true_outside_wage", "mean"),
            perceived_outside_wage=("perceived_outside_wage", "mean"),
            belief_gap=("belief_gap", "mean"),
            applications_next_month=("applications_next_month", "mean"),
            bargaining_attempt=("bargaining_attempt", "mean"),
            moved_job=("moved_job", "mean"),
            wage_growth_next_quarter=("wage_growth_next_quarter", "mean"),
            segmentation_index=("segmentation_index", "mean"),
        )
        .sort_values("arm")
    )
    summary.to_csv(outdir / "outside_option_belief_summary.csv", index=False)

    control = summary.loc[summary["arm"] == "control"].iloc[0]
    effects = summary.copy()
    for col in [
        "belief_gap",
        "applications_next_month",
        "bargaining_attempt",
        "moved_job",
        "wage_growth_next_quarter",
        "segmentation_index",
    ]:
        effects[f"{col}_vs_control"] = effects[col] - control[col]
    effects.to_csv(outdir / "outside_option_effects_vs_control.csv", index=False)

    segmentation = (
        beliefs.groupby(["high_search_friction", "high_market_power"], as_index=False)
        .agg(
            workers=("worker_id", "count"),
            belief_gap=("belief_gap", "mean"),
            applications_next_month=("applications_next_month", "mean"),
            bargaining_attempt=("bargaining_attempt", "mean"),
            moved_job=("moved_job", "mean"),
            wage_growth_next_quarter=("wage_growth_next_quarter", "mean"),
            segmentation_index=("segmentation_index", "mean"),
        )
        .sort_values(["high_search_friction", "high_market_power"])
    )
    segmentation["diagnostic"] = segmentation.apply(
        lambda row: "persistent wedge likely"
        if row["high_search_friction"] == 1 and row["high_market_power"] == 1
        else "discipline more plausible",
        axis=1,
    )
    segmentation.to_csv(outdir / "segmentation_diagnostic.csv", index=False)


def summarize_markets(markets: pd.DataFrame, outdir: Path) -> None:
    markets["arm"] = pd.Categorical(markets["arm"], categories=MARKET_ORDER, ordered=True)
    summary = (
        markets.groupby("arm", observed=False, as_index=False)
        .agg(
            accounts=("account_id", "count"),
            disclosure=("disclosure", "mean"),
            switching_help=("switching_help", "mean"),
            high_switching_cost=("high_switching_cost", "mean"),
            sales_contact=("sales_contact", "mean"),
            fee_salience_index=("fee_salience_index", "mean"),
            demand_elasticity_index=("demand_elasticity_index", "mean"),
            switched_plan=("switched_plan", "mean"),
            chose_low_fee_plan=("chose_low_fee_plan", "mean"),
            realized_fee_bps=("realized_fee_bps", "mean"),
        )
        .sort_values("arm")
    )
    summary.to_csv(outdir / "plan_disclosure_summary.csv", index=False)

    diagnostic = (
        markets.groupby(["high_switching_cost", "sales_contact"], as_index=False)
        .agg(
            accounts=("account_id", "count"),
            fee_salience_index=("fee_salience_index", "mean"),
            demand_elasticity_index=("demand_elasticity_index", "mean"),
            switched_plan=("switched_plan", "mean"),
            chose_low_fee_plan=("chose_low_fee_plan", "mean"),
            realized_fee_bps=("realized_fee_bps", "mean"),
        )
        .sort_values(["high_switching_cost", "sales_contact"])
    )
    diagnostic["interpretation"] = diagnostic.apply(
        lambda row: "transparency weakened by switching costs and sales contact"
        if row["high_switching_cost"] == 1 and row["sales_contact"] == 1
        else "transparency more likely to discipline firms",
        axis=1,
    )
    diagnostic.to_csv(outdir / "demand_switching_diagnostic.csv", index=False)


def make_figure(beliefs: pd.DataFrame, markets: pd.DataFrame, outdir: Path) -> None:
    belief_summary = pd.read_csv(outdir / "outside_option_belief_summary.csv")
    market_summary = pd.read_csv(outdir / "plan_disclosure_summary.csv")

    fig, axes = plt.subplots(2, 2, figsize=(13.2, 7.2))
    axes = axes.flatten()

    axes[0].bar(belief_summary["arm"].astype(str), belief_summary["belief_gap"], color="#4C78A8")
    axes[0].set_ylabel("Outside-option belief gap")
    axes[0].tick_params(axis="x", rotation=22)

    axes[1].bar(
        belief_summary["arm"].astype(str),
        belief_summary["applications_next_month"],
        color="#59A14F",
    )
    axes[1].set_ylabel("Applications next month")
    axes[1].tick_params(axis="x", rotation=22)

    axes[2].bar(
        market_summary["arm"].astype(str),
        market_summary["demand_elasticity_index"],
        color="#F28E2B",
    )
    axes[2].set_ylabel("Demand elasticity index")
    axes[2].tick_params(axis="x", rotation=22)

    axes[3].bar(market_summary["arm"].astype(str), market_summary["realized_fee_bps"], color="#E15759")
    axes[3].set_ylabel("Realized fee, basis points")
    axes[3].tick_params(axis="x", rotation=22)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "equilibrium_transfer_diagnostics.png", dpi=180)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--belief-input", required=True)
    parser.add_argument("--market-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    beliefs = pd.read_csv(args.belief_input)
    markets = pd.read_csv(args.market_input)
    summarize_beliefs(beliefs, outdir)
    summarize_markets(markets, outdir)
    make_figure(beliefs, markets, outdir)

    note = (
        "This bounded transfer uses synthetic outside-option belief and plan-market data. "
        "It distinguishes worker belief response, search and bargaining margins, "
        "segmentation diagnostics, demand elasticity, switching costs, and sales-force "
        "interpretation. It is not an official replication of the cited papers.\n"
    )
    (outdir / "transfer_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
