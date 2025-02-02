from sqlalchemy.orm import Session
from ..models import ItemValue
from ..schemas import ItemValueCreate

class ValuesService:
    def create_value(db: Session, value: ItemValueCreate):
        new_value = ItemValue(
            item_id=value.item_id,
            column_id=value.column_id,
            value=value.value
        )
        db.add(new_value)
        db.commit()
        db.refresh(new_value)
        return new_value

    def list_values(db: Session):
        return db.query(ItemValue).all()
