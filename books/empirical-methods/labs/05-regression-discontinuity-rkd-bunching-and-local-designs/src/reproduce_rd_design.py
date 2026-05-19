"""Run the Week 5 close-election RD reproduce and diagnose workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week5_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week5_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def kernel_weights(running: np.ndarray, bandwidth: float, kernel: str) -> np.ndarray:
    scaled = np.abs(running / bandwidth)
    inside = scaled <= 1.0
    if kernel == "triangular":
        weights = np.maximum(1.0 - scaled, 0.0)
    elif kernel == "uniform":
        weights = inside.astype(float)
    else:
        raise ValueError(f"unknown kernel: {kernel}")
    weights[~inside] = 0.0
    return weights


def weighted_ls(y: np.ndarray, x: np.ndarray, weights: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    keep = weights > 0
    y_k = y[keep]
    x_k = x[keep]
    w_k = weights[keep]
    xwx = x_k.T @ (w_k[:, None] * x_k)
    xwy = x_k.T @ (w_k * y_k)
    beta = np.linalg.pinv(xwx) @ xwy
    residual = y_k - x_k @ beta
    meat = x_k.T @ ((w_k**2 * residual**2)[:, None] * x_k)
    bread = np.linalg.pinv(xwx)
    n, k = x_k.shape
    scale = n / max(n - k, 1)
    cov = scale * bread @ meat @ bread
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    return beta, se


def rd_design_matrix(
    running: np.ndarray,
    order: int,
    covariates: pd.DataFrame | None = None,
) -> tuple[np.ndarray, list[str]]:
    treatment = (running >= 0).astype(float)
    columns = [np.ones_like(running), treatment]
    names = ["intercept_left", "cutoff_jump"]
    for power in range(1, order + 1):
        term = running**power
        columns.append(term)
        columns.append(treatment * term)
        names.append(f"running_power_{power}_left")
        names.append(f"running_power_{power}_right_difference")
    if covariates is not None:
        for col in covariates.columns:
            values = covariates[col].astype(float).to_numpy()
            sd = values.std(ddof=0)
            if sd > 0:
                values = (values - values.mean()) / sd
            else:
                values = values - values.mean()
            columns.append(values)
            names.append(f"covariate_{col}")
    return np.column_stack(columns), names


def local_rd(
    df: pd.DataFrame,
    outcome: str,
    bandwidth: float,
    order: int = 1,
    kernel: str = "triangular",
    covariates: list[str] | None = None,
) -> dict[str, float | str]:
    running = df["vote_margin"].to_numpy(dtype=float)
    y = df[outcome].to_numpy(dtype=float)
    weights = kernel_weights(running, bandwidth, kernel)
    cov_df = df[covariates] if covariates else None
    x, names = rd_design_matrix(running, order, cov_df)
    beta, se = weighted_ls(y, x, weights)
    jump_index = names.index("cutoff_jump")
    inside = weights > 0
    return {
        "outcome": outcome,
        "bandwidth": bandwidth,
        "order": float(order),
        "kernel": kernel,
        "covariates": ",".join(covariates or []),
        "estimate": float(beta[jump_index]),
        "standard_error": float(se[jump_index]),
        "n_left": float(((running < 0) & inside).sum()),
        "n_right": float(((running >= 0) & inside).sum()),
        "effective_n": float(inside.sum()),
    }


def global_polynomial_rd(df: pd.DataFrame, order: int) -> dict[str, float]:
    running = df["vote_margin"].to_numpy(dtype=float)
    y = df["next_vote_share"].to_numpy(dtype=float)
    weights = np.ones_like(running)
    x, names = rd_design_matrix(running, order)
    beta, se = weighted_ls(y, x, weights)
    jump_index = names.index("cutoff_jump")
    return {
        "specification": f"global polynomial order {order}",
        "estimate": float(beta[jump_index]),
        "standard_error": float(se[jump_index]),
        "warning": "Uses all observations; included only to show why global polynomial RD can be unstable.",
    }


def density_diagnostics(df: pd.DataFrame, outdir: Path) -> None:
    bins = np.arange(-0.16, 0.165, 0.02)
    labels = []
    rows = []
    for left, right in zip(bins[:-1], bins[1:]):
        count = int(((df["vote_margin"] >= left) & (df["vote_margin"] < right)).sum())
        rows.append(
            {
                "bin_left": round(float(left), 4),
                "bin_right": round(float(right), 4),
                "count": count,
            }
        )
        labels.append((left + right) / 2)
    pd.DataFrame(rows).to_csv(outdir / "density_bins_near_cutoff.csv", index=False)

    left_count = int(((df["vote_margin"] >= -0.04) & (df["vote_margin"] < 0)).sum())
    right_count = int(((df["vote_margin"] >= 0) & (df["vote_margin"] <= 0.04)).sum())
    total = left_count + right_count
    expected = total / 2
    z_score = (right_count - expected) / np.sqrt(max(total * 0.25, 1.0))
    pd.DataFrame(
        [
            {
                "window": "[-0.04, 0.04]",
                "left_count": left_count,
                "right_count": right_count,
                "right_share": right_count / max(total, 1),
                "binomial_balance_z_score": z_score,
                "interpretation": "Teaching density check; large absolute values would warn about sorting around the cutoff.",
            }
        ]
    ).to_csv(outdir / "density_check.csv", index=False)


def make_rd_plot(df: pd.DataFrame, outdir: Path) -> None:
    bins = np.arange(-0.30, 0.305, 0.015)
    rows = []
    for left, right in zip(bins[:-1], bins[1:]):
        sub = df[(df["vote_margin"] >= left) & (df["vote_margin"] < right)]
        if len(sub) == 0:
            continue
        rows.append(
            {
                "bin_center": float((left + right) / 2),
                "mean_next_vote_share": float(sub["next_vote_share"].mean()),
                "observations": int(len(sub)),
            }
        )
    plot_df = pd.DataFrame(rows)
    plot_df.to_csv(outdir / "rd_plot_bins.csv", index=False)

    plt.figure(figsize=(7.2, 4.4))
    plt.scatter(
        plot_df["bin_center"],
        plot_df["mean_next_vote_share"],
        s=np.maximum(plot_df["observations"] / 7, 8),
        color="#4C78A8",
        alpha=0.78,
        edgecolor="white",
        linewidth=0.4,
    )
    for side, color in [("left", "#F58518"), ("right", "#54A24B")]:
        if side == "left":
            sub = df[(df["vote_margin"] >= -0.12) & (df["vote_margin"] < 0)]
            grid = np.linspace(-0.12, 0, 60)
        else:
            sub = df[(df["vote_margin"] >= 0) & (df["vote_margin"] <= 0.12)]
            grid = np.linspace(0, 0.12, 60)
        x = np.column_stack([np.ones(len(sub)), sub["vote_margin"].to_numpy(dtype=float)])
        beta, *_ = np.linalg.lstsq(x, sub["next_vote_share"].to_numpy(dtype=float), rcond=None)
        plt.plot(grid, beta[0] + beta[1] * grid, color=color, linewidth=2.2)
    plt.axvline(0, color="black", linewidth=1.0)
    plt.xlabel("Vote margin, centered at winning cutoff")
    plt.ylabel("Next election vote share")
    plt.tight_layout()
    plt.savefig(outdir / "close_election_rd_plot.png", dpi=160)
    plt.close()


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    bandwidths = [0.04, 0.06, 0.08, 0.10, 0.12]
    rows = []
    for bandwidth in bandwidths:
        rows.append(local_rd(df, "next_vote_share", bandwidth, order=1, kernel="triangular"))
        rows.append(local_rd(df, "next_vote_share", bandwidth, order=1, kernel="uniform"))
    pd.DataFrame(rows).to_csv(outdir / "bandwidth_kernel_sensitivity.csv", index=False)

    covariates = ["pre_turnout", "party_strength", "district_income"]
    cov_rows = [
        local_rd(df, covariate, 0.08, order=1, kernel="triangular")
        for covariate in covariates
    ]
    pd.DataFrame(cov_rows).to_csv(outdir / "covariate_continuity.csv", index=False)

    baseline = local_rd(df, "next_vote_share", 0.08, order=1, kernel="triangular")
    cov_adjusted = local_rd(
        df,
        "next_vote_share",
        0.08,
        order=1,
        kernel="triangular",
        covariates=covariates,
    )
    local_quadratic = local_rd(df, "next_vote_share", 0.08, order=2, kernel="triangular")
    bias_proxy = float(baseline["estimate"]) - float(local_quadratic["estimate"])
    rbc_style_estimate = float(baseline["estimate"]) - bias_proxy
    smoothness_bound = 1.50
    honest_bias_bound = 0.5 * smoothness_bound * (float(baseline["bandwidth"]) ** 2)
    honest_lower = float(baseline["estimate"]) - 1.96 * float(baseline["standard_error"]) - honest_bias_bound
    honest_upper = float(baseline["estimate"]) + 1.96 * float(baseline["standard_error"]) + honest_bias_bound

    summary = pd.DataFrame(
        [
            {
                "object": "local linear triangular RD",
                "estimate": float(baseline["estimate"]),
                "standard_error": float(baseline["standard_error"]),
                "bandwidth": float(baseline["bandwidth"]),
                "notes": "Primary teaching estimate: local linear, triangular weights, centered vote margin.",
            },
            {
                "object": "covariate-adjusted local linear RD",
                "estimate": float(cov_adjusted["estimate"]),
                "standard_error": float(cov_adjusted["standard_error"]),
                "bandwidth": float(cov_adjusted["bandwidth"]),
                "notes": "Predetermined covariates included for precision; identification still comes from cutoff continuity.",
            },
            {
                "object": "local quadratic bias diagnostic",
                "estimate": float(local_quadratic["estimate"]),
                "standard_error": float(local_quadratic["standard_error"]),
                "bandwidth": float(local_quadratic["bandwidth"]),
                "notes": "Teaching diagnostic for curvature sensitivity, not a replacement for production rdrobust.",
            },
            {
                "object": "robust-bias-correction-style estimate",
                "estimate": rbc_style_estimate,
                "standard_error": float(local_quadratic["standard_error"]),
                "bandwidth": float(baseline["bandwidth"]),
                "notes": "Pedagogical bias correction using local quadratic difference as a bias proxy.",
            },
            {
                "object": "honest-interval lower bound",
                "estimate": honest_lower,
                "standard_error": np.nan,
                "bandwidth": float(baseline["bandwidth"]),
                "notes": f"Uses smoothness_bound={smoothness_bound} and adds worst-case bias to the 95 percent interval.",
            },
            {
                "object": "honest-interval upper bound",
                "estimate": honest_upper,
                "standard_error": np.nan,
                "bandwidth": float(baseline["bandwidth"]),
                "notes": f"Uses smoothness_bound={smoothness_bound} and adds worst-case bias to the 95 percent interval.",
            },
            {
                "object": "synthetic true cutoff effect",
                "estimate": float(df.loc[np.abs(df["vote_margin"]) <= 0.01, "synthetic_true_effect"].mean()),
                "standard_error": np.nan,
                "bandwidth": 0.01,
                "notes": "Known only because the dataset is synthetic.",
            },
        ]
    )
    summary.to_csv(outdir / "rd_estimates.csv", index=False)

    pd.DataFrame([global_polynomial_rd(df, 1), global_polynomial_rd(df, 4)]).to_csv(
        outdir / "global_polynomial_pitfall.csv",
        index=False,
    )

    density_diagnostics(df, outdir)
    make_rd_plot(df, outdir)

    prompts = pd.DataFrame(
        [
            {
                "prompt": "What is the running variable and why is the cutoff meaningful?",
                "student_note": "Use vote_margin and the zero winning threshold.",
            },
            {
                "prompt": "How does the estimate change across bandwidths and kernels?",
                "student_note": "Use bandwidth_kernel_sensitivity.csv.",
            },
            {
                "prompt": "Are predetermined covariates continuous at the threshold?",
                "student_note": "Use covariate_continuity.csv.",
            },
            {
                "prompt": "What does the density check say about sorting near zero?",
                "student_note": "Use density_check.csv and density_bins_near_cutoff.csv.",
            },
            {
                "prompt": "Why is the global fourth-order polynomial not the preferred design?",
                "student_note": "Use global_polynomial_pitfall.csv and explain boundary leverage.",
            },
            {
                "prompt": "How would production rdrobust or rdhonest output differ from this teaching analogue?",
                "student_note": "Name bias correction, variance adjustment, and explicit smoothness assumptions.",
            },
        ]
    )
    prompts.to_csv(outdir / "design_prompts.csv", index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)
    analyze(df, args.outdir)
    print(f"Wrote RD diagnostics to {args.outdir}")


if __name__ == "__main__":
    main()
