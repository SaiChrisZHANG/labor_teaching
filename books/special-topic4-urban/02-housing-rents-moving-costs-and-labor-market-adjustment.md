# Housing, Rents, Moving Costs, and Labor-Market Adjustment

## Learning Objectives

By the end of Week 2, students should be able to:

1. explain how rents, housing supply, moving costs, wealth constraints, and commuting enter labor-market opportunity;
2. distinguish nominal wage gains from real access gains after rents and commuting costs adjust;
3. separate housing-supply constraints from moving-cost frictions in local adjustment;
4. evaluate whether migration, commuting, wages, rents, population, or firms absorb a local shock;
5. organize housing-labor papers by research role rather than as a chronological literature list;
6. identify the data sources and empirical designs commonly used to study housing and labor together.

## Opening Orientation

Week 1 defined local labor markets as systems of jobs, residences, wages, rents, commuting costs, amenities, risks, and outside options. Week 2 asks the first major constraint question: when do housing markets and moving costs prevent workers from reaching better labor-market opportunities?

The lecture is a research-framework lecture, not a generic housing lecture. Housing matters here because it governs labor access. Rents change what a wage is worth. Housing supply determines whether a productive place can absorb workers. Moving costs shape whether workers respond to local shocks. Residential sorting and liquidity constraints determine who can enter high-opportunity places. Commuting can substitute for migration, but only for workers whose time, money, schedules, and transport options make that substitution feasible.

:::{admonition} Core points
:class: important

- Housing matters for labor because workers care about real access to jobs, not nominal wages alone.
- Local shocks can be absorbed through wages, rents, population, commuting, migration, firm behavior, or reduced access.
- A central research contribution is often to identify which friction is binding: housing supply, moving costs, wealth and credit constraints, commuting technology, local regulation, or rent capitalization.
- Incidence can fall on workers, landlords, incumbent homeowners, firms, commuters, or excluded would-be migrants.
- The strongest papers connect a clear labor question to a disciplined spatial framework, credible local variation, and data that measure both housing and labor adjustment.

:::

## Bridge

In a placeless labor model, a worker compares wages and nonwage job attributes. In an urban-labor model, the worker compares job-residence bundles. A high-wage job is valuable only if the worker can pair it with a feasible residence and commute. A productive city can fail to raise worker welfare if the wage gain is capitalized into rent, if housing supply is too inelastic, if moving requires liquidity the worker does not have, or if the relevant jobs are reachable only through costly commuting.

The central discipline is to keep the labor question visible. We are not asking whether housing is expensive in a descriptive sense. We are asking who can reach productive places, who captures wage gains, who is priced out, and how housing mediates labor reallocation after shocks.

## Field Core

### A Labor-Space-Housing Framework

The minimal object is the worker's value of a job-residence bundle:

```{math}
:label: eq:housing-labor-bundle-week2
U_{ijr} = w_j - R_r - \tau(d_{jr}) + A_r - M_{ir} + \varepsilon_{ijr}.
```

Here {math}`w_j` is the wage at workplace {math}`j`, {math}`R_r` is the housing cost at residence {math}`r`, {math}`\tau(d_{jr})` is generalized commuting cost, {math}`A_r` is amenity value, {math}`M_{ir}` is the worker-specific cost of moving to or remaining in residence {math}`r`, and {math}`\varepsilon_{ijr}` is idiosyncratic fit. The point is not to solve a full urban model. The point is to force every empirical claim to say which margin is moving.

Housing enters labor outcomes through six channels:

- **Rents and real wages.** Nominal wage gains may disappear once housing costs and commuting burdens adjust [@roback1982; @albouyLue2015].
- **Moving costs and mobility frictions.** Workers may not leave declining places or enter booming places even when wage gaps are large.
- **Housing supply elasticity.** Productive places with inelastic housing supply adjust through prices more than population [@hsiehMoretti2019HousingConstraints; @ganongShoag2017RegionalConvergence].
- **Residential sorting and wealth/liquidity constraints.** High housing costs select workers by income, wealth, credit access, tenure, family structure, and risk exposure.
- **Commuting as a substitute for migration.** Workers can sometimes access a productive labor market without changing residence [@monteReddingRossiHansberg2018].
- **Local shocks and incidence.** A labor-demand shock changes wages, rents, employment, population, firm location, and commuting flows in equilibrium [@notowidigdo2020LocalDemandShocks].

```{include} assets/tables/02-housing-incidence-framework.md
```

### Nominal Wages Versus Real Access

The first distinction is nominal wage gains versus real access gains. A place can pay higher wages because it is more productive, because workers are selected, or because workers need compensation for high rents, congestion, and disamenities. The labor question is whether a worker can actually convert a place's productivity into higher welfare.

A useful reduced object is:

```{math}
:label: eq:real-access-week2
\Delta RA_i = \Delta w_i - \Delta R_i - \Delta \tau_i + \Delta A_i - \Delta M_i.
```

{math}`\Delta RA_i` is not an estimand that every paper literally estimates. It is a checklist. If a study reports only {math}`\Delta w_i`, students should ask what happens to rents, commuting, amenities, and moving costs. If a study reports only rent growth, students should ask whether wages, job access, or population also changed. The central welfare question is not whether a city is high wage. It is whether workers can afford and reach the opportunity embodied in that wage.

Diamond's work on diverging location choices by skill is useful because it shows that different workers may value, access, and sort into places differently [@diamond2016LocationChoices]. Moretti's local labor market framework provides the broader equilibrium map linking local demand, labor supply, amenities, migration, and housing costs [@moretti2011].

### Housing Supply Constraints Versus Moving-Cost Frictions

A common mistake is to treat all low mobility as the same friction. Housing supply constraints and moving-cost frictions imply different counterfactuals.

With a **housing supply constraint**, many workers may want to enter a productive place, but the housing stock cannot expand at low cost. Adjustment occurs through higher rents and higher house prices, with smaller population growth. This is the misallocation logic in Hsieh and Moretti and the convergence logic in Ganong and Shoag [@hsiehMoretti2019HousingConstraints; @ganongShoag2017RegionalConvergence].

With a **moving-cost friction**, housing might be available, but workers do not move because relocation is costly. The cost may be financial, informational, family-linked, tenure-linked, or psychological. Homeowners may face sale constraints; renters may face deposits, credit checks, search costs, or lease timing. Low-wealth workers may be unable to finance the move that would raise expected income.

The empirical contribution is often to distinguish these two stories. If wages are high, rents are high, and population barely grows in a productive place, housing supply is a candidate friction. If affordable destinations exist but workers still do not move after shocks, moving costs, information, household constraints, or local insurance may be central. Zabel's evidence on migration, housing, and labor responses to employment shocks is useful for seeing how these margins interact [@zabelMigrationHousingMarket2012].

### Migration Versus Commuting

Migration changes residence. Commuting links a residence to a workplace without relocation. Both are adjustment margins, and neither should be treated as residual noise.

After a local labor-demand shock, workers may:

- move into the booming place;
- commute into the booming place while living elsewhere;
- remain in the origin and search locally;
- leave the labor force or accept lower-quality jobs;
- be priced out of the destination before the wage gain is realized.

Commuting can make local labor markets more open than residential migration data suggest. Monte, Redding, and Rossi-Hansberg show why commuting and migration jointly shape local employment elasticities [@monteReddingRossiHansberg2018]. Severen's transit evidence and Brough, Freedman, and Phillips's fare experiment are useful because they treat transportation as a labor-access margin rather than merely an urban infrastructure topic [@severenCommutingLaborHousing2023; @broughEliminatingFaresExpand2025].

This distinction matters for inequality. Commuting is not free. It requires time, money, schedule flexibility, safety, reliability, and information. If high-wealth workers can move and low-wealth workers can only commute, the same labor-demand shock can widen real access gaps even if nominal wages rise.

### Worker, Landlord, Homeowner, And Firm Incidence

The incidence question is: who captures local opportunity?

A positive local productivity or demand shock may raise worker wages. It may also raise rents, house prices, or firm labor costs. If housing supply is inelastic, landlords and incumbent homeowners may capture a large share of the surplus through capitalization. If labor supply is highly elastic through migration or commuting, firms may face less wage pressure. If commuting links the shocked place to outside residences, gains may accrue to workers who do not live in the treated geography.

This is the unifying logic behind local incidence work [@notowidigdo2020LocalDemandShocks; @suarezserratoWhoBenefitsState2016]. Students should leave this week unwilling to accept "a place got a positive shock" as a welfare statement. A credible paper must say whether the relevant outcome is workplace wages, residence-based incomes, rents, employment, population, home values, firm entry, or commuting flows.

### Equilibrium Adjustment In Wages, Rents, And Population

Housing-labor research is equilibrium work even when the design is reduced form. Let a local shock {math}`D_\ell` hit place {math}`\ell`. The observed response can be summarized as a vector:

```{math}
:label: eq:equilibrium-adjustment-week2
\Delta Y_\ell =
\left(
\Delta w_\ell,\,
\Delta R_\ell,\,
\Delta N_\ell,\,
\Delta E_\ell,\,
\Delta C_\ell,\,
\Delta P_\ell
\right),
```

where {math}`w` is wages, {math}`R` rents or housing costs, {math}`N` residents, {math}`E` employment, {math}`C` commuting flows, and {math}`P` prices or house values. The pattern of this vector is often more informative than any single coefficient.

For example, a demand shock with rising wages, rising rents, and little population growth points toward housing supply limits or entry constraints. Rising employment with strong in-commuting but weak residential growth points toward commuting as the adjustment margin. Rising house prices with weak renter gains points toward capitalization to incumbent owners. A strong paper makes this pattern explicit.

### Research Designs And Frontier Questions

The week uses roughly 15 papers, but the architecture matters more than the count. Students should read the papers as research roles:

```{include} assets/tables/02-paper-architecture-map.md
```

The buckets are cumulative. The foundational framework teaches why wages and rents must be interpreted together. The misallocation papers ask whether housing constraints block workers from productive places. The migration papers ask why workers fail to adjust when opportunities diverge. The commuting papers ask whether access can change without moving. The incidence papers ask who captures the gains from local shocks.

This field also has a recognizable design map:

```{include} assets/tables/02-methods-and-design-map.md
```

The design choice should follow the friction. Spatial-equilibrium and calibrated counterfactuals are natural when the question is aggregate misallocation or welfare incidence. Bartik-style or shift-share local demand shocks are natural when the question is how wages, rents, and employment adjust after labor demand changes. Housing-supply elasticity heterogeneity is useful when the hypothesis is price rather than population adjustment. Transport shocks help separate job access from residential migration. Migration event studies help identify timing, persistence, and heterogeneity in relocation.

The contribution margin is often narrow and important: identify which friction is binding. A paper may contribute by showing that the obstacle is not simply "housing" but housing supply regulation, liquidity, landlord capture, commuting technology, homeownership lock-in, or a mismatch between residential geography and workplace opportunity.

Several frontier questions are especially natural for urban-labor research:

- Which workers capture real access gains when high-productivity places expand housing?
- When does housing assistance improve labor-market adjustment rather than only reduce rent burden?
- How do wealth, credit, tenure, and family constraints shape migration responses to shocks?
- When does commuting technology substitute for migration, and when does it merely lengthen burdensome commutes?
- How much of the urban wage premium is available to low-wealth workers after rents and access costs are counted?
- Do local regulations change firm location and hiring enough to alter worker incidence?
- How should researchers measure labor markets when residence, workplace, commuting, and housing data disagree?

## Research Lab

The Week 2 lab should be a bounded teaching path rather than a full official replication. The workflow is **Reproduce -> Diagnose -> Transfer**.

**Primary anchor.** The main paper anchor is Hsieh and Moretti on housing constraints and spatial misallocation [@hsiehMoretti2019HousingConstraints]. Students should use the public replication materials when feasible, but the teaching target is narrower than rerunning the full quantitative model: construct the core city-level objects, compare constrained and less-constrained places, and ask whether high-productivity places adjust through rents, house prices, population, or worker access.

**Reproduce.** Students reproduce a small version of the paper's empirical architecture. They build or use a documented teaching extract with a city-level productivity or wage measure, rents or housing prices, population or employment, and a housing-supply or regulation measure. The output is a compact adjustment table: which places look productive, which places look housing constrained, and whether the observed response is mostly price adjustment, quantity adjustment, or real-access loss.

**Diagnose.** Students classify each result by margin: nominal wage, rent, house value, resident population, employment, commuting flow, and real access. The diagnostic questions are: Is the apparent friction housing supply, moving cost, sorting, or commuting access? Who captures the local surplus: workers, landlords, incumbent homeowners, firms, commuters, or excluded would-be migrants? What would be misread if the analysis reported wages without rents, or rents without population and access?

**Transfer.** The challenge anchor is Notowidigdo on the incidence of local labor-demand shocks [@notowidigdo2020LocalDemandShocks]. Students transfer the Hsieh-Moretti logic from high-productivity constrained places to a positive or negative local demand shock. They ask whether the same shock changes wages, rents, population, and worker composition symmetrically; whether low-skill workers face different real-access changes; and whether lower housing costs or transfers can partly insure immobile workers. The transfer should remain bounded: it can use a synthetic shock panel or public-use aggregate data, and it should state conservatively if it is not using an official replication package.

The lab trains four habits: interpret wages with rents, separate housing-supply constraints from moving frictions, describe adjustment as a vector rather than one coefficient, and state the incidence of local opportunity.

## Methods Box

:::{admonition} Methods Box: Data Used In Housing-Labor Research
:class: note

The practical skill this week is knowing what each data source can and cannot answer. Researchers usually combine labor, housing, mobility, and geography files rather than relying on a single dataset. The research design usually starts by deciding whether the outcome is residence-based, workplace-based, commute-flow-based, or housing-market-based.

```{include} assets/tables/02-data-sources-map.md
```

Three measurement choices deserve special care. First, geography is a design choice: commuting zones, metropolitan areas, counties, tracts, ZIP codes, and travel-time markets answer different questions. Second, tenure matters: renters, homeowners, voucher recipients, and would-be movers face different frictions. Third, residence-based and workplace-based data must be linked or interpreted separately. Without that discipline, a paper can confuse where jobs are located with who actually benefits.

:::

## Reading Ladder And References

**Foundations.** Start with Roback for the wages-rents-amenities logic, Moretti for local labor-market equilibrium, Diamond for heterogeneous location choice by skill, and Albouy and Lue for within-metro rents, wages, commuting, and quality of life [@roback1982; @moretti2011; @diamond2016LocationChoices; @albouyLue2015].

**Housing constraints and misallocation.** Use Hsieh and Moretti, Ganong and Shoag, Hoxie, Shoag, and Veuger, and Saiz to study how housing supply, regulation, geography, and rising housing costs shape spatial allocation [@hsiehMoretti2019HousingConstraints; @ganongShoag2017RegionalConvergence; @hoxieMovingDensityHalf2023; @saizGeographicDeterminantsHousing2010].

**Moving costs and migration adjustment.** Use Notowidigdo, Zabel, and Amior to ask how workers respond to local opportunities or decline, and how mobility differs by worker type and surplus [@notowidigdo2020LocalDemandShocks; @zabelMigrationHousingMarket2012; @amiorEducationGeographicalMobility2024].

**Commuting and within-metro access.** Use Monte, Redding, and Rossi-Hansberg, Severen, and Brough, Freedman, and Phillips to see commuting and transport access as labor-market adjustment margins [@monteReddingRossiHansberg2018; @severenCommutingLaborHousing2023; @broughEliminatingFaresExpand2025].

**Local shocks and incidence.** Use Notowidigdo, Suarez Serrato and Zidar, and Moretti's local multipliers to interpret who receives the surplus from local labor-demand or policy shocks [@notowidigdo2020LocalDemandShocks; @suarezserratoWhoBenefitsState2016; @morettiLocalMultipliers2010].

## Exercises And Discussion Prompts

1. A city has 20 percent higher nominal wages than a comparison city. List the data you need before calling it a better labor-market opportunity.
2. Suppose a local demand shock raises employment but also raises rents. Give one pattern of wages, rents, population, and commuting that would indicate worker gains, and one pattern that would indicate landlord or homeowner capture.
3. Choose one paper from the architecture map. What friction is it trying to identify? What alternative friction would generate similar reduced-form evidence?
4. Design a small empirical project using ACS PUMS, LEHD/LODES, and a rent or price measure. What is the labor outcome? What is the housing mechanism? What is the geography?
5. A new transit line reduces commute time to a high-wage job center. When would this look like a migration shock? When would it look like a commuting shock?

## Reproducibility And Code Lab Note

The Week 2 code lab lives at `labs/02-housing-rents-moving-costs-and-labor-market-adjustment/`. The code path should support the Research Lab rather than replace it. A bounded implementation can use public Hsieh-Moretti materials or a documented teaching extract, then add a small synthetic transfer exercise for local demand shocks. The smoke path should produce the core Week 2 objects: nominal wages, rents or prices, population or employment, real access, and an incidence diagnosis. It should state clearly when it is a teaching replication rather than an official replication package.

## Slide Companion Note

The Week 2 slide deck lives at `slides/week2/02-housing-rents-moving-costs-and-labor-market-adjustment.tex`. The deck follows the chapter's framework, but it is deliberately more compact: it defines the central question, introduces the labor-space-housing model, separates the main empirical margins, summarizes data sources, maps research designs, and ends with incidence takeaways.

## Bridge Forward

Week 3 shifts from aggregate housing and mobility constraints to unequal access inside metropolitan areas: spatial mismatch, segregation, neighborhoods, networks, and job access. The Week 2 lesson carries forward directly. Before interpreting unequal labor outcomes across neighborhoods, students must ask which jobs are reachable, which rents must be paid, which workers can move, and which adjustment margin is actually available.
