from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from sqlalchemy.orm.exc import NoResultFound
from ..schemas import ItemValueCreate
from ..services.values import ValuesService

router = APIRouter()

@router.post("/item-values/")
def add_item_value(value: ItemValueCreate, db: Session = Depends(get_db)):
    return {"message": "Valor adicionado com sucesso!", "item_value": ValuesService.create_value(db, value)}

@router.get("/item-values/")
def list_item_values(db: Session = Depends(get_db)):
    return {"message": "Ok", "data": ValuesService.list_values(db)}