from django.contrib import admin
from .models import *
from .models.Carrinho import CarrinhoItem

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone_celular')
    empty_value_display = 'Vazio'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'porcentagem_desconto')
    empty_value_display = 'Vazio'

class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'cliente', 'data_envio', 'enviar_para_todos', 'lida')
    list_filter = ('categoria', 'enviar_para_todos')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.enviar_para_todos:
            return ['cliente']
        return super().get_readonly_fields(request, obj)

class CartaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_titular', 'bandeira', 'tipo')
    empty_value_display = 'Vazio'

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('user', 'criado_em')
    empty_value_display = 'Anônimo'

class CarrinhoItemAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'carrinho', 'preco', 'imagem')
    empty_value_display = 'Vazio'

admin.site.register(Cartao, CartaoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco)
admin.site.register(Favorito)
admin.site.register(Lote)
admin.site.register(Notificacao, NotificacaoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(CarrinhoItem, CarrinhoItemAdmin)