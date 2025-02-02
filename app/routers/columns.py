from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import DynamicColumn
from ..database import get_db
from ..schemas import DynamicColumnCreate

router = APIRouter()

@router.post("/columns/")
def create_column(column: DynamicColumnCreate, db: Session = Depends(get_db)):
    new_column = DynamicColumn(name=column.name, data_type=column.data_type)
    db.add(new_column)
    db.commit()
    db.refresh(new_column)
    return {"message": "Coluna criada com sucesso!", "column": new_column}

@router.get("/columns/")
def list_columns(db: Session = Depends(get_db)):
    columns = db.query(DynamicColumn).all()
    return columns
