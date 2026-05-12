# Code Lab 7: Violence, Safety, Mobility, And Labor-Market Access

**Course:** Special Topic 3 -- Gender Study  
**Module / Week:** Week 7 -- Violence, safety, mobility, and labor-market access  
**Associated chapter:** `07-violence-safety-mobility-and-labor-market-access.md`  
**Lab slug:** `07-violence-safety-mobility-and-labor-market-access`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchor:** [@adamsPrasslHuttunenNixZhang2024]  
**Secondary / challenge anchor:** [@folkeRickne2022]  
**Optional extension anchor:** [@macdonaldMontonenNix2025]  

## Why This Lab Exists

Week 7 asks students to treat safety as a labor-market constraint and welfare object. The bounded lab uses deterministic synthetic data to practice three moves:

1. **Reproduce** an administrative-linkage style workplace-violence exercise.
2. **Diagnose** whether outputs speak to exposure, reporting, retention, firm response, coworker spillovers, or hidden welfare.
3. **Transfer** the same logic to a harassment-risk sorting exercise.

The lab is a teaching analog. It is not an official replication of the anchor papers and it does not require confidential personnel records, police records, survey microdata, or tax data.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce event-time summaries around synthetic reported workplace violence events;
2. distinguish reported incidents from latent exposure and unsafe-workplace environments;
3. identify retention, separation, sick leave, coworker spillover, and firm hiring as different labor margins;
4. transfer the same margin discipline to harassment-risk sorting;
5. explain why wages and employment do not fully measure welfare when safety risk and hidden harm are present.

## Local Structure

```text
labs/07-violence-safety-mobility-and-labor-market-access/
  lab.md
  smoke.sh
  src/
    build_week7_synthetic_data.py
    reproduce_workplace_violence.py
    transfer_harassment_sorting.py
  original/
    reduced/
  transfer/
    data/
  output/
    reproduced/
    transfer/
```

## First Commands

```bash
conda run -n research python src/build_week7_synthetic_data.py

conda run -n research python src/reproduce_workplace_violence.py \
  --input original/reduced/adams_prassl_huttunen_nix_zhang_workplace_violence_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_harassment_sorting.py \
  --input transfer/data/folke_rickne_harassment_sorting_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/event_time_by_exposure.csv`
- `output/reproduced/separation_did.csv`
- `output/reproduced/firm_response_summary.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the observed event: violence exposure, a reported incident, or a firm environment?
- Which labor margins are observed: separation, sick leave, retention, wages, coworker response, or firm hiring?
- Why might reported incidents understate true exposure?
- What data would be needed to value hidden welfare losses inside continued employment?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Object:** State whether the exercise studies exposure, reporting, retention, firm response, or welfare.
2. **Variation:** State what changes at event firms after the reported incident and why the comparison is useful.
3. **Margin:** State which outcomes are labor margins and which are only partial welfare proxies.
4. **Limitation:** State why a reported-event design does not identify all workplace violence or harassment exposure.

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/harassment_risk_summary.csv`
- `output/transfer/risk_wage_tradeoff.csv`
- `output/transfer/transfer_diagnostics.csv`
- `output/transfer/transfer_note.txt`

Use the harassment-risk sorting exercise inspired by [@folkeRickne2022] to explain why a higher wage in a high-risk job is not necessarily a welfare improvement. State the exposure measure, observed labor margin, and hidden welfare component.

## Optional Frontier Prompt

Write a design memo inspired by [@macdonaldMontonenNix2025]. Do not estimate this extension in the bounded path. State:

- the hierarchy or power margin;
- the exposed workers and coworkers;
- the expected labor outcomes;
- the data needed to distinguish power asymmetry, favoritism, retaliation risk, and ordinary coworker relationships.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced event-time summaries
- [ ] separation difference-in-differences table
- [ ] firm-response summary
- [ ] one-page design memo
- [ ] transfer harassment-risk sorting summaries
- [ ] paragraph on hidden welfare and wage-risk interpretation
