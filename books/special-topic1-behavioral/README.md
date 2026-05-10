# Behavioral Labor

This directory is the standalone MyST / Jupyter Book shell for the Behavioral Labor special-topics course.

## Local build

From this directory:

```bash
conda run -n research jupyter book build --html --strict
```

## Note

`references.bib` is course-local and should absorb future weekly reading packs for this course.

Behavioral Labor chapters should include a visible **Core points** box near the top. Extension boxes are optional rather than default; frontier material can live inside **Field Core** or **Research Lab**. Use linked citation syntax in prose markdown, such as `[@citekey]`.
