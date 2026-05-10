from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ARM_ORDER = ["control", "salience_notice", "simplified_form", "assistance", "full_support"]


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
    workers["post_awareness_adjusted"] = adjusted_outcome(workers, "post_awareness", "baseline_awareness")
    workers["application_completed_adjusted"] = adjusted_outcome(
        workers, "application_completed", "baseline_awareness"
    )
    workers["claimed_adjusted"] = adjusted_outcome(workers, "claimed_by_deadline", "baseline_awareness")

    summary = (
        workers.groupby("arm", observed=False, as_index=False)
        .agg(
            workers=("worker_id", "count"),
            salience=("salience", "mean"),
            simplification=("simplification", "mean"),
            assistance=("assistance", "mean"),
            trust_support=("trust_support", "mean"),
            baseline_awareness=("baseline_awareness", "mean"),
            post_awareness=("post_awareness", "mean"),
            perceived_value=("perceived_value", "mean"),
            procedural_cost=("procedural_cost", "mean"),
            net_perceived_gain=("net_perceived_gain", "mean"),
            application_started=("application_started", "mean"),
            application_completed=("application_completed", "mean"),
            claimed_by_deadline=("claimed_by_deadline", "mean"),
            weeks_to_claim=("weeks_to_claim", "mean"),
            filing_accuracy=("filing_accuracy", "mean"),
            earnings_response_index=("earnings_response_index", "mean"),
            post_awareness_adjusted=("post_awareness_adjusted", "mean"),
            application_completed_adjusted=("application_completed_adjusted", "mean"),
            claimed_adjusted=("claimed_adjusted", "mean"),
        )
        .sort_values("arm")
    )
    summary.to_csv(outdir / "takeup_policy_summary.csv", index=False)

    control = summary.loc[summary["arm"] == "control"].iloc[0]
    effects = summary.copy()
    for col in [
        "post_awareness",
        "procedural_cost",
        "application_started",
        "application_completed",
        "claimed_by_deadline",
        "weeks_to_claim",
        "filing_accuracy",
        "earnings_response_index",
        "post_awareness_adjusted",
        "application_completed_adjusted",
        "claimed_adjusted",
    ]:
        effects[f"{col}_vs_control"] = effects[col] - control[col]
    effects.to_csv(outdir / "takeup_treatment_effects.csv", index=False)

    duration = pd.read_csv(args.duration_input)
    duration["arm"] = pd.Categorical(duration["arm"], categories=ARM_ORDER, ordered=True)
    hazard = (
        duration.groupby(["arm", "week"], observed=False, as_index=False)
        .agg(
            at_risk=("at_risk", "sum"),
            claims=("claim_this_week", "sum"),
            mean_model_hazard=("model_hazard", "mean"),
            mean_post_awareness=("post_awareness", "mean"),
            mean_procedural_cost=("procedural_cost", "mean"),
        )
        .sort_values(["arm", "week"])
    )
    hazard["observed_claim_hazard"] = hazard["claims"] / hazard["at_risk"].clip(lower=1)
    hazard.to_csv(outdir / "takeup_hazard_summary.csv", index=False)

    fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.1))
    axes[0].bar(summary["arm"].astype(str), summary["post_awareness"], color="#4C78A8")
    axes[0].set_ylabel("Post-treatment awareness")
    axes[0].tick_params(axis="x", rotation=24)
    axes[0].spines[["top", "right"]].set_visible(False)

    axes[1].bar(summary["arm"].astype(str), summary["application_completed"], color="#59A14F")
    axes[1].set_ylabel("Application completion")
    axes[1].tick_params(axis="x", rotation=24)
    axes[1].spines[["top", "right"]].set_visible(False)

    for arm in ARM_ORDER:
        arm_hazard = hazard.loc[hazard["arm"] == arm]
        axes[2].plot(
            arm_hazard["week"],
            arm_hazard["observed_claim_hazard"],
            marker="o",
            linewidth=1.2,
            label=arm,
        )
    axes[2].set_xlabel("Week")
    axes[2].set_ylabel("Observed claim hazard")
    axes[2].legend(frameon=False, fontsize=7)
    axes[2].spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(outdir / "takeup_reproduction.png", dpi=180)
    plt.close(fig)

    note = (
        "This bounded reproduction uses synthetic benefit take-up data to connect "
        "salience, simplification, and assistance to extensive-margin treatment "
        "effects and a duration-style claim hazard. It is not an official "
        "replication of Bhargava and Manoli.\n"
    )
    (outdir / "reproduction_note.txt").write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
