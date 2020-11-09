from datetime import datetime, date, timedelta
from decimal import Decimal
from django.db import models
from profiles.models import UserProfile
import uuid

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    location = models.CharField(max_length=30, default='')
    available_from = models.DateField(default=date.today)
    available_to = models.DateField(default=date.today)
    num_days_on_hire = models.IntegerField()
    cost_per_day = models.DecimalField(max_digits=3, decimal_places=0)
    account = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    insurance_per_day = models.IntegerField(default=10)
    support_per_day = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.make}, {self.model}"

    # def save(self, *args, **kwargs):
    #     # tdelta = self.available_to - self.available_from
    #     tdelta = 5
    #     self.num_days_on_hire = tdelta
    #     return super(Car, self).save(*args, **kwargs)

    @property
    def insurance_total(self):
        tdelta = self.available_to - self.available_from
        return self.insurance_per_day * tdelta.days

    @property
    def support_total(self):
        tdelta = self.available_to - self.available_from
        return self.support_per_day * tdelta.days


# class Booking(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     hired_from = models.DateField(default=date.today)
#     hired_to = models.DateField(default=date.today)


#     def __str__(self):
#         return f"Booking no. {self.id}"


class CarImage(models.Model):
    car_image = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_image.name

    def get_url(self):
        return self.car_image.url
