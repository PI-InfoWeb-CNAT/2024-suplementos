from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loja.models import Cliente, Notificacao

@login_required
def notificacoes_view(request):
    user = request.user

    notificacoes_cliente = Notificacao.objects.filter(cliente_id=user.id)

    context = {'notificacoes': notificacoes_cliente}

    return render(request, template_name='notificacoes.html', context=context, status=200)