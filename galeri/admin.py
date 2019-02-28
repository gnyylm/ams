from django.contrib import admin
from .models import galeri

class GaleriAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('title',)
admin.site.register(galeri, GaleriAdmin)