import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Users

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'dateOfBirth', 'profilePicture']
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
        }
