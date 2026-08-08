# ADR-0002 — Python and FastAPI for Analytics & AI Services

**Status:** Accepted

## Context

The Decision Support Platform combines traditional enterprise application development with analytics, AI-assisted capabilities, and evidence-driven decision support.

The platform's long-term roadmap includes:

- Data profiling and quality assessment
- Statistical analysis
- AI-assisted recommendations
- Model evaluation
- Explainability
- Enterprise integrations
- Operational reporting

No single technology stack is equally well suited to every capability.

## Decision

The platform adopts a polyglot architecture.

- **.NET** remains the primary platform for enterprise application development and long-term business services.
- **Python** is used where its mature ecosystem provides significant advantages for analytics, scientific computing, machine learning, and AI integration.
- **FastAPI** provides the HTTP interface for Python-based services through strongly typed APIs.

## Rationale

### Use the Right Tool for the Right Responsibility

Python provides an extensive ecosystem for:

- data analysis
- statistics
- machine learning
- AI frameworks
- scientific computing
- model evaluation
- data quality analysis

These capabilities complement the enterprise strengths of .NET rather than replacing them.

### Strong API Contracts

FastAPI was selected because it offers:

- high performance
- automatic OpenAPI documentation
- native async support
- excellent integration with Pydantic
- first-class type hints
- consistent REST APIs

These characteristics simplify integration between platform components.

### Enterprise Integration

The architecture is intentionally designed to integrate with technologies such as:

- PostgreSQL
- AWS services (including SageMaker and Amazon S3)
- Power BI
- Power Automate
- SharePoint Online
- ServiceNow
- GitHub Actions

Python serves as one component within this broader enterprise architecture.

### Maintainability

Separating analytics and AI-oriented capabilities into Python services allows the platform to evolve those capabilities independently while preserving stable business interfaces.

## Consequences

### Positive

- Access to mature analytics and AI ecosystems
- Strongly typed APIs
- Excellent interoperability
- Clear technology boundaries
- Easier future expansion

### Trade-offs

- Multiple technology stacks require consistent engineering standards.
- Teams must maintain expertise across both .NET and Python.
- Cross-language integration requires disciplined API contracts.

These trade-offs are justified by the capabilities gained.

## Alternatives Considered

### .NET Only

Rejected because it would unnecessarily limit access to mature analytics, scientific computing, and AI libraries.

### Python Only

Rejected because the platform benefits from the enterprise application strengths, ecosystem, and long-term maintainability provided by .NET.

## Relationship to Other ADRs

- ADR-0001 defines the overall modular architecture.
- ADR-0003 standardizes data contracts between services.
- ADR-0004 defines data boundaries.
- ADR-0005 establishes the evidence-first architecture.
