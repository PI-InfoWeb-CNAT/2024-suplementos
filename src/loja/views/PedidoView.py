from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages


from loja.models import Cliente, Carrinho, CarrinhoItem, Endereco, Cartao, Pedido, PedidoItem, Notificacao

@login_required
def finalizar_pedido_view(request):
    cliente = Cliente.objects.get(user=request.user)
    enderecos = cliente.enderecos.all()
    cartoes = cliente.cartoes.all()
    
    carrinho = Carrinho.objects.filter(user=request.user).first()
    total = carrinho.total
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho)

    if request.method == 'POST':
        endereco_id = request.POST.get('endereco')
        cartao_id = request.POST.get('cartao')

        if not endereco_id or not cartao_id:
            messages.error(request, 'Preencha todos os campos antes de confirmar a compra.', extra_tags='page-pedido')
        else:
            endereco = Endereco.objects.get(id=endereco_id)
            cartao = Cartao.objects.get(id=cartao_id)

            pedido = Pedido.objects.create(user=request.user, endereco=endereco, cartao=cartao, total=total, status='1')

            for item in carrinho.itens.all():
                PedidoItem.objects.create(pedido=pedido, produto=item.produto, quantidade=item.quantidade, preco=item.preco, imagem=item.imagem)

                if item.quantidade > item.produto.calcular_estoque():
                    messages.error(request, f'A quantidade do produto {item.produto.nome} está acima do estoque disponível.', extra_tags='page-pedido')
                else:
                    lotes_ordenados = item.produto.lotes.all().order_by('data_validade')

                    for lote in lotes_ordenados:
                        if item.quantidade <= 0:
                            break

                        if item.quantidade >= lote.quantidade:
                            item.quantidade -= lote.quantidade
                            lote.delete() 
                        else:
                            lote.quantidade -= item.quantidade
                            lote.save()  
                            item.quantidade = 0  
                            break

            carrinho.delete()
            Notificacao.objects.create(
                cliente=cliente, 
                categoria='mensagem_personalizada', 
                titulo='Pedido realizado com sucesso', 
                texto=f'O seu pedido de código {pedido.id} foi realizado com sucesso! Agradecemos pela confiança!'
            )
            messages.success(request, f'Pedido realizado com sucesso!', extra_tags='page-pedido')


    context = {
        'enderecos': enderecos,
        'cartoes': cartoes,
        'produtos': carrinho_itens,
        'total': total
    }

    return render(request, template_name='user/finalizar_pedido.html', context=context, status=200) 