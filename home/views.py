from django.shortcuts import render
from .forms import SearchForm

# Create your views here.


def home_view(request):
    """ A view to return the index page """
    template = 'home/index.html'
    search_form = SearchForm()
    context = {
        'search_form': search_form,
    }
    return render(request, template, context)
