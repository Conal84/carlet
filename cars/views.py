from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Car, Insurance, Support
from .forms import CarForm
from .utils import calc_days

from django.forms import inlineformset_factory

# Create your views here.


def cars_all(request):
    """ A view to return the search page with results for cars searched """
    location = None
    template = 'cars/cars-all.html'

    if request.GET:
        location = request.GET['search-location']
        search_from = request.GET['search-from']
        search_to = request.GET['search-to']

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

    images = {
        'image1': car.image1.url,
        'image2': car.image2.url,
        'image3': car.image3.url,
    }

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


@login_required
def car_dashboard(request):
    template = 'cars/car-dashboard.html'

    return render(request, template)


@login_required
def add_car(request):
    """Add a car to the database"""
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Successfully added this car!')
            return redirect(reverse('add_car'))
        else:
            messages.error(request, 'Failed to add this car, Please check that the form is valid!')
    else:
        form = CarForm()

    template = 'cars/add-car.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def display_cars(request):
    """Display a users cars in the database for editing"""
    user = request.user
    cars = Car.objects.filter(user=user)

    template = 'cars/display-cars.html'
    context = {
        'cars': cars,
    }

    return render(request, template, context)


@login_required
def edit_car(request, car_id):
    """Edit an individual car details"""
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Successfully added this car!')
            return redirect(reverse('display_cars'))
        else:
            messages.error(request, 'Failed to add this car, Please check that the form is valid!')
    else:
        form = CarForm(instance=car)

    template = 'cars/edit-car.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_car(request, car_id):
    """Delete an individual car from the database"""
    car = get_object_or_404(Car, pk=car_id)
    car.delete()

    return redirect(reverse('display_cars'))
