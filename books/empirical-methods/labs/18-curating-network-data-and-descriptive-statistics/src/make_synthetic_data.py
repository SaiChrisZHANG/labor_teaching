"""Create deterministic synthetic data for the Week 18 network curation lab."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from network_utils import sigmoid


ROOT = Path(__file__).resolve().parents[1]

EMPLOYERS = pd.DataFrame(
    [
        {"employer_id": "E01", "industry": "health", "firm_quality": 0.55, "outside_observed_frame": 0},
        {"employer_id": "E02", "industry": "logistics", "firm_quality": 0.20, "outside_observed_frame": 0},
        {"employer_id": "E03", "industry": "manufacturing", "firm_quality": 0.10, "outside_observed_frame": 0},
        {"employer_id": "E04", "industry": "retail", "firm_quality": -0.20, "outside_observed_frame": 0},
        {"employer_id": "E05", "industry": "business", "firm_quality": 0.70, "outside_observed_frame": 0},
        {"employer_id": "E06", "industry": "public", "firm_quality": 0.35, "outside_observed_frame": 0},
        {"employer_id": "E07", "industry": "hospitality", "firm_quality": -0.25, "outside_observed_frame": 0},
        {"employer_id": "E08", "industry": "construction", "firm_quality": 0.00, "outside_observed_frame": 0},
        {"employer_id": "E09", "industry": "logistics", "firm_quality": -0.10, "outside_observed_frame": 1},
        {"employer_id": "E10", "industry": "logistics", "firm_quality": 0.30, "outside_observed_frame": 1},
    ]
)

ANCHOR_EMPLOYERS = {
    "N01": ["E01", "E05", "E06", "E04"],
    "N02": ["E02", "E03", "E04", "E09"],
    "N03": ["E05", "E01", "E08", "E10"],
    "N04": ["E03", "E02", "E07", "E09"],
    "N05": ["E06", "E01", "E05", "E04"],
    "N06": ["E08", "E02", "E10", "E07"],
}


def choose_employer(rng: np.random.Generator, neighborhood_id: str, group: str) -> str:
    anchors = ANCHOR_EMPLOYERS[neighborhood_id]
    if group == "A":
        probs = np.array([0.36, 0.30, 0.20, 0.14])
    else:
        probs = np.array([0.24, 0.25, 0.22, 0.29])
    return str(rng.choice(anchors, p=probs / probs.sum()))


def make_workers() -> pd.DataFrame:
    rng = np.random.default_rng(1818)
    rows: list[dict[str, object]] = []
    employer_map = EMPLOYERS.set_index("employer_id").to_dict("index")

    worker_num = 1
    for neighborhood_num in range(1, 7):
        neighborhood_id = f"N{neighborhood_num:02d}"
        for block_num in range(1, 5):
            block_id = f"{neighborhood_id}B{block_num:02d}"
            group_b_prob = 0.36 + 0.14 * (neighborhood_num in {2, 4, 6}) + 0.08 * (block_num in {3, 4})
            for _ in range(6):
                group = "B" if rng.random() < group_b_prob else "A"
                employer_id = choose_employer(rng, neighborhood_id, group)
                employer = employer_map[employer_id]
                skill = float(rng.normal(0.20 if group == "A" else -0.05, 0.75))
                tenure_years = float(np.clip(rng.gamma(2.0, 1.1), 0.15, 8.0))
                survey_response = int(rng.random() < (0.84 if group == "A" else 0.70))
                missing_link_score = float(
                    np.clip(
                        0.10
                        + 0.10 * (group == "B")
                        + 0.12 * int(employer["outside_observed_frame"])
                        + 0.12 * (1 - survey_response)
                        + rng.normal(0.0, 0.035),
                        0.02,
                        0.65,
                    )
                )
                rows.append(
                    {
                        "worker_id": f"W{worker_num:03d}",
                        "neighborhood_id": neighborhood_id,
                        "block_id": block_id,
                        "group": group,
                        "employer_id": employer_id,
                        "industry": employer["industry"],
                        "firm_quality": employer["firm_quality"],
                        "outside_observed_frame": int(employer["outside_observed_frame"]),
                        "skill_index": round(skill, 4),
                        "tenure_years": round(tenure_years, 4),
                        "survey_response": survey_response,
                        "missing_link_score": round(missing_link_score, 4),
                    }
                )
                worker_num += 1

    workers = pd.DataFrame(rows)
    local_counts = workers.groupby(["block_id", "employer_id"])["worker_id"].transform("count") - 1
    peer_counts = workers.groupby("block_id")["worker_id"].transform("count") - 1
    latent_exposure = np.where(peer_counts > 0, local_counts / peer_counts, 0.0)
    rng = np.random.default_rng(1819)
    employment_prob = sigmoid(
        -0.35
        + 0.85 * latent_exposure
        + 0.45 * workers["skill_index"].to_numpy(dtype=float)
        + 0.50 * workers["firm_quality"].to_numpy(dtype=float)
        - 0.16 * (workers["group"].to_numpy() == "B").astype(float)
        - 0.18 * workers["outside_observed_frame"].to_numpy(dtype=float)
    )
    workers["block_same_employer_contacts"] = local_counts.astype(int)
    workers["block_peer_count"] = peer_counts.astype(int)
    workers["latent_local_employer_exposure"] = np.round(latent_exposure, 4)
    workers["employed_next_year"] = rng.binomial(1, employment_prob)
    base_wage = (
        17.0
        + 2.4 * workers["skill_index"].to_numpy(dtype=float)
        + 3.2 * workers["firm_quality"].to_numpy(dtype=float)
        + 1.3 * latent_exposure
        - 0.8 * (workers["group"].to_numpy() == "B").astype(float)
        + rng.normal(0.0, 1.25, len(workers))
    )
    workers["wage"] = np.round(np.maximum(base_wage, 9.5), 2)
    workers["missing_link_risk"] = pd.cut(
        workers["missing_link_score"],
        bins=[-0.01, 0.16, 0.28, 1.0],
        labels=["low", "medium", "high"],
    ).astype(str)
    return workers


def make_referrals(workers: pd.DataFrame) -> pd.DataFrame:
    rng = np.random.default_rng(1820)
    eligible = workers.loc[workers["employed_next_year"] == 1].copy()
    firm_quality = workers.set_index("employer_id")["firm_quality"].groupby(level=0).first().to_dict()
    rows: list[dict[str, object]] = []
    applicant_pool = [f"A{num:03d}" for num in range(1, 76)]
    applicant_groups = {
        applicant_id: ("B" if rng.random() < 0.46 else "A")
        for applicant_id in applicant_pool
    }

    for referral_num in range(1, 101):
        referrer = eligible.sample(n=1, weights=np.exp(eligible["skill_index"]), random_state=int(rng.integers(1, 1_000_000))).iloc[0]
        applicant_id = str(rng.choice(applicant_pool))
        applicant_group = applicant_groups[applicant_id]
        same_group = int(referrer["group"] == applicant_group)
        tie_strength = float(
            np.clip(
                rng.beta(2.4 + 1.2 * same_group, 2.8)
                + 0.10 * (referrer["tenure_years"] > 2.5),
                0.02,
                0.98,
            )
        )
        hire_prob = sigmoid(
            -1.05
            + 1.15 * tie_strength
            + 0.30 * float(referrer["skill_index"])
            + 0.40 * float(firm_quality[str(referrer["employer_id"])])
            + 0.18 * same_group
            - 0.20 * (applicant_group == "B")
        )
        rows.append(
            {
                "referral_id": f"R{referral_num:03d}",
                "referrer_worker_id": referrer["worker_id"],
                "applicant_id": applicant_id,
                "referrer_group": referrer["group"],
                "applicant_group": applicant_group,
                "firm_id": referrer["employer_id"],
                "referral_month": f"2021-{int(rng.integers(1, 13)):02d}",
                "tie_strength": round(tie_strength, 4),
                "same_group_referral": same_group,
                "hired": int(rng.random() < hire_prob),
            }
        )
    return pd.DataFrame(rows).sort_values(["referral_month", "referral_id"]).reset_index(drop=True)


def main() -> None:
    original_dir = ROOT / "original" / "reduced"
    transfer_dir = ROOT / "transfer" / "data"
    original_dir.mkdir(parents=True, exist_ok=True)
    transfer_dir.mkdir(parents=True, exist_ok=True)

    workers = make_workers()
    referrals = make_referrals(workers)

    workers.to_csv(original_dir / "workers_synthetic.csv", index=False)
    referrals.to_csv(transfer_dir / "referrals_synthetic.csv", index=False)

    print(f"Wrote {original_dir / 'workers_synthetic.csv'}")
    print(f"Wrote {transfer_dir / 'referrals_synthetic.csv'}")


if __name__ == "__main__":
    main()
