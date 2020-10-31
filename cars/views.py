from django.shortcuts import render, get_object_or_404
from .models import Car

# Create your views here.


def cars_all(request):
    """ A view to return the search page """
    location = None

    template = 'cars/cars-all.html'

    # cars = Car.objects.all()

    if request.GET:
        location = request.GET['location']
        cars = Car.objects.filter(location__icontains=location)

    context = {
        "cars": cars,
    }
    return render(request, template, context)
