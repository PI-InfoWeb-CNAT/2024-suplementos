from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "produto" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "preco" DOUBLE PRECISION NOT NULL,
    "descricao" TEXT,
    "imagem" VARCHAR(255) NOT NULL,
    "porcentagem_desconto" INT DEFAULT 0,
    "categoria" VARCHAR(15) NOT NULL
);
COMMENT ON COLUMN "produto"."categoria" IS 'acessorios: (''acessorios'',)\nalimentos: (''alimentos'',)\nroupas: (''roupas'',)\nsuplementos: suplementos';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
