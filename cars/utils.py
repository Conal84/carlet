from datetime import datetime


def calc_days(request, day1, day2):
    """A function to calculate number of days between two dates"""
    date1 = datetime.strptime(day1, '%Y-%m-%d')
    date2 = datetime.strptime(day2, '%Y-%m-%d')
    dt = date2 - date1

    num_days = dt.days
    bag = request.session.get('bag', {})

    bag["num_days"] = num_days
    request.session['bag'] = bag
