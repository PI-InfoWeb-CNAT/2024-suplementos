from django import template

register = template.Library()

@register.filter
def first_name(value):
    return value.split()[0].capitalize()

@register.filter
def numero_cartao(num):
    return '*' * 4 + ' ' + num[-4:]