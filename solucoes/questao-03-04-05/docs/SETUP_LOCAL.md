# Setup Local

## Pré-requisitos

- Python
- PostgreSQL
- Git

## 1. Clonar o Repositório

```bash
git clone https://github.com/LucasMAlc/backend-challenge.git
cd solucoes
cd questao-03-04-05
```

## 2. Configurar o Banco de Dados

### Criar o banco de dados

```sql

CREATE DATABASE shipay_challenge;

```

### Executar o script DDL

Cole e execute o conteúdo do arquivo `1_create_database_ddl.sql`

### Inserir dados de teste (opcional)

```sql
INSERT INTO roles (description) VALUES 
    ('Administrador'),
    ('Gerente'),
    ('Usuário'),
    ('Operador');

INSERT INTO claims (description, active) VALUES
    ('Visualizar usuários', true),
    ('Criar usuários', true),
    ('Editar usuários', true),
    ('Excluir usuários', true),
    ('Gerar relatórios', true);
```

## 3. Configurar o Ambiente Python

### Criar ambiente virtual

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

## 4. Configurar Variáveis de Ambiente

### Criar o arquivo .env baseado no .env.example

Ajuste a linha DATABASE_URL com suas informações:

```bash
DATABASE_URL=postgresql+psycopg2://USUARIO:SENHA@HOST:PORTA/NOME_BANCO
```
Para algo como:

```bash
DATABASE_URL=postgresql+psycopg2://postgres:sua_senha@localhost:5432/shipay_challenge
```


## 5. Executar a Aplicação

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A aplicação estará disponível em:
- API: http://localhost:8000
- Documentação Swagger: http://localhost:8000/docs

## 6. Testar os Endpoints

Acesse a documentação interativa Swagger em: **http://localhost:8000/docs**

### Questão 3 - GET /roles/{role_id}

1. Localize a seção **Roles**
2. Clique em **GET /roles/{role_id}**
3. Clique em **"Try it out"**
4. No campo `role_id`, digite: **1**
5. Clique em **"Execute"**

Resposta esperada (status 200):
```json
{
  "id": 1,
  "description": "Administrador"
}
```

### Questão 4 - POST /users

1. Localize a seção **Users**
2. Clique em **POST /users**
3. Clique em **"Try it out"**
4. No campo **Request body**, cole:

```json
{
  "name": "João Silva",
  "email": "joao@example.com",
  "role_id": 1
}
```

5. Clique em **"Execute"**

Resposta esperada (status 201):
```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@example.com",
  "role_id": 1,
  "created_at": "2025-12-20",
  "updated_at": null
}
```

**Nota:** O campo `password` é opcional. Se não fornecido, será gerado automaticamente.

## 7. Testes Automatixados

O projeto possui testes automatizados para os principais endpoints.

Para executar:

```bash
pytest
```

Os testes validam:

- Criação de usuários
- Consulta de roles por id
- Validações básicas de erro

## Estrutura do Projeto

```
questao-03-04-05/
    app/
        models/          
        schemas/         
        services/        
        routes/          
        utils/            
        config.py        
        database.py      
        main.py        
    docs/
        DEPLOY_PRODUCAO.md
        SETUP_LOCAL.md                
    tests/               
    requirements.txt    
    .env                 
```
