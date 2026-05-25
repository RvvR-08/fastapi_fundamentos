# API Sistema Escolar

Projeto desenvolvido com FastAPI e Poetry para gerenciamento de alunos e cursos.

## Tecnologias utilizadas

- Python
- FastAPI
- Poetry
- Pydantic

## Estrutura do Projeto

```bash
sistema_estudos/
│
├── routers/
├── schemas/
├── main.py
└── db.py
```

## Entidades

### Alunos
- nome
- idade
- nota
- ativo
- curso_id

### Cursos
- nome
- carga_horaria
- professor

## Como executar o projeto

### Instalar dependências

```bash
poetry install
```

### Executar servidor

```bash
poetry run fastapi dev .\sistema_estudos\main.py
```

## Rotas disponíveis

### Alunos
- GET /alunos
- POST /alunos

### Cursos
- GET /cursos
- POST /cursos

## Documentação Swagger
# API Sistema Escolar

Projeto desenvolvido com FastAPI e Poetry para gerenciamento de alunos e cursos.

## Tecnologias utilizadas

- Python
- FastAPI
- Poetry
- Pydantic

## Estrutura do Projeto

```bash
sistema_estudos/
│
├── routers/
├── schemas/
├── main.py
└── db.py
```

## Entidades

### Alunos
- nome
- idade
- nota
- ativo
- curso_id

### Cursos
- nome
- carga_horaria
- professor

## Como executar o projeto

### Instalar dependências

```bash
poetry install
```

### Executar servidor

```bash
poetry run fastapi dev .\sistema_estudos\main.py
```

## Rotas disponíveis

### Alunos
- GET /alunos
- POST /alunos

### Cursos
- GET /cursos
- POST /cursos

## HTML
http://127.0.0.1:8000

## Documentação Swagger
http://127.0.0.1:8000/docs