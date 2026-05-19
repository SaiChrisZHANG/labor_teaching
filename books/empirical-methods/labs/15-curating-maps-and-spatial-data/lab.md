# Code Lab 15: Curating Maps And Spatial Data

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 15 - curating maps and spatial data  
**Associated chapter:** `15-curating-maps-and-spatial-data.md`  
**Lab slug:** `15-curating-maps-and-spatial-data`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** grouped aggregation, weighted averages, simple regressions, `pandas`  
**Core economic question:** How do geography, crosswalk, and access choices define the empirical object before causal inference begins?  
**Core design / estimator:** commuting-zone exposure construction, crosswalk diagnostics, MAUP sensitivity, geocoding-quality audit, distance-decay job access, travel-cost access  
**Source paper spine:** Autor, Dorn, and Hanson [@autorDornHanson2013], Chetty, Hendren, and Katz [@chettyHendrenKatz2016], Monte, Redding, and Rossi-Hansberg [@monteReddingRossiHansberg2018], and Miller [@miller2018]

## Why This Lab Exists

Lecture 15 treats spatial curation as empirical design. This lab makes that idea executable with synthetic teaching data. Students build a local labor-market exposure object, diagnose how geography and crosswalk choices change it, and transfer the logic to job-access measurement.

The lab is not an official replication. It is a bounded teaching path for the spatial-data decisions that a real applied paper would need to defend.

## Learning Objectives

By the end of this lab, students should be able to:

1. construct a local labor-market exposure from baseline weights and industry shocks;
2. explain how commuting-zone and county aggregation imply different estimands;
3. diagnose crosswalk weighting, geocoding quality, and edge-effect problems;
4. compare buffer, distance-decay, and travel-time access measures;
5. separate spatial measurement sensitivity from causal identification;
6. write a concise spatial-data audit trail for a replication package.

## Required Local Structure

```text
labs/15-curating-maps-and-spatial-data/
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
      tract_sector_employment_synthetic.csv
      sector_trade_shocks_synthetic.csv
      boundary_crosswalk_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      residential_tracts_synthetic.csv
      workplace_centers_synthetic.csv
  src/
    make_synthetic_data.py
    reproduce_commuting_zone_exposure.py
    diagnose_spatial_choices.py
    transfer_job_access.py
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
python src/reproduce_commuting_zone_exposure.py --tracts original/reduced/tract_sector_employment_synthetic.csv --shocks original/reduced/sector_trade_shocks_synthetic.csv --outdir output/reproduced
python src/diagnose_spatial_choices.py --tracts original/reduced/tract_sector_employment_synthetic.csv --shocks original/reduced/sector_trade_shocks_synthetic.csv --crosswalk original/reduced/boundary_crosswalk_synthetic.csv --outdir output/reproduced
python src/transfer_job_access.py --residences transfer/data/residential_tracts_synthetic.csv --centers transfer/data/workplace_centers_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Local Labor-Market Exposure

### Objective

Construct a commuting-zone exposure measure from tract-level baseline employment and industry shocks.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/cz_exposure.csv`.
4. Open `output/reproduced/tract_exposure_assignment.csv`.
5. Open `output/reproduced/county_vs_cz_exposure.csv`.
6. Open `output/reproduced/downstream_comparison.csv`.

### Required Questions

- What is the unit of observation?
- What is the unit of exposure?
- What is the unit of identifying variation in the constructed shock?
- Why do baseline industry weights matter?
- How does the estimand change when the same shock is aggregated to counties instead of commuting zones?

### Minimum Output

- one paragraph defining the exposure object;
- one paragraph explaining the baseline weights and denominator;
- one table or paragraph comparing commuting-zone and county exposure;
- one sentence explaining why this is a teaching reproduction of curation logic rather than an official replication.

## Part II. Diagnose Spatial Measurement Risk

### Objective

Evaluate whether the constructed spatial object is robust enough to enter a downstream design.

### Student Tasks

1. Open `output/reproduced/maup_sensitivity.csv`.
2. Open `output/reproduced/crosswalk_weighting_sensitivity.csv`.
3. Open `output/reproduced/geocoding_jitter_sensitivity.csv`.
4. Open `output/reproduced/boundary_edge_audit.csv`.
5. Open `output/reproduced/support_comparability.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- Which tracts are most sensitive to the county-vs-commuting-zone choice?
- Which crosswalk weighting rule is appropriate for residents, jobs, or land?
- Which places are most vulnerable to masking or geocoding error?
- Are edge places more likely to have ambiguous exposure?
- Which diagnostics are measurement diagnostics rather than causal-identification checks?

### Minimum Output

- one geography-sensitivity paragraph;
- one crosswalk-weighting paragraph;
- one geocoding or disclosure paragraph;
- one edge-effect paragraph;
- one final sentence stating whether the exposure object is ready for descriptive, causal, or structural use.

## Part III. Transfer The Workflow To Job Access

### Objective

Transfer the curation logic to a job-access measure inspired by job-suburbanization research.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/job_access_measures.csv`.
3. Open `output/transfer/access_group_comparison.csv`.
4. Open `output/transfer/buffer_vs_kernel_access.csv`.
5. Open `output/transfer/edge_effect_audit.csv`.
6. Write a short Transfer memo.

### Required Prompts

- When is an eight-mile buffer a defensible access object?
- When is distance-decay access more defensible?
- How does travel-time access differ from straight-line access for transit-dependent tracts?
- Which job centers create edge effects?
- What metadata would be needed if these travel times came from a live routing API?

### Minimum Output

- one paragraph comparing buffer, kernel, and travel-time access;
- one paragraph explaining group comparability;
- one paragraph on edge effects and omitted outside opportunities;
- one paragraph stating what would be needed before using the measure in a causal design.

## Deliverables Checklist

- [ ] run log;
- [ ] exposure-object definition;
- [ ] commuting-zone versus county comparison;
- [ ] crosswalk-weighting memo;
- [ ] geocoding and disclosure-risk memo;
- [ ] edge-effect memo;
- [ ] job-access transfer memo;
- [ ] final paragraph separating curation from causal inference.

## Suggested Grading Rubric

- **Economic object:** The memo defines the spatial object before discussing software.
- **Estimand discipline:** The memo explains what changes when geography changes.
- **Measurement diagnostics:** The memo uses the curation outputs rather than only describing maps.
- **Transfer conservatism:** The memo does not assume a buffer, kernel, or travel-time measure is automatically best.
- **Replication discipline:** The memo states what data vintages, crosswalks, routing assumptions, and confidentiality rules must be recorded.
