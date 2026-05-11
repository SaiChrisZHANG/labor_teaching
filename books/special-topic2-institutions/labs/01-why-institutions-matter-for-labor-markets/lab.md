# Code Lab 1: Why Institutions Matter For Labor Markets

**Course:** Labor Markets and Political/Cultural Institutions  
**Module / Week:** Week 1 -- Why Institutions Matter for Labor Markets  
**Associated chapter:** `01-why-institutions-matter-for-labor-markets.md`  
**Lab slug:** `01-why-institutions-matter-for-labor-markets`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 2 core hours + 1 challenge hour  
**Primary anchors:** [@guisoSapienzaZingales2006; @alesinaAlganCahucGiuliano2015; @munshiRosenzweig2016]  

## Why This Lab Exists

Week 1 asks students to treat institutions as empirical objects rather than atmosphere. The lab uses synthetic data to practice three moves:

1. **Reproduce** a compact factbook connecting inherited norms, trust, family obligation, and labor outcomes.
2. **Diagnose** which columns are institutional objects, which are mechanisms, and which are outcomes.
3. **Transfer** the same logic to network insurance, migration, and wage gaps.

The lab is a teaching analog. It is not an official replication of any anchor paper.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a small descriptive institutional-labor factbook from local synthetic data;
2. distinguish institutional objects, mechanisms, and outcomes in a data table;
3. explain why inherited culture or network structure is not automatically causal evidence;
4. diagnose persistence mechanisms when informal institutions survive formal rule changes;
5. transfer the Week 1 framework to a network-and-mobility setting.

## Local Structure

```text
labs/01-why-institutions-matter-for-labor-markets/
  lab.md
  smoke.sh
  src/
    build_week1_synthetic_data.py
    reproduce_inherited_norms.py
    transfer_network_mobility.py
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
conda run -n research python src/build_week1_synthetic_data.py

conda run -n research python src/reproduce_inherited_norms.py \
  --input original/reduced/inherited_norms_labor_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_network_mobility.py \
  --input transfer/data/network_mobility_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/norm_group_summary.csv`
- `output/reproduced/institution_mechanism_outcome_map.csv`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the institutional object?
- Which variables are plausible mechanisms?
- Which variables are labor-market outcomes?
- Why should this factbook not be interpreted as causal without further design?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Object:** Is the main institution formal, informal, or hybrid?
2. **Mechanism:** Does the pattern operate through trust, family insurance, mobility costs, compliance, or political support for regulation?
3. **Outcome:** Which labor outcomes are measured directly?
4. **Threat:** Which omitted prices, policies, local labor demand, or selection channels could mimic the pattern?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/network_group_summary.csv`
- `output/transfer/mobility_gap_decomposition.csv`
- `output/transfer/transfer_note.txt`

Use the same logic for the network exercise. State why network insurance can reduce migration even when destination wages are higher, and state what design would be needed to separate insurance from selection.

## Challenge

Choose one later course domain: enforcement, informality, worker voice, identity, persistence, reform, or comparative institutions. Sketch a data table with one institutional object, two mechanisms, two labor outcomes, and one plausible source of identifying variation.

## Deliverables Checklist

- [ ] run log
- [ ] reproduced summary CSVs
- [ ] one-page diagnosis memo
- [ ] transfer summary CSVs
- [ ] short paragraph distinguishing descriptive associations, mechanisms, and causal claims
