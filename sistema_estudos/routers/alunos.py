from fastapi import APIRouter
from sistema_estudos.schemas.alunos import Aluno

router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)

@router.get("/")
def listar_alunos():
    return {"mensagem": "Lista de alunos"}

@router.post("/")
def criar_aluno(aluno: Aluno):
    return aluno