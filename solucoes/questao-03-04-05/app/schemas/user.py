from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date


class UserCreate(BaseModel):
    """
    Schema para criação de usuário (request body do POST /users)
    
    Campos obrigatórios: name, email, role_id
    Campo opcional: password (gerado automaticamente se não fornecido)
    
    Exemplo:
        {
            "name": "João Silva",
            "email": "joao@example.com",
            "role_id": 1,
            "password": "senha123"  // opcional
        }
    """
    name: str = Field(..., min_length=3, max_length=100, description="Nome completo do usuário")
    email: EmailStr = Field(..., description="E-mail válido do usuário")
    role_id: int = Field(..., gt=0, description="ID do papel do usuário")
    password: Optional[str] = Field(None, min_length=6, description="Senha (opcional, gerada automaticamente se não fornecida)")


class UserResponse(BaseModel):
    """
    Schema de resposta para usuário criado
    
    Exemplo:
        {
            "id": 1,
            "name": "João Silva",
            "email": "joao@example.com",
            "role_id": 1,
            "created_at": "2024-01-15"
        }
    """
    id: int
    name: str
    email: str
    role_id: int
    created_at: date
    updated_at: Optional[date] = None
    
    model_config = ConfigDict(from_attributes=True)