"""Shared helpers for the Week 11 policy-learning teaching lab."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


OUTCOME = "earnings_12mo"
TREATMENT = "training_offer"
COST = "training_cost"
TRUE_Y0 = "true_y0"
TRUE_Y1 = "true_y1"
AUDIT_GROUP = "demographic_group"

NUMERIC_FEATURES = [
    "age",
    "education_years",
    "months_unemployed",
    "prior_earnings",
    "digital_skill",
    "local_unemployment",
    "baseline_risk",
]
CATEGORICAL_FEATURES = ["region"]


@dataclass
class FeatureSpec:
    numeric_features: list[str]
    categorical_levels: dict[str, list[str]]
    means: np.ndarray
    scales: np.ndarray
    feature_names: list[str]


@dataclass
class NuisanceModels:
    spec: FeatureSpec
    beta_mu0: np.ndarray
    beta_mu1: np.ndarray
    beta_e: np.ndarray


@dataclass
class NuisancePredictions:
    mu0: np.ndarray
    mu1: np.ndarray
    propensity: np.ndarray
    net_gain: np.ndarray


@dataclass
class PolicyDefinition:
    name: str
    kind: str
    feature: str
    direction: str
    threshold: float
    capacity_feasible: bool
    description: str


def sigmoid(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def add_intercept(x: np.ndarray) -> np.ndarray:
    return np.column_stack([np.ones(x.shape[0]), x])


def ridge_fit(x: np.ndarray, y: np.ndarray, penalty: float = 1e-4) -> np.ndarray:
    x_aug = add_intercept(x)
    gram = x_aug.T @ x_aug
    ridge = penalty * np.eye(gram.shape[0])
    ridge[0, 0] = 0.0
    return np.linalg.pinv(gram + ridge) @ x_aug.T @ y


def ridge_predict(x: np.ndarray, beta: np.ndarray) -> np.ndarray:
    return add_intercept(x) @ beta


def make_feature_spec(df: pd.DataFrame) -> FeatureSpec:
    parts, feature_names = raw_design_parts(df)
    raw = np.column_stack(parts)
    means = raw.mean(axis=0)
    scales = raw.std(axis=0)
    scales[scales < 1e-8] = 1.0
    categorical_levels = {
        column: sorted(df[column].dropna().astype(str).unique().tolist())
        for column in CATEGORICAL_FEATURES
    }
    return FeatureSpec(NUMERIC_FEATURES.copy(), categorical_levels, means, scales, feature_names)


def raw_design_parts(
    df: pd.DataFrame,
    categorical_levels: dict[str, list[str]] | None = None,
) -> tuple[list[np.ndarray], list[str]]:
    parts: list[np.ndarray] = []
    feature_names: list[str] = []

    numeric = df[NUMERIC_FEATURES].astype(float).to_numpy()
    parts.append(numeric)
    feature_names.extend(NUMERIC_FEATURES)

    levels = categorical_levels
    if levels is None:
        levels = {
            column: sorted(df[column].dropna().astype(str).unique().tolist())
            for column in CATEGORICAL_FEATURES
        }
    for column in CATEGORICAL_FEATURES:
        values = df[column].astype(str)
        for level in levels[column]:
            parts.append((values == level).to_numpy(dtype=float).reshape(-1, 1))
            feature_names.append(f"{column}:{level}")

    return parts, feature_names


def transform_features(df: pd.DataFrame, spec: FeatureSpec) -> np.ndarray:
    parts, feature_names = raw_design_parts(df, spec.categorical_levels)
    if feature_names != spec.feature_names:
        raise ValueError("Feature columns changed between training and prediction.")
    raw = np.column_stack(parts)
    return (raw - spec.means) / spec.scales


def net_observed_outcome(df: pd.DataFrame) -> np.ndarray:
    return df[OUTCOME].to_numpy(dtype=float) - df[TREATMENT].to_numpy(dtype=float) * df[COST].to_numpy(dtype=float)


def fit_nuisance(train_df: pd.DataFrame) -> NuisanceModels:
    spec = make_feature_spec(train_df)
    x = transform_features(train_df, spec)
    d = train_df[TREATMENT].to_numpy(dtype=float)
    y_net = net_observed_outcome(train_df)

    control_mask = d < 0.5
    treated_mask = d > 0.5
    if control_mask.sum() < 20 or treated_mask.sum() < 20:
        raise RuntimeError("The teaching sample needs both treated and untreated observations.")

    beta_mu0 = ridge_fit(x[control_mask], y_net[control_mask], penalty=0.05)
    beta_mu1 = ridge_fit(x[treated_mask], y_net[treated_mask], penalty=0.05)
    beta_e = ridge_fit(x, d, penalty=0.20)
    return NuisanceModels(spec=spec, beta_mu0=beta_mu0, beta_mu1=beta_mu1, beta_e=beta_e)


def predict_nuisance(df: pd.DataFrame, models: NuisanceModels) -> NuisancePredictions:
    x = transform_features(df, models.spec)
    mu0 = ridge_predict(x, models.beta_mu0)
    mu1 = ridge_predict(x, models.beta_mu1)
    propensity = np.clip(ridge_predict(x, models.beta_e), 0.05, 0.95)
    return NuisancePredictions(mu0=mu0, mu1=mu1, propensity=propensity, net_gain=mu1 - mu0)


def dr_value_scores(df: pd.DataFrame, policy: np.ndarray, pred: NuisancePredictions) -> np.ndarray:
    d = df[TREATMENT].to_numpy(dtype=float)
    y_net = net_observed_outcome(df)
    pi = policy.astype(float)
    treated_score = pred.mu1 + d / pred.propensity * (y_net - pred.mu1)
    control_score = pred.mu0 + (1.0 - d) / (1.0 - pred.propensity) * (y_net - pred.mu0)
    return pi * treated_score + (1.0 - pi) * control_score


def dr_effect_scores(df: pd.DataFrame, pred: NuisancePredictions) -> np.ndarray:
    d = df[TREATMENT].to_numpy(dtype=float)
    y_net = net_observed_outcome(df)
    return (
        pred.mu1
        - pred.mu0
        + d / pred.propensity * (y_net - pred.mu1)
        - (1.0 - d) / (1.0 - pred.propensity) * (y_net - pred.mu0)
    )


def split_train_eval(df: pd.DataFrame, seed: int = 11011, train_share: float = 0.60) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    order = rng.permutation(len(df))
    train_cut = int(round(train_share * len(df)))
    split = np.array(["eval"] * len(df), dtype=object)
    split[order[:train_cut]] = "train"
    out = df.copy()
    out["analysis_split"] = split
    return out


def make_policy_candidates(
    train_df: pd.DataFrame,
    train_pred: NuisancePredictions,
    capacity: float = 0.35,
) -> list[PolicyDefinition]:
    high_cut = 1.0 - capacity
    low_cut = capacity
    candidates = [
        PolicyDefinition(
            "treat_none",
            "none",
            "",
            "",
            float("nan"),
            True,
            "Assign no applicants to the training offer.",
        ),
        PolicyDefinition(
            "treat_all",
            "all",
            "",
            "",
            float("nan"),
            False,
            "Assign every applicant; useful as a benchmark but not capacity feasible.",
        ),
        PolicyDefinition(
            "high_baseline_risk",
            "threshold",
            "baseline_risk",
            "ge",
            float(np.quantile(train_df["baseline_risk"], high_cut)),
            True,
            "Assign applicants with high baseline labor-market risk.",
        ),
        PolicyDefinition(
            "low_prior_earnings",
            "threshold",
            "prior_earnings",
            "le",
            float(np.quantile(train_df["prior_earnings"], low_cut)),
            True,
            "Assign applicants with low prior earnings.",
        ),
        PolicyDefinition(
            "long_unemployment",
            "threshold",
            "months_unemployed",
            "ge",
            float(np.quantile(train_df["months_unemployed"], high_cut)),
            True,
            "Assign applicants with long unemployment duration.",
        ),
        PolicyDefinition(
            "predicted_net_gain_top35",
            "score_threshold",
            "predicted_net_gain",
            "ge",
            float(np.quantile(train_pred.net_gain, high_cut)),
            True,
            "Assign applicants with the highest estimated net causal gains.",
        ),
    ]
    return candidates


def apply_policy(df: pd.DataFrame, pred: NuisancePredictions, policy: PolicyDefinition) -> np.ndarray:
    if policy.kind == "none":
        return np.zeros(len(df), dtype=int)
    if policy.kind == "all":
        return np.ones(len(df), dtype=int)
    if policy.kind == "score_threshold":
        values = pred.net_gain
    elif policy.kind == "threshold":
        values = df[policy.feature].to_numpy(dtype=float)
    else:
        raise ValueError(f"Unknown policy kind: {policy.kind}")

    if policy.direction == "ge":
        return (values >= policy.threshold).astype(int)
    if policy.direction == "le":
        return (values <= policy.threshold).astype(int)
    raise ValueError(f"Unknown policy direction: {policy.direction}")


def weighted_mean(values: np.ndarray, weights: np.ndarray | None = None) -> float:
    if weights is None:
        return float(np.mean(values))
    weights = np.asarray(weights, dtype=float)
    return float(np.sum(weights * values) / np.sum(weights))


def evaluate_policies(
    df: pd.DataFrame,
    pred: NuisancePredictions,
    policies: list[PolicyDefinition],
    weights: np.ndarray | None = None,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for policy in policies:
        assignment = apply_policy(df, pred, policy)
        scores = dr_value_scores(df, assignment, pred)
        rows.append(
            {
                "policy": policy.name,
                "description": policy.description,
                "policy_kind": policy.kind,
                "feature": policy.feature,
                "direction": policy.direction,
                "threshold": policy.threshold,
                "capacity_feasible": policy.capacity_feasible,
                "assignment_rate": weighted_mean(assignment.astype(float), weights),
                "dr_value": weighted_mean(scores, weights),
                "n": int(len(df)),
            }
        )
    return pd.DataFrame(rows)


def select_policy(training_values: pd.DataFrame) -> str:
    feasible = training_values[training_values["capacity_feasible"]].copy()
    feasible = feasible.sort_values(["dr_value", "policy"], ascending=[False, True])
    return str(feasible.iloc[0]["policy"])


def policy_by_name(policies: list[PolicyDefinition], name: str) -> PolicyDefinition:
    for policy in policies:
        if policy.name == name:
            return policy
    raise KeyError(name)


def add_regret(values: pd.DataFrame) -> pd.DataFrame:
    out = values.copy()
    feasible = out[out["capacity_feasible"]]
    best = float(feasible["dr_value"].max())
    out["regret_within_feasible_class"] = np.where(out["capacity_feasible"], best - out["dr_value"], np.nan)
    return out.sort_values(["capacity_feasible", "dr_value"], ascending=[False, False]).reset_index(drop=True)


def cate_by_risk_group(df: pd.DataFrame, pred: NuisancePredictions) -> pd.DataFrame:
    out = df.copy()
    out["risk_group"] = pd.qcut(out["baseline_risk"], q=3, labels=["low", "middle", "high"])
    out["dr_net_effect"] = dr_effect_scores(df, pred)
    rows: list[dict[str, object]] = []
    for risk_group, group in out.groupby("risk_group", observed=False):
        rows.append(
            {
                "risk_group": str(risk_group),
                "n": int(len(group)),
                "treated": int(group[TREATMENT].sum()),
                "untreated": int(len(group) - group[TREATMENT].sum()),
                "mean_baseline_risk": float(group["baseline_risk"].mean()),
                "dr_net_effect": float(group["dr_net_effect"].mean()),
                "mean_true_net_effect_in_synthetic_data": float(group["true_net_effect"].mean()),
            }
        )
    return pd.DataFrame(rows)


def overlap_diagnostics(
    df: pd.DataFrame,
    pred: NuisancePredictions,
    selected_assignment: np.ndarray,
) -> pd.DataFrame:
    groups = {
        "full_eval_sample": np.ones(len(df), dtype=bool),
        "assigned_by_selected_rule": selected_assignment.astype(bool),
        "not_assigned_by_selected_rule": ~selected_assignment.astype(bool),
    }
    rows: list[dict[str, object]] = []
    for group_name, mask in groups.items():
        if mask.sum() == 0:
            continue
        prop = pred.propensity[mask]
        sub = df.loc[mask]
        rows.append(
            {
                "group": group_name,
                "n": int(mask.sum()),
                "treated": int(sub[TREATMENT].sum()),
                "untreated": int(len(sub) - sub[TREATMENT].sum()),
                "propensity_p10": float(np.quantile(prop, 0.10)),
                "propensity_p50": float(np.quantile(prop, 0.50)),
                "propensity_p90": float(np.quantile(prop, 0.90)),
            }
        )
    return pd.DataFrame(rows)


def fairness_audit(
    df: pd.DataFrame,
    pred: NuisancePredictions,
    assignment: np.ndarray,
    group_column: str = AUDIT_GROUP,
) -> pd.DataFrame:
    out = df.copy()
    out["policy_assignment"] = assignment
    out["predicted_net_gain"] = pred.net_gain
    rows: list[dict[str, object]] = []
    for group_name, group in out.groupby(group_column, observed=False):
        rows.append(
            {
                group_column: str(group_name),
                "n": int(len(group)),
                "policy_assignment_rate": float(group["policy_assignment"].mean()),
                "observed_training_rate": float(group[TREATMENT].mean()),
                "mean_predicted_net_gain": float(group["predicted_net_gain"].mean()),
                "mean_baseline_risk": float(group["baseline_risk"].mean()),
                "mean_true_net_effect_in_synthetic_data": float(group["true_net_effect"].mean()),
            }
        )
    return pd.DataFrame(rows)


def true_policy_value(df: pd.DataFrame, assignment: np.ndarray, weights: np.ndarray | None = None) -> float:
    pi = assignment.astype(float)
    value = pi * (df[TRUE_Y1].to_numpy(dtype=float) - df[COST].to_numpy(dtype=float)) + (1.0 - pi) * df[
        TRUE_Y0
    ].to_numpy(dtype=float)
    return weighted_mean(value, weights)


def source_target_cell_weights(source_df: pd.DataFrame, target_df: pd.DataFrame) -> tuple[np.ndarray, pd.DataFrame]:
    source = source_df.copy()
    target = target_df.copy()
    cuts = np.quantile(source["baseline_risk"], [0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0])
    cuts[0] = -np.inf
    cuts[-1] = np.inf
    labels = ["low", "middle", "high"]
    source["risk_cell"] = pd.cut(source["baseline_risk"], bins=cuts, labels=labels, include_lowest=True)
    target["risk_cell"] = pd.cut(target["baseline_risk"], bins=cuts, labels=labels, include_lowest=True)

    source_cells = source.groupby(["risk_cell", "region"], observed=False).size() / len(source)
    target_cells = target.groupby(["risk_cell", "region"], observed=False).size() / len(target)
    weights = np.ones(len(source), dtype=float)
    rows: list[dict[str, object]] = []
    for idx, row in source.reset_index().iterrows():
        key = (row["risk_cell"], row["region"])
        source_share = float(source_cells.get(key, 0.0))
        target_share = float(target_cells.get(key, 0.0))
        weight = target_share / source_share if source_share > 0 else 0.0
        weights[idx] = min(weight, 8.0)
    weights = weights / weights.mean()

    all_keys = sorted(set(source_cells.index).union(set(target_cells.index)), key=lambda key: (str(key[0]), str(key[1])))
    for key in all_keys:
        source_share = float(source_cells.get(key, 0.0))
        target_share = float(target_cells.get(key, 0.0))
        rows.append(
            {
                "risk_cell": str(key[0]),
                "region": str(key[1]),
                "source_share": source_share,
                "target_share": target_share,
                "target_to_source_weight": target_share / source_share if source_share > 0 else float("nan"),
            }
        )
    return weights, pd.DataFrame(rows)


def effective_sample_size(weights: np.ndarray) -> float:
    return float((weights.sum() ** 2) / np.sum(weights**2))


def ensure_outdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
