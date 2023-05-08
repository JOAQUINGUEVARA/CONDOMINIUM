from django import template
from core.models import Reparacion
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_reparaciones_list():
    reparaciones = Reparacion.objects.filter(terminado=False)
    return reparaciones     