from django.shortcuts import render, redirect
from django.contrib import messages

from loja.models import Produto

def produtos_view(request):
    produtos = Produto.objects.all().order_by('-id')

    categorias = [
        ('acessorios', 'Acessórios'),
        ('alimentos', 'Alimentos'),
        ('roupas', 'Roupas'),
        ('suplementos', 'Suplementos'),
    ]

    context = {
        'produtos': produtos,
        'categorias': categorias
    }

    return render(request, template_name='admin/produtos.html', context=context, status=200)

def criar_produto_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco').replace(',', '.')
        desconto = request.POST.get('desconto') or 0
        categoria = request.POST.get('categoria')
        imagem = request.FILES.get('imagem')

        if not nome or not descricao or not preco or not categoria or not imagem:
            messages.error(request, 'Preencha todos os campos!', extra_tags='criar-produto')
        else:
            try:
                preco = float(preco)
                desconto = int(desconto)

                if preco <= 0:
                    messages.error(request, 'O preço deve ser maior que 0!', extra_tags='criar-produto')
                elif desconto < 0 or int(desconto) > 100:
                    messages.error(request, 'O desconto deve ser entre 0 e 100!', extra_tags='criar-produto')
                else:
                    Produto.objects.create(nome=nome, descricao=descricao, preco=preco, porcentagem_desconto=desconto, categoria=categoria, imagem=imagem)
                    messages.success(request, 'Produto criado com sucesso!', extra_tags='criar-produto')
            except ValueError:
                messages.error(request, 'O preço deve ser um número!', extra_tags='criar-produto')

    return redirect('produtos')

def edit_produto_view(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco').replace(',', '.')
        desconto = request.POST.get('desconto') or 0
        categoria = request.POST.get('categoria')
        imagem = request.FILES.get('imagem')
        print(imagem)

        try:
            preco = float(preco)
            desconto = int(desconto)

            produto = Produto.objects.get(id=produto_id)

            if produto.nome == nome and produto.descricao == descricao and produto.preco == preco and produto.porcentagem_desconto == desconto and produto.categoria == categoria and (not imagem or produto.imagem == imagem):
                messages.error(request, 'Altere algum dado para atualizar!', extra_tags='editar-produto')
            else:
                if preco <= 0:
                    messages.error(request, 'O preço deve ser maior que 0!', extra_tags='editar-produto')
                elif desconto < 0 or int(desconto) > 100:
                    messages.error(request, 'O desconto deve ser entre 0 e 100!', extra_tags='editar-produto')
                else:
                    produto.nome = nome
                    produto.descricao = descricao
                    produto.preco = preco
                    produto.porcentagem_desconto = desconto
                    produto.categoria = categoria
                    if imagem: 
                            produto.imagem = imagem

                    produto.save()
                    messages.success(request, 'Produto atualizado com sucesso!', extra_tags='editar-produto')
        except ValueError:
            messages.error(request, 'O preço deve ser um número!', extra_tags='editar-produto')

    return redirect('produtos')


def excluir_produto_view(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')

        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!', extra_tags='page-produtos')

    return redirect('produtos')