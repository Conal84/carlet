from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    cost_per_day = models.DecimalField(decimal_places=2)
    available = models.BooleanField()
    account = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class CarImage(models.Model):
    car_image = models.ImageField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
