from fastapi import FastAPI
from sistema_estudos.routers import alunos, cursos

app = FastAPI()

app.include_router(alunos.router)
app.include_router(cursos.router)

@app.get("/")
def home():
    return {"mensagem": "Tá funcionano"}