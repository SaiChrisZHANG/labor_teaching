# Code Lab 5: Incentives, Contracts, Reciprocity, and Workplace Behavior

**Course:** Behavioral Labor  
**Module / Week:** Week 5 -- Incentives, Contracts, Reciprocity, and Workplace Behavior  
**Associated chapter:** `05-incentives-contracts-reciprocity-and-workplace-behavior.md`  
**Lab slug:** `05-incentives-contracts-reciprocity-and-workplace-behavior`  
**Scope tier:** Minimal bounded teaching path  
**Primary language:** Python  
**Estimated student time:** 3 core hours + 1 challenge hour  
**Primary anchor:** [@dellaVignaListMalmendierRao2022]  
**Secondary / challenge anchor:** [@kelley2024monitoring]  
**Optional extension anchor:** [@deJanvrySadouletSuriWang2023]  

## Why This Lab Exists

Week 5 turns workplace incentives into applied labor research objects. The bounded path uses deterministic synthetic data to practice three moves:

1. **Reproduce** a compact gift-exchange workplace factbook that separates extra work from productivity.
2. **Diagnose** whether a treatment changes pay, reciprocity, monitoring, evaluation, or contract framing.
3. **Transfer** the same logic to monitoring intensity and subjective evaluation.

The lab does not require confidential employer, supervisor, payroll, personnel, or platform data.

## Learning Objectives

By the end of the lab, students should be able to:

1. reproduce a synthetic gift-exchange summary table and figure;
2. distinguish extra work from productivity and quality;
3. classify treatments by behavioral object and workplace governance margin;
4. compare pay-based incentives with monitoring-based interventions;
5. separate objective output from supervisor-facing influence activity;
6. transfer the diagnostic framework to remote work, digital monitoring, or subjective evaluation settings.

## Local Structure

```text
labs/05-incentives-contracts-reciprocity-and-workplace-behavior/
  lab.md
  smoke.sh
  src/
    build_week5_synthetic_data.py
    reproduce_gift_exchange.py
    transfer_monitoring_and_evaluation.py
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
conda run -n research python src/build_week5_synthetic_data.py

conda run -n research python src/reproduce_gift_exchange.py \
  --input original/reduced/gift_exchange_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_monitoring_and_evaluation.py \
  --monitoring-input transfer/data/monitoring_synthetic.csv \
  --evaluation-input transfer/data/subjective_evaluation_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

Run the synthetic-data builder and reproduction script. Inspect:

- `output/reproduced/gift_exchange_summary.csv`
- `output/reproduced/gift_exchange_effects.csv`
- `output/reproduced/gift_exchange_extra_work_vs_productivity.png`
- `output/reproduced/reproduction_note.txt`

Required interpretation:

- What behavioral object is shifted: gift, generosity, reciprocity, pay, or contract presentation?
- What labor margin moves: extra work, output, productivity, or quality?
- Does the design identify a treatment effect on current workers, selection into contracts, or both?
- Which standard explanation remains plausible: standard incentives, surprise, salience, worker heterogeneity, or task composition?

## Part II. Diagnose

Write a short design memo with four paragraphs:

1. **Benchmark:** What would a standard effort model predict if workers responded only to pay?
2. **Behavioral object:** Is the active channel reciprocity, reference dependence, monitoring salience, fairness, or evaluation pressure?
3. **Margin:** Which outcome moves: extra work, productivity, quality, compliance, gaming, or influence activity?
4. **Identification caution:** Does the design identify treatment, sorting, monitoring, evaluation, or a bundle?

## Part III. Transfer

Run the transfer script. Inspect:

- `output/transfer/monitoring_summary.csv`
- `output/transfer/monitoring_effects.csv`
- `output/transfer/subjective_evaluation_summary.csv`
- `output/transfer/monitoring_and_evaluation.png`
- `output/transfer/transfer_note.txt`

Use [@kelley2024monitoring] to classify the monitoring design. Does monitoring raise productivity, compliance, measured effort, or gaming? Then use [@deJanvrySadouletSuriWang2023] to classify the subjective-evaluation extension. Does the evaluation system reward objective output, supervisor-facing influence, or both?

## Challenge

Propose one bounded transfer design:

- remote-work monitoring;
- gig or platform work;
- algorithmic management;
- training or probation-period supervision;
- public-sector subjective evaluation.

For the chosen setting, state the behavioral object, contract or governance margin, outcome metric, identifying variation, and main standard alternative.

## Deliverables Checklist

- [ ] run log
- [ ] gift-exchange summary table
- [ ] treatment-effect summary table
- [ ] extra-work versus productivity figure
- [ ] one-page diagnosis memo
- [ ] monitoring summary and effect tables
- [ ] subjective-evaluation summary
- [ ] short transfer paragraph naming the object, margin, and identification claim
