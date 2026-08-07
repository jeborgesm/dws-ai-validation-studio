# Testing Strategy

## Objectives

Tests provide confidence that validation evidence is computed consistently and that failures are explicit. The strategy favors deterministic, fast tests at the lowest useful layer.

## Test layers

### Unit tests

Exercise core profiling behavior with temporary files and controlled data. These tests verify counts, thresholds, findings, and edge cases without HTTP.

### API tests

Exercise route behavior, response contracts, status codes, and integration between FastAPI and the core profiler.

### Contract tests

Future tests will snapshot or validate OpenAPI and generated artifact schemas to detect accidental breaking changes.

### Integration tests

Future tests will cover PostgreSQL, object storage, SageMaker adapters, and background workflows using isolated environments or emulators where appropriate.

### End-to-end tests

Future tests will execute a complete validation run from upload through persisted evidence and report generation.

## Quality gates

GitHub Actions runs:

1. Ruff linting.
2. Strict mypy type checking.
3. Pytest with coverage reporting.

A passing build is necessary but not sufficient. Documentation and governance changes are reviewed as part of the definition of done.

## Test-data principles

- Small enough to understand by inspection.
- Synthetic unless a public source is documented.
- Explicitly designed to trigger both passing and failing cases.
- No secrets or personal information.

## Future test cases

- Empty CSV with headers only.
- Malformed encodings and delimiters.
- Extremely wide datasets.
- File-size enforcement.
- NaN, infinite values, and mixed types.
- Threshold boundaries exactly equal to limits.
- Deterministic model metrics and random seeds.
- Drift detection false positives and false negatives.
