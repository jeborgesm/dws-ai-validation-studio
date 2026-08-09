from pathlib import Path

import pandas as pd

from decision_support_platform.core.models import ColumnProfile, DatasetProfile, ValidationFinding

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
    duplicate_percentage = (duplicate_count / row_count * 100.0) if row_count else 0.0

    columns: list[ColumnProfile] = []
    findings: list[ValidationFinding] = []

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
        passed = missing_percentage <= max_missing_percentage
        findings.append(
            ValidationFinding(
                rule=f"missing_values:{column_name}",
                passed=passed,
                observed=round(missing_percentage, 2),
                threshold=max_missing_percentage,
                message=(
                    f"Column '{column_name}' is within the missing-value threshold."
                    if passed
                    else f"Column '{column_name}' exceeds the missing-value threshold."
                ),
            )
        )

    duplicate_passed = duplicate_percentage <= max_duplicate_percentage
    findings.append(
        ValidationFinding(
            rule="duplicate_rows",
            passed=duplicate_passed,
            observed=round(duplicate_percentage, 2),
            threshold=max_duplicate_percentage,
            message=(
                "Duplicate rows are within the configured threshold."
                if duplicate_passed
                else "Duplicate rows exceed the configured threshold."
            ),
        )
    )

    return DatasetProfile(
        file_name=original_file_name,
        row_count=row_count,
        column_count=len(frame.columns),
        duplicate_row_count=duplicate_count,
        columns=columns,
        findings=findings,
        overall_passed=all(finding.passed for finding in findings),
    )
