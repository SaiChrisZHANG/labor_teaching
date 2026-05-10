# Week 7 Source Pack — Experiments, Measurement, and Behavioral Identification in Labor

## Week identity

- Course: Behavioral Labor
- Week: 7
- Canonical chapter path: `books/special-topic1-behavioral/07-experiments-measurement-and-behavioral-identification-in-labor.md`
- Canonical slide path: `books/special-topic1-behavioral/slides/week7/07-experiments-measurement-and-behavioral-identification-in-labor.tex`
- Canonical lab path: `books/special-topic1-behavioral/labs/07-experiments-measurement-and-behavioral-identification-in-labor/`

## Central question

How do behavioral labor economists move from a behavioral object to a labor-market setting, to a data design, to an actual econometric method, and what practical empirical tools are most commonly used in applied work?

## Why this week matters

By Week 7, students have seen the main substantive branches of behavioral labor: nonstandard preferences, beliefs and expectations in job search, attention and complexity, workplace incentives, and micro norms in labor-market allocation. The obvious next question is methodological: **how do labor economists actually identify and estimate these behavioral mechanisms?**

Applied courses often stop too early. Students learn that job-search beliefs can be measured, that information interventions can shift take-up, that complex schedules can attenuate labor-supply elasticities, or that field experiments can uncover social preferences. But they may still be unclear about the actual econometric methods that researchers use once the setting is in place.

This week should close that gap. It is not a generic econometrics lecture. It is a **behavioral-labor toolkit week** that helps students map:

1. a behavioral object,
2. a labor-market setting,
3. an identification strategy,
4. an econometric method,
5. and an interpretation / welfare statement.

The week should leave students with a practical sense of what one actually does in modern applied behavioral labor research.

## Position in the sequence

- Weeks 1–6 built the substantive architecture of Behavioral Labor.
- Week 7 now pauses and systematizes the empirical toolkit.
- Week 8 will turn from toolkit to firm, market, and equilibrium responses, using many of the same methods and designs to distinguish worker response, firm strategy, and market outcomes.

## Core teaching goal

By the end of the week, students should be able to:

- distinguish measurement, identification, estimation, and interpretation in behavioral labor studies;
- understand which econometric methods are typically used in different behavioral-labor settings;
- explain why job-search durations invite hazard models, why nonlinear schedules invite bunching tools, why field experiments often use ANCOVA-style estimators, and why some behavioral questions require structural estimation;
- diagnose when a design identifies a treatment effect, a latent parameter, a behavioral wedge, or just a reduced-form response;
- see the connection between empirical setting and actual econometric practice.

## Required chapter architecture

Use the standard structure:

- opening orientation / why this week matters
- **Core points** box
- Bridge
- Field Core
- Research Lab
- reading ladder / references
- bridge forward to Week 8

Do not add an Extension box by default.

## Bridge

The Bridge should do four things:

1. connect the substantive weeks (2–6) to this toolkit week by explaining that the course now turns from **what the behavioral objects are** to **how they are measured and identified**;
2. make clear that there is no single “behavioral estimator” — instead, behavioral labor combines standard econometric tools with special measurement, design, and modeling choices;
3. remind students that the same labor setting can be analyzed with different empirical strategies depending on the question;
4. foreshadow that Week 8 will apply this toolkit to firm, market, and equilibrium responses before Week 9 turns to policy design.

## Core points box: essentials to surface

- Behavioral labor research links **behavioral objects** to **labor settings**, **identification strategies**, and **econometric methods**.
- Modern applied work often combines standard labor designs with behavioral measurement: field experiments, subjective expectations data, information interventions, nonlinear-incentive settings, and structural estimation.
- Different labor outcomes call for different empirical tools: search duration often uses hazard models, nonlinear schedules often use bunching methods, panel beliefs data often use fixed-effects and validation exercises, and latent behavioral parameters may require structural estimation.
- Good behavioral-labor empirics require students to ask not just “what is the setting?” but also “what is the estimand, what is the method, and what assumptions make the interpretation credible?”
- The frontier is not just new topics; it is better measurement, clearer design, and tighter links between reduced-form evidence and behavioral parameters.

## Field Core: conceptual arc

### A. What counts as behavioral identification in labor?

The chapter should begin by defining the core objects that behavioral labor studies try to recover:

- nonstandard preferences,
- biased or incomplete beliefs,
- limited attention or salience,
- norm sensitivity and social preferences,
- dynamic learning and information acquisition.

A central point of the week is that these are usually not observed directly. Researchers infer them from choice data, experimental responses, elicited beliefs, labor-market transitions, effort data, or combinations of these.

A simple measurement object should appear early:

```{math}
:label: eq:measurement-week7-source
z_{ij} = \theta_i + \eta_{ij}
```

where {math}`\theta_i` is the latent behavioral object of interest and {math}`\eta_{ij}` is measurement noise. The text should explain that much of the week is about how labor economists generate or proxy `{math}`z_{ij}` and then connect it back to `{math}`\theta_i``.

### B. Randomized field experiments and real labor settings

This section should make clear why field experiments became such an important part of behavioral labor. They allow the researcher to shift incentives, information, reminders, gifts, or framing in real work or search environments while observing labor margins that matter.

A basic randomized-treatment equation should be included:

```{math}
:label: eq:rct-week7-source
Y_i = \alpha + \beta T_i + X_i'\gamma + \varepsilon_i
```

The chapter should explain that the practical implementation is often plain OLS or ANCOVA with baseline controls, paired with treatment heterogeneity and design diagnostics. This is a good place to connect students back to labor settings they have already seen:

- job-search advice or information,
- EITC / take-up letters,
- workplace gift exchange,
- incentive-framing experiments,
- work scheduling or contract experiments.

Use `[@listRasul2011]` as a broad labor field-experiments anchor, and then ground the discussion in course-specific examples such as `[@altmannFalkJaegerZimmermann2018]`, `[@bhargavaManoli2015]`, `[@dellaVignaListMalmendierRao2022]`, and `[@dellaVignaPope2018]`.

### C. Subjective expectations, beliefs, and repeated survey measurement

This section should show that behavioral labor often needs **measurement** in addition to exogenous variation. The point is not just to elicit beliefs once, but to understand their level, bias, persistence, and updating over time.

The chapter should explain the practical toolkit around beliefs data:

- repeated elicitation,
- calibration / validation against outcomes,
- panel structure,
- fixed effects,
- forecast errors,
- measurement error,
- and the distinction between beliefs and realized opportunities.

A good running anchor is `[@muellerSpinnewijnTopa2021]`, which naturally opens the door to discussing how subjective job-finding beliefs are related to search duration and subsequent labor-market outcomes.

This is also a good place to tell students explicitly: when the data are repeated subjective expectations, the natural empirical toolkit is often **panel fixed-effects models, validation exercises, and measurement-error-aware interpretation**, not just a cross-sectional reduced form.

### D. Information interventions and learning designs

A separate section should explain information-provision experiments and why they are especially important in behavioral labor. The chapter should distinguish:

- changing beliefs,
- changing salience,
- changing procedural knowledge,
- changing confidence or perceived eligibility,
- and changing learning speed.

Use `[@haalandRothWohlfart2023]` as a methods anchor and connect it back to labor applications such as job-search guidance, benefit take-up, and nonlinear-schedule learning. The main point is that the econometric implementation may still be simple reduced-form treatment effects, but the **interpretation** depends on what information object is actually shifted.

### E. Job-search durations and hazard methods

Because search outcomes are often durations, a practical methods bridge should make hazard models explicit rather than leaving them implicit.

Include a hazard object such as:

```{math}
:label: eq:hazard-week7-source
h_{it} = \Pr(U_{i,t+1}=0 \mid U_{it}=1,\, X_{it}, B_{it})
```

Then explain clearly that behavioral job-search papers often map naturally into:

- discrete-time logit or probit hazard models,
- Cox proportional-hazard models,
- duration-dependence tests,
- state dependence vs belief updating.

Students should understand why the *outcome* often determines the method. If the object is unemployment duration or exit rates, hazard methods are often the practical default.

### F. Nonlinear schedules, salience, and bunching

This subsection should bridge the attention/salience week into methods. When workers respond to nonlinear incentives or tax-benefit schedules, the empirical question often becomes local and design-based.

A simple elasticity or bunching object should appear:

```{math}
:label: eq:bunching-week7-source
\hat e = \frac{\Delta b / b}{\Delta (1-\tau)/(1-\tau)}
```

The point is not to teach the full bunching estimator, but to explain that in salience or knowledge-friction environments, labor economists often use:

- kink / notch logic,
- bunching estimation,
- local reduced-form elasticities,
- and then ask whether attenuation reflects preferences, lack of knowledge, or slow learning.

Use `[@chettyFriedmanSaez2013]` as the labor-relevant anchor for knowledge frictions and nonlinear incentives.

### G. Quasi-experiments: IV, RD, DiD, and event studies in behavioral settings

This section should make clear that behavioral labor is not only experiments and structural work. Many papers rely on quasi-experimental variation generated by policies, information regimes, timing, or institutional thresholds.

The main teaching goal here is not to review all causal inference, but to tell students that when behavior is shifted by:

- a threshold or score,
- staggered information release,
- eligibility changes,
- administrative simplification,
- or exposure to policy/information environments,

then the practical toolkit may be IV, RD, DiD, or event-study designs.

This is where the chapter should explicitly bridge empirical setting to method, rather than listing the settings alone.

### H. Structural behavioral estimation

This section should make clear why some behavioral labor questions cannot be answered with reduced forms alone. If the goal is to recover present bias, reference-point dynamics, social preference parameters, belief updating rules, or dynamic information costs, then the literature often moves toward structural estimation.

A canonical objective should be included:

```{math}
:label: eq:structural-week7-source
\hat \psi \in \arg\min_{\psi \in \Psi}
\left[m^{data}-m^{model}(\psi)\right]'W\left[m^{data}-m^{model}(\psi)\right]
```

The chapter should explain, in plain language, the role of:

- MLE,
- simulated method of moments,
- dynamic discrete-choice style structures,
- calibration vs full structural estimation.

Use `[@dellaVigna2018]` as the conceptual anchor, and connect it to labor-facing applications such as `[@kaurKremerMullainathan2015]` or `[@dellaVignaListMalmendierRao2022]`.

### I. Practical methods bridge: from setting to econometric tool

This is the section you explicitly wanted. It should be practical and concrete.

It can be a subsection, a box, or a heavy-use table, but it should summarize things like:

- **Repeated subjective expectations panel** -> panel FE, forecast-error validation, measurement-error concerns.
- **Randomized labor-field intervention** -> OLS/ANCOVA, randomization inference, heterogeneity analysis.
- **Job-search duration outcome** -> hazard methods.
- **Nonlinear tax-benefit or schedule response** -> bunching / local elasticity tools.
- **Behavioral parameter recovery** -> structural MLE/SMM / dynamic models.
- **Quasi-experimental information or policy shock** -> IV / RD / DiD / event study.

The chapter should emphasize that the econometric method is often determined by the combination of:

1. behavioral object,
2. outcome margin,
3. data structure,
4. source of variation,
5. and the desired estimand.

### J. Failure modes and interpretation

A final Field Core subsection should make the main practical mistakes explicit:

- mistaking a setting for an estimand,
- failing to separate treatment from measurement,
- confusing beliefs with realized opportunities,
- using reduced forms when the interpretation actually requires parameter recovery,
- over-interpreting bunching or attenuation without a knowledge/salience model,
- ignoring equilibrium or external-validity limits.

## How labor economists actually use these methods

This should be a short synthesis section inside Field Core or just before Research Lab. It should answer the user’s concern directly:

Students often understand what empirical settings can be used, but not which methods are typically employed. The chapter should bridge that gap by summarizing the actual tools used in papers they have already seen:

- labor-field experiments: OLS/ANCOVA, treatment heterogeneity, design checks;
- job-search papers: hazard models, beliefs validation, panel analysis;
- salience / complexity papers: bunching and local elasticities plus information-treatment contrasts;
- structural behavioral papers: MLE/SMM or related parameter-recovery exercises;
- policy and institutional settings: IV / RD / DiD / event studies when the setting is quasi-experimental.

This should ideally be one of the clearest practical sections in the entire course.

## Research Lab

### Replication / transfer spine

- Primary anchor: `[@altmannFalkJaegerZimmermann2018]`
- Secondary / challenge anchor: `[@dellaVignaListMalmendierRao2022]`
- Optional extension anchor: `[@chettyFriedmanSaez2013]` or `[@kaurKremerMullainathan2015]`

### What students should diagnose

The lab should require students to identify:

1. the behavioral object,
2. the outcome margin,
3. the identifying variation,
4. the actual econometric method,
5. the key identifying assumptions,
6. whether the paper is primarily reduced form, measurement-based, or structural.

### Transfer logic

The transfer exercise should explicitly ask students to propose:

- a nearby labor setting,
- the relevant data structure,
- the behavioral object,
- the method they would actually estimate,
- and why that method matches the setting.

This is a good week for a short “design-to-method memo” as a lab deliverable.

## Candidate figures to encourage in the chapter draft

1. A behavioral-object -> data -> design -> method pipeline figure.
2. A methods taxonomy figure for experiments, panels, hazards, bunching, and structural estimation.
3. A job-search duration / hazard schematic.
4. A nonlinear-schedule / bunching schematic.

## Tables to use

Use the following tables heavily:

- `assets/tables/07-behavioral-object-data-and-design-map.md`
- `assets/tables/07-empirical-setting-to-econometric-methods-map.md`
- `assets/tables/07-identification-diagnostics-and-common-failures.md`

## Reading ladder expectations

### Framing and methods backbone
- `[@dellaVigna2009]`
- `[@dellaVigna2018]`
- `[@listRasul2011]`
- `[@haalandRothWohlfart2023]`

### Beliefs and expectations measurement
- `[@muellerSpinnewijnTopa2021]`

### Information interventions and labor settings
- `[@altmannFalkJaegerZimmermann2018]`
- `[@bhargavaManoli2015]`

### Structural and parameter-recovery examples
- `[@kaurKremerMullainathan2015]`
- `[@dellaVignaListMalmendierRao2022]`

### Salience, knowledge, and nonlinear schedules
- `[@chettyFriedmanSaez2013]`

### Real-effort experiment benchmark
- `[@dellaVignaPope2018]`

## Forward bridge to Week 8

End the source pack by telling students that Week 8 moves from the empirical toolkit to firm, market, and equilibrium responses to behavioral frictions. The key bridge is that the methods from this week are precisely the tools needed to separate worker-level behavioral objects from firm response margins and market outcomes before Week 9 turns to policy design.
