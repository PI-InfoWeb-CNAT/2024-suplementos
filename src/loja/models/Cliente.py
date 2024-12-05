from loja.models import *

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    nome = models.CharField(null=False, max_length=100)
    cpf = models.CharField(null=False, max_length=11, unique=True)
    telefone_celular = models.CharField(null=False, max_length=11)

    def __str__(self):
        return f'{self.nome}'