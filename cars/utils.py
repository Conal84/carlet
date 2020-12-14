from datetime import datetime
from checkout.models import Booking
from bag.contexts import bag_contents


def calc_days(request, day1, day2):
    """A function to calculate number of days between two dates"""
    date1 = datetime.strptime(day1, '%Y-%m-%d')
    date2 = datetime.strptime(day2, '%Y-%m-%d')
    dt = date2 - date1

    num_days = dt.days
    bag = request.session.get('bag', {})

    current_bag = bag_contents(request)
    current_bag["start_date"] = date1
    current_bag["end_date"] = date2
    bag["num_days"] = num_days
    request.session['bag'] = bag


def check_available(request, car, hire_from, hire_to):
    """A function to check if a car is available"""

    booking_list = Booking.objects.filter(car=car)
    available_list = []

    for booking in booking_list:
        if booking.start_date > hire_to or booking.end_date < hire_from:
            available_list.append(True)

    return all(available_list)
