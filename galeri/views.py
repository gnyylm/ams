from django.shortcuts import render
from .models import galeri

# Create your views here.
def index(request):
    img = galeri.objects.all()
    context = {
        "image" : img
    }
    return render(request, 'galeri/index.html', context)