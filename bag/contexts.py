from django.shortcuts import get_object_or_404
from cars.models import Car


def bag_contents(request):

    # bag_items = []
    # total = 0
    grand_total = 0
    bag = request.session.get('bag', {})

    # for item_id, quantity in bag.items():
    #     car = get_object_or_404(Car, pk=item_id)
    #     total += car.cost_per_day
    #     bag_items.append({
    #         'item_id': item_id,
    #         'car': car,
    #     })

    # grand_total = total

    # Total the contents of the bag
    for value in bag.values():
        grand_total += value

    context = {
        'bag': bag,
        'grand_total': grand_total,
    }

    return context
