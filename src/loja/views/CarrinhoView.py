from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Função para adicionar um item ao carrinho
#@login_required
def create_carrinhoitem_view(request, produto_id=None):
    print ('create_carrinhoitem_view')     
    produto = get_object_or_404(Produto, pk=produto_id)
    if produto:
        print('produto: ' +  str(produto.id))

    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    print ('carrinho: ' + str(carrinho_id))
    carrinho = None
    if carrinho_id:
        # Se o carrinho já estiver na sessão, tentamos obter o carrinho
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print (carrinho)
        print ('carrinho1: ' + str(carrinho.id))
        hoje = datetime.today().date()
        # Caso queira define uma expiração do carrinho
        if carrinho.criado_em.date() != hoje:
            # Se o carrinho não for de hoje, cria um novo carrinho
            carrinho = Carrinho.objects.create()
            # Armazena o ID do carrinho na sessão
            request.session['carrinho_id'] = carrinho.id
            print ('novo carrinho: ' + str(carrinho.id))            
    else:
        # Se o carrinho não existir na sessão, cria um novo carrinho
        carrinho = Carrinho.objects.create()
        # Armazena o ID do carrinho na sessão
        request.session['carrinho_id'] = carrinho.id
        print ('carrinho2: ' + str(carrinho.id))    
    
    # Verifica se o produto já existe no carrinho do usuário
    carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()
    
    if carrinho_item:
        # Se o produto já estiver no carrinho, apenas aumenta a quantidade
        carrinho_item.quantidade += 1        
        print ('item de carrinho: Acrescentou 1 item do produto ' + str(carrinho_item.id))    
    else:
        # Se o produto não estiver no carrinho, cria um novo item no carrinho
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print ('item de carrinho: Acrescentou o produto ' + str(carrinho_item.id))    
    carrinho_item.save()
    print ('item de carrinho salvo: ' + str(carrinho_item.id))

    return redirect('/carrinho')

# Função para exibir os itens do carrinho
#@login_required
def list_carrinho_view(request):
    
    print ('list_carrinho_view')     
    carrinho = None
    
    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        print ('carrinho: ' + str(carrinho_id))     

        # Obtém o carrinho do usuário
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        print ('Data do carrinho' + str(carrinho.criado_em) )

        carrinho_item = None
        # Verifica se o produto já existe no carrinho do usuário
        carrinho_item = CarrinhoItem.objects.filter(carrinho_id=carrinho_id)
        if carrinho_item:
            print ('itens de carrinho encontrado: ' + str(carrinho_item))

    context = {
        'carrinho': carrinho,
        'itens': carrinho_item
    }

    return render(request, 'carrinho/carrinho-listar.html', context=context)

# Função para confirmar a compra, login obrigatorio
@login_required
def confirmar_carrinho_view(request):
    print ('confirmar_carrinho_view')     
    carrinho = None
    
    # Tenta pegar o carrinho da sessão ou cria um novo carrinho
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        print ('carrinho: ' + str(carrinho_id))     

        # Obtém o carrinho do usuário
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()

        # Obtém o usuário
        usuario = get_object_or_404(Usuario, user=request.user)

        if usuario:
            carrinho.usuario = usuario
            carrinho.situacao = 1
            carrinho.confirmado_em = datetime.today()
            carrinho.save()

    context = {
        'carrinho': carrinho
    }
    return render(request, 'carrinho/carrinho-confirmado.html', context=context)

    # Função para excluir um item do carrinho
def remover_item_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)

    # Verifica se o item pertence ao carrinho do usuário (opcional)
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        item.delete()

    return redirect('/carrinho')
    