from django.shortcuts import render
from yaris.models import kurallar
def index(request):
    kr = kurallar.objects.all()
    context = {
        "title" : 'Kurallar',
        "data" : kr
    }
    return render(request, 'kurallar/index.html',context)