from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag """

    template = 'bag/bag.html'
    context = {
        
    }
    return render(request, template, context)