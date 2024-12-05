from loja.models import *
from loja.validators import numero_nao_negativo, porcentagem

class Produto(models.Model):
    CATEGORIAS = [
        ('suplementos', 'Suplementos'),
        ('alimentos', 'Alimentos'),
        ('roupas', 'Roupas'),
        ('acessorios', 'Acessórios'),
    ]
    nome = models.CharField(null=False, max_length=100)
    preco = models.FloatField(null=False, validators=[numero_nao_negativo])
    descricao = models.TextField(null=False)
    imagem = models.ImageField(null=False, blank=True, upload_to='produtos/')
    porcentagem_desconto = models.IntegerField(null=True, default=0, validators=[porcentagem])
    estoque = models.IntegerField(null=False, default=10, validators=[numero_nao_negativo])
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='suplementos')


    def __str__(self):
        return f'{self.Nome}'