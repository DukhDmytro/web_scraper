import json
from django.shortcuts import render
from .models import Vacancies, MyPaginator
from django.core.paginator import Paginator


def index(request):
    vacancies = Vacancies.objects.order_by('id').all()
    p = MyPaginator(vacancies, 5)
    pa = p.my_get_page(1)
    return render(request, 'index.html', {'vacancies': pa})

