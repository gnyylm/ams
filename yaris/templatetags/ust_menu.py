from django import template
from django.conf import settings
from yaris.models import sezon,yaris,sponsorlar
import json
register = template.Library()

@register.simple_tag
def jump_link():
    sz = sezon.objects.all().order_by('-start_date')
    if sz:
        return sz
@register.simple_tag
def races(sezon):
    sz = yaris.objects.all().filter(sezon=sezon).order_by('mesafe')
    if sz:
        return sz
@register.simple_tag
def sponsors():
        sp = sponsorlar.objects.all()
        if sp:
                return sp
@register.simple_tag
def maps(sezon):
        sz = yaris.objects.all().filter(sezon=sezon)
        if sz:
                liste = []
                for rc in sz:
                        liste.append({'yaris': rc.adi,'lat': str(rc.lat),'lng':str(rc.lng)})
                return json.dumps(liste)

@register.simple_tag
def map2(race):
        rc = yaris.objects.get(pk=race)
        if rc:
                return([{'yaris': rc.adi,'lat': str(rc.lat),'lng':str(rc.lng)}])

@register.simple_tag
def ayar(name):
    return getattr(settings, name, "")