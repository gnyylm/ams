from django.shortcuts import render,get_object_or_404
from yaris.models import sezon, katilimci,Pigeon

def index(request):
    if request.GET.get('s'):
        yil = request.GET.get('s')
        sz = sezon.objects.all().order_by("-start_date")
        kt = katilimci.objects.all().filter(sezon__start_date__year=yil)
    else:
        sz = sezon.objects.all().order_by("-start_date")
        kt = get_object_or_404(katilimci,sezon=sz[0].id)
        print(dir(kt))
    content = {
        "title":"Katılımcılar",
        "sezon" : sz,
        "kt": kt
    }
    return render(request, 'katilimci/index.html',content)