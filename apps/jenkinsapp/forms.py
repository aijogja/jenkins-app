from django import forms
from django.core.validators import ValidationError
from .models import Member
# Create the form class.


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the name.'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the valid email address.'}),
        }