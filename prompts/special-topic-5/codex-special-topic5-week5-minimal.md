Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic5-technology/index.md
- @books/special-topic5-technology/OUTLINE.md
- @books/special-topic5-technology/myst.yml
- @books/special-topic5-technology/references.bib
- @books/special-topic5-technology/04-firms-hiring-management-and-organizational-response-to-new-technology.md if it exists
- @books/special-topic5-technology/05-technology-inequality-market-structure-and-labor-market-institutions.md if it exists

If helpful, also inspect:
- the Week 5 slide file if it exists
- the Week 5 lab folder if it exists
- the Week 5 source pack if it exists in the repo

Goal: create or refresh Week 5 of the Technology, Innovation, and Labor course as a market-level lecture on technology, inequality, market structure, structural change, and labor-market institutions.

Goal: replace the current Week 5 prompt logic with a canonical Week 3-style workflow that explicitly targets chapter, slides, and lab outputs for Week 5.

Canonical output files:
- `books/special-topic5-technology/05-technology-inequality-market-structure-and-labor-market-institutions.md`
- `books/special-topic5-technology/slides/week5/05-technology-inequality-market-structure-and-labor-market-institutions.tex`
- `books/special-topic5-technology/labs/05-technology-inequality-market-structure-and-labor-market-institutions/`

Also keep the standard week workflow in sync:
- update `books/special-topic5-technology/myst.yml`
- update `books/special-topic5-technology/index.md`

Use these input materials as the intellectual source of truth if they exist:
- `special_topic5_technology_week5_edit_pack/source/05-technology-inequality-market-structure-and-labor-market-institutions.md`
- `special_topic5_technology_week5_edit_pack/bibliography/05-technology-inequality-market-structure-and-labor-market-institutions.bib`
- all markdown files under `special_topic5_technology_week5_edit_pack/tables/`

This is a week-drafting / sync task using the established special-topics conventions.

Non-negotiable Week 5 identity:
- The week must remain a labor-economics lecture, not a generic industrial-organization, macro, or technology-history lecture.
- The focus is on market-level consequences of technological change: inequality, labor share, rents, labor-market power, structural change, worker voice, and institutional response.
- The week must explicitly cover:
  1. how technology changes who captures rents,
  2. how historical technology waves help situate current AI research,
  3. how structural change reallocates workers across sectors and job-quality regimes,
  4. how global and Global South evidence changes the interpretation of technology shocks,
  5. how AI may interact with infrastructure and outsourcing, including electricity/data-center demand and new service/offshoring channels as frontier questions.

Special-topics defaults to enforce:
- include a clearly visible **Core points** box near the top
- no default Extension box
- linked citations only in prose markdown
- use the course-local bibliography only
- if you merge week-specific bibliography entries into `references.bib`, deduplicate repeated BibTeX entries

Required structure:
1. Opening orientation / why this week matters
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Reading Ladder And References
7. Exercises And Discussion Prompts
8. Reproducibility And Code Lab Note
9. Slide Companion Note
10. Bridge Forward

Required Week 5 content:

A. Technology, inequality, and rent capture
The Field Core should clearly cover:
- task and skill inequality
- labor share and the rise of superstar firms
- patent or intangible rents where relevant
- employer concentration / labor-market power / wage-setting implications
- unions, bargaining, platform rules, and labor institutions as mediators of technology incidence

B. Historical technology waves and persistence
Add a substantive section that situates AI/automation inside the longer technology-and-labor literature.
It should ask:
- how long do technology-induced market changes last?
- are they reversible?
- do successive technology waves offset or reinforce each other?
- what can we learn by comparing mechanization, electrification, computerization, robots, and AI?
- when is AI genuinely new versus another task-reallocation episode?

C. Structural change and job quality
Add a substantive section on:
- agriculture -> manufacturing -> services reallocation
- manufacturing -> services transitions in mature economies
- whether technological change improves or worsens job quality during reallocation
- differences between employment reallocation and welfare-improving reallocation
- formal vs informal service-sector absorption where relevant

D. Global / Global South evidence and frontier themes
Add a substantive section on:
- technology adoption in developing countries
- technology sophistication / diffusion / absorptive capacity
- labor-absorbing services and development
- outsourcing / offshoring of tasks or knowledge services
- AI in developing-country labor markets where the evidence exists
- AI-related electricity / data-center / infrastructure demand as an emerging labor-relevant frontier
- how global evidence can differ from high-income-country automation evidence

E. Methods / data layer
Include a clearly labeled methods or data subsection, or make this content visible in a methods box/table, covering:
- market-level concentration and labor-share decompositions
- long-run historical comparisons
- sectoral/firm structural-change decompositions
- shift-share or exposure designs where relevant
- linked firm-worker and plant-level data
- cross-country establishment data / adoption surveys
- energy/infrastructure or spatial data where relevant to frontier AI questions

F. Research lab
The Research Lab should use actual papers and the standard:
- Reproduce
- Diagnose
- Transfer

Paper-selection principle:
- use one primary anchor paper that is central to technology, market structure, and labor-market incidence
- use one challenge/extension paper that pushes into structural change or global evidence
- do not invent replication packages
- be conservative if replication availability is uncertain

Required tone:
- research-facing
- concrete
- labor-focused
- clear about mechanisms, measurement, and external validity

Allowed changes:
- create or refresh the Week 5 chapter
- add a methods/data subsection or box
- add or revise the Research Lab
- merge week bibliography entries into the course bibliography and deduplicate
- make tiny chapter cross-links if needed

Forbidden changes:
- do not rewrite the rest of the course
- do not change bibliography keys unnecessarily
- do not use the labor-series shared bibliography as the primary bibliography
- do not create a default Extension box
- do not drift into generic AI commentary without a labor-market mechanism

Slides requirements:
- create the Week 5 slide deck under the canonical path:
  `books/special-topic5-technology/slides/week5/05-technology-inequality-market-structure-and-labor-market-institutions.tex`
- use the same default professional beamer style already used elsewhere in the repo
- slides should reflect the chapter structure
- include:
  - one slide on rent capture / labor share / superstar firms
  - one slide on historical technology waves
  - one slide on structural change and job quality
  - one slide on global / Global South evidence
  - one slide on methods / data
  - one slide on the Research Lab design
- do not create duplicate slide files outside the canonical `slides/week5/` folder

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/special-topic5-technology/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key
- do not rewrite citation keys unless absolutely necessary

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce -> Diagnose -> Transfer
- use one primary anchor paper that is central to technology, market structure, and labor-market incidence
- use one challenge/extension paper that pushes into structural change or global evidence
- keep the lab student-facing and concrete
- create the canonical lab folder if it does not exist
- include at minimum:
  - `lab.md`
  - `README.md`
  - `run-log.md`
  - `smoke.sh`
  - `environment/requirements.txt`
  - `original/README.md`
  - `original/source-notes.md`
  - `transfer/README.md`
  - `transfer/data-notes.md`
  - `src/`
  - `output/reproduced/`
  - `output/diagnosed/`
  - `output/transfer/`
  - reduced or synthetic teaching-path data if needed
- do not invent replication packages
- be conservative if replication availability is uncertain

Implementation notes:
- keep the chapter labor-focused
- keep the historical-comparison and global sections substantive, not token mentions
- do not drift into generic AI commentary without a labor-market mechanism
- if the chapter already exists, treat it as the canonical content source and sync slides/lab to it rather than rewriting unnecessarily

Validation:
1. run a strict build:
   `cd books/special-topic5-technology && conda run -n research jupyter book build --html --strict`
2. compile the Week 5 slides from the canonical path
3. if a bounded Week 5 lab path is created, ensure it follows the standard folder structure and run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 5 slides compile from the canonical path
5. whether the Week 5 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
