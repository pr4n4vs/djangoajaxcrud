from operator import mod
from django.db import models

# Create your models here.
# class Class_name(models.Model):

class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    