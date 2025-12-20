from sqlalchemy import Column, BigInteger, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Claim(Base):
    """
    Model que representa a tabela 'claims' no banco de dados.
    
    Atributos:
        id: Identificador único (chave primária, auto-incremento)
        description: Descrição da permissão (ex: "Criar usuários")
        active: Se a permissão está ativa ou não
        users: Relacionamento many-to-many com usuários
    """
    __tablename__ = "claims"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    
    # Relacionamento many-to-many com users através de user_claims
    users = relationship(
        "User",
        secondary="user_claims",
        back_populates="claims"
    )
    
    def __repr__(self):
        return f"<Claim(id={self.id}, description='{self.description}', active={self.active})>"