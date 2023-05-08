from django import template
from upload.models import AnexoPagoReserva
from django.db.models.functions import ExtractYear

register = template.Library()

@register.simple_tag()
def get_anexo_pago_reservas_list():
    anexo_pago_reservas = AnexoPagoReserva.objects.all()
    return anexo_pago_reservas

