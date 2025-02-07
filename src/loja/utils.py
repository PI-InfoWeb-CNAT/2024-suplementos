from django.utils import timezone

from loja.models import Lote, Produto

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

def aplicar_promocao_auto():
    produtos = Produto.objects.all()  

    for produto in produtos:
        lotes = Lote.objects.filter(produto=produto)  
        if not lotes.exists():
            continue  

        lote_mais_proximo = min(lotes, key=lambda lote: lote.data_validade)

        dias_para_validade = (lote_mais_proximo.data_validade - timezone.now().date()).days

        if dias_para_validade < 0:  
            desconto = 90  
        elif 0 <= dias_para_validade <= 10: 
            desconto = 70 
        elif 11 <= dias_para_validade <= 20: 
            desconto = 50
        elif 21 <= dias_para_validade <= 30: 
            desconto = 30  
        else:
            desconto = 0  

        if produto.porcentagem_desconto != desconto:
            produto.porcentagem_desconto = desconto
            produto.save()