from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_, name='logout'),
    path('verify/<str:username>', views.verify, name='verify'),
]
