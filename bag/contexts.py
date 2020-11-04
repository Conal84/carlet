from decimal import Decimal


def bag_contents(request):

    bag_items = []
    total = 0
    grand_total = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
    }

    return context
