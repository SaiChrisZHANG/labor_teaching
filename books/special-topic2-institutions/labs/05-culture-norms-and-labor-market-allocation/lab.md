# Code Lab 5: Culture, Norms, and Labor-Market Allocation

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 5 -- Culture, Norms, and Labor-Market Allocation  
**Associated chapter:** `05-culture-norms-and-labor-market-allocation.md`  
**Lab slug:** `05-culture-norms-and-labor-market-allocation`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@fernandezFogli2009]  
**Secondary / challenge anchor:** [@floryLeibbrandtList2015]  
**Religion extension anchor:** [@carvalho2013]  
**Leadership / networking extension anchor:** [@cullenPerezTruglia2023]  
**Work-norm extension anchor:** [@brezaKaurKrishnaswamy2019]  

## Why This Lab Exists

Week 5 treats norms as labor-market mechanisms rather than residual explanations. The lab uses synthetic data to practice three moves:

1. **Reproduce** inherited-culture reasoning in the spirit of [@fernandezFogli2009].
2. **Diagnose** when a proxy is measuring norms rather than wages, care costs, host demand, or selection.
3. **Transfer** the same diagnostic language to job-entry experiments, religion and reputation, workplace networking, local social environments, market-level wage-acceptance norms, and the Week 6 hierarchy boundary.

The lab is a teaching analog. It is not an official replication of any anchor paper.

## Learning Objectives

By the end of the lab, students should be able to:

1. summarize an inherited-culture proxy and a labor-supply outcome by origin norm group;
2. distinguish inherited cultural transmission from current social pressure;
3. compare norm proxies with price or constraint proxies such as wages, host demand, and childcare costs;
4. interpret job-entry framing as evidence on acceptable-workplace norms;
5. classify whether a design belongs to Week 5 conduct norms or Week 6 structural hierarchy.

## Local Structure

```text
labs/05-culture-norms-and-labor-market-allocation/
  lab.md
  smoke.sh
  src/
    build_week5_synthetic_data.py
    reproduce_inherited_culture.py
    diagnose_norm_proxy.py
    transfer_norm_design_classifier.py
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
conda run -n research python src/build_week5_synthetic_data.py

conda run -n research python src/reproduce_inherited_culture.py \
  --input original/reduced/inherited_culture_norms_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/diagnose_norm_proxy.py \
  --inherited original/reduced/inherited_culture_norms_synthetic.csv \
  --job-entry original/reduced/job_entry_norm_framing_synthetic.csv \
  --outdir output/diagnostics

conda run -n research python src/transfer_norm_design_classifier.py \
  --input transfer/data/norm_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and inherited-culture script. Inspect:

- `output/reproduced/inherited_culture_summary.csv`
- `output/reproduced/inherited_culture_gaps.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which variables are inherited norm proxies?
- Which variables are host-market prices or constraints?
- Does the pattern identify transmitted culture, current peer pressure, or both?
- What selection story could mimic the same origin-group gradient?
- Why is this a labor-supply exercise rather than a generic culture exercise?

## Part II. Diagnose

Run the diagnostic script. Inspect:

- `output/diagnostics/proxy_diagnostic.csv`
- `output/diagnostics/job_entry_summary.csv`
- `output/diagnostics/job_entry_gaps.csv`
- `output/diagnostics/diagnostic_note.txt`

Use the following checklist:

- Is the proxy measuring norms, prices, constraints, current pressure, or structural hierarchy?
- Does the job-entry table isolate an application response to framing?
- What is the exact labor margin: participation, hours, application, occupation entry, or promotion entry?
- Would this evidence belong in Week 5, Week 6, or both?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_object_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether it identifies:

- inherited cultural transmission;
- historical persistence;
- job-entry response to competition or gender-coded work;
- religion, reputation, and acceptable work;
- networking and leadership-entry conduct norms;
- local social-environment pressure;
- market-level wage-acceptance discipline;
- a Week 6 structural hierarchy object.

## Challenge

Add one row to `transfer/data/norm_designs_synthetic.csv` for a study of remote work, public visibility, or platform-mediated job search. Classify whether the design identifies a conduct norm, a price or constraint, or structural hierarchy. Then explain which labor margin moves first.

## Deliverables Checklist

- [ ] inherited-culture summary CSV
- [ ] inherited-culture gap table
- [ ] proxy diagnostic CSV
- [ ] job-entry summary and gap CSVs
- [ ] transfer classification CSV
- [ ] one-page memo distinguishing conduct norms from structural hierarchy
