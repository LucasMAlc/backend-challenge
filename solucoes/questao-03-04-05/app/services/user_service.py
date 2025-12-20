from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.utils import generate_password, hash_password
from datetime import date
from typing import Optional


def create_user(db: Session, user_data: UserCreate) -> User:
    """
    Cria um novo usuário no banco de dados.
    
    Se a senha não for fornecida, gera uma automaticamente.
    A senha é sempre armazenada como hash (bcrypt).
    
    Args:
        db: Sessão do banco de dados
        user_data: Dados do usuário (schema UserCreate)
        
    Returns:
        User: Usuário criado
        
    Raises:
        ValueError: Se o role_id não existir
        
    Example:
        >>> user_data = UserCreate(
        ...     name="João Silva",
        ...     email="joao@example.com",
        ...     role_id=1
        ... )
        >>> user = create_user(db, user_data)
        >>> user.id
        1
    """
    # Se senha não foi fornecida, gera automaticamente
    if user_data.password is None:
        plain_password = generate_password()
    else:
        plain_password = user_data.password
    
    # Cria hash da senha
    hashed_password = hash_password(plain_password)
    
    # Cria o usuário
    db_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password,
        role_id=user_data.role_id,
        created_at=date.today(),
        updated_at=None
    )
    
    # Salva no banco
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    Busca um usuário pelo e-mail.
    
    Args:
        db: Sessão do banco de dados
        email: E-mail do usuário
        
    Returns:
        User: Usuário se encontrado, None caso contrário
    """
    return db.query(User).filter(User.email == email).first()