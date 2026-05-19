# Code Lab 11: Causal ML, Policy Learning, And External Validity

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 11 - causal ML, policy learning, and external validity  
**Associated chapter:** `11-causal-ml-policy-learning-and-external-validity.md`  
**Lab slug:** `11-causal-ml-policy-learning-and-external-validity`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, CATEs, sample splitting, basic regression, `pandas`  
**Core economic question:** When can heterogeneous treatment effects support a feasible policy rule, and when does portability break?  
**Core design / estimator:** empirical welfare comparison, doubly robust policy-value scores, held-out value validation, source-to-target weighting  
**Source paper spine:** Kitagawa and Tetenov [@KitagawaTetenov2018], Athey and Wager [@atheyWager2021], Bansak et al. [@BansakFerwerdaHainmuellerEtAl2018], Allcott [@Allcott2015], Vivalt [@Vivalt2020], and Dehejia, Pop-Eleches, and Samii [@DehejiaPopElechesSamii2021]

## Why This Lab Exists

Lecture 11 argues that heterogeneity estimates are not policy rules. This lab makes that distinction executable. Students first reproduce the logic of empirical welfare maximization using a synthetic job-training setting. They then diagnose whether the selected rule is credible. Finally, they transfer the source-trained rule to a shifted target population and explain why external validity is a design claim rather than an algorithmic guarantee.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on policy value, regret, capacity constraints, overlap, fairness audits, and transportability.

## Learning Objectives

By the end of this lab, students should be able to:

1. define a policy class {math}`\Pi` and a policy rule {math}`\pi(x)`;
2. estimate and compare held-out policy value across simple rules;
3. distinguish predicted outcome levels from predicted causal gains;
4. report regret relative to the best rule in a feasible class;
5. diagnose overlap where the selected rule assigns treatment;
6. audit assignment rates across demographic groups;
7. compare source and target populations before making portability claims;
8. explain why a rule with high source value may have lower target value.

## Required Local Structure

```text
labs/11-causal-ml-policy-learning-and-external-validity/
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
      job_training_policy_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      job_training_target_synthetic.csv
  src/
    make_synthetic_data.py
    policy_learning_utils.py
    reproduce_policy_learning.py
    transfer_transportability.py
  output/
    reproduced/
    transfer/
```

## First Commands To Run

```bash
ENV_NAME=research bash smoke.sh
```

The smoke test runs three steps:

```bash
python src/make_synthetic_data.py
python src/reproduce_policy_learning.py --input original/reduced/job_training_policy_synthetic.csv --outdir output/reproduced
python src/transfer_transportability.py --source-input original/reduced/job_training_policy_synthetic.csv --target-input transfer/data/job_training_target_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Policy-Learning Workflow

### Objective

Learn and evaluate feasible job-training assignment rules using held-out policy value.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/learned_policy_rule.csv`.
4. Open `output/reproduced/policy_training_values.csv`.
5. Open `output/reproduced/policy_value_comparison.csv`.
6. Open `output/reproduced/cate_by_subgroup.csv`.

### Required Questions

- What is the policy class {math}`\Pi`?
- Which rule was selected on the training sample?
- Does the selected rule have high held-out value relative to simple rules?
- How does regret change when treat-all is treated only as a benchmark rather than as a capacity-feasible rule?
- How do subgroup CATEs differ from policy-value comparisons?

### Minimum Output

- one paragraph defining the policy class, capacity constraint, and value object;
- one table or paragraph comparing held-out value and regret across rules;
- one sentence explaining why this is a teaching reproduction of policy-learning logic rather than a replication of a published estimate.

## Part II. Diagnose Value, Overlap, And Fairness

### Objective

Evaluate whether the learned policy rule is credible enough to recommend.

### Student Tasks

1. Open `output/reproduced/overlap_diagnostics.csv`.
2. Open `output/reproduced/fairness_audit.csv`.
3. Open `output/reproduced/diagnostic_prompts.csv`.
4. Write a one-page Diagnose memo.

### Required Prompts

- Is policy value evaluated on held-out data?
- Does the selected-rule group have treated and untreated support?
- Are assignment rates similar across demographic groups?
- Does the selected rule mostly reproduce baseline risk, or does it use estimated net gains?
- Would a simpler threshold rule be easier to implement with similar value?

### Minimum Output

- one value-and-regret paragraph;
- one overlap paragraph;
- one fairness paragraph;
- one final sentence stating whether the rule is ready for implementation or only for further study.

## Part III. Transfer To A Target Population

### Objective

Apply the source-trained rule to a shifted target population and diagnose portability.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/source_vs_target_covariates.csv`.
3. Open `output/transfer/transport_weight_summary.csv`.
4. Open `output/transfer/policy_transfer_values.csv`.
5. Open `output/transfer/subgroup_shift.csv`.
6. Open `output/transfer/fairness_transfer_audit.csv`.
7. Write a short Transfer memo.

### Required Prompts

- How does the target population differ from the source evaluation sample?
- Does source-to-target weighting leave adequate effective support?
- Does the selected rule keep its value in the synthetic target population?
- Which differences are covariate shift, and which represent a changed treatment technology?
- What would a real paper need before claiming external validity?

### Minimum Output

- one source-target comparison paragraph;
- one target-weighting and support paragraph;
- one policy-value transfer paragraph;
- one paragraph on fairness and implementation after transfer.

## Deliverables Checklist

- [ ] run log;
- [ ] policy class definition;
- [ ] held-out policy-value comparison;
- [ ] regret interpretation;
- [ ] subgroup CATE paragraph;
- [ ] overlap diagnostics;
- [ ] fairness audit;
- [ ] source-target covariate comparison;
- [ ] target-weighting summary;
- [ ] transfer-value memo;
- [ ] final paragraph stating what the exercise identifies and what it does not identify.

## Suggested Grading Rubric

- **Research design clarity:** The memo distinguishes CATE estimation, policy learning, and prediction.
- **Value interpretation:** The memo uses held-out value and regret rather than in-sample fit.
- **Diagnostics:** The memo discusses overlap, capacity, and fairness constraints.
- **Transportability:** The memo explains why target value may differ from source value.
- **Conservatism:** The memo avoids claiming an official replication or deployment-ready rule.
