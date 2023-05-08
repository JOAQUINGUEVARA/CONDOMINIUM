from django import template
from ..models import Autorizado,PlataformaWebVehiculo
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_autoriza_plataforma_web_veiculo_list():
    autoriza_plataforma_web_vehiculo = PlataformaWebVehiculo.objects.all()
    return autoriza_plataforma_web_vehiculo