from django import template
from core.models import MiembroConsejo

register = template.Library()

@register.simple_tag
def get_consejo_list():
    consejeros = MiembroConsejo.objects.filter(activo=True)
    return consejeros