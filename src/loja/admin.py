from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'CPF', 'Telefone_celular')
    empty_value_display = 'Vazio'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Preco', 'Descricao', 'Dt_fabricacao', 'Dt_validade', 'Promocao')
    empty_value_display = 'Vazio'

class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'cliente', 'data_envio', 'enviar_para_todos', 'lida')
    list_filter = ('categoria', 'enviar_para_todos')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.enviar_para_todos:
            return ['cliente']
        return super().get_readonly_fields(request, obj)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Endereco)
admin.site.register(Notificacao, NotificacaoAdmin)