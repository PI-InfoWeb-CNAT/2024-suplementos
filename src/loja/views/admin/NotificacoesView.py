from django.shortcuts import render, redirect
from django.contrib import messages

from loja.models import Notificacao, Cliente

def list_notificacoesAdmin_view(request):
    notificacoes = Notificacao.objects.all().order_by('-data_envio')
    clientes = Cliente.objects.all()

    categorias = [
        ('status_pedido', 'Status do pedido'),
        ('status_devolucao', 'Status da devolução'),
        ('mensagem_personalizada', 'Mensagem Personalizada'),
    ]

    context = {
        'notificacoes': notificacoes,
        'clientes': clientes,
        'categorias': categorias,
    }

    return render(request, 'admin/notificacoes.html', context=context, status=200)

def criar_notificacao_view(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        categoria = request.POST.get('categoria')
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        enviar_para_todos = request.POST.get('enviar_todos') 

        if not categoria or not titulo or not texto:
            messages.error(request, 'Preencha os campos obrigatórios (*)!', extra_tags='criar-notificacao')
        elif cliente_id and enviar_para_todos:
                messages.error(request, 'Você deve escolher um cliente OU enviar para todos!', extra_tags='criar-notificacao')
        elif not cliente_id and not enviar_para_todos:
            messages.error(request, 'Selecione um cliente ou envie para todos!', extra_tags='criar-notificacao')
        else:
            if cliente_id:
                cliente = Cliente.objects.get(id=cliente_id)
                Notificacao.objects.create(
                    cliente=cliente,
                    categoria=categoria,
                    titulo=titulo,
                    texto=texto
                )
                messages.success(request, 'Notificação adicionada com sucesso!', extra_tags='criar-notificacao')
            else:
                clientes = Cliente.objects.all()
                for cliente in clientes:
                    Notificacao.objects.create(
                    cliente=cliente,
                    categoria=categoria,
                    titulo=titulo,
                    texto=texto
                )
                messages.success(request, 'Notificações adicionadas com sucesso!', extra_tags='criar-notificacao')

    return redirect('notificacoes-admin')

def edit_notificacao_view(request):
    if request.method == 'POST':
        notificacao_id = request.POST.get('notificacao_id')
        cliente_id = request.POST.get('cliente_id')
        categoria = request.POST.get('categoria')
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')

        notificacao = Notificacao.objects.get(id=notificacao_id)
        cliente = Cliente.objects.get(id=cliente_id)

        if notificacao.cliente == cliente and notificacao.categoria == categoria and notificacao.titulo == titulo and notificacao.texto == texto:
            messages.error(request, 'Altere algum dado para atualizar!', extra_tags='editar-notificacao')
        else:
            notificacao.cliente = cliente
            notificacao.categoria = categoria
            notificacao.titulo = titulo
            notificacao.texto = texto
            notificacao.save()

            messages.success(request, 'Notificação atualizada com sucesso!', extra_tags='editar-notificacao')

    return redirect('notificacoes-admin')

def excluir_notificacao_view(request):
    if request.method == 'POST':
        notificacao_id = request.POST.get('notificacao_id')

        notificacao = Notificacao.objects.get(id=notificacao_id)
        notificacao.delete()
        messages.success(request, 'Notificação excluída com sucesso!', extra_tags='page-notificacoesadmin')

    return redirect('notificacoes-admin')