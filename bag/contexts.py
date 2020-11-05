from django.shortcuts import get_object_or_404
from cars.models import Car


def bag_contents(request):

    bag_items = []
    total = 0
    grand_total = 0
    bag = request.session.get('bag', {})
    print(bag.items())

    for item_id, quantity in bag.items():
        car = get_object_or_404(Car, pk=item_id)
        total = car.cost_per_day
        bag_items.append({
            'item_id': item_id,
            'car': car,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
    }

    return context
