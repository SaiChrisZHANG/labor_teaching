# Labor I

Internal workflow note for the standalone MyST / Jupyter Book course in this directory.

## Commands

Run from this directory:

```bash
conda run -n research jupyter book build --html --strict
conda run -n research --live-stream jupyter book start
conda run -n research jupyter book clean --templates --cache -y
```

## Bibliography

Labor I uses the shared labor-series bibliography at `../../shared/bibliography/references.bib`. Keep course-specific structural notes in this directory and keep weekly slide sources under `slides/weekN/`.
