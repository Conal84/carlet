from django.shortcuts import render

# Create your views here.


def search(request):
    """ A view to return the search page """
    template = 'cars/search.html'
    context = {

    }
    return render(request, template, context)
