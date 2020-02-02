from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, SignInForm


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
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.INFO, "You are logged in")
                return redirect(reverse('scraper:index'))
        messages.add_message(request, messages.INFO, "Invalid password or username")
    return render(request, 'login.html', {'form': form})


def logout_(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You are logged out")
    return redirect(reverse('scraper:index'))
