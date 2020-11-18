from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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


def remove_from_bag(request, item_id):
    """ Remove items from the bag """
    remove_type = request.POST['name']
    bag = request.session.get('bag')

    if remove_type == "del_car":
        bag.pop("car_id")
        bag.pop("car_cost")
    elif remove_type == "del_insurance":
        bag.pop("insurance_cost")
    elif remove_type == "del_support":
        bag.pop("support_cost")

    request.session['bag'] = bag
    return HttpResponse(status=200)
