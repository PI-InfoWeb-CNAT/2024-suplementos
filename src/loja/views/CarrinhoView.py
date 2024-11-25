from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from loja.models import Carrinho, ItemCarrinho

@login_required
def carrinho_view(request):
    # Obtém ou cria o carrinho do usuário autenticado
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)

    # Obtém todos os itens do carrinho
    itens = carrinho.itens.all()

    # Calcula o total do carrinho
    total = sum(item.subtotal() for item in itens)

    # Contexto para o template
    context = {
        'carrinho': carrinho,
        'itens': itens,
        'total': total,
    }

    return render(request, 'home.html', context)
