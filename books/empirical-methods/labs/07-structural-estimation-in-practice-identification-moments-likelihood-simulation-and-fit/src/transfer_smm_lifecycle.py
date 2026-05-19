"""Run the Week 7 simulated-moments transfer workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week7_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week7_cache"),
)
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)
Path(os.environ["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


EPS = 1e-8


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35.0, 35.0)))


def fit_wage_equation(df: pd.DataFrame) -> np.ndarray:
    workers = df[(df["work"] == 1) & df["observed_wage"].notna()].copy()
    y = np.log(np.maximum(workers["observed_wage"].to_numpy(dtype=float), 1.0))
    x = np.column_stack(
        [
            np.ones(len(workers)),
            workers["schooling_years"].to_numpy(dtype=float),
            workers["experience_years"].to_numpy(dtype=float),
        ]
    )
    return np.linalg.pinv(x.T @ x) @ x.T @ y


def predict_wage(schooling: np.ndarray, experience: np.ndarray, wage_beta: np.ndarray) -> np.ndarray:
    x = np.column_stack([np.ones(len(schooling)), schooling, experience])
    return np.exp(x @ wage_beta)


def data_moments(df: pd.DataFrame) -> dict[str, float]:
    moments: dict[str, float] = {}
    for period, sub in df.groupby("period"):
        moments[f"school_rate_period_{int(period)}"] = float(sub["choose_school"].mean())
    last_period = int(df["period"].max())
    final = df[df["period"] == last_period]
    moments["final_mean_schooling_years"] = float(final["schooling_years"].mean())
    moments["final_mean_experience_years"] = float(final["experience_years"].mean())
    moments["final_mean_observed_wage_workers"] = float(final["observed_wage"].mean())
    return moments


def simulate_path(
    initial: pd.DataFrame,
    tuition_by_period: pd.Series,
    wage_beta: np.ndarray,
    tuition_coef: float,
    wage_coef: float,
    draws: np.ndarray,
    tuition_shift: float = 0.0,
    scenario: str = "baseline",
) -> tuple[dict[str, float], pd.DataFrame]:
    schooling = initial["schooling_years"].to_numpy(dtype=float).copy()
    experience = initial["experience_years"].to_numpy(dtype=float).copy()
    rows: list[dict[str, float | int | str]] = []
    moments: dict[str, float] = {}
    n_periods = draws.shape[1]
    for period in range(n_periods):
        tuition = max(0.0, float(tuition_by_period.loc[period]) + tuition_shift)
        wage_offer = predict_wage(schooling, experience, wage_beta)
        school_index = (
            0.85
            - 0.31 * (schooling - 12.0)
            - 0.18 * experience
            + tuition_coef * (tuition / 1_000.0)
            + wage_coef * (np.log(np.maximum(wage_offer, 1.0)) - np.log(35_000.0))
            + 0.20 * float(period <= 2)
        )
        school_prob = np.asarray(sigmoid(school_index))
        school_prob = np.where(schooling >= 16.0, 0.0, school_prob)
        choose_school = draws[:, period] < school_prob
        work = ~choose_school
        moments[f"school_rate_period_{period}"] = float(choose_school.mean())
        rows.append(
            {
                "scenario": scenario,
                "period": period,
                "mean_tuition": tuition,
                "school_rate": float(choose_school.mean()),
                "work_rate": float(work.mean()),
                "mean_school_probability": float(school_prob.mean()),
                "mean_schooling_years": float(schooling.mean()),
                "mean_experience_years": float(experience.mean()),
                "mean_predicted_wage_offer": float(wage_offer.mean()),
            }
        )
        schooling = schooling + choose_school.astype(float)
        experience = experience + work.astype(float)
    final_wage = predict_wage(schooling, experience, wage_beta)
    moments["final_mean_schooling_years"] = float(schooling.mean())
    moments["final_mean_experience_years"] = float(experience.mean())
    moments["final_mean_observed_wage_workers"] = float(final_wage.mean())
    return moments, pd.DataFrame(rows)


def scaled_gap(name: str, data_value: float, model_value: float) -> float:
    if "wage" in name:
        return (data_value - model_value) / 10_000.0
    if "schooling" in name or "experience" in name:
        return (data_value - model_value) / 2.0
    return data_value - model_value


def estimate_smm(df: pd.DataFrame) -> tuple[dict[str, float], pd.DataFrame, pd.DataFrame]:
    wage_beta = fit_wage_equation(df)
    initial = df[df["period"] == 0].sort_values("person_id").reset_index(drop=True)
    tuition_by_period = df.groupby("period")["tuition"].mean()
    n_periods = int(df["period"].max()) + 1
    rng = np.random.default_rng(6727)
    draws = rng.random((len(initial), n_periods))
    data = data_moments(df)

    best: dict[str, float] | None = None
    best_moments: dict[str, float] | None = None
    criterion_rows: list[dict[str, float]] = []
    for tuition_coef in np.linspace(-0.34, -0.06, 15):
        for wage_coef in np.linspace(-0.95, -0.15, 17):
            model, _ = simulate_path(
                initial,
                tuition_by_period,
                wage_beta,
                float(tuition_coef),
                float(wage_coef),
                draws,
            )
            criterion = 0.0
            for name, data_value in data.items():
                criterion += scaled_gap(name, data_value, model[name]) ** 2
            criterion_rows.append(
                {
                    "tuition_coef": float(tuition_coef),
                    "wage_opportunity_coef": float(wage_coef),
                    "criterion": float(criterion),
                }
            )
            if best is None or criterion < best["criterion"]:
                best = {
                    "tuition_coef": float(tuition_coef),
                    "wage_opportunity_coef": float(wage_coef),
                    "criterion": float(criterion),
                }
                best_moments = model
    assert best is not None
    assert best_moments is not None

    _, baseline_path = simulate_path(
        initial,
        tuition_by_period,
        wage_beta,
        best["tuition_coef"],
        best["wage_opportunity_coef"],
        draws,
        scenario="baseline",
    )
    _, subsidy_path = simulate_path(
        initial,
        tuition_by_period,
        wage_beta,
        best["tuition_coef"],
        best["wage_opportunity_coef"],
        draws,
        tuition_shift=-2_000.0,
        scenario="tuition subsidy",
    )

    fit_rows = []
    for name, data_value in data.items():
        fit_rows.append(
            {
                "moment": name,
                "data_value": data_value,
                "model_value": best_moments[name],
                "gap": data_value - best_moments[name],
                "scaled_gap": scaled_gap(name, data_value, best_moments[name]),
            }
        )
    return best, pd.DataFrame(fit_rows), pd.concat([baseline_path, subsidy_path], ignore_index=True)


def make_plot(paths: pd.DataFrame, outdir: Path) -> None:
    plt.figure(figsize=(7.4, 4.4))
    for scenario, sub in paths.groupby("scenario"):
        plt.plot(
            sub["period"],
            sub["mean_schooling_years"],
            marker="o",
            linewidth=2.0,
            label=scenario,
        )
    plt.xlabel("Period")
    plt.ylabel("Mean schooling years before decision")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(outdir / "schooling_counterfactual_paths.png", dpi=160)
    plt.close()


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    estimate, fit, paths = estimate_smm(df)
    pd.DataFrame(
        [
            {
                "estimator": "simulated method of moments",
                "tuition_coef": estimate["tuition_coef"],
                "wage_opportunity_coef": estimate["wage_opportunity_coef"],
                "criterion": estimate["criterion"],
                "interpretation": "Reduced teaching SMM model matching schooling rates and final lifecycle moments.",
            }
        ]
    ).to_csv(outdir / "smm_estimates.csv", index=False)
    fit.to_csv(outdir / "smm_moment_fit.csv", index=False)
    paths.to_csv(outdir / "policy_transfer_counterfactual.csv", index=False)
    final = paths[paths["period"] == paths["period"].max()]
    baseline = final[final["scenario"] == "baseline"].iloc[0]
    subsidy = final[final["scenario"] == "tuition subsidy"].iloc[0]
    pd.DataFrame(
        [
            {
                "object": "final mean schooling years",
                "baseline": float(baseline["mean_schooling_years"]),
                "tuition_subsidy": float(subsidy["mean_schooling_years"]),
                "difference": float(subsidy["mean_schooling_years"] - baseline["mean_schooling_years"]),
            },
            {
                "object": "final mean experience years",
                "baseline": float(baseline["mean_experience_years"]),
                "tuition_subsidy": float(subsidy["mean_experience_years"]),
                "difference": float(subsidy["mean_experience_years"] - baseline["mean_experience_years"]),
            },
            {
                "object": "final mean predicted wage offer",
                "baseline": float(baseline["mean_predicted_wage_offer"]),
                "tuition_subsidy": float(subsidy["mean_predicted_wage_offer"]),
                "difference": float(
                    subsidy["mean_predicted_wage_offer"] - baseline["mean_predicted_wage_offer"]
                ),
            },
        ]
    ).to_csv(outdir / "policy_transfer_summary.csv", index=False)
    make_plot(paths, outdir)
    pd.DataFrame(
        [
            {
                "prompt": "What is the transfer anchor?",
                "guidance": "A reduced lifecycle schooling/work model inspired by dynamic structural applications, not an official replication.",
            },
            {
                "prompt": "Which moments discipline tuition sensitivity?",
                "guidance": "Schooling rates over time and final schooling are the main targeted moments.",
            },
            {
                "prompt": "What remains assumed?",
                "guidance": "Expectations, ability, borrowing constraints, fertility, occupation choice, and equilibrium wages are simplified.",
            },
            {
                "prompt": "What would validation require?",
                "guidance": "Policy variation or holdout moments that move tuition and opportunity costs outside the estimation targets.",
            },
        ]
    ).to_csv(outdir / "transfer_design_prompts.csv", index=False)
    print(f"Wrote SMM transfer outputs to {outdir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()
    analyze(pd.read_csv(args.input), args.outdir)


if __name__ == "__main__":
    main()
