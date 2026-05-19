Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/09-prediction-regularization-and-applied-measurement.md if it exists
- @books/empirical-methods/10-high-dimensional-controls-heterogeneity-and-double-debiased-ml.md if it exists
- @books/empirical-methods/11-causal-ml-policy-learning-and-external-validity.md if it exists

Goal: create Lecture 12 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/12-text-as-data-and-computational-measurement.md`
- `books/empirical-methods/slides/week12/12-text-as-data-and-computational-measurement.tex`
- `books/empirical-methods/labs/12-text-as-data-and-computational-measurement/`

Use these as the intellectual source of truth:
1. the lecture source pack and tables from this week-specific pack
2. the course outline
3. the chapter architecture already used in earlier empirical-methods lectures

Lecture 12 identity to preserve:
- Lecture 12 is NOT a generic NLP or computer-vision lecture.
- It should teach unstructured data as an applied-economics measurement environment.
- It should broaden the block beyond text to include:
  - text/documents
  - images/satellite/street-view/scans
  - audio/speech
  - video/multimodal data
- The focus is on extracting information and constructing variables that economists can use in descriptive, causal, and structural work.
- Methods should be introduced conceptually and with references, not as a deep engineering class.

Non-negotiable content:
A. Why unstructured data matter for applied economics research
B. Measurement model: from raw unstructured object to economic variable
C. Core extraction families:
   - dictionaries / rules
   - supervised classification
   - embeddings / similarity
   - multimodal features
D. Modality-specific opportunities and pitfalls:
   - text
   - images
   - audio
   - video
E. Applications in economics papers
F. Research Lab with a concrete Reproduce → Diagnose → Transfer workflow
G. Methods Box with references/resources for students who want to go deeper technically

Required chapter structure:
1. Opening Orientation
2. Core points box
3. Bridge
4. Field Core
5. Research Lab
6. Methods Box
7. Reading Ladder And References
8. Exercises And Discussion Prompts
9. Reproducibility And Code Lab Note
10. Slide Companion Note
11. Bridge Forward

Equations / math that should appear:
- a generic measurement model:
  `M_i = g(U_i; \theta) + \varepsilon_i`
  where `U_i` is unstructured input and `M_i` is the constructed economic measure
- supervised empirical risk minimization:
  `\hat f = \arg\min_f \frac{1}{n}\sum_i L(y_i, f(x_i)) + \lambda P(f)`
- at least one simple dictionary/share or embedding aggregation equation
- a short note on measurement error propagation into downstream analysis

Paper anchors to use if helpful:
- Gentzkow, Kelly, and Taddy on text as data
- Hansen et al. on remote work from job postings
- Webb on AI exposure via patents/tasks text
- Hassan et al. on text-based firm exposure to epidemic risk
- Jean et al. on satellite imagery and poverty measurement
- Baragwanath / related urban-market imagery work
- Gorodnichenko, Pham, and Talavera on voice as economic information
- Haaland et al. on open-ended responses / LLMs in economics

Slides requirements:
- create the canonical slide deck:
  `books/empirical-methods/slides/week12/12-text-as-data-and-computational-measurement.tex`
- use the same professional default beamer style already used elsewhere in the repo
- include one slide each on:
  - measurement model
  - text applications
  - image/satellite applications
  - audio/video applications
  - modality-specific failure modes
  - research lab design
- do not create duplicate slide files outside `slides/week12/`

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- pick a primary anchor that is feasible for a reduced pedagogical path
- a good default is job-posting text / remote-work or task-exposure style measurement
- if full official replication data are not present locally, create a bounded synthetic teaching path
- create the canonical lab folder if it does not exist
- include at minimum:
  - `lab.md`
  - `README.md`
  - `smoke.sh`
  - `src/`
  - `output/reproduced/`
  - `output/transfer/`

Implementation notes:
- keep the lecture research-oriented
- methods must be tied to papers and implementation caveats
- do not turn the lecture into a software tutorial
- linked citations only in prose markdown
- preserve the course’s canonical structure and local bibliography policy

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Week 12 slides from the canonical path
3. if a bounded Week 12 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 12 slides compile from the canonical path
5. whether the Week 12 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
