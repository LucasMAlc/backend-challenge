from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schemas import UserCreate, UserResponse
from app.services import create_user, get_user_by_email, get_role_by_id

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar novo usuário",
    description="Cria um novo usuário. Campos obrigatórios: name, email, role_id. Senha é opcional (gerada automaticamente se não fornecida)",
    responses={
        201: {
            "description": "Usuário criado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "João Silva",
                        "email": "joao@example.com",
                        "role_id": 1,
                        "created_at": "2024-01-15",
                        "updated_at": None
                    }
                }
            }
        },
        400: {
            "description": "Dados inválidos",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "E-mail já está em uso"
                    }
                }
            }
        },
        404: {
            "description": "Role não encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Role com ID 999 não encontrado"
                    }
                }
            }
        }
    }
)
def create_new_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    **Questão 4:** Cria um novo usuário.
    
    **Campos obrigatórios:**
    - **name**: Nome completo do usuário
    - **email**: E-mail válido do usuário
    - **role_id**: ID do papel do usuário
    
    **Campo opcional:**
    - **password**: Senha (se não fornecida, será gerada automaticamente)
    """
    # Valida se o role existe
    role = get_role_by_id(db, user_data.role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role com ID {user_data.role_id} não encontrado"
        )
    
    # Verifica se o e-mail já está em uso
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já está em uso"
        )
    
    # Cria o usuário
    try:
        user = create_user(db, user_data)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro ao criar usuário. Verifique os dados fornecidos."
        )