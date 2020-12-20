from django.contrib import admin
from .models import Car, Booking

# Register your models here.
admin.site.register(Car, Booking)
