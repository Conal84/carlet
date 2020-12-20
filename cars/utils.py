from datetime import datetime, date
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
    hire_start = datetime.strptime(hire_from, '%Y-%m-%d')
    hire_end = datetime.strptime(hire_to, '%Y-%m-%d')

    # Get all bookings for the car
    booking_list = Booking.objects.filter(car=car)
    print(f"Booking list is: {booking_list}")
    available_list = []

    # If there are no current bookings for this car
    if not booking_list:
        return True
    else:
        # Check each booking against hire dates
        for booking in booking_list:
            print(f"Hey, Im a booking: {booking}")
            print(f"Start date is: {booking.start_date}, End date is {booking.end_date}")
            if booking.start_date > hire_start.date() or booking.end_date < hire_end.date():
                available_list.append(True)
            return all(available_list)
