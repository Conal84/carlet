from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=40, default='')
    street_address1 = models.CharField(max_length=80, default='')
    street_address2 = models.CharField(max_length=80, default='')
    city = models.CharField(max_length=40, default='')
    county = models.CharField(max_length=80, blank=True, default='')
    postcode = models.CharField(max_length=20, blank=True, default='')
    contact_phone_number = models.CharField(max_length=20, default='')
    available_from = models.DateField(default=date.today)
    available_to = models.DateField(default=date.today)
    available = models.BooleanField(default=True)
    cost_per_day = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.make}, {self.model}"

    @property
    def insurance(self):
        "Returns the insurance cost per day for this Car"
        return self.cost_per_day / 10

    @property
    def support(self):
        "Returns the support cost per day for this Car"
        return 5


class Booking(models.Model):
    car = models.ForeignKey(
                            Car,
                            on_delete=models.SET_NULL,
                            null=True, blank=False,
                            related_name='bookings'
                            )
    user = models.ForeignKey(
                             User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=False,
                             )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking for: {self.car}"
