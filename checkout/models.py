import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from cars.models import Car

# Create your models here.


class Order(models.Model):
    """ Handle all orders across the site """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=32, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=True)
    county = models.CharField(max_length=80, null=False, blank=True)
    date = models.DateField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def generate_order_number(self):
        """ Generate random unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total every time a new line item is added to the order
        """
        self.grand_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """ Override the save method to set the unique order number """
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ Handle individual order line items """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    description = models.CharField(max_length=40, null=False, blank=False, default="")
    cost_per_day = models.IntegerField(null=False, blank=False, default=0)
    days = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def __str__(self):
        return f'{self.description} order num: {self.order.order_number}'
