from django import forms

from .models import Participant


class RegistrationForm(forms.Form):
    # will not have any effect on the database,
    # this is used to collect user's data
    email = forms.EmailField(label="Your Email")
