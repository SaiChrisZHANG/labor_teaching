# Code Lab 16: Causal Inference With Spatial Data

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 16 - causal inference with spatial data  
**Associated chapter:** `16-causal-inference-with-spatial-data.md`  
**Lab slug:** `16-causal-inference-with-spatial-data`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** fixed effects, robust standard errors, weighted averages, simple matrix algebra, `pandas`  
**Core economic question:** When does geography identify an effect, threaten inference, or define the mechanism itself?  
**Core design / estimator:** contiguous-border comparison, spatially robust inference diagnostic, exposure mapping audit, shift-share exposure diagnostic  
**Source paper spine:** Dube, Lester, and Reich [@dubeLesterReich2010], Conley [@conley1999], Goldsmith-Pinkham, Sorkin, and Swift [@goldsmithPinkhamSorkinSwift2020], and Borusyak, Hull, and Jaravel [@borusyakHullJaravel2025]

## Why This Lab Exists

Lecture 16 treats spatial causal inference as identification logic under harder geography. This lab makes that discipline executable with synthetic teaching data. Students estimate a border-pair design, diagnose whether nearby comparisons are credible, and transfer the same design discipline to a shift-share exposure problem.

The lab is not an official replication. It is a bounded teaching path for spatial identification problems that appear in real applied papers.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate a simple contiguous-border design with border-pair fixed effects;
2. compare conventional, heteroskedastic-robust, and Conley-style spatial standard errors;
3. diagnose border balance, contaminated controls, and spatially correlated shocks;
4. distinguish bias problems from variance problems;
5. construct a shift-share exposure and inspect dominant contributions;
6. write a short spatial-design memo that names geography's role in the research design.

## Required Local Structure

```text
labs/16-causal-inference-with-spatial-data/
  README.md
  lab.md
  run-log.md
  smoke.sh
  environment/
    requirements.txt
  original/
    README.md
    source-notes.md
    reduced/
      border_counties_synthetic.csv
      neighbor_links_synthetic.csv
      sector_shares_synthetic.csv
      sector_shocks_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      shift_share_counties_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_border_design.py
    diagnose_spatial_design.py
    transfer_shift_share_spatial.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs four steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_border_design.py --counties original/reduced/border_counties_synthetic.csv --links original/reduced/neighbor_links_synthetic.csv --outdir output/reproduced
python src/diagnose_spatial_design.py --counties original/reduced/border_counties_synthetic.csv --links original/reduced/neighbor_links_synthetic.csv --outdir output/reproduced
python src/transfer_shift_share_spatial.py --counties transfer/data/shift_share_counties_synthetic.csv --shares original/reduced/sector_shares_synthetic.csv --shocks original/reduced/sector_shocks_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Border-Pair Design

### Objective

Estimate a simplified contiguous-border comparison inspired by minimum-wage border-pair designs.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/analysis_dataset.csv`.
4. Open `output/reproduced/border_design_estimates.csv`.
5. Open `output/reproduced/conley_cutoff_sensitivity.csv`.
6. Write one paragraph explaining what the border-pair fixed effects compare.

### Required Questions

- What is the unit of observation?
- What is the unit of treatment?
- What is the source of identifying variation?
- Why might nearby residuals be correlated even within a border design?
- What does the Conley-style correction change, and what does it not change?

### Minimum Output

- one paragraph defining the comparison;
- one table or paragraph comparing robust and spatially robust inference;
- one sentence stating that this is a synthetic teaching reproduction rather than an official replication.

## Part II. Diagnose Spatial Design Risk

### Objective

Evaluate whether the border comparison is credible enough to support a causal interpretation.

### Student Tasks

1. Open `output/reproduced/border_balance.csv`.
2. Open `output/reproduced/pair_balance_audit.csv`.
3. Open `output/reproduced/spillover_exposure_audit.csv`.
4. Open `output/reproduced/comparison_set_sensitivity.csv`.
5. Open `output/reproduced/diagnostic_prompts.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- Which predetermined variables are most imbalanced across the border?
- Which border pairs are most fragile?
- Are untreated counties exposed to treated neighbors?
- Does dropping fragile pairs change the estimate?
- Which problems are bias problems, and which are inference problems?

### Minimum Output

- one balance paragraph;
- one spillover paragraph;
- one inference paragraph;
- one comparison-set sensitivity paragraph;
- one final sentence classifying geography as source, threat, and/or mechanism.

## Part III. Transfer The Workflow To Shift-Share Exposure

### Objective

Transfer the design discipline from a border comparison to a shift-share exposure design.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/shift_share_exposure.csv`.
3. Open `output/transfer/dominant_contributions.csv`.
4. Open `output/transfer/share_diagnostics.csv`.
5. Open `output/transfer/transfer_estimates.csv`.
6. Write a short Transfer memo.

### Required Prompts

- What are the shares?
- What are the shocks?
- What is the geography?
- Is identifying variation dominated by a small number of sectors?
- How does the leave-one-out exposure differ from the baseline exposure?
- Is the identifying assumption mainly about shares, shocks, or both?

### Minimum Output

- one paragraph defining the shift-share exposure;
- one paragraph on dominant contributions and effective sector count;
- one paragraph comparing baseline and leave-one-out exposure;
- one paragraph stating what diagnostics would be needed before using the exposure as an instrument.

## Deliverables Checklist

- [ ] run log;
- [ ] border-comparison definition;
- [ ] robust versus spatially robust inference comparison;
- [ ] border-balance memo;
- [ ] spillover and contaminated-control memo;
- [ ] comparison-set sensitivity memo;
- [ ] shift-share transfer memo;
- [ ] final paragraph separating identification problems from inference corrections.

## Suggested Grading Rubric

- **Design clarity:** The memo names the unit, treatment, geography, and counterfactual.
- **Inference discipline:** The memo explains what spatial standard errors do and do not solve.
- **Interference awareness:** The memo treats nearby exposure as an identification issue.
- **Transfer conservatism:** The shift-share memo diagnoses shares and shocks rather than treating exposure as automatic exogeneity.
- **Replication discipline:** The memo states clearly that the lab is synthetic and does not invent a replication package.
