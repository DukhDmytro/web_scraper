from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import reverse
from scraper.models import Vacancies
import spiders


@shared_task
def send_email_task(username, email):
    """
    Send email to verify user registration
    :param username:
    :param email: email to send
    :return:
    """
    send_mail(
        'Verify your account',
        'Follow this link to verify your account: '
        'http://localhost:8000%s' % reverse('users:verify', kwargs={'username': username}),
        'from@me.dev',
        [email],
        fail_silently=False,
    )


@shared_task
def task_periodical_scraping():
    Vacancies.objects.all().delete()
    spiders.start_spiders()
