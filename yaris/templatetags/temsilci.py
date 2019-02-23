from django import template
from yaris.models import temsilci
register = template.Library()

@register.simple_tag
def temsilciler():
    tm = temsilci.objects.all()
    if tm:
        return tm