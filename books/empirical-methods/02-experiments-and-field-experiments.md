# Lecture 2. Experiments And Field Experiments

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain randomized assignment as a research design that builds a counterfactual, not as a statistical ritual;
2. state what randomization guarantees and which parameter is identified under complete randomization, imperfect compliance, and randomized encouragement;
3. distinguish ATE, ITT, take-up, first-stage, Wald/LATE, spillover, and market-level interpretations;
4. diagnose the main threats to experimental interpretation: noncompliance, attrition, outcome measurement, spillovers, weak implementation, and scale;
5. compare individual randomization, cluster randomization, audit/correspondence experiments, firm-level interventions, platform experiments, and labor-market saturation designs;
6. use field-experiment papers to decide when experiments are the best design, when they are not enough, and how to turn an experimental idea into publishable applied research.

## Opening Orientation

Experiments are often introduced as a gold standard. That phrase is too blunt for applied economics. Randomization is powerful because it changes the assignment mechanism: before the treatment is delivered, treated and control units are comparable in expectation by design. But randomization does not by itself define the economic treatment, enforce take-up, prevent missing outcomes, eliminate spillovers, or tell us whether a small pilot will scale to an equilibrium policy.

This lecture begins from randomized assignment as a design choice. The researcher chooses the unit of assignment, the treatment content, the encouragement margin, the outcome window, the implementation protocol, and the scale of delivery. Those choices determine the estimand. A clean individual-level experiment with full compliance can identify an average treatment effect for the experimental sample. A randomized encouragement design identifies an intention-to-treat effect, and under additional assumptions a local effect for compliers. A cluster or saturation design may identify direct effects, peer effects, or market-level effects depending on how exposure is measured.

The paper spine is deliberately applied. Harrison and List organize the field-experiment taxonomy [@harrisonList2004]. Duflo and Saez show why encouragement and spillovers matter in a labor-relevant retirement-saving setting [@dufloSaez2003]. Bertrand and Mullainathan show the power and limits of audit/correspondence designs for hiring discrimination [@bertrandMullainathan2004]. Bloom et al. show what firm-level randomized intervention looks like when the treatment is managerial practice and implementation fidelity is central [@bloomEtAl2013]. Pallais shows how platform experiments can reveal labor-market information frictions [@pallais2014]. Crepon et al. show why labor-market experiments can raise displacement, spillover, and equilibrium questions quickly [@creponEtAl2013].

## Core Points

:::{admonition} Core points
:class: important

- Random assignment builds a counterfactual by design, but the estimand is defined by the assignment unit, treatment, compliance margin, outcome, and scale.
- Under complete randomization and full compliance, the treated-control difference identifies the experimental average treatment effect.
- With imperfect take-up, the clean experimental object is usually the intention-to-treat effect of assignment.
- Randomized encouragement identifies a complier effect through Wald/LATE logic only with relevance, exclusion, monotonicity, and stable interpretation of compliance.
- Spillovers, clustered assignment, saturation, attrition, and implementation failure are not footnotes; they can change the parameter being estimated.
- Field experiments are strongest when the treatment channel, institutional setting, and behavioral mechanism are part of the design rather than hidden behind the estimator.
:::

## Bridge

Lecture 1 used potential outcomes to make the missing counterfactual visible. Selection-on-observables tries to recover that counterfactual by conditioning on rich pre-treatment information. Experiments take a cleaner route: they make assignment independent of potential outcomes by design. That does not remove the need for design discipline. It makes the assumptions more transparent.

The rest of Block 1 will replace random assignment with time paths, instruments, thresholds, kinks, and bunching. Those designs differ in mechanics, but each must answer the same questions introduced here. What is the target parameter? What variation identifies it? What behavior does the treatment change? What outcomes are observed? Could untreated units be affected? Would the result survive a different scale of implementation?

## Field Core

### Random Assignment As A Design

Let {math}`Z_i \in \{0,1\}` denote randomized assignment. Let {math}`D_i \in \{0,1\}` denote realized treatment receipt. In the cleanest experiment, assignment is independent of potential outcomes and pre-treatment covariates:

```{math}
:label: eq:em2-random-assignment
Z_i \perp \{Y_i(1),Y_i(0),X_i\}.
```

Equation {eq}`eq:em2-random-assignment` is the core guarantee. It says the assignment mechanism is not selecting units based on potential outcomes. The guarantee is about assignment, not about everything that happens after assignment. If treatment receipt differs from assignment, if outcomes are missing, or if one person's assignment changes another person's outcome, the researcher needs more structure.

Under complete randomization, full compliance, and no interference, the difference in sample means is unbiased for the sample average treatment effect:

```{math}
:label: eq:em2-ate-complete-randomization
\widehat{\tau}_{ATE}
=
\frac{1}{N_1}\sum_{i:Z_i=1}Y_i
-
\frac{1}{N_0}\sum_{i:Z_i=0}Y_i,
\qquad
\mathbb{E}\left[\widehat{\tau}_{ATE}\mid \{Y_i(1),Y_i(0)\}_{i=1}^N\right]
=
\frac{1}{N}\sum_{i=1}^N\{Y_i(1)-Y_i(0)\}.
```

The design interpretation matters more than the estimator. A regression of {math}`Y_i` on {math}`Z_i` estimates the same mean contrast in a two-arm experiment. Adding pre-treatment covariates can improve precision and account for chance imbalance, but it is not the source of identification. Randomization is.

### What Randomization Guarantees And What It Does Not

Randomization guarantees balance in expectation. It does not guarantee exact balance in a finite sample, perfect implementation, complete outcome measurement, or external validity. This is why experimental papers still report baseline balance, attrition, compliance, implementation, and inference choices.

Three distinctions are essential:

- **Assignment versus receipt.** {math}`Z_i` is randomized; {math}`D_i` may be chosen, constrained, or mediated by institutions after assignment.
- **Direct effects versus exposure effects.** A unit's outcome may depend on own assignment and others' assignments.
- **Experimental population versus policy population.** The sample, setting, and scale of the experiment define the population for which the estimate is most immediate.

Experiments are strongest when the desired policy question matches the design object. If a government can offer a program but not force participation, the ITT may be the most policy-relevant object. If the scientific question is the effect of actually receiving treatment, the researcher must explain who takes it up and why.

### ITT, Take-Up, And Randomized Encouragement

In many applied settings, researchers randomize access, information, encouragement, price, reminders, invitations, or eligibility. The clean experimental estimand is then the intention-to-treat effect:

```{math}
:label: eq:em2-itt
ITT_Y
=
\mathbb{E}[Y_i\mid Z_i=1]
-
\mathbb{E}[Y_i\mid Z_i=0].
```

The first stage or take-up effect is:

```{math}
:label: eq:em2-first-stage
ITT_D
=
\mathbb{E}[D_i\mid Z_i=1]
-
\mathbb{E}[D_i\mid Z_i=0].
```

When {math}`Z_i` is a randomized encouragement, the Wald ratio is:

```{math}
:label: eq:em2-wald-late
\tau_{LATE}
=
\frac{ITT_Y}{ITT_D}
=
\frac{\mathbb{E}[Y_i\mid Z_i=1]-\mathbb{E}[Y_i\mid Z_i=0]}
{\mathbb{E}[D_i\mid Z_i=1]-\mathbb{E}[D_i\mid Z_i=0]}.
```

The ratio in {eq}`eq:em2-wald-late` is not a mechanical upgrade from ITT to "the treatment effect." It identifies a local average treatment effect for compliers under the same logic that will return in the instrumental-variables lecture: the encouragement must shift treatment receipt, affect outcomes only through treatment receipt, and not induce some units to move in the opposite direction [@imbensAngrist1994; @angristImbensRubin1996].

Duflo and Saez are the right anchor for this logic. The university randomly encouraged employees to attend a benefits fair, and the paper studies both direct response and peer/social interaction channels [@dufloSaez2003]. The empirical object is not simply "the effect of retirement saving information." It is the effect of an encouragement and the induced exposure environment in a real workplace.

### Individual Randomization, Cluster Randomization, And Saturation

The unit of randomization is a substantive choice. Individual randomization is attractive when treatment can be delivered separately and interference is limited. Cluster randomization is natural when treatment is delivered through groups, firms, classrooms, offices, caseworkers, villages, or labor-market cells. Saturation designs randomize not only whether a cluster receives treatment, but also the share of units exposed.

Cluster designs often fit applied economics better than individual designs because institutions deliver treatments collectively. The cost is that power can fall sharply when outcomes are correlated within clusters. The number of clusters often matters more than the number of people. A large sample of workers in a few firms can be less informative than a smaller sample spread across many firms if assignment happens at the firm level.

Saturation designs become valuable when spillovers are part of the research question. If job-search assistance helps treated workers find jobs partly by displacing untreated workers, an individual experiment may identify a private gain while missing market incidence. Crepon et al. use clustered variation to study displacement effects of labor-market policies [@creponEtAl2013]. Their lesson is not that experiments fail in markets. It is that market experiments need designs that can see market response.

### Spillovers And Exposure Mapping

The simple potential-outcomes setup assumes that unit {math}`i`'s potential outcome depends only on unit {math}`i`'s treatment. In labor, education, firms, networks, neighborhoods, and platforms, this assumption is often too strong. A transparent exposure mapping writes potential outcomes as:

```{math}
:label: eq:em2-exposure-mapping
Y_i(\mathbf{Z})
=
Y_i\left(Z_i, G_i(\mathbf{Z}_{-i})\right),
```

where {math}`G_i(\mathbf{Z}_{-i})` summarizes others' assignments around unit {math}`i`: the share of treated coworkers, treated classmates, treated firms in a market, treated peers in a network, or treated vacancies on a platform.

Exposure mappings make interference explicit. They also discipline interpretation. If the researcher estimates:

```{math}
:label: eq:em2-direct-spillover-regression
Y_i = \alpha + \beta Z_i + \gamma G_i + \varepsilon_i,
```

then {math}`\beta` is a direct-assignment contrast holding measured exposure fixed, while {math}`\gamma` is an exposure contrast holding own assignment fixed. Whether either parameter is causal depends on how {math}`Z_i` and {math}`G_i` were randomized and whether the exposure summary captures the relevant interference channel.

Spillovers can be threats or mechanisms. In a vaccine, peer-learning, referral, job-search, or workplace-information experiment, spillovers may be the point. The design should say whether the goal is to eliminate them, measure them, or include them in a policy-relevant total effect.

### Audit And Correspondence Experiments

Audit and correspondence experiments randomize signals in real decision environments. Bertrand and Mullainathan randomize racially distinctive names on resumes and measure employer callbacks [@bertrandMullainathan2004]. The design is powerful because it isolates the screening response to a signal while holding resume content fixed.

The estimand is narrow by design. It concerns employer response at the initial contact margin, not all hiring, bargaining, productivity, job search, or equilibrium sorting. That narrowness is a strength when the question is screening discrimination. It becomes a limitation when readers want to infer full labor-market consequences.

Good audit designs therefore report exactly what is randomized, what information set decision-makers see, what outcome is measured, and which stage of the labor-market process is being studied. They also require careful ethical and implementation discipline because real firms, vacancies, and applicants may be affected.

### Firm, Platform, And Organizational Field Experiments

Field experiments become especially valuable when the treatment is an organizational practice, information regime, or platform rule that is difficult to infer from administrative quasi-experiments. Bloom et al. randomize management consulting in Indian textile firms and show that implementation, managerial practice, and operational outcomes are all part of the design [@bloomEtAl2013]. The intervention is not a one-line treatment variable. It is a bundle delivered inside firms.

Pallais uses an online labor-market setting to study information and hiring frictions [@pallais2014]. Platform environments can give researchers fine control over information, reputation, and matching rules while still preserving economically meaningful behavior. The design advantage is control and measurement. The interpretation challenge is portability: platform workers, tasks, and decision-makers may not represent all labor markets.

These papers show what field experiments reveal that administrative quasi-experiments often cannot. They can manipulate information, incentives, or organizational practices directly. They can measure implementation. They can observe intermediate behavior that is usually hidden. But they may be local in setting, scale, and population. A publishable experimental paper should embrace that tradeoff rather than hide it.

### Theory-To-Applied Design Through Papers

The theory-to-applied bridge for this lecture is:

```{include} assets/tables/02-theory-to-applied-bridge.md
```

Harrison and List give the taxonomy: lab experiments, artefactual field experiments, framed field experiments, and natural field experiments differ in subjects, tasks, information, stakes, and environment [@harrisonList2004]. The taxonomy helps students ask whether the experimental setting is close enough to the economic behavior being studied.

Duflo and Saez turn randomized encouragement into a labor-relevant research design [@dufloSaez2003]. The paper teaches the difference between assignment, attendance, retirement-plan participation, and peer exposure. It is also a reminder that social interactions can be central to the design rather than a nuisance to be wished away.

Bertrand and Mullainathan show how signal randomization can isolate employer screening behavior [@bertrandMullainathan2004]. The paper is not merely evidence on discrimination. It is a template for asking what a signal means, who observes it, and what margin of behavior the outcome captures.

Bloom et al. demonstrate the value of firm-level experiments for studying management, productivity, and organizational change [@bloomEtAl2013]. The treatment is embedded in a real production process, so implementation fidelity and managerial response are part of identification and interpretation.

Pallais shows why digital labor markets are useful experimental environments for information frictions [@pallais2014]. The platform makes randomization and measurement feasible, while the economic question remains labor-market design: how do employers learn about worker quality?

Crepon et al. provide the equilibrium caution [@creponEtAl2013]. A program can raise treated workers' outcomes and still have displacement effects for untreated workers. The policy question may require a market-level estimand, not only an individual treatment contrast.

### Methods And Robustness For Experiments

Experimental robustness is not a ritual appendix. It is the evidence that the randomized design was actually implemented and interpreted correctly.

```{include} assets/tables/02-experimental-design-diagnostics.md
```

**Individual versus clustered randomization.** The paper should name the assignment unit and match inference to that unit. If firms are randomized, firm-level clustering is not optional. If markets are randomized, the number of markets constrains what can be learned.

**Compliance and take-up.** Report assignment, receipt, first stage, and the gap between ITT and treatment-on-the-treated interpretations. A weak first stage can make a Wald estimate noisy and substantively local.

**Attrition and outcome measurement.** Missing outcomes can reintroduce selection after randomization. Report attrition by assignment status, pre-treatment predictors of missingness, outcome definitions, and robustness to bounds or alternative measurement.

**Spillovers, interference, and saturation.** Decide whether spillovers are ruled out by design, measured through exposure, or incorporated into a total effect. Do not interpret an individual-level contrast as a market-wide policy effect when untreated units are affected.

**Power and minimum detectable effects.** Power is a design question, not only a grant-table calculation. The researcher needs to know whether the experiment can detect economically meaningful effects given sample size, cluster count, baseline outcome variance, take-up, and multiple outcomes.

**Ethics, implementation, and reproducibility.** Field experiments alter real environments. Strong papers document consent or ethics review where relevant, pre-analysis or design plans when possible, implementation logs, randomization code, outcome construction, and deviations from protocol.

## Research Lab

The Lecture 2 Research Lab follows **Reproduce -> Diagnose -> Transfer**.

**Primary anchor.** Duflo and Saez are the main anchor [@dufloSaez2003]. Students work with a deterministic synthetic teaching path modeled on a workplace retirement-seminar encouragement design. The lab does not reproduce published magnitudes. It reproduces the design logic: random assignment, take-up, ITT, first stage, Wald/LATE, and peer exposure.

**Challenge anchor.** The challenge anchor is Crepon et al. [@creponEtAl2013], with Pallais as a complementary platform example [@pallais2014]. Students ask how interpretation changes when treatment affects a market, a platform, or a cluster rather than only the treated individual.

**Reproduce.** Students estimate the ITT of seminar encouragement on attendance and retirement-plan participation, the first stage for attendance, and a Wald/LATE-style ratio for participation among compliers. They compare those estimates to a naive receipt contrast and explain why receipt is not randomized.

**Diagnose.** Students inspect baseline balance by assignment, take-up rates, attrition, outcome availability, and a simple coworker-exposure measure. They write a short memo explaining what assignment identifies, what receipt does not identify by itself, and whether peer exposure should be treated as a threat or a mechanism.

**Transfer.** Students then move to a synthetic labor-market saturation design inspired by displacement and platform experiments. They compare individual treatment, market saturation, and untreated-worker exposure. The transfer task asks students to decide whether the meaningful estimand is an ITT, a complier effect, a direct effect, a spillover effect, or a market-level effect.

The central lab question is not "does the experiment work?" It is "which object does this design identify, and what interpretation can a skeptical applied reader defend?"

## Methods Box

:::{admonition} Methods Box: What Makes Experimental Designs Persuasive?
:class: note

Strong experimental papers answer six questions before asking readers to believe the estimate.

1. **Assignment.** Who or what was randomized, and was the assignment protocol implemented as planned?
2. **Estimand.** Is the paper estimating an ATE, ITT, complier effect, direct effect, spillover effect, or market-level effect?
3. **Implementation.** Did treated units receive the treatment, did control units avoid it, and what changed in practice?
4. **Measurement.** Are outcomes observed consistently across assignment arms, and are attrition or survey response differences addressed?
5. **Interference and scale.** Could the experiment affect untreated units or change equilibrium behavior?
6. **Portability.** Which features of the population, institution, treatment intensity, and market environment must travel for the result to apply elsewhere?

The key interpretation sentence is: "This experiment identifies the effect of the randomized design margin for the experimental population and scale, subject to the stated compliance, measurement, interference, and implementation conditions." A strong paper makes every phrase in that sentence observable to the reader.
:::

## Reading Ladder And References

```{include} assets/tables/02-reading-architecture.md
```

**Foundations.** Start with Fisher for the design-of-experiments tradition and Imbens and Rubin for modern potential-outcomes notation [@fisher1935; @imbensRubin2015]. Athey and Imbens provide a compact econometric treatment of randomized experiments [@atheyImbens2017]. Gerber and Green are useful for design, analysis, and interpretation in field experiments [@gerberGreen2012].

**Field-experiment framing.** Harrison and List supply the field-experiment taxonomy, while List gives practical advice on running field experiments in economics [@harrisonList2004; @list2011].

**Labor and applied anchors.** Duflo and Saez are the primary encouragement and spillover anchor [@dufloSaez2003]. Bertrand and Mullainathan are the canonical audit/correspondence design [@bertrandMullainathan2004]. Bloom et al. anchor firm-level randomized intervention [@bloomEtAl2013]. Pallais anchors platform labor-market experimentation [@pallais2014].

**Equilibrium and scale.** Crepon et al. are the central caution for displacement, spillovers, and equilibrium response in labor-market experiments [@creponEtAl2013].

**Toolkit.** Duflo, Glennerster, and Kremer remain useful for practical randomized-evaluation design, especially around implementation, power, and field logistics [@dufloGlennersterKremer2007].

## Exercises And Discussion Prompts

1. In a randomized job-training encouragement design, write the ATE, ITT, first stage, and Wald/LATE in words. Which object is most policy-relevant if the government can only offer the program?
2. Starting from {eq}`eq:em2-random-assignment`, explain why baseline balance is expected but not guaranteed in any one finite sample.
3. In Duflo and Saez, why is seminar attendance not the same object as randomized encouragement? What does the first stage measure?
4. Design an audit experiment for hiring discrimination. What signal is randomized, what outcome is measured, and what labor-market margin remains outside the design?
5. Suppose a firm-level management experiment improves treated firms' productivity. What evidence would you want before interpreting the result as a scalable policy lesson?
6. Give one example where spillovers are a threat to a simple treatment-control contrast and one example where spillovers are the mechanism of interest.
7. Why can a clustered experiment have a large number of individuals but low power? What would you report to make the inference problem visible?
8. Read a field experiment in labor, public, development, education, or organizational economics. Identify the assignment unit, treatment, ITT, compliance margin, attrition risk, spillover risk, and external-validity claim.
9. Sketch a transfer project using a platform or administrative partner. What would you randomize, what would you measure, and what ethical or implementation constraints would shape the design?

## Reproducibility And Code Lab Note

The Lecture 2 code lab lives at `labs/02-experiments-and-field-experiments/`. It is a bounded synthetic teaching path inspired by Duflo and Saez's randomized encouragement design and by labor-market saturation concerns in Crepon et al. It does not claim to reproduce the original papers' data or published magnitudes.

The smoke path creates deterministic synthetic data, estimates ITT, first-stage, Wald/LATE, naive receipt contrasts, balance diagnostics, attrition diagnostics, and exposure/spillover summaries, then repeats the logic in a transfer saturation design. The lab is small enough to run locally without external downloads.

## Slide Companion Note

The Lecture 2 slide deck lives at `slides/week2/02-experiments-and-field-experiments.tex`. The deck mirrors the chapter without duplicating it: it defines what randomization identifies, separates ITT from take-up and LATE, shows how audit experiments isolate signal response, explains clustered assignment and spillovers, discusses external validity and equilibrium, and closes with the Research Lab design.

## Bridge Forward

Lecture 2 shows the cleanest version of design-based identification: the counterfactual is built by random assignment. Lecture 3 turns to DID, event studies, and synthetic control. There the counterfactual is no longer randomized. It is built from untreated outcome paths, timing, and comparison units. The experimental logic remains useful because it keeps the questions sharp: what is the target parameter, what creates the comparison, what can break it, and how should the result be interpreted?
