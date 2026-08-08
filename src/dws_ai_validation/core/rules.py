from abc import ABC, abstractmethod
from dataclasses import dataclass

from dws_ai_validation.core.models import ColumnProfile, ValidationFinding


@dataclass(frozen=True)
class DatasetEvidence:
    """Measured dataset facts consumed by validation rules."""

    row_count: int
    duplicate_row_count: int
    columns: list[ColumnProfile]


class ValidationRule(ABC):
    """Base contract for deterministic dataset validation rules."""

    @abstractmethod
    def evaluate(self, evidence: DatasetEvidence) -> list[ValidationFinding]:
        """Evaluate measured dataset evidence and return one or more findings."""


@dataclass(frozen=True)
class MissingValuesRule(ValidationRule):
    """Fail columns whose missing-value percentage exceeds the configured threshold."""

    max_missing_percentage: float

    def evaluate(self, evidence: DatasetEvidence) -> list[ValidationFinding]:
        findings: list[ValidationFinding] = []

        for column in evidence.columns:
            missing_percentage = (
                column.missing_count / evidence.row_count * 100.0
                if evidence.row_count
                else 0.0
            )
            passed = missing_percentage <= self.max_missing_percentage
            findings.append(
                ValidationFinding(
                    rule=f"missing_values:{column.name}",
                    passed=passed,
                    observed=round(missing_percentage, 2),
                    threshold=self.max_missing_percentage,
                    message=(
                        f"Column '{column.name}' is within the missing-value threshold."
                        if passed
                        else f"Column '{column.name}' exceeds the missing-value threshold."
                    ),
                )
            )

        return findings


@dataclass(frozen=True)
class DuplicateRowsRule(ValidationRule):
    """Fail datasets whose duplicate-row percentage exceeds the configured threshold."""

    max_duplicate_percentage: float

    def evaluate(self, evidence: DatasetEvidence) -> list[ValidationFinding]:
        duplicate_percentage = (
            evidence.duplicate_row_count / evidence.row_count * 100.0
            if evidence.row_count
            else 0.0
        )
        passed = duplicate_percentage <= self.max_duplicate_percentage

        return [
            ValidationFinding(
                rule="duplicate_rows",
                passed=passed,
                observed=round(duplicate_percentage, 2),
                threshold=self.max_duplicate_percentage,
                message=(
                    "Duplicate rows are within the configured threshold."
                    if passed
                    else "Duplicate rows exceed the configured threshold."
                ),
            )
        ]
