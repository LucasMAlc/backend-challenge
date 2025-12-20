from sqlalchemy.orm import Session
from app.models import Role
from typing import Optional


def get_role_by_id(db: Session, role_id: int) -> Optional[Role]:
    """
    Busca um papel (role) pelo ID.
    
    Args:
        db: Sessão do banco de dados
        role_id: ID do papel
        
    Returns:
        Role: Objeto Role se encontrado, None caso contrário
        
    Example:
        >>> role = get_role_by_id(db, 1)
        >>> role.description
        'Administrador'
    """
    return db.query(Role).filter(Role.id == role_id).first()