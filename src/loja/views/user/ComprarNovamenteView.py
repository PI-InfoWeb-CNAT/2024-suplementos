from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from loja.models import Produto

@login_required
def comprar_novamente_view(request):
    user = request.user

    produtos_comprados = []

    if user.pedidos.all():
        for pedido in user.pedidos.all():
            for item in pedido.itens.all():
                if item not in produtos_comprados:
                    produtos_comprados.append(item.produto)

    context = {'produtos_comprados': produtos_comprados}

    return render(request, template_name='user/comprar_novamente.html', context=context, status=200)