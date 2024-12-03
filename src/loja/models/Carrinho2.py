from .Produto import Produto
from django.db import models
from django.contrib.auth.models import User
import datetime

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrinho {self.id} - {self.user.username if self.user else "Visitante"}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.Nome}'

    def subtotal(self):
        return self.quantidade * self.produto.Preco
