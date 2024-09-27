from django.contrib.auth.hashers import make_password

from loja.models import *

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    Nome = models.CharField(null=False, max_length=100)
    CPF = models.CharField(null=False, max_length=11, unique=True)
    Telefone_celular = models.CharField(null=False, max_length=11)
    Telefone_fixo = models.CharField(null=True, max_length=11, blank=True)

    def __str__(self):
        return f'{self.Nome}'