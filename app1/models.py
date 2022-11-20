from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    detail = models.TextField(blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)


