"""amanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from home.views import home_view
from django.conf.urls import url
from django.contrib.flatpages import views
from yaris import views as tm


urlpatterns = [
    url(r'^$', home_view, name='home'),
    path('cp/', admin.site.urls),
    url(r'^kurallar/', include('kurallar.urls')),
    url(r'^katilimcilar/', include('katilimci.urls')),
    url(r'^galeri/', include('galeri.urls')),
    url(r'^yarislar/', include('yaris.urls')),
    url(r'^iletisim/', include('iletisim.urls')),
    url(r'^temsilciler/', tm.temsilciler, name='temsilciler'),
    path('hakkimizda/', views.flatpage, {'url': '/hakkimizda/'}, name='hak'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
