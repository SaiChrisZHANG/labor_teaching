# Week 3 Lab: Lifecycle Labor Allocation Around Family Health Shocks

## Purpose

This lab turns the Week 3 lecture into a bounded lifecycle labor-allocation exercise. It does not replicate official estimates in Fadlon and Nielsen or Ameriks and coauthors. Instead, it uses deterministic synthetic data to practice how labor economists distinguish income replacement, care demand, own work capacity, pension incentives, job flexibility, and dynamic selection after a severe family health shock.

Primary anchor: Fadlon and Nielsen on family labor-supply responses to severe health shocks [@fadlonNielsen2021].

Challenge paper: Ameriks and coauthors on older-worker flexibility and late-life work [@ameriksBriggsCaplin2020].

## Workflow

### Reproduce

Run the synthetic event-time path and inspect `output/reproduced/family_health_shock_event_study.csv`.

The script creates a small household-event panel with:

- treated households observed before and after a severe family health shock;
- comparison households observed over the same event-time window;
- age, pension eligibility, baseline assets, job flexibility, care intensity, mortality risk, own hours, spouse hours, household earnings, savings drawdown, retirement claiming, bridge-job transitions, and post-retirement work.

The object to reproduce is the structure of a dynamic family-response event study:

```{math}
Y_{it} =
\sum_{\tau \neq -1} \beta_{\tau}
\mathbf{1}\{t - T_i = \tau\}
+ \alpha_i + \lambda_t + \varepsilon_{it}.
```

The lab reports treated-minus-comparison profiles by event time. It does not claim to recover official administrative or survey estimates.

### Diagnose

Open `output/diagnosed/lifecycle_mechanism_diagnosis.csv`. For each event-time window, classify whether the observed labor-market movement most closely reflects:

- income replacement;
- care-time demand;
- own work-capacity loss;
- pension or benefit incentives;
- job-flexibility response;
- dynamic selection or anticipation.

Answer three questions:

1. Which labor outcome moves immediately after the shock?
2. Which outcome shows medium-run reallocation rather than short-run disruption?
3. Where would you worry most about anticipation, hidden care intensity, pension selection, or employer flexibility?

### Transfer

Open `output/transfer/lifecycle_design_transfer.csv`. The transfer exercise asks students to move the same logic to four settings:

- fertility timing and child penalties;
- caregiving onset;
- pension eligibility reform;
- bridge-job, rehire, or flexible late-life work transitions.

Write a short memo answering:

- What is the event or state transition?
- What is the labor outcome?
- What identifies the design?
- Which channel is most visible?
- Which channel remains bundled or offstage?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one event-study table comparing at least four labor margins before and after the family health shock;
- one paragraph separating income replacement from care-time demand;
- one paragraph explaining how pension eligibility or retirement savings changes the response;
- one paragraph on post-retirement work, bridge jobs, rehiring, or late-life flexibility;
- one transfer paragraph linking a lifecycle event, labor margin, identifying variation, and remaining threat.
