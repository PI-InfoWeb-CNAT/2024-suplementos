from .models import Cliente, Notificacao, Favorito

def notificacoes_nao_lidas(request):
    notificacoes_nao_lidas = ''
    if request.user.is_authenticated:
        clientes = Cliente.objects.all()
        for cliente in clientes:
            if cliente.user_id == request.user.id:
                notificacoes_nao_lidas = Notificacao.objects.filter(cliente_id=cliente.id, lida=False).count()
    else:
        notificacoes_nao_lidas = 0
    return {'notificacoes_nao_lidas': notificacoes_nao_lidas}

def favoritos_cliente(request):
    favoritos_cliente = []
    if request.user.is_authenticated:
        favoritos_cliente = Favorito.objects.filter(cliente=request.user.cliente).values_list('produto_id', flat=True)

    return {'favoritos_cliente': favoritos_cliente}