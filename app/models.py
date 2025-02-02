from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Configuração do banco de dados
DATABASE_URL = "postgresql://root:root@localhost:5432/storage"

# Criação da engine de banco de dados
engine = create_engine(DATABASE_URL)

# Criação da base para os modelos
Base = declarative_base()

# Modelo da tabela Estoque
class Estoque(Base):
    __tablename__ = "estoque"
    id = Column(Integer, primary_key=True, index=True)
    nome_item = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)
