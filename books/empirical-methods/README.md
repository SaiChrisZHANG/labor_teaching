# Empirical Methods for Applied Economics

Internal workflow and build note for the standalone MyST / Jupyter Book course in this directory.

## Course Structure

The course is block-based. Core Blocks 1-4 form the main methods sequence: reduced-form and design-based methods, structural estimation, machine learning for applied economics, and text/computational/LLM workflows. Flexible Optional Blocks 5-6 cover spatial methods and network methods and can be taught at the end of the course or as separate add-ons.

Top-level lecture chapters live as `NN-*.md` files in this directory. `OUTLINE.md` is an internal planning/reference file and is not part of the live book navigation. `index.md` is the syllabus-style landing page.

## Book Commands

Run from `books/empirical-methods/`:

```bash
conda run -n research jupyter book build --html --strict
conda run -n research --live-stream jupyter book start
conda run -n research jupyter book clean --templates --cache -y
```

## Slides And Labs

Slide sources and compiled PDFs live under `slides/weekN/`. The canonical slide source path is `slides/weekN/<lecture-slug>.tex`.

```bash
conda run -n research latexmk -cd -pdf -interaction=nonstopmode slides/weekN/<lecture-slug>.tex
```

Labs live under `labs/<lecture-slug>/` and should keep the standard reproducibility layout: `README.md`, `lab.md`, `run-log.md`, `smoke.sh`, `environment/`, `original/`, `transfer/`, `src/`, and `output/`. Run a lab smoke test from its lab directory with:

```bash
ENV_NAME=research bash smoke.sh
```

## Sources, Assets, And Bibliography

Source-pack notes live in `sources/`. Shared teaching tables and other reusable display assets live in `assets/`, especially `assets/tables/`.

This course uses the course-local `references.bib`. Do not rely on the labor-series shared bibliography as the primary bibliography for this course. Future reading packs and lecture references should be added locally unless a shared bibliography refactor is explicitly approved.
