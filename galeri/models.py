import uuid
import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('kumes', filename)

class galeri(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to =get_file_path)
    image_thumbnail = ImageSpecField(source='image',
                                 processors=[ResizeToFill(400, 200)],
                                 format='JPEG',
                                 options={'quality': 60})

    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = 'Galeri'

    def __str__(self):
        return '%s' % self.title
