from django.db.models import Sum
from django.shortcuts import render

from loja.models import Produto

def maisvendidos_view(request):
    produtos_mais_vendidos = (Produto.objects.annotate(total_vendas=Sum('pedidos__quantidade')).filter(total_vendas__gt=0).order_by('-total_vendas')[:15])

    context = {'produtos_mais_vendidos': produtos_mais_vendidos}
    
    return render(request, template_name='user/maisvendidos.html', context=context, status=200)
