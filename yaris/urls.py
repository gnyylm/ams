from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="yarislar"),
    url(r'^(?P<szn>[-\w]+)/$', views.sezon, name="race_sezon"),
    url(r'^(?P<slug>[-\w]+)/(?P<id>[-\w]+)/$', views.race, name="race"),
]