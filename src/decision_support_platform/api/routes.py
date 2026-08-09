from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from decision_support_platform.core.models import DatasetProfile
from decision_support_platform.core.profiler import profile_csv

router = APIRouter()


@router.post(
    "/datasets/profile",
    response_model=DatasetProfile,
    tags=["dataset validation"],
)
async def profile_dataset(file: Annotated[UploadFile, File()],) -> DatasetProfile:
    file_name = file.filename or "uploaded.csv"
    if not file_name.lower().endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Milestone 0 accepts CSV files only.",
        )

    content = await file.read()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file is empty.",
        )

    temporary_path: Path | None = None
    try:
        with NamedTemporaryFile(suffix=".csv", delete=False) as temporary_file:
            temporary_file.write(content)
            temporary_path = Path(temporary_file.name)
        return profile_csv(temporary_path, original_file_name=file_name)
    except (UnicodeDecodeError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"The CSV could not be parsed: {exc}",
        ) from exc
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
