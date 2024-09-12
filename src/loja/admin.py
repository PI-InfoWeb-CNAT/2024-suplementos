from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone_celular', 'telefone_fixo', 'dt_nasc')
    empty_value_display = 'Vazio'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'dt_fabricacao', 'dt_validade')
    empty_value_display = 'Vazio'

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)