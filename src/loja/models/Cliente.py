from loja.models import *

class Cliente(models.Model):
    Nome = models.CharField(null=False, max_length=100)
    CPF = models.CharField(null=False, max_length=11, default="")
    Email = models.CharField(null=False, max_length=100, default="")
    Senha = models.CharField(null=False, max_length=100, default="")
    Dt_nasc = models.DateField(default="2000-01-01")
    Telefone_fixo = models.CharField(null=True, max_length=11, default="")
    Telefone_cel = models.CharField(null=False, max_length=11, default="")
    Estado_sigla = models.CharField(null=False, max_length=2, default="")
    CEP = models.CharField(null=False, max_length=8, default="")
    Endereco = models.CharField(null=False, max_length=100, default="")

    def __str__(self):
        return f'{self.Nome}'