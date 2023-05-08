from django import template
from ..models import Autorizado,PlataformaWebPeatonal
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_autoriza_plataforma_web_peatonal_list():
    autoriza_plataforma_web_peatonal = PlataformaWebPeatonal.objects.all()
    return autoriza_plataforma_web_peatonal