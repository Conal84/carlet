from django.shortcuts import render, redirect, reverse, get_object_or_404
from cars.models import Car

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag """
    template = 'bag/bag.html'
    return render(request, template)


def add_to_bag(request, item_id):
    """ Add items to the bag """
    car = get_object_or_404(Car, pk=item_id)
    item = request.POST.get('item')
    bag = request.session.get('bag', {})

    context = {
        "car": car,
    }

    if item == 'car':
        template = 'cars/car-insurance.html'
        bag[item_id] = 1
        request.session['bag'] = bag
    elif item == 'insurance':
        template = 'cars/car-support.html'
        bag["insurance"] = 1
    elif item == 'support':
        template = 'checkout/checkout.html'
        bag["support"] = 1

    return render(request, template, context)
