from ast import Add
from django.contrib import admin
from .models import Customer, Address

admin.site.register(Customer)
admin.site.register(Address)
