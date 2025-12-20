# Deploy em Produção

## Visão Geral

Este documento descreve de forma simples como realizar o deploy da API REST desenvolvida com FastAPI e PostgreSQL na AWS.

## Arquitetura de Produção

```
Cliente → API (FastAPI em Docker) → PostgreSQL (RDS)

```

## Serviços Utilizados

- EC2 (Windows Server): execução da aplicação
- Docker Desktop: execução do container
- RDS (PostgreSQL): banco de dados
- Security Groups: controle de acesso

### Passos

#### 1. Criar a instância EC2 (Windows)

- Criar uma instância EC2 com Windows Server

- Liberar portas no Security Group:
    - 3389 (RDP)
    - 8000 (API)

#### 2. Acessar a instância

- Conectar via Remote Desktop (RDP)
- Utilizar a senha gerada pela AWS

#### 3. Instalar Docker Desktop

- Baixar o Docker Desktop para Windows
- Habilitar suporte a containers Linux

#### 4. Configurar a aplicação

- Copiar o código da API para a instância
- Criar o arquivo .env com as variáveis de ambiente

Exemplo:
```bash
DATABASE_URL=postgresql+psycopg2://USUARIO:SENHA@HOST:PORTA/NOME_BANCO
```

#### 5. Build e execução do container

```powershell
docker build -t api .
docker run -d -p 8000:8000 --env-file .env api

```

#### 6. Testar API

```powershell
curl http://<IP_PUBLICO_EC2>:8000/health

```