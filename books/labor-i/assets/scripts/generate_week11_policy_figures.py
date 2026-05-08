#!/usr/bin/env python3
"""Generate Week 11 worker-policy teaching figures."""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, SEQUENTIAL_CMAP, add_arrow, add_box, apply_style, clean_axis, rgba, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def save_policy_margins_framework() -> None:
    fig, ax = plt.subplots(figsize=(11.0, 6.5))
    clean_axis(ax, xlim=(0, 10), ylim=(0, 6))

    add_box(ax, 3.7, 2.45, 2.6, 1.2, "Worker-targeted\npolicy design", edge=COLORS["navy"], fontsize=14.4)

    channels = [
        (1.0, 4.6, 1.9, 0.9, "Incentives\nphase-ins,\nphase-outs,\nearnings tests", COLORS["gold"]),
        (4.05, 4.7, 1.9, 0.85, "Investment\ntraining,\njob readiness,\nskill ladders", COLORS["teal"]),
        (7.1, 4.6, 1.9, 0.9, "Constraints\nchildcare,\nliquidity,\neligibility", COLORS["gold"]),
        (1.0, 1.0, 1.9, 0.9, "Insurance\nincome smoothing,\nconsumption risk", COLORS["gold"]),
        (7.1, 1.0, 1.9, 0.9, "Frictions\nknowledge,\nadmin burden,\nsalience", COLORS["gold"]),
    ]
    for x, y, w, h, text, edge in channels:
        add_box(ax, x, y, w, h, text, edge=edge, fontsize=10.5)

    margins = [
        (0.45, 2.55, 1.25, 0.46, "Participation"),
        (2.2, 0.35, 1.05, 0.46, "Hours"),
        (6.75, 0.35, 1.1, 0.46, "Search"),
        (8.25, 2.55, 0.9, 0.46, "Skill"),
        (4.15, 0.2, 1.7, 0.46, "Household time"),
        (4.25, 3.85, 1.5, 0.46, "Mobility"),
    ]
    for x, y, w, h, text in margins:
        add_box(ax, x, y, w, h, text, edge=COLORS["teal"], fontsize=10, face=rgba(COLORS["teal"], 0.10))

    incoming = [
        ((1.95, 4.6), (4.05, 3.3), (2.9, 4.1)),
        ((5.0, 4.7), (5.0, 3.65), (5.6, 4.2)),
        ((8.05, 4.6), (5.95, 3.3), (7.2, 4.1)),
        ((1.95, 1.9), (4.05, 2.8), (2.9, 1.95)),
        ((8.05, 1.9), (5.95, 2.8), (7.2, 1.95)),
    ]
    for start, end, _text_xy in incoming:
        add_arrow(ax, start, end, color=COLORS["muted"])

    outgoing = [
        ((3.7, 2.95), (1.1, 2.78)),
        ((4.32, 2.45), (2.72, 0.82)),
        ((5.68, 2.45), (7.3, 0.82)),
        ((6.3, 2.95), (8.7, 2.78)),
        ((5.0, 3.65), (5.0, 3.85)),
        ((5.0, 2.45), (5.0, 0.66)),
    ]
    for start, end in outgoing:
        add_arrow(ax, start, end, color=COLORS["teal"], linewidth=1.8)

    ax.text(
        5.0,
        5.98,
        "Worker-side policy maps channels to labor-market margins.",
        ha="center",
        va="top",
        fontsize=11.2,
        color=COLORS["ink"],
        weight="semibold",
    )
    ax.text(
        5.0,
        0.02,
        "Week 11 asks which worker-side margin the policy actually moves, and through which channel.",
        ha="center",
        va="bottom",
        fontsize=10,
        color=COLORS["muted"],
    )
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "11-policy-margins-framework.png")
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

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.8))

    axes[0].plot(earnings, baseline, color=COLORS["muted"], linewidth=2.0, label="No earnings subsidy")
    axes[0].plot(earnings, with_credit, color=COLORS["navy"], linewidth=2.5, label="With in-work credit")
    axes[0].axvspan(0, 10, color=COLORS["gold"], alpha=0.12)
    axes[0].axvspan(10, 22, color=COLORS["teal"], alpha=0.08)
    axes[0].axvspan(22, 40, color=COLORS["rust"], alpha=0.08)
    axes[0].set_title("Policy-adjusted budget set")
    axes[0].set_xlabel("Annual earnings (thousands)")
    axes[0].set_ylabel("Net resources")
    axes[0].legend(loc="upper left")
    style_axis(axes[0], grid_axis="both")

    axes[1].plot(earnings, marginal_rate, color=COLORS["navy"], linewidth=2.4)
    axes[1].axhline(1.0, color=COLORS["muted"], linestyle="--", linewidth=1.0)
    axes[1].axvline(10, color=COLORS["muted"], linestyle=":", linewidth=1.0)
    axes[1].axvline(22, color=COLORS["muted"], linestyle=":", linewidth=1.0)
    axes[1].set_ylim(0.65, 1.55)
    axes[1].set_title("Effective return to earnings")
    axes[1].set_xlabel("Annual earnings (thousands)")
    axes[1].set_ylabel(r"$d(\mathrm{net\ resources}) / d(\mathrm{earnings})$")
    axes[1].text(4.2, 1.42, "Phase-in", color=COLORS["gold"], fontsize=9.5)
    axes[1].text(13.2, 1.08, "Plateau", color=COLORS["teal"], fontsize=9.5)
    axes[1].text(29.0, 0.83, "Phase-out", color=COLORS["rust"], fontsize=9.5)
    style_axis(axes[1], grid_axis="both")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "11-tax-credit-budget-set.png")
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
    ax.plot(x, y, color=COLORS["navy"], linewidth=2.5)
    ax.fill_between(x, y, color=rgba(COLORS["navy"], 0.18))

    for label, (px, py) in points.items():
        ax.scatter(px, py, s=42, color=COLORS["rust"], zorder=3)
        ax.text(px + 0.018, py + 0.02, label, fontsize=8.8, color=COLORS["muted"])

    ax.set_xlim(0.1, 1.02)
    ax.set_ylim(0.1, 1.02)
    ax.set_xlabel("Insurance value / consumption smoothing")
    ax.set_ylabel("Search or work distortion cost")
    ax.set_title("Insurance-incentive trade-offs are policy-design objects")
    ax.text(0.15, 0.16, "Better delivery can shift the frontier inward.", color=COLORS["teal"], fontsize=9)
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "11-insurance-incentive-frontier.png")
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

    fig, ax = plt.subplots(figsize=(8.6, 5.3))
    clean_axis(ax, xlim=(0, 1), ylim=(0, 1))
    colors = ["#315C8D", "#4873A0", "#638CB1", "#80A6C3", "#A2BED3", "#C8D9E7"]
    y = 0.92
    height = 0.105

    for idx, (label, value) in enumerate(stages):
        width = value / 112
        left = 0.5 - width / 2
        rect = Rectangle((left, y - height), width, height * 0.78, facecolor=colors[idx], edgecolor="none")
        ax.add_patch(rect)
        ax.text(0.5, y - height / 2, f"{label}: {value}", ha="center", va="center", color="white", fontsize=10, weight="semibold")
        y -= 0.125

    ax.text(0.5, 0.07, "Take-up falls at every delivery stage, so statutory generosity is not effective exposure.", ha="center", fontsize=10, color=COLORS["muted"])
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "11-takeup-salience-funnel.png")
    plt.close(fig)


def save_policy_design_toolkit() -> None:
    designs = ["Kink /\nbunching", "Field\nexperiment", "Reform\nevent study", "Judge /\nexaminer IV", "Knowledge /\nexposure"]
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

    fig, ax = plt.subplots(figsize=(9.0, 4.9))
    image = ax.imshow(values, cmap=SEQUENTIAL_CMAP, vmin=0, vmax=1)
    ax.set_xticks(range(len(margins)), margins)
    ax.set_yticks(range(len(designs)), designs)
    ax.set_title("Design choice should match the policy margin")

    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            ax.text(col, row, f"{values[row, col]:.1f}", ha="center", va="center", color=COLORS["ink"], fontsize=8.8)

    cbar = fig.colorbar(image, ax=ax, shrink=0.86)
    cbar.set_label("How naturally the design speaks to the margin")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "11-policy-design-toolkit.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    save_policy_margins_framework()
    save_tax_credit_budget_set()
    save_insurance_incentive_frontier()
    save_takeup_salience_funnel()
    save_policy_design_toolkit()
    print(f"Wrote Week 11 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
