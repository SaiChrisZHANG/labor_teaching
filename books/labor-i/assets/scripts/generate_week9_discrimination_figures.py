#!/usr/bin/env python3
"""Generate conceptual Week 9 figures for discrimination, measurement, and sorting."""
from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, SEQUENTIAL_CMAP, apply_style, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def make_gap_vs_discrimination() -> None:
    labels = ["Raw gap", "After pre-treatment controls", "Direct treatment effect"]
    explained = np.array([0.42, 0.24, 0.00])
    treatment = np.array([0.18, 0.12, 0.12])
    sorting = np.array([0.10, 0.08, 0.00])

    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    x = np.arange(len(labels))
    ax.bar(x, explained, color=COLORS["gold"], label="Composition / pre-market factors")
    ax.bar(x, treatment, bottom=explained, color=COLORS["rust"], label="Treatment wedge")
    ax.bar(x, sorting, bottom=explained + treatment, color=COLORS["teal"], label="Sorting / allocation")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Stylized outcome difference")
    ax.set_title("Gap objects are not the same as discrimination objects")
    ax.legend(loc="upper right")
    ax.text(
        0.02,
        0.04,
        "Conditioning can clarify a gap, but it can also partial out mechanisms that are themselves downstream of discrimination.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(ax, grid_axis="y")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "09-gap-vs-discrimination-schematic.png")
    plt.close(fig)


def make_audit_identification() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.6))

    for idx, label in enumerate(["Signal A", "Signal B"]):
        y = 0.75 - idx * 0.35
        axes[0].add_patch(Rectangle((0.06, y - 0.08), 0.25, 0.16, facecolor=(0.19, 0.36, 0.55, 0.12), edgecolor=COLORS["navy"], linewidth=1.2))
        axes[0].text(0.185, y, "Same resume\nquality bundle", ha="center", va="center", fontsize=9)
        axes[0].add_patch(Rectangle((0.42, y - 0.08), 0.17, 0.16, facecolor=(0.72, 0.53, 0.26, 0.12), edgecolor=COLORS["gold"], linewidth=1.2))
        axes[0].text(0.505, y, label, ha="center", va="center", fontsize=9)
        axes[0].annotate("", xy=(0.42, y), xytext=(0.31, y), arrowprops={"arrowstyle": "-|>", "lw": 1.6, "color": COLORS["muted"]})
        axes[0].add_patch(Rectangle((0.72, y - 0.08), 0.18, 0.16, facecolor=(0.23, 0.49, 0.45, 0.12), edgecolor=COLORS["teal"], linewidth=1.2))
        axes[0].text(0.81, y, "Callback", ha="center", va="center", fontsize=9)
        axes[0].annotate("", xy=(0.72, y), xytext=(0.59, y), arrowprops={"arrowstyle": "-|>", "lw": 1.6, "color": COLORS["muted"]})
    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(0.15, 0.95)
    axes[0].axis("off")
    axes[0].set_title("Hold qualifications fixed")

    rates = np.array([0.112, 0.078])
    axes[1].bar(["Signal A", "Signal B"], rates, color=[COLORS["navy"], COLORS["rust"]], width=0.58)
    axes[1].set_ylim(0, 0.14)
    axes[1].set_ylabel("Callback rate")
    axes[1].set_title("Treatment effect at the callback stage")
    for idx, rate in enumerate(rates):
        axes[1].text(idx, rate + 0.004, f"{rate:.1%}", ha="center", va="bottom", fontsize=9)
    axes[1].text(
        0.04,
        0.90,
        r"$\tau^{cb}$ isolates treatment in screening, not the full equilibrium wedge.",
        transform=axes[1].transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    style_axis(axes[1], grid_axis="y")

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "09-audit-identification-schematic.png")
    plt.close(fig)


def make_mechanism_comparison() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.1))

    axes[0].bar(["Group 0", "Group 1"], [1.0, 0.76], color=COLORS["rust"], width=0.65)
    axes[0].set_title("Taste-based")
    axes[0].set_ylabel("Net employer value")
    axes[0].text(0.04, 0.88, "Utility or cost wedge", transform=axes[0].transAxes, fontsize=9, color=COLORS["muted"])
    style_axis(axes[0], grid_axis="y")

    signal = np.linspace(-2, 2, 100)
    axes[1].plot(signal, 0.55 + 0.14 * signal, color=COLORS["muted"], lw=2.0, label="Group 0")
    axes[1].plot(signal, 0.48 + 0.14 * signal, color=COLORS["navy"], lw=2.2, label="Group 1")
    axes[1].axhline(0.60, color=COLORS["muted"], linestyle="--", lw=1.2)
    axes[1].set_title("Belief-based")
    axes[1].set_xlabel("Observed signal")
    axes[1].set_ylabel("Expected productivity")
    axes[1].legend(loc="lower right", fontsize=8)
    style_axis(axes[1], grid_axis="both")

    heat = np.array([[0.42, 0.35, 0.23], [0.24, 0.37, 0.39]])
    image = axes[2].imshow(heat, cmap=SEQUENTIAL_CMAP, vmin=0.15, vmax=0.45)
    axes[2].set_xticks(range(3), ["Low premium", "Mid premium", "High premium"], rotation=18)
    axes[2].set_yticks(range(2), ["Group 0", "Group 1"])
    axes[2].set_title("Sorting-based")
    for row in range(heat.shape[0]):
        for col in range(heat.shape[1]):
            axes[2].text(col, row, f"{heat[row, col]:.2f}", ha="center", va="center", color=COLORS["ink"], fontsize=8.5)
    fig.colorbar(image, ax=axes[2], fraction=0.05, pad=0.04)

    fig.tight_layout()
    save_figure(fig, FIG_DIR / "09-discrimination-mechanisms.png")
    plt.close(fig)


def make_sorting_heatmap() -> None:
    shares = np.array([[0.34, 0.31, 0.22, 0.13], [0.26, 0.29, 0.28, 0.17], [0.18, 0.25, 0.31, 0.26]])
    row_labels = ["Group 0: applicants", "Group 0: employed", "Group 1: employed"]
    col_labels = ["Segment A", "Segment B", "Segment C", "Segment D"]

    fig, ax = plt.subplots(figsize=(8.4, 5.1))
    image = ax.imshow(shares, cmap=SEQUENTIAL_CMAP, vmin=0.10, vmax=0.36)
    ax.set_xticks(range(len(col_labels)), col_labels)
    ax.set_yticks(range(len(row_labels)), row_labels)
    ax.set_title("Differential assignment across labor-market segments")
    for row in range(shares.shape[0]):
        for col in range(shares.shape[1]):
            ax.text(col, row, f"{shares[row, col]:.2f}", ha="center", va="center", color=COLORS["ink"], fontsize=8.5)
    ax.text(
        0.01,
        -0.16,
        "Interpret the cells as assignment shares to firm, occupation, or task segments with different premia or advancement paths.",
        transform=ax.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    fig.colorbar(image, ax=ax, fraction=0.05, pad=0.04)
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "09-sorting-segmentation-heatmap.png")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    apply_style()
    make_gap_vs_discrimination()
    make_audit_identification()
    make_mechanism_comparison()
    make_sorting_heatmap()
    print(f"Wrote Week 9 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
