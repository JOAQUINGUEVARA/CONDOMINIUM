from django import template
from core.models import UserPerfil,Parametros
from core.models import Reservas
from datetime import datetime, timedelta
from django.db.models.functions import ExtractYear

register = template.Library()

@register.simple_tag()
def get_reservas_list():
    reservas = Reservas.objects.filter(confirmada=False,anexo_pago=True)
    return reservas

