from datetime import datetime


def calc_days(request, day1, day2):
    date1 = datetime.strptime(day1, '%Y-%m-%d')
    date2 = datetime.strptime(day2, '%Y-%m-%d')
    dt = date2 - date1

    num_days = dt.days
    print(num_days)

    days = request.session.get('days', {})

    days["num_days"] = num_days
    request.session['days'] = days
