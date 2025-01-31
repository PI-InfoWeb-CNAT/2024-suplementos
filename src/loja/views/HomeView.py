from django.db.models import Sum
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
    
    produtos_mais_vendidos = Produto.objects.annotate(total_vendas=Sum('pedidos__quantidade')).order_by('-total_vendas')[:5]

    context = {
        'produtos_pesquisa': produtos_pesquisa,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'produtos_promocoes': produtos_promocoes,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        produtos_html = render_to_string('user/produtos_pesquisados.html',{'produtos_pesquisa': produtos_pesquisa}, request=request )
        return HttpResponse(produtos_html)

    if request.user.is_staff:
        return render(request, template_name='admin/home.html', status=200)
    else:
        return render(request, template_name='user/home.html', context=context, status=200)