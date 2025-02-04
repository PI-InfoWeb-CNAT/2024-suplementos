from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages


from loja.models import Cliente, Produto, AvaliacaoProduto

def avaliar_produto_view(request):
    cliente = Cliente.objects.get(user=request.user)

    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        nota = request.POST.get('nota')
        nota = int(nota)
        
        produto = Produto.objects.get(id=produto_id)
        avaliado = AvaliacaoProduto.objects.filter(cliente=request.user.cliente, produto=produto_id).first()

        if avaliado:
            avaliado.nota = nota
            avaliado.save()
        else:
            AvaliacaoProduto.objects.create(nota=nota, cliente=cliente, produto=produto)
        
        messages.success(request, 'Produto avaliado com sucesso!', extra_tags='page-meuspedidos')

    return redirect('meus-pedidos')