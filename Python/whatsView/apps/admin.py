from django.contrib import admin
from .models import InfoContent
from .models import VideoContent

# Register your models here.
admin.site.register(InfoContent)
admin.site.register(VideoContent)