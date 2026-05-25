from fastapi import APIRouter
from sistema_estudos.schemas.cursos import Curso

router = APIRouter(
    prefix="/cursos",
    tags=["Cursos"]
)

@router.get("/")
def listar_cursos():
    return {"mensagem": "Lista de cursos"}

@router.post("/")
def criar_curso(curso: Curso):
    return curso