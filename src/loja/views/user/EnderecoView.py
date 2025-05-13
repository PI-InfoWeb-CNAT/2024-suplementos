from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from loja.models import Cliente, Endereco

@login_required
def adicionar_endereco_view(request):
    cliente = Cliente.objects.get(user=request.user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        telefone = request.POST.get('telefone')

        enderecos_cliente = Endereco.objects.filter(cliente=request.user.cliente)

        endereco_existe = enderecos_cliente.filter(rua=rua, numero=numero).exists()

        if nome and cep and estado and cidade and rua and numero:
            if not endereco_existe:
                Endereco.objects.create(cliente=cliente, nome=nome, cep=cep, estado=estado, cidade=cidade, rua=rua, numero=numero, complemento=complemento, telefone=telefone)

                messages.success(request, 'Endereço adicionado com sucesso!', extra_tags='novo-endereco')
                return redirect('perfil')
            else:
                messages.error(request, 'Você já tem um endereço com esses dados!', extra_tags='novo-endereco')
                return redirect('perfil')
        else:
            messages.error(request, 'Preencha os campos obrigatórios. (*)', extra_tags='novo-endereco')
    
    return redirect('perfil')

@login_required
def edit_endereco_view(request):
    if request.method == 'POST':
        endereco_id = request.POST.get('endereco_id')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        telefone = request.POST.get('telefone')

        endereco = Endereco.objects.get(id=endereco_id, cliente=request.user.cliente)

        if endereco.nome == nome and endereco.cep == cep and endereco.estado == estado and endereco.cidade == cidade and endereco.rua == rua and endereco.numero == numero and endereco.complemento == complemento and endereco.telefone == telefone:
            messages.error(request, 'Altere os dados para atualizar!', extra_tags='edit-endereco')
        else:
            enderecos_cliente = Endereco.objects.filter(cliente=request.user.cliente)

            endereco_existe = enderecos_cliente.exclude(id=endereco.id).filter(rua=rua, numero=numero).exists()

            if endereco_existe:
                messages.error(request, 'Você já tem um endereço com esses dados!', extra_tags='edit-endereco')
            else:
                endereco.nome = nome
                endereco.cep = cep
                endereco.estado = estado
                endereco.cidade = cidade
                endereco.rua = rua
                endereco.numero = numero
                endereco.complemento = complemento
                endereco.telefone = telefone

                endereco.save()

                messages.success(request, 'Dados atualizados com sucesso!', extra_tags='edit-endereco')
    return redirect('perfil')

@login_required
def excluir_endereco_view(request):
    if request.method == 'POST':
        endereco_id = request.POST.get('endereco_id')

        endereco = Endereco.objects.get(id=endereco_id, cliente=request.user.cliente)
        endereco.delete()
        messages.success(request, 'Endereço excluído com sucesso!', extra_tags='page-perfil')
    return redirect('perfil')