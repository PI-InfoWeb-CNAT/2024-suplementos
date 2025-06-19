from tortoise import fields, models
from decimal import Decimal
import enum

class Categoria(enum.Enum): 
    acessorios = 'acessorios',
    alimentos = 'alimentos',
    roupas = 'roupas',
    suplementos = 'suplementos'

class Produto(models.Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=255)
    preco = fields.FloatField(null=False)
    descricao = fields.TextField(null=True)
    imagem = fields.CharField(max_length=255, null=True, default=None)
    porcentagem_desconto = fields.IntField(null=True, default=0)
    categoria = fields.CharEnumField(Categoria)

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"
    
    def preco_calculado(self):
        if not self.porcentagem_desconto:
            return self.preco
        return float(Decimal(self.preco) * (1 - Decimal(self.porcentagem_desconto) / 100))
