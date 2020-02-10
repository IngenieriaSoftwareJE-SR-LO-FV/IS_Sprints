from django import template
register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def currency(value):
    return "${:.2f}".format(value)

@register.filter
def porcentaje(value):
    return "{}%".format(value)