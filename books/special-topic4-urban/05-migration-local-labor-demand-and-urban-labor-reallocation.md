# Migration, Local Labor Demand, And Urban Labor Reallocation

## Learning Objectives

By the end of Week 5, students should be able to:

1. explain how local labor-demand shocks propagate through wages, employment, migration, commuting, rents, firm dynamics, and population adjustment;
2. distinguish adjustment for places from adjustment for incumbent workers and migrants;
3. interpret migration and commuting as linked spatial labor-supply margins rather than as background demographic flows;
4. evaluate local-shock designs that use shift-share exposure, predicted-destination instruments, commuting shocks, dynamic event studies, and spatial-equilibrium calibration;
5. analyze gentrification as labor-market restructuring and diversification as worker insurance and reallocation capacity;
6. design a research-facing empirical project that connects a local shock to a labor outcome, spatial mechanism, identification strategy, and welfare object.

## Opening Orientation

Week 5 asks a dynamic labor question: how do workers, firms, wages, rents, and commuting flows adjust when local labor demand changes?

This is not a generic migration lecture. Migration matters here because it is one part of a spatial labor-adjustment system. A local boom or bust changes the value of living in a place, working in a place, commuting into a place, remaining attached to a declining place, entering a growing place, and opening or closing establishments. The same shock can raise nominal wages, raise rents, attract migrants, price out incumbents, induce in-commuting, change firm entry, lower unemployment, or leave incumbent workers scarred long after the place appears to recover.

The central object is therefore not a single migration elasticity. It is a vector of adjustment margins. Local labor markets adjust through people, places, firms, housing, commuting systems, and neighborhoods. The research task is to say which margin moves, for whom, on what time horizon, and with what incidence.

:::{admonition} Core points
:class: important

- Local labor-demand shocks reallocate work through wages, employment, labor-force participation, commuting, migration, rents, firm entry and exit, and neighborhood change.
- Migration and commuting are substitute and complementary adjustment margins: workers can move toward opportunity, commute toward opportunity, remain in place, or be priced away from it.
- Incidence differs for incumbent workers, migrants, commuters, landlords, homeowners, firms, and local governments.
- A place can recover while incumbent workers remain scarred; a worker can recover by leaving while the origin place declines.
- Gentrification is a labor-market restructuring process when it changes job composition, occupational access, service demand, and who can remain near opportunity.
- Diversification is a labor-market object when it changes worker insurance, local resilience, and reallocation capacity after shocks.

:::

## Bridge

Weeks 1-4 built the static architecture. Week 1 defined local labor markets as systems of jobs, residences, commuting costs, rents, amenities, and outside options. Week 2 showed that housing and moving costs determine whether workers can access high-opportunity places. Week 3 showed that opportunity is unequal within metropolitan areas because job access, networks, schools, segregation, and neighborhoods differ. Week 4 showed that safety and environmental conditions change the feasible set for work and the welfare value of wages.

Week 5 adds dynamics. A local demand shock changes the value of a job-residence bundle over time. Workers may respond by changing jobs, residences, commute patterns, sectors, hours, or labor-force attachment. Firms may enter, exit, relocate, change hiring standards, or change technologies. Housing markets may capitalize gains into rents or prices. Neighborhoods may change composition. Commuting flows can move labor supply without moving residence. Migration can move residence without guaranteeing access to the specific jobs that generated the shock.

The discipline is to keep the labor object visible. We are not asking whether places grow in a descriptive sense. We are asking how local shocks change work, earnings, employment, job access, mobility, and welfare, and which workers can actually adjust.

## Field Core

### Block A. Why Migration And Reallocation Are Central Labor Questions

Local labor-demand shocks are canonical labor shocks with spatial incidence. A manufacturing decline, import-competition shock, hospital expansion, energy boom, federal spending change, transit improvement, climate shock, university expansion, or amenity-driven inflow can all change labor demand in one place relative to another. The standard labor questions are immediate: what happens to wages, employment, unemployment, labor-force participation, occupational mobility, and worker welfare?

The urban-labor addition is that none of these outcomes adjusts in a placeless market. Workers and firms are attached to locations through housing, commuting, family networks, local information, sectoral capital, amenities, institutions, and moving costs. A shock to local demand can therefore be absorbed by any combination of:

- nominal wages and earnings;
- employment, unemployment, and labor-force participation;
- population inflows and outflows;
- commuting flows into and out of the treated place;
- rents, house prices, and local nontradable prices;
- firm entry, exit, relocation, and establishment growth;
- occupational and sectoral reallocation;
- neighborhood composition and job-location changes.

This is why the classic local-labor-market literature is foundational for a course on urban labor. Blanchard and Katz ask how regional labor markets evolve after shocks, emphasizing unemployment, participation, and migration adjustment [@blanchardKatz1992RegionalEvolutions]. Bound and Holzer show that local demand shifts can have different effects across demographic groups because population adjustment and labor-market outcomes are jointly determined [@boundHolzer2000DemandShifts]. Autor, Dorn, and Hanson bring this logic to trade exposure, showing that local shocks can generate persistent employment, earnings, and transfer responses rather than frictionless mobility [@autorDornHanson2013ChinaSyndrome].

For this week, the empirical question is not "do people migrate?" The question is: when local demand changes, which parts of the spatial labor system adjust, which workers can use the adjustment margins, and who bears the losses or captures the gains?

### Block B. A Spatial Labor-Adjustment Framework

Start from the job-residence framework from Week 1 and add time and local shocks. Worker {math}`i` evaluates working in job or workplace {math}`j`, living in residence {math}`r`, and facing local demand state {math}`D_{\ell t}`:

```{math}
:label: eq:adjustment-value-week5
V_{ijrt}
=
w_{jt}(D_{\ell t})
- R_{rt}(D_{\ell t})
- \tau_{jrt}
+ A_{rt}
- M_{ir t}
+ \varepsilon_{ijrt}.
```

The wage {math}`w_{jt}` can rise or fall with local demand. Housing cost {math}`R_{rt}` can capitalize expected gains. Commuting cost {math}`\tau_{jrt}` determines whether a worker can access a workplace without moving. Moving cost {math}`M_{irt}` is worker-specific and may depend on wealth, tenure, family structure, housing-market liquidity, information, and attachment to place. Amenities {math}`A_{rt}` may also change when the shock brings congestion, safety changes, pollution, new services, or neighborhood turnover.

A local shock produces an adjustment vector:

```{math}
:label: eq:local-adjustment-vector-week5
\Delta Y_{\ell t}
=
\left(
\Delta w_{\ell t},
\Delta E_{\ell t},
\Delta U_{\ell t},
\Delta N_{\ell t},
\Delta C_{\ell t},
\Delta R_{\ell t},
\Delta F_{\ell t},
\Delta S_{\ell t}
\right),
```

where {math}`w` is wages, {math}`E` employment, {math}`U` unemployment or nonemployment, {math}`N` resident population, {math}`C` commuting flows, {math}`R` rents or housing prices, {math}`F` firm entry and exit, and {math}`S` sectoral or skill composition. The main lesson is that no single element of {math}`\Delta Y_{\ell t}` has a stable welfare interpretation by itself.

If wages rise but rents rise more, incumbent renters may lose. If local employment rises but workers commute from outside, the treated place's residents may not be the main beneficiaries. If population falls after a shock, the origin place may look less distressed in per capita terms because the most mobile workers left. If a place's employment recovers, the workers who were initially displaced may still experience persistent earnings losses. Moretti's local-labor-market framework and Notowidigdo's incidence analysis are useful because they force wages, rents, mobility, and welfare into the same object [@moretti2011; @notowidigdo2020LocalDemandShocks].

```{include} assets/tables/05-housing-mobility-and-incidence-framework.md
```

The framework also clarifies the distinction between **places** and **people**. A place is a geography with jobs, establishments, residents, rents, commuting links, and local public finance. People are workers and households who may stay, leave, enter, commute, switch sectors, or exit work. Place outcomes and person outcomes are connected, but they are not the same estimand.

### Block C. Migration, Commuting, And Incidence After Local Demand Shocks

Migration is one way labor supply reaches local demand. Commuting is another. Treating migration as the only spatial adjustment margin is a common mistake.

A positive local demand shock can attract residents into the place. It can also attract workers who live elsewhere and commute in. If commuting is feasible, local employment can respond strongly even when local population changes little. If commuting is costly, housing supply is tight, or transit is weak, adjustment may show up instead as higher wages, higher rents, slower firm growth, or rationed access to jobs. Monte, Redding, and Rossi-Hansberg show why commuting and migration jointly determine local employment elasticities [@monteReddingRossiHansberg2018].

The same point matters within metropolitan areas. A downtown job boom may raise employment in the central business district without requiring all workers to move downtown. A suburban logistics boom may benefit auto-accessible residents more than transit-dependent central-city residents. A transit investment may change effective labor supply to job centers without changing residential migration. Severen's mass-transport evidence is useful here because it treats commuting access as a labor and housing adjustment margin, not merely an infrastructure amenity [@severenCommutingLaborHousing2023].

Incidence depends on which margin is scarce:

- If labor mobility is easy and housing supply is elastic, population may adjust more than wages or rents.
- If housing supply is inelastic, demand gains can capitalize into rents and prices.
- If commuting is open, in-commuters can capture workplace gains while residents experience rent pressure.
- If workers are immobile, local shocks can produce persistent unemployment, nonemployment, or wage losses.
- If firms can relocate or enter easily, local labor demand may spread across connected places rather than stay inside the initial geography.

Howard's migration accelerator adds an important mechanism: migration itself can raise local demand by increasing housing demand, construction, services, and local spending [@howard2020migration]. In that setting, migrant inflows are not just labor supply. They are also local demand, especially when housing and nontradables respond. That is why migration, housing, and labor demand must be taught as a joint system.

### Block D. Persistence, Hysteresis, And Local Labor-Market Recovery

The old spatial-equilibrium benchmark imagines that workers move from declining places to growing places until utility gaps narrow. The empirical literature repeatedly shows why this benchmark is incomplete. Migration is costly, housing markets are slow, firms and workers are specialized, local information is sticky, and shocks can scar workers.

Persistence can arise through several channels:

- workers lose firm-specific, occupation-specific, or sector-specific capital;
- job loss weakens local networks and search intensity;
- housing wealth declines and locks homeowners in place;
- public finances, schools, safety, and amenities deteriorate after decline;
- young workers leave, changing the remaining worker composition;
- firms exit and reduce the thickness of the local market;
- commuting links are too weak to connect residents to external recovery.

Yagan's Great Recession evidence illustrates employment hysteresis: exposure to local labor-market collapse can have persistent effects on workers even as aggregate conditions improve [@yagan2019EmploymentHysteresis]. Hershbein and Stuart emphasize the evolution of local labor markets after recessions, helping students distinguish short-run cyclical adjustment from medium-run restructuring [@hershbein2024evolution]. Recent work on places versus people puts the distinction sharply: place-level recovery can coexist with persistent losses for incumbent workers, and worker-level recovery may occur through exit from the origin place rather than revival of the origin economy [@autor2025places].

This distinction should govern interpretation. A place can recover if employment, establishments, and population return. Incumbent workers can still lose if they experience occupational downgrading, lower cumulative earnings, or delayed reemployment. A place can decline while some workers recover by leaving. A local policy can raise place employment while the main gains accrue to migrants or commuters. The empirical design must decide whether the target is place recovery, incumbent-worker recovery, migrant gains, or aggregate efficiency.

### Block E. Places Versus People

The phrase "places versus people" is useful only if students make it operational. It is not a debate about whether geography matters. It is a measurement and welfare problem.

Place-based outcomes include local employment, unemployment rates, population, rents, tax base, establishment counts, vacancy creation, commuting inflows, and neighborhood composition. Person-based outcomes include earnings, employment, occupation, commuting time, residential mobility, family resources, exposure, wealth, and welfare for identifiable workers. The same treatment can move these objects in different directions.

Consider a local demand subsidy. A place-based evaluation may ask whether employment rose inside the treated area. A person-based evaluation may ask whether incumbent residents earned more, whether displaced workers returned to work, whether in-migrants captured the new jobs, whether incumbent renters faced higher rents, and whether commuters captured the wage gains. Kline and Moretti's welfare discussion of local economic development programs is useful background because it asks what place-based policy is trying to maximize and whose welfare counts [@klineMoretti2014PeoplePlaces].

The practical implication is that a paper should state its unit of incidence:

- incumbent residents before the shock;
- incumbent workers employed in the local labor market;
- new migrants;
- out-migrants;
- in-commuters;
- local firms;
- landlords and homeowners;
- local taxpayers and public-service users.

Without that discipline, a coefficient on local employment or local wages can be sold as worker welfare when it may instead measure composition change, capitalization, or commuting.

### Block F. Gentrification As Labor-Market Restructuring

Gentrification is often taught as a housing and neighborhood change topic. In this course, it becomes a labor-market restructuring topic.

Through a labor lens, gentrification can change:

- the sectoral mix of jobs located in or near the neighborhood;
- the demand for local services, restaurants, childcare, cleaning, logistics, retail, health, and personal services;
- the wage and skill composition of local employment;
- the commute patterns of workers serving the neighborhood;
- the ability of incumbent residents to remain near jobs and networks;
- the returns to local property ownership relative to renting;
- the geography of job search and informal hiring networks.

The key question is not whether a neighborhood got more expensive in isolation. The key question is which labor-market opportunities were created, destroyed, relocated, upgraded, or made less accessible. Kolko's job-location work makes the neighborhood job geography explicit [@kolko2009joblocation]. Hartley's work on employment impacts of gentrification asks whether neighborhood upgrading changed labor outcomes for residents [@hartley2013longterm]. Couture, Gaubert, Handbury, and Hurst connect neighborhood change to the urbanization of college graduates, which helps students see how high-skill residential demand, amenities, local services, and job composition can move together [@couture2023neighborhood].

This labor framing also prevents two weak interpretations. The first weak interpretation is that gentrification is "good" if local employment grows. Employment growth may accrue to new residents, in-commuters, or higher-skill workers while incumbent renters lose access. The second weak interpretation is that gentrification is only displacement. Some incumbent workers may gain through local service demand, safer amenities, new networks, or rising home equity, while others lose through rents, business turnover, network disruption, or longer commutes. The research contribution is to identify the labor margins and incidence, not to attach a single sign to the neighborhood label.

### Block G. Diversification, Resilience, And Worker Insurance Across Local Shocks

Diversification is also a labor-market object. A city with a diversified industry structure may provide better insurance against sector-specific shocks because displaced workers can move across employers, sectors, or occupations without leaving the local labor market. A specialized city may offer higher upside during a boom but deeper losses when the dominant sector contracts.

The labor question is therefore not "should a city diversify?" in an abstract planning sense. It is:

- does diversification reduce unemployment volatility for workers?
- does it preserve local job ladders after sectoral shocks?
- does it make occupational reallocation easier?
- does it lower the need for costly migration after downturns?
- does it insure low-mobility workers more than high-mobility workers?
- does it trade off static productivity from specialization against dynamic resilience?

Recent work on economic diversity and city resilience, and on whether cities should diversify, gives students a frontier way to connect urban industrial policy to labor-market risk [@desoyres2025diversity; @bouvard2024should]. The empirical challenge is difficult because diversified places differ from specialized places in size, human capital, amenities, institutions, housing supply, and industry life cycles. A good design must separate diversity as insurance from diversity as a proxy for rich, large, high-amenity labor markets.

The worker-insurance interpretation connects directly to migration. If diversification provides local reallocation capacity, workers may not need to leave after a shock. If diversification mainly attracts already-mobile high-skill workers, it may increase resilience for some while leaving low-skill or low-wealth workers exposed. The welfare object is not the Herfindahl index itself. It is the distribution of job-loss risk, reemployment options, earnings losses, moving costs, and real access to alternative work.

### Block H. Methods And Data As Identification Discipline

The methods layer for this week should be practical rather than encyclopedic. The design must connect four objects:

1. the empirical setting;
2. the identification strategy;
3. the actual econometric method;
4. the labor-adjustment margin.

```{include} assets/tables/05-paper-architecture-map.md
```

The architecture map shows why this is not a list of papers. Each paper plays a role in a research design. Local shock papers identify demand exposure. Commuting papers reveal whether labor supply reaches jobs without residential moves. Migration-incidence papers show when movers are also local demand. Persistence papers separate place recovery from worker scarring. Gentrification papers connect neighborhood change to job composition. Diversification papers interpret industrial structure as resilience or insurance.

```{include} assets/tables/05-methods-and-design-map.md
```

Several design families recur.

**Shift-share and Bartik exposure designs.** These designs interact pre-existing local industry shares with national or external industry growth to predict local demand exposure. They are useful when the question is how local labor markets respond to plausibly external sectoral shocks. The econometric tools are usually instrumental variables, panel fixed effects, distributed lags, and event studies. The design must show why exposure is not simply a proxy for local trends, why the industry shares are predetermined, and which adjustment margin is being estimated. Goldsmith-Pinkham, Sorkin, and Swift clarify the identifying variation in Bartik instruments, while Borusyak, Hull, and Jaravel provide practical guidance for shift-share designs [@goldsmithpinkham2020bartik; @borusyak2025practical].

**Predicted-destination instruments for migration.** These designs use historical settlement shares or origin-destination networks to predict where migrants go, then study receiving-place effects. They are useful when actual migrant allocation is endogenous to local trends. The econometric tools are typically two-stage least squares, distributed lags, and robustness checks for pretrends. Howard's migration accelerator is the natural anchor for linking migrant inflows, housing demand, construction, and local unemployment [@howard2020migration].

**Commuting-linked designs.** These use commuting openness, travel-time changes, transport shocks, or flow-based labor-market definitions to measure how workers access demand without moving residence. The econometric tools include event studies, instrumental variables, gravity-style commuting models, and structural counterfactuals. The design must separate demand changes from access changes and must decide whether outcomes are workplace-based or residence-based [@monteReddingRossiHansberg2018; @severenCommutingLaborHousing2023].

**Dynamic local-shock event studies.** These track outcomes before and after local recessions, plant closures, trade exposure, policy shocks, or demand changes. They are useful for persistence and hysteresis. The econometric tools include event-study coefficients, local projections, matched worker-place panels, and cohort or incumbent definitions. The design must separate place-level rebound from worker-level recovery [@hershbein2024evolution; @yagan2019EmploymentHysteresis].

**Spatial-equilibrium and structural approaches.** These are useful when wages, rents, migration, commuting, housing supply, and firm location adjust together. The econometric tools include calibrated spatial-equilibrium models, simulated counterfactuals, GMM or method-of-moments estimation, sufficient-statistics welfare decomposition, and gravity-style mobility systems. The design must make clear which frictions are estimated and which are imposed [@notowidigdo2020LocalDemandShocks; @desoyres2025diversity].

**Neighborhood and job-location designs.** These study gentrification, local job composition, neighborhood employment, and tract-level restructuring. The econometric tools include panel fixed effects, tract exposure measures, business microdata, boundary or transport shocks, and sometimes instrumented neighborhood change. The design must show a labor mechanism rather than only a rent or demographic change [@kolko2009joblocation; @hartley2013longterm].

```{include} assets/tables/05-data-sources-map.md
```

The data choice follows the margin. ACS and Census data are useful for migration, commuting, demographics, rents, and broad labor outcomes. LEHD, LODES, and QWI are central when the design needs residence-workplace links, commuting flows, and job flows. IRS migration flows are natural for inter-county mobility. Housing price and rent data are needed for incidence. Matched employer-employee data are ideal for person-level persistence and firm reallocation. Tract employment and business directories matter for gentrification. Travel-time matrices matter for commuting designs. Historical settlement shares and origin-destination matrices matter for predicted migration instruments.

The minimum standard for a Week 5 empirical design is simple: the paper should make the adjustment system observable enough that the reader can tell whether the shock moved wages, rents, migration, commuting, firms, workers, or composition.

## Research Lab

The Week 5 lab is a bounded synthetic teaching path, not an official replication. It trains students to move from a local shock to a spatial adjustment system.

**Primary anchor.** Howard's migration accelerator is the main replication anchor because it forces students to treat migration as both labor supply and local demand through housing, construction, services, and unemployment [@howard2020migration].

**Challenge anchors.** Monte, Redding, and Rossi-Hansberg provide the commuting-versus-migration benchmark [@monteReddingRossiHansberg2018]. Notowidigdo provides incidence discipline through wages, rents, and mobility [@notowidigdo2020LocalDemandShocks]. Hershbein and Stuart, Yagan, and the recent places-versus-people work provide the persistence and worker-scarring logic [@hershbein2024evolution; @yagan2019EmploymentHysteresis; @autor2025places]. Couture and coauthors, Hartley, and Kolko anchor gentrification as labor-market restructuring [@couture2023neighborhood; @hartley2013longterm; @kolko2009joblocation]. De Soyres and Gaubert and coauthors, plus Bouvard and coauthors, anchor diversification and resilience [@desoyres2025diversity; @bouvard2024should].

**Reproduce.** Students run a deterministic local-shock simulation with four places. One place receives a demand shock. Workers differ in moving costs, commuting access, sectoral skill fit, and housing exposure. The lab computes wages, rents, resident population, in-commuting, employment, and worker welfare before and after the shock.

**Diagnose.** Students classify each output as a place object or person object. They identify who captures the gains: incumbent workers, migrants, commuters, landlords, firms, or homeowners. They also classify whether the observed response is migration, commuting, capitalization, employment adjustment, firm entry, or sectoral reallocation.

**Transfer.** Students apply the same framework to two frontier cases. First, a gentrification scenario changes local service demand, rents, and job composition. Second, a diversification scenario exposes specialized and diversified places to the same sectoral shock. The exercise asks whether diversification insures workers by creating alternative local jobs, or merely changes which workers sort into the place.

The lab's purpose is not to estimate a real migration elasticity. It is to teach the habit of writing down the whole adjustment vector before interpreting any single coefficient.

## Methods Box

:::{admonition} Methods Box: What A Good Local-Reallocation Design Looks Like
:class: note

**Start with the shock.** State whether the variation comes from trade exposure, sectoral demand, migration networks, commuting infrastructure, recession timing, neighborhood change, climate, policy, or firm entry.

**Name the geography.** Justify the unit: commuting zone, county, metro area, tract, workplace zone, residence zone, or flow-based market. The geography should match the mechanism.

**Choose the identification strategy.** Use shift-share exposure for external local demand shocks, predicted-destination instruments for migration allocation, commuting-linked designs for travel access, dynamic event studies for persistence, boundary or policy shocks for neighborhood change, and structural calibration when equilibrium incidence is the target.

**Match the econometric method to the object.** IV, panel fixed effects, event studies, local projections, gravity models, matched worker panels, and spatial-equilibrium calibration answer different questions. The method should reveal the margin, not just produce a coefficient.

**Separate people from places.** Define incumbents, migrants, out-migrants, in-commuters, firms, landlords, and homeowners. A place-level coefficient is not automatically a worker-welfare coefficient.

**Measure adjustment margins jointly.** Whenever possible, report wages, employment, population, commuting, rents, firm dynamics, and composition. Missing margins can reverse the incidence interpretation.

**State the welfare object.** Explain whether the result concerns nominal earnings, real earnings net of rents and commuting, unemployment risk, moving costs, neighborhood access, firm surplus, landlord capitalization, or worker welfare.

:::

## Reading Ladder And References

**Classic local labor-demand adjustment.** Start with Blanchard and Katz for regional evolution, Bound and Holzer for demand shifts and population adjustment, Moretti for the local labor-market overview, and Autor, Dorn, and Hanson for trade exposure and persistent local effects [@blanchardKatz1992RegionalEvolutions; @boundHolzer2000DemandShifts; @moretti2011; @autorDornHanson2013ChinaSyndrome].

**Incidence, migration, and commuting.** Use Notowidigdo for incidence under local demand shocks, Monte, Redding, and Rossi-Hansberg for commuting and migration elasticities, Severen for commuting infrastructure, and Howard for migration as both labor supply and local demand [@notowidigdo2020LocalDemandShocks; @monteReddingRossiHansberg2018; @severenCommutingLaborHousing2023; @howard2020migration].

**Persistence and people versus places.** Use Yagan, Hershbein and Stuart, and Autor, Dorn, Hanson, and coauthors to study hysteresis, local recovery, and the difference between place adjustment and worker adjustment [@yagan2019EmploymentHysteresis; @hershbein2024evolution; @autor2025places].

**Gentrification as labor-market restructuring.** Use Kolko for job location and neighborhood change, Hartley for employment impacts of gentrification, and Couture, Gaubert, Handbury, and Hurst for the urbanization of college graduates and neighborhood transformation [@kolko2009joblocation; @hartley2013longterm; @couture2023neighborhood].

**Diversification and resilience.** Use de Soyres, Gaubert, and coauthors and Bouvard, de Motta, and Titman to ask whether industrial diversity operates as worker insurance, local resilience, or industrial-policy tradeoff [@desoyres2025diversity; @bouvard2024should].

**Methods.** Use Goldsmith-Pinkham, Sorkin, and Swift and Borusyak, Hull, and Jaravel for shift-share identification discipline [@goldsmithpinkham2020bartik; @borusyak2025practical].

## Exercises And Discussion Prompts

1. A commuting zone receives a positive demand shock in a high-wage sector. Write the adjustment vector in Equation {eq}`eq:local-adjustment-vector-week5`. Which elements would have to move before you would call the shock a worker-welfare gain?
2. Suppose employment rises in a downtown workplace zone but resident earnings in nearby neighborhoods do not. Give three explanations involving commuting, rents, worker composition, or firm hiring.
3. Use the places-versus-people distinction to evaluate a place-based subsidy. Who are the possible beneficiaries, and what data would distinguish them?
4. A neighborhood gentrifies and local service employment rises. What evidence would show gains for incumbent workers rather than gains for new residents or in-commuters?
5. A diversified city has smaller employment losses after a manufacturing shock than a specialized city. What threats prevent you from interpreting this as worker insurance?
6. Design a shift-share study of local demand shocks. What are the shares, what are the shifters, what is the geography, and which adjustment margins will you measure?
7. Design a predicted-destination migration IV. What historical shares would you use, what exclusion restriction is required, and what receiving-place outcomes would you measure?
8. Choose one local shock and state the empirical setting, identification strategy, econometric method, labor margin, and welfare object in one paragraph.

## Reproducibility And Code Lab Note

The Week 5 code lab lives at `labs/05-migration-local-labor-demand-and-urban-labor-reallocation/`. It is a bounded synthetic teaching path, not an official replication package. The smoke path creates a deterministic local-shock panel, computes a place adjustment vector, diagnoses incidence across workers and places, transfers the framework to gentrification and diversification scenarios, and writes compact CSV outputs. It runs without confidential microdata or external downloads.

## Slide Companion Note

The Week 5 slide deck lives at `slides/week5/05-migration-local-labor-demand-and-urban-labor-reallocation.tex`. The deck follows the chapter structure but is shorter and presentation-oriented. It defines the dynamic labor question, summarizes adjustment margins, separates people from places, maps migration and commuting to incidence, frames gentrification and diversification as labor-market restructuring, and closes with a methods/data slide and research-design takeaways.

## Bridge Forward

Week 6 turns the course into research design. The Week 5 lesson is the final input: a credible urban-labor project must specify a labor outcome, spatial mechanism, geography, adjustment margin, counterfactual, and welfare object. The final week asks students to build that full design for their own frontier question.
