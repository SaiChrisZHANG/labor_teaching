"""Deterministic teaching surrogate for the Week 14 LLM workflow lab.

The lab intentionally avoids live model APIs. These helpers mimic the shape of
an LLM extraction workflow: prompt profiles, schema-bound outputs, prompt logs,
benchmarks, and audit fields.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd


SCHEMA_VERSION = "mismatch-schema-v1"
MODEL_VERSION = "deterministic-teaching-surrogate-2026-05"
RETRIEVAL_CORPUS = "rubric-and-edge-cases-v1"

SKILL_TERMS = [
    "lacks python",
    "missing python",
    "needs python",
    "lacks sql",
    "missing sql",
    "needs sql",
    "training required",
    "upskilling required",
    "needs forklift",
    "missing equipment",
    "needs ehr",
    "not familiar with dashboards",
    "needs data dashboards",
]

CREDENTIAL_TERMS = [
    "license not held",
    "license pending",
    "certification missing",
    "credential missing",
    "degree requirement unmet",
    "clearance pending",
    "certification not current",
    "permit not current",
]

SCHEDULE_TERMS = [
    "schedule conflict",
    "available only mornings",
    "cannot work nights",
    "onsite conflict",
    "childcare conflict",
    "transportation conflict",
    "weekend restriction",
]

TRANSFER_TERMS = [
    "bridge credential",
    "reciprocity unresolved",
    "wraparound schedule",
    "rapid upskilling",
    "digital intake coaching",
    "license bridge",
    "credential bridge",
    "shift barrier",
]

SUPPORT_TERMS = [
    "meets required credential",
    "credential verified",
    "completed onboarding",
    "ready for placement",
    "skills aligned",
    "schedule aligned",
    "license verified",
    "no training barrier",
]

AMBIGUOUS_TERMS = [
    "could benefit from coaching",
    "transitioning from adjacent role",
    "some exposure",
    "partial fit",
    "informal experience",
    "may need support",
]

STOP_WORDS = {
    "the",
    "and",
    "with",
    "for",
    "from",
    "this",
    "that",
    "role",
    "record",
    "note",
    "summary",
    "candidate",
    "applicant",
    "case",
}


@dataclass(frozen=True)
class PromptProfile:
    name: str
    title: str
    threshold: float
    skill_weight: float
    credential_weight: float
    schedule_weight: float
    transfer_weight: float
    ambiguous_weight: float
    support_weight: float
    prompt_template: str


PROFILES = {
    "conservative_v1": PromptProfile(
        name="conservative_v1",
        title="Conservative explicit-evidence prompt",
        threshold=0.55,
        skill_weight=0.55,
        credential_weight=0.65,
        schedule_weight=0.55,
        transfer_weight=0.10,
        ambiguous_weight=0.05,
        support_weight=-0.70,
        prompt_template=(
            "Extract mismatch only when explicit evidence states a missing skill, "
            "credential, or schedule barrier. Return JSON following mismatch-schema-v1."
        ),
    ),
    "rubric_v1": PromptProfile(
        name="rubric_v1",
        title="Source rubric prompt with examples",
        threshold=0.45,
        skill_weight=0.55,
        credential_weight=0.65,
        schedule_weight=0.55,
        transfer_weight=0.20,
        ambiguous_weight=0.18,
        support_weight=-0.60,
        prompt_template=(
            "Use the labor-mismatch rubric and examples. Code skill, credential, "
            "or schedule mismatch when evidence supports a structured field."
        ),
    ),
    "expansive_v1": PromptProfile(
        name="expansive_v1",
        title="Expansive implicit-evidence prompt",
        threshold=0.25,
        skill_weight=0.55,
        credential_weight=0.65,
        schedule_weight=0.55,
        transfer_weight=0.28,
        ambiguous_weight=0.35,
        support_weight=-0.45,
        prompt_template=(
            "Look for explicit and implicit evidence of mismatch, including weak "
            "signals and adjacent-role transitions. Return all plausible fields."
        ),
    ),
    "transfer_adapted_v1": PromptProfile(
        name="transfer_adapted_v1",
        title="Transfer-domain case-note prompt",
        threshold=0.42,
        skill_weight=0.48,
        credential_weight=0.58,
        schedule_weight=0.50,
        transfer_weight=0.55,
        ambiguous_weight=0.20,
        support_weight=-0.55,
        prompt_template=(
            "Apply the mismatch rubric to workforce-agency case notes. Treat bridge "
            "credentials, reciprocity, rapid upskilling, and shift barriers as domain "
            "specific evidence."
        ),
    ),
}


def prompt_hash(profile: PromptProfile) -> str:
    payload = f"{profile.name}|{profile.prompt_template}|{SCHEMA_VERSION}|{RETRIEVAL_CORPUS}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z][a-z0-9]+", str(text).lower())


def count_phrases(text: str, phrases: Iterable[str]) -> int:
    lowered = str(text).lower()
    return sum(1 for phrase in phrases if re.search(rf"\b{re.escape(phrase)}\b", lowered))


def matching_phrases(text: str, phrases: Iterable[str]) -> list[str]:
    lowered = str(text).lower()
    return [phrase for phrase in phrases if re.search(rf"\b{re.escape(phrase)}\b", lowered)]


def evidence_counts(text: str) -> dict[str, int]:
    return {
        "skill": count_phrases(text, SKILL_TERMS),
        "credential": count_phrases(text, CREDENTIAL_TERMS),
        "schedule": count_phrases(text, SCHEDULE_TERMS),
        "transfer": count_phrases(text, TRANSFER_TERMS),
        "support": count_phrases(text, SUPPORT_TERMS),
        "ambiguous": count_phrases(text, AMBIGUOUS_TERMS),
    }


def evidence_phrases(text: str) -> list[str]:
    phrases: list[str] = []
    for pool in [SKILL_TERMS, CREDENTIAL_TERMS, SCHEDULE_TERMS, TRANSFER_TERMS, AMBIGUOUS_TERMS, SUPPORT_TERMS]:
        phrases.extend(matching_phrases(text, pool))
    return phrases


def classify_text(text: str, profile_name: str) -> dict[str, object]:
    profile = PROFILES[profile_name]
    counts = evidence_counts(text)
    raw_score = (
        profile.skill_weight * counts["skill"]
        + profile.credential_weight * counts["credential"]
        + profile.schedule_weight * counts["schedule"]
        + profile.transfer_weight * counts["transfer"]
        + profile.ambiguous_weight * counts["ambiguous"]
        + profile.support_weight * counts["support"]
    )
    score = float(np.clip(0.12 + raw_score / 2.2, 0.01, 0.99))
    predicted = int(raw_score >= profile.threshold)
    typed_scores = {
        "skill_gap": profile.skill_weight * counts["skill"] + 0.20 * counts["transfer"],
        "credential_gap": profile.credential_weight * counts["credential"] + 0.30 * counts["transfer"],
        "schedule_gap": profile.schedule_weight * counts["schedule"] + 0.18 * counts["transfer"],
    }
    mismatch_type = "none"
    if predicted:
        mismatch_type = max(typed_scores, key=typed_scores.get)
        if typed_scores[mismatch_type] <= 0 and counts["ambiguous"] > 0:
            mismatch_type = "ambiguous_fit"

    explicit_evidence = counts["skill"] + counts["credential"] + counts["schedule"] + counts["transfer"]
    unsupported_flag = int(predicted == 1 and explicit_evidence == 0)
    low_confidence_flag = int(0.42 <= score <= 0.62 or counts["ambiguous"] > 0)
    review_flag = int(unsupported_flag or low_confidence_flag)
    phrases = evidence_phrases(text)
    rationale = "evidence: " + "; ".join(phrases[:4]) if phrases else "no explicit mismatch evidence found"

    raw_output = {
        "schema_version": SCHEMA_VERSION,
        "profile": profile.name,
        "mismatch_label": predicted,
        "mismatch_type": mismatch_type,
        "mismatch_score": round(score, 4),
        "confidence": round(abs(score - 0.5) * 2, 4),
        "evidence": phrases[:6],
        "review_flag": review_flag,
        "rationale": rationale,
    }

    return {
        "profile": profile.name,
        "prompt_hash": prompt_hash(profile),
        "mismatch_label": predicted,
        "mismatch_type": mismatch_type,
        "mismatch_score": round(score, 4),
        "confidence": raw_output["confidence"],
        "schema_valid": 1,
        "unsupported_flag": unsupported_flag,
        "low_confidence_flag": low_confidence_flag,
        "human_review_flag": review_flag,
        "evidence_phrase_count": len(phrases),
        "evidence_phrases": "; ".join(phrases[:8]),
        "raw_output": json.dumps(raw_output, sort_keys=True),
    }


def prompt_log(task: str, profile_names: Iterable[str]) -> pd.DataFrame:
    rows = []
    for name in profile_names:
        profile = PROFILES[name]
        rows.append(
            {
                "task": task,
                "profile": profile.name,
                "profile_title": profile.title,
                "prompt_hash": prompt_hash(profile),
                "schema_version": SCHEMA_VERSION,
                "model_version": MODEL_VERSION,
                "retrieval_corpus": RETRIEVAL_CORPUS,
                "temperature": 0.0,
                "top_p": 1.0,
                "prompt_template": profile.prompt_template,
            }
        )
    return pd.DataFrame(rows)


def score_dataframe(df: pd.DataFrame, text_column: str, profile_names: Iterable[str], id_column: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for _, row in df.iterrows():
        for profile_name in profile_names:
            result = classify_text(str(row[text_column]), profile_name)
            rows.append({id_column: row[id_column], **result})
    return pd.DataFrame(rows)


def binary_metrics(y_true: np.ndarray, labels: np.ndarray, scores: np.ndarray) -> dict[str, float]:
    y_true = y_true.astype(int)
    labels = labels.astype(int)
    tp = float(np.sum((labels == 1) & (y_true == 1)))
    fp = float(np.sum((labels == 1) & (y_true == 0)))
    fn = float(np.sum((labels == 0) & (y_true == 1)))
    tn = float(np.sum((labels == 0) & (y_true == 0)))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "n": float(len(y_true)),
        "accuracy": float(np.mean(labels == y_true)),
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_positive_rate": fp / (fp + tn) if fp + tn else 0.0,
        "false_negative_rate": fn / (fn + tp) if fn + tp else 0.0,
        "positive_rate": float(np.mean(labels)),
        "brier": float(np.mean((scores - y_true) ** 2)),
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
    }


def metric_table(scored: pd.DataFrame, truth_col: str = "benchmark_mismatch") -> pd.DataFrame:
    rows = []
    for profile, group in scored.groupby("profile"):
        metrics = binary_metrics(
            group[truth_col].to_numpy(dtype=int),
            group["mismatch_label"].to_numpy(dtype=int),
            group["mismatch_score"].to_numpy(dtype=float),
        )
        rows.append({"profile": profile, **metrics})
    return pd.DataFrame(rows).sort_values("profile").reset_index(drop=True)


def subgroup_table(
    scored: pd.DataFrame,
    group_columns: list[str],
    truth_col: str = "benchmark_mismatch",
    profile: str = "rubric_v1",
) -> pd.DataFrame:
    use = scored[scored["profile"] == profile].copy()
    rows = []
    for column in group_columns:
        for value, group in use.groupby(column):
            metrics = binary_metrics(
                group[truth_col].to_numpy(dtype=int),
                group["mismatch_label"].to_numpy(dtype=int),
                group["mismatch_score"].to_numpy(dtype=float),
            )
            rows.append({"group_variable": column, "group_value": value, "profile": profile, **metrics})
    return pd.DataFrame(rows).sort_values(["group_variable", "group_value"]).reset_index(drop=True)


def coefficient(y: np.ndarray, x: np.ndarray) -> dict[str, float]:
    xmat = np.column_stack([np.ones(len(x)), x])
    beta = np.linalg.lstsq(xmat, y, rcond=None)[0]
    residual = y - xmat @ beta
    sigma2 = float((residual @ residual) / max(len(y) - 2, 1))
    vcov = sigma2 * np.linalg.pinv(xmat.T @ xmat)
    se = float(np.sqrt(vcov[1, 1]))
    return {"intercept": float(beta[0]), "slope": float(beta[1]), "std_error": se}


def vocabulary_coverage(source_texts: pd.Series, target_texts: pd.Series) -> pd.DataFrame:
    source_vocab = {
        token
        for text in source_texts.fillna("")
        for token in tokenize(str(text))
        if token not in STOP_WORDS
    }
    target_tokens = [
        token
        for text in target_texts.fillna("")
        for token in tokenize(str(text))
        if token not in STOP_WORDS
    ]
    covered = [token for token in target_tokens if token in source_vocab]
    uncovered_counts: dict[str, int] = {}
    for token in target_tokens:
        if token not in source_vocab:
            uncovered_counts[token] = uncovered_counts.get(token, 0) + 1
    top_uncovered = sorted(uncovered_counts.items(), key=lambda item: (-item[1], item[0]))[:12]
    return pd.DataFrame(
        [
            {
                "source_vocabulary_size": len(source_vocab),
                "target_token_count": len(target_tokens),
                "covered_token_count": len(covered),
                "coverage_rate": len(covered) / len(target_tokens) if target_tokens else 0.0,
                "top_uncovered_tokens": "; ".join(f"{token}:{count}" for token, count in top_uncovered),
            }
        ]
    )
