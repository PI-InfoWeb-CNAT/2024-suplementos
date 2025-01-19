from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from loja.models import Produto, Carrinho
from loja.models.Carrinho import CarrinhoItem

def adicionar_ao_carrinho(request, idProduto):
    produto = get_object_or_404(Produto, id=idProduto)
    
    if request.method == 'POST':
        quantidade = request.POST.get('qtd_produto')
        if quantidade == '':
            messages.error(request, 'Defina uma quantidade para adicionar o produto ao carrinho', extra_tags='page-produto')
            return render(request, 'user/produto.html', {'produto': produto}, status=200)
        else:
            quantidade = int(quantidade)
    
    estoque_disponivel = produto.calcular_estoque()
    if quantidade == 0:
        messages.error(request, 'A quantidade deve ser maior que 0', extra_tags='page-produto')
        return render(request, 'user/produto.html', {'produto': produto}, status=200)
    elif quantidade > estoque_disponivel:
        messages.error(request, 'A quantidade não pode ultrapassar o estoque disponível', extra_tags='page-produto')
        return render(request, 'user/produto.html', {'produto': produto}, status=200)
    
    carrinho = None
    hoje = datetime.today().date()

    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key

        carrinho = Carrinho.objects.filter(session_key=session_key).first()

        if not carrinho or carrinho.criado_em.date() != hoje:
            carrinho = Carrinho.objects.create(session_key=session_key)
            request.session['carrinho_id'] = carrinho.id

    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()
    if carrinho_item:
        if carrinho_item.quantidade + quantidade > estoque_disponivel:
            messages.error(request, f'Você já tem {carrinho_item.quantidade} desse produto no carrinho. Não ultrapasse o estoque disponível.', extra_tags='page-produto')
            return render(request, 'user/produto.html', {'produto': produto}, status=200)
        else:
            carrinho_item.quantidade += quantidade
    else:
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=quantidade,
            preco=produto.preco_calculado(),
            imagem=produto.imagem.url
        )
    
    carrinho_item.save()
    messages.success(request, 'Produto adicionado com sucesso', extra_tags='page-produto')

    excluir_carrinhos_expirados()

    return render(request, 'user/produto.html', {'produto': produto}, status=200)

def excluir_carrinhos_expirados():
    limite = datetime.now() - timedelta(days=1)
    Carrinho.objects.filter(user__isnull=True, criado_em__lt=limite).delete()

def listar_carrinho_view(request):
    carrinho_itens = [] 

    carrinho = None

    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        if session_key:
            carrinho = Carrinho.objects.filter(session_key=session_key).first()

    if carrinho:
        carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho)

    context = {
        'carrinho_itens': carrinho_itens,
        'total': carrinho.total
    }

    return render(request, 'user/carrinho.html', context=context, status=200)

def remover_item_view(request, idItem):
    item = get_object_or_404(CarrinhoItem, id=idItem)
    
    if request.user.is_authenticated:
        if item.carrinho.user == request.user:
            item.delete()
    else:
        carrinho_id = request.session.get('carrinho_id')
        print(carrinho_id, item.carrinho.id)
        if carrinho_id == item.carrinho.id:
            item.delete()

    return redirect(reverse('carrinho'))