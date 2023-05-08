from core.models import ActivoFijo,PrestamoActivoFijo
from datetime import datetime, timedelta,date
from django import template

register = template.Library()

@register.simple_tag
def get_prestamos_list():
    prestamo={}
    date = datetime.now()
    hoy = date.date()
    prestamos = PrestamoActivoFijo.objects.filter(devuelto=False)
    for i in prestamos:
        if i.fecha != None:
            dias=hoy-i.fecha
            dias = dias.days
        else:
            dias = 0    
        PrestamoActivoFijo.objects.filter(id=i.id).update(dias = dias)
    prestamos = PrestamoActivoFijo.objects.filter(devuelto=False).select_related()
    return prestamos


     