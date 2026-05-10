from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARM_ORDER = ["control", "belief_info", "planning_prompt", "belief_planning"]


def adjusted_outcome(df: pd.DataFrame, outcome: str, baseline: str) -> pd.Series:
    baseline_centered = df[baseline] - df[baseline].mean()
    variance = (baseline_centered**2).mean()
    if variance == 0:
        return df[outcome]
    slope = ((df[outcome] - df[outcome].mean()) * baseline_centered).mean() / variance
    return df[outcome] - slope * baseline_centered


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker-input", required=True)
    parser.add_argument("--duration-input", required=True)
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    workers = pd.read_csv(args.worker_input)
    workers["arm"] = pd.Categorical(workers["arm"], categories=ARM_ORDER, ordered=True)
    workers["post_belief_adjusted"] = adjusted_outcome(workers, "post_belief", "baseline_belief")
    workers["applications_adjusted"] = adjusted_outcome(workers, "applications_week1", "baseline_applications")
    workers["exit_adjusted"] = adjusted_outcome(workers, "exit_by_week4", "baseline_belief")

    summary = (
        workers.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            information_content=("information_content", "mean"),
            planning_support=("planning_support", "mean"),
            salience_boost=("salience_boost", "mean"),
            baseline_belief=("baseline_belief", "mean"),
            post_belief=("post_belief", "mean"),
            applications_week1=("applications_week1", "mean"),
            search_plan_score=("search_plan_score", "mean"),
            exit_by_week4=("exit_by_week4", "mean"),
            observed_duration_weeks=("observed_duration_weeks", "mean"),
            post_belief_adjusted=("post_belief_adjusted", "mean"),
            applications_adjusted=("applications_adjusted", "mean"),
            exit_adjusted=("exit_adjusted", "mean"),
        )
        .sort_values("arm")
    )
    summary.to_csv(outdir / "information_rct_summary.csv", index=False)

    control = summary.loc[summary["arm"] == "control"].iloc[0]
    effects = summary.copy()
    for col in [
        "post_belief",
        "applications_week1",
        "search_plan_score",
        "exit_by_week4",
        "observed_duration_weeks",
        "post_belief_adjusted",
        "applications_adjusted",
        "exit_adjusted",
    ]:
        effects[f"{col}_vs_control"] = effects[col] - control[col]
    effects.to_csv(outdir / "information_treatment_effects.csv", index=False)

    duration = pd.read_csv(args.duration_input)
    duration["arm"] = pd.Categorical(duration["arm"], categories=ARM_ORDER, ordered=True)
    hazard = (
        duration.groupby(["arm", "week"], observed=False, as_index=False)
        .agg(
            at_risk=("at_risk", "sum"),
            exits=("exit_this_week", "sum"),
            mean_model_hazard=("hazard_probability", "mean"),
            mean_belief=("belief_this_week", "mean"),
            mean_applications=("applications_this_week", "mean"),
        )
        .sort_values(["arm", "week"])
    )
    hazard["observed_hazard"] = hazard["exits"] / hazard["at_risk"]
    hazard.to_csv(outdir / "duration_hazard_summary.csv", index=False)

    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.0))
    axes[0].bar(summary["arm"].astype(str), summary["post_belief"], color="#4C78A8")
    axes[0].set_ylabel("Post-treatment belief")
    axes[0].tick_params(axis="x", rotation=24)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(summary["arm"].astype(str), summary["applications_week1"], color="#59A14F")
    axes[1].set_ylabel("Applications in week 1")
    axes[1].tick_params(axis="x", rotation=24)
    axes[1].spines[["top", "right"]].set_visible(False)

    for arm in ARM_ORDER:
        arm_hazard = hazard.loc[hazard["arm"] == arm]
        axes[2].plot(
            arm_hazard["week"],
            arm_hazard["observed_hazard"],
            marker="o",
            linewidth=1.2,
            label=arm,
        )
    axes[2].set_xlabel("Week")
    axes[2].set_ylabel("Observed exit hazard")
    axes[2].legend(frameon=False, fontsize=7)
    axes[2].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "information_reproduction.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic job-search information data "
        "to connect an information treatment to OLS/ANCOVA-style contrasts and "
        "a discrete-time hazard summary. It is not an official replication of "
        "Altmann, Falk, Jaeger, and Zimmermann.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
