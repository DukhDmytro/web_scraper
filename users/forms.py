from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email@example.org'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=False)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Surname'}), required=False)
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Unique username'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", 'first_name', 'last_name']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Unique username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
