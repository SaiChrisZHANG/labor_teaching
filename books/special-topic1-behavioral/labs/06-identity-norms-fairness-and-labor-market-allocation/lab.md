# Code Lab 6: Identity, Norms, Fairness, and Labor-Market Allocation

**Course:** Behavioral Labor  
**Module / Week:** Week 6 -- Identity, Norms, Fairness, and Labor-Market Allocation  
**Associated chapter:** `06-identity-norms-fairness-and-labor-market-allocation.md`  
**Lab slug:** `06-identity-norms-fairness-and-labor-market-allocation`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@masMoretti2009]  
**Secondary / challenge anchor:** [@brezaKaurShamdasani2018]  
**Optional frontier anchor:** [@huangPacelliShiZou2024] or [@minniNguyenSarsonsSrebot2026]  

## Why This Lab Exists

Week 6 studies identity, norms, fairness, peer pressure, firm culture, and manager transmission as labor-market objects. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact peer-at-work factbook inspired by [@masMoretti2009].
2. **Diagnose** whether a design identifies peer pressure, fairness, sorting, or norm transmission.
3. **Transfer** the same logic to pay comparisons, firm-culture sorting, and manager-driven norm transmission.

The lab does not require confidential employer, personnel, payroll, peer-network, or job-posting data.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a synthetic peer-pressure summary table and figure;
2. distinguish peer pressure from peer learning and common shocks;
3. identify the relevant norm or identity object in a workplace design;
4. name the social or reference group for fairness and peer-comparison claims;
5. classify effects as treatment, sorting, transmission, or equilibrium selection;
6. transfer the diagnostic framework to firm culture, algorithmic teams, and manager rotation settings.

## Local Structure

```text
labs/06-identity-norms-fairness-and-labor-market-allocation/
  lab.md
  smoke.sh
  src/
    build_week6_synthetic_data.py
    reproduce_peer_pressure.py
    transfer_fairness_culture.py
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
conda run -n research python src/build_week6_synthetic_data.py

conda run -n research python src/reproduce_peer_pressure.py \
  --input original/reduced/peer_pressure_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_fairness_culture.py \
  --fairness-input transfer/data/pay_comparison_synthetic.csv \
  --culture-input transfer/data/culture_sorting_synthetic.csv \
  --manager-input transfer/data/manager_transmission_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/peer_pressure_summary.csv`
- `output/reproduced/peer_pressure_effects.csv`
- `output/reproduced/peer_pressure_productivity.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What is the norm object: peer effort, team standard, visibility, or social sanction?
- Who is the reference group: shift peers, team peers, store peers, or managers?
- Which margin moves: effort units, productivity value, deviation from norm, or social penalty?
- Does the design identify peer pressure, peer learning, common shocks, or sorting?

## Part II. Diagnose

Write a short design memo with five paragraphs:

1. **Behavioral object:** Is the active channel identity, fairness, peer pressure, firm culture, or manager norm transmission?
2. **Labor margin:** Which outcome moves: effort, productivity, morale, quit intent, applications, retention, or promotion?
3. **Reference group:** Who provides the comparison: coworkers, managers, team, job applicants, or workers with the same identity?
4. **Identifying variation:** What varies: peer exposure, pay information, culture message, manager assignment, or hiring rule?
5. **Interpretation:** Is the evidence treatment, sorting, transmission, or equilibrium selection?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/pay_comparison_summary.csv`
- `output/transfer/pay_comparison_effects.csv`
- `output/transfer/culture_sorting_summary.csv`
- `output/transfer/manager_transmission_summary.csv`
- `output/transfer/fairness_culture_transfer.png`
- `output/transfer/transfer_note.txt`

Use [@brezaKaurShamdasani2018] to classify the pay-comparison design. Does the treatment shift fairness, beliefs, morale, effort, or quits? Then choose [@huangPacelliShiZou2024] or [@minniNguyenSarsonsSrebot2026] for the frontier transfer. Does the design identify culture-based sorting, manager norm transmission, or a bundle?

## Challenge

Propose one bounded transfer design:

- algorithmic team assignment;
- remote-work peer visibility;
- pay transparency by manager layer;
- job-posting culture language;
- manager rotation across teams;
- promotion norms in a training cohort.

For the chosen setting, state the norm or identity object, reference group, labor margin, identifying variation, and the strongest standard alternative.

## Deliverables Checklist

- [ ] run log
- [ ] peer-pressure summary table
- [ ] peer-pressure effect table
- [ ] peer-pressure productivity figure
- [ ] one-page diagnosis memo
- [ ] pay-comparison transfer tables
- [ ] culture-sorting and manager-transmission summaries
- [ ] short transfer paragraph naming treatment, sorting, transmission, or equilibrium selection
