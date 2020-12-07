from datetime import date
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=30, default='')
    available_from = models.DateField(default=date.today)
    available_to = models.DateField(default=date.today)
    cost_per_day = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make}, {self.model}"


# class Booking(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     booked_from = models.DateField()
#     booked_to = models.DateField()
#     num_days = models.IntegerField()

#     def __str__(self):
#         return f"Booking no. {self.id}"


class Insurance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost_per_day = models.IntegerField(default=10)

    def __str__(self):
        return f"Insurance for {self.car.make}, {self.car.model}"


class Support(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost_per_day = models.IntegerField(default=5)

    def __str__(self):
        return f"Roadside assist for {self.car.make}, {self.car.model}"


class CarImage(models.Model):
    car_image = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_image.name

    def get_url(self):
        return self.car_image.url
