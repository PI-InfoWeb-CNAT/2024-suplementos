from loja.models import *

class Carrinho(models.Model):
    user = models.ForeignKey(User, null=True, related_name='carrinhos', on_delete=models.SET_NULL)
    criado_em = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.quantidade * item.preco for item in self.itens.all())
    
    def __str__(self):
        return f'{self.criado_em}'
    
class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(Carrinho, null=True, related_name='itens', on_delete=models.SET_NULL)
    produto = models.ForeignKey(Produto, null=True, related_name='carrinhos', on_delete=models.SET_NULL)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def total(self):
        return self.quantidade * self.preco
    
    def __str__(self):
        return f'{self.produto}'