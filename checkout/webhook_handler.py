from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime

from .models import Order, OrderLineItem
from cars.models import Car
from cars.models import Booking
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send a confirmation email to a customer"""
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """Handle a webhook event"""

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent succeeded webhook from Stripe"""

        intent = event.data.object
        search_dates = self.request.session.get('search_dates')
        start_string = search_dates["search_from"]
        end_string = search_dates["search_to"]
        start_date = datetime.strptime(start_string, '%Y-%m-%d')
        end_date = datetime.strptime(end_string, '%Y-%m-%d')

        # Get the payment intent data
        pid = intent.id
        bag = intent.metadata.bag
        days = intent.metadata.days
        bag_car_total = intent.metadata.bag_car_total
        bag_insurance_total = intent.metadata.bag_insurance_total
        bag_support_total = intent.metadata.bag_support_total
        shipping_details = intent.shipping
        save_info = intent.metadata.save_info

        id = bag['car_id']
        car = get_object_or_404(Car, pk=id)

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean billing address details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # Check if order already exists in the database
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    town_or_city=billing_details.address.city,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    county=billing_details.address.state,
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    town_or_city=billing_details.address.city,
                    county=billing_details.address.state,
                    postcode=billing_details.address.postal_code,
                    country=billing_details.address.country,
                    stripe_pid=pid,
                    car=car,
                )
                bag = json.loads(bag)
                if "car_id" in bag:
                    # id = bag['car_id']
                    # car = get_object_or_404(Car, pk=id)
                    desc = car.make + " " + car.model
                    order_line_item = OrderLineItem(
                        order=order,
                        description=desc,
                        cost_per_day=car.cost_per_day,
                        days=days,
                        lineitem_total=bag_car_total
                    )
                    order_line_item.save()
                if "insurance" in bag:
                    # id = bag['car_id']
                    # car = get_object_or_404(Car, pk=id)
                    insurance = car.insurance
                    order_line_item = OrderLineItem(
                        order=order,
                        description="Car insurance",
                        cost_per_day=insurance,
                        days=days,
                        lineitem_total=bag_insurance_total
                    )
                    order_line_item.save()
                if "support_id" in bag:
                    # id = bag['car_id']
                    # car = get_object_or_404(Car, pk=id)
                    support = car.support
                    order_line_item = OrderLineItem(
                        order=order,
                        description="Car roadside assistance",
                        cost_per_day=support,
                        days=days,
                        lineitem_total=bag_support_total
                    )
                    order_line_item.save()

                    # Create the related Booking in the database
                    booking = Booking(
                        car=car,
                        user=self.request.user,
                        start_date=start_date,
                        end_date=end_date)
                    booking.save()
            except Exception as e:
                if order:
                    order.delete()
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook!!',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.failed webhook from Stripe"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
