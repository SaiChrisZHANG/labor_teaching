# Health, Risk, And Labor Markets: Core Frameworks And Measurement

## Learning Objectives

By the end of Week 1, students should be able to:

1. define health as work capacity, human capital, labor-market risk, and a constraint on the feasible set for work;
2. distinguish health as a worker-side margin from health as a firm-side margin;
3. explain why self-reported health, diagnoses, biomarkers, disability status, mortality risk, mental health, insurance coverage, and treatment access measure different objects;
4. diagnose reverse causality, omitted socioeconomic status, and dynamic selection in health-labor designs;
5. map health into labor supply, job choice, productivity, mobility, wages, amenities, worker welfare, and firm behavior;
6. design a bounded measurement exercise that compares health measures before making a causal or welfare claim.

The opening question is direct: how should labor economists model and measure health when health affects both productivity and the feasible set for work?

## Opening Orientation

This opening week frames health as a labor-market object, not as a background demographic characteristic. In labor economics, health matters because it changes whether work is feasible, how productive workers are on the job, which occupations and schedules are tolerable, how valuable insurance and flexibility are, and how wages and amenities should be interpreted. The same observed employment loss can reflect diminished work capacity, endogenous exits from demanding jobs, insurance and benefit rules, employer screening, or dynamic selection into healthier workers.

Week 1 also makes measurement a first-order research problem. Health is rarely observed as the exact work-capacity object that a labor model needs. A self-report, a diagnosis, a biomarker, a disability determination, an acute hospitalization, a mortality-risk indicator, a mental-health scale, and insurance coverage all sit at different points between underlying health, measured health, labor-market behavior, and institutional response. Students should leave this week with a discipline that will matter throughout the course: state the labor margin, state the health object, state the likely bias, and state the welfare object before interpreting a health coefficient.

:::{admonition} Core points
:class: important

- Health enters labor economics as human capital, work capacity, labor-market risk, and heterogeneity in the feasible set for work.
- Measurement is central: self-reports, diagnoses, biomarkers, disability status, mortality risk, mental health, insurance coverage, and treatment access do not capture the same object.
- Causal interpretation is hard because health is jointly determined with work through income, stress, insurance, job conditions, and selection [@currieMadrian1999; @bound1991].
- Health affects labor outcomes through worker-side and firm-side channels, so reduced-form estimates can mix labor supply, productivity, sorting, accommodations, screening, and benefit design.
- One of the field's enduring research opportunities is to connect better measurement to more credible identification and better welfare interpretation.

:::

## Bridge

Labor I supplies the worker-side foundations: labor supply, human capital, job amenities, household allocation, mobility, wage determination, inequality, and welfare. Labor II supplies the firm and market architecture: labor demand, productivity, wage setting, insurance provision, accommodations, screening, search, and adjustment. This course sits between them. It asks how health and population forces change work, wages, allocation, and welfare.

The first move is to keep the labor object visible. Health matters here because it changes whether people can work, how much they can work, which jobs are feasible, how productive they are, what risks they face inside jobs, and how firms organize work around health constraints. A health-economics course might begin from medical care, insurance markets, or provider behavior. This course begins from work.

The second move is to avoid treating "health" as a single variable. Measurement error, reverse causality, omitted socioeconomic status, and dynamic selection can all make "health effects" ambiguous unless the labor margin and health object are specified carefully [@currieMadrian1999; @blundellBrittonCostaDiasFrench2023].

## Field Core

### Health As Work Capacity, Human Capital, And Risk

The benchmark labor perspective treats health as simultaneously:

- a productivity input;
- a determinant of work capacity and feasible hours;
- a risk process affecting future employment, wages, mobility, and retirement;
- a source of heterogeneity in tolerance for job tasks, schedules, commuting, stress, and amenities;
- a welfare object, because work may impose pain, risk, stress, or treatment constraints even when wages are observed.

In this sense, health is not just another control variable. It changes the budget set, the feasible set, and the expected value of future labor-market states. A worsening health shock may reduce hours, force occupational downgrading, alter search intensity, raise demand for safer or more flexible jobs, or change the value of employer insurance even when observed employment does not move immediately [@currieMadrian1999; @french2000].

```{include} assets/tables/01-health-as-labor-object-map.md
```

Grossman's health-capital framework is useful because it makes health durable and choice-linked [@grossman1972health]. But the labor application cannot stop there. For labor economists, the central object is not only the demand for health. It is the way health shapes labor supply, productivity, job choice, mobility, firm behavior, and welfare over time.

### Measurement: What Exactly Is Health In Labor Data?

A central open question in the field is what labor economists are measuring when they claim to measure health. Week 1 should make clear that common measures capture different objects:

- **Self-reported health** can summarize private information about functioning, pain, fatigue, cognition, and latent conditions, but it is vulnerable to reporting heterogeneity and justification bias.
- **Diagnosed conditions, biomarkers, and hospitalization records** can be more objective, but they are incomplete proxies for work capacity and may miss functional limitations relevant for labor.
- **Disability status and administrative definitions** are not pure health; they are joint outcomes of health, program rules, administrative criteria, application costs, and incentives.
- **Mortality risk and severe health shocks** can identify severe disruptions, but they may not map cleanly into everyday work capacity or chronic limitations.
- **Mental health and latent conditions** often matter through cognition, stress, persistence, social functioning, pain, and stigma, yet they are especially difficult to measure cleanly in labor data.
- **Insurance coverage and treatment access** can change observed health, labor supply, reported health, recovery, job lock, and mobility at the same time.

```{include} assets/tables/01-measurement-and-identification-map.md
```

The classic measurement lesson is that neither subjective nor objective measures are automatically correct. Bound shows that self-reported and objective measures each have bias problems, while Blundell, Britton, Costa Dias, and French show how richer objective measures and careful dynamic modeling can change estimates of the effect of health on employment near retirement [@bound1991; @blundellBrittonCostaDiasFrench2023]. Baker, Stabile, and Deri remain useful because they show that even allegedly objective self-reported measures can contain substantial measurement error [@bakerStabileDeri2001].

The interpretation rule is simple: different measures imply different empirical objects. Self-reported poor health may be closer to latent work capacity than a diagnosis when the diagnosis misses pain or fatigue. A biomarker may be more clinically objective but less predictive of task feasibility. Disability-program status may be the correct policy object but a poor pure health measure. Disagreement across measures is often information, not a nuisance.

### Reverse Causality, Dynamic Selection, And Omitted Socioeconomic Status

A good Week 1 lecture in this field has to make clear why naive regressions are often uninformative.

**Reverse causality.** Work changes health through injuries, stress, hours, schedules, income, insurance access, workplace safety, commuting, and job conditions. Employment may improve health by providing income and insurance, or worsen health by exposing workers to strain and risk.

**Omitted socioeconomic status.** Early-life resources, education, neighborhood context, parental health, occupation, wealth, insurance status, and local labor demand shape both health and labor outcomes. A health coefficient may partly proxy for cumulative socioeconomic advantage.

**Dynamic selection.** Healthier people remain employed longer, sort into different firms and occupations, accumulate different work histories, and become overrepresented among older workers. Less healthy workers may exit before the researcher observes the relevant shock.

**Program and insurance rules.** Disability insurance, employer insurance, Medicaid, Medicare, sick leave, and workplace accommodation rules alter labor supply independently of underlying work capacity.

A stripped-down empirical design often looks like this:

```{math}
:label: eq:st6-w1-health-labor-design
Y_{it} =
\beta H_{it}
+ X_{it}'\Gamma
+ \alpha_i
+ \lambda_t
+ \varepsilon_{it},
```

where {math}`Y_{it}` may be employment, hours, wages, job choice, mobility, productivity, or welfare, and {math}`H_{it}` is a measured health object. The coefficient {math}`\beta` cannot be interpreted until the measure and timing are explicit. Does {math}`H_{it}` capture latent work capacity, reported limitation, diagnosis, disability determination, treatment access, or a severe shock? Does the design handle the possibility that {math}`Y_{it}` also changes {math}`H_{it}`?

This is why acute-shock designs, hospitalization studies, disability threshold designs, and dynamic retirement models remain so important. Garcia-Gomez and coauthors show how acute shocks can have persistent labor-market effects, while Meyer and Mok illustrate how disability onset affects earnings, income, and consumption over time [@garciaGomez2013; @meyerMok2013].

### Worker-Side And Firm-Side Health Channels

Although much of the literature emphasizes labor supply, Week 1 should set up the course's broader map by separating worker-side and firm-side channels.

```{include} assets/tables/01-worker-and-firm-side-channels-map.md
```

**Worker-side channels** include work capacity, labor supply, hours, job choice, occupational feasibility, commuting tolerance, search intensity, mobility, retirement, exit timing, demand for insurance, and valuation of amenities.

**Firm-side channels** include hiring and screening on perceived health or work capacity, task assignment, accommodation, absenteeism expectations, insurance provision, workplace safety investments, scheduling, contract design, monitoring, and retention responses to health risk.

This distinction helps students see why the same health shock can generate different reduced-form labor outcomes depending on the institutional environment and firm technology. A health limitation may reduce hours in a physically demanding job, change job amenities in a flexible job, alter wages through productivity in a performance-pay job, or trigger accommodation and retention responses inside a firm with costly turnover.

### A Field Map For The Rest Of The Course

Week 1 is broad because the rest of the course unpacks the framework one margin at a time.

```{include} assets/tables/01-field-map.md
```

Week 2 moves directly into disability, chronic conditions, labor supply, job choice, accommodations, and program interaction. Week 3 studies fertility, mortality, caregiving, aging, and lifecycle labor allocation. Week 4 moves inside workplaces through mental health, stress, productivity, absenteeism, presenteeism, and worker welfare. Week 5 scales up to disease exposure, environmental health, demographic change, firms, places, and adjustment. Week 6 converts the sequence into research designs.

Throughout the course, the key empirical discipline is to state:

1. the labor margin of interest;
2. the health or population object being measured;
3. the likely sources of bias;
4. the worker-side and firm-side channels in play;
5. the welfare object being interpreted.

## Research Lab

The Week 1 research lab follows **Reproduce -> Diagnose -> Transfer**. The primary anchor is Blundell, Britton, Costa Dias, and French on how health measures and methods change estimates of the effect of health on employment near retirement [@blundellBrittonCostaDiasFrench2023]. The challenge anchor is Bound's measurement critique of self-reported versus objective health measures [@bound1991]. The lab is not an official replication package for either paper. It is a bounded teaching exercise that uses deterministic synthetic data to practice the field's measurement discipline.

**Reproduce.** Students recover simple reduced-form relationships between alternative health measures and employment or hours. The smoke path compares latent work capacity, self-reported poor health, diagnosed condition severity, biomarker risk, disability-program status, mental-health burden, and insurance or treatment access. The object is the measurement logic: estimates change when the health object changes.

**Diagnose.** Students ask which part of each estimate is likely measurement-driven. They classify each health measure as private-information-rich, clinically objective, administratively defined, severe-shock-based, latent-condition-sensitive, or institutionally mediated. They then diagnose threats from reverse causality, omitted socioeconomic status, and dynamic selection.

**Transfer.** Students transfer the same measurement logic to bounded alternative settings: acute hospitalization, disability onset, mental-health treatment timing, and insurance-linked treatment access. The transfer task keeps the labor question fixed, but varies the health measure and identification design.

## Methods Box

:::{admonition} Methods Box: Measurement Discipline For Health And Labor
:class: note

**Health measure before health effect.** A coefficient on "health" is uninterpretable until the researcher names the measured object: self-report, diagnosis, biomarker, disability status, mortality risk, mental health, insurance, treatment, or severe shock.

**Work capacity versus clinical status.** A diagnosis may be clinically meaningful without being the right work-capacity measure. A self-report may be subjective but closer to pain, fatigue, or functional limitation.

**Disability status is institutional.** Administrative disability status blends health, work capacity, eligibility rules, application costs, expected benefits, and labor-market opportunities.

**Objective does not mean bias-free.** Biomarkers and diagnoses can still miss untreated conditions, functional severity, task demands, and treatment access.

**Timing is part of identification.** Work can affect health, health can affect work, and both evolve with income, stress, insurance, job conditions, and selection.

**Wages are not welfare.** Health changes pain, risk, stress, treatment constraints, job amenities, and insurance value. A wage-only outcome can miss central welfare effects.

:::

## Reading Ladder And References

**Core framing.** Start with Currie and Madrian for the classic labor-market map of health, then read Blundell, Britton, Costa Dias, and French for modern measurement and dynamic labor-supply evidence [@currieMadrian1999; @blundellBrittonCostaDiasFrench2023].

**Measurement foundations.** Use Bound for the classic subjective-versus-objective measurement lesson and Baker, Stabile, and Deri for measurement error in allegedly objective self-reports [@bound1991; @bakerStabileDeri2001].

**Health capital and socioeconomic confounding.** Use Grossman for health capital and Smith or Currie for the two-way relationship between health, socioeconomic status, and human capital [@grossman1972health; @smith1999healthyBodies; @currie2009healthyWealthyWise].

**Shocks and dynamics.** Use Garcia-Gomez and coauthors, Meyer and Mok, and Dobkin and coauthors for severe shocks, disability onset, and hospitalization as labor-market events [@garciaGomez2013; @meyerMok2013; @dobkinFinkelsteinKluenderNotowidigdo2018hospital].

**Disability, retirement, and institutions.** Use Bound, Schoenbaum, Stinebrickner, and Waidmann, Autor and Duggan, Maestas, Mullen, and Strand, Low and Pistaferri, and French and Jones to prepare for Week 2's disability and program-interaction focus [@boundSchoenbaumStinebricknerWaidmann1999dynamic; @autorDuggan2003disabilityRolls; @maestasMullenStrand2013ssdi; @lowPistaferri2015disability; @frenchJones2011retirement].

**Recent synthesis.** Pintor provides a recent review of the broader health-labor evidence [@pintor2024].

## Exercises And Discussion Prompts

1. In what sense is health simultaneously a productivity input and a constraint on the feasible set for work?
2. Why is it misleading to speak of "the effect of health on employment" without specifying a health measure and a labor margin?
3. Compare self-reported health, biomarker risk, and administrative disability status as labor-economics variables. What does each capture, and what does each miss?
4. Give one example of reverse causality, one example of omitted socioeconomic status, and one example of dynamic selection in the health-labor literature.
5. Suppose two papers study the same condition but reach different employment effects. What are the first three design questions you would ask before interpreting the difference substantively?
6. Pick one labor margin: hours, job choice, mobility, wages, amenities, productivity, or welfare. Which health measure would be most informative, and which bias would worry you most?

## Reproducibility And Code Lab Note

The Week 1 code lab lives at `labs/01-health-risk-and-labor-markets-core-frameworks-and-measurement/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates deterministic worker-level teaching data; compares alternative health measures against employment, hours, and feasible-set outcomes; writes compact reproduce, diagnose, and transfer outputs; and requires no confidential data or external downloads.

The lab is conservative by design. Blundell, Britton, Costa Dias, and French are the primary conceptual anchor, and Bound is the challenge anchor, but the local exercise reproduces measurement logic rather than claiming access to official microdata or replication files.

## Slide Companion Note

The Week 1 slide deck lives at `slides/week1/01-health-risk-and-labor-markets-core-frameworks-and-measurement.tex`. The deck mirrors the chapter logic without duplicating the prose: it defines health as a labor object, centers measurement choices, isolates reverse causality and dynamic selection, separates worker-side and firm-side channels, maps the rest of the course, and closes with the Research Lab design.

## Bridge Forward

Week 2 takes the framework from general health measurement to the specific labor-market consequences of disability and chronic conditions. That move is intentional: once students understand why health is difficult to measure and interpret, they can study particular health states with clearer causal discipline. The Week 1 lesson carries forward: before asking whether health reduces work, students must ask which health object is measured, which labor margin is exposed, how workers and firms adjust, and what welfare object is visible.
