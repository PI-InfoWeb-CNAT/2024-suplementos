from django.shortcuts import render, redirect
from datetime import datetime

from loja.models import Produto, Carrinho
from loja.models.Carrinho import CarrinhoItem

def adicionar_ao_carrinho(request, idProduto):
    produto = Produto.objects.get(id=idProduto)
    if request.method == 'POST':
        quantidade = request.POST.get('qtd_produto')

    carrinho_id = request.session.get('carrinho_id')
    carrinho = None

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        hoje = datetime.today().date()
        if carrinho.criado_em.date() != hoje:
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
    else:
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id

    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()

    if carrinho_item:
        carrinho_item.quantidade += quantidade
    else:
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=quantidade,
            preco=produto.preco
            )

    carrinho_item.save()

    return render(request, template_name='user/home.html', status=200)