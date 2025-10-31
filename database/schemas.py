from pydantic import BaseModel, ConfigDict
from datetime import date

class RecordBase(BaseModel):
    date: date
    amount: int
    category: str
    subcategory: str = "General"
    note: str = "General"
    model_config = ConfigDict(from_attributes=True)

class RecordCreate(RecordBase):
    pass

class RecordUpdate(BaseModel):
    date: date | None
    amount: int | None
    category: str | None
    subcategory: str | None
    note: str | None

class RecordOut(RecordBase):
    id: int