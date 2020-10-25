from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    sex = models.CharField(max_length=6)
    address_line1 = models.CharField(max_length=20)
    address_line2 = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
