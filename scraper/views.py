from django.shortcuts import render, redirect, reverse
from .models import Vacancies
from .pagination import make_pagination
import spiders


def index(request):
    try:
        msg = request.session.pop('msg')
    except KeyError:
        msg = ''
    vacancies = Vacancies.objects.order_by('id').all()
    page, last_page = make_pagination(request, vacancies)
    return render(request, 'index.html', {'vacancies': page, 'msg': msg, 'last_page': last_page})


def start_crawler(request):
    """
    Delete all items from vacancies table. Start scraping
    :param request:
    :return:
    """
    Vacancies.objects.all().delete()
    spiders.start_spiders()
    request.session['msg'] = request.POST.get('msg')
    return redirect(reverse('scraper:index'))

