from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import ItemValue
from ..database import get_db
from ..schemas import ItemValueCreate

router = APIRouter()

@router.post("/item-values/")
def add_item_value(value: ItemValueCreate, db: Session = Depends(get_db)):
    new_value = ItemValue(item_id=value.item_id, column_id=value.column_id, value=value.value)
    db.add(new_value)
    db.commit()
    db.refresh(new_value)
    return {"message": "Valor adicionado com sucesso!", "item_value": new_value}

@router.get("/item-values/")
def list_item_values(db: Session = Depends(get_db)):
    values = db.query(ItemValue).all()
    return values

@router.delete("/item-values/{item_value_id}/")
def delete_item_value(item_value_id: int, db: Session = Depends(get_db)):
    try:
        item_value = db.query(ItemValue).filter(ItemValue.id == item_value_id).one()
        db.delete(item_value)
        db.commit()
        return {"message": f"Valor do item {item_value_id} excluído com sucesso!"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Item value not found")