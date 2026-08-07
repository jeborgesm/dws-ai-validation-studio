# ADR-0001: Start as a Modular Monolith

- Status: Accepted
- Date: 2026-08-06

## Context

The target platform spans data profiling, model evaluation, governance, monitoring, cloud services, and enterprise integrations. Splitting these concerns into services immediately would create deployment, networking, observability, versioning, and local-development overhead before the domain boundaries are understood.

## Decision

Start with a modular monolith organized by clear responsibilities. Preserve boundaries in code and contracts so components may be extracted later if operational needs justify it.

## Alternatives considered

### Microservices from day one

Rejected because it would optimize for hypothetical scale while slowing learning and increasing failure modes.

### Single-script notebook

Rejected because notebooks are useful for exploration but weak as the sole foundation for APIs, testing, versioned contracts, and maintainable enterprise behavior.

## Consequences

### Positive

- Fast local setup.
- Simple debugging and testing.
- Fewer distributed-system concerns.
- Domain boundaries can evolve from evidence.

### Negative

- Requires discipline to prevent accidental coupling.
- Independent scaling is deferred.
- Future extraction may require refactoring.

## Revisit when

A component has independently measurable scaling, release cadence, security isolation, or ownership requirements.
