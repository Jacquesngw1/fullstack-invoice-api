import pytest
from fastapi.testclient import TestClient

from app.db.base import Base
from app.db.session import engine
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True, scope="session")
def _setup_db():
    """Ensure all tables exist before tests run."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_invoice():
    response = client.post("/api/v1/invoices", json={"vendor": "Acme", "amount": 150.0})
    assert response.status_code == 200
    data = response.json()
    assert data["vendor"] == "Acme"
    assert data["amount"] == 150.0
    assert data["status"] == "pending"
    assert "id" in data
    assert "created_at" in data


def test_list_invoices():
    # Create an invoice first
    client.post("/api/v1/invoices", json={"vendor": "TestCorp", "amount": 200.0})
    response = client.get("/api/v1/invoices")
    assert response.status_code == 200
    invoices = response.json()
    assert isinstance(invoices, list)
    assert len(invoices) >= 1
    assert all("id" in inv for inv in invoices)
    assert all("vendor" in inv for inv in invoices)
