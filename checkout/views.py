import stripe
import json
import sweetify

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from pathlib import os
from datetime import datetime

from .forms import OrderForm
from .models import Order, OrderLineItem
from bag.contexts import bag_contents
from cars.models import Car, Booking
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from os import path
if path.exists("env.py"):
    import env

# Create your views here.


@require_POST
def cache_checkout_data(request):
    """
    A view to cache the checkout data and
    update the stripe payment intent
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
        bag = request.session.get('bag')
        current_bag = bag_contents(request)
        days = current_bag['num_days']
        bag_car_total = current_bag['bag_car_total']
        if 'bag_insurance_total' in current_bag.keys():
            bag_insurance_total = current_bag['bag_insurance_total']
        else:
            bag_insurance_total = 0
        if 'bag_support_total' in current_bag.keys():
            bag_support_total = current_bag['bag_support_total']
        else:
            bag_support_total = 0
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(bag),
            'days': days,
            'bag_car_total': bag_car_total,
            'bag_insurance_total': bag_insurance_total,
            'bag_support_total': bag_support_total,
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        sweetify.error(request, title='Error!',
                       icon='error',
                       text='Sorry, your payment cannot be \
                             processed right now. Please try again later.',
                       timer=4000)
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ A view to render the checkout form """
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    if request.method == "POST":

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        current_bag = bag_contents(request)
        car = current_bag["bag_car"]
        search_dates = request.session.get('search_dates')
        start_string = search_dates["search_from"]
        end_string = search_dates["search_to"]
        start_date = datetime.strptime(start_string, '%Y-%m-%d')
        end_date = datetime.strptime(end_string, '%Y-%m-%d')

        # Create the related order in the database
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            if "bag_car" in current_bag:
                desc = car.make + " " + car.model
                order_line_item = OrderLineItem(
                    order=order,
                    description=desc,
                    cost_per_day=car.cost_per_day,
                    days=current_bag["num_days"],
                    lineitem_total=current_bag["bag_car_total"]
                )
                order_line_item.save()
            if "bag_insurance" in current_bag:
                insurance = car.insurance
                order_line_item = OrderLineItem(
                    order=order,
                    description="Car insurance",
                    cost_per_day=insurance,
                    days=current_bag["num_days"],
                    lineitem_total=current_bag["bag_insurance_total"]
                )
                order_line_item.save()
            if "bag_support" in current_bag:
                support = car.support
                order_line_item = OrderLineItem(
                    order=order,
                    description="Car roadside assistance",
                    cost_per_day=support,
                    days=current_bag["num_days"],
                    lineitem_total=current_bag["bag_support_total"]
                )
                order_line_item.save()

            request.session['save_info'] = 'save-info' in request.POST

            # Create the related Booking in the database
            booking = Booking(car=car,
                              user=request.user,
                              start_date=start_date,
                              end_date=end_date)
            booking.save()
            return redirect(reverse(
                'checkout_success',
                args=[order.order_number, car.id]
            ))
        else:
            sweetify.error(request, title='Error!',
                           icon='error',
                           text='There was an error with your form. \
                                 Please double check your information.',
                           timer=4000)

    elif request.method == "GET":
        bag = request.session.get('bag', {})
        if not bag:
            return redirect(reverse('all_cars'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total*100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with user profile info
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number, car_id):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    car = get_object_or_404(Car, pk=car_id)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    sweetify.success(request, title='Success!',
                     icon='success',
                     text=f'Your Order has been processed and a confirmation     email has been sent to {order.email}',
                     timer=4000)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
        'car': car,
    }

    return render(request, template, context)
