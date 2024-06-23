from django.shortcuts import render, redirect, reverse, get_object_or_404


from .models import Plan
# Create your views here.
def view_sub_checkout(request, p_id):
    """ A view that renders the subcription checkout page """
    
    plan = get_object_or_404(Plan, pk=p_id)
    print(plan)
    context = {
        'plan': plan,
    }
    return render(request, 'sub_checkout/sub_checkout.html', context)