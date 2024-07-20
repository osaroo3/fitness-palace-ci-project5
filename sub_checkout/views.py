from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from .models import Plan
from sub_checkout.forms import OrderForm
from profiles.models import UserProfile
from sub_checkout.models import Order
# Create your views here.

@require_POST
def cache_sub_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)




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

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            form.stripe_pid = pid
            form.user = request.user
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your subscription was successfull.')
            return redirect('home')  

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


def view_my_plan(request):
    """
    This view renders all the plans subscribed
    by a logged in user
    """
    if request.user.is_authenticated:
        plans = Order.objects.filter(user=request.user)
        return render(
            request,
            'sub_checkout/my_plans.html',
            {'plans': plans}
        )