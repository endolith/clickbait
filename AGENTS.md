# AGENTS.md

Adblock Plus filter list (`clickbait.txt`). Not executable code.

## Workflow

1. Branch `cursor/<topic>-6eeb`.
2. Filter rules must stay valid ABP syntax.
3. Run local validation before pushing (see below).
4. Do not merge.

## Local validation

```bash
python3 scripts/validate_filters.py clickbait.txt
```

## CI

GitHub Actions runs the same validator on every PR.

## Rules

- No duplicate `! Title` headers or duplicate option lines.
- Keep `! Homepage` and license lines at top.
- Test rules against real pages when possible (manual).
