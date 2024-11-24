from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from loja.models import Cliente, Endereco

@login_required
def perfil_view(request):
    user = request.user
    clientes = Cliente.objects.all()

    todos_enderecos = Endereco.objects.all()
    enderecos_cliente = ''

    nome = user.username
    email = user.email
    tel_celular = ''
    cpf = ''

    for cliente in clientes:
        if cliente.user_id == user.id:
            cpf = cliente.CPF
            tel_celular = cliente.Telefone_celular
            enderecos_cliente = todos_enderecos.filter(cliente_id=cliente.id)

    context = {
        'nome': nome,
        'email': email,
        'tel_celular': tel_celular,
        'cpf': cpf,
        'enderecos': enderecos_cliente
    }
    return render(request, template_name='Perfil/perfil.html', context=context, status=200)

@login_required 
def edit_dados_view(request):
    user = request.user
    clientes = User.objects.all()
    cliente = Cliente.objects.get(user=user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tel_celular = request.POST.get('tel_celular')

        if user.username == nome and user.email == email and cliente.CPF == cpf and cliente.Telefone_celular == tel_celular:
            messages.error(request, 'Altere os dados para atualizar!', extra_tags='page-perfil')
        else:
            email_alterado = user.email != email
            email_existe = email_alterado and clientes.filter(email=email).exists()

            if email_existe:
                messages.error(request, 'Esse e-mail já existe.', extra_tags='page-perfil')
            else:
                user.username = nome
                if email_alterado:
                    user.email = email
                user.save()

                cliente.CPF = cpf
                cliente.Telefone_celular = tel_celular
                cliente.save()

                messages.success(request, 'Dados atualizados com sucesso!', extra_tags='page-perfil')

    return redirect(reverse('perfil'))

@login_required
def redefinir_senha_view(request):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        senhaAtual = request.POST.get('senhaAtual')
        novaSenha = request.POST.get('novaSenha')
        confirm_novaSenha = request.POST.get('confirmacao-novaSenha')

        if senhaAtual and novaSenha and confirm_novaSenha:
            if user.check_password(senhaAtual):
                if novaSenha == confirm_novaSenha:
                    if len(novaSenha) >= 8:
                        if novaSenha != senhaAtual:
                            user.set_password(novaSenha)
                            user.save()
                            update_session_auth_hash(request, user) 

                            messages.success(request, 'Senha redefinida com sucesso!', extra_tags='redefinir-senha')
                        else:
                            messages.error(request, 'Altere a senha para redefinir', extra_tags='redefinir-senha')
                    else:
                        messages.error(request, 'A senha deve ter no mínimo 8 caracteres', extra_tags='redefinir-senha')
                else:
                    messages.error(request, 'A confirmação da senha nova está incorreta', extra_tags='redefinir-senha')
            else:
                messages.error(request, 'A senha atual está incorreta.', extra_tags='redefinir-senha')
        else:
            messages.error(request, 'Preencha todos os campos', extra_tags='redefinir-senha')

    return redirect(reverse('perfil'))
    
@login_required
def adicionar_endereco_view(request):
    user = request.user

    cliente = Cliente.objects.get(user=user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        telefone = request.POST.get('telefone')

        enderecos_cliente = Endereco.objects.filter(cliente=user.cliente)

        endereco_existe = enderecos_cliente.filter(rua=rua, numero=numero).exists()

        if nome and cep and estado and cidade and rua and numero:
            if not endereco_existe:
                Endereco.objects.create(cliente=cliente, nome=nome, cep=cep, estado=estado, cidade=cidade, rua=rua, numero=numero, complemento=complemento, telefone=telefone)

                messages.success(request, 'Endereço adicionado com sucesso!', extra_tags='novo-endereco')
                return redirect(reverse('perfil'))
            else:
                messages.error(request, 'Você já tem um endereço com esses dados!', extra_tags='novo-endereco')
                return redirect(reverse('perfil'))
            
        else:
            messages.error(request, 'Preencha os campos obrigatórios. (*)', extra_tags='novo-endereco')
    
    return redirect(reverse('perfil'))

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
    return redirect(reverse('perfil'))

@login_required
def excluir_endereco_view(request):
    if request.method == 'POST':
        endereco_id = request.POST.get('endereco_id')

        endereco = Endereco.objects.get(id=endereco_id, cliente=request.user.cliente)
        endereco.delete()
        messages.success(request, 'Endereço excluído com sucesso!', extra_tags='page-perfil')
    return redirect(reverse('perfil'))
    
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

@login_required
def excluir_conta_view(request):
    if request.method == 'POST':    
        user = request.user

        user.delete()
        logout(request)
        messages.success(request, 'Conta excluída com sucesso!')
        return redirect(reverse('home'))
    
    