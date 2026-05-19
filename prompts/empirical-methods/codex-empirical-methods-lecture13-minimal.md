Read:
- @AGENTS.md
- @docs/repo-workflow.md
- @books/empirical-methods/index.md
- @books/empirical-methods/OUTLINE.md
- @books/empirical-methods/myst.yml
- @books/empirical-methods/references.bib
- @books/empirical-methods/12-text-as-data-and-computational-measurement.md if it exists

Goal: create Lecture 13 of the empirical methods course as a fully synchronized lecture with canonical chapter, slides, and lab outputs, matching the established empirical-methods workflow.

Canonical output files:
- `books/empirical-methods/13-extraction-classification-embeddings-and-validation.md`
- `books/empirical-methods/slides/week13/13-extraction-classification-embeddings-and-validation.tex`
- `books/empirical-methods/labs/13-extraction-classification-embeddings-and-validation/`

Use these as the intellectual source of truth:
1. the lecture source pack and tables from this week-specific pack
2. the course outline
3. Lecture 12 as the immediate conceptual predecessor

Lecture 13 identity to preserve:
- Lecture 13 is NOT another extraction lecture.
- It focuses on validation, robustness, benchmark design, measurement error, subgroup performance, drift, and downstream interpretation.
- It should treat validation as part of identification: if the constructed variable is biased or unstable, the economic interpretation changes.
- It should cover text, images, audio, and video/unstructured data generally, not just text.
- It should stay tightly connected to applied economics papers and the way they defend their choices.

Non-negotiable content:
A. Labeled data, annotation protocols, and benchmark construction
B. Precision, recall, F1, calibration, subgroup performance, and drift
C. Inter-rater reliability and human review
D. Embedding-based similarity and external validation
E. Measurement error and its consequences for downstream descriptive and causal work
F. Robustness / sensitivity / transportability checks
G. Research Lab with Reproduce → Diagnose → Transfer workflow
H. Methods Box with references/resources for deeper technical study

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
- precision, recall, and F1
- calibration:
  `E[Y | \hat p = p] = p`
- Cohen’s kappa or another inter-rater reliability statistic
- a simple misclassification / measurement-error relation, e.g.
  `\tilde X_i = X_i + \nu_i`
  or a binary misclassification setup
- a short statement of how downstream bias can emerge when validation fails

Paper anchors to use if helpful:
- Gentzkow, Kelly, and Taddy on validation principles in text work
- Hansen et al. on classification and human labels for remote work
- Haaland et al. on open-ended responses and LLM-assisted coding
- Jean et al. on image-based measurement and external validation
- Gorodnichenko, Pham, and Talavera on audio-derived variables
- Blattman et al. on qualitative validation / measurement error
- Bound on measurement error as a conceptual anchor if useful

Slides requirements:
- create the canonical slide deck:
  `books/empirical-methods/slides/week13/13-extraction-classification-embeddings-and-validation.tex`
- use the same professional default beamer style already used elsewhere in the repo
- include one slide each on:
  - annotation and benchmark design
  - precision/recall/calibration
  - subgroup performance and fairness
  - measurement error in downstream economics
  - validation examples from papers
  - research lab design
- do not create duplicate slide files outside `slides/week13/`

Bibliography requirements:
- merge any missing entries from the week-specific `.bib` into
  `books/empirical-methods/references.bib`
- delete repeated / duplicate BibTeX entries if duplicates appear
- keep only one canonical entry per cite key

Research Lab requirements:
- the Research Lab must follow the standard:
  Reproduce → Diagnose → Transfer
- the lab should center on validating a constructed variable rather than only building it
- a good default is to use a labeled text task or a small image/text task with:
  - baseline classifier
  - confusion matrix / calibration
  - subgroup comparison
  - transfer to a new domain
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
- methods must be tied to concrete papers and implementation caveats
- explicitly discuss what validation failure means for causal/descriptive claims
- linked citations only in prose markdown
- preserve the course’s canonical structure and local bibliography policy

Validation:
1. run a strict build:
   `cd books/empirical-methods && conda run -n research jupyter book build --html --strict`
2. compile the Week 13 slides from the canonical path
3. if a bounded Week 13 lab path is created, run its smoke test
4. fix the smallest issue and rerun if needed

At the end, report:
1. files created/changed
2. which references were merged into `references.bib`
3. whether duplicate BibTeX entries were removed
4. whether the Week 13 slides compile from the canonical path
5. whether the Week 13 lab folder now exists and follows the standard structure
6. whether the strict build passes
7. any manual follow-up points
