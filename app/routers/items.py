from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.items import ItemsService

router = APIRouter()

@router.post("/items/")
def create_item(db: Session = Depends(get_db)):
    new_item = ItemsService.create_item(db)
    return {"message": "Item criado com sucesso!", "item": new_item}

@router.get("/items/")
def list_items(db: Session = Depends(get_db)):
    return {"message": "Ok", "data": ItemsService.list_items(db)}
