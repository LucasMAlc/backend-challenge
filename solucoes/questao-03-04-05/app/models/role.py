from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Role(Base):
    """
    Model que representa a tabela 'roles' no banco de dados.
    
    Atributos:
        id: Identificador único (chave primária, auto-incremento)
        description: Descrição do papel (ex: "Administrador", "Gerente")
        users: Relacionamento com usuários que possuem este papel
    """
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    
    # Relacionamento: Um role pode ter muitos users
    users = relationship("User", back_populates="role")
    
    def __repr__(self):
        return f"<Role(id={self.id}, description='{self.description}')>"