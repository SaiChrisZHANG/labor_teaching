# Labor I book

This directory is configured as a standalone Jupyter Book / MyST project for the first semester of the labor sequence.

## Local setup

Use the repository-standard conda environment:

```bash
conda activate research
```

## Preview locally

```bash
conda run -n research --live-stream jupyter book start
```

## Build with strict checks

```bash
conda run -n research jupyter book build --html --strict
```

## Clean build artifacts

```bash
conda run -n research jupyter book clean --templates --cache -y
```

## Slide compilation

Weekly slide decks are written in LaTeX Beamer using a built-in theme and the canonical source path `slides/weekN/<week-slug>.tex`.

```bash
latexmk -pdf -interaction=nonstopmode slides/week2/02-static-labor-supply.tex
```

## File map

```text
myst.yml
index.md
OUTLINE.md
01-labor-market-facts.md
slides/
  week1/
  week2/
labs/
```

## Notes

- The site configuration uses `myst.yml`.
- Weekly slide sources and compiled PDFs live under `slides/weekN/`.
- The slide deck is intentionally simple so a more distinctive visual style can be chosen later without rewriting content.
- The Week 1 lab includes a pedagogical reduced-data path plus a place to drop the official replication package.
