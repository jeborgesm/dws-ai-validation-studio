# Threat Model

## Scope

This document identifies material risks for the public learning implementation. It is not a formal certification or complete production security assessment.

## Assets

- Uploaded datasets.
- Model artifacts and validation reports.
- Governance records and approvals.
- Credentials for cloud and enterprise integrations.
- Source code and CI/CD pipeline integrity.
- Audit history.

## Threat actors

- Accidental user misuse.
- Malicious anonymous uploaders in a future hosted environment.
- Compromised dependencies.
- Unauthorized repository or cloud access.
- Insider misuse in a hypothetical enterprise deployment.

## Key threats and controls

### Sensitive data disclosure

**Risk:** Confidential or personal data is uploaded or committed.

**Controls:** Public/synthetic-data policy, source-control ignores, documentation warnings, future data-classification checks, retention limits, and access controls.

### Malicious file upload

**Risk:** Oversized, malformed, or crafted files exhaust resources or exploit parsers.

**Current controls:** CSV extension check, empty-file rejection, temporary-file cleanup, controlled exception mapping.

**Planned controls:** Content sniffing, file-size limits, streaming, parser limits, isolated workers, malware scanning, quotas, and timeouts.

### Formula or content injection

**Risk:** CSV cells later rendered in spreadsheets or HTML contain executable formulas or scripts.

**Planned controls:** Output encoding, spreadsheet formula neutralization, content-security policy, and safe templating.

### Dependency compromise

**Risk:** A malicious or vulnerable package enters the build.

**Controls:** Bounded dependency ranges, automated dependency review planned, lock files planned, minimal dependency set, CI scanning planned.

### Unauthorized cloud actions

**Risk:** Broad AWS permissions permit data exposure or resource abuse.

**Planned controls:** Least-privilege IAM, separate environments, short-lived credentials, encryption, private networking where justified, CloudTrail, budget alerts, and explicit teardown procedures.

### Misleading validation claims

**Risk:** A passing report is interpreted as proof that a model is safe or compliant.

**Controls:** Purpose-bound reports, limitations, human approval boundary, recorded thresholds, versioned evidence, and responsible-use labeling.

### Audit tampering

**Risk:** Findings or approvals are altered without traceability.

**Planned controls:** Append-oriented audit events, immutable artifact hashes, identity attribution, timestamps, and restricted update paths.

## Residual risk

Milestone 0 is suitable for local learning with safe datasets. It is not suitable for untrusted public hosting or regulated production data.
