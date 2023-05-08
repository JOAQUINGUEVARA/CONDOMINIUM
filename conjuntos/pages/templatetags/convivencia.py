from django import template
from core.models import MiembroComiteConvivencia

register = template.Library()

@register.simple_tag
def get_convivencia_list():
    convivencia = MiembroComiteConvivencia.objects.filter(activo=True)
    return convivencia