from django.db import models

# Create your models here.
class client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField()
    client_company = models.CharField()

    def __str__(self):
        return self.client_name

class customer(models.Model):
    c_id = models.IntegerField()
    c_name = models.CharField()
    c_mobile = models.CharField()

    def __str__(self):
        return self.c_name

class order(models.Model):
    o_id = models.IntegerField()
    o_no = models.CharField()
    o_price = models.CharField()
    def __str__(self):
        return self.o_no

    
