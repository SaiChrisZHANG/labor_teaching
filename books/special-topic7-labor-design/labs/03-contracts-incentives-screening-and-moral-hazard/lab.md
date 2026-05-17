# Week 3 Lab: Contracts, Incentives, Screening, And Moral Hazard

## Purpose

This lab turns the contracts and incentives lecture into a student-facing empirical design workflow. It does not replicate official estimates in Lazear, de Janvry and coauthors, or Kaur, Kremer, and Mullainathan. Instead, it uses deterministic synthetic data to practice how labor economists move from a principal-agent question to observable output, pay, sorting, subjective evaluation, and commitment margins.

Primary anchor: Lazear on performance pay and productivity [@lazear2000].

Challenge anchor: subjective performance evaluation and influence activities in de Janvry, He, Sadoulet, Wang, and Zhang [@deJanvryHeSadouletWangZhang2023]. Optional commitment path: self-control at work in Kaur, Kremer, and Mullainathan [@kaurKremerMullainathan2015].

## Workflow

### Reproduce

Run the synthetic teaching path and inspect `output/reproduced/performance_pay_summary.csv`.

The script creates a small worker-contract panel with:

- an hourly baseline period;
- a performance-pay period;
- worker ability, risk tolerance, and commitment indices;
- output, quality, hours, pay, and measured-task share;
- incumbent workers, continuing workers, exits, and entrants.

The object to reproduce is a reduced performance-pay fact:

```{math}
\Delta \bar y =
\bar y_{\text{performance pay}} -
\bar y_{\text{hourly baseline}}.
```

The exercise is pedagogical. It reproduces the design logic of a contract-change study, not the official estimates of the anchor paper.

### Diagnose

Open `output/diagnosed/incentive_sorting_decomposition.csv`, `output/diagnosed/hidden_object_diagnostics.csv`, and `output/diagnosed/subjective_evaluation_comparison.csv`.

For each diagnostic, classify whether the observed difference most likely reflects:

- within-worker incentive response;
- worker sorting into or out of the contract;
- risk shifting;
- measurable output versus quality;
- multitasking toward measured tasks;
- subjective-evaluation influence activities;
- commitment demand.

Answer four questions:

1. Which margins are observed directly in the synthetic data?
2. Which hidden objects remain latent even after the contract change?
3. How much of the raw output gain should be interpreted as incentives rather than sorting?
4. What welfare object would change the interpretation: productivity, worker risk, quality, retention, or worker surplus?

### Transfer

Open `output/transfer/contract_design_transfer.csv`. The transfer exercise asks students to move the same architecture to neighboring labor settings:

- subjective performance evaluation in public agencies;
- commitment contracts for attendance or target completion;
- promotion tournaments;
- team incentives in retail or service work;
- platform bonus schemes.

Write a short memo answering:

- What is the institution?
- What hidden object matters?
- What observable margin captures it?
- What institutional variation or experiment identifies it?
- What competing mechanisms must be separated?
- What welfare object matters?
- What is the main remaining threat?

## Running The Lab

From this lab directory:

```bash
ENV_NAME=research bash smoke.sh
```

The smoke path writes the bounded outputs and checks that they are nonempty. No external downloads are required.

## Submission Checklist

- one table summarizing output, quality, pay, and measured-task share by contract regime;
- one paragraph decomposing the raw output change into incentive response and sorting;
- one paragraph explaining why measured output is not effort;
- one transfer memo naming the institution, hidden object, observed margin, variation, identification strategy, welfare object, and main threat.
