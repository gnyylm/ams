from django.shortcuts import render,HttpResponse
from django.conf import settings
from galeri.models import galeri

def home_view(request):
    rc = galeri.objects.all()
    context = {'konum': settings.LAT_LNG,
    'image' : rc }
    return render(request, 'home.html', context)
