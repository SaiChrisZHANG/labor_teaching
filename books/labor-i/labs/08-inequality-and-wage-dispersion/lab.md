# Code Lab 08: Inequality, Wage Dispersion, and Worker-Firm Decomposition

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 8 --- Inequality and wage dispersion  
**Associated chapter:** `08-inequality-and-wage-dispersion.md`  
**Lab slug:** `08-inequality-and-wage-dispersion`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 5--7, basic command-line use, introductory `pandas`, and comfort with grouped summaries and simple plots  
**Core economic question:** Which inequality objects should labor economists measure, and how much of wage dispersion can be organized through observed groups, residual inequality, and worker-firm allocation?  
**Core design / estimator:** bounded repeated-cross-section factbook plus a synthetic worker-firm transfer decomposition  
**Source paper for reproduction:** Autor, David H., Lawrence F. Katz, and Melissa S. Kearney. 2008. *Trends in U.S. Wage Inequality: Revising the Revisionists.* *Review of Economics and Statistics* 90(2): 300--323.  
**Secondary / challenge anchors:** Song, Jae, David J. Price, Fatih Guvenen, Nicholas Bloom, and Till von Wachter. 2019. *Firming Up Inequality.* *Quarterly Journal of Economics* 134(1): 1--50. Card, David, Ana Rute Cardoso, Jörg Heining, and Patrick Kline. 2018. *Firms and Labor Market Inequality: Evidence and Some Theory.* *Journal of Labor Economics* 36(S1): S13--S70.  
**Optional frontier extension anchor:** Haanwinckel, Daniel. 2025. *Supply, Technology, Firms, and Institutions in the Wage Distribution.*  

## Why this lab exists

Week 8 is the course's architecture week for distributional analysis. The bounded lab turns that architecture into a local workflow. Students first build a small synthetic inequality factbook in the spirit of [@autorKatzKearney2008], then diagnose what those objects do and do not identify, and finally transfer the workflow to a synthetic worker-firm panel that introduces AKM-style logic without needing proprietary administrative data.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded inequality factbook with percentile gaps, a college premium comparison, and between-versus-within dispersion;
2. explain why residual inequality is informative without being a single causal mechanism;
3. compare wage inequality with earnings-oriented or firm-allocation objects rather than treating one statistic as universal;
4. transfer the workflow to a synthetic worker-firm panel and compute a simple worker, firm, and sorting decomposition;
5. explain how Week 7 amenities and Week 8 firms jointly change the interpretation of wage dispersion.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact inequality factbook only.
- Diagnose the design in a short memo or notebook cell block.
- Transfer the workflow to one synthetic worker-firm decomposition only.
- Keep the smoke path fully local and synthetic.
- Treat the frontier extension as conceptual unless the instructor assigns more advanced work.

## Lab roadmap

1. **Reproduce** a synthetic inequality factbook.
2. **Diagnose** what the descriptive objects reveal and what they leave unresolved.
3. **Transfer** the workflow to a synthetic worker-firm decomposition.
4. **Reflect** on the bridge from wage dispersion to discrimination, segmentation, and mobility.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship restricted CPS extracts, confidential employer-employee records, or a literal reproduction package for the original articles. Instead, it builds deterministic synthetic teaching files that preserve the logic of repeated-cross-section inequality accounting and worker-firm decomposition.

### Required local structure

```text
labs/08-inequality-and-wage-dispersion/
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
      autor_katz_kearney_inequality_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      worker_firm_inequality_synthetic.csv
  src/
    build_week8_synthetic_data.py
    reproduce_autor_katz_kearney_inequality.py
    transfer_worker_firm_inequality.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week8_synthetic_data.py

conda run -n research python src/reproduce_autor_katz_kearney_inequality.py \
  --input original/reduced/autor_katz_kearney_inequality_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_worker_firm_inequality.py \
  --input transfer/data/worker_firm_inequality_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded inequality factbook from a synthetic CPS-style wage file.

### Student tasks

1. Run `src/build_week8_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/autor_katz_kearney_inequality_synthetic.csv`.
4. Inspect the percentile-gap, college-premium, and decomposition outputs in `output/reproduced/`.
5. Write a short note on why percentile gaps and residual inequality are complementary rather than interchangeable.

### Required questions

- Why can {math}`p90-p50` and {math}`p50-p10` move differently?
- What does a between-versus-within decomposition teach even when it is not causal?
- Why is the residual component not the same thing as a single technology shock?
- What changes when the object shifts from hourly wages to annual earnings or total job value?

### Minimum output

- one reproduced figure;
- one percentile-gap CSV;
- one college-premium summary CSV;
- one decomposition summary CSV;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "inequality rose" to a disciplined statement about which object rose and how the decomposition should be interpreted.

### Student tasks

1. Distinguish the descriptive role of percentile gaps from the descriptive role of residual inequality.
2. Explain why composition changes and price changes can both matter in repeated-cross-section comparisons.
3. State two reasons lower-tail inequality can move differently from upper-tail inequality.
4. Explain what remains outside the bounded reproduction step when the researcher does not yet observe firms or amenities directly.

### Minimum output

- a one-page design memo;
- one paragraph on the object being measured;
- one paragraph on decomposition discipline;
- one paragraph on what the reproduction step still leaves unresolved.

## Part III. Transfer

### Objective

Use the same Week 8 logic on a synthetic linked employer-employee panel.

### Bounded transfer path

Run `src/transfer_worker_firm_inequality.py` on the synthetic panel and compute a simple variance accounting for worker effects, firm premia, sorting covariance, and residual dispersion.

### Student tasks

1. Produce one main transfer figure.
2. Save the AKM-style component summary table.
3. Save the firm-quartile summary table.
4. Write a short paragraph explaining why firm inequality is one way of organizing worker inequality rather than a separate topic.
5. State how the transfer step changes the interpretation of Week 8 relative to the repeated-cross-section factbook.

### Scope constraints

- Keep the same Week 8 empirical family.
- Produce one main figure and compact summary tables.
- Do not add external data pulls or proprietary files.
- Keep the transfer discussion focused on worker effects, firm premia, sorting, and interpretation.

## Part IV. Optional frontier extension

Use [@haanwinckel2025] to write a short note on how supply, firms, and institutions might interact across the full wage distribution rather than within a single decomposition framework. The goal is not to estimate a structural model here. The goal is to recognize what the bounded descriptive path still abstracts from.

## Part V. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about Week 8?
2. What would still be missing before claiming to know the welfare consequences of rising inequality?
3. How does the lab change the way you will read Week 9 discrimination or Week 10 mobility evidence?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced inequality figure  
- [ ] percentile-gap CSV  
- [ ] decomposition summary CSV  
- [ ] design memo  
- [ ] transfer figure and AKM-style summary  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from teaching students to separate object choice from mechanism choice.
- Use the worker-firm transfer step to prepare students for why Week 9 and Week 10 need more than wage means.
