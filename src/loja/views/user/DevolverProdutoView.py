from django.shortcuts import render, redirect
from django.contrib import messages

from loja.models import Cliente, Produto, DevolucaoProduto, Notificacao

def devolver_produto_view(request):
    cliente = Cliente.objects.get(user=request.user)

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        motivo = request.POST.get('motivo')
        foto_video = request.FILES.get('foto_video')

        produto = Produto.objects.get(id=produto_id)

        devolucao_existente = DevolucaoProduto.objects.filter(produto=produto, cliente=cliente).exists()

        if devolucao_existente:
            messages.error(request, 'Você já solicitou a devolução deste produto.', extra_tags='page-meuspedidos')
        elif motivo:
            DevolucaoProduto.objects.create(produto=produto, cliente=cliente, motivo=motivo, foto_video=foto_video, status='1')
            Notificacao.objects.create(
                cliente=cliente,
                categoria='status_devolucao',
                titulo='Devolução em análise',
                texto=f'Sua solicitação de devolução do produto {produto.nome} foi registrada e está em análise.',
            )

            messages.success(request, 'Solicitação de devolução enviada com sucesso!', extra_tags='page-meuspedidos')
        else:
            messages.error(request, 'Preencha o motivo da devolução!', extra_tags='page-meuspedidos')

    return redirect('meus-pedidos')
