from pydantic import BaseModel, Field


class ColumnProfile(BaseModel):
    name: str
    data_type: str
    missing_count: int = Field(ge=0)
    missing_percentage: float = Field(ge=0, le=100)
    unique_count: int = Field(ge=0)


class ValidationFinding(BaseModel):
    rule: str
    passed: bool
    observed: float
    threshold: float
    message: str


class DatasetProfile(BaseModel):
    file_name: str
    row_count: int = Field(ge=0)
    column_count: int = Field(ge=0)
    duplicate_row_count: int = Field(ge=0)
    columns: list[ColumnProfile]
    findings: list[ValidationFinding]
    overall_passed: bool
