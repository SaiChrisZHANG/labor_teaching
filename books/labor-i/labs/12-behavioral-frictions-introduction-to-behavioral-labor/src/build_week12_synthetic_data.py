#!/usr/bin/env python3
"""Build deterministic synthetic teaching data for the Week 12 behavioral-labor lab."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


LAB_DIR = Path(__file__).resolve().parents[1]
ORIGINAL_DIR = LAB_DIR / "original" / "reduced"
TRANSFER_DIR = LAB_DIR / "transfer" / "data"
FIGURE_DIR = LAB_DIR.parents[1] / "assets" / "figures"


def build_incentive_complexity_data(rng: np.random.Generator) -> pd.DataFrame:
    n = 1800
    arms = rng.choice(["simple_piece_rate", "complex_bonus"], size=n, p=[0.5, 0.5])
    cognitive_score = np.clip(rng.normal(0.0, 1.0, n), -2.2, 2.2)
    baseline_skill = np.clip(rng.normal(0.0, 1.0, n), -2.0, 2.5)
    complexity = np.where(arms == "complex_bonus", 1.0, 0.0)
    true_piece_rate = np.where(arms == "complex_bonus", 1.45, 1.45)
    lambda_attention = np.clip(0.92 - 0.26 * complexity + 0.10 * cognitive_score, 0.25, 0.98)
    perceived_piece_rate = lambda_attention * true_piece_rate + (1.0 - lambda_attention) * 0.80

    rational_effort = (
        7.0
        + 2.0 * true_piece_rate
        + 1.4 * baseline_skill
        + 0.6 * cognitive_score
    )
    observed_effort = (
        7.0
        + 2.1 * perceived_piece_rate
        + 1.4 * baseline_skill
        + 0.55 * cognitive_score
        + rng.normal(0.0, 0.9, n)
    )
    output_units = np.clip(np.round(observed_effort + rng.normal(0.0, 0.4, n)), 3, None)
    effort_gap = observed_effort - rational_effort

    df = pd.DataFrame(
        {
            "worker_id": np.arange(1, n + 1),
            "contract_arm": arms,
            "cognitive_score": cognitive_score,
            "baseline_skill": baseline_skill,
            "lambda_attention": lambda_attention,
            "true_piece_rate": true_piece_rate,
            "perceived_piece_rate": perceived_piece_rate,
            "rational_effort": rational_effort,
            "observed_effort": observed_effort,
            "output_units": output_units,
            "effort_gap": effort_gap,
        }
    )
    df["cognitive_group"] = pd.qcut(
        df["cognitive_score"],
        3,
        labels=["low", "middle", "high"],
    )
    return df


def build_gift_exchange_data(rng: np.random.Generator) -> pd.DataFrame:
    n = 2100
    arms = rng.choice(["baseline", "gift", "high_piece_rate"], size=n, p=[0.34, 0.33, 0.33])
    employer_return_high = rng.binomial(1, 0.5, n)
    worker_type = np.clip(rng.normal(0.0, 1.0, n), -2.2, 2.2)

    extra_work = (
        4.6
        + 0.95 * (arms == "gift").astype(float)
        + 1.15 * (arms == "high_piece_rate").astype(float)
        + 0.08 * employer_return_high
        + 0.55 * worker_type
        + rng.normal(0.0, 0.85, n)
    )
    productivity = (
        99.0
        + 0.15 * (arms == "gift").astype(float)
        + 1.45 * (arms == "high_piece_rate").astype(float)
        + 0.05 * employer_return_high
        + 0.65 * worker_type
        + rng.normal(0.0, 1.1, n)
    )

    df = pd.DataFrame(
        {
            "shift_id": np.arange(1, n + 1),
            "treatment_arm": arms,
            "employer_return_high": employer_return_high,
            "worker_type": worker_type,
            "extra_work_units": extra_work,
            "productivity_index": productivity,
        }
    )
    return df


def add_box(
    ax: plt.Axes,
    xy: tuple[float, float],
    width: float,
    height: float,
    text: str,
    facecolor: str,
    edgecolor: str = "#334155",
    fontsize: int = 10,
    weight: str = "normal",
) -> None:
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=1.2,
        edgecolor=edgecolor,
        facecolor=facecolor,
    )
    ax.add_patch(patch)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        weight=weight,
        wrap=True,
    )


def generate_week12_figures() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({"figure.dpi": 160, "font.size": 10})

    colors = {
        "blue": "#1f5c99",
        "orange": "#c25b2a",
        "green": "#2a7f62",
        "gold": "#d8a25b",
        "gray": "#4b5563",
        "light": "#f5f7fb",
    }

    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    add_box(ax, (0.05, 0.76), 0.22, 0.14, "Nonstandard\npreferences", colors["blue"], fontsize=12, weight="bold")
    add_box(ax, (0.39, 0.76), 0.22, 0.14, "Nonstandard\nbeliefs", colors["orange"], fontsize=12, weight="bold")
    add_box(ax, (0.73, 0.76), 0.22, 0.14, "Nonstandard\ndecision-making", colors["green"], fontsize=12, weight="bold")
    add_box(ax, (0.05, 0.48), 0.22, 0.18, "Hours\nEffort\nSearch\nTraining", "#e9f2fb")
    add_box(ax, (0.39, 0.48), 0.22, 0.18, "Job choice\nAmenities\nTake-up\nJob valuation", "#fbeee7")
    add_box(ax, (0.73, 0.48), 0.22, 0.18, "Contract response\nSalience\nComplexity\nPerceived incentives", "#e9f7f2")
    add_box(ax, (0.22, 0.14), 0.24, 0.17, "Employer and manager response\nSimplify, frame, gift, monitor", colors["gold"])
    add_box(ax, (0.55, 0.14), 0.24, 0.17, "Policy response\nInform, remind, commit, regulate", "#efe6f7")
    for x_coord in [0.16, 0.50, 0.84]:
        ax.add_patch(
            FancyArrowPatch(
                (x_coord, 0.76),
                (x_coord, 0.66),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=1.4,
                color=colors["gray"],
            )
        )
    for start, end in [
        ((0.16, 0.48), (0.34, 0.31)),
        ((0.50, 0.48), (0.34, 0.31)),
        ((0.84, 0.48), (0.67, 0.31)),
        ((0.50, 0.48), (0.67, 0.31)),
    ]:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=1.3,
                color=colors["gray"],
            )
        )
    ax.text(
        0.5,
        0.96,
        "Behavioral labor maps mechanisms into labor-market objects and then into employer or policy response.",
        ha="center",
        va="center",
        fontsize=13,
        weight="bold",
    )
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "12-dellavigna-taxonomy-to-labor.png", bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    add_box(ax, (0.04, 0.58), 0.20, 0.16, "True contract\nWage, taxes, bonus\ntraining payoff", "#e9f2fb", fontsize=11, weight="bold")
    add_box(ax, (0.30, 0.58), 0.18, 0.16, "Preferences\n$u(c,h)$\n$\\beta$, fairness, identity", "#dbeafe")
    add_box(ax, (0.52, 0.58), 0.18, 0.16, "Beliefs\nsubjective returns\nexpected self-control", "#fde7d9")
    add_box(ax, (0.74, 0.58), 0.18, 0.16, "Decision rule\nsalience, opacity\ncomplexity", "#dcfce7")
    add_box(ax, (0.30, 0.22), 0.18, 0.16, "Observed choice\nhours, effort, search", "#f8fafc")
    add_box(ax, (0.52, 0.22), 0.18, 0.16, "Observed response\ntake-up, training,\njob choice", "#f8fafc")
    for start, end in [
        ((0.24, 0.66), (0.30, 0.66)),
        ((0.48, 0.66), (0.52, 0.66)),
        ((0.70, 0.66), (0.74, 0.66)),
        ((0.39, 0.58), (0.39, 0.38)),
        ((0.61, 0.58), (0.61, 0.38)),
        ((0.83, 0.58), (0.61, 0.38)),
    ]:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=1.4,
                color=colors["gray"],
            )
        )
    ax.text(0.14, 0.80, "Benchmark", color=colors["blue"], fontsize=12, weight="bold")
    ax.text(0.52, 0.80, "Behavioral wedges", color=colors["gray"], fontsize=12, weight="bold")
    ax.text(
        0.50,
        0.08,
        "The empirical task is to learn which wedge moved and which standard alternative that rules out.",
        ha="center",
        fontsize=12,
    )
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "12-benchmark-vs-behavioral-wedges.png", bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.axis("off")
    for col_idx, label in enumerate(["Preferences", "Beliefs", "Decision-making", "Welfare"]):
        add_box(ax, (0.9 + col_idx * 0.95, 4.25), 0.82, 0.42, label, colors["light"], fontsize=11, weight="bold")
    for row_idx, label in enumerate(["Field exp.", "Expectations", "Quasi-exp.", "Structural"]):
        add_box(ax, (0.05, 3.25 - row_idx * 0.85), 0.72, 0.42, label, colors["light"], fontsize=11, weight="bold")
    marks = {
        (0, 0): "gifts\ncommitment",
        (0, 2): "salience\ncomplexity",
        (1, 1): "subjective\nreturns",
        (2, 1): "timing\ndefaults",
        (2, 2): "deadlines\nreminders",
        (3, 0): "heterogeneity",
        (3, 1): "naive vs\nsophisticated",
        (3, 3): "counterfactual\npolicy",
    }
    fill_colors = ["#dbeafe", "#fde7d9", "#dcfce7", "#efe6f7"]
    for (row_idx, col_idx), text in marks.items():
        add_box(ax, (0.9 + col_idx * 0.95, 3.2 - row_idx * 0.85), 0.82, 0.46, text, fill_colors[col_idx])
    ax.text(2.6, 4.9, "Behavioral labor design map", ha="center", fontsize=14, weight="bold")
    ax.text(
        2.6,
        0.2,
        "No single design is enough when the mechanism could be preferences, beliefs, or perception.",
        ha="center",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "12-behavioral-labor-design-map.png", bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.plot([0.5, 0.5], [0.12, 0.88], color=colors["gray"], linewidth=1.2)
    ax.plot([0.12, 0.88], [0.5, 0.5], color=colors["gray"], linewidth=1.2)
    add_box(ax, (0.14, 0.58), 0.30, 0.24, "Attenuation\nlearning\nexperience\nsimplification", "#e9f7f2", fontsize=12)
    add_box(ax, (0.56, 0.58), 0.30, 0.24, "Amplification\nopaque contracts\nnaivete\nburden", "#fde7d9", fontsize=12)
    add_box(ax, (0.14, 0.18), 0.30, 0.24, "Employer response\nscreening\nframing\nmonitoring", "#e9f2fb", fontsize=12)
    add_box(ax, (0.56, 0.18), 0.30, 0.24, "Policy and welfare\ninternalities\ncommitment\nregulation", "#efe6f7", fontsize=12)
    ax.text(
        0.5,
        0.94,
        "From worker mechanism to market response to welfare interpretation",
        ha="center",
        fontsize=14,
        weight="bold",
    )
    ax.text(0.5, 0.53, "Market or policy response", ha="center", va="bottom", fontsize=11, weight="bold")
    ax.text(0.11, 0.5, "Worker friction persists", ha="right", va="center", rotation=90, fontsize=11, weight="bold")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "12-market-responses-and-welfare.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    TRANSFER_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(20260512)
    complexity_df = build_incentive_complexity_data(rng)
    gift_df = build_gift_exchange_data(rng)
    generate_week12_figures()

    complexity_df.to_csv(
        ORIGINAL_DIR / "abeler_huffman_raymond_incentive_complexity_synthetic.csv",
        index=False,
    )
    gift_df.to_csv(
        TRANSFER_DIR / "della_vigna_gift_exchange_synthetic.csv",
        index=False,
    )

    print(f"Wrote Week 12 complexity data to {ORIGINAL_DIR}")
    print(f"Wrote Week 12 gift-exchange data to {TRANSFER_DIR}")
    print(f"Wrote Week 12 figures to {FIGURE_DIR}")


if __name__ == "__main__":
    main()
