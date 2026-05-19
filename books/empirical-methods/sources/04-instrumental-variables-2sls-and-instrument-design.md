---
title: Lecture 4. Instrumental Variables, 2SLS, and Instrument Design
bibliography:
  - references.bib
---

# Lecture 4. Instrumental Variables, 2SLS, and Instrument Design

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when instrumental variables is preferable to experiments, DID, or selection-on-observables designs;
2. derive and interpret the Wald estimand, first stage, reduced form, and 2SLS estimand;
3. state and evaluate the core IV assumptions: relevance, exclusion, independence, and monotonicity;
4. distinguish ATE from LATE and explain why IV identifies a local parameter under heterogeneous treatment effects;
5. diagnose weak-instrument, many-instrument, and multiple-instrument interpretation problems in practice;
6. evaluate major instrument families—policy eligibility, distance/access, judge leniency, shift-share, and historical instruments—using concrete empirical criteria;
7. translate an economic story into a credible instrument design and explain its implementation caveats and limits.

## Opening Orientation

Instrumental variables is one of the most commonly used methods in applied economics, but it is also one of the easiest to misuse. The usual textbook story—find a variable correlated with treatment but not with the error term—is mathematically correct and empirically incomplete. In practice, the real work of IV is not running two stages; it is explaining why the instrument moves treatment, which subpopulation it moves, what variation it isolates, and why that variation is informative about the causal question.

This lecture therefore treats IV as a design discipline. The point is not to memorize assumptions, but to learn how to evaluate whether a proposed instrument is believable. Students should leave understanding both why IV has been so productive and why it is often fragile. The best IV papers are powerful because the first stage has clear economic content and the exclusion argument is specific. The weakest IV papers hide behind the estimator while leaving the source of quasi-random variation vague.

:::{admonition} Core points
:class: note

- IV is strongest when treatment is endogenous but a well-understood source of quasi-random variation shifts treatment in a substantively meaningful way.
- The first stage is not a nuisance statistic; it defines what variation is being used and who the compliers are.
- The Wald/2SLS estimand is local under heterogeneity, so interpretation depends on monotonicity and the economic content of the instrument.
- Exclusion is often the hardest assumption to defend, and it is never established by algebra alone.
- Weak instruments, many instruments, and poorly understood instrument families can make nominally precise IV estimates deeply misleading.
- A good IV design is a theory of variation before it is a regression.
:::

## Bridge

Lecture 3 studied comparative panel designs that construct a counterfactual from untreated units over time. Lecture 4 now studies a different strategy: use a source of variation that shifts treatment but is argued not to affect outcomes except through treatment. Lecture 5 will move to regression discontinuity and related local designs, where identification comes from thresholds rather than exclusion restrictions. Together, the three lectures map the main quasi-experimental toolkit.

## Field Core

### Why Instrumental Variables?

Suppose the causal object of interest is the effect of treatment {math}`D_i` on outcome {math}`Y_i`, but treatment is endogenous:

```{math}
:label: eq:iv-structural
Y_i = \beta D_i + X_i'\gamma + u_i.
```

If {math}`D_i` is correlated with {math}`u_i`, OLS does not identify {math}`\beta`. The endogeneity may come from omitted ability, anticipation, sorting, reverse causality, or measurement error. IV tries to recover causal variation in {math}`D_i` using an instrument {math}`Z_i`:

```{math}
:label: eq:iv-firststage
D_i = \pi Z_i + X_i'\delta + v_i.
```

The reduced form is:

```{math}
:label: eq:iv-reducedform
Y_i = \rho Z_i + X_i'\kappa + \varepsilon_i.
```

With a single instrument and no controls, the Wald estimand is

```{math}
:label: eq:wald
\beta^{IV}
=
\frac{\operatorname{Cov}(Y_i, Z_i)}{\operatorname{Cov}(D_i, Z_i)}.
```

With controls and/or multiple instruments, two-stage least squares estimates the coefficient from projecting {math}`Y_i` on the fitted values from the first stage.

### The Core IV Assumptions

The logic of IV can be summarized in four assumptions.

**Relevance.** The instrument shifts treatment:
```{math}
:label: eq:relevance
\operatorname{Cov}(D_i, Z_i \mid X_i) \neq 0.
```

**Exclusion.** The instrument affects the outcome only through treatment:
```{math}
:label: eq:exclusion
Y_i(d, z) = Y_i(d) \quad \text{for all } d,z.
```

**Independence.** The instrument is as-good-as-random with respect to the relevant potential outcomes:
```{math}
:label: eq:independence
Z_i \perp \{Y_i(1), Y_i(0), D_i(1), D_i(0)\} \mid X_i.
```

**Monotonicity.** There are no defiers:
```{math}
:label: eq:monotonicity
D_i(1) \ge D_i(0) \quad \text{for all } i.
```

In practice, relevance is testable at least partially, while exclusion and independence rely on institutional argument. Monotonicity sits in between: it is rarely testable directly, but sometimes easier to argue in one-sided or rule-based settings than in more complex strategic environments.

### LATE and the Interpretation of the First Stage

Under independence, exclusion, and monotonicity, IV identifies the Local Average Treatment Effect for compliers:

```{math}
:label: eq:late
LATE = \mathbb{E}\!\left[Y_i(1)-Y_i(0)\mid D_i(1)>D_i(0)\right].
```

This is why the first stage is substantive, not cosmetic. The first stage tells you:
- which margin of treatment the instrument moves;
- which people or firms comply;
- and therefore which treatment effect is being estimated.

A strong practical question is always: **who are the compliers?** Quarter-of-birth instruments move students near school-leaving margins [@angrist1991; @oreopoulos2006]. College-proximity instruments move students whose schooling responds to access or cost [@card1995]. Judge-leniency instruments move cases at the margin of a judge’s decision rule [@autorKostolMogstadSetzler2019]. Shift-share instruments move places or sectors differentially exposed to aggregate shocks [@borusyakHullJaravel2022].

### 2SLS, Multiple Instruments, and Weighting

When there are multiple instruments, 2SLS combines them through first-stage projection. That is convenient, but the interpretation can become subtle. With heterogeneous treatment effects, a multiple-instrument 2SLS estimand is generally a weighted average of instrument-specific LATEs under strong conditions, and those weights need not correspond to the researcher’s preferred economic population [@mogstadTorgovitskyWalters2021].

This is why “add more instruments” is not automatically a good idea. Multiple instruments can increase precision when valid, but they can also:
- introduce many-instrument bias,
- obscure which variation is identifying the estimate,
- and mix different complier populations with different economic meaning.

### Weak Instruments and Many-Instrument Problems

The basic weak-IV warning is that a small or unstable first stage can make 2SLS behave badly in finite samples. A simple first-stage F-statistic remains a useful diagnostic, though it is not the whole story. At minimum, students should learn to:
- report the first-stage coefficient and economic magnitude,
- report a relevant weak-IV diagnostic,
- use weak-IV robust inference where appropriate,
- and explain what the first-stage variation actually represents.

Weak instruments are not only about small correlations. They are about fragile identification. If the first stage is weak, the 2SLS estimate can be noisy, biased toward OLS, and highly sensitive to specification choices. With many instruments, overfitting in the first stage can further contaminate second-stage estimates.

### The Instrument Design Gallery

The most useful way to teach IV is to classify instrument families and ask the same evaluation questions for each. What creates relevance? What is the exclusion threat? What does the first stage mean? Who are the compliers? What is the correct level of inference? What is the substantive content of the instrument?

#### 1. Policy Eligibility and Institutional-Rule Instruments

Canonical examples are compulsory schooling laws and quarter of birth [@angrist1991; @oreopoulos2006]. The design logic is that institutional rules move treatment probability for some individuals but not others. These instruments are attractive because the first stage is easy to explain: the instrument shifts legal exposure or eligibility. The main threats are:
- cohort or seasonality effects that directly affect outcomes,
- compositional changes in who is affected,
- and overbroad interpretation of a local schooling margin as if it were universal.

#### 2. Distance / Cost / Access Instruments

Card’s college-proximity design is the classic example [@card1995]. The first stage comes from cost and access. The instrument is compelling when access shifts schooling but does not directly change earnings except through schooling. The exclusion threat is that geography can affect labor markets directly through local opportunity, peer quality, or family background. Students should learn that distance instruments are often really geography designs in disguise, so the exclusion story must be unusually careful.

#### 3. Judge- or Caseworker-Leniency Leave-Out Instruments

These instruments use quasi-random assignment to decision-makers with different propensities to approve, sentence, assign, or grant benefits. A modern example is judge leniency in disability insurance [@autorKostolMogstadSetzler2019]. The leave-one-out construction is important because it avoids mechanical self-influence in estimated leniency. But a leave-out average does not solve everything. The key threats are:
- random assignment may fail,
- judges may affect outcomes through channels other than the target treatment,
- and cases may be selected or routed in ways that violate independence.

#### 4. Shift-Share / Bartik-Style Instruments

A shift-share instrument typically takes the form

```{math}
:label: eq:ssiv
Z_{\ell} = \sum_s w_{\ell s} g_s,
```

where {math}`w_{\ell s}` are exposure shares and {math}`g_s` are shocks. Modern work emphasizes that identification must come from quasi-random shocks, not from treating the shares as harmless by construction [@borusyakHullJaravel2022; @adaoKolesarMorales2019]. This has changed practice. Good shift-share work now asks:
- Are the shocks plausibly exogenous?
- What is the shock level for inference?
- Are exposure shares endogenous in ways that matter?
- Does one need leave-one-out or expected-instrument adjustments?
Students should also learn that standard geographic clustering is often not enough; inference must reflect the shock structure.

#### 5. Historical / Legacy Instruments

Historical instruments are common because past variables can be strongly predictive of current treatments. A famous example is settler mortality as an instrument for institutions [@acemogluJohnsonRobinson2001]. These instruments can be powerful, but they are often the hardest to defend because historical variables typically affect many later outcomes through many channels. The main lesson is not “never use them.” It is: a historical instrument requires an unusually explicit mechanism argument and unusually aggressive robustness and falsification work.

### How to Evaluate an Instrument in Practice

The core evaluation dimensions are:
1. **Economic content of the first stage.** Can you explain why the instrument moves treatment?
2. **Independence.** Why is the instrument as-good-as-random?
3. **Exclusion.** What are the most plausible direct channels from the instrument to the outcome?
4. **Monotonicity and complier interpretation.** Who is being moved?
5. **Support and heterogeneity.** Is the identified effect relevant to the question you care about?
6. **Inference.** At what level is the independent variation realized?
7. **Robustness.** What falsification, sensitivity, or alternative-specification checks are convincing?

A good IV paper names these explicitly. A weak IV paper simply reports 2SLS coefficients.

### When IV Is Best, and When It Is Not

IV is strongest when:
- there is a clear source of quasi-random treatment variation,
- the first stage is economically meaningful,
- the treatment margin induced by the instrument is relevant,
- and the exclusion story is specific and transparent.

IV is weakest when:
- the instrument is weak,
- the first stage is hard to interpret,
- exclusion is vague or wishful,
- different instruments move very different populations,
- or the research question really requires a global average while the design identifies only a narrow local parameter.

## Research Lab

The Lecture 4 Research Lab follows **Reproduce → Diagnose → Transfer**.

**Primary anchor.** Oreopoulos [@oreopoulos2006] is the main reproduction anchor because it is a clean, policy-rule-based IV with a clearly interpretable first stage and a public replication package on the journal page.

**Diagnosis anchor.** Modern shift-share or judge-leniency papers provide the diagnosis anchor. The purpose is not to reproduce every result, but to ask what the first stage means, what the excluded variation actually is, and where the exclusion threat lives [@borusyakHullJaravel2022; @autorKostolMogstadSetzler2019].

**Reproduce.** Students reproduce a bounded IV/2SLS exercise built around a schooling-law or eligibility design on reduced or synthetic data.

**Diagnose.** Students then diagnose the design:
- What is the complier population?
- What is the most plausible exclusion threat?
- Is the first stage strong and substantively meaningful?
- At what level should inference be clustered?
- Would weak-IV robust inference change the conclusion?

**Transfer.** Students then transfer the evaluation logic to a different instrument family, such as shift-share or leave-out leniency, and explain how the instrument should be justified and interpreted in that setting.

## Methods Box

:::{admonition} Methods Box: Practical Instrument Evaluation Checklist
:class: note

A usable IV design should be evaluated along the following dimensions:

```{include} assets/tables/04-instrument-evaluation-dimensions.md
```

The point is not to reject every imperfect instrument. It is to force the researcher to explain where identification comes from, what population is identified, and what assumptions are doing the causal work.

:::

## Reading Ladder And References

**Foundations.** Start with Angrist’s JEP review on instrumental variables and with Imbens and Angrist on LATE [@angrist2001; @imbensAngrist1994].

**Classic anchors.** Read Angrist and Krueger [@angrist1991], Card [@card1995], and Oreopoulos [@oreopoulos2006] to see policy-rule and access-based instruments in action.

**Modern design and caution.** Read Borusyak, Hull, and Jaravel and Adão, Kolesár, and Morales for shift-share design and inference [@borusyakHullJaravel2022; @adaoKolesarMorales2019]. Read Autor et al. for leave-out judge leniency in practice [@autorKostolMogstadSetzler2019].

**Interpretation and limits.** Read Mogstad, Torgovitsky, and Walters on multiple-instrument 2SLS interpretation [@mogstadTorgovitskyWalters2021], and use Acemoglu, Johnson, and Robinson as a case for discussing historical instruments and identification controversy [@acemogluJohnsonRobinson2001].

## Exercises And Discussion Prompts

1. Explain the difference between relevance and exclusion in one sentence each, then give one concrete violation of each.
2. Why does the first stage define the estimand in IV rather than merely its strength?
3. In a schooling design, how do the compliers under quarter of birth differ from the compliers under college proximity?
4. Why is a leave-one-out leniency measure preferred to a raw judge average?
5. What exactly do modern shift-share papers say is the source of identifying variation?
6. Give one setting where a historical instrument might be strong but still unpersuasive.
7. Why can a 2SLS estimate with many instruments be harder to interpret than a single-instrument Wald estimate?
8. Suppose an instrument has a large first stage but an implausible exclusion story. How should you discuss the result?

## Reproducibility And Code Lab Note

The eventual lab folder for this lecture should live at:

`books/empirical-methods/labs/04-instrumental-variables-2sls-and-instrument-design/`

The bounded teaching path should use a reduced or synthetic dataset modeled on a policy-rule IV (for example schooling laws) so the lab is runnable locally without external downloads. If full original data are not bundled, the lab should be explicit that it reproduces the design logic rather than published magnitudes.

## Slide Companion Note

The slide deck for this lecture should live at:

`books/empirical-methods/slides/week4/04-instrumental-variables-2sls-and-instrument-design.tex`

The slides should foreground design logic:
- why IV is needed,
- what the first stage means,
- how Wald and 2SLS connect,
- what LATE means,
- how to evaluate instrument families,
- why IV can fail even when the code runs.

## Bridge Forward

Lecture 4 studies identification by exclusion restrictions. Lecture 5 will move to thresholds and local comparison designs, where identification comes from discontinuities rather than instruments. The recurring theme is the same: what variation identifies the effect, for whom, and under what assumptions?
