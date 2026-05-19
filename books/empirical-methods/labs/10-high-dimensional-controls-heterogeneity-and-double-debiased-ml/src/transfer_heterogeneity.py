"""Run the Week 10 heterogeneity transfer path on synthetic youth-program data."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTCOME = "summer_employed"
TREATMENT = "program_offer"


def add_intercept(x: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones(x.shape[0]), x])


def ols_fit(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.linalg.pinv(x.T @ x) @ x.T @ y


def robust_se(x: np.ndarray, residuals: np.ndarray, index: int) -> float:
    bread = np.linalg.pinv(x.T @ x)
    meat = x.T @ (x * residuals.reshape(-1, 1) ** 2)
    variance = bread @ meat @ bread
    return float(np.sqrt(max(variance[index, index], 0.0)))


def controls(df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
    numeric = pd.DataFrame(index=df.index)
    numeric["baseline_risk"] = df["baseline_risk"].astype(float)
    numeric["prior_work_months"] = df["prior_work_months"].astype(float)
    numeric["school_enrolled"] = df["school_enrolled"].astype(float)
    numeric["age"] = df["age"].astype(float)
    numeric["neighborhood_unemployment"] = df["neighborhood_unemployment"].astype(float)
    parts = [numeric.to_numpy(dtype=float)]
    names = list(numeric.columns)
    for neighborhood in sorted(df["neighborhood"].unique().tolist()):
        parts.append((df["neighborhood"] == neighborhood).to_numpy(dtype=float).reshape(-1, 1))
        names.append(f"neighborhood:{neighborhood}")
    x = np.column_stack(parts)
    means = x.mean(axis=0)
    scales = x.std(axis=0)
    scales[scales < 1e-8] = 1.0
    return (x - means) / scales, names


def treatment_effect(df: pd.DataFrame) -> tuple[float, float]:
    if df[TREATMENT].nunique() < 2 or len(df) < 20:
        return float("nan"), float("nan")
    x_controls, _ = controls(df)
    y = df[OUTCOME].to_numpy(dtype=float)
    d = df[TREATMENT].to_numpy(dtype=float)
    x = add_intercept(np.column_stack([d, x_controls]))
    beta = ols_fit(x, y)
    residuals = y - x @ beta
    return float(beta[1]), robust_se(x, residuals, 1)


def interaction_benchmark(df: pd.DataFrame, outdir: Path) -> pd.DataFrame:
    x_controls, names = controls(df)
    y = df[OUTCOME].to_numpy(dtype=float)
    d = df[TREATMENT].to_numpy(dtype=float)
    risk = df["baseline_risk"].to_numpy(dtype=float)
    x = add_intercept(np.column_stack([d, d * risk, x_controls]))
    beta = ols_fit(x, y)
    residuals = y - x @ beta
    se_d = robust_se(x, residuals, 1)
    se_interaction = robust_se(x, residuals, 2)
    rows = [
        {
            "term": "program_offer",
            "coefficient": float(beta[1]),
            "robust_se": se_d,
            "interpretation": "Estimated treatment effect when baseline risk is zero in the linear interaction benchmark.",
        },
        {
            "term": "program_offer_x_baseline_risk",
            "coefficient": float(beta[2]),
            "robust_se": se_interaction,
            "interpretation": "How the treatment effect changes with baseline risk.",
        },
    ]
    for q in [0.20, 0.50, 0.80]:
        risk_value = float(np.quantile(risk, q))
        rows.append(
            {
                "term": f"implied_cate_at_risk_p{int(q * 100)}",
                "coefficient": float(beta[1] + beta[2] * risk_value),
                "robust_se": float("nan"),
                "interpretation": f"Linear-interaction implied CATE at baseline-risk quantile {q:.2f}.",
            }
        )
    out = pd.DataFrame(rows)
    out.to_csv(outdir / "interaction_benchmark.csv", index=False)
    del names
    return out


def cate_by_risk(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["risk_group"] = pd.qcut(out["baseline_risk"], q=3, labels=["low", "middle", "high"])
    rows = []
    for risk_group, group in out.groupby("risk_group", observed=False):
        theta, se = treatment_effect(group)
        treated = int(group[TREATMENT].sum())
        untreated = int(len(group) - treated)
        rows.append(
            {
                "risk_group": str(risk_group),
                "n": int(len(group)),
                "treated": treated,
                "untreated": untreated,
                "mean_baseline_risk": float(group["baseline_risk"].mean()),
                "adjusted_cate": theta,
                "robust_se": se,
                "mean_true_cate_in_synthetic_data": float(group["true_cate"].mean()),
            }
        )
    return pd.DataFrame(rows)


def split_discovery_evaluation(df: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(10301)
    out = df.copy()
    order = rng.permutation(len(out))
    split = np.array(["evaluation"] * len(out), dtype=object)
    split[order[: len(out) // 2]] = "discovery"
    out["honesty_split"] = split
    return out


def split_score(data: pd.DataFrame, variable: str, threshold: float) -> dict[str, object] | None:
    left = data[data[variable] <= threshold]
    right = data[data[variable] > threshold]
    if min(len(left), len(right)) < 45:
        return None
    if min(left[TREATMENT].sum(), len(left) - left[TREATMENT].sum(), right[TREATMENT].sum(), len(right) - right[TREATMENT].sum()) < 10:
        return None
    left_effect, _ = treatment_effect(left)
    right_effect, _ = treatment_effect(right)
    if np.isnan(left_effect) or np.isnan(right_effect):
        return None
    return {
        "split_variable": variable,
        "threshold": float(threshold),
        "left_effect_discovery": left_effect,
        "right_effect_discovery": right_effect,
        "absolute_effect_gap": float(abs(left_effect - right_effect)),
    }


def honest_tree(df: pd.DataFrame, outdir: Path) -> pd.DataFrame:
    split_df = split_discovery_evaluation(df)
    discovery = split_df[split_df["honesty_split"] == "discovery"].copy()
    evaluation = split_df[split_df["honesty_split"] == "evaluation"].copy()
    candidates: list[dict[str, object]] = []
    for variable in ["baseline_risk", "prior_work_months", "neighborhood_unemployment", "age"]:
        for threshold in np.quantile(discovery[variable], [0.33, 0.50, 0.67]):
            scored = split_score(discovery, variable, float(threshold))
            if scored is not None:
                candidates.append(scored)
    if not candidates:
        raise RuntimeError("No feasible honest-tree split found.")
    best = sorted(candidates, key=lambda row: float(row["absolute_effect_gap"]), reverse=True)[0]
    variable = str(best["split_variable"])
    threshold = float(best["threshold"])
    rows: list[dict[str, object]] = []
    for sample_name, sample in [("discovery", discovery), ("evaluation", evaluation)]:
        for leaf_name, leaf in [
            ("left", sample[sample[variable] <= threshold]),
            ("right", sample[sample[variable] > threshold]),
        ]:
            theta, se = treatment_effect(leaf)
            rows.append(
                {
                    "sample": sample_name,
                    "split_variable": variable,
                    "threshold": threshold,
                    "leaf": leaf_name,
                    "n": int(len(leaf)),
                    "treated": int(leaf[TREATMENT].sum()),
                    "untreated": int(len(leaf) - leaf[TREATMENT].sum()),
                    "effect": theta,
                    "robust_se": se,
                    "mean_true_cate_in_synthetic_data": float(leaf["true_cate"].mean()),
                }
            )
    out = pd.DataFrame(rows)
    out.to_csv(outdir / "honest_tree_effects.csv", index=False)
    validation = pd.DataFrame(candidates).sort_values("absolute_effect_gap", ascending=False)
    validation.to_csv(outdir / "honest_tree_candidate_splits.csv", index=False)
    return out


def write_cate_plot(cate: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    positions = np.arange(len(cate))
    ax.errorbar(
        positions,
        cate["adjusted_cate"],
        yerr=1.96 * cate["robust_se"].fillna(0.0),
        fmt="o",
        color="#2b6cb0",
        ecolor="#5a7fb8",
        capsize=4,
        label="adjusted CATE",
    )
    ax.plot(positions, cate["mean_true_cate_in_synthetic_data"], "s", color="#7a7a7a", label="synthetic truth")
    ax.axhline(0.0, color="0.35", linewidth=1.0, linestyle="--")
    ax.set_xticks(positions)
    ax.set_xticklabels(cate["risk_group"].tolist())
    ax.set_xlabel("Baseline-risk group")
    ax.set_ylabel("Effect on summer employment")
    ax.set_title("Heterogeneity by baseline risk")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def overlap_by_risk(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["risk_group"] = pd.qcut(out["baseline_risk"], q=3, labels=["low", "middle", "high"])
    rows = []
    for risk_group, group in out.groupby("risk_group", observed=False):
        rows.append(
            {
                "risk_group": str(risk_group),
                "n": int(len(group)),
                "treated_share": float(group[TREATMENT].mean()),
                "offer_probability_p10": float(np.quantile(group["offer_probability_true"], 0.10)),
                "offer_probability_p50": float(np.quantile(group["offer_probability_true"], 0.50)),
                "offer_probability_p90": float(np.quantile(group["offer_probability_true"], 0.90)),
            }
        )
    return pd.DataFrame(rows)


def validation_summary(tree_effects: pd.DataFrame) -> pd.DataFrame:
    discovery = tree_effects[tree_effects["sample"] == "discovery"].set_index("leaf")
    evaluation = tree_effects[tree_effects["sample"] == "evaluation"].set_index("leaf")
    rows = []
    for leaf in ["left", "right"]:
        rows.append(
            {
                "leaf": leaf,
                "discovery_effect": float(discovery.loc[leaf, "effect"]),
                "evaluation_effect": float(evaluation.loc[leaf, "effect"]),
                "same_sign": bool(np.sign(discovery.loc[leaf, "effect"]) == np.sign(evaluation.loc[leaf, "effect"])),
                "absolute_change": float(abs(discovery.loc[leaf, "effect"] - evaluation.loc[leaf, "effect"])),
            }
        )
    rows.append(
        {
            "leaf": "gap_between_leaves",
            "discovery_effect": float(discovery.loc["right", "effect"] - discovery.loc["left", "effect"]),
            "evaluation_effect": float(evaluation.loc["right", "effect"] - evaluation.loc["left", "effect"]),
            "same_sign": bool(
                np.sign(discovery.loc["right", "effect"] - discovery.loc["left", "effect"])
                == np.sign(evaluation.loc["right", "effect"] - evaluation.loc["left", "effect"])
            ),
            "absolute_change": float(
                abs(
                    (discovery.loc["right", "effect"] - discovery.loc["left", "effect"])
                    - (evaluation.loc["right", "effect"] - evaluation.loc["left", "effect"])
                )
            ),
        }
    )
    return pd.DataFrame(rows)


def run(input_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(input_path)
    interaction_benchmark(df, outdir)
    cate = cate_by_risk(df)
    cate.to_csv(outdir / "cate_by_risk.csv", index=False)
    write_cate_plot(cate, outdir / "cate_by_risk.png")
    tree_effects = honest_tree(df, outdir)
    validation_summary(tree_effects).to_csv(outdir / "heterogeneity_validation.csv", index=False)
    overlap_by_risk(df).to_csv(outdir / "overlap_by_risk.csv", index=False)
    prompts = pd.DataFrame(
        [
            {
                "step": "transfer",
                "prompt": "Compare risk-group CATEs with the simple interaction benchmark.",
            },
            {
                "step": "diagnose",
                "prompt": "Use overlap by risk group and honest-tree validation to decide whether heterogeneity is stable.",
            },
            {
                "step": "interpret",
                "prompt": "Explain why the forest or tree split is not itself a causal mechanism.",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)
    print(f"Wrote heterogeneity outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.input, args.outdir)


if __name__ == "__main__":
    main()
