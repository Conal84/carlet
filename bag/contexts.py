from django.shortcuts import get_object_or_404
from cars.models import Car


def bag_contents(request):

    grand_total = 0
    bag = request.session.get('bag', {})

    # Total the contents of the bag
    # for value in bag.values():
    #     if type(value) == int:
    #         grand_total += value

    if "car_id" in bag:
        id = bag["car_id"]
        car = get_object_or_404(Car, pk=id)
        make = car.make
        model = car.model
        car_cost_per_day = car.cost_per_day
        num_days = car.num_days
        car_total = car.car_total

        context = {
            'id': car.id,
            'make': make,
            'model': model,
            'car_cost_per_day': car_cost_per_day,
            'num_days': num_days,
            'car_total': car_total,
            'grand_total': car_total,
        }

        if "insurance_cost" in bag:
            id = bag["car_id"]
            car = get_object_or_404(Car, pk=id)
            insurance_per_day = car.insurance_per_day
            insurance_total = car.insurance_total
            grand_total = car.car_total + insurance_total
            context["insurance_per_day"] = insurance_per_day
            context["insurance_total"] = insurance_total
            context["grand_total"] = grand_total

            if "support_cost" in bag:
                id = bag["car_id"]
                car = get_object_or_404(Car, pk=id)
                support_per_day = car.support_per_day
                support_total = car.support_total
                grand_total = car.car_total + insurance_total + support_total
                context["support_per_day"] = support_per_day
                context["support_total"] = support_total
                context["grand_total"] = grand_total

    else:
        context = {}

    return context
