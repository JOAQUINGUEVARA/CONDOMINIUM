from django import template
from core.models import ZonaComun,MiembroStaff
from pages.models import Legislacion,Comunicado,Clasificado,Normatividad,Pqr,RespuestaPqr,Comunicado
from upload.models import AnexoLegislacion,AnexoNormatividad,AnexoComunicado
from datetime import datetime, timedelta
import dateutil.parser

register = template.Library()

@register.simple_tag
def get_legislacion_list():
    legislacion = Legislacion.objects.all().order_by('id')
    return legislacion  

@register.simple_tag
def get_anexo_legislacion_list():
    anexos_legislacion = AnexoLegislacion.objects.all().order_by('id')
    return anexos_legislacion

@register.simple_tag
def get_anexos_comunicado_list():
    anexos_comunicado = AnexoComunicado.objects.all().order_by('id')
    return anexos_comunicado

@register.simple_tag
def get_comunicados_list():
    lista = []
    date = datetime.now()
    comunicados_all = Comunicado.objects.all()
    for j in comunicados_all:
        b = j.created.strftime('%Y-%m-%d')
        c = dateutil.parser.parse(b).date()
        s = (date.date()-c).days
        f = int(s)
        if f > j.dias_publicacion:
            lista.append(j.id)
    comunicados = Comunicado.objects.exclude(id__in=lista)
    return comunicados

@register.simple_tag
def get_clasificados_list():
    clasificados = Clasificado.objects.filter(vigente=True).order_by('id')
    return clasificados

@register.simple_tag
def get_normatividad_list():
    normatividad = Normatividad.objects.all().order_by('id')
    return normatividad

@register.simple_tag
def get_anexo_normatividad_list():
    anexos_normatividad = AnexoNormatividad.objects.all().order_by('id')
    return anexos_normatividad

@register.simple_tag
def get_staff_list():
    staff = MiembroStaff.objects.filter(publicar=True).order_by('orden')
    return staff

@register.simple_tag
def get_zonas_comunes_list():
    zonas_comunes = ZonaComun.objects.all().order_by('id')
    return zonas_comunes

@register.simple_tag
def get_pqr_list():
    #pqr = Pqr.objects.exclude(id__in=[elem.id for elem in RespuestaPqr.objects.all()])
    pqr = Pqr.objects.all()
    return pqr
