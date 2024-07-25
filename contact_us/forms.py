from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact Form to reach us
    """
    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'title', 'message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fullname': 'fullname',
            'email': 'email',
            'title': 'title',
            'message': 'message',
        }

        self.fields['fullname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
       