# Curating Maps and Spatial Data

## Learning Objectives

By the end of this lecture, students should be able to:

1. explain why spatial data construction is part of research design rather than just data cleaning;
2. distinguish points, polygons, rasters, and networks as different empirical objects with different identification implications;
3. defend a geography choice in light of the mechanism of interest;
4. construct and critique access, exposure, and distance-based measures;
5. recognize the main pitfalls in spatial data work, including MAUP, geocoding error, temporal mismatch, and confidentiality constraints;
6. design a reproducible spatial-data workflow suitable for applied economics research.

## Opening Orientation

Spatial data enter applied economics whenever the mechanism of interest depends on **where** workers, firms, schools, housing, transport, pollution, or public services are located. The practical challenge is not just collecting coordinates or shapefiles. The deeper problem is deciding what a “place” is for the question at hand, what kind of distance matters, which borders are meaningful, and how these choices affect the estimand.

The lecture therefore treats spatial data curation as the first stage of identification. A commuting zone, census tract, school catchment, buffer around a plant, or travel-time isochrone is not merely a convenient data container; it is an empirical claim about how space enters economic behavior.

:::{admonition} Core points
:class: important
- Spatial data work is part of research design because geography choice and exposure construction define the object being estimated.
- Points, polygons, rasters, and networks encode different mechanisms and carry different advantages and risks.
- Distances, buffers, and spatial joins are not neutral preprocessing steps: they embed assumptions about mobility, access, and interaction.
- Practical spatial work requires reproducibility, sensitivity checks, and awareness of MAUP, geocoding error, confidentiality, and temporal mismatch.
- Good applied work connects spatial data construction directly to an economic mechanism and to a credible downstream design.
:::

## Bridge

Lecture 15 opens the optional spatial-methods block by moving one step earlier than causal inference or structural spatial modeling. Before researchers estimate treatment effects or equilibrium responses with spatial data, they must define the place-based objects, boundaries, and exposure measures that make those designs meaningful. The next lecture will ask how to do causal inference with these objects; this lecture focuses on how those objects are created and what can go wrong before identification even begins.

## Field Core

### 1. Why spatial data are economic objects

Spatial data are not just map layers. They encode economic primitives such as access, proximity, exposure, agglomeration, and jurisdiction. A worker’s feasible set often depends on generalized travel cost to jobs,

```{math}
:label: eq:generalized-travel-cost
c_{ij} = \tau \cdot t_{ij},
```

where {math}`t_{ij}` is travel time or generalized distance from residence {math}`i` to opportunity {math}`j`, and {math}`\tau` converts time or distance into disutility or money-metric cost.

Likewise, many place-based empirical objects are exposure measures of the form

```{math}
:label: eq:spatial-exposure
E_i = \sum_j w_{ij} s_j,
```

where {math}`s_j` is a place-specific shock, opportunity, or amenity, and {math}`w_{ij}` encodes the researcher’s view of how geography mediates exposure: adjacency, inverse distance, commuting flows, transport connectivity, or shared labor market.

The empirical lesson is that a geography is never “just the data.” The unit and weight system must correspond to the mechanism. If the mechanism is commuting, then labor-market areas or travel-time matrices may be the relevant object. If the mechanism is neighborhood exposure during childhood, census tracts or very fine local units may be more appropriate. If the mechanism is trade or local labor demand, commuting zones or counties may be preferable.

### 2. The main spatial data objects

#### Points
Points are addresses, workplaces, plants, schools, clinics, or events. They are the natural object when exact location matters for distance, accessibility, routing, or spatial clustering.

Advantages:
- precise distance-based calculations;
- flexible aggregation later;
- useful for travel-time, routing, and proximity analysis.

Limitations:
- confidentiality concerns;
- geocoding error can be severe;
- point locations may overstate precision when the true mechanism operates over larger catchments.

#### Polygons
Polygons are census tracts, ZIP codes, counties, municipalities, school zones, or administrative regions.

Advantages:
- align well with public administrative data;
- easier to merge with policy and demographic files;
- often the only available unit for confidential microdata.

Limitations:
- MAUP and ecological aggregation;
- boundaries may be arbitrary for labor-market interactions;
- boundary changes over time require crosswalks.

#### Rasters
Rasters represent gridded surfaces such as land cover, pollution, temperature, night lights, population density, or elevation.

Advantages:
- useful for environmental exposure, terrain, and remote-sensing measures;
- often available historically and globally.

Limitations:
- resolution choices matter;
- pixel aggregation to people or firms is nontrivial;
- time alignment and support mismatches can be large.

#### Networks
Networks encode roads, rail, transit, commute links, or social/economic connections.

Advantages:
- better for access than Euclidean distance;
- useful when commuting, routing, or bottlenecks are the mechanism.

Limitations:
- travel-time matrices can be computationally expensive;
- API / routing assumptions may change over time;
- requires explicit decisions about mode, congestion, and schedule.

### 3. Core operations and why they matter

#### Geocoding
Geocoding transforms addresses or textual locations into coordinates. In practice, geocoding error is often systematic: rural addresses, informal settlements, historical addresses, and employer names can be mapped inaccurately.

Practical rules:
- retain original raw addresses separately;
- record geocoding confidence and failures;
- inspect a sample manually;
- rerun key analyses under stricter geocoding-quality filters.

#### Projections and coordinate systems
Distances and areas depend on the map projection. Researchers should never compute economically meaningful distances from latitude/longitude coordinates without checking the projection and the scale.

Practical rules:
- choose a projected CRS suitable for the geography of interest;
- document all reprojections explicitly;
- avoid mixing layers in incompatible CRSs;
- distinguish “visualization CRS” from “analysis CRS.”

#### Spatial joins
A spatial join assigns points to polygons, overlays polygons on polygons, or attaches raster values to locations.

Practical rules:
- define whether “inside,” “intersects,” or “nearest” is the relevant rule;
- inspect edge cases near boundaries;
- document how ties and overlaps are handled;
- do not assume a spatial join is innocuous if boundaries are policy-relevant.

#### Buffers and distance bands
Buffers create treatment or exposure zones around points or lines, often used around plants, transit stations, roads, or hazards.

Practical rules:
- motivate the buffer radius economically;
- test alternative radii;
- understand that buffers discretize what may be a continuous exposure;
- be cautious with irregular geography or barriers that make equal-radius buffers unrealistic.

#### Distance and travel-time measures
Distance can be Euclidean, network-based, or generalized travel cost. The best choice depends on whether the mechanism is visibility, migration, commuting, market access, or environmental spillover.

Practical rules:
- if commuting is the mechanism, prefer travel time or generalized cost over straight-line distance;
- if historical routing is impossible, say so clearly and justify the proxy;
- report sensitivity to alternative definitions.

#### Crosswalks and changing boundaries
Many empirical projects need crosswalks between tracts, ZIP codes, counties, school zones, PUMAs, and commuting zones, or between historical and current boundaries.

Practical rules:
- preserve raw source geography before harmonization;
- document the exact crosswalk and weighting rule;
- distinguish area-weighted from population-weighted crosswalks;
- be explicit when crosswalks create measurement error.

### 4. Spatial estimands and mechanism choice

Spatial data work often fails because the geography is chosen for convenience rather than mechanism. The estimand should determine the spatial object, not the other way around.

Examples:
- **local labor market exposure**: commuting zones or counties may be appropriate when the labor market is regionally integrated;
- **neighborhood exposure**: census tracts or blocks may be better if peer effects, school quality, or safety vary at fine scale;
- **job access**: travel-time or transit-reachable jobs may be better than residential neighborhood characteristics;
- **firm access to workers**: catchment areas, commuting flows, or travel-time surfaces may matter more than administrative borders.

This is why many strong papers spend serious effort justifying their place definition. Local labor-market papers that use commuting zones make a claim about commuting integration rather than county borders. Neighborhood-mobility papers using tracts make a claim about children’s exposure to fine local institutions. Job-access papers with travel-time matrices make a claim that commute cost, not nominal distance, is the key mechanism.

### 5. Major pitfalls

#### MAUP and arbitrary geography
Aggregating the same underlying data to tracts, ZIP codes, counties, or commuting zones can change results materially. That is not a software bug; it reflects that different units correspond to different mechanisms.

#### Geocoding error
Errors in point locations bias distances, exposure measures, and assignment to neighborhoods or policy jurisdictions.

#### Temporal mismatch
Outcomes, addresses, boundaries, and covariates are often measured in different years. Researchers need to say whether a place variable measures the relevant geography at the time the decision was made.

#### Endogenous boundary choice
Choosing the geography after seeing the pattern is a design problem. If several units are plausible, they should be motivated ex ante and checked systematically.

#### Ecological fallacy and aggregation bias
Area-level relationships do not automatically identify individual-level mechanisms.

#### Confidentiality and disclosure control
Exact addresses, workplaces, and especially matched residence-workplace data often require masking, jittering, aggregation, or enclave access. These changes can alter estimands if not handled transparently.

### 6. Practical rules of thumb for defensible spatial data work

1. Start with the mechanism, then choose the geography.
2. Keep raw spatial identifiers and a fully documented cleaned version.
3. Document every spatial transformation: geocode, projection, join, crosswalk, buffer, exposure weighting.
4. Use multiple plausible spatial definitions when the mechanism is uncertain.
5. Treat travel time, not just straight-line distance, as the default for commuting/access questions.
6. Record temporal alignment explicitly.
7. Stress-test boundary and buffer choices.
8. Explain confidentiality limitations and what they imply for interpretation.
9. Keep a reproducible spatial workflow: code, metadata, versioned shapefiles, and frozen auxiliary files.

## Research Lab

### Primary anchor paper
Use a spatial labor-market paper where geography construction is central to the estimand. A strong default anchor is a commuting-zone-based or tract-based labor paper such as Autor, Dorn, and Hanson on commuting zones or Chetty, Hendren, and Katz on tract-level neighborhood exposure.

### Reproduce
Recreate a simplified spatial object from reduced data:
- a commuting-zone or tract crosswalk;
- a travel-time-based access measure;
- or a local labor-demand exposure variable.

### Diagnose
Ask:
- what does the chosen geography assume about the mechanism?
- what would change under counties vs commuting zones vs tracts?
- how much of the empirical claim is spatial construction rather than econometric estimation?

### Transfer
Apply the same curation logic to a new setting:
- build a tract-level job-access measure instead of a commuting-zone exposure;
- compare Euclidean vs travel-time access;
- or compare administrative vs functional labor-market definitions.

## Methods Box

### Typical tools and resources
Students should know where to look for implementation tools even if this lecture is not a software tutorial:
- vector data: `sf`, `geopandas`
- raster data: `terra`, `raster`, `xarray` / geospatial Python stacks
- spatial joins and crosswalks
- routing / travel-time tools
- reproducible metadata and shapefile versioning

### Good workflow questions
- What is the unit of exposure?
- What geography matches the mechanism?
- How much error is induced by geocoding or crosswalks?
- Is travel time more defensible than Euclidean distance?
- Are results robust to alternative place definitions?
- What confidentiality choices may affect measurement?

## Reading Ladder And References

### Core framing
- [@autorDornHanson2013]
- [@chettyHendrenKatz2016]
- [@monteReddingRossiHansberg2018]
- [@miller2018]

### Practical and methodological references
- [@pebesma2018]
- [@bivandPebesmaGomezRubio2021]

## Exercises And Discussion Prompts

1. Give an example where county, commuting-zone, and tract definitions would produce different estimands for the same research question.
2. Why is travel time often superior to straight-line distance in labor-market access work?
3. What kinds of questions are most vulnerable to geocoding error?
4. Suppose a policy boundary changes halfway through your sample. What are three defensible ways to handle it?
5. When does a spatial join create real design risk rather than only data-management inconvenience?

## Reproducibility And Code Lab Note

The lecture should connect to a bounded lab that asks students to create one spatial empirical object from reduced data and then stress-test it under at least one alternative definition. The main learning goal is not software fluency alone; it is understanding that spatial preprocessing choices are part of the research design.

## Slide Companion Note

The slide deck should make the geography-design logic visual:
- points vs polygons vs rasters vs networks;
- crosswalks and joins;
- buffers and travel-time measures;
- mechanism-to-geography mapping;
- practical pitfalls and workflow rules.

## Bridge Forward

Lecture 16 will move from spatial data curation to **causal inference with spatial data**, asking when boundaries, discontinuities, exposure gradients, and place-based shocks can be used credibly for identification.
