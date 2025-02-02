from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from loja.models import Pedido, Notificacao, Cliente, DevolucaoProduto

@receiver(pre_save, sender=Pedido)
def salvar_status_anterior(sender, instance, **kwargs):
    try:
        pedido_antigo = Pedido.objects.get(id=instance.id)
        instance.status_anterior = pedido_antigo.status  
    except Pedido.DoesNotExist:
        instance.status_anterior = None

@receiver(post_save, sender=Pedido)
def notificar_cliente_pedido(sender, instance, created, **kwargs):
    if not created and instance.status_anterior and instance.status != instance.status_anterior:
        cliente = Cliente.objects.get(user=instance.user) 
        
        Notificacao.objects.create(
            cliente=cliente,
            categoria='status_pedido',
            titulo=f"Status do pedido #{instance.id}",
            texto=f"Seu pedido #{instance.id} teve o status alterado para {instance.get_status_display()}."
        )

@receiver(pre_save, sender=DevolucaoProduto)
def salvar_status_anterior_devolucao(sender, instance, **kwargs):
    try:
        devolucao_antiga = DevolucaoProduto.objects.get(id=instance.id)
        instance.status_anterior = devolucao_antiga.status
    except DevolucaoProduto.DoesNotExist:
        instance.status_anterior = None

@receiver(post_save, sender=DevolucaoProduto)
def notificar_cliente_devolucao(sender, instance, created, **kwargs):
    if not created and instance.status_anterior and instance.status != instance.status_anterior:
        cliente = Cliente.objects.get(user=instance.cliente.user) 

        Notificacao.objects.create(
            cliente=cliente,
            categoria='status_devolucao',
            titulo=f"Status da devolução do produto {instance.produto.nome}",
            texto=f"Sua devolução do produto {instance.produto.nome} teve o status alterado para {instance.get_status_display()}."
        )
