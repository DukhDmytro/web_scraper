from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.sign_in, name='sign_in')
]
