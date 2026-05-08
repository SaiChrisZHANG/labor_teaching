# Code Lab 09: Labor Regulation, Enforcement, and Insurance

**Course:** Labor II: Firms, Frictions, and Institutions  
**Module / Week:** Week 9 --- Labor regulation, enforcement, and insurance  
**Associated chapter:** `09-labor-regulation-enforcement-and-insurance.md`  
**Lab slug:** `09-labor-regulation-enforcement-and-insurance`  
**Scope tier:** Extended policy-framework week  
**Primary language:** Python  
**Estimated student time:** 4 core hours + 2 optional hours  
**Prerequisites:** Weeks 7--8, grouped-data intuition, basic `pandas`, simple plots, and comfort distinguishing partial-equilibrium from equilibrium effects  
**Core economic question:** When does a labor regulation bind in practice, who is directly treated, which uncovered margin adjusts, and what welfare tradeoff changes the interpretation of the result?  
**Primary source anchor:** [@almeidaCarneiro2012]  
**Secondary / challenge anchor:** [@laliveLandaisZweimueller2015]  
**Optional extension anchor:** [@vanDoornikGerardNaritomi2023]

## Why this lab exists

Week 9 becomes fuzzy quickly if students say "the policy effect" without naming the treatment margin, the spillover margin, or the welfare benchmark. [@almeidaCarneiro2012] is the reproduction anchor because it forces the distinction between regulation on the books and effective enforcement. [@laliveLandaisZweimueller2015] is the diagnose anchor because it shows that insurance policy can reshape untreated outcomes through market externalities. The optional extension anchor [@vanDoornikGerardNaritomi2023] makes the uncovered informal margin explicit.

## Learning objectives

By the end of this lab, students should be able to:

1. reproduce a bounded enforcement-and-formality exercise in the spirit of [@almeidaCarneiro2012];
2. name the regulation, policy margin, directly treated side of the market, spillover margin, and welfare tradeoff before interpreting any estimate;
3. explain why effective regulation differs from formal law once enforcement, knowledge, and compliance matter;
4. diagnose the difference between a partial-equilibrium enforcement estimate and an equilibrium unemployment-insurance estimate;
5. transfer the design to a small public, synthetic, or aggregate dataset without confidential microdata.

## Scope rules

This lab is intentionally bounded.

- Reproduce one compact Almeida-Carneiro style enforcement panel using synthetic locality-year data.
- Diagnose why that object differs from a Lalive-Landais-Zweimueller equilibrium UI design.
- Transfer the Week 9 framework to synthetic UI spillover and informal-margin panels.
- Keep the smoke path fully local and synthetic.
- Do not turn the lab into a full administrative-data replication package.

## Lab roadmap

1. **Reproduce** a bounded enforcement-and-formality object in the spirit of [@almeidaCarneiro2012].
2. **Diagnose** how that object differs from an equilibrium unemployment-insurance design in [@laliveLandaisZweimueller2015].
3. **Transfer** the logic to synthetic UI spillover and formality-margin panels.
4. **Extend** the framework to a small public or synthetic dataset with a clear uncovered margin.

## Part 0. Setup and orientation

### First commands to run

```bash
conda run -n research python src/reproduce_almeida_enforcement.py \
  --outdir output/reproduced

conda run -n research python src/transfer_regulation_designs.py \
  --outdir output/transfer
```

### Before you touch the outputs

Write down six things.

1. What regulation is being studied?
2. Is the key issue enforcement, insurance, dismissal, or information?
3. Which side of the market is directly treated?
4. What spillover or uncovered margin matters?
5. What is the relevant welfare tradeoff?
6. Which empirical object is still unobserved after the design is run?

## Part I. Reproduce a bounded Almeida-Carneiro object

### Objective

Recover a compact synthetic locality-year panel showing how stronger enforcement can raise effective regulation, alter wages and compliance, and shift workers between formal and informal employment.

### Be explicit before you run anything

1. **Regulation being studied:** labor standards and formality enforcement.
2. **Key issue:** enforcement and effective regulation, not the nominal statute alone.
3. **Directly treated side:** firms and regulators first; covered workers indirectly through actual compliance.
4. **Spillover or uncovered margin:** formal versus informal employment reallocation.
5. **Relevant welfare tradeoff:** stronger worker protection and formal benefits versus higher formal labor cost and possible displacement.
6. **Key unobserved object:** the untreated local state-capacity and labor-demand environment absent the enforcement difference.

### Student tasks

1. Run `src/reproduce_almeida_enforcement.py`.
2. Inspect `output/reproduced/almeida_enforcement_summary.csv`.
3. Inspect `output/reproduced/almeida_enforcement_by_enforcement_tier.csv`.
4. Open `output/reproduced/almeida_enforcement_framework.png`.
5. Write a short note explaining why inspection intensity is part of the treatment rather than only a control.

### Required questions

- What is the regulation on the books, and what makes it effective in practice?
- Which margin absorbs costs in the synthetic panel: wages, formality, or both?
- Why is the uncovered margin informative even if covered-worker compliance rises?
- Which part of the welfare interpretation depends on worker valuation of mandated benefits?

## Part II. Diagnose the design difference

### Objective

Compare an enforcement-and-formality design to an equilibrium unemployment-insurance design.

### Anchor comparison table

| Paper | Core object | Directly treated side | Spillover / uncovered margin | Identifying variation | Key unobserved object |
| --- | --- | --- | --- | --- | --- |
| [@almeidaCarneiro2012] | effective labor regulation through inspections | firms / regulators | informality and wage adjustment | locality-level enforcement intensity | local state capacity and untreated labor demand |
| [@laliveLandaisZweimueller2015] | equilibrium effects of UI extensions | eligible workers first | noneligible workers and vacancies | regional UI extension program | market tightness counterfactual |
| [@vanDoornikGerardNaritomi2023] | UI incentives with informal labor markets | formally employed workers and firms | informal transitions and strategic layoffs | policy-induced eligibility or timing variation | value of uncovered informal options |

### Diagnosis checklist

1. **Almeida-Carneiro object:** effective regulation once enforcement changes.
2. **Lalive-Landais-Zweimueller object:** market externality of insurance generosity.
3. **Main lesson:** these papers need not report the same sign on treated outcomes because they study different policy margins and different equilibrium objects.

### Minimum output

- one short design memo comparing effective regulation and equilibrium insurance;
- one paragraph naming the main identification challenge in each design;
- one paragraph explaining why treated-worker outcomes are insufficient in the Week 9 literature.

## Part III. Transfer the Week 9 framework

### Objective

Move from enforcement to equilibrium UI and uncovered informal margins using synthetic data.

### Be explicit before you interpret the transfer outputs

1. **UI market panel object**
   - unemployment-insurance generosity and duration in a regional market;
   - worker-targeted insurance with equilibrium spillovers onto noneligible workers;
   - main welfare tradeoff: insurance value versus search distortion plus market externalities.

2. **UI informal-margin panel object**
   - policy incentives around formal layoffs and informal transitions;
   - worker and firm responses to a covered benefit with an uncovered outside option;
   - main welfare tradeoff: insurance versus strategic separations and fiscal leakage.

3. **Transfer targets you are allowed to propose**
   - a small public or aggregate UI-by-region panel;
   - a synthetic enforcement/compliance comparison across regions;
   - a public formality or payroll series paired with a policy change;
   - a short policy memo comparing dismissal costs, enforcement, and UI on common margins.

### Student tasks

1. Run `src/transfer_regulation_designs.py`.
2. Inspect `output/transfer/regulation_transfer_summary.csv`.
3. Inspect `output/transfer/synthetic_ui_market_panel.csv`.
4. Inspect `output/transfer/synthetic_ui_informality_panel.csv`.
5. Open `output/transfer/regulation_transfer_designs.png`.
6. Explain why the UI spillover object and the informal-margin object complement rather than duplicate the Week 9 reproduction step.

## Part IV. Optional extension

Choose one extension only.

1. Transfer the Almeida-Carneiro logic to a small synthetic cross-region enforcement panel with a different uncovered margin.
2. Write a short memo comparing [@bertrandCrepon2021] and [@cullen2024PayTransparency] as information-based labor regulations.
3. Build a small aggregate UI panel and say explicitly which market-level outcome you need to observe before making a welfare claim.

## Limitations relative to the original papers

Students should say these plainly.

1. The bounded reproduction path uses synthetic locality-year data; it is not the original enforcement and informality setting in [@almeidaCarneiro2012].
2. The diagnose step is conceptual and synthetic; it does not reproduce the full market-level Austrian UI design in [@laliveLandaisZweimueller2015].
3. The optional extension is a bounded synthetic treatment of uncovered informal margins; it does not reproduce the full Brazil administrative setting in [@vanDoornikGerardNaritomi2023].
4. None of the bounded paths recover the full welfare object because worker valuation, firm incidence, and equilibrium market tightness are only partially observed.

## Deliverables checklist

- [ ] reproduced enforcement summary table  
- [ ] reproduced enforcement-tier table  
- [ ] reproduced enforcement figure  
- [ ] short diagnose memo comparing enforcement and equilibrium UI  
- [ ] transfer summary table and transfer figure  
- [ ] short note proposing one public or synthetic transfer design  

## Instructor notes

- The most valuable habit in this lab is to state the treated side, uncovered margin, and welfare tradeoff before discussing any coefficient.
- The second most valuable habit is to separate formal law from effective regulation.
- Students should leave the lab understanding why enforcement, insurance, and informality can all be part of one labor-regulation framework without being the same empirical object.
