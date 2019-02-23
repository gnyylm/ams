from django.contrib import admin
from yaris.models import ulkeler,sezon,katilimci,iller,Pigeon
import datetime

class sezonAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(sezon, sezonAdmin)

class pigeonInline(admin.TabularInline):
    model = Pigeon
    extra = 1

class LigAdmin(admin.ModelAdmin):
    def category_post_count(self, obj):
        return obj.fanchers.count()
    category_post_count.short_description = "Kayıtlı Kuşu"
    list_display = ['username','name','lastname','mobile','category_post_count']
    list_filter = ['il']
    inlines = [pigeonInline]
admin.site.register(katilimci, LigAdmin)


class pigeonsAdmin(admin.ModelAdmin):
    def get_kunye(self,obj):
        yil = datetime.datetime.strptime(str(obj.yil), '%Y-%m-%d').strftime('%y')
        ulke = obj.ulke.kod
        return ulke+"-"+yil+"-"+obj.kunye
    get_kunye.short_description = "Künye"
    list_display = ['user','get_kunye','kayit']
admin.site.register(Pigeon,pigeonsAdmin)
