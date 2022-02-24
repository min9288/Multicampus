from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoContent(models.Model):
    info_title = models.CharField(max_length=30)
    info_content = models.TextField()
    info_published = models.DateTimeField()
    info_url = models.CharField(max_length=200)

    def __str__(self):
        return self.info_title

class VideoContent(models.Model):
    video_title = models.CharField(max_length=30)
    video_content = models.TextField()
    video_author = models.CharField(max_length=50)
    video_published = models.DateTimeField()

    def __str__(self):
        return '{} :: {}'.format(self.video_title, self.video_author)