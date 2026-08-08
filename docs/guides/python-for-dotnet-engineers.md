# Python Reference for Experienced .NET Engineers

## Mental model

Python is dynamically executed but can be developed with strong discipline through type hints, static analysis, tests, immutable conventions, small modules, and explicit contracts.

## Key differences to internalize

- Indentation is syntax.
- Type hints are not runtime enforcement unless a library validates them.
- `None` is the null value and optionality should be explicit.
- Iterables, generators, comprehensions, and context managers are central idioms.
- Exceptions are commonly used for error propagation, but public boundaries should map them intentionally.
- Virtual environments isolate project dependencies.
- Modules and packages replace assembly/namespace expectations in different ways.
- Duck typing is common, but protocols and abstract base classes can express interfaces.
- Dataclasses and Pydantic models serve different purposes.

## Quality tools selected

- Ruff: formatting-compatible linting and import/order checks.
- mypy strict mode: catches missing and inconsistent type assumptions.
- pytest: concise deterministic tests and fixtures.
- Pydantic: runtime validation at external boundaries.

## Mapping familiar concepts

| .NET concept | Python project equivalent |
|---|---|
| ASP.NET controller/minimal API | FastAPI route |
| DTO with validation attributes | Pydantic model |
| NuGet package | PyPI package |
| `.csproj` | `pyproject.toml` |
| xUnit/NUnit | pytest |
| Roslyn analyzers | Ruff and mypy |
| `using` / `IDisposable` | context manager / `with` |
| LINQ pipeline | comprehensions, iterators, pandas operations |
| Interface | Protocol or abstract base class |
