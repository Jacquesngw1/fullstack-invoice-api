from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceRead

router = APIRouter()


@router.post("/invoices", response_model=InvoiceRead)
def create_invoice(data: InvoiceCreate, db: Session = Depends(get_db)) -> InvoiceRead:
    inv = Invoice(vendor=data.vendor, amount=data.amount)
    try:
        db.add(inv)
        db.commit()
        db.refresh(inv)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create invoice")
    return inv


@router.get("/invoices", response_model=list[InvoiceRead])
def list_invoices(db: Session = Depends(get_db)) -> list[InvoiceRead]:
    return db.query(Invoice).all()
