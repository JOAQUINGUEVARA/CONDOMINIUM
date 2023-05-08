from django import template
from core.models import CompromisoConsejo

register = template.Library()

@register.simple_tag
def get_compromisos_list():
    compromisos = CompromisoConsejo.objects.filter(cumplido=False)
    return compromisos