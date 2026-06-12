#!/usr/bin/env python3
"""Validate Adblock Plus filter list syntax (minimal checks)."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    headers = re.compile(r"^\[(Adblock Plus \d+\.\d+)\]$")
    seen_headers: set[str] = set()

    for i, line in enumerate(text, 1):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("!"):
            continue
        if headers.match(stripped):
            if stripped in seen_headers:
                errors.append(f"{i}: duplicate header {stripped}")
            seen_headers.add(stripped)
            continue
        if stripped.startswith("@@"):
            continue
        if stripped.startswith("/") and stripped.endswith("/"):
            continue
        if "##" in stripped or "#@" in stripped or "#?" in stripped:
            continue
        if "$" in stripped:
            continue
        if stripped.startswith("||") or stripped.startswith("|") or stripped.startswith("."):
            continue
        if stripped.startswith("http"):
            continue
        if stripped.startswith("#"):
            continue
        # Bare domain / hostname blocks (common in older lists)
        if "." in stripped and " " not in stripped and "/" not in stripped:
            continue
        errors.append(f"{i}: unrecognized rule syntax: {stripped[:80]}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <filter.txt>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    errors = validate(path)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"{len(errors)} validation error(s)", file=sys.stderr)
        return 1
    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
