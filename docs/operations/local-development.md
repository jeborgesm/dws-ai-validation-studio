# Local Development

## Purpose

This document describes how to configure a local development environment for the Decision Support Platform.

The objective is to provide a reproducible environment that supports feature development, automated testing, architecture validation, and experimentation while remaining consistent with the platform's long-term enterprise architecture.

The local environment intentionally mirrors production concepts where practical without introducing unnecessary operational complexity.

---

# Development Principles

Local development should be:

- Reproducible
- Easy to configure
- Consistent across contributors
- Automated whenever practical
- Representative of the production architecture

Developers should be able to clone the repository, configure a small number of local settings, and begin contributing without requiring enterprise infrastructure.

---

# Platform Components

## Python Services

Python provides the analytics and AI-oriented capabilities of the platform, including:

- Data profiling
- Analytics
- AI-assisted recommendations
- Decision support services
- API endpoints

FastAPI provides the service interface for these capabilities.

## PostgreSQL

PostgreSQL serves as the platform's operational database.

Future milestones will expand its responsibilities to include:

- Operational persistence
- Evidence storage
- Workflow state
- Reporting data
- Configuration

## GitHub Actions

GitHub Actions execute the automated quality pipeline:

- Dependency installation
- Ruff linting
- mypy type checking
- pytest execution
- Coverage reporting

The local workflow should closely match automated validation.

## Future Enterprise Integrations

The architecture is intentionally designed to support future integration with:

- AWS
- Power BI
- Power Automate
- SharePoint Online
- Enterprise identity providers

These capabilities are introduced incrementally as the platform evolves.

---

# Repository Organization

```
docs/
    Product
    Architecture
    Governance
    Quality
    Operations

src/
    Platform implementation

tests/
    Automated tests

data/
    Synthetic sample datasets

.github/
    Repository automation
```

Refer to the Repository Structure diagram for a complete overview.

---

# Typical Development Workflow

```
Clone Repository
        │
        ▼
Create Feature Branch
        │
        ▼
Implement Capability
        │
        ▼
Run Ruff
        │
        ▼
Run mypy
        │
        ▼
Run pytest
        │
        ▼
Review Results
        │
        ▼
Commit Changes
        │
        ▼
Open Pull Request
```

---

# Local Quality Validation

Run the following before submitting changes:

- Ruff
- mypy
- pytest
- Coverage reporting

Automated validation should confirm that new capabilities satisfy the project's engineering standards.

---

# Configuration

Environment-specific configuration should remain outside the source code.

Examples include:

- Environment variables
- Local configuration files
- API credentials
- Cloud credentials
- Database connection strings

---

# Relationship to Other Documents

- Product Vision
- Business Process
- Architecture Documentation
- Testing Strategy
- Definition of Done
- Architecture Decision Records

---

# Summary

The local development environment is designed to make it easy to contribute to the Decision Support Platform while preserving the engineering standards, architectural principles, and quality expectations required for an enterprise-grade system.
