from django.core.exceptions import ValidationError
from django.utils.timezone import now

def numero_nao_negativo(value):
    if value < 0:
        raise ValidationError('O número não deve ser negativo')
    
def numero_positivo(value):
    if value <= 0:
        raise ValidationError('O número deve ser positivo')
    
def porcentagem(value):
    if value < 0 or value > 100:
        raise ValidationError('O número deve estar entre 0 e 100')
    
def data_futura(value):
    if value < now().date():  
        raise ValidationError('A data não pode ser anterior a hoje.')