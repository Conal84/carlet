from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from cars.models import Car
from .forms import UserProfileForm

from checkout.models import Order

# Create your views here.


@login_required
def profile(request):
    """Display the users profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated succesfully')
        else:
            messages.error(request, 'Profile update failed, Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """A view to show individual historical orders"""
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def all_orders(request):
    """A view to show all orders for a particular user"""
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/all-orders.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)