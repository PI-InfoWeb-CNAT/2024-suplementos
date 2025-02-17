from django.db.models import Sum
from django.http import HttpResponse
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.template.loader import render_to_string

from loja.models import Produto, Lote
from loja.utils import aplicar_promocao_auto

def home_view(request):
    aplicar_promocao_auto()

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

    context_user = {
        'produtos_pesquisa': produtos_pesquisa,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'produtos_promocoes': produtos_promocoes,
    }

    data_limite = timezone.now() + timedelta(days=30)

    lotes_proximos_validade = Lote.objects.filter(data_validade__gte=timezone.now(), data_validade__lte=data_limite).order_by('data_validade')
    lotes_vencidos = Lote.objects.filter(data_validade__lt=timezone.now().date())

    for lote in lotes_vencidos:
        lote.dias_vencidos = (timezone.now().date() - lote.data_validade).days
    for lote in lotes_proximos_validade:
        lote.dias_para_vencer = (lote.data_validade - timezone.now().date()).days

    context_admin = {
        'lotes_vencidos': lotes_vencidos,
        'lotes_proximos_validade': lotes_proximos_validade,
        'produtos': produtos
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        produtos_html = render_to_string('user/produtos_pesquisados.html',{'produtos_pesquisa': produtos_pesquisa}, request=request)
        return HttpResponse(produtos_html)

    if request.user.is_staff:
        return render(request, template_name='admin/home.html', context=context_admin, status=200)
    else:
        return render(request, template_name='user/home.html', context=context_user, status=200)