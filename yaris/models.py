from django.db import models

class ulkeler(models.Model):

    ulke = models.CharField(max_length=200, unique=True, verbose_name="Ülke")
    kod = models.CharField(max_length=3, verbose_name="Ülke Kodu", help_text="TR",null=True,blank=True)
    slug = models.SlugField()
    kayit = models.DateTimeField(auto_now_add=True)
    guncelleme = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Ülke'
        verbose_name_plural = 'Ülkeler'

    def __str__(self):
        return self.ulke

class iller(models.Model):
    ulke = models.ForeignKey('ulkeler', on_delete=models.CASCADE, verbose_name="Ülke", related_name='iller')
    il = models.CharField(max_length=255, verbose_name="İl adi", unique=True)
    slug = models.SlugField()
    kayit = models.DateTimeField(auto_now_add=True)
    guncelleme = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'il'
        verbose_name_plural = 'İller'

    def __str__(self):
        return self.il

class temsilci(models.Model):
    ulke = models.ForeignKey(ulkeler,verbose_name="Ülke",on_delete=models.CASCADE)
    il = models.ForeignKey(iller,verbose_name="İl", on_delete=models.CASCADE)
    adi = models.CharField(max_length=60,verbose_name="Adı")
    soyadi = models.CharField(max_length=60,verbose_name="Soyadı")
    eposta = models.CharField(max_length=120,verbose_name="E-posta",blank=True)
    mobil = models.CharField(max_length=25,verbose_name="Cep Telefonu",blank=True)
    facebook = models.CharField(max_length=150, verbose_name="Facebook Adresi", blank=True)

    class Meta:
        verbose_name = 'Temsilci'
        verbose_name_plural = 'Temsilciler'
    
    def __str__(self):
        return self.adi+" "+self.soyadi

class sezon(models.Model):
    title = models.CharField(max_length=120, verbose_name="Başlık")
    start_date = models.DateField(verbose_name="Başlangıc Tarihi")
    end_date = models.DateField(verbose_name="Bitiş Tarihi")

    class Meta:
        verbose_name = 'Sezon'
        verbose_name_plural = 'Sezonlar'

    def __str__(self):
        return self.title


class katilimci(models.Model):
    sezon = models.ForeignKey('sezon',verbose_name="Sezon", on_delete=models.CASCADE,related_name="katilimcilar")
    il = models.ForeignKey(iller, on_delete=models.CASCADE, verbose_name="İl")
    username = models.CharField(max_length=120,verbose_name="Takma isim", blank=True)
    name = models.CharField(max_length=60,verbose_name="Adı", blank=True)
    lastname = models.CharField(max_length=60,verbose_name="Soyadı", blank=True)
    email = models.EmailField(max_length=254,verbose_name="E-posta", blank=True)
    mobile = models.CharField(max_length=20,verbose_name="Cep Telefonu", blank=True)
    kayit = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Katılımcı'
        verbose_name_plural = 'Katılımcılar'

    def __str__(self):
        return self.username
    def get_name(self):
        if self.username:
            return self.username
        else:
            return self.name+" "+ self.lastname

class Pigeon(models.Model):
    user = models.ForeignKey(katilimci, verbose_name="Katılımcı", on_delete=models.CASCADE, related_name="fanchers")
    ulke= models.ForeignKey(ulkeler,verbose_name="Ülke",on_delete=models.CASCADE)
    yil = models.DateField(verbose_name="Yıl")
    kunye = models.CharField(max_length=30,verbose_name="Künye")
    ucret = models.IntegerField(verbose_name="Alıncan Ücret",default=0)
    kayit = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Kuş'
        verbose_name_plural = 'Kuşları'

    def __str__(self):
        return self.kunye
    def get_kuney(self):
        return self.ulke.kod
    def durum (self):
        if self.ucret:
            return "Aktif"
        else:
            return "Pasif"

tipler = (
    ('1', 'Yarış'),
    ('2', 'Antrenman'),
)

class yaris(models.Model):
    sezon = models.ForeignKey(sezon, verbose_name="sezon", on_delete=models.CASCADE)
    adi = models.CharField(max_length=120, verbose_name="Adı")
    tarih = models.DateTimeField(verbose_name="Salım Tarihi")
    mesafe = models.IntegerField(verbose_name="Mesafe")
    tip = models.CharField(max_length=2,choices=tipler, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True,verbose_name="Enlem")
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name="Boylam")
    sicaklik = models.IntegerField(verbose_name="Sıcaklık", null=True, blank=True)
    h_durum = models.CharField(max_length=50,verbose_name="Hava Durumu", null=True, blank=True)
    ruzgar = models.IntegerField(verbose_name="Rüzgar Hızı",null=True, blank=True)
    r_yon = models.CharField(max_length=50,verbose_name="Rüzgar Yönü",null=True, blank=True)
    nem = models.IntegerField(verbose_name="Nem Oranı",null=True, blank=True)
    slug = models.SlugField()
    kayit = models.DateTimeField(auto_now_add=True)
    guncelleme = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Yarış'
        verbose_name_plural = 'Yarışlar'

    def __str__(self):
       return self.adi+" "+self.sezon.title+""

class basket(models.Model):
    yaris = models.ForeignKey(yaris, on_delete=models.CASCADE)
    kus = models.ForeignKey(Pigeon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Giden'
        verbose_name_plural = 'Gidenler'

    def __str__(self):
        """Unicode representation of basket."""
        pass
class result(models.Model):
    yaris = models.ForeignKey(yaris,on_delete=models.CASCADE)
    kus = models.ForeignKey(Pigeon,on_delete=models.CASCADE)
    time = models.DateTimeField()
    sira = models.IntegerField()
    puan = models.IntegerField()
    class Meta:

        verbose_name = 'Sonuc'
        verbose_name_plural = 'Sonuçlar'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        pass

class oduller(models.Model):
    yaris = models.ForeignKey(yaris,verbose_name="Yarış",blank=True,on_delete=models.CASCADE,default=0,null=True)
    title = models.CharField(verbose_name="Başlık" ,max_length=120,blank=True)
    sira = models.IntegerField(verbose_name="Sıra")
    odul = models.CharField(verbose_name="Ödül",max_length=120)

    class Meta:
        verbose_name = 'oduller'
        verbose_name_plural = 'oduller'

    def __str__(self):
        return self.title

class kurallar(models.Model):
    kural = models.IntegerField()
    aciklama = models.TextField()
    class Meta:
        verbose_name = 'Kural'
        verbose_name_plural = 'Kurallar'

    def __str__(self):
        return str(self.kural)
def logos(instance,filename):
    filebase,extension = filename.split(".")
    if instance.id:
        return "sponsors/%s.%s" %(instance.id,extension)
    else:
        return "sponsors/" %(filename)
class sponsorlar(models.Model):
    sponsor = models.CharField(max_length=120,verbose_name="Sponsor")
    logo = models.ImageField(upload_to=logos)
    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsorlar'
    def __str__(self):
        return self.sponsor