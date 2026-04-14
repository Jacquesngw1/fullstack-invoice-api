# 🎯 Fullstack Invoice API

Production-grade FastAPI backend for invoice processing.

Architecture: `ARCHITECTURE.md` | Tests: ✅ Passing CI

## Quick Start

```bash
git clone https://github.com/Jacquesngw1/fullstack-invoice-api.git
cd fullstack-invoice-api
cp .env.example .env
docker compose up --build
# API: http://localhost:8000 | Swagger: http://localhost:8000/docs
```

## Development

```bash
pip install -r requirements.txt
# Run migrations
alembic upgrade head
# Start server
uvicorn app.main:app --reload
# Run linting
ruff check .
ruff format --check .
# Run tests
pytest -v
```

## Project Structure

```
app/
├── api/v1/endpoints/   # Route handlers
├── core/               # Settings & config
├── db/                 # Engine, session, base
├── models/             # SQLAlchemy ORM models
└── schemas/            # Pydantic request/response models
alembic/                # Database migrations
tests/                  # Integration tests
```