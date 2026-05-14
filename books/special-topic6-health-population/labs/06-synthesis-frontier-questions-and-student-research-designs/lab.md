# Week 6 Lab: Synthesis, Frontier Questions, And Student Research Designs

## Purpose

This capstone lab turns the course into a student-facing research-design workflow. It does not replicate official estimates in Meyer and Mok or Albanesi and Kim. Instead, it uses deterministic synthetic data to practice how labor economists convert health and population mechanisms into credible designs about work, wages, productivity, job choice, firm response, household insurance, inequality, and worker welfare.

Primary anchor: Meyer and Mok on disability, earnings, income, and consumption [@meyerMok2019].

Challenge anchor: Albanesi and Kim on COVID labor-market incidence and heterogeneous adjustment [@albanesiKim2021].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/disability_onset_research_profile.csv`.

The script creates a worker panel around synthetic disability onset. It includes:

- pre-onset capacity, flexible jobs, firm accommodation capacity, household buffers, and program access;
- post-onset severity, accommodation, benefit receipt, job mobility, employment, hours, earnings, consumption, and welfare;
- a matched reference group with the same event-time structure.

The object to reproduce is a compact event-study-style profile:

```{math}
\Delta Y_{\tau}
=
\left(E[Y_{\tau} \mid A=1] - E[Y_{-1} \mid A=1]\right)
-
\left(E[Y_{\tau} \mid A=0] - E[Y_{-1} \mid A=0]\right),
```

where {math}`A` indicates the affected group and {math}`\tau` is event time. The lab reports design objects rather than official causal estimates.

### Diagnose

Open `output/diagnosed/research_design_diagnosis.csv`. For each pattern, classify whether the observed movement most likely reflects:

- work-capacity loss;
- dynamic labor-supply response;
- firm accommodation or retention;
- disability-program incentives or insurance;
- household buffering;
- dynamic selection;
- hidden welfare incidence.

Answer three questions:

1. Which outcomes move immediately at onset, and which adjust slowly?
2. Which patterns would be misread if the researcher observed only earnings?
3. Which mechanisms require firm or household data rather than worker-only data?

### Transfer

Open `output/transfer/frontier_design_transfer.csv`. The transfer exercise asks students to move the same architecture to six frontier settings:

- mental-health treatment and retention;
- caregiving onset and older-worker flexibility;
- disease exposure and migration;
- heat exposure and productivity;
- aging, automation, and accommodation;
- firm accommodation and employer power.

Write a short memo answering:

- What is the health or population mechanism?
- What is the labor object?
- What is the relevant unit of analysis?
- What is the timing or exposure logic?
- What counterfactual would make the design persuasive?
- What is the main remaining threat?
- What welfare object would wages or employment miss?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one event-study table summarizing employment, hours, earnings, consumption, accommodation, benefit receipt, mobility, and welfare around onset;
- one paragraph explaining which parts of the profile are work-capacity effects, program response, firm response, household insurance, and selection;
- one paragraph explaining why earnings alone are an incomplete welfare object;
- one transfer memo naming the mechanism, labor object, unit, timing, counterfactual, threat, and welfare object for a frontier project.
