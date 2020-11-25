from django.shortcuts import render, get_object_or_404
from .models import Car, CarImage

# Create your views here.


def cars_all(request):
    """ A view to return the search page with results for cars searched """
    location = None
    template = 'cars/cars-all.html'

    if request.GET:
        location = request.GET['location']
        search_from = request.GET['search_from']
        search_to = request.GET['search_to']

        cars = Car.objects.filter(
            location__icontains=location
            ).filter(
                available_from__lte=search_from
                ).filter(
                    available_to__gte=search_to
                    )

    context = {
        "cars": cars,
    }

    return render(request, template, context)


def car_detail(request, car_id):
    """ A view to return individual car detail"""

    template = 'cars/car-detail.html'
    car = get_object_or_404(Car, pk=car_id)
    images = CarImage.objects.filter(car__pk=car_id)

    context = {
        "car": car,
        "images": images,
    }
    return render(request, template, context)


def car_insurance(request):
    """ A view to return individual car insurance page"""
    template = 'cars/car-insurance.html'
    return render(request, template)


def car_insurance_skip(request, car_id):
    """ A view to return individual car insurance page"""
    car = get_object_or_404(Car, pk=car_id)
    template = 'cars/car-support.html'
    context = {
        "car": car,
    }
    return render(request, template, context)


def car_support(request):
    """ A view to return individual car support page"""
    template = 'cars/car-support.html'
    return render(request, template)


def car_support_skip(request, car_id):
    """ A view to return individual car support page"""
    car = get_object_or_404(Car, pk=car_id)
    template = 'checkout/checkout.html'
    context = {
        "car": car,
    }
    return render(request, template, context)
