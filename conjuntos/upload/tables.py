from core.models import  AirBnB, AnexoContrato, Correspondencia, UserPerfil,ZonaComun,ReservaZonasComunes,Residente,Autorizado,Mantenimiento,ActivoFijo,Proveedor,Contrato,Obra,Reparacion
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django_tables2 import TemplateColumn,BooleanColumn
from datetime import datetime
import django_tables2
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithThousandsSeparator(django_tables2.Column):
    def render(self,value):
        return intcomma(value)

