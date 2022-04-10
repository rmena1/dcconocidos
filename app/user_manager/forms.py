from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile

class createUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length=50)

    class meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone_number']
        labels = {
                "address": _("Street Address"),
                "phone_number": _("Phone Number"),
                }
                