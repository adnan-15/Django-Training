from django.contrib import admin
from bdapp.models import client
from bdapp.models import customer
from bdapp.models import order
# Register your models here.
admin.site.register(client)
admin.site.register(customer)
admin.site.register(order)