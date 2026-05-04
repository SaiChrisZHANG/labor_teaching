# Code Lab 12: Behavioral Frictions and an Introduction to Behavioral Labor

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 12 -- Behavioral frictions and an introduction to Behavioral Labor  
**Associated chapter:** `12-behavioral-frictions-introduction-to-behavioral-labor.md`  
**Lab slug:** `12-behavioral-frictions-introduction-to-behavioral-labor`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 3, 7, and 11; grouped summaries; simple causal-design interpretation; and comfort comparing incentive objects to perceived incentive objects  
**Core economic question:** How do labor economists distinguish a weak true incentive from a strong but opaque incentive, and how do behavioral labor designs move from complexity and gift exchange toward mechanism and welfare interpretation?  
**Core design / estimator:** bounded incentive-opacity reproduction plus a synthetic workplace gift-exchange transfer exercise  
**Source paper for reproduction:** Abeler, Johannes, David Huffman, and Collin Raymond. 2025. *Incentive Complexity, Bounded Rationality, and Effort Provision.* *American Economic Review* 115(12): 4404--4437.  
**Secondary / challenge anchors:** DellaVigna, Stefano, John A. List, Ulrike Malmendier, and Gautam Rao. 2022. *Estimating Social Preferences and Gift Exchange at Work.* *American Economic Review* 112(3): 1038--1074; and Royer, Heather, Mark Stehr, and Justin Sydnor. 2015. *Incentives, Commitments, and Habit Formation in Exercise: Evidence from a Field Experiment with Workers at a Fortune-500 Company.* *American Economic Journal: Applied Economics* 7(3): 51--84.  
**Optional extension anchors:** DellaVigna, Stefano, and M. Daniele Paserman. 2005. *Job Search and Impatience.* *Journal of Labor Economics* 23(3): 527--588; and DellaVigna, Stefano, and Devin Pope. 2018. *What Motivates Effort? Evidence and Expert Forecasts.* *The Review of Economic Studies* 85(2): 1029--1069.  

## Why this lab exists

Week 12 asks students to stop treating behavioral labor as a vocabulary list and start treating it as a design problem. The bounded lab makes one central point concrete: a complicated incentive schedule can generate a muted or distorted response even when the true economic stakes are large. Students first reproduce a synthetic incentive-opacity factbook in the spirit of `@abelerHuffmanRaymond2025`, then diagnose whether the observed pattern is about low incentives or low perception, and finally transfer the workflow to a synthetic workplace gift-exchange design in the spirit of `@dellaVignaListMalmendierRao2022`.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded behavioral-labor factbook from a synthetic incentive-complexity dataset;
2. distinguish true incentives from perceived incentives in a worker-effort setting;
3. explain why complexity can alter effort provision without changing the underlying contract budget;
4. estimate a compact gift-exchange contrast in a synthetic workplace field experiment;
5. compare preference-based and attention-based explanations for effort responses;
6. connect the Week 12 empirical logic back to Week 3 dynamic self-control and forward to welfare analysis.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact incentive-opacity factbook only.
- Diagnose the identifying logic in a short memo or notebook cell block.
- Transfer the workflow to one synthetic gift-exchange exercise only.
- Keep the smoke path fully local and synthetic.
- Treat dynamic commitment and structural welfare analysis as challenge or extension material rather than required code work.

## Lab roadmap

1. **Reproduce** a synthetic incentive-opacity factbook.
2. **Diagnose** whether the observed response pattern is about true incentives or perceived incentives.
3. **Transfer** the workflow to a synthetic workplace gift-exchange exercise.
4. **Reflect** on what Week 12 adds to standard worker-side labor analysis.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship proprietary employer personnel records, restricted task-level workplace data, or full field-experiment replication packages. Instead, it builds deterministic synthetic teaching files that preserve the logic of incentive-opacity estimation and workplace gift-exchange interpretation.

### Required local structure

```text
labs/12-behavioral-frictions-introduction-to-behavioral-labor/
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
      abeler_huffman_raymond_incentive_complexity_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      della_vigna_gift_exchange_synthetic.csv
  src/
    build_week12_synthetic_data.py
    reproduce_abeler_huffman_raymond.py
    transfer_della_vigna_gift_exchange.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week12_synthetic_data.py

conda run -n research python src/reproduce_abeler_huffman_raymond.py \
  --input original/reduced/abeler_huffman_raymond_incentive_complexity_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_della_vigna_gift_exchange.py \
  --input transfer/data/della_vigna_gift_exchange_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded incentive-opacity factbook from a synthetic worker-task dataset.

### Student tasks

1. Run `src/build_week12_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/abeler_huffman_raymond_incentive_complexity_synthetic.csv`.
4. Inspect the contract summary, opacity regression table, and reproduced figure in `output/reproduced/`.
5. Write a short note explaining why the same true bonus schedule can produce different effort when contract features are opaque.

### Required questions

- What is the relevant treatment variation in the bounded Week 12 reproduction?
- Why is a weak response to a complex contract not the same thing as a low labor-supply elasticity?
- How do perceived incentives enter the interpretation?
- Which standard alternative must be ruled out before calling the result behavioral?

### Minimum output

- one reproduced figure;
- one contract-summary CSV;
- one opacity-regression table;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "complex schedules change effort" to a disciplined statement about what the design actually teaches.

### Student tasks

1. Distinguish true incentives from perceived incentives.
2. Explain why complexity can change response even when posted pay is held fixed.
3. State one way in which standard heterogeneity or low attention to tasks could still complicate interpretation if the design were weaker.
4. Explain why this lab leads naturally into welfare and contract-design questions.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on the standard alternative being ruled out;
- one paragraph connecting the result to welfare or policy design.

## Part III. Transfer

### Objective

Use the same Week 12 logic on a synthetic workplace gift-exchange setting.

### Bounded transfer path

Run `src/transfer_della_vigna_gift_exchange.py` on the synthetic worker-shift experiment and estimate compact contrasts for extra work and productivity across baseline, gift, and high-piece-rate conditions.

### Student tasks

1. Produce one main transfer figure.
2. Save the arm-level effort summary table.
3. Save the employer-return heterogeneity table.
4. Write a short paragraph explaining why a gift can shift extra work even when the return to the employer is held fixed.
5. State how the transfer step broadens Week 12 from attention and complexity to social preferences and reciprocity.

### Scope constraints

- Keep the same Week 12 empirical family.
- Produce one main figure and compact summary tables.
- Do not add external data pulls or proprietary files.
- Keep the transfer discussion focused on effort, reciprocity, and interpretation.

## Part IV. Challenge block

Use `@royerStehrSydnor2015` conceptually to sketch how commitment demand reveals a dynamic self-control problem rather than merely a taste for incentives. The challenge prompt is not to estimate a structural model. It is to state clearly why voluntary commitment is informative, what the standard exponential benchmark would predict, and which outcomes would distinguish short-run incentive response from long-run habit formation.

## Part V. Optional frontier extension

Use `@dellaVignaPaserman2005` to connect present bias to search intensity and unemployment duration. Use `@dellaVignaPope2018` to compare standard incentives, social preferences, and nonmonetary motivators in real-effort settings. The goal is not to exhaust the literature. The goal is to use Week 12 to organize a mechanism map.

## Part VI. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 12?
2. What would still be missing before claiming a full welfare ranking of incentive simplification?
3. How does the lab change the way you will read weak or null labor responses to complicated contracts?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced incentive-opacity figure  
- [ ] contract summary CSV  
- [ ] design memo  
- [ ] transfer figure and workplace-effort summaries  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from teaching students to separate true incentives from perceived incentives.
- Use the challenge block to reconnect Week 12 to Week 3 dynamic labor supply and to the future Behavioral Labor course.
