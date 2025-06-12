from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.db_config import TORTOISE_ORM
from app.models import Produto

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False, 
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "API rodando com Tortoise ORM e models organizados!"}

@app.get("/produtos")
async def listar_produtos():
    produtos = await Produto.all()
    return produtos