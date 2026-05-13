Read @AGENTS.md, @docs/repo-workflow.md, @books/special-topic4-urban/index.md, @books/special-topic4-urban/OUTLINE.md, @books/special-topic4-urban/myst.yml, @books/special-topic4-urban/README.md, @books/special-topic4-urban/references.bib, and the full contents of:

- `books/special-topic4-urban/`
- `books/special-topic4-urban/sources/`
- `books/special-topic4-urban/slides/`
- `books/special-topic4-urban/labs/`
- `books/special-topic4-urban/assets/tables/`

Also read the week-specific files being supplied for this task:
- `special_topic4_urban_week6_edit_pack/source/06-synthesis-frontier-questions-and-student-research-designs.md`
- `special_topic4_urban_week6_edit_pack/bibliography/06-synthesis-frontier-questions-and-student-research-designs.bib`
- all markdown files under `special_topic4_urban_week6_edit_pack/tables/`

Goal: build Week 6 of the Urban and Labor course as the capstone lecture:
`Synthesis, Frontier Questions, and Student Research Designs`.

This is a full week-generation task using the established special-topics workflow.

Non-negotiable conventions:
- Core points box required near the top of the chapter.
- No default Extension box.
- Linked citation syntax only in prose markdown: `[@citekey]`.
- Use the course-local bibliography:
  `books/special-topic4-urban/references.bib`
- Merge any missing entries from the supplied week bibliography into that course bibliography.
- Deduplicate repeated BibTeX entries if duplicates appear.
- Preserve only one canonical entry per cite key.
- Slides must live under:
  `books/special-topic4-urban/slides/week6/`
- The chapter must be wired into the live book cleanly.
- Use the `research` conda environment for validation.

Week identity:
- This is the final synthesis week of a 6-week compact advanced special topic.
- It should integrate space, housing, segregation, safety/environment, migration, and local labor demand into one urban-labor research architecture.
- It should function as a launchpad for student projects.
- It should make clear where urban-labor research is now and where the frontier is going.
- It should stay labor-focused, not become a generic urban-economics recap.

Required outputs:
1. Chapter markdown:
   `books/special-topic4-urban/06-synthesis-frontier-questions-and-student-research-designs.md`
2. Slide source:
   `books/special-topic4-urban/slides/week6/06-synthesis-frontier-questions-and-student-research-designs.tex`
3. Lab handout:
   `books/special-topic4-urban/labs/06-synthesis-frontier-questions-and-student-research-designs/lab.md`
4. Smoke script:
   `books/special-topic4-urban/labs/06-synthesis-frontier-questions-and-student-research-designs/smoke.sh`
5. Any week-local helper files minimally needed for the lab folder structure.

Chapter requirements:
- Short opening orientation explaining why urban labor research is a distinct and valuable field.
- Core points box with concise bullet points.
- Bridge
- Field Core
- Research Lab
- Reading ladder / references block
- Forward-looking final section on frontier opportunities

The Field Core should include:
1. a synthesis of the course’s major urban-labor mechanisms:
   - commuting/access
   - housing and rents
   - segregation/neighborhood exposure
   - safety/environmental risk
   - migration/local adjustment
2. a research-design architecture:
   - labor outcome
   - urban mechanism
   - unit of geography
   - counterfactual/comparison
   - spatial equilibrium/incidence issue
   - welfare object
3. a “where the literature is now” discussion
4. frontier questions, including examples such as:
   - remote work and hybrid geography
   - housing reform and labor access
   - climate/heat and urban labor
   - commuting, monopsony, and local labor market power
   - place-based policy and labor mobility
   - AI / digital infrastructure / urban opportunity
   - child opportunity and intergenerational mobility in cities
   - urban redevelopment / gentrification / displacement and labor outcomes

Research Lab requirements:
- It must be a genuine project-incubator section.
- It should help students move from a broad urban phenomenon to a labor-economics research question.
- It should explicitly discuss what makes an urban labor paper broadly interesting beyond one city.
- It should include a short section on common empirical failure modes in this field.

Tables to use/integrate:
- `10-research-design-template.md` equivalent supplied in this pack
- `where-the-field-is-and-where-it-is-going` style summary
- portability/relevance map
- frontier project opportunities map

You may rename table captions/labels inside the chapter for fit, but keep the files and their logic.

Slides requirements:
- Use the professional default Beamer style already established in the repo.
- Slides should mirror the chapter structure.
- Include a clean project-design slide and a frontier-opportunities slide.
- Keep slide path conventions exact.

Lab requirements:
- This is a design-oriented lab, not a heavy replication lab.
- It should guide students to build a one-page urban-labor research memo.
- It may include a small bounded empirical exercise if helpful, but it should not depend on heavy external data.
- The smoke path should be lightweight and runnable.

Important implementation notes:
- Do not rewrite earlier weeks.
- Do not change substantive course structure outside the minimal wiring needed to add Week 6.
- If `myst.yml` or `index.md` needs a week-6 wiring update, do that cleanly.
- Do not create duplicate slide sources in the book root.
- Do not use bare `@citekey` or backticked citation keys in prose.
- Preserve filenames and paths exactly as specified above.

Validation:
1. Build the book strictly:
   `cd books/special-topic4-urban && conda run -n research jupyter book build --html --strict`
2. Compile slides from:
   `books/special-topic4-urban/slides/week6/06-synthesis-frontier-questions-and-student-research-designs.tex`
3. Run the week-6 lab smoke test.
4. If anything fails, fix the smallest issue and rerun.

At the end, report:
- files created/changed
- whether week 6 is correctly wired into the book
- whether the course bibliography was updated and deduplicated
- pass/fail for strict build, slides, and lab smoke
- any remaining manual review items