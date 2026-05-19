# Code Lab 19: Causal Inference With Network Data

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 19 - causal inference with network data  
**Associated chapter:** `19-causal-inference-with-network-data.md`  
**Lab slug:** `19-causal-inference-with-network-data`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** potential outcomes, experiments, clustered inference, basic network notation, `pandas`  
**Core economic question:** How does network structure change identification, exposure construction, and inference?  
**Core design / estimator:** peer exposure, exposure mappings, randomized saturation intuition, randomization inference, dyadic dependence  
**Source paper spine:** Cornelissen, Dustmann, and Schonberg [@cornelissenPeerEffectsWorkplace2017] with transfer links to Pallais and Sands [@pallaisEvidenceFieldExperiments2016] and Barwick et al. [@barwickJobReferralNetwork2019]

## Why This Lab Exists

Lecture 19 argues that network causal inference begins when links define exposure, interference, or dependence. This lab makes that argument executable at teaching scale. Students build a workplace peer-exposure object, compare exposure mappings, diagnose reflection and partial-interference risks, and transfer the same logic to referral dyads.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on the design architecture: peer group, graph definition, timing, exposure mapping, saturation, randomization inference, and pair-aware uncertainty.

## Learning Objectives

By the end of this lab, students should be able to:

1. construct leave-one-out team peer measures and graph-neighbor exposure measures;
2. estimate direct and spillover associations under alternative exposure mappings;
3. explain why contemporaneous peer outcomes create reflection risk;
4. interpret randomized saturation summaries as exposure variation;
5. run a bounded randomization-inference exercise under a known assignment rule;
6. diagnose when partial interference is plausible or fragile;
7. estimate a referral dyad model and compare naive and pair-aware standard errors;
8. write a memo separating what is identified from what remains an assumption.

## Required Local Structure

```text
labs/19-causal-inference-with-network-data/
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
      workplace_peers_synthetic.csv
      coworker_edges_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      referral_dyads_synthetic.csv
  src/
    make_synthetic_data.py
    network_causal_utils.py
    reproduce_peer_effects.py
    diagnose_network_causality.py
    transfer_referral_dyads.py
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
python src/reproduce_peer_effects.py --workers original/reduced/workplace_peers_synthetic.csv --edges original/reduced/coworker_edges_synthetic.csv --outdir output/reproduced
python src/diagnose_network_causality.py --workers original/reduced/workplace_peers_synthetic.csv --edges original/reduced/coworker_edges_synthetic.csv --outdir output/reproduced
python src/transfer_referral_dyads.py --referrals transfer/data/referral_dyads_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Workplace Peer-Exposure Design

### Objective

Construct a compact workplace peer-effects object inspired by Cornelissen, Dustmann, and Schonberg [@cornelissenPeerEffectsWorkplace2017].

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/team_saturation_summary.csv`.
4. Open `output/reproduced/leave_one_out_peer_measures.csv`.
5. Open `output/reproduced/direct_spillover_estimates.csv`.
6. Open `output/reproduced/exposure_mapping_estimates.csv`.

### Required Questions

- What is the peer group in the team exposure mapping?
- What is the graph-neighbor exposure mapping?
- Which estimates compare own treatment at fixed exposure, and which compare exposure at fixed treatment?
- Why should the coefficients be described as teaching estimates rather than a replication result?
- How does saturation create variation in untreated exposure?

### Minimum Output

- one paragraph defining the peer group and graph;
- one table or paragraph summarizing direct and spillover estimates;
- one paragraph explaining what the saturation contrast teaches;
- one sentence stating that this is a synthetic teaching reproduction rather than an official replication.

## Part II. Diagnose Network-Causal Assumptions

### Objective

Evaluate whether the peer-effect object is robust to plausible network-causal assumptions.

### Student Tasks

1. Open `output/reproduced/exposure_mapping_sensitivity.csv`.
2. Open `output/reproduced/reflection_diagnostics.csv`.
3. Open `output/reproduced/randomization_inference_summary.csv`.
4. Open `output/reproduced/partial_interference_audit.csv`.
5. Open `output/reproduced/diagnostic_prompts.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- How much do spillover estimates move across team, graph, and weighted graph exposure mappings?
- Why is contemporaneous peer productivity reflection-prone?
- What assignment rule is respected by the randomization-inference exercise?
- Does the synthetic design make partial interference plausible across teams?
- Which diagnostic is about identification and which is about inference?

### Minimum Output

- one exposure-mapping paragraph;
- one reflection paragraph;
- one randomization-inference paragraph;
- one partial-interference paragraph;
- one final sentence explaining which causal claim you would and would not defend.

## Part III. Transfer To Referral Dyads

### Objective

Transfer the same network-causal logic to employee-applicant referral pairs.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/dyadic_model_estimates.csv`.
3. Open `output/transfer/dyadic_dependence_audit.csv`.
4. Open `output/transfer/referral_access_summary.csv`.
5. Open `output/transfer/transfer_prompts.csv`.
6. Write a short Transfer memo.

### Required Prompts

- What is the estimating unit in the referral dyad model?
- Why do dyads sharing a referrer or applicant create dependence?
- How do naive and pair-aware standard errors differ in the teaching output?
- What does same-group referral identify in the synthetic model, and what would be needed for a causal claim?
- How does the estimand differ from the workplace peer-exposure design?

### Minimum Output

- one dyad-definition paragraph;
- one inference paragraph comparing standard errors;
- one access-inequality paragraph;
- one paragraph explaining why the transfer is a design template rather than an official replication.

## Deliverables Checklist

- [ ] run log;
- [ ] peer group and graph-exposure definition;
- [ ] direct and spillover estimate interpretation;
- [ ] exposure-mapping sensitivity memo;
- [ ] reflection and partial-interference paragraph;
- [ ] randomization-inference paragraph;
- [ ] referral dyad transfer memo;
- [ ] final paragraph explaining when network-targeted methods are needed beyond Lectures 1 to 5.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Peer exposure and saturation interpretation | 25 |
| Exposure-mapping and reflection diagnostics | 30 |
| Randomization and partial-interference reasoning | 20 |
| Referral dyad inference transfer | 15 |
| Code organization and communication | 10 |

## Instructor Notes

- The data are synthetic and intentionally small enough for local smoke testing.
- The reproduce path is a teaching analogue, not a confidential-data replication.
- The generated outcome depends on direct treatment and graph exposure, so students can see why exposure mappings matter.
- The reflection diagnostic intentionally uses contemporaneous peer outcomes to show why those regressions are hard to interpret causally.
- The transfer task uses a linear probability model for simplicity; the inference lesson is about dyadic dependence, not binary-response modeling.
