from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from cars.models import Car

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag """
    template = 'bag/bag.html'
    return render(request, template)


def add_to_bag(request, item_id):
    """ Add items to the bag """
    car = get_object_or_404(Car, pk=item_id)
    insurance = car.insurance
    support = car.support

    item = request.POST.get('item')
    bag = request.session.get('bag', {})

    if item == 'car':
        bag["car_id"] = item_id
        request.session['bag'] = bag
        return redirect(reverse("car_insurance", kwargs={"id": car.id}))

    elif item == 'insurance':
        bag["insurance"] = insurance
        request.session['bag'] = bag
        return redirect(reverse("car_support", kwargs={"id": car.id}))

    elif item == 'support':
        bag["support"] = support
        request.session['bag'] = bag
        return redirect(reverse("checkout"))


def remove_from_bag(request):
    """ Remove items from the bag """
    remove_type = request.POST['name']
    bag = request.session.get('bag')

    try:
        if remove_type == "del_car":
            bag = {}
        elif remove_type == "del_insurance":
            bag.pop("insurance")
        elif remove_type == "del_support":
            bag.pop("support")

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)
