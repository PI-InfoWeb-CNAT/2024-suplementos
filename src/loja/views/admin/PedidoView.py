from django.shortcuts import render, redirect
from django.contrib import messages

from loja.models import Pedido, Notificacao, Cliente

def list_pedidos_view(request):
    pedidos = Pedido.objects.all().order_by('-dt_hora')

    status = [
        ('1', 'Processando'),
        ('2', 'Enviado'),
        ('3', 'Entregue'),
        ('4', 'Recebido'),
    ]

    context = {
        'pedidos': pedidos,
        'todos_status': status
    }

    return render(request, template_name='admin/pedidos.html', context=context, status=200)

def edit_pedido_view(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        status = request.POST.get('status')

        pedido = Pedido.objects.get(id=pedido_id)

        if pedido.status == status:
            messages.error(request, 'Altere o status do pedido para atualizar!', extra_tags='editar-pedido')
        else:
            pedido.status = status
            pedido.save()

            messages.success(request, 'Status do pedido alterado com sucesso!', extra_tags='editar-pedido')

    return redirect('pedidos')

def excluir_pedido_view(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')

        pedido = Pedido.objects.get(id=pedido_id)
        pedido.delete()
        messages.success(request, 'Pedido excluído com sucesso!', extra_tags='page-pedidos')

    return redirect('pedidos')