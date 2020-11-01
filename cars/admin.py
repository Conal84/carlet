from django.contrib import admin
from .models import Car, CarImage, Available

# Register your models here.
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(Available)
