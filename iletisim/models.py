from django.db import models

# Create your models here.
class iletisim(models.Model):
    adi = models.CharField(max_length=60,verbose_name="Adı")
    soyadi = models.CharField(max_length=60,verbose_name="Soyadi")
    tel = models.CharField(max_length=20,verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-posta")
    mesaj = models.TextField(verbose_name="Mesaj")
    
    class Meta:
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.adi+" "+ self.soyadi
