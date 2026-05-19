"""Transfer the Week 12 source text model to a small multimodal setting."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

from reproduce_computational_measurement import (
    REMOTE_BROAD,
    classification_table,
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
    out["remote_label"] = out["flexible_service_capacity"]
    out["split"] = "transfer"
    return out


def vocabulary_comparison(source_vocabulary: list[str], transfer_texts: pd.Series) -> pd.DataFrame:
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
        for token, count in token_counter.most_common(20)
        if token not in source
    ][:10]
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


def modality_ablation(scored: pd.DataFrame) -> pd.DataFrame:
    y = scored["flexible_service_capacity"].to_numpy(dtype=float)
    methods = {
        "source_text_supervised": "source_text_score",
        "dictionary_broad": "dictionary_broad_score",
        "embedding_similarity": "embedding_similarity_score",
        "image_only": "image_infrastructure_score",
        "audio_only": "audio_clarity_score",
        "video_only": "video_interaction_score",
        "multimodal_index": "multimodal_index",
    }
    rows: list[dict[str, float | str]] = []
    for method, column in methods.items():
        row: dict[str, float | str] = {"method": method}
        row.update(metrics(y, scored[column].to_numpy(dtype=float)))
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["brier", "method"]).reset_index(drop=True)


def failure_modes() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "modality": "source text model",
                "main_failure_mode": "Job-posting language does not match policy-record language.",
                "diagnostic": "Vocabulary coverage and human labels in the transfer domain.",
            },
            {
                "modality": "dictionary",
                "main_failure_mode": "Remote terms may indicate temporary service delivery rather than durable flexibility.",
                "diagnostic": "Audit false positives and refine target definition.",
            },
            {
                "modality": "image score",
                "main_failure_mode": "Visible infrastructure may proxy wealth, office quality, or camera angle.",
                "diagnostic": "Compare against independent facility audits and image-quality checks.",
            },
            {
                "modality": "audio score",
                "main_failure_mode": "Clarity may reflect recording device, room acoustics, or staff identity.",
                "diagnostic": "Balance recording conditions and audit subgroup residuals.",
            },
            {
                "modality": "video score",
                "main_failure_mode": "Interaction quality is difficult to define and expensive to label.",
                "diagnostic": "Use manual review, consent documentation, and modality ablations.",
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
                "step": "transfer",
                "prompt": "Which modality improves predictive diagnostics, and what new validation burden does it create?",
            },
            {
                "step": "diagnose",
                "prompt": "Would you use the multimodal index as a descriptive measure, a treatment variable, or only an exploratory proxy?",
            },
            {
                "step": "diagnose",
                "prompt": "What human-labeled audit sample would be required before using image, audio, or video features in a paper?",
            },
        ]
    )


def run(source_input: Path, transfer_input: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    source = split_data(pd.read_csv(source_input))
    train_validation = source[source["split"].isin(["train", "validation"])].reset_index(drop=True)
    model = fit_final_model(train_validation, penalty=0.05)

    transfer = pd.read_csv(transfer_input)
    model_ready = prepare_transfer_for_source_model(transfer)

    scored = transfer.copy()
    scored["source_text_score"] = predict_scores(model, model_ready)
    scored["dictionary_broad_score"] = scored["policy_text"].map(lambda text: dictionary_score(str(text), REMOTE_BROAD))
    scored["embedding_similarity_score"] = scored["policy_text"].map(embedding_similarity_score)
    scored["multimodal_index"] = (
        0.40 * scored["source_text_score"]
        + 0.20 * scored["dictionary_broad_score"]
        + 0.15 * scored["image_infrastructure_score"]
        + 0.12 * scored["audio_clarity_score"]
        + 0.13 * scored["video_interaction_score"]
    ).clip(0.0, 1.0)

    scored[
        [
            "record_id",
            "organization_type",
            "region",
            "flexible_service_capacity",
            "source_text_score",
            "dictionary_broad_score",
            "embedding_similarity_score",
            "image_infrastructure_score",
            "audio_clarity_score",
            "video_interaction_score",
            "multimodal_index",
        ]
    ].to_csv(outdir / "transfer_multimodal_scores.csv", index=False)

    modality_ablation(scored).to_csv(outdir / "modality_ablation.csv", index=False)
    vocabulary_comparison(model.feature_spec.vocabulary, scored["policy_text"]).to_csv(
        outdir / "source_vs_transfer_vocabulary.csv",
        index=False,
    )
    failure_modes().to_csv(outdir / "modality_failure_modes.csv", index=False)
    transfer_prompts().to_csv(outdir / "transfer_design_prompts.csv", index=False)

    transfer_for_classification = scored.rename(
        columns={
            "flexible_service_capacity": "remote_label",
            "source_text_score": "supervised_score",
            "policy_text": "posting_text",
        }
    ).copy()
    transfer_for_classification["split"] = "transfer"
    transfer_for_classification["dictionary_narrow_score"] = transfer_for_classification["dictionary_broad_score"]
    transfer_for_classification["dictionary_broad_share"] = transfer_for_classification["dictionary_broad_score"]
    transfer_for_classification["constructed_measure"] = transfer_for_classification["multimodal_index"]
    classification_table(transfer_for_classification).to_csv(outdir / "transfer_classification_metrics.csv", index=False)

    print(f"Wrote transfer outputs to {outdir}")


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
