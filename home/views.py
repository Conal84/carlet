from django.shortcuts import render
from .forms import SearchForm

# Create your views here.


def index(request):
    """ A view to return the index page """
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
    else:
        search_form = SearchForm()

    template = 'home/index.html'
    context = {
        'search_form': search_form,
    }
    return render(request, template, context)
