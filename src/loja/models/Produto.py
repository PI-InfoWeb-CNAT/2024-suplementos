from loja.models import *
from loja.validators import *

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
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='suplementos')

    def calcular_estoque(self):
        return sum(lote.quantidade for lote in self.lote_set.all())

    def __str__(self):
        return f'{self.nome}'