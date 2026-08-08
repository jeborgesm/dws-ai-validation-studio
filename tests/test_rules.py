from dws_ai_validation.core.models import ColumnProfile
from dws_ai_validation.core.rules import DatasetEvidence, DuplicateRowsRule, MissingValuesRule


def test_missing_values_rule_preserves_existing_finding_contract() -> None:
    evidence = DatasetEvidence(
        row_count=3,
        duplicate_row_count=0,
        columns=[
            ColumnProfile(
                name="income",
                data_type="float64",
                missing_count=2,
                missing_percentage=66.67,
                unique_count=1,
            )
        ],
    )

    finding = MissingValuesRule(max_missing_percentage=20.0).evaluate(evidence)[0]

    assert finding.rule == "missing_values:income"
    assert finding.passed is False
    assert finding.observed == 66.67
    assert finding.threshold == 20.0
    assert finding.message == "Column 'income' exceeds the missing-value threshold."


def test_duplicate_rows_rule_preserves_existing_finding_contract() -> None:
    evidence = DatasetEvidence(row_count=3, duplicate_row_count=1, columns=[])

    finding = DuplicateRowsRule(max_duplicate_percentage=5.0).evaluate(evidence)[0]

    assert finding.rule == "duplicate_rows"
    assert finding.passed is False
    assert finding.observed == 33.33
    assert finding.threshold == 5.0
    assert finding.message == "Duplicate rows exceed the configured threshold."
