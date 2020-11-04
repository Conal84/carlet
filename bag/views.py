from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag """

    template = 'bag/bag.html'
    return render(request, template)


def add_to_bag(request, item_id):
    """ Add items to the bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    return redirect(redirect_url)
