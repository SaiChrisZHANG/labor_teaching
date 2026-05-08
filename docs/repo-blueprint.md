# Repository Blueprint

## Proposed monorepo structure

```text
labor-teaching/
  README.md
  AGENTS.md
  PLANS.md
  .codex/
    config.toml
  docs/
    portfolio-charter.md
    repo-blueprint.md
  shared/
    bibliography/
      references.bib
    templates/
      module-template.md
      syllabus-template.md
      slide-outline-template.tex
    style/
      code-policy.md
      pedagogy-style-guide.md
    methods-boxes/
    figures/
    code/
      python/
      r/
      stata/
  prompts/
    codex-prompt-pack.md
  books/
    labor-i/
      OUTLINE.md
    labor-ii/
      OUTLINE.md
    empirical-methods/
      OUTLINE.md
    special-topic1-behavioral/
      OUTLINE.md
    special-topic2-institutions/
      OUTLINE.md
```

## Naming rules

- course directories use kebab-case
- module files use an ordered prefix when sequencing matters
- slide files mirror module names
- datasets and generated figures use deterministic names

## Example module naming

```text
books/labor-i/
  01-labor-market-facts.md
  02-static-and-dynamic-labor-supply.md
  03-human-capital.md
```

## Cross-course reuse rules

Put reusable content in `shared/` when:
- the same method explanation appears in 2+ courses
- the same figure appears in 2+ courses
- the same code utility is used in 2+ labs

Keep content course-local when:
- the framing is course-specific
- the pacing differs substantially by audience
- the reading ladder is specific to the course

## Public-facing expectations

Each course should eventually expose:
- a landing page
- syllabus
- weekly/module map
- notes
- slides
- exercises
- selected code labs
