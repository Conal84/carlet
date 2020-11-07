from datetime import datetime, date, timedelta
from decimal import Decimal
from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=30, default='')
    available_from = models.DateField(default=date.today)
    available_to = models.DateField(default=date.today)
    cost_per_day = models.DecimalField(max_digits=3, decimal_places=0)
    insurance = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    support = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    num_days = models.PositiveSmallIntegerField(default=1)
    account = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make}, {self.model}"

    # @property
    # def insurance(self):
    #     return self.cost_per_day * Decimal(0.0137) * self.num_days

    # @property
    # def support(self):
    #     return self.num_days * 6

    def save(self, *args, **kwargs):
        tdelta = self.hire_to - self.hire_from
        self.num_days = (tdelta).days
        self.insurance = self.cost_per_day * self.num_days * 0.05
        self.support = self.num_days * 6


class CarImage(models.Model):
    car_image = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_image.name

    def get_url(self):
        return self.car_image.url
