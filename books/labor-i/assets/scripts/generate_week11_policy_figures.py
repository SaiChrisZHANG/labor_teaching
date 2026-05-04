#!/usr/bin/env python3
"""Generate Week 11 worker-policy teaching figures."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def setup_style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
        }
    )


def save_policy_margins_framework() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    ax.axis("off")

    center = (0.5, 0.52)
    policy_box = dict(boxstyle="round,pad=0.45", facecolor="#eef3fb", edgecolor="#1f5c99", linewidth=1.4)
    margin_box = dict(boxstyle="round,pad=0.35", facecolor="#f9efe3", edgecolor="#c25b2a", linewidth=1.2)

    ax.text(
        center[0],
        center[1],
        "Worker-targeted\npolicy design",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        bbox=policy_box,
    )

    channels = [
        ("Incentives", (0.20, 0.82), "phase-ins,\nphase-outs,\nearnings tests"),
        ("Constraints", (0.80, 0.82), "childcare,\nliquidity,\neligibility"),
        ("Insurance", (0.18, 0.25), "income smoothing,\nconsumption risk"),
        ("Frictions", (0.82, 0.25), "knowledge,\nadmin burden,\nsalience"),
        ("Investment", (0.50, 0.90), "training,\njob readiness,\nskill ladders"),
    ]
    margins = [
        ("Participation", (0.12, 0.55)),
        ("Hours", (0.27, 0.14)),
        ("Search", (0.73, 0.14)),
        ("Skill", (0.88, 0.55)),
        ("Household time", (0.50, 0.05)),
        ("Mobility", (0.50, 0.76)),
    ]

    for label, (x, y), detail in channels:
        ax.text(x, y, f"{label}\n{detail}", ha="center", va="center", bbox=margin_box)
        ax.annotate(
            "",
            xy=center,
            xytext=(x, y),
            arrowprops=dict(arrowstyle="-", color="#6b7280", linewidth=1.5),
        )

    for label, (x, y) in margins:
        ax.text(x, y, label, ha="center", va="center", bbox=margin_box)
        ax.annotate(
            "",
            xy=(x, y),
            xytext=center,
            arrowprops=dict(arrowstyle="->", color="#2a7f62", linewidth=1.5),
        )

    ax.text(
        0.5,
        -0.02,
        "Week 11 asks which worker-side margin the policy actually moves, and through which channel.",
        ha="center",
        va="top",
        fontsize=10,
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "11-policy-margins-framework.png", bbox_inches="tight")
    plt.close(fig)


def save_tax_credit_budget_set() -> None:
    earnings = np.linspace(0, 40, 401)
    baseline = 8 + earnings
    credit = np.piecewise(
        earnings,
        [earnings <= 10, (earnings > 10) & (earnings <= 22), earnings > 22],
        [lambda x: 0.45 * x, 4.5, lambda x: np.maximum(4.5 - 0.20 * (x - 22), 0)],
    )
    with_credit = baseline + credit
    marginal_rate = np.gradient(with_credit, earnings)

    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))

    axes[0].plot(earnings, baseline, color="#4b5563", linewidth=2.0, label="No earnings subsidy")
    axes[0].plot(earnings, with_credit, color="#c25b2a", linewidth=2.4, label="With in-work credit")
    axes[0].axvspan(0, 10, color="#d8a25b", alpha=0.16)
    axes[0].axvspan(10, 22, color="#2a7f62", alpha=0.10)
    axes[0].axvspan(22, 40, color="#7d5ba6", alpha=0.10)
    axes[0].set_title("Policy-adjusted budget set")
    axes[0].set_xlabel("Annual earnings (thousands)")
    axes[0].set_ylabel("Net resources")
    axes[0].legend(frameon=False, loc="upper left")

    axes[1].plot(earnings, marginal_rate, color="#1f5c99", linewidth=2.3)
    axes[1].axhline(1.0, color="#555555", linestyle="--", linewidth=1.2)
    axes[1].axvline(10, color="#555555", linestyle=":", linewidth=1.0)
    axes[1].axvline(22, color="#555555", linestyle=":", linewidth=1.0)
    axes[1].set_ylim(0.65, 1.55)
    axes[1].set_title("Effective return to earnings")
    axes[1].set_xlabel("Annual earnings (thousands)")
    axes[1].set_ylabel("d(net resources) / d(earnings)")
    axes[1].text(4.2, 1.42, "Phase-in", color="#8a4b10")
    axes[1].text(13.2, 1.08, "Plateau", color="#1f5f49")
    axes[1].text(29.0, 0.83, "Phase-out", color="#5e3c8c")

    fig.tight_layout()
    fig.savefig(FIG_DIR / "11-tax-credit-budget-set.png", bbox_inches="tight")
    plt.close(fig)


def save_insurance_incentive_frontier() -> None:
    x = np.linspace(0.15, 1.0, 200)
    y = 0.98 - 0.78 * (x - 0.15) ** 1.35
    y = np.clip(y, 0.16, 1.0)

    points = {
        "Flat cash grant": (0.22, 0.90),
        "Standard UI": (0.45, 0.72),
        "Front-loaded UI": (0.58, 0.63),
        "Search assistance": (0.70, 0.47),
        "Take-up simplification": (0.34, 0.82),
    }

    fig, ax = plt.subplots(figsize=(7.8, 5.4))
    ax.plot(x, y, color="#1f5c99", linewidth=2.5)
    ax.fill_between(x, y, color="#dbe8f8", alpha=0.7)

    for label, (px, py) in points.items():
        ax.scatter(px, py, s=70, color="#c25b2a")
        ax.text(px + 0.015, py + 0.02, label, fontsize=9)

    ax.set_xlim(0.1, 1.02)
    ax.set_ylim(0.1, 1.02)
    ax.set_xlabel("Insurance value / consumption smoothing")
    ax.set_ylabel("Search or work distortion cost")
    ax.set_title("Insurance-incentive trade-offs are policy-design objects")
    ax.text(0.15, 0.16, "Better delivery can shift the frontier inward.", color="#2a7f62", fontsize=9)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "11-insurance-incentive-frontier.png", bbox_inches="tight")
    plt.close(fig)


def save_takeup_salience_funnel() -> None:
    stages = [
        ("Eligible", 100),
        ("Knows program", 78),
        ("Understands gain", 61),
        ("Starts application", 47),
        ("Completes filing", 39),
        ("Receives full-value benefit", 33),
    ]

    fig, ax = plt.subplots(figsize=(8.4, 5.4))
    ax.axis("off")
    colors = ["#1f5c99", "#3d74ad", "#5a8dbb", "#7aa2c8", "#9ab8d6", "#bcd0e5"]
    y = 0.92
    height = 0.11

    for idx, (label, value) in enumerate(stages):
        width = value / 110
        left = 0.5 - width / 2
        rect = plt.Rectangle((left, y - height), width, height * 0.82, color=colors[idx], alpha=0.95)
        ax.add_patch(rect)
        ax.text(0.5, y - height / 2, f"{label}: {value}", ha="center", va="center", color="white", fontweight="bold")
        y -= 0.13

    ax.text(0.5, 0.08, "Take-up falls at every delivery stage, so statutory generosity is not effective exposure.", ha="center")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "11-takeup-salience-funnel.png", bbox_inches="tight")
    plt.close(fig)


def save_policy_design_toolkit() -> None:
    designs = [
        "Kink /\nbunching",
        "Field\nexperiment",
        "Reform\nevent study",
        "Judge /\nexaminer IV",
        "Knowledge /\nexposure",
    ]
    margins = ["Participation", "Hours", "Search", "Take-up", "Timing", "Welfare"]
    values = np.array(
        [
            [0.9, 0.8, 0.2, 0.3, 0.6, 0.3],
            [0.4, 0.3, 0.8, 0.9, 0.4, 0.5],
            [0.8, 0.6, 0.7, 0.5, 0.6, 0.4],
            [0.5, 0.2, 0.4, 0.2, 0.3, 0.7],
            [0.6, 0.4, 0.3, 0.9, 0.5, 0.3],
        ]
    )

    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    image = ax.imshow(values, cmap="YlGnBu", vmin=0, vmax=1)
    ax.set_xticks(range(len(margins)), margins)
    ax.set_yticks(range(len(designs)), designs)
    ax.set_title("Design choice should match the policy margin")

    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            ax.text(col, row, f"{values[row, col]:.1f}", ha="center", va="center", color="#0f172a", fontsize=9)

    cbar = fig.colorbar(image, ax=ax, shrink=0.86)
    cbar.set_label("How naturally the design speaks to the margin")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "11-policy-design-toolkit.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    setup_style()
    save_policy_margins_framework()
    save_tax_credit_budget_set()
    save_insurance_incentive_frontier()
    save_takeup_salience_funnel()
    save_policy_design_toolkit()
    print(f"Wrote Week 11 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
