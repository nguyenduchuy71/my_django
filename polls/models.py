from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    post_created = models.DateTimeField(default=datetime.now, blank=True)
    post_modified = models.DateTimeField(default=datetime.now, blank=True)
    post_content = models.CharField(max_length=2000)
    post_comment_count = models.IntegerField(default=0)
    post_title = models.CharField(max_length=200)
    post_isdeleted = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_created = models.DateTimeField(default=datetime.now, blank=True)
    comment_modified = models.DateTimeField(default=datetime.now, blank=True)
    comment_content = models.CharField(max_length=200)
    comment_isdeleted = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True,  related_name='post')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False,  related_name='user')

