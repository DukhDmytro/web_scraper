import json
from django.db import models
from django.core.paginator import Paginator


class WebSites(models.Model):
    jobs_web_site = models.URLField(max_length=300)

    def __str__(self):
        return self.jobs_web_site


class Vacancies(models.Model):
    title = models.CharField(max_length=300, null=True)
    url = models.URLField(max_length=200, null=True)
    description = models.CharField(max_length=25000, null=True)
    company_web_site = models.URLField(max_length=200, null=True)
    job_info = models.CharField(max_length=500, null=True)
    jobs_web_site = models.ForeignKey(WebSites, on_delete=models.CASCADE, default='')


class Selectors(models.Model):
    jobs_web_site = models.ForeignKey(WebSites, on_delete=models.CASCADE, default='')
    vacancy_link = models.CharField(max_length=150)
    next_page = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    company_web_site = models.CharField(max_length=150)
    job_info = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)

    def __str__(self):
        return f'Selectors for {self.jobs_web_site}'


class MyPaginator(Paginator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def my_get_page(self, *args, **kwargs):
        page = super().get_page(*args, **kwargs)
        for vacancy in page:
            vacancy.description = json.loads(vacancy.description)
        return page


