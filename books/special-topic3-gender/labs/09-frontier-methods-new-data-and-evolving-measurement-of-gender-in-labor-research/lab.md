# Code Lab 9: Frontier Methods, New Data, And Evolving Measurement

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 9 -- Frontier methods, new data, and evolving measurement  
**Associated chapter:** `09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research.md`  
**Lab slug:** `09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@fluchtmannGlennyHarmonMaibom2024]  
**Secondary / challenge anchors:** [@cardCardosoKline2016], [@kuhnShen2023]  
**Optional extension anchors:** [@bakerHalberstamKroftMasMessacar2023], [@cookDiamondHallListOyer2021], [@eames2025]

## Why This Lab Exists

Week 9 is the methods bridge into the final research-design week. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** an application-gap decomposition inspired by [@fluchtmannGlennyHarmonMaibom2024].
2. **Diagnose** what application data can see and what remains unobserved.
3. **Transfer** the same design logic to matched worker-firm and job-posting settings inspired by [@cardCardosoKline2016] and [@kuhnShen2023].

The lab is a teaching analog. It is not an official replication and does not require confidential application, employer, platform, or administrative microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce compact application-gap summaries from worker-job choice-set data;
2. distinguish an application margin from a callback, match, firm-treatment, or welfare margin;
3. decompose observed application gaps into between-occupation sorting and within-occupation job-quality differences;
4. diagnose when the design observes worker sorting but not firm treatment;
5. transfer the design logic to matched worker-firm decompositions and job-posting policy variation;
6. write a short research memo that names the labor object, gender measure, observed margin, identifying variation, and hidden welfare margin.

## Local Structure

```text
labs/09-frontier-methods-new-data-and-evolving-measurement-of-gender-in-labor-research/
  lab.md
  smoke.sh
  src/
    build_week9_synthetic_data.py
    reproduce_application_gap.py
    diagnose_design_shortfalls.py
    transfer_methods_frontier.py
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
conda run -n research python src/build_week9_synthetic_data.py

conda run -n research python src/reproduce_application_gap.py \
  --input original/reduced/fluchtmann_application_gap_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_design_shortfalls.py \
  --input original/reduced/fluchtmann_application_gap_synthetic.csv \
  --outdir output/diagnosed

conda run -n research python src/transfer_methods_frontier.py \
  --worker-firm transfer/data/card_worker_firm_synthetic.csv \
  --postings transfer/data/kuhn_shen_posting_policy_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/application_gap_summary.csv`
- `output/reproduced/application_gap_by_occupation.csv`
- `output/reproduced/application_quality_decomposition.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which gender difference is descriptive, and which would require causal identification?
- Which observed margin is an application margin rather than an accepted-job margin?
- Do women and men apply to different occupations, different firms within occupations, or both?
- Which part of the design speaks to search and sorting, and which part cannot speak to firm treatment?

## Part II. Diagnose

Run the diagnosis script. Inspect:

- `output/diagnosed/observed_vs_missing_margins.csv`
- `output/diagnosed/nonapplication_diagnostics.csv`
- `output/diagnosed/identification_shortfalls.csv`
- `output/diagnosed/diagnosis_note.txt`

Write a one-page diagnostic memo with four labeled paragraphs:

1. **Observed margin:** State what the application data measure directly.
2. **Sorting versus treatment:** Explain whether the design identifies worker sorting, firm treatment, or both.
3. **Hidden margin:** Name one welfare-relevant object not observed in the synthetic data.
4. **Stronger design:** State what new data linkage or source of variation would make the design more credible.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/worker_firm_sorting_decomposition.csv`
- `output/transfer/posting_policy_summary.csv`
- `output/transfer/transfer_design_map.csv`
- `output/transfer/transfer_note.txt`

Use the transfer exercise to compare three settings:

- application data inspired by [@fluchtmannGlennyHarmonMaibom2024],
- matched worker-firm data inspired by [@cardCardosoKline2016],
- job-posting policy variation inspired by [@kuhnShen2023].

For each setting, state the observed margin, the identifying variation, and the main missing margin.

## Optional Frontier Prompts

Choose one optional anchor:

- Use [@bakerHalberstamKroftMasMessacar2023] to explain how a pay-transparency reform could reveal firm response rather than only a wage-gap change.
- Use [@cookDiamondHallListOyer2021] to sketch a platform-data within-worker decomposition of a gender earnings gap.
- Use [@eames2025] to explain how legal sex, self-identified gender, perceived gender, and nonbinary identity would change an audit or application design.

Do not estimate the optional extensions in the bounded path. The deliverable is a short design memo.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced application-gap outputs
- [ ] one-page diagnosis memo
- [ ] transfer outputs
- [ ] setting-to-methods comparison paragraph
- [ ] optional frontier design memo
