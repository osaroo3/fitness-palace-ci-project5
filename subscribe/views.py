from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .models import Plan
# Create your views here.

@login_required
def view_subscription_plan(request):
    """ A view that renders the subcription contents page """
    plans = Plan.objects.all()
    context = {
        'plans': plans,
    }
    return render(request, 'subscribe/subscribtion_plans.html', context)
