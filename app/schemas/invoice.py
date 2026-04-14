from datetime import datetime

from pydantic import BaseModel


class InvoiceCreate(BaseModel):
    vendor: str
    amount: float


class InvoiceRead(BaseModel):
    id: int
    vendor: str
    amount: float
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
