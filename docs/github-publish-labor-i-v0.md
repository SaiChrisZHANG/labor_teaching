# Publish Labor I version 0 to GitHub

The cleanest publication path is:

1. make sure the local repository is committed and tagged
2. create a new GitHub repository without pre-populating it with a README, license, or gitignore
3. push the local repository to GitHub

GitHub's official docs recommend creating a new repository and, when pushing an existing local repository, avoiding initialization with README, license, or gitignore files to prevent conflicts. They also document both a web-flow for creating a new repository and a CLI flow using `gh repo create`. See:
- GitHub Docs: creating a new repository
- GitHub Docs: adding locally hosted code to GitHub

## Recommended repository name

`labor-teaching-platform`

Alternative if you want Labor I isolated first:

`labor-i-phd-field-course`

## Minimal publish sequence with Git

```bash
git init
git add .
git commit -m "Freeze Labor I version 0"
git tag -a labor-i-v0 -m "Labor I version 0"
```

Then create a new empty GitHub repository and push:

```bash
git branch -M main
git remote add origin git@github.com:SaiChrisZHANG/YOUR-REPO-NAME.git
git push -u origin main
git push origin labor-i-v0
```

## Minimal publish sequence with GitHub CLI

```bash
gh repo create YOUR-REPO-NAME --public --source=. --remote=origin --push
```

If you use the CLI flow, GitHub documents that `gh repo create` can create the repository and push an existing local repository in one step.

## Before publishing

- verify `_build/` is not committed
- verify LaTeX auxiliary files are not committed
- decide whether you want generated slide PDFs committed or regenerated locally
- confirm the landing page text is the public-facing version you want
