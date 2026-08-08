# Contributing

This repository is a public proof of concept and engineering reference implementation. Contributions should preserve its evidence-first and responsible-use goals.

## Before opening a change

- Keep the change focused and explain the problem it solves.
- Add or update tests.
- Update documentation in the same change.
- Add an ADR when changing architecture, governance, security posture, or a major dependency.
- Use only public, synthetic, or explicitly authorized data.
- Never include proprietary, customer, or personal confidential information.

## Local checks

```bash
ruff check .
mypy src
pytest
```

## Commit guidance

Prefer small commits with an imperative subject, for example:

- `Add duplicate-row validation finding`
- `Document upload threat model`
- `Add boundary test for missing-value threshold`
