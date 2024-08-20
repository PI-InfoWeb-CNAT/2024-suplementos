from django.contrib.auth.hashers import make_password

from loja.models import *
import datetime

class Produto(models.Model):
    Nome = models.CharField(null=False, max_length=100)
    Preco = models.FloatField(null=False)
    Descricao = models.CharField(null=False, max_length=300)
    Dt_fabricacao = models.DateField(null=False, default=datetime.date(2000, 1, 1))
    Dt_validade = models.DateField(null=False, default=datetime.date(2000, 1, 1))

    def __str__(self):
        return f'{self.Nome}'