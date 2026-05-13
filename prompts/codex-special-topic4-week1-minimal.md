Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic4-urban/references.bib, @books/special-topic4-urban/OUTLINE.md, @books/special-topic4-urban/index.md, @books/special-topic4-urban/myst.yml, @books/special-topic4-urban/sources/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.md, @books/special-topic4-urban/assets/tables/01-local-labor-market-objects-map.md, @books/special-topic4-urban/assets/tables/01-job-residence-choice-framework.md, @books/special-topic4-urban/assets/tables/01-urban-wage-premium-channels-map.md, and @books/special-topic4-urban/assets/tables/01-domain-preview-map.md.

Goal: turn the Urban and Labor Week 1 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 4 — Urban and Labor
- Week: 1
- Canonical chapter path: `books/special-topic4-urban/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.md`
- Canonical slide path: `books/special-topic4-urban/slides/week1/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.tex`
- Canonical lab path: `books/special-topic4-urban/labs/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.bib` into `books/special-topic4-urban/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic4-urban/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic4-urban/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.md`
2. `books/special-topic4-urban/slides/week1/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.tex`
3. `books/special-topic4-urban/labs/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity/lab.md`
4. `books/special-topic4-urban/labs/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic4-urban/myst.yml` or `books/special-topic4-urban/index.md` needed to wire Week 1 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@roback1982]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic4-urban/slides/week1/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic4-urban/slides/week1/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This is the opening lecture for Urban and Labor.
- The chapter must provide a clear theoretical framework for how space enters labor-market choices.
- The city should be treated not as a fixed location label but as a bundle of jobs, wages, rents, commuting costs, amenities, risks, and outside options.
- The lecture should remain labor-focused, not generic urban economics.
- Agglomeration and urban wage premia should appear here only as labor-market objects: productivity, learning, selection, and compensating differentials.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block

- The chapter should do five things clearly:
  1. define local labor markets as linked residential and workplace choice systems
  2. show how commuting costs, rents, amenities, and job access alter the feasible set of labor choices
  3. explain why workplace location and residential location should be analytically separated
  4. introduce the urban wage premium as a labor-market object, not just a city fact
  5. preview how later weeks will study housing, segregation, crime, environment, and migration as labor-market constraints

Formal / conceptual requirements:
Include at least:

1. one worker job-residence utility object:
```{math}
:label: eq:urban-choice-week1
U_{ijr} = w_j - R_r - \tau(d_{jr}) + A_r + \varepsilon_{ijr}
```
where `{math}`w_j`` is earnings at job `{math}`j``, `{math}`R_r`` is housing cost at residence `{math}`r``, `{math}`\tau(d_{jr})`` is commuting cost, and `{math}`A_r`` is amenity value.

2. one job-search/access object showing that accessible jobs decline with distance or generalized commuting cost:
```{math}
:label: eq:job-access-week1
\mathcal{J}_i(c) = \{j : \tau(d_{ij}) \leq c\}
```
with text explaining that space changes the effective opportunity set.

3. one spatial-equilibrium / compensating-differentials object:
```{math}
:label: eq:spatial-eq-week1
w_\ell - R_\ell + A_\ell = \bar{U}
```
or an equivalent equilibrium expression that explains why wages alone are not enough to compare labor-market opportunity across places.

4. one urban-wage-premium decomposition:
```{math}
:label: eq:uwp-week1
\Delta w^{urban} = \Delta w^{productivity} + \Delta w^{learning} + \Delta w^{sorting} + \Delta w^{compensating}
```
used as a framing device rather than a technical theorem.

Field Core requirements:
- Organize the chapter around:
  - local labor markets and job access,
  - residential choice and commuting,
  - wages/rents/amenities in spatial equilibrium,
  - urban wage premia and agglomeration as labor-market objects,
  - welfare interpretation.
- The opening section should provide a compact theoretical framework for how space enters labor choice.
- Make clear that local labor markets are not just administrative boundaries; they are shaped by commuting and search frictions.
- Explain why place of work and place of residence should not be conflated.
- Make clear that observed urban wage premia may reflect:
  - productivity/agglomeration,
  - learning,
  - worker sorting,
  - or compensation for costs/amenities.

Empirical anchors to use:
- spatial equilibrium / wages-rents-amenities:
  - `[@roback1982]`
  - `[@albouyLue2015]`
- spatial search / local labor markets:
  - `[@manningPetrongolo2017]`
- commuting and migration in local adjustment:
  - `[@monteReddingRossiHansberg2018]`
- urban wage premium / learning vs sorting:
  - `[@glaeserMare2001]`
- job access / geography of work:
  - `[@miller2023]`
- broad labor-market framework across places:
  - `[@moretti2011]`

Methods requirements:
- Explicitly distinguish:
  - residence-based vs workplace-based measurement,
  - nominal wages vs real opportunity,
  - access vs realized commute,
  - spatial selection vs causal local effects,
  - local labor market definitions based on geography vs flows.
- Mention key empirical objects students should know:
  - commuting flows,
  - workplace vs residential wage measures,
  - local price/rent adjustment,
  - job suburbanization / job access,
  - commuting-zone or travel-time based markets,
  - spatial equilibrium counterfactuals.

Required tables to use:
- `../tables/01-local-labor-market-objects-map.md`
- `../tables/01-job-residence-choice-framework.md`
- `../tables/01-urban-wage-premium-channels-map.md`
- `../tables/01-domain-preview-map.md`

Reading ladder logic:
1. spatial-equilibrium foundations,
2. spatial job search and local labor markets,
3. commuting/migration adjustment,
4. urban wage premium and learning/sorting,
5. job access / work relocation,
6. preview of later urban-labor themes.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@manningPetrongolo2017]`
- Secondary / challenge anchor: `[@monteReddingRossiHansberg2018]`
- Optional extension anchor: `[@miller2023]`
- The bounded student path must run locally without confidential microdata.
- The lab should train students to distinguish:
  - what the local labor market is,
  - what counts as access,
  - what the equilibrium object is,
  - whether a result is about sorting, productivity, or commuting frictions,
  - and how a place-specific result can still matter broadly.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why this is labor economics
  2. the worker job-residence choice framework
  3. local labor markets and search across space
  4. commuting costs, rents, and amenities
  5. spatial equilibrium and welfare interpretation
  6. urban wage premium: productivity, learning, sorting, compensation
  7. job access and the geography of work
  8. bridge to Week 2 on housing/rents/mobility constraints

Validation requirements:
1. strict book build:
   `cd books/special-topic4-urban && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic4-urban && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 1 slides compile from the canonical path
4. Week 1 lab smoke test passes

Important implementation notes:
- If you add Week 1 to `index.md` or `myst.yml`, do so in the same style that other special topics use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic4-urban/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Preserve the special-topics conventions established earlier: Core points box required, no default Extension box, linked citations only.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
