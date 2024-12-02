from django.shortcuts import render
from loja.models import Produto

def promocoes_view(request):
    produtos = Produto.objects.all()

    produtos_promocoes = []
    for prod in produtos:
        if prod.Promocao != 0:
            produtos_promocoes.append(prod)


    context = {'produtos_promocoes': produtos_promocoes}
    return render(request, template_name='promocoes.html', context=context, status=200)