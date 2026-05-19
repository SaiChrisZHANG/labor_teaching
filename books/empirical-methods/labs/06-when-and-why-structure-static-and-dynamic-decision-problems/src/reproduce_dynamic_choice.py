"""Run the Week 6 dynamic replacement reproduce and diagnose workflow."""

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


DELTA = 0.92
N_STATES = 10
EPS = 1e-8


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -35.0, 35.0)))


def estimate_transition_matrices(df: pd.DataFrame, n_states: int = N_STATES) -> np.ndarray:
    transitions = np.zeros((2, n_states, n_states))

    for state in range(n_states):
        sub = df[(df["mileage_state"] == state) & (df["replace"] == 0)]
        counts = np.ones(n_states) * 0.15
        for next_state, count in sub["next_mileage_state"].value_counts().items():
            counts[int(next_state)] += float(count)
        transitions[0, state] = counts / counts.sum()

    replacement_counts = np.ones(n_states) * 0.15
    replacement_next = df[df["replace"] == 1]["next_mileage_state"].value_counts()
    for next_state, count in replacement_next.items():
        replacement_counts[int(next_state)] += float(count)
    replacement_probs = replacement_counts / replacement_counts.sum()
    for state in range(n_states):
        transitions[1, state] = replacement_probs

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


def choice_neg_log_likelihood(df: pd.DataFrame, replace_prob_by_state: np.ndarray) -> float:
    states = df["mileage_state"].to_numpy(dtype=int)
    choices = df["replace"].to_numpy(dtype=float)
    probs = np.clip(replace_prob_by_state[states], EPS, 1.0 - EPS)
    return float(-np.sum(choices * np.log(probs) + (1.0 - choices) * np.log(1.0 - probs)))


def estimate_dynamic_model(
    df: pd.DataFrame,
    transitions: np.ndarray,
) -> tuple[dict[str, float], pd.DataFrame, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    grid_rows: list[dict[str, float]] = []
    best: dict[str, float] | None = None
    best_solution: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray] | None = None

    for replacement_cost in np.linspace(2.60, 7.10, 46):
        for maintenance_slope in np.linspace(0.22, 0.92, 36):
            solution = solve_dynamic_model(replacement_cost, maintenance_slope, transitions)
            neg_ll = choice_neg_log_likelihood(df, solution[3])
            row = {
                "replacement_cost": float(replacement_cost),
                "maintenance_slope": float(maintenance_slope),
                "neg_log_likelihood": neg_ll,
            }
            grid_rows.append(row)
            if best is None or neg_ll < best["neg_log_likelihood"]:
                best = row
                best_solution = solution

    assert best is not None
    assert best_solution is not None
    surface = pd.DataFrame(grid_rows)
    value, continue_value, replace_value, replace_prob = best_solution
    return best, surface, value, continue_value, replace_value, replace_prob


def estimate_static_logit(df: pd.DataFrame) -> tuple[dict[str, float], np.ndarray]:
    states = df["mileage_state"].to_numpy(dtype=float)
    choices = df["replace"].to_numpy(dtype=float)
    best: dict[str, float] | None = None
    best_probs_by_state = np.zeros(N_STATES)

    for intercept in np.linspace(-5.50, 1.00, 66):
        for slope in np.linspace(0.00, 1.20, 61):
            probs = np.clip(sigmoid(intercept + slope * states), EPS, 1.0 - EPS)
            neg_ll = float(-np.sum(choices * np.log(probs) + (1.0 - choices) * np.log(1.0 - probs)))
            if best is None or neg_ll < best["neg_log_likelihood"]:
                best = {
                    "static_intercept": float(intercept),
                    "static_state_slope": float(slope),
                    "neg_log_likelihood": neg_ll,
                }
                best_probs_by_state = np.asarray(
                    sigmoid(intercept + slope * np.arange(N_STATES, dtype=float))
                )

    assert best is not None
    return best, best_probs_by_state


def make_state_tables(
    df: pd.DataFrame,
    dynamic_probs: np.ndarray,
    static_probs: np.ndarray,
    outdir: Path,
) -> None:
    rows: list[dict[str, float | int]] = []
    support_rows: list[dict[str, float | int]] = []
    for state in range(N_STATES):
        sub = df[df["mileage_state"] == state]
        replace_count = int(sub["replace"].sum())
        continue_count = int((sub["replace"] == 0).sum())
        rows.append(
            {
                "mileage_state": state,
                "observations": int(len(sub)),
                "replace_count": replace_count,
                "empirical_replace_probability": float(sub["replace"].mean()) if len(sub) else np.nan,
                "dynamic_model_replace_probability": float(dynamic_probs[state]),
                "static_logit_replace_probability": float(static_probs[state]),
                "mean_operating_cost": float(sub["operating_cost"].mean()) if len(sub) else np.nan,
                "mean_next_mileage_state": float(sub["next_mileage_state"].mean()) if len(sub) else np.nan,
            }
        )
        support_rows.append(
            {
                "mileage_state": state,
                "observations": int(len(sub)),
                "continue_count": continue_count,
                "replace_count": replace_count,
                "share_of_sample": float(len(sub) / max(len(df), 1)),
                "support_note": "High states are most informative about replacement timing.",
            }
        )

    pd.DataFrame(rows).to_csv(outdir / "replacement_state_ccps.csv", index=False)
    pd.DataFrame(support_rows).to_csv(outdir / "state_support.csv", index=False)


def make_counterfactuals(
    df: pd.DataFrame,
    estimate: dict[str, float],
    transitions: np.ndarray,
    outdir: Path,
) -> None:
    state_dist = df["mileage_state"].value_counts(normalize=True).reindex(range(N_STATES), fill_value=0.0)
    rows: list[dict[str, float | str]] = []
    scenarios = [
        ("baseline", 0.0),
        ("lower replacement cost", -1.25),
        ("higher replacement cost", 1.25),
    ]
    for scenario, cost_shift in scenarios:
        cost = max(0.05, estimate["replacement_cost"] + cost_shift)
        value, _, _, probs = solve_dynamic_model(
            cost,
            estimate["maintenance_slope"],
            transitions,
        )
        rows.append(
            {
                "scenario": scenario,
                "replacement_cost": float(cost),
                "maintenance_slope": float(estimate["maintenance_slope"]),
                "mean_replacement_probability_observed_state_mix": float(np.dot(state_dist.to_numpy(), probs)),
                "mean_value_observed_state_mix": float(np.dot(state_dist.to_numpy(), value)),
                "note": "Partial-equilibrium teaching counterfactual holding transitions and discount factor fixed.",
            }
        )
    pd.DataFrame(rows).to_csv(outdir / "counterfactual_replacement_cost.csv", index=False)


def make_fit_plot(ccp_path: Path, outdir: Path) -> None:
    ccp = pd.read_csv(ccp_path)
    plt.figure(figsize=(7.2, 4.4))
    plt.plot(
        ccp["mileage_state"],
        ccp["empirical_replace_probability"],
        marker="o",
        linewidth=2.0,
        label="Empirical CCP",
        color="#4C78A8",
    )
    plt.plot(
        ccp["mileage_state"],
        ccp["dynamic_model_replace_probability"],
        marker="s",
        linewidth=2.0,
        label="Dynamic model",
        color="#54A24B",
    )
    plt.plot(
        ccp["mileage_state"],
        ccp["static_logit_replace_probability"],
        marker="^",
        linewidth=1.8,
        label="Static logit",
        color="#F58518",
    )
    plt.xlabel("Mileage state")
    plt.ylabel("Replacement probability")
    plt.ylim(-0.02, 1.02)
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(outdir / "replacement_fit.png", dpi=160)
    plt.close()


def analyze(df: pd.DataFrame, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    transitions = estimate_transition_matrices(df)

    dynamic_estimate, surface, value, continue_value, replace_value, dynamic_probs = estimate_dynamic_model(
        df,
        transitions,
    )
    static_estimate, static_probs = estimate_static_logit(df)

    surface.to_csv(outdir / "likelihood_surface.csv", index=False)
    make_state_tables(df, dynamic_probs, static_probs, outdir)

    estimates = pd.DataFrame(
        [
            {
                "model": "dynamic replacement logit",
                "replacement_cost": dynamic_estimate["replacement_cost"],
                "maintenance_slope": dynamic_estimate["maintenance_slope"],
                "discount_factor": DELTA,
                "neg_log_likelihood": dynamic_estimate["neg_log_likelihood"],
                "comparison_static_neg_log_likelihood": static_estimate["neg_log_likelihood"],
                "observations": len(df),
                "interpretation": "Replacement cost and maintenance slope are estimated from state-specific replacement choices with transitions held fixed.",
            },
            {
                "model": "static logit comparison",
                "replacement_cost": np.nan,
                "maintenance_slope": static_estimate["static_state_slope"],
                "discount_factor": np.nan,
                "neg_log_likelihood": static_estimate["neg_log_likelihood"],
                "comparison_static_neg_log_likelihood": static_estimate["neg_log_likelihood"],
                "observations": len(df),
                "interpretation": "Static comparison maps state directly to replacement probability and has no continuation value.",
            },
        ]
    )
    estimates.to_csv(outdir / "replacement_estimates.csv", index=False)

    value_rows = []
    for state in range(N_STATES):
        value_rows.append(
            {
                "mileage_state": state,
                "value": float(value[state]),
                "continue_choice_specific_value": float(continue_value[state]),
                "replace_choice_specific_value": float(replace_value[state]),
                "replacement_probability": float(dynamic_probs[state]),
            }
        )
    pd.DataFrame(value_rows).to_csv(outdir / "choice_specific_values.csv", index=False)

    make_counterfactuals(df, dynamic_estimate, transitions, outdir)
    make_fit_plot(outdir / "replacement_state_ccps.csv", outdir)

    pd.DataFrame(
        [
            {
                "prompt": "What is latent?",
                "guidance": "Replacement costs, maintenance costs, shocks, and continuation values are not directly observed.",
            },
            {
                "prompt": "What disciplines the model?",
                "guidance": "Replacement choices by mileage state and observed transitions across states discipline the dynamic mapping.",
            },
            {
                "prompt": "What does static fit miss?",
                "guidance": "A static hazard can match choice frequencies but cannot recompute behavior when replacement costs alter future states.",
            },
            {
                "prompt": "What is the counterfactual caveat?",
                "guidance": "The replacement-cost exercise holds transition rules, discounting, and shock distributions fixed.",
            },
        ]
    ).to_csv(outdir / "design_prompts.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    analyze(df, args.outdir)
    print(f"Wrote dynamic replacement outputs to {args.outdir}")


if __name__ == "__main__":
    main()
