# Lecture 4. Instrumental Variables, 2SLS, And Instrument Design

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain IV as a research design built around a source of treatment variation, not as a mechanical fix for endogeneity;
2. derive and interpret the structural equation, first stage, reduced form, Wald estimand, 2SLS projection logic, LATE, and a practical weak-IV diagnostic;
3. state the core IV assumptions: relevance, independence, exclusion, monotonicity, and the substantive content of the first stage;
4. distinguish what IV identifies from what OLS, experiments, DID, or selection-on-observables identify;
5. explain why IV estimates are often local to compliers and why that locality can be useful or limiting;
6. diagnose weak instruments, many-instrument bias, multiple-instrument weighting problems, partial-exclusion concerns, and fragile monotonicity;
7. evaluate policy-rule, distance/access, leniency leave-out, shift-share, and historical instruments using concrete implementation checks;
8. design an instrument by naming the treatment margin, the first-stage mechanism, the exclusion threat, the inference level, and the interpretation of the resulting estimate.

## Opening Orientation

Instrumental variables is one of applied economics' most powerful designs because it can turn endogenous treatment choice into interpretable quasi-experimental variation. It is also one of the easiest methods to misuse. A researcher can always write down a first stage and a second stage. The hard part is explaining why the instrument moves treatment, who it moves, why the movement is as-good-as-random, and why the instrument has no direct effect on the outcome.

This lecture treats IV and 2SLS as design logic. The estimator is the last step. The first step is to identify a source of variation with economic content: a compulsory-schooling rule, distance to college, quasi-random judge assignment, sectoral shocks interacting with local exposure shares, or a historical variable that shifts institutions. Each instrument family has a different first-stage story and a different exclusion problem. Good IV work makes those differences visible. Weak IV work hides behind the phrase "instrumented by."

The paper spine is deliberately design-oriented. Angrist and Krueger show how compulsory-schooling rules and quarter of birth create schooling variation [@angrist1991]. Card uses college proximity as an access-cost instrument [@card1995]. Oreopoulos asks how compulsory schooling identifies local and average effects when the policy rule matters [@oreopoulos2006]. Autor, Kostol, Mogstad, and Setzler show how leave-out judge leniency can identify effects of disability insurance receipt [@autorKostolMogstadSetzler2019]. Adao, Kolesar, and Morales and Borusyak, Hull, and Jaravel changed how economists think about shift-share identification and inference [@adaoKolesarMorales2019; @borusyakHullJaravel2022]. Mogstad, Torgovitsky, and Walters clarify why multiple-instrument 2SLS needs interpretive discipline [@mogstadTorgovitskyWalters2021]. Acemoglu, Johnson, and Robinson anchor the promise and controversy of historical instruments [@acemogluJohnsonRobinson2001].

## Core Points

:::{admonition} Core points
:class: important

- IV is strongest when treatment is endogenous but a well-understood source of quasi-random variation shifts treatment on a substantively meaningful margin.
- The first stage is not a nuisance statistic. It defines the treatment margin, the complier population, and the economic interpretation of the estimate.
- The Wald estimand and 2SLS identify a causal effect only under relevance, independence, exclusion, and an interpretation condition such as monotonicity.
- Under heterogeneous effects, IV generally identifies a local average treatment effect for compliers, not a universal ATE.
- Exclusion is not directly testable; it has to be defended through institutional detail, timing, falsification, mechanisms, and sensitivity.
- Weak instruments, many instruments, and multiple-instrument 2SLS can produce estimates that look formal but are fragile or hard to interpret.
- A credible instrument design explains where the variation lives, how inference should respect that variation, and what the estimate does not identify.
:::

## Bridge

Lecture 3 built counterfactuals from untreated paths. DID, event studies, and synthetic control ask whether untreated units can stand in for treated units' missing untreated outcome path. Lecture 4 changes the source of identification. IV asks whether an external shifter changes treatment while remaining otherwise irrelevant to potential outcomes. The key comparison is no longer a control group path. It is the outcome change induced by the instrument divided by the treatment change induced by the instrument.

Lecture 5 will move to thresholds, kinks, and bunching. Those designs identify effects from local changes around rules. IV also often has a local interpretation, but the locality comes from the people or firms whose treatment status responds to the instrument. The recurring discipline is the same: define the estimand, name the identifying variation, explain the assumptions, and state what the estimate can and cannot support.

## Field Core

### Why Instrumental Variables?

Suppose the researcher wants the effect of treatment {math}`D_i` on outcome {math}`Y_i`:

```{math}
:label: eq:em4-structural
Y_i = \beta D_i + X_i'\gamma + u_i.
```

OLS fails when {math}`D_i` is correlated with {math}`u_i`. In applied economics, this can happen because high-ability students choose more schooling, sicker workers apply for disability benefits, firms adopt technology when demand is changing, families move closer to colleges for reasons related to earnings, or historical institutions are correlated with other persistent features of places. The problem is not merely statistical. It is that observed treatment variation mixes the causal effect with selection, sorting, anticipation, reverse causality, or measurement error.

An instrument {math}`Z_i` is useful when it shifts treatment:

```{math}
:label: eq:em4-first-stage
D_i = \pi Z_i + X_i'\delta + v_i.
```

The same instrument may also shift the outcome in the reduced form:

```{math}
:label: eq:em4-reduced-form
Y_i = \rho Z_i + X_i'\kappa + \varepsilon_i.
```

With one instrument and no controls, the Wald estimand is:

```{math}
:label: eq:em4-wald
\beta^{IV}
=
\frac{\mathbb{E}[Y_i\mid Z_i=1]-\mathbb{E}[Y_i\mid Z_i=0]}
{\mathbb{E}[D_i\mid Z_i=1]-\mathbb{E}[D_i\mid Z_i=0]}
=
\frac{\operatorname{Cov}(Y_i,Z_i)}
{\operatorname{Cov}(D_i,Z_i)}.
```

Equation {eq}`eq:em4-wald` is the central intuition. The numerator is the effect of the instrument on the outcome. The denominator is the effect of the instrument on treatment. The IV estimate scales the reduced-form effect by the treatment movement induced by the instrument. If the instrument moves treatment by 10 percentage points and outcomes by 2 percentage points, the Wald ratio is 0.20 for the margin induced by the instrument.

This makes IV best suited for settings where the treatment is endogenous but the researcher can point to a credible external shifter. IV is not best used as a generic repair for an unconvincing observational design. If the instrument's economic content is vague, the 2SLS coefficient is vague too.

### What IV Identifies And What It Does Not

In the clean homogeneous-effects linear model, IV identifies {math}`\beta` in {eq}`eq:em4-structural`. Most applied work is more interesting and more difficult because treatment effects are heterogeneous. Then the IV estimate is tied to the units whose treatment changes when the instrument changes.

For a binary treatment and binary instrument, define potential treatment states {math}`D_i(1)` and {math}`D_i(0)`. Under the LATE conditions, the Wald estimand identifies:

```{math}
:label: eq:em4-late
\beta^{IV}
=
\mathbb{E}\left[Y_i(1)-Y_i(0)\mid D_i(1)>D_i(0)\right].
```

The conditioning event {math}`D_i(1)>D_i(0)` defines compliers. They take treatment when encouraged or exposed by the instrument and do not take it otherwise. Always-takers, never-takers, and defiers do not define the numerator-denominator ratio in the same way. This is why the first stage is part of the estimand, not just a diagnostic.

IV does not automatically identify:

- the ATE for the full population;
- the ATT for all treated units;
- the effect for always-takers or never-takers;
- a long-run or equilibrium effect beyond the treatment margin induced by the instrument;
- a mechanism unless the instrument and outcomes are designed to isolate one;
- the effect of the instrument itself when the policy question concerns the treatment.

The correct interpretation sentence is usually: "This IV estimate identifies the effect of {math}`D` for the margin of units whose treatment is shifted by {math}`Z`, under relevance, independence, exclusion, and monotonicity, in the population and support represented by the design."

### 2SLS As Projection Logic

With controls or multiple instruments, two-stage least squares uses the part of treatment predicted by the instruments and controls. Let {math}`X` include the exogenous controls, let {math}`D` be the endogenous treatment, and let {math}`Z` contain the excluded instrument or instruments. Define the instrument matrix {math}`W=[X,Z]` and the projection matrix:

```{math}
:label: eq:em4-projection
P_W = W(W'W)^{-1}W'.
```

The fitted treatment from the first stage is:

```{math}
:label: eq:em4-fitted-treatment
\widehat{D}=P_WD.
```

The 2SLS estimator for the coefficient on {math}`D` can be written as the coefficient from regressing {math}`Y` on {math}`\widehat{D}` and {math}`X`, or equivalently:

```{math}
:label: eq:em4-2sls
\widehat{\theta}_{2SLS}
=
(\widetilde{X}'P_W\widetilde{X})^{-1}\widetilde{X}'P_WY,
\qquad
\widetilde{X}=[D,X].
```

This notation should not obscure the design. The first stage removes treatment variation that is not predicted by the instrument. The second stage asks how outcomes vary with that instrument-predicted treatment. If the instrument-predicted treatment has no credible causal interpretation, the 2SLS coefficient has no credible causal interpretation either.

Controls in IV play the same role as controls elsewhere: they define the comparison and the conditional independence claim. A quarter-of-birth design may condition on year and state of birth. A distance instrument may condition on local background and region. A judge-leniency design may condition on court, time, charge, and assignment cells. Adding post-treatment controls or variables affected by the instrument can destroy the interpretation.

### The Core IV Assumptions

**Relevance.** The instrument must move treatment after conditioning on the design controls:

```{math}
:label: eq:em4-relevance
\operatorname{Cov}(Z_i,D_i\mid X_i)\neq 0.
```

Relevance has two parts. The statistical part is whether {math}`Z` predicts {math}`D`. The economic part is what margin of treatment {math}`Z` moves. A compulsory-schooling law moves students near the legal school-leaving margin. College proximity moves students whose education responds to access costs. Judge leniency moves cases near a decision-maker's approval threshold. A first stage can be statistically strong and still economically unhelpful if the researcher cannot say what margin it represents.

**Independence.** The instrument must be as-good-as-random relative to the relevant potential outcomes and potential treatment states, usually after controls:

```{math}
:label: eq:em4-independence
Z_i \perp \{Y_i(1),Y_i(0),D_i(1),D_i(0)\}\mid X_i.
```

Independence is an assignment claim. It asks whether quarter of birth, judge assignment, sectoral shocks, or historical exposure is unrelated to unobserved determinants of outcomes after the researcher conditions on the right cells. The evidence is institutional: assignment protocols, timing, routing rules, predetermined shares, balance checks, and knowledge of how the data were generated.

**Exclusion.** The instrument affects the outcome only through treatment:

```{math}
:label: eq:em4-exclusion
Y_i(d,z)=Y_i(d)
\quad \text{for all } d,z.
```

Exclusion is usually the hardest IV assumption. Quarter of birth may capture seasonality or age-at-school-entry channels. Distance to college may proxy local labor markets or family background. Judges may affect defendants or applicants through effort, information, stigma, or other case outcomes. Shift-share shocks may affect places through general-equilibrium channels beyond the measured treatment. Historical variables may affect current outcomes through many persistent channels. Algebra cannot test exclusion directly; the paper has to make the direct channels visible and then narrow them.

**Monotonicity.** The instrument must not push some units toward treatment and others away from it:

```{math}
:label: eq:em4-monotonicity
D_i(1)\ge D_i(0)
\quad \text{for all } i.
```

Monotonicity can be plausible in one-sided encouragement, eligibility, or leniency settings. It becomes harder in settings with strategic behavior, multiple treatment versions, or instruments that change costs and benefits differently across groups. If a distance instrument encourages some students to attend college while discouraging others from moving away, the complier story becomes less clean. If a shift-share shock raises treatment in some sectors and lowers it in others, monotonicity may not be the right interpretive frame.

**First-stage content.** The first stage must be substantively interpretable. This is not always listed as a separate textbook assumption, but it is a practical requirement for applied work. The first stage tells readers whether the instrument moves treatment at a policy-relevant margin, whether the compliers are central or peripheral to the economic question, and whether the IV estimate should be compared to OLS, experimental evidence, or another local design.

### Weak Instruments, Many Instruments, And Fragile Inference

A weak first stage can make 2SLS misleading even when the instrument is conceptually attractive. Bound, Jaeger, and Baker made this warning central for applied IV work, and Staiger and Stock formalized weak-IV behavior [@bound1995; @staigerStock1997]. Weak instruments produce noisy estimates, finite-sample bias toward OLS, unstable signs, and confidence intervals that can be far too optimistic under conventional approximations.

A practical first-stage diagnostic for {math}`q` excluded instruments compares the unrestricted first stage with instruments to a restricted first stage without them:

```{math}
:label: eq:em4-partial-f
F_{\text{excluded }Z}
=
\frac{(RSS_R-RSS_U)/q}{RSS_U/(n-k_U)}.
```

Here {math}`RSS_R` is the residual sum of squares from the restricted first stage, {math}`RSS_U` is the residual sum of squares from the unrestricted first stage, and {math}`k_U` is the number of parameters in the unrestricted first stage. The partial {math}`F` statistic is not a magic pass-fail rule. It is a warning light. Report it with the first-stage coefficient, the economic magnitude of the first stage, and the relevant weak-IV robust inference when the design is fragile. Stock and Yogo provide classic critical-value logic for linear IV, but applied interpretation still has to begin from the source of variation [@stockYogo2005].

Many instruments create another problem. Adding more instruments can increase first-stage fit, but it can also overfit treatment and reintroduce endogeneity into fitted values. Many-instrument bias is especially dangerous when the number of instruments grows with the sample or when instruments are mechanically generated from many cells. Leave-one-out and split-sample constructions can reduce mechanical overfitting in some settings, but they do not solve exclusion or interpretation.

Multiple instruments also complicate meaning. Mogstad, Torgovitsky, and Walters show that 2SLS with several instruments can combine different complier groups and different treatment margins [@mogstadTorgovitskyWalters2021]. The resulting coefficient may be a weighted average of instrument-specific local effects, but the weights can be hard to see and may not match the target population. "More instruments" is useful only when the instruments belong to a coherent design.

### Limitations Of IV

IV is often credible precisely because it is narrow. That narrowness should be reported, not hidden.

**Exclusion is not directly testable.** A reduced form and a first stage do not prove that the only pathway from {math}`Z` to {math}`Y` runs through {math}`D`. Placebo outcomes, predetermined covariate balance, alternative controls, mechanism checks, and sensitivity analysis can strengthen the case, but the exclusion restriction remains an assumption. Conley, Hansen, and Rossi provide one way to study plausibly exogenous instruments when the direct effect may be small but not exactly zero [@conleyHansenRossi2012].

**LATE is local and complier-specific.** This can be a strength when compliers are the policy margin of interest. It is a limitation when the question asks about all treated units, all workers, all firms, or long-run equilibrium response. An estimate of returns to schooling for students moved by compulsory-schooling laws is not automatically the return for college-bound students.

**Monotonicity may fail or be hard to defend.** Instruments can change multiple incentives at once. They may induce substitution across treatment versions, avoidance behavior, or sorting. If the instrument can both increase and decrease treatment for different units, the LATE interpretation becomes fragile.

**Weak instruments can dominate the design.** A beautiful institutional story with little first-stage movement may not identify much. Weak-IV robust inference and transparent first-stage magnitudes are part of the design, not optional robustness.

**Many instruments and generated instruments can overfit.** Flexible first stages, many interactions, or many leave-out cells can make the fitted treatment look strong while the identifying variation becomes noisy or opaque.

**Multiple-instrument 2SLS may be hard to interpret.** If one instrument moves low-income students, another moves rural students, and a third moves older students, the combined coefficient may not answer a clear policy question.

**The instrument's own economic content may matter more than the estimator.** If distance to college affects local labor-market opportunities directly, the coefficient is partly a geography design. If judge leniency changes information or stigma, the coefficient is partly a judge-contact design. If a historical instrument moves many modern institutions at once, the coefficient is not cleanly about the one institution named in the first stage. The instrument is never just a variable; it is an economic object.

### Theory-To-Applied Design Through Papers

The theory-to-applied bridge for this lecture is:

```{include} assets/tables/04-theory-to-applied-bridge.md
```

Angrist and Krueger are the classical rule-based IV anchor [@angrist1991]. Quarter of birth matters because compulsory-schooling laws link birth timing to the earliest legal school-leaving age. The first stage is a policy-rule margin: students induced to stay in school longer by legal exposure. The exclusion threat is that quarter of birth may capture seasonality, age-at-entry, cohort interactions, or other channels that directly affect earnings.

Oreopoulos sharpens the local interpretation [@oreopoulos2006]. Compulsory-schooling laws can have large first stages when they truly bind, and the LATE can be closer to a policy-relevant margin than a generic schooling return. The design question is whether the affected students are the population the paper wants to learn about.

Card's college-proximity instrument is powerful because access and cost are economically meaningful [@card1995]. It also teaches the core danger of distance instruments: geography affects many things. Family background, local labor-market opportunity, school quality, peers, and migration all travel with distance.

Autor, Kostol, Mogstad, and Setzler make modern leave-out leniency concrete [@autorKostolMogstadSetzler2019]. The design uses quasi-random assignment to decision-makers with different propensities to award disability benefits. The leave-out construction avoids letting a case mechanically contribute to its own instrument. The remaining question is whether judge assignment is random within cells and whether judges affect outcomes only through benefit receipt.

Adao, Kolesar, and Morales and Borusyak, Hull, and Jaravel changed shift-share practice [@adaoKolesarMorales2019; @borusyakHullJaravel2022]. Modern shift-share papers no longer treat exposure shares as automatically harmless. They ask whether identification comes from quasi-random shocks, whether shares are endogenous, and whether inference should be organized at the shock level.

Acemoglu, Johnson, and Robinson are essential because historical instruments reveal both ambition and fragility [@acemogluJohnsonRobinson2001]. Settler mortality is intended to shift colonial institutions, but historical variables often affect modern outcomes through many persistent channels. The teaching point is not to dismiss historical IV. It is to demand a mechanism argument that is much more explicit than the first-stage table.

### Instrument Design Gallery

```{include} assets/tables/04-instrument-design-gallery.md
```

#### Policy Eligibility And Institutional-Rule Instruments

Policy-rule instruments use institutional thresholds, eligibility rules, or legal exposure to shift treatment. Quarter-of-birth and compulsory-schooling designs are the canonical examples [@angrist1991; @oreopoulos2006]. Other examples include benefit eligibility, age-based rules, lottery priority, and administrative assignment rules.

The first stage means that the rule changes the probability or intensity of treatment. In schooling applications, the instrument moves education for students near the minimum leaving age. In program applications, it moves take-up among people near an eligibility margin.

The main exclusion threats are direct rule effects, cohort effects, seasonality, anticipation, and simultaneous policies. If the legal rule changes school quality, labor-market entry age, peer cohorts, or local enforcement directly, the exclusion restriction is no longer just about schooling. Implementation should define the rule precisely, show the first stage by affected cohorts or cells, report reduced forms, and avoid interpreting the estimate as a global treatment effect.

#### Distance, Cost, And Access Instruments

Distance and access instruments use variation in the cost of treatment. Card's college-proximity design is the classic schooling example [@card1995]. In other fields, researchers use distance to hospitals, courts, service providers, training centers, transit, or administrative offices.

The first stage means that lower travel cost, information cost, or access cost increases treatment take-up. The compliers are people whose behavior changes because access is easier. This is often a relevant policy margin: building a college, opening a clinic, or changing transport costs can matter exactly through access.

The exclusion problem is that distance is rarely random geography. Nearby colleges may be located in areas with different wages, peer networks, school quality, family resources, amenities, or migration patterns. A distance instrument should report rich geographic controls, pre-treatment covariate balance, sensitivity to alternative distance bands, and a careful interpretation of compliers. The researcher should also ask whether the outcome can be affected directly by access even without treatment.

#### Judge Or Caseworker Leniency Leave-Out Instruments

Leniency instruments use quasi-random assignment to decision-makers who differ in their propensity to assign treatment. Judges, caseworkers, examiners, physicians, teachers, or administrators may be more or less likely to grant benefits, sentence defendants, recommend services, classify disability, approve loans, or assign programs. Autor, Kostol, Mogstad, and Setzler use judge leniency to study disability insurance [@autorKostolMogstadSetzler2019].

The instrument is usually a leave-out measure:

```{math}
:label: eq:em4-leave-out-leniency
Z_{ij}
=
\frac{1}{N_j-1}\sum_{k\neq i: J_k=j}D_k,
```

where {math}`J_k=j` means case {math}`k` was assigned to decision-maker {math}`j`. The leave-one-out construction prevents case {math}`i` from mechanically affecting its own instrument. In practice, researchers often residualize leniency within court, office, time, or case-type cells before using it.

The first stage means that cases assigned to more lenient decision-makers are more likely to receive treatment. The compliers are marginal cases whose treatment status depends on decision-maker style. Random assignment must be credible within the assignment cells: no strategic routing, no manipulation, no systematic case sorting, and enough balance on predetermined characteristics.

Exclusion can still fail. Lenient decision-makers may affect outcomes through channels other than the target treatment: information, monitoring, processing time, stigma, recommendations, sentence length, appeal behavior, or connected services. A strong paper documents the assignment process, tests balance within cells, uses leave-out or split-sample construction, clusters at an appropriate decision-maker or assignment-cell level when needed, and interprets the effect as local to marginal cases.

#### Shift-Share And Bartik-Style Instruments

A shift-share instrument combines predetermined exposure shares with shocks:

```{math}
:label: eq:em4-shift-share
Z_{\ell}
=
\sum_s w_{\ell s}g_s,
```

where {math}`w_{\ell s}` is location {math}`\ell`'s exposure to sector {math}`s`, and {math}`g_s` is a sectoral shock. Classic applications use industry shares interacted with national industry growth, trade shocks, technology shocks, or demographic shocks.

The first stage means that places, firms, or groups with different baseline exposure are differentially affected by common shocks. The treatment might be immigrant inflows, trade exposure, automation exposure, labor demand, or policy exposure. The instrument is persuasive only when the shock variation or the exposure-share variation has a credible exogeneity story.

Modern shift-share work changed practice in three ways [@adaoKolesarMorales2019; @borusyakHullJaravel2022]. First, researchers must say whether identification comes from quasi-random shocks, as in a shock-level design, or from as-good-as-random shares. Second, exposure shares can be endogenous because historical industry composition reflects local productivity, institutions, amenities, or trends. Third, inference should reflect the shock structure. If many locations are exposed to the same small set of shocks, clustering only by geography can overstate precision. Shock-level clustering, exposure-robust standard errors, leave-one-out shocks, and sensitivity to dominant sectors become part of the design.

The main exclusion threats are direct effects of shocks on outcomes beyond the measured treatment, endogenous shares, correlated sectoral trends, and general-equilibrium spillovers. A strong shift-share paper reports the exposure-share construction, shock source, leave-one-out choices, dominant-shock diagnostics, balance or pre-trend evidence by exposure, and inference matched to the level of independent shock variation.

#### Historical And Legacy Instruments

Historical instruments use past conditions to shift current treatment or institutions. Acemoglu, Johnson, and Robinson's settler-mortality design is the canonical teaching example [@acemogluJohnsonRobinson2001]. Other examples use historical infrastructure, settlement patterns, missions, land institutions, administrative boundaries, or technological constraints.

The first stage means that a historical variable predicts a current institution, treatment, or exposure. The appeal is that history may precede modern outcomes by decades or centuries. The danger is that history creates many paths to the present. A historical instrument can affect income through institutions, human capital, geography, health, migration, conflict, legal origins, state capacity, or culture.

The implementation burden is therefore high. The researcher should name the mechanism, show that the first stage corresponds to that mechanism, address alternative persistent channels, report sensitivity to geographic and historical controls, use placebo outcomes when possible, and avoid interpreting the coefficient as if the instrument moved only one modern variable. Historical IV is at its best when the historical story is narrow enough to be falsifiable.

### How To Evaluate An Instrument In Practice

A usable IV design answers seven questions before the main table:

1. What treatment margin does the instrument move?
2. What institutional, geographic, assignment, shock, or historical process makes the instrument as-good-as-random?
3. What direct channels from the instrument to the outcome are most plausible?
4. Who are the compliers, and are they the population the paper cares about?
5. Is the first stage strong in statistical and economic terms?
6. Where does independent variation live for inference?
7. What result would make the design less credible: pre-trends, placebo outcomes, alternative controls, balance failures, weak first stage, or sensitivity to a single shock?

This evaluation should happen before the second-stage coefficient becomes the center of attention. A good IV paper is a theory of variation plus diagnostics plus interpretation. The regression is the implementation.

## Research Lab

The Lecture 4 Research Lab follows **Reproduce -> Diagnose -> Transfer**.

**Primary anchor.** The main reproduction anchor is Oreopoulos, with Angrist and Krueger as the classical companion [@oreopoulos2006; @angrist1991]. Students work with a deterministic synthetic teaching path modeled on compulsory-schooling exposure. The lab does not reproduce published magnitudes. It reproduces the design logic: rule-based instrument, first stage, reduced form, Wald ratio, 2SLS, weak-IV diagnostics, and complier interpretation.

**Diagnosis anchor.** The diagnosis anchor is judge-leniency leave-out IV [@autorKostolMogstadSetzler2019]. Students inspect why leave-out construction matters, what quasi-random assignment must look like, and why exclusion can fail if decision-makers affect outcomes through information, timing, stigma, monitoring, or other treatment channels.

**Reproduce.** Students estimate the naive relationship between schooling and earnings, the first stage from compulsory-schooling exposure to staying in school, the reduced form from exposure to earnings, the Wald ratio, and the 2SLS estimate with controls. They compare OLS and IV and explain why the IV estimate should be interpreted as a complier effect.

**Diagnose.** Students inspect first-stage magnitudes, partial {math}`F` statistics, balance by instrument status, reduced-form signs, and the synthetic complier profile. They write a short memo naming the most plausible exclusion threat and the inference level.

**Transfer.** Students transfer the same evaluation logic to a synthetic shift-share design [@adaoKolesarMorales2019; @borusyakHullJaravel2022]. They construct exposure from baseline sector shares and sector shocks, diagnose dominant shocks and endogenous shares, and explain why inference should reflect the shock structure rather than only the number of places.

The central lab question is not "did 2SLS run?" It is "what variation did the instrument isolate, for whom, and under which assumptions?"

## Methods Box

:::{admonition} Methods Box: Practical Instrument Evaluation Checklist
:class: note

```{include} assets/tables/04-instrument-evaluation-dimensions.md
```

A strong instrument design turns each row of this checklist into observable evidence. It reports the first stage in economic units, makes the exclusion threat specific, explains the complier population, matches inference to the source of variation, and states exactly what the IV estimate leaves unidentified.
:::

## Reading Ladder And References

```{include} assets/tables/04-reading-architecture.md
```

**Foundations.** Start with Imbens and Angrist on LATE, Angrist, Imbens, and Rubin on IV causal effects, Angrist's JEP review, and Angrist and Pischke for applied implementation [@imbensAngrist1994; @angristImbensRubin1996; @angrist2001; @angristPischke2009].

**Classic schooling and access designs.** Read Angrist and Krueger, Card, and Oreopoulos together [@angrist1991; @card1995; @oreopoulos2006]. The design comparison is useful: rule-based exposure, geographic access, and binding compulsory laws move different people.

**Weak instruments and sensitivity.** Read Bound, Jaeger, and Baker, Staiger and Stock, Stock and Yogo, and Conley, Hansen, and Rossi [@bound1995; @staigerStock1997; @stockYogo2005; @conleyHansenRossi2012]. These papers explain why a nonzero first stage is not enough and how to think about imperfect exclusion.

**Modern instrument families.** Read Autor, Kostol, Mogstad, and Setzler for leave-out leniency; Adao, Kolesar, and Morales and Borusyak, Hull, and Jaravel for shift-share; and Mogstad, Torgovitsky, and Walters for multiple-instrument interpretation [@autorKostolMogstadSetzler2019; @adaoKolesarMorales2019; @borusyakHullJaravel2022; @mogstadTorgovitskyWalters2021].

**Historical instruments and debate.** Use Acemoglu, Johnson, and Robinson as the anchor for historical IV [@acemogluJohnsonRobinson2001]. The value for this lecture is not only the result, but the debate it opens about persistence, exclusion, and mechanism specificity.

## Exercises And Discussion Prompts

1. Write the structural equation, first stage, reduced form, and Wald estimand for a binary encouragement design. Interpret each equation in words.
2. In a compulsory-schooling IV, who are the likely compliers? Why might their return to schooling differ from the ATE?
3. Give one example where relevance is strong but exclusion is weak. Give one example where exclusion is plausible but relevance is weak.
4. In Card's college-proximity design, list three direct geography channels that could violate exclusion. What evidence would make each less concerning?
5. Explain why a leave-one-out leniency instrument is preferred to a raw judge approval rate. What problem does leave-one-out solve, and what does it not solve?
6. For a shift-share instrument, state whether identification comes from shocks or shares. What inference level follows from that answer?
7. Suppose a paper uses five instruments for one endogenous treatment. What questions should you ask before interpreting the 2SLS coefficient?
8. Why does a high first-stage {math}`F` statistic not prove that the instrument is valid?
9. Take a historical instrument in a published paper. Name the first-stage mechanism, the main direct-channel threat, and one falsification exercise you would want.
10. Design an IV for a labor-market question of your choice. Define the treatment, instrument, first stage, exclusion restriction, likely compliers, inference level, and what the design cannot identify.

## Reproducibility And Code Lab Note

The Lecture 4 code lab lives at `labs/04-instrumental-variables-2sls-and-instrument-design/`. It is a bounded synthetic teaching path inspired by compulsory-schooling IV designs and modern instrument-design diagnostics. It does not claim to reproduce the original papers' data or published magnitudes.

The smoke path creates deterministic synthetic data, estimates OLS, first-stage, reduced-form, Wald, and 2SLS objects, computes a partial first-stage {math}`F` statistic, writes balance and complier diagnostics, and then runs a shift-share transfer exercise. The lab is small enough to run locally without external downloads.

## Slide Companion Note

The Lecture 4 slide deck lives at `slides/week4/04-instrumental-variables-2sls-and-instrument-design.tex`. The deck mirrors the chapter without duplicating it: it defines why IV is needed, shows Wald and 2SLS, states the assumptions, covers weak and many instruments, compares instrument families, gives dedicated attention to shift-share and leniency leave-out designs, and closes with the Research Lab design.

## Bridge Forward

Lecture 4 studies identification by excluded variation. Lecture 5 moves to regression discontinuity, regression kink, and bunching designs, where rules create local changes in treatment, incentives, or density around thresholds. IV teaches students to ask which margin responds to an instrument. RD asks which margin exists at a cutoff. Both designs are credible only when the local source of variation is economically understood.
