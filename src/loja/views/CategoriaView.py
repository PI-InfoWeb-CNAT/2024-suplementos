from django.shortcuts import render, redirect

from loja.models import Produto

def categoria_view(request, categoria):
    produtos_categoria = Produto.objects.filter(categoria=categoria)

    categorias_dict = dict(Produto.CATEGORIAS) 
    categoria_formatada = categorias_dict.get(categoria, categoria)

    context = {
        'categoria': categoria_formatada,
        'produtos_categoria': produtos_categoria
    }

    return render(request, template_name='categoria.html', context=context, status=200)