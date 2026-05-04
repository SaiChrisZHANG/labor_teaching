# Week 3 source pack — Dynamic Labor Supply and Lifecycle Responses

## Purpose of this file

This is the intellectual control file for Week 3. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

How do labor-supply choices evolve over time once workers face temporary and permanent wage changes, savings possibilities, adjustment costs, human-capital accumulation, and life-cycle transitions?

## Week identity

- Course: Labor I
- Week: 3
- Length: 3 hours
- Position in sequence: the dynamic continuation of the static benchmark from Week 2
- Goal: move from the static labor-supply model to intertemporal and lifecycle labor supply, clarify what different empirical designs identify, and explain why dynamic adjustment and persistence matter for policy

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. write down and interpret a simple dynamic labor-supply problem with savings and a nonlinear tax schedule;
2. distinguish temporary from permanent wage changes and explain why the distinction is central for identification;
3. interpret the Frisch elasticity as an intertemporal substitution object rather than a generic labor-supply elasticity;
4. explain how lifecycle labor supply interacts with human capital, family timing, and changing constraints;
5. understand why persistence in hours or participation can reflect state dependence, adjustment costs, habit, or slow-moving heterogeneity;
6. connect randomized wage variation, tax timing reforms, lifecycle panel evidence, and structural lifecycle models to the same conceptual backbone.

## Tone and authorial voice

- This chapter should sound like an advanced graduate labor field-course chapter, not a macro primer or a generic dynamic-programming note.
- The opening should explicitly state why the Week 2 static benchmark is not enough for persistent policy changes, lifecycle decisions, or anticipated tax reforms.
- The narrative should emphasize that dynamic labor-supply evidence is valuable precisely because empirical designs often recover different objects.
- Avoid generic phrases like "agents optimize over time." Always tie the dynamic margin to a labor question: hours timing, participation timing, career timing, retirement timing, fertility timing, or tax-policy timing.
- The chapter should make students feel the tension between clean theoretical objects and messy empirical targets.

## Canonical references for Week 3

These are the starter references that should appear in the Week 3 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core theory and lifecycle references

- `@maCurdy1981`
- `@imaiKeane2004`
- `@keane2011`
- `@blundellPistaferriSaportaEksten2016`

### Dynamic evidence and intertemporal substitution references

- `@fehrGoette2007`
- `@chettyFriedmanOlsenPistaferri2011`

### Lifecycle and household/labor-supply evolution references

- `@attanasioLowSanchezMarcos2008`
- `@hokayemZiliak2014`
- `@goldinMitchell2017`

### Bridge back to Week 2 and empirical interpretation

- `@chetty2012`
- `@blundellMaCurdy1999`

## Section-level content requirements

### 1. Opening section: why static labor supply is not enough

This section should make four points immediately:
- many labor-market incentives are dynamic rather than one-shot;
- temporary and permanent wage or tax changes can imply very different responses;
- lifecycle labor supply depends on savings, family timing, human-capital evolution, and health;
- policy evaluation is harder when responses are delayed, smoothed, or state-dependent.

The opening should explicitly connect back to Week 2:
- the Week 2 static first-order condition is still useful;
- but the relevant shadow value of wealth is now dynamic;
- and many empirical designs identify dynamic objects rather than static Marshallian elasticities.

### 2. Dynamic benchmark and intertemporal substitution

This section should define a simple multiperiod labor-supply problem with:
- consumption,
- hours or participation,
- savings or assets,
- nonlinear taxes or net wages.

Minimum content:
- dynamic objective function;
- period budget constraint;
- intratemporal first-order condition;
- intuition for the marginal utility of wealth as an intertemporal state variable;
- why the Frisch elasticity is a conditional object holding the marginal utility of wealth fixed.

This section should also explain the difference between:
- intertemporal substitution,
- wealth effects from persistent wage changes,
- and adjustment/persistence that makes observed short-run responses small.

### 3. Lifecycle labor supply and human-capital interaction

This section should introduce the lifecycle view:
- hours profiles over age;
- participation profiles over age;
- career timing and childbearing timing;
- retirement transitions;
- human capital and wage growth.

Minimum content:
- lifecycle hours or participation profiles as equilibrium objects, not mere descriptive curves;
- why anticipated future wages affect current labor supply;
- why human-capital accumulation blurs the line between labor supply and labor demand of the self.

This section should set up Week 4 by making clear that lifecycle labor-supply models naturally feed into human-capital models.

### 4. What empirical designs identify in dynamic labor supply

This section should organize the evidence by identifying design rather than by paper chronology.

Minimum design buckets:
- randomized temporary wage variation;
- tax reforms or tax timing changes;
- panel variation in wages and hours;
- lifecycle structural estimation.

This section should explain:
- what parameter each design most closely targets;
- why the same policy can produce different short-run and long-run elasticities;
- why Chetty's friction framework still matters here.

### 5. Persistence, state dependence, and adjustment costs

This section should make clear that persistent hours or participation patterns are not automatically preference parameters.

Minimum content:
- adjustment costs;
- fixed costs or entry/exit costs;
- slow learning about tax schedules or returns to work;
- state dependence versus serially correlated heterogeneity.

The chapter should use this section to connect Week 3 to:
- Week 6 household timing,
- Week 11 worker-targeted policy evaluation,
- Week 12 labor supply under frictions.

## Required formal objects

The retrofitted chapter should contain at least three formal objects and cross-reference them.

### Equation 1: dynamic labor-supply problem

Use a compact multiperiod problem. A suitable version is:

```tex
\max_{\{c_t,h_t,a_{t+1}\}_{t=0}^T}
\sum_{t=0}^T \beta^t u(c_t, \bar h-h_t)
\quad \text{s.t.} \quad
 a_{t+1} = (1+r)a_t + y_t + w_t h_t - T_t(w_t h_t, y_t) - c_t
```

Interpretation:
- the static labor-supply problem is nested inside a larger intertemporal choice problem;
- the return to work depends on current incentives and on how current work changes future resources.

### Equation 2: intratemporal condition and Frisch object

Use an intratemporal condition such as:

```tex
\frac{u_{\ell,t}(c_t,\ell_t)}{u_{c,t}(c_t,\ell_t)} = w_t \bigl(1-\tau_t^{m}\bigr)
```

where `\tau_t^{m}` is the marginal tax rate.

Then explain that the Frisch elasticity holds fixed the marginal utility of wealth or its multiplier, so it is not the same object as an uncompensated static elasticity.

### Equation 3: dynamic persistence or adjustment-cost object

Use either a reduced-form dynamic hours equation or an explicit adjustment-cost term. A suitable option is:

```tex
u(c_t,\bar h-h_t) - \Phi(h_t-h_{t-1})
\quad \text{with} \quad
\Phi(h_t-h_{t-1}) = \frac{\kappa}{2}(h_t-h_{t-1})^2
```

Interpretation:
- even if workers would like to reoptimize strongly, observed responses may be damped by adjustment costs or other forms of persistence;
- this helps reconcile small short-run micro responses with larger long-run or macro responses.

## Required figures and tables

The week should have at least two figures and two tables.

### Figure 1 (required): synthetic lifecycle hours or participation profiles

Create a conceptual lifecycle figure that shows age on the horizontal axis and hours or participation on the vertical axis.

Minimum contrasts:
- one high-skill versus low-skill lifecycle profile, or
- one male versus female lifecycle profile, or
- one profile before versus after children arrive.

Figure purpose:
- show that lifecycle labor supply is about timing as much as levels;
- motivate why human capital, fertility, and retirement transitions matter.

This can be synthetic, but the chapter should connect it to one cited empirical source.

### Figure 2 (required): temporary versus permanent wage shock response schematic

Create a stylized dynamic-response figure showing hours responses under:
- a temporary wage shock,
- a permanent wage shock,
- and optionally a temporary wage shock with adjustment frictions.

Figure purpose:
- separate intertemporal substitution from wealth effects and persistence;
- show why empirical design and horizon matter.

### Table 1 (required): shock-response taxonomy

Create a table mapping different shocks to the labor-supply object they identify.

Minimum rows:
- temporary unanticipated wage shock,
- temporary anticipated tax holiday,
- permanent wage change,
- lifecycle wage growth,
- one-time fixed work-cost shock.

Minimum columns:
- shock type,
- likely primary margin,
- parameter most closely targeted,
- major interpretation risk.

### Table 2 (required): empirical-design map

Create a table mapping empirical designs to dynamic-labor-supply objects.

Minimum rows:
- randomized temporary wage variation,
- panel wage-hours variation,
- tax timing or tax reform design,
- lifecycle structural model,
- event-study design around a life transition.

Minimum columns:
- design,
- key identifying variation,
- object learned,
- major threat.

## Required references by section

Minimum expectations:
- opening and dynamic benchmark: `@maCurdy1981`, `@blundellMaCurdy1999`, `@keane2011`
- dynamic empirical interpretation: `@chetty2012`, `@fehrGoette2007`, `@chettyFriedmanOlsenPistaferri2011`
- lifecycle section: `@attanasioLowSanchezMarcos2008`, `@blundellPistaferriSaportaEksten2016`, `@goldinMitchell2017`
- health or lifecycle constraints bridge: `@hokayemZiliak2014`

## Lab anchor

The Week 3 lab should be built around one official replication package and one bounded transfer exercise.

### Primary lab candidate

Use `@fehrGoette2007` because the article has an official AEA/openICPSR replication package and gives students a direct encounter with temporary wage variation and intertemporal substitution.

#### Reproduce

Students should reproduce one reduced-form hours or effort response to randomized wage variation using the official package or a reduced pedagogical subset.

#### Transfer

Students should apply the same design logic to one bounded alternative:
- an alternative subsample,
- an alternative response horizon,
- an alternative outcome margin,
- or a synthetic temporary-shock panel used to test how the estimated response changes when persistence is added.

### Secondary lab candidate

Use `@attanasioLowSanchezMarcos2008` if the goal is to emphasize lifecycle timing and structural interpretation.

#### Reproduce

Students reproduce one lifecycle profile or one simulated cohort comparison from the official replication package.

#### Transfer

Students adapt the profile-building workflow to one bounded alternative:
- alternative cohort split,
- alternative age range,
- alternative family-status subgroup,
- or a small public panel/survey sample used to recreate a simplified lifecycle profile.

### Optional bridge lab candidate

If you want a cleaner link to optimization frictions and micro versus macro elasticities, use `@chettyFriedmanOlsenPistaferri2011` as an optional instructor-led extension rather than the default student lab.

## Slide sync requirements

The slide deck should contain, at minimum:
1. one slide stating the week's central question and why the static benchmark is not enough;
2. one slide with the dynamic labor-supply problem;
3. one slide distinguishing temporary versus permanent wage changes;
4. one slide interpreting the Frisch elasticity;
5. one slide with the lifecycle profile figure;
6. one slide summarizing empirical design differences;
7. one slide on adjustment costs and persistence;
8. one slide previewing the bridge to Week 4 human capital.

## Editing rules

When you want to change Week 3 at the intellectual level, edit this file first.

Typical examples:
- changing whether the chapter leans more toward intertemporal substitution or toward lifecycle labor supply;
- changing the primary lab paper;
- adding or dropping a required formal object;
- changing whether the main empirical contrast is randomized wage variation, tax timing reform, or structural lifecycle evidence;
- changing which persistence mechanism should be emphasized.

After editing this file, ask Codex to sync:
- `books/labor-i/03-dynamic-labor-supply.md`
- `books/labor-i/slides/week3/03-dynamic-labor-supply.tex`
- `books/labor-i/labs/03-dynamic-labor-supply/lab.md`
- `books/labor-i/labs/03-dynamic-labor-supply/src/*`
- any generated figures/tables wired into the chapter or slides.
