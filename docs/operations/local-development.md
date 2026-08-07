# Local Development

## Supported baseline

- Python 3.12 or newer.
- Git.
- A shell capable of activating a Python virtual environment.

## Setup

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Run quality gates

```bash
ruff check .
mypy src
pytest
```

## Run the service

```bash
uvicorn dws_ai_validation.main:app --reload
```

Useful endpoints:

- Health: `http://127.0.0.1:8000/health`
- OpenAPI UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Repository hygiene

Never commit:

- Virtual environments.
- Secrets or `.env` files.
- Private datasets.
- Generated cloud credentials.
- Large model binaries unless intentionally managed through an artifact strategy.
