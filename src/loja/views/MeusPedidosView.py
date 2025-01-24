from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

@login_required
def cancelar_pedido_view(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        pedido = Pedido.objects.get(id=pedido_id)

        pedido.delete()
        messages.success(request, 'Pedido cancelado com sucesso!', extra_tags='page-meuspedidos')

    return redirect(reverse('meus-pedidos'))