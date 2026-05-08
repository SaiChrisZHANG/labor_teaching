# Code Lab 05: Wage Posting, Bargaining, Outside Options, and Wage Rules

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 5 --- Wage posting, bargaining, and wage-setting  
**Associated chapter:** `05-wage-posting-bargaining-and-wage-setting.md`  
**Lab slug:** `05-wage-posting-bargaining-and-wage-setting`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Week 4 search and matching, basic command-line use, introductory `pandas`, comfort reading grouped summaries and simple plots  
**Core economic question:** When wages move, are we seeing a posted-wage response, individualized bargaining, or a change in the wage rule itself?  
**Primary source anchor:** [@lachowskaMasSaggioWoodbury2022]  
**Secondary / challenge anchor:** [@massenkoffWilmers2023]  
**Optional extension anchor:** [@biasi2021]

## Why this lab exists

Week 5 can easily become too verbal. The lab is designed to make students state the wage-setting protocol under test before they interpret a coefficient or a graph. [@lachowskaMasSaggioWoodbury2022] is the core anchor because it poses the cleanest version of the title question: posting or bargaining? [@massenkoffWilmers2023] is the challenge anchor because it shifts attention from one match to the firm's wage rule. [@biasi2021] is the extension because teacher salary schedules make standardized versus flexible pay concrete and transferable to public data.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded dual-jobholder exercise that contrasts wage responses with separation responses;
2. state clearly whether the source paper is testing posting, bargaining, or a wage-rule change;
3. name the observable outside-option or wage-setting margin in each exercise;
4. explain the main identification challenge in both the reproduction and transfer steps;
5. transfer the design logic to a public teacher-contract dataset, a public salary-schedule dataset, or a small synthetic offer-and-separation panel.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact dual-jobholder wage-setting object using a local synthetic file.
- Diagnose what that bounded object says about posting versus bargaining, and what it leaves latent.
- Transfer the logic to a synthetic wage-rule panel focused on standardized versus discretionary pay.
- Keep the smoke path fully local and synthetic.
- Do not turn the lab into a confidential microdata replication or a full structural model of wage bargaining.

## Lab roadmap

1. **Reproduce** a dual-jobholder test in the spirit of [@lachowskaMasSaggioWoodbury2022].
2. **Diagnose** the outside-option object, observed margin, and identification challenge.
3. **Transfer** the Week 5 logic to a wage-rule panel inspired by [@massenkoffWilmers2023].
4. **Extend** the design to teacher salary schedules in the spirit of [@biasi2021].

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not a literal replication package for the published papers. It is a synthetic teaching workflow that preserves the Week 5 logic while running locally without confidential wage microdata. The goal is to practice protocol discipline, not to duplicate every institutional and econometric layer of the originals.

### First commands to run

```bash
conda run -n research python src/reproduce_lachowska_wage_setting.py \
  --input original/reduced/lachowska_dual_jobholders_synthetic.csv \
  --outdir output/reproduced

conda run -n research python src/transfer_wage_setting_regimes.py \
  --input transfer/data/wage_setting_regimes_synthetic.csv \
  --outdir output/transfer
```

## Part I. Reproduce a bounded Week 5 object

### Objective

Recover a compact comparison between wage pass-through and separation responses when a worker's outside option shifts.

### Be explicit before you run anything

1. **Paper protocol under test:** posting versus bargaining.
2. **Observable outside-option margin in the bounded file:** the wage shock in the worker's secondary job.
3. **Observed unit:** worker with two jobs.
4. **Observed margins:** incumbent-job wage response and incumbent-job separation response.
5. **Main identification challenge:** the secondary-job shock is not the worker's entire opportunity set; unobserved offers and match quality remain latent.

### Student tasks

1. Run `src/reproduce_lachowska_wage_setting.py`.
2. Inspect `output/reproduced/lachowska_wage_setting_summary.csv`.
3. Inspect `output/reproduced/lachowska_wage_setting_by_bin.csv`.
4. Open `output/reproduced/lachowska_wage_setting_tradeoff.png`.
5. Write a short note answering: does the bounded pattern look more like posting or more like bargaining, and why?

### Required questions

- Is the paper testing posting, bargaining, or a wage-rule change?
- What exactly is the observable outside-option margin in the bounded path?
- Why is an observed secondary-job wage shock not the same as the full value of nonemployment?
- Why does a small incumbent wage response with a larger separation response push the interpretation toward posting?

## Part II. Diagnose the design

### Objective

Move from "wages did or did not respond" to a disciplined statement about what the design identifies and what it still leaves unresolved.

### Diagnosis checklist

1. **Protocol under test:** posting versus bargaining.
2. **Observed unit:** worker with two simultaneous jobs.
3. **Observed margins:** wage pass-through and separations.
4. **Most important latent object:** the worker's full menu of alternatives, not only the observed second job.
5. **Main design risk:** outside-option shocks may proxy for broader worker-level demand or productivity changes.

### Minimum output

- one short design memo;
- one annotated summary table;
- one paragraph on what remains latent;
- one paragraph explaining why this is not a direct estimate of the value of nonemployment.

## Part III. Transfer the Week 5 logic

### Objective

Use a synthetic wage-rule panel to compare standardized and discretionary pay-setting.

### Be explicit before you interpret the transfer file

1. **Paper protocol under study:** a wage-rule change, not a posting-versus-bargaining test.
2. **Observable wage-setting margin:** within-cell wage dispersion, offer-response frequency, and mobility under standardized versus discretionary pay.
3. **Observed unit:** occupation-by-establishment cell.
4. **Main identification challenge:** rule changes may shift many margins at once, including composition and nonwage conditions.

### Student tasks

1. Run `src/transfer_wage_setting_regimes.py`.
2. Inspect `output/transfer/wage_setting_regimes_summary.csv`.
3. Open `output/transfer/wage_setting_regimes_comparison.png`.
4. Explain how the same labor market could display both formal schedule rules and informal discretion.
5. Write one paragraph on how you would transfer the design to a public salary-schedule or teacher-contract setting.

### Transfer directions you are allowed to propose

- a public teacher-contract or salary-schedule dataset in the spirit of [@biasi2021];
- a public salary-grid dataset comparing within-cell wage compression before and after flexibility reforms;
- a small synthetic offer-and-separation panel that asks whether outside-option shocks move wages or mostly trigger turnover.

## Part IV. Optional extension

Choose one extension only.

1. Use [@biasi2021] to explain how teacher salary schedules isolate a wage-rule difference even when school amenities remain partly latent.
2. Design a small synthetic offer-and-separation panel that distinguishes realized outside offers from the value of nonemployment.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path tests a synthetic outside-option shock in a dual-jobholder setting; it is not the full administrative design in [@lachowskaMasSaggioWoodbury2022].
2. The bounded transfer path studies a synthetic wage-rule panel; it does not recover the full historical and organizational detail in [@massenkoffWilmers2023].
3. Neither path directly observes the value of nonemployment, the full offer distribution, or the full internal pay rule.
4. Neither path alone can separate reduced-form rent-sharing evidence from a complete structural interpretation of wage-setting.

## Deliverables checklist

- [ ] run log  
- [ ] reproduced summary table  
- [ ] reproduced by-bin table  
- [ ] reproduced tradeoff figure  
- [ ] one-page diagnose memo  
- [ ] transfer summary table and figure  
- [ ] short note on how to transfer the design to teacher contracts, salary schedules, or synthetic offers  

## Instructor notes

- The biggest payoff comes from forcing students to state whether the paper is testing posting, bargaining, or a wage-rule change before any interpretation starts.
- The next payoff comes from separating observable outside-option margins from the latent value of nonemployment.
- The transfer step is designed to push students from match-level wage determination to firm-level wage-setting regimes without leaving Week 5's conceptual scope.
