import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from loja.models import Cartao, Cliente

@login_required
def list_carteira_view(request):
    cliente = Cliente.objects.get(user=request.user)

    cartoes_cliente = Cartao.objects.filter(cliente=cliente)

    context = {'cartoes': cartoes_cliente}

    return render(request, template_name='user/carteira.html', context=context, status=200) 

@login_required
def adicionar_cartao_view(request):
    cliente = Cliente.objects.get(user=request.user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        nometitular = request.POST.get('nometitular')
        numero = request.POST.get('numero')
        tipo = request.POST.get('tipo')

        numero = ''.join(filter(str.isdigit, numero))
        cartoes_cliente = Cartao.objects.filter(cliente=request.user.cliente)
        cartao_existe = cartoes_cliente.filter(numero=numero).exists()

        if nome and nometitular and numero and tipo:
            numero_bin = numero[:6] 
            url = f"https://api.pagar.me/bin/v1/{numero_bin}"

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    dados = response.json()
                    bandeira = dados.get('brandName', 'Desconhecido')

                    if cartao_existe:
                        messages.error(request, 'Você já possui esse cartão.', extra_tags='novo-cartao')
                    else:
                        if tipo == 'debito':
                            Cartao.objects.create(cliente=cliente, nome=nome, nome_titular=nometitular, numero=numero, bandeira=bandeira, tipo='debito')

                            messages.success(request, 'Cartão adicionado com sucesso!', extra_tags='novo-cartao')

                        elif tipo == 'credito':
                            Cartao.objects.create(cliente=cliente, nome=nome, nome_titular=nometitular, numero=numero, bandeira=bandeira, tipo='credito')

                            messages.success(request, 'Cartão adicionado com sucesso!', extra_tags='novo-cartao')

                else:
                    messages.error(request, 'Cartão não encontrado.', extra_tags='novo-cartao')

            except Exception as e:
                context = {'success': False, 'error': f'Erro ao consultar a API: {e}'}
        else:
            messages.error(request, 'Preencha os campos obrigatórios. (*)', extra_tags='novo-cartao')

    return redirect('minha-carteira')

@login_required
def edit_cartao_view(request):
    if request.method == 'POST':
        cartao_id = request.POST.get('cartao_id')
        nome = request.POST.get('nome')
        nometitular = request.POST.get('nometitular')
        tipo = request.POST.get('tipo')

        cartao = Cartao.objects.get(id=cartao_id, cliente=request.user.cliente)

        if cartao.nome == nome and cartao.nome_titular == nometitular and cartao.tipo == tipo:
            messages.error(request, 'Altere os dados para atualizar!', extra_tags='edit-cartao')
        else:
            cartao.nome = nome
            cartao.nome_titular = nometitular
            cartao.tipo = tipo

            cartao.save()
            messages.success(request, 'Dados atualizados com sucesso!', extra_tags='edit-cartao')

    return redirect('minha-carteira')

@login_required
def excluir_cartao_view(request):
    if request.method == 'POST':
        cartao_id = request.POST.get('cartao_id')

        cartao = Cartao.objects.get(id=cartao_id, cliente=request.user.cliente)
        cartao.delete()
        messages.success(request, 'Cartão excluído com sucesso!', extra_tags='page-carteira')

    return redirect('minha-carteira')