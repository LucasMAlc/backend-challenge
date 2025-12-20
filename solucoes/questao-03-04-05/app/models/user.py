from sqlalchemy import Column, BigInteger, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    """
    Model que representa a tabela 'users' no banco de dados.
    
    Atributos:
        id: Identificador único (chave primária, auto-incremento)
        name: Nome completo do usuário
        email: E-mail do usuário (único)
        password: Senha do usuário (hash)
        role_id: ID do papel do usuário (FK para roles)
        created_at: Data de criação do usuário
        updated_at: Data da última atualização
        role: Relacionamento com o papel do usuário
        claims: Relacionamento many-to-many com permissões
    """
    __tablename__ = "users"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=True)
    
    # Relacionamento: Um user pertence a um role
    role = relationship("Role", back_populates="users")
    
    # Relacionamento many-to-many com claims através de user_claims
    claims = relationship(
        "Claim",
        secondary="user_claims",
        back_populates="users"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"