# Institutional Persistence, Path Dependence, and Historical Labor-Market Inequality

## Learning Objectives

By the end of Week 7, students should be able to:

1. distinguish serial correlation in fundamentals, path dependence, and institutional persistence through labor-market mechanisms;
2. explain how coercive labor systems, migration regimes, land, schooling, public goods, networks, and political rights can leave persistent marks on wages, mobility, occupations, and bargaining power;
3. evaluate historical identification designs without overclaiming persistence from long-run correlations alone;
4. identify the data sources used in historical labor research and the selection problems each source creates;
5. design a bounded persistence exercise that moves from reproduction to mechanism diagnosis to transfer.

## Opening Orientation

Week 7 asks why past labor institutions can keep shaping modern labor outcomes after the original legal rule, coercive regime, or political settlement has disappeared. The object is not "history matters" as a general slogan. The object is a labor-market mechanism: who can move, who can bargain, who receives schooling, which places receive roads and public goods, which networks transmit job information, and which groups retain political rights that affect labor allocation.

The week therefore sits between the identity and hierarchy material in Week 6 and the reform material in Week 8. Week 6 studied current systems of access. Week 7 asks why an institutional origin can survive through workers, firms, places, and public organizations. Week 8 then asks how contemporary reforms interact with those inherited structures.

:::{admonition} Core points
:class: important

- Persistence claims are convincing only when they name a labor mechanism, not just a long-run spatial or group correlation.
- Persistent fundamentals, path dependence, and institutional persistence are different objects.
- Coercion, migration restrictions, land institutions, schooling, public goods, networks, and political rights persist through different labor margins.
- Historical labor research is a data-production field: linked census records, archives, maps, courts, payrolls, newspapers, and GIS layers are often part of the contribution.
- The central warning is simple: do not call a pattern institutional persistence unless you can say which labor-market margin the old institution is still moving.

:::

## Bridge

Earlier weeks treated institutions as current constraints on labor exchange: enforcement capacity, informality, collective voice, norms, and hierarchy. Week 7 adds time. If a coercive labor regime ended long ago, why might workers in former treated areas still have lower schooling, different occupations, weaker outside options, or worse public goods? If mobility restrictions or public employment segregation have been formally removed, why might networks, skills, local demand, and employer beliefs continue to reproduce inequality?

The labor-economics discipline is to start from the outcome. A credible claim should move from historical exposure to a present labor margin: wages, employment, migration, occupation, formalization, school-to-work transition, bargaining power, employer concentration, public employment, job search, or mobility. Historical detail matters because it identifies which mechanism is plausible. But the chapter must not drift into generic economic history. The question is always how institutional origins shape work.

## Field Core

### Three Meanings Of Persistence

Persistence can mean at least three different things.

**Serial correlation or persistent fundamentals** means that a place or group has features that were important historically and remain important today. Geography, mineral endowments, disease environment, transport access, or urban potential may generate persistence without any institutional channel. If historical exposure simply proxies these fundamentals, the result is not yet evidence of institutional persistence.

**Path dependence** means that an initial shock moves an economy onto a trajectory that persists because of increasing returns, coordination, sunk costs, networks, or organizational lock-in. A temporary labor-demand shock can create skills, firms, migrant networks, or public infrastructure that later reproduce themselves.

**Institutional persistence through labor-market mechanisms** means that a past rule or institutional arrangement changes current labor allocation through concrete channels. A labor draft may weaken local public goods and worker outside options. Coercive contract enforcement may strengthen employer power and reduce mobility. Schooling exclusion may persist through human capital and occupational sorting. Political disenfranchisement may change local public finance and the protection workers receive.

A compact empirical object is:

```{math}
:label: eq:persistence-week7
Y_{it}^{labor} = \alpha + \beta H_i + \delta M_{it} + \gamma X_i + \lambda_t + \varepsilon_{it},
```

where {math}`Y_{it}^{labor}` is a labor outcome in place or group {math}`i` at time {math}`t`, {math}`H_i` is historical institutional exposure, {math}`M_{it}` is a measured labor mechanism, and {math}`X_i` captures persistent fundamentals. The interpretive question is not only whether {math}`\beta` is nonzero. It is whether the evidence supports a mechanism in which {math}`H_i` changes {math}`M_{it}`, and {math}`M_{it}` changes labor allocation.

:::{admonition} Warning: Do Not Overclaim Persistence
:class: warning

A long-run coefficient on historical exposure is a starting point, not a mechanism. A strong persistence claim should say what the historical treatment was, why nearby or otherwise comparable units are a credible counterfactual, which fundamentals are ruled out, which labor margin moved first, and why that margin can still matter today.

:::

### Labor Channels Of Institutional Persistence

Historical institutions persist through labor markets when they change worker outside options, employer power, skill formation, access to jobs, or local demand. The main channels this week are:

- **Labor coercion and employer power.** Forced labor, labor drafts, slavery, serfdom, and coercive contract enforcement can alter bargaining power, landholding, firm-worker relations, and mobility long after formal abolition.
- **Migration regimes and mobility constraints.** Pass systems, settlement restrictions, internal passports, deportations, or forced migration affect where workers settle, which networks form, and which labor markets they can enter.
- **Land, schooling, public goods, and occupational structure.** Property institutions and local public finance affect roads, schools, market access, occupations, and skill accumulation.
- **Networks, information, and political rights.** Community organizations, lineage, ethnic composition, voting rights, and local governance shape job information, public employment, enforcement, and worker protection.

```{include} assets/tables/07-persistence-channels-map.md
```

### Coercion, Labor Power, And Contract Enforcement

Coercive labor institutions are central because they directly govern workers' outside options. Dell's study of Peru's mining mita uses the historical boundary of a forced labor system to study persistent effects on modern outcomes [@dell2010mita]. The labor interpretation is not just that a colonial institution mattered. The mechanism runs through public goods, roads, market access, land tenure, and the long-run balance of power between workers, local elites, and employers.

Naidu and Yuchtman make the labor-contract channel even more explicit [@naiduYuchtman2013coercive]. Coercive contract enforcement in nineteenth-century industrial Britain changed workers' ability to quit and employers' ability to discipline labor. That setting helps students see that contract enforcement is not automatically protective. It depends on whose claims are enforceable. When enforcement strengthens employers' control over worker mobility, the labor margin is wages, separations, and bargaining power.

The lesson is portable. If historical coercion is the treatment, the modern labor mechanism cannot remain vague. Students should ask whether former coercive regions have different schooling, employer concentration, self-employment, migration, infrastructure, land access, or political protection. Without that labor margin, the claim risks becoming a generic legacy story.

### Migration Regimes, Mobility, And Occupational Structure

Mobility restrictions can persist because migration is cumulative. Once settlement patterns, origin networks, local information, and employer recruitment systems form, later workers face different moving costs and different job information. Forced migration can also change local public finance, housing markets, occupation composition, and political competition.

This channel is distinct from coercion even when the historical episodes overlap. A coercive labor system restricts outside options by binding workers to employers, estates, mines, or contracts. A migration regime structures where workers and families can move, whether credentials and networks travel, and which labor markets they can enter. Chevalier and coauthors' evidence on postwar forced migration and local public policies illustrates how displacement shocks can reshape local institutions with labor-market implications [@chevalierEtAl2024forcedmigration].

For labor economists, the key diagnostic is whether mobility constraints change worker allocation rather than only population composition. A credible paper should connect the historical shock to commuting, migration, occupational sorting, entrepreneurship, labor-force participation, or job access.

### Land, Schooling, Public Goods, And Occupations

Land and public goods matter because they shape both labor demand and skill formation. Serfdom, plantation systems, cadastral rules, local taxation, and public finance can influence land concentration, schools, roads, and local market access. These channels affect wages, migration, occupational mobility, and the composition of firms.

Markevich and Zhuravskaya study the abolition of serfdom in the Russian Empire as an institutional reform with large labor-market implications [@markevichZhuravskaya2018serfdom]. The reform changed mobility, competition, organization, and local economic structure. The point is not only that abolition increased output. It is that removing a labor-tied institution changed the allocation of workers and the bargaining environment.

Jones and Schmick provide a recent frontier anchor by linking Reconstruction-era education to long-run Black-White inequality [@jonesSchmick2025reconstruction]. This is exactly the kind of paper the course wants students to learn from: the historical institution is not a vague regional legacy, the mechanism is schooling and occupational standing, and the outcome is labor-market inequality.

### Wars, Political Shocks, And Reallocation

Wars, conflicts, and abrupt political shocks can create useful identifying variation, but they are rarely clean treatments. They move labor demand, destruction, migration, employer beliefs, public spending, discrimination, and political power at the same time. They are useful only when the paper narrows the labor mechanism.

Aizer, Boone, Lleras-Muney, and Vogel study World War II as a shock that changed labor-market opportunities and racial disparities [@aizerBooneLlerasMuneyVogel2020wwii]. Ferrara's work on wars and minority labor-market outcomes also keeps the mechanism tied to reallocation rather than treating war as a generic historical disruption [@ferrara2023wars]. For this week, the design question is whether war exposure affected labor demand, skill acquisition, migration, occupational openings, discrimination, or local political rights.

### Networks, Information, And Political Rights

Persistence can also operate through informal institutions and political access. Networks transmit job information, provide insurance, and discipline occupational choices. Political rights affect school finance, local public employment, worker protection, and enforcement. These channels often interact: restricted voting can weaken schools and public goods, which then changes skills and occupations; closed networks can insure workers while keeping them in low-return jobs.

The Week 6 caste-network material returns here as a persistence channel. Munshi and Rosenzweig show how traditional institutions can shape schooling and occupation choices [@munshiRosenzweig2006traditional]. In Week 7, the point is not identity per se. The point is how community institutions can reproduce labor allocation over time through information, insurance, and exit costs.

Comparative and global persistence work has also become more active. Laudares and Valencia Caicedo connect slavery legacies to Brazilian inequality [@laudaresValenciaCaicedo2023tordesillas]. Michalopoulos and Papaioannou synthesize historical legacies and development, which is useful for seeing the broader methodological terrain while keeping this course focused on labor mechanisms [@michalopoulosPapaioannou2020historical].

## Research Lab

The Week 7 lab uses **Reproduce -> Diagnose -> Transfer**.

**Reproduce.** Students use a reduced synthetic boundary dataset inspired by Dell [@dell2010mita]. The exercise compares formerly exposed and nearby non-exposed districts and summarizes labor outcomes such as schooling, wage index, nonfarm work, migration, infrastructure, and public goods. The point is to reproduce the logic of a historical boundary design without needing confidential data or the full original replication package.

**Diagnose.** Students then classify persistence claims. They ask whether each claim is serial correlation, path dependence, or institutional persistence through a labor mechanism. The diagnostic step forces them to name the historical treatment, the first moving labor margin, the modern outcome, the alternative fundamental, and the data weakness.

**Transfer.** Students map the same language to coercive contract enforcement [@naiduYuchtman2013coercive], serfdom abolition [@markevichZhuravskaya2018serfdom], Reconstruction schooling [@jonesSchmick2025reconstruction], war shocks [@aizerBooneLlerasMuneyVogel2020wwii; @ferrara2023wars], forced migration [@chevalierEtAl2024forcedmigration], and slavery legacies [@laudaresValenciaCaicedo2023tordesillas].

The bounded student path produces three objects:

1. a synthetic Dell-style reproduction table separating historical exposure from near-boundary comparison;
2. a persistence diagnostic table that names mechanism strength and overclaiming risk;
3. a transfer classification table that states what each historical design identifies and what it does not identify.

The lab lives at `labs/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality/`. It is a teaching analog, not an official replication of the anchor papers.

## Methods Box

Historical labor research is credible when design, mechanism, and data provenance move together. The common designs are useful because they create comparison groups, but each design has a characteristic failure mode.

:::{admonition} Methods box: historical identification in labor institutions
:class: note

1. **Historical border and discontinuity designs.** These use institutional boundaries, tax lines, colonial maps, or labor-draft borders to compare nearby units with different exposure. Dell is the anchor [@dell2010mita]. The main risk is that the boundary also tracks geography, administrative selection, or later policy.
2. **Wars, conflicts, and abrupt political shocks.** These use mobilization, defense demand, destruction, occupation, or conflict-induced reallocation. Aizer, Boone, Lleras-Muney, and Vogel and Ferrara are useful anchors [@aizerBooneLlerasMuneyVogel2020wwii; @ferrara2023wars]. The risk is bundled treatment.
3. **Regime abolition, liberalization, and institutional reform.** These use changes such as serf emancipation, Reconstruction schooling, labor-law reform, or legal abolition. Markevich and Zhuravskaya and Jones and Schmick are anchors [@markevichZhuravskaya2018serfdom; @jonesSchmick2025reconstruction]. The risk is simultaneous political, fiscal, and market change.
4. **Linked historical census and archival microdata.** These link people, households, schools, military records, payrolls, or courts over time. They are powerful for intergenerational and lifecycle labor questions. The risk is linkage bias, survival bias, and changing coverage.
5. **Lineage, ancestry, ethnic-share, and other persistence proxies.** These are useful when the mechanism plausibly runs through family, community, or group transmission. The risk is that the proxy mixes culture, institutions, selection, and current networks.
6. **Spatial and historical GIS designs.** These overlay old maps, cadastral records, roads, railroads, schools, conflict zones, and current labor outcomes. They are strongest when the labor mechanism is spatial access, market integration, public goods, or land institutions. The risk is boundary error, spatial correlation, and modern sorting.

:::

```{include} assets/tables/07-historical-methods-box.md
```

## Historical Data Sources

Historical labor-market research often begins by building the dataset. That data work is not ancillary. It determines what mechanisms can be tested and which claims are too fragile.

:::{admonition} Data sources box: where historical labor researchers get evidence
:class: tip

- **Historical census and linked census data** measure occupation, literacy, household structure, migration, and sometimes earnings proxies.
- **Archives and court or labor-contract records** reveal enforcement, breach, quitting, disputes, payrolls, apprenticeships, and employer discipline.
- **School, parish, and local public-goods archives** measure education, public finance, teacher supply, roads, poor relief, hospitals, and local state presence.
- **Cadastral maps, colonial maps, and GIS layers** locate historical boundaries, landholding, transport, schools, mines, plantations, and market access.
- **War, conflict, military, and defense records** measure mobilization, destruction, occupation, veteran status, and wartime labor demand.
- **Administrative records and digitized newspapers** can reveal public employment, legal implementation, strikes, vacancies, worker knowledge, and employer discourse.

:::

```{include} assets/tables/07-historical-data-sources-map.md
```

## Reading Ladder And References

**Core coercion and labor power.** Start with Dell on the mining mita and Naidu and Yuchtman on coercive contract enforcement [@dell2010mita; @naiduYuchtman2013coercive].

**Institutional abolition and reform.** Read Markevich and Zhuravskaya on serfdom abolition as a major labor-market institutional change [@markevichZhuravskaya2018serfdom].

**Wars and reallocation.** Use Aizer, Boone, Lleras-Muney, and Vogel and Ferrara to study war as a labor-demand, discrimination, migration, and occupational-opening shock [@aizerBooneLlerasMuneyVogel2020wwii; @ferrara2023wars].

**Schooling, public goods, and race.** Read Jones and Schmick for a recent frontier paper linking historical education policy to long-run Black-White labor inequality [@jonesSchmick2025reconstruction].

**Comparative and global frontier.** Use Laudares and Valencia Caicedo and Chevalier and coauthors for global and forced-migration extensions [@laudaresValenciaCaicedo2023tordesillas; @chevalierEtAl2024forcedmigration].

```{include} assets/tables/07-frontier-and-reading-map.md
```

## Exercises And Discussion Prompts

1. Choose one persistence claim from the reading ladder. Classify it as persistent fundamentals, path dependence, or institutional persistence through a labor mechanism. What evidence would move it from one category to another?
2. Use equation {eq}`eq:persistence-week7` to describe a historical schooling channel. What is {math}`H_i`, what is {math}`M_{it}`, and what belongs in {math}`X_i`?
3. In Dell's setting, why is the labor mechanism not exhausted by the historical mita boundary? Which modern labor outcomes and public-goods channels must be examined?
4. Compare coercive contract enforcement and forced migration. How do they restrict labor allocation differently?
5. Design a historical GIS exercise for a labor question. What old map would you digitize, what current labor outcome would you link, and what spatial threat would worry you most?
6. Take a war or abolition shock. Name the bundled mechanisms and then isolate one labor margin that could be credibly studied.

## Reproducibility And Code Lab Note

The Week 7 lab is a reduced pedagogical path. It does not use the original Dell replication files, British court records, Russian serfdom data, linked Reconstruction census files, confidential administrative data, or proprietary archival material. Instead, it creates deterministic synthetic datasets that mimic the structure of the research designs students need to understand.

The smoke test runs only this bounded path: build synthetic data, reproduce a Dell-style boundary comparison, diagnose persistence mechanisms, and classify transfer designs. The goal is conceptual discipline and local reproducibility, not a full historical replication.

## Slide Companion Note

The Week 7 slide deck lives at `slides/week7/07-institutional-persistence-path-dependence-and-historical-labor-market-inequality.tex`. The deck defines the central question, explains why historical institutions belong in labor economics, distinguishes persistence concepts, covers coercion, mobility, schooling, public goods, methods, data sources, representative papers, and the bridge to Week 8.

## Bridge To Week 8

Week 7 explains why past institutions can survive through labor-market channels. Week 8 turns from persistence to reform. The next question is why similar reforms produce different effects when they arrive in places with different inherited employer power, mobility costs, public goods, schooling gaps, networks, political rights, and administrative capacity.
