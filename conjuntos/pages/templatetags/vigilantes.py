from django import template
from core.models import Vigilante

register = template.Library()

@register.simple_tag
def get_vigilantes_list():
    vigilantes = Vigilante.objects.filter(publicar=True)
    return vigilantes