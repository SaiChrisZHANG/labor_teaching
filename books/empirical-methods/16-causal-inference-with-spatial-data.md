# Lecture 16. Causal Inference With Spatial Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. distinguish when geography is the source of identification, a threat to inference, or the mechanism itself;
2. explain how spatial clustering, spillovers, sorting, MAUP, and correlated local shocks change causal claims;
3. write and interpret exposure mappings for spatial interference;
4. implement the basic logic of Conley-style spatial inference, border comparisons, spatial RD, and shift-share exposure designs;
5. connect each major spatial identification problem to a paper that can serve as a design template;
6. design a student-scale spatial causal inference lab with clear counterfactuals, diagnostics, and reproducibility limits.

## Opening Orientation

Lecture 15 treated spatial data construction as part of empirical design. It asked how researchers turn places, borders, distances, travel costs, and exposure weights into credible empirical objects. Lecture 16 asks the next question: **how do researchers make causal claims once those spatial objects exist?**

Spatial data create identification problems because nearby units often share shocks, influence one another, and sort into similar environments. Geography can be useful, dangerous, or substantive. A border can create quasi-experimental variation. Proximity can make conventional standard errors too small. Neighborhoods, commuting access, or local public goods can be the mechanism being studied. The same map may therefore play three roles:

- **Geography as source of identification:** policy borders, institutional boundaries, distance discontinuities, or spatially varying exposure generate the comparison.
- **Geography as threat to inference:** nearby units share unobserved shocks or residual dependence, so standard variance formulas are too optimistic.
- **Geography as mechanism:** distance, access, local labor demand, neighborhood quality, environmental exposure, or spillovers are the causal channel.

The central question is: **how do spatial spillovers, sorting, exposure, and correlated shocks change causal designs?** The answer is not "add spatial fixed effects" or "cluster by county." A strong spatial design states the mechanism, the geography, the estimand, the comparison group, the interference assumption, and the inference correction together.

This lecture teaches each issue through papers students can use as templates. Conley gives the benchmark for spatially dependent inference [@conley1999]. Miguel and Kremer make interference and treatment externalities visible rather than treating them as nuisance [@miguelKremer2004]. Black, Dell, and Dube, Lester, and Reich show different versions of boundary and border logic [@black1999; @dell2010; @dubeLesterReich2010]. Goldsmith-Pinkham, Sorkin, and Swift and Borusyak, Hull, and Jaravel show why shift-share exposure requires diagnostics, not just a formula [@goldsmithPinkhamSorkinSwift2020; @borusyakHullJaravel2025]. Chetty, Hendren, and Katz and Busso, Gregory, and Kline show why place definitions, sorting, exposure, and equilibrium responses are part of identification rather than post-estimation interpretation [@chettyHendrenKatz2016; @bussoGregoryKline2013].

## Core Points

:::{admonition} Core points
:class: important

- Spatial causal inference begins by deciding whether geography is the source of identification, a threat to inference, or the mechanism itself.
- Conley-style spatial inference solves a variance problem under spatially correlated residuals. It does not solve bias from spillovers, sorting, endogenous boundaries, or omitted local shocks.
- Spillovers and interference require an explicit exposure mapping such as {math}`Y_i = Y_i(D_i,E_i)` and {math}`E_i=\sum_{j\neq i}w_{ij}D_j`.
- Border designs and spatial RD are credible only when local continuity around the border is economically and institutionally plausible.
- Shift-share and place-based designs inherit the geography, weights, and market definitions used to build exposure. Predetermined shares and exogenous shocks must be diagnosed, not assumed.
- Sorting, MAUP, and correlated local shocks are identification problems because they change the counterfactual, not merely the map.
- A defensible spatial design reports the exposure rule, geography, comparison set, interference assumption, inference correction, and main sensitivity checks.
:::

## Bridge

Lecture 15 ended with a warning: spatial curation does not identify causal effects by itself. A commuting-zone exposure, tract-level neighborhood measure, travel-time access index, border assignment, or crosswalked policy variable is only an empirical object. Lecture 16 turns those objects into research designs and asks what can go wrong.

```{include} assets/tables/16-spatial-identification-problems-map.md
```

The bridge from the earlier causal inference lectures is direct. Experiments assumed that treatment assignment could be separated from spillovers or handled by design. DID and event studies required credible untreated paths. IV required exclusion, relevance, and interpretable first-stage variation. RD required local continuity. Spatial data stress every one of these assumptions. Nearby untreated places may be partially treated. Border units may sort differently. Local shocks may be spatially correlated. A shift-share exposure may combine many small shocks or be dominated by one endogenous sector. A neighborhood effect may be mostly selection into neighborhoods unless timing or randomization helps.

The spatial block therefore does not add a separate toolbox detached from the rest of the course. It asks students to use the same identification discipline in settings where geography makes the counterfactual harder to see.

## Field Core

### A. Geography As Source, Threat, Or Mechanism

The first step is to classify the role of geography.

**Source of identification.** Geography creates useful variation when an institutional rule changes at a border, when distance to a treatment boundary generates local variation, or when pre-period local composition interacts with aggregate shocks. Black's school-boundary design uses boundaries between attendance zones to compare nearby homes exposed to different school quality [@black1999]. Dell's mita design uses a historical boundary to study long-run effects of a forced-labor institution [@dell2010]. Dube, Lester, and Reich use contiguous counties on opposite sides of state borders to compare minimum-wage changes while holding local economic context more fixed than a national comparison would [@dubeLesterReich2010].

**Threat to inference.** Geography threatens inference when residuals are correlated across space. Neighboring counties may share weather, regional labor demand, transportation infrastructure, housing markets, or policy environments. In that case, heteroskedastic-robust standard errors can treat many highly related observations as independent. Conley-style corrections address this problem by allowing residual covariance to decay with distance [@conley1999].

**Mechanism.** Geography is the mechanism when the treatment works through access, neighborhoods, labor markets, public goods, environmental exposure, or local spillovers. Chetty, Hendren, and Katz study childhood exposure to better neighborhoods; the spatial object is not just a control, it is the treatment environment [@chettyHendrenKatz2016]. Miguel and Kremer study deworming externalities; the treatment of nearby schools is part of the causal object [@miguelKremer2004].

Many weak papers slide between these roles. A border comparison is not credible merely because it has a border. Spatially robust standard errors do not repair a design with untreated spillovers. A tract exposure index does not identify a neighborhood effect unless selection into tracts is handled. Students should learn to write one sentence early in the paper: **in this design, geography is doing this specific job.**

### B. Spatial Clustering And Conley-Style Inference

The most basic spatial problem is residual dependence. Suppose a researcher estimates:

```{math}
:label: eq:em16-baseline-regression
Y_i = X_i'\beta + u_i.
```

If {math}`\operatorname{Cov}(u_i,u_j)` is positive for nearby observations, then treating observations as independent understates uncertainty. Administrative clustering helps when dependence is nested in a known unit such as state, school district, or labor market. Spatial dependence is less tidy: it often decays with distance, crosses administrative borders, and depends on the scale of the mechanism.

A generic Conley-style variance estimator can be written as:

```{math}
:label: eq:em16-conley-vcov
\widehat{\operatorname{Var}}(\hat\beta)
=
(X'X)^{-1}
\left[
\sum_i \sum_j K\!\left(\frac{d_{ij}}{c}\right)
x_i x_j' \hat u_i \hat u_j
\right]
(X'X)^{-1},
```

where {math}`d_{ij}` is the distance between observations, {math}`c` is a cutoff or bandwidth, and {math}`K(d_{ij}/c)` downweights or removes covariance between distant observations. A rectangular kernel would set the weight to one within the cutoff and zero outside it. A smoother kernel lets covariance fade with distance.

The practical implementation steps are:

1. define the location of each observation, such as centroid, workplace, school, or market center;
2. choose the distance metric, such as great-circle distance, projected Euclidean distance, travel time, adjacency, or network distance;
3. choose a cutoff radius or kernel based on the likely shock process;
4. report sensitivity to plausible cutoffs;
5. keep the design interpretation separate from the inference correction.

The caveat is central. Conley-style inference changes the estimated variance, not the estimand. If treated places contaminate controls, if workers sort into treated neighborhoods, or if a border coincides with unobserved institutions, the coefficient can still be biased. Conley-style standard errors can make uncertainty honest around a bad comparison, but they cannot make the comparison credible.

### C. Spillovers, Interference, And Exposure Mappings

Spatial settings often violate the simplest form of SUTVA. A unit's outcome may depend on its own treatment and on nearby treatment. A useful potential-outcomes object is:

```{math}
:label: eq:em16-spatial-exposure-po
Y_i = Y_i(D_i,E_i),
```

where {math}`D_i` is own treatment and {math}`E_i` summarizes the treatment or exposure of neighbors. A standard exposure measure is:

```{math}
:label: eq:em16-spatial-exposure-map
E_i = \sum_{j \neq i} w_{ij} D_j,
```

where {math}`w_{ij}` encodes geographic proximity, adjacency, travel time, school links, commuting flows, or another exposure channel.

Miguel and Kremer are the teaching anchor because they estimate treatment externalities rather than assuming them away [@miguelKremer2004]. Their setting makes a general point: if treatment affects nearby untreated units, then the "control group" may not represent the no-treatment counterfactual. The researcher must decide whether spillovers are absent, bounded by distance, summarized by an exposure mapping, or the main estimand.

Implementation details matter. A student using Equation {eq}`eq:em16-spatial-exposure-map` must specify:

- whether the weights use distance, adjacency, commuting, school catchments, social links, or market shares;
- whether weights are row-normalized;
- whether exposure is measured contemporaneously or with lags;
- whether the spillover radius is fixed before looking at outcomes;
- whether own treatment is excluded from the exposure measure;
- whether the estimand is the effect of own treatment holding exposure fixed, the effect of exposure holding own treatment fixed, or a combined policy effect.

Exposure mappings partially repair the potential-outcomes notation. They do not magically solve omitted variables. Nearby treated units may be similar because of sorting or local shocks. The exposure mapping needs a design behind it: random assignment with saturation, quasi-random placement of treated units, strong controls for location choice, or a credible source of variation in neighbor exposure.

### D. Border Designs And Spatial RD

Border designs use geography as a source of identification. The core intuition is local comparability: units near one another but on opposite sides of a border may be more similar than units far apart. A simple boundary-discontinuity specification is:

```{math}
:label: eq:em16-spatial-rd-outcome
Y_i
=
\alpha
+ \tau \mathbf{1}\{b_i \ge 0\}
+ f_-(b_i)\mathbf{1}\{b_i < 0\}
+ f_+(b_i)\mathbf{1}\{b_i \ge 0\}
+ X_i'\gamma
+ \varepsilon_i,
```

where {math}`b_i` is signed distance to the border. The same logic can be written for treatment assignment:

```{math}
:label: eq:em16-spatial-rd-treatment
D_i = \mathbf{1}\{b_i \ge 0\}.
```

This notation is intentionally simple. Real spatial RD is harder because boundaries are often irregular and distance to the nearest border does not summarize all relevant geography. Units can differ along the boundary, sorting may occur exactly near the border, and spillovers can cross the line.

The paper anchors teach different lessons.

Black's school-boundary design compares houses near school attendance boundaries to infer parental valuation of school quality [@black1999]. The implementation lesson is that boundary fixed effects and narrow samples help isolate local comparisons, but housing sorting and unobserved neighborhood amenities remain core threats.

Dell's mita design studies long-run effects of a historical institution using a boundary-discontinuity design [@dell2010]. The implementation lesson is that researchers must show continuity in predetermined geography and pre-treatment characteristics, because historical borders can bundle institutions, terrain, ethnicity, roads, markets, and state presence.

Dube, Lester, and Reich use contiguous county pairs across state borders in minimum-wage research [@dubeLesterReich2010]. The implementation lesson is that contiguous comparisons can absorb broad regional differences, but they still require attention to local trends, cross-border labor markets, and spatially correlated shocks.

A practical spatial RD or border design should report:

1. the exact border or boundary segments used;
2. the running variable or local-neighbor rule;
3. bandwidth choices and sensitivity;
4. balance of predetermined variables near the border;
5. evidence on sorting, manipulation, or endogenous boundary placement;
6. treatment and control exposure on both sides of the boundary;
7. inference that allows dependence along or across the boundary.

The main caveat is that geography can be too good at bundling. Borders often separate more than one thing. The design has to argue why the discontinuous object of interest changes at the boundary while other relevant determinants evolve smoothly enough for the intended estimand.

### E. Shift-Share And Place-Based Exposure Designs

Shift-share designs use pre-period local composition and common shocks to create spatially varying exposure:

```{math}
:label: eq:em16-shift-share-exposure
Z_\ell = \sum_s w_{\ell s} g_s,
```

where {math}`w_{\ell s}` is location {math}`\ell`'s baseline share in sector, origin, occupation, or product {math}`s`, and {math}`g_s` is a shock common to all locations. A local labor-market exposure to trade, immigration, technology, or industrial demand often takes this form.

The spatial content is not optional. The location {math}`\ell` might be a commuting zone, county, metro area, school district, or tract. The weights may use baseline employment, population, industry shares, task shares, or origin-country settlement patterns. The shock may be global, national, sectoral, or predicted from leave-one-out variation. Those choices define the estimand and the identifying variation.

Modern shift-share work asks students to inspect what identifies the estimate. Goldsmith-Pinkham, Sorkin, and Swift emphasize diagnostics based on the shares and the sectors that receive weight [@goldsmithPinkhamSorkinSwift2020]. Borusyak, Hull, and Jaravel emphasize the shock-level view and practical conditions under which shocks can be treated as quasi-experimental [@borusyakHullJaravel2025].

Implementation details include:

- report the distribution of exposure {math}`Z_\ell`;
- identify the sectors or shocks contributing most to variation;
- compute leave-one-out or national-minus-own-region shocks when own-region feedback is a concern;
- test sensitivity to alternative baseline years and geography definitions;
- report whether the first stage or reduced form is dominated by a small number of shares;
- use inference appropriate to the effective number and dependence structure of shocks;
- explain whether the identifying assumption is about exogenous shares, exogenous shocks, or both.

Place-based policies create related problems. Busso, Gregory, and Kline study a prominent place-based policy and show why incidence, efficiency, and comparison geography must be handled carefully [@bussoGregoryKline2013]. Treated places may affect nearby untreated places through commuting, firm relocation, housing prices, or worker movement. The treatment can be assigned to a jurisdiction, but the economic exposure may be residents, workplaces, firms, or neighboring areas. A place-based design therefore needs a treatment geography and an exposure geography, and they may not be the same.

### F. Sorting, MAUP, And Correlated Local Shocks

When place itself is the treatment, sorting is usually the first-order threat. Workers, firms, families, and schools choose locations. Those choices reflect income, information, preferences, networks, productivity, amenities, housing prices, and institutional constraints. A cross-sectional regression of outcomes on neighborhood quality rarely identifies a neighborhood effect because people are not randomly allocated across neighborhoods.

Chetty, Hendren, and Katz are useful because the Moving to Opportunity design gives students a template for using random assignment and exposure timing to study neighborhoods [@chettyHendrenKatz2016]. The implementation lesson is that timing matters. Childhood exposure, age at move, origin neighborhood, destination neighborhood, and take-up all affect interpretation.

The modifiable areal unit problem is connected to sorting and mechanisms. If a design produces different estimates at tract, county, and commuting-zone levels, that may mean:

- the mechanism operates at one scale and not another;
- spillovers cross smaller boundaries;
- aggregation changes the treated population;
- residual shocks are correlated at a broader scale;
- the researcher was searching over geographies after seeing results.

MAUP is not merely a mapping nuisance. It can change the causal estimand. A tract-level neighborhood effect, a county-level policy effect, and a commuting-zone labor-demand effect are different objects. Robustness across geographies is useful only when each alternative has an economic interpretation.

Correlated local shocks create a related problem. A factory closure, housing boom, transit investment, school finance change, or local political shock may affect multiple nearby units. If the treatment is assigned in one of those places, the comparison group may share the shock or experience it differently. Diagnostics should therefore look for spatially patterned residuals, pre-trends, covariate gradients, and sensitivity to dropping nearby controls or broadening the comparison geography.

### G. Design Diagnostics And Implementation Checklist

The core design question is not which estimator is fashionable. It is whether the spatial object, comparison, and counterfactual line up.

```{include} assets/tables/16-designs-and-corrections-toolkit.md
```

```{include} assets/tables/16-good-design-checklist.md
```

For applied papers, the checklist can be operationalized as follows:

1. State the economic mechanism before choosing the geography.
2. Define the unit of observation, treatment, exposure, and identifying variation separately.
3. Write the causal object with own treatment and exposure when spillovers are plausible.
4. Show maps only after the estimand and comparison group are stated.
5. Diagnose whether controls are contaminated by spillovers or shared shocks.
6. Report spatial inference as an inference correction, not as an identification claim.
7. Use paper-specific falsification tests: border balance for RD, exposure decomposition for shift-share, timing and take-up checks for mover designs.
8. Interpret geography sensitivity as evidence about the mechanism, not as a mechanical robustness ritual.

The best spatial papers make the reader feel that the map, algebra, and comparison are all describing the same causal object.

## Research Lab

The Week 16 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package.

The primary anchor is the contiguous-border logic in Dube, Lester, and Reich [@dubeLesterReich2010]. This is a good teaching anchor because it forces students to define border pairs, compare nearby treated and untreated places, and confront spatially correlated inference. The challenge paper is the shift-share diagnostic logic in Goldsmith-Pinkham, Sorkin, and Swift and Borusyak, Hull, and Jaravel [@goldsmithPinkhamSorkinSwift2020; @borusyakHullJaravel2025]. The transfer task uses a different spatial logic: exposure built from baseline shares and shocks rather than treatment assignment across a border.

### Reproduce

Students reproduce a simplified contiguous-border comparison with deterministic synthetic county data. The data are designed to resemble a minimum-wage-style local policy exercise, but they are not a replication of any published dataset. Students:

- define border-pair observations;
- estimate a treatment effect with border-pair fixed effects;
- compare heteroskedastic-robust and Conley-style spatial standard errors;
- report the sensitivity of inference to the spatial cutoff.

The goal is to learn how a border design uses nearby comparisons and why spatial inference may matter even when the comparison is local.

### Diagnose

Students then diagnose whether the border design is credible:

- Are treated and control sides balanced on predetermined characteristics?
- Are any untreated units exposed to treated neighbors?
- Does the estimate change when poorly balanced border pairs are dropped?
- Does spatially robust inference change the conclusion?
- Is geography the source of identification, a threat to inference, or the mechanism?

The Diagnose memo must separate bias threats from variance corrections. A larger Conley standard error does not prove the design is unbiased. A small robust standard error does not prove nearby shocks are irrelevant.

### Transfer

Students transfer the design discipline to a shift-share exposure task. Using synthetic county-by-sector baseline shares and sector shocks, they:

- construct {math}`Z_\ell=\sum_s w_{\ell s}g_s`;
- inspect the distribution of exposure across places;
- identify dominant sector contributions;
- compare baseline, leave-one-out, and alternative-geography exposures;
- write a memo explaining whether the identifying assumption is about shares, shocks, or both.

The transfer task shows that spatial identification can come from exposure rather than a border. It also makes the caveat visible: a polished exposure index is not a valid instrument unless the source of identifying variation is defensible.

## Methods Box

:::{admonition} Methods Box: Practical Spatial Causal Inference Rules
:class: note

**Conley-style inference.** Use when residual correlation is likely to decay with distance. Report coordinates, distance metric, cutoff, kernel, and sensitivity. Treat it as a variance correction.

**Exposure mappings.** Use when spillovers are plausible and can be summarized by nearby treatment or exposure. Justify weights, radius, normalization, timing, and whether own treatment is excluded.

**Border designs and spatial RD.** Use when a policy or institution changes at a boundary and local continuity is plausible. Report boundary segments, bandwidths, balance, sorting checks, and spillover concerns.

**Shift-share designs.** Use when pre-period shares and common shocks generate meaningful place-level exposure. Diagnose dominant shares, effective shock variation, baseline-year sensitivity, and leave-one-out shocks.

**Place-based policies.** Distinguish the administrative treatment area from the economic exposure area. Report spillovers to nearby places, worker and firm mobility, and local equilibrium caveats.

**Sorting and MAUP.** Treat location choice and geography choice as identification problems. Explain why the unit of analysis matches the mechanism and how estimates change under plausible alternatives.

The common failure is to fix the estimator before fixing the geography and interference structure. The stronger workflow reverses that order.
:::

## Reading Ladder And References

```{include} assets/tables/16-reading-architecture.md
```

For a first pass, students should read Conley for the variance problem and Miguel and Kremer for interference [@conley1999; @miguelKremer2004]. That pair separates spatial dependence in residuals from spillovers in potential outcomes.

For border logic, students should compare Black, Dell, and Dube, Lester, and Reich [@black1999; @dell2010; @dubeLesterReich2010]. The useful exercise is to ask what "nearby" means in each paper and what the border might bundle besides treatment.

For shift-share and place-based designs, students should read Goldsmith-Pinkham, Sorkin, and Swift alongside Borusyak, Hull, and Jaravel, then use Busso, Gregory, and Kline to see why place-based treatment can raise incidence and spillover questions [@goldsmithPinkhamSorkinSwift2020; @borusyakHullJaravel2025; @bussoGregoryKline2013].

For sorting and neighborhood exposure, Chetty, Hendren, and Katz show how random assignment, mover timing, and exposure duration can make place effects more credible [@chettyHendrenKatz2016].

## Exercises And Discussion Prompts

1. Choose one paper from the reading ladder and classify geography as source, threat, mechanism, or some combination. What sentence in the paper would you use to defend that classification?
2. Explain why Conley-style standard errors may change the confidence interval while leaving the coefficient biased.
3. Write an exposure mapping for a job-training program where treated firms may affect nearby untreated firms through worker poaching.
4. In a border design, what balance tests would be convincing before treatment? What balance tests could be mechanically misleading?
5. Suppose a neighborhood-effect estimate is large at the tract level and near zero at the county level. Give one mechanism-based interpretation and one design-failure interpretation.
6. For a shift-share exposure, identify the shares, the shocks, the geography, and the likely source of identifying variation. What diagnostic would you run first?
7. Design one falsification test for a place-based policy where workers can commute across the treatment boundary.

## Reproducibility And Code Lab Note

The Lecture 16 lab is located in `labs/16-causal-inference-with-spatial-data/`. It uses deterministic synthetic teaching data so the public workflow does not depend on proprietary geographies, confidential county identifiers, or an uncertain replication package. The smoke path creates the data, estimates a border-pair design, runs spatial inference diagnostics, and transfers the logic to shift-share exposure diagnostics.

The lab outputs are intended for design memos, not for substantive claims about minimum wages, trade shocks, neighborhoods, or place-based policy. Students should explicitly state that the lab is a teaching reproduction of design logic.

## Slide Companion Note

The Lecture 16 slides should not duplicate the chapter. They should make the design architecture visible:

- geography as source, threat, or mechanism;
- spatial clustering and Conley-style inference;
- spillovers and exposure mappings;
- border designs and spatial RD;
- shift-share and place-based designs;
- sorting, MAUP, and correlated local shocks;
- a design diagnostics checklist;
- the Reproduce -> Diagnose -> Transfer lab structure.

One slide should state plainly: **spatially robust standard errors are not a substitute for a spillover model or a sorting design.**

The canonical slide source is `slides/week16/16-causal-inference-with-spatial-data.tex`.

## Bridge Forward

Lecture 16 shows how space complicates causal inference in partial-equilibrium designs. Lecture 17 takes the next step and asks when partial-equilibrium estimates are no longer enough because workers, firms, rents, amenities, migration, commuting flows, and local prices interact in spatial equilibrium.
