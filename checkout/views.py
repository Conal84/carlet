from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view to render the checkout form """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag in empty at the moment")
        return redirect(reverse('all cars'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HqFfvAc2MU4pe32X0icUyCYG9NE7oUfAdKRM1e5TZxk5m2TceFl0XEVrOKnzkCdXY4F8ts3Prh0XXl5rXX1oSBO00KgjmaTxQ',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
