from django.contrib import admin
from .models import *
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Email', 'CPF', 'Telefone_celular', 'Telefone_fixo', 'Dt_nasc', 'Endereco', 'Estado', 'CEP')
    empty_value_display = 'Vazio'

admin.site.register(Cliente, ClienteAdmin)