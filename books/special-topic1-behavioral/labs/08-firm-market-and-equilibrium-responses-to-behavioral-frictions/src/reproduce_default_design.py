from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


GROUP_ORDER = ["low_default", "standard_default", "high_default", "active_choice"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    data = pd.read_csv(args.input)
    data["default_group"] = pd.Categorical(data["default_group"], categories=GROUP_ORDER, ordered=True)

    summary = (
        data.groupby("default_group", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            firms=("firm_id", "nunique"),
            active_choice_required=("active_choice_required", "mean"),
            default_contribution_rate=("default_contribution_rate", "mean"),
            participation=("participation", "mean"),
            passive_choice=("passive_choice", "mean"),
            contribution_rate=("contribution_rate", "mean"),
            target_contribution_rate=("target_contribution_rate", "mean"),
            default_gap=("default_gap", "mean"),
            equity_share=("equity_share", "mean"),
            target_equity_share=("target_equity_share", "mean"),
            welfare_distance=("welfare_distance", "mean"),
            undersaving=("undersaving", "mean"),
            oversaving_liquidity_risk=("oversaving_liquidity_risk", "mean"),
            sophistication_index=("sophistication_index", "mean"),
            liquidity_need_index=("liquidity_need_index", "mean"),
        )
        .sort_values("default_group")
    )
    summary.to_csv(outdir / "default_design_summary.csv", index=False)

    active = summary.loc[summary["default_group"] == "active_choice"].iloc[0]
    effects = summary.copy()
    for col in [
        "participation",
        "passive_choice",
        "contribution_rate",
        "default_gap",
        "welfare_distance",
        "undersaving",
        "oversaving_liquidity_risk",
    ]:
        effects[f"{col}_vs_active_choice"] = effects[col] - active[col]
    effects.to_csv(outdir / "default_effects_vs_active_choice.csv", index=False)

    response = (
        data.groupby(["default_group", "firm_response_type"], observed=True, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            participation=("participation", "mean"),
            passive_choice=("passive_choice", "mean"),
            contribution_rate=("contribution_rate", "mean"),
            welfare_distance=("welfare_distance", "mean"),
            undersaving=("undersaving", "mean"),
            oversaving_liquidity_risk=("oversaving_liquidity_risk", "mean"),
        )
        .sort_values(["default_group", "firm_response_type"])
    )
    response["interpretation"] = response["firm_response_type"].map(
        {
            "exploit_or_underinsure": "low default raises undersaving risk for passive workers",
            "insure": "standard default moves passive workers toward a middle benchmark",
            "insure_or_oversteer": "high default can insure present bias but creates liquidity risk",
            "accommodate": "active choice reduces passive defaults but relies on attention",
        }
    )
    response.to_csv(outdir / "firm_response_diagnostic.csv", index=False)

    fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.0))
    labels = summary["default_group"].astype(str)
    axes[0].bar(labels, summary["participation"], color="#4C78A8")
    axes[0].set_ylabel("Participation rate")
    axes[0].tick_params(axis="x", rotation=24)

    axes[1].bar(labels, summary["contribution_rate"], color="#59A14F", label="actual")
    axes[1].plot(labels, summary["target_contribution_rate"], color="#222222", marker="o", label="target")
    axes[1].set_ylabel("Contribution rate")
    axes[1].tick_params(axis="x", rotation=24)
    axes[1].legend(frameon=False, fontsize=8)

    axes[2].bar(labels, summary["welfare_distance"], color="#E15759")
    axes[2].set_ylabel("Mean welfare distance")
    axes[2].tick_params(axis="x", rotation=24)

    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "default_design_reproduction.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic employer-sponsored retirement-default data. "
        "It separates worker-level default response from the firm response margin "
        "and reports a simple welfare-distance diagnostic. It is not an official "
        "replication of Bernheim, Fradkin, and Popov.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
