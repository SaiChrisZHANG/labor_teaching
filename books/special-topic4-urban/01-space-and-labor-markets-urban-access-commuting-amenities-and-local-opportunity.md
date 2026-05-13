# Space And Labor Markets: Urban Access, Commuting, Amenities, And Local Opportunity

## Learning Objectives

By the end of Week 1, students should be able to:

1. define local labor markets as linked systems of workplace and residential choice;
2. explain how commuting costs, rents, amenities, and job access change the feasible set of labor choices;
3. distinguish workplace location from residential location in measurement and theory;
4. interpret urban wage premia as labor-market objects that may reflect productivity, learning, sorting, or compensation;
5. connect housing, segregation, safety, environment, and migration to labor-market opportunity rather than treating them as background urban facts.

Week 1 asks the opening question for Urban and Labor: how does space enter labor-market choice, wage determination, and worker welfare?

The answer is not that workers live in named cities or that regressions need place fixed effects. Workers search over job-residence bundles. A job offer pays a wage at a workplace. A residence carries rent, commuting cost, amenities, risk, and access to other jobs. The local labor market is the system linking these objects through commuting flows, search frictions, housing markets, local amenities, and outside options. This makes the course a labor-economics course first: space matters because it changes which jobs workers can reach, what wages are worth, how search works, and how welfare should be measured.

:::{admonition} Core points
:class: important

- Local labor markets are linked systems of jobs, workers, residences, commuting costs, rents, amenities, and outside options.
- Space changes the feasible labor-market set, not merely the location label attached to a worker or firm.
- Wages alone are not enough to compare opportunity across places because rents, commuting burdens, amenities, and risks enter welfare.
- Workplace location and residential location must be analytically separated.
- Urban wage premia can reflect productivity, learning, sorting, or compensating differentials.

:::

## Bridge

Placeless labor choice imagines a worker choosing among jobs from a common menu. Spatial labor choice begins from a different object: a worker chooses among combinations of workplace, residence, commuting technology, housing cost, amenities, and outside options. Once this is the object, the meaning of a wage changes. A high workplace wage may be attractive if it comes with feasible commuting and affordable housing. The same wage may be less valuable if it requires long travel, high rent, unsafe routes, or weak access to fallback jobs.

The first discipline is to separate administrative places from economically relevant labor markets. A city boundary, county, commuting zone, or metropolitan area can be useful, but none is automatically the labor market. The relevant market is shaped by search and competition across space: which jobs can a worker learn about, reach, accept, and keep? Which workers can firms plausibly hire? Commuting and migration make local labor markets partially open, but commuting frictions can still make job search quite local [@manningPetrongolo2017].

The second discipline is to separate nominal wages from real opportunity. A worker's opportunity is not {math}`w` alone. It is the wage net of housing costs and commuting burdens, plus amenities and other nonwage components of welfare. Spatial equilibrium starts from this joint object rather than from wages alone [@roback1982; @albouyLue2015].

The third discipline is to separate where workers live from where they work. Residence-based data describe residents of a place. Workplace-based data describe jobs located in a place. Commuting flows connect the two, and the distinction matters for search, wages, rents, tax bases, and policy incidence.

## Field Core

### Local Labor-Market Objects

The course begins with a compact vocabulary. Each object is familiar from labor economics, but space changes how the object should be measured and interpreted.

```{include} assets/tables/01-local-labor-market-objects-map.md
```

The key move is to treat the city as a bundle. A city is not just a wage premium or a density statistic. For a worker, it is a set of reachable jobs, housing prices, commuting technologies, amenities, risks, networks, and outside options. For a firm, it is a set of reachable workers, input suppliers, customers, knowledge spillovers, land costs, and local institutions. Urban and Labor keeps the worker-side and labor-market consequences at the center.

### A Worker Job-Residence Choice Framework

A minimal worker problem lets us discipline the rest of the course. Worker {math}`i` evaluates job {math}`j` and residence {math}`r` as a bundle:

```{math}
:label: eq:urban-choice-week1
U_{ijr} = w_j - R_r - \tau(d_{jr}) + A_r + \varepsilon_{ijr}
```

where {math}`w_j` is earnings at job {math}`j`, {math}`R_r` is housing cost at residence {math}`r`, {math}`\tau(d_{jr})` is commuting cost between residence and workplace, {math}`A_r` is amenity value, and {math}`\varepsilon_{ijr}` is idiosyncratic fit. The notation is intentionally spare. It is not a full model of household choice, firm location, or city structure. It is a guardrail: labor choice is made over job-residence bundles, not over jobs alone.

```{include} assets/tables/01-job-residence-choice-framework.md
```

This framework changes the interpretation of several standard labor objects. A job offer is valuable only if it is reachable from some feasible residence. A residence is valuable partly because of the jobs it gives access to. A commute is not only time lost; it is a margin that connects households to labor demand. An amenity can be productive, compensating, or welfare-relevant even when it does not appear in payroll data.

### Local Labor Markets And Spatial Job Search

Local labor markets are search spaces created by commuting and mobility frictions. Workers do not observe and accept every possible job in a national market. They search within a set shaped by distance, travel time, transit reliability, information, networks, family constraints, and employer location. A simple access object is:

```{math}
:label: eq:job-access-week1
\mathcal{J}_i(c) = \{j : \tau(d_{ij}) \leq c\}
```

The set {math}`\mathcal{J}_i(c)` contains jobs worker {math}`i` can access within generalized commuting-cost threshold {math}`c`. As {math}`\tau(d_{ij})` rises with distance, congestion, money cost, unreliability, or risk, the effective opportunity set shrinks. Space therefore changes labor-market opportunity before any wage is observed.

This is why local labor markets should not be defined only by geography. Counties and commuting zones are convenient containers, but labor markets are also flow objects. Commuting flows, travel-time thresholds, vacancy search radii, and worker-firm contact networks reveal the relevant search space. Manning and Petrongolo show how local job search can be highly spatial even inside a broad urban economy [@manningPetrongolo2017]. Monte, Redding, and Rossi-Hansberg show why commuting and migration jointly matter for local employment elasticities and adjustment to shocks [@monteReddingRossiHansberg2018].

Two distinctions are central. First, access is not the same as realized commute. Access asks what jobs are feasible; realized commute is the chosen match conditional on preferences, information, offers, housing, and constraints. Second, commuting is not the same as migration. Commuting links residence and work without moving residence. Migration changes the residential location and may change the entire set of jobs, rents, amenities, and outside options.

### Residential Choice, Commuting, And Workplace Choice

Separating workplace and residence prevents a common empirical mistake. A worker may live in a low-wage residential area and commute to a high-wage workplace, or live in an expensive amenity-rich neighborhood while working in a lower-wage job. Residence-based wage averages, workplace-based wage averages, and household welfare all answer different questions.

Residence-based measurement asks: what opportunities and constraints do residents face? It is useful for studying neighborhood exposure, household resources, housing costs, schools, safety, and local amenities. Workplace-based measurement asks: what jobs and wages are located here? It is useful for studying labor demand, firm productivity, agglomeration, and job suburbanization. Commuting flows connect the two.

This distinction also clarifies policy incidence. A transit expansion may raise job access for residents without changing workplace wages. A housing reform may let workers move closer to jobs without changing firm labor demand. A demand shock may raise workplace employment but benefit in-commuters as well as residents. A local safety improvement may raise the value of work by reducing commuting risk even if wages do not move.

### Wages, Rents, Amenities, And Spatial Equilibrium

Spatial equilibrium begins from the idea that workers compare utility across places, not wages alone. In a stripped-down location version:

```{math}
:label: eq:spatial-eq-week1
w_\ell - R_\ell + A_\ell = \bar{U}
```

The term {math}`w_\ell` is the wage in location {math}`\ell`, {math}`R_\ell` is housing cost, {math}`A_\ell` is amenity value, and {math}`\bar{U}` is the equilibrium utility level for mobile workers. This expression is not a claim that everyone is perfectly mobile or equally compensated. It is a framing device: wages, rents, amenities, and mobility constraints must be interpreted together [@roback1982].

The welfare implication is immediate. A high-wage place may not offer higher utility if rents, commuting costs, risk, or congestion capitalize the wage gain. A low-wage place may offer higher utility for some workers if housing is cheaper, amenities are valuable, or outside options are stable. Albouy and Lue make this point within metropolitan areas by connecting wages, rents, commuting, and quality of life [@albouyLue2015].

The empirical object then becomes real opportunity, not nominal wages. Students should ask which margins equilibrate: rents, wages, commuting, migration, employment, local prices, vacancy creation, or amenities. If mobility is limited, the equality in Equation {eq}`eq:spatial-eq-week1` can fail for constrained workers. That failure is itself a labor-market object, and it motivates Week 2 on housing and mobility constraints.

### Urban Wage Premia As Labor-Market Objects

Dense places often display higher wages. The labor question is what those higher wages mean. A useful decomposition is:

```{math}
:label: eq:uwp-week1
\Delta w^{urban} = \Delta w^{productivity} + \Delta w^{learning} + \Delta w^{sorting} + \Delta w^{compensating}
```

The decomposition is a framing device rather than a theorem. The urban wage premium may reflect productivity or agglomeration if dense places make workers or firms more productive. It may reflect learning if workers accumulate skills faster in cities. It may reflect sorting if higher-productivity workers select into dense places. It may reflect compensating differentials if workers require higher wages to bear rents, congestion, risk, or disamenities.

```{include} assets/tables/01-urban-wage-premium-channels-map.md
```

The labor interpretation depends on the channel. A productivity premium suggests that city density raises output or match quality. A learning premium suggests dynamic human-capital accumulation. A sorting premium cautions against reading wage differences as causal city effects. A compensating premium says that high wages may offset higher costs rather than reveal higher welfare. Glaeser and Mare's cities-and-skills evidence is useful here because it forces students to separate learning, selection, and wage levels over the career [@glaeserMare2001]. Moretti's local labor-market overview provides the broader labor framework for how local demand, supply, productivity, and adjustment interact across places [@moretti2011].

### Welfare Interpretation

Worker welfare depends on the whole bundle. Nominal wages are observable and important, but they are only one component of opportunity. A credible welfare interpretation should state whether the comparison is:

- workplace wage or residence-based earnings;
- nominal wage or wage net of local rents and prices;
- commute realized by current workers or access to reachable jobs;
- spatial selection or causal effect of place;
- local labor market defined by geography or by flows.

These distinctions matter for inequality. Two workers with the same skills may face different search sets because jobs are far from one residence and near another. Two workers in the same workplace may face different welfare because they live in different housing markets or commute under different risks. Two places with the same average wage may provide different opportunity because rents, amenities, and access differ.

### Preview Of Later Urban-Labor Themes

Week 1 provides the language for the rest of the course. Later weeks each study one way that space enters labor-market opportunity.

```{include} assets/tables/01-domain-preview-map.md
```

Week 2 adds housing supply, rents, moving costs, and mobility constraints. Week 3 studies spatial mismatch, segregation, neighborhoods, networks, and unequal job access. Week 4 treats crime, safety, pollution, heat, and environmental quality as constraints on the feasible set for work. Week 5 studies migration, commuting, local demand shocks, and reallocation. Week 6 converts the sequence into research designs with clear labor outcomes, spatial mechanisms, and welfare objects.

## Research Lab

The Week 1 lab trains students to think like researchers about spatial labor markets. The workflow is **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** The primary anchor is the spatial job-search logic in Manning and Petrongolo [@manningPetrongolo2017]. Students use a deterministic synthetic city with residential zones, workplace zones, wages, rents, amenities, and travel times. They compute reachable jobs under alternative commuting-cost thresholds, compare access-based market definitions with administrative geography, and summarize how the local labor market changes when travel costs rise.

**Diagnose.** Students classify each output as an access object, commute object, wage object, rent object, amenity object, or equilibrium object. They explain why access is not realized employment, why workplace wages are not residential welfare, why high nominal wages may not imply high real opportunity, and why spatial selection is different from causal local effects.

**Transfer.** The challenge anchor is Monte, Redding, and Rossi-Hansberg on commuting, migration, and local employment elasticities [@monteReddingRossiHansberg2018]. Students transfer the logic from one synthetic city to a local shock: what changes if workers commute across zones rather than migrate? What is the equilibrium object? Which workers are treated as residents, workers, or commuters? The optional frontier prompt uses Miller's job-suburbanization evidence to ask how a change in the geography of work can matter for racial employment gaps even without confidential microdata [@millerWhenWorkMoves2023].

The lab does not claim to reproduce the official data or estimates in any anchor paper. It is a bounded teaching path that runs locally and teaches five habits: define the local labor market, state what counts as access, name the equilibrium object, separate sorting from productivity and commuting frictions, and explain why a place-specific result can reveal a portable labor-market mechanism.

## Methods Box

:::{admonition} Methods Box: Spatial Measurement Discipline
:class: note

**Residence-based versus workplace-based measurement.** Residence-based measures describe people who live in a place. Workplace-based measures describe jobs located in a place. Commuting flows connect the two.

**Nominal wages versus real opportunity.** Wages must be interpreted with rents, prices, commuting costs, amenities, risk, and mobility constraints.

**Access versus realized commute.** Access is the set of feasible jobs under a generalized travel-cost budget. Realized commute is the chosen match after search, offers, housing, and constraints.

**Spatial selection versus causal local effects.** Higher wages in cities may reflect selected workers, local productivity, learning, or compensation. The empirical design must state which channel it identifies.

**Geographic versus flow-based labor markets.** Administrative boundaries are useful containers, but commuting flows, travel times, search radii, and worker-firm links often define the relevant market more directly.

Key empirical objects include commuting flows, workplace and residential wage measures, local price and rent adjustment, job suburbanization and job access, commuting-zone or travel-time markets, and spatial-equilibrium counterfactuals.

:::

## Reading Ladder And References

**Spatial-equilibrium foundations.** Start with Roback for the wages-rents-amenities logic and use Albouy and Lue to bring that logic inside metropolitan areas through rents, wages, commuting, and quality of life [@roback1982; @albouyLue2015].

**Spatial job search and local labor markets.** Use Manning and Petrongolo as the primary Week 1 anchor for how local labor markets can be measured through spatial search rather than administrative labels alone [@manningPetrongolo2017].

**Commuting and migration adjustment.** Use Monte, Redding, and Rossi-Hansberg to see why commuting and migration jointly determine local employment elasticities and spatial adjustment [@monteReddingRossiHansberg2018].

**Urban wage premia and learning versus sorting.** Use Glaeser and Mare to ask whether dense places raise wages through learning, worker selection, or other city-linked channels [@glaeserMare2001].

**Job access and the geography of work.** Use Miller to connect job suburbanization and workplace relocation to unequal employment access [@millerWhenWorkMoves2023].

**Broad labor-market framework across places.** Use Moretti as the broad labor-market map for local labor demand, labor supply, productivity, amenities, migration, and adjustment [@moretti2011].

## Exercises And Discussion Prompts

1. Write Equation {eq}`eq:urban-choice-week1` for two workers who face the same job wage but different residences. Which terms can make the same job have different welfare value?
2. Choose a residential neighborhood and a workplace cluster. What data would you need to construct {math}`\mathcal{J}_i(c)`? Which jobs would be missed by a county-level market definition?
3. Suppose a dense city pays 20 percent higher wages. Give one productivity story, one learning story, one sorting story, and one compensating-differential story that could generate the premium.
4. Take a local demand shock. Who is affected if the shock changes workplace jobs but many workers commute from outside the place? How would the answer differ for residence-based and workplace-based data?

## Reproducibility And Code Lab Note

The Week 1 code lab lives at `labs/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates a deterministic city grid, computes job access under travel-cost thresholds, diagnoses spatial-equilibrium objects, and transfers the logic to a small commuting-shock scenario. It runs without confidential microdata.

## Slide Companion Note

The Week 1 slide deck lives at `slides/week1/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.tex`. The deck is a course-opening conceptual map rather than a duplicate of the chapter. It defines the central labor question, introduces the job-residence choice framework, separates access from realized commute, interprets spatial equilibrium and urban wage premia, and bridges to Week 2 on housing, rents, and mobility constraints.

## Bridge Forward

Week 2 takes the first major constraint in the Week 1 framework - housing - and asks when rents, housing supply, moving costs, and residential constraints prevent workers from reaching better labor-market opportunities.
