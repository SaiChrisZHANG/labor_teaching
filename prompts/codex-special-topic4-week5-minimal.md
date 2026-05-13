Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic4-urban/index.md, @books/special-topic4-urban/OUTLINE.md, @books/special-topic4-urban/myst.yml, @books/special-topic4-urban/README.md, @books/special-topic4-urban/references.bib, and these week files if they exist:
- `books/special-topic4-urban/01-space-and-labor-markets-urban-access-commuting-amenities-and-local-opportunity.md`
- `books/special-topic4-urban/02-housing-rents-moving-costs-and-labor-market-adjustment.md`
- `books/special-topic4-urban/03-spatial-mismatch-segregation-neighborhood-effects-and-job-access.md`
- `books/special-topic4-urban/04-crime-safety-environment-and-the-urban-feasible-set-for-work.md`

Read the week pack files:
- `source/05-migration-local-labor-demand-and-urban-labor-reallocation.md`
- `bibliography/05-migration-local-labor-demand-and-urban-labor-reallocation.bib`
- all markdown tables under `tables/`

Goal: draft Week 5 for special-topic4-urban as a substantial migration/reallocation lecture that is research-facing, methodologically explicit, and connected to gentrification and diversification through a labor-market lens.

This is a chapter-drafting task that should preserve the special-topics conventions:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown
- course-local bibliography only
- use the `research` conda environment for validation
- slides should live only under `books/special-topic4-urban/slides/week5/`
- labs should live only under `books/special-topic4-urban/labs/05-migration-local-labor-demand-and-urban-labor-reallocation/`

Non-negotiable week identity:
- The week is about migration, local labor demand, and urban labor reallocation.
- It should be longer and heavier than a standard week.
- It must treat migration and local labor reallocation as a spatial labor-adjustment system, not a generic migration lecture.
- It must include a methods/data layer.
- It must touch diversification and gentrification through the lens of labor research.
- It must stay labor-focused.

Before editing:
1. produce a short plan
2. list the files you will create or update
3. identify any path or numbering conflicts
4. do not edit until the plan is complete

Required outputs:
1. Draft the canonical week chapter at:
   `books/special-topic4-urban/05-migration-local-labor-demand-and-urban-labor-reallocation.md`

2. Create the canonical slides at:
   `books/special-topic4-urban/slides/week5/05-migration-local-labor-demand-and-urban-labor-reallocation.tex`

3. Create the lab handout and bounded teaching path at:
   `books/special-topic4-urban/labs/05-migration-local-labor-demand-and-urban-labor-reallocation/lab.md`
   and a `smoke.sh` if the repo conventions require it.

4. Merge any missing BibTeX entries from the week bibliography into:
   `books/special-topic4-urban/references.bib`
   and deduplicate repeated entries if duplicates appear.
   Keep one canonical entry per cite key.

Required lecture content:
- opening orientation
- Core points box
- Bridge
- Field Core
- Research Lab
- reading ladder / references block if already part of the series style
- backward/forward bridge where appropriate

Non-negotiable intellectual structure:
A. Theory / framework
- local labor demand shocks in spatial equilibrium
- migration, commuting, wages, rents, and firm entry/exit as adjustment margins
- incidence on workers, landlords, firms, incumbent residents, and migrants
- persistence vs reallocation
- distinction between “places” and “people”

B. Empirical backbone
- classic local labor-demand adjustment papers
- migration and commuting responses
- recent frontier work on persistence after recessions / demand shocks
- one subsection on gentrification as labor-market restructuring
- one subsection on diversification / resilience as a labor-market object

C. Methods and data layer
- a clearly labeled methods box or section
- explain common designs without turning the chapter into a general econometrics lecture
- include: shift-share/Bartik exposure designs, predicted-destination IVs, commuting-linked designs, spatial-equilibrium calibration/structural approaches, matched employer-employee data, dynamic local-shock event studies, boundary/transport/policy shocks where relevant
- explicitly connect empirical setting -> identification strategy -> actual econometric methods
- explain what a good design looks like for these questions

D. Gentrification and diversification
- treat gentrification as a labor-market reallocation / restructuring process, not just a housing story
- treat diversification as labor-market resilience / worker-insurance / reallocation capacity, not just a city-planning concept

Style requirements:
- research-facing
- labor-focused
- conceptually structured
- not a list of papers
- use the papers in the pack to organize mechanisms and methods
- use linked citations in prose like `[@key]`

Suggested section logic:
1. Why migration and local reallocation are central labor questions
2. A spatial labor-adjustment framework
3. Migration, commuting, and incidence after local demand shocks
4. Persistence, hysteresis, and local labor-market recovery
5. Gentrification, neighborhood change, and labor-market restructuring
6. Diversification, resilience, and worker insurance across local shocks
7. Methods and data box
8. Research Lab
9. Bridge to the final synthesis week

Slide requirements:
- create a polished Beamer deck using the repo’s current default professional theme
- slides should follow the chapter structure, but be shorter and more presentation-oriented
- do not dump full paragraphs on slides
- include one slide that explicitly summarizes the adjustment margins
- include one slide that explicitly summarizes methods/data

Implementation notes:
- keep filenames canonical and stable
- do not create duplicate slide sources outside `slides/week5/`
- do not leave stale copies in the book root
- if week ordering links in `index.md`, `OUTLINE.md`, or `myst.yml` need a tiny update, make the smallest clean fix
- do not rewrite other weeks substantively

Validation:
1. run strict build:
   `cd books/special-topic4-urban && conda run -n research jupyter book build --html --strict`
2. compile the slides from:
   `books/special-topic4-urban/slides/week5/05-migration-local-labor-demand-and-urban-labor-reallocation.tex`
3. if a lab smoke path exists, run it
4. fix the smallest issue if any build/slide/path problem appears and rerun

At the end, report:
1. files created/changed
2. which bibliography entries were merged
3. pass/fail for strict build
4. pass/fail for slide compilation
5. any remaining manual review items