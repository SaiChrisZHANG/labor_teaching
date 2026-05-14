---
title: Mental Health, Stress, Workplace Productivity, and Worker Welfare
bibliography:
  - references.bib
---

# Week 4. Mental Health, Stress, Workplace Productivity, and Worker Welfare

## Opening orientation

Mental health enters labor markets through multiple margins at once. It affects attendance, effort, concentration, interpersonal functioning, job search, disclosure, treatment seeking, and the welfare value of work itself. It is also shaped by jobs: workload, supervision, conflict, insecurity, isolation, schedule volatility, and meaning at work can worsen or improve mental well-being. The main challenge for labor economists is to model and measure these two-way links without collapsing the topic into either clinical description or pure reduced-form correlation.

:::{admonition} Core points
:class: important
- Mental health is both a productivity object and a welfare object: wages alone may miss substantial losses through absenteeism, presenteeism, stress, and diminished job quality.
- Stigma and treatment frictions matter for labor-market outcomes because they shape disclosure, accommodations, care-seeking, and retention.
- Labor-market choices and workplace conditions also affect mental health, so reverse causality is central rather than incidental.
- Measurement is hard: survey symptoms, diagnoses, prescriptions, disability claims, and administrative outcomes each capture different parts of the same phenomenon.
- The empirical frontier is still open because credible causal identification often relies on shocks to treatment access, labor-market conditions, or workplace organization.
:::

## Bridge

Week 1 framed health as work capacity, risk, and a source of labor-market heterogeneity. Week 2 focused on chronic conditions and disability, and Week 3 on lifecycle allocation under fertility, caregiving, aging, and mortality risk. This week narrows in on mental health and stress because they are often less visible, more stigmatized, and harder to identify causally, yet they shape central labor outcomes like productivity, retention, and the welfare value of employment.

## Field Core

### 1. Mental health as a labor-market object

A useful labor-economics starting point is to treat mental health as affecting both the *capacity* to work and the *disutility* of work. Depression, anxiety, stress, pain, and substance use can change attendance, concentration, effort, social interactions, and the ability to sustain particular schedules or job tasks. They may also interact with job amenities, supervision, and workplace control.

Two distinctions are useful:
1. **Productivity losses**: absenteeism, presenteeism, lower task completion, slower learning, and exits.
2. **Welfare losses**: work may be formally “feasible” but much less valuable because it worsens stress, undermines self-respect, or raises psychic costs.

The classic productivity side is well illustrated by [@bubonyaCobbClarkWooden2017], while newer structural work explicitly models two-way interactions between work and mental health [@jolivetPostelVinayRobin2025].

### 2. Measurement: symptoms, diagnosis, treatment, and administrative proxies

Mental health research in labor economics is measurement-intensive. Common empirical objects include:
- symptom scales such as PHQ-9, GHQ, CES-D, and K6;
- self-reported stress, burnout, anxiety, or distress;
- diagnosis records and treatment episodes;
- psychiatric prescriptions;
- sick leave, disability claims, and accommodations;
- workplace outcomes such as absenteeism, presenteeism, quits, and performance ratings.

These are not interchangeable. Symptom scales capture distress even without diagnosis; diagnosis depends on access to care and willingness to disclose; prescriptions capture treatment margins but not untreated need; and workplace outcomes bundle mental health with job design and incentives. A careful paper should be explicit about which latent object is being proxied and why.

### 3. Stigma, disclosure, and treatment as labor mechanisms

Stigma is not just a social background condition. In labor markets it shapes:
- whether workers seek treatment,
- whether they disclose symptoms,
- whether they request accommodations,
- whether employers interpret distress as risk or as treatable need,
- and whether treatment itself is viewed as a negative signal.

This makes treatment access and treatment *use* endogenous. Even when mental-health services exist, workers may avoid them because of perceived penalties for promotion, authority, reliability, or team fit. This is why anti-stigma and information interventions matter conceptually, even when evidence is still emerging. The treatment-gap literature and experimental destigmatization work are especially useful here [@laceyEtAl2022].

### 4. Work causing mental health: job quality, stress, and meaning

Mental health is not only an input into work; work is also a generator of mental-health outcomes. Job design can affect:
- stress exposure,
- autonomy and control,
- schedule unpredictability,
- social isolation,
- conflict and harassment,
- mission alignment and meaning,
- and the gap between effort and accomplishment.

That means job quality is a mental-health object, not just a utility shifter. Recent work highlights that meaning at work and alignment with employer values can be strongly associated with employee mental health [@krantonThomas2025], while broader evidence shows that job quality often matters more than hours per se for worker mental health [@wang2022]. This is also where Labor I themes around job amenities and worker welfare connect naturally to personnel economics.

### 5. Productivity, retention, and worker welfare

A labor-economics treatment of mental health should distinguish:
- **absence** from work,
- **presence but reduced productivity**,
- **sorting away from stressful or low-control jobs**,
- **retention and quits**,
- **delayed career progression**,
- and **changes in the welfare value of the same observed wage**.

The same worker may remain employed but suffer large welfare losses through stress and reduced functioning. Conversely, some treatment or accommodation margins may improve productivity and welfare without large immediate wage effects. This is why absenteeism and presenteeism remain central empirical objects [@bubonyaCobbClarkWooden2017].

### 6. Methods and causal identification caveats

This is one of the hardest parts of the field. Much of the evidence is vulnerable to:
- reverse causality (bad jobs worsen mental health),
- dynamic selection (only some workers remain observed in employment),
- omitted SES and family background,
- differential diagnosis and treatment intensity,
- co-morbidity with physical health,
- and self-report bias.

Credible causal designs therefore often rely on unusually sharp settings:
- shocks to treatment access or waiting times,
- policy expansions of coverage or workplace flexibility,
- severe job loss or workplace reorganization shocks,
- pandemic-era workplace shocks,
- administrative variation in treatment supply,
- or structural models that jointly model work and mental health [@jolivetPostelVinayRobin2025].

The current frontier is not “we have solved identification”; it is that we have a growing toolkit and clearer honesty about what each design does and does not identify.

### 7. Research architecture

A good research design in this area should answer five questions clearly:
1. What is the latent object: distress, diagnosis, treatment, functioning, or workplace loss?
2. Which labor margin is at stake: effort, attendance, job choice, retention, promotion, or welfare?
3. Is the design identifying mental health affecting labor, labor affecting mental health, or treatment affecting both?
4. What are the most serious threats: diagnosis intensity, disclosure, selection, or confounding job conditions?
5. What is the welfare object: income, productivity, treatment take-up, or broader worker well-being?

## Research Lab

### Primary anchor paper

Use [@bubonyaCobbClarkWooden2017] as the primary anchor because it provides a concrete and teachable empirical object: absenteeism and presenteeism as workplace productivity margins linked to mental health and job characteristics.

### Reproduce

Recreate the paper’s basic descriptive and regression logic:
- mental-health measure,
- absenteeism outcome,
- presenteeism outcome,
- heterogeneity by job characteristics.

The goal is not to reproduce the full original dataset exactly unless official materials are available locally, but to reconstruct the empirical logic in a bounded teaching path.

### Diagnose

Ask what the design really identifies:
- How much is a mental-health effect versus a job-quality effect?
- Which margins are measured well, and which are missing?
- What role do reporting bias and endogenous job sorting play?
- Why is presenteeism especially hard to measure credibly?

### Transfer

Apply the same logic to a bounded alternative setting:
- a treatment-access shock,
- a workplace-flexibility reform,
- a remote-work or isolation setting,
- or a job-loss / reemployment event-study design.

The transfer exercise should force students to specify:
- the latent mental-health object,
- the labor outcome,
- the identification threat,
- and the welfare margin.

### Optional extension paper

Use [@krantonThomas2025] or [@jolivetPostelVinayRobin2025] as the challenge paper, depending on whether the extension focuses on job meaning/identity or on dynamic structural identification.

## Reading Ladder And References

### Core framing
- [@currieMadrian1999]
- [@bound1991]
- [@pintor2023]

### Productivity and workplace outcomes
- [@bubonyaCobbClarkWooden2017]
- [@wang2022]
- [@krantonThomas2025]

### Dynamic and structural labor-market links
- [@jolivetPostelVinayRobin2025]
- [@garciaGomezJonesRice2022]

### Treatment, intervention, and stigma
- [@lundEtAl2024]
- [@laceyEtAl2022]

## Exercises And Discussion Prompts

1. Why is presenteeism conceptually attractive but empirically difficult?
2. Suppose a workplace mental-health intervention improves retention but not wages. Is that a labor-market success? A welfare success? Both?
3. How would you separate “job quality harms mental health” from “poor mental health sorts workers into worse jobs”?
4. Design a paper using treatment-access variation to study mental-health effects on labor supply. What are the biggest threats to interpretation?
5. In what sense can stigma itself be treated as a labor-market institution?

## Reproducibility And Code Lab Note

The Week 4 lab should follow the standard **Reproduce → Diagnose → Transfer** workflow. A bounded Python-first teaching path is preferred. If official replication files are not available locally, use reduced or synthetic data to illustrate:
- mental-health measurement,
- productivity outcomes,
- and identification threats.

## Slide Companion Note

The slide deck should make the following distinctions especially clear:
- mental health as productivity vs welfare object,
- stigma and treatment,
- work affecting mental health,
- measurement and causal challenges,
- frontier research opportunities.

## Bridge Forward

The next week broadens from worker-level and workplace-level mental-health mechanisms to disease exposure, environmental health, and demographic change, where population health shocks and labor-market adjustment interact at larger scale. That transition helps distinguish individual mental-health constraints from aggregate health and population pressures.
