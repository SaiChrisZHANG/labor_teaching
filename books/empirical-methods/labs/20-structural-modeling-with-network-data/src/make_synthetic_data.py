"""Create deterministic synthetic data for the Week 20 structural network lab."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

from network_structural_utils import compute_node_exposure, make_directed_edges, sigmoid


ROOT = Path(__file__).resolve().parents[1]


def make_workers(rng: np.random.Generator) -> pd.DataFrame:
    occupations = ["operations", "sales", "technical", "support"]
    rows: list[dict[str, object]] = []
    for worker_num in range(1, 73):
        group = "B" if rng.random() < 0.45 else "A"
        occupation = str(rng.choice(occupations, p=[0.28, 0.24, 0.26, 0.22]))
        neighborhood = int(rng.integers(1, 10))
        senior = int(rng.random() < (0.26 if group == "A" else 0.20))
        skill = float(rng.normal(0.20 if group == "A" else -0.10, 0.72))
        referral_access = float(
            sigmoid(0.15 + 0.55 * senior + 0.35 * skill - 0.20 * (group == "B") + rng.normal(0.0, 0.35))
        )
        rows.append(
            {
                "worker_id": f"W{worker_num:03d}",
                "group": group,
                "occupation": occupation,
                "neighborhood": neighborhood,
                "senior": senior,
                "skill": round(skill, 4),
                "referral_access": round(referral_access, 4),
            }
        )
    return pd.DataFrame(rows)


def make_dyads(workers: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    worker_records = workers.to_dict("records")
    rows: list[dict[str, object]] = []
    for left, right in combinations(worker_records, 2):
        same_group = int(left["group"] == right["group"])
        same_occupation = int(left["occupation"] == right["occupation"])
        skill_distance = abs(float(left["skill"]) - float(right["skill"]))
        geo_distance = abs(int(left["neighborhood"]) - int(right["neighborhood"]))
        either_senior = int(left["senior"] == 1 or right["senior"] == 1)
        referral_opportunity = float((float(left["referral_access"]) + float(right["referral_access"])) / 2)
        score = (
            -2.25
            + 0.82 * same_group
            + 0.58 * same_occupation
            - 0.34 * skill_distance
            - 0.10 * geo_distance
            + 0.34 * either_senior
            + 0.72 * referral_opportunity
        )
        link_prob = float(sigmoid(score))
        linked = int(rng.random() < link_prob)
        tie_strength = float(
            np.clip(
                rng.beta(2.0 + 0.9 * same_group + 0.5 * same_occupation, 3.4)
                + 0.10 * either_senior
                + 0.08 * referral_opportunity,
                0.04,
                0.98,
            )
        )
        rows.append(
            {
                "worker_i": left["worker_id"],
                "worker_j": right["worker_id"],
                "same_group": same_group,
                "same_occupation": same_occupation,
                "skill_distance": round(skill_distance, 4),
                "geo_distance": geo_distance,
                "either_senior": either_senior,
                "referral_opportunity": round(referral_opportunity, 4),
                "true_link_probability": round(link_prob, 4),
                "linked": linked,
                "tie_strength": round(tie_strength, 4),
            }
        )
    return pd.DataFrame(rows)


def add_labor_outcomes(
    workers: pd.DataFrame,
    directed_edges: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    exposed = compute_node_exposure(workers, directed_edges)
    wage = (
        24.0
        + 4.4 * exposed["skill"].to_numpy(dtype=float)
        + 2.2 * exposed["senior"].to_numpy(dtype=float)
        + 3.6 * exposed["network_info_exposure"].to_numpy(dtype=float)
        + 0.22 * exposed["degree"].to_numpy(dtype=float)
        - 1.1 * (exposed["group"].to_numpy() == "B").astype(float)
        + rng.normal(0.0, 1.8, len(exposed))
    )
    exposed["wage"] = np.round(wage, 4)
    offer_prob = sigmoid(
        -1.35
        + 0.75 * exposed["network_info_exposure"].to_numpy(dtype=float)
        + 0.30 * exposed["senior"].to_numpy(dtype=float)
        + 0.42 * exposed["skill"].to_numpy(dtype=float)
        - 0.24 * (exposed["group"].to_numpy() == "B").astype(float)
    )
    exposed["received_referral_offer"] = rng.binomial(1, offer_prob)
    exposed["referral_offer_probability"] = np.round(offer_prob, 4)
    return exposed


def make_referral_opportunities(
    workers: pd.DataFrame,
    dyads: pd.DataFrame,
    rng: np.random.Generator,
) -> pd.DataFrame:
    link_lookup: dict[tuple[str, str], tuple[int, float]] = {}
    for row in dyads.itertuples(index=False):
        link_lookup[(row.worker_i, row.worker_j)] = (int(row.linked), float(row.tie_strength))
        link_lookup[(row.worker_j, row.worker_i)] = (int(row.linked), float(row.tie_strength))

    referrer_pool = workers.loc[workers["senior"] == 1].copy()
    if len(referrer_pool) < 12:
        referrer_pool = workers.nlargest(16, "referral_access").copy()

    rows: list[dict[str, object]] = []
    workers_indexed = workers.set_index("worker_id")
    referrer_weights = np.exp(referrer_pool["referral_access"].to_numpy(dtype=float))
    referrer_weights = referrer_weights / referrer_weights.sum()
    worker_ids = workers["worker_id"].tolist()

    for opportunity_num in range(1, 641):
        referrer_id = str(rng.choice(referrer_pool["worker_id"].to_numpy(), p=referrer_weights))
        applicant_id = referrer_id
        while applicant_id == referrer_id:
            applicant_id = str(rng.choice(worker_ids))
        referrer = workers_indexed.loc[referrer_id]
        applicant = workers_indexed.loc[applicant_id]
        link_exists, base_strength = link_lookup.get((referrer_id, applicant_id), (0, 0.05))
        same_group = int(referrer["group"] == applicant["group"])
        cross_group = 1 - same_group
        latent_strength = float(
            np.clip(
                base_strength
                + 0.18 * link_exists
                + 0.10 * same_group
                + rng.normal(0.0, 0.05),
                0.02,
                0.98,
            )
        )
        observed_score = (
            -1.20
            + 1.55 * link_exists
            + 0.82 * latent_strength
            + 0.54 * float(referrer["referral_access"])
            + 0.28 * same_group
        )
        observed_prob = float(sigmoid(observed_score))
        observed_referral = int(rng.random() < observed_prob)
        signal_quality = float(
            np.clip(
                0.25
                + 0.45 * latent_strength
                + 0.18 * float(referrer["referral_access"])
                + 0.16 * float(applicant["skill"])
                + rng.normal(0.0, 0.12),
                0.02,
                0.98,
            )
        )
        callback_prob = float(
            sigmoid(
                -1.55
                + 1.20 * signal_quality
                + 0.52 * latent_strength
                + 0.34 * float(applicant["skill"])
                + 0.28 * same_group
                - 0.20 * (applicant["group"] == "B")
            )
        )
        callback = int(rng.random() < callback_prob) if observed_referral else np.nan
        rows.append(
            {
                "opportunity_id": f"O{opportunity_num:03d}",
                "referrer_id": referrer_id,
                "applicant_id": applicant_id,
                "referrer_group": referrer["group"],
                "applicant_group": applicant["group"],
                "same_group": same_group,
                "cross_group": cross_group,
                "link_exists": link_exists,
                "tie_strength": round(latent_strength, 4),
                "signal_quality": round(signal_quality, 4),
                "referrer_access": round(float(referrer["referral_access"]), 4),
                "applicant_skill": round(float(applicant["skill"]), 4),
                "observed_referral_probability": round(observed_prob, 4),
                "observed_referral": observed_referral,
                "callback_probability": round(callback_prob, 4),
                "callback": callback,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    rng = np.random.default_rng(2020)
    original_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    original_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)

    workers = make_workers(rng)
    dyads = make_dyads(workers, rng)
    directed_edges = make_directed_edges(dyads)
    workers = add_labor_outcomes(workers, directed_edges, rng)
    directed_edges = make_directed_edges(dyads)
    referrals = make_referral_opportunities(workers, dyads, rng)

    workers.to_csv(original_dir / "workers_synthetic.csv", index=False)
    dyads.to_csv(original_dir / "dyad_opportunities_synthetic.csv", index=False)
    directed_edges.to_csv(original_dir / "network_edges_synthetic.csv", index=False)
    referrals.to_csv(transfer_dir / "referral_search_synthetic.csv", index=False)

    print(f"Wrote {original_dir / 'workers_synthetic.csv'}")
    print(f"Wrote {original_dir / 'dyad_opportunities_synthetic.csv'}")
    print(f"Wrote {original_dir / 'network_edges_synthetic.csv'}")
    print(f"Wrote {transfer_dir / 'referral_search_synthetic.csv'}")


if __name__ == "__main__":
    main()
