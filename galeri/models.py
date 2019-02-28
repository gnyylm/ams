from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class galeri(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to ="kumes")
    image_thumbnail = ImageSpecField(source='image',
                                 processors=[ResizeToFill(400, 200)],
                                 format='JPEG',
                                 options={'quality': 60})

    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = 'Galeri'

    def __str__(self):
        return '%s' % self.title
