from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from loja.models import Cliente, Endereco
from loja.utils import validar_cpf

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
            cpf = cliente.cpf
            tel_celular = cliente.telefone_celular
            enderecos_cliente = todos_enderecos.filter(cliente_id=cliente.id)

    context_user = {
        'nome': nome,
        'email': email,
        'tel_celular': tel_celular,
        'cpf': cpf,
        'enderecos': enderecos_cliente
    }

    context_admin = {
        'nome': nome,
        'email': email,
        'tel_celular': tel_celular,
        'cpf': cpf,
    }

    if request.user.is_staff:
        return render(request, template_name='admin/perfil.html', context=context_admin, status=200)
    else:
        return render(request, template_name='user/perfil.html', context=context_user, status=200)

@login_required 
def edit_dados_view(request):
    user = request.user
    usuarios = User.objects.all()
    clientes = Cliente.objects.all()
    cliente = Cliente.objects.get(user=user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tel_celular = request.POST.get('tel_celular')

        if user.username == nome and user.email == email and cliente.cpf == cpf and cliente.telefone_celular == tel_celular:
            messages.error(request, 'Altere os dados para atualizar!', extra_tags='page-perfil')
        else:
            email_alterado = user.email != email
            email_existe = email_alterado and usuarios.filter(email=email).exists()
            cpf_alterado = cliente.cpf != cpf
            cpf_existe = cpf_alterado and clientes.filter(cpf=cpf).exists()

            if email_existe:
                messages.error(request, 'Esse e-mail já existe.', extra_tags='page-perfil')
            elif cpf_existe:
                messages.error(request, 'Esse cpf já existe.', extra_tags='page-perfil')
            elif not validar_cpf(cpf):
                messages.error(request, 'CPF inválido.', extra_tags='page-perfil')
            else:
                user.username = nome
                if email_alterado:
                    user.email = email
                user.save()

                cliente.nome = nome
                cliente.cpf = cpf
                cliente.telefone_celular = tel_celular
                cliente.save()

                messages.success(request, 'Dados atualizados com sucesso!', extra_tags='page-perfil')

    return redirect('perfil')

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

    return redirect('perfil')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def excluir_conta_view(request):
    if request.method == 'POST':    
        user = request.user

        user.delete()
        logout(request)
        messages.success(request, 'Conta excluída com sucesso!')
        return redirect('home')