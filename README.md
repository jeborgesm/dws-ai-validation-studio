# Decision Support Platform

> **Building trustworthy operational decision systems through business rules, analytics, AI, governance, and evidence.**

[![CI](https://github.com/jeborgesm/decision-support-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/jeborgesm/decision-support-platform/actions/workflows/ci.yml)

Decision Support Platform is an enterprise reference implementation that demonstrates how important operational decisions can be supported by deterministic business rules, analytics, AI-assisted recommendations, human review, governance, and traceable evidence.

The platform is being developed around realistic decision scenarios such as lending and customer risk assessment, but the architecture is intentionally reusable across domains including insurance, fraud operations, compliance, healthcare operations, supply chain, and other decision-intensive environments.

## The business problem

Organizations make high-impact operational decisions every day.

Examples include:

- approving or declining a loan,
- reviewing an insurance claim,
- investigating suspected fraud,
- evaluating customer or transaction risk,
- performing a compliance review,
- qualifying a supplier,
- or deciding whether a case requires additional human review.

These decisions increasingly combine policy, analytics, statistical models, and AI-assisted recommendations.

The difficult part is not simply producing a score or recommendation. The organization must also be able to answer:

- What information was used?
- Which business rules were applied?
- What did the analytics or model contribute?
- Did AI influence the recommendation?
- Why was the recommendation made?
- Was a human required to review it?
- What evidence supports the final decision?
- Can the decision be reconstructed later?
- Is the decision process continuing to perform as expected?

The value of this platform is to make that decision process **transparent, explainable, governable, measurable, and auditable**.

## Executive view

![Decision Support Platform executive overview](docs/architecture/diagrams/01-executive-overview.svg)

The platform treats AI as one capability inside a broader decision process. AI does not automatically become the final authority. Business rules, analytics, evidence, governance controls, and human oversight remain explicit parts of the architecture.

At a high level, the intended lifecycle is:

```text
Operational case or request
        |
        v
Business rules and policy checks
        |
        v
Analytics, scoring, and model evaluation
        |
        v
AI-assisted recommendation when appropriate
        |
        v
Evidence and explanation
        |
        v
Human review when required
        |
        v
Operational decision
        |
        v
Audit trail, monitoring, and improvement
```

## Why this platform exists

This repository demonstrates how an enterprise decision support system can be engineered from the business problem outward.

The goal is not to collect technologies for their own sake. Each capability should contribute to one or more of these outcomes:

- **Better decisions** — combine policy, analytics, models, and human judgment deliberately.
- **Lower operational risk** — identify questionable inputs, recommendations, or outcomes before they cause larger problems.
- **Explainability** — preserve the reasons, rules, measurements, and model information behind a recommendation or decision.
- **Traceability** — reconstruct what happened, when it happened, what version was used, and who approved it.
- **Governance** — apply review, approval, separation-of-duties, retention, and responsible-use controls.
- **Continuous improvement** — monitor outcomes and use evidence to improve rules, models, and workflows over time.

## Demonstration scenario

The initial implementation uses customer-risk and lending-style data because it provides an understandable example of a high-impact operational decision.

A simplified scenario is:

1. A customer or case enters the decision process.
2. The platform validates the available information.
3. Deterministic policies and business rules are applied.
4. Analytics or statistical models calculate measurements or risk scores.
5. AI may provide an additional recommendation, summary, classification, similarity assessment, or explanation.
6. The platform assembles evidence from the inputs, rules, model results, and AI outputs.
7. A human reviewer can approve, decline, refer, or request additional information when required.
8. The decision and supporting evidence are retained for traceability.
9. Outcomes are monitored so rules and models can be evaluated and improved.

The lending scenario is a reference scenario, not the architectural boundary of the platform.

## Current implementation

The current codebase represents the first working vertical slice of the platform.

Milestone 0 currently demonstrates:

- a FastAPI application and REST endpoint,
- CSV dataset upload,
- dataset profiling with pandas,
- column-level missing-value measurements,
- duplicate-row measurements,
- transparent threshold-based validation findings,
- typed Pydantic request and response contracts,
- deterministic validation behavior,
- temporary-file cleanup,
- unit and API tests,
- Ruff linting,
- strict mypy type checking,
- pytest with coverage reporting,
- GitHub Actions continuous integration,
- architecture decision records,
- security and responsible-use documentation,
- validation methodology,
- threat modeling,
- and documented engineering justification.

This is intentionally a small implementation. It establishes the contracts, quality practices, documentation discipline, and architectural boundaries that later decision-support capabilities will build upon.

## Current engineering flow

```text
API client
    |
    v
FastAPI transport layer
    |
    v
Dataset profiler
    |
    +--> Data quality measurements
    |
    +--> Threshold evaluations
    |
    v
Typed validation findings
    |
    v
Pydantic validation report
```

The current implementation does **not** yet make production lending decisions, host an AI model, or provide enterprise workflow automation. Those capabilities belong to the planned platform evolution described below.

## Enterprise architecture direction

The target platform expands the current vertical slice into a modular decision-support architecture.

### Decision capabilities

- **Business Rule Engine** — deterministic policy and eligibility checks.
- **Analytics Engine** — scoring, statistical analysis, performance metrics, and risk measurements.
- **AI / Model Services** — AI-assisted recommendations, classification, similarity, summarization, extraction, and explanation.
- **Evidence Service** — capture inputs, rules, scores, model outputs, explanations, artifacts, and decision context.
- **Workflow & Decision Service** — coordinate review, approval, referral, and role-based actions.
- **Monitoring** — measure outcomes, model behavior, decision quality, drift, failures, and operational trends.

### Enterprise data and platform capabilities

- **PostgreSQL** — operational data, decision records, model metadata, findings, approvals, and history.
- **Object / evidence storage** — datasets, generated reports, model artifacts, and supporting evidence.
- **Audit logging** — immutable or controlled records of access, changes, decisions, and approvals.
- **Authentication and authorization** — role-based access and separation of duties.
- **Observability** — logs, metrics, traces, dashboards, and alerting.
- **CI/CD** — automated quality checks, tests, builds, releases, and deployment controls.
- **Security** — least privilege, secret management, encryption, dependency monitoring, and secure configuration.

## Planned enterprise technology integration

The technical roadmap intentionally includes enterprise tools and services that demonstrate how the platform can operate across the full decision lifecycle.

| Technology / capability | Planned role in the platform |
|---|---|
| **Python** | Decision analytics, data processing, AI/ML integration, orchestration, and services |
| **FastAPI** | Secure APIs for submitting cases, evaluating information, and querying results |
| **PostgreSQL** | Operational records, decision history, rules, model metadata, evidence metadata, and audit relationships |
| **AWS** | Cloud hosting and managed infrastructure |
| **Amazon SageMaker** | Model training, evaluation, registration, deployment, monitoring, and model lifecycle demonstrations |
| **Amazon S3** | Dataset, evidence, report, and model-artifact storage |
| **Power BI** | Executive, operational, risk, validation, and monitoring dashboards using SQL and DAX |
| **Power Automate** | Approval workflows and AI-assisted summarization, extraction, classification, and similarity scenarios |
| **SharePoint Online** | Evidence retention, controlled documentation, review artifacts, and collaboration |
| **ServiceNow** | Operational issue, incident, change, or review workflow integration |
| **JIRA** | Engineering and governance work tracking |
| **GitHub** | Source control, pull requests, automation, security scanning, and CI/CD |
| **DBeaver** | Database inspection and operational development workflows |
| **AI agents / assistants** | Help reviewers interpret evidence, identify gaps, summarize findings, recommend follow-up actions, and prepare reports |
| **Ruff** | Python linting and code-quality enforcement |
| **mypy** | Static verification of Python type contracts |
| **pytest / coverage** | Behavioral verification and evidence that important execution paths are tested |

These integrations are part of the planned reference implementation. Their purpose is to support the decision process, not to exist as isolated technology demonstrations.

## Engineering principles

The platform follows a small set of principles that guide both the code and the documentation:

- **Business purpose first.** Technology should support a meaningful operational capability.
- **Evidence before opinion.** Important claims should be supported by working code, automated tests, measurements, or reproducible artifacts.
- **Explain decisions.** A recommendation or decision should be understandable after the fact.
- **Human oversight where appropriate.** AI and models support decision making; they do not automatically replace accountable human judgment.
- **Make governance visible.** Review, approval, limitations, ownership, and evidence retention should be explicit.
- **Incremental architecture.** Start with a working vertical slice and add complexity when a concrete capability requires it.
- **Separate current state from future state.** Planned architecture is documented as planned architecture, not presented as already implemented.
- **Documentation is part of the product.** Architecture, decisions, limitations, operations, and governance evolve with the implementation.

## Quality gates

The project uses multiple automated checks because each answers a different engineering question.

```powershell
python -m ruff check .
python -m mypy src
python -m pytest
```

- **Ruff** checks whether the Python code follows the project's quality and consistency rules.
- **mypy** checks whether the type contracts remain internally consistent before runtime.
- **pytest** runs the software behavior under automated tests.
- **Coverage reporting** shows how much of the implementation the automated tests actually exercised.

The same checks run in GitHub Actions so that repository quality does not depend only on a developer remembering to run them manually.

## Quick start

The current implementation requires Python 3.12 or later.

Install the project and development dependencies:

```powershell
python -m pip install -e ".[dev]"
```

Run the quality checks:

```powershell
python -m ruff check .
python -m mypy src
python -m pytest
```

For local API startup and other development details, see the [local development guide](docs/operations/local-development.md).

## Architecture and documentation

The repository treats documentation as a first-class engineering artifact.

Start with:

- [Documentation map](docs/README.md)
- [Project charter](docs/project-management/project-charter.md)
- [Foundation architecture](docs/architecture/foundation.md)
- [System context and data flow](docs/architecture/system-context.md)
- [Component responsibilities](docs/architecture/component-responsibilities.md)
- [Validation methodology](docs/quality/validation-methodology.md)
- [Testing strategy](docs/quality/testing-strategy.md)
- [Responsible use](docs/governance/responsible-use.md)
- [Threat model](docs/governance/threat-model.md)
- [Model governance lifecycle](docs/governance/model-governance-lifecycle.md)
- [Architecture decisions](docs/decisions/)
- [Engineering justification guide](docs/guides/engineering-justification-guide.md)
- [Python reference for experienced .NET engineers](docs/guides/python-for-dotnet-engineers.md)
- [Glossary](docs/glossary.md)

## Visual architecture

The diagram set provides multiple levels of detail for different audiences.

- [How to read this project](docs/architecture/diagrams/00-how-to-read-this-project.svg)
- [Executive overview](docs/architecture/diagrams/01-executive-overview.svg)
- [Milestone 0 system context](docs/architecture/diagrams/02-milestone-0-system-context.svg)
- [Milestone 0 component responsibilities](docs/architecture/diagrams/03-milestone-0-component-responsibilities.svg)
- [Validation lifecycle](docs/architecture/diagrams/04-validation-lifecycle.svg)
- [Repository structure](docs/architecture/diagrams/05-repository-structure.svg)
- [Target platform architecture](docs/architecture/diagrams/06-target-platform-architecture.svg)
- [Future AI assistance roadmap](docs/architecture/diagrams/07-future-ai-assistance-roadmap.svg)

The remaining diagrams will be progressively aligned with the Decision Support Platform product narrative during the current repositioning initiative.

## Roadmap

The technical milestones are organized around business capabilities.

### Foundation

Establish the API, typed contracts, deterministic behavior, testing, CI/CD, architecture records, governance boundaries, and safe data practices.

### Decision evaluation

Expand transparent rule evaluation and reusable decision policies.

### Analytics and risk assessment

Add statistical analysis, risk scoring, performance measurements, and richer data-quality evidence.

### AI-assisted recommendations

Integrate model and AI services for recommendation, classification, extraction, summarization, similarity, and explanation scenarios.

### Evidence platform

Persist decision context, model information, findings, explanations, generated artifacts, and approval history.

### Human workflow and governance

Introduce accountable review, approval, separation of duties, exception handling, and governance evidence.

### Enterprise integrations

Integrate PostgreSQL, AWS, SageMaker, S3, Power BI, Power Automate, SharePoint Online, ServiceNow, JIRA, GitHub, and supporting operational tools.

### Operational intelligence

Monitor decision quality, model behavior, drift, exceptions, workflow performance, and business outcomes.

## Data boundary

Only synthetic, public, or explicitly approved data belongs in this repository.

Do not commit:

- credentials or secrets,
- personal information,
- production datasets,
- customer records,
- proprietary organizational data,
- confidential infrastructure information,
- or regulated data.

The public repository is designed to demonstrate architecture and engineering practice without exposing protected organizational information.

## Status

The project is actively evolving from its Milestone 0 validation foundation into the broader Decision Support Platform described here.

The business purpose is stable: **help organizations engineer trustworthy operational decision systems.**

The implementation will grow incrementally, with each technical capability tied to a clear role in the decision lifecycle.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow, pull-request expectations, testing requirements, and contribution guidance.

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting and public-repository security expectations.

## License

Licensed under the [MIT License](LICENSE).
