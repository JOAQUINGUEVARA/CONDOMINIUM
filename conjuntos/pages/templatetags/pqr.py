from django import template
from core.models import UserPerfil,Parametros
from pages.models import Pqr,RespuestaPqr
from datetime import datetime, timedelta
from django.db.models.functions import ExtractYear

register = template.Library()


@register.simple_tag()
def get_pqr_list():
    #pqr = Pqr.objects.exclude(id__in=[elem.id for elem in RespuestaPqr.objects.all()])
    pqr = Pqr.objects.filter(pendiente=True)
    return pqr

