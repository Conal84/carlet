from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages

from .models import Car, CarImage, Insurance, Support
from .forms import CarForm, ImageForm
from .utils import calc_days

# Create your views here.


def cars_all(request):
    """ A view to return the search page with results for cars searched """
    location = None
    template = 'cars/cars-all.html'

    if request.GET:
        location = request.GET['location']
        search_from = request.GET['search_from']
        search_to = request.GET['search_to']

        calc_days(request, search_from, search_to)

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

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    car_total = car.cost_per_day * num_days

    context = {
        "car": car,
        "car_total": car_total,
        "images": images,
    }
    return render(request, template, context)


def car_insurance(request, id):
    """ A view to return individual car insurance page"""
    template = 'cars/car-insurance.html'
    car = get_object_or_404(Car, pk=id)
    insurance = get_object_or_404(Insurance, car__pk=id)

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    insurance_total = insurance.cost_per_day * num_days

    context = {
        "car": car,
        "insurance": insurance,
        "insurance_total": insurance_total,
    }

    return render(request, template, context)


def car_insurance_skip(request, car_id):
    """ A view to return individual car insurance page"""
    template = 'cars/car-support.html'
    car = get_object_or_404(Support, pk=car_id)
    support = get_object_or_404(Support, car__pk=car_id)

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    support_total = support.cost_per_day * num_days

    context = {
        "car": car,
        "support": support,
        "support_total": support_total,
    }
    return render(request, template, context)


def car_support(request, id):
    """ A view to return individual car support page"""
    template = 'cars/car-support.html'
    car = get_object_or_404(Car, pk=id)
    support = get_object_or_404(Support, car__pk=id)

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    support_total = support.cost_per_day * num_days

    context = {
        "car": car,
        "support": support,
        "support_total": support_total,
    }
    return render(request, template, context)


def add_car(request):
    """Add a car to the database"""
    if request.method == 'POST':
        car_form = CarForm(request.POST)
        image_form = ImageForm(request.FILES)
        if car_form.is_valid() and image_form.is_valid():
            car_form.save()
            image_form.save()
            messages.success(request, 'Successfully added this car!')
            return redirect(reverse('add_car'))
        else:
            messages.error(request, 'Failed to add this car, Please check that the form is valid!')

    else:
        car_form = CarForm()
        image_form = ImageForm()

    template = 'cars/add-car.html'
    context = {
        'car_form': car_form,
        'image_form': image_form,
    }

    return render(request, template, context)
