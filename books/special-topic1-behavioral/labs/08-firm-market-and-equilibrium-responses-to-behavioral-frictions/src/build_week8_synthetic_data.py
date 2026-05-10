from __future__ import annotations

from pathlib import Path

import pandas as pd


LAB = Path(__file__).resolve().parents[1]


def unit_interval(index: int, salt: int = 0) -> float:
    return ((index * 37 + salt * 17) % 100) / 100


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def retirement_defaults() -> pd.DataFrame:
    rows = []
    groups = ["low_default", "standard_default", "high_default", "active_choice"]
    default_rates = {
        "low_default": 0.03,
        "standard_default": 0.06,
        "high_default": 0.10,
        "active_choice": 0.00,
    }
    default_equity = {
        "low_default": 0.45,
        "standard_default": 0.60,
        "high_default": 0.70,
        "active_choice": 0.00,
    }
    firm_response = {
        "low_default": "exploit_or_underinsure",
        "standard_default": "insure",
        "high_default": "insure_or_oversteer",
        "active_choice": "accommodate",
    }

    for worker in range(1200):
        group = groups[worker % len(groups)]
        worker_type = worker // len(groups)
        firm_id = f"firm-{worker % 48:02d}"
        sophistication = 0.18 + 0.09 * (worker_type % 8)
        liquidity_need = 0.16 + 0.08 * ((worker_type + 3) % 7)
        income = 42000 + 950 * (worker_type % 45) + 600 * (worker % 4)
        target_contribution = clamp(
            0.035 + 0.075 * sophistication - 0.045 * liquidity_need + 0.003 * (worker_type % 5),
            0.01,
            0.16,
        )
        target_equity = clamp(0.48 + 0.34 * sophistication - 0.16 * liquidity_need, 0.25, 0.90)

        active_choice_required = int(group == "active_choice")
        passive_probability = 0.0
        if not active_choice_required:
            passive_probability = clamp(
                0.78 - 0.46 * sophistication + 0.20 * liquidity_need + 0.04 * (group == "standard_default"),
                0.12,
                0.88,
            )
        passive_choice = int(unit_interval(worker, 4) < passive_probability)

        if active_choice_required or not passive_choice:
            contribution_rate = clamp(
                target_contribution + 0.006 * (unit_interval(worker, 11) - 0.5),
                0.00,
                0.18,
            )
            equity_share = clamp(
                target_equity + 0.04 * (unit_interval(worker, 13) - 0.5),
                0.05,
                0.95,
            )
        else:
            contribution_rate = default_rates[group]
            equity_share = default_equity[group]

        participation = int(contribution_rate >= 0.015)
        default_gap = contribution_rate - target_contribution
        welfare_distance = (
            abs(default_gap)
            + 0.35 * abs(equity_share - target_equity)
            + 0.25 * liquidity_need * max(0.0, default_gap)
            + 0.18 * (1.0 - sophistication) * max(0.0, -default_gap)
        )

        rows.append(
            {
                "worker_id": f"default-worker-{worker:04d}",
                "firm_id": firm_id,
                "default_group": group,
                "firm_response_type": firm_response[group],
                "active_choice_required": active_choice_required,
                "passive_choice": passive_choice,
                "default_contribution_rate": default_rates[group],
                "default_equity_share": default_equity[group],
                "sophistication_index": round(sophistication, 3),
                "liquidity_need_index": round(liquidity_need, 3),
                "annual_income": round(income, 2),
                "target_contribution_rate": round(target_contribution, 3),
                "target_equity_share": round(target_equity, 3),
                "participation": participation,
                "contribution_rate": round(contribution_rate, 3),
                "equity_share": round(equity_share, 3),
                "default_gap": round(default_gap, 3),
                "welfare_distance": round(welfare_distance, 3),
                "undersaving": int(default_gap < -0.015),
                "oversaving_liquidity_risk": int(default_gap > 0.015 and liquidity_need > 0.42),
            }
        )

    return pd.DataFrame(rows)


def outside_option_beliefs() -> pd.DataFrame:
    rows = []
    arms = ["control", "outside_option_info", "bargaining_prompt", "info_bargaining"]

    for worker in range(1000):
        arm = arms[worker % len(arms)]
        worker_type = worker // len(arms)
        current_wage = 17.5 + 0.42 * (worker_type % 36) + 0.25 * (worker % 4)
        true_outside_wage = current_wage * (1.04 + 0.006 * (worker_type % 9))
        search_friction = 0.20 + 0.09 * ((worker_type + 2) % 8)
        market_power = 0.18 + 0.08 * ((worker_type + 5) % 7)
        baseline_gap = 0.04 * current_wage + 0.11 * search_friction * current_wage + 0.07 * market_power * current_wage

        information = int(arm in {"outside_option_info", "info_bargaining"})
        bargaining_support = int(arm in {"bargaining_prompt", "info_bargaining"})
        updated_gap = baseline_gap * (1.0 - 0.58 * information - 0.18 * bargaining_support)
        perceived_outside_wage = true_outside_wage - updated_gap

        applications = (
            1.2
            + 1.9 * information
            + 0.9 * bargaining_support
            + 0.18 * max(0.0, perceived_outside_wage - current_wage)
            - 1.1 * search_friction
            - 0.4 * market_power
            + 0.08 * (worker_type % 5)
        )
        applications = max(0.0, applications)
        bargaining_probability = clamp(
            0.08
            + 0.12 * bargaining_support
            + 0.05 * information
            + 0.045 * max(0.0, perceived_outside_wage - current_wage)
            - 0.08 * market_power,
            0.02,
            0.75,
        )
        mobility_probability = clamp(
            0.05
            + 0.035 * applications
            + 0.018 * max(0.0, perceived_outside_wage - current_wage)
            - 0.11 * search_friction
            - 0.08 * market_power,
            0.01,
            0.65,
        )
        bargaining_attempt = int(unit_interval(worker, 19) < bargaining_probability)
        moved_job = int(unit_interval(worker, 23) < mobility_probability)
        wage_growth = (
            0.012
            + 0.045 * bargaining_attempt
            + 0.085 * moved_job
            + 0.010 * information
            - 0.018 * market_power
        )
        segmentation_index = (updated_gap / current_wage) + 0.45 * search_friction + 0.35 * market_power

        rows.append(
            {
                "worker_id": f"belief-worker-{worker:04d}",
                "arm": arm,
                "information": information,
                "bargaining_support": bargaining_support,
                "current_wage": round(current_wage, 2),
                "true_outside_wage": round(true_outside_wage, 2),
                "perceived_outside_wage": round(perceived_outside_wage, 2),
                "belief_gap": round(true_outside_wage - perceived_outside_wage, 2),
                "search_friction_index": round(search_friction, 3),
                "market_power_index": round(market_power, 3),
                "applications_next_month": round(applications, 2),
                "bargaining_attempt": bargaining_attempt,
                "moved_job": moved_job,
                "wage_growth_next_quarter": round(wage_growth, 3),
                "segmentation_index": round(segmentation_index, 3),
            }
        )

    return pd.DataFrame(rows)


def plan_disclosure_market() -> pd.DataFrame:
    rows = []
    arms = ["opaque", "fee_disclosure", "disclosure_switching_help"]

    for account in range(900):
        arm = arms[account % len(arms)]
        account_type = account // len(arms)
        high_switching_cost = int((account_type + account) % 3 != 0)
        sales_contact = int((account_type + 2) % 4 in {0, 1})
        baseline_fee_bps = 118 + 4 * (account_type % 8) + 18 * sales_contact

        disclosure = int(arm in {"fee_disclosure", "disclosure_switching_help"})
        switching_help = int(arm == "disclosure_switching_help")
        fee_salience = clamp(0.25 + 0.42 * disclosure + 0.18 * switching_help - 0.12 * sales_contact, 0.05, 0.95)
        demand_elasticity = clamp(
            0.22 + 0.62 * fee_salience - 0.23 * high_switching_cost - 0.10 * sales_contact,
            0.05,
            0.95,
        )
        switch_probability = clamp(
            0.05 + 0.30 * fee_salience + 0.16 * switching_help - 0.24 * high_switching_cost,
            0.01,
            0.70,
        )
        switched_plan = int(unit_interval(account, 29) < switch_probability)
        chose_low_fee_plan = int(
            unit_interval(account, 31)
            < clamp(0.28 + 0.45 * fee_salience + 0.12 * switched_plan - 0.18 * sales_contact, 0.05, 0.90)
        )
        realized_fee_bps = baseline_fee_bps - 28 * chose_low_fee_plan - 10 * disclosure - 8 * switched_plan

        rows.append(
            {
                "account_id": f"plan-account-{account:04d}",
                "arm": arm,
                "disclosure": disclosure,
                "switching_help": switching_help,
                "high_switching_cost": high_switching_cost,
                "sales_contact": sales_contact,
                "fee_salience_index": round(fee_salience, 3),
                "demand_elasticity_index": round(demand_elasticity, 3),
                "switched_plan": switched_plan,
                "chose_low_fee_plan": chose_low_fee_plan,
                "realized_fee_bps": round(realized_fee_bps, 2),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    original = LAB / "original" / "reduced"
    transfer = LAB / "transfer" / "data"
    original.mkdir(parents=True, exist_ok=True)
    transfer.mkdir(parents=True, exist_ok=True)

    retirement_defaults().to_csv(original / "retirement_defaults_synthetic.csv", index=False)
    outside_option_beliefs().to_csv(transfer / "outside_option_beliefs_synthetic.csv", index=False)
    plan_disclosure_market().to_csv(transfer / "plan_disclosure_market_synthetic.csv", index=False)


if __name__ == "__main__":
    main()
