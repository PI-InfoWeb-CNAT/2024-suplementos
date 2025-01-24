from loja.models import *

class Pedido(models.Model):
    STATUS = [
        ('1', 'Processando'),
        ('2', 'Enviado'),
        ('3', 'Entregue'),
        ('4', 'Recebido')
    ]

    user = models.ForeignKey(User, null=True, related_name='pedidos', on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, null=True, related_name='pedidos', on_delete=models.CASCADE)
    cartao = models.ForeignKey(Cartao, null=True, related_name='pedidos', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS)
    dt_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.total} - {self.dt_hora}'
    
class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='pedidos', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.produto} - {self.quantidade}'