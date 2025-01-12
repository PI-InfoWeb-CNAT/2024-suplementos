from django.shortcuts import render
from django.http import HttpResponseNotFound

from loja.models import Produto

def produto_view(request, id):
    produto = Produto.objects.get(id=id)
    produtos_relacionados = Produto.objects.filter(categoria=produto.categoria).exclude(id=produto.id)
    produtos_relacionados = produtos_relacionados[:5]

    if not produto:
        return HttpResponseNotFound('Produto não encontrado.')
    
    
    context = {
        'produto': produto,
        'produtos_relacionados': produtos_relacionados
    }

    return render(request, template_name='user/produto.html', context=context, status=200)

def produtosAdmin_view(request):
    produtos = Produto.objects.all()

    context = {'produtos': produtos}

    return render(request, template_name='admin/produtos.html', context=context, status=200)