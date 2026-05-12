Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic3-gender/references.bib, @books/special-topic3-gender/OUTLINE.md, @books/special-topic3-gender/index.md, @books/special-topic3-gender/myst.yml, @books/special-topic3-gender/sources/01-why-gender-matters-for-labor-economics.md, @books/special-topic3-gender/assets/tables/01-core-objects-map.md, @books/special-topic3-gender/assets/tables/01-mechanisms-and-measurement-map.md, @books/special-topic3-gender/assets/tables/01-why-this-field-matters-map.md, and @books/special-topic3-gender/assets/tables/01-domain-preview-map.md.

Goal: turn the Gender Study Week 1 source pack into a polished chapter package while keeping the editable inputs minimal.

Week identity:
- Course: Special Topic 3 — Gender Study
- Week: 1
- Canonical chapter path: `books/special-topic3-gender/01-why-gender-matters-for-labor-economics.md`
- Canonical slide path: `books/special-topic3-gender/slides/week1/01-why-gender-matters-for-labor-economics.tex`
- Canonical lab path: `books/special-topic3-gender/labs/01-why-gender-matters-for-labor-economics/`
- Local conda environment: `research`

Before drafting:
1. Merge any missing entries from `bibliography/01-why-gender-matters-for-labor-economics.bib` into `books/special-topic3-gender/references.bib`.
2. Delete repeated BibTeX entries if any were introduced. Keep only one canonical entry per cite key in `books/special-topic3-gender/references.bib`.
3. Do not duplicate citation keys.

Required outputs:
1. `books/special-topic3-gender/01-why-gender-matters-for-labor-economics.md`
2. `books/special-topic3-gender/slides/week1/01-why-gender-matters-for-labor-economics.tex`
3. `books/special-topic3-gender/labs/01-why-gender-matters-for-labor-economics/lab.md`
4. `books/special-topic3-gender/labs/01-why-gender-matters-for-labor-economics/smoke.sh`
5. any minimal `src/` files needed for the bounded pedagogical lab path
6. any minimal updates to `books/special-topic3-gender/myst.yml` or `books/special-topic3-gender/index.md` needed to wire Week 1 into the book

Non-negotiable conventions:
- Use valid MyST markdown syntax.
- For inline math in markdown, prefer `{math}`...``; do not use `\(...\)` in markdown.
- In prose markdown, use linked citations only, e.g. `[@goldin2014grand]`; do not use bare `@key` or backticked citation keys.
- Include a clearly visible **Core points** box near the top of the chapter.
- Do NOT create an Extension / Optional Extension box by default.
- If there is genuine frontier material, surface it inside Field Core or Research Lab.
- Slides must live only under `books/special-topic3-gender/slides/week1/`.
- Slide compilation outputs should live alongside the `.tex` source in `books/special-topic3-gender/slides/week1/`.
- Use the `research` conda environment for local commands.
- Keep edits minimal and reviewable.

Topic boundary:
- This is the opening lecture for Gender Study.
- Students will already know that gender matters in a general sense; the chapter must explain why gender is a core labor-economics object and why it is a productive field for labor researchers to invest in.
- Do not let the chapter collapse into a single male-female wage-gap lecture.
- The chapter should frame gender through labor-market objects: employment, hours, earnings, wages, occupations, firms, authority, safety, care work, and welfare.
- It should distinguish description from mechanism and show why measurement choices (lifecycle timing, firm structure, family structure, institutions, and identity) matter.
- It should be labor-focused, not generic gender-studies or sociology.

Content requirements:
- Follow the established structure:
  1. short opening orientation / why this week matters
  2. Core points box
  3. Bridge
  4. Field Core
  5. Research Lab
  6. reading ladder / references block
- The chapter should do five things clearly:
  1. define the main labor-market objects of gender inequality
  2. explain why average gaps are useful but incomplete
  3. show the major mechanism classes that later weeks will unpack
  4. explain why gender is a first-order field for labor researchers rather than a niche application
  5. preview how measurement choices discipline the rest of the course

Formal / conceptual requirements:
Include at least:

1. one canonical mean-gap object:
```{math}
:label: eq:gender-gap-week1
G_Y = \mathbb{E}[Y \mid F=1] - \mathbb{E}[Y \mid F=0]
```
where `{math}`Y`` can be employment, hours, earnings, wages, promotion, or authority, and the text should explain why the choice of `{math}`Y`` matters.

2. one decomposition-style object:
```{math}
:label: eq:decomp-week1
G = G^{prices} + G^{quantities} + G^{allocation}
```
or an equivalent decomposition that separates pay-setting, hours, and sorting/allocation channels. The point is conceptual rather than technical.

3. one lifecycle/event-study object tied to family formation:
```{math}
:label: eq:child-penalty-week1
Y_{it} = \sum_{k \neq -1}\beta_k \mathbf{1}\{t - T_i = k\} + \alpha_i + \gamma_t + \varepsilon_{it}
```
with a short explanation of why gender gaps are often best understood dynamically rather than cross-sectionally.

4. one worker-firm / authority object:
```{math}
:label: eq:firm-gap-week1
Y_{if} = \alpha_i + \psi_f + \delta F_i + \varepsilon_{if}
```
used only as a framing object to show that firms and authority structures can matter, even if the full AKM machinery is not taught here.

Field Core requirements:
- Organize the chapter around:
  - what gender changes in labor markets,
  - what counts as a relevant outcome,
  - what the main mechanism classes are,
  - why this is a vibrant labor field.
- The chapter should explicitly state that gender research in labor economics is not only about:
  - wages,
  - or only about women,
  - or only about discrimination.
- It should preview worker-side, firm-side, household-side, institutional, and policy channels.
- It should explain why labor researchers should invest in this field:
  - large remaining disparities,
  - broad links to labor supply, firms, contracts, occupations, authority, and welfare,
  - rich administrative and linked datasets,
  - active policy relevance,
  - strong methodological innovation,
  - abundant frontier questions.

Empirical anchors to use:
- broad labor-gender framing / reviews:
  - `[@blauKahn2017genderwagegap]`
  - `[@goldin2014grand]`
  - `[@olivettiPanPetrongolo2024evolution]`
- lifecycle / family / dynamic inequality:
  - `[@klevenLandaisSogaard2019children]`
  - `[@cortesPan2023children]`
- firm / careers / authority:
  - `[@bertrandGoldinKatz2010dynamics]`
- global/legal/institutional dimension:
  - `[@hylandDjankovGoldberg2020genderedlaws]`

Methods requirements:
- Explicitly distinguish:
  - description vs mechanism,
  - cross-sectional gaps vs lifecycle dynamics,
  - wages vs earnings vs hours,
  - worker-level vs firm-level vs institutional mechanisms,
  - average gaps vs distributional / authority / safety / welfare outcomes.
- Make clear why measurement choices matter:
  - timing,
  - family status,
  - occupation,
  - firm,
  - legal environment,
  - selection into work.

Research Lab requirements:
- Build the lab around Reproduce -> Diagnose -> Transfer.
- Primary lab anchor: `[@hylandDjankovGoldberg2020genderedlaws]`
- Secondary / challenge anchor: `[@klevenLandaisSogaard2019children]`
- Optional extension anchor: `[@bertrandGoldinKatz2010dynamics]`
- The bounded student path must run locally without confidential microdata.
- The lab should train students to distinguish:
  - what outcome is being measured,
  - what the comparison group is,
  - what the mechanism is claimed to be,
  - whether the design is descriptive, causal, or decomposition-based,
  - and how a country-specific or lifecycle-specific result can still matter broadly.

Slide requirements:
- The deck should use the repo's Beamer conventions.
- It should include, at minimum:
  1. central question and why gender is a labor-economics field
  2. core labor-market objects
  3. description vs mechanism
  4. wages, earnings, hours, occupations, firms, authority, safety, care, welfare
  5. lifecycle timing and child penalties
  6. firms, careers, and authority structures
  7. legal/institutional/global dimensions
  8. why this is a high-return research field
  9. bridge to Week 2

Validation requirements:
1. strict book build:
   `cd books/special-topic3-gender && conda run -n research jupyter book build --html --strict`
2. preview check:
   `cd books/special-topic3-gender && conda run -n research --live-stream jupyter book start`
   Treat success as "localhost URL printed"; then stop the server cleanly.
3. Week 1 slides compile from the canonical path
4. Week 1 lab smoke test passes

Important implementation notes:
- If you add Week 1 to `index.md` or `myst.yml`, do so in the same style that other flagship special topics use.
- If you create a new smoke script, make it executable and keep it narrowly scoped.
- Do not leave duplicate slide sources or duplicate build artifacts in `books/special-topic3-gender/`.
- If stale references or workflow mismatches appear, trust the actual repo structure and fix the smallest issue.
- Preserve the special-topics conventions established earlier: Core points box required, no default Extension box, linked citations only.

At the end, report:
- files changed
- whether any BibTeX entries were added or deduplicated
- exact validation commands used
- pass/fail for build, preview, slides, and lab smoke
- any remaining non-blocking warnings
