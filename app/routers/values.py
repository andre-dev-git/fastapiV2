from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from sqlalchemy.orm.exc import NoResultFound
from ..schemas import ItemValueCreate
from ..services.values import ValuesService

router = APIRouter()

@router.post("/item-values/")
def add_item_values(values: List[ItemValueCreate], db: Session = Depends(get_db)):
    values_service = ValuesService()

    values_service.create_values(db=db, values=values)
    
    return {"message": "Valores adicionados com sucesso!"}

@router.get("/item-values/")
def list_item_values(db: Session = Depends(get_db)):
    values_service = ValuesService()
    return {"message": "Ok", "data": values_service.list_values(db)}
