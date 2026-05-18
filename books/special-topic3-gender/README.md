# Gender Study

Internal workflow note for the standalone MyST / Jupyter Book course in this directory.

## Commands

Run from this directory:

```bash
conda run -n research jupyter book build --html --strict
conda run -n research --live-stream jupyter book start
conda run -n research jupyter book clean --templates --cache -y
```

## Bibliography

This special-topics course uses the course-local `references.bib`. Keep course reading-pack additions local unless a shared bibliography refactor is explicitly approved.
