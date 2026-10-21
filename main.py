from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from database import Base, engine
from routers import categoria, usuario, freelancer

#Base.metadata.create_all(bind=engine)

# titulo
app = FastAPI(
    title="Freejob",
    description="api para cadastro de freelancers"
)


# tratamento de erro para registros duplicados
@app.exception_handler(IntegrityError)
async def integrity_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=409,
        content={"detail": "Registro duplicado ou em conflito com dados existentes"}
    )


# incluir rotas
app.include_router(categoria.router)
app.include_router(usuario.router)
app.include_router(freelancer.router)


# rota raiz
@app.get("/")
def home():
    return {"mensagem": "api com sucesso"}