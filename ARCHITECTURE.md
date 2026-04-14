# Architecture Decisions

- **FastAPI over Django**: Async-native, automatic OpenAPI, lower latency for I/O bound endpoints.
- **SQLAlchemy + Pydantic**: Explicit schema validation with `response_model` on all endpoints. Pydantic v2 `from_attributes=True` for ORM compatibility.
- **Alembic Migrations**: Database schema managed via versioned migrations. `alembic upgrade head` runs in CI before tests and in Docker Compose on startup.
- **Docker Compose Healthchecks**: Ensures DB readiness before API boot. Prevents CI flakiness.
- **CORS Configuration**: Origins configured as a JSON list (`list[str]`) via `pydantic-settings`, avoiding fragile comma-split strings.
- **CI Pipeline**: Lint (`ruff check` + `ruff format --check`) → Migrate → Test (`pytest`). Ensures code quality and correctness on every push.
- **Test Strategy**: HTTP-level integration tests via `TestClient`. Session-scoped fixture creates tables as fallback, but CI relies on Alembic migrations.
- **Safer DB Writes**: Create endpoints use try/except with rollback on failure and `db.refresh()` to guarantee returned fields are populated.
- **Next Phase**: Add Celery for async PDF parsing, rate limiting via `slowapi`, and JWT auth via `fastapi-users`.
