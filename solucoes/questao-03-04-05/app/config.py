import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()


class Settings(BaseSettings):
    """
    Configurações da aplicação carregadas das variáveis de ambiente.
    
    As variáveis são carregadas do arquivo .env na raiz do projeto.
    """
    
    # Ambiente
    environment: str = "development"
    
    # Banco de Dados
    database_url: str
    
    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True
    
    # Logs
    log_level: str = "INFO"
    
    # Aplicação
    app_title: str = "Shipay Backend Challenge API"
    app_description: str = "API REST para gerenciamento de usuários, papéis e permissões"
    app_version: str = "1.0.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Instância global das configurações
settings = Settings()