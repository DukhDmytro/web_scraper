from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db import IntegrityError
from .forms import UserRegistrationForm


def registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, "You are registered")
                return redirect(reverse('users:sign_in'))
            except IntegrityError:
                messages.add_message(request, messages.INFO, "Email already registered")
    return render(request, 'registration.html', {'form': form})


def sign_in(request):
    return render(request, 'login.html', {})
