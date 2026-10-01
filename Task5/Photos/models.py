from dataclasses import field

from django.db import models

# Create your models here.
class employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField()
    phone = models.CharField()
    asal = models.FloatField()
