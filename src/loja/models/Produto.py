from loja.models import *
from loja.validators import numero_nao_negativo, porcentagem
import datetime

class Produto(models.Model):
    CATEGORIAS = [
        ('suplementos', 'Suplementos'),
        ('alimentos', 'Alimentos'),
        ('roupas', 'Roupas'),
        ('acessorios', 'Acessórios'),
    ]
    Nome = models.CharField(null=False, max_length=100)
    Preco = models.FloatField(null=False, validators=[numero_nao_negativo])
    Descricao = models.TextField(null=False)
    Imagem = models.ImageField(null=False, blank=True, upload_to='produtos/')
    Porcentagem_desconto = models.IntegerField(null=True, default=0, validators=[porcentagem])
    Estoque = models.IntegerField(null=False, default=10, validators=[numero_nao_negativo])
    Categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='suplementos')


    def __str__(self):
        return f'{self.Nome}'