from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def workplace_self_control() -> pd.DataFrame:
    rows = []
    for worker in range(160):
        high_self_control = worker % 4 in {0, 1}
        chose_commitment = worker % 5 in {0, 1}
        worker_skill = ((worker % 10) - 4.5) * 0.6
        contract = "commitment" if chose_commitment else "standard"
        target = 52

        for day in range(10):
            payday_distance = (worker + day) % 10
            close_to_payday = 9 - payday_distance
            base_output = 49 + worker_skill + 0.35 * day
            commitment_effect = 4.2 if chose_commitment else 0.0
            payday_effect = 0.75 * close_to_payday
            self_control_effect = 2.0 if high_self_control else -1.2
            output_units = base_output + commitment_effect + payday_effect + self_control_effect

            rows.append(
                {
                    "worker_id": f"worker-{worker:03d}",
                    "day": day + 1,
                    "contract": contract,
                    "chose_commitment": int(chose_commitment),
                    "high_self_control_type": int(high_self_control),
                    "payday_distance": payday_distance,
                    "close_to_payday": int(payday_distance <= 2),
                    "target_units": target,
                    "output_units": round(output_units, 2),
                    "met_target": int(output_units >= target),
                }
            )

    return pd.DataFrame(rows)


def work_linked_savings() -> pd.DataFrame:
    rows = []
    regimes = [
        ("active_choice", 0.48, 0.045),
        ("auto_enrollment", 0.74, 0.064),
        ("auto_enrollment_match", 0.82, 0.078),
    ]
    for regime, participation_rate, base_contribution in regimes:
        participation_cutoff = int(participation_rate * 120)
        for employee in range(120):
            tenure_adjustment = (employee % 6) * 0.004
            earnings_adjustment = ((employee % 9) - 4) * 0.001
            participates = int(employee < participation_cutoff)
            contribution_rate = 0.0
            if participates:
                contribution_rate = base_contribution + tenure_adjustment + earnings_adjustment

            rows.append(
                {
                    "employee_id": f"{regime[:4]}-{employee:03d}",
                    "regime": regime,
                    "tenure_years": 1 + (employee % 6),
                    "participates": participates,
                    "contribution_rate": round(max(contribution_rate, 0.0), 3),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    workplace_self_control().to_csv(original / "kaur_self_control_synthetic.csv", index=False)
    work_linked_savings().to_csv(transfer / "work_linked_savings_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
