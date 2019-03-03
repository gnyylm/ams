import uuid
import os
from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import shutil

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


@receiver(models.signals.pre_delete, sender=galeri)
def auto_delet_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    if instance.image_thumbnail:
        if os.path.isfile(instance.image_thumbnail.path):
            shutil.rmtree(os.path.dirname(instance.image_thumbnail.path))