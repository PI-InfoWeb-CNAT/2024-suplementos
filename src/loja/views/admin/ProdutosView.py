from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from loja.models import Produto

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