from .models import Cliente, Notificacao, Favorito, Carrinho

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
        try:
            favoritos_cliente = Favorito.objects.filter(cliente=request.user.cliente).values_list('produto_id', flat=True)
        except Cliente.DoesNotExist:
            pass

    return {'favoritos_cliente': favoritos_cliente}

def itens_carrinho(request):
    carrinho = None

    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        if session_key:
            carrinho = Carrinho.objects.filter(session_key=session_key).first()

    if carrinho:
        itens = carrinho.itens.count()
    else:
        itens = 0

    return {'itens_carrinho': itens}

def verificar_admin(request):
    admin = False

    if request.user.is_staff:
        admin = True

    return {'admin': admin}