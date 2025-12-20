from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import RoleResponse
from app.services import get_role_by_id

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.get(
    "/{role_id}",
    response_model=RoleResponse,
    status_code=status.HTTP_200_OK,
    summary="Buscar papel por ID",
    description="Retorna os dados de um papel (role) específico pelo seu ID",
    responses={
        200: {
            "description": "Papel encontrado com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "description": "Administrador"
                    }
                }
            }
        },
        404: {
            "description": "Papel não encontrado",
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
def get_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    """
    **Questão 3:** Busca um papel (role) pelo ID.
    
    - **role_id**: ID do papel a ser buscado
    """
    # Busca o role usando o service
    role = get_role_by_id(db, role_id)
    
    # Se não encontrou, retorna erro 404
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role com ID {role_id} não encontrado"
        )
    
    return role