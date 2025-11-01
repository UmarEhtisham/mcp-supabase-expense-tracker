from contextlib import asynccontextmanager
from database.database import SessionLocal, engine, Base
from database import crud, schemas
from fastmcp import FastMCP
from pathlib import Path

# Create tables asynchronously
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

BASE_DIR = Path(__file__).resolve().parent

@asynccontextmanager
async def get_db_session():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()

mcp = FastMCP(name="ExpenseTracker")

@mcp.tool
async def create_record(record: schemas.RecordCreate):
    """
    Create a new expense record in the database.
    """
    async with get_db_session() as db:
        new_record = await crud.create_record(db, record)
        return new_record

@mcp.tool
async def get_record(record_id: int):
    """
    Retrieve an expense record by its ID.
    """
    async with get_db_session() as db:
        record = await crud.get_record(db, record_id)
        return record
    
@mcp.tool
async def get_records():
    """
    Retrieve all expense records.
    """
    async with get_db_session() as db:
        records = await crud.get_records(db)
        return records
    
@mcp.tool
async def update_record(record_id: int, record: schemas.RecordUpdate):
    """
    Update an existing expense record by its ID.
    """
    async with get_db_session() as db:
        updated_record = await crud.update_record(db, record_id, record)
        return updated_record

@mcp.tool
async def delete_record(record_id: int):
    """
    Delete an expense record by its ID.
    """
    async with get_db_session() as db:
        deleted_record = await crud.delete_record(db, record_id)
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
    import asyncio
    
    # Initialize database tables
    asyncio.run(init_db())
    
    # Run the MCP server
    # mcp.run(transport="stdio")
    mcp.run(transport="http", host="0.0.0.0", port=8000)