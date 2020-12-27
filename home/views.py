from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    template = 'home/index.html'

    return render(request, template)


def how_it_works(request):
    """ A view to return the how it works page """

    template = "home/how-it-works.html"

    return render(request, template)
