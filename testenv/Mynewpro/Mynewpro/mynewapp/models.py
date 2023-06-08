from django.db import models

class Adminlog(models.Model):
    uname=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.EmailField()

class Userdata(models.Model):
    name = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
