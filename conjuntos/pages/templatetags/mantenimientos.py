from core.models import ActivoFijo
from datetime import datetime, timedelta,date
from django.db.models import F
from django import template
from django.db.models import DurationField, F, ExpressionWrapper
from dateutil.relativedelta import relativedelta
from django.db.models import Q


register = template.Library()

@register.simple_tag
def get_mantenimientos_list():
    lista =[]
    date = datetime.now()
    hoy = date.date()
    activos = ActivoFijo.objects.filter(mantenimiento='SI')
    for i in activos:
        fecha = i.ultimo_mantenimiento
        frecuencia = i.frecuencia_mantenimiento
        fecha_proximo_mantenimiento = fecha + timedelta(frecuencia*30.4167)
        dias = hoy-fecha_proximo_mantenimiento
        #print(fecha_proximo_mantenimiento)
        ActivoFijo.objects.filter(id=i.id).update(fecha_vence_mantenimiento=fecha_proximo_mantenimiento)
        dias_dif = dias.days
        if dias_dif > 0:
            dias_sin_mant = dias_dif
            meses_sin_mant = dias_dif/30
            if  meses_sin_mant > 0:
                lista.append(i.id)
                ActivoFijo.objects.filter(id=i.id).update(meses_sin_mantenimiento=meses_sin_mant,dias_sin_mantenimiento=dias_sin_mant,fecha_vence_mantenimiento=fecha_proximo_mantenimiento)
                lista.append(i.id)    
    mantenimientos = ActivoFijo.objects.filter(id__in=lista)
    
    return mantenimientos


     