# Code Lab 4: Worker Voice, Collective Action, and Bargaining Institutions

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 4 -- Worker Voice, Collective Action, and Bargaining Institutions  
**Associated chapter:** `04-worker-voice-collective-action-and-bargaining-institutions.md`  
**Lab slug:** `04-worker-voice-collective-action-and-bargaining-institutions`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@dinardoLee2004]  
**Secondary / challenge anchor:** [@frandsen2021]  
**Spillover extension anchor:** [@fortinLemieuxLloyd2021]  
**Voice / governance extension anchor:** [@harjuJagerSchoefer2021]  
**Political spillover extension anchor:** [@feigenbaumHertelFernandezWilliamson2018]  

## Why This Lab Exists

Week 4 treats worker voice and bargaining institutions as organization, coverage, bargaining, governance, and spillover objects. The lab uses synthetic data to practice three moves:

1. **Reproduce** the logic of a close certification-election design in the spirit of [@dinardoLee2004].
2. **Diagnose** whether evidence is speaking to organized establishments, workers, payroll, separations, organization formation, or firm response in the spirit of [@frandsen2021].
3. **Transfer** the same diagnostic language to spillover, representation-threshold, organizing-demand, and political-feedback settings.

The lab is a teaching analog. It is not an official replication of any anchor paper.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small close-election summary around a majority threshold;
2. distinguish recognition, membership, coverage, and organization formation in a data table;
3. compare establishment-level outcomes with worker-level outcomes;
4. separate direct effects on organized units from spillovers to uncovered workers;
5. classify whether a design identifies wages, employment, payroll, governance, organizing demand, spillovers, or political participation.

## Local Structure

```text
labs/04-worker-voice-collective-action-and-bargaining-institutions/
  lab.md
  smoke.sh
  src/
    build_week4_synthetic_data.py
    reproduce_union_close_elections.py
    transfer_voice_spillover_classifier.py
  original/
    source-notes.md
    reduced/
  transfer/
    data-notes.md
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week4_synthetic_data.py

conda run -n research python src/reproduce_union_close_elections.py \
  --elections original/reduced/close_elections_synthetic.csv \
  --workers original/reduced/matched_worker_establishment_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_voice_spillover_classifier.py \
  --input transfer/data/collective_institution_designs_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and close-election script. Inspect:

- `output/reproduced/close_election_group_summary.csv`
- `output/reproduced/rd_bandwidth_differences.csv`
- `output/reproduced/worker_establishment_summary.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- Which variable represents legal recognition?
- Which variable represents worker demand for organization?
- Which outcomes are establishment-level outcomes?
- Which outcomes are worker-level outcomes?
- Why does a close-election design identify marginal recognition around the threshold rather than all unionization?

## Part II. Diagnose

Write a short design memo comparing two objects:

1. **DiNardo-Lee object:** establishments barely win or lose recognition in union certification elections [@dinardoLee2004].
2. **Frandsen object:** matched worker-establishment data track payroll, careers, separations, and composition around unionization [@frandsen2021].

Use the following checklist:

- Does the design identify organization formation, direct treatment on organized units, worker sorting, wage-setting, employment, payroll, or firm response?
- What is the unit of observation?
- Which labor-market margin is observed?
- Which side of the market is moving most clearly?
- What spillover or uncovered-worker margin could be missing?

## Part III. Transfer

Run the transfer classifier. Inspect:

- `output/transfer/design_classification.csv`
- `output/transfer/design_object_counts.csv`
- `output/transfer/transfer_note.txt`

For each transfer design, state whether the design identifies:

- organization formation;
- wages, employment, or payroll;
- governance and worker voice;
- spillovers to uncovered workers;
- organizing demand;
- voting or political participation;
- a legal feedback from politics to worker organization.

Then propose one bounded transfer:

1. compare direct and spillover incidence in a wage-distribution exercise;
2. reinterpret a close-election design through organization formation;
3. separate labor-market and political margins of the same right-to-work shock.

## Challenge

Design a synthetic panel with a sectoral bargaining shock and a works-council threshold. Include one coverage measure, one membership measure, one governance measure, one uncovered-worker wage measure, and one political-participation measure. State which variable would move first under a coverage extension and which would move first under a representation-threshold rule.

## Deliverables Checklist

- [ ] close-election group summary CSV
- [ ] bandwidth difference CSV
- [ ] worker-establishment summary CSV
- [ ] one-page diagnosis memo
- [ ] transfer classification CSV
- [ ] short paragraph naming the observed margin and identifying variation
