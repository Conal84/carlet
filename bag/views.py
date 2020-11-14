from django.shortcuts import render, get_object_or_404
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
        bag["car_id"] = item_id
        bag["car_cost"] = car.car_total
        request.session['bag'] = bag
    elif item == 'insurance':
        template = 'cars/car-support.html'
        bag["insurance_cost"] = car.insurance_total
        request.session['bag'] = bag
    elif item == 'support':
        template = 'checkout/checkout.html'
        bag["support_cost"] = car.support_total
        request.session['bag'] = bag

    return render(request, template, context)
