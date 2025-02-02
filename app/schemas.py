from pydantic import BaseModel

class DynamicColumnCreate(BaseModel):
    name: str
    data_type: str

class ItemValueCreate(BaseModel):
    item_id: int
    column_id: int
    value: str
