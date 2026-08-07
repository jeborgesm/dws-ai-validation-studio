# ADR-0003: Use Pydantic for External Contracts

- Status: Accepted
- Date: 2026-08-06

## Decision

Represent API-facing profiles, findings, and reports with Pydantic models.

## Rationale

AI/ML validation evidence must be explicit and machine-readable. Pydantic provides field constraints, serialization, schema generation, and validation close to Python type hints.

## Tradeoff

Domain objects may eventually need to be distinct from transport contracts. Milestone 0 intentionally keeps them together because the models are small and stable. Separation will occur only when behavior or persistence requirements justify it.
