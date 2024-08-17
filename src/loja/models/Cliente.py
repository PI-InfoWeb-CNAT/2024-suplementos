from django.contrib.auth.hashers import make_password

from loja.models import *
import datetime

class Cliente(models.Model):
    Nome = models.CharField(null=False, max_length=100)
    Email = models.CharField(null=False, max_length=100)
    CPF = models.CharField(null=False, max_length=11, unique=True)
    Telefone_celular = models.CharField(null=False, max_length=11)
    Telefone_fixo = models.CharField(null=True, max_length=11, blank=True)
    Dt_nasc = models.DateField(null=False, default=datetime.date(2000, 1, 1))
    Endereco = models.CharField(null=False, max_length=100)
    Estado = models.CharField(null=False, max_length=100)
    CEP = models.CharField(null=False, max_length=8)
    Senha = models.CharField(null=False, max_length=100)

    def save(self, *args, **kwargs):
        if self.pk is None or self._state.adding:
            self.Senha = make_password(self.Senha)
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.Nome}'