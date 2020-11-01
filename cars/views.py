from django.shortcuts import render, get_object_or_404
from .models import Car, Available

# Create your views here.


def cars_all(request):
    """ A view to return the search page """
    location = None
    template = 'cars/cars-all.html'

    if request.GET:
        location = request.GET['location']
        hire_from = request.GET['hire_from']
        hire_to = request.GET['hire_to']

        # cars = Car.objects.filter(
        #     location__icontains=location
        #     ).filter(
        #         available__date__range=[hire_from, hire_to]
        #         ).distinct()

        cars = Car.objects.filter(
            location__icontains=location
            ).filter(
                hire_from=hire_from
                ).filter(
                    hire_to=hire_to
                    )

    context = {
        "cars": cars,
    }

    return render(request, template, context)
