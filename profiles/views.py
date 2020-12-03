from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

# Create your views here.


def profile(request):
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
