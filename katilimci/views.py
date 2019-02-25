from django.shortcuts import render,get_object_or_404
from yaris.models import sezon, katilimci,Pigeon

def index(request):
    if request.GET.get('s'):
        yil = request.GET.get('s')
        sz = sezon.objects.all().order_by("-start_date")
        kt = katilimci.objects.all().filter(sezon__title=yil)
    else:
        sz = sezon.objects.all().order_by("-start_date")
        if sz:
            kt = katilimci.objects.all().filter(sezon__title=sz[0])
        else:
            kt = 0
    print(dir(kt))
    content = {
        "title": sz[0],
        "sezon" : sz,
        "kt": kt
    }
    return render(request, 'katilimci/index.html',content)