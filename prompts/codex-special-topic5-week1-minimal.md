Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/special-topic5-technology/index.md
- @books/special-topic5-technology/OUTLINE.md
- @books/special-topic5-technology/myst.yml
- @books/special-topic5-technology/README.md
- @books/special-topic5-technology/references.bib
- the files in this pack:
  - source/01-technology-tasks-and-labor-market-adjustment-core-frameworks.md
  - bibliography/01-technology-tasks-and-labor-market-adjustment-core-frameworks.bib
  - tables/01-core-frameworks-map.md
  - tables/01-technology-and-innovation-measurement-map.md
  - tables/01-setting-to-measurement-map.md
  - tables/01-domain-preview-map.md

Goal: draft Week 1 of `special-topic5-technology` as a polished chapter, slide deck, and bounded lab package, using the source-pack-first workflow and the course-local bibliography.

Target outputs:
- `books/special-topic5-technology/01-technology-tasks-and-labor-market-adjustment-core-frameworks.md`
- `books/special-topic5-technology/slides/week1/01-technology-tasks-and-labor-market-adjustment-core-frameworks.tex`
- `books/special-topic5-technology/labs/01-technology-tasks-and-labor-market-adjustment-core-frameworks/`

Non-negotiable Week 1 identity:
- This is the opening framework lecture for Technology, Innovation, and Labor.
- It must stay labor-focused, not drift into generic technology studies.
- It must introduce the measurement problem explicitly:
  - what is technology?
  - what is innovation?
  - how do labor economists operationalize and measure them?
- Students should leave Week 1 understanding that measurement is one of the central open questions in this field.

Non-negotiable thematic content:
1. Technology and innovation must be defined as labor-market objects, not as vague buzzwords.
2. The chapter must distinguish:
   - invention vs adoption vs diffusion
   - labor-substituting vs labor-augmenting technologies
   - automation vs augmentation vs new-task creation
   - general-purpose technologies vs application-specific organizational technologies
3. The chapter must introduce the main framework:
   - technology changes task content
   - then firms and workers adjust
   - then wages, employment, skill prices, mobility, organization, and welfare adjust in equilibrium
4. The chapter must include a dedicated section on measurement as a research frontier:
   - patents and patent text
   - robots / industrial adoption
   - software / IT / digital adoption
   - job-posting and vacancy text
   - task surveys / O*NET-style task descriptions
   - firm adoption / investment / resume or worker-skill based measures
5. The chapter should make clear that different measurement choices imply different empirical objects.

Special-topics conventions to preserve:
- Include a clearly visible **Core points** box near the top.
- Do NOT add a default extension box.
- Use linked citations only in prose markdown: `[@citekey]`
- Keep the fuller prompt structure with slide requirements and implementation notes.
- Use the course-local bibliography file as the primary bibliography.

Chapter structure requirements:
- opening orientation
- Core points box
- Bridge
- Field Core
- Research Lab
- Reading Ladder And References
- Exercises And Discussion Prompts
- Reproducibility And Code Lab Note
- Slide Companion Note
- Bridge Forward

Field Core requirements:
- include a short formal/conceptual framework that maps:
  technology/innovation -> tasks -> skills -> worker/firms adjustment -> equilibrium outcomes
- include a dedicated section called something like:
  `### Measurement as a Research Problem`
- use the supplied tables naturally in the chapter where appropriate

Research Lab requirements:
- follow Reproduce -> Diagnose -> Transfer
- primary anchor should be a measurement-oriented paper if feasible
- strong primary options are:
  - Webb (2020) for task/patent-based exposure logic
  - or Kogan et al. (worker-level technology exposure) if that is easier to structure
- the lab should not overclaim official replication availability if uncertain
- if no official materials are available locally, create a reduced pedagogical path
- the lab should help students understand how different measurement choices create different empirical conclusions

Slide requirements:
- place slide source only in:
  `books/special-topic5-technology/slides/week1/`
- no duplicate slide source in the book root
- slides should mirror the chapter logic:
  - framework
  - measurement problem
  - main literature map
  - research design / lab logic

Bibliography requirements:
- merge any missing entries from the week bibliography into:
  `books/special-topic5-technology/references.bib`
- deduplicate repeated BibTeX entries
- keep one canonical entry per cite key
- do not rely on the labor-series shared bibliography

Implementation notes:
- use the local `research` conda environment for validation
- preserve MyST validity
- keep edits minimal outside Week 1
- if `myst.yml` needs week wiring, update it minimally
- if `index.md` needs the Week 1 link wired, update it minimally
- do not rewrite the course scaffold beyond what Week 1 needs

Validation:
1. run a strict build:
   `cd books/special-topic5-technology && conda run -n research jupyter book build --html --strict`
2. if you create the lab folder, create a bounded `smoke.sh` if appropriate
3. if the build breaks, fix the smallest issue and rerun

At the end, report:
1. files created/changed
2. which paper(s) anchor the Research Lab
3. which bibliography entries were merged
4. pass/fail for the strict build
5. any manual follow-up points
