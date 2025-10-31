from sqlalchemy.orm import Session
import database.models as models
import database.schemas as schemas

def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.ExpenseRecords(
        date=record.date,
        amount=record.amount,
        category=record.category,
        subcategory=record.subcategory,
        note=record.note
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return schemas.RecordOut.model_validate(db_record).model_dump(mode='json')

def get_record(db: Session, record_id: int):
    db_record = (
        db
        .query(models.ExpenseRecords)
        .filter(models.ExpenseRecords.id == record_id)
        .first()
    )

    if db_record:
        return schemas.RecordOut.model_validate(db_record).model_dump(mode='json')
    return None

def get_records(db: Session):
    db_records = db.query(models.ExpenseRecords).all()
    return [schemas.RecordOut.model_validate(record).model_dump(mode='json') for record in db_records] 

def update_record(db: Session, record_id: int, record: schemas.RecordUpdate):
    db_record = db.query(models.ExpenseRecords).filter(models.ExpenseRecords.id == record_id).first()
    if not db_record:
        return None  

    # Only update fields that were actually sent by the client
    for field, value in record.model_dump(exclude_unset=True).items():
        setattr(db_record, field, value)

    db.commit()
    db.refresh(db_record)
    return schemas.RecordOut.model_validate(db_record).model_dump(mode='json')


def delete_record(db: Session, record_id: int):
    db_record = db.query(models.ExpenseRecords).filter(models.ExpenseRecords.id == record_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return {"message": "Record deleted successfully", "id": record_id}
    return {"message": "Record not found", "id": record_id}

