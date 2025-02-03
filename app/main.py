from fastapi import FastAPI
from .routers import columns, items, values
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200",  # Permite requisições do Angular
    "http://127.0.0.1:4200"   # Outra forma de acessar localmente
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir essas origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os headers
)


# Incluir as rotas
app.include_router(columns.router, prefix="/api", tags=["Columns"])
app.include_router(items.router, prefix="/api", tags=["Items"])
app.include_router(values.router, prefix="/api", tags=["Values"])

@app.get("/")
def home():
    return {"message": "API dinâmica pronta para uso!"}
