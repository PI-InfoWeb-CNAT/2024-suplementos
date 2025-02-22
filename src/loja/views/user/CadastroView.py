from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User

from loja.models import Cliente, Notificacao
from loja.utils import validar_cpf

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_usuario')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tel_celular = request.POST.get('tel_celular')
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirm_senha')

        if nome and email and senha and cpf and tel_celular and confirm_senha:
            cpf = ''.join(filter(str.isdigit, cpf))
            cpf_validado = validar_cpf(cpf)
            
            if senha == confirm_senha:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail já cadastrado', extra_tags='page-cadastro')
                elif Cliente.objects.filter(cpf=cpf).exists():
                    messages.error(request, 'CPF já cadastrado', extra_tags='page-cadastro')
                elif not cpf_validado:
                    messages.error(request, 'CPF inválido', extra_tags='page-cadastro')
                elif len(senha) < 8:
                    messages.error(request, 'A senha deve ter no mínimo 8 caracteres', extra_tags='page-cadastro')
                else:
                    try:
                        user = User.objects.create_user(username=nome, email=email, password=senha)
                        cliente = Cliente.objects.create(
                            user=user,
                            nome=nome,
                            cpf=cpf,
                            telefone_celular=tel_celular,
                        )

                        Notificacao.objects.create(
                            cliente=cliente,
                            categoria='mensagem_personalizada',
                            titulo='Mensagem de boas-vindas',
                            texto=f'Olá, {nome}! Seja bem-vindo ao nosso time!'
                        )
                        messages.success(request, 'Cadastro realizado com sucesso', extra_tags='page-cadastro')
                    except IntegrityError:
                        messages.error(request, 'Erro ao criar o cadastro. Tente novamente.', extra_tags='page-cadastro')
            else:
                messages.error(request, 'As senhas não estão iguais', extra_tags='page-cadastro')
        else:
            messages.error(request, 'Preencha todos os campos', extra_tags='page-cadastro')

    return render(request, template_name='user/cadastro.html', status=200)