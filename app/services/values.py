from typing import List
from sqlalchemy.orm import Session
from ..models import ItemValue
from ..schemas import ItemValueCreate

class ValuesService:
    
    # Método para criar um único valor
    def create_value(self, db: Session, value: ItemValueCreate):
        new_value = ItemValue(
            item_id=value.item_id,
            column_id=value.column_id,
            value=value.value
        )
        db.add(new_value)
        db.commit()
        db.refresh(new_value)
        return new_value
    
    # Método para criar múltiplos valores
    def create_values(self, db: Session, values: List[ItemValueCreate]):
        for value in values:
            self.create_value(db, value)  # Agora estamos chamando create_value com self

    # Método para listar os valores
    def list_values(self, db: Session):
        return db.query(ItemValue).all()
