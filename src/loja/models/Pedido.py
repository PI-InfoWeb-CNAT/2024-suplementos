from loja.models import *

class Pedido(models.Model):
    total = models.DecimalField(max_digits=8, decimal_places=2)
    dt_hora = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, related_name='pedidos', on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, null=True, related_name='pedidos', on_delete=models.CASCADE)
    cartao = models.ForeignKey(Cartao, null=True, related_name='pedidos', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.dt_hora}'
