from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    idade: int
    nota: float
    ativo: bool
    curso_id: int