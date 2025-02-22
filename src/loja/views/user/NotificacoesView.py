from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Cliente, Notificacao

@login_required
def list_notificacoes_view(request):
    cliente = Cliente.objects.get(id=request.user.id)

    notificacoes_cliente = Notificacao.objects.filter(cliente=cliente)

    context = {'notificacoes': notificacoes_cliente}

    return render(request, template_name='user/notificacoes.html', context=context, status=200)

@login_required
def excluir_notificacoes_view(request):
    cliente = Cliente.objects.get(id=request.user.id)

    notificacoes_cliente = Notificacao.objects.filter(cliente=cliente)
            
    notificacoes_cliente.delete()

    return redirect('notificacoes')