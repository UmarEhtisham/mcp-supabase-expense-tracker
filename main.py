
from contextlib import contextmanager
from database.database import SessionLocal, engine, Base
from database import crud, schemas
from fastmcp import FastMCP
from pathlib import Path

Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

mcp = FastMCP(name = "ExpenseTracker")

@mcp.tool
def create_record(record: schemas.RecordCreate):
    """
    Create a new expense record in the database.
    """
    with get_db_session() as db:
        new_record = crud.create_record(db, record)
        return new_record

@mcp.tool
def get_record(record_id: int):
    """
    Retrieve an expense record by its ID.
    """
    with get_db_session() as db:
        record = crud.get_record(db, record_id)
        return record
    
@mcp.tool
def get_records():
    """
    Retrieve all expense records.
    """
    with get_db_session() as db:
        records = crud.get_records(db)
        return records
    
@mcp.tool
def update_record(record_id: int, record: schemas.RecordUpdate):
    """
    Update an existing expense record by its ID.
    """
    with get_db_session() as db:
        updated_record = crud.update_record(db, record_id, record)
        return updated_record

@mcp.tool
def delete_record(record_id: int):
    """
    Delete an expense record by its ID.
    """
    with get_db_session() as db:
        deleted_record = crud.delete_record(db, record_id)
        return deleted_record
    
from pathlib import Path
import json

@mcp.resource("resource://expense_tracker/categories", mime_type="application/json")
def get_categories():
    """
    Retrieve all expense categories and subcategories for the expense tracker.
    Returns a JSON structure with categories and their subcategories.
    """
    try:
        json_path = BASE_DIR / "categories.json"
        
        with open(json_path, "r", encoding="utf-8") as f:
            categories = f.read()
        
        return categories
    except FileNotFoundError:
        return json.dumps({
            "error": "categories.json not found",
            "categories": []
        })
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "categories": []
        })
    
if __name__ == "__main__":
    mcp.run()

