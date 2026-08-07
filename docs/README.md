# Documentation Map

This directory is the authoritative technical and governance record for DWS AI Validation Studio. The project deliberately treats documentation as a first-class engineering deliverable because AI/ML validation work must be explainable, reproducible, reviewable, and defensible.

## Start here

1. [Project charter](project-management/project-charter.md)
2. [Foundation architecture](architecture/foundation.md)
3. [System context and data flow](architecture/system-context.md)
4. [Validation methodology](quality/validation-methodology.md)
5. [Responsible use and data boundary](governance/responsible-use.md)
6. [Threat model](governance/threat-model.md)
7. [Learning and defense guide](learning/project-defense-guide.md)

## Architecture decision records

Architecture Decision Records (ADRs) document not only what was chosen, but why, which alternatives were considered, and what tradeoffs were accepted.

- [ADR-0001: Modular monolith first](decisions/ADR-0001-modular-monolith.md)
- [ADR-0002: Python and FastAPI](decisions/ADR-0002-python-fastapi.md)
- [ADR-0003: Typed Pydantic contracts](decisions/ADR-0003-pydantic-contracts.md)
- [ADR-0004: Synthetic and public data only](decisions/ADR-0004-data-boundary.md)
- [ADR-0005: Evidence-first development](decisions/ADR-0005-evidence-first.md)

## Quality and operations

- [Testing strategy](quality/testing-strategy.md)
- [Definition of done](quality/definition-of-done.md)
- [Local development](operations/local-development.md)
- [Troubleshooting](operations/troubleshooting.md)
- [Glossary](glossary.md)
