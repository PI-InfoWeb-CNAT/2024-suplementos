from .models import Notificacao

def notificacoes_nao_lidas(request):
    if request.user.is_authenticated:
        notificacoes_nao_lidas = Notificacao.objects.filter(cliente_id=request.user.id, lida=False).count()
    else:
        notificacoes_nao_lidas = 0
    return {'notificacoes_nao_lidas': notificacoes_nao_lidas}