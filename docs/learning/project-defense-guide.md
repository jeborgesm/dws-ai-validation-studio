# Project Defense Guide

This guide prepares the author to explain not only what was built, but why each decision was made and where the system is intentionally incomplete.

## Thirty-second explanation

DWS AI Validation Studio is an enterprise-style Python platform that validates datasets and machine-learning models, produces model-governance evidence, and will integrate with AWS SageMaker, PostgreSQL, Power BI, Power Automate, and SharePoint. It is built publicly with synthetic data so every capability is supported by inspectable code, tests, architecture decisions, and documentation.

## Why Python?

Python provides direct access to the data and ML ecosystem used by pandas, scikit-learn, SHAP, and SageMaker. Using Python in the core demonstrates the missing skill rather than hiding it behind an already familiar .NET layer.

## Why FastAPI?

FastAPI uses Python type hints and Pydantic to produce validated contracts and OpenAPI documentation with little ceremony. It allows the project to demonstrate disciplined service development rather than isolated scripts.

## Why not begin with SageMaker?

Cloud tooling should not obscure the underlying validation concepts. The project first establishes deterministic local behavior, tests, and evidence. SageMaker is introduced after the data and model lifecycle is understood, making the cloud implementation easier to explain and less dependent on vendor-specific terminology.

## Why a modular monolith?

The domain boundaries are still being discovered. A modular monolith minimizes distributed complexity while preserving separations that can later support extraction if scale, security, or release independence justify it.

## Why are the Milestone 0 thresholds simplistic?

They are intentionally transparent demonstration defaults. The repository records observed values and thresholds and explicitly states that real thresholds depend on business purpose, data semantics, and risk. A later milestone will make plans configurable and versioned.

## What makes this model validation rather than only data profiling?

Milestone 0 establishes the data-validation foundation. Later milestones add holdout evaluation, metrics, robustness, explainability, fairness, reproducibility, drift, governance states, and monitoring. The roadmap and data structures are designed around the complete lifecycle.

## What would prevent production use today?

No authentication, authorization, persistent audit store, file-size limit, malware scanning, content sniffing, object storage, secret management, cloud controls, or formal validation policy exists yet. The repository labels these gaps rather than implying production readiness.

## How does prior enterprise experience transfer?

The project applies established engineering skills—architecture, API design, SQL, testing, requirements analysis, auditability, workflow, security thinking, and regulatory documentation—to the Python and AI/ML ecosystem. The learning challenge is the ML-specific lifecycle and tooling, not learning software engineering from zero.

## Hard questions to expect

### Is a model card proof of compliance?

No. It is a structured communication artifact. Its quality depends on accurate evidence, appropriate review, and the governing policy.

### Does explainability prove fairness or correctness?

No. Explainability can help investigate behavior, but it can be unstable, approximate, and easy to misinterpret. It is one part of validation evidence.

### Can drift be detected without labels?

Input or prediction distribution drift can be detected without labels, but actual performance degradation usually requires delayed ground truth or useful proxies.

### Why is accuracy not enough?

Accuracy can hide class imbalance and unequal error costs. Metrics must match the decision context, such as precision, recall, F1, ROC-AUC, PR-AUC, calibration, and subgroup performance.

### What is the difference between verification and validation?

Verification asks whether the system was built according to specification. Validation asks whether it is fit for its intended purpose and operating context.
