# ADR-0004: Use Only Public, Synthetic, or Explicitly Authorized Data

- Status: Accepted
- Date: 2026-08-06

## Context

The project is public and inspired by professional skill requirements. Using proprietary, customer, or personally sensitive data would create unacceptable confidentiality, privacy, and reputational risk.

## Decision

Only public, synthetic, or explicitly authorized data may be committed or processed in demonstrations.

## Enforcement

- Sample data must be synthetic or have a documented public source and license.
- Secrets and private datasets are ignored by source control.
- Documentation must not reproduce confidential statements of work or internal procedures.
- Demonstration model outputs must not be presented as real regulatory decisions.

## Consequences

Synthetic data may be less realistic, so limitations must be documented. This is preferable to creating legal or ethical risk.
