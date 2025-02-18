from django.shortcuts import render, redirect
from django.contrib import messages

from loja.models import DevolucaoProduto

def list_devolucoes_view(request):
    devolucoes = DevolucaoProduto.objects.all()

    status = [
        ('1', 'em análise'),
        ('2', 'aprovado'),
        ('3', 'reprovado'),
    ]

    context = {
        'devolucoes': devolucoes,
        'todos_status': status
    }

    return render(request, 'admin/devolucoes.html', context=context, status=200)

def edit_devolucao_view(request):
    if request.method == 'POST':
        devolucao_id = request.POST.get('devolucao_id')
        status = request.POST.get('status')

        devolucao = DevolucaoProduto.objects.get(id=devolucao_id)

        if devolucao.status == status:
            messages.error(request, 'Altere o status da devolução para atualizar!', extra_tags='editar-devolucao')
        else:
            devolucao.status = status
            devolucao.save()

            messages.success(request, 'Status da devolução alterado com sucesso!', extra_tags='editar-devolucao')

    return redirect('devolucoes')

def excluir_devolucao_view(request):
    if request.method == 'POST':
        devolucao_id = request.POST.get('devolucao_id')

        devolucao = DevolucaoProduto.objects.get(id=devolucao_id)
        devolucao.delete()
        messages.success(request, 'Devolução excluída com sucesso!', extra_tags='page-devolucoes')

    return redirect('devolucoes')