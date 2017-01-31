from django.db import models
from django.utils import timezone
import os 

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Photo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    photoItem = models.TextField()
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title