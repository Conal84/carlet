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
        'order_form': order_form
    }

    return render(request, template, context)
