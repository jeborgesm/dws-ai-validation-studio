# Troubleshooting

## Import errors after installation

Confirm the virtual environment is active, then reinstall editable dependencies:

```bash
pip install -e ".[dev]"
```

## Python version mismatch

```bash
python --version
```

The project requires Python 3.12 or newer. CI currently verifies Python 3.12.

## Coverage command fails to find package

The editable install must complete before running pytest. Running from the repository root is recommended.

## CSV cannot be parsed

Milestone 0 assumes a conventional UTF-compatible comma-separated file. Encoding detection, delimiter selection, and advanced parser controls are planned work. Use a small known UTF-8 CSV during the foundation milestone.

## PowerShell prevents activation

A local execution-policy setting may block scripts. Activation is convenient but not mandatory; the virtual environment's Python executable can be called directly.
