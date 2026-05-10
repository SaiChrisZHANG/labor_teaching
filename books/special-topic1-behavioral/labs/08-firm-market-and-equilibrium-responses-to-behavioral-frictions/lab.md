# Code Lab 8: Firm, Market, and Equilibrium Responses

**Course:** Behavioral Labor  
**Module / Week:** Week 8 -- Firm, Market, and Equilibrium Responses to Behavioral Frictions  
**Associated chapter:** `08-firm-market-and-equilibrium-responses-to-behavioral-frictions.md`  
**Lab slug:** `08-firm-market-and-equilibrium-responses-to-behavioral-frictions`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@bernheimFradkinPopov2015]  
**Challenge anchor:** [@jagerRothRoussilleSchoefer2022]  
**Optional extension anchor:** [@duarteHastings2012] or [@hastingsHortacsuSyverson2017]  

## Why This Lab Exists

Week 8 asks what survives once worker-level behavioral wedges enter firms and markets. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact employer-sponsored retirement-default design inspired by [@bernheimFradkinPopov2015].
2. **Diagnose** whether a measured default effect is a worker-level reduced form, a firm response margin, or a welfare-relevant market outcome.
3. **Transfer** the same logic to outside-option beliefs and segmentation using [@jagerRothRoussilleSchoefer2022], then optionally to disclosure, demand elasticity, and switching costs using [@duarteHastings2012] or [@hastingsHortacsuSyverson2017].

The lab does not require confidential employer, plan, platform, or official replication data.

## Learning Objectives

By the end of the lab, students should be able to:

1. estimate default-design summaries for participation, contribution rates, passive choice, and welfare distance;
2. diagnose whether a default looks like exploitation, accommodation, insurance, or sorting;
3. distinguish worker-level reduced-form effects from firm response margins and market outcomes;
4. summarize outside-option belief distortions and connect them to search, bargaining, and segmentation;
5. interpret demand elasticity and switching-cost diagnostics under disclosure and sales-force variation;
6. write a short equilibrium interpretation memo that states what the data do and do not identify.

## Local Structure

```text
labs/08-firm-market-and-equilibrium-responses-to-behavioral-frictions/
  lab.md
  smoke.sh
  src/
    build_week8_synthetic_data.py
    reproduce_default_design.py
    transfer_beliefs_and_markets.py
  original/
    source-notes.md
    reduced/
  transfer/
    data-notes.md
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week8_synthetic_data.py

conda run -n research python src/reproduce_default_design.py \
  --input original/reduced/retirement_defaults_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_beliefs_and_markets.py \
  --belief-input transfer/data/outside_option_beliefs_synthetic.csv \
  --market-input transfer/data/plan_disclosure_market_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/default_design_summary.csv`
- `output/reproduced/default_effects_vs_active_choice.csv`
- `output/reproduced/firm_response_diagnostic.csv`
- `output/reproduced/default_design_reproduction.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the identifying variation: default contribution, active choice, or menu design?
- Which observed margin moves: participation, contribution, passive choice, or welfare distance?
- Is the first estimate a worker-level default effect or a firm response margin?
- Does the default look like insurance, accommodation, exploitation, or sorting?
- What welfare benchmark would make the interpretation credible?

## Part II. Diagnose

Write a short diagnostic memo with five paragraphs:

1. **Worker-level wedge:** What behavioral wedge is being measured?
2. **Firm response:** What did the employer or intermediary choose?
3. **Market condition:** Which condition lets the wedge survive: switching costs, transparency, search frictions, heterogeneity, competition, or labor-market power?
4. **Welfare benchmark:** Is the target full-information choice, low-hassle choice, sophisticated-worker choice, or a planner target?
5. **Policy implication:** What would change if firms redesign menus after the policy?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/outside_option_belief_summary.csv`
- `output/transfer/outside_option_effects_vs_control.csv`
- `output/transfer/segmentation_diagnostic.csv`
- `output/transfer/plan_disclosure_summary.csv`
- `output/transfer/demand_switching_diagnostic.csv`
- `output/transfer/equilibrium_transfer_diagnostics.png`
- `output/transfer/transfer_note.txt`

Use [@jagerRothRoussilleSchoefer2022] to interpret the outside-option transfer. Does the information margin identify a worker belief effect, a search and bargaining response, or a market segmentation result?

Then use [@duarteHastings2012] or [@hastingsHortacsuSyverson2017] for the optional market transfer. Does disclosure raise demand elasticity? Do high switching costs or sales contacts limit the disciplinary effect of transparency?

## Challenge

Propose one bounded transfer design:

- employer active-choice retirement enrollment with heterogeneous liquidity needs;
- platform job messages that steer application direction;
- wage transparency plus outside-option belief measurement;
- health-plan choice with endogenous employer menu redesign;
- disclosure reform in a high-switching-cost benefit market.

For the chosen setting, state the targeted worker wedge, firm response, market condition, identifying variation, observed margin, welfare benchmark, and policy limit.

## Deliverables Checklist

- [ ] run log
- [ ] default-design summary table
- [ ] default-effect table
- [ ] firm-response diagnostic
- [ ] outside-option belief summary
- [ ] segmentation diagnostic
- [ ] disclosure and switching-cost diagnostic
- [ ] one-page equilibrium interpretation memo
