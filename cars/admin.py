from django.contrib import admin
from .models import Car, CarImage, Insurance, Support

# Register your models here.
admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(Insurance)
admin.site.register(Support)
