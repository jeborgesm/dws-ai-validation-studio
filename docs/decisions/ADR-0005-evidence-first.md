# ADR-0005: Evidence-First Development

- Status: Accepted
- Date: 2026-08-06

## Decision

Every milestone must produce inspectable evidence, not only code. Evidence may include tests, reports, schemas, model cards, diagrams, ADRs, sample outputs, and reproducible commands.

## Rationale

The project exists partly to demonstrate capability. A reviewer should not need to accept unsupported claims such as "understands model validation." The repository should show exactly how validation was defined, executed, interpreted, and limited.

## Required evidence for behavior changes

- Updated or new automated tests.
- Updated user or technical documentation.
- A recorded decision when architecture or governance changes materially.
- Sample output when it improves reviewability.
- Explicit limitations and deferred controls.
