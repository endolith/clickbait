# AGENTS.md

Adblock Plus filter list (`clickbait.txt`). Not executable code.

## Workflow

1. Use a topic branch; do not push directly to `master`.
2. Filter rules must stay valid ABP syntax.
3. Run local validation before pushing (see below).
4. Do not merge pull requests; leave that to the maintainer.

## Local validation

```bash
python3 scripts/validate_filters.py clickbait.txt
```

On Windows, use `python` instead of `python3`.

## CI

GitHub Actions runs the same validator on every PR.

## Rules

- The validator rejects unrecognized lines and duplicate `[Adblock Plus x.y]` header blocks. It recognizes only that header form, and it skips every line containing `##`, so cosmetic rules are not validated.
- Keep `! Homepage` and license lines at top.
- Test rules against real pages when possible (manual).
