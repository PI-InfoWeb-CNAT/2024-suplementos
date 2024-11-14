from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'CPF', 'Telefone_celular')
    empty_value_display = 'Vazio'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Preco', 'Descricao', 'Dt_fabricacao', 'Dt_validade', 'Promocao')
    empty_value_display = 'Vazio'

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Endereco)
admin.site.register(Notificacao)