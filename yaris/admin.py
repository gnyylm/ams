from django.conf import settings
from django.contrib import admin
from .models import yaris,oduller,ulkeler,iller,temsilci,kurallar,sponsorlar



class AdmUlke(admin.ModelAdmin):
    list_display = ['ulke']

admin.site.register(ulkeler, AdmUlke)

class Admiil(admin.ModelAdmin):
    list_display = ['il']

admin.site.register(iller, Admiil)


class admOdul(admin.TabularInline):
    model = oduller
    extra = 5


class AdmYaris(admin.ModelAdmin):
    list_display = ['sezon','adi','tip','tarih','mesafe']
    prepopulated_fields = {"slug": ("adi",)}
    inlines = [admOdul]

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('admin/css/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'admin/js/location_picker.js',
            )
    
admin.site.register(yaris,AdmYaris)

class AdmOduller(admin.ModelAdmin):
    list_display =['title','yaris']

admin.site.register(oduller, AdmOduller)

class AdmTemsilci(admin.ModelAdmin):
    list_display = ['adi','soyadi','il','eposta','mobil']

admin.site.register(temsilci, AdmTemsilci)

class AdmKural(admin.ModelAdmin):
    list_display = ['kural']
admin.site.register(kurallar, AdmKural)

class AdmSponsor(admin.ModelAdmin):
    list_display = ['sponsor']
admin.site.register(sponsorlar, AdmSponsor)