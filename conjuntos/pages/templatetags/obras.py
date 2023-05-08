from django import template
from core.models import Obra
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_obras_list():
    obras = Obra.objects.filter(terminada=False)
    return obras     