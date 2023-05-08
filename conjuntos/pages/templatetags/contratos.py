from django import template
from core.models import Contrato
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def get_contratos_list():
    lista =[]
    date = datetime.now()
    hoy = date.date()
    Contratos = Contrato.objects.all().filter(activo='SI')
    for i in Contratos:
        fecha = i.fecha_contrato
        fecha_vencimiento = fecha + timedelta(i.vigencia*30.4167)
        dias = hoy-fecha_vencimiento
        dias_dif = dias.days
        if dias_dif >-30:
            dias_vence = dias_dif
            meses_vence = dias_vence/30
            lista.append(i.id)
            Contrato.objects.filter(id=i.id).update(meses_vence=meses_vence,dias_vence=dias_vence,fecha_vence=fecha_vencimiento)
            lista.append(i.id)    
    contratos = Contrato.objects.filter(id__in=lista)
    return contratos     