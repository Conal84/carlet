from django.shortcuts import render
from .models import Car

# Create your views here.


def cars_all(request):
    """ A view to return the search page """
    template = 'cars/cars-all.html'

    cars = Car.objects.all()

    context = {
        "cars": cars,

    }
    return render(request, template, context)
