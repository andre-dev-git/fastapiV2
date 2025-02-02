from sqlalchemy.orm import Session
from ..models import DynamicColumn
from ..schemas import DynamicColumnCreate

class ColumnsService:
    def create_column(db: Session, column: DynamicColumnCreate):
        new_column = DynamicColumn(name=column.name, data_type=column.data_type)
        db.add(new_column)
        db.commit()
        db.refresh(new_column)
        return new_column

    def list_columns(db: Session):
        return db.query(DynamicColumn).all()