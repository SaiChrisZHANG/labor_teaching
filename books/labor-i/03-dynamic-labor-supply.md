---
bibliography:
  - ../../shared/bibliography/references.bib
---

# Dynamic Labor Supply and Lifecycle Responses

## Learning objectives

By the end of Week 3, students should be able to:

1. write down a dynamic labor-supply problem with savings and a nonlinear tax schedule;
2. explain why temporary and permanent wage changes identify different labor-supply objects;
3. interpret the Frisch elasticity as an intertemporal substitution object rather than a generic elasticity;
4. connect lifecycle hours and participation profiles to human capital, family timing, and health;
5. distinguish persistence driven by state dependence or adjustment costs from persistence driven by slow-moving heterogeneity;
6. explain why dynamic evidence from experiments, panel variation, tax reforms, and lifecycle structural models should not be forced into one elasticity number.

The economic question for the week is direct: once work decisions are linked across periods through savings, anticipated wages, taxes, and changing constraints, what exactly does labor-supply evidence identify?

## Bridge

Week 2 gave the static first-order condition that maps the net-of-tax wage into a contemporaneous labor-leisure tradeoff. That benchmark remains useful, but it is no longer sufficient once incentives are dynamic. Workers do not encounter taxes, wages, childbearing, health shocks, or retirement decisions as one-shot events. They face timing problems. A temporary bonus today is not the same object as a permanent wage increase, and an anticipated tax holiday is not the same object as an unexpected shift in labor demand [@blundellMaCurdy1999; @keane2011].

The reason is simple but important. In a dynamic environment, current work changes not only current consumption but also assets, future labor choices, and sometimes future wages. The shadow value of wealth is therefore an intertemporal state variable rather than a static constant. That is why dynamic labor-supply evidence is valuable and hard to read at the same time: different designs load differently on intertemporal substitution, wealth effects, and persistence [@maCurdy1981; @chetty2012].

### Dynamic benchmark

The clean benchmark extends Week 2 by letting the worker choose consumption, hours, and savings over time:

```{math}
:label: eq-week3-dynamic-problem
\max_{\{c_t,h_t,a_{t+1}\}_{t=0}^T}
\sum_{t=0}^T \beta^t u(c_t,\bar h-h_t)
\quad \text{s.t.} \quad
a_{t+1} = (1+r)a_t + y_t + w_t h_t - T_t(w_t h_t,y_t) - c_t.
```

Equation {eq}`eq-week3-dynamic-problem` nests the static problem inside a larger intertemporal choice problem. Hours {math}`h_t` still trade off against leisure, but the payoff to current work depends on how the worker values future resources. That is the sense in which Week 2 survives inside Week 3: the static condition remains on the page, but its interpretation changes because the relevant marginal utility of wealth is now dynamic [@maCurdy1981; @blundellMaCurdy1999].

If the worker is interior within the period, the intratemporal condition can still be written as

```{math}
:label: eq-week3-frisch
\frac{u_{\ell,t}(c_t,\ell_t)}{u_{c,t}(c_t,\ell_t)} = w_t \bigl(1-\tau_t^m\bigr),
\qquad \ell_t = \bar h - h_t.
```

Equation {eq}`eq-week3-frisch` looks familiar, but the empirical interpretation is not the same as in Week 2. The Frisch elasticity is the response of hours to a wage change holding fixed the marginal utility of wealth, or equivalently the multiplier on the intertemporal budget constraint. It is therefore a conditional intertemporal substitution object, not the same thing as a static uncompensated elasticity [@maCurdy1981; @keane2011].

That distinction matters immediately for temporary versus permanent wage changes. A temporary high wage mainly changes the relative price of leisure across dates, so the clean prediction emphasizes retiming of work effort toward the high-wage period. A permanent wage increase instead brings both substitution and wealth effects, which is why it cannot be read as a pure Frisch object. Once observed responses are small, we still need one more question: is the true substitution motive weak, or are adjustment frictions muting what we see [@fehrGoette2007; @chetty2012]?

```{figure} assets/figures/03-temporary-permanent-shock-responses.png
:name: fig-week3-shocks
Stylized hours responses to temporary and permanent wage changes. The temporary shock produces a sharper short-run response because it mainly loads on intertemporal substitution. The permanent shock mixes substitution and wealth effects, while adjustment frictions smooth the measured response even when the incentive change is immediate. The figure is conceptual but organized around the distinctions emphasized in @fehrGoette2007, @chetty2012, and @chettyFriedmanOlsenPistaferri2011.
```

Figure {numref}`fig-week3-shocks` summarizes the central Week 3 intuition. Horizon and anticipation are not details to append after estimating an elasticity. They are part of the estimand itself.

## Field Core

### Lifecycle labor supply and the bridge to human capital

The lifecycle view asks workers to choose not only how much to work, but when. Hours and participation profiles over age are equilibrium objects shaped by wages, assets, family timing, health, and anticipated future returns to work. A rising wage path early in life can raise current labor supply because experience accumulation makes current hours more valuable tomorrow. That is why the line between labor supply and human-capital investment begins to blur in dynamic models [@imaiKeane2004; @attanasioLowSanchezMarcos2008].

This is the crucial bridge into Week 4. Once current work affects future wages through learning-by-doing or experience accumulation, labor supply is no longer only about trading leisure for consumption. It also becomes a decision about when to invest in one's own productive capacity. Human capital is therefore not a separate topic pasted onto labor supply later in the course; it is already latent inside lifecycle work decisions [@imaiKeane2004; @goldinMitchell2017].

```{figure} assets/figures/03-lifecycle-labor-supply-profiles.png
:name: fig-week3-lifecycle
Synthetic lifecycle labor-supply profiles. The profiles are schematic rather than data-cleaned estimates, but they are built to highlight the timing logic in lifecycle labor supply: early-career wage growth can raise hours through future returns, family transitions can create mid-career divergence, and later-life hours reflect both incentives and health or retirement constraints. The motivating empirical backdrop comes from @attanasioLowSanchezMarcos2008, @goldinMitchell2017, and @hokayemZiliak2014.
```

Figure {numref}`fig-week3-lifecycle` should be read as a timing map rather than as a descriptive fact to memorize. Female lifecycle employment profiles changed because wages, fertility timing, and household organization changed, not because one static preference parameter was suddenly different [@attanasioLowSanchezMarcos2008; @goldinMitchell2017]. Health also enters the same lifecycle problem by changing both the utility cost of work and the returns to remaining attached [@hokayemZiliak2014].

Blundell, Pistaferri, and Saporta-Eksten show why the family dimension matters for dynamic interpretation. Consumption smoothing and family labor supply jointly determine whether wage risk turns into hour adjustment, spousal adjustment, or asset decumulation [@blundellPistaferriSaportaEksten2016]. That makes lifecycle labor supply empirically inseparable from household structure even before Labor I reaches the dedicated family module.

### What dynamic empirical designs identify

The literature is easiest to organize by identifying design rather than chronology.

```{include} assets/tables/03-shock-taxonomy.md
```

Table {numref}`tbl:week3-shocks` is the shortest route from incentive change to target parameter. A temporary unanticipated wage shock is closest to a Frisch or intertemporal substitution response. A permanent wage change mixes substitution and wealth effects. A fixed work-cost shock is often primarily extensive-margin. Lifecycle wage growth is informative about timing but is not a clean primitive unless human capital and family transitions are modeled explicitly [@keane2011; @chetty2012].

```{include} assets/tables/03-design-map.md
```

Table {numref}`tbl:week3-designs` turns that logic into an evidence map. Randomized temporary wage variation, such as the experiment in @fehrGoette2007, is attractive because it isolates short-run substitution incentives. Tax timing reforms or nonlinear schedule changes are useful because they create horizon-specific changes in the net reward to work, but anticipation and salience matter immediately [@chetty2012]. Panel wage-hours variation can recover dynamic reduced-form responses, yet only after taking wage endogeneity and serial correlation seriously [@maCurdy1981]. Structural lifecycle models ask more of the reader, but they are often the only way to carry savings, family timing, and human-capital accumulation into policy counterfactuals [@attanasioLowSanchezMarcos2008; @keane2011].

The practical teaching lesson is that two papers can disagree numerically without disagreeing economically. One may target short-run intertemporal substitution. Another may target a long-run policy response after assets, spouses, fertility, and experience have adjusted. Dynamic labor supply becomes useful precisely when we stop forcing those objects into one statistic.

### Persistence, state dependence, and adjustment costs

Observed hours often move more slowly than the clean frictionless benchmark suggests. That is not evidence by itself that preferences are flat. It may instead reflect work-schedule rigidities, participation costs, information frictions, institutional constraints, or genuine state dependence in habits and attachment [@chetty2012; @chettyFriedmanOlsenPistaferri2011].

One transparent way to formalize this point is to add an adjustment-cost term:

```{math}
:label: eq-week3-adjustment
\tilde u_t
= u(c_t,\bar h-h_t) - \Phi(h_t-h_{t-1}),
\qquad
\Phi(h_t-h_{t-1}) = \frac{\kappa}{2}(h_t-h_{t-1})^2.
```

Equation {eq}`eq-week3-adjustment` says that changing hours is itself costly. Even when Equation {eq}`eq-week3-frisch` suggests a strong contemporaneous incentive to reoptimize, a large {math}`\kappa` slows the observed response. That interpretation is central to the micro-versus-macro elasticity discussion in @chettyFriedmanOlsenPistaferri2011. Short-run administrative or firm-level data may reveal limited immediate adjustment even when longer-run responses after renegotiation or job mobility are larger.

The same logic keeps Week 3 connected to later parts of the course. Adjustment costs and entry-exit costs forecast the household timing issues of Week 6, the horizon problems in Week 11 policy evaluation, and the broader friction-based interpretation of Week 12. Persistence in hours or participation is therefore not a nuisance pattern to difference away. It is itself part of the labor-supply problem.

## Research Lab

The frontier challenge is not writing down a dynamic problem. It is deciding which margins need to be in the model before the counterfactual becomes credible. The more the labor-supply path depends on family timing, health, or human-capital accumulation, the less informative a one-period elasticity will be for persistent policy design [@attanasioLowSanchezMarcos2008; @hokayemZiliak2014].

This is why dynamic evidence is both powerful and fragmented. Randomized temporary wage variation gives clean leverage on intertemporal substitution but says less about lifecycle family labor supply. Lifecycle structural estimation can speak to richer policy questions but imports stronger assumptions. Tax timing designs sit in the middle: close to policy, but often vulnerable to anticipation, salience, and schedule complexity [@fehrGoette2007; @chetty2012].

The open research agenda follows directly. Which persistence is structural and which is institutional? When do household responses amplify or mute worker-level substitution? Which dynamic objects transport across occupations, countries, or tax systems? Those are the questions that carry Week 3 forward into human capital, family labor supply, and worker-side policy evaluation.

## Methods Box

Week 3 adds one discipline to the Week 2 workflow: identify the horizon before interpreting the estimate.

1. Write the dynamic problem and identify the state variables, especially assets and lagged labor-market choices.
2. Ask whether the design changes the wage temporarily, permanently, or in an anticipated way.
3. Decide whether the estimate is closest to a Frisch object, a mixed substitution-and-wealth object, or a persistence object.
4. Check whether lifecycle features such as experience, family timing, or health make current labor supply affect future opportunities.
5. Interpret small short-run responses against Equations {eq}`eq-week3-frisch` and {eq}`eq-week3-adjustment` before concluding that labor supply is inelastic.

## Reading ladder

### Bridge

- MaCurdy on labor supply in a lifecycle setting and the original Frisch logic [@maCurdy1981]
- Blundell and MaCurdy on how static, intertemporal, and lifecycle labor-supply objects differ [@blundellMaCurdy1999]

### Field Core

- Keane's survey on taxes, dynamic labor supply, and why elasticity definitions matter [@keane2011]
- Fehr and Goette on randomized temporary wage variation and short-run intertemporal substitution [@fehrGoette2007]
- Attanasio, Low, and Sanchez-Marcos on lifecycle female labor supply and the role of changing returns and family timing [@attanasioLowSanchezMarcos2008]
- Chetty, Friedman, Olsen, and Pistaferri on adjustment costs and micro versus macro elasticities [@chettyFriedmanOlsenPistaferri2011]

### Research Lab

- Imai and Keane on intertemporal labor supply with human-capital accumulation [@imaiKeane2004]
- Blundell, Pistaferri, and Saporta-Eksten on consumption risk and family labor supply [@blundellPistaferriSaportaEksten2016]
- Goldin and Mitchell on changing lifecycle employment profiles [@goldinMitchell2017]
- Hokayem and Ziliak on health, human capital, and lifecycle labor supply [@hokayemZiliak2014]
- Chetty on how optimization frictions reconcile different elasticity estimates [@chetty2012]

## Exercises / discussion prompts

1. Use Equations {eq}`eq-week3-dynamic-problem` and {eq}`eq-week3-frisch` to explain why a temporary wage shock is closer to a Frisch experiment than a permanent wage increase.
2. Figure {numref}`fig-week3-shocks` shows a muted short-run response under adjustment frictions. What empirical patterns would help you distinguish a high adjustment cost from a low underlying substitution motive?
3. In Figure {numref}`fig-week3-lifecycle`, why can a hump-shaped hours profile reflect changing returns to work rather than changing tastes for leisure alone?
4. Pick one row from Table {numref}`tbl:week3-designs` and explain what policy question it can answer well and what policy question it answers poorly.
5. How does the Week 3 dynamic interpretation change the way you would read static tax-reform evidence from Week 2?

## Reproducibility or code lab note

The Week 3 lab is built around a bounded pedagogical version of @fehrGoette2007. Students reproduce one reduced-form response to randomized temporary wage variation using local synthetic shift-level data, diagnose whether that response is best read as intertemporal substitution or something broader, and then transfer the workflow to a persistence comparison that contrasts low- and high-adjustment-cost environments. The optional lifecycle extension uses @attanasioLowSanchezMarcos2008 as the conceptual bridge from short-run experimental variation to lifecycle profile construction. The bounded path and smoke test are documented in [labs/03-dynamic-labor-supply/lab.md](labs/03-dynamic-labor-supply/lab.md).

## Slide companion note

The Week 3 deck should isolate the dynamic problem, the Frisch interpretation, the temporary-versus-permanent distinction, the lifecycle profile, the design map, and the adjustment-cost bridge to Week 4 rather than duplicating the chapter. The canonical source is [slides/week3/03-dynamic-labor-supply.tex](slides/week3/03-dynamic-labor-supply.tex).
