from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from loja.models import Lote, Produto

def list_lotes_view(request):
    lotes = Lote.objects.all().order_by('-id')
    produtos = Produto.objects.all()

    context = {
        'lotes': lotes,
        'produtos': produtos
    }

    return render(request, template_name='admin/lotes.html', context=context, status=200)

def criar_lote_view(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade = request.POST.get('qtd')
        data_validade = request.POST.get('data')

        if produto_id and quantidade and data_validade:
            data_validade_formatada = timezone.datetime.strptime(data_validade, "%Y-%m-%d").date()
            if int(quantidade) <= 0:
                messages.error(request, 'A quantidade deve ser maior que 0!', extra_tags='criar-lote')
            elif data_validade_formatada < timezone.now().date():
                messages.error(request, 'A data de validade deve ser maior ou igual a hoje!', extra_tags='criar-lote')
            else:
                Lote.objects.create(produto_id=produto_id, quantidade=quantidade, data_validade=data_validade)
                messages.success(request, 'Lote criado com sucesso!', extra_tags='criar-lote')
        else:
            messages.error(request, 'Preencha todos os campos!', extra_tags='criar-lote')
            
    return redirect('lotes')

def edit_lote_view(request):
    if request.method == 'POST':
        lote_id = request.POST.get('lote_id')
        produto_id = request.POST.get('produto_id')
        quantidade = request.POST.get('qtd')
        data_validade = request.POST.get('data')

        lote = Lote.objects.get(id=lote_id)

        if lote.produto_id == produto_id and lote.quantidade == quantidade and lote.data_validade == data_validade:
            messages.error(request, 'Altere algum dado para atualizar!', extra_tags='editar-lote')
        else:
            data_validade_formatada = timezone.datetime.strptime(data_validade, "%Y-%m-%d").date()
            if int(quantidade) <= 0:
                messages.error(request, 'A quantidade deve ser maior que 0!', extra_tags='editar-lote')
            elif data_validade_formatada < timezone.now().date():
                messages.error(request, 'A data de validade deve ser maior ou igual a hoje!', extra_tags='editar-lote')
            else:
                lote.produto_id = produto_id
                lote.quantidade = quantidade
                lote.data_validade = data_validade
                lote.save()
                messages.success(request, 'Lote atualizado com sucesso!', extra_tags='editar-lote')

    return redirect(request.META.get('HTTP_REFERER', reverse('lotes')))

def excluir_lote_view(request):
    if request.method == 'POST':
        lote_id = request.POST.get('lote_id')

        lote = Lote.objects.get(id=lote_id)
        lote.delete()
        messages.success(request, 'Lote excluído com sucesso!', extra_tags='page-lotes')

    return redirect(request.META.get('HTTP_REFERER', reverse('lotes')))