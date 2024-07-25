from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Membership


from .forms import MembersForm
# Create your views here.


@login_required
def members_info(request):
    """ A view to show members list and update on their success """

    members = Membership.objects.all()
    if request.method == "POST":
        members_form = MembersForm(request.POST)
        if members_form.is_valid():
            members_form = members_form.save(commit=False)
            members_form.user = request.user
            members_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'message delivered'
            )
    members_form = MembersForm()

    context = {
        'members': members,
        'members_form': members_form,
    }

    return render(request, 'members/members.html', context)
