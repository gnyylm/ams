from django.shortcuts import render,get_object_or_404
from django.conf import settings
import json
from .models import sezon as sezonlar,yaris,oduller

def index(request):
    return render(request, 'yaris/index.html')

def sezon(request,szn):
    sz = get_object_or_404(sezonlar,title=szn)
    races = yaris.objects.all().filter(sezon=sz)
    liste = []
    for rc in races:
        liste.append({'title': rc.adi,'lat': str(rc.lat),'lng':str(rc.lng)})
    context = {
        'sezon' : sz,
        'google' : settings.GOOGLE_MAPS_API_KEY,
        'liste' : json.dumps(liste,ensure_ascii=False).encode('utf8')

    }
    return render(request,'yaris/sezon.html', context)

def race(request,slug,id):
    rc = get_object_or_404(yaris,sezon__title=slug, slug=id)
    context = {
        "race" : rc
    }
    return render(request, 'yaris/race.html',context)
def temsilciler (request):
    
    return render(request,'temsilci/index.html')