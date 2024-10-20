from loja.models import *

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome = models.CharField(null=False, max_length=100)
    estado = models.CharField(null=False, max_length=100)
    cidade = models.CharField(null=False, max_length=100)
    rua = models.CharField(null=False, max_length=200)
    numero = models.CharField(null=False, max_length=10)
    complemento = models.CharField(null=True, max_length=200)
    telefone = models.CharField(null=True, max_length=20)
    cep = models.CharField(null=False, max_length=8)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['rua', 'numero'], name='unique_rua_numero')
        ]

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'