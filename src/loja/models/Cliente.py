from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    PERFIL = [
        ('admin', 'Admin'),
        ('user', 'Usuário')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    perfil = models.CharField(null=False, max_length=10, choices=PERFIL, default='user')
    nome = models.CharField(null=False, max_length=100)
    cpf = models.CharField(null=False, max_length=15, unique=True)
    telefone_celular = models.CharField(null=False, max_length=15)

    def __str__(self):
        return f'{self.nome}'

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)
