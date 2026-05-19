# Lecture 5. Regression Discontinuity, RKD, Bunching, And Local Designs

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain when a local-threshold design is preferable to experiments, DID/event studies, IV, or selection-on-observables;
2. derive and interpret sharp RD, fuzzy RD, local-polynomial RD, RKD, and bunching estimands;
3. distinguish what RD, RKD, and bunching identify from what they do not identify;
4. treat bandwidth, weighting, polynomial order, covariates, clustering, and inference as design choices rather than software defaults;
5. explain the logic of robust bias correction, honest inference, covariate adjustment, and the modern rejection of high-order global polynomials;
6. evaluate RD in time, spatial RD, RKD, and bunching with their design-specific threats;
7. compare the major Block 1 causal designs in terms of counterfactual logic, interference risk, strengths, weaknesses, and applied credibility;
8. translate a threshold-based applied question into a reproducible research design with a clear estimand and robustness plan.

## Opening Orientation

Regression discontinuity is often described as the closest observational cousin of a randomized experiment. That instinct is useful, but it can make the design sound too easy. A cutoff does not create credibility by itself. The design earns credibility when the institutional threshold is meaningful, the running variable cannot be precisely manipulated, potential outcomes are smooth at the cutoff, and the researcher makes local estimation choices visible.

This lecture treats regression discontinuity, regression kink designs, bunching, RD in time, and spatial RD as a family of **local designs**. The common logic is that rules, schedules, borders, or thresholds create a sharp change in the level of treatment, the probability of treatment, the slope of incentives, or the density of choices. The differences matter. A sharp RD identifies a local level jump. A fuzzy RD identifies a local Wald ratio. An RKD identifies a local slope ratio. A bunching design uses excess mass around a kink or notch, usually with an optimization model, to recover a behavioral response.

The paper spine follows that design logic. Hahn, Todd, and van der Klaauw establish the RD identification problem [@hahnToddVanderklaauw2001]. Imbens and Lemieux and Lee and Lemieux translate RD into applied practice [@imbensLemieux2008; @leeLemieux2010]. Lee's close-election design is the canonical applied anchor because the running variable and local comparison are visible [@lee2008]. Calonico, Cattaneo, and Titiunik make robust bias correction central to modern RD inference [@calonicoCattaneoTitiunik2014]. Armstrong and Kolesar formalize honest inference under explicit smoothness restrictions [@armstrongKolesar2020]. Gelman and Imbens explain why high-order global polynomials are poor RD practice [@gelmanImbens2019]. Hausman and Rapson clarify why RD in time is not just an event study without controls [@hausmanRapson2018]. Dell and Saez anchor spatial RD and bunching applications [@dell2010; @saez2010].

## Core Points

:::{admonition} Core points
:class: important

- RD-style methods are strongest when an institutional rule creates sharp local variation and continuity near the threshold is more believable than a global selection or trend assumption.
- The estimand is local: sharp RD identifies a jump at the cutoff, fuzzy RD a local Wald ratio, RKD a slope discontinuity ratio, and bunching a response around a kink or notch under a behavioral model.
- Local-polynomial estimation, triangular weighting, bandwidth choice, covariates, clustering, and inference are part of the design, not after-the-fact tuning.
- Robust bias correction and honest inference answer different questions: `rdrobust`-style inference estimates and corrects leading local-polynomial bias, while `rdhonest`-style inference reports intervals valid under an explicit smoothness class.
- High-order global polynomials are discouraged because they can manufacture boundary behavior far from the cutoff and make local evidence look more precise than it is.
- Time RD and spatial RD require extra discipline because dates and borders bring serial correlation, seasonality, anticipation, geographic sorting, spillovers, and multidimensional continuity problems.
- Bunching is not model-free RD. The excess mass is informative only through a credible counterfactual density and an economic model of optimization, salience, and frictions.
- A high-credibility RD paper still has to say what the estimate does not identify: global effects, long-run equilibrium effects, effects away from the cutoff, or effects for units that can sort around the threshold.
:::

## Bridge

Lecture 4 used instruments to isolate treatment variation from endogenous choice. The key IV question was: what variation in treatment is induced by the instrument, and why is the instrument otherwise excluded from outcomes? Lecture 5 changes the source of variation. Local-threshold designs ask whether units just around a rule, score, date, border, kink, or notch can reveal the missing counterfactual.

This is the last lecture of Block 1. The block began with potential outcomes and selection-on-observables, moved through experiments, DID/event studies, synthetic control, and IV, and now ends with local threshold designs. The recurring discipline is the same across the block: define the estimand, name the identifying variation, state the assumptions, diagnose threats, and interpret the estimate within the support that actually identifies it.

## Field Core

### Why Local Threshold Designs?

A local threshold design is most persuasive when the threshold is part of the economic object. Examples include test-score cutoffs for school admission, election vote-share thresholds, age or income eligibility rules, benefit formula kinks, tax notches, environmental regulation boundaries, minimum-population thresholds for transfers, and administrative borders that separate institutional regimes. In these settings the rule is not a nuisance. It defines the comparison.

RD is best used when:

- treatment changes sharply at a known cutoff;
- units just above and below the cutoff are plausibly comparable;
- the running variable is measured before treatment and cannot be precisely manipulated at the threshold;
- the local effect at the cutoff is substantively meaningful;
- enough observations exist near the cutoff to estimate a local comparison without relying on global functional form.

RD is not best used when the cutoff is arbitrary but irrelevant to the question, when the running variable is heavily manipulated, when treatment changes gradually with no first-stage jump, when the outcome has its own discontinuity at the cutoff for reasons unrelated to treatment, or when the paper's main claim is about populations far from the threshold.

The interpretation sentence for a sharp RD should sound local: "Under continuity of potential outcomes at the cutoff and no precise manipulation, the jump in the conditional expectation of the outcome at the threshold identifies the treatment effect for units at that cutoff." If that sentence is too narrow for the paper's question, the researcher needs a portability argument, a different design, or both.

### Sharp RD

Let {math}`X_i` be a running variable, {math}`c` the cutoff, and {math}`D_i` treatment. In a sharp RD, treatment is fully determined by the threshold:

```{math}
:label: eq:em5-sharp-rd-assignment
D_i=\mathbf{1}\{X_i \ge c\}.
```

Let potential outcomes be {math}`Y_i(1)` and {math}`Y_i(0)`. The continuity condition is:

```{math}
:label: eq:em5-rd-continuity
\lim_{x\downarrow c}\mathbb{E}[Y_i(d)\mid X_i=x]
=
\lim_{x\uparrow c}\mathbb{E}[Y_i(d)\mid X_i=x],
\qquad d\in\{0,1\}.
```

Under {eq}`eq:em5-rd-continuity`, the sharp RD estimand is the discontinuity in conditional expectations:

```{math}
:label: eq:em5-sharp-rd-estimand
\tau_{SRD}
=
\lim_{x\downarrow c}\mathbb{E}[Y_i\mid X_i=x]
-
\lim_{x\uparrow c}\mathbb{E}[Y_i\mid X_i=x].
```

This identifies:

```{math}
:label: eq:em5-sharp-rd-effect
\tau_{SRD}
=
\mathbb{E}[Y_i(1)-Y_i(0)\mid X_i=c].
```

The estimand is a treatment effect at the cutoff. Lee's close-election design makes the intuition concrete [@lee2008]. Candidates barely above 50 percent win office; candidates barely below lose. If potential future outcomes are smooth in the vote margin absent winning, the discontinuity in later outcomes at the 50 percent cutoff identifies the local effect of winning office for barely winning candidates.

Sharp RD does **not** identify the effect for landslide winners, the effect in elections far from the cutoff, or the effect of a different institutional rule. It also does not automatically identify mechanisms. If winning changes fundraising, media attention, party resources, and future ballot access, the RD estimates the package induced by winning at the threshold.

Implementation caveats are concrete. The researcher should center the running variable at the cutoff; estimate separate functions on each side; report the bandwidth, polynomial order, kernel, and effective sample size on each side; inspect binscatter or RD plots; test continuity of predetermined covariates; check density or heaping around the cutoff; and avoid choosing specifications after inspecting the preferred result. If treatment assignment is grouped by schools, districts, counties, dates, or elections, inference should respect that grouping.

### Fuzzy RD

In a fuzzy RD, crossing the cutoff changes the probability of treatment but does not perfectly determine it. Let {math}`Z_i=\mathbf{1}\{X_i\ge c\}` be threshold eligibility or assignment. The first-stage discontinuity is:

```{math}
:label: eq:em5-fuzzy-rd-first-stage
\Delta_D
=
\lim_{x\downarrow c}\mathbb{E}[D_i\mid X_i=x]
-
\lim_{x\uparrow c}\mathbb{E}[D_i\mid X_i=x].
```

When {math}`\Delta_D\neq 0`, the fuzzy RD estimand is a local Wald ratio:

```{math}
:label: eq:em5-fuzzy-rd-estimand
\tau_{FRD}
=
\frac{
\lim_{x\downarrow c}\mathbb{E}[Y_i\mid X_i=x]
-
\lim_{x\uparrow c}\mathbb{E}[Y_i\mid X_i=x]
}{
\lim_{x\downarrow c}\mathbb{E}[D_i\mid X_i=x]
-
\lim_{x\uparrow c}\mathbb{E}[D_i\mid X_i=x]
}.
```

Fuzzy RD is best used when eligibility, assignment, or a rule shifts take-up locally but compliance is incomplete. Examples include income eligibility for a program with imperfect take-up, age eligibility for a benefit with delayed claiming, or admission rules where some admitted students decline and some rejected students find another route.

What it identifies is a local average treatment effect for units at the cutoff whose treatment status is shifted by crossing the threshold, under continuity and a monotonicity-style interpretation. What it does not identify is the ATE for all eligible units, the effect for always-takers or never-takers, or the effect far from the cutoff. The first-stage jump is part of the estimand. A tiny or substantively opaque jump makes the Wald ratio fragile even if the outcome jump is visible.

Implementation should present the outcome discontinuity, treatment discontinuity, and Wald ratio together. In practice, the same bandwidth, polynomial order, and kernel should usually be used for the reduced form and first stage unless there is a pre-specified reason to differ. Report the first-stage magnitude in units readers understand, not only as a coefficient.

### Local Polynomial Estimation

Modern RD practice estimates the two conditional expectations locally rather than imposing a global functional form. Let {math}`R_i=X_i-c` be the centered running variable, {math}`h` the bandwidth, and {math}`K(\cdot)` the kernel weight. A local linear RD can be written as the weighted least-squares problem:

```{math}
:label: eq:em5-local-polynomial
\min_{\alpha_-,\alpha_+,\beta_-,\beta_+}
\sum_i
K\!\left(\frac{R_i}{h}\right)\mathbf{1}\{|R_i|\le h\}
\left[
Y_i
-\alpha_-
-\beta_-R_i
-\mathbf{1}\{R_i\ge 0\}\left(\alpha_+-\alpha_-+(\beta_+-\beta_-)R_i\right)
\right]^2.
```

The estimated RD effect is:

```{math}
:label: eq:em5-local-polynomial-tau
\widehat{\tau}_{RD}=\widehat{\alpha}_+-\widehat{\alpha}_-.
```

Equation {eq}`eq:em5-local-polynomial` is practical. It says that observations closer to the cutoff receive more weight, observations outside the bandwidth receive no weight, and the fitted outcome surface can have different intercepts and slopes on the two sides. Local quadratic estimation adds side-specific quadratic terms. Local linear estimation is often the default because RD is a boundary problem: the cutoff is at the edge of the left and right local samples, and local linear fits correct first-order boundary bias better than local constant means.

The triangular kernel is the standard default:

```{math}
:label: eq:em5-triangular-kernel
K(u)=(1-|u|)\mathbf{1}\{|u|\le 1\}.
```

Triangular weights concentrate attention near the cutoff, where the continuity assumption is most plausible. Uniform weights can be useful as a transparent sensitivity check because they show the simple local-regression contrast inside the bandwidth. Other kernels usually matter less than bandwidth and polynomial order, but they still define the effective comparison. A paper should report the kernel because weighting is part of the estimator.

Bandwidth is the core bias-variance choice. A large bandwidth increases precision but risks using observations whose potential outcomes are not locally comparable. A small bandwidth makes the comparison more local but increases variance and can make the estimate sensitive to a handful of observations or mass points. Data-driven bandwidth selectors are useful because they make the tradeoff explicit, but they do not eliminate judgment. A good applied RD reports the selected bandwidth, nearby bandwidth sensitivity, effective sample sizes, and whether the economic interpretation changes as the window narrows.

### Modern RD Inference And Specification Discipline

Modern RD is not "run a polynomial and read the jump." Four implementation choices now carry much of the credibility burden.

**Robust bias correction.** Local-polynomial estimators can have non-negligible bias when the bandwidth is chosen to balance mean squared error. Calonico, Cattaneo, and Titiunik estimate the leading bias term using a higher-order local polynomial, subtract that estimated bias from the point estimate, and adjust the variance to reflect the extra estimation step [@calonicoCattaneoTitiunik2014]. This is the logic behind `rdrobust`. In applied reporting, a baseline `rdrobust`-style table should include the conventional local-polynomial estimate, the robust bias-corrected estimate, robust standard errors, bandwidths for the point estimate and bias correction, polynomial orders, kernel, and effective observations on each side.

**Honest inference.** Robust bias correction relies on local-polynomial smoothness assumptions and estimates the bias. Armstrong and Kolesar's honest approach instead asks what interval remains valid if the regression function belongs to a stated smoothness class, such as a bound on curvature [@armstrongKolesar2020]. This is the logic behind `rdhonest`. Honest intervals are especially useful when readers are worried that the outcome surface may bend adversarially within the selected bandwidth. The tradeoff is that the interval can be wider and the smoothness bound must be defended rather than hidden.

**Covariates.** Predetermined covariates can improve precision and handle chance imbalance, but they do not create RD identification. Calonico, Cattaneo, Farrell, and Titiunik show how covariate adjustment can be incorporated without changing the estimand under appropriate conditions [@calonicoCattaneoFarrellTitiunik2019]. The applied rule is simple: use only pre-treatment covariates, report whether covariates are continuous at the cutoff, avoid controls affected by the threshold, and show that the main interpretation does not depend on covariates. If adding covariates changes the point estimate sharply, treat that as a diagnostic, not as a victory.

**Polynomial discipline.** High-order global polynomials are discouraged because they can use far-away data to shape boundary behavior at the cutoff [@gelmanImbens2019]. They can also generate visually smooth curves that imply enormous extrapolation leverage. Local linear or local quadratic fits with transparent bandwidths are the modern default. If a paper shows a global polynomial figure for visualization, the causal estimate should still come from local estimation.

**Clustering and dependence.** RD standard errors should match the design. If treatment varies at the individual running-variable level and observations are independent, heteroskedasticity-robust inference may be appropriate. If the running variable has mass points, assignment is grouped, outcomes are measured by cluster, or repeated observations appear around the cutoff, cluster or design-level inference is needed. In time RD, serial correlation is first-order. In spatial RD, nearby units often share shocks, amenities, and spillovers. Under-clustering can make a local estimate look far more precise than the design warrants.

**Manipulation and support.** Density checks, heaping diagnostics, and institutional evidence are not optional. Sorting can be fatal because RD compares units just on either side of the cutoff. If students barely manipulate test scores, firms bunch below a regulatory threshold, candidates strategically select races, or households time income around eligibility, the local comparison may no longer approximate random assignment. Formal density tests are informative, but a credible paper also explains the administrative process that makes precise manipulation hard or likely.

### What RD Identifies And How To Interpret It

RD identifies a local causal effect at the cutoff under continuity of potential outcomes and no precise manipulation. In fuzzy RD, it identifies the effect for threshold-induced compliers. It does not identify:

- effects for units far from the threshold;
- the ATE for the full population without a separate extrapolation argument;
- dynamic or equilibrium effects beyond the observed treatment package;
- mechanisms when crossing the threshold changes several channels at once;
- effects under a different threshold or a different policy schedule;
- valid estimates when sorting or manipulation changes the composition around the cutoff.

The research interpretation should connect the local effect to the economic question. A narrow RD can still be important when the cutoff itself is a policy margin. The effect of barely winning office matters because many elections are close. The effect of barely qualifying for a benefit matters because eligibility rules create marginal recipients. The effect at a regulation threshold matters because firms near the threshold are the firms facing the rule. Locality is not a flaw by itself. It becomes a flaw when the paper quietly treats the local effect as a global one.

### Regression Kink Designs

Regression kink designs use a kink in a policy schedule or incentive rule rather than a discontinuous treatment jump. Suppose {math}`B_i` is a benefit, tax price, treatment intensity, or incentive that is a function of the running variable {math}`X_i`, and the slope of that function changes at {math}`c`. The RKD estimand compares slope changes in outcomes to slope changes in treatment or incentives:

```{math}
:label: eq:em5-rkd-estimand
\tau_{RKD}
=
\frac{
\lim_{x\downarrow c}\frac{d}{dx}\mathbb{E}[Y_i\mid X_i=x]
-
\lim_{x\uparrow c}\frac{d}{dx}\mathbb{E}[Y_i\mid X_i=x]
}{
\lim_{x\downarrow c}\frac{d}{dx}\mathbb{E}[B_i\mid X_i=x]
-
\lim_{x\uparrow c}\frac{d}{dx}\mathbb{E}[B_i\mid X_i=x]
}.
```

RKD is best used when the policy changes marginal incentives but not treatment levels. Examples include benefit formulas, tax schedules, student-aid formulas, or unemployment-insurance schedules where the replacement rate changes slope at an earnings or benefit threshold. Card, Lee, Pei, and Weber show why generalized RKD requires careful inference and stronger smoothness discipline than many simple presentations suggest [@cardLeePeiWeber2015].

RKD identifies a local marginal response to a change in the slope of incentives, not a level treatment effect. It does not identify the effect of crossing an eligibility cutoff unless the rule creates a level discontinuity. It is often more fragile than RD because derivatives are noisy, local curvature matters more, and small manipulation or bunching around the kink can contaminate the slope comparison.

Implementation should show the policy schedule, verify the kink is sharp and correctly measured, estimate slopes locally on both sides, report bandwidth sensitivity, and diagnose bunching or sorting around the kink. If the running variable is the same object agents optimize over, such as taxable income, the researcher must confront behavioral response in the density, not only the outcome slope.

### Bunching At Kinks And Notches

Bunching designs study the density of choices around nonlinear incentives. A kink changes the marginal price at a point, such as a tax rate that rises above an earnings threshold. A notch changes the level of liability or payoff discontinuously, creating a dominated region where some agents have a strong incentive to avoid crossing the threshold.

The empirical object is excess mass relative to a counterfactual smooth density. Let {math}`z` be the choice variable, {math}`z^*` the kink or notch, {math}`f(z)` the observed density, and {math}`\widehat f_0(z)` the counterfactual density that would have prevailed without the nonlinear incentive. A generic excess-mass statistic over a bunching window {math}`\mathcal{B}` is:

```{math}
:label: eq:em5-bunching-excess-mass
\widehat B
=
\sum_{z\in \mathcal{B}}
\left[f(z)-\widehat f_0(z)\right],
\qquad
\widehat b
=
\frac{\widehat B}{\widehat f_0(z^*)}.
```

The normalized bunching estimate {math}`\widehat b` can be interpreted as the width of the missing interval of agents who moved to the threshold, measured in units of the counterfactual density at the threshold. To map bunching into an elasticity, the researcher needs an optimization model. In a simple tax kink model, if the net-of-tax rate changes from {math}`1-t_0` to {math}`1-t_1`, a stylized elasticity mapping is:

```{math}
:label: eq:em5-bunching-elasticity
\widehat e
\approx
\frac{\widehat b/z^*}
{\log(1-t_0)-\log(1-t_1)}.
```

Equation {eq}`eq:em5-bunching-elasticity` is not a universal formula. It is a reminder that bunching is a design plus a model. The same excess mass can imply different elasticities depending on preferences, income effects, optimization frictions, frictions in adjustment, salience, enforcement, and whether the threshold is a kink or a notch.

Bunching is convincing when the schedule is sharp and salient, the choice variable is measured precisely, the counterfactual density can be defended, and the model linking choices to incentives is plausible. Saez's taxable-income application is the canonical starting point because the tax schedule creates visible kink incentives [@saez2010]. Kleven's review is useful because it separates the graphical excess-mass object from the structural and sufficient-statistics assumptions needed for interpretation [@kleven2016].

Bunching is fragile when the counterfactual density is arbitrary, the running variable is heavily rounded or mismeasured, multiple policies overlap near the threshold, adjustment frictions are large and unmodeled, or the threshold changes reporting rather than real behavior. A good bunching paper reports bin width, excluded bunching window, polynomial order for the counterfactual density, sensitivity to those choices, institutional details on salience and enforcement, and a separate discussion of real response versus reporting response.

### RD In Time

RD in time uses calendar time as the running variable. The cutoff is a date: a policy begins, a rule changes, a ban takes effect, a platform changes its algorithm, or an enforcement regime starts. The estimand is a local outcome jump around the date. The design can be useful when the treatment date is sharp, the comparison window can be very local, and no other shock changes discontinuously at the same date.

Time RD is different from event studies and interrupted time series. An event study or DID design usually asks whether treated and comparison units have credible untreated paths over a broader window. RD in time asks whether the outcome process would have been continuous through the cutoff date absent treatment. Interrupted time-series designs often model pre- and post-trends; RD in time should avoid leaning on long trends unless the design explicitly justifies them. Hausman and Rapson emphasize that date-based RD can be highly sensitive to seasonality, serial correlation, bandwidth choice, and concurrent shocks [@hausmanRapson2018].

The main threats are:

- **seasonality:** outcomes may jump around holidays, school calendars, weather, fiscal years, or hiring cycles;
- **serial correlation:** adjacent time observations are not independent, so naive standard errors overstate precision;
- **anticipation:** agents may change behavior before the formal cutoff if the date is announced;
- **concurrent shocks:** another policy, news event, reporting change, or macro shock may occur at the same date;
- **manipulated timing:** firms, agencies, or households may shift transactions across the cutoff.

Implementation should report the time unit, bandwidth in calendar units, seasonality controls or comparison dates, whether the policy was anticipated, whether observations are aggregated or individual-level, the serial-correlation correction, and any placebo cutoff exercises. Donut RD can be useful when immediate dates around the cutoff are contaminated by transition behavior, but it changes the estimand by removing the closest observations. Students should always ask whether DID, event-study, or synthetic-control logic would provide a better counterfactual path than a pure local date comparison.

### Spatial RD

Spatial RD uses geography as the running variable or assignment surface. In a one-dimensional border design, the running variable is signed distance to a boundary. Units just on one side are treated; units just on the other side are controls. The estimand is a local discontinuity at the border:

```{math}
:label: eq:em5-spatial-rd
\tau_{border}
=
\lim_{d\downarrow 0}\mathbb{E}[Y_i\mid \text{signed distance}_i=d]
-
\lim_{d\uparrow 0}\mathbb{E}[Y_i\mid \text{signed distance}_i=d].
```

Spatial RD is attractive because nearby places can share geography, markets, climate, and history. Dell's study of the Peruvian mining mita is a canonical application because the historical boundary defines a local institutional contrast and the paper puts heavy weight on geographic comparison [@dell2010].

Spatial RD becomes harder when boundaries are multidimensional. A border is not one point; it is a curve or set of segments. Distance to the border may be insufficient if outcomes vary along the boundary. Practical designs often use boundary-segment fixed effects, latitude-longitude controls, local border windows, or matched pairs across short border segments. Those choices should be reported because they define the comparison.

What makes geographic continuity credible?

- the boundary is institutionally meaningful for treatment but not drawn to sort the outcome of interest;
- nearby units on opposite sides share pre-treatment geography and market access;
- there is limited migration, firm sorting, or household sorting in response to the border;
- other policies or administrative capacity do not change exactly at the same boundary;
- outcomes and covariates are measured comparably on both sides;
- spillovers across the border are either limited or explicitly part of the interpretation.

Spatial RD does not identify a national or regional average treatment effect unless the border local average is portable. It may also miss equilibrium effects if treatment shifts wages, rents, migration, trade, or commuting across the boundary. Inference should account for spatial dependence; nearby observations are not independent simply because they are separate points on a map.

### Choosing Among RD, RKD, Bunching, Time RD, And Spatial RD

The designs in this lecture belong to one family, but they answer different questions.

```{include} assets/tables/05-time-and-spatial-rd.md
```

Use sharp RD when the rule creates a treatment-level jump and the local effect at the cutoff is the target. Use fuzzy RD when the rule creates an eligibility or assignment jump but compliance is incomplete. Use RKD when the policy changes marginal incentives, not treatment levels. Use bunching when the density of optimized choices around a nonlinear schedule is the object. Use time RD only when a local date comparison is more credible than path-based counterfactuals. Use spatial RD when the border is the assignment rule and geographic continuity is defensible.

The warning is the same across all variants: the threshold has to do real identification work. A threshold that is easy to manipulate, a date that coincides with many shocks, a border that reflects deep historical differences, or a bunching estimate with an arbitrary counterfactual density is not a strong design just because it has a cutoff.

### Theory-To-Applied Research Logic

A strong applied paper in this family usually has seven parts.

1. **Institutional rule.** What exact threshold, kink, notch, date, or border creates the variation?
2. **Estimand.** Is the target a level discontinuity, a first-stage ratio, a slope discontinuity, or excess mass under a behavioral model?
3. **Local comparability.** Why should potential outcomes be continuous at the cutoff absent treatment?
4. **Manipulation diagnosis.** Can units sort, time, report, or choose the running variable precisely?
5. **Implementation.** What bandwidth, kernel, polynomial order, covariates, clustering level, and inference method are used?
6. **Robustness and sensitivity.** Do estimates survive reasonable bandwidth changes, alternative kernels, covariate adjustment, donut choices, placebo cutoffs, or boundary definitions?
7. **Interpretation.** What local population and treatment margin does the estimate describe, and what claims remain outside the design?

This is why Lecture 5 is not "the cutoff lecture." It is the lecture about using thresholds as disciplined local counterfactuals.

## Research Lab

The Lecture 5 Research Lab follows the course standard: **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** Students reproduce the logic of Lee's close-election RD using a deterministic synthetic teaching dataset inspired by close-election designs [@lee2008]. The task is to estimate a sharp RD effect of barely winning office on a later political outcome using local linear triangular-weighted estimation. Students inspect the RD plot, bandwidth sensitivity, covariate continuity, and the density of the running variable near zero.

**Diagnose.** Students diagnose the same design using modern RD practice. The diagnosis anchor is Calonico, Cattaneo, and Titiunik for robust bias correction, Armstrong and Kolesar for honest inference, and Gelman and Imbens for polynomial discipline [@calonicoCattaneoTitiunik2014; @armstrongKolesar2020; @gelmanImbens2019]. The lab implements lightweight teaching analogues: conventional local-linear estimates, a local-quadratic bias diagnostic, a robust-bias-correction-style estimate, and a smoothness-bound honest interval. Students must explain what each object is trying to protect against.

**Transfer.** Students transfer the design logic to bunching around a tax kink, using Saez and Kleven as the conceptual anchors [@saez2010; @kleven2016]. The transfer task estimates excess mass relative to a counterfactual density, maps it into a stylized elasticity, and explains why that mapping depends on the optimization model. An instructor can swap in a spatial RD transfer memo using Dell if the course wants a geography-focused lab [@dell2010].

The lab is synthetic by design. It does not reproduce official published estimates. It reproduces the design decisions students need to understand before reading or writing a serious RD-style paper.

## Methods Box

:::{admonition} Methods Box: Practical Design Rules For RD, RKD, Bunching, And Local Designs
:class: note

Use this checklist before claiming a local threshold design is persuasive.

```{include} assets/tables/05-modern-rd-toolkit.md
```

For bandwidth, weighting, covariates, and practical implementation:

```{include} assets/tables/05-bandwidth-weighting-covariates.md
```

The practical bottom line is simple: if a result is credible only under a narrow hidden bandwidth, a high-order polynomial, a post-treatment covariate set, or an implausible no-sorting story, the design is not yet doing the work.
:::

## Causal Inference Block Summary

This lecture closes Block 1. The methods in the block differ less by prestige than by how they construct the missing counterfactual.

```{include} assets/tables/05-causal-block-summary.md
```

Selection-on-observables uses rich covariates, overlap, and conditional independence to construct treated-control comparisons. It is best when observables are substantively rich, treatment timing is not the main source of variation, and no sharper design exists. Its strength is transparency and reach. Its weakness is unobserved selection. SUTVA and interference concerns often enter through hidden spillovers or equilibrium responses that are not captured by covariates.

Experiments use random assignment to construct the counterfactual. They are best when the treatment can be assigned, compliance can be measured, and spillovers can be designed around or estimated. Their strength is internal validity. Their weaknesses are implementation failure, attrition, noncompliance, spillovers, and external validity. Randomization does not solve interference; it makes exposure mapping and design choices visible.

DID, event studies, and synthetic control use untreated paths or donor pools to approximate the treated units' missing untreated path. They are best when timing varies across units or places and untreated comparison paths are credible. Their strength is policy relevance in panel settings. Their weaknesses are bad comparison groups, anticipation, treatment-effect heterogeneity, serial correlation, and spillovers across units or markets.

IV uses instrument-induced treatment variation. It is best when treatment is endogenous but a credible source of quasi-random variation shifts treatment on a meaningful margin. Its strength is the ability to isolate otherwise endogenous treatment movement. Its weakness is exclusion, weak first stages, multiple-margin interpretation, and local complier effects. Interference can appear when the instrument changes markets, peers, prices, or untreated units directly.

RD, RKD, and bunching use local discontinuities, kinks, or density responses around thresholds. They are best when rules or incentives create a sharp local comparison and the local margin matters economically. Their strength is high local transparency. Their weaknesses are local external validity, manipulation, sensitivity to implementation choices, and stronger behavioral modeling for bunching. Interference matters when treatment spills across the threshold, agents sort around it, or local markets equilibrate around the rule.

Applied economists often use a rough credibility hierarchy: well-executed experiments and clean threshold designs are treated as especially persuasive; strong DID/event-study/synthetic-control designs can be highly credible when untreated paths are convincing; IV ranges from powerful to fragile depending on the instrument; selection-on-observables usually needs the heaviest sensitivity work. This hierarchy is a heuristic, not a mechanical publication rule. A clean design that answers the wrong question is less useful than a more demanding design that matches the economic mechanism and documents its assumptions.

## Reading Ladder And References

**Foundations.** Start with Hahn, Todd, and van der Klaauw for identification, then Imbens and Lemieux and Lee and Lemieux for applied RD practice [@hahnToddVanderklaauw2001; @imbensLemieux2008; @leeLemieux2010].

**Canonical applied anchor.** Read Lee's close-election design for a transparent sharp RD where the running variable, cutoff, and local effect are easy to see [@lee2008].

**Modern implementation.** Read Calonico, Cattaneo, and Titiunik on robust bias correction, Calonico, Cattaneo, Farrell, and Titiunik on covariates, Armstrong and Kolesar on honest inference, and Gelman and Imbens on polynomial pitfalls [@calonicoCattaneoTitiunik2014; @calonicoCattaneoFarrellTitiunik2019; @armstrongKolesar2020; @gelmanImbens2019].

**Extensions.** Read Hausman and Rapson for RD in time, Dell for spatial RD, Card, Lee, Pei, and Weber for RKD, Saez for bunching at tax kinks, and Kleven for the broader bunching toolkit [@hausmanRapson2018; @dell2010; @cardLeePeiWeber2015; @saez2010; @kleven2016].

**Use the readings to answer five design questions:**

- What exact threshold, kink, notch, date, or border identifies the estimate?
- What is smooth at the cutoff, and why?
- Who or what can manipulate the running variable?
- Which bandwidth, weights, inference method, and covariates define the effective comparison?
- What local claim is supported, and what broader claim would require extra evidence?

## Exercises And Discussion Prompts

1. Starting from {eq}`eq:em5-sharp-rd-estimand`, explain why sharp RD identifies a local effect rather than a global treatment effect.
2. Use {eq}`eq:em5-fuzzy-rd-estimand` to explain why fuzzy RD is a local Wald estimator. What is the complier group?
3. In a close-election design, what evidence would make the continuity assumption more credible? What evidence would weaken it?
4. Compare a triangular kernel and a uniform kernel inside the same bandwidth. What changes in the effective comparison?
5. Why are high-order global polynomials discouraged in RD even when they improve in-sample fit?
6. When would you prefer honest intervals to reporting only robust bias-corrected intervals?
7. Design a time RD around a policy implementation date. Name the seasonality, serial-correlation, anticipation, and concurrent-shock threats.
8. Design a spatial RD around an administrative boundary. What would make geographic continuity believable or unbelievable?
9. Explain why bunching at a tax kink needs an optimization model while sharp RD does not.
10. Compare selection-on-observables, experiments, DID/event studies/synthetic control, IV, and RD for a labor-market policy threshold. Which method would you trust most, and why?

## Reproducibility And Code Lab Note

The canonical lab path is:

`labs/05-regression-discontinuity-rkd-bunching-and-local-designs/`

The lab uses Python and deterministic synthetic teaching data. The smoke path creates:

- a close-election RD dataset under `original/reduced/close_election_synthetic.csv`;
- a tax-kink bunching dataset under `transfer/data/tax_kink_bunching_synthetic.csv`;
- reproduced RD estimates, bandwidth diagnostics, covariate continuity checks, density checks, and an RD plot under `output/reproduced/`;
- transfer bunching estimates, counterfactual-density diagnostics, elasticity calculations, and a bunching plot under `output/transfer/`.

The lab intentionally implements lightweight teaching analogues of modern RD diagnostics rather than claiming to replace production packages. A publishable project should use established RD tooling where appropriate, document software versions, and report the exact bandwidth, kernel, polynomial order, covariates, clustering level, and inference method.

## Slide Companion Note

The canonical slide path is:

`slides/week5/05-regression-discontinuity-rkd-bunching-and-local-designs.tex`

The deck should define the local-design question, show sharp and fuzzy RD, explain local-polynomial estimation with bandwidths and weights, separate `rdrobust` from `rdhonest`, cover covariates and polynomial pitfalls, compare time RD with event studies, introduce spatial RD, summarize RKD and bunching, close Block 1, and preview the Research Lab.

## Bridge Forward

Block 1 has covered the core design-based causal-inference families used most often in applied economics. Block 2 turns to structural estimation. The question will no longer be only "what causal effect is identified by this source of variation?" It will also be "what model is needed to recover the primitives, behavior, welfare objects, and counterfactuals that the reduced-form design cannot directly see?"
