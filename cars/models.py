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
    num_days = models.IntegerField()
    cost_per_day = models.IntegerField()
    account = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # insurance_per_day = models.IntegerField(default=10)
    # support_per_day = models.IntegerField(default=5)

    def save(self, *args, **kwargs):
        tdelta = self.available_to - self.available_from
        self.num_days = tdelta.days
        super(Car, self).save(*args, **kwargs)

    @property
    def total(self):
        # tdelta = self.available_to - self.available_from
        return self.cost_per_day * self.num_days

    def __str__(self):
        return f"{self.make}, {self.model}"

    # @property
    # def num_days(self):
    #     tdelta = self.available_to - self.available_from
    #     return tdelta.days

    # @property
    # def insurance_total(self):
    #     tdelta = self.available_to - self.available_from
    #     return self.insurance_per_day * tdelta.days

    # @property
    # def support_total(self):
    #     tdelta = self.available_to - self.available_from
    #     return self.support_per_day * tdelta.days


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

    @property
    def total(self):
        # tdelta = self.available_to - self.available_from
        return self.cost_per_day * self.car.num_days

    def __str__(self):
        return f"Insurance for {self.car.make}, {self.car.model}"


class Support(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost_per_day = models.IntegerField(default=5)

    @property
    def total(self):
        # tdelta = self.available_to - self.available_from
        return self.cost_per_day * self.car.num_days

    def __str__(self):
        return f"Roadside assist for {self.car.make}, {self.car.model}"


class CarImage(models.Model):
    car_image = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_image.name

    def get_url(self):
        return self.car_image.url
