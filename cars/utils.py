from datetime import datetime
from .models import Booking


def calc_days(request, day1, day2):
    """A function to calculate number of days between two dates"""
    date1 = datetime.strptime(day1, '%Y-%m-%d')
    date2 = datetime.strptime(day2, '%Y-%m-%d')
    dt = date2 - date1

    num_days = dt.days
    bag = request.session.get('bag', {})

    bag["num_days"] = num_days
    request.session['bag'] = bag


def check_available(car, hire_from, hire_to):
    """
    A function to check car availability between given dates
    check all bookings for the car
    """
    # Get all bookings for the car
    booking_list = Booking.objects.filter(car=car)
    available_list = []
    # Check each booking against hire dates
    for booking in booking_list:
        if booking.start_date > hire_to or booking.end_date < hire_from:
            available_list.append(True)
        return all(available_list)
