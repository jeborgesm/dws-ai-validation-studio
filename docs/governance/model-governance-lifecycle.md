# Model Governance Lifecycle

## Proposed states

1. **Draft** — Purpose and owner identified; evidence incomplete.
2. **In development** — Data and model are changing; not approved for use.
3. **Validation pending** — Version is frozen for independent evaluation.
4. **Validated with conditions** — Criteria met subject to documented restrictions.
5. **Approved** — Authorized human reviewer accepts the evidence for a defined use.
6. **Monitoring** — Deployed or simulated operation is observed.
7. **Review required** — Drift, incident, material change, or review date triggers reassessment.
8. **Retired** — Model is no longer authorized for use.

## Required records

- Model identifier and version.
- Business purpose and prohibited uses.
- Owner and reviewers.
- Training and evaluation dataset references.
- Source-code version and environment.
- Metrics, thresholds, and test results.
- Explainability and fairness evidence where applicable.
- Limitations and known failure modes.
- Approval decision and conditions.
- Monitoring plan and review date.
- Incidents, changes, and retirement rationale.

## Separation of duties

The project will demonstrate a distinction between model developer, validator, and approver even when one person performs all roles in the learning environment. The role distinction matters because it exposes conflicts and clarifies which evidence each responsibility requires.
