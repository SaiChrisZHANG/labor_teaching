---
title: Institutional Persistence, Path Dependence, and Historical Labor-Market Inequality
bibliography:
  - references.bib
---

# Week 7. Institutional Persistence, Path Dependence, and Historical Labor-Market Inequality

## Opening orientation

This week asks why labor institutions continue to matter long after the original legal rule, coercive regime, or reform has disappeared. The goal is not to treat “history” as a residual explanation. The goal is to understand the specific labor-market channels through which past institutions survive: skills, mobility, contract enforcement, occupational sorting, employer power, local public goods, networks, and unequal access to jobs.

```{admonition} Core points
:class: important
- Persistence claims are convincing only when they are tied to a **labor mechanism**, not just a long-run correlation.
- The key distinction is between **persistent fundamentals**, **path dependence**, and **institutional persistence through labor-market channels**.
- Historical labor research often studies coercive labor systems, migration regimes, land and schooling institutions, local public goods, and political rights because all of them shape later labor allocation.
- Strong papers combine historical identification with unusually careful data work: linked census records, archives, GIS, court records, and institutional maps.
- This literature is empirically rich but methodologically tricky; design choice and data provenance matter as much as the headline result.
```

## Bridge

Earlier weeks studied formal institutions, enforcement, informality, worker voice, and norms in contemporary labor markets. This week asks how those same institutions cast a long shadow. The emphasis is labor economics: why do old institutions still shape who works, where they move, which jobs they can access, how much bargaining power they have, and how unequal labor outcomes remain?

## Field Core

### 1. What counts as persistence?

The chapter should begin by separating three ideas that are often conflated:

1. **Persistent fundamentals**: geography, disease environment, transport, or other baseline conditions that continue to matter directly.
2. **Path dependence**: temporary shocks that move an economy onto a persistent trajectory because of increasing returns, networks, or organizational lock-in.
3. **Institutional persistence through labor channels**: formally abolished rules continue to matter because they altered skills, mobility, employer power, information networks, political rights, or local public goods in ways that still shape labor allocation.

A useful organizing expression is:

```{math}
:label: eq:persistence
Y_{it}^{labor} = \alpha + \beta H_i + \gamma X_i + \varepsilon_{it},
```

where {math}`H_i` is historical institutional exposure and {math}`X_i` captures persistent fundamentals. The empirical problem is to give {math}`\beta` a labor-market interpretation, not just a reduced-form persistence interpretation.

### 2. Main labor-market channels of persistence

The chapter should organize the literature around a small number of labor channels:

- **Coercion and employer power**: historical labor drafts, serfdom, slavery, or coercive contract enforcement can shape later bargaining power, landholding, employer concentration, and outside options.
- **Migration and mobility regimes**: pass systems, settlement restrictions, internal passports, or forced migration alter where workers can move and which labor markets they can enter.
- **Schooling and skill formation**: historical access to schools, teachers, and public finance changes later occupational standing and earnings.
- **Land and local public goods**: property institutions, local taxation, roads, and state presence shape market access and labor demand.
- **Networks and occupational structure**: lineage, community organization, and inherited occupational niches change search, matching, and entrepreneurship.

The chapter should repeatedly ask: *which labor margin is the historical institution still moving today?*

### 3. Representative empirical domains

#### Coercive labor systems and labor power
Use [@dell2010mita] and [@naiduYuchtman2013coercive] as benchmark anchors. Dell is useful because the mita boundary gives a historically grounded spatial discontinuity with clear labor-market channels through public goods, roads, and labor coercion. Naidu and Yuchtman is useful because it shows how contract-enforcement rules directly alter labor mobility and wages in a modern labor-economics language.

#### Abolition and institutional reform
Use [@markevichZhuravskaya2018serfdom] as a canonical case where a major institutional reform changes labor markets through competition, mobility, and organizational restructuring. The question is not only whether abolition raised output, but who gained, who lost, and which labor margins adjusted.

#### Wars, shocks, and labor-market reallocation
Use [@aizerBooneLlerasMuneyVogel2020wwii] and [@ferrara2023wars] to show how war shocks can be used as treatments, but only if the labor mechanism is explicit: labor shortages, employer demand, occupational openings, or discrimination changes. The point is not “war matters,” but how war temporarily or permanently changed labor-market access.

#### Reconstruction, schooling, and long-run labor inequality
Use [@jonesSchmick2025reconstruction] as a recent anchor. It is ideal for this course because it ties historical education policy directly to later occupational standing and long-run Black–White labor-market inequality.

#### Frontier comparative/global extensions
Use [@laudaresValenciaCaicedo2023tordesillas] and [@chevalierEtAl2024forcedmigration] as optional frontier references to show where the literature is moving: slavery legacies in Brazil, postwar forced migration, public policy, and local political economy with labor-market implications.

## Methods box

```{admonition} Methods box: historical identification in labor institutions
:class: note
Historical labor research typically relies on a limited set of design families. Students should know both the opportunity and the risk in each one.

1. **Historical border/discontinuity designs**
   - Use institutional boundaries that plausibly changed exposure while leaving nearby places otherwise comparable.
   - Representative anchor: [@dell2010mita].
   - Main risk: boundaries may also proxy for persistent geography or administrative selection.

2. **Wars, conflicts, and abrupt political shocks as treatments**
   - Use wartime mobilization, defense demand, destruction, occupation, or conflict-induced reallocation.
   - Representative anchors: [@aizerBooneLlerasMuneyVogel2020wwii], [@ferrara2023wars].
   - Main risk: war is rarely a clean labor-market treatment unless the mechanism is tightly specified.

3. **Regime abolition / liberalization / institutional reform**
   - Use abrupt changes in coercive systems, labor law, or access to schools/property.
   - Representative anchors: [@markevichZhuravskaya2018serfdom], [@jonesSchmick2025reconstruction].
   - Main risk: reforms often bundle many changes at once.

4. **Linked historical microdata**
   - Link historical census records, school records, military records, or archival personnel data to later outcomes.
   - Representative anchor: [@jonesSchmick2025reconstruction].
   - Main risk: linkage bias, survival bias, and coverage shifts.

5. **Lineage / ancestry / ethnic-share persistence proxies**
   - Use surnames, ethnic homelands, ancestry shares, or historical population composition to track persistence.
   - Useful when institutions operate through family, community, or ethnic transmission.
   - Main risk: these proxies often mix cultural transmission, networks, and selection.

6. **Historical GIS and map-based designs**
   - Combine old maps, cadastral records, boundaries, roads, and topography with current labor-market outcomes.
   - Strong when the labor mechanism runs through spatial access, market integration, or property institutions.
```

## Historical data sources

```{admonition} Data sources box: where historical labor researchers get evidence
:class: tip
Students interested in this literature should think about data collection as part of the research contribution.

- **Historical census and linked census microdata**
  - IPUMS, linked full-count census, population registries, military draft files.
- **Archives and court/labor-contract records**
  - labor contracts, apprenticeship books, court cases, personnel registers, payroll ledgers.
- **School, parish, and local public-goods records**
  - teacher counts, school finance, parish registers, poor relief, local tax records, roads and hospitals.
- **GIS layers and historical maps**
  - colonial maps, cadastral maps, railroads, district boundaries, mining zones, settlement lines.
- **War/conflict and displacement data**
  - military production, bombing/destruction, occupation zones, veteran records, forced migration flows.
- **Digitized newspapers and legal texts**
  - labor disputes, strikes, legal changes, local employer/worker discourse, vacancy advertisements.
```

## Research Lab

This week should be unusually explicit about research design because many students will be interested in this area but may not know how to start.

### 1. Reproduce -> Diagnose -> Transfer
Suggested lab structure:
- **Primary anchor**: [@dell2010mita]
- **Challenge anchor**: [@naiduYuchtman2013coercive]
- **Optional extension**: [@jonesSchmick2025reconstruction] or [@markevichZhuravskaya2018serfdom]

Students should learn to ask:
- What exactly is the historical treatment?
- What is the labor-market mechanism?
- What modern outcome is being moved?
- What data linkage or boundary logic makes the design credible?
- What alternative persistence story could explain the same fact?

### 2. Common failure modes
- historical treatment is clear but the labor mechanism is vague
- persistence claim is really a geography claim
- linked historical sample is selective
- reform timing is used as if it were random
- current outcome is interesting but too far removed from labor allocation
- archival source is rich but not representative

### 3. Research opportunities
This is a good week to encourage students to think about:
- labor-market consequences of institutional reforms whose formal rules ended decades ago
- persistent employer power after coercive labor institutions
- historical schooling/public-goods gaps and modern occupational inequality
- persistence through mobility restrictions or internal migration controls
- historical local governance and modern labor-market protection
- new digitized archives, full-count census linkages, and historical GIS as a source of feasible projects

## Reading ladder

A strong minimum ladder should separate:
- **core coercion and labor power**: [@dell2010mita], [@naiduYuchtman2013coercive]
- **institutional reform / abolition**: [@markevichZhuravskaya2018serfdom]
- **wars and labor reallocation**: [@aizerBooneLlerasMuneyVogel2020wwii], [@ferrara2023wars]
- **recent frontier / education / race**: [@jonesSchmick2025reconstruction]
- **optional comparative/global frontier**: [@laudaresValenciaCaicedo2023tordesillas], [@chevalierEtAl2024forcedmigration]

## Forward bridge

The next week can build naturally from this one by asking how persistent institutions shape contemporary reform, implementation, and comparative development. This week is about why the past survives. The next step is to ask how modern institutional change interacts with those inherited labor-market structures.
