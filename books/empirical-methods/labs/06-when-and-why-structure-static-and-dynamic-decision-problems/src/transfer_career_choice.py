"""Run the Week 6 career-choice transfer workflow."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week6_matplotlib"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "empirical_methods_week6_cache"),
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


def feature_matrix(df: pd.DataFrame, tuition: pd.Series | np.ndarray | None = None) -> tuple[np.ndarray, list[str]]:
    tuition_values = df["tuition"].to_numpy(dtype=float) if tuition is None else np.asarray(tuition, dtype=float)
    wage_offer = np.maximum(df["wage_offer"].to_numpy(dtype=float), 1.0)
    columns = [
        np.ones(len(df)),
        df["schooling_years"].to_numpy(dtype=float) - 12.0,
        df["experience_years"].to_numpy(dtype=float),
        tuition_values / 1_000.0,
        np.log(wage_offer) - np.log(35_000.0),
        (df["period"].to_numpy(dtype=float) <= 2).astype(float),
    ]
    names = [
        "intercept",
        "schooling_years_minus_12",
        "experience_years",
        "tuition_thousands",
        "log_wage_offer_relative",
        "early_period",
    ]
    return np.column_stack(columns), names


def fit_logit_irls(x: np.ndarray, y: np.ndarray, ridge: float = 1e-4, max_iter: int = 80) -> np.ndarray:
    beta = np.zeros(x.shape[1])
    penalty = np.eye(x.shape[1]) * ridge
    penalty[0, 0] = 0.0
    for _ in range(max_iter):
        eta = x @ beta
        p = np.clip(sigmoid(eta), EPS, 1.0 - EPS)
        weights = np.maximum(p * (1.0 - p), 1e-5)
        z = eta + (y - p) / weights
        xw = x * weights[:, None]
        beta_new = np.linalg.pinv(x.T @ xw + penalty) @ (x.T @ (weights * z))
        if np.max(np.abs(beta_new - beta)) < 1e-8:
            beta = beta_new
            break
        beta = beta_new
    return beta


def fit_wage_equation(df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
    work = df[(df["work"] == 1) & (df["observed_wage"].notna())].copy()
    y = np.log(np.maximum(work["observed_wage"].to_numpy(dtype=float), 1.0))
    x = np.column_stack(
        [
            np.ones(len(work)),
            work["schooling_years"].to_numpy(dtype=float),
            work["experience_years"].to_numpy(dtype=float),
        ]
    )
    beta = np.linalg.pinv(x.T @ x) @ x.T @ y
    return beta, ["wage_intercept", "schooling_years", "experience_years"]


def write_moments(df: pd.DataFrame, outdir: Path) -> None:
    rows = []
    for period, sub in df.groupby("period"):
        rows.append(
            {
                "period": int(period),
                "observations": int(len(sub)),
                "school_rate": float(sub["choose_school"].mean()),
                "work_rate": float(sub["work"].mean()),
                "mean_schooling_years": float(sub["schooling_years"].mean()),
                "mean_experience_years": float(sub["experience_years"].mean()),
                "mean_tuition": float(sub["tuition"].mean()),
                "mean_wage_offer": float(sub["wage_offer"].mean()),
                "mean_observed_wage_for_workers": float(sub["observed_wage"].mean()),
            }
        )
    pd.DataFrame(rows).to_csv(outdir / "career_choice_moments.csv", index=False)

    transition_rows = []
    for action, sub in df.groupby("choose_school"):
        transition_rows.append(
            {
                "choose_school": int(action),
                "observations": int(len(sub)),
                "mean_schooling_state": float(sub["schooling_years"].mean()),
                "mean_experience_state": float(sub["experience_years"].mean()),
                "mean_wage_offer": float(sub["wage_offer"].mean()),
                "mean_tuition": float(sub["tuition"].mean()),
            }
        )
    pd.DataFrame(transition_rows).to_csv(outdir / "career_transition_moments.csv", index=False)


def predict_wage_offer(schooling: np.ndarray, experience: np.ndarray, wage_beta: np.ndarray) -> np.ndarray:
    x = np.column_stack([np.ones(len(schooling)), schooling, experience])
    return np.exp(x @ wage_beta)


def simulate_policy(
    initial: pd.DataFrame,
    tuition_by_period: pd.Series,
    choice_beta: np.ndarray,
    wage_beta: np.ndarray,
    scenario: str,
    tuition_shift: float,
    draws: np.ndarray,
) -> pd.DataFrame:
    schooling = initial["schooling_years"].to_numpy(dtype=float).copy()
    experience = initial["experience_years"].to_numpy(dtype=float).copy()
    n_people, n_periods = draws.shape
    rows: list[dict[str, float | str | int]] = []

    for period in range(n_periods):
        tuition = max(0.0, float(tuition_by_period.loc[period]) + tuition_shift)
        wage_offer = predict_wage_offer(schooling, experience, wage_beta)
        temp = pd.DataFrame(
            {
                "period": period,
                "schooling_years": schooling,
                "experience_years": experience,
                "tuition": tuition,
                "wage_offer": wage_offer,
            }
        )
        x, _ = feature_matrix(temp)
        school_prob = np.asarray(sigmoid(x @ choice_beta))
        school_prob = np.where(schooling >= 16.0, 0.0, school_prob)
        choose_school = draws[:, period] < school_prob
        work = ~choose_school

        rows.append(
            {
                "scenario": scenario,
                "period": period,
                "mean_tuition": tuition,
                "school_rate": float(choose_school.mean()),
                "work_rate": float(work.mean()),
                "mean_schooling_years": float(schooling.mean()),
                "mean_experience_years": float(experience.mean()),
                "mean_predicted_wage_offer": float(wage_offer.mean()),
                "mean_school_probability": float(school_prob.mean()),
            }
        )

        schooling = schooling + choose_school.astype(float)
        experience = experience + work.astype(float)

    return pd.DataFrame(rows)


def make_plot(counterfactual: pd.DataFrame, outdir: Path) -> None:
    plt.figure(figsize=(7.2, 4.4))
    for scenario, sub in counterfactual.groupby("scenario"):
        plt.plot(
            sub["period"],
            sub["mean_schooling_years"],
            marker="o",
            linewidth=2.0,
            label=scenario,
        )
    plt.xlabel("Period")
    plt.ylabel("Mean schooling state before decision")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(outdir / "career_counterfactual_paths.png", dpi=160)
    plt.close()


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    write_moments(df, outdir)

    x, feature_names = feature_matrix(df)
    y = df["choose_school"].to_numpy(dtype=float)
    choice_beta = fit_logit_irls(x, y)
    probs = np.clip(sigmoid(x @ choice_beta), EPS, 1.0 - EPS)
    choice_neg_ll = float(-np.sum(y * np.log(probs) + (1.0 - y) * np.log(1.0 - probs)))

    wage_beta, wage_names = fit_wage_equation(df)
    rows = []
    for name, coef in zip(feature_names, choice_beta):
        rows.append(
            {
                "model": "school-choice logit",
                "parameter": name,
                "estimate": float(coef),
                "fit_statistic": choice_neg_ll,
                "interpretation": "Reduced teaching choice model used for transfer counterfactual.",
            }
        )
    for name, coef in zip(wage_names, wage_beta):
        rows.append(
            {
                "model": "log wage equation",
                "parameter": name,
                "estimate": float(coef),
                "fit_statistic": np.nan,
                "interpretation": "Wage-offer mapping used to update simulated career states.",
            }
        )
    pd.DataFrame(rows).to_csv(outdir / "career_choice_model.csv", index=False)

    initial = df[df["period"] == 0].sort_values("person_id").reset_index(drop=True)
    tuition_by_period = df.groupby("period")["tuition"].mean()
    rng = np.random.default_rng(6626)
    draws = rng.random((len(initial), int(df["period"].max()) + 1))

    baseline = simulate_policy(
        initial,
        tuition_by_period,
        choice_beta,
        wage_beta,
        "baseline",
        0.0,
        draws,
    )
    subsidy = simulate_policy(
        initial,
        tuition_by_period,
        choice_beta,
        wage_beta,
        "tuition subsidy",
        -2_000.0,
        draws,
    )
    counterfactual = pd.concat([baseline, subsidy], ignore_index=True)
    counterfactual.to_csv(outdir / "tuition_subsidy_counterfactual.csv", index=False)

    final = counterfactual[counterfactual["period"] == counterfactual["period"].max()]
    baseline_final = final[final["scenario"] == "baseline"].iloc[0]
    subsidy_final = final[final["scenario"] == "tuition subsidy"].iloc[0]
    pd.DataFrame(
        [
            {
                "object": "final mean schooling years",
                "baseline": float(baseline_final["mean_schooling_years"]),
                "tuition_subsidy": float(subsidy_final["mean_schooling_years"]),
                "difference": float(
                    subsidy_final["mean_schooling_years"] - baseline_final["mean_schooling_years"]
                ),
            },
            {
                "object": "final mean experience years",
                "baseline": float(baseline_final["mean_experience_years"]),
                "tuition_subsidy": float(subsidy_final["mean_experience_years"]),
                "difference": float(
                    subsidy_final["mean_experience_years"] - baseline_final["mean_experience_years"]
                ),
            },
            {
                "object": "final mean predicted wage offer",
                "baseline": float(baseline_final["mean_predicted_wage_offer"]),
                "tuition_subsidy": float(subsidy_final["mean_predicted_wage_offer"]),
                "difference": float(
                    subsidy_final["mean_predicted_wage_offer"]
                    - baseline_final["mean_predicted_wage_offer"]
                ),
            },
        ]
    ).to_csv(outdir / "career_counterfactual_summary.csv", index=False)

    make_plot(counterfactual, outdir)

    pd.DataFrame(
        [
            {
                "prompt": "What are the states?",
                "guidance": "Schooling and experience summarize the payoff-relevant history in this small transfer model.",
            },
            {
                "prompt": "What is latent?",
                "guidance": "Preferences, ability, expectations, and continuation values are not directly observed.",
            },
            {
                "prompt": "What does tuition variation discipline?",
                "guidance": "Tuition variation helps discipline the school-choice response, but not full lifecycle welfare.",
            },
            {
                "prompt": "What is missing?",
                "guidance": "The transfer model omits occupation choice, borrowing constraints, fertility, equilibrium wages, and rich expectations.",
            },
        ]
    ).to_csv(outdir / "transfer_design_prompts.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    analyze(df, args.outdir)
    print(f"Wrote career-choice transfer outputs to {args.outdir}")


if __name__ == "__main__":
    main()
