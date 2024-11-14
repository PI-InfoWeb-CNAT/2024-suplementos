from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loja.models import Cliente, Notificacao

@login_required
def notificacoes_view(request):
    user = request.user
    clientes = Cliente.objects.all()
    notificacoes = Notificacao.objects.all()

    notificacoes_cliente = ''

    for cliente in clientes:
        if cliente.user_id == user.id:
            notificacoes_cliente = notificacoes.filter(cliente_id=cliente.id)

    context = {'notificacoes': notificacoes_cliente}

    return render(request, template_name='notificacoes.html', context=context, status=200)