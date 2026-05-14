Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic4-urban/references.bib, @books/special-topic4-urban/OUTLINE.md, @books/special-topic4-urban/index.md, @books/special-topic4-urban/myst.yml, @books/special-topic4-urban/README.md, and these week files if they already exist:

- `books/special-topic4-urban/sources/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.md`
- `books/special-topic4-urban/assets/tables/03-mechanisms-map.md`
- `books/special-topic4-urban/assets/tables/03-empirical-designs-box.md`
- `books/special-topic4-urban/assets/tables/03-good-design-checklist.md`
- `books/special-topic4-urban/assets/tables/03-data-and-measurement-map.md`

Also read the week-specific files supplied with this task:
- source markdown
- week-specific bibliography
- table markdown files

Goal: draft Week 3 of the Urban and Labor course:

**Week 3. Spatial Mismatch, Segregation, Neighborhood Effects, and Job Access**

Central question:
How do residential segregation and neighborhood exposure shape access to jobs, networks, and long-run labor-market opportunity?

This week should help students build a disciplined research framework for job access and neighborhood effects. It should not become a generic neighborhood-effects lecture or a generic race-and-place lecture.

Week identity:
- Course: Special Topic 4 — Urban and Labor
- Week: 3
- Canonical chapter path: `books/special-topic4-urban/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.md`
- Canonical slide path: `books/special-topic4-urban/slides/week3/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.tex`
- Canonical lab path: `books/special-topic4-urban/labs/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.bib` into `books/special-topic4-urban/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic4-urban/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic4-urban/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.md`
2. `books/special-topic4-urban/slides/week3/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.tex`
3. `books/special-topic4-urban/labs/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access/lab.md`
4. `books/special-topic4-urban/labs/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic4-urban/myst.yml` or `books/special-topic4-urban/index.md` needed to wire Week 3 into the book

Special-topic conventions to preserve:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@chettyHendrenKatz2016]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic4-urban/slides/week3/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic4-urban/slides/week3/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This week is about **unequal access**, not aggregate access.
- The chapter must separate mechanisms rather than collapsing everything into “neighborhood effects.”
- The central mechanisms are:
  - distance to jobs / spatial mismatch
  - transit and commuting feasibility
  - employer discrimination or address stigma
  - referral networks and workplace segregation
  - neighborhood peers and social capital
  - schools / public goods / local institutions
  - local safety and exposure
- The lecture should show that these mechanisms imply different empirical designs and different policy levers.

Content requirements:
Follow the established structure:
1. short opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. reading ladder / references block

Field Core requirements:
Organize the chapter around these five blocks.

### Block A. From aggregate access to unequal access
- Start from Week 1/2 and explain why local opportunity is not equally reachable within the same city.
- Make clear that spatial inequality can arise even when total metro labor demand is strong.
- Define spatial mismatch and residential segregation as candidate channels, not complete explanations.

### Block B. Mechanisms of unequal labor-market access
- Distinguish the main mechanisms explicitly:
  1. distance to jobs / commuting frictions
  2. neighborhood or address discrimination
  3. referral networks / residential labor-market networks
  4. neighborhood peers and local social capital
  5. schools, public goods, and childhood environments
  6. local safety and institutional exposure
- For each mechanism, the chapter should ask:
  - what is the labor-market object?
  - what is the relevant counterfactual?
  - what empirical design can isolate it?

### Block C. Segregation, networks, and job access
- Cover spatial mismatch and neighborhood labor-market networks together but distinguish them.
- Use job suburbanization, network concentration, and racially stratified access as central examples.
- Make clear that proximity to jobs is not the same thing as access to jobs.

### Block D. Neighborhood exposure and long-run labor outcomes
- Cover neighborhood effects on long-run earnings, employment, and mobility.
- Emphasize exposure timing, age-at-move logic, and cumulative exposure.
- Keep the lecture labor-focused: later earnings, employment, search scope, and human-capital opportunity.

### Block E. What a good empirical design looks like
This block is required.

The chapter should include a dedicated methodological section or callout that teaches students:
- the main empirical designs used in this subfield,
- what each design is good for,
- and what a credible design should look like.

The required design families to cover are:
1. **Mover designs / age-at-move designs**
   - e.g. exposure timing and family moves
2. **Cohort exposure / cumulative exposure designs**
   - neighborhood duration and timing
3. **Policy shocks**
   - MTO, public housing demolition, transit or commuting shocks, job suburbanization, boundary redrawing, similar quasi-experiments
4. **School attendance / school admission / school-boundary designs**
   - especially when trying to separate neighborhood from school quality
5. **Audit / correspondence designs**
   - especially for neighborhood stigma, distance, or employer beliefs
6. **Matched employer-employee / network designs**
   - especially for referrals, coworker networks, and job access through neighborhoods

The chapter must also explain what a **good empirical design** should do here:
- map the treatment to a single mechanism as cleanly as possible
- define the relevant geographic scale
- measure actual job access rather than proxying it too loosely
- distinguish residence, workplace, school, and neighborhood channels
- address residential sorting
- discuss equilibrium resorting or displacement where relevant
- show which labor margin is actually moving (employment, wages, commute, mobility, long-run outcomes, etc.)

Formal / conceptual requirements:
Include at least:

1. one job-access object:
```{math}
:label: eq:job-access-week3
A_i = \sum_j v_j \exp\{-\kappa \tau_{ij}\}
```
where `{math}`v_j`` captures job opportunities and `{math}`\tau_{ij}`` is generalized travel cost.

2. one mechanism decomposition:
```{math}
:label: eq:mechanism-decomp-week3
Y_i = \beta_A A_i + \beta_N N_i + \beta_P P_i + \beta_S S_i + u_i
```
where `{math}`A_i`` is access, `{math}`N_i`` networks, `{math}`P_i`` neighborhood/peer environment, and `{math}`S_i`` schools or local institutions.

3. one mover/exposure logic statement:
```{math}
:label: eq:exposure-week3
Y_i = \alpha + \theta \, \text{Exposure}_{ig} + \lambda_g + \varepsilon_i
```
with text explaining that age or duration of exposure can identify causal neighborhood effects when moves are plausibly exogenous or differentially timed.

Empirical anchors to use:
- mechanism and mismatch framing:
  - `[@kainHousingSegregationNegro1968]`
  - `[@gobillonSelodZenou2007]`
- networks and spatial access:
  - `[@bayerRossTopa2008]`
  - `[@hellersteinMcInerneyNeumark2011]`
  - `[@millerWhenWorkMoves2023]`
- causal neighborhood exposure:
  - `[@chettyHendrenKatz2016]`
  - `[@chettyHendren2018]`
  - `[@chynPublicHousingDemolition2018]`
  - `[@bergmanChettyDeLucaEtAl2024]`
- address / distance / stigma:
  - `[@phillipsDoLowWageEmployers2020]`
- methods / identification:
  - `[@graham2016]`
  - `[@blackDoBetterSchools1999]`
  - `[@monarrezSchoolAttendance2021]`

Required tables to use:
- `../tables/03-mechanisms-map.md`
- `../tables/03-empirical-designs-box.md`
- `../tables/03-good-design-checklist.md`
- `../tables/03-data-and-measurement-map.md`

Methods/data requirements:
The chapter should explicitly discuss common data sources:
- LEHD / LODES / QWI
- Census / ACS / Decennial Census
- Opportunity Atlas / tax-linked mobility data
- school assignment or school attendance boundary data
- transit / GTFS / travel-time matrices
- audit / correspondence-study data
- matched employer-employee data
- administrative relocation or housing-program data

Reading ladder logic:
1. spatial mismatch foundations,
2. segregation and network mechanisms,
3. causal neighborhood exposure,
4. modern policy-shock and mover designs,
5. measurement and identification challenges.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@chettyHendrenKatz2016]`
- Secondary / challenge anchor: `[@millerWhenWorkMoves2023]`
- Optional extension anchor: `[@bergmanChettyDeLucaEtAl2024]`
- The bounded student path must run locally without confidential microdata.
- The lab should train students to distinguish:
  - access from employment,
  - neighborhood effects from sorting,
  - school from neighborhood channels,
  - movers designs from policy shocks,
  - and mechanism-specific from omnibus neighborhood claims.

Slide requirements:
- The deck should use the repo’s Beamer conventions.
- It should include, at minimum:
  1. central question and why this is labor economics
  2. from aggregate access to unequal access
  3. mechanism taxonomy
  4. spatial mismatch vs networks vs neighborhood effects
  5. job suburbanization and unequal access
  6. mover designs and policy shocks
  7. school-boundary / audit / matched-firm designs
  8. what a good empirical design looks like
  9. bridge to later weeks

Validation requirements:
1. strict book build:
   `cd books/special-topic4-urban && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic4-urban && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 3 slides compile from the canonical path
4. Week 3 lab smoke test passes

Important implementation notes:
- If you add Week 3 to `index.md` or `myst.yml`, do so in the same style as the other special topics.
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
