"""Create deterministic synthetic data for the Week 19 network causal lab."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

from network_causal_utils import sigmoid


ROOT = Path(__file__).resolve().parents[1]


def make_worker_panel() -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(1919)
    team_probs = {
        "T01": 0.25,
        "T02": 0.25,
        "T03": 0.40,
        "T04": 0.40,
        "T05": 0.60,
        "T06": 0.60,
        "T07": 0.75,
        "T08": 0.75,
    }
    rows: list[dict[str, object]] = []
    worker_num = 1
    team_shocks = {team: rng.normal(0.0, 1.0) for team in team_probs}

    for team_id, treatment_prob in team_probs.items():
        for seat in range(1, 13):
            group = "B" if rng.random() < (0.42 + 0.08 * (team_id in {"T03", "T04", "T07"})) else "A"
            role = "senior" if seat in {2, 5, 9} or rng.random() < 0.12 else "junior"
            baseline_skill = rng.normal(0.25 if group == "A" else -0.05, 0.65)
            tenure_years = np.clip(rng.gamma(2.1, 1.2), 0.2, 9.0)
            treated = int(rng.random() < treatment_prob)
            outside_team_contact_count = int(rng.poisson(0.35 + 0.25 * (role == "senior")))
            rows.append(
                {
                    "worker_id": f"W{worker_num:03d}",
                    "team_id": team_id,
                    "seat": seat,
                    "group": group,
                    "role": role,
                    "assigned_treatment_prob": treatment_prob,
                    "saturation_cell": "high" if treatment_prob >= 0.60 else "low",
                    "treated": treated,
                    "baseline_skill": round(float(baseline_skill), 4),
                    "tenure_years": round(float(tenure_years), 4),
                    "team_shock": round(float(team_shocks[team_id]), 4),
                    "outside_team_contact_count": outside_team_contact_count,
                }
            )
            worker_num += 1

    workers = pd.DataFrame(rows)
    edges = make_edges(workers, rng)
    workers = add_outcomes(workers, edges, rng)
    return workers, edges


def make_edges(workers: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for team_id, team in workers.groupby("team_id"):
        team_records = team.to_dict("records")
        for left, right in combinations(team_records, 2):
            same_group = left["group"] == right["group"]
            same_role = left["role"] == right["role"]
            senior_pair = left["role"] == "senior" or right["role"] == "senior"
            link_prob = 0.30 + 0.18 * same_group + 0.10 * same_role + 0.08 * senior_pair
            if rng.random() >= min(link_prob, 0.88):
                continue
            base_weight = rng.beta(2.4 + 0.8 * same_group, 3.0)
            tie_strength = float(np.clip(base_weight + 0.12 * senior_pair, 0.05, 0.98))
            for source, target in [(left, right), (right, left)]:
                rows.append(
                    {
                        "source_worker_id": source["worker_id"],
                        "target_worker_id": target["worker_id"],
                        "team_id": team_id,
                        "same_group": int(same_group),
                        "same_role": int(same_role),
                        "tie_strength": round(tie_strength, 4),
                    }
                )
    return pd.DataFrame(rows)


def add_outcomes(workers: pd.DataFrame, edges: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    treated_map = workers.set_index("worker_id")["treated"].to_dict()
    exposure_rows: list[dict[str, float | str]] = []
    for worker_id, group in edges.groupby("source_worker_id"):
        weighted_degree = group["tie_strength"].sum()
        treated_weight = sum(treated_map[target] * weight for target, weight in zip(group["target_worker_id"], group["tie_strength"]))
        exposure_rows.append(
            {
                "worker_id": worker_id,
                "latent_graph_treated_share": treated_weight / weighted_degree if weighted_degree > 0 else 0.0,
            }
        )
    exposure = pd.DataFrame(exposure_rows)
    data = workers.merge(exposure, on="worker_id", how="left")
    data["latent_graph_treated_share"] = data["latent_graph_treated_share"].fillna(0.0)

    team_treated = data.groupby("team_id")["treated"].transform("sum")
    team_n = data.groupby("team_id")["worker_id"].transform("count")
    data["latent_team_treated_share_loo"] = (
        (team_treated - data["treated"]) / (team_n - 1).replace(0, np.nan)
    ).fillna(0.0)

    productivity = (
        52.0
        + 3.2 * data["treated"].to_numpy(dtype=float)
        + 4.4 * data["latent_graph_treated_share"].to_numpy(dtype=float)
        + 1.4 * data["latent_team_treated_share_loo"].to_numpy(dtype=float)
        + 2.6 * data["baseline_skill"].to_numpy(dtype=float)
        + 0.35 * data["tenure_years"].to_numpy(dtype=float)
        + 1.5 * (data["role"].to_numpy() == "senior").astype(float)
        - 1.0 * (data["group"].to_numpy() == "B").astype(float)
        + data["team_shock"].to_numpy(dtype=float)
        + rng.normal(0.0, 2.4, len(data))
    )
    data["productivity"] = np.round(productivity, 4)
    data["retained_next_period"] = rng.binomial(
        1,
        sigmoid(-1.2 + 0.035 * (productivity - 50.0) + 0.45 * data["treated"].to_numpy(dtype=float)),
    )
    return data.drop(columns=["latent_graph_treated_share", "latent_team_treated_share_loo"])


def make_referral_dyads(workers: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(1920)
    referrers = workers.loc[workers["role"] == "senior"].copy()
    if len(referrers) < 20:
        referrers = workers.sample(n=24, random_state=1920).copy()

    applicant_ids = [f"A{num:03d}" for num in range(1, 121)]
    applicant_groups = {
        applicant_id: ("B" if rng.random() < 0.47 else "A")
        for applicant_id in applicant_ids
    }
    applicant_access = {
        applicant_id: float(np.clip(rng.normal(0.0, 0.8), -1.8, 1.8))
        for applicant_id in applicant_ids
    }

    rows: list[dict[str, object]] = []
    referrer_weights = np.exp(referrers["baseline_skill"].to_numpy(dtype=float))
    referrer_weights = referrer_weights / referrer_weights.sum()

    for referral_num in range(1, 361):
        referrer = referrers.iloc[int(rng.choice(np.arange(len(referrers)), p=referrer_weights))]
        applicant_id = str(rng.choice(applicant_ids))
        applicant_group = applicant_groups[applicant_id]
        same_group = int(referrer["group"] == applicant_group)
        tie_strength = float(
            np.clip(
                rng.beta(2.0 + 1.1 * same_group + 0.5 * int(referrer["treated"]), 3.0),
                0.03,
                0.98,
            )
        )
        referral_score = (
            -1.25
            + 1.25 * tie_strength
            + 0.34 * same_group
            + 0.28 * int(referrer["treated"])
            + 0.18 * float(referrer["baseline_skill"])
            + 0.22 * applicant_access[applicant_id]
            - 0.16 * (applicant_group == "B")
        )
        callback_prob = float(sigmoid(referral_score))
        callback = int(rng.random() < callback_prob)
        rows.append(
            {
                "referral_id": f"R{referral_num:03d}",
                "referrer_worker_id": referrer["worker_id"],
                "applicant_id": applicant_id,
                "referrer_group": referrer["group"],
                "applicant_group": applicant_group,
                "same_group": same_group,
                "referrer_treated": int(referrer["treated"]),
                "referrer_baseline_skill": round(float(referrer["baseline_skill"]), 4),
                "applicant_access_score": round(applicant_access[applicant_id], 4),
                "tie_strength": round(tie_strength, 4),
                "callback": callback,
                "callback_probability": round(callback_prob, 4),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    original_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    original_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)

    workers, edges = make_worker_panel()
    referrals = make_referral_dyads(workers)

    workers.to_csv(original_dir / "workplace_peers_synthetic.csv", index=False)
    edges.to_csv(original_dir / "coworker_edges_synthetic.csv", index=False)
    referrals.to_csv(transfer_dir / "referral_dyads_synthetic.csv", index=False)

    print(f"Wrote {original_dir / 'workplace_peers_synthetic.csv'}")
    print(f"Wrote {original_dir / 'coworker_edges_synthetic.csv'}")
    print(f"Wrote {transfer_dir / 'referral_dyads_synthetic.csv'}")


if __name__ == "__main__":
    main()
