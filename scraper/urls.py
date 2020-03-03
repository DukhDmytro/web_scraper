from django.urls import path
from . import views

app_name = 'scraper'

urlpatterns = [
    path('', views.index, name='index'),
    path('start_crawler/', views.start_crawler, name='start_crawler'),
]
