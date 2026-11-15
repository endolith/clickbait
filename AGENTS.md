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

- Keep `! Homepage` and license lines at top.
- Test rules against real pages when possible (manual).

## Validator limitations

`scripts/validate_filters.py` is a smoke test, not a filter parser:

- It recognizes only `[Adblock Plus x.y]` header blocks, and flags duplicates of them.
- It skips every line containing `##`, `#@`, `#?`, or `$`, so cosmetic rules and network options are not validated.
- It skips `@@` exception rules, `/regex/` rules, and lines starting with `#`.
- Network patterns get only a heuristic check: whitespace-free lines containing one of `| . * ^ /`.
