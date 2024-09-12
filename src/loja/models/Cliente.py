from django.contrib.auth.hashers import make_password

from loja.models import *
import datetime

class Cliente(models.Model):
    nome = models.CharField(null=False, max_length=100)
    email = models.CharField(null=False, max_length=100)
    cpf = models.CharField(null=False, max_length=11, unique=True)
    telefone_celular = models.CharField(null=False, max_length=11)
    telefone_fixo = models.CharField(null=True, max_length=11, blank=True)
    dt_nasc = models.DateField(null=False, default=datetime.date(2000, 1, 1))
    senha = models.CharField(null=False, max_length=100)

    def save(self, *args, **kwargs):
        if self.pk is None or self._state.adding:
            self.Senha = make_password(self.Senha)
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome}'