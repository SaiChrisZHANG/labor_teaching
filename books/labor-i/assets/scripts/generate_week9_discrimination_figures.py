#!/usr/bin/env python3
"""Generate conceptual Week 9 figures for discrimination, measurement, and sorting."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"


def style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 150,
            "axes.titlesize": 14,
            "axes.labelsize": 11,
            "font.size": 10,
        }
    )


def make_gap_vs_discrimination() -> None:
    labels = ["Raw gap", "After pre-treatment controls", "Direct treatment effect"]
    explained = np.array([0.42, 0.24, 0.00])
    treatment = np.array([0.18, 0.12, 0.12])
    sorting = np.array([0.10, 0.08, 0.00])

    fig, ax = plt.subplots(figsize=(8.8, 5.1))
    x = np.arange(len(labels))
    ax.bar(x, explained, color="#d8a25b", label="Composition / pre-market factors")
    ax.bar(x, treatment, bottom=explained, color="#c25b2a", label="Treatment wedge")
    ax.bar(x, sorting, bottom=explained + treatment, color="#5b8c5a", label="Sorting / allocation")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Stylized outcome difference")
    ax.set_title("Gap objects are not the same as discrimination objects")
    ax.legend(frameon=False, loc="upper right")
    ax.text(
        0.02,
        0.04,
        "Conditioning can clarify a gap, but it can also partial out mechanisms that are themselves downstream of discrimination.",
        transform=ax.transAxes,
        fontsize=9,
        color="#374151",
    )
    fig.tight_layout()
    fig.savefig(FIG_DIR / "09-gap-vs-discrimination-schematic.png", bbox_inches="tight")
    plt.close(fig)


def make_audit_identification() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.7))

    for idx, label in enumerate(["Signal A", "Signal B"]):
        y = 0.75 - idx * 0.35
        axes[0].add_patch(plt.Rectangle((0.05, y - 0.08), 0.25, 0.16, facecolor="#dbeafe", edgecolor="#1f5c99"))
        axes[0].text(0.175, y, "Same resume\nquality bundle", ha="center", va="center")
        axes[0].add_patch(plt.Rectangle((0.40, y - 0.08), 0.18, 0.16, facecolor="#fef3c7", edgecolor="#c25b2a"))
        axes[0].text(0.49, y, label, ha="center", va="center")
        axes[0].annotate("", xy=(0.40, y), xytext=(0.30, y), arrowprops={"arrowstyle": "->", "lw": 1.8})
        axes[0].add_patch(plt.Rectangle((0.70, y - 0.08), 0.20, 0.16, facecolor="#dcfce7", edgecolor="#2a7f62"))
        axes[0].text(0.80, y, "Callback", ha="center", va="center")
        axes[0].annotate("", xy=(0.70, y), xytext=(0.58, y), arrowprops={"arrowstyle": "->", "lw": 1.8})
    axes[0].set_xlim(0, 1)
    axes[0].set_ylim(0.15, 0.95)
    axes[0].axis("off")
    axes[0].set_title("Hold qualifications fixed")

    rates = np.array([0.112, 0.078])
    axes[1].bar(["Signal A", "Signal B"], rates, color=["#1f5c99", "#c25b2a"], width=0.6)
    axes[1].set_ylim(0, 0.14)
    axes[1].set_ylabel("Callback rate")
    axes[1].set_title("Treatment effect at the callback stage")
    for idx, rate in enumerate(rates):
        axes[1].text(idx, rate + 0.004, f"{rate:.1%}", ha="center", va="bottom", fontsize=10)
    axes[1].text(
        0.04,
        0.90,
        r"$\tau^{cb}$ isolates treatment in screening, not the full equilibrium wedge.",
        transform=axes[1].transAxes,
        fontsize=9,
        color="#374151",
    )

    fig.tight_layout()
    fig.savefig(FIG_DIR / "09-audit-identification-schematic.png", bbox_inches="tight")
    plt.close(fig)


def make_mechanism_comparison() -> None:
    titles = ["Taste-based", "Belief-based", "Sorting-based"]
    colors = ["#c25b2a", "#1f5c99", "#2a7f62"]

    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))

    axes[0].bar(["Group 0", "Group 1"], [1.0, 0.76], color=colors[0])
    axes[0].set_title(titles[0])
    axes[0].set_ylabel("Net employer value")
    axes[0].text(0.04, 0.88, "Utility or cost wedge", transform=axes[0].transAxes, fontsize=9)

    signal = np.linspace(-2, 2, 100)
    axes[1].plot(signal, 0.55 + 0.14 * signal, color="#4b5563", lw=2.0, label="Group 0")
    axes[1].plot(signal, 0.48 + 0.14 * signal, color=colors[1], lw=2.3, label="Group 1")
    axes[1].axhline(0.60, color="#9ca3af", linestyle="--", lw=1.4)
    axes[1].set_title(titles[1])
    axes[1].set_xlabel("Observed signal")
    axes[1].set_ylabel("Expected productivity")
    axes[1].legend(frameon=False, fontsize=8, loc="lower right")

    heat = np.array(
        [
            [0.42, 0.35, 0.23],
            [0.24, 0.37, 0.39],
        ]
    )
    im = axes[2].imshow(heat, cmap="YlGnBu", vmin=0.15, vmax=0.45)
    axes[2].set_xticks(range(3), ["Low premium", "Mid premium", "High premium"], rotation=20)
    axes[2].set_yticks(range(2), ["Group 0", "Group 1"])
    axes[2].set_title(titles[2])
    for r in range(heat.shape[0]):
        for c in range(heat.shape[1]):
            axes[2].text(c, r, f"{heat[r, c]:.2f}", ha="center", va="center", color="#0f172a", fontsize=9)
    fig.colorbar(im, ax=axes[2], fraction=0.046, pad=0.04)

    fig.tight_layout()
    fig.savefig(FIG_DIR / "09-discrimination-mechanisms.png", bbox_inches="tight")
    plt.close(fig)


def make_sorting_heatmap() -> None:
    shares = np.array(
        [
            [0.34, 0.31, 0.22, 0.13],
            [0.26, 0.29, 0.28, 0.17],
            [0.18, 0.25, 0.31, 0.26],
        ]
    )
    row_labels = ["Group 0: applicants", "Group 0: employed", "Group 1: employed"]
    col_labels = ["Segment A", "Segment B", "Segment C", "Segment D"]

    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    im = ax.imshow(shares, cmap="YlOrBr", vmin=0.10, vmax=0.36)
    ax.set_xticks(range(len(col_labels)), col_labels)
    ax.set_yticks(range(len(row_labels)), row_labels)
    ax.set_title("Differential assignment across labor-market segments")
    for r in range(shares.shape[0]):
        for c in range(shares.shape[1]):
            ax.text(c, r, f"{shares[r, c]:.2f}", ha="center", va="center", color="#111827", fontsize=9)
    ax.text(
        0.01,
        -0.16,
        "Interpret the cells as assignment shares to firm, occupation, or task segments with different premia or advancement paths.",
        transform=ax.transAxes,
        fontsize=9,
        color="#374151",
    )
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "09-sorting-segmentation-heatmap.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    style()
    make_gap_vs_discrimination()
    make_audit_identification()
    make_mechanism_comparison()
    make_sorting_heatmap()
    print(f"Wrote Week 9 figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
