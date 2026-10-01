from django.db import models

# Create your models here.
class Employee(models.Model):
    e_no = models.IntegerField()
    e_name = models.CharField(max_length=40)
    e_salary = models.FloatField()

    def __str__(self):
        return self.e_name