from django.shortcuts import render, redirect
from django.contrib import messages
from loja.models import Cliente, Notificacao
from django.contrib.auth.models import User
from django.urls import reverse

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
            print(cpf_validado)
            if senha == confirm_senha:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'E-mail já cadastrado')
                elif Cliente.objects.filter(cpf=cpf).exists():
                    messages.error(request, 'CPF já cadastrado')
                elif not cpf_validado:
                    messages.error(request, 'CPF inválido')
                elif len(senha) < 8:
                    messages.error(request, 'A senha deve ter no mínimo 8 caracteres')
                else:
                    user = User.objects.create_user(username=nome, email=email, password=senha)
                    user.save()
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
                        texto= f'Olá, {nome}! Seja bem-vindo ao nosso time!'
                    )
                    messages.success(request, 'Cadastro realizado com sucesso')
            else:
                messages.error(request, 'As senhas não estão iguais')
        else:
            messages.error(request, 'Preencha todos os campos')

    return render(request, template_name='cadastro.html', status=200)

def validar_cpf(cpf):
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    def calcular_digito(cpf, fator):
        soma = sum(int(cpf[i]) * (fator - i) for i in range(len(cpf)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    primeiro_digito = calcular_digito(cpf[:9], 10)
    segundo_digito = calcular_digito(cpf[:9] + str(primeiro_digito), 11)

    if cpf[-2:] == f'{primeiro_digito}{segundo_digito}':
        return True
    else:
        return False