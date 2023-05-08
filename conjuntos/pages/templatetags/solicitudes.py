from django import template
from core.models import ResidenteTemp

register = template.Library()

@register.simple_tag
def get_solicitudes_list():
    solicitudes = ResidenteTemp.objects.all()
    return solicitudes