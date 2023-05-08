from django import template
from core.models import Conjunto

register = template.Library()

@register.simple_tag
def get_conjunto_list():
    conjunto = Conjunto.objects.all()
    return conjunto