from django.shortcuts import render,HttpResponse

def home_view(request):
    context = {'isim': 'Misafir Kullanıcı'}
    return render(request, 'home.html', context)
