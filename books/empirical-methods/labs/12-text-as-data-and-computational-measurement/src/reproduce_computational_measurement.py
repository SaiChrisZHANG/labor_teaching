"""Run the Week 12 text-as-measurement teaching path."""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


REMOTE_NARROW = [
    "remote work",
    "work from home",
    "home office",
    "flexible location",
]

REMOTE_BROAD = [
    "remote work",
    "work from home",
    "home office",
    "flexible location",
    "distributed team",
    "virtual meetings",
    "asynchronous communication",
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


def dictionary_score(text: str, phrases: list[str] = REMOTE_BROAD) -> float:
    tokens = tokenize(text)
    if not tokens:
        return 0.0
    count = phrase_count(text, phrases)
    return min(1.0, count / 3.0)


def dictionary_share(text: str, phrases: list[str] = REMOTE_BROAD) -> float:
    tokens = tokenize(text)
    if not tokens:
        return 0.0
    return phrase_count(text, phrases) / len(tokens)


def stable_noise(token: str) -> np.ndarray:
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    raw = np.frombuffer(digest[:12], dtype=np.uint32).astype(float)
    return (raw / np.iinfo(np.uint32).max - 0.5) * 0.08


def token_vector(token: str) -> np.ndarray:
    vector = stable_noise(token)
    if token in REMOTE_WORDS:
        vector += np.array([1.0, 0.20, 0.05])
    if token in ONSITE_WORDS:
        vector += np.array([-0.90, 0.05, 0.15])
    if token in DIGITAL_WORDS:
        vector += np.array([0.20, 0.85, 0.10])
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
    numeric["dictionary_broad"] = df[text_column].fillna("").map(lambda value: dictionary_score(str(value), REMOTE_BROAD))
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
    rng = np.random.default_rng(1248)
    split = np.array(["train"] * len(df), dtype=object)
    for label in [0, 1]:
        idx = np.where(df["remote_label"].to_numpy() == label)[0]
        shuffled = rng.permutation(idx)
        n_test = int(round(0.20 * len(shuffled)))
        n_validation = int(round(0.20 * len(shuffled)))
        split[shuffled[:n_test]] = "test"
        split[shuffled[n_test : n_test + n_validation]] = "validation"
    out = df.copy()
    out["split"] = split
    return out


def metrics(y_true: np.ndarray, scores: np.ndarray) -> dict[str, float]:
    predicted = (scores >= 0.5).astype(int)
    tp = float(np.sum((predicted == 1) & (y_true == 1)))
    fp = float(np.sum((predicted == 1) & (y_true == 0)))
    fn = float(np.sum((predicted == 0) & (y_true == 1)))
    tn = float(np.sum((predicted == 0) & (y_true == 0)))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return {
        "n": float(len(y_true)),
        "brier": float(np.mean((y_true - scores) ** 2)),
        "mae": float(np.mean(np.abs(y_true - scores))),
        "accuracy": float(np.mean(predicted == y_true)),
        "precision": precision,
        "recall": recall,
        "false_positive_rate": fp / (fp + tn) if fp + tn else 0.0,
        "false_negative_rate": fn / (fn + tp) if fn + tp else 0.0,
        "positive_prediction_rate": float(np.mean(predicted)),
    }


def cross_validate(train_df: pd.DataFrame, validation_df: pd.DataFrame) -> pd.DataFrame:
    penalties = [0.005, 0.01, 0.05, 0.10, 0.25, 0.50, 1.0]
    rows: list[dict[str, float]] = []
    for penalty in penalties:
        spec = make_feature_spec(train_df)
        x_train = transform_features(train_df, spec)
        y_train = train_df["remote_label"].to_numpy(dtype=float)
        intercept, beta = fit_ridge(x_train, y_train, penalty)
        model = FittedModel(penalty, intercept, beta, spec)
        validation_scores = predict_scores(model, validation_df)
        y_validation = validation_df["remote_label"].to_numpy(dtype=float)
        row = {"penalty": penalty}
        row.update(metrics(y_validation, validation_scores))
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["brier", "penalty"]).reset_index(drop=True)


def fit_final_model(train_validation_df: pd.DataFrame, penalty: float) -> FittedModel:
    spec = make_feature_spec(train_validation_df)
    x = transform_features(train_validation_df, spec)
    y = train_validation_df["remote_label"].to_numpy(dtype=float)
    intercept, beta = fit_ridge(x, y, penalty)
    return FittedModel(penalty, intercept, beta, spec)


def method_scores(model: FittedModel, df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["dictionary_narrow_score"] = out["posting_text"].map(lambda text: dictionary_score(str(text), REMOTE_NARROW))
    out["dictionary_broad_score"] = out["posting_text"].map(lambda text: dictionary_score(str(text), REMOTE_BROAD))
    out["dictionary_broad_share"] = out["posting_text"].map(lambda text: dictionary_share(str(text), REMOTE_BROAD))
    out["embedding_similarity_score"] = out["posting_text"].map(embedding_similarity_score)
    out["supervised_score"] = predict_scores(model, out)
    out["constructed_measure"] = (
        0.55 * out["supervised_score"]
        + 0.25 * out["dictionary_broad_score"]
        + 0.20 * out["embedding_similarity_score"]
    ).clip(0.0, 1.0)
    return out


def classification_table(scored: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    methods = {
        "dictionary_narrow": "dictionary_narrow_score",
        "dictionary_broad": "dictionary_broad_score",
        "embedding_similarity": "embedding_similarity_score",
        "supervised_ridge": "supervised_score",
        "constructed_measure": "constructed_measure",
    }
    for split, group in scored.groupby("split"):
        y = group["remote_label"].to_numpy(dtype=float)
        for method, score_col in methods.items():
            row: dict[str, float | str] = {"split": str(split), "method": method}
            row.update(metrics(y, group[score_col].to_numpy(dtype=float)))
            rows.append(row)
    return pd.DataFrame(rows)


def subgroup_error(scored: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    test = scored[scored["split"] == "test"].copy()
    for group_var in ["sector", "region", "job_family"]:
        for group_value, group in test.groupby(group_var):
            y = group["remote_label"].to_numpy(dtype=float)
            score = group["supervised_score"].to_numpy(dtype=float)
            row: dict[str, float | str] = {
                "group_variable": group_var,
                "group_value": str(group_value),
                "n": float(len(group)),
                "mean_true_remote": float(y.mean()),
                "mean_supervised_score": float(score.mean()),
                "mean_absolute_error": float(np.mean(np.abs(y - score))),
            }
            row.update(metrics(y, score))
            rows.append(row)
    return pd.DataFrame(rows).sort_values(["mean_absolute_error", "group_variable"], ascending=[False, True])


def dictionary_sensitivity(scored: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    test = scored[scored["split"] == "test"].copy()
    y = test["remote_label"].to_numpy(dtype=float)
    for name, phrases, score_col in [
        ("narrow_dictionary", REMOTE_NARROW, "dictionary_narrow_score"),
        ("broad_dictionary", REMOTE_BROAD, "dictionary_broad_score"),
    ]:
        row: dict[str, float | str] = {
            "dictionary": name,
            "phrase_count": float(len(phrases)),
            "phrases": "; ".join(phrases),
        }
        row.update(metrics(y, test[score_col].to_numpy(dtype=float)))
        rows.append(row)
    return pd.DataFrame(rows)


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
    true_x = scored["remote_label"].to_numpy(dtype=float)
    _, true_slope = simple_slope(y, true_x)
    rows = []
    for measure, column in [
        ("true_remote_label", "remote_label"),
        ("dictionary_broad_score", "dictionary_broad_score"),
        ("embedding_similarity_score", "embedding_similarity_score"),
        ("supervised_score", "supervised_score"),
        ("constructed_measure", "constructed_measure"),
    ]:
        x = scored[column].to_numpy(dtype=float)
        intercept, slope = simple_slope(y, x)
        rows.append(
            {
                "measure": measure,
                "intercept": intercept,
                "slope": slope,
                "slope_relative_to_true_label": slope / true_slope if abs(true_slope) > 1e-12 else np.nan,
                "mean_measure": float(x.mean()),
                "sd_measure": float(x.std(ddof=1)),
            }
        )
    return pd.DataFrame(rows)


def top_terms(model: FittedModel) -> pd.DataFrame:
    weights = pd.DataFrame(
        {
            "feature": model.feature_spec.feature_names,
            "coefficient": model.beta,
            "abs_coefficient": np.abs(model.beta),
        }
    )
    return weights.sort_values(["abs_coefficient", "feature"], ascending=[False, True]).head(35)


def leakage_audit() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "feature": "future_remote_badge",
                "status": "excluded",
                "reason": "Generated after the posting and too close to the label; using it would leak future platform information.",
                "teaching_check": "Draw a timing diagram before feature construction.",
            },
            {
                "feature": "posting_text",
                "status": "included",
                "reason": "Observed at the vacancy-posting stage and central to the measurement problem.",
                "teaching_check": "Audit whether platform edits or later metadata were appended after outcomes.",
            },
            {
                "feature": "sector, region, job_family, year, firm_size",
                "status": "included",
                "reason": "Pre-measurement context that may improve classification but can also encode subgroup shortcuts.",
                "teaching_check": "Report subgroup performance and try text-only sensitivity checks in a real project.",
            },
        ]
    )


def diagnostic_prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "step": "reproduce",
                "prompt": "Define whether the target is explicit remote permission, task portability, hybrid flexibility, or a broader remote-work feasibility object.",
            },
            {
                "step": "diagnose",
                "prompt": "Use subgroup measurement error to decide where the score would be weakest in a labor-market comparison.",
            },
            {
                "step": "diagnose",
                "prompt": "Compare downstream slopes using the true label and constructed measures. What does this imply about measurement error?",
            },
            {
                "step": "transfer",
                "prompt": "Predict which terms and modalities will fail when the workflow moves away from job postings.",
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

    scored = method_scores(model, df)
    scored[
        [
            "posting_id",
            "split",
            "year",
            "sector",
            "region",
            "job_family",
            "remote_label",
            "dictionary_narrow_score",
            "dictionary_broad_score",
            "dictionary_broad_share",
            "embedding_similarity_score",
            "supervised_score",
            "constructed_measure",
            "applicant_interest",
        ]
    ].to_csv(outdir / "remote_measure_scores.csv", index=False)

    classification_table(scored).to_csv(outdir / "classification_metrics.csv", index=False)
    subgroup_error(scored).to_csv(outdir / "subgroup_measurement_error.csv", index=False)
    dictionary_sensitivity(scored).to_csv(outdir / "dictionary_sensitivity.csv", index=False)
    downstream_table(scored).to_csv(outdir / "measurement_error_downstream.csv", index=False)
    top_terms(model).to_csv(outdir / "top_terms.csv", index=False)
    leakage_audit().to_csv(outdir / "leakage_audit.csv", index=False)
    diagnostic_prompts().to_csv(outdir / "diagnostic_prompts.csv", index=False)

    print(f"Selected ridge penalty: {best_penalty}")
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
