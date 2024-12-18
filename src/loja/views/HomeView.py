from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from loja.models import Produto

def home_view(request):
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    produtos_pesquisa = produtos

    produtos_promocoes = []
    descontos = []

    for prod in produtos:
        if prod.porcentagem_desconto != 0:
            produtos_promocoes.append(prod)
    produtos_promocoes = sorted(produtos_promocoes, key=lambda p: p.porcentagem_desconto, reverse=True)

    for promocao in produtos_promocoes:
        descontos.append(promocao.porcentagem_desconto)

    if produto is not None:
        produtos_pesquisa = produtos.filter(nome__contains=produto)

    context = {
        'produtos_pesquisa': produtos_pesquisa,
        'produtos': produtos,
        'produtos_promocoes': produtos_promocoes,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        produtos_html = render_to_string('produtos_pesquisados.html',{'produtos_pesquisa': produtos_pesquisa}, request=request )
        return HttpResponse(produtos_html)

    return render(request, template_name='home.html', context=context, status=200)
