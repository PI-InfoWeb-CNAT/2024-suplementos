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
    enviar_para_todos = models.BooleanField(default=False)

    def clean(self):
        if not self.enviar_para_todos and not self.cliente:
            raise ValidationError("Selecione um cliente ou marque 'Enviar para todos'.")
        if self.enviar_para_todos and self.cliente:
            raise ValidationError("Não é permitido selecionar um cliente e marcar 'Enviar para todos'.")

    def save(self, *args, **kwargs):
        if self.enviar_para_todos:
            clientes = Cliente.objects.all()
            for cliente in clientes:
                Notificacao.objects.create(
                    cliente=cliente,
                    categoria=self.categoria,
                    titulo=self.titulo,
                    texto=self.texto,
                    lida=False,
                )
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        if self.enviar_para_todos:
            return f'{self.titulo} - Enviado para todos os clientes'
        return f'{self.titulo} - {self.cliente}'