# Week 2 Lab: Disability, Chronic Conditions, Labor Supply, And Job Choice

## Purpose

This lab turns the Week 2 lecture into a bounded disability-onset and accommodation exercise. It does not replicate official estimates in Meyer and Mok or Hill, Maestas, and Mullen. Instead, it uses deterministic synthetic data to practice how labor economists separate work-capacity effects, program incentives, workplace accommodation, local labor demand, and selection into disability status or benefit receipt.

Primary anchor: Meyer and Mok on long-run disability effects for earnings, income, and consumption [@meyerMok2019].

Challenge paper: Hill, Maestas, and Mullen on employer accommodation and labor supply of disabled workers [@hillMaestasMullen2016].

## Workflow

### Reproduce

Run the synthetic onset path and inspect `output/reproduced/disability_onset_event_study.csv`.

The script creates a small worker-event panel with:

- treated workers observed before and after disability onset;
- matched comparison workers observed over the same event-time window;
- latent work capacity, condition severity, local labor demand, accommodation access, benefit receipt, job mobility, employment, hours, earnings, and occupation feasibility.

The object to reproduce is the structure of a disability-onset event study:

```{math}
Y_{it} =
\sum_{\tau \neq -1} \beta_{\tau}
\mathbf{1}\{t - T_i = \tau\}
+ \alpha_i + \lambda_t + \varepsilon_{it}.
```

The lab reports treated-minus-comparison profiles by event time. It does not claim to recover official administrative or survey estimates.

### Diagnose

Open `output/diagnosed/mechanism_diagnosis.csv`. For each event-time window, classify whether the observed labor-market movement most closely reflects:

- direct work-capacity effects;
- program incentives and benefit receipt;
- employer accommodation or workplace treatment;
- local labor-demand conditions;
- selection into disability status or program use.

Answer three questions:

1. Which labor outcome moves immediately after onset?
2. Which outcome shows longer-run scarring?
3. Where would you worry most about program selection or employer accommodation endogeneity?

### Transfer

Open `output/transfer/disability_design_transfer.csv`. The transfer exercise asks students to move the same logic to four settings:

- acute hospitalization;
- accommodation access;
- disability-program threshold;
- treatment or return-to-work reform.

Write a short memo answering:

- What is the health object?
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

- one event-study table comparing at least three labor margins before and after disability onset;
- one paragraph separating direct capacity effects from program incentives;
- one paragraph explaining how accommodation changes labor supply or exit;
- one transfer paragraph linking a health object, labor margin, identifying variation, and remaining threat.
