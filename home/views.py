from django.shortcuts import render,HttpResponse
from django.conf import settings

def home_view(request):
    context = {'konum': settings.LAT_LNG}
    return render(request, 'home.html', context)
