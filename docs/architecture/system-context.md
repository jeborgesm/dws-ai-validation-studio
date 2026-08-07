# System Context and Data Flow

## Context

DWS AI Validation Studio receives a dataset or model-related artifact, performs validation work, records findings, and produces evidence that a human reviewer can inspect. It is designed as a learning platform and portfolio reference, but follows enterprise engineering practices.

## Current Milestone 0 flow

```mermaid
flowchart LR
    U[User or API Client] -->|CSV upload| API[FastAPI API]
    API -->|Temporary local file| P[Dataset Profiler]
    P --> R[Rule Evaluation]
    R --> C[Pydantic Report Contract]
    C -->|JSON response| U
    API -->|Always delete temporary file| D[Cleanup]
```

## Target flow

```mermaid
flowchart TB
    U[Analyst / Reviewer] --> UI[Web or BI Experience]
    UI --> API[Validation API]
    API --> ORCH[Validation Orchestrator]
    ORCH --> DP[Data Profiling]
    ORCH --> ME[Model Evaluation]
    ORCH --> EX[Explainability]
    ORCH --> DR[Drift and Anomaly Analysis]
    ORCH --> GOV[Governance Artifact Generator]
    ORCH --> DB[(PostgreSQL Metadata and Audit Store)]
    ORCH --> S3[(S3 Evidence and Dataset Artifacts)]
    ORCH --> SM[AWS SageMaker]
    DB --> PBI[Power BI]
    GOV --> SP[SharePoint / GitHub Evidence]
    GOV --> PA[Power Automate Review Workflow]
```

## Trust boundaries

1. **Upload boundary:** Incoming content is untrusted until validated.
2. **Application boundary:** API and validation components execute with minimum required permissions.
3. **Persistence boundary:** Metadata and artifacts are stored separately because they have different security and retention needs.
4. **Cloud boundary:** AWS services require explicit identity, network, encryption, and logging controls.
5. **Human decision boundary:** Automated validation produces evidence and recommendations; it does not make final governance decisions.

## Current simplifications

Milestone 0 uses temporary local files because it is the smallest testable path. Persistence, authentication, malware scanning, object storage, and background jobs are intentionally deferred and documented as future controls rather than implied to exist.
