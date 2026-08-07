# ADR-0002: Use Python and FastAPI for Validation Services

- Status: Accepted
- Date: 2026-08-06

## Context

Python is the dominant practical language across data preparation, machine learning, model evaluation, explainability, and AWS SageMaker examples. The project also needs a typed, testable HTTP boundary.

## Decision

Use Python 3.12+ and FastAPI for the validation service.

## Why FastAPI

- Native type-hint integration.
- Pydantic request and response validation.
- Automatic OpenAPI documentation.
- Strong fit for small service boundaries.
- Straightforward testing through ASGI clients.

## Alternatives considered

### Flask

Mature and flexible, but requires more manual contract and schema work for this project's evidence goals.

### Django

Capable but heavier than needed for the initial API and validation core.

### .NET API only

The author already has strong .NET evidence. A .NET host may be added later, but using Python for the core directly demonstrates the missing capability and aligns with the ML ecosystem.

## Consequences

- Python quality practices must be learned and enforced, not treated as scripting shortcuts.
- Dependency and environment management become part of the project evidence.
- The system can later demonstrate polyglot integration with .NET or Blazor without hiding Python behind another stack.
