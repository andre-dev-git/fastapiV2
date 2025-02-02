from sqlalchemy.orm import Session
from ..models import Item

class ItemsService:
    def create_item(db: Session):
        new_item = Item()
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    
    def list_items(db: Session):
        return db.query(Item).all()