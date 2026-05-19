"""Transfer the Week 13 validation workflow to shifted synthetic data."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

from reproduce_validation_workflow import (
    REMOTE_TERMS,
    calibration_by_bin,
    classification_metrics,
    confusion_matrix,
    corr,
    cross_validate,
    dictionary_score,
    embedding_similarity_score,
    fit_final_model,
    metrics,
    predict_scores,
    split_data,
    tokenize,
)


def prepare_transfer_for_source_model(transfer: pd.DataFrame) -> pd.DataFrame:
    out = transfer.copy()
    out["posting_text"] = out["policy_text"]
    out["year"] = 2024
    out["firm_size"] = 180
    out["sector"] = out["organization_type"]
    out["job_family"] = "administration"
    return out


def score_transfer(model, transfer: pd.DataFrame) -> pd.DataFrame:
    model_ready = prepare_transfer_for_source_model(transfer)
    out = transfer.copy()
    out["source_text_score"] = predict_scores(model, model_ready)
    out["dictionary_score"] = out["policy_text"].map(lambda text: dictionary_score(str(text), REMOTE_TERMS))
    out["embedding_similarity_score"] = out["policy_text"].map(embedding_similarity_score)
    out["combined_transfer_score"] = (
        0.45 * out["source_text_score"]
        + 0.20 * out["dictionary_score"]
        + 0.15 * out["embedding_similarity_score"]
        + 0.20 * out["image_infrastructure_score"]
    ).clip(0.0, 1.0)
    return out


def vocabulary_shift(source_vocabulary: list[str], transfer_texts: pd.Series) -> pd.DataFrame:
    source = set(source_vocabulary)
    token_counter: Counter[str] = Counter()
    covered_counter: Counter[str] = Counter()
    for text in transfer_texts.fillna(""):
        tokens = tokenize(str(text))
        token_counter.update(tokens)
        covered_counter.update([token for token in tokens if token in source])
    total_tokens = sum(token_counter.values())
    covered_tokens = sum(covered_counter.values())
    top_uncovered = [
        f"{token}:{count}"
        for token, count in token_counter.most_common(30)
        if token not in source
    ][:12]
    return pd.DataFrame(
        [
            {
                "source_vocabulary_size": len(source),
                "transfer_token_count": total_tokens,
                "covered_token_count": covered_tokens,
                "coverage_rate": covered_tokens / total_tokens if total_tokens else 0.0,
                "top_uncovered_tokens": "; ".join(top_uncovered),
            }
        ]
    )


def transfer_metrics(scored: pd.DataFrame) -> pd.DataFrame:
    methods = {
        "source_text_score": "source_text_score",
        "dictionary": "dictionary_score",
        "embedding_similarity": "embedding_similarity_score",
        "image_proxy": "image_infrastructure_score",
        "combined_transfer_score": "combined_transfer_score",
    }
    y = scored["benchmark_label"].to_numpy(dtype=float)
    rows: list[dict[str, float | str]] = []
    for method, column in methods.items():
        row: dict[str, float | str] = {"domain": "transfer", "method": method}
        row.update(metrics(y, scored[column].to_numpy(dtype=float)))
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["brier", "method"]).reset_index(drop=True)


def source_vs_transfer_metrics(source_scored: pd.DataFrame, transfer_scored: pd.DataFrame) -> pd.DataFrame:
    source_test = source_scored[source_scored["split"] == "test"].copy()
    rows: list[dict[str, float | str]] = []
    for method, column in {
        "source_supervised_on_source_test": "supervised_score",
        "source_dictionary_on_source_test": "dictionary_score",
        "source_embedding_on_source_test": "embedding_similarity_score",
    }.items():
        row: dict[str, float | str] = {"domain": "source_test", "method": method}
        row.update(metrics(source_test["benchmark_label"].to_numpy(dtype=float), source_test[column].to_numpy(dtype=float)))
        rows.append(row)
    return pd.concat([pd.DataFrame(rows), transfer_metrics(transfer_scored)], ignore_index=True)


def transfer_calibration(scored: pd.DataFrame) -> pd.DataFrame:
    adapted = scored.rename(columns={"source_text_score": "supervised_score"}).copy()
    adapted["split"] = "transfer"
    adapted["constructed_validation_score"] = adapted["combined_transfer_score"]
    adapted["posting_text"] = adapted["policy_text"]
    return calibration_by_bin(adapted)


def transfer_confusion(scored: pd.DataFrame) -> pd.DataFrame:
    adapted = scored.rename(columns={"source_text_score": "supervised_score"}).copy()
    adapted["split"] = "test"
    adapted["constructed_validation_score"] = adapted["combined_transfer_score"]
    adapted["posting_text"] = adapted["policy_text"]
    return confusion_matrix(adapted)


def transfer_subgroups(scored: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    methods = {
        "source_text_score": "source_text_score",
        "combined_transfer_score": "combined_transfer_score",
    }
    for method, column in methods.items():
        for group_var in ["organization_type", "region"]:
            for group_value, group in scored.groupby(group_var):
                y = group["benchmark_label"].to_numpy(dtype=float)
                score = group[column].to_numpy(dtype=float)
                row: dict[str, float | str] = {
                    "method": method,
                    "group_variable": group_var,
                    "group_value": str(group_value),
                    "mean_benchmark": float(y.mean()),
                    "mean_score": float(score.mean()),
                }
                row.update(metrics(y, score))
                rows.append(row)
    return pd.DataFrame(rows).sort_values(["method", "false_negative_rate", "false_positive_rate"], ascending=[True, False, False])


def transfer_external_validation(scored: pd.DataFrame) -> pd.DataFrame:
    methods = {
        "source_text_score": "source_text_score",
        "dictionary": "dictionary_score",
        "embedding_similarity": "embedding_similarity_score",
        "image_proxy": "image_infrastructure_score",
        "combined_transfer_score": "combined_transfer_score",
    }
    audit = scored["external_service_audit"].to_numpy(dtype=float)
    truth = scored["simulation_truth_label"].to_numpy(dtype=float)
    rows: list[dict[str, float | str]] = []
    for method, column in methods.items():
        score = scored[column].to_numpy(dtype=float)
        rows.append(
            {
                "method": method,
                "correlation_with_external_audit": corr(score, audit),
                "correlation_with_simulation_truth": corr(score, truth),
                "mean_absolute_error_to_external_audit": float(np.mean(np.abs(score - audit))),
            }
        )
    return pd.DataFrame(rows).sort_values("mean_absolute_error_to_external_audit")


def benchmark_redesign_notes() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "issue": "target shift",
                "diagnostic": "Source labels measure remote-work feasibility, while transfer labels measure flexible service capacity.",
                "redesign": "Write a new rubric and relabel a stratified transfer benchmark before interpreting prevalence.",
            },
            {
                "issue": "vocabulary shift",
                "diagnostic": "Service records use tele-service, virtual intake, and mobile casework language not common in job postings.",
                "redesign": "Audit uncovered tokens and add target-domain examples to the benchmark.",
            },
            {
                "issue": "image proxy",
                "diagnostic": "Infrastructure score may proxy institutional resources rather than flexible service capacity.",
                "redesign": "Validate against facility audits and report subgroup performance by organization type.",
            },
            {
                "issue": "downstream use",
                "diagnostic": "Errors may vary by region or institution, contaminating causal comparisons.",
                "redesign": "Re-estimate downstream claims under source-only, transfer-recalibrated, and stricter-label measures.",
            },
        ]
    )


def transfer_prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "step": "transfer",
                "prompt": "Does the source vocabulary cover the transfer records well enough to reuse the text model?",
            },
            {
                "step": "diagnose",
                "prompt": "Which transfer subgroups have the largest false-negative or false-positive rates?",
            },
            {
                "step": "transfer",
                "prompt": "Does the image proxy add external signal or a new source of measurement error?",
            },
            {
                "step": "redesign",
                "prompt": "What labels, annotators, and external checks would be required before using this measure in a paper?",
            },
        ]
    )


def run(source_input: Path, transfer_input: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    source = split_data(pd.read_csv(source_input))
    train = source[source["split"] == "train"].reset_index(drop=True)
    validation = source[source["split"] == "validation"].reset_index(drop=True)
    train_validation = source[source["split"].isin(["train", "validation"])].reset_index(drop=True)
    cv = cross_validate(train, validation)
    best_penalty = float(cv.iloc[0]["penalty"])
    model = fit_final_model(train_validation, best_penalty)

    from reproduce_validation_workflow import score_methods

    source_scored = score_methods(model, source)
    transfer = pd.read_csv(transfer_input)
    transfer_scored = score_transfer(model, transfer)

    transfer_scored[
        [
            "record_id",
            "organization_type",
            "region",
            "simulation_truth_label",
            "benchmark_label",
            "external_service_audit",
            "image_infrastructure_score",
            "source_text_score",
            "dictionary_score",
            "embedding_similarity_score",
            "combined_transfer_score",
        ]
    ].to_csv(outdir / "transfer_scores.csv", index=False)

    source_vs_transfer_metrics(source_scored, transfer_scored).to_csv(outdir / "transport_metrics.csv", index=False)
    transfer_confusion(transfer_scored).to_csv(outdir / "transfer_confusion_matrix.csv", index=False)
    transfer_calibration(transfer_scored).to_csv(outdir / "transfer_calibration_by_bin.csv", index=False)
    transfer_subgroups(transfer_scored).to_csv(outdir / "transfer_subgroup_performance.csv", index=False)
    vocabulary_shift(model.feature_spec.vocabulary, transfer_scored["policy_text"]).to_csv(outdir / "vocabulary_shift.csv", index=False)
    transfer_external_validation(transfer_scored).to_csv(outdir / "transfer_external_validation.csv", index=False)
    benchmark_redesign_notes().to_csv(outdir / "benchmark_redesign_notes.csv", index=False)
    transfer_prompts().to_csv(outdir / "transfer_design_prompts.csv", index=False)

    print(f"Selected source ridge penalty: {best_penalty}")
    print(f"Wrote transfer validation outputs to {outdir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-input", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.source_input, args.input, args.outdir)


if __name__ == "__main__":
    main()
