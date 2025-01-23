from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from loja.models import Pedido

@login_required
def meuspedidos_view(request):
    pedidos = Pedido.objects.filter(user=request.user)

    pedidos_produto_destaque = []
    for pedido in pedidos:
        produto_destaque = pedido.itens.order_by('-quantidade').first()
        
        pedidos_produto_destaque.append({
            'pedido': pedido,
            'imagem': produto_destaque.imagem
        })
    
    context = {'pedidos': pedidos_produto_destaque}

    return render(request, template_name='user/meuspedidos.html', context=context, status=200)