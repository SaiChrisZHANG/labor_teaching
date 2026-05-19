---
title: Lecture 2. Experiments and Field Experiments
bibliography:
  - references.bib
---

# Lecture 2. Experiments and Field Experiments

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain what randomized assignment identifies and why experiments are a design rather than a method label;
2. distinguish the main experimental estimands: ATE, ITT, and the causal effect identified under randomized encouragement;
3. identify the core threats to interpretation in experiments: noncompliance, spillovers, attrition, weak implementation, and external-validity limits;
4. distinguish individual randomization, clustered randomization, audits/correspondence designs, and firm-level or market-level field experiments;
5. use high-quality experimental papers to understand when experiments are strongest, when they are not enough, and how equilibrium concerns change interpretation;
6. translate an experimental idea into a publishable applied research design.

## Opening Orientation

Experiments are often taught as the gold standard, but that phrase can conceal the real design logic. Randomization does not solve every causal problem. It solves a particular problem: it creates a known counterfactual by design, so treated and untreated units are comparable in expectation before treatment occurs. Everything after that depends on implementation. If treatment is not taken up, if outcomes are missing, if subjects interfere with one another, or if the intervention changes the market around them, then the experiment no longer identifies a simple object without additional design work.

This lecture therefore treats experiments as the cleanest place to learn causal design discipline. Students should leave understanding not only why experiments are powerful, but also why the strongest experimental papers are explicit about assignment, take-up, spillovers, implementation, and interpretation. The point is not to worship experiments; it is to learn how to reason carefully about what a design can and cannot identify.

:::{admonition} Core points
:class: note

- Random assignment identifies a causal effect only for the object defined by the assignment and the realized design.
- A clean experiment still requires decisions about unit of randomization, take-up, outcomes, spillovers, and scale.
- ITT is often the most policy-relevant estimand, even when treatment is imperfectly taken up.
- Randomized encouragement identifies a causal effect only for compliers under additional assumptions.
- Field experiments become especially valuable when institutional detail, implementation, and behavior are central to the research question.
- The strongest experimental papers are explicit about interference, attrition, external validity, and equilibrium response.
:::

## Bridge

Lecture 1 showed how causal claims depend on a target parameter and a design-based argument for the missing counterfactual. Lecture 2 now studies the cleanest version of that logic: create the counterfactual by random assignment. The next lectures in Block 1 will replace random assignment with temporal variation, instruments, and thresholds, so the language developed here—estimands, design assumptions, implementation, and interpretation—will carry through the rest of the course.

## Field Core

### Random Assignment as an Identification Device

Let {math}`Z_i` denote randomized assignment and {math}`D_i` realized treatment take-up. Under complete random assignment,

```{math}
:label: eq:rand-independence
Z_i \perp \{Y_i(1), Y_i(0), X_i\}.
```

This guarantees that assigned treatment and control groups are comparable in expectation on both observed and unobserved pre-treatment characteristics. Under full compliance, the average treatment effect is identified by the difference in average observed outcomes across assigned groups:

```{math}
:label: eq:ate-rct
ATE = \mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0].
```

The key design lesson is that the experiment identifies the effect of **assignment** cleanly. Whether that also identifies the effect of **receipt** depends on compliance.

### ITT, Take-Up, and the Logic of Randomized Encouragement

In many field settings, researchers can randomize encouragement, information, access, or an invitation rather than directly forcing treatment. Then the clean experimental estimand is the intention-to-treat effect:

```{math}
:label: eq:itt
ITT_Y = \mathbb{E}[Y_i \mid Z_i = 1] - \mathbb{E}[Y_i \mid Z_i = 0].
```

The corresponding first stage is:

```{math}
:label: eq:first-stage
ITT_D = \mathbb{E}[D_i \mid Z_i = 1] - \mathbb{E}[D_i \mid Z_i = 0].
```

Under standard exclusion and monotonicity assumptions, the Wald ratio identifies the local average treatment effect for compliers:

```{math}
:label: eq:wald
LATE = \frac{ITT_Y}{ITT_D}.
```

This is why encouragement designs are so useful in applied work: they preserve random assignment while respecting institutional limits. But the interpretation changes. Students should understand that `LATE` is not “the effect for everyone”; it is the effect for those whose behavior is shifted by the randomized encouragement.

### Individual Randomization, Cluster Randomization, and Market-Level Designs

Experiments differ not only by treatment content but by the unit of randomization. Randomizing individuals is not equivalent to randomizing schools, firms, offices, villages, platforms, or labor-market cells. Cluster randomization becomes natural when treatment is delivered collectively, when spillovers are expected, or when implementation happens at an organizational level.

This creates tradeoffs:
- cluster randomization can match the institutional unit of treatment more closely,
- but statistical power often falls,
- and interpretation must account for within-cluster correlation and market-level interference.

In labor markets, many of the best field experiments are really institution-level interventions: seminars randomized by workplace or location, management practices randomized at the firm level, or job-search treatments randomized over labor-market cells.

### Spillovers, Interference, and Saturation

The simplest experimental interpretation assumes stable unit treatment values. In labor and market settings, that is often unrealistic. A worker’s outcome can depend on others’ treatment status through referrals, congestion, norms, peer learning, or equilibrium price adjustment. A simple way to represent this is with an exposure mapping:

```{math}
:label: eq:spillover-exposure
Y_i = Y_i(z_i, g_i),
```

where {math}`z_i` is own assignment and {math}`g_i` is some measure of treatment intensity or exposure in the surrounding group, cluster, or market.

This matters because spillovers can be a feature, not a nuisance. Duflo and Saez’s retirement-seminar experiment is valuable precisely because peer exposure matters [@dufloSaez2003]. Crépon et al. are important because they show how labor-market equilibrium can make a successful treatment look different once untreated workers are affected by the market response [@creponEtAl2013].

### Audit and Correspondence Designs

Audit and correspondence experiments deserve separate attention because they are field experiments that randomize signals rather than policies. The classic example is hiring discrimination: résumés or applicants are randomized on names, credentials, or signals of group membership, and the researcher studies callback or offer differences [@bertrandMullainathan2004].

These designs are especially powerful when:
- the key outcome is initial screening,
- the treatment is a signal,
- and the researcher wants to isolate employer response before endogenous worker reactions occur.

But they are also narrow. They usually identify a margin at the point of contact, not a full labor-market equilibrium effect.

### Theory-to-Applied Research Logic

A strong experimental paper in applied economics usually has this architecture:

1. **Economic mechanism.** What behavior or institution is the treatment trying to shift?
2. **Assignment design.** What is randomized: individuals, firms, clusters, or information?
3. **Estimand.** Is the paper about assignment, receipt, compliance types, or market-level effects?
4. **Implementation.** Who actually received treatment? Who knew? What changed on the ground?
5. **Interference and scale.** Could untreated units be affected? Does scale matter?
6. **Interpretation.** Is the result a narrow local design result, or does it speak to a broader mechanism?

This is why field experiments are so useful for empirical methods teaching. They force students to name the mechanism and the institutional treatment channel rather than hiding behind a generic regression.

### Signature Papers and What They Teach

Duflo and Saez [@dufloSaez2003] are the right experimental anchor for labor because the design combines randomized encouragement, peer spillovers, and a policy-relevant labor/retirement mechanism. The paper teaches students that even a simple seminar intervention becomes interesting when assignment and peer exposure are both taken seriously.

Bloom et al. [@bloomEtAl2013] teach the logic of firm-level randomized interventions: treatment is implemented inside organizations, outcomes are operational, and the design lives or dies on treatment delivery and follow-through.

Pallais [@pallais2014] shows how online labor markets can be used as experimental environments to study information, reputation, and hiring under controlled but economically meaningful conditions.

Bertrand and Mullainathan [@bertrandMullainathan2004] remain the canonical audit experiment for showing how signal randomization isolates employer response.

Crépon et al. [@creponEtAl2013] are the benchmark reminder that experiments in labor markets may have equilibrium effects that change what the direct treatment contrast means.

## Research Lab

The Lecture 2 Research Lab follows **Reproduce → Diagnose → Transfer**.

**Primary anchor.** Duflo and Saez’s 401(k) seminar field experiment is the primary anchor [@dufloSaez2003]. It is ideal for Lecture 2 because it forces students to think about randomized encouragement, peer spillovers, and the difference between assignment and take-up.

**Challenge anchor.** Crépon et al. provide the challenge case [@creponEtAl2013]. They show why a successful labor-market intervention can have different direct and equilibrium effects once untreated workers are also affected.

**Reproduce.** Students reproduce a bounded version of the Duflo–Saez design on a reduced or synthetic dataset, estimating an ITT on seminar attendance or retirement-plan participation and contrasting naive treatment-on-treated intuition with the actual randomized design.

**Diagnose.** Students then diagnose what the design really identifies: assignment, not universal treatment receipt. They inspect take-up, cluster-level assignment, and simple exposure/spillover variation. The goal is to see how the estimand changes when interference is possible.

**Transfer.** Students then transfer the design logic to another experimental setting, such as an audit experiment, a platform experiment, or a labor-market treatment with cluster-level exposure. The transfer task should force them to name:
- the unit of randomization,
- the mechanism,
- the treatment receipt margin,
- the likely spillovers,
- and whether ITT, TOT/LATE, or a market-level estimand is the most meaningful target.

## Methods Box

:::{admonition} Methods Box: What Makes Experimental Designs Persuasive?
:class: note

Strong experimental papers usually answer six design questions clearly:

```{include} assets/tables/02-experimental-design-diagnostics.md
```

The key lesson is that randomization is the beginning of interpretation, not the end. Experiments are strongest when assignment, implementation, compliance, outcomes, interference, and scale are all disciplined and transparent.

:::

## Reading Ladder And References

**Foundations.** Start with Harrison and List for a field-experiment taxonomy and with Imbens and Rubin for experimental potential-outcomes logic [@harrisonList2004; @imbensRubin2015].

**Canonical labor/field anchors.** Read Duflo and Saez first [@dufloSaez2003], then Bertrand and Mullainathan [@bertrandMullainathan2004], then Bloom et al. [@bloomEtAl2013], then Pallais [@pallais2014].

**Equilibrium caution.** Read Crépon et al. [@creponEtAl2013] to understand why labor-market experiments often raise equilibrium questions quickly.

**Interpretation layer.** Use these papers not as disconnected examples, but as a set of answers to four questions:
- What was randomized?
- What does the design identify?
- Where can the design fail?
- How broadly should the results be interpreted?

## Exercises And Discussion Prompts

1. Write down the difference between `ATE`, `ITT`, and `LATE` in the context of a randomized job-training encouragement design.
2. Why might a labor-market experiment randomize seminars, firms, or locations rather than workers individually?
3. In Duflo and Saez, what makes peer spillovers a feature of the design rather than merely a nuisance?
4. Why are audit experiments powerful for measuring screening behavior but weaker for measuring full labor-market equilibrium effects?
5. Give one example where a successful randomized intervention could still produce misleading welfare conclusions because of equilibrium adjustment.
6. Suppose you want to study a new job-search platform feature. What would be randomized? What would the main risks to interpretation be?

## Reproducibility And Code Lab Note

The eventual lab folder for this lecture should live at:

`books/empirical-methods/labs/02-experiments-and-field-experiments/`

The bounded teaching path should use a reduced or synthetic dataset modeled on a randomized encouragement design so the lab is runnable locally without external downloads. If full original data are not bundled, the lab should be explicit that it reproduces the design logic rather than published magnitudes.

## Slide Companion Note

The slide deck for this lecture should live at:

`books/empirical-methods/slides/week2/02-experiments-and-field-experiments.tex`

The slides should foreground design logic:
- what randomization identifies,
- why ITT is often the clean experimental estimand,
- how LATE emerges with take-up,
- why cluster assignment and spillovers matter,
- and how to interpret field experiments under scale and equilibrium concerns.

## Bridge Forward

Lecture 2 shows what it looks like when the counterfactual is built by design. Lecture 3 will move to DID, event studies, and synthetic control, where the counterfactual is no longer randomized but constructed from untreated time paths. The design logic is the same; the identifying assumption changes.
