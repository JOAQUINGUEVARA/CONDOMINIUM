from django import template
from pages.models import Panel

register = template.Library()

@register.simple_tag
def get_panel_list():
    panel = Panel.objects.all()
    return panel   