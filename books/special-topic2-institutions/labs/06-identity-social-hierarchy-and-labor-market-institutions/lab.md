# Code Lab 6: Identity, Social Hierarchy, and Labor-Market Institutions

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 6 -- Identity, Social Hierarchy, and Labor-Market Institutions  
**Associated chapter:** `06-identity-social-hierarchy-and-labor-market-institutions.md`  
**Lab slug:** `06-identity-social-hierarchy-and-labor-market-institutions`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@bertrandMullainathan2004]  
**Secondary / challenge anchor:** [@oreopoulos2011]  
**Network / caste extension anchor:** [@munshiRosenzweig2006]  
**Contact / hierarchy extension anchor:** [@lowe2021]  
**Public-rule extension anchor:** [@anejaXu2020]  
**Misallocation extension anchor:** [@hsiehHurstJonesKlenow2019]  

## Why This Lab Exists

Week 6 treats category-based hierarchy as a labor-market institution. The lab uses synthetic data to practice three moves:

1. **Reproduce** a resume-audit comparison in the spirit of [@bertrandMullainathan2004].
2. **Diagnose** whether a barrier is belief-based, network-based, credential-based, legal or public-rule-based, contact-based, spatial, or macro.
3. **Transfer** the same diagnostic language to immigrant credentials, caste networks, contact design, federal employment segregation, macro talent misallocation, and stratification.

The lab is a teaching analog. It is not an official replication of any anchor paper.

## Learning Objectives

By the end of the lab, students should be able to:

1. summarize callback rates by randomized category signal and resume quality;
2. state what a resume-audit callback gap identifies and what it does not identify;
3. classify barriers as belief-based, network-based, credential-based, legal, contact, spatial, or macro;
4. distinguish micro, meso, and macro hierarchy evidence;
5. separate Week 5 conduct norms from Week 6 category-based hierarchy.

## Local Structure

```text
labs/06-identity-social-hierarchy-and-labor-market-institutions/
  lab.md
  smoke.sh
  src/
    build_week6_synthetic_data.py
    reproduce_resume_audit.py
    diagnose_hierarchy_barrier.py
    transfer_hierarchy_design_classifier.py
  original/
    source-notes.md
    reduced/
  transfer/
    data-notes.md
    data/
  output/
    reproduced/
    diagnostics/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week6_synthetic_data.py

conda run -n research python src/reproduce_resume_audit.py \
  --input original/reduced/resume_audit_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_hierarchy_barrier.py \
  --input original/reduced/hierarchy_barriers_synthetic.csv \
  --outdir output/diagnostics

conda run -n research python src/transfer_hierarchy_design_classifier.py \
  --input transfer/data/hierarchy_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and resume-audit script. Inspect:

- `output/reproduced/resume_audit_summary.csv`
- `output/reproduced/resume_audit_gaps.csv`
- `output/reproduced/quality_callback_summary.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which rows isolate a race-name signal?
- Which rows add immigrant status or foreign credential recognition?
- What does the callback gap identify?
- Why is this not a wage, productivity, promotion, or lifecycle estimate?
- How does resume quality change the interpretation?

## Part II. Diagnose

Run the diagnostic script. Inspect:

- `output/diagnostics/barrier_diagnostic.csv`
- `output/diagnostics/barrier_type_counts.csv`
- `output/diagnostics/evidence_level_counts.csv`
- `output/diagnostics/diagnostic_note.txt`

Use the following checklist:

- Is the barrier belief-based, network-based, credential-based, legal, contact-based, spatial, or macro?
- Is the evidence micro, meso, or macro?
- What is the first moving margin: callback, referral, credential recognition, public job, contact, place, or occupation allocation?
- Would the same case belong in Week 5 if the mechanism were conduct rather than category-based access?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_object_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether it identifies:

- audit evidence on employer beliefs;
- credential or resume evidence on immigrant screening;
- network evidence on referrals and occupation persistence;
- contact experiment evidence on integration design;
- historical or public-rule evidence on state action;
- macro evidence on talent misallocation;
- a stratification framework rather than a single causal estimate.

## Challenge

Add one row to `transfer/data/hierarchy_designs_synthetic.csv` for a study of housing segregation, licensing rules, public-sector hiring, or migrant legal status. Classify the design family, evidence level, and first labor-market gate. Then explain whether the case is a Week 5 conduct-norm problem, a Week 6 hierarchy problem, or both.

## Deliverables Checklist

- [ ] resume-audit summary CSV
- [ ] callback gap table
- [ ] quality-by-signal callback table
- [ ] barrier diagnostic CSV
- [ ] evidence-level counts
- [ ] transfer classification CSV
- [ ] one-page memo distinguishing conduct norms from category hierarchy
