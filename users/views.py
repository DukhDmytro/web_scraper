from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from .models import User
from .forms import UserRegistrationForm, SignInForm


def verify(request, username):
    user = get_object_or_404(User, username=username)
    if user.is_active:
        return HttpResponseNotFound()
    user.is_active = True
    user.save()
    messages.add_message(request, messages.INFO, "You are registered")
    return redirect('users:sign_in')


def registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.INFO, "Please verify registration on your email")
                send_mail(
                    'Verify your account',
                    'Follow this link to verify your account: '
                    'http://localhost:8000%s' % reverse('users:verify', kwargs={'username': form.cleaned_data['username']}),
                    'from@me.dev',
                    [form.cleaned_data['email']],
                    fail_silently=False,
                )
                return redirect(reverse('users:sign_in'))
            except IntegrityError:
                messages.add_message(request, messages.INFO, "Email already registered")
    return render(request, 'registration.html', {'form': form})


def sign_in(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
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
