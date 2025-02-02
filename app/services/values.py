from typing import List
from sqlalchemy.orm import Session
from ..models import ItemValue, DynamicColumn, Item
from ..schemas import ItemValueCreate

class ValuesService:
    
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
    
    def create_values(self, db: Session, values: List[ItemValueCreate]):
        for value in values:
            self.create_value(db, value)

    def list_values(self, db: Session):
        items = db.query(Item).all()
        items_data = {item.id: [] for item in items}

        values = db.query(ItemValue, DynamicColumn, Item).\
            join(DynamicColumn, ItemValue.column_id == DynamicColumn.id).\
            join(Item, ItemValue.item_id == Item.id).\
            all()

        for value in values:
            item_value: ItemValue = value[0] 
            dynamic_column: DynamicColumn = value[1]
            item: Item = value[2]
            
            items_data[item.id].append({
                "column_id": dynamic_column.id,
                "column_name": dynamic_column.name,
                "value": item_value.value
            })

        return items_data
  