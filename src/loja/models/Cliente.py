from loja.models import *
import datetime

class Cliente(models.Model):
    Nome = models.CharField(null=False, max_length=100)
    email = models.CharField(null=False, max_length=100)
    CPF = models.CharField(null=False, max_length=11)
    Telefone_celular = models.CharField(null=False, max_length=11)
    Telefone_fixo = models.CharField(null=True, max_length=11, blank=True)
    Dt_nasc = models.DateField(null=False, default=datetime.date(2000, 1, 1))
    Endereco = models.CharField(null=False, max_length=100)
    Estado = models.CharField(null=False, max_length=100)
    CEP = models.CharField(null=False, max_length=8)
    senha = models.CharField(null=False, max_length=100)

    def __str__(self):
        return f'{self.Nome}'