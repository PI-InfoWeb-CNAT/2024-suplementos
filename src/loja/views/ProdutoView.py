from django.shortcuts import render
from django.http import HttpResponseNotFound

from loja.models import Produto

def produto_view(request, id):
    produto = Produto.objects.get(id=id)

    if not produto:
        return HttpResponseNotFound('Produto não encontrado.')
    
    context = {'produto': produto}

    return render(request, template_name='produto.html', context=context, status=200)