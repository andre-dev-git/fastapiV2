from sqlalchemy.orm import Session
from . import models, schemas

# Função para adicionar um item no estoque
def adicionar_item(db: Session, item: schemas.ItemEstoque):
    novo_item = models.Estoque(nome_item=item.nome_item, quantidade=item.quantidade)
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return {"message": "Item adicionado com sucesso!", "item": novo_item}

# Função para listar os itens do estoque
def listar_estoque(db: Session):
    return db.query(models.Estoque).all()
