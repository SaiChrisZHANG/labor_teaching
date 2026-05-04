"""Generate conceptual figures for Labor I Week 3: dynamic labor supply.

The figures are synthetic and pedagogical. They are meant to support the Week 3
chapter and slides without requiring restricted data.
"""
from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] / ".mpl-cache"))

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "assets" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def lifecycle_profiles() -> None:
    ages = np.arange(22, 66)
    base = 0.42 + 0.018 * (ages - 22) - 0.00036 * (ages - 22) ** 2
    high_skill = np.clip(base + 0.05, 0.22, 0.78)
    caregiving_dip = 0.09 * np.exp(-((ages - 33) / 5.0) ** 2)
    family_timing = np.clip(base - 0.02 - caregiving_dip, 0.18, 0.74)

    plt.figure(figsize=(8, 5))
    plt.plot(ages, high_skill, linewidth=2.6, label="Higher-return / stronger attachment profile")
    plt.plot(ages, family_timing, linewidth=2.6, label="Profile with mid-career caregiving dip")
    plt.axvspan(29, 38, color="#d9d9d9", alpha=0.35)
    plt.text(30, 0.24, "Family timing\nand adjustment zone", fontsize=9)
    plt.xlabel("Age")
    plt.ylabel("Hours share of available time")
    plt.title("Synthetic lifecycle labor-supply profiles")
    plt.ylim(0.15, 0.82)
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "03-lifecycle-labor-supply-profiles.png", dpi=200)
    plt.close()


def temporary_permanent_responses() -> None:
    periods = np.arange(0, 10)
    temp = np.array([0.0, 0.36, 0.18, 0.08, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0])
    permanent = np.array([0.0, 0.18, 0.16, 0.14, 0.13, 0.12, 0.11, 0.10, 0.10, 0.09])
    temp_with_friction = np.array([0.0, 0.18, 0.16, 0.11, 0.06, 0.03, 0.01, 0.0, 0.0, 0.0])

    plt.figure(figsize=(8, 5))
    plt.plot(periods, temp, marker="o", linewidth=2.4, label="Temporary wage shock")
    plt.plot(periods, permanent, marker="s", linewidth=2.4, label="Permanent wage shock")
    plt.plot(
        periods,
        temp_with_friction,
        marker="^",
        linewidth=2.4,
        label="Temporary shock with adjustment frictions",
    )
    plt.axvline(1, linestyle="--", color="black", linewidth=1)
    plt.text(1.1, 0.33, "Shock arrives", fontsize=9)
    plt.xlabel("Periods since shock")
    plt.ylabel("Change in hours index")
    plt.title("Stylized dynamic labor-supply responses")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "03-temporary-permanent-shock-responses.png", dpi=200)
    plt.close()


def main() -> None:
    lifecycle_profiles()
    temporary_permanent_responses()
    print(f"Saved figures to {FIG_DIR}")


if __name__ == "__main__":
    main()
