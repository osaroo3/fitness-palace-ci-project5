from django import forms
from .models import Membership

class MembersForm(forms.ModelForm):
    """
     Form to update fellow members
    """
    class Meta:
        model = Membership
        fields = ('title', 'message',)