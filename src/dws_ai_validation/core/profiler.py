from pathlib import Path

import pandas as pd

from dws_ai_validation.core.models import ColumnProfile, DatasetProfile, ValidationFinding
from dws_ai_validation.core.rules import (
    DatasetEvidence,
    DuplicateRowsRule,
    MissingValuesRule,
    ValidationRule,
)

DEFAULT_MAX_MISSING_PERCENTAGE = 20.0
DEFAULT_MAX_DUPLICATE_PERCENTAGE = 5.0


def profile_csv(
    path: Path,
    *,
    original_file_name: str,
    max_missing_percentage: float = DEFAULT_MAX_MISSING_PERCENTAGE,
    max_duplicate_percentage: float = DEFAULT_MAX_DUPLICATE_PERCENTAGE,
) -> DatasetProfile:
    frame = pd.read_csv(path)
    row_count = len(frame)
    duplicate_count = int(frame.duplicated().sum())

    columns: list[ColumnProfile] = []
    for column_name in frame.columns:
        series = frame[column_name]
        missing_count = int(series.isna().sum())
        missing_percentage = (missing_count / row_count * 100.0) if row_count else 0.0
        columns.append(
            ColumnProfile(
                name=str(column_name),
                data_type=str(series.dtype),
                missing_count=missing_count,
                missing_percentage=round(missing_percentage, 2),
                unique_count=int(series.nunique(dropna=True)),
            )
        )

    evidence = DatasetEvidence(
        row_count=row_count,
        duplicate_row_count=duplicate_count,
        columns=columns,
    )
    rules: list[ValidationRule] = [
        MissingValuesRule(max_missing_percentage=max_missing_percentage),
        DuplicateRowsRule(max_duplicate_percentage=max_duplicate_percentage),
    ]

    findings: list[ValidationFinding] = []
    for rule in rules:
        findings.extend(rule.evaluate(evidence))

    return DatasetProfile(
        file_name=original_file_name,
        row_count=row_count,
        column_count=len(frame.columns),
        duplicate_row_count=duplicate_count,
        columns=columns,
        findings=findings,
        overall_passed=all(finding.passed for finding in findings),
    )
