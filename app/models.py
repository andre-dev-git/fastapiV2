from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class DynamicColumn(Base):
    __tablename__ = "dynamic_columns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    data_type = Column(String, nullable=False)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)

class ItemValue(Base):
    __tablename__ = "item_values"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    column_id = Column(Integer, ForeignKey("dynamic_columns.id"), nullable=False)
    value = Column(String, nullable=False)  # Armazena todos os tipos como string

    item = relationship("Item", back_populates="values")
    column = relationship("DynamicColumn")

Item.values = relationship("ItemValue", back_populates="item")
