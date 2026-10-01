from django.db import models

# Create your models here.
class Student(models.Model):
    si = models.IntegerField(primary_key=True)
    sn = models.CharField(max_length=20)
    sp = models.CharField(max_length=10)
    se = models.CharField()
def __str__(self):
    return self.sn