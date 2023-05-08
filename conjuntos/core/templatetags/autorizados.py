from django import template
from ..models import Autorizado
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_autorizados_list():
    autorizados = Autorizado.objects.all()
    return autorizados