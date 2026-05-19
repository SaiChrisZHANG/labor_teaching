# Code Lab 18: Curating Network Data And Descriptive Statistics

**Course:** Empirical Methods for Applied Economics  
**Module / Week:** Week 18 - curating network data and descriptive statistics  
**Associated chapter:** `18-curating-network-data-and-descriptive-statistics.md`  
**Lab slug:** `18-curating-network-data-and-descriptive-statistics`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** grouped summaries, weighted averages, basic graph intuition, `pandas`  
**Core economic question:** How do researchers define and diagnose network objects before making causal claims?  
**Core design / estimator:** bipartite construction, one-mode projection, descriptive network statistics, definition sensitivity  
**Source paper spine:** Bayer, Ross, and Topa [@bayerRossTopa2008] with referral-transfer links to Beaman and Magruder [@beamanMagruderWhoGetsJob2012], Barwick et al. [@barwickReferralsInequalityLabor2024], and Friebel et al. [@friebelWhatDoEmployee2020]

## Why This Lab Exists

Lecture 18 argues that network definition is part of empirical design. This lab makes that claim executable at teaching scale. Students build a neighborhood-employer network object, compute descriptive statistics, diagnose how construction choices move the object, and transfer the same logic to directed referral data.

The lab is not an official replication. It uses deterministic synthetic data so students can focus on nodes, edges, weights, projection, boundaries, missing links, and descriptive interpretation.

## Learning Objectives

By the end of this lab, students should be able to:

1. construct a worker-neighborhood-employer bipartite object;
2. project the bipartite object into worker-level local employer exposure;
3. compute degree, weighted degree, components, homophily, and exposure summaries;
4. interpret a descriptive relationship between network exposure and labor outcomes without causal language;
5. diagnose sensitivity to edge definitions, boundaries, projection, missing links, and time aggregation;
6. construct a directed referral graph with in-degree, out-degree, and referral success measures;
7. write a short memo explaining what a network statistic means economically.

## Required Local Structure

```text
labs/18-curating-network-data-and-descriptive-statistics/
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
  transfer/
    README.md
    data-notes.md
    data/
      referrals_synthetic.csv
  src/
    make_synthetic_data.py
    network_utils.py
    reproduce_network_descriptives.py
    diagnose_network_definitions.py
    transfer_referral_network.py
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
python src/reproduce_network_descriptives.py --workers original/reduced/workers_synthetic.csv --outdir output/reproduced
python src/diagnose_network_definitions.py --workers original/reduced/workers_synthetic.csv --outdir output/reproduced
python src/transfer_referral_network.py --referrals transfer/data/referrals_synthetic.csv --outdir output/transfer
```

## Part I. Reproduce A Neighborhood-Employer Network Object

### Objective

Construct a compact residential labor-market network object inspired by Bayer, Ross, and Topa [@bayerRossTopa2008].

### Student Tasks

1. Read `original/source-notes.md`.
2. Run the smoke path.
3. Open `output/reproduced/neighborhood_employer_bipartite.csv`.
4. Open `output/reproduced/network_summary_by_worker.csv`.
5. Open `output/reproduced/network_metric_summary.csv`.
6. Open `output/reproduced/graph_components.csv`.
7. Open `output/reproduced/descriptive_relationship.csv`.

### Required Questions

- What are the nodes in the raw bipartite object?
- What edge rule creates worker-level local employer exposure?
- Is the main exposure a binary link, a weighted link, or a projection?
- Which workers have high degree because they have many local same-employer contacts?
- Does the descriptive relationship invite a causal interpretation? Why not?
- Why is this not an official replication of Bayer, Ross, and Topa?

### Minimum Output

- one paragraph defining the network object;
- one table or paragraph summarizing degree and weighted degree;
- one paragraph interpreting the descriptive relationship without causal language;
- one sentence stating that this is a synthetic teaching reproduction rather than an official replication.

## Part II. Diagnose Network Definitions

### Objective

Evaluate whether the network object is robust to plausible construction choices.

### Student Tasks

1. Open `output/reproduced/definition_sensitivity.csv`.
2. Open `output/reproduced/missing_link_audit.csv`.
3. Open `output/reproduced/projection_audit.csv`.
4. Open `output/reproduced/boundary_truncation_audit.csv`.
5. Open `output/reproduced/diagnostic_prompts.csv`.
6. Write a one-page Diagnose memo.

### Required Prompts

- How much do exposure means and descriptive slopes move across edge rules?
- Does the object change when the graph boundary excludes outside-frame employers?
- Are missing-link risks concentrated by group or survey-response status?
- Does the worker-worker projection mainly reflect large employers?
- Which descriptive statistic is most fragile?
- Which sensitivity check is measurement sensitivity rather than causal robustness?

### Minimum Output

- one node-and-edge paragraph;
- one boundary paragraph;
- one missing-link paragraph;
- one projection paragraph;
- one final sentence explaining which network definition you would defend.

## Part III. Transfer To Directed Referral Data

### Objective

Transfer the same curation logic to a directed referral-program setting.

### Student Tasks

1. Read `transfer/data-notes.md`.
2. Open `output/transfer/referral_graph_metrics.csv`.
3. Open `output/transfer/applicant_access_metrics.csv`.
4. Open `output/transfer/referral_inequality_summary.csv`.
5. Open `output/transfer/transfer_prompts.csv`.
6. Write a short Transfer memo.

### Required Prompts

- What does an edge mean in the directed referral graph?
- What is the difference between out-degree for referrers and in-degree for applicants?
- Which group receives more referral access in the synthetic data?
- What does referral success measure, and what does it miss?
- What extra design would be needed before claiming that referrals caused hiring?

### Minimum Output

- one directed-link paragraph;
- one in-degree/out-degree paragraph;
- one group-comparison paragraph;
- one paragraph explaining why the transfer is descriptive rather than causal.

## Deliverables Checklist

- [ ] run log;
- [ ] network object definition;
- [ ] bipartite and projected-summary interpretation;
- [ ] descriptive relationship memo;
- [ ] edge-definition sensitivity memo;
- [ ] missing-link and privacy paragraph;
- [ ] directed referral transfer memo;
- [ ] final paragraph explaining what network curation adds and what remains unresolved.

## Suggested Grading Rubric

| Component | Weight |
|---|---:|
| Network object definition | 20 |
| Descriptive network interpretation | 25 |
| Construction diagnostics | 30 |
| Referral transfer memo | 15 |
| Code organization and communication | 10 |

## Instructor Notes

- The data are synthetic and intentionally small enough for local smoke testing.
- The worker-neighborhood-employer object is a teaching analogue, not a confidential-data replication.
- The descriptive slope is designed to move when edge definitions change, so students can see that construction choices matter.
- The transfer task prepares students for Lecture 19 by making direction, timing, and exposure explicit before causal inference begins.
