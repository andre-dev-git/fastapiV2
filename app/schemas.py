from pydantic import BaseModel

# Esquema para o item no estoque
class ItemEstoque(BaseModel):
    nome_item: str
    quantidade: int

    class Config:
        orm_mode = True
