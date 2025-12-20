from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

# Cria a engine de conexão com o PostgreSQL
engine = create_engine(
    settings.database_url,
    echo=False,  # True para ver SQL no console (útil para debug)
    pool_pre_ping=True,  # Verifica conexão antes de usar
    pool_size=5,  # Máximo de 5 conexões simultâneas
    max_overflow=10  # Permite até 15 conexões no total (5 + 10)
)

# Factory para criar sessões do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os models herdarem
Base = declarative_base()

def get_db():
    """
    Cria uma sessão de banco de dados e garante que seja fechada após o uso.
    
    Esta função é usada como dependência nos endpoints FastAPI.
    
    Uso:
        @app.get("/endpoint")
        def meu_endpoint(db: Session = Depends(get_db)):
            # usa db aqui
            pass
    
    Yields:
        Session: Sessão ativa do SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()