# Optional Code Lab: LGBTQ+ Identities, Work, Discrimination, And Labor-Market Institutions

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Optional long lecture after Week 9 -- LGBTQ+ identities, work, discrimination, and labor-market institutions  
**Associated chapter:** `optional-lgbtq-identities-work-discrimination-and-labor-market-institutions.md`  
**Lab slug:** `optional-lgbtq-identities-work-discrimination-and-labor-market-institutions`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@tilcsik2011prideprejudice]  
**Secondary / challenge anchors:** [@granbergAnderssonAhmed2020transhiring], [@sansone2019pinkwork]  
**Optional extension anchors:** [@carpenterLee2024transgenderearnings], [@klineRoseWalters2021systemic], [@carpenterPostolekWarman2024sameSexBenefits]

## Why This Lab Exists

The optional LGBTQ+ lecture uses familiar labor-economics designs in a measurement-fragile setting. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a Tilcsik-style correspondence experiment and estimate callback gaps by randomized identity signal.
2. **Diagnose** what audit data identify and what remains hidden about disclosure, underlying population membership, and within-job treatment.
3. **Transfer** the logic to legal recognition and benefit design inspired by marriage-equality and employer-benefits evidence.

The lab is a teaching analog. It is not an official replication and does not require confidential audit, employer, benefits, survey, or administrative microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce callback-rate summaries from synthetic correspondence-audit data;
2. distinguish randomized identity signals from underlying LGBTQ+ population membership;
3. separate hiring discrimination from within-job treatment and selection into applications;
4. diagnose how a transgender hiring audit changes the measured identity object and signal;
5. transfer the design logic to policy/event-study and employer-benefits margins;
6. write a short research memo that names the labor object, identity object, observed margin, identifying variation, and hidden welfare margin.

## Local Structure

```text
labs/optional-lgbtq-identities-work-discrimination-and-labor-market-institutions/
  lab.md
  smoke.sh
  src/
    build_week10_synthetic_data.py
    reproduce_tilcsik_audit.py
    diagnose_lgbtq_designs.py
    transfer_law_benefits.py
  original/
    reduced/
  transfer/
    data/
  output/
    reproduced/
    diagnosed/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week10_synthetic_data.py

conda run -n research python src/reproduce_tilcsik_audit.py \
  --input original/reduced/tilcsik_pride_prejudice_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_lgbtq_designs.py \
  --audit original/reduced/tilcsik_pride_prejudice_synthetic.csv \
  --trans transfer/data/granberg_andersson_ahmed_trans_hiring_synthetic.csv \
  --outdir output/diagnosed

conda run -n research python src/transfer_law_benefits.py \
  --policy transfer/data/sansone_marriage_policy_synthetic.csv \
  --benefits transfer/data/carpenter_postolek_warman_benefits_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/callback_gap_summary.csv`
- `output/reproduced/callback_gap_by_occupation.csv`
- `output/reproduced/employer_climate_gradient.csv`
- `output/reproduced/design_balance.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which labor margin is observed directly?
- What is randomized, and what is not randomized?
- Does the audit identify discrimination against an underlying population or treatment of a visible identity signal?
- Is the callback gap concentrated in particular occupations or employer-climate cells?

## Part II. Diagnose

Run the diagnosis script. Inspect:

- `output/diagnosed/observed_vs_hidden_margins.csv`
- `output/diagnosed/trans_hiring_diagnostics.csv`
- `output/diagnosed/identification_shortfalls.csv`
- `output/diagnosed/diagnosis_note.txt`

Write a one-page diagnostic memo with four labeled paragraphs:

1. **Observed margin:** State what the correspondence audit measures directly.
2. **Identity object:** Explain the difference between an identity signal, disclosure, and underlying population membership.
3. **Sorting versus treatment:** Explain whether the design identifies worker sorting, employer screening, within-job treatment, or all three.
4. **Stronger design:** State what data linkage or source of variation would let a researcher connect hiring discrimination to later careers.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/marriage_policy_event_study.csv`
- `output/transfer/benefit_response_summary.csv`
- `output/transfer/transfer_design_map.csv`
- `output/transfer/transfer_note.txt`

Use the transfer exercise to compare three settings:

- correspondence audits inspired by [@tilcsik2011prideprejudice],
- transgender hiring evidence inspired by [@granbergAnderssonAhmed2020transhiring],
- legal recognition and benefits evidence inspired by [@sansone2019pinkwork] and [@carpenterPostolekWarman2024sameSexBenefits].

For each setting, state the observed margin, the identifying variation, and the main missing margin.

## Optional Frontier Prompts

Choose one optional anchor:

- Use [@carpenterLee2024transgenderearnings] to explain how administrative identity linkage can observe earnings dynamics while still measuring a selected subgroup.
- Use [@klineRoseWalters2021systemic] to sketch how large-employer audit data can separate market-wide discrimination from firm-concentrated discrimination.
- Use [@carpenterPostolekWarman2024sameSexBenefits] to explain why employer benefit design is labor-market compensation rather than background policy.

Do not estimate the optional extensions in the bounded path. The deliverable is a short design memo.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced callback-gap outputs
- [ ] one-page diagnosis memo
- [ ] transfer outputs
- [ ] setting-to-methods comparison paragraph
- [ ] optional frontier design memo
