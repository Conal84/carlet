import sweetify

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Car
from .forms import CarForm
from .utils import calc_days, check_available
from profiles.models import UserProfile

from decimal import getcontext, Decimal
getcontext().prec = 3

# Create your views here.


def cars_all(request):
    """ A view to return the search page with results for cars searched """
    location = None
    template = 'cars/cars-all.html'
    search_dates = request.session.get('search_dates', {})

    if request.GET:
        location = request.GET['search-location']
        search_from = request.GET['search-from']
        search_to = request.GET['search-to']

        # Add search dates to the session
        search_dates["search_from"] = search_from
        search_dates["search_to"] = search_to
        request.session['search_dates'] = search_dates

        # Calc the days between search days
        calc_days(request, search_from, search_to)

        # cars = Car.objects.filter(
        #     location__icontains=location
        # ).filter(
        #     available_from__lte=search_from
        # ).filter(
        #     available_to__gte=search_to
        # )
        cars = Car.objects.filter(
            location__icontains=location
        )
        print(f"Cars by location are: {cars}")
        car_available_list = []
        for car in cars:
            if check_available(car, search_from, search_to):
                car_available_list.append(car)

        print(f"Cars available are: {car_available_list}")

    context = {
        "cars": car_available_list,
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
        "num_days": num_days,
        "images": images,
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def car_insurance(request, id):
    """ A view to return individual car insurance page"""
    template = 'cars/car-insurance.html'
    car = get_object_or_404(Car, pk=id)
    insurance = Decimal(car.insurance)

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    insurance_total = Decimal(insurance * num_days)

    context = {
        "car": car,
        "insurance": insurance,
        "num_days": num_days,
        "insurance_total": insurance_total,
    }

    return render(request, template, context)


def car_insurance_skip(request, car_id):
    """ A view to return individual car insurance page"""
    template = 'cars/car-support.html'
    car = get_object_or_404(Car, pk=car_id)
    support = Decimal(car.support)

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    support_total = Decimal(support * num_days)

    context = {
        "car": car,
        "support": support,
        "num_days": num_days,
        "support_total": support_total,
    }
    return render(request, template, context)


def car_support(request, id):
    """ A view to return individual car support page"""
    template = 'cars/car-support.html'
    car = get_object_or_404(Car, pk=id)
    support = Decimal(car.support)

    bag = request.session.get('bag')
    num_days = bag["num_days"]
    support_total = Decimal(support * num_days)

    context = {
        "car": car,
        "support": support,
        "num_days": num_days,
        "support_total": support_total,
    }
    return render(request, template, context)


@login_required(login_url='/login/')
def car_dashboard(request):
    template = 'cars/car-dashboard.html'

    return render(request, template)


@login_required(login_url='/login/')
def add_car(request):
    """Add a car to the database"""
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            sweetify.success(request, title='Success!',
                             icon='success',
                             text='Car successfully added',
                             timer=4000)
            return redirect(reverse('add_car'))
        else:
            sweetify.error(request, title='Error!',
                           icon='error',
                           text='Failed to add this car, please try again',
                           timer=4000)
    else:
        form = CarForm()

    template = 'cars/add-car.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required(login_url='/login/')
def display_cars(request):
    """Display a users cars in the database for editing"""
    user = request.user
    cars = Car.objects.filter(user=user)

    template = 'cars/display-cars.html'
    context = {
        'cars': cars,
    }

    return render(request, template, context)


@login_required(login_url='/login/')
def edit_car(request, car_id):
    """Edit an individual car details"""
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            sweetify.success(request, title='Success!',
                             icon='success',
                             text='Car successfully edited',
                             timer=4000)
            return redirect(reverse('display_cars'))
        else:
            sweetify.error(request, title='Error!', icon='error',
                           text='Failed to edit this car, please try again',
                           timer=4000)
    else:
        form = CarForm(instance=car)

    template = 'cars/edit-car.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required(login_url='/login/')
def delete_car(request, car_id):
    """Delete an individual car from the database"""
    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    sweetify.success(request, title='Success!', icon='success',
                     text='Car successfully deleted', timer=4000)

    return redirect(reverse('display_cars'))


def car_bookings(request):
    """A view to show all bookings for a particular car owner"""
    user = request.user
    cars = Car.objects.filter(user=user)
    bookings = cars.bookings.all()

    template = 'cars/car-bookings.html'
    context = {
        'bookings': bookings,
    }

    return render(request, template, context)
