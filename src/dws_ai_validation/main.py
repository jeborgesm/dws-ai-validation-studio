from fastapi import FastAPI

from dws_ai_validation.api.routes import router

app = FastAPI(
    title="Decision Support Platform",
    summary="Dataset, model, and governance validation services.",
    version="0.1.0",
)
app.include_router(router, prefix="/api/v1")


@app.get("/health", tags=["operations"])
def health() -> dict[str, str]:
    return {"status": "healthy"}
