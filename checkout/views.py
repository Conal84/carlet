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

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag in empty at the moment")
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
