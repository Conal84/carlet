from django.shortcuts import render
from .models import Car, CarImage

# Create your views here.


def search(request):
    """ A view to return the search page """
    template = 'cars/search.html'

    cars = Car.objects.all()

    context = {
        "cars": cars,

    }
    return render(request, template, context)
