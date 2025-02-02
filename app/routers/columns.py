from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import DynamicColumnCreate
from ..services.columns import ColumnsService

router = APIRouter()

@router.post("/columns/")
def create_column(column: DynamicColumnCreate, db: Session = Depends(get_db)):
    result = ColumnsService.create_column(db, column)
    return {"message": "Coluna criada com sucesso!", "column": result}

@router.get("/columns/")
def list_columns(db: Session = Depends(get_db)):
    return {"message": "Ok", "data": ColumnsService.list_columns(db)}
