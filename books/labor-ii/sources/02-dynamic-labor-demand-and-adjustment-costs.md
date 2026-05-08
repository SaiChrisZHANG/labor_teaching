# Week 2 source pack — Dynamic Labor Demand and Adjustment Costs

## Purpose of this file

This is the intellectual control file for Labor II Week 2. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

Why do firms adjust employment slowly after shocks, what kinds of adjustment costs generate persistence and inaction, and how should labor economists identify dynamic labor-demand frictions in data?

## Week identity

- Course: Labor II
- Week: 2
- Length: 3 hours core, with an optional 45--60 minute extension block if you want to spend more time on fixed versus convex adjustment costs, uncertainty, or structural estimation
- Position in sequence: second firm-side week of Labor II; follows the static benchmark of Week 1 and precedes Week 3 on personnel economics and internal labor markets
- Goal: move from static labor demand to dynamic firm adjustment, explain why employment responds gradually, and establish the empirical logic economists use to separate persistence from true adjustment frictions

## Why this week comes second

Week 1 gave the static benchmark: labor demand as a derived demand from technology, costs, and output demand. Week 2 asks why that benchmark does not immediately map into observed employment paths. Firms do not usually jump frictionlessly to the new optimum. Hiring, firing, reorganizing production, and changing hours are costly and often lumpy.

This week should make four transitions explicit:
- from **static comparative statics** to **dynamic adjustment**;
- from **target employment** to **observed employment paths**;
- from **one labor margin** to **multiple adjustment margins** such as hours, heads, hiring, firing, and vacancies;
- from **reduced-form elasticity language** to **dynamic identification and structural interpretation**.

It should also make clear what is deliberately *not* in scope yet:
- no full internal incentive design yet (Week 3),
- no search-and-matching equilibrium yet (Week 4),
- no bargaining or monopsony yet (Weeks 5--6).

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. explain why employment can remain away from its static target when adjustment is costly;
2. distinguish clearly between **convex adjustment costs**, **fixed/nonconvex adjustment costs**, and **quasi-fixed labor**;
3. connect employment persistence to underlying frictions rather than treating all serial correlation as evidence of costs;
4. explain why firms may use different margins -- hours, overtime, headcount, hiring, separations, vacancies, temporary labor -- before changing permanent employment;
5. interpret dynamic labor-demand evidence using the language of state dependence, inaction regions, and partial adjustment;
6. distinguish what different empirical designs identify: timing responses, hazard responses, structural cost parameters, or policy incidence paths;
7. understand why adjustment frictions matter for labor policy, including payroll taxes, employment protection, and labor-cost shocks.

## Tone and authorial voice

- This chapter should sound like a PhD field-course continuation of Week 1, not a macro note in disguise.
- It should begin from the static labor-demand target and then show why actual employment paths differ.
- The theory should be crisp and cumulative: target employment, state variables, convex versus nonconvex costs, and observed adjustment margins.
- The empirical section should emphasize that slow employment adjustment may reflect true costs, time aggregation, uncertainty, managerial inertia, or the availability of alternative margins.
- The chapter should remain firmly on the firm side. Search, bargaining, and market power should only appear as foreshadowing.

## Canonical references for Week 2

These are the starter references that should appear in the Week 2 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core benchmark references

- [@nickell1986]
- [@shapiro1986]
- [@hamermesh1989]

### Dynamic adjustment and friction references

- [@bentolilaBertola1990]
- [@caballeroEngelHaltiwanger1997]
- [@dibiasiMikoschSarferaz2025]

### Policy-timing bridge reference

- [@saezSchoeferSeim2019]

## Section-level content requirements

### 1. Opening: from static targets to dynamic paths

This section must:
- remind students that Week 1 derived the firm's static target labor demand;
- state that Week 2 explains why firms do not jump immediately to that target;
- define the object of interest as the *path* of adjustment, not just the comparative static.

The opening should explicitly preview:
- Week 3: internal labor markets and personnel choices;
- Week 4: search, turnover, and unemployment flows;
- later policy lectures where adjustment timing changes incidence and welfare.

### 2. Target employment and the dynamic firm problem

This is the conceptual backbone of the week.

Minimum content:
- define desired or target employment relative to the static benchmark;
- explain why dynamic choice depends on both current state and future payoffs;
- introduce the idea that labor may be quasi-fixed even when output and wages move.

This section should use labor-market language students can carry forward:
- target versus actual employment,
- state dependence,
- persistence,
- adjustment margin,
- quasi-fixed labor.

### 3. Convex adjustment costs and partial adjustment

This section should teach the most standard dynamic benchmark cleanly.

Minimum content:
- write a dynamic problem with quadratic or otherwise convex costs of changing employment;
- derive or explain a partial-adjustment representation;
- show why convex costs smooth employment responses over time;
- explain the meaning of a speed-of-adjustment parameter.

This section should make clear what convex costs imply:
- frequent but small changes,
- smooth responses,
- gradual incidence of policy shocks.

### 4. Fixed / nonconvex costs, inaction, and lumpiness

This section should explain why firms may adjust rarely but by a lot.

Minimum content:
- define fixed or nonconvex adjustment costs;
- explain inaction regions and lumpy adjustments;
- distinguish these patterns from the convex-cost benchmark;
- connect to establishment-level micro evidence and hazard-style adjustment patterns.

This is the right place to emphasize:
- micro lumpiness can coexist with smoother aggregate adjustment,
- observed inaction can reflect both costs and uncertainty.

### 5. Which margin adjusts first? Hours, heads, hiring, firing, and labor hoarding

This section should link theory to observable labor-market margins.

Minimum content:
- distinguish changes in hours from changes in headcount;
- distinguish hiring margins from separation margins;
- explain why firms may hoard labor after temporary shocks;
- discuss the measurement consequences of using employment rather than hours or vacancies.

This section should be explicit that the observed elasticity depends on:
- the margin measured,
- the horizon,
- and the firm's other available responses.

### 6. Empirical designs: what do they identify?

Organize this section by identification strategy, not by a chronological literature review.

Minimum design buckets:
- plant or establishment panels and employment dynamics;
- payroll-tax or labor-cost reforms with dynamic timing;
- uncertainty shocks and expectation-based evidence;
- structural dynamic estimation;
- event-study designs that trace adjustment paths.

For each design, the chapter should say:
- what varies,
- what labor margin is observed,
- what dynamic object is estimated,
- and what the main threat to interpretation is.

### 7. Dynamic labor demand and policy timing

This section should explain why adjustment frictions matter for policy interpretation.

Minimum content:
- why employment effects may build over time rather than appear immediately;
- how adjustment costs alter the timing of payroll-tax incidence;
- why short-run and long-run policy effects differ even with the same eventual target;
- how firing costs and employment protection can change both the level and timing of response.

This is also the right place to connect back to Labor I:
- worker-side adjustment costs and frictions matter,
- but now firm-side timing and margin choices are central.

### 8. Optional extension block

This chapter should have an explicit optional extension block that can be used in one of three ways:
- taught as an extra 45--60 minute session,
- assigned as reading plus the lab,
- or turned into appendix slides.

The extension block should cover one or both of:
- uncertainty and real-options style delays in labor adjustment;
- structural estimation of adjustment-cost parameters and the mapping from micro evidence to aggregate dynamics.

## Required formal objects

The chapter should contain at least four formal objects and cross-reference them.

### Equation 1: target employment or static benchmark

Use a compact notation for the static target such as

```tex
L_t^{\ast} = L^{\ast}(w_t, p_t, K_t, A_t, q_t)
```

Interpretation:
- Week 1 delivered the target;
- Week 2 explains why observed employment {math}`L_t` may not equal {math}`L_t^{\ast}`.

### Equation 2: dynamic objective with adjustment costs

Use a Bellman-style or discounted-profit object such as

```tex
V(L_{t-1}, s_t) = \max_{L_t} \left\{ \pi(L_t, s_t) - C(L_t-L_{t-1}) + \beta E_t[V(L_t, s_{t+1})] \right\}
```

Interpretation:
- dynamic labor demand depends on both current profits and future consequences;
- the cost function {math}`C(\cdot)` is the central week-2 object.

### Equation 3: convex-cost example / partial-adjustment law

Use a quadratic-cost implication such as

```tex
L_t - L_{t-1} = \lambda \left(L_t^{\ast} - L_{t-1}\right)
```

with {math}`0 < \lambda \le 1`.

Interpretation:
- convex costs imply gradual adjustment;
- {math}`\lambda` is a reduced-form speed-of-adjustment object, not itself a primitive.

### Equation 4: nonconvex-cost intuition / inaction threshold

Use a compact threshold-style object such as

```tex
\text{adjust if } \left|L_t^{\ast} - L_{t-1}\right| > \bar{\Delta}
```

Interpretation:
- fixed or nonconvex costs generate inaction bands and lumpy adjustment;
- this helps students connect the theory to establishment-level spikes and zeros in adjustment.

### Equation 5: policy timing object

Use a dynamic response expression such as

```tex
\frac{\partial L_{t+h}}{\partial \tau_t}
```

Interpretation:
- policy incidence and employment effects are dynamic objects;
- the horizon {math}`h` matters for both interpretation and welfare.

## Candidate figures and tables

The chapter should include at least four figures and three tables.

### Candidate figures to create or refine

1. `assets/figures/02-target-vs-actual-employment.png`
   - target employment versus actual employment after a shock
2. `assets/figures/02-convex-vs-nonconvex-adjustment.png`
   - smooth partial adjustment versus inaction/lumpiness
3. `assets/figures/02-hours-vs-headcount-adjustment.png`
   - alternative margins of adjustment over time
4. `assets/figures/02-policy-incidence-over-time.png`
   - short-run versus long-run employment response to a labor-cost shock

### Required tables

1. `assets/tables/02-adjustment-cost-taxonomy.md`
2. `assets/tables/02-design-map.md`
3. `assets/tables/02-observed-margins-map.md`

## Reading ladder expectations

The reading ladder should be organized in four buckets.

### Bucket A: dynamic benchmark
- [@nickell1986]
- [@shapiro1986]
- [@hamermesh1989]

### Bucket B: adjustment frictions and firing costs
- [@bentolilaBertola1990]
- [@caballeroEngelHaltiwanger1997]

### Bucket C: modern empirical measurement of adjustment frictions
- [@dibiasiMikoschSarferaz2025]

### Bucket D: policy timing and incidence bridge
- [@saezSchoeferSeim2019]

## Lab design requirements

The week's code lab should follow the established Reproduce -> Diagnose -> Transfer format.

### Primary lab anchor
- [@dibiasiMikoschSarferaz2025]

### Secondary / challenge anchor
- [@caballeroEngelHaltiwanger1997]

### Optional extension anchor
- [@saezSchoeferSeim2019]

### Lab logic

The lab should teach three things:
1. how economists infer adjustment frictions from dynamic responses rather than one-shot elasticities;
2. how the observed response changes when the margin is hours versus headcount;
3. how a bounded simulated or public-data exercise can transfer the paper's logic without requiring confidential firm microdata.

The bounded student path must run locally without confidential microdata. A pedagogical simulation or reduced public-data path is acceptable if the original paper's full replication package is not practical for teaching.

## What this week should leave students with

By the end of the week, students should be able to say:

- Week 1 told us where the firm wants to be.
- Week 2 tells us why the firm does not get there immediately.
- Week 3 will ask how firms organize workers internally while living with those adjustment frictions.
