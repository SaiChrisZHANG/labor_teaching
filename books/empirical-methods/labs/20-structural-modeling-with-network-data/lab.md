# Code Lab 20: Structural Modeling With Network Data

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 20 - structural modeling with network data  
**Associated chapter:** `20-structural-modeling-with-network-data.md`  
**Lab slug:** `20-structural-modeling-with-network-data`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** network notation, peer effects, interference, structural estimation basics, `pandas`  
**Core economic question:** When does a labor-market network counterfactual require modeling link formation or network-mediated behavior?  
**Core design / estimator:** link-formation model, behavior-on-network equation, moment validation, fixed-network versus endogenous-link counterfactual  
**Source paper spine:** Mele [@mele2017structural] and Graham [@graham2017econometric], with transfer to Galenianos [@galenianos2021referral] and Dustmann et al. [@dustmann2016referral]

## Why This Lab Exists

Lecture 20 argues that structural network models are useful when the policy changes links, information flows, search opportunities, matching sets, or equilibrium behavior. This lab makes that claim executable at teaching scale. Students estimate a simple formation model, connect it to network moments, estimate a behavior-on-network equation, and compare fixed-network and endogenous-link counterfactuals.

The lab is not an official replication. It uses deterministic synthetic data because no official replication package for the anchor papers is locally available in the repository. The goal is to teach the workflow: define the network, state the formation and behavior assumptions, choose moments that matter for the counterfactual, validate, and write down what remains unsupported.

## Learning Objectives

By the end of this lab, students should be able to:

1. estimate a simple dyadic link-formation model;
2. compute moments that matter for structural network counterfactuals;
3. estimate a behavior-on-network equation for a labor-market outcome;
4. compare fixed-network and endogenous-link policy simulations;
5. diagnose which moments validate formation and which validate behavior;
6. explain why clustering and strategic formation can be validation gaps for dyadic models;
7. transfer the logic to referral-search and cross-group matching opportunities;
8. write a memo separating teaching simulation from credible empirical evidence.

## Required Local Structure

```text
labs/20-structural-modeling-with-network-data/
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
      workers_synthetic.csv
      dyad_opportunities_synthetic.csv
      network_edges_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      referral_search_synthetic.csv
  src/
    make_synthetic_data.py
    network_structural_utils.py
    reproduce_network_formation.py
    diagnose_structural_network.py
    transfer_referral_search.py
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
python src/reproduce_network_formation.py --nodes original/reduced/workers_synthetic.csv --dyads original/reduced/dyad_opportunities_synthetic.csv --edges original/reduced/network_edges_synthetic.csv --outdir output/reproduced
python src/diagnose_structural_network.py --nodes original/reduced/workers_synthetic.csv --dyads original/reduced/dyad_opportunities_synthetic.csv --edges original/reduced/network_edges_synthetic.csv --outdir output/reproduced
python src/transfer_referral_search.py --referrals transfer/data/referral_search_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Structural Network Workflow

### Objective

Construct a compact version of the structural logic in Mele and Graham: link formation is a modeled object, not a nuisance.

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/formation_model_estimates.csv`.
4. Open `output/reproduced/network_moments.csv`.
5. Open `output/reproduced/behavior_on_network_estimates.csv`.
6. Open `output/reproduced/fixed_vs_endogenous_counterfactual.csv`.

### Required Questions

- Which dyad characteristics predict links in the teaching formation model?
- Which network moments are most relevant for a cross-group link policy?
- What does the behavior equation treat as the network-mediated channel?
- How does the policy effect differ when links are fixed versus endogenous?
- Why should the estimates be described as teaching estimates rather than replication results?

### Minimum Output

- one paragraph describing the link-formation model;
- one table or paragraph summarizing network moments;
- one paragraph interpreting the behavior-on-network coefficient;
- one paragraph comparing fixed-network and endogenous-link counterfactuals;
- one sentence stating that this is a synthetic teaching reproduction rather than an official replication.

## Part II. Diagnose Structural Validation

### Objective

Evaluate whether the model fits the network and behavior moments needed for the counterfactual.

### Student Tasks

1. Open `output/reproduced/validation_moments.csv`.
2. Open `output/reproduced/behavior_fit_summary.csv`.
3. Open `output/reproduced/assumption_audit.csv`.
4. Open `output/reproduced/counterfactual_sensitivity.csv`.
5. Open `output/reproduced/diagnostic_prompts.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- Which moments are well disciplined by a dyadic formation model?
- Why is clustering listed as a validation gap?
- What assumptions are needed for the behavior equation to remain stable under policy?
- Which Lecture 19 reduced-form design would best discipline the structural counterfactual?
- What additional data would be needed before estimating the model on a real labor market?

### Minimum Output

- one formation-validation paragraph;
- one behavior-validation paragraph;
- one fixed-versus-endogenous counterfactual paragraph;
- one paragraph explaining a missing assumption or validation gap;
- one final sentence explaining which structural claim you would not defend yet.

## Part III. Transfer To Referral Search

### Objective

Transfer the formation-and-behavior logic to a referral-search setting inspired by Galenianos and Dustmann et al.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/callback_model_estimates.csv`.
3. Open `output/transfer/referral_access_summary.csv`.
4. Open `output/transfer/referral_policy_counterfactuals.csv`.
5. Open `output/transfer/added_cross_group_referrals.csv`.
6. Open `output/transfer/transfer_prompts.csv`.
7. Write a short Transfer memo.

### Required Prompts

- What is the economic meaning of a referral link in this transfer?
- Which scenario changes information quality on existing links?
- Which scenario changes the set of observed referral opportunities?
- What happens to cross-group referral share and the applicant-group callback gap?
- What real validation evidence would be needed for a publishable paper?

### Minimum Output

- one paragraph defining the referral link;
- one paragraph comparing fixed-link and endogenous-link scenarios;
- one paragraph on inequality or callback gaps;
- one paragraph explaining why this transfer is a design template, not a policy estimate.

## Deliverables Checklist

- [ ] run log;
- [ ] formation-model interpretation;
- [ ] network-moment table or summary;
- [ ] behavior-on-network interpretation;
- [ ] fixed-versus-endogenous counterfactual comparison;
- [ ] validation memo;
- [ ] referral-search transfer memo;
- [ ] final paragraph explaining when structural network models add value beyond Lectures 18 and 19.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Formation model and network moments | 25 |
| Behavior-on-network interpretation | 20 |
| Fixed versus endogenous counterfactual reasoning | 25 |
| Validation and assumption audit | 20 |
| Referral-search transfer memo | 10 |

## Instructor Notes

- The synthetic data are intentionally small enough for local smoke testing.
- The link-formation model is a linear probability teaching approximation, not a frontier estimator.
- The behavior equation is useful for seeing how counterfactuals depend on network exposure, but it is not causal without stronger design evidence.
- The transfer exercise separates better information on existing links from a policy that adds cross-group referral opportunities.
- The strongest student memos will explain what the model can show and what a real empirical project would still need to validate.
