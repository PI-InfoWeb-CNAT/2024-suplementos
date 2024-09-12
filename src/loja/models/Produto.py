from loja.models import *
import datetime

class Produto(models.Model):
    nome = models.CharField(null=False, max_length=100)
    preco = models.FloatField(null=False)
    descricao = models.CharField(null=False, max_length=300)
    dt_fabricacao = models.DateField(null=False, default=datetime.date(2000, 1, 1))
    dt_validade = models.DateField(null=False, default=datetime.date(2000, 1, 1))
    imagem = models.ImageField(null=True, blank=True, upload_to='produtos/')
    promocao = models.IntegerField(null=True, default=0)
    favorito = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f'{self.nome}'