from django.core.exceptions import ValidationError
from loja.models import *

class Notificacao(models.Model):
    CATEGORIAS = [
        ('status_pedido', 'Status do pedido'),
        ('status_devolucao', 'Status da devolução'),
        ('mensagem_personalizada', 'Mensagem Personalizada'),
    ]

    cliente = models.ForeignKey(Cliente, related_name='notificacoes', on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    titulo = models.CharField(null=False, max_length=100)
    texto = models.TextField(null=False)
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.titulo} - {self.cliente}'