from datetime import datetime, date
from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    cost_per_day = models.DecimalField(max_digits=3, decimal_places=0)
    location = models.CharField(max_length=30, default='')
    hire_from = models.DateField(default=date.today)
    hire_to = models.DateField(default=date.today)
    account = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make}, {self.model}"


class CarImage(models.Model):
    car_image = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_image.name

    def get_url(self):
        return self.car_image.url


class Available(models.Model):
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Available"

    def __str__(self):
        available_date = self.date.strftime("%d/%m/%Y")
        return f"{self.car.make}, {self.car.model} - available: {available_date}"
