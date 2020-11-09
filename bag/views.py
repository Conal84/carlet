from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag """
    template = 'bag/bag.html'
    return render(request, template)


def add_to_bag(request, item_id):
    """ Add items to the bag """
    redirect_url = 'car_extra'

    bag = request.session.get('bag', {})

    bag[item_id] = 1

    request.session['bag'] = bag

    return redirect(reverse(redirect_url))
