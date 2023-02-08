from django.db import models
from datetime import datetime


class FileSys(models.Model):
    filename = models.CharField(max_length=64)
    uploader = models.CharField(max_length=20)
    file_size = models.IntegerField(max_length=4)
    first_upload_time = models.DateTimeField()
    last_upload_time = models.DateTimeField()


class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now())
