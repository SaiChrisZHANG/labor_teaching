"""Shared figure house style for Labor I and Labor II assets."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgba
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DPI = 220

COLORS = {
    "ink": "#1F2933",
    "muted": "#52606D",
    "grid": "#D9E2EC",
    "navy": "#315C8D",
    "teal": "#3B7D73",
    "rust": "#B35C3F",
    "gold": "#B78843",
    "slate": "#748094",
    "surface": "#F5F7FA",
    "panel": "#EEF2F6",
    "panel_alt": "#FAFBFC",
}

SEQUENTIAL_CMAP = LinearSegmentedColormap.from_list(
    "labor_sequential",
    ["#F8FBFD", "#DDEAF2", "#B3CCDA", "#7FA4B8", "#315C8D"],
)


def rgba(color: str, alpha: float) -> tuple[float, float, float, float]:
    return to_rgba(color, alpha)


def apply_style() -> None:
    """Register a calm house style for chart and diagram scripts."""
    plt.style.use("default")
    plt.rcParams.update(
        {
            "figure.dpi": DPI,
            "savefig.dpi": DPI,
            "savefig.facecolor": "white",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.edgecolor": COLORS["muted"],
            "axes.linewidth": 0.9,
            "axes.titleweight": "semibold",
            "axes.titlesize": 13,
            "axes.labelsize": 10.5,
            "axes.labelcolor": COLORS["ink"],
            "axes.titlecolor": COLORS["ink"],
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "xtick.labelsize": 9.5,
            "ytick.labelsize": 9.5,
            "grid.color": COLORS["grid"],
            "grid.linewidth": 0.7,
            "grid.alpha": 0.9,
            "legend.frameon": False,
            "legend.fontsize": 9,
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "text.color": COLORS["ink"],
            "lines.solid_capstyle": "round",
            "lines.dash_capstyle": "round",
            "patch.edgecolor": "none",
            "patch.linewidth": 0.0,
            "mathtext.default": "regular",
        }
    )


def style_axis(ax, *, grid_axis: str = "y") -> None:
    """Apply consistent spine and grid treatment to quantitative charts."""
    ax.set_facecolor("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(COLORS["muted"])
    ax.spines["bottom"].set_color(COLORS["muted"])
    ax.tick_params(axis="both", colors=COLORS["muted"], labelcolor=COLORS["muted"])
    if grid_axis == "both":
        ax.grid(True)
    elif grid_axis == "x":
        ax.grid(axis="x")
    elif grid_axis == "y":
        ax.grid(axis="y")
    else:
        ax.grid(False)
    ax.set_axisbelow(True)


def clean_axis(ax, *, xlim: tuple[float, float], ylim: tuple[float, float]) -> None:
    """Hide axes for conceptual diagrams while preserving layout bounds."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_facecolor("white")


def save_figure(fig, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.patch.set_facecolor("white")
    fig.savefig(path, bbox_inches="tight", facecolor="white")


def add_box(
    ax,
    x: float,
    y: float,
    width: float,
    height: float,
    text: str,
    *,
    edge: str,
    face: str | None = None,
    fontsize: float = 11.5,
    weight: str = "semibold",
    rounding: float = 0.16,
    pad: float = 0.06,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle=f"round,pad={pad},rounding_size={rounding}",
        facecolor=face or rgba(edge, 0.12),
        edgecolor=edge,
        linewidth=1.8,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=COLORS["ink"],
        weight=weight,
    )
    return patch


def add_arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str | None = None,
    linewidth: float = 1.7,
    text: str | None = None,
    text_xy: tuple[float, float] | None = None,
    text_size: float = 9.5,
    connectionstyle: str | None = None,
    bidirectional: bool = False,
    linestyle: str = "-",
    alpha: float = 1.0,
    shrink_a: float = 8.0,
    shrink_b: float = 8.0,
) -> FancyArrowPatch:
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="<->" if bidirectional else "-|>",
        mutation_scale=14,
        linewidth=linewidth,
        color=color or COLORS["muted"],
        connectionstyle=connectionstyle,
        linestyle=linestyle,
        alpha=alpha,
        shrinkA=shrink_a,
        shrinkB=shrink_b,
    )
    ax.add_patch(patch)
    if text and text_xy:
        ax.text(text_xy[0], text_xy[1], text, ha="center", va="center", fontsize=text_size, color=COLORS["muted"])
    return patch
