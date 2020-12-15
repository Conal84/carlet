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
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.make}, {self.model}"

    @property
    def insurance(self):
        "Returns the insurance cost per day for this Car"
        return self.cost_per_day / 10

    @property
    def support(self):
        "Returns the support cost per day for this Car"
        return Decimal(5)


# class Insurance(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     cost_per_day = models.IntegerField(default=10)

#     def __str__(self):
#         return f"Insurance for {self.car.make}, {self.car.model}"


# class Support(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     cost_per_day = models.IntegerField(default=5)

#     def __str__(self):
#         return f"Roadside assist for {self.car.make}, {self.car.model}"
