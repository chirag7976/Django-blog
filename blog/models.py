from distutils.command.upload import upload
from email.policy import default
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    img=models.ImageField(default='default.jpg',upload_to='media')

    def __str__(self):
        return self.title[0:25]
    