from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from contact_us.forms import ContactForm

# Create your views here.


def contact_us(request):
    """ A view that renders the contact us page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your message was successfully received.\
                    We will get back to you')
            return redirect('contact_us')
        else:
            messages.error(
                request, 'Message delivery failed. \
                    Check the form and try again.')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact_us/contact_us.html', context)
