from sqlalchemy import Column, Integer, String
from sqlalchemy import Date
from database.database import Base

class ExpenseRecords(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
    category = Column(String, nullable=False, index=True)
    subcategory = Column(String, default="General", index=True)
    note = Column(String, default="General")


