from django import template
from core.models import Vigilante

register = template.Library()

@register.simple_tag
def get_vigilancia_list():
    vigilantes = Vigilante.objects.all()
    return vigilantes