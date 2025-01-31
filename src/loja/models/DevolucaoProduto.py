from loja.models import *

class DevolucaoProduto(models.Model):
    STATUS = [
        ('1', 'em análise'),
        ('2', 'aprovado'),
        ('3', 'reprovado'),
    ]

    produto = models.ForeignKey(Produto, related_name='devolucoes', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='devolucoes', on_delete=models.CASCADE)
    motivo = models.TextField()
    foto_video = models.FileField(upload_to='devolucoes/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS)
    data_devolucao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.produto.nome} - {self.motivo}'