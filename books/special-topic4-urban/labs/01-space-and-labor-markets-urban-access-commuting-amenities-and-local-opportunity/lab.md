# Week 1 Lab: Local Labor Markets, Job Access, And Spatial Opportunity

## Purpose

This lab turns the Week 1 framework into a bounded empirical workflow. It does not replicate the confidential or full data in the anchor papers. Instead, it uses a deterministic synthetic city to practice the objects that appear in spatial job-search and local labor-market research.

Primary anchor: Manning and Petrongolo on spatial job search and local labor markets [@manningPetrongolo2017].

Challenge anchor: Monte, Redding, and Rossi-Hansberg on commuting, migration, and local employment elasticities [@monteReddingRossiHansberg2018].

Optional frontier anchor: Miller on job suburbanization and unequal employment access [@miller2023].

## Workflow

### Reproduce

Run the synthetic access path and inspect `output/reproduced/job_access_by_residence.csv`.

The script constructs residential zones, workplace zones, wages, rents, amenities, and generalized commuting costs. For each residence and travel-cost threshold, it computes:

- accessible jobs,
- average accessible wage,
- average generalized commute cost,
- best net opportunity,
- an access-based local labor-market label.

The object to reproduce is the chapter's job-access object:

```{math}
\mathcal{J}_i(c) = \{j : \tau(d_{ij}) \leq c\}.
```

### Diagnose

Open `output/diagnosed/spatial_objects_map.csv`. For each object, classify whether it is about access, realized commute, nominal wage, rent, amenity, or spatial equilibrium.

The diagnostic questions are:

1. What is the local labor market in this exercise?
2. What counts as access?
3. What is the equilibrium object?
4. Is the result about sorting, productivity, or commuting frictions?
5. Which comparisons use workplace measures, and which use residential measures?

### Transfer

Open `output/transfer/commuting_shock_summary.csv`. The transfer exercise lowers generalized commuting costs for selected residence-workplace pairs. Interpret the resulting change in access as a commuting-friction exercise, not as a migration exercise.

Write a short paragraph answering:

- Who gains access when travel costs fall?
- Does the local wage distribution change, or does the feasible set change?
- What would be different if the shock induced residential migration?
- How could the same logic apply to job suburbanization in the spirit of Miller [@miller2023]?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path runs the complete bounded exercise and checks that the three output files were written. No confidential data or external downloads are required.

## Submission Checklist

- one table or figure describing access by residence;
- one paragraph distinguishing access from realized commute;
- one paragraph distinguishing nominal wages from net opportunity;
- one transfer paragraph explaining why a place-specific access result can still teach a general labor-market mechanism.
