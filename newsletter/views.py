from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import NewsletterForm


# Create your views here.
def newsletter_subscription(request):
    """ A view that renders the newsletter subscription page """

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your subscription to our newsletters was successful')
            return redirect('home')
        else:
            messages.error(
                request, 'Subscription failed. \
                    Check the form and try again.')
    else:
        form = NewsletterForm()

    context = {
        'form': form
    }
    return render(request, 'newsletter/newsletter.html', context)
