from loja.models import *
from loja.validators import *

class Lote(models.Model):
    produto = models.ForeignKey(Produto, related_name='lotes', on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, validators=[numero_positivo])
    data_validade = models.DateField(null=False, validators=[data_futura])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.produto.estoque = self.produto.calcular_estoque()
        self.produto.save()

    def delete(self, *args, **kwargs):
        produto = self.produto
        super().delete(*args, **kwargs)
        produto.estoque = produto.calcular_estoque()
        produto.save()

    def __str__(self):
        return f'{self.produto} - {self.data_validade} - {self.quantidade}'