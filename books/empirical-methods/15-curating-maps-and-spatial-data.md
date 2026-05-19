# Lecture 15. Curating Maps And Spatial Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain why spatial data construction is part of empirical design rather than clerical GIS work;
2. distinguish points, polygons, rasters, networks, and panel geographies as different empirical objects;
3. defend a geography choice in light of the economic mechanism, population, and estimand;
4. construct and critique access, exposure, distance-decay, and boundary-crosswalk measures;
5. diagnose MAUP, geocoding error, temporal mismatch, endogenous boundary choice, aggregation bias, edge effects, and support problems;
6. design a reproducible spatial-data workflow suitable for applied economics research.

## Opening Orientation

Spatial data enter applied economics whenever the mechanism depends on **where** workers, firms, schools, housing, transport, pollution, institutions, or public services are located. The practical work can look like collecting coordinates, cleaning shapefiles, geocoding addresses, choosing a projection, building crosswalks, or calculating travel times. But the economic work is deeper: the researcher is deciding what a place is, which people or firms are exposed to which locations, and how distance or borders enter the behavior being studied.

The central question is: **how do researchers turn places, borders, distances, and exposure measures into usable empirical objects?** A commuting zone, census tract, school catchment, buffer around a plant, distance band around a transit station, or travel-time isochrone is not merely a data container. It is a claim about the relevant market, neighborhood, policy jurisdiction, search set, or exposure technology.

The paper spine is deliberately applied. Autor, Dorn, and Hanson use commuting zones to study how import competition affected local labor markets, making the local labor-market definition part of the estimand [@autorDornHanson2013]. Chetty, Hendren, and Katz use neighborhood exposure to study childhood environments and mobility, making tract-level place construction central to interpretation [@chettyHendrenKatz2016]. Monte, Redding, and Rossi-Hansberg model commuting and migration responses, reminding us that local labor markets are connected through worker flows rather than isolated boxes [@monteReddingRossiHansberg2018]. Miller studies job suburbanization and Black employment, where access is about the location of jobs relative to workers rather than a generic county average [@miller2018]. Donaldson and Hornbeck provide a market-access example in which networks and trade costs define the economic object [@donaldsonHornbeck2016].

The lecture's claim is conservative. Spatial curation is not spatial causal inference. It does not, by itself, solve sorting, spillovers, correlated shocks, or endogenous treatment placement. But weak spatial curation can defeat a strong downstream design. If geography, exposure, crosswalks, and travel costs are mismeasured, the next lecture's causal tools will be answering the wrong question.

## Core Points

:::{admonition} Core points
:class: important

- Spatial data work is part of research design because geography choice, exposure construction, crosswalks, and travel-cost measurement help define the estimand.
- Points, polygons, rasters, networks, and panel geographies encode different mechanisms and therefore create different advantages, errors, and confidentiality risks.
- Distances, buffers, spatial joins, and aggregation rules are not neutral preprocessing steps. They embed assumptions about mobility, access, interaction, and jurisdiction.
- Exposure measures such as {math}`E_i=\sum_j w_{ij}s_j` require the researcher to justify both the shock or opportunity {math}`s_j` and the spatial weights {math}`w_{ij}`.
- Crosswalks and boundary harmonization are measurement choices. Area weights, population weights, residence weights, workplace weights, and flow weights answer different questions.
- A defensible spatial workflow reports sensitivity to plausible geographies, boundary choices, buffer radii, geocoding quality thresholds, travel-cost definitions, and confidentiality masking.
- Spatial curation ends when the empirical objects are defined, validated, and documented. Spatial causal inference begins when the researcher claims a counterfactual effect, spillover, or equilibrium response.
:::

## Bridge

Lecture 15 opens the optional spatial-methods block by moving one step earlier than causal inference or quantitative spatial modeling. Lectures 3 to 5 studied designs that often use places as units. Lecture 8 introduced spatial equilibrium as a structural environment. This lecture asks what must happen before either kind of analysis can be credible: the researcher must create the empirical objects called "place," "distance," "access," and "exposure."

```{include} assets/tables/15-spatial-data-concepts-map.md
```

The bridge from previous modules is simple. A DID design using counties, an IV design using commuting-zone shocks, a prediction exercise using satellite rasters, a structural model using travel costs, or a text workflow geocoding job ads all inherit the spatial choices made upstream. When those choices are undocumented, the estimand is partly hidden.

## Field Core

### A. Spatial Data Are Economic Objects

Spatial data encode economic primitives: access, proximity, exposure, agglomeration, local public goods, jurisdiction, transportation frictions, and neighborhood environments. A worker's feasible set often depends on generalized travel cost to jobs:

```{math}
:label: eq:em15-generalized-travel-cost
c_{ijm} = \tau_m t_{ijm} + \pi_m d_{ijm} + \kappa_m,
```

where {math}`t_{ijm}` is travel time from residence {math}`i` to opportunity {math}`j` by mode {math}`m`, {math}`d_{ijm}` is distance or route length, {math}`\tau_m` converts time into money-metric or utility cost, and {math}`\kappa_m` captures fixed costs such as transit transfers, parking, reliability, or search frictions. A straight-line distance is one possible proxy, not the object itself.

Many place-based empirical variables are exposure measures:

```{math}
:label: eq:em15-spatial-exposure
E_i = \sum_j w_{ij} s_j,
```

where {math}`s_j` is a shock, opportunity, amenity, disamenity, policy, or characteristic at location {math}`j`, and {math}`w_{ij}` encodes how geography mediates exposure. Weights can be adjacency indicators, inverse distances, commuting shares, residence histories, school catchment rules, flow shares, market-access weights, or model-implied probabilities.

A common distance-decay form is:

```{math}
:label: eq:em15-kernel-exposure
w_{ij}(h)
=
\frac{K(d_{ij}/h)}
{\sum_{\ell}K(d_{i\ell}/h)},
```

where {math}`K(\cdot)` is a kernel and {math}`h` controls the spatial bandwidth. A small {math}`h` says exposure is very local; a large {math}`h` says farther locations remain relevant. The bandwidth is therefore an economic assumption, not only a smoothing parameter.

Spatial choices also enter structural or equilibrium objects. A simple net-value expression for choosing job or location {math}`j` from residence {math}`i` is:

```{math}
:label: eq:em15-net-value
V_{ij}=w_j-r_i+A_i-c_{ij}+\varepsilon_{ij},
```

where wages, rents, amenities, and travel costs together define the value of a spatial option. In this object, a travel-time matrix, a rent geography, and an amenity geography all matter for the interpretation of {math}`V_{ij}`.

### B. Geography Choice Defines The Estimand

The estimand should determine the geography, not the other way around. A county, tract, commuting zone, labor market, school zone, ZIP code, grid cell, or isochrone answers a different question even when the same raw data are underneath.

In Autor, Dorn, and Hanson, the commuting zone is useful because the object is a local labor market exposed to import competition through its pre-existing industry mix [@autorDornHanson2013]. If the same shock were assigned to counties, the estimate would place more weight on administrative boundaries that may split commuting flows. If assigned to states, it would wash out much of the within-state labor-market heterogeneity. If assigned to tracts, it might overstate the precision of a shock that operates through a regional labor market.

In neighborhood-exposure work, the logic changes. Chetty, Hendren, and Katz study children's exposure to better neighborhoods, so fine local environments and timing of residence matter [@chettyHendrenKatz2016]. A commuting zone average would be too coarse for that mechanism. A block, tract, or neighborhood measure is closer to the relevant exposure, though it raises new concerns about sorting, confidentiality, and boundary stability.

In job-access work, the natural object may be neither the residential tract nor the county. Miller's job suburbanization setting asks whether employment opportunities moved away from Black workers, so travel costs and the geography of workplaces relative to residences are central [@miller2018]. The measurement object is closer to reachable jobs than to average local characteristics.

Monte, Redding, and Rossi-Hansberg push the point further by modeling commuting and migration adjustment across locations [@monteReddingRossiHansberg2018]. A local shock does not stay inside a polygon when workers commute or move. This does not mean every curation lecture must solve a full spatial equilibrium model. It does mean that the chosen geography should be explicit about whether the mechanism is residence, workplace, commute, migration, market access, or jurisdiction.

### C. Main Spatial Data Objects

**Points.** Points represent addresses, workplaces, plants, schools, clinics, transit stops, inspections, events, or geocoded documents. They are best when exact location matters for distance, nearest-neighbor access, routing, buffers, or clustering. The risks are geocoding error, confidentiality, false precision, and sample selection if failures are systematic. Exact coordinates often cannot be released, and jittering can change distance-based assignment near boundaries.

**Polygons.** Polygons represent tracts, ZIP codes, counties, municipalities, school zones, service areas, commuting zones, or labor markets. They align well with administrative data and policy rules. Their risks are MAUP, ecological fallacy, boundary arbitrariness, changing boundaries, and the possibility that the polygon is a poor proxy for the mechanism. A county may be a tax jurisdiction, a commuting zone may be a functional labor market, and a tract may be a neighborhood proxy. They are not interchangeable.

**Rasters.** Rasters store gridded surfaces such as pollution, temperature, land cover, night lights, population density, elevation, flood risk, or satellite-derived poverty proxies. They are useful for environmental exposure, terrain, and remote sensing. The key choices are pixel resolution, temporal resolution, aggregation rule, and whether exposure should be assigned to residences, workplaces, schools, routes, or time-weighted activity spaces.

**Networks.** Networks encode roads, rail, transit, walking routes, commute links, supply chains, or migration flows. They are essential when access depends on routes, congestion, mode, transfers, or bottlenecks. The main risks are computational burden, proprietary or changing routing algorithms, schedule assumptions, missing historical networks, and mode-specific feasibility. A travel-time API call is not automatically reproducible unless the query time, routing mode, departure assumptions, and API version are recorded.

**Panel geographies.** Panel geographies track places over time: tracts split, counties change boundaries, school zones are redrawn, commuting zones are redefined, roads are built, transit schedules change, and people move. Panel spatial work requires harmonization choices. Holding boundaries fixed can improve comparability but may obscure real institutional change. Letting boundaries change can reflect policy reality but may create artificial jumps in measured exposure.

```{include} assets/tables/15-data-sources-and-geographies-map.md
```

### D. Core Operations And Their Design Content

**Geocoding.** Geocoding transforms addresses or place names into coordinates. Researchers should preserve raw address strings separately from cleaned coordinates; record provider, date, match score, match type, and failure reason; inspect a sample of matches and nonmatches; and rerun key results under stricter match-quality rules. Historical addresses, rural locations, informal addresses, employer names, and post-office boxes can fail in ways correlated with income, race, industry, or region.

**Projections and coordinate systems.** Distances and areas require an analysis coordinate reference system. Latitude and longitude are angular coordinates, not a safe default for economic distance calculations. A defensible workflow records the CRS of each input layer, transforms layers into a projected CRS appropriate for the study region, and distinguishes visualization choices from analysis choices. The projection is part of the audit trail.

**Spatial joins.** A spatial join assigns points to polygons, overlays polygons on polygons, attaches raster values to points or areas, or finds nearest features. The researcher must state whether the rule is "within," "intersects," "centroid within," "largest overlap," "nearest," or "distance threshold." Edge cases are not minor when policy eligibility, neighborhood assignment, or treatment status changes at a boundary.

**Buffers and distance bands.** Buffers define zones around points, lines, or polygons. They are useful around plants, transit stops, roads, schools, hazards, and borders. The radius should be motivated by the mechanism and tested over plausible alternatives. Buffers discretize exposure and can ignore barriers, transit topology, rivers, highways, and jurisdictional edges. A one-mile circle can be a poor commute proxy in a city with uneven transit.

**Distance and travel-time construction.** Researchers should distinguish Euclidean distance, great-circle distance, network distance, travel time, generalized cost, and observed commuting flows. For labor-market access, straight-line distance is usually a fallback, not the first-best object. A travel-time matrix should document origin and destination definitions, mode, departure time, congestion assumptions, routing source, and missing routes. Historical travel times require special humility because current networks may not represent past access.

**Boundary crosswalks.** Crosswalks map one geography into another: tracts to counties, ZIP codes to tracts, PUMAs to counties, historical tracts to current tracts, blocks to commuting zones, or school zones to neighborhoods. The weighting rule defines the interpretation. Area weights transfer land; population weights transfer residents; employment weights transfer jobs; residence-workplace flow weights transfer labor-market connections. A crosswalk can create real measurement error, especially when a source unit is split across target units.

**Aggregation.** Aggregation to commuting zones, tracts, counties, or labor markets should match the object. Local labor-demand shocks often use pre-period employment weights, as in the commuting-zone logic of Autor, Dorn, and Hanson [@autorDornHanson2013]. Job-access measures often aggregate jobs reachable within travel-cost bands or distance-decay weights. Neighborhood measures often aggregate over residence histories or childhood exposure windows. The denominator matters: per resident, per worker, per child, per job seeker, or per baseline worker are different objects.

**Confidentiality and disclosure control.** Spatial data are often high-risk because exact residence and workplace locations can reidentify people or firms. Masking, jittering, rounding, suppressing cells, aggregating to larger geographies, or using secure enclaves may be necessary. These are not only legal choices. They can alter treatment assignment, distance measures, exposure gradients, and subgroup comparability. A paper should say how disclosure control affects interpretation.

### E. Crosswalks, Weights, And Exposure Algebra

Crosswalks deserve their own notation because they often decide what the empirical variable means. Suppose source geography {math}`g` must be assigned to target geography {math}`h`. Let {math}`a_{gh}` be the share of source unit {math}`g` assigned to target unit {math}`h`. A harmonized variable can be written:

```{math}
:label: eq:em15-crosswalk
X_h = \sum_g a_{gh} X_g.
```

The formula is simple; the economics is not. If {math}`a_{gh}` is an area share, {math}`X_h` is a land-based allocation. If {math}`a_{gh}` is a population share, it is a resident-based allocation. If {math}`a_{gh}` is a workplace share, it is a job-based allocation. If it is a commuting-flow share, it is a labor-market connection. A crosswalk built for one interpretation should not silently be used for another.

Exposure measures also need denominators. A local labor-market shock might be:

```{math}
:label: eq:em15-shift-share-exposure
E_g = \sum_k \left(\frac{L_{gk,0}}{L_{g,0}}\right)\Delta s_k,
```

where {math}`L_{gk,0}` is baseline employment in industry {math}`k` and geography {math}`g`, and {math}`\Delta s_k` is an industry shock. This is a curation object before it is an instrument, treatment, or causal variable. It depends on the local labor-market definition, baseline year, industry classification, denominator, and whether {math}`g` is a county, commuting zone, or some other market.

### F. Pitfalls That Change The Economics

**MAUP and arbitrary unit choice.** Results can change when the same underlying points are aggregated to blocks, tracts, ZIP codes, counties, or commuting zones. That is not a software bug. It means different units correspond to different mechanisms and different sources of variation.

**Geocoding error.** Mislocated residences, workplaces, schools, or plants can bias exposure, treatment assignment, distance bands, and nearest-neighbor measures. Errors are often systematic: rural areas, low-income addresses, informal settlements, historical records, and multi-establishment firms may geocode poorly.

**Temporal mismatch.** Outcomes, addresses, boundaries, roads, transit schedules, covariates, and shocks are often observed in different years. A tract measured in 2020 may be the wrong place object for a childhood exposure in 1990 or a commute decision in 2005.

**Endogenous boundary choice.** Choosing a geography, radius, or access measure after seeing the result is design search. Plausible alternatives should be motivated before estimation and reported systematically.

**Ecological fallacy and aggregation bias.** Area-level associations do not automatically identify individual mechanisms. A tract with high poverty and low employment does not prove that a particular resident's outcome is caused by tract poverty.

**Edge effects.** Units near the edge of a study area or policy boundary may have exposure just outside the observed geography. Dropping outside opportunities can understate access for border places.

**Support and comparability.** Some places have no comparable controls, no nearby jobs, no valid routes, or no overlap in covariates. Spatial support problems can be hidden when maps look complete but the empirical comparison is thin.

Gibbons and Overman warn that spatial econometrics can become "mostly pointless" when researchers add spatial terms without a clear economic object [@gibbonsOverman2012]. The curation analogue is similar: a beautiful map does not make the empirical geography valid.

### G. Rules Of Thumb For Defensible Spatial Work

```{include} assets/tables/15-practical-rules-and-pitfalls.md
```

For applied economics, the checklist can be sharpened:

1. State the mechanism before opening the map file.
2. Define the unit of observation, unit of exposure, and unit of variation separately.
3. Keep raw identifiers, coordinates, shapefiles, and crosswalks immutable; write cleaned versions as derived data.
4. Record CRS, geocoder, routing source, API date, shapefile vintage, and crosswalk version.
5. Inspect edge cases visually and numerically, especially around boundaries and missing routes.
6. Use travel time or generalized cost when commuting, job access, or service access is the mechanism.
7. Report at least one alternative plausible geography or bandwidth when the mechanism is uncertain.
8. Separate measurement sensitivity from causal robustness. Both matter, but they answer different questions.
9. Explain confidentiality masking as a measurement decision, not only as a data-use constraint.
10. Make the workflow rerunnable without requiring hidden manual GIS clicks.

### H. Where Curation Ends And Causal Inference Begins

Spatial curation produces empirical objects: geographies, assignments, exposures, distances, access measures, and harmonized panels. Spatial causal inference asks whether variation in those objects identifies a counterfactual effect. The boundary is important.

After curation, a researcher may have a commuting-zone import exposure, tract-level neighborhood measure, job-access index, pollution raster aggregated to residences, or travel-time matrix. Those objects still do not identify effects by themselves. The next step requires assumptions about treatment assignment, sorting, spillovers, interference, correlated shocks, anticipation, migration, and inference under spatial dependence. Conley-style dependence, border designs, spillover mappings, and place-based identification belong mainly in Lecture 16 [@conley1999].

The right standard for Lecture 15 is therefore: can another researcher understand what spatial object was built, why it matches the mechanism, how sensitive it is to plausible alternatives, and what errors remain before the causal design begins?

## Research Lab

The Week 15 lab follows the standard **Reproduce -> Diagnose -> Transfer** structure. It is a bounded synthetic teaching path, not an official replication package. The primary anchor is the commuting-zone exposure logic in Autor, Dorn, and Hanson [@autorDornHanson2013]. The challenge paper is Miller's job-access and job-suburbanization setting, where finer geography and travel costs matter for the empirical object [@miller2018]. Chetty, Hendren, and Katz provide an additional reference point for fine neighborhood exposure and timing [@chettyHendrenKatz2016].

### Reproduce

Students reproduce a simplified local labor-market exposure measure. The synthetic data contain tract-level baseline employment by industry, a tract-to-commuting-zone assignment, and industry shocks. Students:

- aggregate tracts to commuting zones using baseline employment weights;
- construct a shift-share exposure of the form in Equation {eq}`eq:em15-shift-share-exposure`;
- assign the commuting-zone exposure back to tracts;
- compare the object with a county-based version of the same shock;
- estimate a simple descriptive relationship between exposure and synthetic employment growth.

The purpose is not to estimate the China shock. It is to make visible how the geography and weights define the local labor-market exposure object.

### Diagnose

Students diagnose how spatial choices change interpretation:

- What mechanism is assumed by commuting zones rather than counties or tracts?
- Which tracts are sensitive to crosswalk weighting rules?
- How much does the exposure distribution change under county aggregation?
- Which places are near boundaries where edge effects and commuting flows matter?
- How would geocoding jitter or confidentiality masking alter distance-based assignment?

The Diagnose memo must separate measurement sensitivity from causal identification. A stable exposure measure does not prove exogeneity; an unstable exposure measure means the downstream design is already fragile.

### Transfer

Students transfer the curation logic to a job-access problem inspired by job suburbanization research [@miller2018]. Using synthetic residences, workplace centers, and travel-cost parameters, they:

- construct Euclidean buffer access;
- construct distance-decay access;
- construct travel-time access using a generalized cost matrix;
- compare access measures for groups with different residential locations and transit penalties;
- write a short memo explaining which access object matches the economic question.

The transfer task previews Lecture 16 without turning it into a causal claim. The output is a documented access measure and a design memo, not an effect estimate.

## Methods Box

### Practical Tools And Caveats

Common tools include `sf` in R and `geopandas` in Python for vector geometries, `terra`, `raster`, `xarray`, and related geospatial stacks for raster data, GTFS and routing tools for transit networks, and dedicated crosswalk files for harmonizing Census and administrative geographies. These tools are useful only when the workflow records the empirical choices they implement.

**Vector data.** Use simple-features objects for points, lines, and polygons; validate geometries; check CRS before distance calculations; and make joins explicit. Pebesma's `sf` paper is a useful practical reference for standardized vector operations [@pebesma2018].

**Raster data.** Record pixel resolution, temporal coverage, resampling rule, zonal-statistic method, and whether the raster is assigned to residences, workplaces, routes, or polygons.

**Routing and APIs.** Freeze query parameters, route mode, departure time, API version or data snapshot, and failed routes. If the API cannot be rerun later, preserve the returned matrix.

**Crosswalks.** Store the source file, vintage, weight type, and many-to-many structure. Never collapse a many-to-many crosswalk without preserving the original weights.

**Confidential data.** Record masking, aggregation, suppression, and jittering rules in the secure workflow. Release synthetic examples, metadata, and aggregate diagnostics when raw coordinates cannot be shared.

### Good Spatial Workflow Checklist

- Define the economic mechanism and target estimand.
- Select the spatial unit and exposure rule that match the mechanism.
- Preserve raw spatial identifiers and source files.
- Validate geocoding, CRS, joins, crosswalks, and route construction.
- Construct the primary object and at least one plausible alternative.
- Audit edge cases, missing locations, split units, and out-of-support places.
- Document confidentiality restrictions and their measurement consequences.
- Export a run manifest with data vintages, code versions, and output hashes where feasible.

## Reading Ladder And References

```{include} assets/tables/15-reading-architecture.md
```

A practical reading sequence is:

1. Read Autor, Dorn, and Hanson for the logic of a functional local labor market and baseline-weighted exposure [@autorDornHanson2013].
2. Read Chetty, Hendren, and Katz for fine neighborhood exposure and the timing of place environments [@chettyHendrenKatz2016].
3. Read Miller for job access, residential location, and the economic meaning of reachable employment [@miller2018].
4. Read Monte, Redding, and Rossi-Hansberg for commuting and migration links across places [@monteReddingRossiHansberg2018].
5. Use Donaldson and Hornbeck, Redding and Rossi-Hansberg, and Ahlfeldt and coauthors to see how market access, trade costs, and spatial equilibrium objects become model inputs [@donaldsonHornbeck2016; @reddingRossiHansberg2017; @ahlfeldtReddingSturmWolf2015].
6. Use Pebesma and Bivand, Pebesma, and Gomez-Rubio for implementation habits, while keeping the economics rather than software syntax at the center [@pebesma2018; @bivandPebesmaGomezRubio2021].

## Exercises And Discussion Prompts

1. Choose a labor-market research question and explain how the estimand changes when the unit is a county, commuting zone, tract, or travel-time isochrone.
2. For a job-access measure, compare Euclidean distance, network distance, travel time, and observed commuting flows. Which object best matches the mechanism, and what data would each require?
3. Suppose a plant address geocodes to the ZIP centroid for some establishments and to exact coordinates for others. Which estimates are most at risk?
4. A tract boundary changes halfway through your sample. Give three defensible harmonization strategies and the estimand each one implies.
5. Build an exposure measure {math}`E_i=\sum_jw_{ij}s_j` for pollution, jobs, or school quality. What are {math}`s_j`, {math}`w_{ij}`, the unit of observation, and the relevant exposure window?
6. Explain why a spatial join can create design risk rather than only data-management inconvenience.
7. Identify one confidentiality protection for exact coordinates and explain how it could change distance bands or treatment assignment.

## Reproducibility And Code Lab Note

The canonical Week 15 lab lives in `labs/15-curating-maps-and-spatial-data/`. It creates synthetic teaching data and produces a reproducible spatial-curation path:

- `src/make_synthetic_data.py` writes local labor-market and job-access inputs;
- `src/reproduce_commuting_zone_exposure.py` constructs a commuting-zone exposure object;
- `src/diagnose_spatial_choices.py` audits geography, crosswalk, and geocoding sensitivities;
- `src/transfer_job_access.py` constructs alternative access measures for the transfer setting.

The lab deliberately avoids proprietary shapefiles, live geocoding, and routing APIs. Students still see the empirical design choices: geography, crosswalk weights, exposure denominators, distance decay, travel costs, and disclosure-related precision loss.

## Slide Companion Note

The Lecture 15 slide deck should not duplicate this chapter. It should make the geography-design logic visible:

- why spatial data are economic objects, not clerical inputs;
- points, polygons, rasters, networks, and panel geographies;
- how geographies and exposure definitions shape estimands;
- core operations: geocoding, joins, buffers, travel costs, crosswalks, aggregation, and confidentiality;
- practical pitfalls and rules of thumb;
- the Reproduce -> Diagnose -> Transfer lab design.

The canonical slide source is `slides/week15/15-curating-maps-and-spatial-data.tex`.

## Bridge Forward

Lecture 16 moves from spatial data curation to **causal inference with spatial data**. Once places, distances, and exposures have been built, the next questions are harder: when does spatial variation identify a causal effect, how should spillovers and interference be represented, how should inference handle spatial dependence, and when does sorting or equilibrium response defeat a simple place-based comparison?
