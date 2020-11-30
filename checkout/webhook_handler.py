from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a webhook event"""

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean billing address details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        order = Order.objects.get(
            full_name__iexact=billing_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=billing_details.phone,
            street_address1__iexact=billing_details.address.line1,
            street_address2__iexact=billing_details.address.line2,
            town_or_city=billing_details.address.city,
            county=billing_details.address.county,
            postcode=billing_details.address.postal_code,
            country=billing_details.address.country,
            grand_total=grand_total,
        )
        order_exists = True

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.failed webhook from Stripe"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)