from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import roles, users

# Inicializa a aplicação FastAPI
app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração de CORS (permite requisições de qualquer origem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra os routers
app.include_router(roles.router)
app.include_router(users.router)


@app.get("/", tags=["Health Check"])
def root():
    """
    Endpoint raiz - Health check da API.
    
    Retorna informações básicas sobre a API e seus endpoints disponíveis.
    """
    return {
        "message": "Shipay Backend Challenge API",
        "version": settings.app_version,
        "status": "online",
        "environment": settings.environment,
        "endpoints": {
            "questao_3": "GET /roles/{role_id} - Buscar papel por ID",
            "questao_4": "POST /users - Criar novo usuário",
            "docs": "GET /docs - Documentação interativa (Swagger)",
            "redoc": "GET /redoc - Documentação alternativa (ReDoc)"
        }
    }


@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Endpoint de health check simples.
    
    Usado para verificar se a API está rodando.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload
    )