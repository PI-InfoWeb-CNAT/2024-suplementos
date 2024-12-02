from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from loja.models import Carrinho, ItemCarrinho, Produto

# Função que lida com o carrinho de usuários logados e visitantes
def carrinho_view(request):
    if request.user.is_authenticated:
        # Carrinho para usuário logado
        carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    else:
        # Carrinho para visitante
        carrinho_id = request.session.get('carrinho_id')
        if carrinho_id:
            # Recupera o carrinho de visitante baseado no ID da sessão
            carrinho = get_object_or_404(Carrinho, id=carrinho_id, user=None)
        else:
            # Cria um carrinho para o visitante se não houver
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id  # Salva o ID do carrinho na sessão

    # Obtém os itens do carrinho
    itens = carrinho.itens.all()

    for item in itens:
        item.subtotal_value = item.subtotal()

    total = sum(item.subtotal() for item in itens)

    context = {
        'carrinho': carrinho,
        'itens': itens,
        'total': total,
    }

    return render(request, 'carrinho.html', context)


def adicionarcarrinho_view(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id') 
        produto = get_object_or_404(Produto, id=produto_id) 

        if request.user.is_authenticated:
            # Carrinho para usuário logado
            carrinho, created = Carrinho.objects.get_or_create(user=request.user)
        else:
            # Carrinho para visitante
            carrinho_id = request.session.get('carrinho_id')
            if carrinho_id:
                carrinho = get_object_or_404(Carrinho, id=carrinho_id, user=None)
            else:
                carrinho = Carrinho.objects.create()  
                request.session['carrinho_id'] = carrinho.id 

  
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, produto=produto).first()

        if item_carrinho:
          
            item_carrinho.quantidade += 1
            item_carrinho.save()
        else:
       
            ItemCarrinho.objects.create(carrinho=carrinho, produto=produto, quantidade=1)

        return JsonResponse({'message': 'Produto adicionado ao carrinho!'})
