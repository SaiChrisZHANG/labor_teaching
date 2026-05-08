"""Generate conceptual figures for Labor I Week 3: dynamic labor supply."""
from __future__ import annotations

import os
from pathlib import Path
import sys

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from shared.figure_style import COLORS, apply_style, save_figure, style_axis


ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "assets" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def lifecycle_profiles() -> None:
    ages = np.arange(22, 66)
    base = 0.42 + 0.018 * (ages - 22) - 0.00036 * (ages - 22) ** 2
    high_skill = np.clip(base + 0.05, 0.22, 0.78)
    caregiving_dip = 0.09 * np.exp(-((ages - 33) / 5.0) ** 2)
    family_timing = np.clip(base - 0.02 - caregiving_dip, 0.18, 0.74)

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    ax.plot(ages, high_skill, linewidth=2.6, color=COLORS["navy"], label="Higher-return / stronger attachment")
    ax.plot(ages, family_timing, linewidth=2.6, color=COLORS["rust"], label="Profile with mid-career caregiving dip")
    ax.axvspan(29, 38, color=COLORS["grid"], alpha=0.6)
    ax.text(30.0, 0.24, "Family timing\nand adjustment zone", fontsize=9, color=COLORS["muted"])
    ax.set_xlabel("Age")
    ax.set_ylabel("Hours share of available time")
    ax.set_title("Synthetic lifecycle labor-supply profiles")
    ax.set_ylim(0.15, 0.82)
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "03-lifecycle-labor-supply-profiles.png")
    plt.close(fig)


def temporary_permanent_responses() -> None:
    periods = np.arange(0, 10)
    temp = np.array([0.0, 0.36, 0.18, 0.08, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0])
    permanent = np.array([0.0, 0.18, 0.16, 0.14, 0.13, 0.12, 0.11, 0.10, 0.10, 0.09])
    temp_with_friction = np.array([0.0, 0.18, 0.16, 0.11, 0.06, 0.03, 0.01, 0.0, 0.0, 0.0])

    fig, ax = plt.subplots(figsize=(8.2, 5.2))
    ax.plot(periods, temp, marker="o", linewidth=2.4, color=COLORS["navy"], label="Temporary wage shock")
    ax.plot(periods, permanent, marker="s", linewidth=2.4, color=COLORS["rust"], label="Permanent wage shock")
    ax.plot(
        periods,
        temp_with_friction,
        marker="^",
        linewidth=2.4,
        color=COLORS["teal"],
        label="Temporary shock with adjustment frictions",
    )
    ax.axvline(1, linestyle="--", color=COLORS["muted"], linewidth=1.2)
    ax.text(1.12, 0.33, "Shock arrives", fontsize=9, color=COLORS["muted"])
    ax.set_xlabel("Periods since shock")
    ax.set_ylabel("Change in hours index")
    ax.set_title("Stylized dynamic labor-supply responses")
    ax.legend(loc="upper right")
    style_axis(ax, grid_axis="both")
    fig.tight_layout()
    save_figure(fig, FIG_DIR / "03-temporary-permanent-shock-responses.png")
    plt.close(fig)


def main() -> None:
    apply_style()
    lifecycle_profiles()
    temporary_permanent_responses()
    print(f"Saved figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
