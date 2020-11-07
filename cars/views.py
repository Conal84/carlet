from django.shortcuts import render, get_object_or_404
from .models import Car, CarImage

# Create your views here.


def cars_all(request):
    """ A view to return the search page """
    location = None
    template = 'cars/cars-all.html'

    if request.GET:
        location = request.GET['location']
        search_from = request.GET['hire_from']
        search_to = request.GET['hire_to']

        cars = Car.objects.filter(
            location__icontains=location
            ).filter(
                hire_from__lte=search_from
                ).filter(
                    hire_to__gte=search_to
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
