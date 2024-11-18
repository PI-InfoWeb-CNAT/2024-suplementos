from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loja.models import Cliente, Notificacao

@login_required
def list_notificacoes_view(request):
    user = request.user
    clientes = Cliente.objects.all()

    notificacoes_cliente = ''
    for cliente in clientes:
        if cliente.user_id == user.id:
            notificacoes_cliente = Notificacao.objects.filter(cliente_id=cliente.id)
            notificacoes_cliente.update(lida=True)
    print(notificacoes_cliente)

    context = {'notificacoes': notificacoes_cliente}

    return render(request, template_name='notificacoes.html', context=context, status=200)

@login_required
def excluir_notificacoes_view(request):
    user = request.user

    notificacoes_cliente = Notificacao.objects.filter(cliente_id=user.id)
    notificacoes_cliente.delete()

    return render(request, template_name='notificacoes.html', status=200)