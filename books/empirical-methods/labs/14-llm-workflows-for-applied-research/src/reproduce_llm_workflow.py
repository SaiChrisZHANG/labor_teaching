"""Run the Week 14 source-domain LLM workflow teaching path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from llm_teaching_surrogate import (
    MODEL_VERSION,
    RETRIEVAL_CORPUS,
    SCHEMA_VERSION,
    coefficient,
    metric_table,
    prompt_log,
    score_dataframe,
    subgroup_table,
)


PROFILES = ["conservative_v1", "rubric_v1", "expansive_v1"]


def attach_scores(source: pd.DataFrame, outputs: pd.DataFrame) -> pd.DataFrame:
    return outputs.merge(source, on="doc_id", how="left", validate="many_to_one")


def prompt_sensitivity(scored: pd.DataFrame) -> pd.DataFrame:
    wide = scored.pivot(index="doc_id", columns="profile", values="mismatch_label").reset_index()
    wide["any_disagreement"] = (
        wide[["conservative_v1", "rubric_v1", "expansive_v1"]].nunique(axis=1) > 1
    ).astype(int)
    source_cols = [
        "doc_id",
        "sector",
        "region",
        "occupation_group",
        "document_type",
        "benchmark_mismatch",
        "benchmark_type",
        "source_text",
    ]
    source_once = scored[source_cols].drop_duplicates("doc_id")
    return wide.merge(source_once, on="doc_id", how="left").sort_values(
        ["any_disagreement", "doc_id"],
        ascending=[False, True],
    )


def review_queue(scored: pd.DataFrame) -> pd.DataFrame:
    primary = scored[scored["profile"] == "rubric_v1"].copy()
    sensitivity = prompt_sensitivity(scored)[["doc_id", "any_disagreement"]]
    primary = primary.merge(sensitivity, on="doc_id", how="left")
    primary["false_positive"] = ((primary["mismatch_label"] == 1) & (primary["benchmark_mismatch"] == 0)).astype(int)
    primary["false_negative"] = ((primary["mismatch_label"] == 0) & (primary["benchmark_mismatch"] == 1)).astype(int)
    primary["review_priority"] = (
        primary["human_review_flag"]
        + primary["any_disagreement"]
        + primary["false_positive"]
        + primary["false_negative"]
        + primary["unsupported_flag"]
    )
    columns = [
        "doc_id",
        "review_priority",
        "sector",
        "occupation_group",
        "document_type",
        "benchmark_mismatch",
        "mismatch_label",
        "mismatch_score",
        "mismatch_type",
        "human_review_flag",
        "unsupported_flag",
        "any_disagreement",
        "false_positive",
        "false_negative",
        "evidence_phrases",
        "source_text",
    ]
    return primary[columns].sort_values(["review_priority", "doc_id"], ascending=[False, True]).head(40)


def downstream_table(scored: pd.DataFrame) -> pd.DataFrame:
    primary = scored[scored["profile"] == "rubric_v1"].copy()
    rows = []
    for label, column in [
        ("benchmark_mismatch", "benchmark_mismatch"),
        ("llm_rubric_label", "mismatch_label"),
        ("llm_rubric_score", "mismatch_score"),
    ]:
        estimate = coefficient(primary["applicant_interest"].to_numpy(float), primary[column].to_numpy(float))
        rows.append({"measure": label, **estimate})
    return pd.DataFrame(rows)


def hallucination_audit(scored: pd.DataFrame) -> pd.DataFrame:
    primary = scored[scored["profile"] == "rubric_v1"].copy()
    primary["false_positive"] = ((primary["mismatch_label"] == 1) & (primary["benchmark_mismatch"] == 0)).astype(int)
    use = primary[(primary["unsupported_flag"] == 1) | (primary["false_positive"] == 1)].copy()
    columns = [
        "doc_id",
        "sector",
        "occupation_group",
        "benchmark_mismatch",
        "benchmark_type",
        "mismatch_label",
        "mismatch_type",
        "mismatch_score",
        "unsupported_flag",
        "evidence_phrases",
        "source_text",
    ]
    return use[columns].sort_values(["unsupported_flag", "doc_id"], ascending=[False, True])


def diagnostic_prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "stage": "reproduce",
                "prompt": "What economic object does the mismatch schema measure: skill gap, credential gap, schedule fit, or general employability?",
            },
            {
                "stage": "diagnose",
                "prompt": "Which cases change labels across conservative, rubric, and expansive prompts?",
            },
            {
                "stage": "diagnose",
                "prompt": "Which unsupported or false-positive outputs should be routed to human review?",
            },
            {
                "stage": "downstream",
                "prompt": "How much does the downstream slope change when the benchmark variable is replaced by the LLM-coded variable?",
            },
        ]
    )


def run(input_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    source = pd.read_csv(input_path)
    outputs = score_dataframe(source, "source_text", PROFILES, "doc_id")
    scored = attach_scores(source, outputs)

    prompt_log("source structured-data extraction", PROFILES).to_csv(outdir / "prompt_log.csv", index=False)
    scored.to_csv(outdir / "structured_outputs_all_profiles.csv", index=False)
    scored[scored["profile"] == "rubric_v1"].to_csv(outdir / "structured_outputs.csv", index=False)
    metric_table(scored).to_csv(outdir / "classification_metrics.csv", index=False)
    subgroup_table(scored, ["sector", "region", "occupation_group", "document_type"]).to_csv(
        outdir / "subgroup_stability.csv",
        index=False,
    )
    prompt_sensitivity(scored).to_csv(outdir / "prompt_sensitivity.csv", index=False)
    review_queue(scored).to_csv(outdir / "human_review_queue.csv", index=False)
    hallucination_audit(scored).to_csv(outdir / "hallucination_audit.csv", index=False)
    downstream_table(scored).to_csv(outdir / "downstream_estimates.csv", index=False)
    diagnostic_prompts().to_csv(outdir / "diagnostic_prompts.csv", index=False)

    manifest = {
        "lab": "14-llm-workflows-for-applied-research",
        "input": str(input_path),
        "schema_version": SCHEMA_VERSION,
        "model_version": MODEL_VERSION,
        "retrieval_corpus": RETRIEVAL_CORPUS,
        "profiles": PROFILES,
        "live_api_used": False,
        "note": "Deterministic teaching surrogate; not an official replication.",
    }
    (outdir / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote reproduced outputs to {outdir}")


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
