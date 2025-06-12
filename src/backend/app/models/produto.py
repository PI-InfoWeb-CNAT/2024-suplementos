from tortoise import fields, models

class Produto(models.Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=255)
    descricao = fields.TextField(null=True)
    preco = fields.DecimalField(max_digits=10, decimal_places=2)
