from django.shortcuts import get_object_or_404
from cars.models import Car, Insurance, Support


def bag_contents(request):

    grand_total = 0
    bag = request.session.get('bag', {})

    if "car_id" in bag:
        car_id = bag["car_id"]
        car = get_object_or_404(Car, pk=car_id)
        car_total = bag["num_days"] * car.cost_per_day
        grand_total = car_total

        context = {
            "car_id": car.id,
            "bag_car": car,
            "num_days": bag["num_days"],
            "bag_car_total": car_total,
            "grand_total": grand_total,
        }

        if "insurance_id" in bag:
            insurance_id = bag["insurance_id"]
            insurance = get_object_or_404(Insurance, pk=insurance_id)
            insurance_total = bag["num_days"] * insurance.cost_per_day
            grand_total = grand_total + insurance_total

            context["insurance_id"] = insurance.id
            context["bag_insurance"] = insurance
            context["bag_insurance_total"] = insurance_total
            context["grand_total"] = grand_total

        if "support_id" in bag:
            support_id = bag["support_id"]
            support = get_object_or_404(Support, pk=support_id)
            support_total = bag["num_days"] * support.cost_per_day
            grand_total = grand_total + support_total

            context["support_id"] = support.id
            context["bag_support"] = support
            context["bag_support_total"] = support_total
            context["grand_total"] = grand_total

    else:
        context = {}

    return context
