from django.db import models
from django.utils import timezone


# Create your models here.
class Post( models.Model):
    # 작성자
    author = models.ForeignKey ('auth.User', on_delete = models.CASCADE)
    # 제목
    title = models.CharField (max_length = 200)
    # 내용
    text = models.TextField()
    # 작성일
    created_date = models.DateTimeField ( default=timezone.now)
    # 게시일
    published_date = models.DateTimeField (blank=True , null=True)

