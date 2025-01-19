from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseNotFound

from loja.models import Produto

def produto_view(request, id):
    produto = get_object_or_404(Produto, id=id)
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