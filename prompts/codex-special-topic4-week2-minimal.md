Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic4-urban/index.md, @books/special-topic4-urban/OUTLINE.md, @books/special-topic4-urban/myst.yml, @books/special-topic4-urban/README.md, @books/special-topic4-urban/references.bib, and these week files:

- `books/special-topic4-urban/source/02-housing-rents-moving-costs-and-labor-market-adjustment.md` if it exists
- `books/special-topic4-urban/assets/tables/02-housing-incidence-framework.md` if it exists
- `books/special-topic4-urban/assets/tables/02-paper-architecture-map.md` if it exists
- `books/special-topic4-urban/assets/tables/02-data-sources-map.md` if it exists
- `books/special-topic4-urban/assets/tables/02-methods-and-design-map.md` if it exists

Also read the week-specific files supplied with this task:
- source markdown
- week-specific bibliography
- table markdown files

Goal: draft Week 2 of the Urban and Labor course:

**Week 2. Housing, Rents, Moving Costs, and Labor-Market Adjustment**

This week should be a research-framework lecture, not a paper dump. The chapter should help students see how to study housing and labor together in a disciplined way.

Central question:
When do housing markets and moving costs prevent workers from reaching better labor-market opportunities?

Core content requirements:
1. Start from a labor-space framework in which housing enters labor outcomes through:
   - rents and real wages
   - moving costs and mobility frictions
   - housing supply elasticity
   - residential sorting and wealth/liquidity constraints
   - commuting as a substitute for migration
   - local labor-demand shocks and adjustment incidence
2. Keep the lecture labor-focused:
   - who can reach productive places
   - who captures wage gains
   - who is priced out
   - how housing mediates labor reallocation after shocks
3. Do not let the chapter become a generic housing course or a generic urban policy lecture.
4. Include a dedicated practical section or methods box on data currently used in this subfield.
5. Use roughly 15 high-quality papers, organized by research role rather than listed indiscriminately.
6. The lecture should teach a compact architecture for research:
   - theory / framework
   - key empirical margins
   - canonical designs
   - data sources
   - frontier questions

Special-topic conventions to preserve:
- Core points box required near the top
- no default Extension box
- linked citations only in prose markdown: `[@key]`
- use only the course-local bibliography as the canonical course bibliography
- merge missing entries from the week bibliography into `books/special-topic4-urban/references.bib`
- deduplicate repeated BibTeX entries if duplicates appear

Required chapter structure:
1. opening orientation
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading ladder / references section if consistent with the course style

Specific substantive instructions:
- In the Field Core, make the following distinctions explicit:
  a. nominal wage gains vs real access gains
  b. housing supply constraints vs moving-cost frictions
  c. migration vs commuting as adjustment margins
  d. worker incidence vs landlord/homeowner incidence vs firm incidence
  e. equilibrium adjustment in wages, rents, and population
- Use the data survey to show students what researchers actually use:
  - ACS / ACS PUMS
  - Decennial Census / Census long form
  - LEHD / LODES / QWI
  - IRS migration data
  - Zillow / FHFA / CoreLogic / transaction-level housing data
  - HUD administrative data / voucher data where relevant
  - HMDA where relevant
  - commuting-zone / metro delineations
  - local housing-supply/regulation measures
- The Research Lab should explicitly tell students what kind of research designs dominate this field:
  - spatial equilibrium / calibrated quantitative counterfactuals
  - Bartik-style or shift-share local demand shocks
  - local labor-demand shocks and incidence
  - housing-supply elasticity heterogeneity
  - commuting or transport shocks
  - migration response / event-study designs
- The chapter should emphasize that the contribution margin is often in identifying which friction is binding:
  - housing supply
  - moving costs
  - wealth/credit constraints
  - commuting technology
  - local regulation
  - landlord capture / rent capitalization

Paper architecture requirement:
- Organize the papers into 4–5 buckets such as:
  - foundational framework
  - housing constraints and misallocation
  - moving costs and migration adjustment
  - commuting and within-metro access
  - recent/frontier directions
- Do not just list papers chronologically.

Slide requirements:
- Create the slide source at:
  `books/special-topic4-urban/slides/week2/02-housing-rents-moving-costs-and-labor-market-adjustment.tex`
- Use the project’s standard professional Beamer setup
- Slides should follow the chapter structure and be concise, readable, and teachable
- Include one slide that summarizes the data sources researchers use in this area
- Include one slide that summarizes the research architecture / design map

Implementation notes:
- Create/update the chapter file at:
  `books/special-topic4-urban/02-housing-rents-moving-costs-and-labor-market-adjustment.md`
- Place editable tables under:
  `books/special-topic4-urban/assets/tables/`
- If a week-specific source file is maintained under `sources/`, keep naming consistent:
  `books/special-topic4-urban/sources/02-housing-rents-moving-costs-and-labor-market-adjustment.md`
- Keep chapter links/index/myst wiring coherent if the week is not already wired in
- Do not rewrite other weeks
- Keep edits minimal outside the Week 2 package

Validation:
1. Run a strict build:
   `cd books/special-topic4-urban && conda run -n research jupyter book build --html --strict`
2. Compile the Week 2 slides from the canonical path
3. Fix the smallest issue if anything breaks

At the end, report:
1. files created/changed
2. which week-bibliography entries were merged into the course bibliography
3. whether any BibTeX duplicates were removed
4. build command used
5. slide compile command used
6. pass/fail for book build and slide compilation
7. any remaining manual review items
