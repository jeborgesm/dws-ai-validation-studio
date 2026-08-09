from pathlib import Path

from decision_support_platform.core.profiler import profile_csv


def test_profile_csv_identifies_missing_values_and_duplicates(tmp_path: Path) -> None:
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text(
        "customer_id,income,risk_flag\n"
        "1,50000,0\n"
        "2,,1\n"
        "2,,1\n",
        encoding="utf-8",
    )

    result = profile_csv(csv_path, original_file_name="sample.csv")

    assert result.row_count == 3
    assert result.column_count == 3
    assert result.duplicate_row_count == 1
    assert result.overall_passed is False
    income = next(column for column in result.columns if column.name == "income")
    assert income.missing_count == 2
