from django.shortcuts import get_object_or_404
from cars.models import Car, Insurance, Support


def bag_contents(request):

    grand_total = 0
    bag = request.session.get('bag', {})

    if "car_id" in bag:
        car_id = bag["car_id"]
        car = get_object_or_404(Car, pk=car_id)
        grand_total = car.car_total

        context = {
            "car_id": car.id,
            "make": car.make,
            "model": car.model,
            "num_days": car.num_days,
            "car_cost_per_day": car.cost_per_day,
            "car_total": car.car_total,
            "grand_total": grand_total,
        }

        if "insurance_id" in bag:
            insurance_id = bag["insurance_id"]
            insurance = get_object_or_404(Insurance, pk=insurance_id)
            grand_total = grand_total + insurance.total

            context["insurance_id"] = insurance.id
            context["insurance_cost_per_day"] = insurance.cost_per_day
            context["insurance_total"] = insurance.total
            context["grand_total"] = grand_total

        if "support_id" in bag:
            support_id = bag["support_id"]
            support = get_object_or_404(Support, pk=support_id)
            grand_total = grand_total + support.total

            context["support_id"] = support.id
            context["support_cost_per_day"] = support.cost_per_day
            context["support_total"] = support.total
            context["grand_total"] = grand_total

    else:
        context = {}

    return context
