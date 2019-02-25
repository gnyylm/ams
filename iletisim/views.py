from django.shortcuts import render
from django.conf import settings
def index(request):
    context = {
        "konum" : settings.LAT_LNG
    }
    return render(request, 'iletisim/index.html' ,context)
