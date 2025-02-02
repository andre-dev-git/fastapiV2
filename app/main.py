from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, database

# Iniciar a aplicação FastAPI
app = FastAPI()

# Dependência para acessar a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API de Estoque"}

@app.post("/estoque/")
def adicionar_item(item: schemas.ItemEstoque, db: Session = Depends(get_db)):
    return crud.adicionar_item(db=db, item=item)

@app.get("/estoque/")
def listar_estoque(db: Session = Depends(get_db)):
    return crud.listar_estoque(db=db)
