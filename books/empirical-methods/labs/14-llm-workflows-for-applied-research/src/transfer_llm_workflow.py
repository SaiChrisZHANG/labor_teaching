"""Transfer the Week 14 LLM workflow to synthetic workforce case notes."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from llm_teaching_surrogate import (
    coefficient,
    metric_table,
    prompt_log,
    score_dataframe,
    subgroup_table,
    vocabulary_coverage,
)


PROFILES = ["rubric_v1", "transfer_adapted_v1"]


def attach_scores(transfer: pd.DataFrame, outputs: pd.DataFrame) -> pd.DataFrame:
    return outputs.merge(transfer, on="case_id", how="left", validate="many_to_one")


def transport_metrics(scored: pd.DataFrame) -> pd.DataFrame:
    table = metric_table(scored)
    table["domain"] = "transfer_workforce_case_notes"
    return table


def transfer_sensitivity(scored: pd.DataFrame) -> pd.DataFrame:
    wide = scored.pivot(index="case_id", columns="profile", values="mismatch_label").reset_index()
    wide["label_changed_after_adaptation"] = (wide["rubric_v1"] != wide["transfer_adapted_v1"]).astype(int)
    cols = [
        "case_id",
        "program_area",
        "region",
        "benchmark_mismatch",
        "benchmark_type",
        "case_text",
    ]
    once = scored[cols].drop_duplicates("case_id")
    return wide.merge(once, on="case_id", how="left").sort_values(
        ["label_changed_after_adaptation", "case_id"],
        ascending=[False, True],
    )


def downstream_table(scored: pd.DataFrame) -> pd.DataFrame:
    adapted = scored[scored["profile"] == "transfer_adapted_v1"].copy()
    rows = []
    for label, column in [
        ("benchmark_mismatch", "benchmark_mismatch"),
        ("adapted_llm_label", "mismatch_label"),
        ("adapted_llm_score", "mismatch_score"),
    ]:
        estimate = coefficient(adapted["placement_score"].to_numpy(float), adapted[column].to_numpy(float))
        rows.append({"measure": label, **estimate})
    return pd.DataFrame(rows)


def redesign_notes() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "issue": "source prompt misses transfer vocabulary",
                "evidence_to_check": "vocabulary_shift.csv and transfer_prompt_sensitivity.csv",
                "redesign_action": "add domain examples for bridge credentials, reciprocity, shift barriers, and rapid upskilling",
            },
            {
                "issue": "benchmark may not match source document unit",
                "evidence_to_check": "manual audit of case-note labels",
                "redesign_action": "label a stratified transfer benchmark before using the measure downstream",
            },
            {
                "issue": "case notes can include sensitive information",
                "evidence_to_check": "privacy review and redaction protocol",
                "redesign_action": "preserve redacted prompt logs and avoid sending identifiable notes to external APIs",
            },
            {
                "issue": "prompt adaptation changes the estimand",
                "evidence_to_check": "label changes after adaptation",
                "redesign_action": "state whether the target is source-domain mismatch or transfer-domain placement readiness",
            },
        ]
    )


def diagnostic_prompts() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "stage": "transfer",
                "prompt": "Which transfer phrases are outside the source vocabulary and why do they matter economically?",
            },
            {
                "stage": "transfer",
                "prompt": "Does the adapted prompt improve benchmark performance or simply change the target construct?",
            },
            {
                "stage": "privacy",
                "prompt": "Which fields would be redacted or kept inside a secure environment in a real case-note project?",
            },
            {
                "stage": "replication",
                "prompt": "What synthetic examples and aggregate diagnostics should be released if raw case notes cannot be shared?",
            },
        ]
    )


def run(source_input: Path, transfer_input: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    source = pd.read_csv(source_input)
    transfer = pd.read_csv(transfer_input)
    outputs = score_dataframe(transfer, "case_text", PROFILES, "case_id")
    scored = attach_scores(transfer, outputs)

    prompt_log("transfer structured-data extraction", PROFILES).to_csv(outdir / "prompt_log.csv", index=False)
    scored.to_csv(outdir / "transfer_structured_outputs.csv", index=False)
    transport_metrics(scored).to_csv(outdir / "transport_metrics.csv", index=False)
    subgroup_table(scored, ["program_area", "region"], profile="transfer_adapted_v1").to_csv(
        outdir / "transfer_subgroup_stability.csv",
        index=False,
    )
    transfer_sensitivity(scored).to_csv(outdir / "transfer_prompt_sensitivity.csv", index=False)
    vocabulary_coverage(source["source_text"], transfer["case_text"]).to_csv(outdir / "vocabulary_shift.csv", index=False)
    downstream_table(scored).to_csv(outdir / "transfer_downstream_estimates.csv", index=False)
    redesign_notes().to_csv(outdir / "benchmark_redesign_notes.csv", index=False)
    diagnostic_prompts().to_csv(outdir / "transfer_design_prompts.csv", index=False)
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
