from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # email = forms.EmailField()
    first_name = forms.CharField(max_length=75)
    last_name = forms.CharField(max_length=75)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
