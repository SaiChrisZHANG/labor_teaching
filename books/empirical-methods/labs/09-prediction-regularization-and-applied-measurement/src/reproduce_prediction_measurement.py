"""Run the Week 9 prediction-as-measurement teaching path."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


TECH_KEYWORDS = {
    "python",
    "sql",
    "cloud",
    "machine",
    "learning",
    "automation",
    "pipeline",
    "api",
    "analytics",
    "dashboard",
    "monitoring",
}


@dataclass
class FeatureSpec:
    vocabulary: list[str]
    feature_names: list[str]
    means: np.ndarray
    scales: np.ndarray
    sector_levels: list[str]
    region_levels: list[str]


@dataclass
class FittedModel:
    model_type: str
    penalty: float
    alpha: float
    intercept: float
    beta: np.ndarray
    feature_spec: FeatureSpec


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z0-9]+", str(text).lower())


def build_vocabulary(texts: pd.Series, min_count: int = 2) -> list[str]:
    counts: dict[str, int] = {}
    for text in texts:
        for token in set(tokenize(str(text))):
            counts[token] = counts.get(token, 0) + 1
    return sorted([token for token, count in counts.items() if count >= min_count])


def design_matrix(
    df: pd.DataFrame,
    vocabulary: list[str],
    sector_levels: list[str],
    region_levels: list[str],
    text_column: str = "posting_text",
) -> tuple[np.ndarray, list[str]]:
    matrix_parts: list[np.ndarray] = []
    feature_names: list[str] = []

    token_index = {token: idx for idx, token in enumerate(vocabulary)}
    text_matrix = np.zeros((len(df), len(vocabulary)), dtype=float)
    for row_idx, text in enumerate(df[text_column].fillna("")):
        for token in tokenize(str(text)):
            if token in token_index:
                text_matrix[row_idx, token_index[token]] += 1.0
    if vocabulary:
        matrix_parts.append(text_matrix)
        feature_names.extend([f"text:{token}" for token in vocabulary])

    numeric = pd.DataFrame(index=df.index)
    numeric["log_firm_size"] = np.log(df.get("firm_size", pd.Series(100, index=df.index)).astype(float))
    numeric["year_centered"] = df.get("year", pd.Series(2023, index=df.index)).astype(float) - 2023.0
    numeric["remote_signal"] = df.get("remote_signal", pd.Series(0, index=df.index)).astype(float)
    matrix_parts.append(numeric.to_numpy(dtype=float))
    feature_names.extend(list(numeric.columns))

    for sector in sector_levels:
        matrix_parts.append((df.get("sector", pd.Series("", index=df.index)) == sector).to_numpy(dtype=float).reshape(-1, 1))
        feature_names.append(f"sector:{sector}")
    for region in region_levels:
        matrix_parts.append((df.get("region", pd.Series("", index=df.index)) == region).to_numpy(dtype=float).reshape(-1, 1))
        feature_names.append(f"region:{region}")

    return np.column_stack(matrix_parts), feature_names


def make_feature_spec(train_df: pd.DataFrame, text_column: str = "posting_text") -> FeatureSpec:
    vocabulary = build_vocabulary(train_df[text_column])
    sector_levels = sorted(train_df["sector"].dropna().unique().tolist())
    region_levels = sorted(train_df["region"].dropna().unique().tolist())
    x_raw, feature_names = design_matrix(train_df, vocabulary, sector_levels, region_levels, text_column=text_column)
    means = x_raw.mean(axis=0)
    scales = x_raw.std(axis=0)
    scales[scales < 1e-8] = 1.0
    return FeatureSpec(vocabulary, feature_names, means, scales, sector_levels, region_levels)


def transform_features(df: pd.DataFrame, spec: FeatureSpec, text_column: str = "posting_text") -> np.ndarray:
    x_raw, feature_names = design_matrix(
        df,
        spec.vocabulary,
        spec.sector_levels,
        spec.region_levels,
        text_column=text_column,
    )
    if feature_names != spec.feature_names:
        raise ValueError("Feature names changed between training and prediction.")
    return (x_raw - spec.means) / spec.scales


def soft_threshold(value: float, threshold: float) -> float:
    if value > threshold:
        return value - threshold
    if value < -threshold:
        return value + threshold
    return 0.0


def fit_regularized(
    x: np.ndarray,
    y: np.ndarray,
    model_type: str,
    penalty: float,
    alpha: float = 0.55,
    max_iter: int = 4000,
    tolerance: float = 1e-7,
) -> tuple[float, np.ndarray]:
    y_centered = y - y.mean()
    intercept = float(y.mean())
    n_features = x.shape[1]

    if model_type == "ridge":
        gram = (x.T @ x) / x.shape[0]
        rhs = (x.T @ y_centered) / x.shape[0]
        beta = np.linalg.solve(gram + penalty * np.eye(n_features), rhs)
        return intercept, beta

    if model_type == "lasso":
        l1_weight = 1.0
        l2_weight = 0.0
    elif model_type == "elastic_net":
        l1_weight = alpha
        l2_weight = 1.0 - alpha
    else:
        raise ValueError(f"Unknown model_type: {model_type}")

    beta = np.zeros(n_features, dtype=float)
    column_norms = (x**2).mean(axis=0)
    column_norms[column_norms < 1e-10] = 1.0

    for _ in range(max_iter):
        old_beta = beta.copy()
        fitted = x @ beta
        for j in range(n_features):
            residual = y_centered - fitted + x[:, j] * beta[j]
            rho = float(np.mean(x[:, j] * residual))
            updated = soft_threshold(rho, penalty * l1_weight / 2.0)
            updated = updated / (column_norms[j] + penalty * l2_weight)
            fitted += x[:, j] * (updated - beta[j])
            beta[j] = updated
        if float(np.max(np.abs(beta - old_beta))) < tolerance:
            break

    return intercept, beta


def predict_scores(model: FittedModel, df: pd.DataFrame, text_column: str = "posting_text") -> np.ndarray:
    x = transform_features(df, model.feature_spec, text_column=text_column)
    scores = model.intercept + x @ model.beta
    return np.clip(scores, 0.0, 1.0)


def prediction_metrics(y_true: np.ndarray, scores: np.ndarray, prefix: str = "") -> dict[str, float]:
    predictions = (scores >= 0.5).astype(int)
    positives = predictions == 1
    actual_positives = y_true == 1
    true_positive = float(np.sum(positives & actual_positives))
    false_positive = float(np.sum(positives & ~actual_positives))
    false_negative = float(np.sum(~positives & actual_positives))
    accuracy = float(np.mean(predictions == y_true))
    precision = true_positive / (true_positive + false_positive) if true_positive + false_positive else 0.0
    recall = true_positive / (true_positive + false_negative) if true_positive + false_negative else 0.0
    brier = float(np.mean((y_true - scores) ** 2))
    mae = float(np.mean(np.abs(y_true - scores)))
    out = {
        "brier": brier,
        "mae": mae,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "positive_rate": float(np.mean(predictions)),
    }
    if prefix:
        return {f"{prefix}_{key}": value for key, value in out.items()}
    return out


def split_train_test(df: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(9191)
    order = rng.permutation(len(df))
    test_cut = int(round(0.30 * len(df)))
    split = np.array(["train"] * len(df), dtype=object)
    split[order[:test_cut]] = "test"
    out = df.copy()
    out["split"] = split
    return out


def make_folds(train_df: pd.DataFrame, k: int = 5) -> np.ndarray:
    rng = np.random.default_rng(9291)
    fold_ids = np.zeros(len(train_df), dtype=int)
    for label in [0, 1]:
        label_positions = np.where(train_df["technology_intensive"].to_numpy() == label)[0]
        shuffled = rng.permutation(label_positions)
        for idx, position in enumerate(shuffled):
            fold_ids[position] = idx % k
    return fold_ids


def cross_validate(train_df: pd.DataFrame, spec: FeatureSpec) -> pd.DataFrame:
    folds = make_folds(train_df)
    y = train_df["technology_intensive"].to_numpy(dtype=float)
    penalties = [0.001, 0.01, 0.05, 0.10, 0.25, 0.50]
    rows: list[dict[str, float | str]] = []
    for model_type in ["ridge", "lasso", "elastic_net"]:
        for penalty in penalties:
            fold_losses = []
            for fold in sorted(set(folds)):
                fit_df = train_df.iloc[folds != fold]
                val_df = train_df.iloc[folds == fold]
                fold_spec = make_feature_spec(fit_df)
                x_fit = transform_features(fit_df, fold_spec)
                y_fit = fit_df["technology_intensive"].to_numpy(dtype=float)
                intercept, beta = fit_regularized(x_fit, y_fit, model_type=model_type, penalty=penalty)
                model = FittedModel(model_type, penalty, 0.55, intercept, beta, fold_spec)
                scores = predict_scores(model, val_df)
                y_val = val_df["technology_intensive"].to_numpy(dtype=float)
                fold_losses.append(float(np.mean((y_val - scores) ** 2)))
            rows.append(
                {
                    "model_type": model_type,
                    "penalty": penalty,
                    "mean_validation_brier": float(np.mean(fold_losses)),
                    "sd_validation_brier": float(np.std(fold_losses, ddof=1)),
                }
            )
    return pd.DataFrame(rows).sort_values(["mean_validation_brier", "model_type", "penalty"]).reset_index(drop=True)


def fit_from_cv(train_df: pd.DataFrame, cv_results: pd.DataFrame, model_type: str | None = None) -> FittedModel:
    if model_type is None:
        row = cv_results.iloc[0]
    else:
        row = cv_results[cv_results["model_type"] == model_type].iloc[0]
    spec = make_feature_spec(train_df)
    x_train = transform_features(train_df, spec)
    y_train = train_df["technology_intensive"].to_numpy(dtype=float)
    intercept, beta = fit_regularized(
        x_train,
        y_train,
        model_type=str(row["model_type"]),
        penalty=float(row["penalty"]),
    )
    return FittedModel(str(row["model_type"]), float(row["penalty"]), 0.55, intercept, beta, spec)


def keyword_scores(df: pd.DataFrame) -> np.ndarray:
    scores = []
    for text in df["posting_text"].fillna(""):
        tokens = set(tokenize(str(text)))
        scores.append(1.0 if tokens & TECH_KEYWORDS else 0.0)
    return np.asarray(scores, dtype=float)


def calibration_table(df: pd.DataFrame, score_column: str, label_column: str) -> pd.DataFrame:
    bins = np.linspace(0.0, 1.0, 6)
    out = df.copy()
    out["score_bin"] = pd.cut(out[score_column], bins=bins, include_lowest=True)
    rows = []
    for score_bin, group in out.groupby("score_bin", observed=False):
        if len(group) == 0:
            continue
        rows.append(
            {
                "score_bin": str(score_bin),
                "n": int(len(group)),
                "mean_score": float(group[score_column].mean()),
                "realized_rate": float(group[label_column].mean()),
                "absolute_calibration_gap": float(abs(group[score_column].mean() - group[label_column].mean())),
            }
        )
    return pd.DataFrame(rows)


def subgroup_table(df: pd.DataFrame, score_column: str, label_column: str) -> pd.DataFrame:
    rows = []
    for group_var in ["sector", "region"]:
        for group_value, group in df.groupby(group_var):
            metrics = prediction_metrics(group[label_column].to_numpy(dtype=float), group[score_column].to_numpy(dtype=float))
            rows.append(
                {
                    "group_variable": group_var,
                    "group_value": group_value,
                    "n": int(len(group)),
                    **metrics,
                }
            )
    return pd.DataFrame(rows)


def feature_stability(train_df: pd.DataFrame, cv_results: pd.DataFrame) -> pd.DataFrame:
    best_type = str(cv_results.iloc[0]["model_type"])
    best_penalty = float(cv_results.iloc[0]["penalty"])
    folds = make_folds(train_df)
    selected: dict[str, int] = {}
    for fold in sorted(set(folds)):
        fit_df = train_df.iloc[folds != fold]
        fold_spec = make_feature_spec(fit_df)
        x_fit = transform_features(fit_df, fold_spec)
        y_fit = fit_df["technology_intensive"].to_numpy(dtype=float)
        intercept, beta = fit_regularized(x_fit, y_fit, best_type, best_penalty)
        del intercept
        for name, coefficient in zip(fold_spec.feature_names, beta):
            if abs(coefficient) > 1e-5:
                selected[name] = selected.get(name, 0) + 1
    rows = [
        {
            "feature": name,
            "selection_rate_across_folds": count / len(set(folds)),
            "selected_folds": count,
        }
        for name, count in selected.items()
    ]
    return pd.DataFrame(rows).sort_values(
        ["selection_rate_across_folds", "feature"],
        ascending=[False, True],
    )


def write_calibration_plot(calibration: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    ax.plot([0, 1], [0, 1], color="0.45", linestyle="--", linewidth=1.0, label="perfect calibration")
    ax.scatter(calibration["mean_score"], calibration["realized_rate"], s=70, color="#2b6cb0")
    for _, row in calibration.iterrows():
        ax.annotate(str(int(row["n"])), (row["mean_score"], row["realized_rate"]), xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel("Mean predicted score")
    ax.set_ylabel("Realized technology-intensive rate")
    ax.set_title("Calibration on held-out postings")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def run(input_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    df = split_train_test(pd.read_csv(input_path))
    train_df = df[df["split"] == "train"].reset_index(drop=True)
    test_df = df[df["split"] == "test"].reset_index(drop=True)

    spec = make_feature_spec(train_df)
    del spec
    cv_results = cross_validate(train_df, make_feature_spec(train_df))
    cv_results.to_csv(outdir / "cv_results.csv", index=False)

    best_model = fit_from_cv(train_df, cv_results)
    model_rows = []
    for label, score_train, score_test in [
        (
            "majority_probability",
            np.full(len(train_df), train_df["technology_intensive"].mean()),
            np.full(len(test_df), train_df["technology_intensive"].mean()),
        ),
        ("keyword_rule", keyword_scores(train_df), keyword_scores(test_df)),
    ]:
        row: dict[str, float | str] = {"model": label, "model_type": "baseline", "penalty": 0.0}
        row.update(prediction_metrics(train_df["technology_intensive"].to_numpy(dtype=float), score_train, prefix="train"))
        row.update(prediction_metrics(test_df["technology_intensive"].to_numpy(dtype=float), score_test, prefix="test"))
        row["nonzero_features"] = 0.0
        model_rows.append(row)

    for model_type in ["ridge", "lasso", "elastic_net"]:
        model = fit_from_cv(train_df, cv_results, model_type=model_type)
        train_scores = predict_scores(model, train_df)
        test_scores = predict_scores(model, test_df)
        row = {"model": f"best_{model_type}", "model_type": model.model_type, "penalty": model.penalty}
        row.update(prediction_metrics(train_df["technology_intensive"].to_numpy(dtype=float), train_scores, prefix="train"))
        row.update(prediction_metrics(test_df["technology_intensive"].to_numpy(dtype=float), test_scores, prefix="test"))
        row["nonzero_features"] = float(np.sum(np.abs(model.beta) > 1e-5))
        model_rows.append(row)
    pd.DataFrame(model_rows).to_csv(outdir / "train_test_metrics.csv", index=False)

    test_scores = predict_scores(best_model, test_df)
    train_scores = predict_scores(best_model, train_df)
    scores_df = pd.concat(
        [
            train_df.assign(predicted_score=train_scores),
            test_df.assign(predicted_score=test_scores),
        ],
        ignore_index=True,
    )
    scores_df["predicted_label"] = (scores_df["predicted_score"] >= 0.5).astype(int)
    scores_df[
        [
            "posting_id",
            "split",
            "year",
            "sector",
            "region",
            "technology_intensive",
            "predicted_score",
            "predicted_label",
        ]
    ].to_csv(outdir / "measurement_scores.csv", index=False)

    calibration = calibration_table(test_df.assign(predicted_score=test_scores), "predicted_score", "technology_intensive")
    calibration.to_csv(outdir / "calibration_by_bin.csv", index=False)
    write_calibration_plot(calibration, outdir / "calibration_by_bin.png")

    subgroup_table(test_df.assign(predicted_score=test_scores), "predicted_score", "technology_intensive").to_csv(
        outdir / "subgroup_performance.csv",
        index=False,
    )

    weights = pd.DataFrame(
        {
            "feature": best_model.feature_spec.feature_names,
            "coefficient": best_model.beta,
            "abs_coefficient": np.abs(best_model.beta),
        }
    ).sort_values("abs_coefficient", ascending=False)
    weights.head(30).to_csv(outdir / "top_feature_weights.csv", index=False)
    feature_stability(train_df, cv_results).head(40).to_csv(outdir / "feature_stability.csv", index=False)

    leakage = pd.DataFrame(
        [
            {
                "feature": "future_verified_skill_tag",
                "status": "excluded",
                "reason": "Post-outcome verification tag; including it would leak label information into the model.",
                "teaching_check": "Draw a timing diagram before feature construction.",
            },
            {
                "feature": "posting_text",
                "status": "included",
                "reason": "Observed at vacancy posting time and central to the economic measurement task.",
                "teaching_check": "Audit whether later edits or platform metadata were appended after outcomes.",
            },
        ]
    )
    leakage.to_csv(outdir / "leakage_audit.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "step": "reproduce",
                "prompt": "Define the technology-intensive target and explain why test Brier loss is the main tuning metric.",
            },
            {
                "step": "diagnose",
                "prompt": "Use calibration and subgroup tables to decide whether the score is fit for a regional labor-demand study.",
            },
            {
                "step": "transfer",
                "prompt": "Predict how performance will change when the model is applied to short occupation titles.",
            },
        ]
    )
    prompts.to_csv(outdir / "diagnostic_prompts.csv", index=False)

    print(f"Best model: {best_model.model_type} with penalty {best_model.penalty}")
    print(f"Wrote outputs to {outdir}")


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
