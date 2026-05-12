# Code Lab 1: Why Gender Matters For Labor Economics

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 1 -- Why Gender Matters for Labor Economics  
**Associated chapter:** `01-why-gender-matters-for-labor-economics.md`  
**Lab slug:** `01-why-gender-matters-for-labor-economics`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@hylandDjankovGoldberg2020genderedlaws]  
**Secondary / challenge anchor:** [@klevenLandaisSogaard2019children]  
**Optional frontier anchor:** [@bertrandGoldinKatz2010dynamics]  

## Why This Lab Exists

Week 1 teaches students to classify gender-and-labor evidence before they over-interpret it. The bounded path uses synthetic data to practice three moves:

1. **Reproduce** a compact gendered-laws and workforce factbook.
2. **Diagnose** the outcome, comparison group, mechanism, level of analysis, and design type.
3. **Transfer** the same diagnostic workflow to lifecycle child-penalty event time.

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require confidential microdata.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small institutional gender-and-labor factbook from local synthetic data;
2. distinguish outcomes, comparison groups, mechanisms, and design types;
3. classify worker-level, household-level, firm-level, and institutional claims;
4. explain why country-specific and lifecycle-specific results can still teach broad labor lessons;
5. transfer the same measurement discipline from legal institutions to child penalties and career dynamics.

## Local Structure

```text
labs/01-why-gender-matters-for-labor-economics/
  lab.md
  smoke.sh
  src/
    build_week1_synthetic_data.py
    reproduce_gendered_laws.py
    transfer_child_penalty.py
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
conda run -n research python src/build_week1_synthetic_data.py

conda run -n research python src/reproduce_gendered_laws.py \
  --input original/reduced/gendered_laws_workforce_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_child_penalty.py \
  --input transfer/data/child_penalty_event_time_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/legal_access_tier_summary.csv`
- `output/reproduced/high_low_gap_diagnostics.csv`
- `output/reproduced/design_diagnosis_map.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the labor-market outcome?
- What is the comparison group?
- Which legal or institutional object is being measured?
- What mechanism could connect the legal measure to work, hours, employment, or authority?
- Is this path descriptive, causal, decomposition-based, or a hybrid?

## Part II. Diagnose

Write a short design memo with five paragraphs:

1. **Outcome:** Is the paper measuring employment, labor-force participation, hours, earnings, authority, safety, care, or welfare?
2. **Comparison:** Are the relevant comparisons across gender groups, legal environments, countries, event times, occupations, or firms?
3. **Mechanism:** Is the channel worker-side, household-side, firm-side, institutional, or policy-based?
4. **Design:** Is the evidence descriptive, causal, decomposition-based, or a structured diagnostic?
5. **General lesson:** Why can a country-year institutional result matter for labor economics beyond the countries in the table?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/child_penalty_event_time_summary.csv`
- `output/transfer/child_penalty_diagnostics.csv`
- `output/transfer/transfer_design_map.csv`
- `output/transfer/transfer_note.txt`

Use the same classification logic for the child-penalty exercise inspired by [@klevenLandaisSogaard2019children]. State why the measured gap changes when the outcome is earnings, hours, or employment. Then state what extra evidence would be needed to move from a lifecycle pattern to a claim about care constraints, firm flexibility, occupational sorting, or bargaining.

## Challenge

Use [@bertrandGoldinKatz2010dynamics] to sketch how the Week 1 framework changes inside a professional career setting. Do not estimate anything. State the outcome, comparison group, mechanism, design type, and the firm or career object that would need to be measured.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced legal-access summary CSVs
- [ ] one-page diagnosis memo
- [ ] transfer child-penalty summary CSVs
- [ ] short paragraph distinguishing descriptive patterns, mechanisms, and causal claims
