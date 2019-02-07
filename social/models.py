from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    enrichment_data = models.CharField(max_length = 255)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=255)
    text = models.TextField()

    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'post',),)