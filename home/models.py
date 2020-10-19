from django.db import models

# Create your models here.


class Cars(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    cost_per_day = models.DecimalField()
    available = models.BooleanField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)