from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def worker_wellness() -> pd.DataFrame:
    rows = []
    arms = [
        ("control", 0.36, 0.36, 0.35, 0.00),
        ("incentive", 0.36, 0.54, 0.39, 0.00),
        ("commitment", 0.36, 0.46, 0.44, 0.38),
        ("incentive_commitment", 0.36, 0.59, 0.47, 0.42),
    ]
    for arm_index, (arm, baseline, program, post, commit_rate) in enumerate(arms):
        for worker in range(90):
            ability = ((worker % 9) - 4) * 0.012
            day_cycle = (worker % 5) * 0.004
            rows.append(
                {
                    "worker_id": f"{arm[:3]}-{worker:03d}",
                    "arm": arm,
                    "baseline_participation": round(baseline + ability, 3),
                    "program_participation": round(program + ability + day_cycle, 3),
                    "post_participation": round(post + 0.7 * ability, 3),
                    "commitment_takeup": int(commit_rate > 0 and (worker % 100) < int(commit_rate * 100)),
                }
            )
    return pd.DataFrame(rows)


def job_search() -> pd.DataFrame:
    rows = []
    arms = [
        ("control", 4.1, 0.31, 0.22),
        ("information", 4.9, 0.39, 0.29),
        ("information_planning", 5.4, 0.43, 0.34),
    ]
    for arm, apps, belief, employed in arms:
        for seeker in range(80):
            heterogeneity = ((seeker % 8) - 3.5) * 0.08
            rows.append(
                {
                    "seeker_id": f"{arm[:4]}-{seeker:03d}",
                    "arm": arm,
                    "weekly_applications": round(apps + heterogeneity, 2),
                    "subjective_job_finding_prob": round(belief + ((seeker % 6) - 2.5) * 0.01, 3),
                    "employed_within_8_weeks": int((seeker % 100) < int(employed * 100)),
                }
            )
    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)
    worker_wellness().to_csv(original / "royer_stehr_sydnor_worker_wellness_synthetic.csv", index=False)
    job_search().to_csv(transfer / "altmann_job_search_synthetic.csv", index=False)


if __name__ == "__main__":
    main()

