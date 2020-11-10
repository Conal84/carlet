from django.shortcuts import render

# Create your views here.


def checkout(request):
    """ A view to render the shopping bag """
    template = 'checkout/checkout.html'
    return render(request, template)
