from django.db import models

class Data(models.Model):
    token = models.CharField(max_length=50)
    teamName = models.CharField(max_length=50)
    roomName = models.CharField(max_length=50)
    writerName = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=50)
    createdAt = models.CharField(max_length=50)


class Echo(models.Model):
    token = models.CharField(max_length=50)
    teamName = models.CharField(max_length=50)
    roomName = models.CharField(max_length=50)
    writerName = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=50)
    createdAt = models.CharField(max_length=50)