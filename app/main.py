from fastapi import FastAPI
from .routers import columns, items, values
from .database import Base, engine

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir as rotas
app.include_router(columns.router, prefix="/api", tags=["Columns"])
app.include_router(items.router, prefix="/api", tags=["Items"])
app.include_router(values.router, prefix="/api", tags=["Values"])

@app.get("/")
def home():
    return {"message": "API dinâmica pronta para uso!"}
