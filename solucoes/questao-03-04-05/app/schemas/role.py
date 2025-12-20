from pydantic import BaseModel, ConfigDict


class RoleResponse(BaseModel):
    """
    Schema de resposta para o endpoint GET /roles/{role_id}
    
    Define o formato JSON retornado pela API ao buscar um papel.
    
    Exemplo:
        {
            "id": 1,
            "description": "Administrador"
        }
    """
    id: int
    description: str
    
    model_config = ConfigDict(from_attributes=True)