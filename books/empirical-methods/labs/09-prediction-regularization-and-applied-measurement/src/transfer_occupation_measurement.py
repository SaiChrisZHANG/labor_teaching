"""Transfer the Week 9 posting classifier to occupation-title measurement."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from reproduce_prediction_measurement import (
    calibration_table,
    cross_validate,
    fit_from_cv,
    keyword_scores,
    make_feature_spec,
    predict_scores,
    prediction_metrics,
    subgroup_table,
    tokenize,
    write_calibration_plot,
)


def vocabulary_coverage(titles: pd.DataFrame, vocabulary: list[str]) -> pd.DataFrame:
    vocab = set(vocabulary)
    rows = []
    for _, row in titles.iterrows():
        tokens = tokenize(str(row["raw_title"]))
        covered = [token for token in tokens if token in vocab]
        rows.append(
            {
                "title_id": int(row["title_id"]),
                "raw_title": row["raw_title"],
                "token_count": len(tokens),
                "covered_token_count": len(covered),
                "coverage_rate": len(covered) / len(tokens) if tokens else 0.0,
                "technology_occupation": int(row["technology_occupation"]),
                "sector": row["sector"],
                "region": row["region"],
            }
        )
    return pd.DataFrame(rows)


def confusion_matrix(y_true: np.ndarray, scores: np.ndarray) -> pd.DataFrame:
    predictions = (scores >= 0.5).astype(int)
    rows = []
    for actual in [0, 1]:
        for predicted in [0, 1]:
            rows.append(
                {
                    "actual": actual,
                    "predicted": predicted,
                    "count": int(np.sum((y_true == actual) & (predictions == predicted))),
                }
            )
    return pd.DataFrame(rows)


def run(train_input: Path, transfer_input: Path, outdir: Path, reproduced_outdir: Path | None = None) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    postings = pd.read_csv(train_input)
    titles = pd.read_csv(transfer_input)

    cv_results = cross_validate(postings, make_feature_spec(postings))
    model = fit_from_cv(postings, cv_results)

    transfer_for_prediction = titles.copy()
    transfer_for_prediction["posting_text"] = transfer_for_prediction["raw_title"]
    transfer_for_prediction["firm_size"] = 100
    transfer_for_prediction["remote_signal"] = 0
    scores = predict_scores(model, transfer_for_prediction, text_column="posting_text")
    keyword = keyword_scores(transfer_for_prediction)
    y = titles["technology_occupation"].to_numpy(dtype=float)

    metric_rows = []
    for name, model_scores in [("posting_model_on_titles", scores), ("keyword_rule_on_titles", keyword)]:
        row = {
            "model": name,
            "training_object": "technology-intensive job posting",
            "transfer_object": "technology occupation from raw title",
        }
        row.update(prediction_metrics(y, model_scores))
        metric_rows.append(row)
    pd.DataFrame(metric_rows).to_csv(outdir / "transport_metrics.csv", index=False)

    scores_df = titles.copy()
    scores_df["predicted_score"] = scores
    scores_df["predicted_label"] = (scores >= 0.5).astype(int)
    scores_df.to_csv(outdir / "transfer_scores.csv", index=False)

    calibration = calibration_table(scores_df, "predicted_score", "technology_occupation")
    calibration.to_csv(outdir / "transfer_calibration_by_bin.csv", index=False)
    write_calibration_plot(calibration, outdir / "transfer_calibration_by_bin.png")
    subgroup_table(scores_df, "predicted_score", "technology_occupation").to_csv(
        outdir / "transport_subgroup_performance.csv",
        index=False,
    )
    confusion_matrix(y, scores).to_csv(outdir / "occupation_confusion_matrix.csv", index=False)
    vocabulary_coverage(titles, model.feature_spec.vocabulary).to_csv(outdir / "vocabulary_coverage.csv", index=False)

    if reproduced_outdir is not None:
        comparison_path = reproduced_outdir / "train_test_metrics.csv"
        if comparison_path.exists():
            comparison = pd.read_csv(comparison_path)
            best_row = comparison.loc[comparison["model"] == f"best_{model.model_type}"].copy()
            if not best_row.empty:
                best_row["comparison_note"] = "Original held-out posting performance for the same selected model."
                best_row.to_csv(outdir / "original_vs_transfer_reference.csv", index=False)

    prompts = pd.DataFrame(
        [
            {
                "prompt": "Which title tokens were not covered by the posting vocabulary, and why does that matter for transportability?",
            },
            {
                "prompt": "Would the title classifier be good enough for a study of occupational mobility by region?",
            },
            {
                "prompt": "What human validation sample would you collect before using these labels in a downstream design?",
            },
            {
                "prompt": "How would the conclusion change if false positives were more costly than false negatives?",
            },
        ]
    )
    prompts.to_csv(outdir / "transfer_design_prompts.csv", index=False)

    print(f"Transfer model: {model.model_type} with penalty {model.penalty}")
    print(f"Wrote outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-input", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--reproduced-outdir", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.train_input, args.input, args.outdir, args.reproduced_outdir)


if __name__ == "__main__":
    main()
