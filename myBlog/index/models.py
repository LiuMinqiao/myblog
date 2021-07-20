from django.db import models

# Create your models here.

class logindata(models.Model):
    email = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)

class user(models.Model):
    name =models.CharField(max_length=100)
    email = models.CharField(max_length=200,default="")
    age =models.IntegerField()

