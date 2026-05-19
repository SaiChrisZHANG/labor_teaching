"""Run the Week 13 validation teaching path on synthetic source data."""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


REMOTE_TERMS = [
    "remote work",
    "work from home",
    "distributed team",
    "virtual meetings",
    "home office",
    "asynchronous communication",
    "flexible location",
    "hybrid schedule",
    "secure video calls",
]

REMOTE_WORDS = {
    "remote",
    "home",
    "distributed",
    "virtual",
    "hybrid",
    "asynchronous",
    "flexible",
    "video",
    "online",
}

ONSITE_WORDS = {
    "onsite",
    "site",
    "presence",
    "floor",
    "desk",
    "field",
    "warehouse",
    "storefront",
    "physical",
    "person",
    "counter",
}

DIGITAL_WORDS = {
    "cloud",
    "data",
    "software",
    "dashboard",
    "dashboards",
    "documentation",
    "workflow",
    "tools",
    "records",
    "calls",
}

STOP_WORDS = {
    "the",
    "and",
    "with",
    "for",
    "role",
    "this",
    "that",
    "through",
    "candidates",
    "managers",
    "teams",
    "supports",
}


@dataclass
class FeatureSpec:
    vocabulary: list[str]
    feature_names: list[str]
    means: np.ndarray
    scales: np.ndarray
    sector_levels: list[str]
    region_levels: list[str]
    job_family_levels: list[str]


@dataclass
class FittedModel:
    penalty: float
    intercept: float
    beta: np.ndarray
    feature_spec: FeatureSpec


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z0-9]+", str(text).lower())


def phrase_count(text: str, phrases: list[str]) -> int:
    lowered = str(text).lower()
    return sum(len(re.findall(rf"\b{re.escape(phrase)}\b", lowered)) for phrase in phrases)


def dictionary_score(text: str, phrases: list[str] = REMOTE_TERMS) -> float:
    return float(np.clip(phrase_count(text, phrases) / 3.0, 0.0, 1.0))


def stable_noise(token: str) -> np.ndarray:
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    raw = np.frombuffer(digest[:12], dtype=np.uint32).astype(float)
    return (raw / np.iinfo(np.uint32).max - 0.5) * 0.08


def token_vector(token: str) -> np.ndarray:
    vector = stable_noise(token)
    if token in REMOTE_WORDS:
        vector += np.array([1.0, 0.18, 0.05])
    if token in ONSITE_WORDS:
        vector += np.array([-0.90, 0.04, 0.12])
    if token in DIGITAL_WORDS:
        vector += np.array([0.20, 0.82, 0.10])
    return vector


def document_vector(text: str) -> np.ndarray:
    tokens = tokenize(text)
    if not tokens:
        return np.zeros(3, dtype=float)
    return np.vstack([token_vector(token) for token in tokens]).mean(axis=0)


def embedding_similarity_score(text: str) -> float:
    reference = np.vstack([token_vector(token) for token in sorted(REMOTE_WORDS)]).mean(axis=0)
    doc = document_vector(text)
    denom = float(np.linalg.norm(reference) * np.linalg.norm(doc))
    if denom < 1e-12:
        return 0.0
    cosine = float(np.dot(reference, doc) / denom)
    return float(np.clip((cosine + 1.0) / 2.0, 0.0, 1.0))


def build_vocabulary(texts: pd.Series, min_count: int = 2) -> list[str]:
    counts: dict[str, int] = {}
    for text in texts.fillna(""):
        for token in set(tokenize(str(text))):
            if token not in STOP_WORDS:
                counts[token] = counts.get(token, 0) + 1
    return sorted([token for token, count in counts.items() if count >= min_count])


def design_matrix(
    df: pd.DataFrame,
    vocabulary: list[str],
    sector_levels: list[str],
    region_levels: list[str],
    job_family_levels: list[str],
    text_column: str = "posting_text",
) -> tuple[np.ndarray, list[str]]:
    parts: list[np.ndarray] = []
    names: list[str] = []

    token_index = {token: idx for idx, token in enumerate(vocabulary)}
    text_matrix = np.zeros((len(df), len(vocabulary)), dtype=float)
    for row_idx, text in enumerate(df[text_column].fillna("")):
        for token in tokenize(str(text)):
            if token in token_index:
                text_matrix[row_idx, token_index[token]] += 1.0
    if vocabulary:
        parts.append(text_matrix)
        names.extend([f"text:{token}" for token in vocabulary])

    numeric = pd.DataFrame(index=df.index)
    numeric["year_centered"] = df.get("year", pd.Series(2023, index=df.index)).astype(float) - 2023.0
    numeric["log_firm_size"] = np.log(df.get("firm_size", pd.Series(100, index=df.index)).astype(float))
    numeric["dictionary_score"] = df[text_column].fillna("").map(lambda value: dictionary_score(str(value)))
    numeric["embedding_similarity"] = df[text_column].fillna("").map(embedding_similarity_score)
    parts.append(numeric.to_numpy(dtype=float))
    names.extend(list(numeric.columns))

    for sector in sector_levels:
        parts.append((df.get("sector", pd.Series("", index=df.index)) == sector).to_numpy(dtype=float).reshape(-1, 1))
        names.append(f"sector:{sector}")
    for region in region_levels:
        parts.append((df.get("region", pd.Series("", index=df.index)) == region).to_numpy(dtype=float).reshape(-1, 1))
        names.append(f"region:{region}")
    for family in job_family_levels:
        parts.append((df.get("job_family", pd.Series("", index=df.index)) == family).to_numpy(dtype=float).reshape(-1, 1))
        names.append(f"job_family:{family}")

    return np.column_stack(parts), names


def make_feature_spec(train_df: pd.DataFrame, text_column: str = "posting_text") -> FeatureSpec:
    vocabulary = build_vocabulary(train_df[text_column])
    sector_levels = sorted(train_df["sector"].dropna().unique().tolist())
    region_levels = sorted(train_df["region"].dropna().unique().tolist())
    job_family_levels = sorted(train_df["job_family"].dropna().unique().tolist())
    x_raw, names = design_matrix(train_df, vocabulary, sector_levels, region_levels, job_family_levels, text_column)
    means = x_raw.mean(axis=0)
    scales = x_raw.std(axis=0)
    scales[scales < 1e-8] = 1.0
    return FeatureSpec(vocabulary, names, means, scales, sector_levels, region_levels, job_family_levels)


def transform_features(df: pd.DataFrame, spec: FeatureSpec, text_column: str = "posting_text") -> np.ndarray:
    x_raw, names = design_matrix(
        df,
        spec.vocabulary,
        spec.sector_levels,
        spec.region_levels,
        spec.job_family_levels,
        text_column,
    )
    if names != spec.feature_names:
        raise ValueError("Feature names changed between training and prediction.")
    return (x_raw - spec.means) / spec.scales


def fit_ridge(x: np.ndarray, y: np.ndarray, penalty: float) -> tuple[float, np.ndarray]:
    intercept = float(y.mean())
    centered = y - intercept
    gram = (x.T @ x) / x.shape[0]
    rhs = (x.T @ centered) / x.shape[0]
    beta = np.linalg.solve(gram + penalty * np.eye(x.shape[1]), rhs)
    return intercept, beta


def predict_scores(model: FittedModel, df: pd.DataFrame, text_column: str = "posting_text") -> np.ndarray:
    x = transform_features(df, model.feature_spec, text_column)
    return np.clip(model.intercept + x @ model.beta, 0.0, 1.0)


def split_data(df: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(13131)
    split = np.array(["train"] * len(df), dtype=object)
    for label in [0, 1]:
        idx = np.where(df["benchmark_label"].to_numpy() == label)[0]
        shuffled = rng.permutation(idx)
        n_test = int(round(0.20 * len(shuffled)))
        n_validation = int(round(0.20 * len(shuffled)))
        split[shuffled[:n_test]] = "test"
        split[shuffled[n_test : n_test + n_validation]] = "validation"
    out = df.copy()
    out["split"] = split
    return out


def metrics(y_true: np.ndarray, scores: np.ndarray, threshold: float = 0.5) -> dict[str, float]:
    predicted = (scores >= threshold).astype(int)
    tp = float(np.sum((predicted == 1) & (y_true == 1)))
    fp = float(np.sum((predicted == 1) & (y_true == 0)))
    fn = float(np.sum((predicted == 0) & (y_true == 1)))
    tn = float(np.sum((predicted == 0) & (y_true == 0)))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "n": float(len(y_true)),
        "threshold": float(threshold),
        "brier": float(np.mean((y_true - scores) ** 2)),
        "mae": float(np.mean(np.abs(y_true - scores))),
        "accuracy": float(np.mean(predicted == y_true)),
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_positive_rate": fp / (fp + tn) if fp + tn else 0.0,
        "false_negative_rate": fn / (fn + tp) if fn + tp else 0.0,
        "positive_prediction_rate": float(np.mean(predicted)),
    }


def cohen_kappa(a: np.ndarray, b: np.ndarray) -> dict[str, float]:
    a = a.astype(int)
    b = b.astype(int)
    observed = float(np.mean(a == b))
    p_yes = float(a.mean() * b.mean())
    p_no = float((1 - a.mean()) * (1 - b.mean()))
    expected = p_yes + p_no
    kappa = (observed - expected) / (1 - expected) if abs(1 - expected) > 1e-12 else np.nan
    return {
        "n": float(len(a)),
        "observed_agreement": observed,
        "expected_agreement": expected,
        "cohens_kappa": float(kappa),
        "rater_a_positive_rate": float(a.mean()),
        "rater_b_positive_rate": float(b.mean()),
    }


def cross_validate(train_df: pd.DataFrame, validation_df: pd.DataFrame) -> pd.DataFrame:
    penalties = [0.005, 0.01, 0.05, 0.10, 0.25, 0.50, 1.0]
    rows: list[dict[str, float]] = []
    for penalty in penalties:
        spec = make_feature_spec(train_df)
        x_train = transform_features(train_df, spec)
        y_train = train_df["benchmark_label"].to_numpy(dtype=float)
        intercept, beta = fit_ridge(x_train, y_train, penalty)
        model = FittedModel(penalty, intercept, beta, spec)
        validation_scores = predict_scores(model, validation_df)
        y_validation = validation_df["benchmark_label"].to_numpy(dtype=float)
        row = {"penalty": penalty}
        row.update(metrics(y_validation, validation_scores))
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["brier", "penalty"]).reset_index(drop=True)


def fit_final_model(train_validation_df: pd.DataFrame, penalty: float) -> FittedModel:
    spec = make_feature_spec(train_validation_df)
    x = transform_features(train_validation_df, spec)
    y = train_validation_df["benchmark_label"].to_numpy(dtype=float)
    intercept, beta = fit_ridge(x, y, penalty)
    return FittedModel(penalty, intercept, beta, spec)


def score_methods(model: FittedModel, df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["dictionary_score"] = out["posting_text"].map(lambda text: dictionary_score(str(text)))
    out["embedding_similarity_score"] = out["posting_text"].map(embedding_similarity_score)
    out["supervised_score"] = predict_scores(model, out)
    out["constructed_validation_score"] = (
        0.60 * out["supervised_score"]
        + 0.20 * out["dictionary_score"]
        + 0.20 * out["embedding_similarity_score"]
    ).clip(0.0, 1.0)
    return out


def classification_metrics(scored: pd.DataFrame) -> pd.DataFrame:
    methods = {
        "dictionary": "dictionary_score",
        "embedding_similarity": "embedding_similarity_score",
        "supervised_baseline": "supervised_score",
        "constructed_validation_score": "constructed_validation_score",
    }
    rows: list[dict[str, float | str]] = []
    for split, group in scored.groupby("split"):
        y = group["benchmark_label"].to_numpy(dtype=float)
        for method, score_col in methods.items():
            row: dict[str, float | str] = {"split": str(split), "method": method}
            row.update(metrics(y, group[score_col].to_numpy(dtype=float)))
            rows.append(row)
    return pd.DataFrame(rows)


def confusion_matrix(scored: pd.DataFrame) -> pd.DataFrame:
    methods = {
        "dictionary": "dictionary_score",
        "embedding_similarity": "embedding_similarity_score",
        "supervised_baseline": "supervised_score",
        "constructed_validation_score": "constructed_validation_score",
    }
    test = scored[scored["split"] == "test"]
    rows: list[dict[str, int | str]] = []
    for method, score_col in methods.items():
        predicted = (test[score_col].to_numpy(dtype=float) >= 0.5).astype(int)
        actual = test["benchmark_label"].to_numpy(dtype=int)
        for actual_value in [0, 1]:
            for predicted_value in [0, 1]:
                rows.append(
                    {
                        "method": method,
                        "actual": actual_value,
                        "predicted": predicted_value,
                        "count": int(np.sum((actual == actual_value) & (predicted == predicted_value))),
                    }
                )
    return pd.DataFrame(rows)


def calibration_by_bin(scored: pd.DataFrame) -> pd.DataFrame:
    methods = {
        "embedding_similarity": "embedding_similarity_score",
        "supervised_baseline": "supervised_score",
        "constructed_validation_score": "constructed_validation_score",
    }
    bins = np.linspace(0.0, 1.0, 6)
    rows: list[dict[str, float | str]] = []
    for split, group in scored.groupby("split"):
        y = group["benchmark_label"].to_numpy(dtype=float)
        for method, score_col in methods.items():
            scores = group[score_col].to_numpy(dtype=float)
            bin_ids = np.digitize(scores, bins, right=True)
            bin_ids = np.clip(bin_ids, 1, len(bins) - 1)
            for bin_id in range(1, len(bins)):
                mask = bin_ids == bin_id
                if not np.any(mask):
                    continue
                rows.append(
                    {
                        "split": str(split),
                        "method": method,
                        "bin_lower": float(bins[bin_id - 1]),
                        "bin_upper": float(bins[bin_id]),
                        "n": float(mask.sum()),
                        "mean_score": float(scores[mask].mean()),
                        "mean_label": float(y[mask].mean()),
                        "calibration_error": float(scores[mask].mean() - y[mask].mean()),
                    }
                )
    return pd.DataFrame(rows)


def subgroup_performance(scored: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    test = scored[scored["split"] == "test"].copy()
    for group_var in ["sector", "region", "job_family", "year"]:
        for group_value, group in test.groupby(group_var):
            y = group["benchmark_label"].to_numpy(dtype=float)
            score = group["supervised_score"].to_numpy(dtype=float)
            row: dict[str, float | str] = {
                "group_variable": group_var,
                "group_value": str(group_value),
                "mean_benchmark": float(y.mean()),
                "mean_score": float(score.mean()),
            }
            row.update(metrics(y, score))
            rows.append(row)
    return pd.DataFrame(rows).sort_values(["false_negative_rate", "false_positive_rate"], ascending=False)


def threshold_sensitivity(scored: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    for split_name in ["validation", "test"]:
        group = scored[scored["split"] == split_name]
        y = group["benchmark_label"].to_numpy(dtype=float)
        scores = group["supervised_score"].to_numpy(dtype=float)
        for threshold in [0.30, 0.40, 0.50, 0.60, 0.70]:
            row: dict[str, float | str] = {"split": split_name}
            row.update(metrics(y, scores, threshold=threshold))
            rows.append(row)
    return pd.DataFrame(rows)


def corr(x: np.ndarray, y: np.ndarray) -> float:
    if float(np.std(x)) < 1e-12 or float(np.std(y)) < 1e-12:
        return np.nan
    return float(np.corrcoef(x, y)[0, 1])


def external_validation(scored: pd.DataFrame) -> pd.DataFrame:
    methods = {
        "dictionary": "dictionary_score",
        "embedding_similarity": "embedding_similarity_score",
        "supervised_baseline": "supervised_score",
        "constructed_validation_score": "constructed_validation_score",
    }
    rows: list[dict[str, float | str]] = []
    test = scored[scored["split"] == "test"].copy()
    audit = test["external_remote_audit"].to_numpy(dtype=float)
    truth = test["simulation_truth_label"].to_numpy(dtype=float)
    for method, column in methods.items():
        score = test[column].to_numpy(dtype=float)
        row: dict[str, float | str] = {"method": method}
        row["correlation_with_external_audit"] = corr(score, audit)
        row["correlation_with_simulation_truth"] = corr(score, truth)
        row["mean_absolute_error_to_external_audit"] = float(np.mean(np.abs(score - audit)))
        rows.append(row)
    return pd.DataFrame(rows).sort_values("mean_absolute_error_to_external_audit")


def error_audit(scored: pd.DataFrame) -> pd.DataFrame:
    test = scored[scored["split"] == "test"].copy()
    test["predicted_label"] = (test["supervised_score"] >= 0.5).astype(int)
    test["error_type"] = "correct"
    test.loc[(test["predicted_label"] == 1) & (test["benchmark_label"] == 0), "error_type"] = "false_positive"
    test.loc[(test["predicted_label"] == 0) & (test["benchmark_label"] == 1), "error_type"] = "false_negative"
    errors = test[test["error_type"] != "correct"].copy()
    errors["confidence_gap"] = np.abs(errors["supervised_score"] - 0.5)
    keep = [
        "posting_id",
        "error_type",
        "sector",
        "region",
        "job_family",
        "benchmark_label",
        "simulation_truth_label",
        "supervised_score",
        "dictionary_score",
        "embedding_similarity_score",
        "posting_text",
        "confidence_gap",
    ]
    return errors.sort_values("confidence_gap", ascending=False)[keep].head(25)


def simple_slope(y: np.ndarray, x: np.ndarray) -> tuple[float, float]:
    x_mean = float(x.mean())
    y_mean = float(y.mean())
    denom = float(np.sum((x - x_mean) ** 2))
    if denom < 1e-12:
        return y_mean, 0.0
    slope = float(np.sum((x - x_mean) * (y - y_mean)) / denom)
    intercept = y_mean - slope * x_mean
    return intercept, slope


def downstream_table(scored: pd.DataFrame) -> pd.DataFrame:
    y = scored["applicant_interest"].to_numpy(dtype=float)
    true_x = scored["simulation_truth_label"].to_numpy(dtype=float)
    _, true_slope = simple_slope(y, true_x)
    rows = []
    for measure, column in [
        ("simulation_truth_label", "simulation_truth_label"),
        ("benchmark_label", "benchmark_label"),
        ("dictionary_score", "dictionary_score"),
        ("embedding_similarity_score", "embedding_similarity_score"),
        ("supervised_score", "supervised_score"),
        ("constructed_validation_score", "constructed_validation_score"),
    ]:
        x = scored[column].to_numpy(dtype=float)
        intercept, slope = simple_slope(y, x)
        rows.append(
            {
                "measure": measure,
                "intercept": intercept,
                "slope": slope,
                "slope_relative_to_simulation_truth": slope / true_slope if abs(true_slope) > 1e-12 else np.nan,
                "mean_measure": float(x.mean()),
                "sd_measure": float(x.std(ddof=1)),
            }
        )
    return pd.DataFrame(rows)


def diagnostic_prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "step": "reproduce",
                "prompt": "Define the benchmark and explain what inter-rater reliability does not prove.",
            },
            {
                "step": "diagnose",
                "prompt": "Use confusion matrices, calibration bins, and subgroup performance to identify where validation fails.",
            },
            {
                "step": "diagnose",
                "prompt": "Compare downstream slopes using the simulation truth, benchmark, and constructed scores.",
            },
            {
                "step": "transfer",
                "prompt": "Decide what must be relabeled before moving the validation workflow to a new domain.",
            },
        ]
    )


def run(input_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    df = split_data(pd.read_csv(input_path))
    train = df[df["split"] == "train"].reset_index(drop=True)
    validation = df[df["split"] == "validation"].reset_index(drop=True)
    train_validation = df[df["split"].isin(["train", "validation"])].reset_index(drop=True)

    cv = cross_validate(train, validation)
    cv.to_csv(outdir / "validation_metrics.csv", index=False)
    best_penalty = float(cv.iloc[0]["penalty"])
    model = fit_final_model(train_validation, best_penalty)
    scored = score_methods(model, df)

    scored[
        [
            "posting_id",
            "split",
            "year",
            "sector",
            "region",
            "job_family",
            "simulation_truth_label",
            "rater_a_label",
            "rater_b_label",
            "benchmark_label",
            "external_remote_audit",
            "dictionary_score",
            "embedding_similarity_score",
            "supervised_score",
            "constructed_validation_score",
            "applicant_interest",
        ]
    ].to_csv(outdir / "validation_scores.csv", index=False)

    reliability = cohen_kappa(
        scored["rater_a_label"].to_numpy(dtype=int),
        scored["rater_b_label"].to_numpy(dtype=int),
    )
    pd.DataFrame([reliability]).to_csv(outdir / "inter_rater_reliability.csv", index=False)
    classification_metrics(scored).to_csv(outdir / "classification_metrics.csv", index=False)
    confusion_matrix(scored).to_csv(outdir / "confusion_matrix.csv", index=False)
    calibration_by_bin(scored).to_csv(outdir / "calibration_by_bin.csv", index=False)
    subgroup_performance(scored).to_csv(outdir / "subgroup_performance.csv", index=False)
    threshold_sensitivity(scored).to_csv(outdir / "threshold_sensitivity.csv", index=False)
    external_validation(scored).to_csv(outdir / "external_validation.csv", index=False)
    error_audit(scored).to_csv(outdir / "error_audit.csv", index=False)
    downstream_table(scored).to_csv(outdir / "measurement_error_downstream.csv", index=False)
    diagnostic_prompts().to_csv(outdir / "diagnostic_prompts.csv", index=False)

    print(f"Selected ridge penalty: {best_penalty}")
    print(f"Wrote reproduced validation outputs to {outdir}")


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
