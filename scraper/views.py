import json
from django.shortcuts import render
from .models import Vacancies


def index(request):
    vacancies = Vacancies.objects.get_vacancies()

    return render(request, 'index.html', {'products': vacancies})

