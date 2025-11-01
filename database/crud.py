from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import database.models as models
import database.schemas as schemas

async def create_record(db: AsyncSession, record: schemas.RecordCreate):
    db_record = models.ExpenseRecords(
        date=record.date,
        amount=record.amount,
        category=record.category,
        subcategory=record.subcategory,
        note=record.note
    )
    db.add(db_record)
    await db.commit()
    await db.refresh(db_record)
    return schemas.RecordOut.model_validate(db_record).model_dump(mode='json')

async def get_record(db: AsyncSession, record_id: int):
    result = await db.execute(
        select(models.ExpenseRecords)
        .filter(models.ExpenseRecords.id == record_id)
    )
    db_record = result.scalar_one_or_none()

    if db_record:
        return schemas.RecordOut.model_validate(db_record).model_dump(mode='json')
    return None

async def get_records(db: AsyncSession):
    result = await db.execute(select(models.ExpenseRecords))
    db_records = result.scalars().all()
    return [schemas.RecordOut.model_validate(record).model_dump(mode='json') for record in db_records] 

async def update_record(db: AsyncSession, record_id: int, record: schemas.RecordUpdate):
    result = await db.execute(
        select(models.ExpenseRecords)
        .filter(models.ExpenseRecords.id == record_id)
    )
    db_record = result.scalar_one_or_none()
    
    if not db_record:
        return None  

    # Only update fields that were actually sent by the client
    for field, value in record.model_dump(exclude_unset=True).items():
        setattr(db_record, field, value)

    await db.commit()
    await db.refresh(db_record)
    return schemas.RecordOut.model_validate(db_record).model_dump(mode='json')


async def delete_record(db: AsyncSession, record_id: int):
    result = await db.execute(
        select(models.ExpenseRecords)
        .filter(models.ExpenseRecords.id == record_id)
    )
    db_record = result.scalar_one_or_none()
    
    if db_record:
        await db.delete(db_record)
        await db.commit()
        return {"message": "Record deleted successfully", "id": record_id}
    return {"message": "Record not found", "id": record_id}