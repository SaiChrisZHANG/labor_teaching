# AGENTS.md

## Repository purpose

This repository hosts a public teaching platform in labor economics and applied methods. It contains:
- Jupyter Book / MyST course books
- LaTeX Beamer slide decks
- executable code labs
- shared methods/toolkit modules
- public-facing teaching artifacts for the academic job market

## Core portfolio

Primary courses:
1. Labor I: Workers, Human Capital, and Inequality
2. Labor II: Firms, Frictions, and Institutions
3. Empirical Methods for Applied Economics
4. Behavioral Labor

Incubator course:
5. Labor Markets and Political/Cultural Institutions

## Audience layers

Every module must serve three audiences:
- Bridge: advanced undergraduates / master's students
- Field Core: PhD students
- Research Lab: frontier and open research directions

## Language policy

- Python is the backbone language for public labs and reproducible examples.
- R is allowed for packages or literatures where R is a teaching advantage.
- Stata is allowed for selected applied-economics workflows and replication snippets.
- Do not create parallel code in all three languages by default.
- Prefer one primary Python workflow plus small R/Stata companion notes when justified.

## Non-negotiable structure for each teaching module

Each module should contain, in this order:
1. title and learning objectives
2. Bridge section
3. Field Core section
4. Research Lab section
5. Methods Box
6. reading ladder
7. exercises / discussion prompts
8. reproducibility or code lab note
9. slide companion note

## Special-topics chapter conventions

Special-topics chapters follow the standard audience layers, with these additional defaults:
- include a clearly visible **Core points** box near the top of every chapter
- do not require an Extension or Optional Extension box by default
- place genuine frontier or optional material inside **Field Core** or **Research Lab** unless a separate extension box is truly warranted
- use linked citation syntax for prose markdown citations: `[@citekey]`
- do not use bare prose citations like `@citekey` or backticked prose citations like `` `@citekey` `` outside true code/example contexts

## Writing style

- Clear, high-signal, and graduate-level
- No filler
- State the economic question early
- Distinguish theory, evidence, and identification clearly
- Use notation consistently across books
- Prefer modular, reusable explanations over one-off prose
- Surface tradeoffs and competing interpretations where they matter

## Slide philosophy

Slides should not duplicate the book verbatim.
Each deck should:
- define the question
- show the conceptual map
- present only the essential equations or figures
- isolate identification logic
- end with takeaways and open questions

## File conventions

- Use kebab-case file names
- Use text-based source files when possible
- Keep shared content in `shared/`
- Keep course-specific content in `books/<course>/`
- Place weekly slide sources and compiled slide PDFs under `books/<book>/slides/weekN/`
- Treat `books/<book>/slides/weekN/<week-slug>.tex` as the canonical slide source path for every week
- Do not place canonical slide files directly in `books/<book>/` or directly in `books/<book>/slides/`
- Reuse bibliography entries across books
- Avoid duplicated figures and duplicated method explainers

## Environment conventions

- The canonical local conda environment for repo workflows is `research`
- Local Python and Jupyter Book commands should use `conda run -n research ...` unless the instructions explicitly say the environment has already been activated with `conda activate research`
- Preview commands should use `conda run -n research --live-stream jupyter book start` when output visibility matters

## Done criteria for content tasks

A module is not done until it has:
- clear learning objectives
- the full Bridge / Field Core / Research Lab structure
- a reading ladder
- at least one exercise or discussion block
- slide outline or completed slide deck
- explicit note on code lab or replication opportunity

## Weekly acceptance criteria

A week is not done until:
- the strict HTML build passes
- preview starts and prints a localhost URL
- slides compile
- the lab smoke test passes

## Validation rules

When you modify or create content:
- check internal links
- check cross-references
- ensure headings are hierarchical and consistent
- ensure code blocks are labeled by language
- ensure notation is consistent with the shared style guide
- do not invent citations or bibliographic metadata
- flag missing references explicitly
- treat non-fatal Node or font warnings as acceptable only when the required outputs still succeed

## Constraints

- Do not sprawl the course scope without updating the outline first.
- Do not add a new framework or method section unless it clearly belongs in the module.
- Do not write generic literature reviews with no labor-economics anchor.
- Do not make every page interactive.
- Prefer durable core content plus optional frontier extensions.

## Preferred workflow for difficult tasks

For any task that touches more than one file or changes course structure:
1. read the local outline and relevant shared templates
2. produce a short written plan
3. identify files to be created or modified
4. implement in small coherent batches
5. verify consistency before finishing

## Preferred workflow for content generation

When drafting new teaching content:
- start from the outline
- write the learning goals first
- specify the economic question
- state the canonical models or empirical designs
- connect them to labor applications
- end with research extensions

## What to avoid

- bloated lecture notes
- unstructured reading dumps
- undocumented code
- mixed notation across chapters
- unexplained jumps from intuition to formalism
- unexplained jumps from econometric method to application
