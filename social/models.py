from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Post(models.Model):
    title = models.TextField(unique=True)
    added = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):

        return "{} - {} - {} - {} - {}".format(self.title, self.added, self.content, self.likes, self.dislikes)