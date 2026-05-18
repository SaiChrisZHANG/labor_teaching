---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Discrimination, Measurement, and Sorting

## Learning Objectives

By the end of Week 9, students should be able to:

1. explain why a raw group gap is not yet a measure of discrimination;
2. distinguish taste-based discrimination, statistical discrimination, identity or norm-based mechanisms, and sorting or segmentation mechanisms;
3. explain how discrimination can operate at hiring, wage, promotion, task-assignment, and retention margins;
4. write down and interpret raw-gap, conditional-gap, decomposition, taste-based, statistical-discrimination, audit, and sorting objects;
5. explain why omitted variables, post-treatment controls, and endogenous selection complicate empirical measurement;
6. distinguish what correspondence or audit studies identify from what regression decompositions identify;
7. connect discrimination to Week 8 inequality without collapsing discrimination into general dispersion;
8. see why Week 10 mobility is partly about how workers move across labor-market segments that may already be shaped by discrimination.

## Opening Orientation

The economic question for the week is narrower and harder than Week 8's question. Week 8 mapped the architecture of inequality across wages, hours, firms, and amenities. Week 9 asks which part of observed group differences should be interpreted as discrimination, through which mechanism, at which margin, and under which identification design [@altonjiBlank1999; @heckman1998; @neumark2018].

:::{admonition} Core materials
:class: tip
- a raw gap is an outcome object, not yet a discrimination object
- discrimination mechanisms can generate similar reduced-form patterns
- controls can help or hurt depending on whether they are pre-treatment or post-treatment
- sorting and segmentation belong inside the discrimination architecture, not outside it
:::

## Bridge

Week 8 taught three disciplines that matter immediately here. First, inequality is multi-object: wages, annual earnings, employment, task assignment, and access to high-premium firms can all diverge. Second, descriptive decompositions are useful without being fully causal. Third, sorting across firms and segments is not background noise; it is part of labor-market architecture. Week 9 keeps those disciplines and asks a sharper question: when should unequal labor-market outcomes across groups be read as discrimination rather than as broader inequality?

That sharper question is difficult because observed gaps mix many channels. Group differences in labor outcomes can reflect pre-market skill accumulation, endogenous schooling responses, occupational steering, employer tastes, employer beliefs under imperfect information, unequal access to search networks, and differential assignment across firms, occupations, tasks, and places [@becker1957; @phelps1972; @arrow1973]. The field's core challenge is therefore conceptual and empirical at once. Students must separate gaps from treatment, beliefs from preferences, and within-firm wedges from between-firm allocation.


:::{admonition} Optional Extension Block
:class: note
- employer-level report cards and ranking uncertainty in the spirit of [@klineRoseWalters2024]
- task-based discrimination and equilibrium occupational assignment in the spirit of [@hurstRubinsteinShimizu2024]
- algorithmic screening, monopsony, and the interaction between discrimination and firm power
:::

## Field Core

### From outcome gaps to discrimination objects

The cleanest opening distinction is between an observed gap and discriminatory treatment. Let {math}`G_i \in \{0,1\}` index a signaled group identity and let {math}`Y_i` denote a labor-market outcome such as callback probability, hourly wage, promotion, or assignment to a high-contact task. Then the raw gap is

```{math}
:label: eq-week9-raw-gap
\Delta = \mathbb{E}[Y \mid G=1] - \mathbb{E}[Y \mid G=0].
```

Equation {eq}`eq-week9-raw-gap` is often the first object the public sees, but it is not yet a discrimination estimate. It is an average difference in outcomes across groups. A conditional analogue,

```{math}
:label: eq-week9-conditional-gap
\Delta(x) = \mathbb{E}[Y \mid G=1, X=x] - \mathbb{E}[Y \mid G=0, X=x],
```

asks a different question by holding fixed some observed characteristics {math}`X`. The difficulty is that the meaning of Equation {eq}`eq-week9-conditional-gap` depends entirely on what enters {math}`X`. Conditioning on pre-market characteristics can be useful. Conditioning on schooling, occupation, firm assignment, or current task can be dangerous if those variables are themselves downstream of discrimination [@altonjiBlank1999; @heckman1998].

```{figure} assets/figures/09-gap-vs-discrimination-schematic.png
:name: fig-week9-gap-vs-disc
Raw gaps, adjusted gaps, and causal discriminatory treatment are different objects. Conditioning can remove relevant composition differences, but it can also partial out mechanisms that are themselves shaped by discrimination.
```

Figure {numref}`fig-week9-gap-vs-disc` should be read as a warning against naive residual reasoning. A raw gap can be too broad to interpret, but a conditional gap can be too narrow if the controls erase the mechanism of interest. Week 9 therefore studies discrimination as an architecture of objects rather than as one residual number.

### Competing economic definitions of discrimination

The classic economic definitions remain foundational because they classify mechanisms that often look similar in reduced form.

Taste-based discrimination enters the decision maker's utility or effective cost function. Becker's formulation treats group identity as a wedge that makes some workers less attractive to prejudiced employers, coworkers, or customers even when productivity is the same [@becker1957]. Statistical discrimination instead operates through beliefs under imperfect information: employers use group-conditioned expectations when signals about productivity are noisy or incomplete [@phelps1972; @arrow1973]. Identity, norm, or stigma mechanisms add a broader social layer in which workplace culture, evaluative standards, and interaction effects alter outcomes even without a literal taste parameter or a simple Bayesian signal problem [@altonjiBlank1999].

```{figure} assets/figures/09-discrimination-mechanisms.png
:name: fig-week9-mechanisms
The same observed gap can arise through taste-based wedges, belief-based screening, or allocation-based sorting. The empirical task is to separate mechanisms rather than to assume one canonical channel.
```

Figure {numref}`fig-week9-mechanisms` matters because many empirical papers identify treatment differences without pinning down whether the operative channel is taste, beliefs, norms, or equilibrium allocation. Labor economists need the mechanism map before they can decide which estimand is informative.

```{include} assets/tables/09-mechanism-map.md
```

Table {numref}`tbl:disc-mechanism-map` is the summary map for this section. It keeps the lecture from collapsing into either a history-of-thought survey or an undifferentiated list of discriminatory outcomes.

### Measurement architecture: why gaps are not enough

The source pack insists that Week 9 train students to resist turning any conditional residual into "discrimination." The workhorse descriptive device is still Oaxaca-Blinder style accounting:

```{math}
:label: eq-week9-oaxaca
\mathbb{E}[Y \mid G=1] - \mathbb{E}[Y \mid G=0]
= \big(\mathbb{E}[X \mid G=1]-\mathbb{E}[X \mid G=0]\big)\beta_0
+ \mathbb{E}[X \mid G=1](\beta_1-\beta_0).
```

Equation {eq}`eq-week9-oaxaca` is useful because it separates composition differences from coefficient differences. But the second term is not automatically a causal measure of discrimination [@altonjiBlank1999]. Coefficient differences can reflect omitted productivity dimensions, equilibrium responses, measurement error, or selection into the observed sample. The decomposition is descriptive discipline, not a stand-alone identification design.

This is where bad controls enter. Suppose current occupation, firm, or schooling is partly shaped by discriminatory screening earlier in the life cycle. Conditioning on those variables may absorb exactly the mechanism one wants to understand. The same problem arises if the wage sample contains only workers who were hired. Employment selection can turn wage-gap inference into a selected-sample problem: the observed wage gap among workers need not equal the gap that would arise in the full applicant pool [@heckman1998].

The central habit for students is therefore procedural. Before interpreting a gap, ask:

1. What is the outcome?
2. What is the conditioning set?
3. Which controls are plausibly pre-treatment?
4. What selection process determines who enters the sample?
5. Could discrimination at an earlier margin already be hidden inside the observables?

### Mechanism block I: taste-based discrimination

The cleanest compact taste-based object is an employer profit function with a group-specific wedge:

```{math}
:label: eq-week9-taste
\pi_j = p \cdot q_{ij} - w_i - d_j \mathbf{1}\{G_i=1\}.
```

In Equation {eq}`eq-week9-taste`, {math}`d_j > 0` acts like a group-specific cost wedge for employer {math}`j`. Even if worker productivity {math}`q_{ij}` is identical, prejudiced employers behave as if some workers are more expensive. That can lower hiring, reduce wages, distort task assignment, or push workers toward less prejudiced firms or occupations [@becker1957].

The important field-course correction is that competition need not wash this away mechanically. Search frictions, customer discrimination, coworker tastes, local concentration, and information frictions can let taste-based wedges survive in equilibrium. Taste-based models therefore predict both treatment differences and sorting patterns. If prejudiced employers avoid certain workers, those workers may be concentrated in particular firms, market segments, or tasks even when within-firm wage gaps look modest.

### Mechanism block II: statistical discrimination and belief-based mechanisms

The compact statistical-discrimination object is a group-conditioned decision rule:

```{math}
:label: eq-week9-statdisc
\text{Hire if } \mathbb{E}[a_i \mid s_i, G_i] \geq c_j.
```

Equation {eq}`eq-week9-statdisc` says that employers hire when expected productivity {math}`a_i`, inferred from signals {math}`s_i` and group identity {math}`G_i`, exceeds a threshold {math}`c_j`. The mechanism operates through beliefs rather than tastes. If signals are noisy and employers believe one group has a lower mean or a wider distribution, they may screen differently even when they do not literally dislike the group [@phelps1972; @arrow1973].

This mechanism connects directly to Week 4 and Week 5. If workers anticipate that returns to a credential or signal differ by group, then schooling, task acquisition, test-taking, and occupational investment can respond endogenously. Lang and Manove show why education can function as a compensating signal in a discriminatory environment rather than as a clean pre-treatment control [@langManove2011]. That is precisely why Week 9 cannot treat all observed human-capital variables as innocent controls.

Belief-based models also generate feedback. If biased beliefs steer some groups away from high-return tasks or firms, the resulting observed productivity distribution may later appear to validate the original screening rule. This is one route through which discrimination becomes an equilibrium allocation problem rather than just a one-shot hiring decision.

### Mechanism block III: discrimination, segmentation, and sorting

Week 9 is the week where discrimination and sorting must be taught together. A compact sorting object is

```{math}
:label: eq-week9-sorting
s_{gf} = \Pr(F_i = f \mid G_i = g),
```

or, equivalently, the expected premium of the firm to which a worker from group {math}`g` is assigned, {math}`\mathbb{E}[\psi_{F_i} \mid G_i=g]`. Equation {eq}`eq-week9-sorting` makes the point that discrimination can appear through assignment across firms, occupations, tasks, networks, or local labor markets. It is not only a within-firm wage wedge.

```{figure} assets/figures/09-sorting-segmentation-heatmap.png
:name: fig-week9-sorting
Sorting and segmentation can generate persistent group differences through differential assignment to low-premium and high-premium firms, occupations, or tasks. Observed treatment gaps and allocation gaps often coexist.
```

Figure {numref}`fig-week9-sorting` is the bridge back to Week 8's firm and sorting architecture and forward to Week 10 mobility. A worker may face little within-firm wage discrimination conditional on task, yet still be disproportionately sorted into low-premium firms or low-learning tasks. Conversely, large within-firm treatment gaps may coexist with modest between-firm sorting. The empirical lesson is that discriminatory treatment and discriminatory allocation are complements, not substitutes.

```{include} assets/tables/09-sorting-map.md
```

Table {numref}`tbl:disc-sorting-map` keeps the segmentation block concrete. Occupation, firm, task, network, and location margins each generate different empirical objects and different bridges to later weeks.

### Empirical identification: what designs identify

The cleanest direct-treatment object in the weekly package comes from correspondence or audit studies:

```{math}
:label: eq-week9-audit
\tau^{cb} = \mathbb{E}[C_i(1) - C_i(0)],
```

where treatment changes signaled identity while holding qualifications fixed, and {math}`C_i` is a callback or contact outcome. Equation {eq}`eq-week9-audit` is powerful because it makes discriminatory treatment experimentally legible at a specific hiring margin [@bertrandMullainathan2004; @neumark2018].

```{figure} assets/figures/09-audit-identification-schematic.png
:name: fig-week9-audit
Correspondence and audit studies isolate treatment at a specific margin by changing signaled identity while holding credentials fixed. The design is clean at the callback stage but does not by itself recover every equilibrium consequence of discrimination.
```

Figure {numref}`fig-week9-audit` highlights both the strength and the limit of the design. A correspondence experiment identifies a treatment effect in the opportunity set presented to employers. It is especially good for hiring-stage discrimination because it holds application content fixed. But it does not, by itself, reveal the full wage path, task assignment, or equilibrium sorting consequences generated after hiring.

```{include} assets/tables/09-identification-map.md
```

Table {numref}`tbl:disc-identification-map` should organize the empirical core of the lecture. Oaxaca-Blinder decompositions answer descriptive accounting questions. Correspondence studies identify treatment at a narrow margin. Paired audits control common opportunity sets more tightly. Quasi-experimental information or policy shocks speak to broader institutional channels. Structural and equilibrium models connect treatment, sorting, and welfare, but at the cost of stronger assumptions [@heckman1998; @neumark2018].

### How to think about causality in discrimination research

Week 9's main causal-inference lesson is that the appropriate estimand depends on the mechanism and margin. A callback treatment effect from Equation {eq}`eq-week9-audit` identifies discriminatory treatment in a specific stage of employer screening. It is not the same as the wage gap among employed workers, because the wage sample is already selected by earlier hiring decisions. A coefficient-difference term in Equation {eq}`eq-week9-oaxaca` may be informative, but it does not recover a clean treatment effect without much stronger assumptions. A sorting object such as Equation {eq}`eq-week9-sorting` may capture an equilibrium barrier, but it mixes preferences, constraints, search, networks, and employer behavior unless the design separates them.

Heckman's critique remains essential here. If discrimination affects who applies, who is interviewed, who is hired, and who remains employed, then inference at any later margin inherits the earlier selection problem [@heckman1998]. That is why modern discrimination research often uses a portfolio of designs rather than a single estimator. Experimental designs reveal direct treatment at one stage; decomposition work clarifies how much is left unexplained conditional on chosen controls; structural and equilibrium work translate treatment and sorting into broader labor-market wedges [@neumark2018; @klineRoseWalters2024; @hurstRubinsteinShimizu2024].

The right Week 9 conclusion is therefore disciplined rather than cynical. No single design is enough for every discrimination question, but different designs are informative precisely because they target different objects.

## Research Lab

The bounded Week 9 lab follows the standard `Reproduce -> Diagnose -> Transfer` structure with a teaching-safe path that stays fully local. The reproduction step uses a synthetic correspondence-study file in the spirit of [@bertrandMullainathan2004] to estimate an average callback gap, quality-specific callback gaps, and firm-segment heterogeneity. The diagnostic step asks students to explain why that treatment effect is narrower than a general labor-market discrimination object. The transfer step then moves to synthetic employer-level report cards in the spirit of [@klineRoseWalters2024], where students estimate firm-specific callback gaps, think about noise in rankings, and see how measurement uncertainty complicates employer comparisons.

An optional extension note points to [@hurstRubinsteinShimizu2024], where discrimination operates partly through task assignment and equilibrium occupational structure. That extension is deliberately conceptual in the bounded path. Students do not need restricted employer microdata or a real field experiment to learn the core logic of discrimination measurement and sorting.

Open research questions should remain visible:

1. How much of an observed wage gap reflects treatment at the hiring stage versus sorting across firms and tasks?
2. When do information frictions and taste-based wedges produce observationally similar patterns?
3. How much uncertainty should researchers tolerate before ranking employers by discriminatory behavior?
4. How do discriminatory beliefs alter human-capital investment before workers ever enter the observed labor market?
5. Which mobility margins in Week 10 reflect voluntary reallocation and which reflect movement within a segmented opportunity set?

## Methods Box

### Methods Box 1: decomposition discipline and bad controls

Equations {eq}`eq-week9-raw-gap`, {eq}`eq-week9-conditional-gap`, and {eq}`eq-week9-oaxaca` are descriptive tools for organizing group differences. They are most useful when they clarify which part of a gap is tied to observables and when they force the researcher to defend the conditioning set. They become misleading when post-treatment controls are added mechanically or when the unexplained component is relabeled as causal discrimination without a design argument [@altonjiBlank1999; @heckman1998].

### Methods Box 2: experimental treatment effects, firm report cards, and sorting

Equation {eq}`eq-week9-audit` gives a sharp experimental object at the callback stage. Equation {eq}`eq-week9-sorting` extends the conversation from direct treatment to equilibrium allocation. Modern firm-level report-card work sits between these objects: it keeps the treatment logic of audits while asking how discrimination varies across firms and how precisely those differences can be estimated [@bertrandMullainathan2004; @klineRoseWalters2024].

## Reading Ladder And References

### Bridge

- Becker on taste-based discrimination [@becker1957]
- Phelps and Arrow on statistical discrimination and group-conditioned beliefs [@phelps1972; @arrow1973]

### Field Core

- Altonji and Blank for a broad labor-market synthesis of race and gender evidence [@altonjiBlank1999]
- Heckman on what audit studies and residual gaps do and do not identify [@heckman1998]
- Bertrand and Mullainathan for a transparent experimental treatment-gap design [@bertrandMullainathan2004]
- Lang and Manove for the interaction between education, signaling, and discrimination [@langManove2011]
- Neumark for a modern synthesis of experimental discrimination evidence [@neumark2018]

### Research Lab

- Kline, Rose, and Walters on employer discrimination report cards and ranking uncertainty [@klineRoseWalters2024]
- Hurst, Rubinstein, and Shimizu on task-based discrimination and equilibrium occupational assignment [@hurstRubinsteinShimizu2024]

## Exercises And Discussion Prompts

1. Why does Equation {eq}`eq-week9-raw-gap` not identify discrimination by itself?
2. Give one example of a control variable that may be pre-treatment and one that may be post-treatment in a wage-gap regression.
3. In Equation {eq}`eq-week9-oaxaca`, why is the coefficient-difference term not automatically a clean discrimination measure?
4. Use Equation {eq}`eq-week9-taste` to explain why taste-based discrimination can generate both pay gaps and firm segregation.
5. Use Equation {eq}`eq-week9-statdisc` to explain how noisy signals can create discriminatory treatment without employer prejudice in the Becker sense.
6. Why can education be a bad control in discrimination work if credentials are themselves chosen in anticipation of differential treatment?
7. What does a correspondence-study estimand like Equation {eq}`eq-week9-audit` identify especially well, and what does it leave unresolved?
8. How can Equation {eq}`eq-week9-sorting` help explain persistent group wage gaps even when within-firm wage gaps appear modest?
9. Which concepts from Week 8 inequality are necessary before a student can interpret Week 9 discrimination evidence carefully?
10. Why is Week 10 mobility partly about movement across an opportunity set that Week 9 shows may already be segmented?

## Reproducibility And Code Lab Note

The Week 9 lab uses a bounded local workflow rather than a literal field-experiment replication. Students first reproduce callback-gap summaries from a synthetic correspondence-study dataset in the spirit of [@bertrandMullainathan2004], then diagnose what that treatment effect does and does not identify, and finally transfer the logic to firm-level discrimination report cards in the spirit of [@klineRoseWalters2024]. The student-facing workflow is documented in [labs/09-discrimination-measurement-and-sorting/lab.md](labs/09-discrimination-measurement-and-sorting/lab.md).

## Slide Companion Note

The Week 9 deck should isolate the chapter's architecture rather than reproduce its prose. It should start from the Week 8 inequality bridge, define the difference between gaps and discrimination objects, contrast taste-based and statistical-discrimination mechanisms, warn about bad controls, show the logic of audit identification, keep sorting and segmentation inside the discrimination lecture, and end by bridging to Week 10 mobility. The canonical source is [slides/week9/09-discrimination-measurement-and-sorting.tex](slides/week9/09-discrimination-measurement-and-sorting.tex).

## Bridge Forward

Use this closing bridge to carry the module's labor object, mechanism, and evidence into the next course step or research-design exercise.
