from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Item
from ..database import get_db

router = APIRouter()

@router.post("/items/")
def create_item(db: Session = Depends(get_db)):
    new_item = Item()
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item criado com sucesso!", "item": new_item}

@router.get("/items/")
def list_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
