from django import template
from core.models import RecomendacionRevisor

register = template.Library()

@register.simple_tag
def get_recomendaciones_list():
    recomendaciones = RecomendacionRevisor.objects.filter(cumplido=False)
    return recomendaciones