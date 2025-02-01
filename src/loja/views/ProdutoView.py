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

def produtosAdmin_view(request):
    produtos = Produto.objects.all()

    categorias = [
        ('acessorios', 'Acessórios'),
        ('alimentos', 'Alimentos'),
        ('roupas', 'Roupas'),
        ('suplementos', 'Suplementos'),
    ]

    context = {
        'produtos': produtos,
        'categorias': categorias
    }

    return render(request, template_name='admin/produtos.html', context=context, status=200)

def excluir_produto_view(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')

        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!', extra_tags='page-produtos')

    return redirect(reverse('produtos'))