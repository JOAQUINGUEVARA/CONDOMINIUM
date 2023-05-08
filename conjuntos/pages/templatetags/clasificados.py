from django import template
from pages.models import Clasificado
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_clasificados_list():
    d = timedelta(days=30)
    clasificados = Clasificado.objects.filter(vigente=True).filter(created__gte=datetime.now()-d).order_by('-created')
    return clasificados