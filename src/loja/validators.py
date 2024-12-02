from django.core.exceptions import ValidationError

def numero_nao_negativo(value):
    if value < 0:
        raise ValidationError('O número não deve ser negativo')
    
def porcentagem(value):
    if value < 0 or value > 100:
        raise ValidationError('O número deve estar entre 0 e 100')