# Codex Prompt Pack

Use these as starting prompts inside Codex. Keep `AGENTS.md` and the relevant outline files in context.

---

## 1. Scaffold the monorepo

Read `AGENTS.md`, `PLANS.md`, and `docs/repo-blueprint.md`. Then scaffold the repository exactly as described, creating all missing directories and starter files. Do not add extra frameworks or infrastructure. After scaffolding, summarize what was created and list any placeholders that still need human input.

---

## 2. Build the shared toolkit skeleton

Read `docs/portfolio-charter.md`, `AGENTS.md`, and `shared/templates/module-template.md`. Create skeleton pages for the shared toolkit modules:
1. labor market facts and datasets
2. identification primer
3. reproducibility workflow
4. structural estimation primer
5. treatment heterogeneity / causal ML primer
6. text and LLM measurement primer

Each page should include learning objectives, section headings, and a placeholder reading ladder, but should not invent citations.

---

## 3. Draft the first Labor I module

Read `AGENTS.md`, `books/labor-i/OUTLINE.md`, and `shared/templates/module-template.md`. Draft the first complete Labor I module as a polished teaching note. Use the full Bridge / Field Core / Research Lab structure. Include a short Methods Box and a reading ladder. Keep it labor-economics focused and avoid generic literature review prose.

---

## 4. Create the matching slide deck

Read the completed Labor I module and `shared/templates/slide-outline-template.tex`. Produce a Beamer slide deck at `books/<book>/slides/weekN/<week-slug>.tex` that is shorter and sharper than the chapter. Keep only the essential figures, equations, and identification logic. End with takeaways and two open questions.

---

## 5. Add the first Python code lab

Read the completed module and create a Python lab that either simulates the mechanism or reproduces one stylized fact. The lab must be runnable, clearly commented, and designed for teaching. Include one extension exercise for students.

---

## 6. Add optional R and Stata sidecars

Read the Python lab and propose whether R and/or Stata sidecars are justified. If they are, create concise companion scripts that mirror the core output without duplicating every detail. If they are not justified, explain why not and stop.

---

## 7. Draft the methods course outline

Read `books/empirical-methods/OUTLINE.md` and `docs/portfolio-charter.md`. Expand the methods outline into module-level descriptions with explicit links to labor applications. Keep the four-block structure:
- design-based causal inference
- structural estimation
- ML for applied economics
- text / LLM / computational measurement

---

## 8. Draft the behavioral labor outline into a syllabus

Read `books/behavioral-labor/OUTLINE.md` and `shared/templates/syllabus-template.md`. Write a polished syllabus with learning goals, module structure, assessment options, and a reading philosophy. Keep the course visibly anchored in both behavioral economics and labor economics.

---

## 9. Build the incubator page

Read `books/institutions-labor/OUTLINE.md` and `docs/portfolio-charter.md`. Create a polished incubator course page for "Labor Markets and Political/Cultural Institutions" with:
- course rationale
- full syllabus outline
- 4 showcase modules
- short note on methods and sources
Do not present it as a fully built course.

---

## 10. Create a bibliography cleanup pass

Inspect all course outlines and any drafted modules. Create or update `shared/bibliography/references.bib` using only citations that are explicitly provided in the source text. Flag missing bibliographic information rather than inventing it.

---

## 11. Build a job-market-facing landing page

Read the course outlines and `docs/portfolio-charter.md`. Create a public landing page that presents the teaching platform as a coherent portfolio. Emphasize:
- labor field depth
- empirical breadth
- behavioral specialization
- institutions incubator
- public code and reproducibility

---

## 12. Write a project-local AGENTS refinement

Read all existing files in the repository and revise `AGENTS.md` so that it reflects the actual repo structure, build commands, and content conventions. Keep the instructions concrete and reusable. Remove anything no longer true.

---

## 13. Generate a PLAN before editing

Before you change anything, read `PLANS.md` and create a task-specific plan in that format. Wait until the plan is complete before writing or modifying files.
