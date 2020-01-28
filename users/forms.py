from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email@example.org'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Unique username'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", 'first_name', 'last_name']
