from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Cliente, Notificacao

@login_required
def list_notificacoes_view(request):
    clientes = Cliente.objects.all()

    notificacoes_cliente = ''
    for cliente in clientes:
        if cliente.user_id == request.user.id:
            notificacoes_cliente = Notificacao.objects.filter(cliente_id=cliente.id).order_by('-data_envio')
            notificacoes_cliente.update(lida=True)

    context = {'notificacoes': notificacoes_cliente}

    return render(request, template_name='user/notificacoes.html', context=context, status=200)

@login_required
def excluir_notificacoes_view(request):
    clientes = Cliente.objects.all()

    notificacoes_cliente = ''
    for cliente in clientes:
        if cliente.user_id == request.user.id:
            notificacoes_cliente = Notificacao.objects.filter(cliente_id=cliente.id)
            
    notificacoes_cliente.delete()

    return redirect('notificacoes')