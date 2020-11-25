from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from pathlib import os

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

from os import path
if path.exists("env.py"):
    import env

# Create your views here.


def checkout(request):
    """ A view to render the checkout form """
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    if request.method == "POST":
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['toen_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
    #     if order_form.is_valid():
    #         order_form.safe()
    #         for item_id,

    # else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty at the moment")
            return redirect(reverse('all cars'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total*100)
        
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, template, context)
