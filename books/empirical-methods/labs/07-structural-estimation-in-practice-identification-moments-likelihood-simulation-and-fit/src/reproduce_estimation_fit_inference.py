"""Run the Week 7 replacement-model estimation, fit, and inference workflow."""

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


DELTA = 0.92
N_STATES = 9
EPS = 1e-8


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35.0, 35.0)))


def estimate_transition_matrices(df: pd.DataFrame, n_states: int = N_STATES) -> np.ndarray:
    transitions = np.zeros((2, n_states, n_states))
    for state in range(n_states):
        continue_sub = df[(df["mileage_state"] == state) & (df["replace"] == 0)]
        continue_counts = np.ones(n_states) * 0.20
        for next_state, count in continue_sub["next_mileage_state"].value_counts().items():
            continue_counts[int(next_state)] += float(count)
        transitions[0, state] = continue_counts / continue_counts.sum()

        replace_sub = df[(df["mileage_state"] == state) & (df["replace"] == 1)]
        replace_counts = np.ones(n_states) * 0.20
        if len(replace_sub) < 5:
            replace_sub = df[df["replace"] == 1]
        for next_state, count in replace_sub["next_mileage_state"].value_counts().items():
            replace_counts[int(next_state)] += float(count)
        transitions[1, state] = replace_counts / replace_counts.sum()
    return transitions


def solve_dynamic_model(
    replacement_cost: float,
    maintenance_slope: float,
    transitions: np.ndarray,
    delta: float = DELTA,
    tolerance: float = 1e-10,
    max_iter: int = 10_000,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    states = np.arange(transitions.shape[1], dtype=float)
    value = np.zeros_like(states)
    for _ in range(max_iter):
        continue_value = -maintenance_slope * states + delta * transitions[0] @ value
        replace_value = -replacement_cost + delta * transitions[1] @ value
        new_value = np.logaddexp(continue_value, replace_value)
        if np.max(np.abs(new_value - value)) < tolerance:
            value = new_value
            break
        value = new_value
    continue_value = -maintenance_slope * states + delta * transitions[0] @ value
    replace_value = -replacement_cost + delta * transitions[1] @ value
    log_denom = np.logaddexp(continue_value, replace_value)
    replace_prob = np.exp(replace_value - log_denom)
    return value, continue_value, replace_value, replace_prob


def choice_neg_log_likelihood(df: pd.DataFrame, probs_by_state: np.ndarray) -> float:
    states = df["mileage_state"].to_numpy(dtype=int)
    choices = df["replace"].to_numpy(dtype=float)
    probs = np.clip(probs_by_state[states], EPS, 1.0 - EPS)
    return float(-np.sum(choices * np.log(probs) + (1.0 - choices) * np.log(1.0 - probs)))


def empirical_state_moments(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | int]] = []
    for state in range(N_STATES):
        sub = df[df["mileage_state"] == state]
        rows.append(
            {
                "mileage_state": state,
                "observations": int(len(sub)),
                "empirical_replace_probability": float(sub["replace"].mean()) if len(sub) else np.nan,
                "mean_next_mileage_state": float(sub["next_mileage_state"].mean()) if len(sub) else np.nan,
                "mean_operating_cost": float(sub["operating_cost"].mean()) if len(sub) else np.nan,
                "mean_downtime_days": float(sub["downtime_days"].mean()) if len(sub) else np.nan,
            }
        )
    return pd.DataFrame(rows)


def moment_weights(moment_table: pd.DataFrame, kind: str) -> np.ndarray:
    support = moment_table["observations"].to_numpy(dtype=float) > 0
    p = np.clip(moment_table.loc[support, "empirical_replace_probability"].to_numpy(dtype=float), 0.02, 0.98)
    n = moment_table.loc[support, "observations"].to_numpy(dtype=float)
    if kind == "identity":
        return np.ones_like(p)
    variances = np.maximum(p * (1.0 - p) / np.maximum(n, 1.0), 1e-4)
    weights = 1.0 / variances
    return weights / weights.mean()


def moment_criterion(
    moment_table: pd.DataFrame,
    model_probs: np.ndarray,
    kind: str,
) -> float:
    support = moment_table["observations"].to_numpy(dtype=float) > 0
    empirical = moment_table.loc[support, "empirical_replace_probability"].to_numpy(dtype=float)
    diff = empirical - model_probs[support]
    weights = moment_weights(moment_table, kind)
    return float(np.sum(weights * diff**2))


def estimate_on_grid(
    df: pd.DataFrame,
    transitions: np.ndarray,
    estimator: str,
    weight_kind: str = "identity",
    cost_grid: np.ndarray | None = None,
    slope_grid: np.ndarray | None = None,
    smm_seed: int = 123,
) -> tuple[dict[str, float | str], np.ndarray]:
    costs = np.linspace(3.00, 5.80, 29) if cost_grid is None else cost_grid
    slopes = np.linspace(0.30, 0.82, 27) if slope_grid is None else slope_grid
    moment_table = empirical_state_moments(df)
    best: dict[str, float | str] | None = None
    best_probs = np.zeros(N_STATES)
    state_counts = moment_table["observations"].to_numpy(dtype=int)
    empirical = moment_table["empirical_replace_probability"].to_numpy(dtype=float)
    rng = np.random.default_rng(smm_seed)

    for replacement_cost in costs:
        for maintenance_slope in slopes:
            _, _, _, probs = solve_dynamic_model(
                float(replacement_cost),
                float(maintenance_slope),
                transitions,
            )
            if estimator == "likelihood":
                criterion = choice_neg_log_likelihood(df, probs)
            elif estimator == "smm":
                draws = []
                for state, count in enumerate(state_counts):
                    if count <= 0:
                        draws.append(np.nan)
                        continue
                    simulated_counts = rng.binomial(count, float(probs[state]), size=6)
                    draws.append(float(simulated_counts.mean() / count))
                simulated = np.asarray(draws)
                support = state_counts > 0
                weights = moment_weights(moment_table, weight_kind)
                criterion = float(np.sum(weights * (empirical[support] - simulated[support]) ** 2))
            else:
                criterion = moment_criterion(moment_table, probs, weight_kind)
            if best is None or criterion < float(best["criterion"]):
                best = {
                    "estimator": estimator,
                    "weighting": weight_kind,
                    "replacement_cost": float(replacement_cost),
                    "maintenance_slope": float(maintenance_slope),
                    "criterion": float(criterion),
                }
                best_probs = probs
    assert best is not None
    return best, best_probs


def estimate_static_logit_variance(df: pd.DataFrame) -> pd.DataFrame:
    x = np.column_stack(
        [
            np.ones(len(df)),
            df["mileage_state"].to_numpy(dtype=float),
        ]
    )
    y = df["replace"].to_numpy(dtype=float)
    beta = np.zeros(x.shape[1])
    for _ in range(80):
        eta = x @ beta
        p = np.clip(sigmoid(eta), EPS, 1.0 - EPS)
        weights = np.maximum(p * (1.0 - p), 1e-5)
        z = eta + (y - p) / weights
        beta_new = np.linalg.pinv(x.T @ (x * weights[:, None])) @ (x.T @ (weights * z))
        if np.max(np.abs(beta_new - beta)) < 1e-9:
            beta = beta_new
            break
        beta = beta_new
    eta = x @ beta
    p = np.clip(sigmoid(eta), EPS, 1.0 - EPS)
    weights = np.maximum(p * (1.0 - p), 1e-5)
    n = len(df)
    a = (x.T @ (x * weights[:, None])) / n
    residual = y - p
    scores = x * residual[:, None]
    b = scores.T @ scores / n
    info_var = np.linalg.pinv(a) / n
    sandwich_var = np.linalg.pinv(a) @ b @ np.linalg.pinv(a) / n
    return pd.DataFrame(
        [
            {
                "model": "auxiliary static logit",
                "parameter": "intercept",
                "estimate": float(beta[0]),
                "information_se": float(np.sqrt(max(info_var[0, 0], 0.0))),
                "sandwich_opg_se": float(np.sqrt(max(sandwich_var[0, 0], 0.0))),
                "note": "Auxiliary variance calculation for Hessian and OPG logic.",
            },
            {
                "model": "auxiliary static logit",
                "parameter": "mileage_state",
                "estimate": float(beta[1]),
                "information_se": float(np.sqrt(max(info_var[1, 1], 0.0))),
                "sandwich_opg_se": float(np.sqrt(max(sandwich_var[1, 1], 0.0))),
                "note": "Auxiliary variance calculation for Hessian and OPG logic.",
            },
        ]
    )


def write_fit_tables(
    df: pd.DataFrame,
    transitions: np.ndarray,
    likelihood_probs: np.ndarray,
    gmm_probs: np.ndarray,
    outdir: Path,
) -> None:
    moments = empirical_state_moments(df)
    states = np.arange(N_STATES, dtype=float)
    moments["likelihood_model_replace_probability"] = likelihood_probs
    moments["gmm_model_replace_probability"] = gmm_probs
    moments.to_csv(outdir / "targeted_moment_fit.csv", index=False)

    untargeted_rows: list[dict[str, float | int | str]] = []
    for state in range(N_STATES):
        empirical_next = moments.loc[state, "mean_next_mileage_state"]
        likelihood_expected_next = float(
            (1.0 - likelihood_probs[state]) * (transitions[0, state] @ states)
            + likelihood_probs[state] * (transitions[1, state] @ states)
        )
        gmm_expected_next = float(
            (1.0 - gmm_probs[state]) * (transitions[0, state] @ states)
            + gmm_probs[state] * (transitions[1, state] @ states)
        )
        untargeted_rows.append(
            {
                "mileage_state": state,
                "observations": int(moments.loc[state, "observations"]),
                "empirical_mean_next_mileage_state": empirical_next,
                "likelihood_model_expected_next_state": likelihood_expected_next,
                "gmm_model_expected_next_state": gmm_expected_next,
                "empirical_mean_downtime_days": moments.loc[state, "mean_downtime_days"],
                "diagnostic_note": "Next-state fit is implied through transitions; downtime is untargeted and not modeled.",
            }
        )
    pd.DataFrame(untargeted_rows).to_csv(outdir / "untargeted_fit.csv", index=False)

    plt.figure(figsize=(7.4, 4.4))
    plt.plot(
        moments["mileage_state"],
        moments["empirical_replace_probability"],
        marker="o",
        linewidth=2.0,
        label="Empirical",
        color="#4C78A8",
    )
    plt.plot(
        moments["mileage_state"],
        likelihood_probs,
        marker="s",
        linewidth=2.0,
        label="Likelihood",
        color="#54A24B",
    )
    plt.plot(
        moments["mileage_state"],
        gmm_probs,
        marker="^",
        linewidth=1.8,
        label="GMM",
        color="#F58518",
    )
    plt.xlabel("Mileage state")
    plt.ylabel("Replacement probability")
    plt.ylim(-0.02, 1.02)
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(outdir / "replacement_fit.png", dpi=160)
    plt.close()


def replacement_counterfactual(
    replacement_cost: float,
    maintenance_slope: float,
    transitions: np.ndarray,
    state_distribution: np.ndarray,
    cost_shift: float,
) -> float:
    _, _, _, probs = solve_dynamic_model(
        max(0.05, replacement_cost + cost_shift),
        maintenance_slope,
        transitions,
    )
    return float(state_distribution @ probs)


def cluster_bootstrap(
    df: pd.DataFrame,
    draws: int,
    seed: int,
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    units = np.asarray(sorted(df["unit_id"].unique()))
    rows: list[dict[str, float | int]] = []
    cost_grid = np.linspace(3.20, 5.60, 17)
    slope_grid = np.linspace(0.34, 0.78, 15)
    for draw in range(1, draws + 1):
        sampled = rng.choice(units, size=len(units), replace=True)
        boot = pd.concat([df[df["unit_id"] == unit] for unit in sampled], ignore_index=True)
        transitions = estimate_transition_matrices(boot)
        estimate, _ = estimate_on_grid(
            boot,
            transitions,
            estimator="gmm",
            weight_kind="diagonal",
            cost_grid=cost_grid,
            slope_grid=slope_grid,
        )
        rows.append(
            {
                "bootstrap_draw": draw,
                "replacement_cost": float(estimate["replacement_cost"]),
                "maintenance_slope": float(estimate["maintenance_slope"]),
                "criterion": float(estimate["criterion"]),
            }
        )
    return pd.DataFrame(rows)


def write_counterfactual_uncertainty(
    df: pd.DataFrame,
    transitions: np.ndarray,
    estimate: dict[str, float | str],
    bootstrap: pd.DataFrame,
    outdir: Path,
) -> pd.DataFrame:
    state_distribution = (
        df["mileage_state"]
        .value_counts(normalize=True)
        .reindex(range(N_STATES), fill_value=0.0)
        .to_numpy(dtype=float)
    )
    theta = np.asarray(
        [
            float(estimate["replacement_cost"]),
            float(estimate["maintenance_slope"]),
        ]
    )
    cost_shift = -0.80
    point = replacement_counterfactual(theta[0], theta[1], transitions, state_distribution, cost_shift)

    boot_theta = bootstrap[["replacement_cost", "maintenance_slope"]].to_numpy(dtype=float)
    covariance = np.cov(boot_theta.T) if len(bootstrap) > 1 else np.eye(2) * np.nan

    step = np.asarray([0.05, 0.02])
    gradient = np.zeros(2)
    for idx in range(2):
        high = theta.copy()
        low = theta.copy()
        high[idx] += step[idx]
        low[idx] -= step[idx]
        high_value = replacement_counterfactual(high[0], high[1], transitions, state_distribution, cost_shift)
        low_value = replacement_counterfactual(low[0], low[1], transitions, state_distribution, cost_shift)
        gradient[idx] = (high_value - low_value) / (2.0 * step[idx])
    delta_var = float(gradient @ covariance @ gradient) if np.all(np.isfinite(covariance)) else np.nan

    boot_values = np.asarray(
        [
            replacement_counterfactual(row.replacement_cost, row.maintenance_slope, transitions, state_distribution, cost_shift)
            for row in bootstrap.itertuples(index=False)
        ]
    )
    baseline = replacement_counterfactual(theta[0], theta[1], transitions, state_distribution, 0.0)
    rows = pd.DataFrame(
        [
            {
                "object": "baseline mean replacement probability",
                "estimate": baseline,
                "delta_method_se": np.nan,
                "cluster_bootstrap_se": np.nan,
                "bootstrap_p05": np.nan,
                "bootstrap_p95": np.nan,
                "draws": len(bootstrap),
                "note": "Baseline model-implied replacement probability using observed state mix.",
            },
            {
                "object": "lower replacement cost counterfactual",
                "estimate": point,
                "delta_method_se": float(np.sqrt(max(delta_var, 0.0))) if np.isfinite(delta_var) else np.nan,
                "cluster_bootstrap_se": float(np.std(boot_values, ddof=1)) if len(boot_values) > 1 else np.nan,
                "bootstrap_p05": float(np.quantile(boot_values, 0.05)) if len(boot_values) else np.nan,
                "bootstrap_p95": float(np.quantile(boot_values, 0.95)) if len(boot_values) else np.nan,
                "draws": len(bootstrap),
                "note": "Delta method uses numerical gradient and cluster-bootstrap parameter covariance.",
            },
        ]
    )
    rows.to_csv(outdir / "counterfactual_uncertainty.csv", index=False)
    return rows


def write_simulation_noise(
    df: pd.DataFrame,
    transitions: np.ndarray,
    outdir: Path,
) -> pd.DataFrame:
    rows: list[dict[str, float | int | str]] = []
    cost_grid = np.linspace(3.30, 5.50, 12)
    slope_grid = np.linspace(0.36, 0.76, 11)
    for seed in [101, 202, 303, 404, 505]:
        estimate, _ = estimate_on_grid(
            df,
            transitions,
            estimator="smm",
            weight_kind="diagonal",
            cost_grid=cost_grid,
            slope_grid=slope_grid,
            smm_seed=seed,
        )
        rows.append(
            {
                "simulation_seed": seed,
                "replacement_cost": float(estimate["replacement_cost"]),
                "maintenance_slope": float(estimate["maintenance_slope"]),
                "criterion": float(estimate["criterion"]),
                "note": "Same data and grid; only simulation draws change.",
            }
        )
    output = pd.DataFrame(rows)
    output.to_csv(outdir / "simulation_noise.csv", index=False)
    return output


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    transitions = estimate_transition_matrices(df)

    likelihood_estimate, likelihood_probs = estimate_on_grid(df, transitions, estimator="likelihood")
    identity_estimate, identity_probs = estimate_on_grid(
        df,
        transitions,
        estimator="gmm",
        weight_kind="identity",
    )
    diagonal_estimate, diagonal_probs = estimate_on_grid(
        df,
        transitions,
        estimator="gmm",
        weight_kind="diagonal",
    )
    smm_estimate, _ = estimate_on_grid(
        df,
        transitions,
        estimator="smm",
        weight_kind="diagonal",
        cost_grid=np.linspace(3.20, 5.60, 17),
        slope_grid=np.linspace(0.34, 0.78, 15),
        smm_seed=777,
    )

    pd.DataFrame([likelihood_estimate]).to_csv(outdir / "likelihood_estimates.csv", index=False)
    pd.DataFrame([identity_estimate, diagonal_estimate, smm_estimate]).to_csv(
        outdir / "moment_estimates.csv",
        index=False,
    )
    pd.DataFrame([identity_estimate, diagonal_estimate]).to_csv(
        outdir / "weighting_sensitivity.csv",
        index=False,
    )
    write_fit_tables(df, transitions, likelihood_probs, diagonal_probs, outdir)

    bootstrap = cluster_bootstrap(df, draws=30, seed=6787)
    bootstrap.to_csv(outdir / "bootstrap_estimates.csv", index=False)
    counterfactual = write_counterfactual_uncertainty(df, transitions, diagonal_estimate, bootstrap, outdir)
    simulation_noise = write_simulation_noise(df, transitions, outdir)
    static_variance = estimate_static_logit_variance(df)
    static_variance.to_csv(outdir / "auxiliary_static_logit_variance.csv", index=False)

    structural_variance = pd.DataFrame(
        [
            {
                "method": "cluster bootstrap",
                "object": "replacement_cost",
                "estimate": float(diagonal_estimate["replacement_cost"]),
                "standard_error": float(bootstrap["replacement_cost"].std(ddof=1)),
                "note": "Resamples units and re-estimates the moment estimator on a reduced grid.",
            },
            {
                "method": "cluster bootstrap",
                "object": "maintenance_slope",
                "estimate": float(diagonal_estimate["maintenance_slope"]),
                "standard_error": float(bootstrap["maintenance_slope"].std(ddof=1)),
                "note": "Resamples units and re-estimates the moment estimator on a reduced grid.",
            },
            {
                "method": "delta method",
                "object": "lower replacement cost counterfactual",
                "estimate": float(counterfactual.loc[1, "estimate"]),
                "standard_error": float(counterfactual.loc[1, "delta_method_se"]),
                "note": "Uses finite-difference gradient and cluster-bootstrap covariance.",
            },
            {
                "method": "simulation multi-seed check",
                "object": "SMM replacement_cost",
                "estimate": float(simulation_noise["replacement_cost"].mean()),
                "standard_error": float(simulation_noise["replacement_cost"].std(ddof=1)),
                "note": "Shows finite simulation variation across random seeds.",
            },
        ]
    )
    structural_variance.to_csv(outdir / "variance_summary.csv", index=False)

    pd.DataFrame(
        [
            {
                "prompt": "What identifies replacement cost?",
                "guidance": "Replacement choices by mileage state and transition consequences discipline the cost of replacement.",
            },
            {
                "prompt": "What do targeted moments carry?",
                "guidance": "State-specific replacement probabilities carry most of the moment-based identifying power.",
            },
            {
                "prompt": "What is untargeted?",
                "guidance": "Downtime and parts of next-state fit are diagnostics rather than direct estimation targets.",
            },
            {
                "prompt": "What does the bootstrap respect?",
                "guidance": "The teaching bootstrap resamples units so within-unit histories stay together.",
            },
            {
                "prompt": "What is the simulation caveat?",
                "guidance": "SMM estimates can move across seeds when simulated moments are noisy relative to empirical moments.",
            },
        ]
    ).to_csv(outdir / "design_prompts.csv", index=False)

    print(f"Wrote replacement estimation outputs to {outdir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()
    analyze(pd.read_csv(args.input), args.outdir)


if __name__ == "__main__":
    main()
