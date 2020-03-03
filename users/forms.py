from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'email@example.org'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=False)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Surname'}), required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", 'first_name', 'last_name']


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@mail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
