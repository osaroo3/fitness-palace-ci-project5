from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe

from .models import Plan
from sub_checkout.forms import OrderForm
# Create your views here.
def view_sub_checkout(request, p_id):
    """ A view that renders the subcription checkout page """
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    plan = get_object_or_404(Plan, pk=p_id)
    total = plan.price
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')    

    context = {
        'plan': plan,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,        
    }
    return render(request, 'sub_checkout/sub_checkout.html', context)