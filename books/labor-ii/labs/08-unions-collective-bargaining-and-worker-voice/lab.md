# Code Lab 08: Unions, Collective Bargaining, and Worker Voice

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 8 --- Unions, collective bargaining, and worker voice  
**Associated chapter:** `08-unions-collective-bargaining-and-worker-voice.md`  
**Lab slug:** `08-unions-collective-bargaining-and-worker-voice`  
**Scope tier:** Standard  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 5--7, basic command-line use, introductory `pandas`, comfort reading grouped summaries, simple plots, and RD-style design intuition  
**Core economic question:** Are we studying union membership, bargaining coverage, or organizing success, and is the estimated effect direct on covered workers, indirect through spillovers, or threat-based on uncovered workers?  
**Primary source anchor:** [@farberHerbstKuziemkoNaidu2021]  
**Secondary / challenge anchor:** [@dinardoLee2004]  
**Optional extension anchor:** [@fortinLemieuxLloyd2021]

## Why this lab exists

Week 8 gets muddy fast if students say "the union effect" without naming the object. [@farberHerbstKuziemkoNaidu2021] is the reproduction anchor because it makes unions a wage-structure and inequality object rather than only a point wage premium. [@dinardoLee2004] is the diagnose anchor because it is explicit about organizing success near a certification threshold. [@fortinLemieuxLloyd2021] is the optional extension because it pushes students to ask what happens to uncovered workers when bargaining institutions are strong or weak.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded coverage-and-inequality exercise in the spirit of [@farberHerbstKuziemkoNaidu2021];
2. state clearly whether the object is union membership, bargaining coverage, or an organizing / certification margin;
3. say whether the estimated effect is direct, spillover, or threat-based;
4. explain the main identification challenge in a long-run decomposition and in a certification-election RD;
5. transfer the design to a small public CPS/Unionstats panel, certification-election panel, or synthetic coverage / inequality panel.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact Farber-Herbst-Kuziemko-Naidu style state-year decomposition using synthetic data.
- Diagnose how that object differs from a DiNardo-Lee style close-election RD.
- Transfer the logic to a synthetic certification panel and a synthetic spillover panel.
- Keep the smoke path fully local and synthetic.
- Do not turn the lab into a confidential matched worker-firm replication package.

## Lab roadmap

1. **Reproduce** a bounded coverage-and-inequality panel in the spirit of [@farberHerbstKuziemkoNaidu2021].
2. **Diagnose** how that object differs from a close-election organizing design in [@dinardoLee2004].
3. **Transfer** the logic to a synthetic certification-election panel and a synthetic nonunion spillover panel.
4. **Extend** the design to a public CPS/Unionstats panel or an uncovered-worker spillover exercise in the spirit of [@fortinLemieuxLloyd2021].

## Part 0. Setup and orientation

### Official package reality

The bounded path here is not the published replication archive. It is a synthetic teaching workflow that preserves the Week 8 identification logic while running locally without restricted microdata. The goal is to learn which union object is being estimated and why different designs do not answer the same question.

### First commands to run

```bash
conda run -n research python src/reproduce_farber_union_inequality.py \
  --outdir output/reproduced

conda run -n research python src/transfer_union_designs.py \
  --outdir output/transfer
```

## Part I. Reproduce a bounded Farber-Herbst-Kuziemko-Naidu object

### Objective

Recover a compact decomposition linking bargaining coverage to wage compression and inequality in a synthetic state-year panel.

### Be explicit before you run anything

1. **Union object:** bargaining coverage and surrounding union presence, not only dues-paying membership.
2. **Effect type:** both direct compression for covered workers and indirect compression for uncovered workers through spillovers.
3. **Identifying variation:** long-run state-year changes in coverage and membership with a synthetic inequality counterfactual.
4. **Observed unit:** state-year panel and grouped era summary.
5. **Observed margin:** coverage, membership, direct compression, spillover compression, and the 90/10 wage gap.
6. **Key unobserved object:** the untreated wage structure absent deunionization and the exact split between direct and spillover effects.

### Student tasks

1. Run `src/reproduce_farber_union_inequality.py`.
2. Inspect `output/reproduced/farber_union_inequality_summary.csv`.
3. Inspect `output/reproduced/farber_union_inequality_by_era.csv`.
4. Open `output/reproduced/farber_union_inequality_decomposition.png`.
5. Write a short note explaining why the main object is coverage and wage compression rather than only a membership premium.

### Required questions

- Is the object here union membership, bargaining coverage, or organizing success?
- Which part of the effect is direct on covered workers, and which part is spillover onto uncovered workers?
- Why is a decomposition exercise informative even though it is not a close-election causal design?
- What remains latent after we see the synthetic inequality decomposition?

## Part II. Diagnose the design difference

### Objective

Compare a long-run coverage-and-inequality object to a certification-election RD organizing object.

### Anchor comparison table

| Paper | Core object | Effect type | Identifying variation | Observed unit | Key unobserved object |
| --- | --- | --- | --- | --- | --- |
| [@farberHerbstKuziemkoNaidu2021] | bargaining coverage and union presence | direct plus spillover compression | long-run union decline and distributional decomposition | worker-year or state-year cell | untreated wage structure absent deunionization |
| [@dinardoLee2004] | organizing success near the threshold | direct effect of union victory for close elections | close certification wins versus losses | establishment / election | outcomes away from the threshold and broader equilibrium effects |
| [@fortinLemieuxLloyd2021] | union spillovers onto uncovered workers | indirect or threat-based effects | institutional exposure and wage-distribution variation | worker / region / wage cell | untreated nonunion wage structure absent spillovers |

### Diagnosis checklist

1. **Farber-Herbst-Kuziemko-Naidu object:** coverage and union presence as a distributional institution.
2. **DiNardo-Lee object:** causal effect of close union wins on establishments near the legal threshold.
3. **Main lesson:** these papers need not report the same number because they study different objects, margins, and counterfactuals.

### Minimum output

- one short design memo comparing coverage decomposition and certification RD;
- one paragraph naming the main identification challenge in each design;
- one paragraph on why direct effects and spillovers should not be mixed together.

## Part III. Transfer the Week 8 logic

### Objective

Use synthetic election and spillover panels to practice moving from organizing to coverage to uncovered-worker effects.

### Be explicit before you interpret the transfer outputs

1. **Certification panel object**
   - Organizing / certification margin, not broad bargaining coverage.
   - Direct effect for establishments near the threshold.
   - Main identification challenge: local external validity and post-election selection.

2. **Spillover panel object**
   - Nonunion wage response to union presence.
   - Spillover or threat-based effect, not a covered-worker premium.
   - Main identification challenge: nonunion wages move for many reasons besides union presence.

3. **Transfer targets you are allowed to propose**
   - a small public CPS/Unionstats panel;
   - a certification-election panel;
   - a synthetic or public coverage / inequality panel with spillover terms.

### Student tasks

1. Run `src/transfer_union_designs.py`.
2. Inspect `output/transfer/union_transfer_summary.csv`.
3. Inspect `output/transfer/synthetic_certification_elections.csv`.
4. Inspect `output/transfer/synthetic_spillover_panel.csv`.
5. Open `output/transfer/union_transfer_designs.png`.
6. Explain why the election panel and spillover panel complement rather than duplicate the Week 8 reproduction step.

## Part IV. Optional extension

Choose one extension only.

1. Transfer the reproduction logic to a small CPS/Unionstats state-year panel using membership and coverage separately.
2. Add a threat-effect interpretation to the spillover panel and explain how it differs from pure positive spillovers.
3. Design a public-sector or education-sector extension, but say explicitly why that legal environment differs from private-sector certification.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path uses a synthetic state-year panel; it is not the original survey microdata and historical decomposition in [@farberHerbstKuziemkoNaidu2021].
2. The bounded transfer path uses a stylized close-election panel; it does not reproduce the full private-sector employer panel in [@dinardoLee2004].
3. The optional spillover extension is conceptual and synthetic; it does not reproduce the full wage-distribution analysis in [@fortinLemieuxLloyd2021].
4. None of the bounded paths recover the full general-equilibrium counterfactual or the complete political environment around bargaining institutions.

## Deliverables checklist

- [ ] reproduced inequality summary table  
- [ ] reproduced era summary table  
- [ ] reproduced coverage-and-inequality figure  
- [ ] short diagnose memo comparing Farber-Herbst-Kuziemko-Naidu and DiNardo-Lee  
- [ ] transfer summary table and transfer figure  
- [ ] short note on one public or synthetic transfer design  

## Instructor notes

- The highest-value habit is to ask whether the paper studies membership, coverage, or organizing before any interpretation begins.
- The next highest-value habit is to separate direct covered-worker effects from spillovers and threat effects on uncovered workers.
- Students should leave the lab understanding why a distributional decomposition, a certification RD, and a spillover study are all valid evidence on unions without being the same estimand.
