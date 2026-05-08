# Week 1 source pack — Labor Demand and Production

## Purpose of this file

This is the intellectual control file for Labor II Week 1. Edit this file first when changing the chapter's scholarly spine. Then ask Codex to sync the chapter, slides, and code lab from this source pack.

## Central question

How do firms choose labor input in a static production setting, and how do technology, substitution possibilities, labor's cost share, and output demand jointly determine labor demand elasticities?

## Week identity

- Course: Labor II
- Week: 1
- Length: 3 hours core, with an optional 45--60 minute extension block if you want to spend more time on rent sharing, payroll-tax incidence, or empirical estimation choices
- Position in sequence: opening week of Labor II; first firm-side week after the worker-side architecture of Labor I
- Goal: reorient students from worker behavior to firm optimization, teach the static labor-demand benchmark cleanly, and set up Week 2 on dynamic adjustment costs

## Why this week comes first

Labor II begins inside the firm. The worker-side course asked how workers choose, invest, sort, and respond to policy. Labor II starts by asking the corresponding firm-side question: how much labor does the firm want to hire, and what objects govern that choice?

This week should make three transitions explicit:
- from **worker decisions** to **firm input demand**;
- from **partial worker-side responses** to **firm-side comparative statics**;
- from **price-taking textbook intuition** to **modern empirical labor demand**, where output demand, local shocks, firm heterogeneity, and institutional wedges matter.

It should also make clear what is deliberately *not* in scope yet:
- no dynamic adjustment costs yet (Week 2),
- no internal incentive design yet (Week 3),
- no search, bargaining, or monopsony yet (Weeks 4--6).

## Non-negotiable learning goals

By the end of the week, students should be able to:
1. write down and solve a static cost-minimization problem with labor and at least one other input;
2. distinguish clearly between the **production function**, **cost function**, **conditional factor demand**, and **unconditional labor demand**;
3. explain the difference between **conditional labor demand elasticities** and **total labor demand elasticities**;
4. interpret the Hicks--Marshall laws of derived demand using labor share, product demand elasticity, and the ease of substitution;
5. explain why short-run and long-run labor demand differ even in a static comparative-statics lecture;
6. connect payroll-tax or cost-shock evidence to static labor-demand and incidence logic;
7. understand what modern empirical papers are actually estimating when they report labor-demand elasticities.

## Tone and authorial voice

- This chapter should sound like the opening week of a PhD labor field course, not like a generic micro theory note.
- It should explicitly connect Labor I to Labor II in the opening pages.
- The theory should be crisp and compact: production, duality, conditional demand, scale and substitution, Hicks--Marshall.
- The empirical section should emphasize that estimated labor-demand elasticities depend on the **margin observed**, the **source of variation**, the **time horizon**, and the **product-market environment**.
- The chapter should avoid drifting into wage-setting, search, or full monopsony analysis; those belong later in Labor II.
- Still, it should foreshadow those later topics by explaining why the static benchmark is often too simple for modern labor markets.

## Canonical references for Week 1

These are the starter references that should appear in the Week 1 chapter, slides, or lab. Use citation keys from `shared/bibliography/references.bib`.

### Core benchmark references

- [@hicks1932]
- [@hamermesh1993]
- [@acemogluAutor2011]

### Core empirical and modern labor-demand references

- [@beaudryGreenSand2018]
- [@saezSchoeferSeim2019]
- [@buttersSacksSeo2022]
- [@cardCardosoHeiningKline2018]

## Section-level content requirements

### 1. Opening: why Labor II begins with labor demand

This section must:
- remind students that Labor I mainly studied workers, households, policy, and worker-side frictions;
- state that Labor II begins by embedding labor markets inside the firm's production and cost problem;
- explain why labor-demand elasticities matter for policy incidence, wage-setting, employment responses, and later equilibrium reasoning.

The opening should explicitly preview:
- Week 2: dynamic labor demand and adjustment costs;
- Week 5: wage-setting and bargaining;
- Week 6: monopsony and labor market power.

### 2. Production, marginal products, and the static firm problem

This is the theoretical backbone of the week.

Minimum content:
- define a production function with labor and at least one other factor;
- distinguish output maximization from cost minimization;
- introduce labor demand as a **derived demand**;
- explain why labor demand depends on technology, factor prices, and output demand.

This section should stay close to economic objects students will use later:
- marginal product of labor,
- labor share,
- substitution possibilities,
- product demand.

### 3. Conditional factor demand and cost minimization

This section should teach the static duality logic cleanly.

Minimum content:
- solve the firm's cost-minimization problem conditional on output;
- define conditional labor demand;
- explain why conditional demand isolates substitution across inputs holding output fixed;
- make clear why this is not the same as the observed employment response to a wage or tax shock.

This section should connect conditional labor demand to the elasticity of substitution and labor's cost share.

### 4. Unconditional labor demand and the Hicks--Marshall laws

This section is the conceptual center of the lecture.

Minimum content:
- define total labor demand as allowing output to adjust;
- decompose total labor demand into a substitution effect and a scale effect;
- teach the Hicks--Marshall laws in plain language;
- explain why the elasticity of product demand and labor's share matter for the total response.

This section should make students comfortable moving between:
- production-side comparative statics,
- cost duality,
- and labor-policy intuition.

### 5. Short run versus long run in a "static" lecture

This section should explain why the static benchmark still contains different effective horizons.

Minimum content:
- fixed capital versus variable capital;
- short-run versus long-run substitution possibilities;
- why long-run labor demand is usually more elastic;
- why empirical elasticities depend on the time window and margin studied.

This is also the right place to note that Week 2 will endogenize adjustment speed formally.

### 6. Empirical labor-demand designs: what do they identify?

Organize this section by identification strategy, not chronology.

Minimum design buckets:
- payroll-tax or labor-cost reforms;
- local or industry demand shocks;
- product-market cost shocks;
- matched employer-employee rent-sharing evidence;
- cross-city or city-industry labor-demand estimation.

For each design, the chapter should say:
- what varies,
- what employment/wage margin is observed,
- which elasticity or incidence object is being estimated,
- and what the main limitation is.

### 7. Static labor demand and policy interpretation

This section should explain why the week matters for real policy work.

Minimum content:
- payroll taxes and statutory incidence versus economic incidence;
- labor-demand elasticities and the effects of wage subsidies or payroll-tax cuts;
- why firm heterogeneity and product-market conditions matter for policy pass-through;
- why static labor demand is necessary but not sufficient for later weeks on wage-setting and institutions.

### 8. Optional extension block

This chapter should have an explicit optional extension block that can be used in one of three ways:
- taught as an extra 45--60 minute session,
- assigned as reading plus the lab,
- or turned into appendix slides.

The extension block should cover one or both of:
- rent sharing and the boundary between static labor demand and wage-setting;
- richer product-market links, including local cost shocks and pass-through.

## Required formal objects

The chapter should contain at least four formal objects and cross-reference them.

### Equation 1: production function

Use a compact technology such as

```tex
q = F(L, K; A)
```

Interpretation:
- labor demand is derived from production;
- technology and factor substitutability are primitive objects.

### Equation 2: static first-order condition / cost minimization condition

Use either a profit-maximization condition or a cost-minimization condition such as

```tex
p \frac{\partial F(L,K;A)}{\partial L} = w
```

or the MRTS condition for the cost-minimization problem.

Interpretation:
- firms hire labor up to the point where the value of the marginal product matches the marginal labor cost.

### Equation 3: conditional labor-demand elasticity under constant returns

Use a compact elasticity object such as

```tex
\eta^{c}_{LL} = -(1-s_L)\sigma
```

where {math}`s_L` is labor's cost share and {math}`\sigma` is the elasticity of substitution between labor and capital.

Interpretation:
- conditional demand isolates substitution holding output fixed;
- labor share and substitutability matter immediately.

### Equation 4: total labor-demand elasticity with scale and substitution

Use a decomposition such as

```tex
\eta_{LL} = -(1-s_L)\sigma - s_L\eta
```

where {math}`\eta` is the absolute value of product-demand elasticity.

Interpretation:
- total demand is more elastic when substitution is easier and output demand is more elastic;
- this is the clean route into the Hicks--Marshall laws.

### Equation 5: payroll-tax wedge / effective labor cost

Use a compact incidence object such as

```tex
c_L = (1+\tau)w
```

or an equivalent relation inside the first-order condition.

Interpretation:
- payroll taxes shift effective labor costs;
- the employment response depends on labor demand and whatever labor-supply or wage-setting environment the firm faces.

## Required figures and tables

The chapter should include at least four figures and three tables.

### Figures

1. `assets/figures/01-static-labor-demand-isoquant-isocost.png`
   - isoquant/isocost diagram with optimum
2. `assets/figures/01-conditional-vs-unconditional-demand.png`
   - conditional vs total labor-demand curves or comparative-statics schematic
3. `assets/figures/01-hicks-marshall-laws.png`
   - schematic showing how substitution, labor share, and product-demand elasticity affect own-wage demand elasticity
4. `assets/figures/01-payroll-tax-incidence.png`
   - static incidence schematic or employment response to payroll-tax/labor-cost wedge

### Tables

1. `assets/tables/01-elasticity-taxonomy.md`
   - conditional vs unconditional demand, short run vs long run, own- vs cross-price objects
2. `assets/tables/01-design-map.md`
   - empirical designs and what they identify
3. `assets/tables/01-policy-incidence-map.md`
   - common policy/cost shocks and the relevant labor-demand objects

## Reading ladder guidance

The chapter should end with a real reading ladder.

### Core reading ladder

- [@hamermesh1993]
- [@beaudryGreenSand2018]
- [@saezSchoeferSeim2019]

### Supporting/extension ladder

- [@buttersSacksSeo2022]
- [@cardCardosoHeiningKline2018]
- [@acemogluAutor2011]

The reading ladder should say explicitly:
- what is benchmark theory,
- what is modern empirical labor demand,
- and what foreshadows later weeks on wage-setting, rent sharing, and labor market power.

## Research-lab expectations

This week's Research Lab should do three things:
1. teach students to map a source of variation into a labor-demand object;
2. show why estimated labor-demand elasticities are not one-size-fits-all;
3. preview how later weeks add frictions, bargaining, and institutional wedges.

Good research-lab questions include:
- Which empirical designs identify conditional rather than total demand?
- When is a payroll-tax estimate informative about labor demand and when is it also informative about wage-setting?
- How do product-market conditions change what a local labor-cost shock means?

## Code-lab design

Keep the standard **Reproduce -> Diagnose -> Transfer** structure.

### Primary lab anchor

- [@beaudryGreenSand2018]

Rationale:
- directly about labor demand;
- official AEA page and replication package exist;
- easy to translate into a reduced pedagogical city-industry or industry panel exercise.

### Secondary / challenge anchor

- [@saezSchoeferSeim2019]

Rationale:
- excellent for static labor-demand and incidence intuition;
- sharp policy variation;
- natural bridge to the policy and wage-setting weeks.

### Optional extension anchor

- [@buttersSacksSeo2022]

Rationale:
- strong product-market/cost-shock perspective;
- helps explain why labor demand depends on how product markets absorb shocks.

The bounded student path should run without confidential data and should ideally let students:
- estimate a simple labor-demand relationship in synthetic or public panel data,
- compare conditional vs total response logic,
- and compute a scale/substitution decomposition in a stylized environment.

## Explicit bridge to Week 2

End the chapter by stating:
- static labor demand tells us where firms want to be after a shock;
- Week 2 asks why they often do not get there immediately.

That bridge should be a real closing section, not a throwaway sentence.
