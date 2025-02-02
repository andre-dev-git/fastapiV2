from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL do banco de dados
DATABASE_URL = "postgresql://root:root@localhost:5432/storage"

# Criando a engine do banco de dados
engine = create_engine(DATABASE_URL)

# Criando a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
