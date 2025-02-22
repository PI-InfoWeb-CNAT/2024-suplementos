from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from loja.models import Favorito, Cliente, Produto

@login_required
def favorito_view(request):
    cliente = Cliente.objects.get(user=request.user)

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        
        produto = Produto.objects.get(id=produto_id)
        favorito_cliente = Favorito.objects.filter(cliente=request.user.cliente, produto=produto_id)
        
        if not favorito_cliente:
            Favorito.objects.create(cliente=cliente, produto=produto)
        else:
            favorito_cliente.delete()
        return redirect('meus-favoritos')
        
    return redirect('meus-favoritos')