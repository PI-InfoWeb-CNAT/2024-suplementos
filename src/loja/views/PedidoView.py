from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from loja.models import Cliente, Carrinho, CarrinhoItem

@login_required
def finalizar_pedido_view(request):
    cliente = Cliente.objects.get(user=request.user)
    enderecos = cliente.enderecos.all()
    cartoes = cliente.cartoes.all()
    
    carrinho = Carrinho.objects.filter(user=request.user).first()
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho)
    

    context = {
        'enderecos': enderecos,
        'cartoes': cartoes,
        'produtos': carrinho_itens
    }

    return render(request, template_name='user/finalizar_pedido.html', context=context, status=200) 