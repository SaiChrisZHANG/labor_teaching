# Code Lab 11: Public Policy Targeting Workers

**Course:** Labor I: Workers, Human Capital, and Inequality  
**Module / Week:** Week 11 -- Public policy targeting workers  
**Associated chapter:** `11-public-policy-targeting-workers.md`  
**Lab slug:** `11-public-policy-targeting-workers`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 2, 3, 4, 6, and 10; grouped summaries; simple panel and experiment interpretation; and comfort reading causal-design figures  
**Core economic question:** How do labor economists distinguish a policy schedule from effective worker exposure once knowledge, filing, timing, and administrative burden intervene?  
**Core design / estimator:** bounded effective-exposure reproduction plus a synthetic take-up field-experiment transfer exercise  
**Source paper for reproduction:** Chetty, Raj, John N. Friedman, and Emmanuel Saez. 2013. *Using Differences in Knowledge across Neighborhoods to Uncover the Impacts of the EITC on Earnings.* *American Economic Review* 103(7): 2683--2721.  
**Secondary / challenge anchors:** Linos, Elizabeth, Allen Prohofsky, Aparna Ramesh, Jesse Rothstein, and Matthew Unrath. 2022. *Can Nudges Increase Take-Up of the EITC? Evidence from Multiple Field Experiments.* *American Economic Journal: Economic Policy* 14(4): 432--452; and Lindner, Attila, and Balazs Reizer. 2020. *Front-Loading the Unemployment Benefit: An Empirical Assessment.* *American Economic Journal: Applied Economics* 12(3): 140--174.  
**Optional frontier extension anchors:** French, Eric, and Jae Song. 2014. *The Effect of Disability Insurance Receipt on Labor Supply.* *American Economic Journal: Economic Policy* 6(2): 291--337; Autor, David, Andreas R. Kostol, Magne Mogstad, and Bradley Setzler. 2019. *Disability Benefits, Consumption Insurance, and Household Labor Supply.* *American Economic Review* 109(7): 2613--2654; Manoli, Day, and Andrea Weber. 2016. *Nonparametric Evidence on the Effects of Financial Incentives on Retirement Decisions.* *American Economic Journal: Economic Policy* 8(4): 160--182; Wheeler, Laurel, Robert Garlick, Eric Johnson, Patrick Shaw, and Marissa Gargano. 2022. *LinkedIn(to) Job Opportunities: Experimental Evidence from Job Readiness Training.* *American Economic Journal: Applied Economics* 14(2): 101--125; and Verho, Jouko, Kari Hamalainen, and Ohto Kanninen. 2022. *Removing Welfare Traps: Employment Responses in the Finnish Basic Income Experiment.* *American Economic Journal: Economic Policy* 14(1): 501--522.  

## Why this lab exists

Week 11 is the course's worker-policy capstone. The bounded lab makes one central point concrete: a policy's statutory schedule is not the same thing as actual worker exposure. Students first reproduce a synthetic effective-exposure design in the spirit of [@chettyFriedmanSaez2013], then diagnose why neighborhood knowledge changes interpretation, and finally transfer the workflow to a synthetic take-up experiment in the spirit of [@linosProhofskyRameshRothsteinUnrath2022].

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded effective-exposure factbook from a synthetic neighborhood panel;
2. distinguish a statutory EITC schedule from effective exposure mediated by knowledge and filing support;
3. explain why stronger post-reform responses in high-knowledge places are informative about delivery and salience rather than only about tax rates;
4. estimate a compact causal take-up effect from a synthetic field experiment;
5. explain how delivery interventions differ from benefit-schedule interventions;
6. connect the Week 11 empirical logic to Week 12 frictions and to dynamic policy design questions such as front-loading.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact effective-exposure factbook only.
- Diagnose the identification and interpretation in a short memo or notebook cell block.
- Transfer the workflow to one take-up field experiment only.
- Keep the smoke path fully local and synthetic.
- Treat UI timing, disability adjudication, and retirement thresholds as challenge or extension material rather than required code work.

## Lab roadmap

1. **Reproduce** a synthetic neighborhood-knowledge factbook.
2. **Diagnose** why policy exposure differs from policy statute.
3. **Transfer** the workflow to a synthetic take-up field experiment.
4. **Reflect** on what Week 11 adds to labor-supply and policy interpretation.

## Part 0. Setup and orientation

### Official package reality

The source papers are the conceptual benchmarks. The bounded course path does **not** ship IRS administrative files, confidential tax-return microdata, or state UI records. Instead, it builds deterministic synthetic teaching files that preserve the logic of effective-exposure estimation and take-up field experiments.

### Required local structure

```text
labs/11-public-policy-targeting-workers/
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
      chetty_friedman_saez_knowledge_synthetic.csv
  transfer/
    README.md
    data-notes.md
    data/
      linos_eitc_nudge_synthetic.csv
  src/
    build_week11_synthetic_data.py
    reproduce_chetty_friedman_saez.py
    transfer_linos_takeup.py
  output/
    reproduced/
    transfer/
```

### First commands to run

```bash
conda run -n research python src/build_week11_synthetic_data.py

conda run -n research python src/reproduce_chetty_friedman_saez.py \
  --input original/reduced/chetty_friedman_saez_knowledge_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_linos_takeup.py \
  --input transfer/data/linos_eitc_nudge_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce

### Objective

Recover a bounded effective-exposure factbook from a synthetic neighborhood panel.

### Student tasks

1. Run `src/build_week11_synthetic_data.py`.
2. Read `original/source-notes.md`.
3. Run the reproduction script on `original/reduced/chetty_friedman_saez_knowledge_synthetic.csv`.
4. Inspect the quartile summary, gradient estimates, and reproduced figure in `output/reproduced/`.
5. Write a short note explaining why higher responses in high-knowledge neighborhoods are informative about policy salience and delivery.

### Required questions

- What is the relevant treatment variation in the bounded Week 11 reproduction?
- Why is the object closer to effective exposure than to a pure statutory tax elasticity?
- How do filing support and neighborhood knowledge enter the interpretation?
- Why can stronger post-reform responses in one neighborhood type coexist with a common statutory schedule?

### Minimum output

- one reproduced figure;
- one quartile summary CSV;
- one regression-style gradient table;
- one short interpretation note.

## Part II. Diagnose

### Objective

Move from "high-knowledge neighborhoods respond more" to a disciplined statement about what the design actually teaches.

### Student tasks

1. Distinguish statutory EITC generosity from effective policy exposure.
2. Explain what is learned from comparing neighborhoods with different knowledge and filing support.
3. State one way in which local labor demand could still complicate interpretation if the design were weaker.
4. Explain why this lab naturally leads into take-up, salience, and Week 12 frictions.

### Minimum output

- a one-page design memo;
- one paragraph on the estimand;
- one paragraph on what remains outside the design;
- one paragraph connecting the result to take-up and frictions.

## Part III. Transfer

### Objective

Use the same Week 11 logic on a synthetic EITC take-up field experiment.

### Bounded transfer path

Run `src/transfer_linos_takeup.py` on the synthetic claimant-level experiment and estimate compact treatment effects for take-up, filing completion, and received benefits.

### Student tasks

1. Produce one main transfer figure.
2. Save the arm-level take-up summary table.
3. Save the burden-heterogeneity table.
4. Write a short paragraph explaining why reminders and simplified notices change treatment intensity without changing the statutory schedule.
5. State how the transfer step broadens Week 11 from tax schedules to administrative delivery.

### Scope constraints

- Keep the same Week 11 empirical family.
- Produce one main figure and compact summary tables.
- Do not add external data pulls or proprietary files.
- Keep the transfer discussion focused on delivery, take-up, and interpretation.

## Part IV. Challenge block

Use [@lindnerReizer2020] conceptually to sketch how front-loading would change the continuation value of nonemployment from the Week 11 chapter's dynamic UI object. The challenge prompt is not to estimate a full structural model. It is to state clearly how a timing reform differs from a level reform, which outcomes would move first, and which design would best identify the response.

## Part V. Optional frontier extension

Use [@frenchSong2014] and [@autorKostolMogstadSetzler2019] to write a short note on why disability-insurance receipt is both a labor-supply and a household-insurance object. Use [@manoliWeber2016] to explain why retirement thresholds invite bunching logic. Use [@wheelerGarlickJohnsonShawGargano2022] or [@verhoHamalainenKanninen2022] to compare search-help and welfare-trap interventions to the Week 11 take-up exercises.

## Part VI. Reflection

### Student prompts

1. What does the bounded teaching path teach especially well about effective policy exposure?
2. What would still be missing before claiming to estimate a full labor-supply elasticity for a worker policy?
3. How does the lab change the way you will read a null or small treatment effect in policy evaluation?

## Deliverables checklist

- [ ] run log  
- [ ] reproduced effective-exposure figure  
- [ ] quartile summary CSV  
- [ ] design memo  
- [ ] transfer figure and take-up summaries  
- [ ] reflection note  
- [ ] clear distinction between bounded synthetic path and official paper benchmarks  

## Instructor notes

- The bounded path is the default for routine course use.
- The strongest payoff comes from teaching students to separate statutory schedules from effective delivery.
- Use the challenge block to bridge to Week 12 frictions or to a later methods discussion on dynamic design.
