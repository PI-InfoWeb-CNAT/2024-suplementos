from loja.models import *

class AvaliacaoProduto(models.Model):
    nota = models.PositiveIntegerField()
    cliente = models.ForeignKey(Cliente, related_name='avaliacoes', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='avaliacoes',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cliente} - {self.produto} - {self.nota}'