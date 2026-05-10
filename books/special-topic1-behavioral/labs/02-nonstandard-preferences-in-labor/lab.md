# Code Lab 2: Nonstandard Preferences in Labor

**Course:** Behavioral Labor  
**Module / Week:** Week 2 -- Nonstandard Preferences in Labor Supply, Effort, Savings, and Training  
**Associated chapter:** `02-nonstandard-preferences-in-labor.md`  
**Lab slug:** `02-nonstandard-preferences-in-labor`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@kaurKremerMullainathan2010; @kaurKremerMullainathan2015]  
**Savings transfer anchor:** [@madrianShea2001]  
**Challenge anchor:** [@mas2006]  
**Optional frontier anchor:** [@dellaVignaListMalmendierRao2022]  

## Why This Lab Exists

Week 2 turns preference objects into applied labor designs. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact Kaur-Kremer-Mullainathan-style workplace self-control factbook.
2. **Diagnose** whether the design speaks to present bias, commitment demand, payday timing, or standard alternatives.
3. **Transfer** the same logic to a work-linked savings default design.

The lab does not require proprietary workplace, payroll, or administrative data.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small factbook on workplace effort and commitment choice;
2. distinguish a labor incentive effect from commitment demand;
3. state the observed worker-side margin before naming the behavioral object;
4. transfer the design logic from workplace effort to retirement or payroll-linked saving;
5. explain why welfare depends on ex ante preferences, ex post choices, and the counterfactual choice environment.

## Local Structure

```text
labs/02-nonstandard-preferences-in-labor/
  lab.md
  smoke.sh
  src/
    build_week2_synthetic_data.py
    reproduce_kaur_self_control.py
    transfer_work_linked_savings.py
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
conda run -n research python src/build_week2_synthetic_data.py

conda run -n research python src/reproduce_kaur_self_control.py \
  --input original/reduced/kaur_self_control_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_work_linked_savings.py \
  --input transfer/data/work_linked_savings_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/contract_summary.csv`
- `output/reproduced/payday_gradient.csv`
- `output/reproduced/workplace_self_control.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the worker-side margin: output, contract choice, target completion, or welfare?
- What identifying variation is being used: contract structure, payday timing, or worker type?
- Why is choosing a restrictive contract informative about commitment demand?
- What standard explanations remain: liquidity, effort costs, fatigue, monitoring, selection, or learning?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Benchmark:** What would a standard incentive model predict about output and contract choice?
2. **Preference object:** Is the plausible object present bias, commitment demand, risk aversion, or reference dependence?
3. **Margin:** Which observed outcome is moved by the design?
4. **Welfare caution:** Would the ex ante self and ex post self evaluate the same restriction in the same way?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/savings_summary.csv`
- `output/transfer/savings_effects.csv`
- `output/transfer/work_linked_savings.png`
- `output/transfer/transfer_note.txt`

Use [@madrianShea2001] to classify the work-linked savings design. State whether the default primarily identifies inertia, procrastination, transaction costs, information, or a reduced-form participation response. Use [@dufloGaleLiebmanOrszagSaez2006] as a comparison for designs where saving incentives are made explicit.

## Challenge

Use [@mas2006] to sketch a reference-dependent labor design. State:

- the reference point;
- the identifying variation;
- the observed performance margin;
- one reason the result could instead reflect standard incentives, morale, staffing, or measurement.

## Optional Frontier Extension

Use [@dellaVignaListMalmendierRao2022] to classify a workplace social-preference design. Do not estimate anything. Identify the private incentive, employer-surplus variation, gift variation, observed effort margin, and welfare caution.

## Deliverables Checklist

- [ ] run log
- [ ] workplace self-control figure
- [ ] contract summary and payday-gradient CSVs
- [ ] one-page design memo
- [ ] work-linked savings figure and tables
- [ ] short paragraph distinguishing treatment effects, preference objects, and welfare claims
