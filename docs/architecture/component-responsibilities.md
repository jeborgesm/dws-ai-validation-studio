# Component Responsibilities

## API layer

Owns HTTP concerns only:

- Route definitions.
- File-extension and empty-file rejection.
- Mapping known parsing errors to explicit HTTP responses.
- Returning typed response contracts.
- Cleaning up temporary resources.

It must not contain dataset profiling rules or persistence logic.

## Core profiler

Owns deterministic dataset inspection:

- Row and column counts.
- Duplicate-row detection.
- Per-column missing-value counts and percentages.
- Unique-value counts.
- Basic inferred data types.
- Threshold evaluation.

It must not know about HTTP, FastAPI, or cloud services.

## Contracts

Pydantic models provide:

- Runtime validation.
- Generated OpenAPI schemas.
- Explicit field constraints.
- Stable boundaries between internal logic and external clients.

## Future orchestration layer

Will coordinate multi-step validation runs, persistence, artifact generation, and status transitions. It should remain independent from any one UI or cloud provider.

## Future infrastructure adapters

Infrastructure implementations will provide PostgreSQL, S3, SageMaker, GitHub, SharePoint, Power BI, and workflow integration behind explicit interfaces where that abstraction provides real value.
