from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Count, Avg
from django.http import HttpResponseNotFound
from django.contrib import messages

from loja.models import Produto, AvaliacaoProduto

def produto_view(request, id):
    produto = get_object_or_404(Produto, id=id)
    produtos_relacionados = Produto.objects.filter(categoria=produto.categoria).exclude(id=produto.id)
    produtos_relacionados = produtos_relacionados[:5]

    total_avaliacoes = produto.avaliacoes.count()
    media_avaliacoes = produto.avaliacoes.aggregate(media=Avg('nota'))['media'] or 0

    nota_1 = AvaliacaoProduto.objects.filter(produto=produto, nota=1).count()
    nota_2 = AvaliacaoProduto.objects.filter(produto=produto, nota=2).count()
    nota_3 = AvaliacaoProduto.objects.filter(produto=produto, nota=3).count()
    nota_4 = AvaliacaoProduto.objects.filter(produto=produto, nota=4).count()
    nota_5 = AvaliacaoProduto.objects.filter(produto=produto, nota=5).count()
    
    context = {
        'produto': produto,
        'produtos_relacionados': produtos_relacionados,
        'total_avaliacoes': total_avaliacoes,
        'media_avaliacoes': round(media_avaliacoes, 1),
        'nota_5': nota_5,
        'nota_4': nota_4,
        'nota_3': nota_3,
        'nota_2': nota_2,
        'nota_1': nota_1
    }

    return render(request, template_name='user/produto.html', context=context, status=200)